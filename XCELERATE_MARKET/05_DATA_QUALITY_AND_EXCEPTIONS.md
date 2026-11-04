# DATA QUALITY AND EXCEPTIONS REPORT
## Maruti Suzuki XCELerate 2026 E-Track — Market Intelligence Data Pack

**Purpose:** This report documents every material uncertainty, data-integrity issue, and source limitation in the five output files (01–05). It is an inseparable part of the data pack — no claim in outputs 01–05 should be used without reading the associated qualification in this file.

**Method:** Every CSV field was inspected for alignment, count, and consistency against the original source documents (source register, redteam reports v2–v6.1, underlying research). Where CSV field counts or content did not match the expected structure, the original raw line was examined and corroborating research was checked before assigning any value.

---

## A. CSV Field Alignment Inspection

### 01_MARKET_STRUCTURE.csv
- All rows have 14 columns as header specifies. No misalignment detected.
- Caveat fields contain explanatory notes where segment-table metrics are S-D/C-D. These are intentional qualifications, not data errors.

### 02_OPERATOR_EVIDENCE.csv
- Inspected all 32 records for field count and alignment.
- **Record O4 (Evera repo onboarded):** The `deployment_status` field value "220 onboarded; 280 in progress; another 500 planned" spans what could be two logical fields. This was kept as a single cell because the original source (BS/PTI Oct 2026) presents these three figures as a connected status update, not as separate deployments. Readers must treat this as one composite status, not three independent data points.
- **Record O12 (Bharat Taxi 600 phase 1):** The `evidence_grade` is S-C/C-B (company-reported). The `caveat` field explicitly states "The 600 cabs phase 1 are national figures; the NMIA 'up to 40' figure is a separate planned deployment at single airport. Different scopes." This qualification is mandatory — the record would be misleading without it.
- **Record O20 (Lithium 300 km/day):** The `verification_status` is S-C/C-C (company-reported, Mint interview). The `caveat` is mandatory: "The ~300 km/day and 10-12h shifts are company-reported (Mint interview). No independent telematics data confirms this duty cycle." Without this caveat, the figure would be presented as established fact.

### 03_PROCUREMENT_RELATIONSHIPS.csv
- All 10 records have 16 columns as specified. No field count misalignment.
- **P5 (Evera repossessed 500 BluSmart EVs):** The `agreement_or_deployment_status` field value "220 onboarded; 280 in progress; another 500 planned" similarly spans composite status from the BS/PTI Oct 2026 source. Kept as one cell for the same reason as O4 above.
- **P9 (OHM 1,300 ordered EVs):** The `ownership_outcome` field is "Not specified (ordered)" per the source CSV row 11. The `caveat` explicitly states "Do not treat as confirmed delivery." This is a critical qualification.

### 04_MARKET_CONTEXT_METRICS.csv
- All 7 records have 13 columns. No field count misalignment.
- Each row has a mandatory `interpretation_limit` field documenting the scope and evidence constraints. These are essential qualifications.

### 05_DATA_QUALITY_AND_EXCEPTIONS.md
- This file is the primary exception repository. All other files reference it.

---

## B. Conflicting Fleet Counts

| Operator/Figure | conflicting | Resolution | Source |
|---|---|---|---|
| **Everest Fleet EV count** | ESG FY24-25: 2,000+ EV + 18,000+ CNG = 20,000+ total; Company current: 23,500+ mixed | Gap of 3,500+ unexplained (new acquisitions or reclassification). ESG figure is the most granular breakdown. | ESG report FY24-25 (S-C); Everest website; ET Sep 2024 (S-B) |
| **Bharat Taxi at NMIA** | Company: 600 cabs phase 1 (national); Adani announcement: "up to 40 dedicated vehicles" | Different scopes: national vs. single airport. Actual NMIA deployment unverified. | TOI Jul 2026 (S-B); Adani Oct 2026 (S-B) |
| **Evera fleet total** | ~2,200 EVs + 500 repossessed (company-reported, Oct 2026); 500 more planned | The 500 planned are not added to the ~2,200+ count; they are separate. The ~2,200 already includes or excludes the repossessed depending on interpretation. | BS/PTI Oct 2026 (S-B); Delhi Airport cabs page (S-A) |
| **OHM ordered vs deployed** | 100 EVs deployed at RGIA (2022, documented); 1,000 Xpres-T + 300 BYD e6 ordered (2022-24) | Deployed (100) vs ordered (1,300, delivery unverified). Critical distinction. | EVJoints guide; company statements (S-C/C-C) |
| **Refex EV count** | 1,750+ vehicles (company-reported, BS FY26); EV count not specified | The 1,750+ is total fleet; EV subset is unreported. | BS FY26 (S-C) |
| **GMR 200+ taxis** | "200+ EV fleet at Hyderabad" (conflation) vs "200+ premium taxis announced (not EV)" | GMR announced 200+ premium taxis (sedans/SUVs), not documented as EV. OHM operates EV fleet at RGIA separately. | NewsMeter 2025 (S-B); DIAL blog Oct 2022 (S-A) |
| **DIEL 57 EVs** | "Delhi airport EV fleet" vs "own airport operations not taxi fleet" | DIAL's 57 EVs are for own airport operations (passengers, employees, cab service providers), separate from any taxi fleet. | DIAL blog Oct 2022 (S-A) |

---

## C. Announced vs. Completed Deployments

| Announced / Stated | Actual deployed/verified | Status |
|---|---|---|
| OHM: 1,000 Xpres-T + 300 BYD e6 ordered (2022-24) | Delivery unverified; only 100 EVs documented at RGIA (2022) | Announced order, not confirmed delivery |
| Refex: 1,000 EVs by 2026 (Uber partnership) | Announced target; no confirmed deployment data | Announced target |
| Bharat Taxi: "up to 40 dedicated vehicles" at NMIA (Oct 2026) | Not deployed as of Oct 2026 (Adani says "planned") | Announced, not deployed |
| Evera: 500 more EVs planned (Oct 2026) | Plan; no confirmation of delivery or deployment | Plan, not deployed |
| WTi Cabs: Target 2,000+ premium cars (doubling) | Target not achieved; no published achieved count | Target, not achieved |
| GMR: 200+ premium taxis announced at RGIA (not EV) | Announced; not documented as EV | Announced, not EV |

---

## D. Company-Reported vs. Independently Documented

| Claim | Company-reported (S-C) | Independently documented (S-A/S-B) |
|---|---|---|
| Evera ~2,200 EVs + 500 repossessed | Yes | No independent audit |
| Lithium Urban 3,000+ EVs, 600+ chargers, 25,000 trips/day | Yes | No independent audit (telematics data would be required) |
| OHM 100 EVs deployed at RGIA (2022) | Yes (company-reported) | Partially: EVJoints guide confirms deployment of 100; this is the only independently documented airport EV deployment in India |
| Everest 23,500+ mixed fleet | Yes | No independent audit |
| Snap-E 600 EVs | Yes | No independent audit |
| Bharat Taxi 600 phase 1 (national) | Yes | The NMIA "up to 40" is a separate planned deployment, not yet deployed |
| DIAL 57 EVs own ops | Yes (official airport listing) | Yes: DIAL blog Oct 2022, A-S verified |
| GMR 200+ premium taxis not EV | Yes (press report) | Conflated with "200+ EV fleet at Hyderabad" — incorrect; OHM operates EV fleet at RGIA |

---

## E. Claims in Earlier Slide Documents Contradicted by Master Research

| Contradicted claim | Source of contradiction | Resolution |
|---|---|---|
| "Airport has the highest margin" | Master research v6.1 §1.4: Airport has the **lowest** revenue per paid trip-km (₹17.1) of five archetypes | Corrected: Airport margin thesis unproven; lowest unit revenue |
| "61% intra-city market share" | Master research v6.1 §8: No trip-purpose classification exists; 61% unsourced | Corrected: Excluded from slide |
| "19.14% airport CAGR" | Master research v6.1 §8: Unreconciled with 26% table figure | Corrected: Excluded from slide |
| "Uber+Rapido ₹29/day" | Master research v6.1 §8: Rapido auto ₹9–29, cab ₹40; Uber commission-based | Corrected: Excluded from slide |
| "GMR operates 200+ EV fleet at Hyderabad" | Master research v6.1 §1.2: 200+ taxis announced, not EVs; OHM operates EV fleet at RGIA | Corrected: Do not classify GMR as EV fleet |
| "BluSmart assumed 10%, realised 26% residual" | Master research v6.1 §1.4: Management statement (Mint interview, Sep 2024), not audited | Corrected: Excluded from slide; S-C/C-C |
| "Procurement is consistently asset-light" | Master research v6.1 §1.3: Mixed models documented (leasing, owned, financed, cooperative) | Corrected: Mixed models; no single model dominates |
| "No airport offers general depot charging" | Master research §2.7: Absence of evidence, not evidence of absence. Public charging exists on premises at some airports; third-party access rights unpublished. | Corrected: Public charging exists; third-party access unproven |
| "Airport app-cabs are 20–30% of ground transport" | Master research §7 item 8: Assumption, not measured; proxies exist but no national figure | Corrected: Excluded from slide as measured figure |
| "591.3M and 810M are directly comparable" | Master research §2.3: Different scopes; 591.3M = 3-platform daily annualised; 810M = 27% of ~3B total | Corrected: Do not combine; different scopes |
| "Segment table km/day, trips/day, fares are verified" | Master research §2.2: All 35 deck segment-table cells are S-D/C-D, unsourced | Corrected: Excluded from slide; all unsourced |

---

## F. Claims That Cannot Be Independently Substantiated

| Claim | Why it cannot be substantiated | Evidence grade |
|---|---|---|
| Airport app-cab mode share 20–30% | No Indian airport publishes app-cab share of ground transport; proxies exist (Evera 55% airport bookings; Uber Reserve ~40% trips end at airports) but no measured national figure | S-D/C-D |
| Empty running / total vehicle-km for all archetypes | Unmeasured for all archetypes; no telematics data published by operators | S-D/C-D |
| Corporate commute contract terms (duration, renewal, payment structure) | Unpublished by all operators | S-D |
| Pick-up fee incidence (passenger vs. fleet) at Delhi airport | ₹290/trip verified; incidence (who bears the cost) unverified | S-A (fee verified); S-D (incidence) |
| Duty cycle for FleetLine E1 (200 km/day, 312 days/yr) | Design assumption (S-D/C-Grade); need 30–50 driver-days of GPS/trip data | S-D/C-D |
| Residual value data for EVs | No transaction prices published for repossessed BluSmart EVs; 10%/26% claim is management statement, not audited | S-C/C-C |
| Segment table growth rates (18%, 24%, 26%, 28%, 20%) | All unsourced (S-D/C-D); no independent verification | S-D/C-D |
| Price sensitivity indices (0.35, 0.40, 0.85, 0.90, 0.30) | No source; undefined scale; S-D/C-D | S-D/C-D |
| 40,000–50,000 addressable metro vehicles | Unverified; no public data on metro vehicle fleet composition or replacement cycles | S-D |
| WTi 2,000+ fleet (as achieved count) | Target, not achieved; no published actual fleet count | S-C/C-C (target) |
| BluSmart 4,704 stranded EVs residual values | No per-vehicle resale/auction prices published | S-C/C-C |
| AAI 196.24M exact figure | Secondary compilation sums to 195.94M; PDF inaccessible; exact figure unverified | S-C/C-C |
| Rapido cab rides 320,000 (Motilal Oswal) vs ~6.5M daily rides all-modes (Sensor Tower) | Different scopes (cab-only vs. all modes) | S-B/C-B (different scopes) |
| Dzire Tour S fleet pricing | Official retail pricing ₹6.24–7.10L; fleet pricing unverified | S-A (retail); S-D (fleet) |

---

## G. Malformed/Misaligned CSV Records Inspection

During inspection of the original project CSVs, the following was noted:

1. **02_OPERATOR_LANDSCAPE.csv row 10 (GMR/GHIAL):** The `charging_infrastructure` field value "Not specified" and `procurement_documented` field value "Not applicable" are correct per the source data. However, the `source` field "NewsMeter 2025; DIAL blog Oct 2022" contains two sources for different claims within one cell. This was kept as-is because splitting would lose the connection between the GMR press report and the DIAL clarification. Readers should treat these as two distinct claims with different evidence grades (S-B press report vs S-A DIAL blog).

2. **02_OPERATOR_LANDSCAPE.csv row 11 (Ola Fleet):** The `evidence_status` field "Declining (FY23 revenue -57%); entity exists but scale unverified" is a composite status. The FY23 financials are verified (S-A), but the current fleet scale is unverified (S-D). This was kept as one cell because the source presents them as connected observations.

3. **03_PROCUREMENT_EVIDENCE.csv row 11 (OHM ordered 1,300 EVs):** The `agreement_or_deployment_status` field "Delivery unverified" is correct per the source. The `financial_value` field "Not specified (ordered)" matches the source CSV row 11. No misalignment detected.

4. **01_MARKET_STRUCTURE.csv:** All caveats are intentionally written to prevent misinterpretation of S-D/C-D segment table metrics. No misalignment detected.

---

## H. Summary of Evidence Grading

| Evidence Grade | Source Type | Calculation Grade | Application in outputs |
|---|---|---|---|
| S-A | Government, regulatory, or authoritative primary evidence | C-A: Directly verifiable; C-B: Reproducible calculation | Used for: DIAL charging (12 stations/22 points); pickup fee ₹290/trip; GST rates; Maharashtra road tax; PM E-DRIVE no e-4W subsidy; Vahan EV registrations; AAI passenger movements (partial); DIAL 57 EVs own ops |
| S-B | Credible secondary source (business press, trade publication, analyst report with named attribution) | C-B: Arithmetic verified; C-C: Derived with stated inputs | Used for: Motilal Oswal data (591.3M); Redseer estimates; Evera airport presence; Uber co-investment; Ola/Rapido fees; Tata-Xpres-T agreements; OHM financing; Ola/FY25 financials; Ola FY25 financials; WTi target |
| S-C | Company-reported or management statement (not independently audited) | C-C: Derived from stated inputs but assumptions unverified; C-D: Not reproducible | Used for: Operator fleet counts (Everest 23,500+; Lithium 3,000+; Refex 1,750+; Evera ~2,700); OHM 100 EVs deployed; Lithium utilisation ~300 km/day; Refex shifted airport→B2B; Segment table metrics; All segment table data; Most procurement relationships |
| S-D | No source found; unsourced assertion or assumption-based | C-D: No defensible calculation basis | Used for: Segment table km/day, trips/day, fares, growth, EV share, price sensitivity; 20-30% airport app-cab mode share; Empty running; Profit per vehicle-km; Many "verified" claims in earlier slide decks that cannot be traced to primary sources |

**Rule:** Do not upgrade a source's evidence quality simply because the same claim appears in multiple previous summaries. Each claim must stand on its own source traceability.

---

## I. Final Quality Statement

This data pack (outputs 01–05) is designed for traceability and accuracy, not completeness. Blank fields indicate information that is unavailable or cannot be substantiated. Every substantive record has source traceability (original source document, source name, publication date, direct URL where available, evidence grade, and qualification/caveat).

**Do not use any claim from outputs 01–05 without reading the associated qualification in 05_DATA_QUALITY_AND_EXCEPTIONS.md.** The exception report is not a supplementary appendix — it is an integral part of the data pack. Any use of the data without reading the exception report invalidates the traceability guarantee.

**Key principle:** Accuracy and traceability are more important than filling every field. Blank fields where information is unavailable are preferable to invented or silently standardised values.