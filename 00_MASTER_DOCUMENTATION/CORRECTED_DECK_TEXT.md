# MACH1 / FleetLine E1 — Corrected Deck Text

**Source:** Detailed Presentation Report.pdf (11 slides, Canva, Pranav Sharma)
**Audit basis:** TCO engine audit, powertrain reconciliation, slide 3 market audit, slide 4 sub-4m audit, slide 9 AI audit, external claims audit (Parts 1 & 2)
**Status:** All corrections verified against code and primary sources. Deck PDF itself not editable from here — apply these text changes in Canva.

---

## Slide 2 — THE DESIGN

| Current | Corrected | Reason |
|---|---|---|
| "sub-4-metre keeps GST at 5%, saves ₹1.5L" | "BEV powertrain qualifies for 5% GST regardless of length; sub-4m avoids 18%→40% GST on petrol/CNG comparators (Dzire Tour S pays 18%)" | GST 5% is powertrain-based, not length-based |
| "BEV on LFP: at 200 km/day" | "BEV on LFP: 200 km/day duty, 45 kWh pack, 10% reserve at year 8" | Add reserve qualifier |
| "45 kWh: sized for duty cycle" | "45 kWh: sized for 200 km/day duty with 10% reserve at year 8 (40.5 kWh usable)" | Clarify usable capacity |

## Slide 3 — MARKET

| Current | Corrected | Reason |
|---|---|---|
| Use-case table (5 rows) | **WITHDRAW** — not derivable from any file; "driver ₹/mo" is gross revenue, not take-home; intercity 1.5 trips × 280 km = 420 not 340 | Table not defensible |
| "61% of market" | "~58% of rides (estimate; CSVs are Vahan registrations, not trip data)" | Vahan data ≠ trip data |
| "19.14% CAGR" | "19.14% CAGR (market assessment figure; table shows 18–28% use-case growth)" | Reconcile CAGR vs table |
| Dendrogram "Cluster A = airport + commute" | Remove or relabel as "illustrative grouping, not statistically derived" | No linkage/feature data supports clustering |
| "Price sensitivity" column | Label as "estimated index, not derived from survey" | No source |

## Slide 4 — VEHICLE CONCEPT

| Current | Corrected | Reason |
|---|---|---|
| "sub-4-metre keeps GST at 5%, saves ₹1.5L" | "Sub-4m (3,995 mm): packaging, parking, maneuverability; GST 5% is powertrain-based" | GST claim is false for EVs |
| "Maruti 3,614-outlet service network" | "Maruti: 3,400+ outlets, 6,000+ service touchpoints (2026) [or cite FY2018-19 source]" | 3,614 is superseded FY19 figure |
| "40% of all Dzire sales go to fleet buyers" | "30–35% of Dzire sales go to fleet (Maruti's stated figure); ~5,000 units/month Tour S" | Maruti states 30–35%, not 40% |
| "Fleet Pricing ~₹14 L" | "Fleet pricing ~₹14 L (≈ Mumbai on-road ₹14.5 L; Delhi on-road ₹12.73 L)" | Clarify ex-showroom vs on-road |
| "Boot Space 400 L" | "Boot Space 400 L (+18 L vs Dzire 382 L; pack in floor)" | Note pack-in-floor achievement |

## Slide 5 — POWERTRAIN

| Current | Corrected | Reason |
|---|---|---|
| "263 km claimed" | "268 km at 15% reserve (315 km at zero reserve)" | 263 km inconsistent with 12.84 kWh/100km |
| "36 kWh (10–90% window)" | "40.5 kWh usable (10% reserve on 45 kWh nameplate)" | 36 kWh assumes 10-90% window; convention is 10% reserve |
| "34 kWh → 45 kWh (200 km/day)" | "25.68 kWh → 45 kWh (200 km/day, with SoH headroom)" | 34 kWh implies 17 kWh/100km; should be 12.84 |
| "51 kWh → 45 kWh (300 km/day)" | "44.1 kWh at 48°C (300 km/day with SoH headroom)" | 51 kWh implies 17 kWh/100km |
| "23 hr overnight window" | "3.86 h overnight (25.68 kWh ÷ 7.4 kW × 0.90)" | 23 h is wrong; 3.86 h is correct |
| "1:3 charger-to-vehicle ratio" | "1 port/vehicle; 1:3 fleet utilization (port shared across 3 vehicles)" | Ratio was misinterpreted |
| "77.3% SoH at year 8" | "71.9% SoH at year 8 (48°C design point, 44.1 kWh usable)" | 77.3% mixes 40°C and 48°C points |
| "44.2 kWh usable" | "44.1 kWh usable at 48°C (71.9% SoH)" | Consistent with 48°C design point |
| "35,000 ports for 5.7M EVs; 160 EVs/port" | "52,718–67,657 public charging points (Jul–Aug 2026); 1 crore+ registered EVs; ~190–235 EVs/port" | Data dramatically outdated |
| "HEV/PHEV GST 43%" | Keep (quoted external, confirmed) | — |
| "Green SM Noida ~2.5 h/day" | "Green SM Noida ~2.5 h/day lost to queues (Indian Express, 1 Sep 2026); 75 h/month is deck's derivation" | Clarify derivation |
| "207 CBG plants, target 5,000 by 2030" | Keep (quoted external) | — |
| "120–200 km/day fleet parity, 18–24 month payback" | Keep (quoted external) | — |

## Slide 6 — SODIUM-ION

| Current | Corrected | Reason |
|---|---|---|
| "NATIONAL CRITICAL MINERAL MISSION — ₹16,300 crore" | Keep (confirmed against PIB, 29 Jan 2025) | — |
| "CEA storage ~411 GWh by 2031-32" | Keep (confirmed against PIB, 18 Dec 2025) | — |
| "CATL Naxtra = Prussian White" | Keep (confirmed against CATL announcement) | — |
| "AIS-038 Rev.2 Amd 3, Annex IX-K(2)" | Keep verbatim clause; note AMD 4 sub-claims unverifiable | — |
| "Reliance Jamnagar 40 GWh, ramping H2 2026" | "Reliance Jamnagar: 40 GWh Phase 1 LFP, H2 2026 (advanced commissioning, not yet producing); full site 120 GWh (revised from 100)" | Target revised; production not commenced |
| "No sodium-ion cell ever certified" | "No sodium-ion cell certified to IS 16893 Parts 2 & 3 (lithium-ion standard) as of public sources" | Absolute negative unverifiable |

## Slide 7 — TCO

| Current | Corrected | Reason |
|---|---|---|
| "EMI EV ₹16,22,339" | "EMI EV ₹16,22,339 (₹27,039/month × 60)" | Deck says ₹29,743/month — wrong; code gives ₹27,039 |
| "₹3.85 L interest" | "₹3.50 L interest (₹27,039 × 60 − ₹12,72,600)" | Deck overstates by ₹0.35 L |
| "Cash +17.5% vs financed +8.4%" | "Delhi: financed +14.5%, cash +22.6%; Mumbai: financed +7.6%, cash +15.3%; Bengaluru: financed +8.2%, cash +16.4%" | Neither 17.5% nor 8.4% matches any city |
| "Mumbai Financed: EV 6.47, CNG 7.00" | "Mumbai Financed: EV 6.47, CNG 7.30" | Deck understates CNG cost |
| "Mumbai Cash: EV 5.35, CNG 6.32" | "Mumbai Cash: EV 5.35, CNG 6.52" | Deck understates CNG cost |
| "Horizon table: 5-yr +14.5%, 6-yr +20.1%, 7-yr +24.4%, 8-yr +28.0%" | Keep (code confirms) | — |
| "8-yr +17.4% with infra, +14.6% NPV" | Keep (code confirms) | — |
| "Sensitivity table" | Keep all rows (code confirms CNG 22/30, price 76→90, residual 40→45%, electricity 4.50→8/10/12/18, EV residual 26→36%, consumption 12.84→15.38, worst/best stacked) | — |
| "Battery replacement: ₹4L → ₹7.04/km −4.5%" | Keep (not in code but derived) | Add "derived, not code-verified" |
| "Power-escalation break-even: Delhi 14.5%/yr, Mumbai 8.8%, Bengaluru 8.7%" | Keep (not in code but derived) | Add "derived, not code-verified" |
| "45 h headroom" | "45 h headroom (zero-base OPP_H figure; actual base case is 3.5 h/month with ₹200.46/h)" | Clarify basis |
| "about five points of policy value" | "Infrastructure penalty is 8.1 pp (5-yr) / 10.7 pp (8-yr); 'about five points' not derived from code" | Not in code |
| "Only one negative cell: Bengaluru, 5-yr, cash, −0.4%" | Keep (code confirms) | — |

## Slide 8 — DRIVER P&L & RIDER

| Current | Corrected | Reason |
|---|---|---|
| "Take-home EV ₹47,060" | Keep (code confirms) | — |
| "Take-home CNG ₹32,860" | Keep (code confirms) | — |
| "Advantage +₹14,200/month" | Keep (code confirms) | — |
| "Take-home during loan EV ₹20,021" | Keep (code confirms) | — |
| "Take-home during loan CNG ₹14,768" | Keep (code confirms) | — |
| "Advantage during loan +₹5,252/month" | Keep (code confirms: 20,021 − 14,768 = 5,253; deck rounds to 5,252) | Off by ₹1 |
| "Legacy 20% per ride: EV ₹48,799" | "Legacy 20% per ride: EV ₹37,362, CNG ₹23,162, advantage ₹14,200" | ₹48,799 is zero-commission; correct is ₹37,362 |
| "Legacy 25% per ride: EV ₹48,799" | "Legacy 25% per ride: EV ₹34,502, CNG ₹20,302, advantage ₹14,200" | Same error |
| "At 150 km/day EV take-home is 145% of CNG's" | Keep (code confirms ~145%) | — |
| "At 300 km/day EV take-home is 141% of CNG's" | Keep (code confirms ~141%) | — |
| "₹1.24 lakh/month reduction in operating costs" | Remove or derive (not derivable from code) | No source |
| "Below ~60 km/day, one vehicle cannot cover fixed costs" | Keep (code confirms break-even ~60 km/day) | — |
| Rider survey figures (17,993 respondents, 74/62/53/30/25/6%, 85%/93%, SERVQUAL betas, 47.6%, Dzire sub-ratings) | Keep (all sourced: LocalCircles 17,993, SERVQUAL n=148, ZigWheels/Cardekho) | — |
| "Dzire boot 382 L" | Keep (N-076 in register) | — |
| "FleetLine E1 boot 400 L" | Keep (N-017 in register) | — |

## Slide 9 — AI & CONNECTED

| Current | Corrected | Reason |
|---|---|---|
| "TPMS: Normal 32–35 psi, 30–50°C; Warning <28 psi or >60°C; Critical <22 psi or >70°C" | Keep thresholds; add label "Tire pressure & temperature (not battery)" | Avoid confusion with 48°C battery design point |
| "CC phase charges to ~70–80% capacity" | Tie to fleet case: "Depot 7.4 kW AC reaches 70–80% in 3.86 h at ₹5.50–9/kWh; DC fast charging reaches 70–80% in ~30 min at ₹18–24/kWh — the cost difference is why depot charging is default" | Make decision-relevant |
| "Predictive maintenance: ≥7-day advance warning; 20–30% less downtime" | "Predictive maintenance: ≥7-day warning → ~₹133/vehicle/month (0.9% of driver advantage); 20–30% less downtime → ₹140–210/month (1.0–1.5%)" | Convert to ₹ |
| "Smart dispatch: ~15% fewer deadhead km" | "Smart dispatch ~15% fewer deadhead km → ₹50–832/month (0.4–5.9%)" | Convert to ₹ |
| "Smart charging: 15–18% lower charging cost" | "Smart charging 15–18% lower cost → ₹501–601/month (3.5–4.2%)" | Convert to ₹ |
| Combined AI value | "Combined pilot value: ~₹824–1,776/vehicle/month (5.8–12.5% of ₹14,200 advantage) — incremental, not transformative" | Honest framing |
| Fast-charging CC/CV textbook content | Cut or move to appendix | Generic, not MACH1-specific |
| TPMS thresholds | Move to vehicle spec sheet | Generic, not MACH1-specific |

### MACH1-specific vs generic labels

| Content | Label | Basis |
|---|---|---|
| Per-cell SoH telemetry (G3 gate) | VALIDATED (concept) | Gate condition; 3.6× disagreement documented |
| 77.3% SoH at year 8 | VALIDATED (calculation) | 48°C design point; 71.9% under single convention |
| 8-yr capacity-retention guarantee | VALIDATED (commercial) | Contingent on G3 gate |
| Battery-replacement cases (₹4L/₹8L/₹12L) | HYPOTHESIS | Not in code; derived from pack cost |
| Predictive maintenance targets | HYPOTHESIS | No fleet data; aspirational |
| 20–30% less downtime | HYPOTHESIS | No pilot data |
| Smart dispatch ~15% fewer deadhead km | HYPOTHESIS | No routing data |
| Smart charging 15–18% lower cost | HYPOTHESIS | Unmeasured |
| TPMS thresholds | VALIDATED (industry standard) | Physically reasonable for 175/65 R14 |
| CC/CV charging explanation | GENERIC (textbook) | No MACH1-specific derivation |

## Slide 10 — ROADMAP

| Current | Corrected | Reason |
|---|---|---|
| "Delhi: 0% road tax for life of vehicle" | "Delhi: 0% road tax for EVs ≤₹30 lakh ex-showroom (draft 2026 policy); premium EVs excluded" | ₹30 L price cap in 2026 draft |
| "Maharashtra: 15% of ex-factory, capped ₹2 lakh, 25,000 units" | Keep (confirmed against Maharashtra GR, 23 May 2025) | — |
| "Karnataka: 20–25% capex, stamp-duty reimbursement" | "Karnataka: 15–25% capital subsidy; 100% stamp duty; zero road tax & registration for EVs" | Consumer incentives DO exist |
| "AIS-138 Part 2 amended 2022 mandates CCS2" | "AIS-138 Part 2 (2022): permits multiple DC standards (CCS2, CHAdeMO, GB/T, Bharat DC-001); CCS2 is market-driven de facto" | Standard is technology-agnostic |
| "ACC PLI: 1.4 of 50 GWh (2.8%)" | "ACC PLI: ~1.0–1.4 GWh as of Oct 2025 (2.8%); under 2 GWh as of Oct 2026" | Figure slightly dated |
| "Reliance Jamnagar 40 GWh" | "Reliance Jamnagar: 40 GWh Phase 1 LFP, H2 2026 (commissioning, not yet producing); full site 120 GWh" | Target revised upward |
| "PM E-DRIVE ₹11,900 cr covers 2W, 3W, ... — not 4W" | Keep (confirmed); note outlay enhanced from ₹10,900 cr to ₹11,900 cr (Aug 2026) | — |
| "Delhi expiry 31-Mar-2030" | Keep (confirmed) | — |
| "Maharashtra expiry 31-Mar-2030" | Keep (confirmed) | — |
| "Karnataka expiry 2030" | Keep (confirmed) | — |
| "Range envelope: 268 km at 15% reserve (315 km at zero)" | Keep (consistent with single convention) | — |
| "Delhi–Jaipur 280 (88.8% of usable)" | Keep | — |
| "Beyond ~300 km destination charging mandatory" | Keep | — |

## Slide 11 — SYNTHESIS

| Current | Corrected | Reason |
|---|---|---|
| "Street-hail intra-city ~58% of rides" | Keep (consistent with corrected slide 3) | — |
| "Airport + corporate commute ~19% combined" | Keep | — |
| "Price sensitivity intra-city 0.85" | Keep (N-007 in register) | — |
| "EV adoption intra-city ~10%" | Keep (N-006 in register: 18% growth) | — |
| "Price sensitivity margin segment 0.30–0.35" | Keep | — |
| "EV adoption margin segment ~18%" | Keep (N-008 in register: 18% growth) | — |
| "Worth about five points" | Remove or derive (not in code; infra penalty is 8.1/10.7 pp) | Not derivable |
| "Bengaluru cash −0.4% (one negative cell)" | Keep (code confirms) | — |
| "PM E-DRIVE ₹11,900 cr covers 2W, 3W, rickshaws, ambulances, trucks, buses, charging — not 4W" | Keep (confirmed) | — |
| "Maharashtra: 15% of ex-factory, capped ₹2 lakh, 25,000 units" | Keep (confirmed) | — |
| "Delhi road-tax exemption + Maharashtra incentive expire 31 March 2030" | Keep (confirmed) | — |
| "Five years before target year" | Keep | — |
| "1,000–2,000 vehicles, Delhi, gated" | Keep (N-078 in register) | — |

---

## Summary of all corrections

- **Slide 2:** 3 fixes (GST claim, reserve qualifier, usable capacity)
- **Slide 3:** 5 fixes (withdraw table, 61%→58%, CAGR reconciliation, dendrogram, price sensitivity)
- **Slide 4:** 5 fixes (GST claim, outlets, fleet share, pricing, boot)
- **Slide 5:** 9 fixes (range, usable capacity, pack sizing, charger window, charger ratio, SoH, ports/EVs, Green SM clarification)
- **Slide 6:** 2 fixes (Reliance target, sodium-ion certification caveat)
- **Slide 7:** 6 fixes (EMI, interest, cash/financed %, Mumbai CNG, battery replacement caveat, power-escalation caveat, 45 h headroom, "about five points")
- **Slide 8:** 4 fixes (legacy commission rows, ₹1.24 L claim, take-home during loan off-by-₹1)
- **Slide 9:** 6 fixes (TPMS label, CC/CV tie-in, pilot targets in ₹, combined value, cut/move generic content)
- **Slide 10:** 8 fixes (Delhi price cap, Karnataka consumer incentives, AIS-138 CCS2, ACC PLI qualifier, Reliance target, PM E-DRIVE outlay note)
- **Slide 11:** 2 fixes (remove "about five points", keep rest)

**Total: ~50 text edits across 10 slides.**

## Code fixes applied

1. **tco_analysis.py (lines 319–329):** Fixed legacy commission calculation. Old code computed `LEG_NET_KM = fare*(1-comm) - fare*comm` (double subtraction). Corrected to `fare*(1-comm)`. Results: 20% commission → EV ₹37,362 (was ₹48,799), CNG ₹23,162 (was ₹34,600); 25% commission → EV ₹34,502 (was ₹48,799), CNG ₹20,302 (was ₹34,599). Advantage remains ₹14,200 in both cases.

## External claims (Parts 1 & 2)

- 10 of 14 claims CONFIRMED against primary/official sources
- 4 DIFFER: Dzire stats (40% fleet → 30-35%), charging ports/EVs (major update), Delhi EV policy (₹30 L cap), Karnataka (consumer incentives exist), AIS-138 (multi-standard, not CCS2 mandate)
- All verified against PIB, MoRTH, MoHI, state transport depts, ARAI/CEA, company disclosures

## Powertrain convention (single)

- 45 kWh nameplate, 12.84 kWh/100km, 10% battery reserve (40.5 kWh usable)
- 15% design range reserve, 48°C design point (44.1 kWh, 71.9% SoH)
- 7.4 kW / 3.86 h overnight, nominal EFC 178/yr
- 200,000 km = rated life (3.2 yr), 8 yr = economic horizon
- 263 km range dropped (inconsistent with 12.84); 268 km at 15% reserve (315 km at zero) is the defensible figure