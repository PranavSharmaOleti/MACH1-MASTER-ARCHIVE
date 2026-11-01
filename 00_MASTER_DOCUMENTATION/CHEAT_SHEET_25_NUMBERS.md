# MACH1 / FleetLine E1 — 25 Numbers to Recite and Re-Derive

**Rule:** Every number below must be stated with its basis (nominal/NPV, with/without charger, financed/cash, city, horizon). If you can't state the basis, don't state the number.

---

## The 5 headline economics (must know cold)

| # | Number | Basis | Re-derive in one line |
|---|---|---|---|
| 1 | **₹5.75/km** (EV) vs **₹6.73/km** (CNG) | Delhi, 5-yr, financed, nominal, **excl-infra** | TCO/km: (EMI×60 + energy + maint + ins − residual) ÷ 62,400 km |
| 2 | **+14.5%** EV advantage | Delhi, 5-yr, financed, nominal, **excl-infra** | (6.73−5.75)/6.73 = 14.5% |
| 3 | **+6.7%** EV advantage | Delhi, 5-yr, financed, NPV 12%, escalated, **incl-infra** | Bottom-right cell of section L matrix |
| 4 | **+14.6%** EV advantage | Delhi, 8-yr, financed, NPV 12%, escalated, **incl-infra** | Same cell, 8-yr horizon |
| 5 | **₹14,200/month** | Delhi, yr6+ (no EMI), flat-fee, driver advantage | CNG opex (₹22,598) − EV opex (₹8,398) = ₹14,200 |

## The 5 driver P&L (slide 8)

| # | Number | Basis | Re-derive in one line |
|---|---|---|---|
| 6 | **₹47,060** (EV take-home, yr6+) | Delhi, 200 km/day, ₹11/km fare, no EMI | ₹55,458 net fare − ₹3,338 energy − ₹1,560 maint − ₹3,500 ins |
| 7 | **₹32,860** (CNG take-home, yr6+) | Same basis | ₹55,458 − ₹15,808 − ₹3,500 − ₹3,290 |
| 8 | **₹20,021** (EV during loan) | Delhi, 200 km/day, financed | ₹47,060 − ₹27,039 EMI |
| 9 | **₹14,768** (CNG during loan) | Same basis | ₹32,860 − ₹18,092 EMI |
| 10 | **₹5,252** (advantage during loan) | During loan period | ₹20,021 − ₹14,768 (note: exact is ₹5,253) |

## The 5 powertrain (slides 4-5)

| # | Number | Basis | Re-derive in one line |
|---|---|---|---|
| 11 | **45 kWh** (pack nameplate) | 48°C design point, 200 km/day | 25.68 kWh/day ÷ (0.719 SoH × 0.90 reserve × 0.90 ceff) = 44.1 → 45 |
| 12 | **268 km** (range at 15% reserve) | 45 kWh, 12.84 kWh/100km | 45×0.90÷12.84×100×(1−0.15) = 268 km (315 km at zero reserve) |
| 13 | **3.86 h** (overnight charge) | 25.68 kWh, 7.4 kW, 90% ceff | 25.68 ÷ (7.4 × 0.90) = 3.86 h |
| 14 | **71.9% SoH** (year 8, 48°C) | LFP at 48°C design point | Naumann √t: 3.7 yr to 80% at 40°C; at 48°C → 71.9% at year 8 |
| 15 | **178 EFC/yr** (nominal) | 62,400 km/yr, 45 kWh pack | 62,400 × 12.84/100 ÷ 45 = 178 (usable basis: 181.3; wall basis: 197.8) |

## The 5 TCO sensitivities (slide 7)

| # | Number | Basis | Re-derive in one line |
|---|---|---|---|
| 16 | **21.9 h** (downtime headroom) | Delhi, 5-yr, financed | Break-even 25.4 h/mo − 3.5 h base = 21.9 h (at ₹200.46/h net cost) |
| 17 | **₹99,000** (charger/vehicle) | Depot, 7.4 kW AC | (50,000 + 30,000 + 10,000) × 1.10 N+1 = ₹99,000 |
| 18 | **−0.4%** (Bengaluru cash, 5-yr) | Bengaluru, 5-yr, cash, NPV incl-infra | Sole negative cell of 48; survives road-tax correction |
| 19 | **3.6×** (LFP study disagreement) | Published LFP cycling studies at 40°C | Naumann √t 13.3 yr ÷ Lewerenz linear 3.7 yr = 3.6 |
| 20 | **₹3.50 L** (interest on ₹14 L) | 10% rate, 60 months, no down payment | ₹27,039/month × 60 − ₹12,72,600 = ₹3,49,740 ≈ ₹3.50 L |

## The 5 market/policy (slides 3, 10-11)

| # | Number | Basis | Re-derive in one line |
|---|---|---|---|
| 21 | **3,995 mm** (length) | Design spec, 5 mm under 4,000 mm tax line | Packaging/parking; GST 5% is powertrain-based |
| 22 | **31-Mar-2030** (policy expiry) | Delhi EV Policy 2026 + Maharashtra EV Policy 2025 | 5 years before 2035 target year |
| 23 | **₹11,900 cr** (PM E-DRIVE) | Central scheme, enhanced Aug 2026 | No e-4W category; covers 2W, 3W, buses, trucks, charging |
| 24 | **40 GWh** (Reliance Phase 1) | Jamnagar LFP, H2 2026 (commissioning) | Full site revised to 120 GWh (was 100) |
| 25 | **52,718–67,657** (charging points) | India, Jul–Aug 2026 | 1 crore+ registered EVs; ~190–235 EVs per port |

---

## Quick-reference: which basis for which number

| Number | Nominal | NPV | Excl-infra | Incl-infra | Financed | Cash | City | Horizon |
|---|---|---|---|---|---|---|---|---|
| ₹5.75/km EV | ✓ | | ✓ | | ✓ | | Delhi | 5-yr |
| ₹6.73/km CNG | ✓ | | ✓ | | ✓ | | Delhi | 5-yr |
| +14.5% | ✓ | | ✓ | | ✓ | | Delhi | 5-yr |
| +6.7% | | ✓ | | ✓ | ✓ | | Delhi | 5-yr |
| +14.6% | | ✓ | | ✓ | ✓ | | Delhi | 8-yr |
| ₹14,200 | ✓ | | ✓ | | | (yr6+) | Delhi | monthly |
| ₹20,021 | ✓ | | ✓ | | ✓ | | Delhi | during loan |
| 21.9 h | ✓ | | ✓ | | ✓ | | Delhi | 5-yr |
| ₹99,000 | ✓ | | | ✓ | | | Delhi | 5-yr life |
| 268 km | ✓ | | | | | | All | design |
| 71.9% SoH | ✓ | | | | | | All | 8-yr |

---

## The one sentence that defends everything

> "The EV wins on every basis we tested — nominal, NPV, with or without the charger, financed or cash, in all three cities — and the only negative cell out of 48 is Bengaluru 5-yr cash at −0.4%, which disappears on the NPV basis. The charger costs ₹99,000 per vehicle and narrows the advantage by 8.1 pp (5-yr) or 10.7 pp (8-yr), but never reverses it."