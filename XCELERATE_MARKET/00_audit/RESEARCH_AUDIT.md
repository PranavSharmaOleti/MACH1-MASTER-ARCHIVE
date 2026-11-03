# MACH1 / FleetLine E1 — Research Audit

**Scope:** all project material under `~/Downloads/MACH1_WORKING_FILES` (incl. `MACH1_MASTER_ARCHIVE/`), `~/Downloads/mach1_audit/`, `E-Track Case Study.pdf`.
**Date of audit:** 3 Nov 2026. **Auditor:** independent pass — existing conclusions treated as hypotheses.
**Reproduce:** `python3 segment_table_check.py` (20 checks → `segment_table_checks.csv`); `python3 ../tco_engine/tco_analysis.py > run.txt` (878 lines, exit 0); `python3 ../Market/market_analysis.py`.

## Confidence scale used below

| Grade | Meaning |
|---|---|
| **A** | Reproduced from data or script **inside this repository**, deterministically, by this audit. |
| **B** | Single traceable secondary source (named publisher + date), not independently verifiable here. |
| **C** | Internal assertion: no source file anywhere in the archive. |
| **D** | **Contradicted** by the project's own evidence. |

Evidence type is tagged: `[calc]` calculated · `[reported]` reported by a third party · `[est]` estimate · `[assump]` assumption.

---

## 1. Audit table

### A. Market size and segmentation — the weakest block in the project

| # | Claim | Existing evidence | Conf. | Gap | Recommended action |
|---|---|---|---|---|---|
| A1 | Five-segment use-case table: 35 cells in the left table (avg km, km/day, trips/day, ₹/trip, growth, EV share, price sensitivity) plus 5 driver ₹/mo cells in the right | Deck p3 only. `MACH1_MARKET_ASSESSMENT.pdf` (18 Oct 2026) **withdraws it**; provenance register holds **8 of ~40 distinct cells** (MCH-N-006…013), all `Source = Deck`. Traces to `NITDurgapur/Detailed Report.pdf` → drafts → deck, with no derivation at any step. | **D/C** | Every cell except two growth rates. No source exists in the archive, and the project's own ruling document forbids the table. | **Withdraw.** Do not repair. Replace with the measured-inputs table in §3, or state the segmentation as an explicit `[est]` with stated method. |
| A2 | "61% of market is intra-city" / "~58% of rides" | Two different numbers in the same deck (p3 vs p11). Register N-010 calls 61% "~58% derived" — but no derivation exists. | **D** | Sum of segment shares is undefined: the five rows are **not a partition** (check C6) — "premium/shared-premium" is a service class, not a trip purpose, so rows overlap and cannot sum to 100%. | Delete. Any share claim needs trip-level purpose data (none public — see §3). |
| A3 | "19.14% CAGR, fastest-growing" (airport) | Register N-009 marks it `External source` with **no source file**. Appears only in deck/derived docs. | **C** | No source. Also self-contradictory: the same table prints airport 26% and premium 28% growth (MCH-I-005), so 19.14% cannot be "fastest". | Delete or cite. If a CAGR is needed, derive it from a registration series and label the series. |
| A4 | 591.3M platform rides/year | `market_analysis.py` reproduces 1.62M/day × 365 = 591.3M exactly. Underlying data: Uber 840k / Ola 460k / Rapido 320k daily, Motilal Oswal **as cited by** Business Standard, 18 Apr 2025. | **A** (arithmetic) / **B** (inputs) | Rapido is predominantly two-wheelers; article scope unclear. Three platform counts summed ≠ India taxi trips (no de-duplication, no offline taxis, no black-yellow). | Keep, but relabel "platform ride-flow proxy" and show a **car-only sensitivity** (excl. Rapido: 474.5M/yr — a −20% swing that moves every downstream number). |
| A5 | GMV scenarios ₹887 / ₹2,661 / ₹5,322 cr | `market_analysis.py` reproduces all three. Correctly labelled "scenario envelope, not TAM". | **A** (arithmetic) / `[assump]` (share 5–15%, fare ₹300–600) | Target share is the dominant unknown and is pure assumption. | Keep as labelled. Convert to **vehicles**, not GMV, before it informs the design (formula already written in `MARKET_ASSESSMENT.pdf` §1). |
| A6 | EV share: 10% intra-city, 18% airport | Register N-006/N-008, `Source = Deck`, `Unverified`. | **D** | Contradicted in-house: `E1_Audience_and_Positioning.pdf` says 8,000–10,000 EVs of 40,000–50,000 addressable-metro vehicles = **16–25%** (check C5). | One number, one measurement. VAHAN commercial-class EV registrations can give a **fleet-stock proxy**, not a share of active ride-hailing cars — say which. |
| A7 | Price sensitivity 0.85 / 0.90 / 0.35 / 0.40 / 0.30 | Register N-007, `Source = Deck`. `PPT_CHANGE_LIST` edit #8 already orders it labelled "estimated index". | **D** | Index undefined (own-price elasticity? willingness-to-pay score? scale 0–1?). Two incompatible scales: table 0.30–0.90 vs p11 "0.30–0.35". 0.85 is called "highest" while 0.90 is printed (MCH-I-003). | Delete the column or define the metric, estimator and sample. Nothing in this project can be salvaged from it. |
| A8 | Dendrogram / "Cluster A = airport + corporate-commute" | `MARKET_ASSESSMENT.pdf` §2 condemns it: 5 hand-built rows, 7 columns, 2 residual df. Register: "stated only". | **D** | No feature matrix, no observations. | Remove (already `PPT_CHANGE_LIST` edit #7). Do not substitute another clusterer on the same 5 rows. |

### B. Operating characteristics — assumed, then quoted as fact

| # | Claim | Existing evidence | Conf. | Gap | Recommended action |
|---|---|---|---|---|---|
| B1 | "Fleet duty is 200 km/day, 312 days/yr, 62,400 km/yr" (deck p11, stated as fact about Indian fleets) | Model constant in `tco_engine.py` (`KM_DAY=200`, `DAYS_YEAR=312`). No measured source. | **C** | It is the **design assumption**, not an observed duty cycle. Note the deck's own segment table gives 95/144/176/210/340 km/day — i.e. the fleet does *not* run 200 km/day on average. | Reword as "specified duty cycle". Then measure it: this is the single highest-value field dataset (see §3, P0-2). |
| B2 | Segment km/day: 95 / 176 / 210 / 340 / 144 | Deck p3 only. | **C** | **Inter-city row is arithmetically wrong**: 1.5 trips × 280 km = 420 km driven, table prints 340 (check C1; already `PPT_CHANGE_LIST` edit #4). Other four rows reconcile exactly. | Row must go with the table. If reinstated, 340 → 420 (or 1.5 → 1.21 trips). |
| B3 | ~8 trips per driver-day, ~₹300 average fare | `MARKET_ASSESSMENT.pdf` §1, citing TOI 23 Jun 2025. | **B** | One press reference, broad all-cab basis, not segment-specific. Anchors the national active-fleet estimate (~202,500 cars). | Keep as range input with the source quoted and period stated. |
| B4 | Trips/day 7.5 / 8.0 / 6.0 / 1.5 / 8.0 | Deck p3 only. | **C** | No source. Note these are *per vehicle per day*, and reconstruct the table's ₹/month exactly (check C2: trips × fare × 26 = printed figure, all five rows). So the table is internally coherent as **gross revenue**, and was mislabelled "DRIVER ₹/MO". | If any part survives, relabel "gross revenue, not take-home". `DRIVER_AND_RIDER_ANALYSIS.pdf` §1 already says this. |

### C. Fleet ownership and the buyer hypothesis — the strategic risk

| # | Claim | Existing evidence | Conf. | Gap | Recommended action |
|---|---|---|---|---|---|
| C1 | **Buyer = fleet operator running 5,000–40,000 vehicles**; "every commercial conversation ends at an operations manager's desk" | `E1_Audience_and_Positioning.pdf` §1. No survey, no interview, no procurement record. Named examples are Ola/Uber (platforms that mostly **do not own** Indian cars), Refex, Everest, Lithium Urban, Evera, GMR, Bharat Taxi. | **C** | No evidence of any Indian ride-hailing fleet of this size outside a platform. The one at-scale leased EV fleet in India — BluSmart, whose Gensol lease programme covered **6,400 EVs, of which 4,704 were actually purchased** (SEBI interim order, 15 Apr 2025) — **suspended operations in April 2025** (Reuters, 17 Apr 2025). The document cites BluSmart's exit as *demand* for the same segment, which is circular: the failure of the only comparable buyer is treated as validation. | **Highest-priority strategic question.** Test the buyer hypothesis before anything else. If the real buyer is the owner-driver or a 20–200-vehicle operator, the product, finance and channel all change. |
| C2 | 40,000–50,000 ride-hailing vehicles in addressable metros; 8,000–10,000 already electric; "replacement window now open" | `E1_Audience_and_Positioning.pdf`, footnote, **no named source**. | **D** | Inconsistent with the project's own ride count: 1.62M rides/day ÷ 8 trips/day ≈ **202,500 active cars nationally** (check C4). The claim makes addressable metros 20–25% of the national fleet. `[est]` Delhi NCR alone is plausibly of that order, which makes the metro total implausibly low. | Reconcile to one fleet anchor, or state both and explain the gap. |
| C3 | "Drivers choose the platform; operators choose the vehicle" | Assertion in audience doc. | **C** | In India the modal arrangement is the **owner-driver attached to a platform** — the same person makes both choices. Under flat-fee economics the platform also constrains both. | Test with any state transport-authority permit/ownership data or platform onboarding terms. |

### D. Platform economics — low risk to the headline, high risk to credibility

| # | Claim | Existing evidence | Conf. | Gap | Recommended action |
|---|---|---|---|---|---|
| D1 | "Ola at ₹67 per vehicle per day, Uber and Rapido at ₹29" (flat fee) | `E1_Audience_and_Positioning.pdf` §2 and `DRIVER_AND_RIDER_ANALYSIS.pdf` §5. No citation. | **C** | Drives the driver P&L line (−₹1,742/mo). **The ₹14,200 EV advantage is invariant to commission structure** — verified: flat ₹67/day, 20%/ride and 25%/ride all give +₹14,200. So the *conclusion* survives even if the fee is wrong. | Cite or drop. The invariance argument is the defensible one; lead with it. |
| D2 | Legacy 20–25% commission | `DRIVER_AND_RIDER_ANALYSIS.pdf` §5. | **C/B** | Directionally well known, unsourced here. | One dated citation. |
| D3 | Slide 3 "DRIVER ₹/MO" column | Reproduced exactly as trips × fare × 26 (check C2). | **A** (that it is gross) | Mislabelled: it is gross revenue, identical for EV and CNG. `DRIVER_AND_RIDER_ANALYSIS.pdf` §1 flags this itself; the deck still prints it. | Remove with the table. |

### E. TCO — the strongest block; reproducible, self-audited

| # | Claim | Existing evidence | Conf. | Gap | Recommended action |
|---|---|---|---|---|---|
| E1 | Delhi 5-yr ₹5.75/km EV vs ₹6.73/km CNG (+14.5%) | `tco_analysis.py` §F+§L reproduce **exactly** (1,795,367 vs 2,100,781 over 312,000 km). | **A** | None on arithmetic. Basis is nominal, **excludes** charging infrastructure — the deck has at times presented it as if it included it. | Keep; always print the basis label with the number (this is the project's own "Rev 4" rule). |
| E2 | +6.5% nominal incl. ₹99,000/vehicle infra; +6.7% NPV@12% escalated incl. infra | Reproduced exactly (§G, §L). | **A** | The ₹99,000 charger cost is `[assump]` (₹50k charger + ₹30k installation + ₹10k meter, ×1.10). | State as assumption with its build-up; run the breakeven (engine does: Delhi headroom ₹1.12 lakh). |
| E3 | City matrix 5-yr: Delhi +6.7 / Mumbai +4.0 / Bengaluru +0.9; 8-yr: +14.6 / +10.6 / +9.0 | Reproduced **exactly** by current §M and §R. Deck matches engine. | **A** | `tco_engine/figures.txt` is **stale** and contradicts both: it reports Mumbai −0.2% (5-yr) and "4 negative cells of 48" and "the 5-year case does not close outside Delhi". That file predates the §R Mumbai road-tax correction (Maharashtra MV Tax Amendment Act 2025, gazetted 19-03-2025). Anyone re-deriving from `figures.txt` will conclude the deck is wrong. | **Regenerate or delete `figures.txt`.** One artefact disagreeing with the engine is the most dangerous file in the repository. |
| E4 | "One cell in 48 is negative — Bengaluru, cash, −0.4%" | Reproduced exactly (§M: 1 of 48). | **A** | None. | Keep. |
| E5 | Driver advantage +₹14,200/mo, invariant across fare, duty and commission model | Reproduced (§A: during loan +₹5,252, after loan +₹14,200; 150 km/day → +₹10,597). | **A** ([calc]) | It is a **modelled** difference between two cost stacks, not observed earnings. Two driver views exist (with/without ₹1,742 platform fee) and reconcile exactly — documented, not an error. | Keep. Never present as observed driver income. |
| E6 | Residual value: EV 26%, CNG 40% | Engine inputs. | `[assump]` | The "BluSmart assumed 10%, realised 26%" justification is **unverified** and its source company is defunct. | Replace with a defensible residual study or drop the narrative. This input moves the answer a lot: EV residual 26→36% moves the advantage +14.5→+20.6%. |
| E7 | 200,000 km rated life vs 312,000 km 5-yr duty | `MCH-I-008`, open. | **D** | The comparator is retired mid-model-life; replacement cost treatment is unstated. | Resolve before any external use. |
| E8 | Two range bases: 263 km (old 15.38 kWh/100km) vs 268 km (12.84 kWh/100km) | `MACH1_POWERTRAIN_SPECS_REPORT.pdf` documents both; deck p11 uses 268. | **D** | Two conventions live in the repo (also 36 kWh @10–90% vs 45×0.9 usable). | Declare one usable-capacity + reserve convention and delete the other. |

### F. Positioning narrative — evidence exists, but not in this repository

| # | Claim | Existing evidence | Conf. | Gap | Recommended action |
|---|---|---|---|---|---|
| F1 | Evera at Delhi terminals; GMR Hyderabad "200+ vehicle premium airport fleet"; Bharat Taxi at Navi Mumbai | Audience doc §1, deck p3. **No citation, no date, no document.** | **C** | These three are the *entire* real-world basis for the airport lane. None is in the archive. | Verify against company/airport-operator press releases. This is cheap and decisive. |
| F2 | "Airport EV share is already 18% → the operator is already electrifying this lane" | Register N-008, `Source = Deck`. | **C** | Suspicious coincidence: 18% also appears as *intra-city growth* in the same table. No measurement. | Drop unless a VAHAN commercial-class or operator disclosure supports it. |
| F3 | "Uber Black's top two use cases are airport and corporate travel" | Deck p3. No citation. | **C** | Unverifiable as written (Uber Black is a small premium tier; inferring segment structure from it is a category error). | Drop. |
| F4 | **Airport + corporate commute is the margin segment** (the core thesis) | Never calculated. The claim rests on `[assump]` margin, not on any margin arithmetic. | **D (as stated)** | On the table's **own** numbers, airport earns the **lowest gross revenue per vehicle-km of all five segments**: ₹17.1/km vs premium ₹28.9, intra-city ₹27.6, commute ₹25.0, inter-city ₹18.5 (check C3/C7). The margin claim must therefore rest on *cost* (zero deadhead, pre-booked, depot charging) — which the project never quantifies. | **Reframe the thesis**: airport is not a fare-premium segment, it is a **cost-structure** segment. Then prove the cost claim. As written, a panel member with the table in front of them can refute the thesis with one division. |
| F5 | BluSmart "assumed 10%, realised 26%" residual | Audience doc §3, deck. | **C** | Company defunct (Apr 2025); no filing supports either figure. | Verify or remove (see E6). |

### G. Data assets and reproducibility

| # | Item | Evidence | Conf. | Gap | Action |
|---|---|---|---|---|---|
| G1 | `data/vahan_panel.csv` | 16,274 rows but **4 states only**; year labels mixed with month labels; Oct-2026 likely partial. | **A** | Cannot support a national or metro claim. | Keep as exploratory; never cite for totals. |
| G2 | `Market/market_analysis.py` | Runs; reproduces §A4/A5. | **A** | **Path bug**: `DATA = ROOT/"data"`, but the CSVs live in `../data`. It silently prints "missing" for all six files, so the data-inventory section has never actually run. | One-line fix, then rerun. |
| G3 | AutoPunditz CSVs | Model/month series, Feb 2020–Sep 2026 (188 rows); OEM file Apr–Sep 2026 only (87 rows). | **A** | Mixes wholesale dispatch with retail registration; no `measure_type` field. | Add the field before any use. |
| G4 | Provenance register | 92 numerical records, 46 `Verified — Derived`, 13 `External source`, 11 `Unverified`, 6 `Discrepancy`. | **A** | Covers **8 of ~35** market-table cells; the gap analysis lists 160 further deck numbers not registered. Register tracks the TCO well and the market barely at all. | Extend coverage only for claims that survive; do not register numbers that are being deleted. |

---

## 2. What is actually established

**Established (Grade A, keep and build on):** the TCO engine. Every headline TCO number in the deck reproduces from `tco_analysis.py`, the self-tests inside it pass, the Mumbai road-tax correction is documented with a gazette reference and its direction stated honestly, and the one-negative-cell claim is exact. This is genuinely better work than the market side and should not be redone.

**Established but thin (Grade A arithmetic, B inputs):** the 591.3M ride proxy and the three GMV scenarios. The arithmetic is right and the labelling is honest. The inputs are one press article citing one broker.

**Not established anywhere (Grade C/D):** everything that makes the strategy a strategy — that the five segments exist as measurable markets, that intra-city is 61% (or 58%), that airport is the margin segment, that the buyer is a 5,000–40,000-vehicle fleet operator, that 40,000–50,000 addressable-metro vehicles exist of which 8,000–10,000 are electric, and that price sensitivity differs by segment.

**Net:** the project has a defensible **cost** model and an indefensible **market** model. The deck's weakest slide (p3) is the one that decides which vehicle to build. That is the gap to close, and it is not closable by re-reading the archive.

## 3. Prioritised research plan

Ordered by *decision impact per unit of effort*. P0 items each change the recommended vehicle; P2 items only harden the story.

### P0-1 — Test the buyer hypothesis (2–3 days; decides channel and finance)
- Do **not** start with market size. Start with who signs the purchase order.
- Sources: state transport authority permit/ownership data (Delhi, Maharashtra, Karnataka); platform onboarding terms and driver-attachment models; Refex/Lithium/Everest fleet disclosures; airport-operator concession documents (DIAL, BCAS) for taxi/EV fleet contracts; BluSmart/Gensol insolvency record as the counter-case.
- Deliverable: a buyer map with fleet-size bands, ownership type, and the actual decision-maker, each with a citation. **Kill criterion:** if no Indian buyer routinely purchases >500 cars per order, the 5,000–40,000-vehicle thesis is dead and the product must work for a 20–200-vehicle operator.

### P0-2 — Build a measured duty-cycle and fare dataset (the single highest-value input)
The 200 km/day, 8 trips/day and ₹300–600 fare assumptions drive everything downstream, and none is measured. Priority order of feasible sources:
1. Airport prepaid-taxi and app-cab operator data (trip distance distribution, fare, wait time) — airport operators publish concession statistics.
2. Company filings/disclosures of ride-hailing and fleet operators (paid km, trips, utilisation).
3. Primary collection: 30–50 driver-days of logged trips across Bengaluru/Delhi (odometer, app screenshots, fuel/charge receipts). Cheap, fast, and directly usable — and it makes the `[assump]` labels disappear.
- Deliverable: km/day, trips/day, paid-km ratio, fare distribution, **by segment**, with n and collection dates.

### P0-3 — Replace the segment table with a defensible segmentation (1 week)
- Segmentation must be **orthogonal**. Recommended axes: trip purpose (commute / airport / intercity / other) × booking channel (hail / app / contract) × service tier (standard / premium). Report premium as a *tier*, never as a segment, and never sum across axes.
- Size only what can be measured: platform ride proxy × measured purpose mix × measured fare. Where a cell is unknown, print "not measured" rather than a number.
- Explicitly test the **car-only** ride base (excl. Rapido two-wheelers): 474.5M/yr vs 591.3M/yr.

### P1-4 — Reframe and prove the airport/corporate thesis as a cost story (3–4 days)
The table shows airport at ₹17.1/vehicle-km — the lowest of five. Either:
(a) prove the cost advantage: deadhead ratio, pre-booked utilisation, airport surcharge/toll/queue economics, depot-charging access; or
(b) abandon "margin is in airport" and let the data pick the launch segment.
Recommended: do (a) as a **segment P&L** — revenue/km, cost/km, contribution/vehicle-month — using the existing TCO engine, which already has the structure. That single table would replace three slides of assertion.

### P1-5 — Verify the six external lynchpins (1 day, desk research)
Evera at Delhi terminals · GMR Hyderabad 200+ EV fleet · Bharat Taxi Navi Mumbai · BluSmart 10%/26% residual · Uber Black top-two use cases · ₹67/₹29 platform flat fees. All six are currently Grade C and each is a single citation away from being Grade B — or from being deleted. Note: live web search was unavailable during this audit (HTTP 402), so none of the six could be checked here; direct URL fetches work, general search does not.

### P1-6 — Repair the repository's internal contradictions (half day)
- Regenerate or delete `tco_engine/figures.txt` (stale; contradicts engine and deck).
- Fix the `market_analysis.py` data path so the inventory actually runs.
- Declare one range/usable-capacity convention and delete the other (263 vs 268 km; 36 kWh vs 45×0.9).
- Resolve `MCH-I-008` (200,000 km rated life vs 312,000 km duty) — it is the only open issue that changes a headline number.

### P2-7 — 2035 demand path (2–3 days, only after P0-3)
Do not extrapolate the ride proxy with a CAGR (the project's own ruling forbids it). Build a bottom-up 2035 scenario: metro population × trips per capita × modal share of app-cabs × purpose mix, with each factor sourced and ranged; cross-check against VAHAN commercial-vehicle registration trend and any NITI/MoRTH projection. Present as a range with named drivers, not a point estimate.

### P2-8 — Competitive supply response (1–2 days)
Maruti is not the only supplier: Tata (Xpres-T), Hyundai, MG, and the CNG incumbent. Test whether the proposed vehicle's spec is actually differentiated at a ₹12.7 lakh on-road price. This is a *positioning* question the market data cannot answer.

---

## 4. Open questions this audit cannot close

1. Is there any public measurement of Indian ride-hailing trip-purpose mix? If not (probable), every segment-share number in the project is an assumption and the deck must say so.
2. Does any Indian buyer routinely procure ride-service vehicles in four- or five-figure volumes? BluSmart's collapse is evidence against, not for.
3. Is the airport lane's cost advantage (deadhead, queue, depot charging) large enough to overcome the lowest revenue/km of the five segments? Never tested.
4. Which of the two driver-economics views is the intended one (with or without the ₹1,742 platform fee)? They reconcile, but the deck should quote one.
5. Was `figures.txt` ever used to write any external submission? If so, the Mumbai and negative-cell discrepancies are already in circulation.
