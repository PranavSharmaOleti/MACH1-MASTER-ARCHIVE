# 01 — Project story and timeline

## What MACH1 / FleetLine E1 was

MACH1 was a student case submission for **Maruti Suzuki XCELerate 2026, E-Track**. The proposed vehicle was **FleetLine E1**: a sub-4-metre, ~45 kWh LFP battery-electric compact sedan intended for Indian fleet operators by 2035. The design premise was a depot-charged vehicle sized to a ~200 km/day duty cycle, competing with CNG sedans such as the Dzire Tour S on cost per kilometre.

**Original thesis (as stated on deck slide 3):** "India's ride-service volume is in intra-city. India's ride-service margin is in airport and commute. This matters because they require fundamentally different vehicles." The strategic recommendation was to pitch FleetLine E1 to airport-transfer and contracted corporate-commute fleet operators.

**Why the ride-service market was investigated:** the case required a target market, a buyer, and a demand justification for the vehicle concept. Desk research was used because no primary fleet/operator data was collected.

## Original analytical sequence

1. Collect secondary research on Indian ride-hailing, EV adoption, fleet operators, TCO and competitor vehicles.
2. Build a five-row "use case" comparison table (deck slide 3) with seven numeric columns.
3. Attach a hierarchical-clustering figure to that table and label a branch "CLUSTER A = AIRPORT + CORPORATE-COMMUTE" as if clustering independently supported the choice.
4. Add a weighted multi-criteria segment-scoring model (11 criteria, 5 segments) and a sensitivity analysis.
5. Build TCO and battery models (separate workstreams; substantively stronger than the market work).
6. Write a strategic recommendation built on the table, the scoring model and operator "evidence".
7. Audit and red-team the work (v2–v6.1), correcting figures, evidence grades and claims.

**Role of the dendrogram:** it was presentation evidence for step 3 — an attempt to make the airport+commute grouping look data-driven rather than judgment-driven. It was not the basis of the scoring model, and the final recommendation survived its removal because the scoring model produced the same rank order.

## Chronology (from git and document dates)

| Stage | Date / commit | What was done | What we believed | Problems that emerged | What changed |
|---|---|---|---|---|---|
| Original deck | pre-git, archived 31 Oct (`969a099`) | Slide 3: five-use-case table + hierarchical-clustering figure + "CLUSTER A" label | Airport + commute formed a natural, data-supported cluster | Table cells unsourced; five rows are hand-built; rows are not a partition; dendrogram pairs Airport with Premium, not Commute | — |
| External market assessment | 18 Oct 2026 (`MACH1_MARKET_ASSESSMENT.pdf`) | Full withdrawal of prior market assessment | — | "five manually constructed use-case rows and seven columns"; no rider/city/trip/vehicle observations; remove dendrogram and "independent agreement"; regression 2 residual df | dendrogram and regression declared non-decision-grade |
| Repository archive + audit tooling | 31 Oct (`d4a28b3` … `e1b6733`) | Deck numbers extracted (481), 160 gaps, correction list, panel Q&A | Audit conclusions authoritative | — | PPT_CHANGE_LIST edit #7 ordered dendrogram removal/relabel; ERRATA #27 "Removed" |
| XCELERATE_MARKET research | 4 Nov (`a00b017`) | Market report, sizing model, buyer/competitor analysis, segment prioritisation, red-team v2–v6.1, slide data pack | Scoring model can replace dendrogram | All 35 segment-table cells S-D/C-D; 10→11 criteria text error; equal-weight tie; inter-city arithmetic error; premium/service-tier conflation | Segment archetypes redefined; scoring model v4; thesis reframed as "candidate beachheads" |
| Market-intelligence pack | 4 Nov (`1cb0b01`…`371ff8c`) | Content brief, 4 CSVs + exception report, then cleaned CSVs | Operator/procurement evidence can be made traceable | Fleet counts company-reported; Evera ~2,200 target vs 600+ reported; scope differences | Cleaned datasets with explicit caveats |
| Final archive | 5 Nov (`edcd356`, `154fb71`) | Cleaned CSVs added alongside originals; claim-audit reports, rendered slides, notes | Reconstruction files preserved | — | Dendrogram no longer appears as a supported method |

## Where the project ended up

- The TCO and battery-engine work remains intact and Grade A on arithmetic.
- The market thesis was downgraded from "proven margin segment" to "candidate market-entry environments requiring validation".
- The dendrogram was removed from corrected slide text; the original deck slide 3 remains only as a superseded artifact.
- The weighted scoring model survived, with explicit caveats that its ratings are analyst-assigned (S-D) and that Airport and Commute tie under equal weights.
- No primary fleet procurement interviews were conducted; all operator figures are company-reported.

**Key distinction for the professor:** the original intention was to *demonstrate* that airport + commute were a distinct, data-supported cluster. What actually happened is that the cluster claim was retired, while the strategic recommendation was retained on weaker, judgment-based grounds and reframed as a hypothesis.
