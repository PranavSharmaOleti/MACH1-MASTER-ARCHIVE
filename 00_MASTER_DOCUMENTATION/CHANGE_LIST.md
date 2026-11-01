# MACH1 Provenance Register — Audit Fix Change List

## Summary of corrections

| # | Sheet | Row | Field | Old → New | Reason |
|---|-------|-----|-------|-----------|--------|
| 1 | Numerical Data Register | MCH-N-006 | Value as displayed | '18%' → '10%' | Intra-city EV share is 10%, not 18%. Growth rate 18% is correct. |
| 2 | Numerical Data Register | MCH-N-006 | Original source value | '18' → '10' | Corrected EV share. |
| 3 | Numerical Data Register | MCH-N-006 | Notes | 'Table flagged withdrawn by MARKET_ASSESSMENT.pdf' → 'Table flagged withdrawn by MARKET_ASSESSMENT.pdf. EV share corrected 18%→10%; growth 18% unchanged.' | EV share was 10% not 18%. |
| 4 | Numerical Data Register | MCH-N-008 | Value as displayed | '26%' → '18%' | Airport EV share is 18%, not 26%. Growth rate 26% is correct. |
| 5 | Numerical Data Register | MCH-N-008 | Original source value | '26' → '18' | Corrected EV share. |
| 6 | Numerical Data Register | MCH-N-008 | Notes | 'Withdrawn table' → 'Withdrawn table. EV share corrected 26%→18%; growth 26% unchanged.' | EV share was 18% not 26%. |
| 7 | Numerical Data Register | MCH-N-005 | Verification status | 'Partially verified' → 'Discrepancy' | 10% reserve conflicts with 3% (slide 5) and 15% (slide 11). |
| 8 | Numerical Data Register | MCH-N-027 | Verification status | 'Partially verified' → 'Discrepancy' | 36 kWh (80% usable) conflicts with 3% top/bottom reserve (94%) and 90% convention. |
| 9 | Numerical Data Register | MCH-N-032 | Verification status | 'Verified — Derived' → 'Discrepancy' | 197.8 EFC/yr overstates nominal by 11.1% (wall vs nominal mixing). |
| 10 | Numerical Data Register | MCH-N-092 | Verification status | 'Verified — Derived' → 'Discrepancy' | References pre road-tax-fix model; current model differs. |
| 11 | Numerical Data Register | MCH-N-004 | Verification status | 'External' → 'Discrepancy' | GST claim is internal contradiction: EV GST is 5% regardless of length. |
| 12 | Numerical Data Register | MCH-N-013 | Notes | 'Coincides with CNG energy cost ₹948,480/60=15,808 — no, 93,600 is distinct' → '93,600 coincidentally equals 5-yr EV maintenance (figures.txt line 6). Different quantity, same number. Table withdrawn.' | Cleaned up confusing note. |
| 13 | Numerical Data Register | MCH-N-010 | Value as displayed | '61%' → '61% (~58% derived)' | Deck says 61%; table-derived share is ~58%. Flagged unverified. |
| 14 | Calculation Traceability | ALL 30 rows | 8 fields → 9 columns | 8 fields → 9 fields | 'Deck value' column was missing; single number was Reproduced value; Match? and Status were shifted. All rows corrected to 9 columns with proper Deck value / Reproduced value split. |
| 15 | Technical Claims | MCH-T-004 | Verification status | 'Partially verified' → 'Discrepancy' | 25.4 break-even − 3.5 baseline = 21.9 h/mo headroom, not 45 h. Deck's 45 h is unexplained. |
| 16 | Technical Claims | MCH-T-001 | Verification status | 'Partially verified' → 'Discrepancy' | +19.5% to +11.6% band does not match table's worst case +7.6% (Mumbai financed). |
| 17 | Discrepancies | MCH-D-011 | Detail | 'LocalCircles 17,993; Bengaluru 10,000+; complaint shares 74/62/53/30/6%' → 'LocalCircles 17,993 respondents (325 districts); Bengaluru 10,000+ responses. Complaint shares: cancellation 74%, rude behaviour 62%, vehicle condition 53%, safety 30%, driver behaviour 25%, fare 6%. (25% driver-behaviour share was omitted in original.)' | Added missing 25% driver-behaviour complaint share to D-011 detail. |

**Total changes: 17**

## Structural errors found

1. **N-006 / N-008 swapped EV share and growth**: Intra-city EV share is 10% (not 18%), growth 18%. Airport EV share is 18% (not 26%), growth 26%. The values were transposed.
2. **Calculation Traceability: 8 fields under 9 headers**: 'Deck value' column was missing; the single numeric value was actually the Reproduced value; Match? and Status were shifted left by one. All 30 rows corrected to 9 columns.
3. **T-004 '45 h headroom' misclassified**: 25.4 break-even − 3.5 baseline = 21.9 h/mo, not 45 h. Status changed from 'Partially verified' to 'Discrepancy'.
4. **N-092 'pre road-tax fix' marked Verified**: References pre-fix model. Status changed to 'Discrepancy'.
5. **D-011 omits 25% driver-behaviour complaint share**: Added to detail text.
6. **N-005 reserve 10% misclassified**: Conflicts with 3% and 15%. Status → 'Discrepancy'.
7. **N-027 usable energy 36 kWh misclassified**: Conflicts with 3% reserve. Status → 'Discrepancy'.
8. **N-032 EFC 197.8 misclassified**: Overstates by 11.1%. Status → 'Discrepancy'.
9. **N-004 GST claim misclassified**: Internal contradiction (EV GST 5% regardless of length). Status → 'Discrepancy'.
10. **T-001 +19.5% band misclassified**: Doesn't match table worst case +7.6%. Status → 'Discrepancy'.
11. **N-013 note confusing**: Cleaned up to clarify 93,600 = 5-yr EV maintenance coincidence.

## Additional flags (not corrected, need verification)

- N-010: '61% of market' — deck says 61%, table-derived ~58%. Marked Unverified (no measured data). Consider changing to Discrepancy if table-derived share is trusted.
- N-036: '411 GWh by 2031-32' — parliamentary response Dec 2025. Marked External source. Verify citation.
- N-015: '80 bhp' on slide 4 — verify against slide 5 powertrain table.
- N-011: 'Dimensions 1,684×1,532' — verify against Dzire drawing (1,735×1,515). May be FleetLine E1's own dimensions.
