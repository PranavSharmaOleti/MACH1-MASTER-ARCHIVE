# MACH1 / FleetLine E1 — Master Archive

**Project:** Design the ideal ride-service vehicle for India 2035. Determine optimal vehicle size, seating, body style, powertrain strategy, and digital ecosystem for intra-city, inter-city, shared, and premium mobility.

**Central thesis:** Volume is in intra-city. Margin is in airport and commute. They are structurally different trips. The vehicle that wins both is a 45 kWh BEV sedan (FleetLine E1) sized for depot charging.

**Headline result:** BEV TCO +14.5% nominal (+6.5% incl. infra, +6.7% NPV at 5 yr, +14.6% NPV at 8 yr). Driver take-home +₹14,200/month on EV vs CNG.

---

## Repository structure

| Folder | Contents |
|--------|----------|
| `00_MASTER_DOCUMENTATION/` | Provenance register, issue log, corrected deck text, evidence binder, cheat sheet, Maruti panel questions, errata handout, revised deck changelog, 10-min presentation script, deck number extraction + gap analysis |
| `01_PRESENTATION_AND_REPORTS/` | Final deck PDF + video + earlier drafts |
| `02_PRIMARY_SOURCE_REPORTS/` | Key source reports (TCO, market, powertrain, battery, driver, roadmap) + Mach1 NITDurgapur round-1 materials |
| `03_ENGINEERING_AND_MARKET_DATA/` | Vahan/autopunditz CSVs, market analysis script |
| `04_MODELS_AND_CALCULATIONS/` | TCO engine (Python), battery model (Python) |
| `05_CAD_AND_DRAWINGS/` | Dzire dimension drawing (DWG) |
| `07_RESEARCH_AND_REFERENCES/` | Extracted papers + research references |
| `08_IMAGES_SCREENSHOTS_AND_MEDIA/` | Screenshots and media |
| `90_ARCHIVE_AND_OLD_VERSIONS/` | Superseded docs, duplicate artifacts, 172 MB zip |

---

## Key deliverables (00_MASTER_DOCUMENTATION/)

| File | Purpose |
|------|---------|
| `01_MASTER_DATA_PROVENANCE.xlsx` | Central provenance register — 7 sheets, 92 numerical records, calculation traceability, technical claims, source file index, discrepancies, reference index |
| `05_ISSUE_LOG.xlsx` | Master issue log — 13 seeded issues, 3-tier status scheme, severity legend, summary |
| `CORRECTED_DECK_TEXT.md` | 50 text edits across 10 slides with old→new→reason |
| `PPT_CHANGE_LIST.md` | Slide-by-slide exact text replacements for Canva |
| `EVIDENCE_BINDER_INDEX.md` | 10 headline numbers with definition, formula, inputs, source |
| `CHEAT_SHEET_25_NUMBERS.md` | 25 numbers to recite and re-derive from memory |
| `MARUTI_PANEL_40_QUESTIONS.md` | 40 hardest panel questions with answers, sources, concessions |
| `ERRATA_HANDOUT.md` | One-page errata (31 corrections, 3 tiers) + spoken opener |
| `REVISED_DECK_CHANGELOG.md` | Full revised deck with change log + decision guide (A vs B) |
| `PRESENTATION_SCRIPT_10MIN.md` | 10-minute timed presentation script |
| `DECK_NUMBERS_EXTRACTED.csv` | All 481 numbers from the 11-slide deck |
| `DECK_GAP_ANALYSIS.md` | 160 numbers not in the provenance register |

---

## Key source files

| File | Role |
|------|------|
| `04_MODELS_AND_CALCULATIONS/tco_engine/tco_engine.py` | TCO model — city/basis matrix, cost stack, sensitivity |
| `04_MODELS_AND_CALCULATIONS/tco_engine/tco_analysis.py` | TCO analysis — driver P&L, downtime, battery replacement |
| `04_MODELS_AND_CALCULATIONS/battery_model/mach1_model.py` | Battery degradation model |
| `02_PRIMARY_SOURCE_REPORTS/Key docs/MACH1_TCO_ANALYSIS.pdf` | TCO report |
| `02_PRIMARY_SOURCE_REPORTS/Key docs/MACH1_MARKET_ASSESSMENT.pdf` | Market assessment |
| `02_PRIMARY_SOURCE_REPORTS/Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf` | Powertrain specs |
| `01_PRESENTATION_AND_REPORTS/Detailed Presentation Report.pdf` | Final 11-slide deck |

---

## Powertrain convention (single)

- 45 kWh nameplate, 12.84 kWh/100 km, 10% battery reserve (40.5 kWh usable)
- 15% design range reserve, 48°C design point (44.1 kWh, 71.9% SoH)
- 7.4 kW / 3.86 h overnight, nominal EFC 178/yr
- 200,000 km = rated life (3.2 yr), 8 yr = economic horizon
- 268 km range at 15% reserve (315 km at zero reserve)

---

## TCO headline (verified against code)

| Metric | Value |
|--------|-------|
| Nominal excl-infra (5 yr) | +14.5% |
| Nominal incl-infra (5 yr) | +6.5% |
| NPV incl-infra (5 yr) | +6.7% |
| NPV incl-infra (8 yr) | +14.6% |
| Driver take-home EV | ₹47,060/mo |
| Driver take-home CNG | ₹32,860/mo |
| Driver advantage | +₹14,200/mo |

---

## GitHub

https://github.com/PranavSharmaOleti/MACH1-MASTER-ARCHIVE

## Git history

12 commits. See `git log --oneline` for full history.
