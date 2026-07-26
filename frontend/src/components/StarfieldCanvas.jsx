import React,{useRef,useEffect} from 'react'
// Interactive canvas starfield: parallax by depth, stars flee the cursor, comet trail follows.
export default function StarfieldCanvas(){
  const ref=useRef()
  useEffect(()=>{
    if(matchMedia('(prefers-reduced-motion: reduce)').matches) return
    const cv=ref.current, ctx=cv.getContext('2d')
    let W,H,dpr,stars,raf
    const mouse={x:-1e4,y:-1e4,px:-1e4,py:-1e4,active:false}
    const trail=[]
    function resize(){
      dpr=Math.min(devicePixelRatio||1,2)
      W=cv.width=innerWidth*dpr; H=cv.height=innerHeight*dpr
      cv.style.width=innerWidth+'px'; cv.style.height=innerHeight+'px'
      const n=Math.round(innerWidth*innerHeight/6500)
      stars=Array.from({length:n},()=>{
        const depth=Math.random()   // 0 far … 1 near
        return {x:Math.random()*W,y:Math.random()*H,z:depth,
          r:(depth*1.6+0.3)*dpr, base:Math.random()*0.5+0.4,
          tw:Math.random()*Math.PI*2, hue:Math.random()<0.15?'gold':'white',
          vx:0,vy:0}
      })
    }
    function onMove(e){
      mouse.px=mouse.x; mouse.py=mouse.y
      mouse.x=e.clientX*dpr; mouse.y=e.clientY*dpr; mouse.active=true
      trail.push({x:mouse.x,y:mouse.y,life:1})
      if(trail.length>26) trail.shift()
    }
    function onLeave(){mouse.active=false}
    let t=0
    function frame(){
      raf=requestAnimationFrame(frame); t+=0.016
      ctx.clearRect(0,0,W,H)
      const cx=W/2, cy=-H*0.05
      // ambient parallax toward cursor
      const ox=mouse.active?(mouse.x-W/2)*0.012:0
      const oy=mouse.active?(mouse.y-H/2)*0.012:0
      for(const s of stars){
        // repulsion from cursor
        if(mouse.active){
          const dx=s.x-mouse.x, dy=s.y-mouse.y, d2=dx*dx+dy*dy
          const R=150*dpr
          if(d2<R*R){
            const d=Math.sqrt(d2)||1, f=(1-d/R)*2.4*dpr
            s.vx+=dx/d*f; s.vy+=dy/d*f
          }
        }
        s.vx*=0.9; s.vy*=0.9
        s.x+=s.vx; s.y+=s.vy
        // ease back toward home drift
        s.x-=s.vx*0.02; s.y-=s.vy*0.02
        const px=s.x+ox*s.z*6, py=s.y+oy*s.z*6
        const tw=s.base+Math.sin(t*1.5+s.tw)*0.35
        ctx.beginPath()
        ctx.arc(px,py,s.r,0,7)
        ctx.fillStyle = s.hue==='gold'
          ? `rgba(236,210,138,${Math.max(0,tw)})`
          : `rgba(255,255,255,${Math.max(0,tw)})`
        if(s.z>0.75){ctx.shadowColor='rgba(200,190,255,.9)';ctx.shadowBlur=6*dpr}else ctx.shadowBlur=0
        ctx.fill()
      }
      ctx.shadowBlur=0
      // comet trail following cursor
      for(let i=0;i<trail.length;i++){
        const p=trail[i]; p.life*=0.9
        const rad=(i/trail.length)*6*dpr+1
        ctx.beginPath(); ctx.arc(p.x,p.y,rad,0,7)
        ctx.fillStyle=`rgba(150,130,255,${p.life*0.5*(i/trail.length)})`
        ctx.fill()
      }
      // glowing head
      if(mouse.active){
        const g=ctx.createRadialGradient(mouse.x,mouse.y,0,mouse.x,mouse.y,120*dpr)
        g.addColorStop(0,'rgba(160,140,255,.18)')
        g.addColorStop(.5,'rgba(236,210,138,.06)')
        g.addColorStop(1,'transparent')
        ctx.fillStyle=g; ctx.fillRect(mouse.x-120*dpr,mouse.y-120*dpr,240*dpr,240*dpr)
      }
    }
    resize(); frame()
    addEventListener('resize',resize)
    addEventListener('mousemove',onMove,{passive:true})
    addEventListener('mouseout',onLeave)
    addEventListener('touchmove',e=>{if(e.touches[0])onMove(e.touches[0])},{passive:true})
    return()=>{cancelAnimationFrame(raf);removeEventListener('resize',resize)
      removeEventListener('mousemove',onMove);removeEventListener('mouseout',onLeave)}
  },[])
  return <canvas ref={ref} className="starfield"/>
}
