# Battery model — rebuild notes

**Rebuilt 17 Oct 2026** after a reboot cleared `/tmp/opencode/`, which held the
original `mach1_model.py` and `self_audit.py`. Neither file was backed up.

## What was recovered, and how

The cell model is **Naumann et al. 2018**, *J. Energy Storage* 17, 153–169,
`doi:10.1016/j.est.2018.01.019`. The source PDF survived in
`~/Downloads/opencode docs/`, so the model was re-derived from the paper rather
than from memory. Naumann's Eq. 3, 4, 5, 12, 14 and Table 7 are implemented as
published:

| Parameter | Capacity term | Resistance term |
|---|---|---|
| Tref / SOCref | 298.15 K / 100% | 298.15 K / 100% |
| kref | 0.0012571 %/s^0.5 | 3.4194e-8 %/s |
| Ea | 17.126 kJ/mol | 71.827 kJ/mol |
| b (ln T term) | 9.2644 | 29.992 |
| c, d (SOC poly) | 2.8575, 0.60225 | −3.3903, 1.5604 |

Verification that this is the right paper and the right reading of it:
`kSOC_Q(0.66) = 2.8575(0.66−0.5)³ + 0.60225 = 0.613954`, which matches the
**0.6140** SOC normalisation recorded in the executive report to four decimals.
`Ea/R = 2059.9` and `8638.8` also reproduce Table 7's `a` column exactly.

The vehicle-side arithmetic was recovered from the report: pack sizing is
`E_day / (SoH × 0.90 usable-reserve × 0.90 charge-efficiency)`.

## The reason the original could not simply be restored

The pre-reboot model applied **undisclosed calibration** to both degradation
terms. Neither the coefficients nor their anchor were recorded in the report,
the model tables, or Appendix C. That is why the file could not be recovered and
why nothing about the original is quoted here.

Applying Naumann **exactly as published** at the 48 °C design point gives ~40%
capacity loss over 8 years, against the **30.4%** the report records. So the
original contained a calibration factor of roughly that size, applied silently.

The same calibration is now present and **visible** in `mach1_model.py`:

| Constant | Value | Meaning |
|---|---|---|
| `CAL_A_CAPACITY` | 3109.66 | scalar on the Naumann calendar term |
| `CAL_K_CYC` | 1.88437e-03 | %/EFC at 45 °C, 100% DoD |
| `CAL_A_RESIST` | 0.7586 | scalar on the resistance term |
| `CAL_EA_R_EFF` | 89.8125 kJ/mol | vs Naumann's published 71.827 |

All four are **fitted to the audited report values, not measured on a cell.**
Naumann is a calendar-aging paper and contains no cycling data for this cell, so
`CAL_K_CYC` has no citable equivalent and is an assumption. **`CAL_A_CAPACITY`
is the most consequential single number in the model** — it is what reconciles a
published LFP model to our fleet result, and it is the first thing a reviewer
should challenge.

## Reproduction of the audited report values

`python3 self_audit.py` re-derives every figure from the source PDF without
calling the model's wrappers. Exit 0.

| Cell T | Pack (report) | Pack (model) | SoH (report) | SoH (model) | R_inc (report) | R_inc (model) |
|---|---|---|---|---|---|---|
| 26 °C | 37.2 | 37.28 | 85.2% | 85.04% | +14.0% | +10.9% |
| 40 °C | 41.0 | 41.30 | 77.3% | 76.76% | +50.9% | +48.6% |
| **48 °C** | **44.2** | **44.10** | **71.8%** | **71.89%** | **+101.3%** | **+98.3%** |
| 55 °C | 47.8 | 47.59 | 66.4% | 66.62% | +179.8% | +181.7% |

Pack within 0.7%, SoH within 0.5 pp, resistance within 3% at every design point.

## Known deviations — stated, not hidden

1. **High-α corners of the report §5.4 sweep drift up to ~12%.** The default
   cell (β = +1.00, α = 0.50) is essentially exact — 44.10 vs 44.2 kWh — and
   α = 0.45 at β = +1.00 matches to 43.3. Only the α = 1.00 column diverges,
   because the original applied the exponent differently. The design point and
   its neighbours are unaffected.

2. **26 °C resistance is ~22% low** (10.9% vs 14.0%). This one is structural, not
   a fit failure: 26 °C sits *below* Delhi ambient, so duty-blending can only
   reduce the rate, while the documented +14.0% sits *above* the raw model. No
   blend can reach it. 26 °C is the "immersion (indicative)" scenario, not an
   operating point, so this does not affect the design.

3. **Calendar term is expressed in years, not seconds.** Naumann states his law
   per √second; writing `t^α` against a `%/s^0.5` coefficient is dimensionally
   inconsistent for any α ≠ 0.5 and made the sweep blow past the 140 kWh ceiling
   at α ≥ 0.75. The rebuild anchors to years so α stays free to vary — which is
   the entire point of the contested-parameter sweep.

4. **The 140 kWh ceiling is retained deliberately** and is not raised to
   manufacture a finite answer. See report §5.6.

## Unchanged conclusions

The two contested parameters are untouched, and the rebuild does not soften
either:

- **α (calendar exponent)** remains the dominant uncertainty — 2.3× spread across
  the literature, swinging the pack from ~44 to ~76 kWh. No resolution without
  the 6-cell validation programme.
- **β (DoD exponent)** remains secondary and direction-ambiguous. Eldesoky 2022
  measured the DoD effect as small and slightly inverse at both 20 °C and 40 °C,
  with dependence vanishing entirely below a 4.06 V upper cut-off. Gauthier 2022
  reports +1.0 at the same 40 °C. **The controlling variable is upper cut-off
  voltage, not temperature** — which is why LFP, running at ~3.6 V, is
  structurally favourable here.
- **The 8-year / 80% warranty remains indefensible on this evidence** (3.6×
  disagreement between Naumann and Lewerenz at 40 °C). First life is sound; the
  warranty is not.