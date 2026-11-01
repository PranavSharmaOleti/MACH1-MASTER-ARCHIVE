# MACH1 / FleetLine E1 — Evidence Binder Index

**Purpose:** For every headline number in the deck, one-line definition, formula, inputs with sources, and file/page where proof lives. Use this to defend any figure in Q&A.

---

## 1. ₹5.75 / ₹6.73 per km (Delhi, 5-yr, financed, nominal, excl-infra)

- **Definition:** Cost per km for EV vs CNG over 5 years at 200 km/day, Delhi, financed, nominal rupees, excluding charging infrastructure.
- **Formula:** `TCO_total / total_km` where TCO = CAPEX (EMI×60) + Energy + Maintenance + Insurance − Residual
- **Inputs:** EV on-road ₹12,72,600 (ex ₹12.12L × 5% GST, 0% road tax); CNG on-road ₹8,51,488 (ex ₹6.56L × 18% GST, 10% road tax); Energy EV ₹0.64/km (12.84 kWh/100km × ₹4.50/kWh ÷ 0.90 ceff); CNG ₹3.04/km (₹76/kg ÷ 25 km/kg); Maintenance EV ₹1,200/yr, CNG ₹3,500/yr; Insurance EV ₹3,500/mo, CNG ₹3,290/mo; Residual EV 26%, CNG 40%
- **Proof:** `tco_engine/tco_engine.py` lines 25-54 (tco function); `tco_analysis.py` section A; run: `python3 tco_analysis.py` → section A output
- **Basis:** Nominal, excl-infra, financed, Delhi, 5-yr

## 2. +6.7% / +14.6% (NPV, incl-infra, 5-yr / 8-yr)

- **Definition:** EV advantage as NPV at 12% hurdle, escalated, financed, including ₹99,000 depot charger, Delhi.
- **Formula:** `(CNG_NPV − EV_NPV) / CNG_NPV × 100` where NPV = discounted monthly cash flows (EMI, energy, maint, ins, infra, residual) at 12%/12 per month, with escalation (elec 4.5%, CNG 3.5%, maint 4.0%, ins 5.0%, residual 4.5%)
- **Inputs:** Same as #1 plus charger capex ₹99,000/vehicle (₹50K HW + ₹30K install + ₹10K DISCOM × 1.10 N+1), opex ₹15,000/yr, 5-yr life; CNG hydro-test ₹4,500/3yr
- **Proof:** `tco_analysis.py` sections G, H, L (line 360-451); run: `python3 tco_analysis.py` → section L output; bottom-right cell
- **Basis:** NPV (12%), escalated, financed, incl-infra, Delhi, 5-yr/8-yr

## 3. ₹14,200 (driver advantage per month)

- **Definition:** Monthly take-home difference between EV and CNG for a driver at 200 km/day, ₹11/km fare, Delhi, year 6+ (no EMI).
- **Formula:** `(Net fare − EV opex) − (Net fare − CNG opex)` = CNG opex − EV opex = (15,808+3,500+3,290) − (3,338+1,560+3,500) = ₹14,200
- **Inputs:** Net fare ₹10.665/km × 5,200 km = ₹55,458/mo; EV opex = energy ₹3,338 + maint ₹1,560 + ins ₹3,500 = ₹8,398; CNG opex = energy ₹15,808 + maint ₹3,500 + ins ₹3,290 = ₹22,598
- **Proof:** `tco_analysis.py` section A (line 6-15) and section J (line 270-299); run: `python3 tco_analysis.py` → section A
- **Basis:** Nominal, excl-infra, Delhi, year 6+ (no EMI), flat-fee platform model

## 4. 268 km (range at 15% reserve)

- **Definition:** One-way range at 15% design reserve on 45 kWh pack at 12.84 kWh/100km.
- **Formula:** `45 kWh × 0.90 (usable) ÷ 12.84 kWh/100km × (1 − 0.15 reserve) = 268 km`
- **Inputs:** 45 kWh nameplate, 90% usable fraction, 12.84 kWh/100km consumption, 15% reserve target
- **Proof:** `tco_analysis.py` section N (line 640-693); run: `python3 tco_analysis.py` → section N1/N2
- **Basis:** Single convention: 45 kWh, 12.84 kWh/100km, 10% battery reserve, 15% design reserve

## 5. 21.9 h (additional downtime beyond baseline)

- **Definition:** Extra downtime hours per month the EV can absorb before CNG becomes cheaper, beyond the 3.5 h/month base case.
- **Formula:** Break-even at ~25.4 h/month total downtime (at ₹200.46/h net cost) − 3.5 h base = 21.9 h
- **Inputs:** Base downtime 3.5 h/mo (0.5 queue + 1.0 planned + 1.5 repair + 0.5 charger failure); net cost per lost hour ₹200.46 (20 km/h × ₹11/km gross − platform fee − energy avoided); OPP_H ₹200.46/h
- **Proof:** `tco_analysis.py` section I (line 230-269); run: `python3 tco_analysis.py` → section I
- **Basis:** Delhi, 5-yr, financed, at net cost per hour (not OPP_H)

## 6. 3.6× (LFP studies disagreement on time-to-80%)

- **Definition:** Ratio between Naumann √t (13.3 yr to 80% at 40°C) and Lewerenz linear (3.7 yr to 80% at 40°C) capacity fade models.
- **Formula:** 13.3 ÷ 3.7 = 3.6
- **Inputs:** Naumann √t model: 3.7 years to 80% at 40°C; Lewerenz linear model: 13.3 years to 80% at 40°C (published LFP studies)
- **Proof:** Deck slide 10 (G3 gate); `tco_analysis.py` section K (line 331-359); battery_model/mach1_model.py
- **Basis:** Published LFP cycling studies at 40°C; 48°C design point gives 71.9% SoH at year 8

## 7. ₹99,000 (charger per vehicle)

- **Definition:** Depot charging infrastructure cost per vehicle (hardware + install + DISCOM + N+1 spare).
- **Formula:** (₹50,000 HW + ₹30,000 install + ₹10,000 DISCOM) × 1.10 (N+1: 1 spare per 10 vehicles) = ₹99,000
- **Inputs:** 7.4 kW AC port hardware ₹50,000; civil+cabling ₹30,000; DISCOM sanction ₹10,000; N+1 factor 1.10
- **Proof:** `tco_analysis.py` section G (line 104-125); run: `python3 tco_analysis.py` → section G
- **Basis:** Per vehicle, Delhi, 5-yr life, replaced every 5 years

## 8. 45 kWh (pack nameplate)

- **Definition:** Battery pack nominal capacity for FleetLine E1.
- **Formula:** Pack-sizing rule: E_day / (SoH × 0.90 reserve × 0.90 ceff) = 25.68 / (0.719 × 0.90 × 0.90) = 44.1 kWh → converged to 45 kWh
- **Inputs:** 200 km/day × 12.84 kWh/100km = 25.68 kWh/day battery-side; 71.9% SoH at 48°C; 90% usable reserve; 90% charge efficiency
- **Proof:** `tco_analysis.py` section K (line 331-359); battery_model/mach1_model.py; deck slide 5 (param table)
- **Basis:** 48°C design point, 200 km/day duty, 10% battery reserve

## 9. 3,995 mm (length)

- **Definition:** Overall vehicle length, 5 mm under the 4,000 mm small-car tax threshold.
- **Formula:** N/A (design specification)
- **Inputs:** Sub-4m for parking/maneuverability/packaging; GST 5% is powertrain-based (BEV), not length-based
- **Proof:** Deck slide 4 (param table); specs report; `MACH1_POWERTRAIN_SPECS_REPORT.pdf`
- **Basis:** Design specification; tax threshold is 4,000 mm for petrol/CNG (18% vs 40% GST)

## 10. Policy expiry: 31-Mar-2030

- **Definition:** Expiry date for Delhi EV Policy 2026 road-tax exemption and Maharashtra EV Policy 2025.
- **Formula:** N/A (policy date)
- **Inputs:** Delhi: 100% road tax + registration exemption for EVs ≤₹30 L, effective 1 Jul 2026, expires 31 Mar 2030; Maharashtra: 15% ex-factory, ₹2 L cap, 25,000 units, to 31 Mar 2030
- **Proof:** Delhi EV Policy 2026 (draft, notified Jun 2026); Maharashtra EV Policy GR MVR-0125/C.R.13/Tra-2 (23 May 2025); deck slide 10
- **Basis:** State policy notification; 5 years before 2035 target year

---

## Additional headline numbers (supporting)

| # | Number | Definition | Formula | Proof |
|---|---|---|---|---|
| 11 | ₹6.31/km (EV) | EV cost per km, Delhi 5-yr financed, nominal excl-infra | TCO/km | tco_engine.py line 65 |
| 12 | ₹6.75/km (CNG) | CNG cost per km, same basis | TCO/km | tco_engine.py line 65 |
| 13 | ₹6.47/km (Mumbai EV) | Mumbai 5-yr financed nominal | TCO/km | tco_analysis.py section F |
| 14 | ₹7.30/km (Mumbai CNG) | Mumbai 5-yr financed nominal (corrected from 7.00) | TCO/km | tco_analysis.py section F |
| 15 | ₹6.66/km (Bengaluru EV) | Bengaluru 5-yr financed nominal | TCO/km | tco_analysis.py section F |
| 16 | ₹7.25/km (Bengaluru CNG) | Bengaluru 5-yr financed nominal | TCO/km | tco_analysis.py section F |
| 17 | ₹20,021 (EV during loan) | Driver take-home during 60-month loan, year 1-5 | Net fare − EMI − opex | tco_analysis.py section J |
| 18 | ₹14,768 (CNG during loan) | Same for CNG | Net fare − EMI − opex | tco_analysis.py section J |
| 19 | ₹5,252 (advantage during loan) | Monthly advantage during loan period | 20,021 − 14,768 | tco_analysis.py section J |
| 20 | ₹37,362 (legacy 20% EV) | Take-home under 20% per-ride commission, yr6+ | Net fare (8.80×5200) − opex | tco_analysis.py fixed section |
| 21 | ₹34,502 (legacy 25% EV) | Take-home under 25% per-ride commission, yr6+ | Net fare (8.25×5200) − opex | tco_analysis.py fixed section |
| 22 | ₹0.64/km (EV energy at ₹4.50) | Energy cost per km at Delhi tariff | 12.84/100 × 4.50 ÷ 0.90 | tco_engine.py line 34 |
| 23 | ₹1.21/km (EV energy at ₹8.50) | Energy cost at Bengaluru tariff | 12.84/100 × 8.50 ÷ 0.90 | tco_engine.py line 34 |
| 24 | ₹1.71/km (EV energy at ₹12.00) | Energy cost at public DC rate | 12.84/100 × 12.00 ÷ 0.90 | tco_engine.py line 34 |
| 25 | 48-cell matrix (0 negative excl-infra) | All 48 city×horizon×basis×capital cells positive without charger | M[(city,yrs,fin,i)] > 0 for i<2 | tco_analysis.py section M |
