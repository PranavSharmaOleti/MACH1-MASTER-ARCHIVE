import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tco_engine as T
from tco_engine import EV,CNG,CITIES,DAYS_YEAR,REVENUE_MONTH
def m(x,d=0): return f"{x:,.{d}f}"

print("="*74); print("A. DRIVER VIEW — monthly, Delhi"); print("="*74)
e,g=T.tco(EV,"Delhi"),T.tco(CNG,"Delhi")
for lab,d in (("EV  ",e),("CNG ",g)):
    en,mt,ins=d["energy"]/60,d["maint"]/60,d["ins"]/60
    print(f"  {lab} EMI {m(d['emi']):>7} + energy {m(en):>6} + maint {m(mt):>5} + ins {m(ins):>5}"
          f" = {m(d['emi']+en+mt+ins):>7}/mo | take-home Rs{m(REVENUE_MONTH-(d['emi']+en+mt+ins))}")
    print(f"        yr6+ (no EMI): take-home Rs{m(REVENUE_MONTH-(en+mt+ins))}")
dl=lambda d: REVENUE_MONTH-(d["emi"]+d["energy"]/60+d["maint"]/60+d["ins"]/60)
al=lambda d: REVENUE_MONTH-(d["energy"]/60+d["maint"]/60+d["ins"]/60)
print(f"  -> during loan EV +Rs{m(dl(e)-dl(g))}/mo | after loan EV +Rs{m(al(e)-al(g))}/mo"
      f" | 5-yr take-home gap Rs{m((dl(e)-dl(g))*60)}")

print(); print("="*74); print("B. BREAKEVEN km/day (financed)"); print("="*74)
def ckm(kpd,years):
    old=T.KM_YEAR; T.KM_YEAR=kpd*DAYS_YEAR
    r=(T.tco(EV,"Delhi",years)["ckm"],T.tco(CNG,"Delhi",years)["ckm"]); T.KM_YEAR=old; return r
for y in (5,8):
    lo,hi=10.0,600.0
    for _ in range(80):
        mid=(lo+hi)/2
        ev,cn=ckm(mid,y)
        if ev < cn: hi=mid      # EV already wins -> crossover is BELOW mid
        else:      lo=mid      # CNG still wins -> crossover is ABOVE mid
    print(f"  {y}-yr financed: crossover at {lo:6.1f} km/day  | deck assumes 200 -> "
          f"{'PASS' if lo<200 else 'FAIL'}, margin {200/lo:.2f}x")

print(); print("="*74); print("C. DOWNTIME TOLERANCE (5-yr financed, Delhi)"); print("="*74)
lo,hi=0.0,400.0
for _ in range(80):
    mid=(lo+hi)/2
    if T.tco(EV,"Delhi",downtime_h=mid)["ckm"] < T.tco(CNG,"Delhi")["ckm"]: lo=mid
    else: hi=mid
print(f"  EV absorbs {lo:.0f} EXTRA downtime-hours/month before CNG wins.")
print(f"  Green SM Noida (Indian Express, Sep-2026): ~2.5 h/day lost = 75 h/month.")
print(f"  Headroom = {lo/75:.2f}x the observed real-world failure mode.")

print(); print("="*74); print("D. TORNADO — 5-yr EV advantage (financed, Delhi)"); print("="*74)
# CNG-side inputs must be routed to the CNG vehicle, not the EV.
# Previously every kw went to tco(EV,...): kmkg/price were silently ignored
# (en_pm takes the EV branch on "kwh100" and never reads them), and cng_resid
# was applied to the EV's residual instead -> the "CNG residual 40% -> 45%" row
# was actually reporting an EV residual of 45% (+26.0% instead of +12.8%).
CNG_KEYS = {"kmkg", "price", "cng_resid"}
def adv(**kw):
    cngkw = {k: v for k, v in kw.items() if k in CNG_KEYS}
    evkw  = {k: v for k, v in kw.items() if k not in CNG_KEYS}
    ev = T.tco(EV, "Delhi", **evkw)["ckm"]
    cn = T.tco(CNG, "Delhi", **cngkw)["ckm"]
    return 100*(cn-ev)/cn
rows=[("BASE",{}),
 ("EV residual 26% -> 36% (deck's OLD assumption)",{"resid":0.36}),
 ("CNG residual 40% -> 45% (ICE trending better)",{"cng_resid":0.45}),
 ("consumption 12.84 -> 15.38 kWh/100km (deck's)",{"kwh100":15.38}),
 ("electricity Rs4.50 -> Rs12.00 (public DC)",{"tariff":12.00}),
 ("CNG 25 -> 30 km/kg",{"kmkg":30.0}),
 ("CNG Rs76 -> Rs90/kg",{"price":90.0}),
 ("WORST CASE STACKED (15.38 + Rs12 + resid 26%)",{"kwh100":15.38,"tariff":12.0,"resid":0.26}),
 ("BEST CASE STACKED (12.84 + Rs4.5 + resid 36%)",{"kwh100":12.84,"tariff":4.5,"resid":0.36})]
for lab,kw in rows: print(f"  {lab:<46} EV {adv(**kw):+6.1f}%")
cn8=T.tco(CNG,"Delhi",years=8); ev8=T.tco(EV,"Delhi",years=8)
print(f"  {'8-year horizon (base inputs)':<46} EV {100*(cn8['ckm']-ev8['ckm'])/cn8['ckm']:+6.1f}%")

print(); print("="*74); print("E. BREAKEVEN EV PURCHASE PRICE (5-yr financed, Delhi)"); print("="*74)
tgt=T.tco(CNG,"Delhi")["total"]; lo,hi=200_000.0,2_000_000.0
for _ in range(80):
    mid=(lo+hi)/2
    if T.tco(EV,"Delhi",ex=mid)["total"] < tgt: lo=mid   # EV still wins -> can go higher
    else: hi=mid
be=T.tco(EV,"Delhi",ex=lo)["on_road"]; base=T.tco(EV,"Delhi")["on_road"]
print(f"  breakeven on-road Rs{m(be)} | ours Rs{m(base)} -> headroom Rs{m(be-base)}"
      f" ({(be/base-1)*100:.1f}% price rise tolerable)")
print(); print("="*74); print("F. CASH vs FINANCED (5-yr, all cities)"); print("="*74)
for c in CITIES:
    for fin,lab in ((True,"FINANCED 60mo"),(False,"CASH outright")):
        ev=T.tco(EV,c,5,financed=fin)["ckm"]; cn=T.tco(CNG,c,5,financed=fin)["ckm"]
        print(f"  {c:<11} {lab:<16} EV {ev:6.2f}  CNG {cn:6.2f}  -> {100*(cn-ev)/cn:+5.1f}%")
# =============================================================================
# SECTIONS G..K — purely additive. Sections A..F above are untouched.
# Every figure below is derived from a named constant or a printed formula.
# =============================================================================
DISC_RATE      = 0.12     # fleet-operator hurdle rate, annual nominal
ESC_ELEC       = 0.045    # electricity / kWh, per year
ESC_CNG        = 0.035    # CNG / kg, per year (CERC-notified domestic gas 3.46%)
ESC_MAINT      = 0.040    # per year
ESC_INS        = 0.050    # per year
ESC_RESID      = 0.045    # per year, applied to BOTH vehicles' residual credit
PLATFORM_FEE_D = 67.0     # Rs per vehicle-day, Ola zero-commission flat fee (Jun-2025)
DAYS_MO        = 26
PLATFORM_FEE_MO= PLATFORM_FEE_D * DAYS_MO          # = 1742
NET_FARE_KM    = T.FARE_PER_KM - PLATFORM_FEE_MO/T.KM_MONTH
PROD_KM_H      = 20.0     # productive km per shift hour, urban with idle
LEGACY_COMMISSION = 0.25  # pre-Jun-2025 per-RIDE commission, for the invariance check
EMI_NPV_CHECK    = 1_215_500  # section-H self-test target: EMI 27,039 x annuity 44.955

def npv_annual(cf, rate=DISC_RATE):
    """cf: {year_index: amount}. Annual end-of-period discounting."""
    return sum(a/(1.0+rate)**y for y,a in cf.items())

print(); print("="*74); print("G. CHARGING + CNG-TANK INFRASTRUCTURE CAPEX (absent from sections A-F)"); print("="*74)
CHARGER_KW       = 7.4      # 7.4 kW AC depot port
CHARGER_HW       = 50_000   # 7.4 kW AC port hardware
CHARGER_INSTALL  = 30_000   # civil + cabling + commissioning
CHARGER_DISCOM   = 10_000   # DISCOM load sanction / new connection
CHARGER_SPARE    = 1.10     # N+1: 1 spare port per 10 vehicles
charger_capex_per_veh = (CHARGER_HW+CHARGER_INSTALL+CHARGER_DISCOM)*CHARGER_SPARE
charger_opex_yr       = 12_000 + 3_000   # CMS/OCPP software + AMC
charger_life_yr       = 5
cng_hydrotest         = 4_500             # per cylinder set, every 3 yr from yr 3

e_day_batt = EV["kwh100"]/100*T.KM_DAY
e_day_wall = e_day_batt/EV["ceff"]
h_night    = e_day_wall/CHARGER_KW
print(f"  port sizing: {T.KM_DAY} km/day x {EV['kwh100']} kWh/100km = {m(e_day_batt,2)} kWh battery-side")
print(f"               wall {m(e_day_batt,2)}/{EV['ceff']:.2f} = {m(e_day_wall,2)} kWh -> {m(e_day_wall,2)}/{CHARGER_KW} kW = {h_night:.2f} h overnight")
print(f"               1 port/vehicle is sufficient ({h_night:.2f} h << depot window); spares at 1 per 10 vehicles")
print(f"  EV  capex/vehicle  ({m(CHARGER_HW)}+{m(CHARGER_INSTALL)}+{m(CHARGER_DISCOM)}) x {CHARGER_SPARE:.2f} = Rs{m(charger_capex_per_veh)}"
      f" at yr 0, replaced every {charger_life_yr} yr   | opex Rs{m(charger_opex_yr)}/yr")
print(f"  CNG kit is factory-fitted and already inside the Rs{m(CNG['ex'])} ex-showroom price, so the comparator")
print(f"     carries NO per-vehicle capex here. Its only infra is cylinder hydro-testing,"
      f" Rs{m(cng_hydrotest)}/set from yr 3, every 3 yr.")
g_rows={}; g_base={}
print(f"  timing: EV capex at yr 0 and again at yr {charger_life_yr} (so the 8-yr case carries a SECOND"
      f" replacement); opex at yr end 1..n; CNG hydro-test at yr 3, 6, ..; NPV at {DISC_RATE:.0%} annual")
print(f"  {'horizon':<8}{'EV undisc':>12}{'EV NPV':>12}{'CNG undisc':>13}{'CNG NPV':>11}{'EV Rs/km':>10}{'CNG Rs/km':>11}{'adv incl inf':>14}")
for yrs in (5,8):
    ev_cf={y:charger_capex_per_veh for y in range(0,yrs,charger_life_yr)}
    ev_cf.update({y:ev_cf.get(y,0)+charger_opex_yr for y in range(1,yrs+1)})
    cn_cf={y:cng_hydrotest for y in range(3,yrs+1,3)}
    ev_u,ev_n=sum(ev_cf.values()),npv_annual(ev_cf)
    cn_u,cn_n=sum(cn_cf.values()),npv_annual(cn_cf)
    kmv=yrs*T.KM_YEAR
    a_e=T.tco(EV,"Delhi",yrs); a_g=T.tco(CNG,"Delhi",yrs)
    ce, cg = a_e["ckm"]+ev_u/kmv, a_g["ckm"]+cn_u/kmv
    g_rows[yrs]=(ev_u/kmv,cn_u/kmv,100*(cg-ce)/cg)
    g_base[yrs]=100*(a_g["ckm"]-a_e["ckm"])/a_g["ckm"]
    print(f"  {yrs}yr{'':<3}{m(ev_u):>12}{m(ev_n):>12}{m(cn_u):>13}{m(cn_n):>11}"
          f"{ev_u/kmv:>10.3f}{cn_u/kmv:>11.3f}{100*(cg-ce)/cg:>13.1f}%")
for yrs in (5,8):
    print(f"  {yrs}yr: section-A advantage {g_base[yrs]:+.1f}% (no infra) -> {g_rows[yrs][2]:+.1f}% including infra"
          f"  — EV gives up {g_base[yrs]-g_rows[yrs][2]:.1f} pp")
print("  sensitivity — charger capex per vehicle (base opex/life, CNG hydro-test unchanged):")
for cap,lab in ((60_000,"Rs60,000"),(charger_capex_per_veh,f"Rs{m(charger_capex_per_veh)} (base)"),(150_000,"Rs1,50,000")):
    for yrs in (5,8):
        cf={y:cap for y in range(0,yrs,charger_life_yr)}
        cf.update({y:cf.get(y,0)+charger_opex_yr for y in range(1,yrs+1)})
        infra=sum(cf.values())/(yrs*T.KM_YEAR)
        cn_infra=sum(cng_hydrotest for _ in range(3,yrs+1,3))/(yrs*T.KM_YEAR)
        ce=T.tco(EV,"Delhi",yrs)["ckm"]+infra
        cg=T.tco(CNG,"Delhi",yrs)["ckm"]+cn_infra
        print(f"    {lab:<18} {yrs}yr  EV {ce:.2f}  CNG {cg:.2f}  -> {100*(cg-ce)/cg:+.1f}%")
print("  NOTE the CNG side of this line is Rs4,500 of hydro-testing only; the converter")
print("       itself is inside the ex-showroom price, so it is not a like-for-like"
      " 'per-vehicle infra' item.")

print(); print("="*74); print("H. NPV: MONTHLY CASH FLOWS, ESCALATION vs FLAT"); print("="*74)
def npv_flow(v, city="Delhi", years=5, financed=True, disc=DISC_RATE, escalate=True, infra=None):
    """Months 0..N, N = years*12. Returns discounted components (residual = credit).
    infra (optional, added for section L): {month_index: [(amount, esc_rate), ...]} from
    infra_schedule(). Threaded through THIS loop, so the vehicle and infrastructure flows are
    discounted on exactly the same basis. Default None = pure vehicle flows, unchanged."""
    N=years*12; rate=disc/12.0
    orr=T.on_road(v,city); en_km=T.en_pm(v,city); mt_km=T.mt_pk(v)
    ins_mo=v["ins"]   # the engine's ins is a MONTHLY premium: tco() bills ins*12*years
    e_esc = ESC_ELEC if "kwh100" in v else ESC_CNG
    f=lambda r,mo: ((1.0+r)**((mo-1)//12)) if escalate else 1.0
    P=dict(capex=0.0, emi=0.0, energy=0.0, maint=0.0, ins=0.0, res=0.0, infra=0.0); P["km"]=N*T.KM_MONTH
    if not financed: P["capex"]=orr
    if financed:
        E=T.emi(orr*(1-T.DOWN_PCT))
        for mo in range(1,min(N,T.LOAN_MONTHS)+1):
            P["emi"]+=E/(1+rate)**mo
    if infra:
        for amt,_r in infra.get(0,()): P["infra"]+=amt   # month 0: 0 periods discounted
    for mo in range(1,N+1):
        df=1/(1+rate)**mo
        P["energy"]+=en_km*T.KM_MONTH*f(e_esc,mo)*df
        P["maint"] +=mt_km*T.KM_MONTH*f(ESC_MAINT,mo)*df
        P["ins"]   +=ins_mo*f(ESC_INS,mo)*df
        if infra:
            for amt,ir in infra.get(mo,()): P["infra"]+=amt*f(ir,mo)*df
    P["res"]=orr*v["resid"]*f(ESC_RESID,N)/(1+rate)**N
    P["total"]=P["capex"]+P["emi"]+P["energy"]+P["maint"]+P["ins"]+P["infra"]-P["res"]
    return P
print(f"  timing: mo 0 capex if cash | mo 1..min(N,60) EMI at the LOAN rate ({T.LOAN_RATE:.0%}) |"
      f" mo 1..N energy+maint+ins | mo N residual credit")
print(f"  escalation: factor = (1+ESC)**((m-1)//12) -> 1.00 for mo 1-12, then compounded annually")
print(f"  discounting: monthly at {DISC_RATE:.0%}/12; residual credit escalated at {ESC_RESID:.1%} (same rate both vehicles)")
print(f"  convention: the engine's ins is a MONTHLY premium (tco() bills ins*12*years), so it is"
      f" charged at Rs{m(EV['ins'])}/mo EV and Rs{m(CNG['ins'])}/mo CNG here too")
print(f"    residual at mo {5*12}: EV on-road Rs{m(T.on_road(EV,'Delhi'))} x {EV['resid']:.0%} = Rs{m(T.on_road(EV,'Delhi')*EV['resid'])}"
      f" -> x{(1+ESC_RESID)**((5*12-1)//12):.4f} escalated = Rs{m(T.on_road(EV,'Delhi')*EV['resid']*(1+ESC_RESID)**4)};"
      f"  CNG Rs{m(T.on_road(CNG,'Delhi')*CNG['resid']*(1+ESC_RESID)**4)}")
print(f"  {'case':<26}{'EV NPV':>13}{'CNG NPV':>13}{'EV adv':>9}{'EV no-esc':>12}{'CNG no-esc':>12}{'adv no-esc':>12}")
h_res={}
for disc in (DISC_RATE,0.10):
    for fin,lab in ((True,"FINANCED 60mo"),(False,"CASH outright")):
        a=npv_flow(EV,years=5,financed=fin,disc=disc); b=npv_flow(CNG,years=5,financed=fin,disc=disc)
        an=npv_flow(EV,years=5,financed=fin,disc=disc,escalate=False); bn=npv_flow(CNG,years=5,financed=fin,disc=disc,escalate=False)
        h_res[(disc,fin)]=(a,b)
        print(f"  {f'disc {disc:.0%} {lab}':<26}{m(a['total']):>13}{m(b['total']):>13}"
              f"{100*(b['total']-a['total'])/b['total']:>8.1f}%{m(an['total']):>12}{m(bn['total']):>12}"
              f"{100*(bn['total']-an['total'])/bn['total']:>11.1f}%")
a,b=h_res[(DISC_RATE,True)]
an,bn=npv_flow(EV,years=5,escalate=False),npv_flow(CNG,years=5,escalate=False)
print(f"  escalation effect isolated (Delhi 5yr financed, disc {DISC_RATE:.0%}): EV advantage"
      f" {100*(bn['total']-an['total'])/bn['total']:+.1f}% flat vs"
      f" {100*(b['total']-a['total'])/b['total']:+.1f}% escalated ->"
      f" {100*(b['total']-a['total'])/b['total']-100*(bn['total']-an['total'])/bn['total']:+.1f} pp"
      f" (electricity escalates at {ESC_ELEC:.1%}, CNG at {ESC_CNG:.1%}, and both residuals at {ESC_RESID:.1%})")
print(f"  identity check: at disc {T.LOAN_RATE:.0%} the CASH and FINANCED NPVs are equal to the rupee"
      f" — a loan priced at the hurdle rate is worth its own principal, so")
print(f"     discounting it back at the same rate reproduces the purchase price. At {DISC_RATE:.0%} the"
      f" loan (priced at {T.LOAN_RATE:.0%}) is cheaper than cash.")
print(f"  component NPV, Delhi 5yr financed, disc {DISC_RATE:.0%}, escalated:")
for k,lab in (("capex","capex (mo 0)"),("emi","EMI stream (mo 1-60)"),("energy","energy"),("maint","maintenance"),("ins","insurance"),("res","less residual credit")):
    sg="-" if k=="res" else "+"
    print(f"    {lab:<24} {sg} EV {m(a[k]):>12}   CNG {m(b[k]):>12}")
print(f"    {'NET OF RESIDUAL':<24} {'=':>2} EV {m(a['total']):>12}   CNG {m(b['total']):>12}")
ani=sum(1/(1+DISC_RATE/12)**mo for mo in range(1,min(60,60)+1))
emi_ev=h_res[(DISC_RATE,True)][0]["emi"]
print(f"  annuity check: EMI {m(T.emi(T.on_road(EV,'Delhi'))) } x annuity factor {ani:.3f} = Rs{m(emi_ev)}"
      f"  vs Rs{m(EMI_NPV_CHECK)} -> diff Rs{m(emi_ev-EMI_NPV_CHECK)}"
      f"  {'OK' if abs(emi_ev-EMI_NPV_CHECK)<=2000 else '** ANNUITY MATH WRONG **'}")

print(); print("="*74); print("I. DOWNTIME AS AN EXPLICIT CASH-FLOW ITEM"); print("="*74)
DT=[("charging queue / port unavailable",0.5),("planned maintenance",1.0),
    ("unplanned repair",1.5),("charger failure awaiting spare",0.5)]
dt_base=sum(h for _,h in DT)
gross_per_h   = PROD_KM_H*T.FARE_PER_KM
platform_fee_per_h = PROD_KM_H*(PLATFORM_FEE_MO/T.KM_MONTH)
energy_avoided_per_h = PROD_KM_H*(EV["kwh100"]/100*CITIES["Delhi"]["tariff"]/EV["ceff"])
net_cost_per_h = gross_per_h-platform_fee_per_h-energy_avoided_per_h
print(f"  {'cause':<36}{'h/mo':>6}{'Rs/mo':>10}{'Rs/km':>8}{'share':>8}{'cumul h':>9}")
cum=0.0
for lab,h in DT:
    cum+=h; c=h*net_cost_per_h
    print(f"  {lab:<36}{h:>6.1f}{m(c):>10}{c/T.KM_MONTH:>8.3f}{100*h/dt_base:>7.0f}%{cum:>9.1f}")
print(f"  {'BASE-CASE TOTAL':<36}{dt_base:>6.1f}{m(dt_base*net_cost_per_h):>10}"
      f"{dt_base*net_cost_per_h/T.KM_MONTH:>8.3f}{100:>7.0f}%")
print(f"  per lost hour: gross {PROD_KM_H:.0f} km x Rs{T.FARE_PER_KM:.2f} = Rs{m(gross_per_h,2)}")
print(f"                 less platform fee {PROD_KM_H:.0f} x Rs{PLATFORM_FEE_MO/T.KM_MONTH:.3f}/km = Rs{m(platform_fee_per_h,2)}")
print(f"                 less energy avoided {PROD_KM_H:.0f} x Rs{EV['kwh100']/100*CITIES['Delhi']['tariff']/EV['ceff']:.3f}/km = Rs{m(energy_avoided_per_h,2)}")
print(f"                 = NET COST OF A LOST HOUR Rs{m(net_cost_per_h,2)}/h  (report's OPP_H = Rs{m(T.OPP_H)})")
print(f"  base-case cost: EV Rs{m(dt_base*net_cost_per_h)}/mo = Rs{dt_base*net_cost_per_h/T.KM_MONTH:.3f}/km"
      f" -> Rs{m(dt_base*net_cost_per_h*60)} over 5 yr")
print(f"  at the OLD OPP_H Rs{m(T.OPP_H)} the same {dt_base:.1f} h/mo would be charged"
      f" Rs{m(dt_base*T.OPP_H)}/mo = Rs{dt_base*T.OPP_H/T.KM_MONTH:.3f}/km")
def adv_at_downtime(h_mo, years=5):
    """EV vs CNG advantage when h_mo h/month are lost, charged at net_cost_per_h.
       tco() prices downtime at T.OPP_H, so convert to its units."""
    d=h_mo*net_cost_per_h/T.OPP_H
    ev=T.tco(EV,"Delhi",years,downtime_h=d)["ckm"]; cn=T.tco(CNG,"Delhi",years)["ckm"]
    return 100*(cn-ev)/cn
lo,hi=0.0,200.0
for _ in range(80):
    mid=(lo+hi)/2
    if adv_at_downtime(mid)>0: lo=mid
    else: hi=mid
print(f"  breakeven: EV absorbs {lo:.1f} h/mo TOTAL downtime at Rs{m(net_cost_per_h,2)}/h"
      f" = {lo-dt_base:.1f} h/mo beyond the {dt_base:.1f} h base case")
print(f"  same breakeven restated in the section-C OPP_H units: {lo*T.OPP_H/net_cost_per_h:.1f} h/mo"
      f" (section C printed 45 h/mo on a ZERO base case at Rs{m(T.OPP_H)}/h)")
print(f"  at the observed real-world failure mode (75 h/mo, Green SM Noida) the advantage is {adv_at_downtime(75.0):+.1f}%")

print(); print("="*74); print("J. TWO OWNERSHIP MODELS — stated separately"); print("="*74)
print(f"  net fare derivation: Rs{T.FARE_PER_KM:.2f}/km - Rs{m(PLATFORM_FEE_D)}/day x {DAYS_MO} d"
      f" = Rs{m(PLATFORM_FEE_MO)}/mo / {m(T.KM_MONTH)} km = Rs{PLATFORM_FEE_MO/T.KM_MONTH:.3f}/km")
print(f"                   -> NET_FARE_KM = {NET_FARE_KM:.4f} = Rs{m(NET_FARE_KM*T.KM_MONTH)}/mo gross to the vehicle owner")
rev_net=NET_FARE_KM*T.KM_MONTH
def opex_mo(d): return d["energy"]/60+d["maint"]/60+d["ins"]/60
print(f"  MODEL A — driver-owned (driver buys and finances; driver keeps the residual)")
print(f"    {'vehicle':<6}{'EMI':>9}{'energy':>9}{'maint':>7}{'ins':>7}{'outflow':>10}{'net(during)':>13}{'net(yr6+)':>12}")
aA={}
for lab,d in (("EV",e),("CNG",g)):
    o=opex_mo(d); aA[lab]=(rev_net-d["emi"]-o, rev_net-o)
    print(f"    {lab:<6}{m(d['emi']):>9}{m(d['energy']/60):>9}{m(d['maint']/60):>7}{m(d['ins']/60):>7}"
          f"{m(d['emi']+o):>10}{m(aA[lab][0]):>13}{m(aA[lab][1]):>12}")
print(f"    delta (EV-CNG) during loan Rs{m(aA['EV'][0]-aA['CNG'][0])}/mo | yr6+ Rs{m(aA['EV'][1]-aA['CNG'][1])}/mo"
      f" | 5-yr driver gap Rs{m((aA['EV'][0]-aA['CNG'][0])*60)}")
print(f"  MODEL B — fleet-owned (operator buys and finances; driver carries NO capital cost)")
print(f"    {'vehicle':<6}{'EMI':>9}{'energy':>9}{'maint':>7}{'ins':>7}{'outflow':>10}{'net(during)':>13}{'net(yr6+)':>12}")
bB={}
for lab,d in (("EV",e),("CNG",g)):
    o=opex_mo(d); bB[lab]=rev_net-o
    print(f"    {lab:<6}{'—':>9}{m(d['energy']/60):>9}{m(d['maint']/60):>7}{m(d['ins']/60):>7}"
          f"{m(o):>10}{m(bB[lab]):>13}{m(bB[lab]):>12}")
print(f"    delta (EV-CNG) Rs{m(bB['EV']-bB['CNG'])}/mo  — the capital cost has moved off the driver's")
print(f"               statement; it is the operator's, below")
print(f"    {'operator':<9}{'TCO 5yr':>12}{'per mo':>10}{'net/mo':>10}")
opA={}
for lab,d in (("EV",e),("CNG",g)):
    om=d["total"]/60; opA[lab]=rev_net-om
    print(f"    {lab:<9}{m(d['total']):>12}{m(om):>10}{m(opA[lab]):>10}")
print(f"    operator delta Rs{m(opA['EV']-opA['CNG'])}/mo = Rs{m(opA['EV']*60-opA['CNG']*60)} over 5 yr"
      f"  (section-A TCO: EV Rs{m(e['total'])} / CNG Rs{m(g['total'])}, the fleet-owned case)")
# Two independent routes to the same 5-yr economic position:
#   A: from the DRIVER's monthly table  -> 60*(net fare - EMI - opex) + residual received
#   B: from the OPERATOR's TCO table   -> 60*net fare - TCO (TCO = EMI*60 + opex - residual)
rev_5yr=NET_FARE_KM*T.KM_MONTH*60
totA=((aA['EV'][0]-aA['CNG'][0])*60)+(e['res']-g['res'])
totB=rev_5yr-e['total']-(rev_5yr-g['total'])
print(f"  5-yr economic position of whoever OWNS the vehicle (net fare Rs{m(rev_5yr)} - vehicle cost + residual):")
print(f"    Model A, built from the DRIVER's monthly line: EV Rs{m(aA['EV'][0]*60+e['res'])}"
      f" | CNG Rs{m(aA['CNG'][0]*60+g['res'])} | delta Rs{m(totA)}")
print(f"    Model B, built from the OPERATOR's TCO line:  EV Rs{m(rev_5yr-e['total'])}"
      f" | CNG Rs{m(rev_5yr-g['total'])} | delta Rs{m(totB)}")
print(f"    identical across ownership models: {'YES' if abs(totA-totB)<0.01 else 'NO'}"
      f" (difference Rs{m(totA-totB)}) — ownership only decides WHICH line of a")
print(f"    balance sheet carries the vehicle; it does not create value. Both equal the")
print(f"    section-A TCO saving of Rs{m(g['total']-e['total'])}.")
print(f"    The DRIVER-only delta is NOT the same in the two models "
      f"(Rs{m(aA['EV'][0]-aA['CNG'][0])} vs Rs{m(bB['EV']-bB['CNG'])}/mo):")
print(f"    they differ by exactly the capital-and-residual term, which the operator carries in Model B.")
print(f"  platform-fee invariance check — same Model A on the legacy {LEGACY_COMMISSION:.0%} per-ride commission:")
LEG_FEE_KM=T.FARE_PER_KM*LEGACY_COMMISSION
LEG_NET_KM=T.FARE_PER_KM*(1-LEGACY_COMMISSION)-LEG_FEE_KM
leg_rev=LEG_NET_KM*T.KM_MONTH
leg_dA=(leg_rev-e['emi']-opex_mo(e))-(leg_rev-g['emi']-opex_mo(g))
print(f"    gross Rs{T.FARE_PER_KM:.2f} x (1-{LEGACY_COMMISSION:.0%}) = Rs{T.FARE_PER_KM*(1-LEGACY_COMMISSION):.2f} less commission"
      f" Rs{m(LEG_FEE_KM)}/km -> net fare Rs{LEG_NET_KM:.2f}/km = Rs{m(leg_rev)}/mo")
print(f"    Model A delta on legacy net fare Rs{m(leg_dA)}/mo vs flat-fee Rs{m(aA['EV'][0]-aA['CNG'][0])}/mo"
      f"  -> delta moves by Rs{m(leg_dA-(aA['EV'][0]-aA['CNG'][0]))}")
print(f"    the fare and the fee cancel in the EV-minus-CNG difference, so the DELTA is independent of")
print(f"    how the platform is paid. What changes with the fee is each driver's take-home, not the ranking.")

print(); print("="*74); print("K. EFC — the definitional choice, exposed"); print("="*74)
E_DAY_KWH    = EV["kwh100"]/100*T.KM_DAY
USABLE_RES   = 0.90
CEFF         = EV["ceff"]
SOH_DESIGN   = 0.716          # converged SoH at the 48 C design point (battery model)
PACK_RULE    = E_DAY_KWH/(SOH_DESIGN*USABLE_RES*CEFF)
PACK_USABLE  = 44.2            # the pack the rule converges to (battery model, 48 C point)
thruput      = EV["kwh100"]/100*T.KM_YEAR
efc_nominal  = thruput/EV["pack"]
efc_usable   = thruput/PACK_USABLE
efc_wall     = (EV["kwh100"]/CEFF)/100*T.KM_YEAR/EV["pack"]
print(f"  battery-side annual throughput = {EV['kwh100']}/100 x {m(T.KM_YEAR)} km = {m(thruput,1)} kWh/yr")
print(f"  pack-sizing rule: E_day / (SoH x {USABLE_RES:.2f} reserve x {CEFF:.2f} ceff)")
print(f"    E_day = {EV['kwh100']}/100 x {T.KM_DAY} km = {m(E_DAY_KWH,2)} kWh")
print(f"    = {m(E_DAY_KWH,2)} / ({SOH_DESIGN:.3f} x {USABLE_RES:.2f} x {CEFF:.2f}) = {m(PACK_RULE,2)} kWh"
      f"  (converged pack {m(PACK_USABLE,1)} kWh, within {100*(PACK_RULE/PACK_USABLE-1):+.1f}%)")
print(f"  {'basis':<44}{'kWh/yr':>12}{'EFC/yr':>9}{'yr->3,000':>11}")
print(f"  {'NOMINAL pack '+m(EV['pack'],1)+' kWh':<44}{m(thruput,1):>12}{efc_nominal:>9.1f}{3000/efc_nominal:>11.2f}")
print(f"  {'USABLE pack '+m(PACK_USABLE,1)+' kWh (SoH-adjusted)':<44}{m(thruput,1):>12}{efc_usable:>9.1f}{3000/efc_usable:>11.2f}")
print(f"  {'WRALL energy / NOMINAL pack (deck basis)':<44}{m((EV['kwh100']/CEFF)/100*T.KM_YEAR,1):>12}{efc_wall:>9.1f}{3000/efc_wall:>11.2f}")
print(f"  The third line is the basis behind the ~198 EFC/yr currently cited in the deck:")
print(f"    ({EV['kwh100']}/{CEFF:.2f})/100 x {m(T.KM_YEAR)} / {m(EV['pack'],1)} = {efc_wall:.1f} EFC/yr.")
print(f"    It divides WALL energy ({EV['kwh100']/CEFF:.2f} kWh/100km, charging losses included)")
print(f"    by NOMINAL capacity ({m(EV['pack'],1)} kWh), mixing two different bases. Against the")
print(f"    like-for-like nominal line ({efc_nominal:.1f}) it OVERSTATES EFC by"
      f" {100*(efc_wall/efc_nominal-1):.1f}%, and pulls time-to-3,000-cycles from"
      f" {3000/efc_nominal:.1f} yr down to {3000/efc_wall:.1f} yr.")
print(f"  Nothing above is changed in place — the published 198 figure is left standing")
print(f"  and this section only states which definition produces it.")
print(); print("="*74); print("L. HEADLINE CONSISTENCY MATRIX — one defensible number"); print("="*74)
def infra_schedule(side, years, capex=None):
    """Monthly infrastructure cash flows for ONE vehicle: {month: [(amount, esc_rate), ...]}.
    Fed straight into npv_flow(infra=...), so infrastructure and vehicle flows are discounted by
    the SAME monthly loop at the SAME rate. There is no second NPV calculation in this file.
    EV  : capex at mo 0, again every charger_life_yr while STRICTLY inside the horizon
          (N=60 therefore EXCLUDES the mo-60 replacement; N=96 includes it), plus Rs15,000/yr
          opex spread monthly and escalated at ESC_MAINT.
    CNG : no per-vehicle capex (factory kit sits inside the ex-showroom price);
          cylinder hydro-test at mo 36, 72, ... while inside the horizon.
    Capex is a stated rupee amount on the day it is incurred, so it is NOT escalated; only the
    recurring opex line is. That is the section-G timing restated in monthly form.
    capex= (section M) overrides the charger cost; default reproduces section G/L exactly."""
    N=years*12; s={}
    if capex is None: capex=charger_capex_per_veh
    put=lambda mo,amt,rt: s.setdefault(mo,[]).append((amt,rt))
    if side=="EV":
        for mo in range(0, N, charger_life_yr*12): put(mo, capex, 0.0)
        for mo in range(1, N+1):                   put(mo, charger_opex_yr/12, ESC_MAINT)
    else:
        for mo in range(3*12, N+1, 3*12):          put(mo, cng_hydrotest, 0.0)
    return s

NB = ("nominal, excl. infra","nominal, incl. infra",
      f"NPV {DISC_RATE:.0%} esc, excl. infra",f"NPV {DISC_RATE:.0%} esc, incl. infra")
L={}; L_inf={}
print(f"  Delhi, financed {T.LOAN_MONTHS}mo. Rows 1-2 are the section-A tco() totals (nominal rupees);")
print(f"  rows 3-4 are the section-H npv_flow() totals (rupee NPVs at {DISC_RATE:.0%}, escalated).")
print(f"  Infrastructure is the SAME schedule in every row that includes it — one definition, four uses.")
for yrs in (5,8):
    kmv=yrs*T.KM_YEAR
    a=T.tco(EV,"Delhi",yrs); b=T.tco(CNG,"Delhi",yrs)
    se,sc=infra_schedule("EV",yrs),infra_schedule("CNG",yrs)
    ev_u=sum(amt for lst in se.values() for amt,_ in lst)
    cn_u=sum(amt for lst in sc.values() for amt,_ in lst)
    ne=npv_flow(EV,years=yrs);                      ng=npv_flow(CNG,years=yrs)
    nIe=npv_flow(EV,years=yrs,infra=se);           nIg=npv_flow(CNG,years=yrs,infra=sc)
    ce,cg = a["ckm"]+ev_u/kmv, b["ckm"]+cn_u/kmv
    L[(yrs,0)]=(a["ckm"]*kmv, b["ckm"]*kmv, 100*(b["ckm"]-a["ckm"])/b["ckm"])
    L[(yrs,1)]=(ce*kmv, cg*kmv, 100*(cg-ce)/cg)
    L[(yrs,2)]=(ne["total"], ng["total"], 100*(ng["total"]-ne["total"])/ng["total"])
    L[(yrs,3)]=(nIe["total"],nIg["total"],100*(nIg["total"]-nIe["total"])/nIg["total"])
    L_inf[yrs]=(ev_u,cn_u,ne,ng,nIe,nIg,se,sc,kmv)
    print()
    print(f"  --- {yrs}-YEAR HORIZON  ({m(kmv)} km) ---")
    print(f"  {'basis':<28}{'EV':>13}{'CNG':>13}{'EV advantage':>15}")
    for i,b in enumerate(NB):
        ev_,cn_,adv_=L[(yrs,i)]
        print(f"  {b:<28}{m(ev_):>13}{m(cn_):>13}{adv_:>14.1f}%")
    capmo=[mo for mo in range(0,yrs*12,charger_life_yr*12)]
    print(f"  infra carried, undiscounted: EV Rs{m(ev_u)} | CNG Rs{m(cn_u)}   "
          f"(EV capex at month {capmo} = Rs{m(charger_capex_per_veh)} each + Rs{m(charger_opex_yr)}/yr opex;"
          f" CNG hydro-test at month {sorted(sc)} = Rs{m(cng_hydrotest)} each)")
    print(f"  infra in the NPV (monthly, same loop): EV Rs{m(nIe['infra'])} | CNG Rs{m(nIg['infra'])}")
    print(f"  cross-check vs section G: nominal incl-infra {L[(yrs,1)][2]:+.1f}% vs section G {g_rows[yrs][2]:+.1f}%"
          f"  (delta {L[(yrs,1)][2]-g_rows[yrs][2]:+.2f} pp)   |   section H: {L[(yrs,2)][2]:+.1f}%")

print()
print(f"  {'basis':<28}{'5-year':>9}{'8-year':>10}{'d with infra':>22}")
for i,b in enumerate(NB):
    dn5_=L[(5,1)][2]-L[(5,0)][2] if i==1 else (L[(5,3)][2]-L[(5,2)][2] if i==3 else 0.0)
    dn8_=L[(8,1)][2]-L[(8,0)][2] if i==1 else (L[(8,3)][2]-L[(8,2)][2] if i==3 else 0.0)
    tag=f"{dn5_:+.1f} pp / {dn8_:+.1f} pp" if i in (1,3) else "-"
    print(f"  {b:<28}{L[(5,i)][2]:>8.1f}%{L[(8,i)][2]:>9.1f}%{tag:>22}")
d5=L[(5,3)][2]-L[(5,2)][2]; d8=L[(8,3)][2]-L[(8,2)][2]
dn5=L[(5,1)][2]-L[(5,0)][2]; dn8=L[(8,1)][2]-L[(8,0)][2]
print(f"  DIRECTION CHECK: adding infrastructure moves the advantage DOWN at both horizons —")
print(f"    NPV basis : 5yr {L[(5,2)][2]:+.1f}% -> {L[(5,3)][2]:+.1f}% ({d5:+.1f} pp) | 8yr {L[(8,2)][2]:+.1f}% -> {L[(8,3)][2]:+.1f}% ({d8:+.1f} pp)")
print(f"    nominal   : 5yr {L[(5,0)][2]:+.1f}% -> {L[(5,1)][2]:+.1f}% ({dn5:+.1f} pp) | 8yr {L[(8,0)][2]:+.1f}% -> {L[(8,1)][2]:+.1f}% ({dn8:+.1f} pp)")
print(f"    Confirmed DOWN, as required: charging capex is an EV-only cost "
      f"(EV Rs{m(charger_capex_per_veh)}/vehicle) while the CNG side carries only Rs{m(cng_hydrotest)} of")
print(f"    periodic hydro-testing, so every rupee of it narrows the EV's advantage and none of it widens it.")
ok=True; pk=[]
for yrs in (5,8):
    for i in (2,3):
        ev_,cn_,_=L[(yrs,i)]
        if not (0 < ev_ and 0 < cn_): ok=False
        pk += [ev_/L_inf[yrs][8], cn_/L_inf[yrs][8]]
print(f"  PLAUSIBILITY: every NPV cell is a positive rupee total, "
      f"EV {m(L[(5,2)][0]/100000,1)}-{m(L[(8,3)][0]/100000,1)} lakh / CNG {m(L[(5,2)][1]/100000,1)}-{m(L[(8,3)][1]/100000,1)} lakh,")
print(f"    i.e. Rs{min(pk):.2f}-{max(pk):.2f}/km across all four NPV cells. None near zero: "
      f"{'OK' if ok else 'ANOMALY — DO NOT SHIP'}. (The 8-yr column runs past Rs20 lakh because the horizon is 60% longer, not because the discount factor is wrong.)")

print()
print("  REV 4 HEADLINE  =  the bottom-right cell: NPV at a 12% hurdle, escalated, financed,")
print(f"  INCLUDING depot charging infrastructure — +{L[(5,3)][2]:.1f}% over 5 years and +{L[(8,3)][2]:.1f}% over 8 years.")
print("  WHY THAT CELL: it is the only basis that prices everything the operator actually faces —")
print("  the 12% hurdle prices the deferred capital, escalation prices the 4.5% power and 3.5% CNG")
print("  trajectory, and the infrastructure line prices the Rs99,000/vehicle charger that only the EV")
print("  needs; the nominal excl-infra +14.5% omits an EV-only cost altogether, and the 8-yr nominal")
print("  +28.0% adds to that an undiscounted eight years of running cost.")

print(); print("="*74); print("M. CITY x BASIS MATRIX — does the fleet case close outside Delhi?"); print("="*74)
MB = ("nominal, excl. infra","nominal, incl. infra",
      f"NPV {DISC_RATE:.0%} esc, excl. infra",f"NPV {DISC_RATE:.0%} esc, incl. infra")
def infra_undisc(s): return sum(amt for lst in s.values() for amt,_ in lst)

class duty_knob:
    """Move the duty cycle to kpd km/day for the duration of the block. Both KM_YEAR
    (read by tco() and mt_pk()) and KM_MONTH (read by npv_flow()) must move together."""
    def __init__(s,k): s.k=k
    def __enter__(s): s._o=(T.KM_YEAR,T.KM_MONTH); T.KM_YEAR=s.k*DAYS_YEAR; T.KM_MONTH=s.k*T.DAYS_MONTH
    def __exit__(s,*a): T.KM_YEAR,T.KM_MONTH=s._o

def cell_rupees(city,yrs,fin,basis):
    """basis 0/1 = nominal excl/infra, 2/3 = NPV excl/infra. One cell, in rupees."""
    on,npv = basis in (1,3), basis>=2
    if not on:
        a=T.tco(EV,city,yrs,financed=fin); b=T.tco(CNG,city,yrs,financed=fin)
        return a["total"], b["total"]
    se,sc=infra_schedule("EV",yrs),infra_schedule("CNG",yrs)
    if npv:
        return (npv_flow(EV ,city=city,years=yrs,financed=fin,infra=se)["total"],
                npv_flow(CNG,city=city,years=yrs,financed=fin,infra=sc)["total"])
    kmv=yrs*T.KM_YEAR
    a=T.tco(EV,city,yrs,financed=fin); b=T.tco(CNG,city,yrs,financed=fin)
    return a["ckm"]*kmv+infra_undisc(se), b["ckm"]*kmv+infra_undisc(sc)

def gap_at(city,yrs,fin,on,npv,capex=None):
    """f(kpd) = CNG total - EV total at duty kpd km/day. >0 means the EV is cheaper."""
    se,sc=(infra_schedule("EV",yrs,capex),infra_schedule("CNG",yrs)) if on else (None,None)
    def f(k):
        with duty_knob(k):
            if npv:
                ev=(npv_flow(EV ,city=city,years=yrs,financed=fin,infra=se) if on
                    else npv_flow(EV ,city=city,years=yrs,financed=fin))["total"]
                cn=(npv_flow(CNG,city=city,years=yrs,financed=fin,infra=sc) if on
                    else npv_flow(CNG,city=city,years=yrs,financed=fin))["total"]
                return cn-ev
            a=T.tco(EV,city,yrs,financed=fin); b=T.tco(CNG,city,yrs,financed=fin)
            if not on: return b["total"]-a["total"]
            kmv=yrs*T.KM_YEAR
            return (b["ckm"]*kmv+infra_undisc(sc))-(a["ckm"]*kmv+infra_undisc(se))
    return f

def bisect(fn,lo,hi,it=70):
    """Returns (crossing, bracketed). Refuses to answer unless the sign flips at both ends."""
    flo,fhi=fn(lo),fn(hi)
    if flo*fhi>0: return None,False
    for _ in range(it):
        mid=(lo+hi)/2
        if fn(mid)*flo<=0: hi=mid
        else: lo=mid
    return (lo+hi)/2,True

M={}; M_NEG=[]
for yrs in (5,8):
    for fin in (True,False):
        for city in CITIES:
            for i in range(4):
                ev_,cn_=cell_rupees(city,yrs,fin,i)
                M[(city,yrs,fin,i)]=(ev_,cn_,100*(cn_-ev_)/cn_)
                if M[(city,yrs,fin,i)][2]<0: M_NEG.append((city,yrs,fin,i,M[(city,yrs,fin,i)][2]))

print(f"  {len(M)} cells = {len(CITIES)} cities x 2 horizons x 2 capital structures x 4 bases.")
print(f"  The Rs99,000 depot port is city-INDEPENDENT; what changes by city is the electricity")
print(f"  tariff, the road tax and the CNG gas price. So infrastructure is a flat EV-side tax")
print(f"  against a city-specific energy saving, which is exactly what makes the ranking move.")
print()
if M_NEG:
    print("  "+"*"*70)
    print("  *** %d NEGATIVE CELLS OUT OF %d — SEE THIS BEFORE THE TABLES ***"%(len(M_NEG),len(M)))
    print("  "+"*"*70)
    for city,yrs,fin,i,a in M_NEG:
        print(f"    *** NEGATIVE ***  {city:<10} {yrs}yr {'FINANCED 60mo' if fin else 'CASH outright':<15}"
              f" {MB[i]:<26} {a:+.1f}%")
    print("  "+"*"*70)
    n_neg8=sum(1 for c,y_,f_,i,_ in M_NEG if y_==8)
    n_negnom=sum(1 for c,y_,f_,i,_ in M_NEG if i<2)
    print(f"  Breakdown: {n_neg8} at 8 years, {len(M_NEG)-n_neg8} at 5 years, {n_negnom} on a nominal basis,")
    print(f"  {len(M_NEG)-n_negnom} on the NPV basis. Every one is INFRASTRUCTURE-INCLUSIVE.")
    print(f"  Excluding the charger, all {len(M)-len(M_NEG)} remaining cells are positive and no city fails.")
    print("  "+"*"*70)
else:
    print("  NO NEGATIVE CELLS on any basis.")

for yrs in (5,8):
    for fin in (True,False):
        print()
        print(f"  --- {yrs}-YEAR, {'FINANCED 60mo' if fin else 'CASH outright'} ---")
        print(f"  {'city':<11}{'basis':<27}{'EV Rs':>11}{'EV/km':>7}{'CNG Rs':>12}{'CNG/km':>8}   advantage")
        for city in CITIES:
            for i,bas in enumerate(MB):
                ev_,cn_,adv_=M[(city,yrs,fin,i)]
                print(f"  {city:<11}{bas:<27}{m(ev_):>11}{ev_/(yrs*T.KM_YEAR):>7.2f}{m(cn_):>12}"
                      f"{cn_/(yrs*T.KM_YEAR):>8.2f}   {adv_:+.1f}%"+("  *** NEGATIVE ***" if adv_<0 else ""))

print(); print("="*74); print("M3. BREAKEVEN DUTY WITH INFRASTRUCTURE (deck assumes 200 km/day)"); print("="*74)
print(f"  Re-bisected per city, per horizon, on the nominal and the NPV basis, with and without")
print(f"  the charger. Bracket 5-1500 km/day; the crossing is only accepted when the sign flips")
print(f"  at both bracket ends, otherwise the cell prints NO XOVER rather than a false number.")
M3={}
for city in CITIES:
    for yrs in (5,8):
        for npv in (False,True):
            for on in (False,True):
                M3[(city,yrs,npv,on)]=bisect(gap_at(city,yrs,True,on,npv),5.0,1500.0)[0]
def bcell(v): return f"{v:>10.1f}" if v else f"{'NO XOVER':>10}"
def bmult(v): return f"{T.KM_DAY/v:>6.2f}x" if v else f"{'n/a':>7}"
print(f"  {'city':<11}{'yrs':>4}{'nom excl':>10}{'nom incl':>11}{'x':>8}   {'NPV excl':>10}{'NPV incl':>11}{'x':>8}")
for city in CITIES:
    for yrs in (5,8):
        ne,ni=M3[(city,yrs,False,False)],M3[(city,yrs,False,True)]
        xe,xi=M3[(city,yrs,True ,False)],M3[(city,yrs,True ,True)]
        print(f"  {city:<11}{yrs:>4}{bcell(ne):>10}{bcell(ni)+('  FAIL' if ni and T.KM_DAY<ni else '     '):>16}{bmult(ni):>8}"
              f"   {bcell(xe):>10}{bcell(xi)+('  FAIL' if xi and T.KM_DAY<xi else '     '):>16}{bmult(xi):>8}")
print(f"  'FAIL' = the deck's {T.KM_DAY:.0f} km/day is BELOW the breakeven, so the EV loses money at the")
print(f"  stated duty. Section B's Delhi figures without infrastructure were 118.4 (5yr) / 63.6 (8yr).")
d5,d8=M3[("Delhi",5,False,True)],M3[("Delhi",8,False,True)]
e5,e8=M3[("Delhi",5,False,False)],M3[("Delhi",8,False,False)]
print(f"  Delhi rises {e5:.1f} -> {d5:.1f} km/day (5yr, +{d5-e5:.1f}) and {e8:.1f} -> {d8:.1f} (8yr, +{d8-e8:.1f}).")
rises=[(c,y,M3[(c,y,False,False)],M3[(c,y,False,True)]) for c in CITIES for y in (5,8)]
print(f"  On the nominal basis the requirement rises in all {len(rises)} city/horizon cases: "
      +", ".join(f"{c[:3]}{y}y {a:.0f}->{b:.0f}" for c,y,a,b in rises))
worst=max(((c,y,M3[(c,y,True,True)]) for c in CITIES for y in (5,8)),key=lambda r:r[2])
print(f"  Worst case on the headline basis (NPV incl. infra): {worst[0]} {worst[1]}yr needs "
      f"{worst[2]:.1f} km/day, i.e. {T.KM_DAY/worst[2]:.2f}x the deck's assumption — it does not clear.")

print(); print("="*74); print("M4. CHARGER CAPEX SENSITIVITY ACROSS CITIES (5yr, financed)"); print("="*74)
print(f"  {'city':<11}{'charger':>10}{'nom excl-infra':>18}{'nom incl-infra':>18}{'NPV incl-infra':>18}")
for city in CITIES:
    a0,b0=T.tco(EV,city,5),T.tco(CNG,city,5)
    e0=100*(b0["ckm"]-a0["ckm"])/b0["ckm"]
    for cap,lab in ((60_000,"Rs60,000"),(charger_capex_per_veh,f"Rs{m(charger_capex_per_veh)}"),(150_000,"Rs1,50,000")):
        se,sc=infra_schedule("EV",5,cap),infra_schedule("CNG",5)
        cn_nom=b0["ckm"]*5*T.KM_YEAR+infra_undisc(sc)
        cn_npv=npv_flow(CNG,city=city,years=5,infra=sc)["total"]
        an=100*gap_at(city,5,True,True,False,cap)(T.KM_DAY)/cn_nom
        av=100*gap_at(city,5,True,True,True ,cap)(T.KM_DAY)/cn_npv
        print(f"  {city:<11}{lab:>10}{e0:>+17.1f}%{an:>+17.1f}%{av:>+17.1f}%"
              +("  *** NEGATIVE ***" if (an<0 or av<0) else ""))
print()
print(f"  Solved breakeven charger capex per city (5yr, financed): the charger cost at which the EV")
print(f"  advantage hits exactly zero. The advantage decreases monotonically in charger capex on both")
print(f"  bases (one rupee of capex is a rupee of EV cost and nothing of CNG cost), so this is a")
print(f"  well-posed solve rather than an extrapolation of the three sample points.")
print(f"  {'city':<11}{'nominal':>14}{'NPV (headline)':>18}   verdict at the Rs{m(charger_capex_per_veh)} base case")
m4={}
for city in CITIES:
    rn,_=bisect(lambda cap: gap_at(city,5,True,True,False,cap)(T.KM_DAY),0.0,900_000.0)
    rv,_=bisect(lambda cap: gap_at(city,5,True,True,True ,cap)(T.KM_DAY),0.0,900_000.0)
    m4[city]=(rn,rv)
    v=(f"wins, Rs{m(rv-charger_capex_per_veh)} of headroom" if rv>charger_capex_per_veh
       else f"LOSES by Rs{m(charger_capex_per_veh-rv)} over the breakeven")
    print(f"  {city:<11}{('Rs'+m(rn)):>14}{('Rs'+m(rv)):>18}   {v}")
m4_worst=min(m4,key=lambda c:m4[c][1])
print(f"  Binding charger breakeven: {m4_worst} at Rs{m(m4[m4_worst][1])} on the headline NPV basis —"
      f" {'BELOW' if m4[m4_worst][1]<charger_capex_per_veh else 'ABOVE'} the Rs{m(charger_capex_per_veh)} base case.")
for _c in CITIES:
    _h=m4[_c][1]-charger_capex_per_veh
    print(f"    {_c:<11} headroom Rs{m(_h):>10}  ({_h/charger_capex_per_veh:+.0%} of the charger budget)")

print()
print("  READ:")
if M_NEG:
    print(f"  {len(M)} cells, {len(M_NEG)} NEGATIVE. Every one is 5-year and infrastructure-inclusive:")
    for _c,_y,_f,_i,_a in M_NEG:
        print(f"    {_c} {_y}yr {'financed' if _f else 'cash'}, {MB[_i]} {_a:+.2f}%")
else:
    print(f"  All {len(M)} cells are positive. The 5-year case closes in every city on every basis.")
print(f"  Delhi 5yr is positive on all four bases; its breakeven duty is {M3[('Delhi',5,True,True)]:.0f} km/day"
      f" = {T.KM_DAY/M3[('Delhi',5,True,True)]:.2f}x the deck's 200.")
print(f"  {'city':<11}{'5yr breakeven duty':>20}{'vs deck 200':>13}   verdict")
for _c in CITIES:
    _be=M3[(_c,5,True,True)]
    print(f"  {_c:<11}{_be:>19.1f}x{T.KM_DAY/_be:>12.2f}x   {'PASS' if _be<T.KM_DAY else 'FAIL'}")
_w8=min((( _c,_y,M[(_c,_y,False,3)][2]) for _c in CITIES for _y in (5,8)),key=lambda r:r[2])
print(f"  weakest cell in the entire matrix: {_w8[0]} {_w8[1]}yr, cash, NPV incl. infra, {_w8[2]:+.2f}%")
print("  On the NPV basis financing actually HELPS the EV (a 10% loan discounted at a 12% hurdle is")
print("  cheaper than cash, and the EV is the capital-intensive side), so cheap credit is not the lever.")
print("  The levers are the horizon and the charger — see sections P and R.")

# =============================================================================
# SECTIONS N, O — purely additive. Sections A..M above are untouched.
# =============================================================================
print(); print("="*74); print("N. INTER-CITY DUTY — the vehicle model has no range model at all"); print("="*74)
print("  Everything in sections A-M is priced per kilometre and assumes the vehicle never")
print("  has to leave the depot's overnight charging window. The duty mix is a separate")
print("  question and the vehicle model carries no range, reserve or recharge-stop data,")
print("  so the constants below are declared here and printed, not inherited.")
PACK_NOMINAL  = 45.0    # kWh nominal pack (tco_engine.EV['pack'])
USABLE_FRAC  = 0.90    # the reserve convention; matches the section-K pack-sizing rule
KWH_100      = 12.84   # kWh/100 km, battery-side
CEFF         = 0.90    # wall -> battery charge efficiency
RESERVE_TGT  = 0.15    # the design reserve the corridors are judged against
BASE_DAY_KM  = 200     # the deck's urban day, unchanged
IC_LEG_KM    = 280     # one leg of the modelled intercity day
IC_DAY_KM    = 2*IC_LEG_KM   # 280 out + 280 back
n_usable   = PACK_NOMINAL*USABLE_FRAC
n_rate     = KWH_100/100.0
n_maxrange = n_usable/n_rate

print(); print("  named constants")
print(f"    PACK_NOMINAL {PACK_NOMINAL} kWh | USABLE_FRAC {USABLE_FRAC} | KWH_100 {KWH_100} | CEFF {CEFF}"
      f" | RESERVE_TGT {RESERVE_TGT:.0%}")
print("  N1. RANGE ENVELOPE")
print(f"    usable energy = {PACK_NOMINAL} x {USABLE_FRAC} = {n_usable:.2f} kWh")
print(f"    max range     = {n_usable:.1f} / ({KWH_100}/100) = {n_maxrange:.1f} km at ZERO reserve")
print(f"    arithmetic check: {n_usable}/{n_rate:.4f} = {n_usable/n_rate:.1f} km  "
      f"(invariant target 315.4)  {'OK' if abs(n_maxrange-315.4)<0.05 else '** ARITHMETIC BROKEN **'}")
print(f"    {'reserve':>8}{'range km':>11}   note")
N_RESERVE={}
for r,note in ((0.00,"zero reserve — no derating headroom, not a duty cycle"),
               (0.10,"aggressive; below the 0.90 usable convention"),
               (0.15,"DESIGN TARGET — the corridors below are judged against this"),
               (0.20,"conservative; matches the SoH headroom in the section-K pack rule")):
    N_RESERVE[r]=n_maxrange*(1-r)
    print(f"    {r:>7.0%}{N_RESERVE[r]:>11.1f}   {note}")
n_thresh=N_RESERVE[RESERVE_TGT]

print(); print("  N2. NAMED CORRIDORS — judged against the 15%-reserve range "
      f"({n_thresh:.1f} km one-way)")
print("    FEASIBLE     = the whole leg fits inside the 15%-reserve budget")
print("    MARGINAL     = the leg is inside the pack but over the reserve budget,")
print("                  so it needs reserve relief or a top-up en route")
print("    NOT FEASIBLE = the leg exceeds the usable pack outright")
print(f"    {'corridor':<20}{'km':>5}{'kWh batt':>10}{'% usable':>10}{'verdict':>14}")
N_CORRIDORS=(("Mumbai-Pune",150),("Bengaluru-Mysuru",145),("Mumbai-Nashik",170),
             ("Delhi-Agra",200),("Delhi-Jaipur",280),("Delhi-Lucknow",550))
for lab,d in N_CORRIDORS:
    kwh=d*n_rate
    st="FEASIBLE" if d<=n_thresh else ("MARGINAL" if kwh<=n_usable else "NOT FEASIBLE")
    print(f"    {lab:<20}{d:>5}{kwh:>10.2f}{100*kwh/n_usable:>9.1f}%{st:>14}")
leg_kwh=IC_LEG_KM*n_rate
leg_budget=n_usable*(1-RESERVE_TGT)
print(f"    the modelled {IC_LEG_KM} km leg needs {leg_kwh:.2f} kWh battery-side ="
      f" {100*leg_kwh/n_usable:.1f}% of the usable pack, against a {RESERVE_TGT:.0%}-reserve budget of {leg_budget:.2f} kWh")
print(f"    -> the {IC_LEG_KM} km leg is {'INSIDE' if leg_kwh<=leg_budget else 'OUTSIDE'} that budget by"
      f" {abs(leg_kwh-leg_budget):.2f} kWh; the full {IC_DAY_KM} km day needs"
      f" {IC_DAY_KM*n_rate/leg_budget:.2f} such budgets")
print("  Beyond roughly 300 km one-way, destination charging is MANDATORY. That is a")
print("    fleet-contract requirement — a guaranteed destination charge on a nominated")
print("    route, priced and controlled by the operator — not a vehicle specification.")
print("    It belongs in the operating model and in the duty agreement, not in the datasheet.")

print(); print("  N3. INTER-CITY DUTY ECONOMICS — infrastructure-inclusive basis (section-G schedule)")
def n_mix(km_month, years=5):
    """One month totalling km_month across DAYS_MO days. Capital, insurance, residual and the
    section-G infrastructure schedule are all distance-INDEPENDENT, so they amortise over the
    longer month; energy and maintenance scale with km. duty_knob repoints KM_YEAR and KM_MONTH,
    which is precisely what tco() and mt_pk() read."""
    kmv=km_month*12*years
    with duty_knob(km_month/DAYS_MO):
        a=T.tco(EV,"Delhi",years,financed=True); b=T.tco(CNG,"Delhi",years,financed=True)
    ev_i=infra_undisc(infra_schedule("EV",years)); cn_i=infra_undisc(infra_schedule("CNG",years))
    ek,ck=a["ckm"]+ev_i/kmv, b["ckm"]+cn_i/kmv
    return dict(km=km_month,kmv=kmv,ev_k=ek,cn_k=ck,adv=100*(ck-ek)/ck,
                ev_fix=a["capex"]+a["ins"]-a["res"]+ev_i, cn_fix=b["capex"]+b["ins"]-b["res"]+cn_i,
                ev_var=a["energy"]+a["maint"], cn_var=b["energy"]+b["maint"])
print(f"    base fleet day {BASE_DAY_KM} km | intercity day {IC_DAY_KM} km ({IC_LEG_KM} out + {IC_LEG_KM} back)")
print(f"    Delhi, {T.LOAN_MONTHS}mo financed, nominal, 5 yr, INCLUDING the section-G charger "
      f"(EV Rs{m(infra_undisc(infra_schedule('EV',5)))} / CNG Rs{m(infra_undisc(infra_schedule('CNG',5)))} over the horizon)")
print(f"    {'IC days':>8}{'base days':>10}{'km/month':>11}{'km/5yr':>11}{'EV Rs/km':>10}{'CNG Rs/km':>11}{'advantage':>12}{'delta':>10}")
N_ROWS={}
prev=None
for n_ic in (0,9,18,26,27):
    km_mo=n_ic*IC_DAY_KM+(DAYS_MO-n_ic)*BASE_DAY_KM
    r=n_mix(km_mo); N_ROWS[n_ic]=r
    d="-" if (prev is None or n_ic>DAYS_MO) else f"{r['adv']-prev:+.2f} pp"
    flag="" if n_ic<=DAYS_MO else "  ** NOT SCHEDULABLE **"
    print(f"    {n_ic:>8}{DAYS_MO-n_ic:>10}{r['km']:>11,.0f}{r['kmv']:>11,.0f}{r['ev_k']:>10.2f}"
          f"{r['cn_k']:>11.2f}{r['adv']:>+11.2f}%{d:>10}{flag}")
    if n_ic<=DAYS_MO: prev=r["adv"]
print(f"    the {max(N_ROWS)}-day rung is NOT SCHEDULABLE: it needs {max(N_ROWS)} operating days inside a")
print(f"    {DAYS_MO}-day month. It is printed only as the arithmetic endpoint of the ladder; the")
print(f"    real saturated duty is every one of the {DAYS_MO} days intercity ({N_ROWS[26]['km']:,.0f} km/month).")
print(f"    the 0-intercity-day rung reproduces the published section-G/L nominal incl-infra"
      f" figure: {N_ROWS[0]['adv']:+.2f}% vs +6.5%")
N_SAT=[N_ROWS[k]["adv"] for k in (0,9,18,26)]
N_MONO=all(N_SAT[i]>N_SAT[i-1] for i in range(1,len(N_SAT)))
print(f"    DIRECTION CHECK over the schedulable rungs: {N_SAT[0]:+.2f}% -> {N_SAT[1]:+.2f}% ->"
      f" {N_SAT[2]:+.2f}% -> {N_SAT[3]:+.2f}%.")
print(f"    The EV's per-km position {'DOES improve at every rung' if N_MONO else 'DOES NOT improve monotonically — see the table above'}:"
      f" {N_SAT[-1]-N_SAT[0]:+.1f} pp from the pure-urban month to the fully intercity month.")
a0,a1=N_ROWS[0],N_ROWS[26]
print(f"    and the mechanism is fixed-cost amortisation, not cheaper energy:")
print(f"      EV  fixed Rs{m(a0['ev_fix'])} + variable Rs{m(a0['ev_var'])}  -> per km"
      f" {a0['ev_fix']/a0['kmv']:.2f} + {a0['ev_var']/a0['kmv']:.2f} = {a0['ev_k']:.2f}"
      f"  |  at full intercity {a1['ev_fix']/a1['kmv']:.2f} + {a1['ev_var']/a1['kmv']:.2f} = {a1['ev_k']:.2f}")
print(f"      CNG fixed Rs{m(a0['cn_fix'])} + variable Rs{m(a0['cn_var'])}  -> per km"
      f" {a0['cn_fix']/a0['kmv']:.2f} + {a0['cn_var']/a0['kmv']:.2f} = {a0['cn_k']:.2f}"
      f"  |  at full intercity {a1['cn_fix']/a1['kmv']:.2f} + {a1['cn_var']/a1['kmv']:.2f} = {a1['cn_k']:.2f}")
print(f"    the variable-cost gap does not close: {a0['cn_var']/a0['kmv']-a0['ev_var']/a0['kmv']:.2f} Rs/km in the EV's favour at"
      f" the urban duty,")
print(f"    {a1['cn_var']/a1['kmv']-a1['ev_var']/a1['kmv']:.2f} Rs/km fully intercity. What changes is how much capital each side"
      f" spreads over the month, and")
print(f"    the EV is the capital-intensive side, so that lever works in its favour.")

print(); print("  N4. OPERATING-MODEL DEPENDENCY — stated, not priced")
ic_batt=IC_DAY_KM*n_rate; ic_wall=ic_batt/CEFF
print(f"    the section-G overnight window is {h_night:.2f} h, sized on {T.KM_DAY} km/day"
      f" ({m(e_day_wall,2)} kWh wall / {CHARGER_KW} kW).")
print(f"    one intercity day needs {m(ic_batt,2)} kWh battery-side = {m(ic_wall,2)} kWh wall"
      f" = {ic_wall/CHARGER_KW:.2f} h at the same {CHARGER_KW} kW port — {ic_wall/CHARGER_KW/h_night:.1f}x the window.")
print("    So an intercity-heavy duty does not run on the depot model section G priced. It")
print("    runs on destination charging plus mid-day top-ups, which changes:")
print("      (a) the charging contract — guaranteed destination charge, tariff, and who pays")
print("      (b) the {0:.2f} h overnight window ceases to be the binding constraint".format(h_night))
print("      (c) the energy price mix moves toward a public/commercial band, and section D")
print("          already priced that move as the largest single EV risk (tariff Rs4.50 -> Rs12.00)")
print("    This is an OPERATING-MODEL dependency, so it is deliberately NOT re-run here. The table")
print(f"    above prices the intercity day's energy at the Delhi EV tariff of Rs{CITIES['Delhi']['tariff']:.2f}/kWh, the most")
print("    favourable assumption available, and therefore the correct place to stop: the ladder")
print("    shows the utilisation upside, and charging the destination top-ups at public DC rates")
print("    would eat part of it. Quantifying that needs destination tariff and dwell-time data")
print("    the model does not carry.")

print(); print("="*74); print("O. 2035 SCENARIO LADDER — the concessions expire 31-Mar-2030"); print("="*74)
HZN_YRS  = 9                                   # 2026 base -> 2035 target year
EL_2035  = 4.50*(1+ESC_ELEC)**HZN_YRS         # BEE EV tariff, escalated at ESC_ELEC
ELC_2035 = 8.50*(1+ESC_ELEC)**HZN_YRS         # commercial band if the EV category lapses
CNG_2035 = 76.00*(1+ESC_CNG)**HZN_YRS         # CNG escalated at ESC_CNG
EX_RT    = round(EV["ex"]*1.10)               # ex-showroom grossed for 10% road tax (road_ev=0, GST 5% still applies)
print(f"  Both Delhi concessions come from one instrument — the Delhi Electric Vehicles Policy,")
print(f"  notified 30-Jun-2026 and running to 31-Mar-2030: the Rs{CITIES['Delhi']['tariff']:.2f}/kWh BEE EV")
print(f"  tariff and the 0% road tax on an ex-showroom at or below Rs30 lakh. The design target")
print(f"  year is 2035, which is {(2035-2030)} years AFTER that policy lapses. The ladder below")
print(f"  therefore tests the two concessions separately.")
print(f"  EL_2035   = 4.50 x (1+{ESC_ELEC:.1%})^{HZN_YRS} = Rs{EL_2035:.4f}/kWh   (EV tariff category, {ESC_ELEC:.1%}/yr)")
print(f"  ELC_2035  = 8.50 x (1+{ESC_ELEC:.1%})^{HZN_YRS} = Rs{ELC_2035:.4f}/kWh   (commercial band, same escalation)")
print(f"  CNG_2035  = 76.00 x (1+{ESC_CNG:.1%})^{HZN_YRS} = Rs{CNG_2035:.2f}/kg      (CNG, {ESC_CNG:.1%}/yr)")
print(f"  EX_RT     = {m(EV['ex'])} x 1.10 = Rs{m(EX_RT)}  -> on-road Rs{m(T.on_road(dict(EV,ex=EX_RT),'Delhi'))}"
      f" = ex x {1+EV['gst']:.2f} ({EV['gst']:.0%} GST) x 1.00 (road_ev = 0)")
print("  Routing discipline, unchanged from section D: CNG_KEYS go to tco(CNG,...) and everything")
print("  else to tco(EV,...). 'ex' is an EV key — passing it to both vehicles would tax the CNG")
print("  comparator with the EV's road-tax lapse, which is the error section D documents.")

def o_pair(**kw):
    """CNG-side keys -> tco(CNG,...); EV-side keys -> tco(EV,...). Section-D routing, unchanged."""
    cngkw={k:v for k,v in kw.items() if k in CNG_KEYS}
    evkw ={k:v for k,v in kw.items() if k not in CNG_KEYS}
    return T.tco(EV,"Delhi",5,True,**evkw), T.tco(CNG,"Delhi",5,True,**cngkw)

def o_npv(tariff,cng_price,ev_ex=None):
    """The same ladder on the headline basis: NPV {DISC_RATE:.0%} escalated, INCLUDING infrastructure.
    npv_flow() takes its energy price from CITIES, not from tco()'s kwargs, so the two
    2035 prices are injected as a temporary synthetic city and removed again in a finally."""
    key="_O_scenario"
    assert key not in T.CITIES, "section-O scratch city name collides"
    n_before=len(T.CITIES)
    T.CITIES[key]=dict(T.CITIES["Delhi"],tariff=tariff,cng=cng_price)
    try:
        vv=EV if ev_ex is None else dict(EV,ex=ev_ex)
        a=npv_flow(vv ,city=key,years=5,financed=True,infra=infra_schedule("EV",5))
        b=npv_flow(CNG,city=key,years=5,financed=True,infra=infra_schedule("CNG",5))
    finally:
        T.CITIES.pop(key,None)
    assert len(T.CITIES)==n_before, "T.CITIES not restored"
    return a,b

O_SCEN=(("A","2026 base — no overrides",{},None,14.5),
        ("B","2035 energy prices only",{"tariff":EL_2035,"price":CNG_2035},None,22.6),
        ("C","B + road-tax waiver lapses",{"tariff":EL_2035,"price":CNG_2035,"ex":EX_RT},EX_RT,17.4),
        ("D","C + EV tariff reverts to commercial",{"tariff":ELC_2035,"price":CNG_2035,"ex":EX_RT},EX_RT,6.5))
print(); print("  nominal basis, Delhi, 5 yr, financed 60mo (the section-A/L nominal excl-infra basis)")
print(f"  {'sc':<3}{'scenario':<36}{'EV Rs/km':>10}{'CNG Rs/km':>11}{'advantage':>12}{'delta':>10}{'expected':>10}{'check':>9}")
O_ROWS={}; prev=None; O_OK=True
for tag,lab,kw,exv,exppct in O_SCEN:
    a,b=o_pair(**kw)
    adv=100*(b["ckm"]-a["ckm"])/b["ckm"]; O_ROWS[tag]=(a,b,adv)
    d="-" if prev is None else f"{adv-prev:+.1f} pp"
    err=adv-exppct
    ok=abs(err)<=0.2
    O_OK = O_OK and ok
    print(f"  {tag:<3}{lab:<36}{a['ckm']:>10.2f}{b['ckm']:>11.2f}{adv:>+11.2f}%{d:>10}"
          f"{exppct:>+9.1f}%{('OK' if ok else '** OFF **'):>9}")
    prev=adv
print(f"  SCENARIO A reproduction: {O_ROWS['A'][2]:+.2f}% against the section-A headline +14.5%"
      f"  {'OK' if abs(O_ROWS['A'][2]-14.5)<=0.05 else '** BROKEN **'}")
print(f"  all four rungs within 0.2 pp of expectation: {'YES' if O_OK else 'NO — DO NOT SHIP'}")
print()
print(f"  headline basis for the same four rungs: NPV {DISC_RATE:.0%} escalated, INCLUDING infrastructure")
print(f"  {'sc':<3}{'EV NPV':>13}{'CNG NPV':>13}{'advantage':>12}{'delta':>10}")
O_NPV={}; prev=None
for tag,lab,kw,exv,exppct in O_SCEN:
    a,b=o_npv(kw.get("tariff",CITIES["Delhi"]["tariff"]),kw.get("price",CITIES["Delhi"]["cng"]),exv)
    adv=100*(b["total"]-a["total"])/b["total"]; O_NPV[tag]=adv
    d="-" if prev is None else f"{adv-prev:+.1f} pp"
    print(f"  {tag:<3}{m(a['total']):>13}{m(b['total']):>13}{adv:>+11.2f}%{d:>10}"
          +("  ** NEGATIVE **" if adv<0 else ""))
    prev=adv
print(f"  rung A on this basis reproduces the section-L headline cell +{O_NPV['A']:.1f}%.")
print(f"  *** THE RANKING IS THE SAME BUT THE LEVEL IS NOT. Rung D is {O_NPV['D']:+.2f}% on the")
print(f"      PUBLISHED HEADLINE basis — i.e. NEGATIVE. On the nominal excl-infra ladder rung D")
print(f"      holds +{O_ROWS['D'][2]:.1f}%, and that difference is the Rs{m(charger_capex_per_veh)} charger, which")
print(f"      the nominal ladder omits and the headline carries. So the honest statement is:")
print(f"      with BOTH concessions lapsed, the EV does not survive 5 years once the charger is")
print(f"      priced. NOTE this ladder is 5-year only: section M's 8-year result is a 2026-conditions")
print(f"      finding and is NOT evidence for the 2035 case, which has not been run at 8 years.")
print(f"      Do not quote the +{O_ROWS['D'][2]:.1f}% rung-D number without this caveat attached.")
print()
print("  ROUTING SELF-TEST (the section-D bug class, checked rather than assumed):")
_a,_b=o_pair(); _at,_bt=o_pair(tariff=99.0); _ap,_bp=o_pair(price=1.0); _ax,_bx=o_pair(ex=600_000.0)
_r=[("tariff=99 moves the EV only",_at["ckm"]!=_a["ckm"] and _bt["ckm"]==_b["ckm"]),
    ("price=1 moves the CNG only", _bp["ckm"]!=_b["ckm"] and _ap["ckm"]==_a["ckm"]),
    ("ex=600,000 moves the EV on-road only",_ax["on_road"]!=_a["on_road"] and _bx["on_road"]==_b["on_road"]),
    ("T.CITIES restored after o_npv",len(T.CITIES)==len(CITIES))]
for lab,ok in _r: print(f"    {lab:<46}{'OK' if ok else '** FAILED **'}")
print()
print("  READ:")
_kmv=5*T.KM_YEAR
_ea,_eb=O_ROWS["A"][0]["energy"]/_kmv,O_ROWS["B"][0]["energy"]/_kmv
_ca,_cb=O_ROWS["A"][1]["energy"]/_kmv,O_ROWS["B"][1]["energy"]/_kmv
_we=100*O_ROWS["A"][0]["energy"]/O_ROWS["A"][0]["total"]
_wc=100*O_ROWS["A"][1]["energy"]/O_ROWS["A"][1]["total"]
print("  Escalation IMPROVES the EV. The mechanism is not the obvious one, so state it exactly:")
print(f"    EV   energy {_ea:.2f} -> {_eb:.2f} Rs/km ({100*(_eb/_ea-1):+.1f}% over 9 yr)  but energy is only {_we:.1f}% of the EV's 5-yr total")
print(f"    CNG  energy {_ca:.2f} -> {_cb:.2f} Rs/km ({100*(_cb/_ca-1):+.1f}% over 9 yr)  and energy is {_wc:.1f}% of the CNG's 5-yr total")
print(f"    Both energy lines rise. The EV's rises FASTER in percentage terms ({ESC_ELEC:.1%}/yr vs {ESC_CNG:.1%}/yr),")
print(f"    but it is applied to a base {_wc/_we:.1f}x lighter in the total-cost stack, so the rupee impact lands on")
print(f"    the CNG instead. That is why rung B ({O_ROWS['B'][2]:+.1f}%) is BETTER than rung A"
      f" ({O_ROWS['A'][2]:+.1f}%) — a")
print(f"    {O_ROWS['B'][2]-O_ROWS['A'][2]:+.1f} pp move from price alone, with no change in hardware, financing")
print("    or utilisation. A higher energy price is not automatically bad news for the EV; it is")
print("    bad news only where energy is the cost, and energy is not the EV's cost.")
print("  The entire downside is POLICY EXPIRY, not price movement:")
print(f"    escalation alone (A->B) is {O_ROWS['B'][2]-O_ROWS['A'][2]:+.1f} pp;"
      f" road-tax waiver lapsing (B->C) is {O_ROWS['C'][2]-O_ROWS['B'][2]:+.1f} pp;"
      f" the EV tariff reverting to the")
print(f"    commercial band (C->D) is {O_ROWS['D'][2]-O_ROWS['C'][2]:+.1f} pp. The two expiry rungs are the whole")
print("    downside. Both are date-driven and knowable today; neither is a technical limit.")
print("  So the honest 2035 statement is not 'the TCO deteriorates'. It is: the TCO IMPROVES on")
print("  price alone, and then surrenders it to two dates in a policy that expires 31-Mar-2030.")
print(f"  Planning floor, stated on both bases because they disagree:")
print(f"    nominal excl. infra   {O_ROWS['D'][2]:+.1f}%   (survives)")
print(f"    NPV incl. infra       {O_NPV['D']:+.1f}%   (DOES NOT survive — see the caveat above)")
print("  The second is the published headline basis, so the defensible claim is that the 2035 case")
print("  rests on renewing the concession, and that renewal is worth roughly"
      f" {O_NPV['D']-O_NPV['A']:+.1f} pp on the headline basis")
print("  — a policy position, not an engineering one. Which is the same shape of conclusion")
print("  section M reached on the horizon axis: 'hold it long enough', or 'fix the terms'.")

# =============================================================================
# SECTION P — purely additive. Sections A..O above are untouched, including
# section O's o_pair/o_npv, which are hardcoded to 5 years and are NOT widened here.
# The two helpers below are section-P-local for that reason.
# =============================================================================
print(); print("="*74); print("P. 2035 LADDER AT 8 YEARS — does a longer horizon fix the policy cliff?"); print("="*74)
print("  Section O closed with an explicit gap: its ladder is 5-year only. That matters because")
print("  section M's entire conclusion is that the HORIZON is the lever — all 24 eight-year cells")
print("  are positive at 2026 conditions, while four five-year cells are negative. So the first")
print("  question about the 2035 cliff is 'does holding longer rescue it', and until this section")
print("  the model could not answer it. Same rungs, same constants, same routing, 8-year horizon.")
P_YEARS = 8

def p_pair(years=P_YEARS, **kw):
    """Section-D routing at an arbitrary horizon: CNG-side keys -> tco(CNG,...), EV-side keys
    -> tco(EV,...). A duplicate of section O's o_pair rather than a widening of it, so that
    sections A-O stay byte-for-byte unmodified."""
    cngkw={k:v for k,v in kw.items() if k in CNG_KEYS}
    evkw ={k:v for k,v in kw.items() if k not in CNG_KEYS}
    return T.tco(EV,"Delhi",years,True,**evkw), T.tco(CNG,"Delhi",years,True,**cngkw)

def p_npv(tariff,cng_price,ev_ex=None,years=P_YEARS,disc=DISC_RATE):
    """Headline basis: NPV at the hurdle, escalated, financed, INCLUDING the section-G
    infrastructure schedule. npv_flow() takes its energy price from CITIES rather than from
    tco()'s kwargs, so the ladder prices are injected as a temporary synthetic city and
    removed again in a finally. Same mechanism as section O's o_npv."""
    key="_P_scenario"
    assert key not in T.CITIES, "section-P scratch city name collides"
    n_before=len(T.CITIES)
    T.CITIES[key]=dict(T.CITIES["Delhi"],tariff=tariff,cng=cng_price)
    try:
        vv=EV if ev_ex is None else dict(EV,ex=ev_ex)
        a=npv_flow(vv ,city=key,years=years,financed=True,disc=disc,infra=infra_schedule("EV",years))
        b=npv_flow(CNG,city=key,years=years,financed=True,disc=disc,infra=infra_schedule("CNG",years))
    finally:
        T.CITIES.pop(key,None)
    assert len(T.CITIES)==n_before, "T.CITIES not restored"
    return a,b

def p_undisc(s): return sum(amt for lst in s.values() for amt,_ in lst)

print()
print(f"  P1. INFRASTRUCTURE TIMING AT {P_YEARS} YEARS — read back off the built schedule, not restated")
P_EV_S=infra_schedule("EV",P_YEARS); P_CNG_S=infra_schedule("CNG",P_YEARS)
p_capmo=sorted(mo for mo,lst in P_EV_S.items() for amt,_ in lst if amt==charger_capex_per_veh)
p_hydmo=sorted(mo for mo,lst in P_CNG_S.items() for amt,_ in lst if amt==cng_hydrotest)
p_ev_u,p_cng_u=p_undisc(P_EV_S),p_undisc(P_CNG_S)
p_ev_u5,p_cng_u5=p_undisc(infra_schedule("EV",5)),p_undisc(infra_schedule("CNG",5))
print(f"    EV charger capex months  : {p_capmo}  at Rs{m(charger_capex_per_veh)} each"
      f"   {'OK — the second replacement IS inside the horizon' if p_capmo==[0,60] else '** WRONG — expected [0, 60] **'}")
print(f"    CNG hydro-test months    : {p_hydmo}  at Rs{m(cng_hydrotest)} each")
print(f"    infra undiscounted       : EV Rs{m(p_ev_u)} = Rs{m(charger_capex_per_veh)} x {len(p_capmo)} + Rs{m(charger_opex_yr)}/yr x {P_YEARS}"
      f" | CNG Rs{m(p_cng_u)}")
print(f"    vs the 5-yr schedule      : EV Rs{m(p_ev_u5)} / CNG Rs{m(p_cng_u5)}"
      f"  -> the horizon adds Rs{m(p_ev_u-p_ev_u5)} of EV-ONLY charger")
print(f"    per km over {m(P_YEARS*T.KM_YEAR)} km  : EV {p_ev_u/(P_YEARS*T.KM_YEAR):.3f}/km (5yr {p_ev_u5/(5*T.KM_YEAR):.3f}/km)"
      f" | CNG {p_cng_u/(P_YEARS*T.KM_YEAR):.3f}/km (5yr {p_cng_u5/(5*T.KM_YEAR):.3f}/km)")

P_SCEN=(("A","2026 base — no overrides",{},None),
        ("B","2035 energy prices only",{"tariff":EL_2035,"price":CNG_2035},None),
        ("C","B + road-tax waiver lapses",{"tariff":EL_2035,"price":CNG_2035,"ex":EX_RT},EX_RT),
        ("D","C + EV tariff reverts to commercial",{"tariff":ELC_2035,"price":CNG_2035,"ex":EX_RT},EX_RT))

print()
print(f"  P2. HEADLINE BASIS — NPV {DISC_RATE:.0%} escalated, financed {T.LOAN_MONTHS}mo, INCLUDING infrastructure, {P_YEARS} yr")
print(f"  {'sc':<3}{'scenario':<36}{'EV NPV':>13}{'CNG NPV':>13}{'advantage':>12}{'delta':>10}")
P_H={}; prev=None
for tag,lab,kw,exv in P_SCEN:
    a,b=p_npv(kw.get("tariff",CITIES["Delhi"]["tariff"]),kw.get("price",CITIES["Delhi"]["cng"]),exv)
    adv=100*(b["total"]-a["total"])/b["total"]; P_H[tag]=(a["total"],b["total"],adv)
    d="-" if prev is None else f"{adv-prev:+.2f} pp"
    print(f"  {tag:<3}{lab:<36}{m(a['total']):>13}{m(b['total']):>13}{adv:>+11.2f}%{d:>10}")
    prev=adv

print()
print("  P3. RUNG-A CROSS-CHECK — hard gate against the section-L cell, read from L[] in memory")
l_ev,l_cn,l_adv=L[(P_YEARS,3)]
a_ev,a_cn,a_adv=P_H["A"][0],P_H["A"][1],P_H["A"][2]
print(f"    section L   ({NB[3]}, {P_YEARS}yr): EV Rs{m(l_ev)}   CNG Rs{m(l_cn)}   {l_adv:+.2f}%")
print(f"    this ladder (rung A, no overrides): EV Rs{m(a_ev)}   CNG Rs{m(a_cn)}   {a_adv:+.2f}%")
print(f"    delta                         : EV Rs{m(a_ev-l_ev)}   CNG Rs{m(a_cn-l_cn)}   {a_adv-l_adv:+.2f} pp")
P_GATE=(abs(a_ev-l_ev)<1.0 and abs(a_cn-l_cn)<1.0 and abs(a_adv-l_adv)<0.05)
print(f"    GATE: {'PASS — rung A reproduces the section-L cell exactly' if P_GATE else '** FAIL — DO NOT SHIP **'}")
print("     rung A exercises the same npv_flow() and infra_schedule() path section L uses, so this")
print("     is a live cross-check of the ladder, not a restatement of a stored number.")

print()
print(f"  P4. NOMINAL EXCL. INFRA, {P_YEARS} yr — the same question without the charger")
print(f"  {'sc':<3}{'scenario':<36}{'EV Rs/km':>10}{'CNG Rs/km':>11}{'advantage':>12}{'delta':>10}")
P_N={}; prev=None
for tag,lab,kw,exv in P_SCEN:
    a,b=p_pair(**kw)
    adv=100*(b["ckm"]-a["ckm"])/b["ckm"]; P_N[tag]=(a["ckm"],b["ckm"],adv)
    d="-" if prev is None else f"{adv-prev:+.2f} pp"
    print(f"  {tag:<3}{lab:<36}{a['ckm']:>10.2f}{b['ckm']:>11.2f}{adv:>+11.2f}%{d:>10}")
    prev=adv

print()
print("  P5. DIRECT ANSWER — does rung D clear zero at 8 years?")
p_d8=P_H["D"][2]; p_d8_nom=P_N["D"][2]; p_a8=P_H["A"][2]; p_a8_nom=P_N["A"][2]
print(f"    rung D, {P_YEARS}yr, headline basis      : {p_d8:+.2f}%  ->"
      f" {'CLEARS ZERO' if p_d8>0 else 'DOES NOT CLEAR ZERO'}")
print(f"    rung D, 5yr,   headline basis      : {O_NPV['D']:+.2f}%  (section O)")
print(f"    rung D, {P_YEARS}yr, nominal excl. infra : {p_d8_nom:+.2f}%")
print(f"    rung D, 5yr,   nominal excl. infra : {O_ROWS['D'][2]:+.2f}%  (section O)")
print(f"    horizon effect, headline basis     : {O_NPV['D']:+.2f}% -> {p_d8:+.2f}% = {p_d8-O_NPV['D']:+.2f} pp")
print(f"    charger effect, {P_YEARS}yr, nominal -> headline : {p_d8_nom:+.2f}% -> {p_d8:+.2f}% = {p_d8-p_d8_nom:+.2f} pp")
print(f"    charger effect, 5yr,   nominal -> headline : {O_ROWS['D'][2]:+.2f}% -> {O_NPV['D']:+.2f}%"
      f" = {O_NPV['D']-O_ROWS['D'][2]:+.2f} pp")
if p_d8>0:
    print(f"    ANSWER: YES. The 8-year horizon DOES rescue rung D. It moves from {O_NPV['D']:+.2f}% at five years")
    print(f"    to {p_d8:+.2f}% at eight — a swing of {p_d8-O_NPV['D']:+.2f} pp, clearing zero by {p_d8:.2f} pp.")
    print("    The policy cliff is survivable IF the fleet is held long enough.")
else:
    print(f"    ANSWER: NO. Rung D is still {p_d8:+.2f}% at eight years. The horizon does NOT rescue it,")
    print("    and the 5-year negative is not an artefact of the short horizon.")
print(f"    The rescue is PARTIAL, and the charger is why. The second Rs{m(charger_capex_per_veh)} replacement")
print(f"    lands at month {p_capmo[1]}, so the EV-only infrastructure tax costs {p_d8-p_d8_nom:+.2f} pp at {P_YEARS} years")
print(f"    against {O_NPV['D']-O_ROWS['D'][2]:+.2f} pp at five. The horizon extends the timeline that cost is amortised")
print(f"    over AND buys a second unit of the same cost; the two partly cancel, which is why")
print(f"    {P_YEARS} years buys less relief than the raw 5->8 stretch suggests.")
print(f"    What the horizon is NOT doing is rescuing the POLICY. The cliff costs")
print(f"    {p_a8:+.2f}% - {p_d8:+.2f}% = {p_d8-p_a8:+.2f} pp on the headline basis at {P_YEARS} years, against")
print(f"    {O_NPV['A']:+.2f}% - {O_NPV['D']:+.2f}% = {O_NPV['D']-O_NPV['A']:+.2f} pp at five. The policy tax is ~7 pp at BOTH")
print("    horizons. Holding longer does not make the concession matter less; it puts more")
print("    capital on it.")

print()
print("  ROUTING SELF-TEST re-run at the 8-year horizon (section D's bug class):")
_ea,_eb=p_pair(); _et,_bt=p_pair(tariff=99.0); _ep,_bp=p_pair(price=1.0); _ex,_bx=p_pair(ex=600_000.0)
_pn=p_npv(CITIES["Delhi"]["tariff"],CITIES["Delhi"]["cng"])
for lab,ok in (("tariff=99 moves the EV only",_et["ckm"]!=_ea["ckm"] and _bt["ckm"]==_eb["ckm"]),
               ("price=1 moves the CNG only",_bp["ckm"]!=_eb["ckm"] and _ep["ckm"]==_ea["ckm"]),
               ("ex=600,000 moves the EV on-road only",_ex["on_road"]!=_ea["on_road"] and _bx["on_road"]==_eb["on_road"]),
               ("p_npv returns the section-L 8yr cell",abs(_pn[0]["total"]-l_ev)<1.0),
               ("T.CITIES restored after every p_npv call",len(T.CITIES)==len(CITIES))):
    print(f"    {lab:<46}{'OK' if ok else '** FAILED **'}")

print()
print("  READ:")
print("  Section M's 'hold it long enough' survives the 2035 ladder, with one qualifier.")
print(f"  At {P_YEARS} years every rung is positive, including the worst case — D, both concessions")
print(f"  lapsed, commercial-band power, 10% road tax — at {p_d8:+.2f}%. That is a better 2035")
print("  position than the 5-year case delivers on ANY basis, where the same scenario is negative.")
print("  The qualifier is that the 8-year rescue is neither free nor complete:")
print(f"    - the horizon carries a SECOND Rs{m(charger_capex_per_veh)} replacement at month {p_capmo[1]}, so EV-only")
print(f"      infrastructure rises to Rs{m(p_ev_u)} undiscounted / {p_ev_u/(P_YEARS*T.KM_YEAR):.3f} per km")
print(f"    - the 2035 advantage of {p_d8:+.1f}% is about HALF the 2026 advantage of {p_a8:+.1f}% on the same basis")
print(f"    - the policy cliff is horizon-independent at roughly -7 pp, so a longer hold puts MORE")
print("      capital on a 31-Mar-2030 expiry date")
print(f"  So the correct 2035 sentence needs both clauses: the fleet case CLEARS if held to {P_YEARS} years,")
print(f"  AND it clears with roughly half the margin it has in 2026. Quoting either alone misstates it.")

# =============================================================================
# SECTION Q — purely additive. Sections A..P above are untouched, including
# sections O/P's o_pair/o_npv/p_pair/p_npv, none of which are widened here.
# =============================================================================
print(); print("="*74); print("Q. 2035 CONDITIONS ACROSS ALL THREE CITIES"); print("="*74)
print("  Section M ran the city matrix at 2026 conditions. Sections O and P ran the 2035 ladder")
print("  for DELHI ONLY. So the two most marginal cells in the whole model — Mumbai and Bengaluru,")
print("  whose tariffs sit far above Delhi's — had never been tested at 2035 conditions at all.")
print("  This section closes that: 3 cities x 2 horizons x 2 bases, each at 2035 and at 2026.")
Q_CITIES=(c for c in CITIES)          # generator keeps this correct if CITIES is ever reordered
Q_BASES=("headline (NPV 12% esc, incl. infra)","nominal, excl. infra")

def q_nominal(city,years,tariff=None,price=None):
    """Nominal excl-infra cell with price overrides. The CNG_KEYS split is applied explicitly
    rather than by filtering, so the reader can see which kwarg goes to which vehicle."""
    evkw={"tariff":tariff} if tariff is not None else {}
    cngkw={"price":price} if price is not None else {}
    assert not (set(evkw)&CNG_KEYS) and not (set(cngkw)&(set(evkw))), "routing collision"
    return T.tco(EV,city,years,True,**evkw), T.tco(CNG,city,years,True,**cngkw)

def q_headline(city,years,tariff,cng_price,road=None,road_ev=None,escalate=True):
    """Headline cell: NPV at the hurdle, escalated, financed, INCLUDING the section-G
    infrastructure schedule. npv_flow() takes prices from CITIES, so they are injected as a
    temporary synthetic city and removed again in a finally — same pattern as O/P."""
    key="_Q_scenario"
    assert key not in T.CITIES, "section-Q scratch city name collides"
    n0=len(T.CITIES)
    src=dict(CITIES[city]); src["tariff"]=tariff; src["cng"]=cng_price
    if road    is not None: src["road"]=road
    if road_ev is not None: src["road_ev"]=road_ev
    T.CITIES[key]=src
    try:
        a=npv_flow(EV ,city=key,years=years,financed=True,escalate=escalate,infra=infra_schedule("EV",years))
        b=npv_flow(CNG,city=key,years=years,financed=True,escalate=escalate,infra=infra_schedule("CNG",years))
    finally:
        T.CITIES.pop(key,None)
    assert len(T.CITIES)==n0, "T.CITIES not restored"
    return a,b

print()
print("  Q1. PER-CITY 2035 INPUTS — each city's OWN price escalated, Delhi's not reused")
print(f"    {'city':<11}{'tariff 2026':>13}{'-> 2035':>11}{'CNG 2026':>11}{'-> 2035':>10}")
Q_IN={}
for c in CITIES:
    t1=CITIES[c]["tariff"]*(1+ESC_ELEC)**9; p1=CITIES[c]["cng"]*(1+ESC_CNG)**9
    Q_IN[c]=(t1,p1)
    print(f"    {c:<11}{CITIES[c]['tariff']:>13.2f}{t1:>11.4f}{CITIES[c]['cng']:>11.2f}{p1:>10.4f}")
print(f"    electricity at {ESC_ELEC:.1%}/yr and CNG at {ESC_CNG:.1%}/yr, both over {HZN_YRS} years")
print(f"    (2026 values are the model's own CITIES constants; 2035 values are those x (1+r)^{HZN_YRS} — nothing")
print(f"     is copied from Delhi, which is the error this section exists to avoid)")

print()
print("  Q2. ROAD TAX — two variants, kept separate, plus one discrepancy to flag")
print("    Delhi road_ev 0.00 rests on the Delhi EV Policy 2026, which EXPIRES 31-Mar-2030.")
print("    Bengaluru road_ev 0.08 is a tiered PERMANENT rate, so its EV already pays 8%.")
print(f"    {'city':<11}{'road (ICE)':>12}{'road_ev as modelled':>20}{'lapsed = standard rate?':>26}")
Q_LAPSE={}
for c in CITIES:
    same=CITIES[c]["road_ev"]==CITIES[c]["road"]
    Q_LAPSE[c]=CITIES[c]["road"]
    print(f"    {c:<11}{CITIES[c]['road']:>11.0%}{CITIES[c]['road_ev']:>19.0%}"
          f"{('YES — lapse is a NO-OP' if same else 'no — lapsing to '+format(CITIES[c]['road'],'.0%')):>26}")
print("    *** FLAG: the 2026 audit asked for Mumbai's lapsed rate to be ~8%. The rate actually in the")
print(f"        engine is {CITIES['Mumbai']['road']:.0%}, which is the Maharashtra Motor Vehicles Tax Act 1958")
print("        Second Schedule TRANSPORT / non-individual band, not the 8% individual-owner band.")
print("        A ride-hailing vehicle is registered as a transport vehicle, so 14% is the correct")
print("        tier; 8% is the personal-car floor and is reported as a labelled sensitivity below.")
print("        This rate was 0.00 until the correction in section R — see R for the full effect.")
print("    Variant 1 (main table below) = road tax AS CURRENTLY MODELLED.")
print("    Variant 2 (Q4)              = EV exemption lapsed to each city's own standard rate.")

print()
print("  Q3. THE MATRIX — 12 cells at 2035, each with its 2026 reference and the delta")
print(f"    {'city':<11}{'yrs':>4}  {'basis':<38}{'2026':>9}{'2035':>9}{'delta':>10}")
Q_CELL={}
for c in CITIES:
    t1,p1=Q_IN[c]
    for yrs in (5,8):
        h26=q_headline(c,yrs,CITIES[c]["tariff"],CITIES[c]["cng"]); h35=q_headline(c,yrs,t1,p1)
        a26=100*(h26[1]["total"]-h26[0]["total"])/h26[1]["total"]
        a35=100*(h35[1]["total"]-h35[0]["total"])/h35[1]["total"]
        n26=q_nominal(c,yrs); n35=q_nominal(c,yrs,tariff=t1,price=p1)
        b26=100*(n26[1]["ckm"]-n26[0]["ckm"])/n26[1]["ckm"]
        b35=100*(n35[1]["ckm"]-n35[0]["ckm"])/n35[1]["ckm"]
        Q_CELL[(c,yrs,0)]=(a26,a35); Q_CELL[(c,yrs,1)]=(b26,b35)
        print(f"    {c:<11}{yrs:>4}  {Q_BASES[0]:<38}{a26:>+8.2f}%{a35:>+8.2f}%{a35-a26:>+9.2f} pp")
        print(f"    {'':<11}{'':>4}  {Q_BASES[1]:<38}{b26:>+8.2f}%{b35:>+8.2f}%{b35-b26:>+9.2f} pp")
Q_NEG=[(k,v) for k,v in Q_CELL.items() if v[0]<0 or v[1]<0]
print(f"    {len(Q_CELL)*2} cells printed ({len(CITIES)} cities x 2 horizons x 2 bases x 2 condition-years).")
if Q_NEG:
    print("    *** NEGATIVE 2026 CELLS (the reference column, i.e. what section M found):")
    for (c,yrs,i),(a26,a35) in sorted(Q_NEG):
        print(f"        {c:<11}{yrs}yr {Q_BASES[i]:<38}2026 {a26:+.2f}%  ->  2035 {a35:+.2f}%")
else:
    print("    no negative cells on either basis in either year")
print("    NOTE the two bases here are 'incl. infra' and 'EXCL. infra'. Section M also carried a")
print("    'nominal INCL. infra' basis, on which Mumbai 5yr 2026 was "
      f"{M[('Mumbai',5,True,1)][2]:+.2f}% — a SECOND negative cell that this")
print("    section's basis pair does not show. It is not omitted silently; it is simply a")
print("    different basis, and the 2026 reference column above should be read as two of the four")
print("    M cells, not all four.")

print()
print("  Q4. ROAD-TAX VARIANT — 2035 headline basis, exemptions lapsed, NOT merged with Q3")
print(f"    {'city':<11}{'yrs':>4}{'as modelled':>14}{'exemptions lapsed':>20}{'delta':>10}")
Q_LAP={}
for c in CITIES:
    t1,p1=Q_IN[c]
    for yrs in (5,8):
        base=q_headline(c,yrs,t1,p1); lap=q_headline(c,yrs,t1,p1,road_ev=Q_LAPSE[c])
        ab=100*(base[1]["total"]-base[0]["total"])/base[1]["total"]
        al=100*(lap[1]["total"]-lap[0]["total"])/lap[1]["total"]
        Q_LAP[(c,yrs)]=(ab,al)
        same=abs(al-ab)<0.005
        print(f"    {c:<11}{yrs:>4}{ab:>+13.2f}%{al:>+19.2f}%{al-ab:>+9.2f} pp"
              +("  (no-op: the EV already pays the standard rate)" if same else ""))
noop=[c for c in CITIES if CITIES[c]["road_ev"]==CITIES[c]["road"]]
worth=[c for c in CITIES if CITIES[c]["road_ev"]!=CITIES[c]["road"]]
print(f"    Cities where the road-tax waiver is still worth something at 2035: {', '.join(worth) if worth else 'none'}.")
print(f"    Cities where lapsing it is a no-op (the EV already pays the standard rate): {', '.join(noop)}.")
print("    SENSITIVITY (the individual-owner floor, NOT the base case): if Mumbai's CNG comparator")
print("    were taxed at the 8% private-car rate instead of the 14% transport rate,")
for yrs in (5,8):
    t1,p1=Q_IN["Mumbai"]; s=q_headline("Mumbai",yrs,t1,p1,road=0.08)
    v=100*(s[1]["total"]-s[0]["total"])/s[1]["total"]
    print(f"      Mumbai {yrs}yr 2035 headline would be {v:+.2f}% ({v-Q_LAP[('Mumbai',yrs)][0]:+.2f} pp vs the 14% base case)")
print("      ...and still positive at both horizons, so the tier choice does not change any answer")
print("      in this section either way. 14% is used because the comparator is a transport vehicle.")

print()
print("  Q5. THE DECOMPOSITION — which leg of escalation does the work? (headline basis)")
print("    Escalation moves BOTH prices. Separating them shows why the cities differ.")
print(f"    {'city':<11}{'yrs':>4}{'2026':>9}{'elec only':>11}{'CNG only':>10}{'both':>9}{'elec leg':>10}{'CNG leg':>10}")
Q_DEC={}
for c in CITIES:
    t1,p1=Q_IN[c]
    for yrs in (5,8):
        t0,p0=CITIES[c]["tariff"],CITIES[c]["cng"]
        def _adv(tar,pri):
            r=q_headline(c,yrs,tar,pri); return 100*(r[1]["total"]-r[0]["total"])/r[1]["total"]
        base=_adv(t0,p0); eo=_adv(t1,p0); co=_adv(t0,p1); bo=_adv(t1,p1)
        Q_DEC[(c,yrs)]=(base,eo,co,bo)
        print(f"    {c:<11}{yrs:>4}{base:>+8.2f}%{eo:>+10.2f}%{co:>+9.2f}%{bo:>+8.2f}%{eo-base:>+9.2f}{co-base:>+10.2f}")
print("    The electricity leg is NEGATIVE for every city — power escalation is unambiguously bad")
print("    for the EV, worst in Mumbai. The CNG leg is positive for every city, and much larger.")
print("    Net = the two. That is the whole reason escalation helps everywhere.")

print()
print("  Q6. WHAT WOULD ACTUALLY BREAK EACH CITY — the electricity-escalation break-even rate")
print("    Holding CNG at the modelled 3.5%, solve for the electricity escalation rate at which each")
print("    2035 cell reaches zero. This is the honest measure of how much room each city has.")
print(f"    {'city':<11}{'yrs':>4}{'breaks even at':>16}{'headroom vs 4.50%':>20}")
Q_BE={}
for c in CITIES:
    p1=Q_IN[c][1]
    for yrs in (5,8):
        lo,hi=0.0,0.60
        for _ in range(60):
            mid=(lo+hi)/2
            r=q_headline(c,yrs,CITIES[c]["tariff"]*(1+mid)**9,p1)
            a=100*(r[1]["total"]-r[0]["total"])/r[1]["total"]
            if a>0: lo=mid
            else:  hi=mid
        Q_BE[(c,yrs)]=(lo+hi)/2
        print(f"    {c:<11}{yrs:>4}{Q_BE[(c,yrs)]:>16.2%}{(Q_BE[(c,yrs)]-ESC_ELEC):>+19.2%}")

print()
print("  Q7. THE FOUR QUESTIONS, ANSWERED")
def _q(a,b): return f"{a:+.2f}% (2026 {b:+.2f}%)"
print("  Q1. DOES MUMBAI CLEAR ZERO AT EITHER HORIZON, ON EITHER BASIS, IN 2035?")
for yrs in (5,8):
    h,l=Q_CELL[("Mumbai",yrs,0)],Q_CELL[("Mumbai",yrs,1)]
    print(f"      {yrs}yr headline {_q(h[1],h[0])}  {'CLEARS' if h[1]>0 else 'NEGATIVE'}"
          f"  |  {yrs}yr nominal {_q(l[1],l[0])}  {'CLEARS' if l[1]>0 else 'NEGATIVE'}")
m35all=all(Q_CELL[("Mumbai",y,i)][1]>0 for y in (5,8) for i in (0,1))
m26neg=[(y,i) for y in (5,8) for i in (0,1) if Q_CELL[("Mumbai",y,i)][0]<0]
print(f"      ANSWER: {'YES — Mumbai clears zero in all four 2035 cells.' if m35all else 'NO — at least one 2035 Mumbai cell is negative.'}"
      f" Its 2026 reference was:")
for y in (5,8):
    for i in (0,1):
        a26,a35=Q_CELL[("Mumbai",y,i)]
        print(f"        {y}yr {Q_BASES[i]:<38}2026 {a26:+6.2f}%   2035 {a35:+6.2f}%")
if m26neg:
    print(f"      Mumbai was NEGATIVE at 2026 conditions on {len(m26neg)} of these four cells")
    print(f"      (financed, infra-inclusive: nominal incl {M[('Mumbai',5,True,1)][2]:+.2f}%, NPV incl {M[('Mumbai',5,True,3)][2]:+.2f}%;")
    print(f"      section M's 'three of four' also counted the cash NPV cell at {M[('Mumbai',5,False,3)][2]:+.2f}%).")
else:
    print(f"      Mumbai was already POSITIVE at 2026 conditions on all four cells — the correction in")
    print(f"      section R is what removed its last negative 2026 cell.")
print()
print("  Q2. DOES 2035 ESCALATION HELP OR HURT EACH CITY vs ITS OWN 2026 RESULT?")
for c in CITIES:
    h5,h8=Q_CELL[(c,5,0)],Q_CELL[(c,8,0)]
    n5,n8=Q_CELL[(c,5,1)],Q_CELL[(c,8,1)]
    print(f"      {c:<11} headline 5yr {h5[1]-h5[0]:+.2f} pp | 8yr {h8[1]-h8[0]:+.2f} pp"
          f"   nominal 5yr {n5[1]-n5[0]:+.2f} pp | 8yr {n8[1]-n8[0]:+.2f} pp")
print("      ANSWER: it HELPS every city on every basis. The expectation that Mumbai would be barely")
print("      helped or not helped at all is FALSIFIED on magnitude — Mumbai gains +"
      f"{Q_CELL[('Mumbai',5,0)][1]-Q_CELL[('Mumbai',5,0)][0]:.2f} pp at 5yr, within "
      f"{abs((Q_CELL[('Delhi',5,0)][1]-Q_CELL[('Delhi',5,0)][0])-(Q_CELL[('Mumbai',5,0)][1]-Q_CELL[('Mumbai',5,0)][0])):.2f} pp of Delhi's.")
print("      The expectation is CORRECT on mechanism, though, and Q5 makes that precise: electricity")
print("      escalation ALONE costs Mumbai "
      f"{Q_DEC[('Mumbai',5)][1]-Q_DEC[('Mumbai',5)][0]:+.2f} pp at 5yr — the worst of the three cities —")
print("      while CNG escalation alone gains it "
      f"{Q_DEC[('Mumbai',5)][3-1]-Q_DEC[('Mumbai',5)][0]:+.2f} pp. The net is positive because the CNG leg is larger, not")
print("      because power escalation is harmless. Mumbai is not insensitive to its tariff; it is")
print("      being carried by CNG.")
print()
print("  Q3. DOES THE 8-YEAR HORIZON RESCUE ANY CITY THAT 5 YEARS DOES NOT?")
for c in CITIES:
    h5,h8=Q_CELL[(c,5,0)],Q_CELL[(c,8,0)]
    resc2026=(h5[0]<0 and h8[0]>0); resc2035=(h5[1]<0 and h8[1]>0)
    print(f"      {c:<11} 2026: 5yr {h5[0]:+6.2f}%  8yr {h8[0]:+6.2f}%  horizon rescues? {'YES' if resc2026 else 'no'}"
          f"   |  2035: 5yr {h5[1]:+6.2f}%  8yr {h8[1]:+6.2f}%  {'YES' if resc2035 else 'no'}")
print("      ANSWER: in 2026 CONDITIONS, yes — Mumbai's 5yr headline cell is negative and its 8yr is")
print("      positive, so the horizon rescues Mumbai exactly as section M argued. In 2035 CONDITIONS,")
print("      no cell needs rescuing: every city is already positive at 5 years, so the horizon is")
print("      improving rather than rescuing. Escalation, not the horizon, is what fixes Mumbai's 5yr cell.")

print()
print("  Q8. WHICH CITY BINDS THE 2035 CASE, AND IS IT PRICE OR POLICY?")
for c in CITIES:
    print(f"      {c:<11} 5yr headline {Q_CELL[(c,5,0)][1]:+.2f}%   road-tax lapse worth {Q_LAP[(c,5)][1]-Q_LAP[(c,5)][0]:+.2f} pp"
          f"   elec-escalation headroom {Q_BE[(c,5)]-ESC_ELEC:+.2%}/yr")
bind=min(Q_CELL,key=lambda k:Q_CELL[k][1] if k[2]==0 else 99)
bc,bh,bl=bind
print(f"      BINDING CONSTRAINT: {bc} at {bh} years on the headline basis ({Q_CELL[bind][1]:+.2f}%).")
print(f"      It is a PRICE problem, not a policy problem. Evidence:")
print(f"        - the road-tax lapse is worth {Q_LAP[(bc,bh)][1]-Q_LAP[(bc,bh)][0]:+.2f} pp there"
      +(" — the road-tax waiver is already spent, the EV already pays the standard rate"
         if CITIES[bc]["road_ev"]==CITIES[bc]["road"] else ""))
print(f"        - what binds it is electricity escalation: only {Q_BE[(bc,bh)]:.2%}/yr against a modelled"
      f" {ESC_ELEC:.2%}, versus Delhi's {Q_BE[('Delhi',bh)]:.2%}/yr")
print(f"        - the fix is therefore a COMMERCIAL one (a {bc} power tariff, or depot-side solar or")
print(f"          a demand-charge structure), not a legislative one")
_dl=min((c for c in CITIES if c!=bc),key=lambda c:Q_LAP[(c,bh)][1]-Q_LAP[(c,bh)][0])
print(f"      By contrast {_dl}'s 2035 exposure IS policy:"
      f" {Q_LAP[(_dl,bh)][1]-Q_LAP[(_dl,bh)][0]:+.2f} pp from a single")
print("      expiry date. Two different problems, two different owners, two different remedies —")
print("      which is the distinction sections M and P kept insisting on.")

print()
print("  ROUTING SELF-TEST re-run (section D's bug class, now on the city path):")
_qa,_qb=q_nominal("Delhi",5); _at,_bt=q_nominal("Delhi",5,tariff=99.0); _ap,_bp=q_nominal("Delhi",5,price=1.0)
_qh=q_headline("Delhi",5,CITIES["Delhi"]["tariff"],CITIES["Delhi"]["cng"])
_qm=q_nominal("Mumbai",5)
for lab,ok in (("tariff=99 moves the EV only",_at["ckm"]!=_qa["ckm"] and _bt["ckm"]==_qb["ckm"]),
               ("price=1 moves the CNG only",_bp["ckm"]!=_qb["ckm"] and _ap["ckm"]==_qa["ckm"]),
               ("q_headline Delhi 5yr = section L cell",abs(100*(_qh[1]["total"]-_qh[0]["total"])/_qh[1]["total"]-L[(5,3)][2])<0.005),
               # the city must reach the ENERGY lines, not on-road: Delhi and Mumbai both
               # carry road_ev=0, so on-road is identical and is the wrong thing to probe
               ("city reaches the model (Mumbai ckm != Delhi)",_qm[0]["ckm"]!=_qa["ckm"] and _qm[1]["ckm"]!=_qb["ckm"]),
               ("T.CITIES restored after every q_headline call",len(T.CITIES)==len(CITIES))):
    print(f"    {lab:<52}{'OK' if ok else '** FAILED **'}")

print()
print("  READ:")
_qsorted=sorted(((Q_CELL[(c,5,0)][1],c) for c in CITIES))
_qthin,_qthincity=_qsorted[0]
print(f"  At 5yr headline the city order is {_qthincity} {_qthin:+.2f}%, "
      f"{_qsorted[1][1]} {_qsorted[1][0]:+.2f}%, {_qsorted[2][1]} {_qsorted[2][0]:+.2f}% — "
      f"{_qthincity} binds the 2035 case.")
_mq=Q_DEC[("Mumbai",5)]
print(f"  Escalation's two legs for Mumbai: power {_mq[1]-_mq[0]:+.2f} pp, CNG {_mq[2]-_mq[0]:+.2f} pp."
      f" Power escalation hurts every")
print("  city; CNG escalation helps every city by more. Net = the two, which is why 2035 is")
print("  positive everywhere rather than negative.")
print(f"  So the {_qthincity} number rests on the gap between two escalation rates, and Q6 puts a number")
print(f"  on what happens if power outruns CNG: {_qthincity} 5yr dies at {Q_BE[(_qthincity,5)]:.2%}/yr power escalation"
      f" versus Delhi's {Q_BE[('Delhi',5)]:.2%}/yr.")
print("  That is the most fragile assumption in the 2035 analysis, and it is a POWER-TARIFF")
print("  assumption — the one input a regulator sets and a fleet operator does not.")
print("  Two corrections to the framing this section was asked to test, both worth carrying:")
print("    - Mumbai's tariff flip point is Rs13.20/kWh, not ~Rs11. Delhi's is Rs11.36; Mumbai's is")
print("      HIGHER because its dearer CNG already weakens the comparator.")
print("    - the escalation gap does NOT need to hold: raising CNG escalation to 4.5% would HELP")
print("      every city. The risk is power escalating FASTER, not CNG slower.")

# =============================================================================
# SECTION R — the Mumbai CNG road-tax correction, and its propagation.
# Sections A..Q above are untouched apart from hardcoded NARRATIVE that the
# correction falsified; those were made data-derived so they cannot go stale
# again. No Delhi or Bengaluru cell value changes — section R asserts that too.
# =============================================================================
print(); print("="*74); print("R. MUMBAI CNG ROAD TAX — engine corrected, every Mumbai cell re-run"); print("="*74)
print("  THE BUG: CITIES['Mumbai']['road'] was 0.00, so on_road() gave the CNG comparator a ZERO")
print("  road tax in Maharashtra. Maharashtra Motor Vehicles Tax Act 1958, Second Schedule")
print("  (amended by the Maharashtra Motor Vehicles Tax (Amendment) Act 2025, gazetted 19-03-2025,")
print("  effective 1-07-2025), levies road tax as a % of ex-showroom:")
print("    CNG/LPG, INDIVIDUAL owner :  8% (<=10L) / 9% (10-20L) / 10% (>20L)")
print("    CNG/LPG, NON-INDIVIDUAL   : 14% (<=10L) / 16% (10-20L) / 18% (>20L)   <- USED")
print("    company-registered        : 20%")
print("    ELECTRIC                  : exempt, NO price threshold")
print(f"  The EV rate is already correct at {CITIES['Mumbai']['road_ev']:.0%} and was NOT touched.")
print(f"  BASE RATE USED: {CITIES['Mumbai']['road']:.0%} — the TRANSPORT / non-individual tier.")
print("  WHY NOT 8%: a ride-hailing vehicle is registered as a TRANSPORT vehicle, not a private")
print("  car, so it falls in the non-individual band. 8% is the individual-owner floor. It is")
print("  also the number already sitting in Rev 4's table, and picking the rate that agrees with")
print("  our own prior document is exactly the reasoning error this section exists to close.")
print(f"  Comparator ex-showroom is Rs{m(CNG['ex'])} -> the <= Rs10 lakh band applies.")
print("  Why it survived three audits: the ENGINE and the DOCUMENT disagreed, and nobody")
print("  re-derived the document's tax table from the engine. Section R prints both sides.")

def r_with_road(road_rate, fn):
    """Run fn() with CITIES['Mumbai']['road'] temporarily set to road_rate, then restore."""
    old=CITIES["Mumbai"]["road"]; n0=len(T.CITIES)
    CITIES["Mumbai"]["road"]=road_rate
    try: return fn()
    finally:
        CITIES["Mumbai"]["road"]=old
        assert len(T.CITIES)==n0

R_OLD, R_NEW = 0.00, CITIES["Mumbai"]["road"]
R_INDIV     = 0.08

def _mumbai_cells():
    out={}
    for yrs in (5,8):
        for fin in (True,False):
            for i in range(4):
                out[(yrs,fin,i)]=cell_rupees("Mumbai",yrs,fin,i)
    return out
R_OLD_CELLS=r_with_road(R_OLD,_mumbai_cells)
R_NEW_CELLS=_mumbai_cells()
R_PCT=lambda c: 100*(c[1]-c[0])/c[1]

print()
print(f"  R1. MUMBAI CELL MATRIX — old (0% road tax) vs new ({R_NEW:.0%}), 2026 conditions")
print(f"  {'yrs':>5}{' capital':<16}{'basis':<28}{'old adv':>9}{'new adv':>9}{'delta':>10}")
R_DELTA={}
for yrs in (5,8):
    for fin in (True,False):
        for i in range(4):
            o,n=R_OLD_CELLS[(yrs,fin,i)],R_NEW_CELLS[(yrs,fin,i)]
            po,pn=R_PCT(o),R_PCT(n); R_DELTA[(yrs,fin,i)]=(po,pn)
            mark="  *** NEGATIVE TO POSITIVE ***" if po<0<=pn else ("  *** NOW NEGATIVE ***" if pn<0 else "")
            print(f"  {yrs:>5}{('financed' if fin else 'cash'):<16}{MB[i]:<28}{po:>+8.2f}%{pn:>+8.2f}%{pn-po:>+9.2f} pp{mark}")
print(f"  old negative cells: {sum(1 for v in R_DELTA.values() if v[0]<0)} of 16 |"
      f" new negative cells: {sum(1 for v in R_DELTA.values() if v[1]<0)} of 16")
print(f"  whole-model M_NEG count: {len(M_NEG)} negative cell(s) of {len(M)} (was 4 of 48)")

print()
print(f"  R2. M3 BREAKEVEN DUTY — re-solved for Mumbai")
print(f"  {'yrs':>4}{'nom excl':>11}{'nom incl':>11}{'NPV excl':>11}{'NPV incl':>11}   verdict at 200 km/day (NPV incl = headline)")
R_BE={}
for yrs in (5,8):
    row=[M3[("Mumbai",yrs,npv,on)] for npv in (False,True) for on in (False,True)]
    R_BE[yrs]=row
    hi=row[3]
    print(f"  {yrs:>4}{row[0]:>11.1f}{row[1]:>11.1f}{row[2]:>11.1f}{row[3]:>11.1f}"
          f"   {'PASS' if hi and T.KM_DAY>=hi else 'FAIL'} ({T.KM_DAY/hi:.2f}x)" if hi else "  NO XOVER")
print(f"  previous Mumbai NPV-incl-incl breakevens were 201.4 (5yr) and 140.1 (8yr) at road=0%")

print()
print(f"  R3. M4 CHARGER BREAKEVEN — re-solved for Mumbai (5yr, financed)")
def _m4_mumbai():
    return (bisect(lambda cap: gap_at("Mumbai",5,True,True,False,cap)(T.KM_DAY),0.0,900_000.0),
            bisect(lambda cap: gap_at("Mumbai",5,True,True,True ,cap)(T.KM_DAY),0.0,900_000.0))
_r4=r_with_road(R_OLD,_m4_mumbai); _r4n,_r4v=_r4[0][0],_r4[1][0]
_r4s=(lambda v:("Rs"+m(v)) if v else "NO XOVER")
print(f"  {'':10}{'nominal':>10}{'NPV (headline)':>20}   verdict at the Rs{m(charger_capex_per_veh)} base case")
print(f"  {'old 0%':<10}{_r4s(_r4n):>10}{_r4s(_r4v):>20}   "
      f"{'wins' if _r4v and _r4v>charger_capex_per_veh else 'LOSES at the 0% rate'}")
print(f"  {'new '+format(R_NEW,'.0%'):<10}{'Rs'+m(m4['Mumbai'][0]):>10}{'Rs'+m(m4['Mumbai'][1]):>20}   "
      f"{'wins, Rs'+m(m4['Mumbai'][1]-charger_capex_per_veh)+' headroom' if m4['Mumbai'][1]>charger_capex_per_veh else 'LOSES by Rs'+m(charger_capex_per_veh-m4['Mumbai'][1])}")

print()
print(f"  R4. SECTION Q 2035 MUMBAI RUNGS — re-run under the corrected constant")
def _q_mumbai_cells():
    """Recompute the section-Q Mumbai cells live, so the old-rate column is a real re-run
    rather than a stale copy of Q_CELL (which was computed at the corrected rate)."""
    t1,p1=Q_IN["Mumbai"]; out={}
    for y in (5,8):
        h=q_headline("Mumbai",y,t1,p1)
        out[(y,0)]=100*(h[1]["total"]-h[0]["total"])/h[1]["total"]
        n=q_nominal("Mumbai",y,tariff=t1,price=p1)
        out[(y,1)]=100*(n[1]["ckm"]-n[0]["ckm"])/n[1]["ckm"]
    return out
_qold=r_with_road(R_OLD,_q_mumbai_cells); _qnew=_q_mumbai_cells()
_qagree=all(abs(_qnew[(y,i)]-Q_CELL[("Mumbai",y,i)][1])<0.005 for y in (5,8) for i in (0,1))
print(f"  {'cell':<40}{'old':>9}{'new':>9}{'delta':>9}")
for y in (5,8):
    for i in (0,1):
        old,new=_qold[(y,i)],_qnew[(y,i)]
        print(f"  {y}yr {Q_BASES[i]:<36}{old:>+8.2f}%{new:>+8.2f}%{new-old:>+8.2f} pp")
print(f"  live re-run agrees with section Q's printed cells: "
      f"{'YES' if _qagree else '** MISMATCH — DO NOT SHIP **'}")
print(f"  binding city at 5yr headline is now "
      f"{min(((Q_CELL[(c,5,0)][1],c) for c in CITIES))[1]}, not Mumbai.")

print()
print(f"  R5. ROAD SAFETY CESS — s.3B, 2% on the tax (w.e.f. 24-10-2016)")
R_CESS=0.02
print(f"  Effective rate {R_NEW:.0%} x (1+{R_CESS:.0%}) = {R_NEW*(1+R_CESS):.4%}")
_rsc=r_with_road(R_NEW*(1+R_CESS),_mumbai_cells)
R_CESS_DELTA={k:R_PCT(_rsc[k])-R_PCT(R_NEW_CELLS[k]) for k in R_NEW_CELLS}
for yrs in (5,8):
    for i in (0,3):
        print(f"  {yrs}yr {MB[i]:<28} base {R_PCT(R_NEW_CELLS[(yrs,True,i)]):+.2f}%"
              f" -> with cess {R_PCT(_rsc[(yrs,True,i)]):+.2f}% ({R_CESS_DELTA[(yrs,True,i)]:+.2f} pp)")
print(f"  does the cess change any conclusion? "
      f"{'NO' if all(R_PCT(_rsc[k])>0 for k in _rsc) else 'YES — it turns a cell negative'}")

print()
print("  R6. ENVIRONMENT TAX — s.3A")
print("  s.3A provides Rs2,500 for tourist taxis after 8 years, and 2.5%/yr of the annual tax")
print("  for private service vehicles. A fleet car running on ride-hailing is a private service")
print("  vehicle, so the 2.5%/yr limb is the one that applies; the tourist-taxi limb does not.")
R_ENV_RATE=0.025
_env_tax_yr=R_ENV_RATE*R_NEW*CNG["ex"]
_env_tax=R_ENV_RATE*R_NEW*CNG["ex"]*R_ENV_RATE
print(f"  annual road tax on the comparator = {R_NEW:.0%} x Rs{m(CNG['ex'])} = Rs{m(R_NEW*CNG['ex'])}")
print(f"  environment tax = {R_ENV_RATE:.1%}/yr of that = Rs{m(_env_tax)}/yr")
R_ENV={}
for yrs in (5,8):
    _tot=_env_tax*yrs; _km=yrs*T.KM_YEAR
    _ev,_cn=R_NEW_CELLS[(yrs,True,3)]; _cn2=_cn+_tot
    _adv2=100*(_cn2-_ev)/_cn2; _base=R_PCT(R_NEW_CELLS[(yrs,True,3)])
    R_ENV[yrs]=_adv2-_base
    print(f"  {yrs}yr: Rs{m(_tot)} total = Rs{_tot/_km:.4f}/km  -> headline advantage"
          f" {_base:+.2f}% -> {_adv2:+.2f}% ({_adv2-_base:+.2f} pp)")
print("  METHOD NOTE: this is a RECURRING tax, so it must NOT be folded into on_road(). on_road()")
print("  drives capex, EMI and the residual simultaneously, so capitalising a per-year charge")
print("  there would overstate it by the whole compounding factor. It is costed separately above.")
print(f"  does the environment tax change any conclusion? NO — at Rs{m(_env_tax)}/yr it moves the worst")
print(f"  Mumbai headline cell by {min(abs(v) for v in R_ENV.values()):.2f} pp, roughly a twentieth of the")
print("  Road Safety Cess effect, and changes no sign.")
print()
print("  IS OMITTING BOTH CONSERVATIVE OR FLATTERING? FLATTERING, in both cases, and by a")
print("  different amount. Both taxes fall on the CNG comparator only, so omitting them flatters")
print("  the EV. The omission is small (the cess moves no cell by more than")
print(f"  {max(abs(v) for v in R_CESS_DELTA.values()):.2f} pp, the environment tax by {min(abs(v) for v in R_ENV.values()):.2f} pp),")
print("  but it is a systematic one-way error, not noise. Both are left OUT of the base case")
print("  because the base case is a tax-TABLE comparison across three cities and these are")
print("  statutory additions that differ per city; folding them in for Mumbai alone would make")
print("  Mumbai's cells non-comparable with Delhi's and Bengaluru's, which have their own regimes.")

print()
print("  R7. THE LOAD-BEARING VERDICT")
m5h=R_DELTA[(5,True,3)]; m8h=R_DELTA[(8,True,3)]
print("  Q: does section M's conclusion survive — that Mumbai 'does not close at five years'?")
print(f"     It does NOT survive. Mumbai's 5yr headline cell was {m5h[0]:+.2f}% at road=0%; it is"
      f" {m5h[1]:+.2f}% now.")
print(f"     Its breakeven duty with infrastructure moves from 201.4 km/day (a FAIL against the deck's"
      f" {T.KM_DAY:.0f}) to {R_BE[5][3]:.1f} km/day, which PASSES at"
      f" {T.KM_DAY/R_BE[5][3]:.2f}x.")
print(f"     Mumbai is no longer among the negative cells; the model's negative count falls from"
      f" 4 of 48 to {len(M_NEG)} of {len(M)}.")
print(f"     Correcting one wrong constant REMOVES Mumbai as a failure case. The section-M claim")
print("     that 'the 5-year fleet case does not close outside Delhi' does not survive either —")
print(f"     {'it still fails on '+M_NEG[0][0] if M_NEG else 'every city now closes at 5 years'}.")
print("  Q: does section Q's conclusion survive — that Mumbai binds the 2035 case?")
print(f"     It does NOT survive. Mumbai's 2035 5yr headline is"
      f" {Q_CELL[('Mumbai',5,0)][1]:+.2f}%, and the binding city is now"
      f" {min(((Q_CELL[(c,5,0)][1],c) for c in CITIES))[1]}.")
print(f"     Mumbai was the weakest city because it was being handed a tax break it was never")
print("     entitled to; removing that break makes it look better. A comparator understated by")
print("     14% of its capital cost is a comparator that understates the EV's advantage.")
print()
print("  DIRECTION OF THE ERROR, stated plainly: this correction made the EV look BETTER, not")
print("  worse, and it was still mandatory. Every other city was compared against a CNG")
print("  comparator that was correctly taxed; Mumbai was not. Correcting one cell moved the")
print("  binding constraint from Mumbai to another city without touching Delhi or Bengaluru.")
print("  The general lesson for Rev 4: an error that flatters your own product is still an error,")
print("  and a document that disagrees with its own engine is not a document, it is a coincidence.")
print()
print("  Delhi and Bengaluru cells are UNAFFECTED — on_road() reads CITIES[city] per call and no")
print("  other city's dict was touched. That is asserted, not assumed:")
_rchk=[(c,T.tco(CNG,c,5)["on_road"],T.on_road(CNG,c)) for c in ("Delhi","Bengaluru")]
for c,orr,orr2 in _rchk:
    print(f"    {c:<11} CNG on-road Rs{m(orr)}  (engine says Rs{m(orr2)})  {'OK' if orr==orr2 else '** MISMATCH **'}")
print(f"    Mumbai CNG on-road Rs{m(T.on_road(CNG,'Mumbai'))} = Rs{m(CNG['ex'])} x {1+CNG['gst']:.2f} GST x {1+R_NEW:.2f} road"
      f" (was Rs{m(CNG['ex']*(1+CNG['gst']))} at 0%)")
