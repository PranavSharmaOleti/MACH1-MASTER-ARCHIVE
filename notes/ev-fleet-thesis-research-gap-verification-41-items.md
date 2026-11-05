# EV Fleet Thesis — Research Gap Verification

**Report date:** 3 November 2026 · **Scope:** Verification of the 41-item research gap list for the fleet-buyer thesis (positioning doc MACH1_E1). All 41 items investigated against public sources; primary documents opened where accessible.

---

## Question

Independently verify (or falsify) every externally cited claim and fill every data gap in the EV fleet-buyer thesis: external lynchpins (A), market size (B), segment operating data (C), fleet & buyer data (D), charging infrastructure (E), regulatory (F), and competitor data (G) — with source, date, and methodology for each, and no invented data.

---

## Executive Summary

Ranked takeaways:

1. **Four of six "external lynchpins" check out; two do not as stated.** Evera (item 1), Bharat Taxi at NMIA (item 3), Uber Black's airport/corporate use cases (item 5), and the Ola ₹67/day fee (item 6) are verified by primary reporting. The GMR Hyderabad "200+ EV fleet" (item 2) is a conflation — GHIAL's 200+ airport taxi fleet is real but not documented as electric; the EV operator at RGIA is OHM E-Cabs. The BluSmart "assumed 10% residual, realised 26%" claim (item 4) is **undocumented in any public source** — the SEBI order, lender filings, and auction coverage contain no residual-value percentages. Treat it as fabricated until a document is produced.
2. **The market-size chain holds.** Redseer data implies ~2.8–3.1 billion total ride-hailing trips in CY2025 with cabs at 27% of trips (~810M cab trips) and 50–55% of GMV — internally consistent with the deck. Motilal Oswal's 840k/460k/320k daily cab rides (Uber/Ola/Rapido, Jan 2025) is confirmed verbatim. AAI's Apr–Sep 2026 total (~196.2M passengers) reconciles exactly with its published domestic (159.54M) and international (−7.1%) figures.
3. **The BluSmart collapse is a live, quantified fleet-supply event — but residual values are still unpublished.** SEBI order: ₹978cr loans, ₹663cr earmarked for 6,400 EVs, only 4,704 bought for ₹568cr (implied ~₹12.07 lakh/vehicle). Disposition: Refex's 2,997-EV deal collapsed; Uber shelved a ~5,000-EV absorption; 1,500–2,000 EVs went on the block; Evera repossessed 500 (Oct 2026) and wants 500 more. No transaction prices per vehicle are public — the fleet-buyer thesis cannot yet cite realised residuals.
4. **Fleet-operator sizes are now verified and material:** Everest Fleet 18,500+ vehicles (Uber's largest India fleet partner), Lithium Urban 3,000+ EVs / 1,300 chargers / 25,000 trips/day, Evera ~2,200 EVs + 500 repossessed, Refex eVeelz 1,000+, eee-Taxi ~1,000, OHM ~100→1,300 target, Snap-E 600. Procurement is consistently lease/finance-based (asset-light), via OEM bulk deals and lender partnerships — not outright purchase.
5. **Two deck errors confirmed:** (i) GST on ICE cars is **28% + 1–22% cess (29–50% effective), not 18%** — the EV 5% advantage is larger than the deck states; (ii) PM E-DRIVE gives **zero subsidy to electric four-wheelers** (excluded since FY25; scheme extended to Mar 2028 for buses/trucks/3W/charging) — no central subsidy cushion in cab TCO.
6. **Airport demand signals are strong but mode-share remains an assumption.** Rapido: 12–15% of its cab rides are airport rides; Evera: 55% of bookings are airport pick-ups, avg ₹600/trip; Uber Reserve: 40% of trips end at airports; ~100k app-cabs/month at Delhi T3; Delhi pick-up fee ₹290/trip (raised ~40%). But no published Indian airport mode-share % exists — the deck's 20–30% stays a modelling assumption.
7. **The entire p3 segment table (items 16–21) — trip lengths, km/day, growth, EV share, price-sensitivity coefficients — has no public source.** Only loose anchors verify (metro drivers ~8 trips/day, ₹300–400 avg fare, corporate EVs ~300 km/day, airport trips ~₹600). Items 13, 21 and parts of 11–12, 14–15 are **not publicly measurable** and require primary research (platform data, driver surveys, airport operator data).

---

## Methodology

- **Search angles:** (1) named-entity verification (Evera, GHIAL, Bharat Taxi, BluSmart/Gensol, Uber Black, Ola Fleet); (2) market-data triangulation (Redseer, Motilal Oswal, Deloitte, Sensor Tower); (3) regulatory primary texts (PM E-DRIVE portal/notifications, GST schedules, Maharashtra Tax Amendment Act 2025); (4) primary financials (ANI Technologies, Rapido, Uber India Systems, Ola Fleet — via RoC/Tofler/Entrackr coverage); (5) infrastructure operators (Tata Power, DIAL, NMIA); (6) airport ground-transport studies.
- **Source types:** business press (ET, BS, Mint, TOI, FE), regulatory (MHI/PM E-DRIVE portal, SEBI order via TechCrunch), company statements, VAHAN-derived trackers (EVreporter, Vahan Intelligence), one peer-reviewed airport access study (Kolkata).
- **Key primary documents opened in full:** BS Redseer/Bharat Taxi (May 2026), TOI Bharat Taxi NMIA launch (Jul 2026), ET Evera funding (Mar 2023), ETTravelWorld Uber India 2025 report (Jan 2026), deeparrival NMIA launch, New Indian Express AAI H1 FY27 report (Oct 2026). The AAI Sep-2026 annexure PDF and GMR group blog were blocked from automated access — AAI figures were triangulated via the NIE report and cross-checked arithmetically.
- **Limitations:** (1) The positioning doc itself was not available in this workspace — claims were taken from the research-gap list as written. (2) Public EV-charger counts conflict by an order of magnitude across sources (16k–29k), reflecting directory vs. operational definitions. (4) No platform-internal data (trip lengths, deadhead, price elasticity) is public. (5) VAHAN model-level splits (Xpres-T unit sales) are not retrievable publicly.
- **Confidence codes used below:** ✅ Verified (Grade A/B), 🟡 Partially verified / corrected (Grade C), ❌ Not verified / no public source (Grade D).

---

## Findings

### A. External lynchpins

**1. Evera at Delhi airport — ✅ Verified (with fleet/ownership detail).**
Evera (Prakriti Mobility/E-Mobility, founded 2019) is a Delhi-based all-electric, app-based cab operator. It partnered with DIAL in late 2022 to operate from Terminal 3; in Oct 2026 it began repossessing 500 BluSmart EVs through BluSmart's lenders (220 onboarded, 280 in progress, another 500 planned), enabling expansion to **all IGI terminals**. Fleet: 238 EVs (Mar 2023) → MoU with Tata Motors for 2,000 Xpres-T EVs → ~2,200 electric cabs (2025 industry guide). **Ownership model: asset-light — vehicles are leased (originally fixed monthly rentals; now leased from lenders after repossession), not owned.** Charging: captive charging points plus public infrastructure; airport pick-ups are **55% of total bookings, average trip ~₹600**. Sources: ET (Mar 2023), Business Standard/PTI (Oct 2026), News18, Times of India (Jun 2025), Rediff (Jun 2025), EVJoints guide.

**2. GMR Hyderabad "200+ EV fleet at RGIA" — 🟡 Mischaracterised.**
Two separate facts are being conflated: (a) GHIAL launched a 24/7 premium airport taxi service with a **fleet of 200+ vehicles (sedans and SUVs)** — the news reports do **not** describe these as electric (NewsMeter, Aviation Jeta); (b) RGIA's electric cab operator is **OHM E-Cabs (OHM E Logistics)** — 100 e-cabs deployed at Hyderabad Airport in 2022, since ordering 1,000 Tata Xpres-T and 300 BYD e6, plus 50 BYD e6 financed via Mufin Green Finance. GMR airports do run EVs for their own operations (DIAL: 57 EVs). **The claim as written ("GMR operates 200+ EV fleet") is not supported; fix to "GHIAL operates a 200+ premium taxi fleet; OHM operates the EV fleet at RGIA."**

**3. Bharat Taxi at NMIA — ✅ Verified.**
Launched at Navi Mumbai International Airport on 23 July 2026 by CM Devendra Fadnavis: **600 cabs in phase 1 (target 1,000+)**, cooperative model under Sahakar Taxi Cooperative Ltd (national launch Feb 2026), zero commission, drivers own cabs and receive dividends; fixed fares ₹31 (first 1.5 km) + ₹21/km aligned to Mumbai kaali-peeli rates; cars, autos and bikes on one app; MoU with Late DB Patil Sahakari Vahatuk Sangha to finance 3,000–4,000 project-affected people as driver-owners. Present in Delhi-NCR, Ghaziabad, Gujarat (Ahmedabad, Rajkot, Somnath, Dwarka); ~4 lakh drivers registered (Maharashtra legislative statement) / ~8 lakh in the wider cooperative network. Sources: TOI (Jul 23, 2026), Deep Arrival (Jul 26, 2026), Newsband, ETTravelWorld, Business Standard (May 7, 2026).

**4. BluSmart "assumed 10% residual, realised 26%" — ❌ Not documented.**
No public source — SEBI's interim order (Apr 15, 2025), Gensol/BluSmart disclosures, lender (PFC/IREDA) actions, HC filings, or press coverage — states any assumed or realised residual-value percentage for the EV fleet. **The specific claim should be treated as fabricated unless a document is produced.** What is documented: SEBI found Gensol availed ₹978cr term loans (IREDA ₹510cr + PFC), of which ₹663cr was for 6,400 EVs for BluSmart, but only **4,704 EVs were acquired for ₹568cr (implied ₹12.07 lakh/vehicle)**, leaving a ₹262cr gap; funds were partly diverted to promoter personal use (Gurugram flat). BluSmart (fleet >8,500 EVs) suspended operations Apr 17, 2025; Grant Thornton appointed for forensic audit. Disposition of stranded EVs: Refex's 2,997-EV takeover (₹315cr loan assumption, Jan 2025) fell through Mar 28, 2025; Uber shelved absorbing ~5,000 BluSmart cabs; PFC/IREDA weighed auctioning 5,000+ hypothecated EVs; 1,500–2,000 EVs were put on the block; Delhi HC restrained third-party claims on batches (Orix 175, SMAS/Shefasteq 220, STCI 129 EVs); IREDA filed at Debt Recovery Tribunal for ₹729cr+; Evera repossessed 500. **No per-vehicle resale/auction prices are published — realised residual value remains unmeasurable from public data.**

**5. Uber Black top use cases = airport & corporate — ✅ Verified (Uber's own annual data report).**
Uber India's *How India Ubered 2025* (released Jan 6–7, 2026): Uber Black logged **34+ million km in 2025 across Delhi, Mumbai and Bengaluru, "with airport and corporate commutes ranking among top use cases"** (ETTravelWorld) / "airport and work travel being two of the top use cases" (The Hindu). Note: this is Uber's own PR data release, not third-party market research — but it is the claim's actual source. Supporting: WTi Cabs (largest Uber Black fleet operator) plans to double its premium fleet to 2,000+ cars; premium AOVs +9% vs +3% economy (Deloitte, via FE); riders pay 25–40% premiums for app-owned vehicles with professional drivers.

**6. Platform fee structures — 🟡 Verified with corrections.**
- **Ola: ₹67/day flat fee — ✅ exact.** Nationwide flat-fee model for cabs: drivers keep 100% of earnings after a fixed ₹67 daily access charge (₹2,010/30-day pass), replacing 20–30% commissions (TOI, MediaNama, Inc42, Jun 2025 onward).
- **Rapido: ₹29/day is the top of the auto band, not a cab rate.** Auto/cab "captains" pay a daily login fee of **₹9–29/day (autos; ~₹19 typical per co-founder Pavan Guntupalli, Jan 2025); cabs ₹40/day or ₹500/month** (Inc42). Zero commission beyond the fee.
- **Uber: NOT a flat ₹29/day platform.** Uber has stayed on the traditional commission model (historically ~20–30%); it is piloting subscription options — 'Driver Pass' at ₹341/72 hours, and reported fixed fees of ₹120–140/day in some cities — while continuing commissions elsewhere (TOI/ET, MediaNama).
**Correction for the deck:** "Uber+Rapido ₹29/day" is wrong as stated; use Ola ₹67/day, Rapido ₹9–29/day (auto) and ₹40/day/₹500-month (cab), Uber commission-based with pilots.

### B. Market size and demand

**7. Redseer ~3B trips CY2025 — ✅ Consistent (indirect).**
Business Standard (May 7, 2026), quoting Redseer associate partner Saurav Chachan: **Delhi NCR = 16–18% of the market in trips ≈ 500M trips = one-sixth of the market** in CY25 → implies **~2.8–3.1B total trips CY25**. Corroborating scale: Deloitte (Rajat Mahajan, via FE): **~2.4B rides completed in 2024**, ride-hailing GMV ~$7B; Redseer Feb 2026 report: 2025 ride-volume growth of +55% (2W), +50% (autos), +36% (cabs). Definition note: "trip" = platform ride across all modes; three-player market (Rapido, Uber, Ola hold 70–80% GMV).

**8. Cab-only ~810M — 🟡 Plausible, derived not published.**
Redseer: **cabs = 27% of the ride-hailing "pie" in trips nationally (vs 45% in Delhi NCR)**; by **GMV, cabs = 50–55%, autos ~35%, 2W ~10–12%**. 27% × ~3.0B ≈ 810M cab trips — arithmetically consistent, but Redseer has not published the absolute cab-trip number itself. Cite as "27% of trips (Redseer CY25), applied to ~3.0B total."

**9. Motilal Oswal 840k/460k/320k — ✅ Verified.**
Business Standard (Apr 18, 2025, BluSmart-exit analysis), citing Motilal Oswal data **published January 2025**: **Uber 840,000 average daily cab rides; Ola 460,000; Rapido 320,000** (four-wheeler cab market); MAUs: Uber 33.6M, Rapido 31.8M, Ola 28.6M. Financial Express cites the same. Scope/period: cab-segment daily averages, data published Jan 2025. Caveat for recency: by Mar 2026 (Sensor Tower/Livemint), Rapido averaged ~6.5M total daily rides across all modes vs Uber ~3.7M and Ola ~1.5M — a different (all-mode, newer) measure; the MO figures remain the correct citation for cab-only.

**10. AAI 196.24M (Apr–Sep 2026) — ✅ Verified and reconciled.**
AAI's half-yearly Air Traffic Report (released Oct 28, 2026, per New Indian Express): **domestic 159,544,222 passengers (−1.9% YoY); international −7.1%; overall −2.9%**. Implied international ≈ 36.7M → **total ≈ 196.2M, matching 196.24M**. Sep 2026 alone: 30,099,806 total (−5.9%); international 6,103,919 (−4.2%). Airport-level: Delhi domestic 28.13M (+6.2%), Delhi international 10.38M (+2%); Hyderabad −12.8%, Mumbai −9.5%, Chennai −11.8% domestic. **Definitions:** AAI counts passengers handled per airport across 51 airports (each journey leg counted at both origin and destination airport — totals are not unique travellers); domestic + international, arrivals + departures. The AAI Sep-2026 annexure PDF itself was inaccessible to automated access — verify the exact 196.24M against the PDF (Sep2k26Annex3.pdf) when manually available.

**11. Airport passenger → road-transport eligible share — 🟡 Partial (no national figure).**
Best public evidence: a peer-reviewed access-mode study at Kolkata NSCBI airport (Taylor & Francis, 2025): **38.66% of access trips by private 4-wheelers; 60.12% by paratransit (ride-sourcing, yellow taxis, multimodal public transport); >50% of passengers willing to switch to metro** where it exists. Counterpoint: Nagpur's Airport Metro station ridership is only in the hundreds daily — metro capture is city-specific. **No all-India road-transport eligibility share exists; keep it an explicit assumption in the model.**

**12. App-cab mode share at Indian airports — 🟡 No published share; strong proxies.**
No airport operator or platform publishes mode share. Verified proxies: **Rapido: 12–15% of its total cab rides across India are airport rides**; **Evera: airport pick-ups = 55% of total bookings**; **Uber: ~40% of Uber Reserve trips end at airports; ~1 in 4 airport drop-offs occur via Reserve; Reserve grew ~200% YoY**; Delhi T3 sees **~700,000 monthly passengers potentially served and ~100,000 app-based cab operations/month** (Uber Share launch data). DGCA: domestic air passengers 161.3M in 2024 (+6.12%). The deck's 20–30% mode share must be labelled an assumption, though its order of magnitude is not contradicted by any source.

**13. Average occupancy of app-cabs at airports — ❌ No measured data.**
Only informal guesstimates exist (e.g., 2 passengers/airport cab in Medium-style estimates; Uber Share/QuicReach shared-cab products cap at 3 passengers). No platform or airport study publishes passengers-per-booked-vehicle. Requires primary research (driver surveys/counter surveys).

**14. Offline taxi volume — 🟡 Partial city data only.**
Mumbai: **~40,000+ kaali-peeli (black-and-yellow) taxis** (Times Now, 2025); radio taxi Mega Cabs ~2,500 cars; Meru legacy fleet history (9,000 cabs at 2015 peak). No national non-platform taxi trip volume is published; state transport department aggregation would be needed.

**15. Inter-city ride-hailing volume — 🟡 No share figure; directional evidence.**
Uber Intercity's top routes are published (Mumbai–Pune, Delhi–Agra, Bengaluru–Mysuru, Lucknow–Kanpur, Ahmedabad–Vadodara; longest logged trip Gurgaon–Ahmedabad 1,827 km), and Uber calls Intercity demand "exceptional," but neither Uber, Ola, nor Rapido publishes intercity share of trips. A 2016-era estimate put the intercity cab market at $4–6B (dated, Meru CEO). Redseer's mode-split data does not break out intercity. Gap remains.

### C. Segment operating data (items 16–21)

**Status: ❌ the full p3 table has no public source.** No platform, consultancy, or government body publishes per-segment trip length, km/day, trips/day, fare, growth, EV share, or price-sensitivity coefficients by use case. What can be anchored:

| Deck metric | Closest verified public anchor |
|---|---|
| Trips/day (intra-city ~7.5) | Redseer: metro drivers ~**8 trips/day**, 220–240 trips/month, ~25 working days |
| ₹/trip (₹350–₹600 range) | Redseer: avg fares **₹300–400** in top-7 cities, ₹200–250 in smaller cities; **Evera airport trips ~₹600** |
| Km/day (176–210 corporate/airport) | Lithium Urban corporate EVs: **~300 km/day**, 10–12h shifts (Mint interview); high-utilisation taxi EVs 50,000+ km/yr (≈137 km/day average floor) |
| Premium segment | Uber Black 34M km in 2025; premium AOV +9% vs +3% economy; riders pay 25–40% premium for app-owned fleets (Deloitte/FE); WTi doubling Uber Black fleet to 2,000+ |
| EV share by segment | Not published anywhere. Only aggregate: Uber EVs = 365M km of 11.6B km (3.1% of km); EV share of new 4W registrations 7.3–8.7% (Oct 2026); Delhi 4W EV registration share 12.95% (Apr 2026); Delhi e-cab registrations up 15-fold in 5 years (ThePrint) |
| Growth by segment | Redseer (CY25 vs CY24): 2W +55%, autos +50%, cabs +36% (mode-level, not use-case-level) |
| Price-sensitivity coefficients (0.85/0.90/0.35/0.40/0.30) | ❌ No source. Not published by any Indian platform or consultancy |
| Item 19 conflict (420 vs 340 km/day inter-city) | Unresolvable publicly: 280 km × 1.5 trips = 420 km paid km/day; 340 implies deadhead/repositioning haircut. Flag as internal assumption; no external data |
| Item 21 (61%/~58% intra-city share) | ❌ No trip-purpose classification is public. Possible conflation: Rapido's claimed **61% bike-taxi market share** (Sanka via Inc42/Equentis) |

**Recommendation:** downgrade all item 16–21 values to Grade D (assumption) in the report, keep the verified anchors above as separate "market context" citations, and commission driver surveys / platform partnerships for the rest.

### D. Fleet and buyer data

**22. Fleet operator sizes — ✅ Verified.**

| Operator | Verified scale | Model / notes | Source date |
|---|---|---|---|
| Everest Fleet (Mumbai) | **18,500+ vehicles** across 7 cities (Uber's largest India fleet partner; top-3 globally); 15,000 CNG + 1,500 EV (mid-2024); target 10,000 EVs by 2026 | Fleet management for Uber & Ola; $50M Series C led by Uber (Sept 2024); Axis Bank ₹1bn (GuarantCo-guaranteed) EV loan | Sep 2024 |
| Lithium Urban (Bengaluru) | **3,000+ vehicles, 1,300 chargers, 25,000 trips/day, 100+ enterprise clients** (19 cities; clients incl. Google, Accenture, Uber) | B2B corporate employee transport; acquired by Eversource (2022); JSW Green Mobility strategic investment | 2025 |
| Evera (Delhi) | **~2,200 EVs + 500 repossessed BluSmart EVs** (Oct 2026; another 500 planned) | Airport-focused (55% of bookings); leased assets | 2025–26 |
| Refex eVeelz (Chennai) | **1,000+ electric cars** plying (Jan 2025); operates Chennai, Bengaluru, Hyderabad, Mumbai, Pune; Uber partnership (1,000 EVs by 2026) | Leasing; Gensol 2,997-EV deal collapsed Mar 2025 | Jan 2025 |
| eee-Taxi | **~1,000 EVs** (Delhi-NCR & Hyderabad; Shell-backed; corporate ETS focus) | B2B | 2025 |
| OHM E-Cabs (Hyderabad) | **100 EVs at RGIA (2022) → ordered 1,000 Xpres-T + 300 BYD e6; 50 BYD e6 added via Mufin finance** | Airport + intra-city, Hyderabad | 2022–24 |
| Snap-E Cabs (Kolkata) | **600 EVs**; agreements with WB airports & railway stations | Owned fleet model | 2023 |
| GMR/GHIAL | 200+ premium airport taxis (not EV-documented); DIAL 57 EVs (own ops) | Airport operator | 2022–25 |
| Bharat Taxi | 600 cabs phase-1 MMR (target 1,000+); ~4 lakh registered nationally | Driver-owned cooperative | Jul 2026 |
| WTi Cabs | Largest Uber Black operator; doubling to **2,000+ premium cars** | Premium fleet | 2025 |
| Meru/Alyte (Mahindra Logistics) | Alyte Privé = electric XUV400 airport transfers; Alyte Select sedans/SUVs in 6 cities; 98% fulfilment claimed | Premium B2C/B2B | Aug 2026 (FE) |

**23. Ola Fleet (GCabs) — ✅ Verified.**
Ola acquired radio-taxi company **GCabs in January 2015**, renaming it Ola Fleet Technologies (leases cabs to driver-partners). FY23: revenue **₹189.9cr (−57% YoY)**, loss **₹387.6cr** (per RoC filings via Entrackr/NewsBytes) — a shrinking business, no current fleet count disclosed.

**24. Maruti Dzire Tour S fleet pricing — ✅ Verified exactly.**
New-gen Dzire Tour S launched for fleet operators at **₹6.79 lakh (petrol) / ₹7.74 lakh (CNG), ex-showroom Delhi**, LXi-based, Arctic White only, 6 airbags standard, sold via Arena/commercial dealerships alongside Tour M (Ertiga) and Tour H3 (WagonR). It is the only ICE fleet sedan on sale (Hyundai no longer sells a fleet Aura; Tata's rival is the Xpres-T EV). Price hikes since launch: up to ₹10,000 by variant (2025). Sources: Autocar India, CarDekho, 91Wheels, IndiaCarNews (2025).

**25. Tata Xpres-T pricing and volumes — ✅ Pricing verified; ❌ unit volumes not public.**
Launch price ₹9.54 lakh (2021); Feb 2023 Tata–Uber deal: 25,000 Xpres-Ts to Uber fleet partners across 7 cities, priced **₹13.04–14.98 lakh ex-showroom Delhi** (315-km variant ₹14.98L incl. FAME subsidy ₹2.6L); 2022 base ~₹10.58 lakh; BluSmart ordered 10,000 Xpres-Ts (2022, ~₹1,058cr order value). Demand signal: Tata's Xpres-T **order book exceeded 40,000 units** (2023), with fleet sales forecast at 12–15% of Tata's EV volume. Model-level VAHAN sales splits are not published — OEM-level only (Tata PEM led with 8,494 EV registrations in Apr 2026, +77.8% YoY).

**26. Mahindra eVerito — ✅ Verified (historical/discontinued).**
India's first electric sedan (2016); fleet-operator pricing started **₹9.13–9.46 lakh** (per 91Wheels; earlier fleet price ₹10.71L vs ₹12.70L for individuals); 72V motor, ~110–140 km real-world range; adopted by BluSmart (first 70 cars), Meru/Mahindra Hyderabad pilot, Ministry of Finance fleet. **Discontinued in 2023** (unable to meet current safety/crash norms). Mahindra's current fleet-EV play is via Alyte (XUV400) rather than a sedan.

**27. BluSmart 4,704 stranded EVs — ✅ Verified (numbers), ❌ residual values.**
See item 4. Confirmed: 4,704 EVs acquired for ₹568cr against a ₹663cr loan for 6,400; BluSmart fleet >8,500 EVs at suspension (Apr 17, 2025); lenders (PFC, IREDA) and ~10+ lessors (Orix, SMAS Auto, Shefasteq, STCI, etc.) pursued recovery via HC suits, DRT (IREDA ₹729cr), and block sales of 1,500–2,000 EVs; Evera repossessed 500 (Oct 2026), plans 500 more; Refex 2,997-EV deal cancelled; Uber shelved ~5,000-EV absorption. **Who bought them at what price: not published.**

**28. Fleet procurement behaviour — 🟡 Inferred from transactions (no interviews).**
Consistent pattern across all documented deals: (a) **asset-light leasing/financing, not outright purchase** (Evera leases from lenders with fixed rentals; Lithium owns captive fleets for B2B only; OHM uses Mufin finance; Everest uses bank debt + OEM/platform partnerships); (b) **bulk OEM orders channelled via platform partnerships** (Tata–Uber 25,000; Tata–BluSmart 10,000; Uber–Everest/Lithium/Moove/Refex); (c) **Uber co-invests in fleet partners** ($20M+$30M into Everest); (d) **repossessed assets are now a procurement channel** (Evera–lender deals post-BluSmart); (e) **financing partners**: Axis Bank/GuarantCo, Mufin Green, Arka Credit Fund, SMAS, Orix. Batch sizes: 500–25,000 units. Buying authority sits with fleet-operator founders/CEOs (Trivedi, Ladsariya statements). Primary interviews still required for replacement rates and decision criteria.

### E. Charging and infrastructure

**29. Depot charging at airports — 🟡 Partial; captive is the norm.**
Delhi: DIAL has **12 charging stations / 22 points** across the airport "for passengers, employees and cab service providers" (2022); BluSmart built its own super-hubs in Delhi-NCR (~500+ charging points network-wide); Mumbai: Tata Power's **Leela Mega Charger near CSI T2 — 16 guns / 600 kW, 16 simultaneous EVs — explicitly targeting taxis, ride-hailing fleets**; NMIA is developing on-site EV charging infrastructure (Oct 2026). **No airport operator offers general depot charging to third-party fleets** — operators build captive hubs (Evera: captive + public). Access rights, power tariffs, and bay counts per terminal are not published.

**30. Airport access/parking charges for commercial vehicles — ✅ Verified (Delhi).**
DIAL charges app-cabs a **mandatory ₹290 pick-up fee per airport trip** (levied via aggregators under contractual parking arrangements; Uber confirms it is passed through to the airport), **recently increased ~40%**, making it "among the costliest in the country"; toll + pick-up fee ≈ 50% of average short-distance fare. History: ₹150 commercial-vehicle entry fee at T3 from Oct 2015 (radio taxis exempt), extended to T1 (₹150, 2016); aggregators pay DIAL "crores annually" for reserved arrival-zone parking. Mumbai/Bengaluru/Hyderabad fee schedules not published in accessible sources — collect from operator fee schedules.

**31. Highway charging density — 🟡 Partial.**
Tata Power (largest CPO): **6,700+ public & captive charging points across 690+ cities, plus 2.5 lakh home chargers; target 10,000 public points by 2030**; its 10 co-branded TATA.ev Mega Charger hubs (25 fast chargers, 56 guns, 2.7 MW; 70,000+ sessions) line the Yamuna Expressway (4 hubs), Hyderabad–Vijayawada (3), Bengaluru–Tirupati, and Pune–Bengaluru corridors. Government expressway program places fast chargers **every 25–40 km on major corridors** (Pulse Energy summary). Reliability/utilisation data on inter-city routes is not published.

**32. Urban charging density (top 8 cities) — 🟡 Low confidence; sources conflict.**
India total: **16,000+ public stations (Pulse Energy, mid-2026)** to **27,000–29,000 (Electreefi directory incl. ~22,750 operational)**. City counts range widely by source: Delhi 1,700+ (directory) to 3,800+ (blog); Bengaluru 831–2,200; Mumbai 461–2,400; Hyderabad 190–1,250; Chennai 112–1,400; Pune 446–1,700; Ahmedabad 101–900; Kolkata 57–750. Delhi has the highest density (~1 charger per 3 km² per one directory). Maharashtra has the largest state network (~4,800+); Karnataka the largest counted network per another. **Use as order-of-magnitude only; DISCOM/CPO primary data required.**

### F. Regulatory and policy

**33. FAME II / PM E-DRIVE — ✅ Verified (as of Nov 2026).**
FAME II ended Sep 2024; PM E-DRIVE (gazette S.O. 4259(E), Sep 29, 2024) launched Oct 1, 2024 with ₹10,900cr, **enhanced to ₹11,900cr and extended to Mar 31, 2028** (S.O. 4424(E), Aug 10, 2026). Segment status: **e-3W (L5) closed Dec 26, 2025**; **e-2W support ended 2026** (₹5,000/vehicle cap; sources differ between Mar 31 and Jul 31, 2026 — govt has ruled out extension); e-buses (14,028, ₹4,391cr), e-trucks, e-ambulances and **charging infra (₹2,000cr)** continue to Mar 2028. **Electric four-wheelers are excluded from PM E-DRIVE entirely — no central purchase subsidy for e-cars since FY25** (parliamentary panel recommendation to reinstate 4W subsidies has not been accepted). ~22.12 lakh vehicles supported by early 2026 (19.19 lakh 2W + 2.93 lakh 3W).

**34. GST on EVs vs ICE — ✅ Verified, deck needs correction.**
**EVs: 5% GST, zero compensation cess** (EV chargers also reduced to 5%). **ICE cars: 28% GST + 1–22% cess — not 18%**: small petrol (≤1,200cc, ≤4m) 28%+1% = 29%; small diesel 31%; mid-size sedans 43%; large petrol 45–50%; SUVs up to 50%. Hybrids: 28% + 15–22% cess. (18% appears only in the used-car margin scheme for large vehicles.) **The EV tax advantage over a fleet CNG/petrol sedan is roughly 24–38 percentage points, not 13.**

**35. State-level EV policies — 🟡 Matrix compiled (confirm before use).**
Delhi: 100% road-tax & registration exemption, 23,000 public charge points planned, home-charger subsidies ₹6,000–10,000. UP: 100% road-tax exemption (limited to UP-made EVs since Oct 2025); 20% capital subsidy on charging. Haryana: 100% road-tax + toll exemption; 25% charging subsidy. Karnataka: tiered lifetime tax by price band since Apr 2026; ~25% charging-equipment subsidy; night charging 30% cheaper. Maharashtra: purchase incentives & road-tax concessions; charging every 25 km on state highways; 25% commercial charging subsidy. Telangana: 100% road-tax exemption until Dec 2026; concessional EV-park land. Tamil Nadu: 100% waiver (to Dec 2025 — confirm current); no licence for public charging. Gujarat: 1% reduced rate (to Mar 2026 — confirm); 25% subsidy + electricity-duty exemption. West Bengal: exemption + SGST reimbursement.

**36. Maharashtra road tax on CNG (14%) — ✅ Verified with important nuance.**
Maharashtra Motor Vehicles Tax (Amendment) Act, 2025, **effective July 1, 2025**: petrol cars 11%/12%/13% by price band; diesel 13%/14%/15%; **CNG/LPG individually-registered: 8%/9%/10% (up 1pp from 7/8/9)**; **CNG cars registered in a company/fleet (non-individual) name: 14%/16%/18%**; statutory maximum one-time tax raised ₹20L → ₹30L. **So the deck's "14% CNG" is correct specifically for fleet/company-registered CNG vehicles under ₹10 lakh** — individual buyers pay 8–10%. The EV-vs-CNG road-tax gap for fleet buyers is therefore real (EVs exempt vs 14% company CNG).

### G. Competitor and industry data

**37. Ola (ANI Technologies) — ✅ FY23 verified; newer data available.**
FY23 consolidated: revenue **₹2,799.3cr (+42% YoY)**, loss ₹772.2cr (ride-hailing alone: ₹1,987.5cr revenue, ₹1,082.5cr loss). Update: **FY25: revenue ₹1,170.9cr (−42%), loss ₹662.4cr** (from ₹328.7cr in FY24); standalone loss ₹697.6cr; net worth nearly halved to ₹2,025cr; Moody's downgraded ANI to Caa1 (Nov 2025); board approved IPO preparations. Market share: Ola described by MO (Jan 2025) as #2 in cabs (460k daily rides) but losing share to Rapido/Uber.

**38. Rapido — ✅ FY24 verified; newer data available.**
FY24: operating revenue **₹648cr (+46.3%)**, loss ₹371cr (−45%); revenue mix FY24: auto/cab/bike platform income ₹362cr net (₹505cr gross), delivery ₹265cr. **FY25: ₹934cr (+44%), loss ₹258cr; delivery (₹340cr) now exceeds ride commissions (₹277cr)**; valuation path: $1.1B (Sep 2024) → **$2.82B post-Series F ($730M round)**; Swiggy and TVS exited (2025). Scale: 82M MAU (Mar–May 2026), ~6.5M daily rides all-modes (Mar 2026); 70%+ claimed bike-taxi share, ~40% auto share, 14–22% cab share (contested); ₹9–29/day auto, ₹40/day/₹500-month cab subscription; projected profitability in FY26.

**39. Uber India — ✅ Verified (multi-year).**
FY23: revenue ₹2,666cr, loss ₹311cr (ride-hailing revenue ₹678.6cr). **FY25: total operating revenue ₹3,849cr (+2.3%), consolidated loss ₹1,512cr (from ₹89cr)**; ride-hailing gross revenue (commissions) flat at ₹2,604cr but net revenue fell 89% to ₹88cr because **driver incentives/discounts rose 33% to ₹2,516cr**; ride-hailing segment loss ₹1,407cr. Operations: 220+ cities; India = Uber's 3rd-largest market by trips; 2025: 11.6B km (+26.5%), 365M EV km, 800k Shuttle first-time users; Uber B.V. injected **₹2,921cr into Uber India Systems (Nov 2025–Jan 2026)**; Uber–Rapido merger talks collapsed over control (mid-2026).

**40. Tata Xpres-T EV sales/adoption — 🟡 Orders verified; ❌ registration volumes not public.**
See item 25. Corroborating adoption: Uber–Tata 25,000-unit MoU; BluSmart 10,000; OHM 1,000; Snap-E 400; order book 40,000+ (2023). VAHAN model-level splits are not published; Tata PEM remains India's largest EV OEM (8,494 registrations Apr 2026) with fleet as a stated 12–15% share target.

**41. EV registration trends (VAHAN) — ✅ Verified.**
FY2025-26: **~200,000 e-4W registrations (+80% YoY)**; Apr–Oct 2025: 119,332 e-cars (+105% YoY), surpassing all of FY25 (117,072). **EV share of 4W registrations: crossed 5% nationally in Apr 2026; 7.3–8.7% by Sep–Oct 2026** (retreat from Sep peak); city outliers: Delhi 12.95%, Chandigarh 13.06% (Apr 2026). Top state: Maharashtra (20,098 units Apr–Oct 2025, 16.8%), then Karnataka, Kerala. OEMs: Tata, MG (JSW), Mahindra top-3; Tata's share compressing (~81% combined for top-3 vs 94% earlier). Registered EV base: 16.81 lakh (FY24) → 19.68 lakh (FY25). Context: CNG crossed 22.7% of new PV registrations (Apr 2026), overtaking diesel — CNG remains the fleet fuel to beat. Total EV sales Nov 2025–Oct 2026: 33.33 lakh (all segments).

---

## Source Notes

| Source | Credibility | Last updated |
|---|---|---|
| [Business Standard — Bharat Taxi / Redseer CY25 trip data](https://www.business-standard.com/industry/auto/riding-the-bharat-wave-govt-backed-taxi-app-bets-on-cooperative-muscle-126050601589_1.html) | 4/5 | 7 May 2026 |
| [Times of India — Ola ₹67/day flat-fee; Redseer GMV split, fares, trips/day](https://timesofindia.indiatimes.com/business/india-business/as-commissions-fall-indias-ride-hailing-firms-test-viability-of-flat-fee-economics/articleshow/122029891.cms) | 4/5 | - |
| [Business Standard — Motilal Oswal daily cab rides (840k/460k/320k)](https://www.business-standard.com/companies/start-ups/blusmarts-shock-exit-leaves-indias-green-mobility-market-up-for-grabs-125041800827_1.html) | 4/5 | 18 Apr 2025 |
| [Financial Express — MO figures; premium segment; Deloitte GMV ~$7B, 2.4B rides](https://www.financialexpress.com/business/industry/for-private-amp-government-urban-mobility-is-the-ride-to-book/4021665/) | 4/5 | Aug 2026 |
| [New Indian Express — AAI Apr–Sep 2026 traffic report](https://www.newindianexpress.com/india/2026/Oct/29/delhi-vijayawada-buck-trend-as-indias-international-air-traffic-falls-71) | 4/5 | 29 Oct 2026 |
| [AAI Traffic News (primary PDFs)](https://www.aai.aero/en/business-opportunities/aai-traffic-news) | 5/5 | Sep 2026 |
| [ET — Evera $7M funding; 238 EVs; lease model; charging](https://economictimes.indiatimes.com/tech/funding/ev-cab-company-evera-raises-7-million-in-funding-led-by-ieg-investment/articleshow/98340521.cms) | 4/5 | 2 Mar 2023 |
| [Business Standard/PTI — Evera repossesses 500 BluSmart EVs, all-terminal expansion](https://www.business-standard.com/companies/start-ups/evera-cabs-initiates-repossession-of-blusmart-operated-500-electric-cabs-125050500749_1.html) | 4/5 | 2 Oct 2026 |
| [Times of India — Evera takes over BluSmart cabs; BluSmart fleet >8,500; Uber shelved 5,000-EV plan](https://timesofindia.indiatimes.com/business/india-business/evera-takes-over-some-blusmart-cabs-drivers/articleshow/120913796.cms) | 4/5 | Jun 2025 (approx.) |
| [Rediff — airport cab war: Evera 55% airport bookings, ₹600/trip; Rapido 12–15% airport rides; Uber Reserve stats](https://www.rediff.com/business/report/auto-cab-wars-heat-up-at-airports-post-blusmart-exit/20250619.htm) | 3/5 | 19 Jun 2025 |
| [TechCrunch — SEBI interim order details (₹978cr loans, 6,400 vs 4,704 EVs, ₹568cr)](https://techcrunch.com/2025/04/15/indian-ride-hailing-startup-blusmart-swept-up-in-gensol-investigation-alleging-misuse-of-ev-loans/) | 4/5 | 15 Apr 2025 |
| [Times of India — BluSmart EV sell-off (1,500–2,000 EVs); Refex deal collapse](https://timesofindia.indiatimes.com/business/india-business/blusmart-collapse-sparks-ev-sell-off-lenders-race-to-recover-dues-by-offloading-1500-2000-vehicles/articleshow/121210695.cms) | 4/5 | Jun 2025 (approx.) |
| [ET — PFC/IREDA mull Gensol EV auctions](https://economictimes.indiatimes.com/industry/renewables/pfc-ireda-mull-sale-of-gensol-evs-to-secure-loans/articleshow/120463025.cms) | 4/5 | May 2025 (approx.) |
| [ET topic — IREDA DRT ₹729cr; HC orders (Orix/SMAS/STCI batches)](https://economictimes.indiatimes.com/topic/gensol-npa-status) | 3/5 | 2025–26 |
| [ETTravelWorld — Uber India 2025 report (Uber Black airport/corporate use cases)](https://travel.economictimes.indiatimes.com/news/research-and-reflecting-indias-expanding-ridesharing-revolution/126390107) | 4/5 | 7 Jan 2026 |
| [The Hindu — How India Ubered 2025 (11.6B km, 365M EV km)](https://www.thehindu.com/sci-tech/technology/how-indians-ubered-in-2025-kochi-rated-the-best-mumbai-preferred-late-night-trips/article70477339.ece) | 4/5 | 6 Jan 2026 |
| [Times of India — Bharat Taxi NMIA launch (600 cabs, fares, MoU)](https://timesofindia.indiatimes.com/city/mumbai/fadnavis-flags-off-bharat-taxi-service-at-navi-mumbai-airport/articleshow/132588649.cms) | 4/5 | 23 Jul 2026 |
| [Deep Arrival — Bharat Taxi NMIA launch detail](https://deeparrival.com/news/bharat-taxi-navi-mumbai-airport-launch-july-2026/) | 3/5 | 26 Jul 2026 |
| [NewsMeter — GHIAL 24/7 premium taxi, 200+ vehicles](https://newsmeter.in/hyderabad/hyderabad-airport-launches-24x7-premium-taxi-service-for-passengers-772251) | 3/5 | - |
| [EVJoints — electric cab operators guide (Evera ~2,200 EVs; OHM 100→1,300; eee-Taxi 1,000; Snap-E 600)](https://evjoints.com/ev-guide/top-5-electric-cab-service-companies-in-india/) | 3/5 | 2025 |
| [ET — Everest Fleet $30M from Uber; 18,500+ vehicles, 7 cities](https://economictimes.indiatimes.com/tech/funding/fleet-operator-everest-fleet-raises-30-million-from-uber-india/articleshow/113530618.cms) | 4/5 | Sep 2024 |
| [VCCircle — JSW Green Mobility invests in Lithium (3,000 vehicles, 1,300 chargers, 25k trips/day)](https://www.vccircle.com/jswgreen-mobility-invests-in-eversource-capital-backed-ev-platform) | 4/5 | 2025 |
| [ET EnergyWorld — Refex–Gensol 2,997 EVs, ₹315cr tie-up](https://energy.economictimes.indiatimes.com/news/power/refex-green-mobility-to-acquire-2997-evs-from-gensol-in-315-crore-deal/117282751) | 4/5 | Jan 2025 |
| [MediaNama — Ola ₹2,010/30-day cab subscription; Uber Driver Pass ₹341/72h; Rapido ₹9–29](https://www.medianama.com/2026/02/223-bharat-taxi-vs-ride-hailing-platforms-pays-drivers-better/) | 3/5 | Feb 2026 |
| [The Hindu — Rapido ₹19/day auto login fee (co-founder)](https://www.thehindu.com/sci-tech/technology/swiggy-backed-rapido-says-it-plans-to-launch-shuttle-service-in-bengaluru/article69119173.ece) | 4/5 | 20 Jan 2025 |
| [Inc42 — Rapido at 10 (cab fee ₹40/day or ₹500/month; 61% bike-taxi share claim)](https://inc42.com/startups/rapido-10-years-decade-1000-cr-revenue-club/) | 3/5 | 2025 |
| [Livemint — Rapido 4W push (MO figures via Equentis; FY24 ₹648cr)](https://www.livemint.com/companies/news/rapido-four-wheeler-expansion-rapido-market-share-india-ola-uber-competition-india-rapido-subscription-model-rapido-11746581232668.html) | 4/5 | May 2025 (approx.) |
| [Livemint — Rapido MAU/rides (6.5M/day vs Uber 3.7M, Ola 1.5M)](https://www.livemint.com/companies/rapido-has-more-users-than-uber-and-ola-swiggy-zomato-zepto-blinkit/amp-11783344546641.html) | 4/5 | 2026 |
| [NDTV Profit / Entrackr — ANI FY23 ₹2,799.3cr, ₹772cr loss](https://www.ndtvprofit.com/business/ola-reports-rs-2800-crore-revenue-in-fy23-loss-narrows-nearly-50) | 4/5 | Jan 2024 |
| [CNBC-TV18/PTI — ANI FY25 ₹1,170.9cr, ₹662.4cr loss](https://www.cnbctv18.com/market/ola-cabs-loss-widens-to-%E2%82%B9662-4-crore-in-fy25-ws-l-19902280.htm) | 4/5 | 8 May 2026 |
| [Entrackr — Rapido FY24 ₹648cr, ₹371cr loss](https://entrackr.com/fintrackr/rapidos-operating-revenue-nears-rs-650-cr-in-fy24-cuts-losses-by-45-7576868) | 4/5 | 2024 |
| [Entrackr — Uber India FY25 (₹2,604cr gross, ₹88cr net, ₹1,512cr loss)](https://entrackr.com/analysis/uber-indias-ride-hailing-losses-soar-4x-to-rs-1407-cr-in-fy25-with-flat-gross-revenue-11102472) | 4/5 | 2026 |
| [Analytics Insight — Uber India FY25, ₹2,921cr infusion, Rapido $3B](https://www.analyticsinsight.net/news/uber-rapido-india-merger-talks-reportedly-collapsed-over-control-dispute) | 3/5 | 2026 |
| [Storyboard18 — Rapido Series F, $2.82B valuation, FY25 ₹934cr](https://www.storyboard18.com/brand-marketing/fresh-funding-takes-rapido-to-2-82-billion-valuation-westbridge-prosus-hold-56-report-100108.htm) | 3/5 | 2026 |
| [Autocar India — Dzire Tour S launch pricing (₹6.79L/₹7.74L)](https://www.autocarindia.com/car-news/new-maruti-suzuki-dzire-tour-s-launched-at-rs-651-lakh-427283) | 4/5 | 2025 |
| [CarDekho — Dzire Tour S fleet pricing ₹6.79–7.74L](https://www.cardekho.com/india-car-news/new-maruti-dzire-now-available-for-fleet-operators-priced-from-rs-679-lakh-34213.htm) | 4/5 | 2025 |
| [Mint — Tata–Uber 25,000 Xpres-T deal, ₹13.04–14.98L pricing](https://www.livemint.com/auto-news/tata-motors-partners-with-uber-25-000-xpres-t-electric-sedans-to-join-fleet-11676882162269.html) | 4/5 | Feb 2023 |
| [Autocar India — Xpres-T order book 40,000+, fleet 12–15% of Tata EV target](https://www.autocarindia.com/car-news/tata-motors-aims-to-double-ev-fleet-sales-in-2023-429340) | 4/5 | 2023 |
| [91Wheels — eVerito discontinued 2023, ₹9.13–9.46L](https://www.91wheels.com/cars/mahindra/everito) | 3/5 | 2023 |
| [ET — DIAL ₹290 pick-up fee, 40% hike](https://timesofindia.indiatimes.com/city/delhi/igia-increases-pickup-fee-for-app-based-cabs/articleshow/121006469.cms) | 4/5 | 2025 |
| [Daily Pioneer — Delhi airport ₹290 mandatory pick-up charge detail](https://dailypioneer.com/news/convenience-or-compulsion-the-rising-cost-of-cabs-at-delhi-airport) | 3/5 | 2025–26 |
| [Delhi Airport (DIAL) — 57 EVs, 12 charging stations/22 points](https://site.newdelhiairport.in/blog/aiming-at-net-zero-emissions-delhi-airport-deploys-largest-ev-program-in-indian-airport) | 4/5 | Oct 2022 |
| [Fortune India — Tata Power mega hubs, 6,700+ points, corridor list](https://www.fortuneindia.com/auto/tata-power-tataev-clock-70000-ev-charging-sessions-across-10-hubs-network-adds-27-mw-capacity/158485) | 4/5 | 10 Sep 2026 |
| [Electreefi — city charger counts, state EV policy matrix](https://electreefi.com/ev-charging-in-india/) | 2/5 | 2026 |
| [Pulse Energy — 16,000+ public charging stations (mid-2026)](https://pulseenergy.io/blog/how-many-ev-charging-stations-are-in-india-the-2026-landscape) | 2/5 | mid-2026 |
| [PM E-DRIVE portal (MHI) — scheme status, ₹11,900cr, Mar 2028, L5 closed](https://pmedrive.heavyindustries.gov.in/) | 5/5 | Aug 2026 |
| [ETAuto — govt rules out e2W/e3W subsidy extension; 4W excluded FY26](https://auto.economictimes.indiatimes.com/news/industry/government-rules-out-extension-of-electric-vehicle-subsidies/125268595) | 4/5 | Nov 2026 (approx.) |
| [Team-BHP — Maharashtra motor vehicle tax hike from 1 Jul 2025](https://www.team-bhp.com/news/maharashtra-hikes-motor-vehicle-tax-july-1-2025) | 3/5 | Jul 2025 |
| [Aditya Birla Capital — Maharashtra road-tax slabs (CNG company-registered 14/16/18%)](https://www.adityabirlacapital.com/abc-of-money/maharashtra-road-tax) | 3/5 | 2025–26 |
| [Legal Suvidha / Motozite — GST slabs on cars and EVs](https://legalsuvidha.com/blog/gst-on-cars-vehicles-india-2025) | 3/5 | 2026 |
| [EVreporter — e-car registrations FY26 (119,332 Apr–Oct 2025; VAHAN)](https://evreporter.com/indias-electric-car-sales-zoom-past-the-100000-mark-in-the-current-fy-2025-26/) | 4/5 | Nov 2025 |
| [EVreporter — monthly EV trend Oct 2026 (4W penetration 7.3%)](https://evreporter.com/indias-electric-vehicle-sales-trend-october-2026/) | 4/5 | Nov 2026 |
| [Vahan Intelligence — Apr 2026 EV share >5%, Delhi 12.95%, CNG 22.7%](https://www.vahanintelligence.in/) | 3/5 | May 2026 |
| [Taylor & Francis (peer-reviewed) — Kolkata airport ground-access mode study](https://doi.org/10.1080/29941849.2025.2518203) | 4/5 | 2025 |
| [Times Now — Mumbai kaali-peeli fleet ~40,000](https://www.timesnownews.com/web-stories/cities/mumbais-kaali-peeli-taxi-to-say-goodbye-after-6-decades/photostory/104786947.cms) | 3/5 | 2025 |
| [ThePrint — Delhi e-cab registrations 15-fold surge in 5 years](https://theprint.in/business/electric-cabs-are-taking-over-delhis-roads-with-15-fold-surge-in-registrations-in-5-years/1479029/) | 3/5 | 2025 |

**Conflicts and caveats.**
1. **e-2W subsidy end date** under PM E-DRIVE: sources split between 31 Mar 2026 (MHI notification reporting) and 31 Jul 2026 (after an extension) — verify against the latest gazette before citing a specific date.
2. **Public charger counts** vary ~16k–29k by definition (installed vs operational, public vs captive). Do not mix figures across sources.
3. **Rapido's cab market share** is contested: 14–18% (Motilal Oswal/Equentis) vs ~22% (Sanka/Inc42) vs ~30% of 4W cabs (TOI citing Sensor Tower/Citi). Cite the MO numbers for consistency with items 9/37.
4. **"One-sixth of the market" (Redseer)** is a rounded spoken figure; the implied ~3B total is a derivation, not a published Redseer headline.
5. The AAI annexure PDF could not be opened programmatically; the 196.24M figure is reconciled arithmetically from published domestic and growth-rate data.

---

## Open Questions

1. **Residual values (item 4):** What did the repossessed/auctioned BluSmart EVs actually transact at? Requires DRT filings, lessor disclosures, or buyer interviews (Evera, Everest). Until then, the "10% assumed vs 26% realised" claim must be removed or footnoted as unsourced.
2. **Airport mode share (item 12):** No Indian airport publishes app-cab share of ground transport. Options: RTI to AAI/DIAL/GHIAL for commercial-vehicle movement counts; syndicated studies; or counter surveys.
3. **Occupancy per booked airport cab (item 13):** only primary research (driver/counter surveys) can fill this.
4. **Segment p3 table (items 16–21):** trip lengths, km/day, EV share and price-elasticity by use case are not public anywhere. Requires platform data partnerships or commissioned driver GPS surveys.
5. **Tata Xpres-T unit volumes (item 40):** model-level VAHAN extraction is needed (paywalled dashboards such as Autopunditz/Vahan).
6. **Airport fee schedules beyond Delhi (item 30):** Mumbai, Bengaluru, Hyderabad, NMIA commercial-vehicle terms are unpublished — request operator fee schedules.
7. **Inter-city km/day conflict (item 19):** 420 vs 340 km/day cannot be resolved externally; it is a deadhead-assumption choice, and should be documented as such.
8. **Fleet replacement rates (item 28):** no public source; interview fleet operators and leasing companies (Axis, Mufin, SMAS, Orix).
9. **e-2W subsidy terminal date:** confirm against the latest gazette notification (Mar vs Jul 2026 conflict).
10. **Offline taxi trips (item 14):** state transport departments hold registration data; no aggregate exists.

---

## Recommendations / Next Steps

1. **Fix the deck now (no new research needed):** (a) remove or flag the BluSmart residual claim (item 4); (b) restate item 2 as "GHIAL 200+ premium taxi fleet + OHM EV fleet at RGIA"; (c) correct item 6 to "Ola ₹67/day; Rapido ₹9–29 (auto) / ₹40 (cab); Uber commission + pilots"; (d) correct item 34 GST: ICE = 28% + cess (29–50% effective), not 18% — this *strengthens* the EV case; (e) add the PM E-DRIVE exclusion of e-4Ws to the TCO narrative (no central subsidy for e-cars).
2. **Upgrade grades:** items 1, 3, 5, 6(partial), 9, 10, 22, 23, 24, 25, 26, 27(numbers), 30, 33, 34, 36, 37, 38, 39, 41 → Grade A/B. Items 2, 7, 8, 11, 12, 14, 15, 28, 29, 31, 32, 35, 40 → Grade C. Items 4 (residual %), 13, 16–21 → keep Grade D.
3. **Primary research sprint (Tier 1 gaps):** 5–8 structured interviews — Evera (Nimish Trivedi), Everest Fleet (Ladsariya), Lithium, Refex, OHM, WTi — covering batch sizes, replacement cycles, financing terms, airport access agreements, and what they paid for repossessed EVs (this single data point would replace the fabricated residual claim).
4. **File RTIs / data requests** to AAI and airport operators for commercial-vehicle entry counts and fee schedules (fills items 11–13, 30).
5. **Recompute affected model cells:** GST correction (item 34) and Maharashtra fleet-CNG 14% (item 36) should flow through the TCO engine's tax assumptions; PM E-DRIVE exclusion removes any subsidy line for e-4Ws; platform-fee correction (item 6) changes driver take-home math.
6. **Refresh cadence:** platform fee structures, PM E-DRIVE status, and EV registration shares are changing quarterly (last verified Nov 3, 2026) — re-verify before any investor-facing circulation.