# Evidence, reports and open work

[Home](../../README.md) · [Walkthrough](REVIEWER_WALKTHROUGH.md) · [Setup](GETTING_STARTED.md) · [Architecture](ARCHITECTURE.md)

Software correctness, map agreement and operational usefulness are separate questions. Passing tests do not establish flood accuracy. Historical records retain their date and population; they have not been rewritten to match newer status.

## Software and workflow checks

| Record | Result | Scope |
| --- | --- | --- |
| [27 Oct verification](../presentation/VERIFICATION.md) | 70 passed; 31 warnings; 2.46 s | Fresh unchanged-code tests in existing WSL Python 3.11.16. XML stored separately. |
| [Historical JUnit](../test-results.xml) | 70 tests; 0 failures/errors/skips; 2.621 s | Historical captured report. [Closure](../closure-checks.md) records a distinct 2.40 s run. |
| [Full workflow](../full-workflow-verification.json) | `event-fe47db331390`; 15 verified downloads; copilot value matches | Historical Syapru area/date API run, not unrestricted global coverage. |
| [Live download checks](../live-verification.json) | Prepared Syapru and automatic Syapru exports | Saved run-specific records. Payloads remain local. |
| [Graph tests](../../tests/test_impact.py) | 11 known-answer cases | Bridge cuts, alternatives, overpasses, one-way and missing/boundary inputs; not actual isolation. |
| [Copilot development check](../copilot-routing-evaluation.json) | 9/12 topic-routing questions | Small development challenge before guardrails; no independent Nepali benchmark. |

The [Evidence screen](../images/evidence.png) is genuine. Its overview reads historical software results and an empty benchmark summary; it does not automatically incorporate later external reference comparisons. Use the dated records below for those.

## Reference comparisons

Sources: [15 Oct closure](../closure-checks.md), [demo status JSON](../demo-status.json). Predictions were frozen before reference scoring. Reference payloads are excluded from Git; filenames/hashes remain in [dataset readiness](../dataset-readiness.json). Implementations: [UNOSAT scoring](../../scripts/evaluate_unosat_reference_agreement.py), [EMSR scoring](../../scripts/evaluate_debris_reference.py).

| Comparison | Population and counts | Result | Interpretation |
| --- | --- | --- | --- |
| Water vs UNOSAT Product 4259 | Two AOIs; 57,446 valid pixels. TP 318, FP 531, FN 22,906, TN 33,691. | IoU 0.01339; F1 0.02642; precision 0.37456; recall 0.01369. | **Poor agreement.** Preliminary mixed flood/mudflow/rockflow extent is not field-validated water-only truth. Mismatch does not prove the detector accurate. |
| Debris proxy vs EMSR927 mass movement | Two AOIs; 47,127 valid pixels. TP 4,425, FP 64, FN 10,740, TN 31,898. | IoU 0.29056; F1 0.45029; precision 0.98574; recall 0.29179. | Class-mismatched diagnostic. High precision does not validate debris detection. |

Earlier material quotes single-AOI debris IoU 0.3279. That is a different population, not a model improvement. Do not retune against inspected references and present the same evaluation as held out.

## Runtime and expense

[Closure](../closure-checks.md) records **five successful full area/date requests**, mean **51.6 s**, range **35.5–81.8 s**: four Syapru rectangles and one Timure request. This small repeated sample is not a latency guarantee, independent-event benchmark or competitor comparison. Cached calculation timings in reports have different stage boundaries.

No complete electricity, compute billing, engineering-time or user-time ledger was measured. Free data/quota access is not measured zero cost. Larger areas, concurrency, cold starts and recovery need broader evaluation.

## Deliverables

| Item | Where | Role |
| --- | --- | --- |
| Situation report | [PDF](../../output/pdf/nepal-situation-report.pdf) | Historical analyst-facing example. |
| Technical report | [PDF](../../output/pdf/technical-report.pdf) | Historical methods/workflow snapshot. |
| Full evidence report | [PDF](../../output/pdf/flood-impact-final-report.pdf) | Detailed results, sources, feasibility and limits. |
| Demo narration | [90-second script](../demo-script.md) | Click cues for configured local data; no video included. |
| Acceptance status | [Closure](../closure-checks.md), [demo status](../demo-status.json) | Later boundary; read ahead of early status notes. |
| Audit history | [Specification](../official-spec-audit.md), [experiment log](../experiment-log.md), [data access](../data-access.md) | Preserve dated findings. Earlier access blockers were followed by acquisition. |
| Inheritance | [Reuse](../reuse-audit.md), [UI audit](../ui-inheritance.md) | Discloses SatQuery components and limits on transferred claims. |

No competition submission or completed acceptance is claimed. Organizer reuse clearance and final compliance remain open in saved records. Original competition PDF assets are not redistributed here.

## Data sources

| Source | Role | Access and attribution |
| --- | --- | --- |
| [Copernicus Data Space](https://dataspace.copernicus.eu/) | Sentinel-1/2 catalogue and processed observations | OAuth for processing; preserve scene IDs/request provenance. [API docs](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Overview.html). |
| [Copernicus DEM](https://registry.opendata.aws/copernicus-dem/) | Terrain source; provider correction records DEM30 | Correction does not establish complete layover masking. |
| [HeiGIT/ohsome](https://docs.ohsome.org/ohsome-api/) and [OpenStreetMap](https://www.openstreetmap.org/copyright) | Historical features, versions and node topology | OSM ODbL attribution. Missing mapping is not zero exposure. |
| [Copernicus EMSR927](https://mapping.emergency.copernicus.eu/activations/EMSR927/) | Checking-only reference products | Not prediction inputs or threshold-tuning labels. Class/date/resolution caveats. |
| [UNOSAT Product 4259](https://unosat.org/products/4259/) | Preliminary mixed-impact comparison | Evaluation only; not field-validated water truth. |
| [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) | Optional topic routing | [Pinned revision](../copilot-model.json); answers use saved calculations. |

Contains modified Copernicus Sentinel data 2026. [Sentinel notice](https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice). Existing [MIT software license](../../LICENSE); data/model terms apply separately.

## Open work

- Compatible independent water labels and event-level accuracy validation.
- Direct debris labels and expert interpretation.
- Reviewed topology, hubs, coverage and closure assumptions before real isolation conclusions.
- Native Nepali review and broader independent topic-routing evaluation.
- Varied operational trials and measured resource/cost ledger.
- Demo recording, organizer reuse clearance and complete acceptance review.

These are future evaluation needs. Repository presentation does not close them.
