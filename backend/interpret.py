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


SIGN_DEVA={"Mesha":"मेष","Vrishabha":"वृष","Mithuna":"मिथुन","Karka":"कर्क","Simha":"सिंह","Kanya":"कन्या",
 "Tula":"तुला","Vrischika":"वृश्चिक","Dhanu":"धनु","Makara":"मकर","Kumbha":"कुम्भ","Meena":"मीन"}
PLANET_DEVA={"Sun":"सूर्य","Moon":"चन्द्र","Mars":"मंगल","Mercury":"बुध","Jupiter":"गुरु","Venus":"शुक्र",
 "Saturn":"शनि","Rahu":"राहु","Ketu":"केतु"}
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
    hn=p["house"]
    return f"{name} ({sig}) {dg}; {hn} {UI[lang]['house']} ({hs}) मा सक्रिय।" if lang=="ne" \
           else f"{name} ({sig}) {dg}; {hn} {UI[lang]['house']} ({hs}) में सक्रिय।"

def build_readings(chart):
    out={}
    for lang in LANGS:
        P=chart["planets"]; asc=chart["ascendant"]
        lagna_sign=asc["rashi_num"]-1; moon_sign=P["Moon"]["rashi_num"]-1
        t=SIGN_TRAITS[lang]; ui=UI[lang]
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
        focus=weak or [chart["lagna_lord"],"Saturn"]
        remedies=" ".join(REMEDY[lang][n] for n in dict.fromkeys(focus) if n in REMEDY[lang])
        sec={"personality":personality,"career":career,"relationships":relationships,
                   "health":health,"strengths":sc.strip(),"remedies":remedies,
                   "purpose":build_purpose(lang,chart)}
        if lang in ("ne","hi"): sec={k:_localize(v) for k,v in sec.items()}
        out[lang]=sec
    return out


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


PLANET_AREA={
 "en":{
  "Sun":{"career":"leadership, authority and public recognition","wealth":"status-linked income and government/official sources","relationships":"matters of ego, pride and the father","health":"heart, spine, eyes and overall vitality","mind":"confidence, willpower and sense of self"},
  "Moon":{"career":"public-facing work, care roles and changeable paths","wealth":"fluctuating cash-flow tied to moods and the public","relationships":"emotional bonding, the mother and home life","health":"mind, chest, fluids and sleep","mind":"emotions, intuition and inner peace"},
  "Mars":{"career":"drive, competition, engineering, sports or defence","wealth":"gains through effort, property and bold action","relationships":"passion, friction and the need for patience","health":"blood, muscles, accidents and inflammation","mind":"courage, anger and decisiveness"},
  "Mercury":{"career":"communication, business, writing, trade and analysis","wealth":"income through skill, commerce and networks","relationships":"friendship, wit and clear communication","health":"nerves, skin, speech and digestion","mind":"intellect, adaptability and learning"},
  "Jupiter":{"career":"teaching, advising, law, finance and expansion","wealth":"growth, savings and fortunate opportunities","relationships":"marriage, children, mentors and trust","health":"liver, weight and metabolism","mind":"wisdom, optimism and ethics"},
  "Venus":{"career":"art, design, media, luxury and relationships work","wealth":"comfort, vehicles and pleasant sources of income","relationships":"love, marriage, romance and harmony","health":"reproductive system, kidneys and throat","mind":"desire, aesthetics and contentment"},
  "Saturn":{"career":"slow, steady rise through discipline and long labour","wealth":"delayed but lasting gains through persistence","relationships":"commitment, duty and testing of bonds","health":"bones, joints, teeth and chronic issues","mind":"patience, discipline and endurance"},
  "Rahu":{"career":"unconventional fields, foreign links and sudden rises","wealth":"speculative, foreign or unexpected gains and risks","relationships":"unusual, intense or unconventional ties","health":"mysterious, hard-to-diagnose or nervous issues","mind":"ambition, obsession and restlessness"},
  "Ketu":{"career":"research, spirituality, healing and behind-the-scenes work","wealth":"detachment from money; gains then loss of interest","relationships":"karmic bonds, separations and inner distance","health":"subtle, immune and psychosomatic matters","mind":"detachment, insight and spiritual seeking"}},
}
PLANET_AREA["ne"]={
 "Sun":{"career":"नेतृत्व, अधिकार र सार्वजनिक प्रतिष्ठा","wealth":"पद-सम्बद्ध आय र सरकारी स्रोत","relationships":"अहं, स्वाभिमान र पिता","health":"मुटु, मेरुदण्ड, आँखा र ओज","mind":"आत्मविश्वास र इच्छाशक्ति"},
 "Moon":{"career":"जनसम्पर्क, हेरचाह र परिवर्तनशील मार्ग","wealth":"मनोदशासँग जोडिएको अस्थिर नगद-प्रवाह","relationships":"भावनात्मक बन्धन, माता र घर","health":"मन, छाती र निद्रा","mind":"भावना, अन्तर्ज्ञान र शान्ति"},
 "Mars":{"career":"ऊर्जा, प्रतिस्पर्धा, इन्जिनियरिङ वा सुरक्षा","wealth":"परिश्रम, जग्गा र साहसिक कार्यबाट लाभ","relationships":"आवेग, टकराव र धैर्यको आवश्यकता","health":"रगत, मांसपेशी र चोटपटक","mind":"साहस, रिस र निर्णयक्षमता"},
 "Mercury":{"career":"सञ्चार, व्यापार, लेखन र विश्लेषण","wealth":"सीप, वाणिज्य र सञ्जालबाट आय","relationships":"मित्रता र स्पष्ट सञ्चार","health":"स्नायु, छाला र पाचन","mind":"बुद्धि, अनुकूलनशीलता र सिकाइ"},
 "Jupiter":{"career":"शिक्षण, सल्लाह, कानून र वित्त","wealth":"वृद्धि, बचत र भाग्यशाली अवसर","relationships":"विवाह, सन्तान र गुरु","health":"कलेजो, तौल र चयापचय","mind":"ज्ञान, आशावाद र नैतिकता"},
 "Venus":{"career":"कला, डिजाइन, मिडिया र विलासिता","wealth":"सुविधा, सवारी र सुखद आय-स्रोत","relationships":"प्रेम, विवाह र सामंजस्य","health":"प्रजनन प्रणाली, मृगौला र घाँटी","mind":"इच्छा, सौन्दर्यबोध र सन्तुष्टि"},
 "Saturn":{"career":"अनुशासन र दीर्घ परिश्रमबाट क्रमिक उन्नति","wealth":"ढिलो तर दिगो लाभ","relationships":"प्रतिबद्धता, कर्तव्य र बन्धनको परीक्षा","health":"हाड, जोर्नी, दाँत र दीर्घ रोग","mind":"धैर्य, अनुशासन र सहनशीलता"},
 "Rahu":{"career":"अपरम्परागत क्षेत्र, विदेशी सम्बन्ध र अकस्मात् उन्नति","wealth":"सट्टा, विदेशी वा अप्रत्याशित लाभ र जोखिम","relationships":"असामान्य, गहन वा अपरम्परागत सम्बन्ध","health":"रहस्यमय वा स्नायुजन्य समस्या","mind":"महत्त्वाकांक्षा, आसक्ति र बेचैनी"},
 "Ketu":{"career":"अनुसन्धान, अध्यात्म, उपचार र पर्दा पछाडिको काम","wealth":"धनप्रति वैराग्य; लाभपछि रुचि हराउने","relationships":"कार्मिक बन्धन, वियोग र आन्तरिक दूरी","health":"सूक्ष्म, प्रतिरक्षा र मनोदैहिक कुरा","mind":"वैराग्य, अन्तर्दृष्टि र आध्यात्मिक खोज"}}
PLANET_AREA["hi"]={
 "Sun":{"career":"नेतृत्व, अधिकार व सार्वजनिक प्रतिष्ठा","wealth":"पद-संबद्ध आय व सरकारी स्रोत","relationships":"अहं, स्वाभिमान व पिता","health":"हृदय, रीढ़, नेत्र व ओज","mind":"आत्मविश्वास व इच्छाशक्ति"},
 "Moon":{"career":"जनसंपर्क, देखभाल व परिवर्तनशील मार्ग","wealth":"मनोदशा से जुड़ा अस्थिर नकदी-प्रवाह","relationships":"भावनात्मक बंधन, माता व घर","health":"मन, वक्ष व निद्रा","mind":"भावना, अंतर्ज्ञान व शांति"},
 "Mars":{"career":"ऊर्जा, प्रतिस्पर्धा, इंजीनियरिंग या सुरक्षा","wealth":"परिश्रम, भूमि व साहसिक कार्य से लाभ","relationships":"आवेग, टकराव व धैर्य की आवश्यकता","health":"रक्त, मांसपेशी व चोट","mind":"साहस, क्रोध व निर्णयक्षमता"},
 "Mercury":{"career":"संचार, व्यापार, लेखन व विश्लेषण","wealth":"कौशल, वाणिज्य व नेटवर्क से आय","relationships":"मित्रता व स्पष्ट संचार","health":"स्नायु, त्वचा व पाचन","mind":"बुद्धि, अनुकूलनशीलता व सीख"},
 "Jupiter":{"career":"शिक्षण, सलाह, विधि व वित्त","wealth":"वृद्धि, बचत व भाग्यशाली अवसर","relationships":"विवाह, संतान व गुरु","health":"यकृत, वजन व चयापचय","mind":"ज्ञान, आशावाद व नैतिकता"},
 "Venus":{"career":"कला, डिज़ाइन, मीडिया व विलासिता","wealth":"सुविधा, वाहन व सुखद आय-स्रोत","relationships":"प्रेम, विवाह व सामंजस्य","health":"प्रजनन तंत्र, गुर्दे व गला","mind":"इच्छा, सौंदर्यबोध व संतोष"},
 "Saturn":{"career":"अनुशासन व दीर्घ परिश्रम से क्रमिक उन्नति","wealth":"विलंबित पर स्थायी लाभ","relationships":"प्रतिबद्धता, कर्तव्य व बंधनों की परीक्षा","health":"अस्थि, जोड़, दाँत व दीर्घ रोग","mind":"धैर्य, अनुशासन व सहनशीलता"},
 "Rahu":{"career":"अपरंपरागत क्षेत्र, विदेशी संबंध व आकस्मिक उन्नति","wealth":"सट्टा, विदेशी या अप्रत्याशित लाभ व जोखिम","relationships":"असामान्य, गहन या अपरंपरागत संबंध","health":"रहस्यमय या स्नायुजन्य समस्याएँ","mind":"महत्वाकांक्षा, आसक्ति व बेचैनी"},
 "Ketu":{"career":"अनुसंधान, अध्यात्म, उपचार व पर्दे के पीछे का कार्य","wealth":"धन से वैराग्य; लाभ के बाद रुचि का ह्रास","relationships":"कार्मिक बंधन, वियोग व आंतरिक दूरी","health":"सूक्ष्म, प्रतिरक्षा व मनोदैहिक विषय","mind":"वैराग्य, अंतर्दृष्टि व आध्यात्मिक खोज"}}

VALENCE={
 "en":{"strong":"strongly supported and favourable","weak":"tested — progress needs conscious effort","mixed":"steady but mixed; results come gradually"},
 "ne":{"strong":"बलियो र अनुकूल","weak":"परीक्षणपूर्ण — प्रगतिका लागि सचेत प्रयास चाहिन्छ","mixed":"स्थिर तर मिश्रित; फल क्रमशः आउँछ"},
 "hi":{"strong":"बलवान व अनुकूल","weak":"परीक्षणपूर्ण — प्रगति हेतु सचेत प्रयास आवश्यक","mixed":"स्थिर पर मिश्रित; फल क्रमशः आते हैं"}}

def _valence(dig):
    if dig in ("Exalted","Own sign"): return "strong"
    if dig in ("Debilitated","Enemy sign"): return "weak"
    return "mixed"

def build_timeline(chart):
    P=chart["planets"]; out={l:[] for l in LANGS}
    for m in chart["dasha"]["sequence"]:
        lord=m["lord"]; hp=P[lord]; dig=hp.get("dignity","-"); val=_valence(dig)
        for lang in LANGS:
            sig=PLANET_SIG[lang][lord]; hs=HOUSE_SIG[lang][hp["house"]-1]; dgp=DIGNITY_PHRASE[lang][dig]
            va=VALENCE[lang][val]
            if lang=="en":
                summary=(f"A life-chapter shaped by {sig}. {lord} sits in the {_ordinal(hp['house'])} house of {hs} and {dgp}, "
                         f"so this period centres on {hs}.")
            elif lang=="ne":
                summary=_localize(f"{sig} le आकार दिने जीवन-अध्याय। {lord} {hp['house']} भाव ({hs}) मा रहेर {dgp}, "
                         f"यस अवधि {hs} मा केन्द्रित हुन्छ।")
            else:
                summary=_localize(f"{sig} से आकार पाने वाला जीवन-अध्याय। {lord} {hp['house']} भाव ({hs}) में स्थित होकर {dgp}, "
                         f"यह अवधि {hs} पर केंद्रित रहती है।")
            area=PLANET_AREA[lang][lord]
            aspects={}
            for key in ("career","wealth","relationships","health","mind"):
                kw=area[key]
                if lang=="en": aspects[key]=f"{kw} — {va}."
                elif lang=="ne": aspects[key]=_localize(f"{kw} — {va}।")
                else: aspects[key]=_localize(f"{kw} — {va}।")
            out[lang].append({"lord":lord,"start":m["start"],"end":m["end"],
                              "summary":summary,"aspects":aspects})
    return out
