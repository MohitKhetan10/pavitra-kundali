const BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function getChart(payload) {
  const res = await fetch(`${BASE}/api/chart`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
  if (!res.ok) {
    const e = await res.json().catch(() => ({ detail: 'Request failed' }))
    throw new Error(e.detail || 'Could not calculate the chart')
  }
  return res.json()
}

export async function geocode(q) {
  const res = await fetch(`${BASE}/api/geocode?q=${encodeURIComponent(q)}`)
  if (!res.ok) throw new Error('Place search unavailable')
  const d = await res.json()
  return d.results || []
}
