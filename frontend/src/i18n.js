// Central localization: sign/planet names, table headers, dignity, chart labels, UI strings.
const SIGN_ROMAN=["Mesha","Vrishabha","Mithuna","Karka","Simha","Kanya",
  "Tula","Vrischika","Dhanu","Makara","Kumbha","Meena"]
const SIGN_DEVA=["मेष","वृष","मिथुन","कर्क","सिंह","कन्या","तुला","वृश्चिक","धनु","मकर","कुम्भ","मीन"]

export const SIGN = { en:SIGN_ROMAN, ne:SIGN_DEVA, hi:SIGN_DEVA }
export const PLANET = {
  en:{Sun:"Sun",Moon:"Moon",Mars:"Mars",Mercury:"Mercury",Jupiter:"Jupiter",Venus:"Venus",Saturn:"Saturn",Rahu:"Rahu",Ketu:"Ketu"},
  ne:{Sun:"सूर्य",Moon:"चन्द्र",Mars:"मंगल",Mercury:"बुध",Jupiter:"गुरु",Venus:"शुक्र",Saturn:"शनि",Rahu:"राहु",Ketu:"केतु"},
  hi:{Sun:"सूर्य",Moon:"चंद्र",Mars:"मंगल",Mercury:"बुध",Jupiter:"गुरु",Venus:"शुक्र",Saturn:"शनि",Rahu:"राहु",Ketu:"केतु"},
}
export const ABBR = {
  en:{Sun:"Su",Moon:"Mo",Mars:"Ma",Mercury:"Me",Jupiter:"Ju",Venus:"Ve",Saturn:"Sa",Rahu:"Ra",Ketu:"Ke"},
  ne:{Sun:"सू",Moon:"च",Mars:"मं",Mercury:"बु",Jupiter:"गु",Venus:"शु",Saturn:"श",Rahu:"रा",Ketu:"के"},
  hi:{Sun:"सू",Moon:"चं",Mars:"मं",Mercury:"बु",Jupiter:"गु",Venus:"शु",Saturn:"श",Rahu:"रा",Ketu:"के"},
}
export const DIGNITY = {
  en:{"Exalted":"Exalted","Own sign":"Own sign","Friendly":"Friendly","Neutral":"Neutral","Enemy sign":"Enemy sign","Debilitated":"Debilitated","-":"—"},
  ne:{"Exalted":"उच्च","Own sign":"स्वगृही","Friendly":"मित्र","Neutral":"सम","Enemy sign":"शत्रु","Debilitated":"नीच","-":"—"},
  hi:{"Exalted":"उच्च","Own sign":"स्वगृही","Friendly":"मित्र","Neutral":"सम","Enemy sign":"शत्रु","Debilitated":"नीच","-":"—"},
}
export const TH = {
  en:["Graha","Rāśi","Degree","Dignity","Nakṣatra","Pada","D9","House"],
  ne:["ग्रह","राशि","अंश","बल","नक्षत्र","पाद","D9","भाव"],
  hi:["ग्रह","राशि","अंश","बल","नक्षत्र","पाद","D9","भाव"],
}
export const sign = (lang,romanName)=> SIGN[lang][SIGN_ROMAN.indexOf(romanName)] ?? romanName
export const signIdx = (romanName)=> SIGN_ROMAN.indexOf(romanName)

export const T = {
  en:{dob:"Date of Birth",tob:"Time of Birth",gen:"Reveal My Kuṇḍalī",chart:"The Chart",
    pos:"Planetary Positions",read:"Your Reading",purpose:"Your Life Purpose",timeline:"Major Life Predictions",
    dasha:"Vimśottarī Daśā",asc:"Ascendant (Lagna)",moon:"Moon Sign",sun:"Sun Sign",atma:"Soul Planet (Ātmakāraka)",
    nak:"Birth Nakṣatra",run:"Running Daśā",ayan:"Ayanāṁśa",north:"North Indian",south:"South Indian",d9:"Navāṁśa (D9)",
    d1cap:"Rāśi chart (D1)",d9cap:"Navāṁśa — soul, marriage & dharma",tlnote:"Each daśā period is a chapter of life. The current one is highlighted."},
  ne:{dob:"जन्म मिति",tob:"जन्म समय",gen:"मेरो कुण्डली हेर्नुहोस्",chart:"कुण्डली",
    pos:"ग्रह स्थिति",read:"तपाईंको फलादेश",purpose:"तपाईंको जीवन उद्देश्य",timeline:"प्रमुख जीवन भविष्यवाणी",
    dasha:"विंशोत्तरी दशा",asc:"लग्न",moon:"चन्द्र राशि",sun:"सूर्य राशि",atma:"आत्मग्रह (आत्मकारक)",
    nak:"जन्म नक्षत्र",run:"चालु दशा",ayan:"अयनांश",north:"उत्तर भारतीय",south:"दक्षिण भारतीय",d9:"नवांश (D9)",
    d1cap:"राशि कुण्डली (D1)",d9cap:"नवांश — आत्मा, विवाह र धर्म",tlnote:"प्रत्येक दशा जीवनको एक अध्याय हो। चालु दशा हाइलाइट गरिएको छ।"},
  hi:{dob:"जन्म तिथि",tob:"जन्म समय",gen:"मेरी कुंडली देखें",chart:"कुंडली",
    pos:"ग्रह स्थिति",read:"आपका फलादेश",purpose:"आपका जीवन उद्देश्य",timeline:"प्रमुख जीवन भविष्यवाणी",
    dasha:"विंशोत्तरी दशा",asc:"लग्न",moon:"चंद्र राशि",sun:"सूर्य राशि",atma:"आत्मग्रह (आत्मकारक)",
    nak:"जन्म नक्षत्र",run:"चालू दशा",ayan:"अयनांश",north:"उत्तर भारतीय",south:"दक्षिण भारतीय",d9:"नवांश (D9)",
    d1cap:"राशि कुंडली (D1)",d9cap:"नवांश — आत्मा, विवाह और धर्म",tlnote:"प्रत्येक दशा जीवन का एक अध्याय है। चालू दशा हाइलाइट है।"},
}
export const LOADING={en:"Aligning the heavens…",ne:"ग्रहहरू मिलाउँदै…",hi:"ग्रहों का मिलान…"}
