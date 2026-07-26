import React from 'react'
import { PLANET, sign } from '../i18n.js'
const L={
  en:{flags:'Key Indicators',nak:'Birth Nakṣatra',yogas:'Yogas',aspects:'Planetary Aspects (Dṛṣṭi)',
      manglik:'Maṅgal Dosha',sade:'Sāde Sātī',present:'Present',absent:'Absent',active:'Active',inactive:'Inactive',
      house:'house',casts:'aspects houses',deity:'Deity',symbol:'Symbol',gana:'Gaṇa',nature:'Nature',
      none:'No major yogas in the core set.'},
  ne:{flags:'मुख्य सङ्केत',nak:'जन्म नक्षत्र',yogas:'योग',aspects:'ग्रह दृष्टि',
      manglik:'मंगल दोष',sade:'साढेसाती',present:'छ',absent:'छैन',active:'सक्रिय',inactive:'निष्क्रिय',
      house:'भाव',casts:'भावमा दृष्टि',deity:'देवता',symbol:'चिन्ह',gana:'गण',nature:'स्वभाव',none:'मुख्य योग भेटिएन।'},
  hi:{flags:'मुख्य संकेत',nak:'जन्म नक्षत्र',yogas:'योग',aspects:'ग्रह दृष्टि',
      manglik:'मंगल दोष',sade:'साढ़ेसाती',present:'है',absent:'नहीं',active:'सक्रिय',inactive:'निष्क्रिय',
      house:'भाव',casts:'भावों पर दृष्टि',deity:'देवता',symbol:'चिन्ह',gana:'गण',nature:'स्वभाव',none:'मुख्य योग नहीं मिले।'},
}
export default function Analysis({chart,lang}){
  const t=L[lang], pl=PLANET[lang], nd=chart.nak_detail
  const yogas=(chart.yogas_i18n&&chart.yogas_i18n[lang])||[]
  return <div>
    <div className="sec-title"><h2 className="deva">{t.flags}</h2></div>
    <div className="flags">
      <div className="flag"><div className="t">{t.manglik}</div>
        <div className={`s ${chart.mangal_dosha.present?'on':'off'}`}>{chart.mangal_dosha.present?t.present:t.absent}</div>
        <div className="note">{pl.Mars} · {t.house} {chart.mangal_dosha.mars_house}</div></div>
      <div className="flag"><div className="t">{t.sade}</div>
        <div className={`s ${chart.sade_sati.active?'on':'off'}`}>{chart.sade_sati.active?t.active:t.inactive}</div>
        <div className="note">{pl.Saturn} · {sign(lang,chart.sade_sati.saturn_sign)}</div></div>
    </div>
    <div className="sec-title"><h2 className="deva">{t.nak}</h2></div>
    <div className="card">
      <h3 style={{color:'var(--gold-soft)',fontFamily:'Marcellus',fontSize:'1.4rem',marginBottom:10}}>
        {chart.moon_nakshatra} · pada {chart.planets.Moon.pada}</h3>
      {nd&&nd.deity&&<div className="summary">
        <div className="row"><span className="k">{t.deity}</span><span className="v">{nd.deity}</span></div>
        <div className="row"><span className="k">{t.symbol}</span><span className="v">{nd.symbol}</span></div>
        <div className="row"><span className="k">{t.gana}</span><span className="v">{nd.gana}</span></div>
        <div className="row"><span className="k">{t.nature}</span><span className="v">{nd.trait}</span></div>
      </div>}
    </div>
    <div className="sec-title"><h2 className="deva">{t.yogas}</h2></div>
    <div>{yogas.length?yogas.map((y,i)=>(
      <div key={i} className={`yoga${y.good?'':' bad'}`}><div className="n">{y.name}</div><div className="d">{y.desc}</div></div>
    )):<p style={{color:'var(--ink-dim)',fontStyle:'italic'}}>{t.none}</p>}</div>
    <div className="sec-title"><h2 className="deva">{t.aspects}</h2></div>
    <div className="card"><table><tbody>
      {chart.aspects.map(a=>(<tr key={a.planet}>
        <td style={{fontFamily:'Marcellus',color:'var(--gold-soft)',width:120}}>{pl[a.planet]}</td>
        <td style={{color:'var(--ink-dim)'}}>{t.casts}: {a.aspects_houses.join(', ')}</td>
      </tr>))}
    </tbody></table></div>
  </div>
}
