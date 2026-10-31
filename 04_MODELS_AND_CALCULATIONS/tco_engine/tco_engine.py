"""MACH1 / FleetLine E1 — Total Cost of Ownership engine. v2
CAPEX is counted ONCE: either cash on-road, or the full EMI stream. Never both.
INR. Duty 200 km/day x 26 days x 312 days/yr."""
KM_DAY, DAYS_MONTH = 200, 26
DAYS_YEAR  = DAYS_MONTH*12
KM_MONTH   = KM_DAY*DAYS_MONTH
KM_YEAR    = KM_DAY*DAYS_YEAR
LOAN_MONTHS, LOAN_RATE, DOWN_PCT = 60, 0.10, 0.0
FARE_PER_KM, REVENUE_MONTH = 11.0, 11.0*KM_MONTH
OPP_H = 112.0

EV  = dict(name="FleetLine E1 (BEV)", ex=1_212_000, gst=0.05, kwh100=12.84, pack=45.0,
           ceff=0.90, maint=1_200, tyre=0.30, ins=3_500, resid=0.26)
CNG = dict(name="Dzire Tour S (CNG)", ex=656_000, gst=0.18, kmkg=25.0, price=90.0,
           maint=3_500, ins=3_290, resid=0.40)
# road is now per-VEHICLE: Delhi Electric Vehicles Policy 2026 (notified 30-Jun-2026,
# effective 1-Jul-2026, to 31-Mar-2030) grants 100% road-tax + registration-fee
# exemption for the LIFE of the vehicle to all EVs registered in the period.
# Car eligibility: ex-showroom <= Rs30 lakh (ours is Rs12.12L -> qualifies).
# CNG comparator pays standard Delhi rate.
CITIES = {"Delhi":     dict(tariff=4.50, road=0.10, road_ev=0.00, cng=76.0),
          "Mumbai":    dict(tariff=9.50, road=0.14, road_ev=0.00, cng=88.0),
          "Bengaluru": dict(tariff=8.50, road=0.08, road_ev=0.08, cng=90.0)}

def on_road(v,c):
    rt = CITIES[c]["road_ev"] if "kwh100" in v else CITIES[c]["road"]
    return v["ex"]*(1+v["gst"])*(1+rt)
def emi(P,rate=LOAN_RATE,n=LOAN_MONTHS):
    if P<=0: return 0.0
    r=rate/12.0; f=(1+r)**n
    return P*r*f/(f-1)
def en_pm(v,c,tariff=None,kmkg=None,price=None):
    t = tariff if tariff is not None else CITIES[c]["tariff"]
    if "kwh100" in v: return (v["kwh100"]/100)*t/v["ceff"]
    return (price if price is not None else CITIES[c]["cng"])/(kmkg or v["kmkg"])
def mt_pk(v): return v["maint"]*12/KM_YEAR*(1+v.get("tyre",0))

def tco(v,c,years=5,financed=True,tariff=None,kmkg=None,price=None,
        downtime_h=0.0,resid=None,ex=None,kwh100=None,cng_resid=None):
    vv=dict(v)
    if ex is not None: vv["ex"]=ex
    if kwh100 is not None: vv["kwh100"]=kwh100
    if cng_resid is not None: vv["resid"]=cng_resid
    orr=on_road(vv,c)
    capex = emi(orr*(1-DOWN_PCT))*LOAN_MONTHS if financed else orr
    km=years*KM_YEAR
    d=dict(capex=capex, energy=en_pm(vv,c,tariff,kmkg,price)*km,
           maint=mt_pk(vv)*km, ins=vv["ins"]*12*years,
           down=downtime_h*12*years*OPP_H,
           res=orr*((resid if resid is not None else vv["resid"])))
    d["total"]=d["capex"]+d["energy"]+d["maint"]+d["ins"]+d["down"]-d["res"]
    d["ckm"]=d["total"]/km; d["km"]=km; d["on_road"]=orr
    d["emi"]=emi(orr*(1-DOWN_PCT)) if financed else 0.0
    return d
def m(x,d=0): return f"{x:,.{d}f}"

if __name__=="__main__":
    print(f"DUTY {KM_MONTH:,} km/mo | {KM_YEAR:,} km/yr | 5yr {5*KM_YEAR:,} km | 8yr {8*KM_YEAR:,} km")
    print(f"Rev Rs{m(REVENUE_MONTH)}/mo @ Rs11/km | loan {LOAN_RATE:.0%}/{LOAN_MONTHS}mo\n")
    for c in CITIES:
        print(f"===== {c}  elec Rs{CITIES[c]['tariff']}/kWh | road tax {CITIES[c]['road']:.0%} | CNG Rs{CITIES[c]['cng']}/kg")
        for fin in (True,False):
            e,g=tco(EV,c,5,fin),tco(CNG,c,5,fin)
            lbl="FINANCED 60mo" if fin else "CASH outright"
            print(f"  {lbl:<16} EV {e['ckm']:>6.2f}/km  ({m(e['total'])})   "
                  f"CNG {g['ckm']:>6.2f}/km ({m(g['total'])})   -> EV {100*(g['ckm']-e['ckm'])/g['ckm']:+.1f}%")
        print("  horizon sweep (financed):")
        for y in (5,6,7,8):
            e,g=tco(EV,c,y),tco(CNG,c,y)
            print(f"    {y}yr ({y*KM_YEAR:>7,} km)  EV {e['ckm']:>6.2f}  CNG {g['ckm']:>6.2f}  "
                  f"-> EV {100*(g['ckm']-e['ckm'])/g['ckm']:+6.1f}%   (EV saves {m(g['total']-e['total']):>10})")
        print()
