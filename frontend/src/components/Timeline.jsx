import React,{useState} from 'react'
import { PLANET } from '../i18n.js'
const today=new Date().toISOString().slice(0,10)
const AREA={
  en:{career:'Career',wealth:'Wealth',relationships:'Relationships',health:'Health',mind:'Mind & Spirit',more:'View life-area breakdown',less:'Hide breakdown'},
  ne:{career:'करियर',wealth:'धन',relationships:'सम्बन्ध',health:'स्वास्थ्य',mind:'मन र आत्मा',more:'जीवन-क्षेत्र विवरण हेर्नुहोस्',less:'विवरण लुकाउनुहोस्'},
  hi:{career:'करियर',wealth:'धन',relationships:'संबंध',health:'स्वास्थ्य',mind:'मन व आत्मा',more:'जीवन-क्षेत्र विवरण देखें',less:'विवरण छिपाएँ'},
}
const ICON={career:'\u{1F4BC}',wealth:'\u{1F4B0}',relationships:'\u{1F495}',health:'\u{1F33F}',mind:'\u{1F9D8}'}
const ORDER=['career','wealth','relationships','health','mind']

function Chapter({r,lang,defaultOpen}){
  const[open,setOpen]=useState(defaultOpen)
  const A=AREA[lang], pl=PLANET[lang]
  const now=r.start<=today&&today<=r.end
  return <div className={`tl-chapter${now?' now':''}`}>
    <div className="tl-head">
      <span className="tl-lord">{pl[r.lord]}</span>
      <span className="tl-span">{r.start} → {r.end}</span>
      {now&&<span className="tl-now">now</span>}
    </div>
    <p>{r.summary}</p>
    <button className="tl-toggle" onClick={()=>setOpen(o=>!o)}>{open?A.less:A.more}</button>
    {open&&<div className="tl-aspects">
      {ORDER.map(k=>(
        <div className="tl-aspect" key={k}>
          <span className="tl-aspect-label">{ICON[k]} {A[k]}</span>
          <span className="tl-aspect-text">{r.aspects[k]}</span>
        </div>))}
    </div>}
  </div>
}
export default function Timeline({timeline,lang}){
  const rows=timeline[lang]||[]
  return <div className="timeline">
    {rows.map((r,i)=><Chapter key={i} r={r} lang={lang} defaultOpen={r.start<=today&&today<=r.end}/>)}
  </div>
}
