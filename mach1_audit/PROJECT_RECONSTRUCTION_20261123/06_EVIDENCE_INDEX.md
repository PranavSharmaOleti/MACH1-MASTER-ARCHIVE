# 06 — Evidence index

Status key: **Confirmed** = directly inspected and verified; **Partially verified** = source states it but primary detail missing/unreproducible; **Unverified** = claim exists but not substantiated; **Missing** = artifact absent.

## Dendrogram

| Finding | Evidence | Status |
|---|---|---|
| Dendrogram figure exists on slide 3 | `01_PRESENTATION_AND_REPORTS/Detailed Presentation Report.pdf` slide 3; `mach1_audit/rendered/slide-03.png` (Captions: "Agglomerative Hierarchical Clustering", "Average linkage · Euclidean distance · 7 z-scored features", heights 1.000/1.63/2.64/5.036) | Confirmed |
| Deck label "CLUSTER A — AIRPORT + CORPORATE-COMMUTE" | slide 3 text; `00_MASTER_DOCUMENTATION/DECK_NUMBERS_EXTRACTED.csv:88` | Confirmed |
| Figure groups Airport+Premium, Commute+Intra-city | Visual inspection of slide-03.png | Confirmed |
| No clustering script/feature matrix/distance matrix/linkage output in repo or git history | `git grep` across all commits; only Python files listed; `03_ENGINEERING_AND_MARKET_DATA/Market/market_analysis.py` docstring explicitly excludes clustering | Confirmed (absence verified) |
| Merge heights not reproducible from visible 5×7 table | Independent scipy recomputation and exhaustive subset/scaling/linkage search | Confirmed (recomputation in `02_…md` §C) |
| "Five rows, seven columns; no observations; z-scoring cannot repair" | `02_PRIMARY_SOURCE_REPORTS/Key docs/MACH1_MARKET_ASSESSMENT.pdf` §2; `XCELERATE_MARKET/00_audit/RESEARCH_AUDIT.md:33` (A8) | Confirmed |
| Two residual df (regression, not clustering) | `MACH1_MARKET_ASSESSMENT.pdf` §2 "Multivariate regression" | Confirmed |
| Removal ordered | `00_MASTER_DOCUMENTATION/PPT_CHANGE_LIST.md:24` (edit #7); `ERRATA_HANDOUT.md:53`; `CORRECTED_DECK_TEXT.md:24`; `MARUTI_PANEL_40_QUESTIONS.md:186-190`; `REVISED_DECK_CHANGELOG.md:38` | Confirmed |
| Original computation procedure | No script/output survives | Missing |

## Chronology

| Finding | Evidence | Status |
|---|---|---|
| Repo archived after audit; earliest commit 31 Oct 2026 | `git log --reverse`: `d4a28b3` (31 Oct) … `154fb71` (5 Nov) | Confirmed |
| Dendrogram phrase first tracked in git | commit `ae3bf59` (1 Nov), `DECK_NUMBERS_EXTRACTED.csv` | Confirmed |
| XCELERATE_MARKET research added | `a00b017` (4 Nov) | Confirmed |
| Cleaned CSVs and audit tooling | `edcd356`, `154fb71` (5 Nov) | Confirmed |

## Mathematical issues

| Finding | Evidence | Status |
|---|---|---|
| 35 segment cells unsourced | `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:4-65` all S-D/C-D; `RESEARCH_AUDIT.md:26` (A1) | Confirmed |
| Inter-city 1.5×280=420 vs 340 | `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:46-48`; `RESEARCH_AUDIT.md:40` (B2) | Confirmed |
| 2625/95 = 27.63 not 27.58 | `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:9` note "2625/95"; independent arithmetic | Confirmed |
| 2062.5/75 = 27.50 not 27.58 | `MARKET_STRATEGY_SLIDE_METRICS.csv:11` | Confirmed |
| "100.1%" weight claim | No such weight figure found; only 105 raw weights normalised in `segment_prioritisation.py:12-26`, and 380.98 vs 380.95 rounding note in `60_final_redteam_report_v3.md:26` | Unverified as stated; related issues confirmed |
| 10 vs 11 criteria text error | `50_strategic_recommendation.md:46`; `60_final_redteam_report_v2.md:51-53` | Confirmed |
| Equal-weight tie 354.55 | `sensitivity_results_v4.csv:2-3`; independent run of `segment_prioritisation_v4.py`; `60_final_redteam_report_v4.md:50` | Confirmed |
| 591.3M vs 810M different scopes | `MARKET_STRATEGY_SOURCE_REGISTER.csv:2,4`; `04_MARKET_CONTEXT_METRICS_CLEAN.csv` MC1/MC2 | Confirmed |
| Airport lowest revenue/km ₹17.14 | `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:36`; `RESEARCH_AUDIT.md:80` (F4) | Confirmed |
| Scoring ratings analyst-assigned | `segment_prioritisation.py:28-30`; `60_final_redteam_report.md:237`; `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:68-73` | Confirmed |

## Research foundation and operators

| Finding | Evidence | Status |
|---|---|---|
| 42-source register | `MARKET_STRATEGY_SOURCE_REGISTER.csv` (42 rows) | Confirmed |
| 52-row metrics dataset | `MARKET_STRATEGY_SLIDE_METRICS.csv` | Confirmed |
| Operator figures mostly company-reported | `MARKET_STRATEGY_OPERATOR_LANDSCAPE.csv` evidence_status column; source register 34-37 | Confirmed |
| OHM 100 EVs at RGIA documented; orders unverified | source register:37; `02_OPERATOR_EVIDENCE_CLEAN.csv` O6-O8 | Partially verified (100 deployment documented; 1,300 order delivery unverified) |
| Evera ~2,200 was expansion target; 600+ reported figure | `02_OPERATOR_EVIDENCE_CLEAN.csv:O2`; Business Standard 24 Jun 2025 | Confirmed |
| Tata–Uber 25,000 agreement | source register:19; `03_PROCUREMENT_RELATIONSHIPS_CLEAN.csv:P1` | Confirmed (agreement; delivery status not audited) |
| Lithium 25,000 trips/day, 300 km/day company-reported | source register:35; `02_OPERATOR_EVIDENCE_CLEAN.csv` O18/O20/O21 | Partially verified (company-reported only) |
| No primary interviews/trip-level data | `MARKET_STRATEGY_DATA_GAPS.md` P0-1 etc.; `RESEARCH_AUDIT.md` §3 | Confirmed |

## Key git commits for reconstruction

`a00b017` (XCELERATE_MARKET deliverables) · `ae3bf59` (deck numbers extraction) · `41dd064` (corrected deck text, panel Q&A) · `60_final_redteam_report*.md` (v2 errors through v6.1 final) · `371ff8c` / `edcd356` (cleaned data packs) · `154fb71` (audit tooling and rendered slides).

## Note on evidence limits

The original dendrogram's computation is **Missing** — no code, feature matrix, distance matrix, or linkage log survives anywhere in the repository or its history. Merge-height reproduction is therefore a reconstruction attempt, not a recovery of the original procedure. All other findings above are **Confirmed** by direct file inspection or independent calculation unless marked otherwise.
