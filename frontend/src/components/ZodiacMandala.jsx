import React from 'react'
// 12 rāśi glyphs, Aries at top, clockwise
const GLYPHS=['\u2648','\u2649','\u264A','\u264B','\u264C','\u264D','\u264E','\u264F','\u2650','\u2651','\u2652','\u2653']
export default function ZodiacMandala({size=150}){
  const R=46, rGlyph=39, rInner=30, cx=50, cy=50
  return (
    <svg className="mandala" width={size} height={size} viewBox="0 0 100 100"
         fill="none" stroke="currentColor" role="img" aria-label="Zodiac wheel">
      <circle cx={cx} cy={cy} r={R} strokeWidth="1.1"/>
      <circle cx={cx} cy={cy} r={rInner} strokeWidth="0.8" opacity="0.7"/>
      <circle cx={cx} cy={cy} r="6" strokeWidth="1"/>
      {/* spokes dividing the 12 houses */}
      {Array.from({length:12}).map((_,i)=>{
        const a=(i*30-90)*Math.PI/180
        return <line key={'s'+i}
          x1={cx+rInner*Math.cos(a)} y1={cy+rInner*Math.sin(a)}
          x2={cx+R*Math.cos(a)} y2={cy+R*Math.sin(a)} strokeWidth="0.7" opacity="0.6"/>
      })}
      {/* sign glyphs sitting in each segment */}
      {GLYPHS.map((g,i)=>{
        const a=(i*30-90+15)*Math.PI/180
        const x=cx+rGlyph*Math.cos(a), y=cy+rGlyph*Math.sin(a)
        return <text key={'g'+i} x={x} y={y+3} textAnchor="middle"
          fill="currentColor" stroke="none" fontSize="6.6"
          style={{fontFamily:'serif'}}>{g}</text>
      })}
      {/* central bindu / spark */}
      <circle cx={cx} cy={cy} r="1.6" fill="currentColor" stroke="none"/>
    </svg>
  )
}
