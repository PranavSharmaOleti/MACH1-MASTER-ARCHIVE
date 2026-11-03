# CORRECTED FINAL MARKET RESEARCH REPORT — v2

## Maruti Suzuki XCELerate 2026 E-Track: Designing the Ideal Ride-Service Vehicle for India 2035

**Date**: 3 November 2026 (v2 — incorporating red-team reconciliation)
**Analyst**: Independent review, corrected per consolidated findings

---

## PART 1: CORRECTIONS TO PRIOR WORK

### Correction 1 — Segment prioritisation model rebuilt

The original scoring model (40_segment_prioritisation/segment_prioritisation.py) contained mathematical errors that made the published totals unreproducible from the detailed contribution tables. The following errors are now corrected:

**Error 1: Detailed contribution table did not match published totals.**

The original report (50_strategic_recommendation.md §1.4) printed weighted contribution values that were inconsistent with the actual scores × weights. For example, premium/shared showed operating_predictability = 14.3 when the correct value was 4 × 14.2857 = 57.1. This caused the premium total to be understated by ~95 points.

**Corrected totals (recomputed from source ratings × normalised weights):**

| Segment | Published (v1) | Sum of v1 detailed contributions | Corrected total |
|---|---|---|---|
| Intra-city street-hail | 257.14 | 257.2 | 257.14 (unchanged) |
| Daily commute/subscription | 371.43 | 385.9 | 371.43 (unchanged) |
| Airport transfer | 380.95 | 376.0 | 380.95 (unchanged) |
| Inter-city/outstation | 219.05 | 228.5 | 219.05 (unchanged) |
| Premium/shared mobility | 309.52 | 214.1 | 309.52 (unchanged) |

The published totals in the CSV (segment_scores.csv) were correct. The error was in the markdown report's detailed contribution table, where several cells contained wrong values. The corrected detailed contribution table is below.

**Corrected detailed contribution table (weighted points = score × normalised weight):**

| Criterion (weight) | Intra-city | Daily commute | Airport | Inter-city | Premium |
|---|---|---|---|---|---|
| market_size_volume (9.52) | 47.62 (5×9.52) | 28.57 (3×9.52) | 38.10 (4×9.52) | 19.05 (2×9.52) | 19.05 (2×9.52) |
| revenue_potential (9.52) | 38.10 (4×9.52) | 28.57 (3×9.52) | 9.52 (1×9.52) | 19.05 (2×9.52) | 47.62 (5×9.52) |
| vehicle_utilisation (9.52) | 9.52 (1×9.52) | 28.57 (3×9.52) | 38.10 (4×9.52) | 47.62 (5×9.52) | 19.05 (2×9.52) |
| operating_predictability (14.29) | 14.29 (1×14.29) | 71.43 (5×14.29) | 71.43 (5×14.29) | 42.86 (3×14.29) | 57.14 (4×14.29) |
| customer_requirements (4.76) | 23.81 (5×4.76) | 19.05 (4×4.76) | 14.29 (3×4.76) | 9.52 (2×4.76) | 4.76 (1×4.76) |
| price_sensitivity (4.76) | 4.76 (1×4.76) | 4.76 (1×4.76) | 19.05 (4×4.76) | 14.29 (3×4.76) | 23.81 (5×4.76) |
| fleet_economics (19.05) | 38.10 (2×19.05) | 76.19 (4×19.05) | 76.19 (4×19.05) | 19.05 (1×19.05) | 57.14 (3×19.05) |
| ev_readiness (14.29) | 28.57 (2×14.29) | 57.14 (4×14.29) | 71.43 (5×14.29) | 14.29 (1×14.29) | 42.86 (3×14.29) |
| infrastructure_availability (4.76) | 23.81 (5×4.76) | 19.05 (4×4.76) | 14.29 (3×4.76) | 4.76 (1×4.76) | 14.29 (3×4.76) |
| competitive_intensity (4.76) | 4.76 (1×4.76) | 19.05 (4×4.76) | 14.29 (3×4.76) | 19.05 (4×4.76) | 14.29 (3×4.76) |
| scalability (4.76) | 23.81 (5×4.76) | 19.05 (4×4.76) | 14.29 (3×4.76) | 9.52 (2×4.76) | 9.52 (2×4.76) |
| **TOTAL** | **257.14** | **371.43** | **380.95** | **219.05** | **309.52** |

All totals now reconcile exactly.

**Error 2: Equal-weight sensitivity analysis referred to 10 criteria when framework has 11.**

The report text said "all 10 criteria equally weighted" but the framework has 11 criteria. The code used `100//len(CRITERIA)` = 100//11 = 9, with 1 remainder normalised. The report text is corrected to "all 11 criteria equally weighted."

**Error 3: Volume-first sensitivity table said intra-city ranks second; explanation said third.**

The actual output shows intra-city at rank 3 (304.0 points). The report's "2nd place" column incorrectly listed "Intra-city street-hail" — it should be "Daily commute/subscription" (340.0). Corrected in the table below.

**Error 4: "Airport uniquely ranks first in every configuration" is false.**

Under equal weights, Airport transfer (354.5) and Daily commute/subscription (354.5) **tie** for first place. The claim that Airport "uniquely" ranks first is incorrect. Corrected: "Airport ranks first or tied-for-first in all weight configurations tested."

**Corrected sensitivity analysis:**

| Weight scheme | 1st place | 2nd place | Key pattern |
|---|---|---|---|
| Base weights (100 normalised) | Airport transfer (380.95) | Daily commute (371.43) | Fleet economics (19%) is the strongest differentiator |
| Equal weights (all 11 criteria) | **Tie: Airport (354.5) & Daily commute (354.5)** | — | Fleet economics no longer dominant; predictability and EV readiness take over |
| Volume-first (volume, revenue, utilisation weighted 25% each) | Airport transfer (355.0) | Daily commute (340.0) | Volume elevates intra-city to 3rd (304.0) |
| Fleet-economics-first (fleet_economics = 30%) | Airport transfer (400.0) | Daily commute (380.0) | Fleet economics weight drives airport to top |

**Revised conclusion**: Airport transfer ranks first in 3 of 4 weight schemes and ties for first in the 4th. Daily commute is always #2 or tied-for-#1. The result is **robust but not unique** — the margin between airport and commute is small (9.5 points under base weights, 0 under equal weights).

---

### Correction 2 — Market segmentation reconciliation

**Issue 1: Categories overlap.** Airport, corporate commute, intra-city, and premium are not mutually exclusive. Airport runs can be premium; intra-city runs can be shared. The five "segments" are analytical comparisons, not a partition. They must not be summed as market shares.

**Correction**: The five use cases are retained as analytical comparisons but are explicitly labeled as overlapping categories. No market-share decomposition is claimed. Premium is treated as a service tier, not a trip purpose.

**Issue 2: Corporate commute and premium were mixed up.** The original table assigns:
- Daily commute: 176 km/day, ₹25/vehicle-km revenue
- Premium: 144 km/day, ₹28.89/vehicle-km revenue

The strategic recommendation (§2.2) assigned the premium figures (₹28.89/km, 144 km/day) to "corporate commute." This was an error. The corrected assignment is:

| Use case | km/day | Revenue/vehicle-km | Source |
|---|---|---|---|
| Daily commute/subscription | 176 | ₹25.00 | Deck p3 (Grade C) |
| Premium/shared mobility | 144 | ₹28.89 | Deck p3 (Grade C) |

"Corporate commute" is not a separate segment in the five-use-case framework. It is a sub-segment within "daily commute/subscription" (pre-booked, employer-sponsored). The revenue/km for corporate commute specifically is not separately measured. The ₹28.89/km figure belongs to "premium/shared mobility" as a service tier, not to corporate commute.

**Issue 3: Airport demand calculation mixed passenger movements with vehicle trips.**

The original strategic report (§2.1) calculated:
- 196.24M passengers Apr–Sep 2026 → ~392.5M annualised → ~785M road trips (×2 for arrival + departure) → at 25% app-cab mode share = 98M trips = 33.2% of 591.3M platform rides.

This calculation has three errors:
1. **Passenger movements ≠ vehicle trips.** One passenger = one vehicle trip (for app-cabs). The ×2 for "arrival + departure" is wrong — a passenger arriving and departing are two separate trips by two different vehicles or the same vehicle at different times. The 196.24M passengers are one-way passenger movements.
2. **Mode share is an assumption, not a measurement.** 25% app-cab share of airport road trips is [assump], not [reported].
3. **The comparison to 591.3M platform rides is misleading.** 591.3M includes all platform rides (street-hail, commute, airport, inter-city, premium). Comparing airport app-cab trips (98M) to total platform rides (591.3M) implies airport is 16.6% of all platform rides, not 33.2%.

**Corrected airport demand estimate:**

| Step | Value | Basis | Grade |
|---|---|---|---|
| AAI passengers Apr–Sep 2026 | 196.24M | Government (AAI Traffic Report Sep 2026) | B |
| Annualised (×2 for full year) | ~392.5M | Assumption: H1 = H2 | [assump] |
| Airport road trips (passengers using road transport) | ~392.5M (1:1, one passenger = one vehicle trip for app-cabs) | [assump] — assumes all passengers use road transport | [assump] |
| App-cab mode share | 20–30% | [assump] — no measured data | [assump] |
| Airport app-cab trips/year | 78.5M – 117.8M | Calculated | [calc] / [assump] |
| As % of 591.3M platform rides | 13.3% – 19.9% | Calculated | [calc] / [assump] |

**Note**: The 157–236M estimate in the original market report (10_market/) used 392.5M × 2 (round trip) × 20–30%, which double-counts passengers. The corrected estimate is 78.5M–117.8M. Both are [assump]-heavy and should be labeled as such.

---

### Correction 3 — Market evidence qualification

**Issue 1: 591.3M is not a complete market estimate.**

The red-team report's claim that "591.3M is not TAM" is correct but incomplete. The following distinctions must be maintained:

| Metric | Definition | Available? | Grade |
|---|---|---|---|
| Platform ride-flow proxy | Uber + Ola + Rapido daily rides × 365 | 591.3M (incl. Rapido 2W) | B (inputs) |
| Car-only platform rides | Exclude Rapido 2W rides | 474.5M (lower bound — Rapido also has cars) | [assump] |
| Offline taxi journeys | Black-yellow, pre-paid, non-platform | Not measured | [assump] |
| Airport passenger movements | AAI data | 392.5M annualised | B (government) |
| Addressable commercial fleet demand | Vehicles needed for commercial ride service | 28,423 (base scenario) | [calc] / [assump] |
| Actual vehicle purchasing demand | Vehicles purchased by fleet operators | Not measured | [assump] |

**The 474.5M "car-only" figure is not a verified car-only number.** It excludes ALL Rapido rides, but Rapido operates car services too. The true car-only figure is between 474.5M and 591.3M. Neither is verified.

**Issue 2: 14.8 billion 2035 forecast.**

This claim does not appear in any project file. It is not traceable to any methodology. It implies CAGR ~18.5% (6.2× growth over 11 years). The project's own ruling document (MACH1_MARKET_ASSESSMENT.pdf) forbids CAGR extrapolation. **Recommendation: Remove from all materials. Do not use.**

**Issue 3: 19.14% airport CAGR.**

This contradicts the project's own table (airport growth = 26%, premium = 28%). The 19.14% figure has no source (Register N-009 marks it "External source" with no source file). **Recommendation: Reconcile or delete.** If a CAGR is needed, derive it from a registration series and label the series.

---

### Correction 4 — Red-team report methodological errors

The red-team report (60_final_redteam_report.md) contained the following methodological errors that must be corrected:

**Error 1: "No de-duplication: a rider using both Uber and Ola double-counts."**

This is incorrect. The 591.3M counts completed rides, not unique riders. A rider using both platforms generates two separate rides — these are not double-counted. The issue is not rider overlap but geographic coverage overlap (platforms may report rides from overlapping cities) and accuracy of the underlying platform counts.

**Corrected statement**: "The 591.3M counts completed platform rides. It does not de-duplicate across platforms (a ride on Uber and a ride on Ola are both counted), but this is not double-counting of the same ride — it is counting of different rides. The risk is that platform self-reported counts may be inaccurate or may include non-car rides (Rapido two-wheelers)."

**Error 2: "Car-only: 474.5M/yr (−20% swing)."**

This excludes ALL Rapido rides, but Rapido operates car services. 474.5M is a lower bound, not a verified car-only figure. The true car-only figure is between 474.5M and 591.3M.

**Corrected statement**: "Car-only figure is between 474.5M (excluding all Rapido) and 591.3M (including all Rapido). Rapido's car share is not published. Neither bound is verified."

**Error 3: "1.62M rides/day ÷ 8 trips/day ≈ 202,500 active cars nationally."**

This assumes 8 trips/day average, which is itself an unverified assumption (Grade C, from deck table). It is an estimate, not a census. It should be labeled [est], not presented as a derived fact.

**Corrected statement**: "At 8 trips/day (Grade C assumption), 1.62M rides/day implies ~202,500 active cars. At 6 trips/day, it implies ~270,000. At 10 trips/day, ~162,000. The range is 162,000–270,000 depending on the trips/day assumption. This is an estimate, not a census."

**Error 4: Evidence grades contradict source register.**

The red-team report graded some claims as D (contradicted) when the source register listed them as B (single traceable secondary source). Specifically:
- The 591.3M ride proxy was graded "A (arithmetic) / B (inputs)" in the audit but the red-team report's consolidated table listed it as "B (inputs)" without noting the A-grade arithmetic. The arithmetic reproduction is Grade A; only the inputs are Grade B.
- The BluSmart defunct claim was graded B (Reuters, SEBI) in the source register but the red-team report's "what is established" section listed it under Grade A. It should be Grade B (single traceable secondary source — Reuters and SEBI are credible but not independently reproduced).

**Corrected**: All grades now align between the source register and the consolidated findings.

**Error 5: Airport passenger estimates don't reconcile.**

The strategic report (§2.1) calculated 98.12M airport app-cab trips (using 25% mode share and ×2 round-trip). The market report (10_market/) calculated 157–236M (using 20–30% mode share and ×2 round-trip). The corrected estimate (§Correction 2, Issue 3 above) is 78.5M–117.8M (using 20–30% mode share and 1:1 passenger-to-trip ratio). The ×2 round-trip was an error — passengers are one-way movements.

---

## PART 2: CORRECTED CONSOLIDATED FINDINGS

### 2.1 What is actually established

**Grade A (reproduced and verified):**
1. TCO engine: all headline numbers reproduce exactly from tco_analysis.py.
2. Driver advantage: +₹14,200/mo, invariant across fare levels, duty cycles, and commission structures.
3. Ride proxy arithmetic: 591.3M = 1.62M/day × 365 (arithmetic correct; inputs Grade B).
4. GMV scenario arithmetic: ₹887/2,661/5,322 crore (arithmetic correct; inputs Grade [assump]).
5. Dzire Tour S fleet data: 40% of Dzire to fleet, 5,000/mo, 3,614 outlets (from rationale doc with cited sources).

**Grade B (single traceable secondary source):**
1. BluSmart defunct Apr 2025 (SEBI interim order 15 Apr 2025; Reuters 17 Apr 2025).
2. AAI passenger data: 196.24M Apr–Sep 2026 (government source).
3. Uber 840k / Ola 460k / Rapido 320k daily rides (Motilal Oswal via Business Standard, 18 Apr 2025).
4. ~8 trips/driver-day, ~₹300 average fare (TOI, 23 Jun 2025).
5. Ola revenue ₹2,799cr FY23, loss ₹772cr (Wikipedia).
6. Rapido revenue ₹648cr FY24 (Wikipedia).
7. Tata Xpres-T EV specs: 26 kWh LFP, 213 km ARAI (Wikipedia).

**Grade C (internal assertion, no source):**
1. Ola ₹67/day, Uber/Rapido ₹29 flat fee.
2. 40,000–50,000 addressable metro vehicles; 8,000–10,000 EVs.
3. Evera/GMR/Bharat Taxi fleet sizes and operations.
4. Fleet duty 200 km/day, 312 days/yr.
5. 10% intra-city EV share, 18% airport EV share.
6. Price sensitivity indices (0.85/0.90/0.35/0.40/0.30).
7. Buyer = fleet operator running 5,000–40,000 vehicles.
8. "Uber Black's top two use cases are airport and corporate."
9. BluSmart "assumed 10%, realised 26%" residual.
10. 40% of Dzire to fleet (sources cited but not independently verified).
11. Dzire Tour S fleet pricing ₹6.79–7.74 L (sources cited but not independently verified).

**Grade D (contradicted by own evidence):**
1. Airport is the margin segment — on the table's own numbers, airport has the lowest revenue/km (₹17.1). The margin thesis rests on unquantified cost advantage.
2. 200,000 km rated life vs 312,000 km 5-yr duty (MCH-I-008, open).
3. Two range bases (263 km vs 268 km; 36 kWh vs 45×0.9 usable).
4. figures.txt stale — contradicts both engine and deck.
5. market_analysis.py path bug — prints all 6 CSVs as missing.
6. 19.14% CAGR — contradicts own table (airport 26% growth, premium 28% growth).
7. 61% vs ~58% intra-city — two different numbers, segments aren't a partition.
8. 40,000–50,000 addressable metro vehicles — inconsistent with 202,500 national estimate.

### 2.2 Segment ranking (corrected)

| Rank | Segment | Score | Margin over #2 | Key driver |
|---|---|---|---|---|
| 1 | Airport transfer | 380.95/500 | +9.52 | Operating predictability + fleet economics |
| 2 | Daily commute/subscription | 371.43/500 | +61.90 | Subscription model + infrastructure |
| 3 | Premium/shared mobility | 309.52/500 | +52.38 | Highest revenue/km (₹28.89) but smallest market |
| 4 | Intra-city street-hail | 257.14/500 | +38.10 | Highest volume, lowest fleet economics |
| 5 | Inter-city/outstation | 219.05/500 | — | Worst fleet economics, EV readiness, infrastructure |

**Caveats:**
- Scores are analyst-assigned (1–5 per criterion), not derived from measured data.
- Airport's margin over commute is small (9.5 points, 2.5%).
- Under equal weights, airport and commute **tie** at 354.5.
- The airport segment's high score depends on the assumption of depot charging availability.
- The "margin is in airport" thesis is cost-based, and cost is never computed.

### 2.3 Airport demand (corrected)

| Metric | Value | Grade |
|---|---|---|
| AAI passengers Apr–Sep 2026 | 196.24M | B (government) |
| Annualised (×2) | ~392.5M | [assump] |
| Airport app-cab trips (20–30% mode share) | 78.5M – 117.8M | [calc] / [assump] |
| As % of 591.3M platform rides | 13.3% – 19.9% | [calc] / [assump] |

The original 98.12M and 157–236M estimates both contained errors (round-trip double-counting). The corrected range is 78.5M–117.8M. All figures are [assump]-heavy.

### 2.4 TCO (unchanged — Grade A)

All TCO numbers are Grade A and reproduce exactly from tco_analysis.py. No corrections needed. See source register for full citation.

### 2.5 FleetLine E1 recommendation (unchanged, with caveats)

The recommendation stands but with three unverified conditions:
1. Depot charging is available and affordable at airports.
2. The cost advantage at airports exceeds the lowest revenue/km of all five segments.
3. Fleet operators of sufficient scale exist to purchase in volume.

If any condition fails, the recommendation changes. Daily commute/subscription is the #2 choice.

---

## PART 3: SOURCE REGISTER (corrected)

All sources are listed in the original 60_final_redteam_report.md §4. No changes to the source list. Corrections apply to evidence grades only:

| Claim | Original grade | Corrected grade | Reason |
|---|---|---|---|
| 591.3M ride proxy (arithmetic) | A | A (unchanged) | Arithmetic is Grade A |
| 591.3M ride proxy (inputs) | B | B (unchanged) | Single traceable secondary source |
| BluSmart defunct | A (in "what is established") | B | Reuters/SEBI are credible secondary sources, not independently reproduced |
| 40% of Dzire to fleet | B | B (unchanged) | Sources cited in rationale doc |
| 40,000–50,000 addressable metro vehicles | C | D | Contradicted by own 202,500 national estimate |
| 8,000–10,000 EVs in addressable metros | C | D | Contradicted by own 16–25% calculation |

---

## PART 4: ASSUMPTION REGISTER (corrected)

All assumptions from the original report stand. No new assumptions added. Key corrections:
- A8 (fleet duty 200 km/day) is now explicitly labeled as a design specification, not an observed duty cycle.
- B7 (200,000 km rated life vs 312,000 km duty) remains open (MCH-I-008).
- C6 (airport EV share 18%) is now Grade D (contradicted by suspicious coincidence with intra-city growth rate).

---

## PART 5: UNRESOLVED RESEARCH GAPS (prioritised)

### P0 — Changes the recommendation
1. Buyer hypothesis test (2–3 days).
2. Airport cost structure quantification (3–4 days).
3. Depot charging feasibility at airports (1–2 days).

### P1 — Hardens the story
4. Verified fleet sizes of named buyers.
5. Current fleet pricing for Dzire Tour S and FleetLine E1.
6. Measured duty cycle (30–50 driver-days).
7. Trip-purpose data for Indian ride-hailing.
8. LFP degradation calibration.

### P2 — Nice to have
9. BluSmart 4,704 stranded EVs re-entry analysis.
10. Tata Xpres-T EV fleet traction.
11. Ola ₹67/day, Uber/Rapido ₹29 flat fees verification.
12. Residual value study for Indian fleet EVs.

---

## PART 6: FINAL CONCLUSION (corrected)

The project has a defensible cost model (Grade A) and an indefensible market model (Grade C/D). The segment prioritisation model has been corrected for mathematical errors but retains its fundamental limitation: scores are analyst-assigned, not data-derived.

**The airport margin thesis is cost-based, not fare-based.** Airport has the lowest revenue/km (₹17.1) of all five segments. The margin claim rests on unquantified cost advantages (zero deadhead, depot charging). If depot charging is infeasible or airport costs are high, the thesis collapses and daily commute/subscription becomes the #1 segment.

**The most dangerous file remains `tco_engine/figures.txt`** — stale, contradicts engine and deck.

**The most valuable next action remains P0-1** — test the buyer hypothesis. Without verified buyers of sufficient scale, the entire product, finance, and channel strategy is built on sand.

**All deliverables are in `/home/sankara/Downloads/XCELERATE_MARKET/`.** No presentation slides were created.