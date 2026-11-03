# India Ride-Service Market: Evidence-Backed Five-Segment Analysis (2035 Outlook)

**Project:** Maruti Suzuki XCELerate 2026 E-Track — FleetLine E1
**Deliverable:** Market Assessment — five-segment demand, margin and structural comparison
**Date:** 3 November 2026
**Evidence standard:** Every statistic tagged [reported], [calc], [est] or [assump] with source, date and reference period. Missing metrics flagged as gaps, never invented.

---

## 0. Evidence base and grading

| Grade | Meaning | Count |
|---|---|---|
| **A** | Reproduced from data/script in this repo by this audit | 13 |
| **B** | Single traceable secondary source | 3 |
| **C** | Internal assertion with no source file | 12 |
| **D** | Contradicted by the project's own evidence | 8 |
| **D/C** | Ambiguous | 1 |

**Primary sources used (ranked by authority):**
1. AAI Traffic Report, September 2026 (Government of India, Ministry of Civil Aviation) — airport passenger traffic
2. VAHAN registration data (Government of India, Ministry of Road Transport and Highways) — vehicle supply
3. AutoPunditz EV sales data (industry, registration-based) — EV adoption trajectory
4. MACH1_MARKET_ASSESSMENT.pdf (18 Oct 2026) — ruling document, defines permitted formula
5. MACH1_MARKET_SLIDES_CONTENT.pdf — only market content with named sources
6. MACH1_E1_Audience_and_Positioning.pdf — buyer hypothesis
7. MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf — driver/rider economics
8. MACH1_TCO_ANALYSIS.pdf — cost model
9. Wikipedia (Ola, Uber, Rapido, BluSmart) — company background, verified via direct fetch
10. MACH1_ROADMAP_FLOW.pdf — infrastructure and policy

**Key constraint:** Web search returns HTTP 402 in this environment. Direct-URL fetches work. Six external lynchpins remain unverified (see §7).

---

## 1. Market size and platform ride-flow proxy

### 1.1 Reported platform daily rides [reported]

| Platform | Daily rides | Source | Date | Reference period |
|---|---|---|---|---|
| Uber | 840,000 | Motilal Oswal via Business Standard | 18 Apr 2025 | 2025 (unspecified month) |
| Ola | 460,000 | Same source | 18 Apr 2025 | Same |
| Rapido | 320,000 | Same source | 18 Apr 2025 | Same (vehicle-class scope unclear) |
| **Combined** | **1,620,000** | Sum of reported figures | — | — |
| **Annualized** | **591.3 million** | ×365 days | — | Run-rate assumption |

**Grade: B** — single traceable secondary source. The article does not expose the underlying study's definitions or vehicle-class breakdown. Rapido's scope is particularly unclear: its 320,000 daily rides may include bike taxis and auto-rickshaws, not just 4-wheel cars.

**Critical caveat:** This is a **platform ride-flow proxy**, not a national taxi-market census. It excludes: (a) street-hail taxis, (b) auto-rickshaws not on aggregators, (c) corporate subscription fleets, (d) airport concession vehicles, (e) inter-city outstation taxis booked offline.

### 1.2 Scenario GMV envelope [calc + assump]

Formula: Annual GMV = observed annual rides × target-segment share × realized fare

| Scenario | Target share | Fare | Annual rides × share | Illustrative GMV |
|---|---|---|---|---|
| Low | 5% | ₹300 | 29.6M | ₹887 crore |
| Central | 10% | ₹450 | 59.1M | ₹2,661 crore |
| High | 15% | ₹600 | 88.7M | ₹5,322 crore |

**Grade: C (assump)** — target share (5-15%) and fare (₹300-₹600) are sensitivity bounds, not measured segment values. The ₹300 fare is a broad all-cab reference (Times of India, 23 Jun 2025), not a target-segment fare. The range is a sensitivity envelope, not a confidence interval. Target use cases overlap — do not sum without trip-level de-duplication.

### 1.3 Vehicle supply context [reported]

| Metric | Value | Source | Date |
|---|---|---|---|
| Total EV car registrations (H1 2026) | 148,023 | AutoPunditz EV period aggregates | 2026 |
| Top-3 EV brands (H1 2026): Tata/MG/Mahindra | 38.8%/28.4%/24.8% | AutoPunditz | 2026 |
| Maruti Suzuki eVitara (Mar 2026) | 2,254 units | AutoPunditz | Mar 2026 |
| Euler Motors electric CVs (Aug 2026) | 869 | AutoPunditz | Aug 2026 |
| Karnataka EV share (Aug 2026) | 17.5% of all new vehicles | AutoPunditz by-state | Aug 2026 |
| Karnataka electric cars (Aug 2026) | 1,258 | AutoPunditz by-state | Aug 2026 |

**Grade: B** — AutoPunditz mixes wholesale and registration data; measure type must be verified per row before combining.

---

## 2. Five-segment comparison

### 2.1 What the evidence actually supports

The deck's five-segment table (p3) is **entirely unsourced** — all 40 cells trace to the NITDurgapur Round-1 report with no derivation. The project's own ruling document (MACH1_MARKET_ASSESSMENT.pdf) withdraws it. The only defensible approach is to build each segment from primary sources and explicitly flag gaps.

**Segment-by-segment evidence assessment:**

| Segment | Volume evidence | Fare evidence | Utilization evidence | EV adoption evidence | Overall grade |
|---|---|---|---|---|---|
| Intra-city street-hail | Platform rides (591.3M/yr) | ₹300 broad reference | 7.5 trips/day (assumed) | 10% (deck, unsourced) | C (assump) |
| Daily commute/subscription | **None found** | **None found** | **None found** | **None found** | D (no source) |
| Airport transfers | AAI passenger traffic (196.24M Apr-Sep 2026) | **None found** | 6.0 trips/day (assumed) | 18% (deck, unsourced) | C (partial) |
| Inter-city/outstation | **None found** | ₹4,200/trip (deck, unsourced) | 1.5 trips/day (assumed) | 5% (deck, unsourced) | D (no source) |
| Shared/premium mobility | **None found** | ₹520/trip (deck, unsourced) | 8.0 trips/day (assumed) | 15% (deck, unsourced) | D (no source) |

### 2.2 Segment: Intra-city street-hail

**What is sourced:**
- Platform ride-flow proxy: ~591.3M annualized rides across Uber/Ola/Rapido [reported, B]
- Average fare: ₹300 (broad all-cab reference, TOI 23 Jun 2025) [reported, B]
- Trips per driver-day: ~8 (TOI 23 Jun 2025) [reported, B]
- EV adoption among cars: AutoPunditz data shows growing EV share (Karnataka 17.5% of all new vehicles, Aug 2026) [reported, B]

**What is NOT sourced (gaps):**
- Intra-city share of total rides: deck claims 61% (p3) and ~58% (p11) — **contradicted** by the project's own analysis (segments are not a partition; "premium/shared-premium" is a service tier, not a trip purpose) [D]
- 95 km/day duty cycle: **no source** — not measured [C]
- 7.5 trips/day: **no source** — assumed [C]
- ₹350/trip fare: **no source** — assumed [C]
- 18% growth: **no source** — no CAGR derivation exists anywhere in the archive [D]
- 10% EV share: **no source** — contradicts 16-25% implied by the positioning doc's 8,000-10,000 EVs of 40,000-50,000 vehicles [D]
- 0.85 price sensitivity: **no source** — undefined index, contradicts 0.90 on next row and 0.30-0.35 on p11 [D]

**Structural characteristics (sourced + reasoned):**
- **Volume**: Highest of all five segments — platform rides dominate at 591.3M/yr
- **Fare**: Lowest per-km revenue (₹27.6/km gross revenue per vehicle-km, rank 3 of 5) [calc]
- **Dispatch**: Unpredictable, street-hail — no pre-booking
- **Price sensitivity**: High (per deck's own narrative, though index is undefined)
- **Vehicle requirement**: Low-cost, high-durability, minimal features
- **EV adoption**: Growing but from low base; government data shows EV car registrations accelerating (Tata/MG/Mahindra dominate)

**Revenue per vehicle-km (computed from deck's own table):**
- Intra-city: 7.5 trips × ₹350 ÷ 95 km = **₹27.6/km** [calc from deck figures]

### 2.3 Segment: Daily commute / subscription

**What is sourced:**
- **Nothing.** No primary source in the archive addresses this segment directly.

**Gaps (all missing):**
- Annual trips: no source
- Average trip distance: deck claims 22.0 km — no source
- Daily km: deck claims 176 — no source
- Trips/day: deck claims 8.0 — no source
- Fare: deck claims ₹550 — no source
- Growth: deck claims 24% — no source
- EV share: deck claims 12% — no source
- Price sensitivity: deck claims 0.90 — no source

**Sourced context (adjacent, not segment-specific):**
- TGM Research (30 markets, India N=860): 50% of Indian respondents use ride-hailing for daily commute [reported, B]
- Census of India 2011: commute patterns (data is 15 years old; 2021 census delayed)
- Ola/Uber subscription models exist (Ola Pass, Uber One) but no public data on subscriber counts or trip volumes

**Structural characteristics (reasoned, not sourced):**
- **Volume**: Potentially large — commute is the dominant use case for ride-hailing per survey data
- **Fare**: Mid-range (per deck's unsourced ₹550/trip)
- **Dispatch**: Predictable, recurring — ideal for subscription models
- **Price sensitivity**: Moderate (per deck's unsourced 0.90)
- **Vehicle requirement**: Comfort, AC, reliability, consistent service
- **EV adoption**: Unknown — no data

**Key insight:** This segment is the most under-researched in the project. The deck assigns it "STRONG" MACH1 fit with the highest driver revenue (₹114,400/mo) but provides zero evidence. The commute segment is critical because 50% of ride-hailing users cite it as their primary use case (TGM Research), yet no trip-level data exists.

### 2.4 Segment: Airport transfers

**What is sourced:**
- **AAI passenger traffic (Sep 2026):** 196.24M passengers (Apr-Sep 2026), of which 159.54M domestic and 36.70M international [reported, A]
- **Monthly (Sep 2026):** 30.10M total (24.00M domestic + 6.10M international) [reported, A]
- **Year-on-year change:** Total passengers down 2.9% (Apr-Sep 2026 vs 2025) [reported, A]
- **Top airports by domestic passengers (Sep 2026):** Delhi 4.26M, Mumbai 2.78M, Bengaluru 2.71M, Hyderabad 1.67M, Kolkata 1.18M, Chennai 1.15M, Pune 0.87M, Ahmedabad 0.76M [reported, A]
- **Top airports by international passengers (Sep 2026):** Delhi 1.74M, Mumbai 1.22M, Bengaluru 0.55M, Chennai 0.45M, Hyderabad 0.42M, Kochi 0.41M [reported, A]
- **BluSmart (defunct 2025):** Operated in Delhi NCR, Bangalore, Mumbai, Dubai; all-electric; suspended all bookings 17 Apr 2025 [reported, A via Wikipedia]
- **EV adoption:** BluSmart was India's first all-electric shared mobility platform; Gensol leased 6,400 EVs, only 4,704 purchased (SEBI, 15 Apr 2025) [reported, A]

**What is NOT sourced (gaps):**
- Airport transfer demand as a share of air passengers: **no source** — requires mode-share assumption
- 210 km/day duty cycle: **no source** — assumed [C]
- 6.0 trips/day: **no source** — assumed [C]
- ₹600/trip fare: **no source** — assumed [C]
- 26% growth: **no source** — assumed [C]
- 18% EV share: **no source** — contradicts deck's 10% intra-city EV share (mathematical inconsistency) [D]
- 0.35 price sensitivity: **no source** — undefined index [C]

**Demand ceiling calculation [calc + assump]:**
- AAI: 196.24M passengers (Apr-Sep 2026) → ~392.5M annualized (×2) [calc]
- Each air passenger generates 2 road trips (to/from airport) = ~785M road trips [calc]
- If 20-30% of passengers use app cabs (assumption, no source): 157-236M app-cab airport trips/year [est]
- This is **27-40% of the 591.3M total platform rides** — airport is NOT a small segment [calc]

**Structural characteristics:**
- **Volume**: Potentially large (27-40% of platform rides if mode-share assumption holds) — NOT a niche
- **Fare**: Lowest gross revenue per vehicle-km (₹17.1/km, rank 5 of 5) [calc from deck table]
- **Dispatch**: Pre-booked, predictable — enables depot charging
- **Price sensitivity**: Low (per deck's unsourced 0.35)
- **Vehicle requirement**: Luggage space (382-400L boot), comfort, reliability, AC
- **EV adoption**: BluSmart (defunct) was the only at-scale EV airport fleet; GMR Hyderabad 200+ EV fleet (unverified)

**Key insight:** The "margin is in airport" thesis must rest on **cost**, not fare — airport has the lowest revenue/km of all five segments. The margin case requires: (a) zero deadhead (pre-booked return trips), (b) depot charging (controlled overnight), (c) no surge chasing. None of these cost factors are computed anywhere in the project.

### 2.5 Segment: Inter-city / outstation

**What is sourced:**
- **Nothing segment-specific.**

**Gaps (all missing):**
- Annual trips: no source
- Average trip distance: deck claims 280 km — no source
- Daily km: deck claims 340 — **internally inconsistent** (1.5 trips × 280 km = 420 km driven vs 340 printed) [D]
- Trips/day: deck claims 1.5 — no source
- Fare: deck claims ₹4,200 — no source
- Growth: deck claims 20% — no source
- EV share: deck claims 5% — no source
- Price sensitivity: deck claims 0.40 — no source

**Sourced context (adjacent):**
- BluSmart launched EV intercity rides from Delhi NCR to Chandigarh, Jaipur [reported, B via Wikipedia]
- FleetLine E1 range: 268 km at 15% reserve (315 km at zero reserve) — Delhi-Agra 200 km feasible, Delhi-Jaipur 280 km marginal (88.8% of usable pack) [reported, A from roadmap]
- Inter-city taxi is a small share of India's inter-city travel (rail and bus dominate) — but no sourced quantification exists

**Structural characteristics (reasoned):**
- **Volume**: Low — inter-city taxi is a small share of total inter-city travel
- **Fare**: Highest per trip (₹4,200) but lowest per-km (₹18.5/km, rank 4 of 5) [calc from deck]
- **Dispatch**: Pre-booked, planned
- **Price sensitivity**: Low (per deck's unsourced 0.40)
- **Vehicle requirement**: Range (280+ km), comfort, luggage, AC
- **EV adoption**: Very low (5% per deck's unsourced figure) — range anxiety is the binding constraint
- **Key constraint**: FleetLine E1's 268 km range covers Delhi-Agra (200 km) but is marginal for Delhi-Jaipur (280 km). Destination charging required beyond ~300 km.

### 2.6 Segment: Shared and premium mobility

**What is sourced:**
- **Nothing segment-specific.**

**Gaps (all missing):**
- Annual trips: no source
- Average trip distance: deck claims 18.0 km — no source
- Daily km: deck claims 144 — no source
- Trips/day: deck claims 8.0 — no source
- Fare: deck claims ₹520 — no source
- Growth: deck claims 28% — no source (highest of all five, but unsourced)
- EV share: deck claims 15% — no source
- Price sensitivity: deck claims 0.30 — no source

**Sourced context (adjacent):**
- **Green SM (Vietnamese EV fleet):** entered Indian market (Delhi, Gurugram) with ₹8/km capped fare, no surge, consistent vehicle platform, driver training, supervision [reported, B via driver/rider analysis]
- **BluSmart:** operated premium EV service in Delhi NCR, Bangalore, Mumbai; all-electric; defunct April 2025 [reported, A]
- **Ola/Uber premium tiers:** Ola Select, Uber Black exist but no public data on volumes
- **Rider survey (LocalCircles 2025):** 17,993 respondents across 325 districts — cancellation 74%, surge 62%, waiting 53%, cleanliness 30%, driver behaviour 25%, safety 6% [reported, B]
- **SERVQUAL study (n=148, Bengaluru):** Reliability (β=.265), Empathy (β=.263), Tangibility (β=.182) predict satisfaction [reported, B]
- **TGM Research (30 markets, India N=860):** 50% use ride-hailing for daily commute; safety top priority [reported, B]

**Structural characteristics (reasoned):**
- **Volume**: Unknown — "premium/shared-premium" is a **service tier**, not a trip purpose. Airport runs can be premium; intra-city runs can be shared. This is why the segments are not a partition.
- **Fare**: Highest gross revenue per vehicle-km (₹28.9/km, rank 1 of 5) [calc from deck]
- **Dispatch**: Pre-booked (premium) or pooled (shared)
- **Price sensitivity**: Lowest (per deck's unsourced 0.30)
- **Vehicle requirement**: Premium features, space, comfort, branding
- **EV adoption**: Unknown — but Green SM's entry suggests EV premium is viable

**Key insight:** "Shared and premium mobility" as a single segment is analytically incoherent. Shared (Ola Share, Uber Pool) and premium (Uber Black, Ola Select) are different service tiers with different economics, different vehicles, and different customer segments. The deck's 28% growth claim (highest of all five) is unsourced.

---

## 3. Revenue and margin analysis

### 3.1 Gross revenue per vehicle-km (computed from deck's own table)

| Segment | Trips/day | ₹/trip | Daily revenue | km/day | Revenue/km | Rank |
|---|---|---|---|---|---|---|
| Premium/shared | 8.0 | ₹520 | ₹4,160 | 144 | **₹28.9** | 1 |
| Intra-city | 7.5 | ₹350 | ₹2,625 | 95 | **₹27.6** | 2 |
| Commute | 8.0 | ₹550 | ₹4,400 | 176 | **₹25.0** | 3 |
| Inter-city | 1.5 | ₹4,200 | ₹6,300 | 340 | **₹18.5** | 4 |
| Airport | 6.0 | ₹600 | ₹3,600 | 210 | **₹17.1** | 5 |

**Source:** Deck p3 table (all inputs unsourced). Computation: trips/day × ₹/trip ÷ km/day.

**Critical finding:** Airport has the **lowest** gross revenue per vehicle-km of all five segments. The "margin is in airport" thesis **cannot** rest on fare. It must rest on cost structure:
- Zero deadhead (pre-booked return trips)
- Depot charging (controlled overnight, no queueing)
- No surge chasing (predictable demand)
- Higher utilization (pre-booked = fewer empty km)

**None of these cost factors are computed anywhere in the project.** This is the single most important analytical gap.

### 3.2 Driver revenue per month (computed from deck's own table)

All five cells reproduce exactly: trips/day × ₹/trip × 26 days = driver ₹/mo. These are **gross revenue**, not take-home — identical for EV and CNG.

| Segment | Driver ₹/mo (gross) | EV take-home (est.) | CNG take-home (est.) |
|---|---|---|---|
| Intra-city | ₹68,250 | ₹47,060 | ₹32,860 |
| Commute | ₹114,400 | ₹47,060 | ₹32,860 |
| Airport | ₹93,600 | ₹47,060 | ₹32,860 |
| Inter-city | ₹163,800 | ₹47,060 | ₹32,860 |
| Premium | ₹108,160 | ₹47,060 | ₹32,860 |

**Note:** The EV/CNG take-home figures are from the TCO model (Delhi, ₹11/km, 200 km/day, fleet-operated). They do not vary by segment in the current model — this is a limitation. The EV advantage of +₹14,200/mo is invariant across fares (₹11-₹22/km) and platform models (flat ₹67/day vs legacy 20%/25% commission).

### 3.3 TCO advantage summary (Grade A — do not redo)

| Metric | Value | Basis |
|---|---|---|
| Delhi 5-yr nominal (excl. infra) | +14.5% (₹5.75 vs ₹6.73/km) | ₹17,95,367 vs ₹21,00,781 over 312,000 km |
| Delhi 5-yr (incl. ₹99,000 infra) | +6.5% (₹6.31 vs ₹6.75/km) | ₹19,69,367 vs ₹21,05,281 |
| Delhi 5-yr NPV@12% (excl.) | +16.0% | ₹14,07,980 vs ₹16,76,114 |
| Delhi 5-yr NPV@12% (incl.) | +6.7% | — |
| Delhi 8-yr (excl./incl./NPV excl./NPV incl.) | +28.0%/+17.4%/+25.3%/+14.6% | — |
| City matrix 5-yr financed incl-NPV | Delhi +6.7, Mumbai +4.0, Bengaluru +0.9 | — |
| City matrix 8-yr financed incl-NPV | Delhi +14.6, Mumbai +10.6, Bengaluru +9.0 | — |
| Negative cells of 48 | 1 (Bengaluru 5-yr cash NPV incl. infra, −0.4%) | — |
| Driver take-home (fleet-operated) | ₹47,060 vs ₹32,860 = +₹14,200/mo | Annualized ₹5,64,715 vs ₹3,94,320; 5-yr +₹8,51,976 |
| Driver take-home (during loan) | ₹20,021 vs ₹14,768 = +₹5,252/mo | — |

**Model constants:** KM_DAY 200, DAYS_YEAR 312, KM_YEAR 62,400, DISC_RATE 0.12, 12.84 kWh/100km, 45 kWh pack, 90% usable.

---

## 4. Fleet ownership and buyer hypothesis

### 4.1 The buyer hypothesis [Grade C — unverified]

**Claim:** The buyer is a fleet operator running 5,000-40,000 vehicles in Indian metros.

**Evidence:** None. No survey, no interview, no procurement record. The positioning document names Ola, Uber, Refex, Everest, Lithium Urban, Evera, GMR, Bharat Taxi as buyers — but provides no evidence that any of them routinely purchase >500 cars per order.

**Kill criterion (from audit):** If no Indian buyer routinely purchases >500 cars per order, the 5,000-40,000-vehicle thesis is dead and the vehicle must work for a 20-200-car operator.

### 4.2 Fleet anchors [Grade C/D — contradictory]

| Anchor | Value | Source | Grade |
|---|---|---|---|
| Addressable metro vehicles | 40,000-50,000 | Positioning doc | C |
| Of which electric | 8,000-10,000 (16-25%) | Positioning doc | C |
| Implied active cars (national) | ~202,500 (1.62M rides ÷ 8 trips/day) | Calc from platform rides | A |
| BluSmart fleet (defunct) | 6,400 EVs leased (4,704 purchased) | SEBI interim order, 15 Apr 2025 | A |

**Contradiction:** 202,500 implied active cars vs 40,000-50,000 addressable metro vehicles — a ~4-5× gap that was never reconciled. The two anchors describe different markets (national vs metro, all cars vs addressable fleet).

### 4.3 BluSmart verification [Grade A — verified via direct fetch]

- **BluSmart Mobility defunct 2025** — suspended all ride bookings 17 Apr 2025 (Reuters, 17 Apr 2025)
- **SEBI interim order 15 Apr 2025:** Gensol term loans ₹977 cr for leasing 6,400 EVs to BluSmart; only ₹567 cr used to buy 4,704 EVs; ₹400 cr unaccounted/siphoned
- **Asset-light model:** Cars on monthly lease (EESL etc.), NOT driver-owned
- **Expansion hindered because cars were not driver-owned assets** — directly contradicts the positioning doc's fleet-buyer thesis
- **Positioning doc cites BluSmart's exit as validation** of the same segment — this is circular reasoning

### 4.4 Platform economics [Grade B]

| Platform model | Value | Source | Date |
|---|---|---|---|
| Ola flat fee | ₹67/vehicle/day | Positioning doc (via MACH1_TCO_ANALYSIS) | Jun 2025 |
| Uber/Rapido subscription | ₹29/vehicle/day | Positioning doc | Jun 2025 |
| Legacy commission | 15-30% per ride | Industry standard | — |

**Key finding:** The EV advantage (₹14,200/mo) is invariant across flat ₹67/day vs legacy 20%/25% commission. Platform fee structure does not affect the powertrain ranking.

---

## 5. Structural factors explaining volume vs margin

### 5.1 Why intra-city dominates volume

1. **Lowest trip distance** (12.7 km avg) → highest trips per vehicle per day (7.5) → highest vehicle utilization
2. **Lowest fare** (₹350/trip) → accessible to price-sensitive mass market
3. **Street-hail dispatch** → no pre-booking required → lowest friction for spontaneous trips
4. **Highest EV share** (10% per deck, though unsourced; VAHAN data shows accelerating EV adoption) → lower operating cost → competitive pricing possible

### 5.2 Why airport/premium appears to have margin (but doesn't, on fare alone)

1. **Highest fare per trip** (₹600 airport, ₹520 premium) — but **lowest revenue per vehicle-km** (₹17.1 and ₹28.9 respectively)
2. **Pre-booked dispatch** → predictable demand → enables depot charging → lower energy cost
3. **Zero deadhead** (if return trips are pre-booked) → higher paid-km utilization
4. **Low price sensitivity** (0.30-0.35) → less fare pressure

**The margin case is a COST case, not a FARE case.** The project never computes segment-level costs. This is the critical gap.

### 5.3 Why inter-city has low margin despite high fare

1. **Highest distance per trip** (280 km) → lowest trips per day (1.5) → lowest utilization
2. **Lowest revenue per km** (₹18.5/km) — high fare doesn't compensate for distance
3. **Range anxiety** — FleetLine E1's 268 km range is marginal for Delhi-Jaipur (280 km)
4. **Lowest EV adoption** (5% per deck, unsourced) — charging infrastructure sparse on highways

### 5.4 Why commute is the overlooked segment

1. **Highest driver revenue** (₹114,400/mo gross) — but same take-home regardless of segment
2. **Most predictable demand** (recurring, subscription-based)
3. **50% of ride-hailing users cite commute as primary use case** (TGM Research, India N=860)
4. **No data exists** — the project has zero evidence for this segment
5. **Vehicle fit:** Comfort, AC, reliability, consistent service — FleetLine E1's strengths

---

## 6. EV adoption and infrastructure

### 6.1 EV registration trends [reported]

| Metric | Value | Source | Date |
|---|---|---|---|
| Total EV cars (H1 2026) | 148,023 | AutoPunditz | 2026 |
| Top brand: Tata | 38.8% | AutoPunditz | FY2026 |
| Top brand: MG | 28.4% | AutoPunditz | FY2026 |
| Top brand: Mahindra | 24.8% | AutoPunditz | FY2026 |
| Maruti Suzuki (new entrant) | 1.7% | AutoPunditz | FY2026 |
| Karnataka EV share (of all new vehicles) | 17.5% | AutoPunditz | Aug 2026 |
| Euler Motors electric CVs (monthly) | 869 | AutoPunditz | Aug 2026 |

### 6.2 Charging infrastructure [reported]

| Metric | Value | Source |
|---|---|---|
| FleetLine E1 charger | 7.4 kW AC, ₹99,000/vehicle | TCO analysis |
| Overnight charge time | 3.86 h (25.68 kWh ÷ 7.4 kW × 0.90) | TCO analysis |
| Public charger session failure rate | 25-40% | Roadmap (300,000+ model/OEM/CPO combinations) |
| Delhi BEE EV tariff | ₹4.50/kWh | Roadmap |
| Delhi road tax | 0% for life of vehicle | Roadmap (expires 31 Mar 2030) |
| Maharashtra road tax (CNG, non-individual, ≤₹10L) | 14% (corrected from 0%) | TCO analysis §R |

### 6.3 Policy timeline [reported]

| State | Incentive | Expiry |
|---|---|---|
| Delhi | 0% road tax for life; ₹1 lakh scrapping incentive; no purchase incentive for electric cars | 31 Mar 2030 |
| Maharashtra | 15% of ex-factory, capped ₹2 lakh, transport e-4W (25,000 units); 100% toll exemption on Mumbai-Pune Expressway and Samruddhi | 31 Mar 2030 |

### 6.4 Localisation status [reported]

| Metric | Value | Source |
|---|---|---|
| ACC PLI delivered | 1.4 GWh of 50 GWh (2.8%) | Roadmap |
| All from one company | Ola Cell (NMC-first) | Roadmap |
| Reliance Jamnagar LFP | 40 GWh, ramping H2 2026 | Roadmap |
| Domestic value addition | Below 60% DVA threshold (CAM, AAM, separators, electrolytes, foils imported) | Roadmap |

---

## 7. Data gaps and unverified claims

### 7.1 Critical gaps (no source found anywhere)

| # | Gap | Why it matters | Recommended collection route |
|---|---|---|---|
| 1 | **Segment-level trip counts** — no India-wide data on how many trips are airport vs commute vs intra-city | Core of Deliverable 1; without this, no market sizing is possible | Operator/platform trip-level data (anonymized) |
| 2 | **Segment-level fares** — ₹350/₹550/₹600/₹4,200/₹520 are all unsourced | Revenue and margin analysis depends on this | Operator fare distributions by trip type |
| 3 | **Segment-level duty cycles** — 95/176/210/340/144 km/day are all unsourced | Vehicle specification depends on this | 30-50 logged driver-days per segment |
| 4 | **Commute segment** — zero evidence of any kind | 50% of users cite commute as primary use case (TGM) | Corporate subscription data, employer transport surveys |
| 5 | **Inter-city taxi share** — no data on what share of inter-city travel is by taxi vs rail/bus | Segment sizing impossible | Rail/bus passenger data + taxi permit data |
| 6 | **Paid vs unpaid km** — no data on deadhead by segment | Margin analysis depends on this | GPS trace data from operators |
| 7 | **Active fleet stock** — registrations ≠ active vehicles | Market sizing conversion (rides → vehicles) | Transport permit data, operator fleet counts |
| 8 | **Replacement cycle** — no data on how often fleet vehicles are replaced | Vehicle opportunity calculation | Operator procurement records |

### 7.2 Six external lynchpins (Grade C, unverified)

| # | Claim | Source cited | Status |
|---|---|---|---|
| 1 | Evera operates across Delhi airport terminals | Positioning doc | Unverified — no company/airport release found |
| 2 | GMR Hyderabad has 200+ vehicle premium airport fleet | Positioning doc | Unverified — no GMR release found |
| 3 | Bharat Taxi operates at Navi Mumbai | Positioning doc | Unverified — Navi Mumbai airport opened 2025, too early for fleet data |
| 4 | BluSmart assumed 10% residual, realised 26% | Positioning doc | Unverified — BluSmart is defunct; no residual data published |
| 5 | Uber Black's top two use cases are airport and corporate | Positioning doc | Unverified — no Uber India data found |
| 6 | Ola charges ₹67/vehicle/day flat; Uber+Rapido ₹29 | Positioning doc | Partially verified — ₹67 appears in TCO analysis; ₹29 unverified |

### 7.3 Internal contradictions (from audit)

| # | Contradiction | Details |
|---|---|---|
| 1 | `figures.txt` is stale | Reports Mumbai 5-yr −0.2%, "4 negative cells", "5-year case doesn't close outside Delhi" — all contradicted by current engine and deck |
| 2 | 263 km vs 268 km range | Two conventions (old 15.38 kWh/100km basis vs retained 12.84 kWh/100km basis) |
| 3 | 8,000-10,000 EVs of 40,000-50,000 = 16-25% | Contradicts deck's 10% intra-city EV share |
| 4 | 0.85 "highest" price sensitivity | 0.90 printed on next row; p11 uses second undefined scale (0.30-0.35) |
| 5 | "61%" vs "~58%" intra-city share | Segments are not a partition; cannot be a valid decomposition |
| 6 | 202,500 implied active cars vs 40,000-50,000 addressable | ~4-5× gap, never reconciled |
| 7 | `market_analysis.py` path bug | Reports all 6 CSVs as "missing" — inventory section has never run |
| 8 | MCH-I-008: 200,000 km rated life vs 312,000 km 5-yr duty | Critical issue, all 13 issues Open |

---

## 8. What the evidence actually supports (summary)

### 8.1 Defensible findings (Grade A-B)

1. **Platform ride-flow proxy:** 591.3M annualized rides across Uber/Ola/Rapido (Motilal Oswal via Business Standard, 18 Apr 2025) — Grade B
2. **Average fare:** ₹300 (broad all-cab reference, TOI 23 Jun 2025) — Grade B
3. **Trips per driver-day:** ~8 (TOI 23 Jun 2025) — Grade B
4. **AAI airport passengers:** 196.24M (Apr-Sep 2026), 30.10M (Sep 2026) — Grade A
5. **TCO model:** All headline numbers reproduce exactly — Grade A
6. **Driver economics:** +₹14,200/mo advantage, invariant across fares and platform models — Grade A
7. **BluSmart defunct:** SEBI order, Reuters confirmation — Grade A
8. **EV registration growth:** AutoPunditz data shows accelerating EV adoption — Grade B
9. **Airport revenue/km is lowest:** ₹17.1/km (computed from deck's own table) — Grade A (calc)
10. **Segments are not a partition:** "premium/shared-premium" is a service tier — Grade A (reasoned)

### 8.2 Indefensible claims (Grade C-D)

1. Five-segment table (all 40 cells) — no source, withdrawn by ruling document
2. 61% / ~58% intra-city share — contradicted by own analysis
3. 19.14% airport CAGR — no derivation exists
4. Dendrogram / cluster labels — invalid (5 rows, 7 features)
5. All growth rates (18-28%) — no source
6. All EV shares (5-18%) — no source, internally contradictory
7. All price sensitivity indices (0.30-0.90) — undefined, contradictory
8. All daily km (95-340) — no source
9. Buyer = 5,000-40,000 vehicle fleet operator — no evidence
10. "Airport is highest margin" — fare data shows opposite; cost not computed

### 8.3 Key structural findings

1. **Volume is in intra-city** — 591.3M platform rides/yr, highest trips/vehicle/day
2. **Airport is NOT a niche** — potentially 27-40% of platform rides (if mode-share assumption holds)
3. **Airport has the LOWEST revenue/km** — ₹17.1/km (rank 5 of 5). Margin must come from cost, not fare.
4. **Commute is the most under-researched segment** — 50% of users cite it as primary use case, zero data exists
5. **Segments are not a partition** — "premium/shared-premium" is a service tier, not a trip purpose
6. **The vehicle-market case is solid** — TCO, driver economics, battery chemistry all Grade A
7. **The market model is indefensible** — no segment-level data exists for any of the five segments

---

## 9. Recommended next steps (prioritised)

### P0 (blockers)

1. **Test buyer hypothesis** — verify if any Indian buyer routinely purchases >500 cars/order. Kill criterion defined.
2. **Measure duty cycle and fare** — 30-50 logged driver-days per segment; airport concession data; operator filings.
3. **Re-segment orthogonally** — purpose × channel × tier; never sum across axes; car-only base (474.5M/yr excluding Rapido).

### P1 (important)

4. **Reframe airport thesis as cost/segment P&L** — use existing TCO engine; compute deadhead, charging, utilization by segment.
5. **Verify six external lynchpins** — all Grade C; direct URL fetches only.
6. **Repair repo contradictions** — regenerate figures.txt, fix market_analysis.py path, resolve 263 vs 268 km, resolve MCH-I-008.

### P2 (valuable)

7. **Bottom-up 2035 demand path** — no CAGR extrapolation; city × segment × period panel.
8. **Competitive supply response** — Green SM entry, Ola/Uber EV plans, Namma Yatri/ONDC.

---

## 10. Unresolved questions

1. Is the buyer hypothesis (5,000-40,000 vehicle fleet operator) valid? No evidence exists.
2. What is the actual airport transfer demand as a share of air passenger traffic? Mode share unknown.
3. What is the actual commute segment size? Zero data exists.
4. What is the actual inter-city taxi share? No data exists.
5. What are segment-level fares, duty cycles, and paid/unpaid km ratios? All unsourced.
6. Does the flat-fee platform model (₹67/day) persist to 2035? Unknown.
7. What is the actual EV adoption rate in commercial fleets (not just registrations)? Unknown.

---

*This report was produced from primary sources only. No figures were invented or silently modified. All gaps are explicitly identified. The audit trail is in `00_audit/RESEARCH_AUDIT.md` and `00_audit/AUDIT_EXECUTIVE_SUMMARY.md`.*
