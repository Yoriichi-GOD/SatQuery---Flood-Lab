# Run Flood Lab locally

[Home](../../README.md) · [Walkthrough](REVIEWER_WALKTHROUGH.md) · [Architecture](ARCHITECTURE.md) · [Evidence](EVIDENCE.md)

The repository includes code, preview imagery, reports and saved verification records. It excludes `data/`, `artifacts/`, evaluation GeoPackages, model weights and credentials. A new clone starts without the saved Nepal analyses shown in the screenshots.

## Python setup

Use Python **3.11**. The verified host uses 3.11.16 in Ubuntu WSL. From the repository root, activation is optional because each command names the environment interpreter.

```powershell
git clone https://github.com/Yoriichi-GOD/SatQuery---Flood-Lab.git
Set-Location SatQuery---Flood-Lab
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m pip install pyarrow==26.0.0
.\.venv\Scripts\python.exe -m uvicorn floodlab.server:app --host 127.0.0.1 --port 8770
```

Open **http://localhost:8770/**. The last command stays in the foreground; **Ctrl+C** stops it. An empty Saved analysis menu is expected until a run is prepared/acquired. The health endpoint is `http://localhost:8770/api/health`; its `real_event_complete: false` reflects the open scientific acceptance boundary.

Linux/WSL equivalent:

```bash
python3.11 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python -m pip install pyarrow==26.0.0
.venv/bin/python -m uvicorn floodlab.server:app --host 127.0.0.1 --port 8770
```

**Dependency boundary:** the historical lockfile omits `pyarrow`, which acquisition/topology imports. The supplement matches the installed version used for this review. The lockfile is preserved. Installation into an empty environment and native Windows geospatial wheel compatibility have **not** been verified here. App/tests ran in the existing WSL environment. Report generation has separate dependencies; shipped PDFs can be reviewed directly.

## Offline example

This is an **invented bridge-cut fixture**, not Nepal imagery or an accuracy benchmark. It requires no account, model or GPU. In a second terminal at the repository root:

```powershell
.\.venv\Scripts\python.exe -m floodlab.fixture data/reviewer-fixture
.\.venv\Scripts\python.exe -m floodlab.pipeline data/reviewer-fixture/manifest.json artifacts/runs/reviewer-fixture
```

Linux/WSL:

```bash
.venv/bin/python -m floodlab.fixture data/reviewer-fixture
.venv/bin/python -m floodlab.pipeline data/reviewer-fixture/manifest.json artifacts/runs/reviewer-fixture
```

Refresh the browser and select `reviewer-fixture`. Expected values: **32 candidate pixels / 3,200 m²**, one intersected building, **40 m** of intersected road and one potentially cut-off **synthetic** settlement. Optical choices are unavailable for this fixture. Outputs and inputs are written to the ignored locations above.

Use a new input directory and run ID for a repeat. Completed output directories cannot be overwritten. Do not generate fixtures into historical datasets or frozen runs.

## Real area/date requests

Create Git-ignored `.env.local` in the repository root with your own values:

```dotenv
CDSE_CLIENT_ID=your-client-id
CDSE_CLIENT_SECRET=your-client-secret
OHSOME_API_KEY=your-api-key
```

Acquisition reads this file directly; browser login alone is insufficient. Configure a [Copernicus Sentinel Hub OAuth client](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview/Authentication.html) and [HeiGIT/ohsome access](https://docs.ohsome.org/ohsome-api/). Access, quotas and availability are external dependencies.

In **Analyze an area and date**, supply west, south, east, north in longitude/latitude degrees and a past UTC event date. Historical Syapru bounds: `85.3232, 28.1491, 85.3483, 28.1882`; date `2026-08-26`. This identifies the saved case; retrieval today is not guaranteed.

The Workspace path discovers SAR scenes, obtains provider processing, requests pre-event OSM, builds topology, checks optical coverage, calculates exposure and freezes exports. It runs one job at a time. Limits: one million 10 m pixels, 2,500 pixels per side, no antimeridian support. A failed stage must not be read as completed analysis. Authenticated acquisitions were not rerun for this documentation update.

## Optional AI and PowerShell launcher

**Explicit topics** work without a model: select Water, Buildings, Roads, Settlement access, Situation report or Limitations, then Ask. Values come from frozen results.

**AI selects topic** requires port **8771**. The implementation uses a pinned local Qwen3-0.6B snapshot, Torch/Transformers and CUDA device 0 with BF16. These dependencies are absent from the core lockfile. The model path is host-specific in [ai_worker.py](../../floodlab/ai_worker.py); this is not a portable CPU deployment. See [model record](../copilot-model.json) and [download script](../../scripts/download_copilot.py).

For a configured machine, the launcher derives the checkout path and uses WSL distribution `Ubuntu`:

```powershell
$env:SATQUERY_FLOOD_PYTHON_WSL = '/root/satquery-flood-lab/venv/bin/python'
$env:SATQUERY_AI_PYTHON_WSL = '/root/satquery/.venv/bin/python'
.\start-demo.ps1
```

These are the defaults, shown explicitly for override. [start.ps1](../../start.ps1) delegates to [start-demo.ps1](../../start-demo.ps1). Logs go to `.runtime/`. The launcher may reuse existing services on 8770/8771; verify which checkout they serve. Use the foreground command for a core-only launch.

## Verification

From an activated Python 3.11 environment, create `.runtime/` and run:

```bash
python -m pytest -q -p no:cacheprovider --junitxml=.runtime/reviewer-tests.xml
```

PowerShell directory command: `New-Item -ItemType Directory -Force .runtime`. New results belong in this ignored directory. Preserve historical `docs/test-results.xml` and frozen reports. [Current verification scope](../presentation/VERIFICATION.md).

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Empty saved-analysis menu | Fresh clones exclude event payloads. Create the fixture or acquire inputs. |
| Missing `pyarrow` | Install the supplement in the interpreter running Uvicorn. |
| Local AI unavailable | Select an explicit topic or configure the separate GPU worker. |
| Optical choice disabled | No preview is registered for that run/grid; not a claim that no imagery exists. |
| Empty access / `connectivity_assessed: false` | Unknown result, not zero isolation. |
| Acquisition stopped | Inspect execution events and runtime logs; confirm access/coverage. Keep secrets out of issue text. |
| Existing run ID | Pick a new ID; frozen outputs are protected. |
