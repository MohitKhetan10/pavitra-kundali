"""
Pavitra Kundali — Jyotish engine (v2, expanded).
Sidereal / Lahiri (Chitrapaksha). Swiss Ephemeris, Moshier mode (no data files).
Features: D1 + D9(Navamsa), dignity, drishti(aspects), Mangal dosha, Sade Sati,
nakshatra detail, core yogas, multi-level Vimshottari dasha.
"""
import swisseph as swe
from datetime import datetime, timedelta
from nakshatra_data import NAK_DETAIL

swe.set_sid_mode(swe.SIDM_LAHIRI)
_FLG = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_MOSEPH | swe.FLG_SPEED

SIGNS = ["Mesha","Vrishabha","Mithuna","Karka","Simha","Kanya",
         "Tula","Vrischika","Dhanu","Makara","Kumbha","Meena"]
SIGNS_EN = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo",
            "Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
SIGN_LORD = ["Mars","Venus","Mercury","Moon","Sun","Mercury",
             "Venus","Mars","Jupiter","Saturn","Saturn","Jupiter"]
ELEMENT = ["Fire","Earth","Air","Water"]*3

NAK = ["Ashwini","Bharani","Krittika","Rohini","Mrigashira","Ardra","Punarvasu",
       "Pushya","Ashlesha","Magha","Purva Phalguni","Uttara Phalguni","Hasta",
       "Chitra","Swati","Vishakha","Anuradha","Jyeshtha","Mula","Purva Ashadha",
       "Uttara Ashadha","Shravana","Dhanishta","Shatabhisha","Purva Bhadrapada",
       "Uttara Bhadrapada","Revati"]
DASHA_LORDS = ["Ketu","Venus","Sun","Moon","Mars","Rahu","Jupiter","Saturn","Mercury"]
DASHA_YEARS = {"Ketu":7,"Venus":20,"Sun":6,"Moon":10,"Mars":7,
               "Rahu":18,"Jupiter":16,"Saturn":19,"Mercury":17}
NAK_LORD = [DASHA_LORDS[i % 9] for i in range(27)]

PLANETS = [("Sun",swe.SUN),("Moon",swe.MOON),("Mars",swe.MARS),("Mercury",swe.MERCURY),
           ("Jupiter",swe.JUPITER),("Venus",swe.VENUS),("Saturn",swe.SATURN),
           ("Rahu",swe.MEAN_NODE)]

# Dignity tables (by sign index 0..11)
EXALT = {"Sun":0,"Moon":1,"Mars":9,"Mercury":5,"Jupiter":3,"Venus":11,"Saturn":6}   # sign of exaltation
DEBIL = {k:(v+6)%12 for k,v in EXALT.items()}
OWN   = {"Sun":[4],"Moon":[3],"Mars":[0,7],"Mercury":[2,5],"Jupiter":[8,11],"Venus":[1,6],"Saturn":[9,10]}
FRIEND = {  # classical natural friends
 "Sun":["Moon","Mars","Jupiter"],"Moon":["Sun","Mercury"],
 "Mars":["Sun","Moon","Jupiter"],"Mercury":["Sun","Venus"],
 "Jupiter":["Sun","Moon","Mars"],"Venus":["Mercury","Saturn"],
 "Saturn":["Mercury","Venus"]}
ENEMY = {
 "Sun":["Venus","Saturn"],"Moon":[],
 "Mars":["Mercury"],"Mercury":["Moon"],
 "Jupiter":["Mercury","Venus"],"Venus":["Sun","Moon"],
 "Saturn":["Sun","Moon","Mars"]}
# special aspects (houses counted from planet, 1=same)
SPECIAL_ASPECT = {"Mars":[4,7,8],"Jupiter":[5,7,9],"Saturn":[3,7,10]}

def _dms(deg):
    d=int(deg); m=int((deg-d)*60); s=int(round(((deg-d)*60-m)*60))
    if s==60: s=0; m+=1
    if m==60: m=0; d+=1
    return f"{d}\u00b0{m:02d}'{s:02d}\""

def _pos(lon):
    sign=int(lon//30); deg=lon%30
    n=int(lon//(13+1/3.0)); pada=int((lon%(13+1/3.0))//(3+1/3.0))+1
    return {"lon":round(lon,4),"rashi":SIGNS[sign],"rashi_en":SIGNS_EN[sign],
            "rashi_num":sign+1,"rashi_lord":SIGN_LORD[sign],"element":ELEMENT[sign],
            "degree":round(deg,4),"dms":_dms(deg),
            "nakshatra":NAK[n],"nak_num":n+1,"nak_lord":NAK_LORD[n],"pada":pada}

def navamsa_sign(lon):
    """D9 sign index 0..11."""
    sign=int(lon//30); pos_in=lon%30
    nav=int(pos_in//(30/9.0))          # 0..8
    # starting navamsa sign depends on element of the sign
    starts=[0,9,6,3]                    # movable/fixed... element cycle: Fire->Aries,Earth->Cap,Air->Libra,Water->Cancer
    start=starts[sign%4]
    return (start+nav)%12

def dignity(planet, sign):
    if planet in ("Rahu","Ketu"): return "-"
    if sign==EXALT.get(planet): return "Exalted"
    if sign==DEBIL.get(planet): return "Debilitated"
    if sign in OWN.get(planet,[]): return "Own sign"
    lord=SIGN_LORD[sign]
    if lord==planet: return "Own sign"
    if lord==planet: return "Own sign"
    if lord in FRIEND.get(planet,[]): return "Friendly"
    if lord in ENEMY.get(planet,[]): return "Enemy sign"
    return "Neutral"

def _to_jd(dob,tob,tz):
    y,mo,d=map(int,dob.split("-")); hh,mm=map(int,tob.split(":"))
    return swe.julday(y,mo,d,hh+mm/60.0-tz)


KARAKA_ROLES=["Atmakaraka","Amatyakaraka","Bhratrikaraka","Matrikaraka",
              "Pitrikaraka","Putrakaraka","Gnatikaraka","Darakaraka"]
def chara_karakas(planets):
    """Jaimini 8-planet Chara Karakas by degrees within sign (Rahu counted in reverse)."""
    items=[]
    for n in ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Rahu"]:
        d=planets[n]["degree"]
        if n=="Rahu": d=30-d
        items.append((n,d))
    items.sort(key=lambda x:-x[1])
    role_of={}; planet_of={}
    for i,(n,_) in enumerate(items):
        role_of[n]=KARAKA_ROLES[i]; planet_of[KARAKA_ROLES[i]]=n
    return {"role_of":role_of,"planet_of":planet_of,"atmakaraka":items[0][0]}

def compute_chart(dob,tob,lat,lon_geo,tz):
    jd=_to_jd(dob,tob,tz)
    planets={}
    for name,pid in PLANETS:
        res=swe.calc_ut(jd,pid,_FLG)[0]
        p=_pos(res[0]); p["speed"]=round(res[3],4)
        p["retro"]=bool(res[3]<0) and name not in ("Sun","Moon")
        p["dignity"]=dignity(name,p["rashi_num"]-1)
        p["navamsa"]=SIGNS[navamsa_sign(res[0])]
        planets[name]=p
    kl=(planets["Rahu"]["lon"]+180)%360
    k=_pos(kl); k["speed"]=planets["Rahu"]["speed"]; k["retro"]=True
    k["dignity"]="-"; k["navamsa"]=SIGNS[navamsa_sign(kl)]; planets["Ketu"]=k

    cusps,ascmc=swe.houses_ex(jd,lat,lon_geo,b'W',_FLG)
    asc=_pos(ascmc[0]); asc["navamsa"]=SIGNS[navamsa_sign(ascmc[0])]
    lagna=asc["rashi_num"]-1
    for p in planets.values():
        p["house"]=((p["rashi_num"]-1)-lagna)%12+1

    aspects=compute_aspects(planets,lagna)
    kar=chara_karakas(planets)
    tenth_sign=(lagna+9)%12; ninth_sign=(lagna+8)%12
    dharma={"tenth_sign":SIGNS[tenth_sign],"tenth_lord":SIGN_LORD[tenth_sign],
            "ninth_sign":SIGNS[ninth_sign],"ninth_lord":SIGN_LORD[ninth_sign]}
    return {
        "input":{"dob":dob,"tob":tob,"lat":lat,"lon":lon_geo,"tz":tz},
        "ayanamsa":round(swe.get_ayanamsa_ut(jd),4),
        "ascendant":asc,"lagna_lord":SIGN_LORD[lagna],
        "planets":planets,
        "moon_nakshatra":planets["Moon"]["nakshatra"],
        "aspects":aspects,
        "mangal_dosha":mangal_dosha(planets),
        "sade_sati":sade_sati(planets["Moon"]["rashi_num"]-1,jd),
        "yogas":detect_yogas(planets,lagna),
        "dasha":vimshottari(planets["Moon"]["lon"],dob,tob,tz),
        "nak_detail":NAK_DETAIL.get(planets["Moon"]["nakshatra"],{}),
        "karakas":kar,"atmakaraka":kar["atmakaraka"],"dharma":dharma,
    }

def compute_aspects(planets,lagna):
    """Return list of graha->house/planet aspects (drishti)."""
    out=[]
    for name,p in planets.items():
        if name=="Ketu": continue
        h=p["house"]
        casts=set([(h+6-1)%12+1])      # 7th aspect (all planets)
        for off in SPECIAL_ASPECT.get(name,[]):
            casts.add((h+off-1-1)%12+1)
        out.append({"planet":name,"from_house":h,"aspects_houses":sorted(casts)})
    return out

def mangal_dosha(planets):
    mars_h=planets["Mars"]["house"]
    dosha_houses={1,2,4,7,8,12}
    present=mars_h in dosha_houses
    return {"present":present,"mars_house":mars_h,
            "note":"Mars in house %d"%mars_h+(" — Manglik" if present else " — no Kuja dosha")}

def sade_sati(moon_sign,jd):
    """Is Saturn currently transiting 12th/1st/2nd from natal Moon?"""
    now=swe.julday(*map(int,datetime.now().strftime("%Y %m %d").split()),12.0)
    sat=swe.calc_ut(now,swe.SATURN,_FLG)[0][0]
    sat_sign=int(sat//30)
    diff=(sat_sign-moon_sign)%12
    phases={11:"Rising (first dhaiya)",0:"Peak (janma Shani)",1:"Setting (last dhaiya)"}
    active=diff in phases
    return {"active":active,"phase":phases.get(diff,"Not active"),
            "saturn_sign":SIGNS[sat_sign],"moon_sign":SIGNS[moon_sign]}

def detect_yogas(planets,lagna):
    y=[]
    # Gaja-Kesari: Jupiter in kendra (1/4/7/10) from Moon
    jh=planets["Jupiter"]["house"]; mh=planets["Moon"]["house"]
    if ((planets["Jupiter"]["rashi_num"]-planets["Moon"]["rashi_num"])%12)+1 in (1,4,7,10):
        y.append({"name":"Gaja-Kesari Yoga","good":True,
                  "desc":"Jupiter in a kendra from the Moon — wisdom, respect, lasting reputation."})
    # Budha-Aditya: Sun+Mercury same sign
    if planets["Sun"]["rashi_num"]==planets["Mercury"]["rashi_num"]:
        y.append({"name":"Budha-Aditya Yoga","good":True,
                  "desc":"Sun and Mercury together — sharp intellect and communication."})
    # Pancha-Mahapurusha (Ruchaka/Bhadra/Hamsa/Malavya/Sasa)
    mp={"Mars":"Ruchaka","Mercury":"Bhadra","Jupiter":"Hamsa","Venus":"Malavya","Saturn":"Sasa"}
    for pl,nm in mp.items():
        p=planets[pl]
        if p["house"] in (1,4,7,10) and p["dignity"] in ("Exalted","Own sign"):
            y.append({"name":nm+" Yoga (Pancha-Mahapurusha)","good":True,
                      "desc":f"{pl} strong in a kendra — a hallmark of distinction and character."})
    # Kemadruma (Moon isolated) — no planets in 2/12 from Moon, excl Sun/nodes
    mh=planets["Moon"]["rashi_num"]
    occ=set(pl["rashi_num"] for n,pl in planets.items() if n not in ("Moon","Sun","Rahu","Ketu"))
    kendra_from_moon=any(((pl["rashi_num"]-mh)%12)+1 in (1,4,7,10)
                         for n,pl in planets.items() if n not in ("Moon","Sun","Rahu","Ketu"))
    if (mh%12+1) not in occ and ((mh-2)%12+1) not in occ and not kendra_from_moon:
        y.append({"name":"Kemadruma Yoga","good":False,
                  "desc":"Moon without support from adjacent houses — periods of struggle; strengthened by a well-placed Moon lord."})
    return y

def vimshottari(moon_lon,dob,tob,tz):
    seg=13+1/3.0; nak=int(moon_lon//seg); frac=(moon_lon%seg)/seg
    idx=nak%9
    y,mo,d=map(int,dob.split("-")); hh,mm=map(int,tob.split(":"))
    birth=datetime(y,mo,d,hh,mm)
    lord=DASHA_LORDS[idx]
    start=birth-timedelta(days=DASHA_YEARS[lord]*frac*365.25)
    seq=[]; cur=start
    for i in range(9):
        L=DASHA_LORDS[(idx+i)%9]; yrs=DASHA_YEARS[L]
        end=cur+timedelta(days=yrs*365.25)
        node={"lord":L,"years":yrs,"start":cur.strftime("%Y-%m-%d"),"end":end.strftime("%Y-%m-%d"),
              "antar":_antar(L,cur,yrs)}
        seq.append(node); cur=end
    now=datetime.now()
    cur_maha=next((s for s in seq if s["start"]<=now.strftime("%Y-%m-%d")<=s["end"]),seq[0])
    return {"balance_years":round(DASHA_YEARS[lord]*(1-frac),2),
            "current":cur_maha["lord"],"sequence":seq}

def _antar(maha,start,maha_years):
    """Antardasha (bhukti) within a mahadasha, each with pratyantar."""
    out=[]; idx=DASHA_LORDS.index(maha); cur=start
    for i in range(9):
        L=DASHA_LORDS[(idx+i)%9]
        dur=maha_years*DASHA_YEARS[L]/120.0          # years
        end=cur+timedelta(days=dur*365.25)
        out.append({"lord":L,"start":cur.strftime("%Y-%m-%d"),"end":end.strftime("%Y-%m-%d"),
                    "pratyantar":_praty(maha,L,cur,dur)})
        cur=end
    return out

def _praty(maha,antar,start,antar_years):
    out=[]; idx=DASHA_LORDS.index(antar); cur=start
    for i in range(9):
        L=DASHA_LORDS[(idx+i)%9]
        dur=antar_years*DASHA_YEARS[L]/120.0
        end=cur+timedelta(days=dur*365.25)
        out.append({"lord":L,"start":cur.strftime("%Y-%m-%d"),"end":end.strftime("%Y-%m-%d")})
        cur=end
    return out

if __name__=="__main__":
    c=compute_chart("1997-05-21","14:30",27.7172,85.3240,5.75)
    print("Lagna",c["ascendant"]["rashi"],c["ascendant"]["dms"],"| ayan",c["ayanamsa"])
    for n in ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn","Rahu","Ketu"]:
        p=c["planets"][n]
        print(f'{n:8}{p["rashi"]:11}{p["dms"]:11}H{p["house"]:<3}{p["dignity"]:14}D9:{p["navamsa"]:10}{p["nakshatra"]}')
    print("Mangal:",c["mangal_dosha"]["note"])
    print("Sade Sati:",c["sade_sati"]["phase"],c["sade_sati"]["saturn_sign"])
    print("Yogas:",[y["name"] for y in c["yogas"]])
    print("Dasha now:",c["dasha"]["current"],"| maha count",len(c["dasha"]["sequence"]),
          "| antar in 1st",len(c["dasha"]["sequence"][0]["antar"]),
          "| praty in 1st antar",len(c["dasha"]["sequence"][0]["antar"][0]["pratyantar"]))
