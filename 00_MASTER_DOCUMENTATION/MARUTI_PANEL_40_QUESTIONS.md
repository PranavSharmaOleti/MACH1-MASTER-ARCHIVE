# MACH1 / FleetLine E1 — Maruti Suzuki Panel: 40 Hardest Questions

**Panel composition:** Fleet Ops Head, Battery Engineer, Finance Lead, Policy Analyst
**Basis:** Final corrected deck + evidence binder + cheat sheet
**Format:** Each question includes: why they'd ask, 30-second strong answer, number/source to cite, honest concession
**Stress-test analysis:** Included at end — where panel focus will concentrate, which data gets referenced most, and where we might have problems

---

## Theme 1: Powertrain & Battery (Fleet Ops Head + Battery Engineer)

### Q1. Why 1 charger per vehicle if 1:3 utilization works?
- **Why they'd ask:** Fleet ops head wants capital efficiency; 1:3 saves ₹66,000/vehicle
- **30s answer:** 1:3 is utilization ratio, not hardware ratio. At 200 km/day, one vehicle needs 3.86 h on 7.4 kW. Three vehicles need 11.6 h sequentially — fits in 12 h with zero margin. One port per vehicle gives 8.1 h slack, N+1 spares at 1:10, and handles inter-city duty (280 km leg needs 5.5 h, exceeding overnight window).
- **Cite:** tco_analysis.py §G (charger sizing), §N4 (inter-city duty)
- **Concession:** If duty drops below 120 km/day, 1:3 works and saves ₹66,000/vehicle. We chose conservatism.

### Q2. What if Lewerenz is right — 3.7 years to 80% at 40°C?
- **Why they'd ask:** Battery engineer wants to know the 8-yr guarantee isn't a fantasy
- **30s answer:** At 48°C, even Naumann √t gives 71.9% SoH at year 8 (44.1 kWh usable, still above 200 km/day need). Lewerenz linear would be worse — but that model assumes no temperature derating and no SoH headroom in pack sizing. Our 45 kWh pack has 10% battery reserve + 15% design reserve = 25% total headroom. Even at 60% SoH, we'd have 27 kWh usable = 210 km range.
- **Cite:** tco_analysis.py §K (pack-sizing rule), §10 G3 gate
- **Concession:** If Lewerenz is right, the 8-yr capacity-retention guarantee is unsignable. That's why G3 exists as a kill gate. We'd drop to 5-yr guarantee.

### Q3. What if electricity is ₹12/kWh (public DC)?
- **Why they'd ask:** Finance lead stress-tests the worst case
- **30s answer:** At ₹12/kWh, EV energy cost is ₹1.71/km vs CNG ₹3.04/km. Advantage drops from +14.5% to −1.4% (Delhi, 5-yr). But this assumes 100% public DC charging — our model assumes depot charging at ₹4.50–9/kWh. The 75 h/month Green SM case (−28.4%) is the real risk: if depot charging fails, EV loses.
- **Cite:** tco_analysis.py §D (tornado), §I (downtime); deck slide 7 sensitivity
- **Concession:** Public DC at ₹12 is the single biggest threat. Depot charging reliability is not optional — it's the entire business case.

### Q4. What if depot charging queues are 75 h/month (Green SM Noida)?
- **Why they'd ask:** Fleet ops head has seen this fail in the real world
- **30s answer:** At 75 h/month, EV advantage is −28.4% (Delhi, 5-yr). That's why we require 1 port/vehicle with N+1 spares, smart charging scheduling, and 45 h/month of downtime headroom. The Green SM failure was 1 port per 10 vehicles with no scheduling.
- **Cite:** tco_analysis.py §I (adv_at_downtime(75) = −28.4%); Indian Express 1 Sep 2026
- **Concession:** If we can't guarantee depot charging, we don't launch. G4 gate: 20,000 cumulative vehicles with 21.9 h/mo slack.

### Q5. Why not CNG? Dzire Tour S is proven.
- **Why they'd ask:** Fleet ops head's default position
- **30s answer:** CNG at ₹7.42–8.34/km vs EV at ₹6.42/km (depot). Driver take-home is ₹14,200/month higher on EV. CNG has cylinder hydro-testing (₹4,500/3yr), range anxiety (500-600 km real), and CBG supply risk (207 plants, 20-60% capacity). But CNG wins if: (a) depot charging fails, (b) electricity exceeds ₹11/kWh sustained, (c) driver can't access overnight charging.
- **Cite:** tco_engine.py (energy costs), deck slide 5 (comparison table), tco_analysis.py §G (CNG hydro-test)
- **Concession:** CNG is the right answer if charging infrastructure is unreliable. We're betting it won't be.

### Q6. What's the AI/connected layer worth in rupees?
- **Why they'd ask:** Finance lead wants to know if AI investment is justified
- **30s answer:** Combined pilot value: ₹824–1,776/vehicle/month (5.8–12.5% of ₹14,200 driver advantage). Smart charging is the biggest lever (₹501–601, 3.5–4.2%). Predictive maintenance is smallest (₹133, 0.9%). These are hypothesis, not validated — no fleet data yet.
- **Cite:** Slide 9 audit, tco_analysis.py §I (OPP_H basis)
- **Concession:** AI is incremental, not transformative. The ₹14,200 comes from powertrain economics. If AI targets miss by 50%, it's still worth doing but not the core case.

### Q7. What happens when concessions expire in 2030?
- **Why they'd ask:** Policy analyst wants to know the cliff risk
- **30s answer:** Delhi road-tax exemption and Maharashtra 15% incentive both expire 31-Mar-2030. That's 5 years before our 2035 target. At 2035, Delhi 5-yr NPV advantage is +15.7% (vs +6.7% today) — actually improves because escalation compounds. But the NPV advantage assumes policy continues. If road tax returns (10% on EV), advantage drops ~2-3 pp. We've modeled this: even with full road tax, EV still wins in Delhi at 5-yr.
- **Cite:** tco_analysis.py §M (city×basis matrix), deck slide 10 (policy table), Claim Audit Part 2 (Delhi ₹30 L cap)
- **Concession:** If ALL concessions expire simultaneously and no new ones replace them, the 2035 case weakens but doesn't break. The 8-yr case (+14.6%) has more buffer.

### Q8. How do you know intra-city isn't the bigger opportunity?
- **Why they'd ask:** Fleet ops head sees 58% of rides are intra-city
- **30s answer:** Intra-city is 58% of rides but price sensitivity is 0.85 (highest) and EV share is only 10% (lowest). Our vehicle is optimized for airport+commute (19% of rides, 0.30–0.35 price sensitivity, 18% EV share). The sedan form factor, 400 L boot, and 268 km range serve airport duty. Intra-city is higher volume but lower margin and harder to electrify (unpredictable hail, 95 km/day, no depot return).
- **Cite:** Deck slide 3 (use-case table), slide 11 (synthesis); tco_analysis.py §N (inter-city duty economics)
- **Concession:** If intra-city electrification accelerates (e.g., battery swapping), our vehicle may be over-engineered for that segment. We'd need a cheaper, smaller variant.

### Q9. What if Dzire gets a CNG/hybrid update?
- **Why they'd ask:** Battery engineer + finance lead want to know the competitive moat
- **30s answer:** Dzire Tour S is CNG at ₹7.42–8.34/km. A hybrid would reduce CNG consumption 20-30% (→ ₹5.9-6.7/km) but adds ₹1-1.5 L to ex-showroom. At ₹7.5 L ex-showroom, hybrid on-road ≈ ₹9 L, EMI ≈ ₹19,000/mo — still higher than EV's ₹27,039? No, hybrid EMI is lower but energy cost is higher. Hybrid would need to beat ₹6.42/km to threaten us. At 30% consumption improvement, hybrid = ₹5.9/km — still above EV's ₹6.31? No, 5.9 < 6.31. So hybrid could be competitive IF it achieves 30%+ improvement AND maintains CNG's ₹76/kg price. But CNG price is rising (₹76→₹90 in sensitivity: EV advantage +21.1%).
- **Cite:** Deck slide 5 (comparison table), slide 7 (sensitivity: CNG price ₹76→₹90)
- **Concession:** A well-executed hybrid Dzire at current CNG prices would narrow our advantage significantly. We're betting CNG prices rise faster than hybrid efficiency improves.

### Q10. Why 45 kWh when 34 kWh covers 200 km/day?
- **Why they'd ask:** Battery engineer wants to know you're not over-packing
- **30s answer:** 34 kWh covers 200 km at 12.84 kWh/100km with zero reserve. But: (a) SoH degrades to 71.9% at year 8 → 32.4 kWh usable; (b) 15% design reserve for temperature derating, AC load (−20-35% range), and charging inefficiency; (c) 300 km/day inter-city duty needs 44.1 kWh. The 45 kWh pack is the minimum that survives 8 years at 48°C with all reserves.
- **Cite:** tco_analysis.py §K (pack-sizing rule), §N (inter-city duty), deck slide 5 (pack sizing table)
- **Concession:** If duty stays strictly 200 km/day urban, a 34 kWh pack saves ₹1.5 L upfront but risks range anxiety and resale value.

---

## Theme 2: TCO & Finance (Finance Lead)

### Q11. Your EMI is ₹27,039 but deck says ₹29,743. Which is right?
- **Why they'd ask:** Finance lead caught the discrepancy
- **30s answer:** ₹27,039 is correct. On-road price ₹12,72,600 at 10% over 60 months with no down payment. The deck's ₹29,743 was an error — likely used a different principal or rate. Interest is ₹3.50 L, not ₹3.85 L. We've corrected this.
- **Cite:** tco_engine.py line 28-31 (emi function); tco_analysis.py §H (annuity check)
- **Concession:** This was an error in the deck. It's fixed in the corrected text.

### Q12. Cash +17.5% vs financed +8.4% — neither matches your city table.
- **Why they'd ask:** Finance lead spotted the inconsistency
- **30s answer:** You're right. The actual figures are: Delhi cash +22.6%, financed +14.5%; Mumbai cash +15.3%, financed +7.6%; Bengaluru cash +16.4%, financed +8.2%. The "17.5% / 8.4%" was a labeling error — likely an average or a different city basis. Corrected.
- **Cite:** tco_analysis.py §F (cash vs financed table)
- **Concession:** This was a real error in the deck. Fixed.

### Q13. Mumbai CNG costs are understated (7.00/6.32 vs your code's 7.30/6.52).
- **Why they'd ask:** Finance lead verified the numbers
- **30s answer:** Corrected. Mumbai CNG at ₹88/kg (not ₹76) with 14% road tax gives 7.30/6.52. The deck used ₹76/kg (Delhi price) for Mumbai, understating CNG cost by ₹0.30/km. This actually makes our case stronger in Mumbai.
- **Cite:** tco_engine.py CITIES dict (Mumbai cng=88.0); tco_analysis.py §F
- **Concession:** We used Delhi CNG price for Mumbai. Fixed — makes our case stronger.

### Q14. Your legacy commission rows show ₹48,799 — higher than the flat-fee case. That's wrong.
- **Why they'd ask:** Finance lead spotted the arithmetic error
- **30s answer:** You're right. The code had a double-subtraction bug: net fare = fare×(1-comm) − fare×comm instead of fare×(1-comm). Corrected: 20% commission → EV ₹37,362 (not ₹48,799), CNG ₹23,162. 25% commission → EV ₹34,502, CNG ₹20,302. Advantage remains ₹14,200 in all cases — the invariance holds, only the absolutes were wrong.
- **Cite:** tco_analysis.py (fixed lines 319-329); corrected deck text
- **Concession:** This was a real code bug. Fixed. The advantage invariance (₹14,200) is confirmed correct.

### Q15. "About five points of policy value" — where does 5 come from?
- **Why they'd ask:** Finance lead can't find 5 anywhere
- **30s answer:** It doesn't come from anywhere. The infrastructure penalty is 8.1 pp (5-yr) or 10.7 pp (8-yr). "About five points" was an unsourced claim. We've removed it.
- **Cite:** tco_analysis.py §L (direction check: d5=+8.1, d8=+10.7)
- **Concession:** This was an unsourced claim. Removed from corrected deck.

### Q16. "45 h headroom" — is that real?
- **Why they'd ask:** Finance lead wants to know the downtime basis
- **30s answer:** 45 h is the zero-base break-even at ₹200.46/h (OPP_H). The actual base case is 3.5 h/month downtime (0.5 queue + 1.0 planned + 1.5 repair + 0.5 charger failure), leaving 21.9 h of additional headroom. The "45 h" figure is defensible only if you state it's on a zero-base.
- **Cite:** tco_analysis.py §C (45 h at zero base), §I (21.9 h at 3.5 h base)
- **Concession:** We should state 21.9 h (actual) not 45 h (theoretical). Fixed in corrected text.

### Q17. What if electricity is ₹12/kWh sustained?
- **Why they'd ask:** Finance lead stress-tests the worst case
- **30s answer:** EV energy cost rises to ₹1.71/km. Advantage drops from +14.5% to −1.4% (Delhi, 5-yr). But this requires 100% public DC charging. Our model assumes depot charging at ₹4.50–9/kWh. If depot charging is reliable, ₹12 is irrelevant. If it's not, we lose.
- **Cite:** tco_analysis.py §D (tornado: electricity ₹4.50→₹12.00 = −1.4%)
- **Concession:** This is the single biggest threat. Depot charging reliability is the entire business case.

### Q18. Your 48-cell matrix has 0 negative cells without infrastructure. With infrastructure?
- **Why they'd ask:** Finance lead wants to know the charger's impact
- **30s answer:** With the ₹99,000 charger included, 1 cell goes negative: Bengaluru, 5-yr, cash, at −0.4%. On the NPV basis, it's positive. The charger narrows the advantage by 8.1 pp (5-yr) and 10.7 pp (8-yr) but never reverses it except that one cell.
- **Cite:** tco_analysis.py §M (M_NEG list, direction check)
- **Concession:** Bengaluru cash 5-yr is genuinely marginal. If charger costs rise above ₹1.5 L, more cells go negative.

### Q19. What's the break-even charger cost per vehicle?
- **Why they'd ask:** Finance lead wants to know the infrastructure budget ceiling
- **30s answer:** Delhi: ₹1.8 L nominal, ₹1.5 L NPV. Mumbai: lower (higher electricity tariff means less energy saving to offset charger). Bengaluru: lowest (highest tariff, road tax not exempt). The binding constraint is Bengaluru NPV at ~₹1.2 L.
- **Cite:** tco_analysis.py §M4 (charger capex sensitivity)
- **Concession:** If charger costs exceed ₹1.2 L in Bengaluru, the 5-yr case breaks. We need to keep charger costs under ₹1 L.

### Q20. How do you know the Dzire won't get a hybrid update?
- **Why they'd ask:** Finance lead wants competitive moat analysis
- **30s answer:** A hybrid Dzire at ₹7.5 L ex-showroom would cost ~₹9 L on-road, EMI ~₹19,000/mo. At 30% consumption improvement → ₹5.9/km energy cost. That's below EV's ₹6.31/km. So hybrid could be competitive IF it achieves 30%+ improvement AND CNG stays at ₹76/kg. But CNG price is rising (₹76→₹90 in sensitivity: EV advantage +21.1%). We're betting CNG prices rise faster than hybrid efficiency improves.
- **Cite:** Deck slide 5 (comparison table), slide 7 (sensitivity)
- **Concession:** A well-executed hybrid Dzire at current CNG prices narrows our advantage significantly. This is our biggest competitive risk.

---

## Theme 3: Charging & Infrastructure (Fleet Ops Head)

### Q21. 1 port per vehicle is capital-intensive. Why not 1:3?
- **Why they'd ask:** Fleet ops head wants capital efficiency
- **30s answer:** At 200 km/day, 1 vehicle needs 3.86 h on 7.4 kW. Three vehicles need 11.6 h sequentially — fits in 12 h with zero margin. No redundancy, no scheduling flexibility. One port per vehicle gives 8.1 h slack, N+1 spares at 1:10, and handles inter-city duty (280 km leg needs 5.5 h, exceeding the overnight window).
- **Cite:** tco_analysis.py §G (port sizing), §N4 (inter-city duty)
- **Concession:** If duty drops below 120 km/day, 1:3 works and saves ₹66,000/vehicle. We chose conservatism for reliability.

### Q22. What if depot charging queues are 75 h/month?
- **Why they'd ask:** Fleet ops head has seen Green SM fail
- **30s answer:** At 75 h/month, EV advantage is −28.4%. That's why we require 1 port/vehicle, smart scheduling, and 45 h/month headroom. Green SM had 1 port per 10 vehicles with no scheduling. Our model prices this: 3.5 h base downtime (0.5 queue + 1.0 planned + 1.5 repair + 0.5 charger failure) with 21.9 h additional headroom.
- **Cite:** tco_analysis.py §I (adv_at_downtime(75) = −28.4%); Indian Express 1 Sep 2026
- **Concession:** If we can't guarantee depot charging, we don't launch. G4 gate exists for this.

### Q23. Your 3.86 h overnight window assumes 7.4 kW. What if we only get 3.3 kW?
- **Why they'd ask:** Fleet ops head worries about site power limits
- **30s answer:** At 3.3 kW, charge time = 25.68 ÷ (3.3 × 0.90) = 8.65 h. Still fits in 12 h window but with only 3.35 h slack. If we need 7.4 kW and can't get it, we'd need either: (a) 2 ports per vehicle (double capex), or (b) reduce duty to 150 km/day (7.4 h at 3.3 kW). Site power is a real constraint.
- **Cite:** tco_analysis.py §G (h_night calculation)
- **Concession:** Site power availability is an unpriced risk. We've assumed 7.4 kW is available; if not, costs rise.

### Q24. What about inter-city duty (280 km one-way)?
- **Why they'd ask:** Fleet ops head wants to know if the vehicle works beyond urban
- **30s answer:** 280 km one-way needs 36 kWh battery-side = 40.5 kWh wall = 5.5 h at 7.4 kW — exceeds the 3.86 h overnight window. Inter-city requires destination charging (guaranteed, operator-controlled) plus mid-day top-ups. Beyond 300 km one-way, destination charging is mandatory. This is an operating-model dependency, not a vehicle spec.
- **Cite:** tco_analysis.py §N4 (inter-city duty), §N2 (corridor feasibility)
- **Concession:** The vehicle doesn't do inter-city on depot charging alone. We need destination charging contracts.

### Q25. Why not battery swapping instead of depot charging?
- **Why they'd ask:** Fleet ops head has seen swapping work for 2W/3W
- **30s answer:** Swapping needs: (a) standardized pack (our 45 kWh CTP pack is semi-structural, not swappable), (b) swap station network (none exists for 4W), (c) battery-as-a-service economics (unproven at 4W scale). Depot charging at ₹5.50–9/kWh is cheaper than swapping's implied cost. But swapping would eliminate the 75 h/month queue risk entirely.
- **Cite:** Deck slide 5 (charging readiness), slide 6 (pack architecture)
- **Concession:** If swapping becomes viable for 4W, our pack architecture (semi-structural CTP) would need redesign. We've chosen optionality: detachable pack design costs ₹2-3 Cr vs ₹15-25 Cr for full redesign.

---

## Theme 4: Market & Positioning (Fleet Ops Head + Policy Analyst)

### Q26. 61% of market is intra-city. Why not optimize for that?
- **Why they'd ask:** Fleet ops head sees the volume opportunity
- **30s answer:** Intra-city is 58% of rides but has highest price sensitivity (0.85) and lowest EV share (10%). Our vehicle is optimized for airport+commute (19% of rides, 0.30–0.35 price sensitivity, 18% EV share). The sedan form factor, 400 L boot, and 268 km range serve airport duty. Intra-city is higher volume but lower margin and harder to electrify (unpredictable hail, 95 km/day, no depot return).
- **Cite:** Deck slide 3 (use-case table), slide 11 (synthesis); tco_analysis.py §N (inter-city duty economics)
- **Concession:** If intra-city electrification accelerates (battery swapping), our vehicle may be over-engineered for that segment. We'd need a cheaper, smaller variant.

### Q27. Your use-case table says 61% but slide 11 says 58%. Which is right?
- **Why they'd ask:** Policy analyst spotted the inconsistency
- **30s answer:** Neither is rigorously derived. Both are estimates from Vahan registration data (not trip data). The table is being withdrawn. The honest position: intra-city is the largest segment by ride count, but the exact share is uncertain. We're using ~58% as the more conservative figure.
- **Cite:** Deck slide 3 (narrative), slide 11 (synthesis); corrected deck text
- **Concession:** We don't have trip-level data. The share figures are estimates, not measurements.

### Q28. Your dendrogram claims "Cluster A = airport + commute." Is that real?
- **Why they'd ask:** Policy analyst wants statistical rigor
- **30s answer:** No. The dendrogram is illustrative. No linkage method, feature set, or distance metric is documented. We're removing it.
- **Cite:** Deck slide 3 (dendrogram); corrected deck text
- **Concession:** The clustering claim is unsupported. Removed.

### Q29. What if the Dzire gets a CNG/hybrid update?
- **Why they'd ask:** Fleet ops head wants competitive analysis
- **30s answer:** A hybrid Dzire at ₹7.5 L ex-showroom → ~₹9 L on-road, EMI ~₹19,000/mo. At 30% consumption improvement → ₹5.9/km energy cost. That's below EV's ₹6.31/km. Hybrid could be competitive IF it achieves 30%+ improvement AND CNG stays at ₹76/kg. But CNG price is rising (₹76→₹90: EV advantage +21.1%). We're betting CNG prices rise faster than hybrid efficiency improves.
- **Cite:** Deck slide 5 (comparison), slide 7 (sensitivity)
- **Concession:** A well-executed hybrid Dzire at current CNG prices narrows our advantage significantly. This is our biggest competitive risk.

### Q30. Why a sedan and not an SUV?
- **Why they'd ask:** Fleet ops head knows SUVs dominate
- **30s answer:** Sedan: airport fare premium (₹600/trip vs ₹350 intra-city) + separate boot for luggage. SUV: higher CAPEX, worse aerodynamics (higher kWh/100km), higher insurance. At 200 km/day, a 10% increase in consumption (SUV) = ₹0.64/km more energy = ₹4,000/month more. The sedan form factor is the economic choice, not the fashionable one.
- **Cite:** Deck slide 2 (THE DESIGN), slide 3 (use-case table: airport ₹600/trip)
- **Concession:** If airport duty shifts to SUV preference (premium segment), our sedan may lose. But premium is 15% EV share vs airport's 18% — the economics favor airport.

---

## Theme 5: Policy & Regulatory (Policy Analyst)

### Q31. Delhi road-tax exemption has a ₹30 L cap now. Does your vehicle qualify?
- **Why they'd ask:** Policy analyst knows the 2026 draft added a price cap
- **30s answer:** Yes. Our ex-showroom is ₹12.12 L, well under ₹30 L. But the policy is still a draft (released 11 Apr 2026, not final notified). If the cap drops to ₹15 L or ₹10 L, we'd still qualify. If it drops to ₹10 L, we'd be marginal.
- **Cite:** Claim Audit Part 2 (Delhi EV Policy 2026), deck slide 10
- **Concession:** The policy is a draft, not final. If the final policy has a lower cap or different terms, our cost model changes.

### Q32. Karnataka says "no consumer incentive" but actually has zero road tax.
- **Why they'd ask:** Policy analyst caught the error
- **30s answer:** You're right. Karnataka Clean Mobility Policy 2025-2030 provides zero road tax and zero registration charges for EVs. Our deck said "No consumer incentive" — that's wrong. Also, the capital subsidy is 15-25% (not 20-25%). Corrected.
- **Cite:** Claim Audit Part 2 (Karnataka), Invest Karnataka
- **Concession:** This was an error. Fixed in corrected deck text.

### Q33. AIS-138 doesn't mandate CCS2. Why did you say it does?
- **Why they'd ask:** Policy analyst knows the standard
- **30s answer:** You're right. AIS-138 Part 2 permits multiple DC standards (CCS2, CHAdeMO, GB/T, Bharat DC-001). CCS2 is the de facto market standard because OEMs chose it, not because the standard mandates it. We overstated the regulatory prescriptiveness. Corrected to "permits multiple standards; CCS2 is market-driven."
- **Cite:** Claim Audit Part 2 (AIS-138), EVPulse 11 Jun 2026
- **Concession:** This was an overstatement. Fixed.

### Q34. What happens when concessions expire in 2030?
- **Why they'd ask:** Policy analyst wants the cliff scenario
- **30s answer:** Delhi road-tax exemption and Maharashtra 15% incentive both expire 31-Mar-2030. At 2035, Delhi 5-yr NPV advantage is +15.7% (vs +6.7% today) — actually improves because escalation compounds. But if ALL concessions expire and none replace them, advantage drops ~2-3 pp. Even with full road tax (10%), EV still wins in Delhi at 5-yr. The 8-yr case (+14.6%) has more buffer.
- **Cite:** tco_analysis.py §M (city matrix), §L (NPV headline)
- **Concession:** If no new policies replace expiring ones, the 2035 case weakens but doesn't break. The 5-yr case is more vulnerable.

### Q35. PM E-DRIVE has no e-4W category. Where's your government support?
- **Why they'd ask:** Policy analyst knows the scheme excludes cars
- **30s answer:** Correct — PM E-DRIVE covers 2W, 3W, buses, trucks, ambulances, charging — not private electric cars. Our NPV advantage does NOT come from central purchase incentives. It comes from: (a) 5% GST on BEV (vs 18-43% on ICE), (b) state road-tax exemptions (Delhi, Maharashtra, Karnataka), (c) lower energy cost (₹0.64/km at depot vs ₹3.04/km CNG). The central scheme is irrelevant to our economics.
- **Cite:** Claim Audit Part 1 (PM E-DRIVE), PIB factsheet 1 Oct 2026
- **Concession:** We have no central purchase subsidy. Our case rests entirely on state policies and powertrain economics.

---

## Theme 6: AI & Connected (Finance Lead + Fleet Ops Head)

### Q36. What's the AI layer worth in rupees?
- **Why they'd ask:** Finance lead wants ROI on AI investment
- **30s answer:** Combined pilot value: ₹824–1,776/vehicle/month (5.8–12.5% of ₹14,200 driver advantage). Smart charging is biggest (₹501–601, 3.5–4.2%). Predictive maintenance is smallest (₹133, 0.9%). These are hypothesis — no fleet data yet.
- **Cite:** Slide 9 audit, tco_analysis.py §I (OPP_H basis)
- **Concession:** AI is incremental, not transformative. If AI targets miss by 50%, it's still worth doing but not the core case.

### Q37. "Predictive maintenance ≥7-day warning" — how is that worth ₹133/month?
- **Why they'd ask:** Finance lead wants the derivation
- **30s answer:** 1 breakdown/yr prevented × 1 day downtime × 8 h × ₹200.46/h = ₹1,600/yr ≈ ₹133/mo. This assumes 1 preventable breakdown per year. If breakdowns are more frequent, value scales. If less frequent, value shrinks. The 7-day warning is the target; actual warning time depends on sensor quality and model accuracy.
- **Cite:** Slide 9 audit, tco_analysis.py §I (OPP_H)
- **Concession:** This is a rough estimate. Actual value depends on failure frequency, which we don't have data for.

### Q38. "Smart dispatch ~15% fewer deadhead km" — what's the deadhead baseline?
- **Why they'd ask:** Fleet ops head wants the assumption
- **30s answer:** We estimated intra-city deadhead at ~10% of 5,200 km = 520 km/month (no explicit deadhead figure in code; inter-city deadhead is 280 km/round trip). 15% reduction = 78 km saved. At ₹0.64/km energy cost = ₹50/month. At ₹10.665/km net fare (if freed km generates revenue) = ₹832/month. Range is ₹50–832 depending on whether freed km becomes revenue.
- **Cite:** Slide 9 audit (this conversation)
- **Concession:** The deadhead estimate is rough. Actual deadhead depends on dispatch patterns, which we haven't measured.

### Q39. TPMS thresholds — are 28 psi / 22 psi right for 175/65 R14?
- **Why they'd ask:** Battery engineer (or tire engineer) wants to verify
- **30s answer:** Normal cold inflation for 175/65 R14 is 30-33 psi. Warning at 28 psi = 12-15% below normal (reasonable). Critical at 22 psi = 30%+ below normal (near-deflation). Temperature: 30-50°C normal tire surface temp for Indian ambient. 60°C warning / 70°C critical. These are tire thresholds, NOT battery cell thresholds (48°C design point). We've added a clarifying label.
- **Cite:** Slide 9 audit (this conversation); deck slide 9
- **Concession:** The thresholds are standard industry values, not MACH1-specific. They could be tightened for fleet duty.

### Q40. Your CC/CV charging explanation is textbook. What's MACH1-specific?
- **Why they'd ask:** Battery engineer wants to know what's actually yours
- **30s answer:** The CC/CV explanation is generic. What's MACH1-specific: (a) depot 7.4 kW AC reaches 70-80% in 3.86 h at ₹5.50-9/kWh vs DC fast charging at ₹18-24/kWh — the cost difference is why depot charging is default; (b) per-cell SoH telemetry gating the 8-yr guarantee (G3); (c) 71.9% SoH at 48°C (44.1 kWh usable); (d) 3.6× disagreement between published LFP studies. We've moved CC/CV to appendix or tied it to depot charging cost.
- **Cite:** Slide 9 audit (this conversation); tco_analysis.py §K, §N
- **Concession:** Most of slide 9's content is generic. Only the SoH telemetry and battery-replacement economics are MACH1-specific.

---

## Stress-Test Analysis: Where Panel Focus Will Concentrate

### Highest-probability attack vectors (ranked by likelihood)

| Rank | Vector | Panelist | Why | Our vulnerability | Mitigation |
|---|---|---|---|---|---|
| 1 | **Depot charging reliability** (75 h/month) | Fleet Ops Head | Green SM failure is real, recent, and well-documented | −28.4% advantage if it fails | 1 port/vehicle, N+1, smart scheduling, G4 gate |
| 2 | **Lewerenz 3.7-yr to 80%** | Battery Engineer | Published study directly contradicts 8-yr guarantee | Guarantee unsignable if Lewerenz is right | G3 kill gate; 25% total headroom in pack sizing |
| 3 | **Hybrid Dzire update** | Finance Lead | Maruti's core competency; hybrid technology is maturing | Could beat EV at ₹5.9/km if 30% improvement achieved | CNG price rising (₹76→₹90); our bet on fuel price trajectory |
| 4 | **"61% vs 58%" market share** | Policy Analyst | Inconsistent figures in the deck itself | No trip-level data; both are estimates | Withdraw table; use "largest segment" language |
| 5 | **"About five points" unsourced** | Finance Lead | Can't find 5 anywhere in the code | Credibility damage if challenged | Removed from corrected deck |
| 6 | **Legacy commission rows (₹48,799)** | Finance Lead | Arithmetic error visible in the deck | Undermines analytical credibility | Fixed in code and corrected deck |
| 7 | **AIS-138 CCS2 mandate** | Policy Analyst | Overstated regulatory prescriptiveness | Overclaim on standard's scope | Corrected to "permits multiple standards" |
| 8 | **Karnataka "no consumer incentive"** | Policy Analyst | Factually wrong — zero road tax exists | Direct factual error | Corrected |
| 9 | **Delhi ₹30 L price cap** | Policy Analyst | Premium EVs excluded; policy is draft | Could affect premium variant planning | Our vehicle at ₹12.12 L qualifies; note draft status |
| 10 | **AI value (₹824-1,776/mo)** | Finance Lead | Hypothesis, not validated | Only 5.8-12.5% of driver advantage | Frame as incremental; don't overstate |

### Data that will get referenced most (ranked)

| Rank | Data point | Why | Source |
|---|---|---|---|
| 1 | ₹14,200 driver advantage | Core economic claim | tco_analysis.py §A, §J |
| 2 | 75 h/month Green SM | Real-world failure mode | Indian Express 1 Sep 2026 |
| 3 | 3.7 yr (Lewerenz) vs 13.3 yr (Naumann) | Battery guarantee credibility | Published LFP studies |
| 4 | ₹12/kWh public DC | Worst-case energy cost | Deck slide 7 sensitivity |
| 5 | 48-cell matrix (0 negative excl-infra) | Fleet case robustness | tco_analysis.py §M |
| 6 | ₹99,000 charger | Infrastructure cost | tco_analysis.py §G |
| 7 | 21.9 h headroom | Downtime tolerance | tco_analysis.py §I |
| 8 | 3,614 outlets (superseded) | Dzire service network | Maruti FY2018-19 AR |
| 9 | 30-35% fleet share (Maruti's figure) | Dzire fleet share | Maruti sales head statements |
| 10 | ₹30 L Delhi price cap | Policy eligibility | Delhi EV Policy 2026 draft |

### Where we might have problems (honest assessment)

1. **The 8-yr guarantee is the biggest risk.** If Lewerenz is right, the guarantee is unsignable. The 25% headroom in pack sizing helps but doesn't eliminate the risk. G3 gate is the right mechanism but it's a kill gate — if it triggers, we lose the 8-yr value proposition.

2. **Depot charging is the single point of failure.** Everything — ₹14,200 advantage, +14.5% TCO, driver take-home — depends on ₹4.50–9/kWh depot charging. If we can't guarantee this, the entire case collapses. The Green SM precedent (75 h/month) shows this is not theoretical.

3. **The hybrid threat is real and under-modeled.** We've estimated hybrid Dzire at ₹5.9/km but haven't modeled it in code. If Maruti executes a hybrid update well, our advantage narrows to 5-7% — still positive but much less compelling.

4. **Market share figures are estimates, not measurements.** "58% intra-city" and "19% airport+commute" come from Vahan registrations, not trip data. If challenged, we have no primary source. The use-case table is being withdrawn.

5. **AI value is small and unvalidated.** ₹824-1,776/month is 5.8-12.5% of the driver advantage. If we're asked to justify AI investment, the honest answer is "it's incremental, not transformative." Don't overstate.

6. **The "45 h headroom" figure was misleading.** It's the zero-base break-even, not the actual headroom (21.9 h). This could damage credibility if challenged by someone who knows the code. Fixed in corrected text.

7. **Policy dependency is high.** 5 of 10 policies expire by 2030. If no replacements emerge, the 2035 case weakens by 2-3 pp. The 5-yr case is more vulnerable than the 8-yr case.

8. **Bengaluru is genuinely marginal.** −0.4% on 5-yr cash basis with charger. If charger costs rise or electricity tariffs increase, Bengaluru breaks first. This is the weakest market for our case.

### Recommended panel prep priority

1. **Memorize the 25 cheat-sheet numbers** with basis (nominal/NPV, with/without charger, financed/cash, city)
2. **Practice the 30-second answers** for Q3, Q4, Q7, Q9, Q17 (the existential threats)
3. **Be ready to concede** on: legacy commission rows (fixed), "about five points" (removed), AIS-138 CCS2 (corrected), Karnataka consumer incentives (corrected), 45 h headroom (clarified)
4. **Don't overstate** AI value, market share precision, or policy certainty
5. **Lead with the code** — every number traces to tco_engine.py or tco_analysis.py; the panel respects reproducibility