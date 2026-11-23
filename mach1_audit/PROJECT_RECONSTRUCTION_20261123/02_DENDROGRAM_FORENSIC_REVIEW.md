# 02 — Dendrogram forensic review

## Bottom-line answer to the critical question

**The dendrogram WAS mathematically generated using hierarchical clustering — it was not hand-drawn, and it was not merely a conceptual tree.** The rendered slide 3 shows a real dendrogram with a method caption and four numeric merge heights. However, it cannot be reproduced from the visible input table under the stated method, it contradicts its own "Cluster A" label, and its input data were five hand-constructed rows with no observations. So: **real computation, methodologically weak inputs, and an interpretation not supported by the computation itself.**

## A. The original artifact

- Source: `01_PRESENTATION_AND_REPORTS/Detailed Presentation Report.pdf`, slide 3 ("MARKET"); preserved as `mach1_audit/rendered/slide-03.png`.
- The figure title: **"Agglomerative Hierarchical Clustering"**, subtitle **"Average linkage · Euclidean distance · 7 z-scored features"**.
- Y-axis: "Merge height (Euclidean distance)". Four merge heights labelled on the figure: **1.000, 1.63, 2.64, 5.036**.
- X-axis categories, left to right: **Airport, Premium, Intra-city, Corporate commute, Inter-city**.
- Bracket structure: **Airport + Premium merge first (1.000); Intra-city + Corporate commute merge (1.63); the two pairs merge (2.64); Inter-city joins last (5.036).**
- Adjacent text box on the same slide: **"THE PRIMARY POSITION — CLUSTER A — AIRPORT + CORPORATE-COMMUTE"** with explanatory bullets.

**Critical internal contradiction:** the dendrogram does NOT place Airport and Corporate commute in the same cluster at any level below the full five-way merge. The first two clusters are (Airport, Premium) and (Intra-city, Corporate commute). The "Cluster A = airport + corporate-commute" claim is a **text label beside the figure, not an output of the figure**. This alone invalidates the claimed clustering "agreement".

The deck text itself never uses the word "dendrogram" — the term appears only in the later audit/correction documents.

## B. Reconstruction of the input data

The only candidate input visible on the slide is the seven-column table immediately above the figure. Deck slide 3 left table, five rows × seven numeric columns:

| Use case | AVG KM | KM/DAY | TRIPS/DAY | ₹/TRIP | GROWTH | EV SHARE | PRICE SENS. |
|---|---|---|---|---|---|---|---|
| Intra-city street hail | 12.7 | 95 | 7.5 | 350 | 18% | 10% | 0.85 |
| Daily commute / subscription | 22.0 | 176 | 8.0 | 550 | 24% | 12% | 0.90 |
| Airport transfer | 35.0 | 210 | 6.0 | 600 | 26% | 18% | 0.35 |
| Inter-city / outstation | 280 | 340 | 1.5 | 4,200 | 20% | 5% | 0.40 |
| Premium / shared-premium | 18.0 | 144 | 8.0 | 520 | 28% | 15% | 0.30 |

These map exactly to the "five rows, seven columns" in the external assessment. `XCELERATE_MARKET/MARKET_STRATEGY_SEGMENT_COMPARISON.csv` preserves all 35 cells and grades **every one S-D/C-D (unsourced)**.

## C. Independent recomputation (what the figure should have shown)

Using the table above, z-scored column-wise (population ddof=0), Euclidean distance, average linkage:

```
Raw 5x7 matrix -> column z-scores -> Euclidean distances ->
Average-linkage merge heights:
  Airport + Premium       -> 1.454
  Intra-city + Commute    -> 1.971
  (above two pairs)       -> 3.202
  Inter-city              -> 5.630
```
Complete linkage gives 1.454 / 1.971 / 3.742 / 5.923; single linkage 1.454 / 1.971 / 2.667 / 5.349; Ward 1.454 / 1.971 / 4.244 / 6.782.

**None reproduce the deck's 1.000 / 1.63 / 2.64 / 5.036.** An exhaustive search over all 3–7 column subsets and seven scaling conventions (z ddof0/1, min-max, max-abs, divide-mean, divide-std, none) across the four linkage methods failed to reproduce the deck's four heights. Closest candidate: columns (AVGKM, TRIPSDAY, FARE, GROWTH, PRICESENS), z-ddof0, average linkage → 1.009 / 1.650 / 2.823 / 4.699 (summed error 0.548).

**Conclusion:** the stated method + visible table do not reproduce the displayed merge heights. Either a different (undocumented) feature set/scaling was used, or the figure was produced by a different procedure than its caption claims. The original computation cannot be reproduced from the repository. No clustering script, feature matrix, distance matrix or linkage output exists anywhere in the repo or its git history — the only clustering-named script (`03_ENGINEERING_AND_MARKET_DATA/Market/market_analysis.py`) explicitly states: *"This script intentionally does not run clustering or regression."*

## D. Methodological criticism — verified

Source: `02_PRIMARY_SOURCE_REPORTS/Key docs/MACH1_MARKET_ASSESSMENT.pdf` (18 Oct 2026), §2 "What the old clustering and regressions establish":

> "The earlier analysis had five manually constructed use-case rows and seven columns. It did not have rider, city, trip, or vehicle observations. The row labels were the analyst's own categories, and several inputs (including price sensitivity, daily duty, segment EV share, and segment growth) were unsupported or not measured on a common basis. Z-scoring seven features across five rows cannot turn those judgments into sampled market behavior. A distance matrix and linkage rule would make the arithmetic visible, but would not repair the sample or the provenance."

> "Do not report the dendrogram, merge heights, cluster labels, or 'independent agreement.' Do not replace the method with K-means, DBSCAN, or another clusterer on the same five rows."

Repeated at `XCELERATE_MARKET/00_audit/RESEARCH_AUDIT.md:33` (claim A8, grade D, "No feature matrix, no observations", "Remove … Do not substitute another clusterer on the same 5 rows").

The **two residual degrees of freedom** criticism belongs to a **separate five-row regression** (5 rows − 3 parameters incl. intercept), not to the clustering itself — the assessment says: "The prior five-observation regression had only two residual degrees of freedom after three predictors including the intercept." The user's recollection conflates the two critiques; both originate in the same document but target different methods.

**Why the limitations matter statistically:**
- Clustering *actual observations* (trips, cities, operators) estimates structure in sampled data; with n large, distances and merge heights have sampling meaning.
- Clustering *aggregated market-segment profiles* treats five constructed averages as if they were five sampled units — there is no within-segment variance, so no estimate of cluster stability or uncertainty.
- Clustering *manually assigned scores* is even weaker: the values are judgments, so the topology reflects the analyst's coding choices, not market behaviour.
- With n=5 and p=7, p > n/2; z-scoring standardises on the same five points being clustered, making the distances highly sensitive to any single value and to which columns are included. No resampling is possible (residual df ≈ 0 for the clustering; 2 for the regression).

**Is hierarchical clustering inherently inappropriate?** No. The method is fine for exploratory segmentation of repeated observed cells (city × use case × period). The failure was the **input construction and interpretation**, not the choice of hierarchical clustering per se.

## E. Chronology of criticism and revision

| Stage | Evidence | Effect |
|---|---|---|
| 18 Oct 2026 — external assessment | `MACH1_MARKET_ASSESSMENT.pdf` §2 | Dendrogram, merge heights, cluster labels and "independent agreement" ordered removed |
| 1 Nov — deck correction artifacts | `DECK_NUMBERS_EXTRACTED.csv:88` records "Dendrogram, Cluster A — Airport + Corporate-commute, stated"; `PPT_CHANGE_LIST.md:24` edit #7 "Remove or relabel as illustrative grouping, not statistically derived"; `ERRATA_HANDOUT.md:53` "Removed"; `MARUTI_PANEL_40_QUESTIONS.md:186-190` Q28 30-second answer "No. The dendrogram is illustrative … We're removing it"; `CORRECTED_DECK_TEXT.md:24`, `REVISED_DECK_CHANGELOG.md:38` | Language changed; claim retired in corrected deck materials |
| 31 Oct–1 Nov — repository archive | `00_audit/RESEARCH_AUDIT.md:33` | Formal grade D, recommendation to remove |
| 4 Nov — XCELERATE_MARKET red-team v2–v6.1 | red-team reports focus on scoring/evidence, not the dendrogram | The dendrogram was not re-litigated; **the strategic recommendation survived via the weighted scoring model**, not via clustering |
| Present | original slide 3 superseded; cleaned data pack files carry no clustering | No rebuilt dendrogram; no clustering claim in current datasets |

## F. What remains of the dendrogram today

- Preserved: the original image/text (`Detailed Presentation Report.pdf`, `mach1_audit/rendered/slide-03.png`) as a historical artifact, and the correction documents that retire it.
- Not preserved: any claim that clustering supports airport + corporate commute.
- Not reproducible: the exact merge heights shown in the figure.

## G. What the evidence supports about Airport + Commute after the dendrogram was retired

The surviving basis is the **weighted 11-criteria scoring model** (Airport 380.95, Commute 371.43 out of 500 under base weights), whose ratings are explicitly analyst-assigned (S-D), plus operator-presence evidence (company-reported). Under equal weights the two **tie at 354.55**. That is the honest status: a judgment-based shortlist, not a data-derived cluster.
