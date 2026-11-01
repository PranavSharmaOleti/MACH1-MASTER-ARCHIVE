# MACH1 / FleetLine E1 — Exact PPT Text Change List for Canva

**Source:** Detailed Presentation Report.pdf (11 slides)
**Basis:** CORRECTED_DECK_TEXT.md (50 edits, verified against code and primary sources)
**Format:** Slide → Location → Old text → New text → Reason

---

## Slide 2 — THE DESIGN

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 1 | THE DESIGN | "sub-4-metre keeps GST at 5%, saves ₹1.5L" | "BEV powertrain qualifies for 5% GST regardless of length; sub-4m avoids 18%→40% GST on petrol/CNG comparators (Dzire Tour S pays 18%)" | GST 5% is powertrain-based, not length-based |
| 2 | THE DESIGN | "BEV on LFP: at 200 km/day" | "BEV on LFP: 200 km/day duty, 45 kWh pack, 10% reserve at year 8" | Add reserve qualifier |
| 3 | THE DESIGN | "45 kWh: sized for duty cycle" | "45 kWh: sized for 200 km/day duty with 10% reserve at year 8 (40.5 kWh usable)" | Clarify usable capacity |

## Slide 3 — MARKET

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 4 | Table 1/2 | Use-case table (5 rows) | **WITHDRAW entirely** | "Driver ₹/mo" is gross revenue not take-home; intercity 1.5 trips × 280 km = 420 not 340; not derivable from any file |
| 5 | Narrative | "61% of market" | "~58% of rides (estimate; CSVs are Vahan registrations, not trip data)" | Vahan data ≠ trip data |
| 6 | Narrative | "19.14% CAGR" | "19.14% CAGR (market assessment figure; table shows 18–28% use-case growth)" | Reconcile CAGR vs table growth rates |
| 7 | Dendrogram | "Cluster A = airport + commute" | Remove or relabel as "illustrative grouping, not statistically derived" | No linkage/feature data supports clustering |
| 8 | Table 1 | "Price SENS." column | Label as "estimated index, not derived from survey" | No source |

## Slide 4 — VEHICLE CONCEPT

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 9 | THE DESIGN | "sub-4-metre keeps GST at 5%, saves ₹1.5L" | "Sub-4m (3,995 mm): packaging, parking, maneuverability; GST 5% is powertrain-based" | GST claim is false for EVs |
| 10 | Narrative | "Maruti 3,614-outlet service network" | "Maruti: 3,400+ outlets, 6,000+ service touchpoints (2026)" | 3,614 is superseded FY19 figure |
| 11 | Narrative | "40% of all Dzire sales go to fleet buyers" | "30–35% of Dzire sales go to fleet (Maruti's stated figure); ~5,000 units/month Tour S" | Maruti states 30–35%, not 40% |
| 12 | Param table | "Fleet Pricing ~₹14 L" | "Fleet pricing ~₹14 L (≈ Mumbai on-road ₹14.5 L; Delhi on-road ₹12.73 L)" | Clarify ex-showroom vs on-road |
| 13 | Param table | "Boot Space 400 L" | "Boot Space 400 L (+18 L vs Dzire 382 L; pack in floor)" | Note pack-in-floor achievement |

## Slide 5 — POWERTRAIN

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 14 | Specs table | "263 km claimed" | "268 km at 15% reserve (315 km at zero reserve)" | 263 km inconsistent with 12.84 kWh/100km |
| 15 | Specs table | "10–90% — 36 kWh usable" | "40.5 kWh usable (10% reserve on 45 kWh nameplate)" | 36 kWh assumes 10-90% window; convention is 10% reserve |
| 16 | Pack sizing | "200 km/day: 34 kWh → 45 kWh" | "200 km/day: 25.68 kWh → 45 kWh (with SoH headroom)" | 34 kWh implies 17 kWh/100km; should be 12.84 |
| 17 | Pack sizing | "300 km/day: 51 kWh → 45 kWh" | "300 km/day: 44.1 kWh at 48°C" | 51 kWh implies 17 kWh/100km |
| 18 | Specs table | "11 kW AC, 3-phase, 23 hr overnight window" | "11 kW AC, 3-phase, 3.86 h overnight (25.68 kWh ÷ 7.4 kW × 0.90)" | 23 h is wrong; 3.86 h is correct |
| 19 | Comparison table | "1:3 charger-to-vehicle ratio" | "1 port/vehicle; 1:3 fleet utilization (port shared across 3 vehicles)" | Ratio was misinterpreted |
| 20 | Pack sizing | "77.3% SoH at year 8" | "71.9% SoH at year 8 (48°C design point, 44.1 kWh usable)" | 77.3% mixes 40°C and 48°C points |
| 21 | Pack sizing | "44.2 kWh usable" | "44.1 kWh usable at 48°C (71.9% SoH)" | Consistent with 48°C design point |
| 22 | Comparison table | "35,000 public charging ports for 5.7 million EVs; 160 EVs per port" | "52,718–67,657 public charging points (Jul–Aug 2026); ~1 crore registered EVs; ~190–235 EVs/port" | Data dramatically outdated |
| 23 | Without depot charging | "Green SM Noida quote: ~2.5 h/day lost" | "Green SM Noida ~2.5 h/day lost to queues (Indian Express, 1 Sep 2026); 75 h/month is deck's derivation" | Clarify derivation |

## Slide 6 — SODIUM-ION

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 24 | Scale | "Reliance Jamnagar 40 GWh, ramping H2 2026" | "Reliance Jamnagar: 40 GWh Phase 1 LFP, H2 2026 (commissioning, not yet producing); full site 120 GWh (revised from 100)" | Target revised; production not commenced |
| 25 | Certification | "No sodium-ion cell ever certified" | "No sodium-ion cell certified to IS 16893 Parts 2 & 3 (lithium-ion standard) as of public sources" | Absolute negative unverifiable |

## Slide 7 — TCO

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 26 | Cost stack | "Finance EMI EV ₹16,22,339" | "Finance EMI EV ₹16,22,339 (₹27,039/month × 60)" | Deck says ₹29,743/month — wrong; code gives ₹27,039 |
| 27 | Lever 1 | "₹14 L asset interest ₹3.85 L" | "₹3.50 L interest (₹27,039 × 60 − ₹12,72,600)" | Deck overstates by ₹0.35 L |
| 28 | Lever 1 | "Cash purchase gives +17.5% vs financed +8.4%" | "Delhi: financed +14.5%, cash +22.6%; Mumbai: financed +7.6%, cash +15.3%; Bengaluru: financed +8.2%, cash +16.4%" | Neither 17.5% nor 8.4% matches any city |
| 29 | City table | "Mumbai Financed: EV 6.47, CNG 7.00" | "Mumbai Financed: EV 6.47, CNG 7.30" | Deck understates CNG cost |
| 30 | City table | "Mumbai Cash: EV 5.35, CNG 6.32" | "Mumbai Cash: EV 5.35, CNG 6.52" | Deck understates CNG cost |
| 31 | Factors | "45 hours/month downtime headroom" | "45 h headroom (zero-base OPP_H figure; actual base case is 3.5 h/month with ₹200.46/h)" | Clarify basis |
| 32 | Conclusions | "Worth about five points" | **Remove** | Infra penalty is 8.1 pp (5-yr) / 10.7 pp (8-yr); "about five points" not derived from code |
| 33 | Factors | "Battery replacement: ₹4L → ₹7.04/km −4.5%" | Keep; add "derived, not code-verified" | Not in code but derived from pack cost |
| 34 | Factors | "Power-escalation break-even: Delhi 14.5%/yr, Mumbai 8.8%, Bengaluru 8.7%" | Keep; add "derived, not code-verified" | Not in code but derived |

## Slide 8 — DRIVER P&L & RIDER

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 35 | Driver P&L | "Advantage during loan +₹5,252/month" | "Advantage during loan +₹5,253/month" | 20,021 − 14,768 = 5,253; deck rounds to 5,252 |
| 36 | Platform model | "Legacy 20% per ride: EV ₹48,799" | "Legacy 20% per ride: EV ₹37,362, CNG ₹23,162, advantage ₹14,200" | ₹48,799 is zero-commission; correct is ₹37,362 |
| 37 | Platform model | "Legacy 25% per ride: EV ₹48,799" | "Legacy 25% per ride: EV ₹34,502, CNG ₹20,302, advantage ₹14,200" | Same error |
| 38 | What not to claim | "₹1.24 lakh/month reduction in operating costs" | **Remove** | Not derivable from code |

## Slide 9 — AI & CONNECTED

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 39 | TPMS | "TPMS: Normal 32–35 psi, 30–50°C; Warning <28 psi or >60°C; Critical <22 psi or >70°C" | Keep thresholds; add label "Tire pressure & temperature (not battery)" | Avoid confusion with 48°C battery design point |
| 40 | Fast charging | "CC phase charges to ~70–80% capacity" | "Depot 7.4 kW AC reaches 70–80% in 3.86 h at ₹5.50–9/kWh; DC fast charging reaches 70–80% in ~30 min at ₹18–24/kWh — the cost difference is why depot charging is default" | Make decision-relevant |
| 41 | Pilot targets | "Predictive maintenance: ≥7-day advance warning; 20–30% less downtime" | "Predictive maintenance: ≥7-day warning → ~₹133/vehicle/month (0.9% of driver advantage); 20–30% less downtime → ₹140–210/month (1.0–1.5%)" | Convert to ₹ |
| 42 | Pilot targets | "Smart dispatch: ~15% fewer deadhead km" | "Smart dispatch ~15% fewer deadhead km → ₹50–832/month (0.4–5.9%)" | Convert to ₹ |
| 43 | Pilot targets | "Smart charging: 15–18% lower charging cost" | "Smart charging 15–18% lower cost → ₹501–601/month (3.5–4.2%)" | Convert to ₹ |
| 44 | Pilot targets | (combined) | "Combined pilot value: ~₹824–1,776/vehicle/month (5.8–12.5% of ₹14,200 advantage) — incremental, not transformative" | Honest framing |
| 45 | Fast charging | CC/CV textbook content | **Cut or move to appendix** | Generic, not MACH1-specific |
| 46 | TPMS | TPMS thresholds | **Move to vehicle spec sheet** | Generic, not MACH1-specific |

## Slide 10 — ROADMAP

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 47 | Policy | "Delhi: 0% road tax for life of vehicle" | "Delhi: 0% road tax for EVs ≤₹30 lakh ex-showroom (draft 2026 policy); premium EVs excluded" | ₹30 L price cap in 2026 draft |
| 48 | Policy | "Karnataka: 20–25% capex, stamp-duty reimbursement" | "Karnataka: 15–25% capital subsidy; 100% stamp duty; zero road tax & registration for EVs (exemption ended April 2026 for EVs >₹10 L)" | Consumer incentives DO exist |
| 49 | Infrastructure | "AIS-138 Part 2 amended 2022 mandates CCS2" | "AIS-138 Part 2 (2022): permits multiple DC standards (CCS2, CHAdeMO, GB/T, Bharat DC-001); CCS2 is market-driven de facto" | Standard is technology-agnostic |
| 50 | Localisation | "ACC PLI: 1.4 of 50 GWh (2.8%)" | "ACC PLI: ~1.0–1.4 GWh as of Oct 2025 (2.8%); under 2 GWh as of Oct 2026" | Figure slightly dated |
| 51 | Localisation | "Reliance Jamnagar 40 GWh" | "Reliance Jamnagar: 40 GWh Phase 1 LFP, H2 2026 (commissioning, not yet producing); full site 120 GWh" | Target revised upward |
| 52 | Policy | "PM E-DRIVE ₹11,900 cr covers 2W, 3W, ... — not 4W" | Keep; note outlay enhanced from ₹10,900 cr to ₹11,900 cr (Aug 2026) | — |

## Slide 11 — SYNTHESIS

| # | Location | Old text | New text | Reason |
|---|----------|----------|----------|--------|
| 53 | Synthesis | "Worth about five points" | **Remove** | Not in code; infra penalty is 8.1/10.7 pp |
| 54 | Synthesis | All other figures | Keep | Verified against code and sources |

---

## Items kept (no change needed)

- TCO headline: +14.5% nominal excl-infra; +6.5% nominal incl-infra; +6.7% NPV incl-infra (5yr) / +14.6% (8yr) — code confirms
- Driver take-home: ₹47,060 (EV) vs ₹32,860 (CNG); advantage +₹14,200/month — code confirms
- All external claims: 10 of 14 confirmed against primary sources; 4 differ (documented above)
- All rider survey figures: 17,993 respondents (LocalCircles), SERVQUAL n=148, Dzire sub-ratings — all sourced
- All powertrain specs under single convention: 45 kWh, 12.84 kWh/100km, 10% reserve, 48°C design point, 7.4 kW/3.86 h, 178 EFC/yr

---

**Total: 54 edits across 10 slides.**
**Full corrected text:** CORRECTED_DECK_TEXT.md
**Full evidence:** EVIDENCE_BINDER_INDEX.md
**Full numbers:** CHEAT_SHEET_25_NUMBERS.md
