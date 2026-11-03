# CORRECTED FINAL MARKET RESEARCH REPORT — v3

## Maruti Suzuki XCELerate 2026 E-Track: Designing the Ideal Ride-Service Vehicle for India 2035

**Date**: 3 November 2026 (v3 — incorporating detailed red-team reconciliation)
**Analyst**: Independent review, corrected per consolidated findings

---

## PART 1: CORRECTIONS TO PRIOR WORK

### 1.1 Segment prioritisation model — corrected

The original scoring model (40_segment_prioritisation/segment_prioritisation.py) contained mathematical errors. The following are now corrected:

**Corrected totals (recomputed from source ratings × normalised weights):**

| Segment | Score (/500) | Margin over #2 | Key driver |
|---|---|---|---|
| Airport transfer | 380.95 | +9.52 | Operating predictability + fleet economics |
| Daily commute/subscription | 371.43 | +61.90 | Subscription model + infrastructure |
| Premium/shared mobility | 309.52 | +52.38 | Highest revenue/km (₹28.89) but smallest market |
| Intra-city street-hail | 257.14 | +38.10 | Highest volume, lowest fleet economics |
| Inter-city/outstation | 219.05 | — | Worst fleet economics, EV readiness, infrastructure |

**Note on rounding**: The two-decimal contributions in the displayed table do not sum exactly to every displayed total. For example, Airport's displayed contributions sum to 380.98, while its total is 380.95. This is a rounding discrepancy in display only. The unrounded values reconcile exactly. The normalised weights are derived from exact proportions 2:2:2:3:1:1:4:3:1:1:1 (summing to 21), not from the rounded percentages shown.

**Sensitivity analysis — corrected and rebuilt:**

The original sensitivity analysis contained a mathematically impossible result (Airport volume-first score of 355.0, which exceeds the maximum possible of 350 under the stated scheme). The following corrected analysis uses explicit weight vectors.

**Base weights (weights as normalised from proportions 2:2:2:3:1:1:4:3:1:1:1):**

| Criterion | Weight | Intra-city | Commute | Airport | Inter-city | Premium |
|---|---|---|---|---|---|---|
| market_size_volume | 9.52% | 5 | 3 | 4 | 2 | 2 |
| revenue_potential | 9.52% | 4 | 3 | 1 | 2 | 5 |
| vehicle_utilisation | 9.52% | 1 | 3 | 4 | 5 | 2 |
| operating_predictability | 14.29% | 1 | 5 | 5 | 3 | 4 |
| customer_requirements | 4.76% | 5 | 4 | 3 | 2 | 1 |
| price_sensitivity | 4.76% | 1 | 1 | 4 | 3 | 5 |
| fleet_economics | 19.05% | 2 | 4 | 4 | 1 | 3 |
| ev_readiness | 14.29% | 2 | 4 | 5 | 1 | 3 |
| infrastructure_availability | 4.76% | 5 | 4 | 3 | 1 | 3 |
| competitive_intensity | 4.76% | 1 | 4 | 3 | 4 | 3 |
| scalability | 4.76% | 5 | 4 | 3 | 2 | 2 |
| **TOTAL** | **100%** | **257.14** | **371.43** | **380.95** | **219.05** | **309.52** |

**Equal weights (all 11 criteria at 9.09% each):**

All criteria at 9.09%. Airport and Daily Commute both score 354.5 — a tie for first place. This is reproducible and correct.

**Volume-first (explicit weight vector):**

Weights: market_size_volume 25%, revenue_potential 25%, vehicle_utilisation 25%, and the remaining 8 criteria sharing 25% equally (3.125% each).

| Segment | Recomputed score | Rank |
|---|---|---|
| Airport transfer | 318.75 | 1st (tied) |
| Daily commute/subscription | 318.75 | 1st (tied) |
| Intra-city street-hail | 318.75 | 1st (tied) |
| Premium/shared mobility | 300.00 | 4th |
| Inter-city/outstation | 278.13 | 5th |

*Note: This is one specific interpretation of "volume-first." The original report's claimed Airport score of 355.0 is impossible under any valid interpretation of the stated scheme, because Airport's three volume/revenue/utilisation scores (4+1+4 = 9) × 25% = 225 points, and the remaining 8 criteria can contribute at most 125 points, for a maximum of 350. The original 355.0 was an arithmetic error. Under the equal-distribution interpretation above, three segments tie at 318.75.*

**Fleet-economics-first (explicit weight vector):**

Weights: fleet_economics 30%, and the remaining 10 criteria sharing 70% proportionally to their base weights (i.e., each other criterion's weight = base_weight × 0.70/0.8095).

| Segment | Recomputed score | Rank |
|---|---|---|
| Airport transfer | 383.53 | 1st |
| Daily commute/subscription | 375.29 | 2nd |
| Premium/shared mobility | 308.24 | 3rd |
| Intra-city street-hail | 249.41 | 4th |
| Inter-city/outstation | 202.94 | 5th |

*Note: This does not reproduce the original report's claimed 400.0/380.0. The original figures used an unspecified method. The proportional-rescaling method above is the most defensible interpretation and produces the scores shown. The original 400.0/380.0 should be withdrawn.*

**Revised sensitivity conclusion:**

Airport narrowly leads under base weights (380.95 vs 371.43, margin 9.52 points / 2.5%). Under equal weights, Airport and Daily Commute tie at 354.5. Under volume-first, three segments tie. Under fleet-economics-first, Airport leads but the published original figures (400.0/380.0) do not reproduce.

**The claim "robust but not unique" is withdrawn.** The correct statement is: "Airport narrowly leads under the base weighting and ties with Daily Commute under equal weighting. The alternative weighting tests have not been fully reconciled, so ranking robustness has not been established."

**Rating sensitivity test (new — not previously performed):**

The base-case lead is only 9.52 points. One rating-point change in a criterion weighted at 9.52% is enough to erase that lead. The scores are analyst-assigned (1–5 per criterion), not derived from measured data. The following test varies each segment's rating by ±1 on its weakest criterion (the criterion where it scores lowest relative to its nearest competitor) and re-ranks:

| Perturbation | Airport score | Commute score | Leader |
|---|---|---|---|
| Base (no change) | 380.95 | 371.43 | Airport (+9.52) |
| Airport fleet_economics 4→3 | 361.90 | 371.43 | Commute (+9.52) |
| Airport operating_predictability 5→4 | 366.67 | 371.43 | Commute (+4.76) |
| Commute operating_predictability 5→4 | 380.95 | 357.14 | Airport (+23.81) |
| Commute fleet_economics 4→3 | 380.95 | 352.38 | Airport (+28.57) |

**Conclusion**: The airport lead is fragile. A single rating-point reduction on Airport's two strongest criteria (fleet economics or operating predictability) flips the ranking to Daily Commute. The model tests weight sensitivity but not rating sensitivity. Until rating sensitivity is tested and documented, the score difference should not be described as robust.

### 1.2 Market segmentation — corrected

**Issue: Categories overlap.** Airport, corporate commute, intra-city, and premium are not mutually exclusive. Airport runs can be premium; intra-city runs can be shared. The five "segments" are analytical comparisons, not a partition. They must not be summed as market shares.

**Correction**: The five use cases are retained as analytical comparisons but are explicitly labeled as overlapping categories. No market-share decomposition is claimed. Premium is treated as a service tier, not a trip purpose.

**Issue: Corporate commute and premium were mixed up.** The original table assigns:
- Daily commute: 176 km/day, ₹25/vehicle-km revenue
- Premium: 144 km/day, ₹28.89/vehicle-km revenue

The strategic recommendation (§2.2) assigned the premium figures (₹28.89/km, 144 km/day) to "corporate commute." This was an error. The corrected assignment:

| Use case | km/day | Revenue/vehicle-km | Source |
|---|---|---|---|
| Daily commute/subscription | 176 | ₹25.00 | Deck p3 (Grade C) |
| Premium/shared mobility | 144 | ₹28.89 | Deck p3 (Grade C) |

"Corporate commute" is not a separate segment in the five-use-case framework. It is a sub-segment within "daily commute/subscription" (pre-booked, employer-sponsored). The revenue/km for corporate commute specifically is not separately measured. The ₹28.89/km figure belongs to "premium/shared mobility" as a service tier, not to corporate commute.

**Issue: Inter-city distance arithmetic.** The original table gives 280 km average trip distance and 1.5 trips/day, implying 420 km/day. But it lists 340 km/day. This is an internal inconsistency.

If 340 km/day is correct, the revenue/km is ₹18.53/km (₹6,300/day ÷ 340 km). If 420 km/day is correct, the revenue/km is ₹15.00/km (₹6,300/day ÷ 420 km). The inter-city revenue/km is therefore either ₹15.00 or ₹18.53, not a single established figure. This must be resolved before any inter-city comparison is used.

**Issue: DRIVER ₹/MO is gross fare revenue, not take-home.** The values in the original table are trips/day × fare × 26. For example, 8 daily trips at ₹550 over 26 days gives ₹114,400. This is gross fare revenue generated, not driver take-home income. It must be labeled accordingly, with commissions, costs, financing, work hours and downtime distinguished from net earnings.

**Issue: Airport demand calculation mixed passenger movements with vehicle trips.**

The original strategic report calculated:
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
| Airport app-cab passenger journeys/year | 78.5M – 117.8M | Calculated | [calc] / [assump] |
| As % of 591.3M platform rides | 13.3% – 19.9% | Calculated | [calc] / [assump] |

**Conversion to vehicle trips (missing — must be added before use):**

The 78.5M–117.8M figure counts passenger journeys, not vehicle trips. To convert to vehicle trips:

\[
\text{App-cab vehicle trips} = \frac{\text{airport passenger movements} \times \text{eligible passenger share} \times \text{app-cab passenger mode share}}{\text{average passengers per app-cab vehicle}}
\]

Each term needs a defined source or an explicit assumption. The missing conversions are:
1. **Eligible passenger share**: Not every passenger movement represents a city-side ground journey. Direct-transit passengers do not leave the airport. Transfer passengers may remain within the airport system. The AAI data distinguishes terminating, transfer and direct-transit passengers (direct-transit counted once).
2. **Occupancy**: One passenger ≠ one vehicle. Several passengers may share one cab. If the mode share is passenger-based, the result is app-cab passenger journeys; to estimate vehicle trips, divide by average passengers per booked vehicle.

For illustration only: if the 78.5M–117.8M passenger-journey estimate were divided by an assumed occupancy of 1.4 passengers per cab, it would become approximately 56–84 million vehicle trips. This is not a replacement estimate; it shows how materially the missing occupancy assumption can change the answer.

**The comparison with 591.3M platform rides should be removed.** The annualised 2026 airport estimate and the 2025 platform ride proxy are different periods, and one is a passenger-based estimate while the other is a ride count. The resulting 13.3–19.9% share should not be used.

**Recommendation**: Retain the AAI data as an airport-demand indicator, but rename the current 78.5M–117.8M figure to "modelled airport app-cab passenger journeys under a 20–30% assumed mode share." Do not call it vehicle trips until the occupancy and eligible-passenger conversions are done.

### 1.3 Market evidence qualification — corrected

**591.3M is an annualised run-rate, not an observed annual total.**

The arithmetic is straightforward: (840,000 + 460,000 + 320,000) × 365 = 591.3M. The underlying daily counts are attributed to Motilal Oswal's January 2025 research and reported by Business Standard. They are reported daily ride figures, not an independently measured total of all Indian car trips over a completed year. Multiplying them by 365 creates an annualised run-rate, not an observed annual total.

The revised report is right to avoid calling this TAM. However, its proposed car-only range of 474.5M–591.3M is still not established. Excluding every Rapido ride does not prove that the Uber and Ola counts contain only cars. The service-mode definitions must be verified across all three inputs.

**External cross-check (Redseer, May 2026)**: A Business Standard report citing Redseer put Indian ride-hailing at approximately 3 billion trips in CY2025, with cabs contributing 27%, two-wheelers 28–30%, and autos around 45%. That implies roughly 810 million cab trips under that source's definitions. It is not directly comparable to the Motilal Oswal proxy (different definitions, different periods), but the difference is large enough that the report should explain the coverage and methodology rather than quietly rely on 591.3M as its main national proxy.

**202,500 is implied active driver-day equivalents, not active cars.**

The calculation: 1.62M rides/day ÷ 8 trips/day = 202,500. This produces an implied number of driver-day equivalents, conditional on the assumption of eight rides per driver-day. It does not establish the number of active cars.

Two problems:
- The numerator does not have a verified four-wheeler-only service-mode split.
- The denominator is a driver-day assumption. One vehicle may be used by multiple drivers or shifts, and one driver may not correspond to one distinct vehicle.

The sensitivity range of 162,000–270,000 at 10 to 6 trips/day is useful as a mathematical scenario, but it is not a fleet census. The trips/day figure is Grade C (from deck table, no source). The result should be renamed "implied active driver-day equivalents" and only calculated as active cars after obtaining mode-specific ride volumes and vehicle-shift utilisation.

**40,000–50,000 metro vehicles and 8,000–10,000 EVs: unverified, not contradicted.**

The report downgraded these to Grade D because they conflict with the 202,500 national estimate. This is not a demonstrated contradiction. A 40,000–50,000 metro subset could be part of a larger national population. More importantly, the 202,500 figure is not a verified active-car count in the first place.

The EV arithmetic is also not contradictory: 16–25% of 40,000–50,000 gives a broad range of 6,400–12,500. An estimate of 8,000–10,000 falls inside it.

Both the metro vehicle estimate and EV estimate may be unsupported. That makes them unverified, not contradicted. Grade D is too strong. **Corrected grade: C (unverified internal assertion).**

**14.8 billion 2035 forecast.**

This claim does not appear in any project file. It is not traceable to any methodology. It implies CAGR ~17.98% (not 18.5% — the arithmetic gives approximately 17.98% over 11 years). The project's own ruling document (MACH1_MARKET_ASSESSMENT.pdf) forbids CAGR extrapolation. **Recommendation: Remove from all materials. Do not use.**

**19.14% airport CAGR.**

This may disagree with the 26% table figure, but the report has not shown that both numbers measure the same thing over the same period. Calling it contradicted is stronger than the evidence permits. **Corrected: Unverified, not contradicted. Remove until its source, metric and time window are established.**

### 1.4 Evidence grading — corrected

**Three-grade contradiction for 40% Dzire fleet.**

The claim that 40% of Dzire vehicles go to fleet use appears as:
- Grade A in "established findings"
- Grade C in "internal-assertion list"
- Grade B in "corrected source register"

These classifications cannot all be true. The report must settle on one grade and explain precisely what was verified. **Corrected: Grade B (single traceable secondary source).** The rationale document cites sources but they were not independently verified. The claim is "sources cited but not independently verified" — a Grade B with a caveat, not Grade A.

**Grade D for claims that are merely unsourced or based on different denominators.**

The following Grade D classifications should be changed:

| Claim | v2 treatment | Corrected treatment |
|---|---|---|
| Airport EV share of 18% | D (suspicious coincidence) | C / unverified — a suspicious coincidence is not evidence of falsification |
| 40–50k metro vehicles | D (contradicted by national estimate) | C / unverified — not proven contradictory |
| 8–10k metro EVs | D (contradicted by 16–25% calculation) | C / unverified — arithmetic does not contradict the stated range |
| Airport is the margin segment | D (lowest revenue/km) | Unproven, not disproven — see §1.5 |
| 61% vs ~58% intra-city | D | Unreconciled definitions and denominators — not a contradiction |
| 19.14% CAGR vs 26% growth | D | Unreconciled until metric and time windows are shown |

**Grade system: separate source quality from calculation quality.**

The report describes Grade B as "single traceable secondary source" yet puts official AAI data under Grade B. The clean solution is to separate two concepts:

1. **Source quality**: official primary data (government statistics, regulatory filings), company-reported data, credible secondary reporting (Reuters, Business Standard), internal assertion, or unsupported.
2. **Calculation quality**: reproduced (arithmetic verified), partially reproduced (some inputs unverified), assumption-dependent (key inputs are assumptions), or not reproducible (method unclear).

The 591.3M calculation demonstrates why: its arithmetic can be reproduced (Grade A calculation) even though the input data and market coverage are uncertain (Grade B source). Apply this distinction consistently.

### 1.5 Airport margin thesis — corrected

The v2 report correctly recognises that Airport has the lowest revenue per vehicle-kilometre in the five-use-case table. It then treats the airport margin claim as contradicted by this figure. **This conclusion goes too far in the opposite direction.**

Revenue per kilometre is not profit per kilometre. Airport work could conceivably have better margins if it has lower empty running, more predictable bookings, less price sensitivity, better utilisation or a sufficiently favourable operating arrangement. But none of those advantages should be assumed.

The figures in the original segment table make the burden of proof clear:

| Use case | Gross revenue/day | km/day | Gross revenue/km |
|---|---|---|---|
| Airport | ₹3,600 | 210 | ₹17.14 |
| Daily commute | ₹4,400 | 176 | ₹25.00 |
| Premium/shared | ₹4,160 | 144 | ₹28.89 |

These are gross fare calculations, not margins. On the table's assumptions, Airport generates ₹800 less gross fare revenue per vehicle-day than Daily Commute and ₹560 less than Premium.

To beat Daily Commute on net contribution per vehicle-day, Airport needs to save at least ₹800/day in comparable costs. To beat Premium, it needs at least ₹560/day. These are useful hurdles for the market thesis; they are not proof that Airport cannot be profitable.

**Wording correction**: The v2 report said "the airport cost advantage must exceed the lowest revenue/km." These are not directly comparable quantities. The proper test is whether the net contribution per vehicle-day or per total vehicle-kilometre is better under matched operating assumptions.

**Classification (corrected):**
- "Airport has the highest margin": not established.
- "Airport may have a cost advantage under controlled operating conditions": plausible hypothesis.
- "Airport is superior to Daily Commute": not yet demonstrated by this market evidence.

The airport margin claim should be cross-referenced with the separate TCO work (which is Grade A). The market report should not claim "the whole project has no cost model" — the TCO engine exists and is defensible. The market report's job is to say the market evidence alone does not establish an airport margin advantage.

### 1.6 Segment model discipline — corrected

The report has fixed the overlap problem conceptually. It has not fully fixed the comparison problem. Airport, commute, intra-city, inter-city and premium are not five equivalent market categories:

- Airport is a trip purpose.
- Commute is a use case or contract type.
- Intra-city and inter-city describe geography.
- Premium describes service tier.

A premium airport transfer is simultaneously airport, intra-city and premium. A corporate commute can be intra-city and premium. The report now acknowledges this, but its score model still compares them as if each column represents a clearly bounded alternative.

**Required definitions (must be added before the model is used again):**

| Archetype | Definition (must be specified) |
|---|---|
| Airport transfer | All airport-related rides? Only pre-booked airport transfers? Operator-controlled airport fleets? |
| Daily commute/subscription | Individual subscriptions? Employee transport contracts? Both? |
| Intra-city street-hail | All non-pre-booked intra-city rides? Only street-hail? |
| Inter-city/outstation | All inter-city trips? Only outstation (round-trip)? |
| Premium/shared mobility | Premium service tier? Shared rides? Both? |

**Scoring direction must be defined for each criterion:**

| Criterion | Score of 5 means... | Score of 1 means... |
|---|---|---|
| market_size_volume | Largest market | Smallest market |
| revenue_potential | Highest revenue/km | Lowest revenue/km |
| vehicle_utilisation | Highest utilisation | Lowest utilisation |
| operating_predictability | Most predictable demand | Least predictable demand |
| customer_requirements | Easiest requirements to meet | Hardest requirements to meet |
| price_sensitivity | Lowest price sensitivity (least sensitive) | Highest price sensitivity |
| fleet_economics | Best fleet economics | Worst fleet economics |
| ev_readiness | Most EV-ready | Least EV-ready |
| infrastructure_availability | Best infrastructure | Worst infrastructure |
| competitive_intensity | Least competitive (easiest to enter) | Most competitive (hardest to enter) |
| scalability | Most scalable | Least scalable |

*Note: The direction for price_sensitivity and competitive_intensity is ambiguous in the original model. A score of 5 under price sensitivity could mean "high price sensitivity" (bad for operators) or "low price sensitivity" (good). The definition above assumes 5 = favourable (low sensitivity). This must be confirmed.*

**Vehicle utilisation criterion needs definition:**

Is it trips/day, paid kilometres/day, total vehicle kilometres/day, productive hours/day, or utilisation as a percentage of available hours? These measures can rank the same use cases differently. The inter-city segment's high utilisation score (5/5) is especially difficult to interpret without that definition, because inter-city has the fewest trips/day (1.5) but the highest km/day (340).

### 1.7 Inherited errors — corrected

**Inter-city distance arithmetic:**

The original table gives 280 km average trip distance and 1.5 trips/day, implying 420 km/day. But it lists 340 km/day. If 340 km/day is correct, the 280 km and 1.5 trips/day assumptions need explanation. This changes the gross revenue/km calculation from ₹18.53/km at 340 km/day to ₹15.00/km at 420 km/day. It also affects any utilisation comparison.

**DRIVER ₹/MO label:**

The values in the original table are trips/day × fare × 26. For example, 8 daily trips at ₹550 over 26 days gives ₹114,400. That is gross fare revenue generated, not take-home driver income. It needs to be labelled accordingly, with commissions, costs, financing, work hours and downtime distinguished from net earnings.

**14.8B 2035 forecast CAGR:**

The stated 18.5% implied CAGR is slightly wrong. The arithmetic gives approximately 17.98% over 11 years (14.8/2.4 = 6.167×; ln(6.167)/11 = 0.1798). The forecast should remain removed because it has no traceable source or methodology.

**19.14% airport CAGR:**

Should be removed until its source, metric and time window are established. It may disagree with the 26% table figure, but the report has not shown that both numbers measure the same thing over the same period. Calling it contradicted is stronger than the evidence permits.

---

## PART 2: CORRECTED CONSOLIDATED FINDINGS

### 2.1 What is actually established

**Source quality and calculation quality are graded separately.**

| Grade | Source quality | Calculation quality |
|---|---|---|
| A | Official primary (government stats, regulatory filings) | Reproduced (arithmetic verified by running code) |
| B | Credible secondary (Reuters, Business Standard, Wikipedia) | Partially reproduced (some inputs unverified) |
| C | Internal assertion (no source, or sources cited but not verified) | Assumption-dependent (key inputs are assumptions) |
| D | Contradicted by specific counter-evidence | Not reproducible (method unclear or arithmetic wrong) |

**Grade A (reproduced and verified):**
1. TCO engine: all headline numbers reproduce exactly from tco_analysis.py.
2. Driver advantage: +₹14,200/mo, invariant across fare levels, duty cycles, and commission structures.
3. Ride proxy arithmetic: 591.3M = 1.62M/day × 365 (arithmetic correct; inputs Grade B).
4. GMV scenario arithmetic: ₹887/2,661/5,322 crore (arithmetic correct; inputs Grade [assump]).

**Grade B (credible secondary source):**
1. BluSmart defunct Apr 2025 (SEBI interim order 15 Apr 2025; Reuters 17 Apr 2025).
2. AAI passenger data: 196.24M Apr–Sep 2026 (government source).
3. Uber 840k / Ola 460k / Rapido 320k daily rides (Motilal Oswal via Business Standard, 18 Apr 2025).
4. ~8 trips/driver-day, ~₹300 average fare (TOI, 23 Jun 2025).
5. Ola revenue ₹2,799cr FY23, loss ₹772cr (Wikipedia).
6. Rapido revenue ₹648cr FY24 (Wikipedia).
7. Tata Xpres-T EV specs: 26 kWh LFP, 213 km ARAI (Wikipedia).
8. Dzire Tour S: 40% of Dzire to fleet, 5,000/mo, 3,614 outlets (sources cited in rationale doc, not independently verified — Grade B with caveat).

**Grade C (internal assertion / unverified):**
1. Ola ₹67/day, Uber/Rapido ₹29 flat fee.
2. 40,000–50,000 addressable metro vehicles; 8,000–10,000 EVs (unverified, not contradicted).
3. Evera/GMR/Bharat Taxi fleet sizes and operations.
4. Fleet duty 200 km/day, 312 days/yr.
5. 10% intra-city EV share, 18% airport EV share.
6. Price sensitivity indices (0.85/0.90/0.35/0.40/0.30).
7. Buyer = fleet operator running 5,000–40,000 vehicles.
8. "Uber Black's top two use cases are airport and corporate."
9. BluSmart "assumed 10%, realised 26%" residual.
10. Dzire Tour S fleet pricing ₹6.79–7.74 L (sources cited but not independently verified).
11. 19.14% airport CAGR (unverified, not contradicted).

**Grade D (contradicted by specific counter-evidence):**
1. 200,000 km rated life vs 312,000 km 5-yr duty (MCH-I-008, open).
2. Two range bases (263 km vs 268 km; 36 kWh vs 45×0.9 usable).
3. figures.txt stale — contradicts both engine and deck.
4. market_analysis.py path bug — prints all 6 CSVs as missing.
5. 61% vs ~58% intra-city — two different numbers (unreconciled definitions, not a contradiction per se).

**What is NOT contradicted (corrected from v2):**
- "Airport is the margin segment" — unproven, not disproven. See §1.5.
- "40,000–50,000 addressable metro vehicles" — unverified, not contradicted.
- "8,000–10,000 EVs" — unverified, not contradicted.
- "19.14% airport CAGR" — unverified, not contradicted.

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
- Under volume-first weights, three segments tie at 318.75.
- Under fleet-economics-first weights, airport leads but original figures (400/380) do not reproduce.
- The airport segment's high score depends on the assumption of depot charging availability.
- The "margin is in airport" thesis is cost-based, and cost is never computed in the market model.
- A single rating-point reduction on Airport's fleet economics or operating predictability flips the ranking to Daily Commute.
- Rating sensitivity has not been formally tested or documented.

### 2.3 Airport demand (corrected)

| Metric | Value | Grade |
|---|---|---|
| AAI passengers Apr–Sep 2026 | 196.24M | B (government) |
| Annualised (×2) | ~392.5M | [assump] |
| Airport app-cab passenger journeys (20–30% mode share) | 78.5M – 117.8M | [calc] / [assump] |
| Airport app-cab vehicle trips (after occupancy conversion) | Not yet calculated | [assump] — occupancy data missing |

The original 98.12M and 157–236M estimates both contained errors (round-trip double-counting). The corrected passenger-journey range is 78.5M–117.8M. All figures are [assump]-heavy.

**Do not compare with 591.3M platform rides.** Different periods (2026 vs 2025), different units (passenger journeys vs completed rides).

### 2.4 TCO (unchanged — Grade A)

All TCO numbers are Grade A and reproduce exactly from tco_analysis.py. No corrections needed. Key results:
- Delhi 5-yr: ₹5.75/km EV vs ₹6.73/km CNG (+14.5% nominal, excl. charging infra)
- Incl. ₹99,000/vehicle infra: +6.5%
- NPV@12% escalated: +16.0% excl / +6.7% incl
- 8-yr: +28.0%/+17.4%/+25.3%/+14.6%
- City matrix 5-yr financed incl-NPV: Delhi +6.7, Mumbai +4.0, Bengaluru +0.9
- Exactly 1 negative cell of 48 (Bengaluru 5-yr cash NPV incl. infra, −0.4%)
- Driver advantage: +₹14,200/mo, invariant across fares ₹11/14/18/22 per km (+43.2%/+29.3%/+20.5%/+15.8%)
- EV residual 26% → 36% moves advantage from +14.5% to +20.6%
- Charger breakeven in Mumbai: ₹94k vs ₹99k assumed (knife-edge)

### 2.5 FleetLine E1 recommendation (with corrected caveats)

The recommendation stands but with four unverified conditions:
1. Depot charging is available and affordable at airports.
2. The cost advantage at airports exceeds the revenue gap (₹800/day vs commute, ₹560/day vs premium) in comparable economic units.
3. Fleet operators of sufficient scale exist to purchase in volume.
4. The airport margin thesis is demonstrated under real operating conditions, not just hypothesised.

If conditions 1–4 fail, daily commute/subscription becomes the #1 segment.

---

## PART 3: SOURCE REGISTER (corrected)

All sources from the original report stand. Evidence grades corrected per §1.4.

| Claim | Original grade | Corrected grade | Reason |
|---|---|---|---|
| 591.3M ride proxy (arithmetic) | A | A (unchanged) | Arithmetic is Grade A |
| 591.3M ride proxy (inputs) | B | B (unchanged) | Single traceable secondary source |
| BluSmart defunct | A (in "what is established") | B | Reuters/SEBI are credible secondary sources, not independently reproduced |
| 40% of Dzire to fleet | B | B (unchanged) | Sources cited in rationale doc, not independently verified |
| 40,000–50,000 addressable metro vehicles | C | C (unchanged) | Unverified, not contradicted |
| 8,000–10,000 EVs in addressable metros | C | C (unchanged) | Unverified, not contradicted |
| Airport is the margin segment | D | Unproven (not D) | Revenue/km ≠ profit/km; cost advantage unquantified |
| 19.14% airport CAGR | D | Unverified (not D) | Unreconciled, not contradicted |
| 61% vs ~58% intra-city | D | Unreconciled (not D) | Different denominators, not a contradiction |

---

## PART 4: ASSUMPTION REGISTER (corrected)

All assumptions from the original report stand. Key corrections:
- A8 (fleet duty 200 km/day) is now explicitly labeled as a design specification, not an observed duty cycle.
- B7 (200,000 km rated life vs 312,000 km duty) remains open (MCH-I-008).
- C6 (airport EV share 18%) is now Grade C (unverified), not Grade D.
- Airport demand (78.5M–117.8M) is now labeled "passenger journeys" not "vehicle trips."
- 202,500 is now labeled "implied active driver-day equivalents" not "active cars."

---

## PART 5: UNRESOLVED RESEARCH GAPS (prioritised)

### P0 — Changes the recommendation

**P0-1: Validate who actually buys the vehicle.**

Do not start from the assumption that one 5,000–40,000-vehicle fleet operator must exist. A viable market could be fragmented across many smaller operators. The relevant question is whether the total reachable annual procurement volume is large enough and whether you can access those buyers.

Map the roles separately:

| Role | What needs to be established |
|---|---|
| Asset owner | Who owns or leases the vehicle? |
| Procurement decision-maker | Who selects and approves the vehicle? |
| Fleet operator | Who controls schedules, routes and utilisation? |
| Service payer | Who pays for the ride or transport contract? |
| Driver | Who operates the vehicle and bears the day-to-day burden? |
| Gatekeeper | Who controls airport access, parking or charging? |
| Financier/leasing provider | Who enables the acquisition? |

Interview decision-makers from airport fleets, corporate transport contractors, smaller fleet owners and leasing/financing providers. Ask for actual fleet counts, annual additions and replacements, procurement batches, current operating arrangements, buying authority, financing preferences and expected vehicle utilisation.

A statement that someone "likes the concept" is weak evidence. A specific trial quantity, procurement timeline, budget, or willingness to issue a conditional letter of intent is much stronger.

**P0-2: Test the airport economics against commute using comparable units.**

Use the existing cost work rather than building another TCO model. The question for this market report is narrower: does the airport operating arrangement create enough additional benefit to offset the lower gross revenue figures?

The comparison must account for paid and empty kilometres, waiting and queue time, airport access and parking charges, contract or platform fees, duty hours and practical utilisation. Use the same definitions for Airport and Daily Commute.

**P0-3: Verify actual charging access.**

A charging station being near an airport does not mean the operator can use it. Obtain a site-specific answer on location, permitted vehicle access, charging rights, number of bays, power availability, tariff, operating hours, parking rights, who pays for the installation and who controls the facility.

A depot arrangement should be treated as real only when the access and commercial terms are established.

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

FleetLine E1 remains a credible candidate for airport-transfer and contracted-commute operations, but the market evidence does not yet establish that Airport is the superior beachhead.

Under the base prioritisation model, Airport narrowly leads Daily Commute (380.95 vs 371.43, margin 9.52 points / 2.5%). Under equal weighting, they tie at 354.5. The alternative sensitivity results still require reconciliation, and the analyst-assigned ratings need evidence and uncertainty testing.

Airport has lower gross fare revenue per kilometre than Daily Commute and Premium (₹17.14 vs ₹25.00 vs ₹28.89). Its potential advantage therefore depends on demonstrably lower operating costs, more predictable utilisation, lower empty running, or other verified fleet-level benefits. These benefits must be established under real airport operating and charging conditions. The required cost advantage is at least ₹800/day vs Daily Commute and ₹560/day vs Premium in comparable economic units.

The immediate decision is not to abandon Airport or to declare it the winner. It is to validate the buyer, operating arrangement and infrastructure access, while keeping contracted Daily Commute as the principal alternative.

The market model should be treated as a prioritisation hypothesis until those tests are complete.

The underlying strategic direction still makes sense as a hypothesis. What needs fixing now is the proof that this is the right initial customer and operating environment — not the entire vehicle concept.

**The most dangerous file remains `tco_engine/figures.txt`** — stale, contradicts engine and deck.

**The most valuable next action remains P0-1** — test the buyer hypothesis with specific evidence (trial quantities, procurement timelines, budgets, conditional letters of intent), not opinions.

**All deliverables are in `/home/sankara/Downloads/XCELERATE_MARKET/`.** No presentation slides were created.