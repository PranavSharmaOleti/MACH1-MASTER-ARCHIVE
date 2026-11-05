# MACH1 Audit Handoff Report

**Repository:** `/home/sankara/Downloads/MACH1_WORKING_FILES`  
**Audit status:** Paused before archive creation and reorganisation  
**Original files:** Unchanged. No source file was moved, renamed, edited, deleted, or copied into a final archive.

## Work completed

- Recursively inventoried the repository: **121 files in 17 directories**.
- Identified `Detailed Presentation Report.pdf` as the likely requested central presentation. It has **11 pages**, including a cover.
- Rendered and visually reviewed all presentation pages, then extracted selectable text from them.
- Inspected the principal source groups:
  - `tco_engine/` — TCO/range/sensitivity Python model and generated figures.
  - `battery_model/` — battery sizing/degradation model, audit script and rebuild notes.
  - `data/` and `Market/` — VAHAN/AutoPunditz data, market script and Lens screenshots.
  - `Key docs/` — current reports supporting the deck.
  - `superseded/` — older TCO, roadmap, synthesis and vehicle-feature analysis.
  - `extracted_papers/` — battery research papers and ZIP packages.
  - NIT Durgapur submission folders, images, PPTX, ZIPs, PDFs and the DWG drawing.
- Calculated SHA-256 hashes for each original file and found **25 exact duplicate-hash groups**. No duplicate was removed.
- Began a structured provenance register in temporary working data, covering source locations, calculation methods, verification status and discrepancies.

## Important findings

### 1. Slide 3 market table is not supported by the current repository evidence

`Key docs/MACH1_MARKET_ASSESSMENT.pdf` explicitly says that the earlier five-row use-case table should be withdrawn. This includes the deck’s use-case daily kilometres, trip counts, fares, growth rates, EV shares, price sensitivities and fit conclusions.

Treat these presentation claims as **unverified/discrepant** until sourced from measured trip/operator data:

- Intra-city / commute / airport / inter-city / premium market-table values.
- “61% of market” and “19.14% CAGR” positioning values.
- Segment-level EV adoption and price-sensitivity figures.

### 2. The TCO headline requires a clear infrastructure basis

The local TCO material supports two different Delhi five-year results:

| Result basis | EV | CNG | Claimed EV advantage |
|---|---:|---:|---:|
| Nominal, **excluding** charging infrastructure | ₹5.75/km | ₹6.73/km | +14.5% |
| Nominal, **including** ₹99,000/vehicle charging infrastructure | ₹6.31/km | ₹6.75/km | +6.5% |
| NPV, infrastructure included | — | — | +6.7% |

The deck shows the +14.5% figure alongside charger-inclusive discussion. Do not describe +14.5% as charger-inclusive.

Key local sources:

- `Key docs/MACH1_TCO_ANALYSIS.pdf`, especially pages 3, 5, 7, 8, 10, 12 and 13.
- `tco_engine/tco_engine.py`
- `tco_engine/tco_analysis.py`
- `tco_engine/figures.txt`

### 3. Range and energy bases need reconciliation

The retained model supports:

- Consumption: **12.84 kWh/100 km**.
- Daily energy at 200 km/day: **25.68 kWh**.
- 45 kWh pack with 90% usable energy: **315.4 km** at zero reserve.
- 15% reserve range: **268.1 km**.

The deck’s **263 km** figure comes from an older **15.38 kWh/100 km** consumption basis. `Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf` explicitly identifies this discrepancy.

The deck also mixes:

- 36 kWh usable energy at 10–90% SOC;
- 3% top and bottom reserve; and
- a 45 kWh × 90% usable range calculation.

These should be reconciled into one declared usable-capacity and reserve convention.

### 4. Battery strategy is traceable internally, but many policy/supplier assertions are external

The local files support the internal strategy of LFP at launch with sodium-ion retained as a later option. The battery report documents disagreement between two LFP degradation models:

- Naumann interpretation: **13.3 years to 80% at 40°C**.
- Lewerenz interpretation: **3.7 years to 80% at 40°C**.
- Spread: approximately **3.6×**.

Relevant sources:

- `Key docs/MACH1_BATTERY_EXECUTIVE_REPORT.pdf`
- `battery_model/mach1_model.py`
- `battery_model/self_audit.py`
- `battery_model/REBUILD_NOTES.md`

The following need primary external sources before being reused as facts:

- Sodium-ion research/programme numbers.
- Government spending/outlay figures.
- Sodium-ion supplier scale and homologation claims.
- Cost/time estimates for chemistry/architecture changes.
- Policy and regulatory interpretations.

### 5. Driver economics is an internally traceable model, not observed earnings evidence

`Key docs/MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf` supports the deck’s modelled figures, including:

- ₹14,200/month post-loan driver advantage.
- ₹47,060 versus ₹32,860 monthly take-home at the stated ₹11/km scenario.
- ₹10,597/month advantage in the 150 km/day sensitivity case.

These depend on the stated Delhi, distance, fare, cost and financing assumptions. They should not be presented as observed fleet-driver outcomes.

### 6. Rider, policy and market statistics need their original evidence packets

No retained primary source was found for several numerical claims, including:

- Rider survey sample sizes, complaint shares and feature scores.
- Maruti service-network size and sales/fleet share claims.
- Public charging-port-to-EV ratio.
- Bio-CNG plant/capacity/blending figures.
- State EV incentive/expiry details and central-scheme assertions.
- Route-distance figures used in corridor examples.

These should be logged as **External source** or **Unverified** in the final provenance workbook unless their original source documents are supplied.

### 7. AI/connected-mobility performance figures are proposals

Slide 9’s anticipated benefits—fault-warning lead time, downtime reduction, fewer deadhead kilometres and charging-cost reductions—are explicitly labelled as illustrative pilot targets. No validation dataset, TPMS supplier specification, BMS control definition or pilot result was found.

## Temporary audit material available

Temporary work was kept outside the repository in `/tmp/mach1_audit/`:

- `inventory.json` — recursive file inventory, metadata, hashes, extracted textual content and ZIP/PPTX listings.
- `extract_audit.py` — inventory/extraction helper.
- `rendered/slide-01.png` through `slide-11.png` — rendered central-presentation pages.
- `contact.png` — presentation contact sheet.
- `assemble_archive.py` — incomplete archive-generation draft. Do not execute without reviewing it first.

## Work not completed

- `MACH1_MASTER_ARCHIVE/` was not created.
- No source files were copied into an organised archive.
- `01_MASTER_DATA_PROVENANCE.xlsx` was not created.
- Final audit report, repository map and audit log were not written into the intended archive.
- Copy/hash integrity validation was not run because copying did not begin.

## Recommended continuation plan

1. Preserve the original repository as read-only.
2. Create `MACH1_MASTER_ARCHIVE/` separately within the repository only after reviewing the temporary inventory.
3. Build the Excel register with at least these sheets:
   - Presentation Index
   - Numerical Data Register
   - Calculation Traceability
   - Technical Claims
   - Source File Index
   - Discrepancies & Unresolved Items
   - Reference Index
   - Original-to-Archive Copy Map
4. Preserve `tco_engine/` and `battery_model/` as whole project folders.
5. Preserve `superseded/` and prior submission folders. They explain deck values and must not be discarded.
6. Copy rather than move every source file, then compare original/copy SHA-256 hashes.
7. Prioritise recovery of original sources for market segmentation, policies, rider surveys and sodium-ion claims before presenting the deck externally.

## Suggested archive structure

```text
MACH1_MASTER_ARCHIVE/
  00_MASTER_DOCUMENTATION/
  01_PRESENTATION_AND_REPORTS/
  02_PRIMARY_SOURCE_DOCUMENTS/
  03_ENGINEERING_DATA/
  04_CALCULATIONS_AND_ANALYSIS/
  05_CAD_AND_DESIGN/
  06_SIMULATIONS_AND_RESULTS/
  07_RESEARCH_AND_REFERENCES/
  08_IMAGES_PLOTS_AND_MEDIA/
  09_CODE_AND_AUTOMATION/
  90_ARCHIVE_AND_OLD_VERSIONS/
  99_UNCLASSIFIED_REVIEW_REQUIRED/
```
