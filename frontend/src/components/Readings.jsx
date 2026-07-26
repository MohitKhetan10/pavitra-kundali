import React from 'react'
const SEC={
  purpose:{ic:'\u{1F52F}',en:'Your Life Purpose',ne:'जीवन उद्देश्य',hi:'जीवन उद्देश्य'},
  personality:{ic:'\u{1F9D8}',en:'Personality & Character',ne:'व्यक्तित्व र स्वभाव',hi:'व्यक्तित्व और स्वभाव'},
  career:{ic:'\u{1F4BC}',en:'Career & Wealth',ne:'करियर र धन',hi:'करियर और धन'},
  relationships:{ic:'\u{1F495}',en:'Relationships & Marriage',ne:'सम्बन्ध र विवाह',hi:'संबंध और विवाह'},
  health:{ic:'\u{1F33F}',en:'Health & Wellbeing',ne:'स्वास्थ्य र कल्याण',hi:'स्वास्थ्य और कल्याण'},
  strengths:{ic:'\u{2728}',en:'Strengths & Challenges',ne:'शक्ति र चुनौती',hi:'शक्ति और चुनौती'},
  remedies:{ic:'\u{1FA94}',en:'Remedies (Upāya)',ne:'उपाय',hi:'उपाय'},
}
const ORDER=['personality','career','relationships','health','strengths','remedies']
export default function Readings({readings,lang}){
  const r=readings[lang]
  return <div>{ORDER.map(k=>(
    <div className={`reading ${k}`} key={k}>
      <h3><span className="ic">{SEC[k].ic}</span>{SEC[k][lang]}</h3>
      <p>{r[k]}</p>
    </div>))}</div>
}
