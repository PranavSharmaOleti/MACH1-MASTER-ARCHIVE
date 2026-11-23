# 04 — Mathematical issues and reconciliation

Verified independently, 23 Nov 2026. Leads from the user and from audit documents were re-derived from source files; nothing copied without checking.

## 1. Five-segment analysis validity — CONFIRMED INVALID AS DATA

The 35 segment-table cells are all graded S-D/C-D in `MARKET_STRATEGY_SEGMENT_COMPARISON.csv` (lines 4–65). The five rows are not a partition: "Premium / shared-premium" is a service tier overlapping the trip-purpose rows (`00_audit/RESEARCH_AUDIT.md:27`, A2; red-team `60_final_redteam_report.md:54`). **Type: definitional/documentary.** Affected the dendrogram and segment-share claims directly.

## 2. Inter-city 420 vs 340 km/day — CONFIRMED

`MARKET_STRATEGY_SEGMENT_COMPARISON.csv:47` shows km/day = 340 with note "1.5×280=420; 340 implies deadhead"; line 48 shows 1.5 trips/day; line 46 shows 280 km/trip. Independent calculation: **1.5 × 280 = 420**, not 340. Confirmed also in `RESEARCH_AUDIT.md:40` (B2) and `PPT_CHANGE_LIST.md` edit #4. **Type: arithmetic/internal inconsistency.** Affected the segment table and hence the clustering inputs; not the final scoring model.

## 3. Revenue per km ₹27.58 vs ₹27.63 — CONFIRMED, two separate issues

- `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:9` records 27.58 with calculation note "2625/95". Independent arithmetic: **2625 / 95 = 27.6316** → 27.63, not 27.58. The stated value and its stated calculation disagree.
- `MARKET_STRATEGY_SLIDE_METRICS.csv:11` records 27.58 with note "2062.5/75 (approx)" → **2062.5 / 75 = 27.50**, also not 27.58.
- Deck and reports round to **₹27.6** (`INDIA_RIDE_SERVICE_MARKET_REPORT.md:260`, `MARKET_STRATEGY_SLIDE_DATA_PACK.md:63`).

**Type: arithmetic + documentary.** The three values 27.5/27.58/27.63 trace to inconsistent inputs; only 27.63 follows from the deck's own ₹2,625 and 95 km. Did not affect clustering (fare was a clustering column, but its derived ratio was not).

## 4. Weights sum 100.1% — NOT CONFIRMED as stated; underlying issue found

`segment_prioritisation.py` and `_v4.py` declare raw weights `10,10,10,15,5,5,20,15,5,5,5`, whose **raw sum is 105**, then normalise by `_tw` to 100 in code. No 100.1% figure appears in the segment-scoring context; the only "100.1" in the repo is a battery-model sweep value. However `60_final_redteam_report_v3.md:26` documents a **display rounding discrepancy**: Airport's displayed contributions sum to 380.98 while its total is 380.95; the unrounded values reconcile. **Type: documentary/rounding, not a weight-sum error of 100.1%.** The user's recollection appears to conflate the 105 raw weights, the normalisation step, and the 380.98 vs 380.95 rounding note.

## 5. Sensitivity "10 criteria" vs 11 — CONFIRMED

`50_strategic_recommendation.md:46` says "Equal weights (all 10 criteria equally weighted)" while `segment_prioritisation.py:2` and the framework list **11 criteria**. `60_final_redteam_report_v2.md:51-53` records this error and the correction; `segment_prioritisation_v4.py` re-ran it with 11. **Type: documentary.** Did not change scores; only the description.

## 6. Equal-weight result: tie, not airport win — CONFIRMED

Independent run of `segment_prioritisation_v4.py`: under equal weights (11 × 9.09%), **Daily commute 354.55 and Airport 354.55 — exact tie**; `sensitivity_results_v4.csv:2-3` confirms. Also confirmed `50_strategic_recommendation.md:46` and `60_final_redteam_report_v2.md:61`, `v4.md:50`. Under base weights Airport 380.95 vs Commute 371.43, a +9.52 margin (2.5%); `60_final_redteam_report_v4.md:43`. **Type: prior misinterpretation, corrected.** Directly relevant to the strategic conclusion: "Airport uniquely ranks first" is false under equal weights.

## 7. 591.3M vs 810M — CONFIRMED different scopes

591.3M = (840k Uber + 460k Ola + 320k Rapido) × 365 = 591,300,000; source Motilal Oswal via Business Standard 18 Apr 2025 (`MARKET_STRATEGY_SOURCE_REGISTER.csv:2`), reproduced in `market_analysis.py`. 810M = 27% of ~3.0B total ride-hailing trips (Redseer, 7 May 2026; source register line 4). `04_MARKET_CONTEXT_METRICS_CLEAN.csv` explicitly recommends 591.3M as headline and 810M as note only. **Type: definitional/scope, not an error.** Must not be combined.

## 8. Dendrogram merge heights not reproducible — CONFIRMED

Deck displays 1.000 / 1.63 / 2.64 / 5.036. Independent recomputation from the visible 5×7 table (z-score ddof0, Euclidean, average linkage) gives 1.454 / 1.971 / 3.202 / 5.630. Exhaustive subset/scaling/linkage search did not reproduce the deck values (best sum-absolute-error 0.548). **Type: methodological/documentary — the caption's method and the visible table do not generate the displayed figure.** No script, feature matrix, distance matrix or linkage output exists in the repository or git history. Detailed in `02_DENDROGRAM_FORENSIC_REVIEW.md`.

## 9. Residual degrees of freedom — CONFIRMED, but about regression

5-row regression with 3 parameters including intercept → 2 residual df (`MACH1_MARKET_ASSESSMENT.pdf` §2; `RESEARCH_AUDIT.md` A8 context). **Type: methodological.** Applies to the discarded five-row regression, not to hierarchical clustering. The user's recollection merges two critiques from the same document.

## 10. Airport margin thesis — CONFIRMED UNSUPPORTED

Airport has the **lowest** gross revenue per paid trip-km (₹17.14) of five archetypes (deck-derived; `MARKET_STRATEGY_SEGMENT_COMPARISON.csv:36`). The "margin" claim was never calculated (`RESEARCH_AUDIT.md:80`, F4, grade D). **Type: methodological/documentary.** Did not affect clustering, but did affect the strategic narrative.

## Summary of impact on the strategic conclusion

- Errors 1, 2, 3, 8, 9 undermine the dendrogram and the segment table.
- Errors 5, 6 affect how the surviving scoring model is described (tie under equal weights).
- Error 7 is a scope caveat, not an error; both figures remain usable with labels.
- The final shortlist (Airport + Commute) survives as a **judgment-based hypothesis** from the scoring model, not as a data-derived cluster or proven margin segment.
