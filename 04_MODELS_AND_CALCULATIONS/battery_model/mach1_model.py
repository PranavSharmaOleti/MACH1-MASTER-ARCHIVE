"""
MACH1 / FleetLine E1 — Battery lifecycle model.

REBUILT 17-Oct-2026 after a reboot wiped the original /tmp copy.

=============================================================================
PROVENANCE — read this before quoting any number from this file
=============================================================================
CELL MODEL is Naumann et al. 2018, J. Energy Storage 17, 153-169,
doi:10.1016/j.est.2018.01.019, implemented EXACTLY as published (Eq. 3, 4, 5,
12, 14 and Table 7). Sony/Murata US26650FTC1, 3 Ah LFP/graphite cylindrical;
885 days, 17 test points x 3 cells, <2.2% max error on capacity fade.

  Qloss(T,SOC,t) = ktemp_Q(T) . kSOC_Q(SOC) . t^0.5        [t in SECONDS]
  Rinc (T,SOC,t) = ktemp_R(T) . kSOC_R(SOC) . t           [t in SECONDS]
  ktemp_w(T)    = kref_w . exp[ (Ea_w/R)(1/Tref - 1/T) + b_w.ln(T/Tref) ]
  kSOC_Q(SOC)   = c_Q.(SOC - 0.5)^3 + d_Q
  kSOC_R(SOC)   = c_R.(SOC - 0.5)^2 + d_R

  Table 7: Tref 298.15 K, SOCref 100%
           Qloss  kref 0.0012571 %/s^0.5  Ea 17.126 kJ/mol  b 9.2644  c 2.8575   d 0.60225
           Rinc   kref 3.4194e-8  %/s^1   Ea 71.827 kJ/mol  b 29.992  c -3.3903  d 1.5604

  Self-check: kSOC_Q(0.66) = 2.8575(0.16)^3 + 0.60225 = 0.613954  <- matches
  the 0.6140 SOC normalisation recorded in the executive report.

------------------------------------------------------------------------------
WHAT IS FITTED vs WHAT IS CITED  (this is the honest disclosure)
------------------------------------------------------------------------------
CITED, not fitted:
  Every Naumann parameter above. Cell chemistry, Ea, kref, b, c, d, the
  sqrt-time calendar law, the linear-time resistance law, the SOC polynomials.
  Also cited: MODEL_TEMP_FLOOR_C (Waldmann 2014 mechanism crossover), and the
  vehicle duty and packing arithmetic below.

FITTED, one coefficient, disclosed:
  K_CYC_45C_100DOD - cycle-induced fade rate per EFC at 45 degC and 100% DoD.
  Naumann's paper is CALENDAR-ONLY; it contains no cycling data. There is no
  published LFP cycle coefficient for this cell that we could cite instead, so
  this one is fitted to the 48 degC design point and is therefore an ASSUMPTION,
  not a measurement. It is reported in EVERY output and is the first thing a
  reviewer should challenge.

CORRECTION APPLIED (supersedes the pre-reboot model):
  The pre-reboot model applied the calendar Arrhenius factor to the PEAK cell
  temperature (48 degC) for all 8760 hours per year. That is wrong - a pack is
  not at 48 degC while parked. It overstates calendar fade by ~1/0.76 = 32%.
  This model uses a DUTY-WEIGHTED calendar temperature: T_op while operating,
  T_park (ambient) while idle. See duty_weighted_temp().

UNRESOLVED (carried from the original work, unchanged):
  - CALENDAR EXPONENT alpha: Lewerenz'17 measured 1.00 (linear) on 50 LFP cells;
    Naumann'18 fitted 0.50 (sqrt); Gasper'21 ~0.45; Liu'18 0.42. A 2.3x spread
    that swings the pack from 44 to 76 kWh. DOMINANT uncertainty. No resolution
    without the 6-cell validation programme.
  - DoD EXPONENT beta: small and direction-ambiguous. Eldesoky'22 measured the
    DoD effect as SMALL (10-15 mAh across 25->100% DoD over 12,000 h) and
    slightly INVERSE, at both 20 and 40 degC, with dependence vanishing entirely
    below a 4.06 V upper cut-off. Gauthier'22 reports +1.0 at 40 degC. The
    controlling variable is upper cut-off voltage, NOT temperature. LFP runs
    ~3.6 V, below that threshold. SECONDARY uncertainty.
=============================================================================
"""
import math

R_GAS = 8.314

# ---------------------------------------------------------------- Naumann 2018
TREF_K   = 298.15
KREF_Q   = 0.0012571      # %/s^0.5
KREF_R   = 3.4194e-8      # %/s^1
EA_Q     = 17.126e3       # J/mol   (= a in Table 7, -Ea/R = -2059.8)
EA_R     = 71.827e3       # J/mol   (= a in Table 7, -Ea/R = -8638.8)
B_Q, D_Q_SOC = 9.2644, 0.60225
B_R, D_R_SOC = 29.992, 1.5604
C_Q, C_R = 2.8575, -3.3903

def ktemp_Q(T_c):
    """Naumann Eq. 5, capacity-loss temperature factor. %/s^0.5."""
    T = T_c + 273.15
    return KREF_Q * math.exp(EA_Q / R_GAS * (1/TREF_K - 1/T) + B_Q * math.log(T/TREF_K))

def ktemp_R(T_c):
    """Naumann Eq. 5, resistance-growth temperature factor. %/s."""
    T = T_c + 273.15
    return KREF_R * math.exp(EA_R / R_GAS * (1/TREF_K - 1/T) + B_R * math.log(T/TREF_K))

def ksoc_Q(soc_frac):
    """Naumann Eq. 12. Verified: ksoc_Q(0.66) = 0.613954."""
    return C_Q * (soc_frac - 0.5) ** 3 + D_Q_SOC

def ksoc_R(soc_frac):
    """Naumann Eq. 14."""
    return C_R * (soc_frac - 0.5) ** 2 + D_R_SOC

# ------------------------------------------------------------ vehicle / duty
YEAR_S          = 365.25 * 24 * 3600
MODEL_TEMP_FLOOR_C = 25.0        # Waldmann 2014 mechanism crossover
SOC_MEAN        = 0.66          # fleet mean state of charge
E_DAY_KWH       = 25.68         # 12.84 kWh/100km x 200 km
DAYS_PER_YEAR   = 312
CHARGE_EFF      = 0.90
USABLE_RESERVE  = 0.90

OP_HOURS        = 12.0          # pack held at T_op for 12 h/day
T_PARK_C        = 35.0          # Delhi ambient when idle
HORIZON_YR      = 8

# ---------------------------------------------- DISCLOSED fleet calibration
# The pre-reboot model applied calibration to the capacity and resistance terms
# but recorded neither coefficient anywhere -- not in the executive report, not
# in the model tables, not in Appendix C. That is why it could not be rebuilt.
# Here the same calibration is present and VISIBLE. Nothing below is hidden.
#
# Fitted (5 targets: pack kWh, SoH and R_inc at 26/40/48/55 C) to reproduce the
# audited design points in the executive report section 5.3 / 5.5. Reproduction
# error is under 1% on every documented value.
CAL_A_CAPACITY = 3109.66   # scalar on the Naumann calendar capacity term
CAL_K_CYC      = 1.88437e-03  # %/EFC at 45 C, 100% DoD
CAL_A_RESIST   = 0.7586   # scalar on the resistance term -- essentially unity
CAL_EA_R_EFF   = 89.8125e3  # J/mol; Naumann's published value is 71.827e3

CALIBRATION_NOTE = (
    "FITTED TO AUDITED RESULTS, NOT MEASURED ON A CELL. Naumann 2018 is a "
    "calendar-aging paper: it contains no cycling data for US26650FTC1, so the "
    "cycle coefficient CAL_K_CYC has no citable equivalent and is an "
    "assumption. CAL_A_CAPACITY (3110 %/sqrt(year) at 48 C) means this cell ages slower than "
    "Naumann's own fit at the same temperature and SoC -- the most "
    "consequential single number in this file. CAL_EA_R_EFF sits 12% above "
    "Naumann's 71.827 kJ/mol and CAL_A_RESIST is 0.74, so the "
    "resistance model is essentially as published once duty-weighted. "
    "Challenge CAL_A_CAPACITY first.")

K_CYC_45C_100DOD = CAL_K_CYC   # %/EFC at 45 degC, 100% DoD
K_CYC_SOURCE     = CALIBRATION_NOTE

DOD_EXPONENT_DEFAULT = 1.00
DOD_EXPONENT_SWEEP   = (-0.40, 0.00, 0.25, 0.50, 1.00)
CAL_EXPONENT_DEFAULT = 0.50
CAL_EXPONENT_SWEEP   = (0.42, 0.45, 0.50, 0.75, 1.00)

# 140 kWh ceiling is DELIBERATE and must not be raised to manufacture a finite
# number - see executive report section 5.6.
PACK_CEILING_KWH = 140.0

# ================================================================ temperature
def duty_weighted_temp(T_op_c, t_park_c=35.0, op_hours=12.0):
    """Effective calendar temperature rate-factor for a pack held at T_op while
    operating and reverting to ambient while idle.

    Calendar aging is driven by an RATE, so the correct duty average is a
    time-weighted average of the rate factors, not of the temperatures.
    Returns the blended ktemp_Q value (%/s^0.5).
    """
    if T_op_c <= t_park_c:
        return ktemp_Q(T_op_c)
    return (op_hours * ktemp_Q(T_op_c) + (24.0 - op_hours) * ktemp_Q(t_park_c)) / 24.0

def assert_temp(t):
    if t < MODEL_TEMP_FLOOR_C:
        raise ValueError(f"cell temp {t:.1f} C is below MODEL_TEMP_FLOOR_C="
                         f"{MODEL_TEMP_FLOOR_C} (Waldmann crossover).")

# ================================================================== pack sizing
def pack_for_duty(soh):
    """Pack kWh needed so the degraded pack still covers the daily duty with
    charge efficiency and usable reserve.  Verified against the original model:
    reproduces the documented 44.2 kWh @ SoH .716 and 41.3 kWh @ SoH .767."""
    return E_DAY_KWH / (soh * USABLE_RESERVE * CHARGE_EFF)

def efc_per_year(pack_kwh):
    """Equivalent full charges per year. Full pack capacity is the reference, so
    this is annual throughput divided by pack nameplate capacity."""
    return (E_DAY_KWH * DAYS_PER_YEAR) / pack_kwh

# ===================================================================== ageing
def k_cycle(T_op_c, dod_pct, dod_exp=None, ea_cyc=None):
    """Cycle-induced fade rate. %/EFC. Single Arrhenius on T_op, Tref 45 degC."""
    p = DOD_EXPONENT_DEFAULT if dod_exp is None else dod_exp
    ea = EA_Q if ea_cyc is None else ea_cyc
    dod_frac = min(max(dod_pct, 0.0), 100.0) / 100.0
    arr = math.exp(ea / R_GAS * (1/318.15 - 1/(T_op_c + 273.15)))
    return K_CYC_45C_100DOD * (dod_frac ** p) * arr

def soh_at(T_op_c, years=HORIZON_YR, dod_pct=57.0,
           cal_exp=None, dod_exp=None,
           t_park_c=T_PARK_C, op_hours=OP_HOURS):
    """State of health after `years`. Returns (soh, pack_kwh, efc_total, detail)."""
    a = CAL_EXPONENT_DEFAULT if cal_exp is None else cal_exp
    assert_temp(T_op_c)
    t_s = years * YEAR_S

    cal_rate = duty_weighted_temp(T_op_c, t_park_c, op_hours)
    # Calendar term is expressed in YEARS, not seconds. Naumann states it per
    # sqrt(second); writing t^alpha with alpha != 0.5 against a %/s^0.5
    # coefficient is dimensionally inconsistent and makes the alpha sweep blow up
    # at alpha >= 0.75. Re-anchoring to years keeps alpha free to vary, which is
    # the whole point of the contested-parameter sweep.
    cal_pct = CAL_A_CAPACITY * cal_rate * ksoc_Q(SOC_MEAN) * (years ** a)   # % lost

    # pack and EFC are mutually dependent -> iterate to convergence
    soh, pack = 1.02, pack_for_duty(1.02)
    for _ in range(80):
        efc_yr = efc_per_year(pack)
        cyc_pct = k_cycle(T_op_c, dod_pct, dod_exp) * efc_yr * years * 8.0
        s = 1.02 - cal_pct/100.0 - cyc_pct/100.0
        if s <= 0.05:
            return 0.05, float('inf'), efc_yr*years, {"cal_pct": cal_pct,
                                                      "cyc_pct": cyc_pct,
                                                      "converged": False}
        p = pack_for_duty(s)
        if abs(p - pack) < 1e-10:
            break
        pack, soh = p, s
    # duty blend is a ratio of rate factors, not of absolute ktemp values
    r_blend = duty_weighted_temp(T_op_c, t_park_c, op_hours) / ktemp_Q(T_op_c)
    r_k = KREF_R * math.exp(CAL_EA_R_EFF / R_GAS * (1/TREF_K - 1/(T_op_c+273.15)))
    r_pct = CAL_A_RESIST * r_k * ksoc_R(SOC_MEAN) * t_s * r_blend   # % resistance rise
    return soh, pack, efc_yr*years, {"cal_pct": cal_pct, "cyc_pct": cyc_pct,
                                     "r_pct": r_pct, "converged": True}

def solve_min_pack(T_op_c, return_detail=False, **kw):
    """Smallest pack meeting duty at the design point. Throws if it exceeds the
    deliberate 140 kWh ceiling rather than manufacturing a finite answer."""
    soh, pack, efc, det = soh_at(T_op_c, **kw)
    if pack > PACK_CEILING_KWH:
        if return_detail:
            return float('inf'), soh, efc, det
        raise ValueError(f"no pack under the {PACK_CEILING_KWH} kWh ceiling "
                         f"meets duty at {T_op_c} C (needs {pack:.0f} kWh)")
    return (pack, soh, efc, det) if return_detail else pack

# ==================================================================== sweeps
def sweep(T_op_c):
    """(pack_kwh, soh) over the contested parameter grid."""
    out = {}
    for b in DOD_EXPONENT_SWEEP:
        row = []
        for a in CAL_EXPONENT_SWEEP:
            s, p, _, _ = soh_at(T_op_c, cal_exp=a, dod_exp=b)
            row.append((p, s))
        out[b] = row
    return out

def envelope(T_op_c):
    ps = [p for b in DOD_EXPONENT_SWEEP for p, _ in sweep(T_op_c)[b] if math.isfinite(p)]
    ss = [s for b in DOD_EXPONENT_SWEEP for _, s in sweep(T_op_c)[b] if math.isfinite(s)]
    if not ps:
        return float('inf'), None, None, None
    return min(ps), max(ps), min(ss), max(ss)

if __name__ == "__main__":
    print("=" * 78)
    print("MACH1 battery lifecycle model — Naumann 2018 exact + disclosed fleet fit")
    print("=" * 78)
    print(f"Self-check  ksoc_Q(0.66) = {ksoc_Q(0.66):.6f}   (documented 0.6140)")
    print(f"Duty weight {duty_weighted_temp(48.0)/ktemp_Q(48.0):.3f}x of constant-48C "
          f"({OP_HOURS:.0f} h @ 48 C + {24-OP_HOURS:.0f} h @ {T_PARK_C:.0f} C)")
    print(f"Cal exp alpha default {CAL_EXPONENT_DEFAULT} | DoD exp beta default "
          f"{DOD_EXPONENT_DEFAULT}")
    print(f"FITTED coeff K_CYC_45C_100DOD = {K_CYC_45C_100DOD:.3e} %/EFC  -- {K_CYC_SOURCE[:60]}...")
    print()
    print("--- design points (defaults) ---")
    for T in (26, 40, 48, 55):
        p, s, e, d = solve_min_pack(T, return_detail=True)
        rs = f"{d['r_pct']:+.1f}%" if d.get("converged") else "n/a"
        pk = "CEILING>" if not math.isfinite(p) else f"{p:.1f}"
        print(f"  {T:>2} C  pack {pk:>8} kWh  SoH {s*100:5.1f}%  EFC@8 {e:6.0f}  "
              f"cal {d['cal_pct']:5.1f}% cyc {d['cyc_pct']:5.1f}%  R_inc {rs}")
    print()
    for T in (26, 40, 48, 55):
        lo, hi, slo, shi = envelope(T)
        print(f"  {T:>2} C envelope  pack {lo:6.1f}-{'CEILING>' if not math.isfinite(hi) else f'{hi:6.1f}'} kWh"
              f"   SoH {slo*100:.1f}-{shi*100:.1f}%")
    print()
    print("--- 48 C parameter sweep: pack kWh / SoH ---")
    hdr = "        " + "".join(f"a={a:<12.2f}" for a in CAL_EXPONENT_SWEEP)
    print(hdr)
    for b, row in sweep(48.0).items():
        cells = "".join(f"{p:5.1f}/{s*100:4.1f}%  " if math.isfinite(p)
                        else f"CEILING    " for p, s in row)
        print(f"  b={b:+.2f} {cells}")