import React from 'react'
import { ABBR, signIdx } from '../i18n.js'

const NPOS={1:[200,95],2:[100,45],3:[45,100],4:[100,200],5:[45,300],6:[100,355],
  7:[200,300],8:[300,355],9:[355,300],10:[300,200],11:[355,100],12:[300,45]}

export function ChartNorth({ chart, lang }){
  const ab=ABBR[lang]||ABBR.en
  const lagna=chart.ascendant.rashi_num
  const hSign=(h)=>((lagna-1+(h-1))%12)+1
  const byH={}
  Object.entries(chart.planets).forEach(([n,p])=>(byH[p.house]||=[]).push([n,p]))
  return <svg className="chart-svg" viewBox="0 0 400 400">
    <rect x="2" y="2" width="396" height="396" rx="4"/>
    <line x1="2" y1="2" x2="398" y2="398"/><line x1="398" y1="2" x2="2" y2="398"/>
    <line x1="200" y1="2" x2="398" y2="200"/><line x1="398" y1="200" x2="200" y2="398"/>
    <line x1="200" y1="398" x2="2" y2="200"/><line x1="2" y1="200" x2="200" y2="2"/>
    {Array.from({length:12},(_,i)=>i+1).map(h=>{const[x,y]=NPOS[h];const pls=byH[h]||[]
      return <g key={h}>
        <text className="sign-num" x={x} y={y-12} textAnchor="middle">{hSign(h)}</text>
        {h===1&&<text className="la" x={x} y={y+1} textAnchor="middle">La</text>}
        {pls.map(([n,p],i)=><text key={n} className={`pl${p.retro?' retro':''}`} x={x} y={y+15+i*14}
          textAnchor="middle">{ab[n]}{p.retro?'\u1d3f':''}</text>)}
      </g>})}
  </svg>
}

const SPOS={11:[0,0],0:[1,0],1:[2,0],2:[3,0],10:[0,1],3:[3,1],9:[0,2],4:[3,2],8:[0,3],7:[1,3],6:[2,3],5:[3,3]}
function ChartSouth({ signMap, lagnaSign, lang }){
  const ab=ABBR[lang]||ABBR.en
  return <svg className="chart-svg" viewBox="0 0 400 400">
    <rect x="2" y="2" width="396" height="396" rx="4"/>
    {[1,2,3].map(i=><line key={'v'+i} x1={i*100} y1="2" x2={i*100} y2="398"/>)}
    {[1,2,3].map(i=><line key={'h'+i} x1="2" y1={i*100} x2="398" y2={i*100}/>)}
    {Object.entries(SPOS).map(([si,[c,r]])=>{const s=Number(si);const x=c*100,y=r*100;const pls=signMap[s]||[]
      return <g key={si}>
        <text className="sign-num" x={x+8} y={y+18}>{s+1}</text>
        {s===lagnaSign&&<text className="la" x={x+90} y={y+18} textAnchor="end">La</text>}
        {pls.map(([n,p],i)=><text key={n} className={`pl${p&&p.retro?' retro':''}`} x={x+50} y={y+40+i*15}
          textAnchor="middle">{ab[n]}{p&&p.retro?'\u1d3f':''}</text>)}
      </g>})}
  </svg>
}
export function ChartD1South({ chart, lang }){
  const map={}; Object.entries(chart.planets).forEach(([n,p])=>(map[p.rashi_num-1]||=[]).push([n,p]))
  return <ChartSouth signMap={map} lagnaSign={chart.ascendant.rashi_num-1} lang={lang}/>
}
export function ChartD9({ chart, lang }){
  const map={}; Object.entries(chart.planets).forEach(([n,p])=>(map[signIdx(p.navamsa)]||=[]).push([n,p]))
  return <ChartSouth signMap={map} lagnaSign={signIdx(chart.ascendant.navamsa)} lang={lang}/>
}
