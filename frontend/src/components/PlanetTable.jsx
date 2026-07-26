import React from 'react'
import { PLANET, SIGN, DIGNITY, TH, sign } from '../i18n.js'
const ORDER=['Sun','Moon','Mars','Mercury','Jupiter','Venus','Saturn','Rahu','Ketu']
const GLYPH={Sun:'\u2609',Moon:'\u263D',Mars:'\u2642',Mercury:'\u263F',Jupiter:'\u2643',
  Venus:'\u2640',Saturn:'\u2644',Rahu:'\u260A',Ketu:'\u260B'}
const dgClass=(d)=>({'Exalted':'dg-Exalted','Own sign':'dg-Own','Debilitated':'dg-Debilitated','Enemy sign':'dg-Enemy'}[d]||'')
export default function PlanetTable({planets,lang}){
  const th=TH[lang], pl=PLANET[lang]
  return <table><thead><tr>{th.map(h=><th key={h}>{h}</th>)}</tr></thead><tbody>
    {ORDER.map(n=>{const p=planets[n];return <tr key={n}>
      <td>{GLYPH[n]} {pl[n]} {p.retro&&<span className="retro-tag">℞</span>}</td>
      <td>{sign(lang,p.rashi)}</td>
      <td style={{color:'var(--gold-soft)'}}>{p.dms}</td>
      <td className={dgClass(p.dignity)}>{DIGNITY[lang][p.dignity]}</td>
      <td>{p.nakshatra}</td>
      <td><span className="pill">{p.pada}</span></td>
      <td style={{color:'var(--ink-dim)'}}>{sign(lang,p.navamsa)}</td>
      <td>{p.house}</td>
    </tr>})}
  </tbody></table>
}
