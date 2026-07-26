import React,{useState,useRef,useEffect} from 'react'
import { getChart } from './api.js'
import { T, LOADING, PLANET, sign } from './i18n.js'
import PlaceInput from './components/PlaceInput.jsx'
import { ChartNorth, ChartD1South, ChartD9 } from './components/charts.jsx'
import PlanetTable from './components/PlanetTable.jsx'
import Readings from './components/Readings.jsx'
import Analysis from './components/Analysis.jsx'
import Timeline from './components/Timeline.jsx'
import DashaTree from './components/DashaTree.jsx'
import ZodiacMandala from './components/ZodiacMandala.jsx'
import StarfieldCanvas from './components/StarfieldCanvas.jsx'

export default function App(){
  const[lang,setLang]=useState('en')
  const[form,setForm]=useState({dob:'1997-05-21',tob:'14:30',lat:27.7172,lon:85.3240,place:'Kathmandu, Nepal'})
  const[chart,setChart]=useState(null)
  const[loading,setLoading]=useState(false)
  const[error,setError]=useState('')
  const[tab,setTab]=useState('north')
  const resultsRef=useRef()
  const t=T[lang]

  useEffect(()=>{
    const io=new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting&&e.target.classList.add('in')),{threshold:.1})
    document.querySelectorAll('.reveal').forEach(el=>io.observe(el))
    return()=>io.disconnect()
  },[chart,lang])



  async function submit(){
    setError(''); setLoading(true); setChart(null)
    setTimeout(()=>resultsRef.current?.scrollIntoView({behavior:'smooth',block:'start'}),50)
    try{ setChart(await getChart({dob:form.dob,tob:form.tob,lat:Number(form.lat),lon:Number(form.lon)})) }
    catch(e){ setError(e.message) }
    finally{ setLoading(false) }
  }
  const set=(k,v)=>setForm(f=>({...f,[k]:v}))

  return <div className="app">
    <div className="sky"/>
    <StarfieldCanvas/>
    <header>
      <div className="mandala-wrap"><ZodiacMandala size={150}/></div>
      <h1 className="deva">पवित्र कुण्डली</h1>
      <div className="sub">Pavitra Kundali — know yourself through the stars</div>
      <div className="sys">Sidereal · Lahiri Ayanāṁśa</div>
      <div className="langbar">
        {[['en','English'],['ne','नेपाली'],['hi','हिन्दी']].map(([l,lbl])=>
          <button key={l} className={lang===l?'on':''} onClick={()=>setLang(l)}>{lbl}</button>)}
      </div>
    </header>

    <div className="card">
      <div className="form-grid">
        <div className="field"><label>{t.dob}</label>
          <input type="date" value={form.dob} onChange={e=>set('dob',e.target.value)}/></div>
        <div className="field"><label>{t.tob}</label>
          <input type="time" value={form.tob} onChange={e=>set('tob',e.target.value)}/></div>
        <PlaceInput value={form.place} onSelect={o=>setForm(f=>({...f,lat:o.lat,lon:o.lon,place:o.name}))}/>
        {error&&<div className="err">{error}</div>}
        <button className="btn" onClick={submit} disabled={loading}>{loading?LOADING[lang]:t.gen}</button>
      </div>
    </div>

    <div ref={resultsRef}/>
    {loading&&<div className="loading"><div className="orbit"/><p>{LOADING[lang]}</p></div>}

    {chart&&<>
      <div className="sec-title reveal"><h2 className="deva">{t.chart}</h2></div>
      <div className="grid-2">
        <div className="card reveal">
          <div className="tabs">
            <button className={tab==='north'?'on':''} onClick={()=>setTab('north')}>{t.north}</button>
            <button className={tab==='south'?'on':''} onClick={()=>setTab('south')}>{t.south}</button>
            <button className={tab==='d9'?'on':''} onClick={()=>setTab('d9')}>{t.d9}</button>
          </div>
          {tab==='north'&&<ChartNorth chart={chart} lang={lang}/>}
          {tab==='south'&&<ChartD1South chart={chart} lang={lang}/>}
          {tab==='d9'&&<ChartD9 chart={chart} lang={lang}/>}
          <div className="cap">{tab==='d9'?t.d9cap:t.d1cap}</div>
        </div>
        <div className="card summary reveal">
          <div className="row"><span className="k">{t.asc}</span><span className="v">{sign(lang,chart.ascendant.rashi)} <span className="g">{chart.ascendant.dms}</span></span></div>
          <div className="row"><span className="k">{t.moon}</span><span className="v">{sign(lang,chart.planets.Moon.rashi)}</span></div>
          <div className="row"><span className="k">{t.sun}</span><span className="v">{sign(lang,chart.planets.Sun.rashi)}</span></div>
          <div className="row"><span className="k">{t.atma}</span><span className="v"><span className="g">{PLANET[lang][chart.atmakaraka]}</span></span></div>
          <div className="row"><span className="k">{t.nak}</span><span className="v">{chart.moon_nakshatra} · {chart.planets.Moon.pada}</span></div>
          <div className="row"><span className="k">{t.run}</span><span className="v"><span className="g">{PLANET[lang][chart.dasha.current]}</span></span></div>
          <div className="row"><span className="k">{t.ayan}</span><span className="v">{chart.ayanamsa}°</span></div>
        </div>
      </div>

      <div className="sec-title reveal"><h2 className="deva">{t.purpose}</h2></div>
      <div className="purpose-card reveal"><span className="ic">🔯</span><p>{chart.readings[lang].purpose}</p></div>

      <div className="sec-title reveal"><h2 className="deva">{t.pos}</h2></div>
      <div className="card reveal"><PlanetTable planets={chart.planets} lang={lang}/></div>

      <div className="reveal"><Analysis chart={chart} lang={lang}/></div>

      <div className="sec-title reveal"><h2 className="deva">{t.read}</h2></div>
      <div className="card reveal"><Readings readings={chart.readings} lang={lang}/></div>

      <div className="sec-title reveal"><h2 className="deva">{t.timeline}</h2></div>
      <div className="card reveal"><p style={{color:'var(--ink-dim)',fontStyle:'italic',marginBottom:18}}>{t.tlnote}</p>
        <Timeline timeline={chart.timeline} lang={lang}/></div>

      <div className="sec-title reveal"><h2 className="deva">{t.dasha}</h2></div>
      <div className="card reveal"><DashaTree dasha={chart.dasha} lang={lang}/></div>
    </>}

    <footer><span className="om deva">ॐ</span>
      Pavitra Kundali · Sidereal · Lahiri ayanāṁśa · Swiss Ephemeris</footer>
  </div>
}
