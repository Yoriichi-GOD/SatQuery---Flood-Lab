# SatQuery · Flood Impact

Local IIT Mandi Track B workspace at http://localhost:8770. Original SatQuery remains on 8767. **Real Nepal evidence is available; full Track B completion is still pending.** No competition submission has been made.

## Run locally

Clone this repository, open PowerShell in its folder, and run `./start-demo.ps1`.
The launcher uses WSL distro `Ubuntu`. By default it expects the flood Python environment at `/root/satquery-flood-lab/venv` and the optional AI environment at `/root/satquery/.venv`. Set `SATQUERY_FLOOD_PYTHON_WSL` or `SATQUERY_AI_PYTHON_WSL` to override those interpreter paths.

Portable core setup: Python 3.11, install `requirements-lock.txt`, then run `python -m uvicorn floodlab.server:app --host 127.0.0.1 --port 8770`. Satellite and historical OSM acquisition require `CDSE_CLIENT_ID`, `CDSE_CLIENT_SECRET`, and `OHSOME_API_KEY` in Git-ignored `.env.local`. Never commit this file or paste credentials into reports. The AI worker additionally needs its pinned Qwen3 model and compatible Torch/Transformers runtime; see `docs/copilot-model.json`.

## Public repository contents

This repository includes source code, UI preview imagery, verification records, and report PDFs. It intentionally excludes acquired satellite rasters, historical OSM snapshots, frozen per-run payloads, and EMSR GRA reference GeoPackages. The event IDs in `docs/demo-script.md` refer to the locally verified demo workspace; a fresh clone will not contain those saved runs. Configure data access and acquire or prepare inputs locally before running a new analysis.
## Workspace workflow

Open **Analyze an area and date**, supply west/south/east/north coordinates and a past UTC flood date, then run. The bounded automatic path discovers a same-platform, same-orbit 12-day VV/VH pair, requests terrain-corrected SAR, validates scene identity and alignment, acquires a pre-event OSM snapshot, computes water candidates and infrastructure intersections, and freezes downloadable evidence. Progress reconnects after page reload; server interruption is reported as interrupted. Only one acquisition job runs at a time.

Maximum automatic area: one million 10 m pixels and 2500 pixels per side. No antimeridian support. Missing scene coverage and catalogue pagination fail closed. Automatic optical/debris proxy and historical road topology are connected and verified on a fresh Workspace API run. Empty access results do not mean no isolated settlements.

For the more complete prepared Nepal case, select `nepal-syapru-004`: SAR August 16/28, optical August 12/27, historical OSM July 27, 2026. It includes a debris proxy and a historical-node road graph. Settlement access remains unknown because of coverage/boundary and snapping limitations.

Use the copilot for evidence-backed English/Nepali answers. A local Qwen3-0.6B model selects a topic; templates insert saved calculations with source pointers. Topic selection scored 9/12 development questions before guardrails, not an independent benchmark. Select a topic explicitly when routing is wrong. Nepali wording needs human review.

## Evidence boundaries

Water baseline: VV below -17 dB after the event and a drop of at least 3 dB; fixed uncalibrated defaults. Two-date water is not proof of permanent water. Invalid pixels are excluded. All arrays load into RAM; pixelwise tiling tests do not validate tiled neural-network inference.

Debris proxy: vegetation loss to bare ground with SAR change. It can confuse clearing/agriculture and miss deposits on already bare ground. Diagnostic agreement with one EMSR927 landslide AOI: IoU 0.3279, F1 0.4939, recall 0.3285. Reference dates, resolution and class differ. This is not independent validated debris accuracy. Water accuracy has no compatible reference score.

EMSR damage labels remain evaluation-only and are not prediction inputs or threshold-tuning data. Their source GeoPackages are excluded from this public repository; registered filenames and SHA-256 digests remain in `docs/dataset-readiness.json`. Historical road nodes preserve crossings; turn restrictions are not modelled. Exposure does not establish damage, actual closures, casualties or evacuation instructions.

## Verification

Run `python -m pytest -q --junitxml=docs/test-results.xml --disable-warnings` in the flood environment. Latest machine test report is in `docs/test-results.xml`; live download checks are in `docs/live-verification.json`. Frozen results cannot overwrite existing run IDs. SHA-256 evidence hashes are downloadable with each run.

## Remaining acceptance work

- Validate on additional compatible independent events; current automatic success covers one Nepal rectangle.
- Browser interaction/layout, launcher, and full API workflow have been exercised.
- Independent validation, meaningful operational timings, Nepali review.
- One-page sitrep, two-page technical report, and full evidence report are rendered in output/pdf; record the 90-second demo.
- The owner authorized this public repository push. Organizer clearance for reused SatQuery components and submission authorization remain unconfirmed; no competition submission has been made.

Contains modified Copernicus Sentinel data 2026. Sentinel Data Legal Notice: https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice. Other sources: Copernicus DEM; © OpenStreetMap contributors (ODbL), historical extraction via HeiGIT/ohsome; Copernicus EMS reference products (evaluation only); Qwen/Qwen3-0.6B (Apache-2.0, pinned revision in model record). Retain source attribution and upstream license terms.
