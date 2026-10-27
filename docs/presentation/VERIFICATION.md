# Repository presentation verification

[Home](../../README.md) · [Setup](../guides/GETTING_STARTED.md) · [Evidence](../guides/EVIDENCE.md)

Documentation review date: **27 October 2026**. Application base: `ae61e5d` (the GitHub main branch at review start). Work was isolated on `codex/flood-repository-presentation` because the original local checkout contains unrelated unfinished application changes.

## Scope

The presentation update changes the README and adds guides, actual product screenshots and this verification record. Application code, tests, lockfile, licenses, historical records, PDFs and datasets remain unchanged. No product features, deployment, model training, external acquisition or frozen prediction regeneration is part of this work.

## Checks performed

- Existing WSL Python **3.11.16** environment, existing dependencies; no claim of a fresh-machine installation.
- Unchanged test suite: **70 passed, 31 warnings, 2.46 s**. Warnings concern Rasterio transform deprecation, Shapely transform deprecation and synthetic preview georeferencing. Historical XML was not overwritten.
- Current JUnit output: [regression-20261027.xml](regression-20261027.xml), separately saved from the historical report. Hostname, machine timestamp and file-path attributes were removed from the public copy; test outcomes and durations are unchanged.
- Existing saved Syapru run copied into the isolated checkout only for local inspection. All **15 frozen artifact hashes** matched before display. Local payloads remain ignored and are excluded from the commit.
- Actual local Workspace, optical views, explicit Water answer and Evidence overview inspected. Water answer equals the frozen result: **95,600 m² / 956 pixels**. No AI inference was needed for explicit-topic rendering.
- Offline fixture and prepared-raster command exercised in ignored local directories; expected **32 pixels / 3,200 m²**, one building, **40 m** of road and one synthetic cut-off settlement.
- **127 local links/heading targets** and all image references checked across seven authored Markdown pages. All seven were rendered at **1440 px and 390 px**, light and dark: **28 local preview variants**, with no broken images or document-level horizontal overflow. Visual inspection used a local GitHub-style Markdown renderer, not the exact GitHub web renderer. Wide code/tables can scroll within their containers. No private material was sent to a rendering service.
- All documented PowerShell blocks parse. Offline module commands and the foreground Uvicorn entry point ran in the existing environment; installation and background-launcher limitations below still apply.
- Final diff checked against the GitHub base. The original local checkout retains identical Git status, **29 tracked file hashes and 77 untracked file hashes**. No historical application/evidence file enters this change. Credentials, raw rasters, local run payloads, dependency folders and preview-server files are excluded.

## Limits

The dependency record lacks `pyarrow`; setup documents the installed **26.0.0** supplement. A clean dependency installation, native Windows installation, PowerShell background-launcher execution, CUDA model setup and new authenticated area/date retrieval were **not** performed in this pass. Uvicorn, API inspection, tests and fixture commands ran in the existing WSL environment; screenshots used a separate local port.

External source links point to provider/project documentation; access and provider quotas can change. The scientific gaps in the [evidence guide](../guides/EVIDENCE.md) remain open. A documentation preview is not a new product acceptance or scientific validation study.
