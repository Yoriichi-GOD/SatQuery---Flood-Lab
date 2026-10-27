# Architecture and methods

[Home](../../README.md) · [Setup](GETTING_STARTED.md) · [Evidence](EVIDENCE.md)

## Data flow

```text
Area bounds + past UTC event date
    ↓
Scene discovery → authenticated provider processing
    ↓
Comparable SAR + pre-event OSM + available optical
    ↓
Contracts: dates · orbit · dB units · grid · hashes · coverage
    ↓
Water rule / debris proxy → intersections → road graph
    ↓
Frozen masks · tables · reports · provenance · checksums
    ↓
Workspace map + saved-value answers / optional topic router
```

This diagram describes implemented data flow. Screenshots show the working app. Space artwork is interface decoration, not scientific imagery.

## Code map

| Component | Code | Responsibility |
| --- | --- | --- |
| Service | [server.py](../../floodlab/server.py) | UI, frozen runs, allowlisted downloads and answers. |
| Jobs | [jobs.py](../../floodlab/jobs.py) | One job, persisted events, restart/failure handling. |
| Satellite inputs | [event_acquisition.py](../../floodlab/event_acquisition.py), [acquisition.py](../../floodlab/acquisition.py) | Discovery, bounded requests, OAuth and provenance. |
| Historical inputs | [automatic.py](../../floodlab/automatic.py), [automatic_topology.py](../../floodlab/automatic_topology.py), [historical.py](../../floodlab/historical.py) | Pre-event features, way versions and node topology. |
| Optical/proxy | [automatic_optical.py](../../floodlab/automatic_optical.py), [debris.py](../../floodlab/debris.py) | Clear coverage and vegetation-loss/SAR-change candidates. |
| Calculation | [core.py](../../floodlab/core.py), [pipeline.py](../../floodlab/pipeline.py), [impact.py](../../floodlab/impact.py) | Contracts, classification, intersections, reachability, frozen exports. |
| Questions | [copilot.py](../../floodlab/copilot.py), [ai_worker.py](../../floodlab/ai_worker.py) | Frozen-value rendering and optional topic selection. |
| Interface | [index.html](../../web/index.html), [flood-workspace.js](../../web/flood-workspace.js) | Saved runs, image/map viewer, evidence, questions and progress. |
| Fixture/checks | [fixture.py](../../floodlab/fixture.py), [tests](../../tests) | Invented known-answer case and software checks. |

`jobs.py` is the full Workspace path: acquire → prepare → topology → optical → pipeline. The older `automatic.py` CLI is a narrower water/exposure path, not identical to the UI job.

## Methods and limits

**Water:** two aligned VV/VH Sentinel-1 dB rasters in a projected metre CRS. Require pre < event < post, consistent relative orbit/direction, declared terrain correction and matching hashes. New water requires post-event VV < −17 dB, pre-event VV ≥ −17 dB and a drop ≥ 3 dB on valid pixels. VH is checked but does not drive the water rule. Defaults are fixed and uncalibrated; this is not learned flood inference.

Classes: 0 = no candidate under the heuristic; 1 = water on both dates; 2 = new-water candidate; 255 = invalid. Two dates do not prove permanent water. Arrays load into RAM. Tiled equality checks test this pixelwise rule, not neural inference or subpixel registration.

**Debris:** fixed vegetation-to-bare transition supported by SAR change. Clouds, shadows and NoData retain uncertainty. Clearing/agriculture can trigger it; already-bare deposits can be missed. SCL is resampled from a coarser grid. Optical search is limited to three dates per side within 14 days. The proxy is unvalidated.

**Exposure:** intersect candidate geometry with historical OSM, keeping IDs and valid coverage. Missing assets are absent from counts. Overlap does not establish damage, closures or casualties. [Impact tests](../../tests/test_impact.py) include area, length, touch and unknown coverage.

**Access:** compare reachability after assumed candidate-based disruptions. Original OSM node IDs preserve crossings; an overpass does not become a junction just because lines intersect. One-way/access handling is partial; turn restrictions are absent. Missing hubs, snapping, graph gaps and AOI boundaries can leave results unknown. Synthetic graph tests do not prove real closures.

**Questions:** optional Qwen3-0.6B selects a topic; answers render saved values with source pointers. It is not a general image-analysis model. Explicit topics need no model. Native Nepali review remains open.

## Outputs and storage

| Location / artifact | Meaning |
| --- | --- |
| `data/` | Acquired/prepared inputs, provider responses, provenance and jobs; ignored. |
| `artifacts/runs/<run-id>/` | Immutable local exports; ignored. |
| `prediction.tif`, `debris-candidates.tif` | Georeferenced candidates; debris only where assessed. |
| `result.json`, `manifest.json` | Summary, settings, inputs and limitations. |
| `layers.geojson`, `exposure.csv`, `debris-exposure.csv` | Layers and per-feature intersections. |
| `graph.json`, `connectivity.json`, `topology-audit.json` | Access calculations and available topology audit. |
| `sensitivity.json` | Exposure under one-pixel dilation/erosion. |
| `report-en.html`, `report-ne.html` | Reports from saved calculations. |
| `freeze.json` | Output SHA-256 map; existing run IDs cannot be overwritten. |
| `docs/`, `output/pdf/` | Historical records and generated reports. |

EMSR/UNOSAT labels are evaluation-only, excluded from prediction/threshold selection. Provider preprocessing is external; the core prepared-raster pipeline is not a local SAFE processor. Radar layover masking remains incomplete.

## Inheritance and acceptance

SatQuery supplied the visual foundation: [reuse audit](../reuse-audit.md), [UI inheritance](../ui-inheritance.md), [upstream notice](../../vendor/SATQUERY-LICENSE.txt). Flood Lab uses a fixed SAR rule; original SatQuery WaterUNet/CDVQA scores do not transfer here.

Read the [specification audit](../official-spec-audit.md) with its later updates and [closure record](../closure-checks.md). Early status phrases remain historical. Scientific validation and competition acceptance are incomplete.
