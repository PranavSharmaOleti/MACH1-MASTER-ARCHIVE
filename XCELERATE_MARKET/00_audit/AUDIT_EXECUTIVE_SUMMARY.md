# Research Audit — Executive Summary

**Project:** Maruti Suzuki XCELerate 2026, E-Track — ideal ride-service vehicle for India 2035 (MACH1 / FleetLine E1)
**Date:** 3 November 2026
**Full audit:** `RESEARCH_AUDIT.md` (35 rows, 7 groups, confidence A–D)
**Reproduction:** `segment_table_check.py` → `segment_table_checks.csv` (20 checks); `tco_engine/tco_analysis.py` (878 lines, exit 0); `Market/market_analysis.py`

---

## 1. Bottom line

**This project has a defensible cost model and an indefensible market model.**

The TCO engine is Grade A. Every headline TCO number in the deck reproduces exactly from `tco_analysis.py` — including the Mumbai road-tax correction and the "one negative cell in 48" claim. It should not be redone.

The market side is Grade C/D throughout. Slide 3 decides which vehicle to build, and it is the only slide in the deck with no evidential basis anywhere in the archive. The five-segment table, the ~61% intra-city share, the 19.14% CAGR and the dendrogram all trace back to `NITDurgapur/Detailed Report.pdf` → drafts → deck, with no derivation at any step, and the project's own ruling document (`MACH1_MARKET_ASSESSMENT.pdf`, 18 Oct 2026) withdraws the table.

---

## 2. Five findings that matter

| # | Finding | Grade | Consequence |
|---|---|---|---|
| 1 | **Airport earns the LOWEST gross revenue per vehicle-km of the five segments** — ₹17.1 vs premium ₹28.9, intra-city ₹27.6, commute ₹25.0, inter-city ₹18.5 | `[calc]` A | The core thesis ("margin is in airport + corporate commute") is a *cost* claim, not a fare claim — and the project never computes segment cost. A panel member can refute the thesis with one division using the deck's own table. |
| 2 | **`tco_engine/figures.txt` is stale and actively misleading** — reports Mumbai 5-yr −0.2%, "4 negative cells of 48", "the 5-year case does not close outside Delhi" | A | All three are contradicted by the current engine *and* the deck. It predates the §R Mumbai road-tax fix. Anyone re-deriving from that file will wrongly conclude the deck is wrong. Regenerate or delete. |
| 3 | **Fleet anchors are ~4× apart and never reconciled** — 1.62M rides/day ÷ 8 trips/day ⇒ ~202,500 active cars nationally, vs 40,000–50,000 "addressable metro" vehicles | A / C | The buyer-hypothesis document and the market document describe different markets. |
| 4 | **The five segments are not a partition** — "premium/shared-premium" is a service tier, not a trip purpose; airport runs can be premium; intra-city runs can be shared | A | "61%" and "~58%" cannot be a valid decomposition of any total. This is why the two numbers disagree. |
| 5 | **`Market/market_analysis.py` has a data-path bug** — it reports all six CSVs "missing"; the data-inventory section has never run | A | The 591.3M ride proxy and GMV scenarios compute correctly, but the script's own data validation is inert. |

---

## 3. Where the evidence actually stands

| Block | Status | Action |
|---|---|---|
| **TCO — Delhi, city matrix, NPV, driver economics** | **Grade A.** Reproduced exactly; internally self-audited; Mumbai correction documented with gazette reference. | Keep. Do not redo. Tag every figure with its basis (nominal/incl-infra/NPV). |
| **591.3M platform rides, GMV scenarios** | Grade A arithmetic, Grade B inputs (Motilal Oswal via Business Standard, 18 Apr 2025). Correctly labelled "scenario envelope, not TAM". | Keep, but add car-only sensitivity (excl. Rapido: 474.5M/yr, −20%). |
| **Five-segment table, 61%, 19.14% CAGR, dendrogram, price sensitivity** | **Grade C/D.** Withdrawn by the project's own ruling document. Register covers 8 of ~40 cells. | Withdraw. Do not repair. |
| **Buyer = 5,000–40,000-vehicle fleet operator** | **Grade C.** No survey, no interview, no procurement record. BluSmart — the only at-scale leased EV fleet in India (6,400 EVs under Gensol; 4,704 purchased per SEBI, 15 Apr 2025) — suspended operations in April 2025, and the positioning doc cites that exit as *validation* of the same segment. | Test first. This is the assumption the product rests on. |
| **Airport lane evidence** (Evera Delhi terminals, GMR Hyderabad 200+ EV fleet, Bharat Taxi Navi Mumbai) | **Grade C.** The entire real-world basis for the airport lane; none of it is in the archive. | Verify against company/airport-operator releases. Cheap and decisive. |

---

## 4. Priority

1. **P0-1 — Test the buyer hypothesis before market size.** *Kill criterion:* if no Indian buyer routinely purchases >500 cars per order, the 5,000–40,000-vehicle thesis is dead and the vehicle must work for a 20–200-car operator.
2. **P0-2 — Measure duty cycle and fare** (airport concession data, filings, 30–50 logged driver-days). 200 km/day, 8 trips/day and ₹300–600 fares are assumptions quoted as facts — and the deck's own table contradicts 200 km/day.
3. **P0-3 — Re-segment orthogonally** (purpose × channel × tier; never sum across axes).
4. **P1-4 — Reframe the airport thesis as a cost/segment P&L** using the existing engine, or let the data pick the launch segment.
5. **P1-5 — Verify six external lynchpins** (all currently Grade C, one citation each).
6. **P1-6 — Repair repo contradictions** (`figures.txt`, script path, 263 vs 268 km, MCH-I-008 rated life).

---

## 5. Limits of this audit

Live web search was unavailable in this environment (HTTP 402; DDG blocked, Bing proxied). Direct URL fetches work — the BluSmart and SEBI facts were confirmed that way. The six external lynchpins remain unverified because they require search rather than a known URL; they are logged as P1-5 and should not be presented as facts until closed.
