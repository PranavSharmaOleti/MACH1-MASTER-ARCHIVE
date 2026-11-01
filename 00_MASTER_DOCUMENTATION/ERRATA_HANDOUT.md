# MACH1 / FleetLine E1 — Errata & "What We Tightened Since Submission"

**Prepared for:** Maruti Suzuki panel review
**Original submission:** Detailed Presentation Report.pdf (11 slides, Canva, Pranav Sharma)
**Status:** All corrections verified against TCO code (tco_engine.py, tco_analysis.py) and primary sources (PIB, MoRTH, MoHI, state transport depts, ARAI/CEA)

---

## What we found and fixed (self-audit, not panel discovery)

After submission we ran a full audit of every number against our own code and sources. Here is what changed and why. We are presenting this proactively because we would rather you hear it from us.

### Tier 1 — Arithmetic corrections (code-verified)

| # | Slide | Original claim | Corrected | Source |
|---|-------|---------------|-----------|--------|
| 1 | 7 | EMI ₹29,743/month | ₹27,039/month (₹16,22,339 ÷ 60) | tco_engine.py |
| 2 | 7 | Interest ₹3.85 L | ₹3.50 L (₹27,039 × 60 − ₹12,72,600) | Derived from #1 |
| 3 | 7 | Cash +17.5% vs financed +8.4% | Delhi: financed +14.5%, cash +22.6%; Mumbai: +7.6% / +15.3%; Bengaluru: +8.2% / +16.4% | tco_engine.py city table |
| 4 | 7 | Mumbai Financed EV 6.47, CNG 7.00 | CNG 7.30 (deck understated CNG cost) | tco_engine.py |
| 5 | 7 | Mumbai Cash EV 5.35, CNG 6.32 | CNG 6.52 | tco_engine.py |
| 6 | 8 | Legacy 20% per ride EV ₹48,799 | EV ₹37,362, CNG ₹23,162 (commission was not deducted) | tco_analysis.py (fixed) |
| 7 | 8 | Legacy 25% per ride EV ₹48,799 | EV ₹34,502, CNG ₹20,302 | tco_analysis.py (fixed) |
| 8 | 8 | Advantage during loan +₹5,252 | +₹5,253 (20,021 − 14,768) — rounding | Arithmetic |
| 9 | 5 | 263 km range | 268 km at 15% reserve (315 km at zero reserve) | Powertrain convention |
| 10 | 5 | 36 kWh usable (10–90%) | 40.5 kWh usable (10% reserve on 45 kWh nameplate) | Single convention |
| 11 | 5 | 34 kWh → 45 kWh (200 km/day) | 25.68 kWh → 45 kWh (with SoH headroom) | 12.84 kWh/100km × 200 |
| 12 | 5 | 51 kWh → 45 kWh (300 km/day) | 44.1 kWh at 48°C | Single convention |
| 13 | 5 | 23 h overnight window | 3.86 h (25.68 kWh ÷ 7.4 kW × 0.90) | Single convention |
| 14 | 5 | 77.3% SoH at year 8 | 71.9% SoH at 48°C (44.1 kWh usable) | Single convention |
| 15 | 5 | 44.2 kWh usable | 44.1 kWh at 48°C | Single convention |

### Tier 2 — Data corrections (source-verified)

| # | Slide | Original | Corrected | Source |
|---|-------|----------|-----------|--------|
| 16 | 4 | "3,614-outlet service network" | 3,400+ outlets, 6,000+ service touchpoints (2026) | Maruti annual report (FY19 figure superseded) |
| 17 | 4 | "40% of Dzire sales to fleet" | 30–35% (Maruti's stated figure) | Maruti disclosure |
| 18 | 5 | "35,000 ports for 5.7M EVs; 160 EVs/port" | 52,718–67,657 public charging points (Jul–Aug 2026); ~1 crore registered EVs; ~190–235 EVs/port | MoHI/CEA |
| 19 | 10 | "Delhi: 0% road tax for life" | 0% road tax for EVs ≤₹30 lakh ex-showroom (2026 draft policy) | Delhi EV Policy 2026 |
| 20 | 10 | "Karnataka: 20–25% capex, stamp-duty reimbursement" | 15–25% capital subsidy; 100% stamp duty; zero road tax & registration for EVs (exemption ended April 2026 for EVs >₹10 L) | Karnataka EV Policy |
| 21 | 10 | "AIS-138 Part 2 mandates CCS2" | Permits multiple DC standards (CCS2, CHAdeMO, GB/T, Bharat DC-001); CCS2 is market-driven de facto | AIS-138 Part 2 (2022) |
| 22 | 10 | "ACC PLI: 1.4 of 50 GWh (2.8%)" | ~1.0–1.4 GWh as of Oct 2025; under 2 GWh as of Oct 2026 | MoHI update |
| 23 | 10 | "Reliance Jamnagar 40 GWh" | 40 GWh Phase 1 LFP, H2 2026 (commissioning, not yet producing); full site 120 GWh (revised from 100) | Financial Express, 29 May 2026 |

### Tier 3 — Claim withdrawals (not defensible as stated)

| # | Slide | Original claim | Action |
|---|-------|---------------|--------|
| 24 | 2/4/11 | "Sub-4-metre keeps GST at 5%, saves ₹1.5L" | **False for EVs.** GST 5% is powertrain-based, not length-based. Sub-4m avoids 18%→40% GST on petrol/CNG comparators (Dzire Tour S pays 18%). What 3,995 mm buys: packaging, parking, maneuverability. |
| 25 | 3 | Use-case table (5 rows) | **Withdrawn.** "Driver ₹/mo" is gross revenue, not take-home. Intercity 1.5 trips × 280 km = 420, not 340. Not derivable from any file. |
| 26 | 3 | "61% of market" | **Relabeled as estimate.** CSVs are Vahan registrations, not trip data. Corrected to ~58%. |
| 27 | 3 | Dendrogram "Cluster A = airport + commute" | **Removed.** No linkage/feature data supports clustering. |
| 28 | 7 | "45 h headroom" | **Clarified.** Zero-base OPP_H figure; actual base case is 3.5 h/month with ₹200.46/h. |
| 29 | 7 | "About five points of policy value" | **Removed.** Infra penalty is 8.1 pp (5-yr) / 10.7 pp (8-yr); "about five points" not derived from code. |
| 30 | 8 | "₹1.24 lakh/month reduction in operating costs" | **Removed.** Not derivable from code. |
| 31 | 9 | TPMS thresholds + CC/CV content | **Relabeled.** Moved to vehicle spec sheet / appendix. Generic, not MACH1-specific. |

### What we kept and verified (no change)

- **TCO headline:** +14.5% nominal excl-infra; +6.5% nominal incl-infra; +6.7% NPV incl-infra (5yr) / +14.6% (8yr). Code confirms all.
- **Driver take-home:** ₹47,060 (EV) vs ₹32,860 (CNG); advantage +₹14,200/month. Code confirms.
- **All external claims:** 10 of 14 confirmed against primary sources. 4 differ (documented above).
- **All rider survey figures:** 17,993 respondents (LocalCircles), SERVQUAL n=148, Dzire sub-ratings (ZigWheels/Cardekho). All sourced.
- **All powertrain specs under single convention:** 45 kWh, 12.84 kWh/100km, 10% reserve, 48°C design point, 7.4 kW/3.86 h, 178 EFC/yr.

### Spoken opener (if presenting errata verbally)

> "Before we begin, we want to flag something ourselves. After submission, we ran a full audit of every number in this deck against our own code and primary sources. We found 31 items that needed correction or qualification — 15 arithmetic, 8 data, and 8 claims we withdrew. We have a one-page errata handout. The headline TCO result — +14.5% nominal, +6.7% NPV at 5 years — survives every correction. The driver advantage of ₹14,200/month survives. What changed is the precision of the supporting numbers, not the conclusion. We would rather you hear this from us than find it yourselves."

---

*Prepared from: CORRECTED_DECK_TEXT.md, TCO engine audit, powertrain reconciliation, external claims audit Parts 1 & 2, slide 3 market audit, slide 4 sub-4m audit, slide 9 AI audit.*
