"""Pavitra Kundali API — FastAPI wrapper around the verified Jyotish engine."""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from zoneinfo import ZoneInfo
import httpx

from jyotish import compute_chart
from interpret import build_readings, build_timeline, build_yogas

app = FastAPI(title="Pavitra Kundali API", version="2.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

_tf = None
def _tz_name(lat, lon):
    """Resolve IANA timezone from coordinates (lazy import; safe fallback to UTC)."""
    global _tf
    try:
        if _tf is None:
            from timezonefinder import TimezoneFinder
            _tf = TimezoneFinder()
        return _tf.timezone_at(lat=lat, lng=lon) or "UTC"
    except Exception:
        return "UTC"

def offset_for(lat, lon, dob, tob):
    """Historical UTC offset (hours) for a birth moment — respects old DST/rule changes."""
    tzname = _tz_name(lat, lon)
    y,mo,d = map(int, dob.split("-")); hh,mm = map(int, tob.split(":"))
    dt = datetime(y,mo,d,hh,mm, tzinfo=ZoneInfo(tzname))
    return tzname, dt.utcoffset().total_seconds()/3600.0

class ChartRequest(BaseModel):
    dob: str = Field(..., example="1997-05-21")
    tob: str = Field(..., example="14:30")
    lat: float = Field(..., example=27.7172)
    lon: float = Field(..., example=85.3240)
    tz:  Optional[float] = Field(None, description="Explicit UTC offset. If omitted, resolved from lat/lon + date.")

@app.get("/")
def root():
    return {"service":"Pavitra Kundali API","system":"Sidereal / Lahiri (Chitrapaksha)","status":"ok"}

@app.get("/api/geocode")
async def geocode(q: str = Query(..., min_length=2)):
    """Place autocomplete via OpenStreetMap Nominatim (free, no key). Adds timezone name."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": q, "format": "json", "limit": 6, "addressdetails": 1}
    headers = {"User-Agent": "PavitraKundali/2.0 (birth-chart app)"}
    try:
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(url, params=params, headers=headers)
            r.raise_for_status()
            rows = r.json()
    except Exception as e:
        raise HTTPException(502, f"Geocoding unavailable: {e}")
    out = []
    for row in rows:
        lat, lon = float(row["lat"]), float(row["lon"])
        try:
            tzname = _tz_name(lat, lon)
        except Exception:
            tzname = "UTC"
        out.append({"name": row["display_name"], "lat": lat, "lon": lon, "tz_name": tzname})
    return {"results": out}

@app.post("/api/chart")
def chart(req: ChartRequest):
