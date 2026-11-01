# MACH1 / FleetLine E1 — Revised Deck with Change Log

**Original:** Detailed Presentation Report.pdf (11 slides, Canva, Pranav Sharma)
**Revised:** FleetLine E1 — Corrected Deck (all text changes applied)
**Basis:** CORRECTED_DECK_TEXT.md (50 edits across 10 slides, verified against code and primary sources)

---

## Change log (summary)

| Slide | Edits | Type |
|-------|-------|------|
| 2 | 3 | GST claim rewrite, reserve qualifier, usable capacity |
| 3 | 5 | Withdraw table, 61%→58%, CAGR reconcile, dendrogram removal, price sensitivity label |
| 4 | 5 | GST claim rewrite, outlets update, fleet share update, pricing clarify, boot note |
| 5 | 9 | Range, usable capacity, pack sizing, charger window, charger ratio, SoH, ports/EVs, Green SM clarify |
| 6 | 2 | Reliance target, sodium-ion certification caveat |
| 7 | 8 | EMI, interest, cash/financed %, Mumbai CNG, battery replacement caveat, power-escalation caveat, 45 h headroom, "about five points" removal |
| 8 | 4 | Legacy commission rows fix, ₹1.24 L removal, take-home off-by-₹1 |
| 9 | 6 | TPMS label, CC/CV tie-in, pilot targets in ₹, combined value, cut/move generic content |
| 10 | 8 | Delhi price cap, Karnataka incentives, AIS-138 CCS2, ACC PLI qualifier, Reliance target, PM E-DRIVE note |
| 11 | 2 | "About five points" removal, rest kept |
| **Total** | **~50** | |

---

## Slide-by-slide revised text (key changes only)

### Slide 2 — THE DESIGN
- **GST:** "BEV powertrain qualifies for 5% GST regardless of length; sub-4m avoids 18%→40% GST on petrol/CNG comparators (Dzire Tour S pays 18%)"
- **Reserve:** "BEV on LFP: 200 km/day duty, 45 kWh pack, 10% reserve at year 8"
- **Usable:** "45 kWh: sized for 200 km/day duty with 10% reserve at year 8 (40.5 kWh usable)"

### Slide 3 — MARKET
- **Table:** WITHDRAW — not derivable. Replace with duty-cycle argument (pre-booked, depot-return, schedulable overnight charging).
- **Market share:** "~58% of rides (estimate; CSVs are Vahan registrations, not trip data)"
- **CAGR:** "19.14% CAGR (market assessment figure; table shows 18–28% use-case growth)"
- **Dendrogram:** Remove or relabel as "illustrative grouping, not statistically derived"
- **Price sensitivity:** Label as "estimated index, not derived from survey"

### Slide 4 — VEHICLE CONCEPT
- **GST:** "Sub-4m (3,995 mm): packaging, parking, maneuverability; GST 5% is powertrain-based"
- **Outlets:** "Maruti: 3,400+ outlets, 6,000+ service touchpoints (2026)"
- **Fleet share:** "30–35% of Dzire sales go to fleet (Maruti's stated figure); ~5,000 units/month Tour S"
- **Pricing:** "Fleet pricing ~₹14 L (≈ Mumbai on-road ₹14.5 L; Delhi on-road ₹12.73 L)"
- **Boot:** "Boot Space 400 L (+18 L vs Dzire 382 L; pack in floor)"

### Slide 5 — POWERTRAIN
- **Range:** "268 km at 15% reserve (315 km at zero reserve)" (drop 263 km)
- **Usable:** "40.5 kWh usable (10% reserve on 45 kWh nameplate)" (drop 36 kWh)
- **Pack sizing:** "25.68 kWh → 45 kWh (200 km/day, with SoH headroom)" and "44.1 kWh at 48°C (300 km/day)"
- **Charger:** "3.86 h overnight (25.68 kWh ÷ 7.4 kW × 0.90)" (drop 23 h)
- **Ratio:** "1 port/vehicle; 1:3 fleet utilization (port shared across 3 vehicles)"
- **SoH:** "71.9% SoH at year 8 (48°C design point, 44.1 kWh usable)" (drop 77.3%)
- **Ports/EVs:** "52,718–67,657 public charging points (Jul–Aug 2026); ~1 crore registered EVs; ~190–235 EVs/port"
- **Green SM:** "Green SM Noida ~2.5 h/day lost to queues (Indian Express, 1 Sep 2026); 75 h/month is deck's derivation"

### Slide 6 — SODIUM-ION
- **Reliance:** "Reliance Jamnagar: 40 GWh Phase 1 LFP, H2 2026 (commissioning, not yet producing); full site 120 GWh (revised from 100)"
- **Certification:** "No sodium-ion cell certified to IS 16893 Parts 2 & 3 (lithium-ion standard) as of public sources"

### Slide 7 — TCO
- **EMI:** "EMI EV ₹16,22,339 (₹27,039/month × 60)" (deck said ₹29,743/month — wrong)
- **Interest:** "₹3.50 L interest (₹27,039 × 60 − ₹12,72,600)" (deck said ₹3.85 L)
- **Cash/financed:** "Delhi: financed +14.5%, cash +22.6%; Mumbai: +7.6% / +15.3%; Bengaluru: +8.2% / +16.4%" (neither 17.5% nor 8.4% matches any city)
- **Mumbai CNG:** Financed CNG 7.30 (was 7.00); Cash CNG 6.52 (was 6.32)
- **Battery replacement:** Keep; add "derived, not code-verified"
- **Power-escalation break-even:** Keep; add "derived, not code-verified"
- **45 h headroom:** "45 h headroom (zero-base OPP_H figure; actual base case is 3.5 h/month with ₹200.46/h)"
- **"About five points":** Remove. Infra penalty is 8.1 pp (5-yr) / 10.7 pp (8-yr).
- **Negative cell:** Keep — "Only one negative cell: Bengaluru, 5-yr, cash, −0.4%" (code confirms)

### Slide 8 — DRIVER P&L & RIDER
- **Take-home during loan:** "Advantage during loan +₹5,253/month" (was +₹5,252; off by ₹1)
- **Legacy 20%:** "EV ₹37,362, CNG ₹23,162, advantage ₹14,200" (was ₹48,799 — zero-commission error)
- **Legacy 25%:** "EV ₹34,502, CNG ₹20,302, advantage ₹14,200" (was ₹48,799)
- **₹1.24 L claim:** Remove (not derivable)
- **All other figures:** Keep (code confirms)

### Slide 9 — AI & CONNECTED
- **TPMS:** Keep thresholds; add "Tire pressure & temperature (not battery)"
- **CC/CV:** Tie to fleet case: "Depot 7.4 kW AC reaches 70–80% in 3.86 h at ₹5.50–9/kWh; DC fast charging reaches 70–80% in ~30 min at ₹18–24/kWh"
- **Pilot targets in ₹:** Predictive maintenance ~₹133/mo; smart dispatch ₹50–832/mo; smart charging ₹501–601/mo
- **Combined AI value:** "~₹824–1,776/vehicle/month (5.8–12.5% of ₹14,200 advantage) — incremental, not transformative"
- **Generic content:** Cut TPMS thresholds and CC/CV textbook; move to appendix
- **Labels:** Per-cell SoH = VALIDATED (concept); predictive maintenance = HYPOTHESIS; etc.

### Slide 10 — ROADMAP
- **Delhi:** "0% road tax for EVs ≤₹30 lakh ex-showroom (draft 2026 policy); premium EVs excluded"
- **Karnataka:** "15–25% capital subsidy; 100% stamp duty; zero road tax & registration for EVs (exemption ended April 2026 for EVs >₹10 L)"
- **AIS-138:** "Permits multiple DC standards (CCS2, CHAdeMO, GB/T, Bharat DC-001); CCS2 is market-driven de facto"
- **ACC PLI:** "~1.0–1.4 GWh as of Oct 2025 (2.8%); under 2 GWh as of Oct 2026"
- **Reliance:** "40 GWh Phase 1 LFP, H2 2026 (commissioning, not yet producing); full site 120 GWh"
- **PM E-DRIVE:** Keep; note outlay enhanced from ₹10,900 cr to ₹11,900 cr (Aug 2026)
- **All other figures:** Keep

### Slide 11 — SYNTHESIS
- **"About five points":** Remove
- **All other figures:** Keep

---

## Code fix applied
- **tco_analysis.py (lines 319–329):** Fixed legacy commission calculation. Old: `LEG_NET_KM = fare*(1-comm) - fare*comm` (double subtraction). Corrected: `fare*(1-comm)`. Results: 20% → EV ₹37,362 (was ₹48,799), CNG ₹23,162 (was ₹34,600); 25% → EV ₹34,502 (was ₹48,799), CNG ₹20,302 (was ₹34,599). Advantage remains ₹14,200.

---

## Decision guide: revised deck vs errata handout

### Option A: Revised deck with change log (use if updates are allowed)
- **Pros:** Cleanest presentation; panel sees corrected numbers without cognitive load of tracking errata; change log demonstrates self-audit rigor.
- **Cons:** Requires Canva re-edit; risk of introducing new typos; panel may question why you changed things after submission.
- **When to use:** If competition rules allow resubmission or if you present in person with a revised PDF.

### Option B: Errata handout + spoken opener (use if no resubmission allowed)
- **Pros:** No re-edit risk; demonstrates intellectual honesty; panel hears corrections in your voice (more credible than silent edits); preserves original submission as-is.
- **Cons:** Panel must track two documents; cognitive load during presentation; may raise questions you didn't anticipate.
- **When to use:** If submission is locked and you present orally; also works as a supplement to Option A.

### Recommendation
**Present Option B (errata handout + spoken opener) even if you also have Option A.** The spoken opener ("we audited ourselves and found 31 items") is more credible than silent corrections. If you can also submit a revised deck, do both — the errata handout then becomes a "what changed" summary rather than a confession.

---

*Full corrected text: CORRECTED_DECK_TEXT.md*
*Full evidence: EVIDENCE_BINDER_INDEX.md*
*Full numbers: CHEAT_SHEET_25_NUMBERS.md*
*Full questions: MARUTI_PANEL_40_QUESTIONS.md*
