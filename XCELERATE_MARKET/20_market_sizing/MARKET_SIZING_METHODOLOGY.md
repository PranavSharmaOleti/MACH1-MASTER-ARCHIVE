# Market Sizing and 2035 Forecast — Methodology Report

**Project:** Maruti Suzuki XCELerate 2026 E-Track — FleetLine E1
**Deliverable:** Market Sizing — top-down + bottom-up estimates, 2035 forecast, scenario comparison
**Date:** 3 November 2026
**Model file:** `market_sizing_model.xlsx` (7 sheets, all formulas live)

---

## 1. Audit of existing claims: "2.4 billion rides in 2024" and "14.8 billion rides projected for 2035"

**Result: These claims were NOT found in any project file.**

Searched: deck PDF, all Key docs PDFs, all CSVs, all Python scripts, all HTML files, all markdown files, the NITDurgapur Round-1 report, and the MACH1_MASTER_ARCHIVE. The strings "2.4 billion" and "14.8 billion" (in the context of ride counts) appear in none of them.

**Possible origins:**
- Mordor Intelligence "India Taxi Market" report (cited as secondary cross-check in MACH1_MARKET_ASSESSMENT.pdf) — Mordor reports typically use proprietary frameworks and revenue/value shares
- An external source not in the project archive
- A different version of the presentation not included in the working files

**Assessment:** Without the original source, these claims cannot be verified. The project's own ruling document (MACH1_MARKET_ASSESSMENT.pdf, 18 Oct 2026) explicitly forbids extending the 591.3M ride proxy to 2035 with a CAGR. The 14.8B figure implies a 6.2× growth over 11 years (CAGR ~18.5%), which is not supported by any observed trend in the archive.

**Recommendation:** Do not use these claims. Replace with the transparent scenario framework below.

---

## 2. Permitted formula (from MACH1_MARKET_ASSESSMENT.pdf)

```
Annual addressable GMV = observed annual ride count
                        × target-segment share of those rides
                        × average realized fare in the target segment

Target active vehicles = target-segment annual rides ÷ rides per active vehicle per year

Annual vehicle opportunity = target active fleet × (net fleet growth + annual replacement rate)

MACH1 units = annual vehicle opportunity × serviceable city share × attainable OEM share
```

**Key rule:** Do not call GMV "TAM/SAM/SOM" or a forecast. Do not extend 591.3M to 2035 with a CAGR. Do not sum overlapping segments without de-duplication.

---

## 3. Top-down estimate

### 3.1 Observed annual rides [reported, Grade B]

| Platform | Daily rides | Source | Date |
|---|---|---|---|
| Uber | 840,000 | Motilal Oswal via Business Standard | 18 Apr 2025 |
| Ola | 460,000 | Same | 18 Apr 2025 |
| Rapido | 320,000 | Same (vehicle-class scope unclear) | 18 Apr 2025 |
| **Combined** | **1,620,000** | Sum | — |
| **Annualized** | **591.3M** | ×365 days | Run-rate assumption |

**Caveat:** This is a platform ride-flow proxy, not a national taxi-market census. It excludes street-hail, offline bookings, corporate fleets, and auto-rickshaws.

### 3.2 Scenario results

| Scenario | Target share | Fare | Target rides | GMV (INR cr) | Active vehicles | E1 units |
|---|---|---|---|---|---|---|
| Conservative | 5% | ₹300 | 29.6M | ₹887 | 14,212 | 43 |
| Base | 10% | ₹450 | 59.1M | ₹2,661 | 28,423 | 85 |
| Optimistic | 15% | ₹600 | 88.7M | ₹5,322 | 42,635 | 128 |

**Note:** E1 units = vehicle opportunity × 60% city share × 5% OEM share. These are illustrative, not forecasts.

---

## 4. Bottom-up estimate (airport segment)

### 4.1 Inputs [reported, Grade A]

| Input | Value | Source |
|---|---|---|
| AAI passengers (Apr-Sep 2026) | 196.24M | AAI Traffic Report, Sep 2026 |
| Annualized passengers | ~392.5M | ×2 (Apr-Sep → full year) |
| Road trips (to + from airport) | ~785M | ×2 per passenger |
| App-cab mode share | 15-35% | Assumption (no sourced data) |

### 4.2 Results

| Scenario | Mode share | Airport app-cab trips | % of platform rides | Active vehicles | E1 units |
|---|---|---|---|---|---|
| Conservative | 15% | 117.7M | 19.9% | 56,606 | 170 |
| Base | 25% | 196.2M | 33.2% | 94,346 | 283 |
| Optimistic | 35% | 274.7M | 46.5% | 132,087 | 396 |

**Key insight:** Airport is NOT a niche segment. Even at conservative mode share (15%), it represents ~20% of platform rides. At base (25%), it is one-third.

---

## 5. Distinctions maintained

| Metric | Definition | Value (base) | Unit |
|---|---|---|---|
| Ride volume | Number of trips | 59.1M (target segment) | rides/yr |
| Transaction value (GMV) | Rides × fare | ₹2,661 crore | INR/yr |
| Operator revenue | GMV × operator take | Not computed (no operator take data) | INR/yr |
| Vehicle sales (opportunity) | Active vehicles × (growth + replacement) | 28,423 (top-down) / 94,346 (airport) | vehicles/yr |
| Addressable (FleetLine E1) | Vehicle opportunity × city share × OEM share | 85 (top-down) / 283 (airport) | vehicles/yr |

**These are fundamentally different quantities and must not be conflated.**

---

## 6. Sensitivity analysis

The model is most sensitive to:
1. **Target segment share** (5-15% range) — dominant driver of GMV and vehicle demand
2. **Average realized fare** (₹300-₹600) — second most important
3. **Rides per active vehicle per year** (1,500-2,500) — inversely affects vehicle count
4. **App-cab mode share** (15-35%) — airport segment only

All other variables (growth rate, replacement rate, city share, OEM share) have moderate impact.

---

## 7. What the model does NOT do

1. **No 2035 forecast** — the market assessment explicitly forbids extending 591.3M to 2035 with a CAGR. This model sizes the current market and derives vehicle demand from current ride volumes. A 2035 projection requires validated base series and segment allocation.
2. **No operator revenue** — no data on operator take rates, commissions, or subscription revenue.
3. **No vehicle sales forecast** — the addressable vehicle numbers are illustrative, not forecasts. They depend on assumptions about fleet growth, replacement, and OEM share that are not measured.
4. **No segment-level sizing** — without trip-level data, segment shares are assumptions, not measurements.

---

## 8. Unresolved questions

1. What is the actual target-segment share of platform rides? (Assumed 5-15%; no measurement exists)
2. What is the actual realized fare in the target segment? (Assumed ₹300-₹600; only broad ₹300 reference exists)
3. What is the actual app-cab mode share at airports? (Assumed 15-35%; no data exists)
4. What is the actual rides-per-vehicle rate? (Assumed 2,080; no fleet utilization data exists)
5. What is the actual fleet growth and replacement rate? (Assumed 3% and 15%; no data exists)
6. What is the actual serviceable city share? (Assumed 60%; no geographic data exists)
7. What is the actual attainable OEM share? (Assumed 5%; no competitive data exists)

---

*All formulas, assumptions, and sources are in `market_sizing_model.xlsx`. No figures were invented. All gaps are explicitly identified.*
