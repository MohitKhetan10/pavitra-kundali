import React,{useState} from 'react'
import { PLANET } from '../i18n.js'
const today=new Date().toISOString().slice(0,10)
const isNow=(a,b)=>a<=today&&today<=b

function Row({node,depth,children,defaultOpen,pl}){
  const[open,setOpen]=useState(defaultOpen||false)
  const has=!!children
  return <div>
    <div className={`drow${isNow(node.start,node.end)?' active':''}${open?' open':''}`}
      onClick={()=>has&&setOpen(o=>!o)} style={{paddingLeft:12+depth*16}}>
      <span className="caret">{has?'▸':''}</span>
      <span className="lord">{(pl&&pl[node.lord])||node.lord}</span>
      <span className="span">{node.start} → {node.end}</span>
      {isNow(node.start,node.end)&&<span className="now">now</span>}
    </div>
    {open&&has&&<div className="dnode">{children}</div>}
  </div>
}
export default function DashaTree({dasha,lang='en'}){
  const pl=PLANET[lang]
  return <div>
    <p style={{color:'var(--ink-dim)',fontStyle:'italic',marginBottom:14}}>
      Vimśottarī · balance at birth <b style={{color:'var(--gold-soft)'}}>{dasha.balance_years} yrs of {(pl&&pl[dasha.sequence[0].lord])||dasha.sequence[0].lord}</b>
      &nbsp;· running now: <b style={{color:'var(--saffron)'}}>{(pl&&pl[dasha.current])||dasha.current}</b> — tap a period to expand
    </p>
    {dasha.sequence.map(maha=>(
      <Row key={maha.lord+maha.start} node={maha} depth={0} pl={pl} defaultOpen={isNow(maha.start,maha.end)}>
        {maha.antar.map(an=>(
          <Row key={an.lord+an.start} node={an} depth={1} pl={pl} defaultOpen={isNow(an.start,an.end)}>
            {an.pratyantar.map(pr=>(<Row key={pr.lord+pr.start} node={pr} depth={2} pl={pl}/>))}
          </Row>))}
      </Row>))}
  </div>
}
