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

async def _photon(q):
    """Photon (Komoot) — free, no key, built for autocomplete. Covers worldwide places."""
    url = "https://photon.komoot.io/api/"
    params = {"q": q, "limit": 8}
    async with httpx.AsyncClient(timeout=8) as client:
        r = await client.get(url, params=params, headers={"User-Agent": "PavitraKundali/2.0"})
        r.raise_for_status()
        data = r.json()
    out = []
    for f in data.get("features", []):
        c = f.get("geometry", {}).get("coordinates")
        p = f.get("properties", {})
        if not c or len(c) < 2:
            continue
        lon, lat = float(c[0]), float(c[1])
        parts = [p.get("name"), p.get("city") or p.get("county"), p.get("state"), p.get("country")]
        name = ", ".join([x for x in parts if x])
        if not name:
            continue
        out.append({"lat": lat, "lon": lon, "name": name})
    return out

async def _nominatim(q):
    """Fallback geocoder."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": q, "format": "json", "limit": 8, "addressdetails": 1}
    async with httpx.AsyncClient(timeout=8) as client:
        r = await client.get(url, params=params, headers={"User-Agent": "PavitraKundali/2.0 (birth-chart app)"})
        r.raise_for_status()
        rows = r.json()
    return [{"lat": float(x["lat"]), "lon": float(x["lon"]), "name": x["display_name"]} for x in rows]

@app.get("/api/geocode")
async def geocode(q: str = Query(..., min_length=2)):
    """Place autocomplete — Photon first, Nominatim fallback. Adds timezone. Worldwide coverage."""
    rows = []
    try:
        rows = await _photon(q)
    except Exception:
        rows = []
    if not rows:
        try:
            rows = await _nominatim(q)
        except Exception as e:
            raise HTTPException(502, f"Geocoding unavailable: {e}")
    out = []
    seen = set()
    for row in rows:
        key = (round(row["lat"], 3), round(row["lon"], 3))
        if key in seen:
            continue
        seen.add(key)
        try:
            tzname = _tz_name(row["lat"], row["lon"])
        except Exception:
            tzname = "UTC"
        out.append({"name": row["name"], "lat": row["lat"], "lon": row["lon"], "tz_name": tzname})
    return {"results": out}

@app.post("/api/chart")
def chart(req: ChartRequest):
    try:
        tz = req.tz
        if tz is None:
            _, tz = offset_for(req.lat, req.lon, req.dob, req.tob)
        data = compute_chart(req.dob, req.tob, req.lat, req.lon, tz)
        data["resolved_tz"] = tz
        data["readings"] = build_readings(data)
        data["timeline"] = build_timeline(data)
        data["yogas_i18n"] = build_yogas(data)
        return data
    except Exception as e:
        raise HTTPException(400, f"Calculation error: {e}")
