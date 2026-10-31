# Implementation Roadmap
### MACH1 / FleetLine E1 — scaling a fleet EV across India
### Phasing, localisation and supply chain, infrastructure dependencies, partnerships

---

## 0. The constraint that shapes this roadmap

The vehicle is not the hard part. Two things around it are, and both are measurable today:

**1. No central scheme pays for an electric passenger car.** PM E-DRIVE (₹11,900 crore, extended
to 31 March 2028) incentivises e-2W, e-3W, e-ambulances, e-trucks, e-buses, public charging and
testing-agency upgradation. **e-4W passenger cars are not an eligible category.** There is no
demand subsidy to build a business case around, and there is no near-term prospect of one — the
e-3W (L5) component was *closed* on 26 December 2025 because penetration hit 41%, and the
ministry's stated policy is that subsidies taper and stop as penetration rises. Any roadmap
that assumes a central purchase incentive for our vehicle is assuming something that does not exist.

**2. India's cell manufacturing is not yet a supply chain — it is an ambition.**
The ACC PLI scheme (₹18,100 crore, 50 GWh target) has awarded 40 GWh across four firms. **As of
October 2025, 1.4 GWh had been commissioned — 2.8% of target, all from one company.** MHI's own
stated reasons for the delay: unavailability of technology, skilled manpower gap, import of critical
equipment, non-availability of upstream components. MHI also states that domestic demand
"continues to be met largely through imports," and that domestic value addition remains **below
the 60% threshold** because cathode and anode active materials, separators, electrolytes and foils
are still largely imported. S&P Global Mobility projects only **13% of cell demand domestically
sourced by 2030**.

We chose LFP. That choice is defensible on physics — our own battery report rests on it — but it
has a supply consequence: **Ola Cell, the only Indian cell maker actually producing at scale, is
NMC-first.** LFP is Reliance's chemistry — 40 GWh planned at Jamnagar, commissioning through
2026, with a stated roadmap to 120 GWh, and Anant Ambani describing it in June 2026 as on track to
make Reliance "one of the world's largest manufacturers of lithium iron phosphate batteries."
That is the single most important fact in this document.

**Therefore the roadmap is not "build, then scale." It is "de-risk the cell and the charger while
the fleet proves the duty."** Every phase below is gated on evidence, not on calendar.

---

## 1. Phase 1 — Prove the cell and the duty (2026–27)

**Objective.** Establish that an LFP pack can be sourced reliably at fleet-grade cost, and that a
depot-charged fleet actually returns the cost advantage our TCO claims — *on infrastructure
included*, which is the basis Rev 4 of the TCO uses.

| | |
|---|---|
| **Geography** | Delhi NCR only, margin segment (airport transfers + corporate commute) |
| **Fleet size** | 1,000–2,000 vehicles, indicative and gate-conditional — **not a forecast** |
| **Charging** | One 7.4 kW Type 2 AC port per vehicle, 10% N+1 spare-port redundancy |
| **Cells** | Dual-sourced: Reliance Jamnagar LFP as primary, qualified import as bridge |
| **Energy** | Delhi BEE-notified EV tariff ₹4.50/kWh, contracted as a premise not a hope |

**Why Delhi first, and only the margin segment.** Delhi is the only city where the TCO clears at a
five-year horizon once the charger is counted — breakeven duty 163.7 km/day against our 200, a
1.22× margin, and ₹1,11,972 of headroom before charger capex erases the advantage. Mumbai does not
clear: its breakeven duty with infrastructure is **201.4 km/day, above the 200 km/day our own deck
assumes**, and its solved breakeven charger cost is ₹96,171 against a ₹99,000 real budget. We are
not launching in Mumbai to find out. Bengaluru needs 195.8 km/day — a 1.02× margin, which is a pass
on arithmetic, not a comfortable one.

**Three gates, not three dates.** Phase 2 does not begin because a quarter ended.

| Gate | Test | Threshold |
|---|---|---|
| **G1 — Cell** | Two qualified LFP cell sources at volume; delivered cost at or below the imported benchmark | Both sources contracted; price parity within 10% |
| **G2 — Duty** | Measured paid km/day across the fleet against the TCO model's assumption | ≥ 200 km/day sustained, or the model is re-run at the measured duty |
| **G3 — Battery** | Twelve months of per-cell State-of-Health telemetry from the fleet | Empirical fade curve published, replacing the contested calendar exponent |

**G3 is the one people will underrate.** Our battery report found published LFP studies disagreeing
**3.6×** on time-to-80% — Naumann's √t law gives 13.3 years at 40 °C, Lewerenz's measured linear law
gives 3.7 years. That disagreement is why the pack carries per-cell SoH telemetry as a specified
rather than optional feature. Twelve months of our own fleet data is the cheapest available way to
close it, and it converts the largest unresolved scientific risk in the proposal into a number we
own.

---

## 2. Phase 2 — Industrialise the pack, expand carefully (2028–30)

Only after G1–G3 clear.

| | |
|---|---|
| **Geography** | Delhi (scaled) + Bengaluru, **Mumbai only if measured duty exceeds 205 km/day** |
| **Cumulative fleet** | 15,000–25,000 vehicles, gate-conditional |
| **Localisation** | In-house pack assembly, BMS and thermal management; **cells imported or Reliance-sourced** |
| **Charging** | Type 2 AC primary; CCS2 DC introduced as backup and intercity top-up |

**The honest localisation ceiling for this phase is pack assembly.** India's automotive-grade cell
supply does not exist at the volume or the qualification level this vehicle needs. Claiming
domestic cells here would be a claim the MHI's own progress figures contradict.

**Plant siting — Karnataka.** The Clean Mobility Policy 2025–2030 offers large, mega and ultra-mega
enterprises a **20–25% capital investment subsidy in five annual instalments**, 100% stamp-duty and
land-conversion-fee reimbursement, up to ₹7–10 crore for anchor industries, and 50% subsidy on
effluent treatment plants up to ₹2.5 crore. Three ready clusters exist with plug-and-play
infrastructure: **Gauribidanur (825 acres), Harohalli (700 acres)**, both within 70 km and 40 km of
Bengaluru, and Chikkamalligewada in Dharwad (1,000 acres). Karnataka also runs an advanced-chemistry
battery anchor incentive reimbursing 30% of eligible R&D expenditure up to ₹1 crore.

Alternatives: Tamil Nadu's EV Special Manufacturing Package (SGST reimbursement, turnover-based
subsidy, dedicated ACC capital subsidy, interest subvention up to 5% for six years) with Ola's
Krishnagiri ecosystem nearby; Maharashtra, where supply-side support is weaker and sits in the
Industrial Policy 2019 and Thrust Sector Policy 2024 rather than the EV policy itself. Gujarat
offers capital subsidies but, distinctively among the large states, **no stamp-duty exemption and no
SGST reimbursement**.

---

## 3. Phase 3 — Pan-India, and cells only if the evidence is there (2031–35)

| | |
|---|---|
| **Geography** | Pune, Hyderabad, Ahmedabad, Jaipur, Indore, Lucknow, Kochi, Coimbatore |
| **Cumulative fleet** | 100,000+ vehicles, gate-conditional |
| **Cells** | Domestic **only if** operating Indian LFP capacity exceeds 20 GWh with automotive qualification |

That last condition is deliberately written as a measurement, not a hope. If Reliance's 40 GWh
ramp delivers and Ola adds LFP alongside its NMC base, the condition is met. If it is not met by
2031, Phase 3 scales on imported cells and the localisation claim stays honest.

**What we will never claim:** a fully localised battery supply chain by 2035. The ACC PLI mandates
domestic value addition of 25% within two years and 60% within five, and MHI states plainly that
value addition remains below the 60% threshold because cathode and anode active materials,
separators, electrolytes and foils are still largely imported. China refines roughly 74% of global
lithium and controls about 98% of LFP cathode active material. An honest roadmap says India will
integrate packs domestically and progressively localise cell content — not that it will own the
material base.

---

## 4. Localisation ladder

| Level | What is Indian | When | Honest label |
|---|---|---|---|
| **L1** | Pack assembly, BMS, thermal management, vehicle integration | 2026–27 | Pack integration |
| **L2** | Domestic LFP cells for a share of volume; imported for the balance | 2028–30 | Partial cell localisation |
| **L3** | Domestic cells + CAM/AAM/separator content | 2031+ **if gated** | Progressive value addition |

Anyone claiming L3 on a fixed date has not read MHI's DVA figures.

---

## 5. Infrastructure dependencies

### Per-vehicle requirement

| Item | Specification | Basis |
|---|---|---|
| AC port | 7.4 kW, Type 2 | AIS-138 Part 1; IS 17017-1/-2 |
| DC backup | CCS2 | AIS-138 Part 2 **as amended in 2022, CCS2 is mandated for four-wheelers**; Bharat DC001 is retained for 2W/3W only |
| Overnight window | 25.68 kWh ÷ (7.4 kW × 0.90 charge efficiency) = **3.86 hours** | 200 km/day at 12.84 kWh/100 km |
| Redundancy | 1 spare port per 10 vehicles | N+1 |
| Backend | OCPP 1.6J minimum, 2.0.1 preferred | MoP/CeA guidelines |

**One AC port per vehicle is sufficient and no DC fast-charging is required for the duty.** That is
a cost result worth stating plainly: the DC question that dominates public infrastructure
discussion does not arise in a return-to-base overnight fleet model.

### The dependency we cannot control, and must contract around

**Charging interoperability in India is measurably broken.** A June 2026 industry assessment found
**25–40% session failure rates** across 60+ vehicle models, 25+ hardware OEMs and 50+ CPOs
generating 300,000+ protocol combinations — degrading real capacity and amplifying perceived
shortages by roughly 35%. Current deployment is one public charging station per 11 four-wheelers.

This is not background colour. It attacks the uptime term in our TCO directly, and our TCO
already shows the EV tolerating only **21.9 hours per month** of downtime beyond its 3.5-hour
baseline before the CNG comparator wins. Against Green SM's documented 75 hours per month lost to
charger queues, a 25–40% failure rate is not a rounding error.

**Mitigation is contractual, not technical:** chargers procured to AIS-138 certification with
OCPP conformance tested per port, a guaranteed-response maintenance SLA, spare-port redundancy at
N+1, and depot backup generation sized for the overnight window.

### Do not plan on government chargers

PM E-DRIVE allocated ₹2,000 crore for public EV charging. As of 28 September 2026, ₹851 crore had
been approved for 8,147 chargers across three oil marketing companies and ten states. But MHI's own
March 2026 statement is that **"no charging stations have been installed under the scheme so far."**
Separately, the 2024 MoP guidelines provide government funding for only 60% of public chargers, with
the balance on CPOs and OEMs. The 2024 Cabinet plan envisages ~72,300 fast chargers including 22,100
for electric cars.

Our business case requires **owned depot infrastructure**, which is consistent with that. It is also
the reason the charger sits inside the TCO boundary in Rev 4 rather than outside it.

---

## 6. Policy levers available — and one that constrains us

### Delhi — the one that works, and the one that bites

The Delhi Electric Vehicles Policy 2026 (Council approval 29 June 2026, notified 30 June, effective
1 July 2026, to 31 March 2030) gives our vehicle:

- **100% road tax and registration-fee exemption for the life of the vehicle**, for electric cars at
  ex-showroom ≤ ₹30 lakh. Worth **₹1,27,260** on our vehicle and already inside the Rev 4 TCO.
- **No purchase incentive for electric cars.** The notified policy is explicit: incentives cover
  e-2W (₹10,000/kWh capped ₹30,000 in year one, tapering over three years), e-3W autorickshaws, and
  N1 e-trucks. Electric cars are excluded from the purchase-incentive schedule.
  *(Note: the CEEW state-policy matrix still shows a legacy ₹10,000/kWh Delhi e-4W figure. That is
  the superseded 2021 policy. Verify against the notified instrument — the same trap that produced
  the road-tax error in TCO Revision 3.)*
- **₹1,00,000 scrapping incentive** for purchasing a new electric car on scrapping a Delhi-registered
  BS-IV or below car, ex-showroom ≤ ₹30 lakh, limited to the first 1,00,000 applicants, claimed
  within six months of the Certificate of Deposit, vehicle must be Delhi-registered. **This is worth
  verifying specifically for CNG-fleet replacement**, where the scrapped vehicle is a BS-IV
  derivative. At ₹1 lakh per unit it is material at fleet scale. We have not verified eligibility
  for CNG-registered vehicles, and we are not claiming it.
- **A three-year NoC lock — and this one matters more than it looks.** Clause 4.1.4: any vehicle
  availing a purchase incentive cannot obtain a No Objection Certificate for transfer or
  re-registration in another State or UT for **three years** from notification.

For a private buyer that is a reasonable anti-arbitrage rule. **For a fleet operator it is a
constraint on the business model**, because redeploying assets between cities is how a multi-city
fleet captures utilisation. This is a concrete reason to treat Phase 1 as Delhi-dedicated rather
than as a Delhi launch pad for a pan-India fleet, and it is worth raising with Delhi as an
exemption for registered fleet operators. It also argues for registering Phase 2 vehicles in the
city where they will be operated rather than buying centrally in Delhi.

### Other states

State e-4W purchase incentives have historically run from 5% to 30% of cost in Odisha, Tamil Nadu,
Kerala, Goa, Chhattisgarh, Rajasthan and others. **None is claimed here** — validity periods,
vehicle caps and current notification status differ and must be verified per state at the point of
purchase, not assumed from a matrix. Karnataka's policy is notable for having **no consumer
purchase incentive at all**, which is why Bengaluru's advantage in our TCO is electricity tariff
and road tax, not subsidy.

### Charging-side support

Delhi policy nominates **Delhi Transco Limited as the nodal agency** for charging and swapping
infrastructure, mandates a **single-window clearance** for charge-point operators, and directs
DISCOMs through DERC to explore **time-of-day tariffs and differential pricing** to reduce EV
charging cost. The BEE-notified ₹4.50/kWh EV tariff category is the input our entire energy line
depends on; if it were withdrawn the case inverts above roughly ₹11/kWh. OEMS operating in Delhi
also carry an obligation to deploy at least one public charging station per dealer.

---

## 7. Partnerships

| Partner type | Who | What we need | What they get |
|---|---|---|---|
| **Fleet operators** | Ola, Uber, Evera, GMR Hyderabad, Bharat Taxi, Refex, Everest, Lithium Urban | Anchor volume in the **margin segment** — airport and corporate commute, not street-hail volume | A vehicle specified for pre-booked, higher-utilisation duty with a published per-km cost they can audit |
| **Cell** | **Reliance New Energy** (LFP, Jamnagar 40 GWh) primary; qualified import as bridge; Ola Cell secondary | Automotive-grade LFP at volume, with price parity to import inside the window | Anchor offtake for a first Indian LFP automotive programme |
| **Charging** | AIS-138-certified AC/CCS2 suppliers; CPOs (ChargeZone, PluggedIn, Ather Grid) for public backup | Certified Type 2 + CCS2, OCPP conformance tested, maintenance SLA | Depot density and a fleet-grade load profile |
| **Power** | Delhi DISCOMs, DERC, DTL | LT EV tariff category retained; ToD structure; demand-charge treatment for >50 kW connections | Managed load profile and depot demand forecasting |
| **State** | Karnataka (Karnataka Clean Mobility Policy 2025–2030), TN, Maharashtra | Capital subsidy, land, cluster infrastructure | Employment, EV manufacturing depth, ecosystem |
| **Certification** | ARAI / testing agencies, BIS | Homologation, AIS-138 conformance, PMP certificates | Test volume and Indian test capability |
| **End-of-life** | Recycler / EPR partner | Take-back at end of first life | A guaranteed feedstock of retired packs |

**On fleet operators, be precise about who we are targeting.** Under flat-fee platform economics —
Ola ₹67 per vehicle per day, Uber and Rapido ₹29 — platform revenue per vehicle is fixed in the fare
and largely independent of trip count, so **utilisation, not fare, decides fleet economics.** Volume
sits in street-hail intra-city (~58% of rides, price sensitivity 0.85, ~10% EV adoption). Margin
sits in airport and premium (~19% combined, 144–210 paid km/day, price sensitivity 0.30–0.35, 18%
EV adoption). We specified for the margin segment and we say so. An operator running airport and
corporate-commute duty is the counterparty whose economics actually improve.

**Airport concession fees are not operator margin.** At IGI, ₹245 plus 18% GST is roughly 40% of
the rider fare, remitted to the airport authority — so the margin in airport duty is thinner than
the segment headline implies. This is a reason to include corporate commute alongside airport
transfers in Phase 1 rather than airport alone.

---

## 8. Risks in this roadmap, in order of size

| Risk | Exposure | Mitigation |
|---|---|---|
| **Domestic LFP cell supply does not materialise** | ACC PLI at 2.8% delivered; Reliance ramping but unproven at automotive volume | Dual-sourced from day one; import bridge is the plan, not the exception; Phase 3 gated on measured capacity >20 GWh |
| **Charger session failure eats the uptime allowance** | 25–40% failure rate vs only 21.9 h/month of real slack | AIS-138 certification, per-port OCPP conformance testing, N+1 redundancy, maintenance SLA, depot backup power |
| **Duty comes in below 200 km/day** | Breakeven is 163.7 km/day in Delhi; Mumbai needs 201.4 | Phase 2 cities gated on measured Phase 1 duty, not on a business plan |
| **Delhi EV tariff category withdrawn** | Inverts the case above ~₹11/kWh | Contractual tariff assumption; G2 re-run at actual tariff |
| **Pack replacement inside the horizon** | ₹4 L reverses the 5-year case to −4.5% | Capacity-retention guarantee or pack-to-pack service — the warranty structure carries this, not the chemistry |
| **No purchase incentive ever arrives for e-4W** | Removes a 12–37% cost lever we have not counted | We have built the case **without** one; treat any future incentive as upside, never as basis |
| **Three-year NoC lock constrains redeployment** | Limits multi-city fleet optimisation | Delhi-dedicated Phase 1; register in the city of operation; seek a fleet-operator exemption |
| **Battery fade resolves at Lewerenz, not Naumann** | 3.7 years vs 13.3 to 80% at 40 °C | Twelve months of our own per-cell telemetry in Phase 1; sizing already absorbs it; the warranty carries the residual risk |

---

## 9. What this roadmap will not claim

- **Not** that PM E-DRIVE subsidises our vehicle. It does not, and no e-4W category exists.
- **Not** that the battery supply chain is localised. 1.4 GWh of 50 GWh is commissioned.
- **Not** that domestic cells arrive on a schedule. Phase 3 is gated on a measurement, not a date.
- **Not** that government charging infrastructure will be available. None has been installed under
  PM E-DRIVE to date.
- **Not** that Delhi offers a purchase incentive for electric cars. The notified 2026 policy
  excludes them; road tax and registration exemption plus a scrapping incentive are what exist.
- **Not** that Mumbai clears at five years. On our own numbers with the charger counted, it does not.
- **Not** that the e-4W market is 16–28% cheaper. That figure predated infrastructure. It is +6.7%
  over five years and +14.6% over eight, on NPV at a 12% hurdle, with the charger included.

---

## 10. Sources

**Cell manufacturing and PLI**
1. PIB, Ministry of Heavy Industries, *National Programme on Advanced Chemistry Cell (ACC) Battery Storage* (Feb 2026) — 40 GWh awarded across four firms, ₹3,237 cr invested, 1,118 direct jobs
2. PIB / Lok Sabha unstarred question AU1521 — PLI ACC domestic value addition below the 60% threshold; CAM, AAM, separators, electrolytes and foils largely imported
3. IEEFA, *Assessing India's ACC PLI Scheme* (Feb 2026) — 1.4 GWh of 50 GWh commissioned (2.8%) as of Oct 2025; beneficiary comparison
4. IEEFA, *Securing India's Battery Supply Chain* (May 2026) — ~66 GWh non-PLI announced, much of it pack assembly; China refines 74% of lithium, controls 98% of LFP cathode active material
5. Business Standard (12 Aug 2026) — Ola Cell Technologies revised timelines; full five-year PLI window to CY2031, up to ₹7,240 cr; 2.5 GWh installed, 3.5 GWh under installation, 6 GWh targeted
6. Financial Express (29 May 2026) — Reliance Jamnagar 40 GWh LFP, up from 30 GWh target, roadmap to 100–120 GWh; production ramping through H2 2026
7. Business Today / Reliance AGM (19 Jun 2026) — Anant Ambani: first phase of 40 GWh on track for 2026; equipment delivered
8. IISD, *Unlocking Supply Chains for Localizing EV Battery Production in India* (Nov 2024) — S&P Global Mobility: 13% domestic cell sourcing by 2030; company-by-company chemistry map
9. MoEFCC — battery recycling obligations

**Demand incentives**
10. PIB (28 Jul 2026) — PM E-DRIVE ₹10,900 cr; category-by-category incentive schedule; e-3W L5 closed 26 Dec 2025; ₹2,000 cr for EV PCS
11. PIB factsheet (1 Oct 2026) — outlay raised to ₹11,900 cr; extension to 31 Mar 2028; ₹851 cr approved for 8,147 chargers as of 28 Sep 2026
12. PM E-DRIVE portal, Ministry of Heavy Industries — category schedule, terminal dates, fund allocation table
13. PIB (24 Mar 2026) — year-wise utilisation; "no charging stations have been installed under the scheme so far"
14. Economic Times / Business Standard (11 Aug 2026) — e-2W incentive cut to ₹2,500/kWh; e-3W closed at 41% penetration; ₹1,000 cr additional
15. EV penetration 0.7% FY2019-20 → 8.2% FY2025-26

**Charging standards and reality**
16. BIS / e-Amrit, IS 17017 and AIS-138 — AC and DC EVSE standards; Part 25 low-power DC; Part 24 communications
17. EVPulse (11 Jun 2026) — AIS-138 Part 2 amended 2022 to mandate CCS2 for four-wheelers; Bharat DC001 retained for 2W/3W; OCPP 1.6J vs 2.0.1; five connector types in active deployment
18. P3 Group (18 Jun 2026) — 25–40% session failure rate; 300,000+ combinations; one public station per 11 four-wheelers
19. MoP Guidelines for Installation and Operation of EV Charging Infrastructure 2024 — siting norms, 60% government funding share
20. Cabinet 2024 plan — ~72,300 fast chargers including 22,100 for e-cars
21. DERC — EV charging infrastructure regulation and PM E-DRIVE subsidy utilisation

**State policy**
22. Delhi Electric Vehicles Policy 2026, notified 30 Jun 2026 (SG.DEL-E.30062026-273960) — clause 4.1.4 three-year NoC lock; clause 4.6.3 ₹1 lakh e-car scrapping incentive; clause 4.7 road tax; clause 5 DTL as nodal agency; clause 6.2 OEM charging obligation
23. JSA Prism, *Delhi notifies the Delhi Electric Vehicles Policy 2026* (Aug 2026) — draft-to-notified changes
24. Karnataka Clean Mobility Policy 2025–2030 — 20–25% capital subsidy, cluster locations, anchor and ETP incentives
25. Invest Karnataka — EV policy schedule: 15% fixed assets, 1% turnover for 5 years, 100% stamp duty, ETP subsidy
26. Tamil Nadu Electric Vehicles Policy 2023–2028 — EV Special Manufacturing Package, SGST reimbursement, ACC capital subsidy, 5% interest subvention
27. Maharashtra Electric Vehicle Policy 2025–2030 and Industrial Policy 2019 / Thrust Sector Policy 2024
28. Gujarat Industrial Policy 2020 and State EV Policy 2021 — capital subsidy without stamp duty or SGST reimbursement
29. IISD, *States in the Driver's Seat: Policies localizing EV and battery manufacturing in India* (Apr 2026) — 14 states with capex/opex-reducing support; policy thinness at midstream and upstream
30. CEEW State Policy Matrix — state e-4W purchase incentives; legacy Delhi figure superseded

**Market context**
31. Redseer via Times of India (23 Jun 2025) — driver trip and fare economics; flat-fee comparison
32. IGI / BIAL concession rates — airport fee as a share of rider fare

---

*Every volume, cost and policy figure in this roadmap is either sourced above or gated on a
measurement defined in §1. Volumes are indicative planning figures, not forecasts. Where a figure
could not be verified against a primary instrument, it is marked for verification rather than used.*
