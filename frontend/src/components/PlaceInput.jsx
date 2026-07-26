import React,{useState,useRef} from 'react'
import { geocode } from '../api.js'
export default function PlaceInput({value,onSelect}){
  const[q,setQ]=useState(value||'')
  const[opts,setOpts]=useState([])
  const[open,setOpen]=useState(false)
  const timer=useRef()
  function change(v){
    setQ(v); setOpen(true)
    clearTimeout(timer.current)
    if(v.length<3){setOpts([]);return}
    timer.current=setTimeout(async()=>{
      try{ setOpts(await geocode(v)) }catch{ setOpts([]) }
    },350)
  }
  function pick(o){
    setQ(o.name.split(',').slice(0,3).join(', ')); setOpen(false)
    onSelect(o)
  }
  return <div className="field full">
    <label>Place of Birth</label>
    <input value={q} placeholder="Start typing a city… e.g. Kathmandu"
      onChange={e=>change(e.target.value)} onFocus={()=>q.length>=3&&setOpen(true)}/>
    {open&&opts.length>0&&<div className="ac">
      {opts.map((o,i)=><div key={i} onClick={()=>pick(o)}>{o.name}</div>)}
    </div>}
  </div>
}
