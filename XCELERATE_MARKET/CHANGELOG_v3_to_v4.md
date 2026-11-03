# Change Log: v3 → v4

## What was corrected

### 1. Scoring model — verified and reproduced
- All 5 segment scores recomputed from ratings × weights using `segment_prioritisation_v4.py`. Results match: Airport 380.95, Commute 371.43, Premium 309.52, Intra-city 257.14, Inter-city 219.05.
- Decomposed why Airport beats Commute: +47.62 from 4 criteria (market_size +9.52, vehicle_utilisation +9.52, price_sensitivity +14.29, ev_readiness +14.29) vs −38.10 from 5 criteria (revenue −19.05, customer_req −4.76, infrastructure −4.76, competitive −4.76, scalability −4.76). Operating predictability and fleet economics are tied (0.00).
- Corrected the "355 is impossible" claim from v3: the volume-first weight scheme (market 25%, revenue 15%, util 15%, predictability 10%, fleet 10%, rest 3–5%) is internally consistent and produces 355.0. The reviewer's "max 350" was based on a different (incorrect) reading of the weights.
- Rating sensitivity test added: 5 single-point reductions on Airport flip the leader to Commute. This was not previously performed.
- All sensitivity outputs saved to CSV for reproducibility.

### 2. Market segmentation — defined with limitations
- Five archetypes defined with overlap explanation (airport = trip purpose, commute = use case, intra/inter-city = geography, premium = service tier).
- Premium/shared combination explained: premium is a service tier, not a trip purpose. ₹28.89/km belongs to premium, not corporate commute.
- Airport vs contracted corporate commute distinguished: airport is trip purpose, corporate commute is contract type. Revenue/km for corporate commute not separately measured.
- Limitation stated: archetypes are not clearly bounded; model is prioritisation of use-case archetypes, not a market partition.

### 3. Market sizing — verified calculations
- 591.3M arithmetic verified: (840k + 460k + 320k) × 365 = 591,300,000.
- 591.3M labeled as annualised run-rate, not observed annual total. Not a complete market estimate.
- 810M (Redseer) noted as alternative with different scope/period. Not forced into agreement.
- AAI 196.24M verified as reported (Grade B, government source). Annualised 392.5M labeled [assump].
- Airport app-cab passenger journeys 78.5M–117.8M labeled as passenger journeys, not vehicle trips. Occupancy conversion specified but not calculated (data missing).
- 202,500 renamed "implied active driver-day equivalents" not "active cars." Sensitivity range 162,000–270,000 noted.
- 40,000–50,000 and 8,000–10,000 graded C (unverified), not D (contradicted).
- 14.8B forecast: CAGR corrected to 17.98% (was 18.5%). Still removed.
- 19.14% airport CAGR: graded unverified, not contradicted.

### 4. Airport economics — corrected
- Revenue/km ≠ profit/km distinction stated explicitly.
- Paid-km vs total vehicle-km distinction noted (ranking unaffected).
- Hurdle calculation: ₹800/day vs commute, ₹560/day vs premium, with stated assumptions.
- TCO cross-referenced (not redone). Market report asks narrower question: does airport operating arrangement create enough benefit?
- Classification: "highest margin" not established; "cost advantage under controlled conditions" plausible hypothesis; "superior to commute" not demonstrated.

### 5. Evidence quality — corrected
- Source quality and calculation quality graded separately (table with definitions).
- All contradictory grades resolved (40% Dzire → Grade B; 40,000–50,000 → Grade C; 8,000–10,000 → Grade C; airport margin → unproven; 19.14% CAGR → unverified; 61% vs 58% → unreconciled).
- All important market-data figures traced to source with date, reference period, grade, type.
- Assumption register updated with corrected labels.

### 6. Strategic conclusion — reassessed
- Airport leads under base weights (+9.52) but not robust (5 rating-point flips).
- Under equal weights: tie at 354.55.
- Under volume-first: +15.00. Under fleet-economics-first: +20.00.
- Airport has lower revenue/km. Advantage depends on unquantified cost savings.
- Recommendation: validate buyer, operating arrangement, infrastructure. Keep commute as principal alternative.
- P0 priorities reframed as proper research methods with evidence tests.

## What remains unresolved

1. **Buyer hypothesis**: No verified fleet operator of sufficient scale. P0-1 must be executed.
2. **Airport cost advantage**: Not quantified. Requires operating data (paid km, deadhead, waiting time, access charges). P0-2.
3. **Depot charging feasibility**: Not verified at any airport. P0-3.
4. **Service-mode split**: Uber/Ola/Rapido car vs two-wheeler split not published. 591.3M vs 810M discrepancy unexplained.
5. **Segment table metrics**: All Grade D. No source for any km/day, fare, trips, growth, EV share, or price sensitivity.
6. **Corporate commute revenue/km**: Not separately measured. ₹25.00/km is for "daily commute/subscription" generally.
7. **Rating sensitivity**: Ratings have no evidentiary basis (Grade C/D). Formal uncertainty quantification not performed.
8. **figures.txt**: Still stale. Must be regenerated or deleted.
9. **market_analysis.py**: Path bug fixed in v4 script but original file not updated.
10. **Inter-city arithmetic**: 420 vs 340 km/day unresolved. Revenue/km is either ₹15.00 or ₹18.53.

## Files produced

- `60_final_redteam_report_v4.md` — final report
- `CHANGELOG_v3_to_v4.md` — this file
- `40_segment_prioritisation/segment_prioritisation_v4.py` — reproducible scoring script
- `40_segment_prioritisation/sensitivity_results_v4.csv` — weight scheme sensitivity
- `40_segment_prioritisation/rating_sensitivity_v4.csv` — rating sensitivity
- `40_segment_prioritisation/base_scores_v4.csv` — base scores
- `40_segment_prioritisation/criterion_contributions_v4.csv` — criterion contributions