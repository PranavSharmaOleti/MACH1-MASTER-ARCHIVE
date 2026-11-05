# MACH1 Audit — Execution Plan

## State (from handoff)
- Repository: /home/sankara/Downloads/MACH1_WORKING_FILES (121 files, 18 dirs) — READ-ONLY, unchanged
- inventory.json in /home/sankara/Downloads/mach1_audit/ has full file inventory, sha256, classifications, 25 duplicate-hash groups (25 groups, none removed)
- Temp audit material copied to /home/sankara/Downloads/mach1_audit/ (inventory.json, extract_audit.py, assembled_archive.py, contact.png, rendered/slide-01..11.png)
- Presentation identified: Detailed Presentation Report.pdf (11 pages incl cover)
- Phases 3-5 NOT started (archive, xlsx register, reports, integrity validation)

## Remaining work
1. Re-examine repository + inventory (done largely) — build repo map
2. Extract presentation text (selectable + OCR of rendered slides) — slide-by-slide audit
3. Trace each datum to source (tco_engine.py, tco_analysis.py, figures.txt, battery_model, Key docs PDFs, data/ CSVs)
4. Create MACH1_MASTER_ARCHIVE/ + copy files with hash verification (preserve tco_engine/, battery_model/, superseded/, NIT folders intact)
5. Build 01_MASTER_DATA_PROVENANCE.xlsx (7+ sheets)
6. Write 02_PRESENTATION_AUDIT_REPORT.md, 03_REPOSITORY_MAP.md, 04_AUDIT_LOG.md
7. Final integrity & completeness verification; completion summary

## Key known data (figures.txt = primary source for TCO deck figures)
- Delhi 5yr financed nominal excl-infra: EV 5.75, CNG 6.73, +14.5% (figures.txt line 20)
- incl infra: +6.5%; NPV incl infra: +6.7% (5yr), +14.6% (8yr)
- Range: 12.84 kWh/100km, 45kWh pack, 315.4km zero reserve, 268.1km at 15% reserve
- Driver: 14,200/mo post-loan advantage; 47,060 vs 32,860 take-home @11/km; 10,597 @150km/day

## Open questions / decisions
- Confirm exact presentation slide count and titles via text extraction
- Decide how much OCR/deep visual audit is feasible vs selectable text