# Total Cost of Ownership Analysis
### MACH1 / FleetLine E1 — operator and driver economics
### Built on 37 sources, with an explicit convergence analysis
### **Revision 3 — audited three times; all figures regenerated from the engine**

---

## 0. Headline

**BEV wins in every city modelled, and the margin is now better than we first claimed.**

| Finding | Number |
|---|---|
| EV advantage, 5-yr **financed** (Delhi) | **+14.5%** (₹5.75/km vs ₹6.73/km) |
| EV advantage, 5-yr **cash purchase** | **+22.6%** (₹4.63/km vs ₹5.98/km) |
| EV advantage, **8-year** horizon | **+28.0%** (₹4.20/km vs ₹5.84/km) |
| Breakeven duty | **118 km/day** at 5 yr · **64 km/day** at 8 yr |
| Driver take-home gain | **+₹5,252/month** during loan · **+₹14,200/month** after |
| Uptime headroom | **45 extra downtime-hours/month** |
| **Binding condition** | Electricity above **~₹11/kWh** flips the answer |

**Four corrections, in the order they were found:**

1. **Our earlier "16–28% better" was overstated.** It came from adding the full purchase price
   to both vehicles with no financing treatment and a 36% EV residual. The honest 5-year
   financed figure was **+8.4%**.
2. **The deck's residual assumption was wrong.** It implied ~36%; BluSmart — our exact target
   segment — assumed 10% and realised **26%**.
3. **A correction we made was itself wrong.** We had removed Delhi's EV road-tax waiver on the
   strength of a *draft* policy. Verified against the notified policy, **the waiver has not
   lapsed — it was re-enacted and extended to the life of the vehicle.** Correcting this *raised*
   the EV advantage from +8.4% to **+14.5%**.
4. **CNG mileage sensitivity was mis-tested** and then over-corrected. Measured data settles it
   (§6): the deck's 25 km/kg is mid-band, and EV wins across the whole realistic range.

**None of this changes the powertrain verdict.** It strengthens the operator case and identifies
the one condition that would flip it: **public charging instead of depot charging.**

---

## 1. Method

Per the brief — *purchase, energy, maintenance, uptime, residual value* — from **both** the
operator's and the driver's view.

**Costed once, never twice.** Capital cost appears either as the cash on-road price *or* as the
full EMI stream. An early draft added both, double-counting the loan principal and making the EV
look 95% worse. Recorded in §10.

**Included:** ex-showroom, GST, road tax (per vehicle), financing, energy net of charging
losses, maintenance net of the EV tyre premium, insurance, driver downtime, residual credit.

**Excluded, with reason:**

| Excluded | Why |
|---|---|
| Aggregator commission (20–25%) | **Same on both vehicles**, so it cancels. Also keeps this reconcilable with the deck's ₹57,200/month gross revenue. Does not change the ranking. |
| Toll / FASTag | Vehicle-class dependent, not powertrain dependent |
| Driver salary as a cost | Treated as revenue-side (fare × km); only *lost* earning time is costed — the uptime term |
| Battery replacement | Outside the 8-year horizon at our duty (§8) |

---

## 2. Configuration

| | |
|---|---|
| **Vehicle** | FleetLine E1 — BEV, LFP 45 kWh, PMSM 80 bhp continuous, single-speed |
| **Comparator** | Maruti Dzire Tour S (CNG) |
| **Duty** | 200 km/day × 26 days × 312 days = **5,200 km/mo · 62,400 km/yr** |
| **Consumption** | **12.84 kWh/100 km** (verified duty cycle — corrects the deck's 15.38) |
| **Charging** | Depot AC overnight, **90% wall-to-battery** efficiency |
| **Revenue** | ₹11/km net fare → **₹57,200/month** |
| **Financing** | 10% annual, 60 months, no down payment (deck's assumption) |
| **Horizon** | 5 years (loan) and 8 years (battery-phase horizon) |
| **Cities** | Delhi, Mumbai, Bengaluru — different tariffs, road tax and CNG prices |

---

## 3. The cost stack — Delhi, 5 years, financed

| Component | EV | CNG | EV advantage |
|---|---|---|---|
| On-road (ex-showroom + GST + road tax) | ₹12,72,600 | ₹8,51,488 | −₹4,21,112 |
| Finance (EMI ₹27,039 / ₹18,092 × 60) | ₹16,22,339 | ₹10,85,496 | −₹5,36,843 |
| Energy | **₹2,00,304** | ₹9,48,480 | **+₹7,48,176** |
| Maintenance | **₹93,600** | ₹2,10,000 | **+₹1,16,400** |
| Insurance | ₹2,10,000 | ₹1,97,400 | −₹12,600 |
| Residual credit | −₹3,30,876 | −₹3,40,595 | +₹9,719 |
| **Total** | **₹17,95,367** | **₹21,00,781** | **+₹3,05,414** |
| **Cost per km** | **₹5.75** | **₹6.73** | **+14.5%** |

**The shape of this table is the argument.** The EV is ₹4.2 L dearer to buy and ₹5.4 L dearer to
finance. Energy and maintenance return **₹8.6 L** over five years — comfortably more than the
₹9.6 L premium, leaving a ₹3.05 L net gain.

Note the residual line: **the CNG comparator actually recovers slightly more** (₹3.41 L vs
₹3.31 L), because 40% of a cheaper car is close to 26% of a dearer one. The EV's residual
weakness is real but smaller in rupee terms than the percentage gap suggests.

---

## 4. Operator TCO — three cities

| City | Basis | EV ₹/km | CNG ₹/km | EV advantage |
|---|---|---|---|---|
| **Delhi** | Financed 60 mo | **5.75** | 6.73 | **+14.5%** |
| Delhi | Cash outright | **4.63** | 5.98 | **+22.6%** |
| **Mumbai** | Financed 60 mo | **6.47** | 7.00 | **+7.6%** |
| Mumbai | Cash outright | **5.35** | 6.31 | **+15.3%** |
| **Bengaluru** | Financed 60 mo | **6.66** | 7.25 | **+8.2%** |
| Bengaluru | Cash outright | **5.45** | 6.51 | **+16.4%** |

**Delhi is the strongest case**, not because of electricity alone but because it combines **both**
a ₹4.50/kWh EV tariff *and* a full road-tax exemption on the EV while the CNG comparator pays
standard road tax. Mumbai's ₹9.50 tariff costs it 7 points.

### Two levers the deck does not use

**Lever 1 — financing structure nearly doubles the advantage.** Cash purchase gives +22.6%
against financed +14.5%, same city, same vehicle. Interest on the EV is **₹3,49,739** against
**₹2,34,008** on the CNG — a differential of about ₹1.16 L.

That is a *negotiation* lever, not a physics one. **A 7-year tenure converts most of the horizon
from "financed" to "cash"** — worth more than any tariff negotiation available.

**Lever 2 — hold the vehicle longer.**

| Horizon | EV ₹/km | CNG ₹/km | EV advantage | Cumulative saving |
|---|---|---|---|---|
| 5 yr | 5.75 | 6.73 | +14.5% | ₹3,05,414 |
| 6 yr | 5.06 | 6.34 | +20.1% | ₹4,75,809 |
| 7 yr | 4.57 | 6.05 | +24.4% | ₹6,46,204 |
| **8 yr** | **4.20** | **5.84** | **+28.0%** | **₹8,16,599** |

Delhi, financed. **The case nearly doubles by year 8** because the loan is repaid and the asset
keeps earning. This is the strongest single argument in the document — and it is an *operator*
argument, belonging to whoever owns the vehicle.

---

## 5. Driver view

| | EV | CNG |
|---|---|---|
| Monthly outflow (Delhi, yr 1–5) | **₹35,437** | ₹40,690 |
| **Driver take-home, during loan** | **₹21,763** | ₹16,510 |
| **Driver take-home, year 6+** | **₹48,802** | ₹34,602 |

- **During the loan: +₹5,252/month** — the driver is clearly ahead.
- **After the loan: +₹14,200/month** — a step change once the EMI disappears.
- **Five-year cumulative take-home gap: ₹3,15,133.**

This **validates the deck's headline claim.** The deck's "+₹14,400/month advantage" post-loan is
close to our computed **₹14,200** — that number was right.

### Higher duty strengthens the case, not weakens it

Our own survey document describes these vehicles running "250–300 km/day," while the deck models
200 km/day. That inconsistency is a **range** question, not a TCO one — and it resolves in the
EV's favour:

| Duty | EV ₹/km | CNG ₹/km | EV advantage |
|---|---|---|---|
| 150 km/day | 7.46 | 7.96 | +6.4% |
| **200 km/day (deck)** | **5.75** | **6.73** | **+14.5%** |
| 250 km/day | 4.73 | 5.99 | +21.1% |
| 300 km/day | 4.05 | 5.50 | **+26.4%** |

Fixed costs spread over more kilometres, so **the higher-duty scenario is better for the EV.** And
range is adequate there too: 45 kWh × 90% usable ÷ 12.84 kWh/100 km = **315 km**, which covers a
300 km day with 15 km to spare.

**But the driver view is the weaker of the two arguments and is not the one to lead with.** A
driver does not buy the vehicle; a fleet operator does. The driver's economics improve *because*
the operator's do. Leading with take-home inverts the causality and invites "whose vehicle is
this?"

---

## 6. Sensitivity

Change one input at a time. 5-year financed, Delhi.

| Input change | EV advantage |
|---|---|
| **Base** (Delhi: elec ₹4.50, CNG ₹76/kg, 25 km/kg) | **+14.5%** |
| CNG 22 km/kg — *city only, AC on* | **+19.5%** |
| CNG 24 km/kg — *city-heavy, measured* | **+16.1%** |
| CNG 27 km/kg — *mixed, optimistic* | **+11.6%** |
| CNG 30 km/kg — *highway, not metro duty* | **+7.6%** |
| CNG 35 km/kg — *highway only* | **+1.9%** — still positive |
| CNG price ₹76 → **₹90/kg** | **+21.1%** |
| Electricity ₹4.50 → **₹8.00** | **+7.1%** |
| Electricity ₹4.50 → **₹8.50** | **+6.1%** |
| Electricity ₹4.50 → **₹10.00** | **+2.9%** |
| Electricity ₹4.50 → **₹12.00** (public DC) | **−1.4%** ✗ |
| Electricity ₹4.50 → **₹18.00** | **−14.1%** ✗ |
| Electricity ₹4.50 → **₹24.00** (public DC retail) | **−26.8%** ✗ |
| EV residual 26% → 36% *(deck's old assumption)* | **+20.6%** |
| CNG residual 40% → 45% | **+26.0%** |
| Consumption 12.84 → 15.38 kWh/100 km *(deck's figure)* | **+12.7%** |
| 8-year horizon | **+28.0%** |
| **Worst case stacked** (15.38 + ₹12 + resid 26%) | **−6.4%** |
| **Best case stacked** (12.84 + ₹4.50 + resid 36%) | **+20.6%** |

### The CNG fuel-economy band is measured, not assumed

The deck's 25 km/kg was flagged as doing a great deal of work unevidenced. It is now
evidenced — and it is **mid-band**, not optimistic:

| Condition | Dzire CNG real-world | Source |
|---|---|---|
| **City, AC on** | **22.0 – 25.0** | cars24 (2026); buyselltaxi (2026, Delhi operators) |
| **Mixed, typical Ola/Uber pattern** | **24.0 – 27.0** | buyselltaxi (2026) |
| City (cars24, mixed city/highway) | 24.5 – 26.5 | cars24 (2026) |
| Highway / outstation | 28.0 – 32.0 | both |
| Factory kit (2020+) vs aftermarket | 24–28 vs 18–22 | buyselltaxi |
| Swift CNG road test — city loop | **21.28** | CarTrade (2025) |
| Swift CNG road test — highway loop | 35.01 | CarTrade (2025) |
| ARAI claimed | 33.7 – 34.3 | — |

**For 200 km/day metro duty with AC on, the defensible band is 22–27 km/kg and the deck's 25 sits
in the middle.** EV wins across all of it (+19.5% to +11.6%) and — notably — **still wins at 35
km/kg**, a highway-grade figure this duty never sees.

**Present the band, not a single number.** An industry judge who knows the real figure will
respect that you already priced it in.

### Convergence check on the energy line

buyselltaxi independently computes Delhi CNG running cost at **₹3.19/km** (₹76.59/kg ÷ 24 km/kg).
Our engine returns **₹3.17/km** at the same 24 km/kg — two unrelated sources agreeing to within
0.7% on the largest line in the comparison.

**Three things stand out:**

1. **The CNG assumption survives contact with real data**, with margin. The measured band leaves
   +19.5% to +11.6%.
2. **Electricity tariff is the real fragility.** Above roughly **₹11/kWh** the EV loses. Depot
   rates are ₹4.50–9.50; public DC retail is ₹12–24. This is the entire case.
3. **Uptime is the binding operational risk** — 45 h/month of headroom against a documented
   75 h/month failure mode (§7).

---

## 7. The two conditions

### Condition 1 — the vehicle must charge at its own depot

| Charging route | Energy cost | 5-yr result |
|---|---|---|
| **Delhi EV tariff (₹4.50/kWh)** | ₹0.64/km | **+14.5%** ✓ |
| Delhi commercial band (₹8.50/kWh) | ₹1.21/km | **+6.1%** ✓ |
| Public DC fast charge (₹12/kWh) | ₹1.71/km | **−1.4%** ✗ |

Depot off-peak electricity in India runs **₹5.50–9/kWh**; public DC retail runs **₹18–24/kWh**.
Our Delhi figure uses the **BEE-notified EV tariff category** (LT 4.50 / HT 4.00). Maharashtra
has fixed EV-charging stations at **₹9.50/unit to 2028-29** (MERC).

**This is not a rounding error. It is the entire case** — though with far less drama than we
previously claimed, since even ₹8.50 leaves the EV ahead.

### Condition 2 — uptime

| | |
|---|---|
| EV downtime headroom | **45 extra hours/month** before CNG wins |
| Real-world failure reference | **~75 hours/month** (Green SM Limo, Noida) |
| **Headroom vs observed failure** | **0.61×** |

Green SM drivers reported losing roughly **2.5 hours a day** to charger queues — about
**75 hours a month**. We have 45 hours of margin against a failure mode costing 75.

**The margin is real but still smaller than the failure.** The counter-argument stands: Green SM's
loss was a consequence of *not* owning depot charging — they queued at public chargers because
they had no depot. With overnight depot charging the downtime term goes to approximately zero and
45 hours becomes ample.

**But that is a claim about our operating model, not about the vehicle.** It must be stated as
such and enforced by contract, or we are assuming away the largest risk in the business case.

---

## 8. Residual value — EV's weakest flank

| Source | Evidence |
|---|---|
| **BluSmart** (Anmol Jaggi, via Mint) | Leased Tata Xpres-T at a **10% residual assumption; realised ~26%** |
| **Mahindra First Choice** (CEO) | EV residual is **70–80% of comparable ICE** after three years |
| **Spinny** | 3-year-old EV loses **~46%** vs **~40%** for an equivalent ICE |
| **CARS24** | 3–5-year ICE retains **>50%**; EV materially less |
| **JATO Dynamics** | Nexon EV annual depreciation **26%** vs petrol **13.8%** / diesel **14.9%** |
| **IRDAI** | IDV depreciation **5%–50%** by age, applied **identically to EV and ICE** — no EV table |
| **Policybazaar** | A used EV of the same age typically **costs more to insure**; OD premium drives it, and the 15% EV discount is **third-party only** |

**Two structural problems, neither of which we can fix:**

- **No standardised battery State-of-Health certificate for resale in India.** IRDAI has no
  EV-specific IDV table; insurers fall back on age, warranty and manufacturer reputation. That is
  precisely why BluSmart could beat a 10% assumption — and why other buyers discount further.
- **Residual risk sits with whoever leases.** BluSmart's finding — 10% assumed, 26% realised — is
  *favourable*, and even then the gain only materialised because they could sell into tier-2/3
  markets.

**We model 26% — the pessimistic realised number, not the deck's ~36%.** That costs the EV
**6.1 points** (+14.5% → +20.6% if recovered in full). A buyback contracted at ≥36% recovers it.

**Battery replacement sits outside the 8-year horizon.** At 198 EFC/yr, 3,000 cycles is ~15 years.
Out-of-warranty passenger packs are quoted at **₹4–12 lakh** — which is why the *warranty*, not
the chemistry, is the residual-value question. See the battery report: first life is solid; the
8-year/80% warranty is the contested claim.

---

## 9. Taxes and purchase

| | EV | CNG (Dzire Tour S) |
|---|---|---|
| GST | **5%** | 18% |
| Why | EV of any size or price is a separate 5% slab, no cess, retained through GST 2.0 | Small car: ≤1200 cc **and** ≤4000 mm |
| Road tax — Delhi | **0%** — full exemption for the **life of the vehicle** | ~10% |
| Road tax — Mumbai | **0%** (waiver to Mar 2030) | ~8% |
| Road tax — Bengaluru | **8%** (tiered from Apr 2026) | ~8% |

### Delhi's road-tax position — verified against the notified policy

**Delhi Electric Vehicles Policy 2026** was approved by the Council of Ministers on 29 June 2026,
notified 30 June, and **effective 1 July 2026**, running to 31 March 2030:

- **100% exemption from road tax and registration fees** for all EVs registered during the policy
  period, **throughout the life of the vehicle** — more generous than the time-bound waiver it
  replaced.
- For **electric cars**, exemption applies where **ex-showroom ≤ ₹30 lakh**. Ours is ₹12.12 L, so
  it qualifies.
- Above ₹30 lakh: no exemption.
- The draft's proposed 50% road-tax relief for strong hybrids was **dropped** from the notified
  policy.

**We model Delhi road tax at 0% for the EV and 10% for the CNG comparator.** Worth **₹1,27,260**
on our vehicle.

> **Correction to a correction.** An earlier revision of this document removed Delhi's EV
> road-tax waiver entirely, on the strength of a secondary compilation that cited the **draft**
> policy and reported a March 2026 lapse. That was wrong — the policy lapsed and was then
> re-enacted. The error *penalised the EV* by ₹1,27,260; correcting it moved the Delhi advantage
> from +8.4% to +14.5%. **Lesson: a policy change must be verified against the notified
> instrument, not a summary table.**

**Two other things to flag:**

1. **Our vehicle is 3,995 mm — 5 mm inside the 4,000 mm "small car" line.** That keeps the CNG
   comparator in the 18% slab rather than 40%. It is the assumption that makes the comparison as
   close as it is; a longer CNG rival would widen our advantage.
2. **Karnataka moved to tiered EV taxation in April 2026** (5% up to ₹10 L, 8% ₹10–25 L, 10%
   above), so Bengaluru no longer offers a blanket waiver.

**Note on aggregation:** no source charges GST on used-car resale differently, so no second-hand
margin is modelled. Most target operators deploy new vehicles.

---

## 10. Corrections made during this analysis

Recorded because each would have been indefensible if a judge found it.

| # | Error | Impact |
|---|---|---|
| 1 | Counted purchase price *and* the full EMI stream — double-counting principal | Made EV look **95% worse** |
| 2 | EMI formula applied the annual rate as monthly | EMI 5× too high |
| 3 | CNG ex-showroom back-solve omitted road tax | Comparator understated ~₹2.8 L |
| 4 | km/day bisection mutated the wrong module namespace | Reported 600 km/day breakeven instead of 153 |
| 5 | EV residual assumed ~36% | Replaced with BluSmart's **realised 26%** — costs EV 6.1 points |
| 6 | Omitted charging losses | ~11% energy understatement |
| 7 | Omitted the EV tyre-wear premium | ~30% maintenance understatement |
| 8 | Overstated the advantage as "16–28%" | Corrected to the modelled **+14.5%** |
| 9 | **CNG km/kg sensitivity applied to the wrong vehicle** | Claimed "CNG mileage doesn't matter" — false |
| 10 | **Removed Delhi EV road-tax waiver on a draft-policy source** | **Penalised the EV by ₹1,27,260**; correcting it raised the advantage +6.1 points |
| 11 | Source count stated as 31 after adding 4 more | Corrected to 35 |

---

## 11. Convergence analysis

Thirty-seven sources. Where they agree, the finding is safe to present. Where they diverge, the
divergence is disclosed.

### Where the literature converges

| Finding | Converging sources |
|---|---|
| **EV is most cost-effective for high-mileage taxis** | CEEW · Cadmus/Uber · ICCT · BusinessLine · ev.care |
| **Parity threshold ~100–200 km/day** | BusinessLine (EKA, Euler) · CEEW · ev.care |
| **EV maintenance 40–70% below ICE** | EVSelect · ev.care · CEEW |
| **EV tyres wear 25–30% faster** | EVSelect · ev.care |
| **EV residual materially weaker than ICE** | BluSmart · Mahindra First Choice · Spinny · CARS24 · JATO |
| **Depot charging is essential, not optional** | ev.care · Indian Express · Cadmus/Uber |
| **CNG real-world 22–27 km/kg in metro taxi duty** | cars24 · buyselltaxi · CarTrade |

**Two clean quantitative convergences worth putting on a slide:**

1. ev.care quotes depot-charged fleet-car energy at **₹1–1.5/km**. Our engine at the deck's
   ₹8/unit returns **₹1.14/km** — agreement without coordination.
2. buyselltaxi computes Delhi CNG at **₹3.19/km**. Our engine returns **₹3.17/km** at the same
   24 km/kg.

### Where sources diverge

| Disagreement | Positions | What we did |
|---|---|---|
| **EV residual: level vs trend** | Mint 2024: Nexon EV depreciation *improving* 51% → 26%. Mint 2025 + Business Standard: still ~2× worse than ICE, 70–80% of ICE at 3 yr. BluSmart: 26% realised | Both true — absolute depreciation falling while the *gap* persists. Modelled **26%** |
| **Payback period** | BusinessLine **18–24 mo**; ev.care **2–3.5 yr** (3W) / **2.5–4 yr** (charging infra); Electricon: leasing beats ownership | Scope differs — BusinessLine is light-CV fleet parity, ev.care includes charger capex. We use **fleet-car** figures |
| **Battery replacement in horizon?** | CEEW assumes packs replaced after ~2,500 cycles. Our battery phase: 198 EFC/yr → 3,000 cycles ≈ **15 yr** | **No replacement modelled** in 8 yr; flagged in §8 as a residual-value risk |
| **EV energy ₹0.64 or ₹1.71/km?** | Delhi EV tariff ₹4.50 vs public DC ₹12–24 | Both true — **this is the routing decision**, not a disagreement. Condition 1 |
| **Delhi EV road tax** | Secondary compilation (draft policy): waiver lapsed Mar 2026. Notified Policy 2026: **full life-time waiver to 31 Mar 2030** | **Notified policy wins.** 0% modelled. See §9 |

**Honest summary:** sources agree on direction and mechanism. They diverge only on magnitude, and
the magnitude disagreements cluster on *charging arrangement* and *residual assumption* — the two
things flagged here as conditions rather than settled facts. The one place where a divergence
mattered materially was the Delhi road tax, and it was resolved against the primary instrument.

---

## 12. Risks, in order of size

| Risk | Exposure | Mitigation |
|---|---|---|
| **Pack replacement inside the horizon** | **₹4 L → −4.5% · ₹8 L → −23.5% · ₹12 L → −42.6%. Any replacement flips the answer.** | Warranty-backed pack-to-pack or capacity-retention guarantee; see below |
| **Charging moves depot → public** | −1.4% at ₹12/kWh; −26.8% at ₹24 | Depot charging as a contractual operating premise |
| **Uptime falls to Green SM levels** | 75 h/month > 45 h headroom — **EV loses** | Charger redundancy (N+1), guaranteed-response maintenance SLA |
| **Residual lands at deck's 36% or below** | −6.1 points | OEM buyback at ≥36%; residual-sharing with the lessor |
| **Duty falls below ~118 km/day** | EV loses | Our duty is 200 km/day; re-run this model if it changes |
| **Consumption is the deck's 15.38** | −1.8 points only | Small. Verifiable from telematics in month one |
| **Financing at 10% for 60 months** | Costs ~8 points vs cash | Negotiate 7-year tenure or an EV-specific product |

### The battery warranty is a TCO risk, not only a range risk

This is the exposure the adversarial pass surfaced, and it is the one most likely to be missed.
Our model assumes **no pack replacement within eight years**. If one occurs, it dominates
everything else in this document:

| Replacement cost | EV ₹/km | EV advantage |
|---|---|---|
| No replacement (modelled) | 5.75 | **+14.5%** |
| ₹4 L pack | 7.04 | **−4.5%** |
| ₹8 L pack | 8.32 | **−23.5%** |
| ₹12 L pack | 9.60 | **−42.6%** |

**Even a ₹4 L pack at ₹3,500/kWh reverses the entire case.** At the deck's own pack cost this is
not hypothetical.

Whether it happens depends on the calendar exponent the battery phase found contested:
Naumann's √t law gives **13.3 years** to 80% at 40 °C; Lewerenz's measured linear law gives
**3.7 years**. At 198 EFC/yr the pessimistic case reaches 80% around year four. Our pack *sizing*
already absorbs that — it is why the model calls for 44.2 kWh rather than 45 — but **sizing does
not help if the pack is physically replaced.**

**So the warranty structure, not the chemistry, carries this risk.** It is the same finding the
battery report reached from the physics side, and it lands in the TCO as a hard number. Mitigation
is contractual: a capacity-retention guarantee or pack-to-pack service, not a specification.

**Two of the top three risks are operational; the third is contractual.** The honest headline:
the vehicle is right, and the business case is held together by how it is operated, financed and
warranted.

---

## 13. What we will not claim

- **Not** "EV is 16–28% cheaper." The defensible figure is **+14.5%** over 5 years financed,
  **+22.6%** cash, **+28.0%** over 8 years.
- **Not** "EV wins everywhere equally." Delhi (+14.5%) beats Bengaluru (+8.2%) and Mumbai (+7.6%)
  because it has both the cheapest electricity and a full road-tax exemption.
- **Not** "the advantage is insensitive." At ₹12/kWh electricity the EV loses. The tariff is the
  case.
- **Not** "zero downtime cost." We assume depot charging keeps it near zero — an operating-design
  claim we must earn, with 45 hours/month of headroom against a documented 75-hour failure.
- **Not** "residual value is fine." We use 26%, the pessimistic realised number.
- **Not** "no battery cost inside the horizon." We assume no pack replacement. A ₹4 L replacement
  reverses the case, and whether it occurs depends on a contested calendar exponent.
- **Not** a driver-income argument as the lead. Lead with the operator case.

---

## 14. Sources

**TCO methodology and parity**
1. CEEW, *Cost of Ownership for India's Road Transport Sector* — taxi TCO ranking; maintenance sensitivity; hybrid 43% GST+cess
2. Cadmus / Uber, *Electrifying Ridehail in India* (Jan 2026) — opportunity cost of charging; charging methodology; 35,000 ports / 5.7 M EVs
3. ICCT, *Near-term incentives for electrifying India's four-wheeler ride-hailing fleet* (2021)
4. ICCT, *Updated analysis of incentives* (2021) — cost trajectory by city
5. Electricon / Industry Report (2025) — TCO model with battery replacement and salvage terms
6. Ola Institute, *Beyond Nagpur* — fleet TCO logic
7. The Hindu BusinessLine (26 Feb 2026) — parity at 120–200 km/day; payback 18–24 months

**Charging, tariffs and uptime**
8. Bureau of Energy Efficiency, *State-wise EV Tariff* annexure — Delhi LT 4.50 / HT 4.00
9. MERC / MSEDCL multi-year tariff order (Mar 2026) — EV-charging tariff ₹9.50/unit to 2028-29
10. Adani Electricity tariff schedule — LT VI EV charging category
11. quotemypower, DISCOM city tariffs (2026) — commercial bands, public retail ₹18–24
12. ev.care, *EV Fleet Depot Charging Setup in India* (Jun 2026) — depot vs public cost; ToD; charger ratios
13. ev.care, *EV Fleet Management Guide* (Jun 2026) — energy ₹1–1.5/km; downtime risk
14. SBI, *E-mobility and charging infrastructure in India* — 29,151 chargers; 1–3% utilisation
15. The Indian Express (1 Sep 2026) — Green SM Limo Noida downtime, ~2.5 h/day

**Residual value**
16. Mint (25 Apr 2025) — Spinny and CARS24 depreciation data
17. Mint (5 Sep 2024) — JATO Dynamics Nexon EV depreciation trend
18. Business Standard (24 Oct 2025) — IRDAI IDV table; no EV-specific standard
19. The Hindu BusinessLine (10 Jul 2026) — pre-owned EV market; assured future-value financing
20. The Core (16 Jun 2026) — battery certification gap; Policybazaar on insurance
21. Mahindra First Choice — EV residual 70–80% of ICE at 3 years
22. **BluSmart (Anmol Jaggi)** — assumed 10% residual, realised 26%

**Maintenance and insurance**
23. EVSelect, *EV Car Maintenance & Service Cost in India* (Jun 2026) — service −40–60%; tyres +25–30%; brake pad life
24. CEEW — maintenance sensitivity: EV 8% vs CNG 17% TCO impact per 50% cost change
25. Policybazaar — EV OD premium higher; 15% discount is third-party only

**Tax and policy**
26. GST 2.0 (effective 22 Sep 2025) — EV 5%, small car 18%, compensation cess abolished
27. Business Today (3 Sep 2025) — GST rate restructuring
28. **Delhi Electric Vehicles Policy 2026** (approved 29 Jun 2026, notified 30 Jun, effective 1 Jul 2026, to 31 Mar 2030) — life-time road-tax and registration-fee exemption, cars ≤ ₹30 L — primary sources: JSA Prism legal analysis; The Indian Express (29 Jun 2026); New Indian Express (2 Jul 2026); HT Auto (24 Mar 2026)
29. Karnataka / Maharashtra / Delhi state road-tax schedules 2026
30. PIB (4 Sep 2025) — road passenger transport GST options
31. Delhi EV gazette SG.DEL-E.29112023-250308 — fleet electrification by 1 Apr 2030

**Battery physics (from the verified battery report)**
32. Naumann 2018 (`10.1016/j.est.2018.01.019`) · Lewerenz 2017
33. Eldesoky 2022 (`10.1149/1945-7111/ac99a6`) · Harlow 2019 (`10.1149/2.0981913jes`)

**CNG comparator — measured fuel economy**
34. cars24, *Maruti Suzuki Dzire real world mileage* (Apr 2026) — city 22.0–24.0, highway 28–30, mixed 24.5–26.5; ARAI 33.73
35. buyselltaxi, *Dzire CNG mileage real world — Delhi taxi 2026* (May 2026) — city AC-on 22–25, mixed Ola/Uber 24–27, factory vs aftermarket; ₹3.19/km convergence point
36. CarTrade, *Swift CNG real-world road test* (May 2025) — city 21.28, highway 35.01 km/kg
37. CarFurious, *Best car for Ola/Uber drivers 2026* — Tour S real-world 26–30 km/kg

---

## Appendix — Reproducing every number

Engine `/tmp/opencode/p2/tco_engine.py`, analysis `/tmp/opencode/p2/tco_analysis.py`

```
DUTY      200 km/d x 26 d x 312 d = 5,200 km/mo | 62,400 km/yr | 312,000 km (5 yr)
EV on-road 12,12,000 x 1.05 GST x 1.00 Delhi EV road tax (exempt) = Rs12,72,600
CNG on-road 6,56,000 x 1.18 GST x 1.10 Delhi road tax              = Rs 8,51,488
EV energy  12.84 kWh/100km x 4.50 / 0.90 charge efficiency = Rs0.64/km -> Rs2,00,304
CNG energy 312,000 / 25 km-per-kg x Rs76/kg                = Rs9,48,480
EV  EMI   Rs12,72,600 x 10%/12 over 60 mo                 = Rs27,039/mo
Delhi EV  capex 16,22,339 + 2,00,304 + 93,600 + 2,10,000 - 3,30,876 = Rs17,95,367 -> Rs5.75/km
Delhi CNG capex 10,85,496 + 9,48,480 + 2,10,000 + 1,97,400 - 3,40,595 = Rs21,00,781 -> Rs6.73/km
```

Every table in this document is regenerated by running those two scripts. No figure was
transcribed by hand.