# -*- coding: utf-8 -*-
"""Rule-based, trilingual (en/ne/hi) interpretation engine.
Readings are composed from building blocks: sign traits, planet significations,
house significations and planetary dignity — so every chart yields specific text."""

LANGS = ["en","ne","hi"]

SIGN_TRAITS = {
 "en":["bold, energetic and pioneering","steady, sensual and reliable","curious, communicative and quick",
       "nurturing, emotional and protective","confident, generous and proud","analytical, precise and modest",
       "harmonious, fair and relational","intense, secretive and transformative","optimistic, philosophical and free",
       "disciplined, ambitious and patient","original, humane and independent","compassionate, imaginative and spiritual"],
 "ne":["साहसी, ऊर्जावान् र अगुवा","स्थिर, भोगप्रिय र भरपर्दो","जिज्ञासु, कुशल वक्ता र फुर्तिलो",
       "ममतामयी, भावुक र संरक्षक","आत्मविश्वासी, उदार र स्वाभिमानी","विश्लेषक, सूक्ष्म र विनम्र",
       "सन्तुलित, न्यायप्रिय र सम्बन्धमुखी","गहन, गोप्य र परिवर्तनकारी","आशावादी, दार्शनिक र स्वतन्त्र",
       "अनुशासित, महत्त्वाकांक्षी र धैर्यवान्","मौलिक, मानवतावादी र स्वतन्त्र","करुणामय, कल्पनाशील र आध्यात्मिक"],
 "hi":["साहसी, ऊर्जावान और अग्रणी","स्थिर, भोगी और भरोसेमंद","जिज्ञासु, वाक्पटु और तेज़",
       "ममतामयी, भावुक और रक्षक","आत्मविश्वासी, उदार और स्वाभिमानी","विश्लेषक, सटीक और विनम्र",
       "संतुलित, न्यायप्रिय और संबंधप्रिय","गहन, गोपनीय और परिवर्तनकारी","आशावादी, दार्शनिक और स्वतंत्र",
       "अनुशासित, महत्वाकांक्षी और धैर्यवान","मौलिक, मानवीय और स्वतंत्र","करुणामय, कल्पनाशील और आध्यात्मिक"],
}

PLANET_SIG = {
 "en":{"Sun":"soul, vitality and authority","Moon":"mind, emotions and mother","Mars":"drive, courage and conflict",
       "Mercury":"intellect, speech and commerce","Jupiter":"wisdom, fortune and dharma","Venus":"love, beauty and comfort",
       "Saturn":"discipline, karma and endurance","Rahu":"ambition, obsession and worldly desire","Ketu":"detachment, spirituality and past karma"},
 "ne":{"Sun":"आत्मा, ओज र अधिकार","Moon":"मन, भावना र माता","Mars":"साहस, ऊर्जा र संघर्ष",
       "Mercury":"बुद्धि, वाणी र व्यापार","Jupiter":"ज्ञान, भाग्य र धर्म","Venus":"प्रेम, सौन्दर्य र सुख",
       "Saturn":"अनुशासन, कर्म र सहनशीलता","Rahu":"महत्त्वाकांक्षा, आसक्ति र सांसारिक इच्छा","Ketu":"वैराग्य, अध्यात्म र पूर्वकर्म"},
 "hi":{"Sun":"आत्मा, ओज और अधिकार","Moon":"मन, भावना और माता","Mars":"साहस, ऊर्जा और संघर्ष",
       "Mercury":"बुद्धि, वाणी और व्यापार","Jupiter":"ज्ञान, भाग्य और धर्म","Venus":"प्रेम, सौंदर्य और सुख",
       "Saturn":"अनुशासन, कर्म और सहनशीलता","Rahu":"महत्वाकांक्षा, आसक्ति और सांसारिक इच्छा","Ketu":"वैराग्य, अध्यात्म और पूर्वकर्म"},
}

HOUSE_SIG = {
 "en":["self, body and personality","wealth, family and speech","courage, siblings and effort","home, mother and happiness",
       "creativity, children and intellect","health, enemies and service","marriage, partnership and others","longevity, transformation and the hidden",
       "fortune, dharma and higher learning","career, status and action","gains, friends and aspirations","loss, expenses and liberation"],
 "ne":["स्वयं, शरीर र व्यक्तित्व","धन, परिवार र वाणी","साहस, भाइबहिनी र प्रयास","घर, माता र सुख",
       "सृजन, सन्तान र बुद्धि","स्वास्थ्य, शत्रु र सेवा","विवाह, साझेदारी र अरू","आयु, परिवर्तन र गुप्त कुरा",
       "भाग्य, धर्म र उच्च शिक्षा","करियर, प्रतिष्ठा र कर्म","लाभ, मित्र र आकांक्षा","व्यय, हानि र मोक्ष"],
 "hi":["स्वयं, शरीर और व्यक्तित्व","धन, परिवार और वाणी","साहस, भाई-बहन और प्रयास","घर, माता और सुख",
       "सृजन, संतान और बुद्धि","स्वास्थ्य, शत्रु और सेवा","विवाह, साझेदारी और अन्य","आयु, परिवर्तन और गुप्त",
       "भाग्य, धर्म और उच्च शिक्षा","करियर, प्रतिष्ठा और कर्म","लाभ, मित्र और आकांक्षा","व्यय, हानि और मोक्ष"],
}

DIGNITY_PHRASE = {
 "en":{"Exalted":"is exalted here, giving its finest results","Own sign":"sits in its own sign, strong and stable",
       "Friendly":"is comfortably placed in a friend's sign","Neutral":"gives balanced, mixed results here",
       "Enemy sign":"is placed in a difficult sign and must work harder","Debilitated":"is debilitated, so its results come with effort and lessons","-":"acts through the house it occupies"},
 "ne":{"Exalted":"उच्चको भई उत्कृष्ट फल दिन्छ","Own sign":"स्वगृही भई बलियो र स्थिर छ",
       "Friendly":"मित्रराशिमा सहज अवस्थामा छ","Neutral":"सन्तुलित र मिश्रित फल दिन्छ",
       "Enemy sign":"शत्रुराशिमा भई बढी परिश्रम खोज्छ","Debilitated":"नीचको भएकाले फल परिश्रम र शिक्षासहित आउँछ","-":"आफू रहेको भावअनुसार फल दिन्छ"},
 "hi":{"Exalted":"उच्च का होकर श्रेष्ठ फल देता है","Own sign":"स्वगृही होकर बलवान और स्थिर है",
       "Friendly":"मित्र राशि में सहज स्थित है","Neutral":"संतुलित और मिश्रित फल देता है",
       "Enemy sign":"शत्रु राशि में होकर अधिक परिश्रम माँगता है","Debilitated":"नीच का होने से फल परिश्रम व सीख के साथ आता है","-":"जिस भाव में है उसके अनुसार फल देता है"},
}

# short section framing words
UI = {
 "en":{"asc":"Ascendant","moon":"Moon","in_house":"in the","house":"house","reads":"Reading",
       "no_manglik":"No Maṅgal dosha — Mars is not in a dosha house.",
       "manglik":"Maṅgal (Kuja) dosha is present — traditionally advised to match with a compatible partner; many classical cancellations can apply.",
       "sade_on":"Sāde Sātī is currently active","sade_off":"Sāde Sātī is not active right now",
       "health_note":"This is a traditional astrological view of tendencies, not medical advice."},
 "ne":{"asc":"लग्न","moon":"चन्द्र","in_house":"भावमा","house":"भाव","reads":"फलादेश",
       "no_manglik":"मंगल दोष छैन — मंगल दोष भावमा छैन।",
       "manglik":"मंगल (कुज) दोष छ — परम्परागत रूपमा अनुकूल जोडी मिलाउन सल्लाह दिइन्छ; धेरै शास्त्रीय अपवाद लागू हुन सक्छन्।",
       "sade_on":"साढेसाती हाल सक्रिय छ","sade_off":"साढेसाती हाल सक्रिय छैन",
       "health_note":"यो प्रवृत्तिको परम्परागत ज्योतिषीय दृष्टिकोण हो, चिकित्सा सल्लाह होइन।"},
 "hi":{"asc":"लग्न","moon":"चंद्र","in_house":"भाव में","house":"भाव","reads":"फलादेश",
       "no_manglik":"मंगल दोष नहीं — मंगल दोष भाव में नहीं है।",
       "manglik":"मंगल (कुज) दोष है — परंपरा अनुसार अनुकूल जीवनसाथी का मिलान उचित; अनेक शास्त्रीय अपवाद लागू हो सकते हैं।",
       "sade_on":"साढ़ेसाती अभी सक्रिय है","sade_off":"साढ़ेसाती अभी सक्रिय नहीं है",
       "health_note":"यह प्रवृत्तियों का पारंपरिक ज्योतिषीय दृष्टिकोण है, चिकित्सकीय सलाह नहीं।"},
}

# which houses/planets each life-section keys on
SECTION_HOUSES = {"career":[10,2,11,6],"relationships":[7,5,4],"health":[1,6,8],"personality":[1]}
REMEDY = {
 "en":{"Sun":"Offer water to the Sun at dawn; honour Surya.","Moon":"Respect the mother; observe Monday fasts; wear white.",
       "Mars":"Support siblings; recite Hanuman Chalisa; give red lentils on Tuesday.","Mercury":"Feed green fodder to cows; help students; wear green on Wednesday.",
       "Jupiter":"Respect teachers and elders; donate turmeric or gram on Thursday.","Venus":"Cultivate art and cleanliness; honour women; donate white sweets on Friday.",
       "Saturn":"Serve the elderly and labourers; give sesame/oil on Saturday; be patient.","Rahu":"Avoid shortcuts; donate to the marginalised; keep routines clean.","Ketu":"Pursue meditation and simplicity; care for dogs; keep spiritual discipline."},
 "ne":{"Sun":"बिहान सूर्यलाई जल चढाउनुहोस्; सूर्यको आदर गर्नुहोस्।","Moon":"आमाको सम्मान; सोमबार व्रत; सेतो वस्त्र।",
       "Mars":"भाइबहिनीलाई सहयोग; हनुमान चालीसा; मंगलबार रातो दाल दान।","Mercury":"गाईलाई हरियो घाँस; विद्यार्थीलाई सहयोग; बुधबार हरियो।",
       "Jupiter":"गुरु र ठूलाको आदर; बिहीबार बेसार/चना दान।","Venus":"कला र सफाइ; महिलाको सम्मान; शुक्रबार सेतो मिठाई दान।",
       "Saturn":"वृद्ध र श्रमिकको सेवा; शनिबार तिल/तेल दान; धैर्य।","Rahu":"छोटो बाटो नखोज्नु; वञ्चितलाई दान; नियमित दिनचर्या।","Ketu":"ध्यान र सरलता; कुकुरको हेरचाह; आध्यात्मिक अनुशासन।"},
 "hi":{"Sun":"प्रातः सूर्य को जल; सूर्य का सम्मान।","Moon":"माता का सम्मान; सोमवार व्रत; श्वेत वस्त्र।",
       "Mars":"भाई-बहन की सहायता; हनुमान चालीसा; मंगलवार लाल दाल दान।","Mercury":"गाय को हरा चारा; विद्यार्थियों की मदद; बुधवार हरा।",
       "Jupiter":"गुरु व बड़ों का सम्मान; गुरुवार हल्दी/चना दान।","Venus":"कला व स्वच्छता; स्त्रियों का सम्मान; शुक्रवार श्वेत मिठाई दान।",
       "Saturn":"वृद्ध व श्रमिकों की सेवा; शनिवार तिल/तेल दान; धैर्य।","Rahu":"शॉर्टकट से बचें; वंचितों को दान; नियमित दिनचर्या।","Ketu":"ध्यान व सरलता; कुत्तों की देखभाल; आध्यात्मिक अनुशासन।"},
}


# Devanagari localisation for sign & planet names (ne/hi share script)
SIGN_DEVA={"Mesha":"मेष","Vrishabha":"वृष","Mithuna":"मिथुन","Karka":"कर्क","Simha":"सिंह","Kanya":"कन्या",
 "Tula":"तुला","Vrischika":"वृश्चिक","Dhanu":"धनु","Makara":"मकर","Kumbha":"कुम्भ","Meena":"मीन"}
PLANET_DEVA={"Sun":"सूर्य","Moon":"चन्द्र","Mars":"मंगल","Mercury":"बुध","Jupiter":"गुरु","Venus":"शुक्र",
 "Saturn":"शनि","Rahu":"राहु","Ketu":"केतु"}
NAK_DEVA={}  # names kept in transliteration; optional future work
def _localize(text):
    for k,v in SIGN_DEVA.items(): text=text.replace(k,v)
    for k,v in PLANET_DEVA.items(): text=text.replace(k,v)
    return text

def _ordinal(n):
    return {1:"1st",2:"2nd",3:"3rd"}.get(n,f"{n}th")

def planet_line(lang, name, p):
    sig=PLANET_SIG[lang][name]; hs=HOUSE_SIG[lang][p["house"]-1]; dg=DIGNITY_PHRASE[lang][p["dignity"]]
    if lang=="en":
        return f"{name} ({sig}) {dg}, active in the {_ordinal(p['house'])} house of {hs}."
    conn={"ne":"—","hi":"—"}[lang]
    hn=p["house"]
    return f"{name} ({sig}) {dg}; {hn} {UI[lang]['house']} ({hs}) मा सक्रिय।" if lang=="ne" \
           else f"{name} ({sig}) {dg}; {hn} {UI[lang]['house']} ({hs}) में सक्रिय।"

def build_readings(chart):
    """Return {lang: {section: text}} for all six sections."""
    out={}
    for lang in LANGS:
        P=chart["planets"]; asc=chart["ascendant"]
        lagna_sign=asc["rashi_num"]-1; moon_sign=P["Moon"]["rashi_num"]-1
        t=SIGN_TRAITS[lang]; ui=UI[lang]
        # PERSONALITY
        if lang=="en":
            personality=(f"With {asc['rashi']} rising, your core nature is {t[lagna_sign]}. "
                f"The Moon in {P['Moon']['rashi']} makes your emotional world {t[moon_sign]}, "
                f"while the Sun in {P['Sun']['rashi']} shapes a {t[P['Sun']['rashi_num']-1]} inner drive. "
                f"Born under {P['Moon']['nakshatra']} nakṣatra, subtle themes of that star colour your temperament.")
        elif lang=="ne":
            personality=(f"{asc['rashi']} लग्न भएकाले तपाईंको मूल स्वभाव {t[lagna_sign]} छ। "
                f"{P['Moon']['rashi']} मा चन्द्र हुँदा भावनात्मक संसार {t[moon_sign]} बन्छ, "
                f"र {P['Sun']['rashi']} को सूर्यले {t[P['Sun']['rashi_num']-1]} आन्तरिक प्रेरणा दिन्छ। "
                f"{P['Moon']['nakshatra']} नक्षत्रले तपाईंको मिजासमा सूक्ष्म प्रभाव पार्छ।")
        else:
            personality=(f"{asc['rashi']} लग्न होने से आपका मूल स्वभाव {t[lagna_sign]} है। "
                f"{P['Moon']['rashi']} में चंद्र आपके भावनात्मक संसार को {t[moon_sign]} बनाता है, "
                f"और {P['Sun']['rashi']} का सूर्य {t[P['Sun']['rashi_num']-1]} आंतरिक प्रेरणा देता है। "
                f"{P['Moon']['nakshatra']} नक्षत्र आपके मिजाज़ में सूक्ष्म प्रभाव डालता है।")
        def section_for(planets_of_interest):
            return " ".join(planet_line(lang,n,P[n]) for n in planets_of_interest)
        career=section_for(["Sun","Saturn","Mercury","Jupiter"])
        relationships=section_for(["Venus","Mars"]) + " " + (ui["manglik"] if chart["mangal_dosha"]["present"] else ui["no_manglik"])
        health=section_for(["Mars","Saturn"]) + " " + ui["health_note"]
        # STRENGTHS / CHALLENGES from dignity
        strong=[n for n in P if P[n]["dignity"] in ("Exalted","Own sign")]
        weak=[n for n in P if P[n]["dignity"]=="Debilitated"]
        if lang=="en":
            sc=(("Strengths: "+", ".join(strong)+" are well-placed and support you. " if strong else "")
                +("Growth areas: "+", ".join(weak)+" ask for conscious effort. " if weak else "")
                +("Notable yogas: "+", ".join(y["name"] for y in chart["yogas"])+"." if chart["yogas"] else ""))
        elif lang=="ne":
            sc=(("बलियो पक्ष: "+", ".join(strong)+" राम्रो अवस्थामा छन्। " if strong else "")
                +("सुधार्ने पक्ष: "+", ".join(weak)+" ले सचेत प्रयास खोज्छन्। " if weak else "")
                +("योग: "+", ".join(y["name"] for y in chart["yogas"])+"।" if chart["yogas"] else ""))
        else:
            sc=(("शक्ति: "+", ".join(strong)+" उत्तम स्थिति में हैं। " if strong else "")
                +("सुधार क्षेत्र: "+", ".join(weak)+" सचेत प्रयास माँगते हैं। " if weak else "")
                +("योग: "+", ".join(y["name"] for y in chart["yogas"])+"।" if chart["yogas"] else ""))
        # REMEDIES for weak/afflicted planets (fallback: lagna lord + Saturn)
        focus=weak or [chart["lagna_lord"],"Saturn"]
        remedies=" ".join(REMEDY[lang][n] for n in dict.fromkeys(focus) if n in REMEDY[lang])
        sec={"personality":personality,"career":career,"relationships":relationships,
                   "health":health,"strengths":sc.strip(),"remedies":remedies,
                   "purpose":build_purpose(lang,chart)}
        if lang in ("ne","hi"): sec={k:_localize(v) for k,v in sec.items()}
        out[lang]=sec
    return out


def _ord3(lang,n):
    if lang=="en": return _ordinal(n)
    return str(n)


YOGA_TR={
 "Gaja-Kesari":{"name":{"en":"Gaja-Kesari Yoga","ne":"गजकेसरी योग","hi":"गजकेसरी योग"},
   "desc":{"en":"Jupiter in a kendra from the Moon — wisdom, respect and lasting reputation.",
           "ne":"चन्द्रमाबाट केन्द्रमा गुरु — ज्ञान, सम्मान र दीर्घ प्रतिष्ठा।",
           "hi":"चंद्रमा से केंद्र में गुरु — ज्ञान, सम्मान और स्थायी प्रतिष्ठा।"}},
 "Budha-Aditya":{"name":{"en":"Budha-Aditya Yoga","ne":"बुधादित्य योग","hi":"बुधादित्य योग"},
   "desc":{"en":"Sun and Mercury together — sharp intellect and fluent communication.",
           "ne":"सूर्य र बुध सँगै — तीक्ष्ण बुद्धि र प्रवाहमय अभिव्यक्ति।",
           "hi":"सूर्य और बुध साथ — तीक्ष्ण बुद्धि और प्रवाहमय अभिव्यक्ति।"}},
 "Kemadruma":{"name":{"en":"Kemadruma Yoga","ne":"केमद्रुम योग","hi":"केमद्रुम योग"},
   "desc":{"en":"Moon without support from adjacent houses — periods of struggle, eased by a strong Moon-lord.",
           "ne":"छेउका भावबाट सहयोग नपाएको चन्द्र — संघर्षका कालखण्ड, बलियो चन्द्र-स्वामीले सहज बनाउँछ।",
           "hi":"निकट भावों से सहयोग रहित चंद्र — संघर्ष के काल, बलवान चंद्र-स्वामी से सुगम।"}},
 "Pancha":{"name":{"en":"","ne":"","hi":""},
   "desc":{"en":"A strong benefic in its own or exalted sign in a kendra — a Pañca-Mahāpuruṣa marker of distinction, character and success.",
           "ne":"केन्द्रमा स्वगृही वा उच्च शुभ ग्रह — पञ्चमहापुरुष योगको लक्षण: प्रतिष्ठा, चरित्र र सफलता।",
           "hi":"केंद्र में स्वगृही या उच्च शुभ ग्रह — पंचमहापुरुष योग का लक्षण: प्रतिष्ठा, चरित्र और सफलता।"}},
}
def build_yogas(chart):
    out={l:[] for l in LANGS}
    for y in chart["yogas"]:
        nm=y["name"]
        if "Gaja-Kesari" in nm: key="Gaja-Kesari"
        elif "Budha-Aditya" in nm: key="Budha-Aditya"
        elif "Kemadruma" in nm: key="Kemadruma"
        elif "Pancha" in nm: key="Pancha"
        else: key=None
        for lang in LANGS:
            if key=="Pancha":
                # keep specific name (Ruchaka etc.), localised desc
                nm_l=nm.split(" Yoga")[0]+(" योग" if lang!="en" else " Yoga")
                out[lang].append({"name":nm_l if lang!="en" else nm,"desc":YOGA_TR["Pancha"]["desc"][lang],"good":y["good"]})
            elif key:
                out[lang].append({"name":YOGA_TR[key]["name"][lang],"desc":YOGA_TR[key]["desc"][lang],"good":y["good"]})
            else:
                out[lang].append({"name":nm,"desc":y["desc"],"good":y["good"]})
    return out

def build_purpose(lang, chart):
    P=chart["planets"]; asc=chart["ascendant"]
    ak=chart["atmakaraka"]; dk=chart["karakas"]["planet_of"]["Darakaraka"]
    ketu_h=P["Ketu"]["house"]; rahu_h=P["Rahu"]["house"]
    d=chart["dharma"]; tl=d["tenth_lord"]
    aksig=PLANET_SIG[lang][ak]; kh=HOUSE_SIG[lang][ketu_h-1]; rh=HOUSE_SIG[lang][rahu_h-1]
    thsig=HOUSE_SIG[lang][9]
    if lang=="en":
        txt=(f"Your soul-planet (Ātmakāraka) is {ak}, governing {aksig} — the central lesson your life keeps returning to. "
             f"Ketu in the {_ordinal(ketu_h)} house shows mastery you already carry from before: {kh} come to you naturally, almost effortlessly. "
             f"Rāhu in the {_ordinal(rahu_h)} house marks the unfamiliar frontier your growth demands this lifetime — {rh} is where you are meant to stretch, hunger, and evolve. "
             f"Worldly dharma flows through your 10th lord {tl} and a {d['ninth_sign']} 9th house of higher purpose ({thsig}). "
             f"Your purpose crystallises where these meet: honour the {ak} lesson, use Ketu's inborn gifts as your tools, and walk consciously toward Rāhu's direction rather than retreating into old comfort. That tension, lived well, is your dharma.")
    elif lang=="ne":
        txt=(f"तपाईंको आत्मग्रह (आत्मकारक) {ak} हो, जसले {aksig} लाई प्रतिनिधित्व गर्छ — यही जीवनको केन्द्रीय पाठ हो। "
             f"{ketu_h} भावमा केतुले पूर्वजन्मबाट ल्याएको दक्षता देखाउँछ: {kh} सहजै प्राप्त हुन्छ। "
             f"{rahu_h} भावमा राहुले यस जन्ममा विकासका लागि अपरिचित क्षेत्र देखाउँछ — {rh} मै तपाईंले आफूलाई खार्नुपर्छ। "
             f"सांसारिक धर्म दशम स्वामी {tl} र {d['ninth_sign']} नवम भाव ({thsig}) मार्फत बग्छ। "
             f"उद्देश्य यहीँ प्रकट हुन्छ: {ak} को पाठलाई सम्मान गर्नुहोस्, केतुका जन्मजात गुणलाई साधन बनाउनुहोस्, र पुरानो सुविधामा फर्किनुको सट्टा सचेत भई राहुको दिशातर्फ अघि बढ्नुहोस्।")
    else:
        txt=(f"आपका आत्मग्रह (आत्मकारक) {ak} है, जो {aksig} का प्रतिनिधित्व करता है — यही जीवन का केंद्रीय पाठ है। "
             f"{ketu_h} भाव में केतु पूर्वजन्म से लाई दक्षता दर्शाता है: {kh} सहज ही मिलता है। "
             f"{rahu_h} भाव में राहु इस जन्म में विकास हेतु अपरिचित क्षेत्र दिखाता है — {rh} में ही आपको स्वयं को गढ़ना है। "
             f"सांसारिक धर्म दशम स्वामी {tl} और {d['ninth_sign']} नवम भाव ({thsig}) से प्रवाहित होता है। "
             f"उद्देश्य यहीं प्रकट होता है: {ak} के पाठ का सम्मान करें, केतु के जन्मजात गुणों को साधन बनाएँ, और पुरानी सुविधा में लौटने के बजाय सचेत होकर राहु की दिशा में बढ़ें।")
    if lang in ("ne","hi"): txt=_localize(txt)
    return txt

def build_timeline(chart):
    """Major life-prediction chapters, one per mahadasha, trilingual."""
    P=chart["planets"]; out={l:[] for l in LANGS}
    for m in chart["dasha"]["sequence"]:
        lord=m["lord"]
        if lord in ("Rahu","Ketu"):
            hp=P[lord]; hsig_i=hp["house"]-1
        else:
            hp=P[lord]; hsig_i=hp["house"]-1
        dig=hp.get("dignity","-")
        for lang in LANGS:
            sig=PLANET_SIG[lang][lord]; hs=HOUSE_SIG[lang][hsig_i]; dgp=DIGNITY_PHRASE[lang][dig]
            if lang=="en":
                text=(f"A chapter shaped by {sig}. With {lord} placed in the {_ordinal(hp['house'])} house of {hs} and {dgp}, "
                      f"life focuses on {hs}; results are {'strong and supportive' if dig in ('Exalted','Own sign') else 'testing but growth-giving' if dig in ('Debilitated','Enemy sign') else 'mixed and gradual'}.")
            elif lang=="ne":
                text=(f"{sig} ले आकार दिने कालखण्ड। {lord} {hp['house']} भाव ({hs}) मा रहेर {dgp}, "
                      f"जीवन {hs} मा केन्द्रित हुन्छ; फल {'बलियो र अनुकूल' if dig in ('Exalted','Own sign') else 'परीक्षण तर विकासकारी' if dig in ('Debilitated','Enemy sign') else 'मिश्रित र क्रमिक'} रहन्छ।")
                text=_localize(text)
            else:
                text=(f"{sig} से आकार पाने वाला कालखंड। {lord} {hp['house']} भाव ({hs}) में स्थित होकर {dgp}, "
                      f"जीवन {hs} पर केंद्रित रहता है; फल {'बलवान व अनुकूल' if dig in ('Exalted','Own sign') else 'परीक्षणपूर्ण पर विकासकारी' if dig in ('Debilitated','Enemy sign') else 'मिश्रित व क्रमिक'} रहते हैं।")
                text=_localize(text)
            out[lang].append({"lord":lord,"start":m["start"],"end":m["end"],"text":text})
    return out

if __name__=="__main__":
    from jyotish import compute_chart
    c=compute_chart("1997-05-21","14:30",27.7172,85.3240,5.75)
    r=build_readings(c)
    for lang in LANGS:
        print("\n===",lang,"===")
        print("PERSONALITY:",r[lang]["personality"][:220])
        print("CAREER:",r[lang]["career"][:180])
    print("\nRemedies(en):",r["en"]["remedies"][:160])
