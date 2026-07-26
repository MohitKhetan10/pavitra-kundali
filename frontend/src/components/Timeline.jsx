import React from 'react'
import { PLANET } from '../i18n.js'
const today=new Date().toISOString().slice(0,10)
export default function Timeline({timeline,lang}){
  const rows=timeline[lang]||[]
  const pl=PLANET[lang]
  return <div className="timeline">
    {rows.map((r,i)=>{const now=r.start<=today&&today<=r.end
      return <div className={`tl-chapter${now?' now':''}`} key={i}>
        <div className="tl-head"><span className="tl-lord">{pl[r.lord]}</span>
          <span className="tl-span">{r.start} → {r.end}</span>
          {now&&<span className="tl-now">now</span>}</div>
        <p>{r.text}</p>
      </div>})}
  </div>
}
