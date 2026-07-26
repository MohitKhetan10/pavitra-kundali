# Pavitra Kundali 2.0 — पवित्र कुण्डली

A Vedic (Jyotish) self-knowledge platform. Enter birth details, get a complete,
correctly-calculated chart with readings in **English, Nepali and Hindi**.

**System:** Sidereal / nirāyana zodiac, **Lahiri (Chitrapaksha) ayanāṁśa** — the modern
Jyotish standard. Powered by **Swiss Ephemeris** (Moshier mode: arc-second accuracy, no
data files). Verified: Lahiri @ J2000 = 23.857° ✓; sidereal Sun enters Meṣa 13–14 Apr
(Meṣa Saṅkrānti) ✓; India-independence chart returns its documented Vṛṣabha Lagna ✓.

## Why the old site was wrong
It computed **tropical** positions instead of **sidereal**, shifting every planet ~24°
into the wrong rāśi. This version applies Lahiri ayanāṁśa correctly.

## Features
- Three charts: **North Indian**, **South Indian**, and **Navāṁśa (D9)**
- All nine grahas: sidereal degree, rāśi, nakṣatra + pada, retrograde, **dignity**, D9 sign
- Ascendant (Lagna) and whole-sign houses
- Six trilingual readings: personality, career & wealth, relationships, health,
  strengths & challenges, remedies — rule-based, offline, no API
- **Multi-level Vimśottarī Daśā** (Mahā → Antar → Pratyantar) with exact dates, expandable
- Analysis: planetary aspects (dṛṣṭi), core yogas, Sāde Sātī, Maṅgal dosha, nakṣatra deep-dive
- Place autocomplete (OpenStreetMap Nominatim) with **historical-DST timezone** resolution
- Cosmic-observatory UI, animated starfield, language toggle, scroll-into-results

## Run locally
### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000               # docs at /docs
```
### Frontend
```bash
cd frontend
npm install
cp .env.example .env        # set VITE_API_URL if backend isn't on localhost:8000
npm run dev
```

## Deploy (later, per your plan)
- **Frontend → Netlify:** build `npm run build`, publish `dist`, set `VITE_API_URL`.
- **Backend → Render/Railway (free):** start `uvicorn main:app --host 0.0.0.0 --port $PORT`.
  Netlify can't host Python, so FastAPI lives here; the Netlify site calls it.
  First request may cold-start on free tiers.
- After deploy, set CORS `allow_origins` in `main.py` to your Netlify domain.
- Nominatim is free but rate-limited (~1 req/sec) and asks for a real User-Agent — fine
  for this traffic; swap to a paid geocoder only if you scale up.

## Notes & scope
- No user data is stored anywhere (on-page only).
- Rāhu = mean node (Jyotish default); Ketu = Rāhu + 180°. Houses = whole-sign (Parāśarī).
- Yogas cover a correct **core set** (Gaja-Kesari, Budha-Āditya, Pañca-Mahāpuruṣa,
  Kemadruma with cancellation). Strength uses **dignity**; full numerical Ṣaḍbala can be
  added later. Health readings are traditional tendencies, not medical advice.
