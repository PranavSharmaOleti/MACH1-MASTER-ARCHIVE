# 03 — Data and research foundation

## What research base existed when clustering was attempted

**Essentially none at observation level.** All market-side research was secondary desk research. No operator interviews, no rider survey, no trip-level or city-level panel was collected for the segmentation exercise. The five dendrogram rows were hand-assembled from a single presentation table, not from data.

## Datasets and their role

| Dataset | File | Content | Evidence character | Role in segmentation |
|---|---|---|---|---|
| Five-segment comparison | `XCELERATE_MARKET/MARKET_STRATEGY_SEGMENT_COMPARISON.csv` (73 rows) | 5 archetypes × ~7 metrics; also scoring rows | All 35 deck cells S-D/C-D; verified anchors S-B/C-B | Direct input to the dendrogram table |
| Deck numbers | `00_MASTER_DOCUMENTATION/DECK_NUMBERS_EXTRACTED.csv` | 481 extracted numbers | Extraction of the deck, not independent evidence | Source of the "stated" dendrogram record |
| Market report | `XCELERATE_MARKET/10_market/INDIA_RIDE_SERVICE_MARKET_REPORT.md` | Ride-volume proxies, Redseer, TOI anchors | S-B/C-B secondary | Provided 591.3M, ~810M, 8 trips/day, ₹300 fare |
| Market sizing | `XCELERATE_MARKET/20_market_sizing/` (`build_model.py`, methodology, xlsx) | Scenario GMV model | Arithmetic Grade A; share/fare assumptions | Not used by clustering |
| Segment prioritisation | `XCELERATE_MARKET/40_segment_prioritisation/` (7 files) | 11 criteria, 5 segments, analyst-assigned 1–5 scores, weights, sensitivity | Scores S-D; arithmetic C-A/C-B | Replaced clustering in the final recommendation |
| Source register | `XCELERATE_MARKET/MARKET_STRATEGY_SOURCE_REGISTER.csv` (42 rows) | Claim → source → URL → verification status | S-A to S-C | Traceability index for later corrections |
| Operator landscape | `XCELERATE_MARKET/MARKET_STRATEGY_OPERATOR_LANDSCAPE.csv` | 10 operators; fleet/EV/ownership/charging | Mostly S-C company-reported | Operator-presence argument |
| Airport / corporate / procurement | `MARKET_STRATEGY_AIRPORT_ECOSYSTEM.csv`, `MARKET_STRATEGY_CORPORATE_ECOSYSTEM.csv`, `MARKET_STRATEGY_PROCUREMENT_EVIDENCE.csv` | Airport charging, fees, operators; corporate clients; OEM/leasing deals | Mixed S-A to S-C | Beachhead and buyer narrative |
| Target accounts | `MARKET_STRATEGY_TARGET_ACCOUNTS.csv` | 11-operator database | S-C | Sales-target narrative |
| Data gaps | `MARKET_STRATEGY_DATA_GAPS.md` | 28 gaps, 11 unsupported claims | Audit artifact | Documents what could not be substantiated |
| Vahan / AutoPunditz panels | `03_ENGINEERING_AND_MARKET_DATA/Market/data/*.csv`, Autiqa screenshots | Registration/sales series | Grade A data, limited states/measure ambiguity | Supply-side only; never segmentation inputs |
| Cleaned data pack | `01_–04_*_CLEAN.csv`, `05_DATA_QUALITY_AND_EXCEPTIONS.md` | Corrected market structure, operator evidence, procurement, context metrics | Explicit caveats per record | Current slide-source; no clustering |

## Which variables were genuinely sourced vs assumed

**Sourced (S-B/C-B, secondary):** three-platform daily ride counts (Uber 840k, Ola 460k, Rapido 320k → 591.3M/yr annualised); Redseer ~3B total ride-hailing trips and 27% cab share (~810M); ~196M airport passenger movements (AAI, partial); ~8 trips/driver-day and ₹300–400 fare (TOI/Redseer); Evera ~₹600 airport fare; ₹290 Delhi pick-up fee (S-A); DIAL 12 stations/22 charging points (S-A); EV share of new 4W registrations 7.3–8.7% (Vahan).

**Assumed / unsourced (S-D/C-D):** all 35 segment-table cells — avg km, km/day, trips/day, fare, growth, EV share, price sensitivity; 20–30% airport app-cab mode share; 200 km/day 312-day duty cycle (design assumption); residual values; "airport highest margin"; 61%/58% intra-city share; 19.14% airport CAGR.

**Scoring-model ratings (S-D):** all 1–5 ratings across 11 criteria for 5 segments (analyst-assigned). Weights are transparent (10/10/10/15/5/5/20/15/5/5/5, normalised) but the ratings are judgment, not measurement.

## Competitor / buyer / procurement research

- Operators: Everest (23,500+ mixed), Lithium (3,000+ EV), Evera (~600+ reported; ~2,200 was an unachieved expansion target), Refex (1,750+), OHM (100 deployed at RGIA), Snap-E (600), Bharat Taxi, GMR/GHIAL, DIAL, Ola Fleet. Nearly all figures **company-reported** (S-C); OHM's 100 RGIA deployment is the only documented site-specific airport EV deployment, but not asserted as unique.
- Procurement channels documented: Tata–Uber 25,000 Xpres-T agreement (Feb 2023), Tata–BluSmart 10,000 (2022), Uber–Everest $20M+$30M co-investment, Evera lender leasing, OHM/Mufin financing, Lithium owned fleet, Bharat Taxi cooperative, Evera's 500-vehicle repossession (secondary asset acquisition, not OEM procurement).
- Buyer-chain roles identified: OEM, asset owner, financier, fleet operator, aggregator, employer, driver.

## What remained missing

1. Trip-level or operator-month data (purpose, fare, paid km, deadhead km, city, month) — **the single most needed dataset**.
2. Any measurement of airport app-cab mode share or airport cost advantage (pick-up fee incidence, deadhead, depot access).
3. Verified fleet sizes, financing terms, replacement cycles and buying authority.
4. Corporate commute contract terms and trip data (Lithium's 25,000 trips/day and 300 km/day are company-reported, not audited).
5. Trip-purpose classification of ride-hailing demand; segment shares are not a partition.
6. Residual values and repossessed-EV transaction prices.

**Assessment:** the research foundation was adequate for a qualitative operator/procurement narrative and for a clearly-labelled scenario model. It was **not adequate** for statistical clustering, segment-share claims, or a margin comparison. The dendrogram was built on the weakest layer of that foundation.
