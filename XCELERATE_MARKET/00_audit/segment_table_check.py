#!/usr/bin/env python3
"""Internal-consistency audit of the FleetLine E1 five-segment market table.

Source of the table: MACH1_WORKING_FILES/Detailed Presentation Report.pdf, page 3
("MARKET / WHAT DOES THE MARKET SAY?"), and the right-hand column of the same page.

The table has no external provenance (see RESEARCH_AUDIT.md, row A1). This script does
not validate it against the world. It only asks: *is the table consistent with itself?*
Anything that fails here cannot be rescued by finding a source later.

Run:  python3 segment_table_check.py
Out:  segment_table_checks.csv, stdout summary
"""

from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parent

# --- The table exactly as printed on deck page 3 -----------------------------
# Left table: USE CASE | AVG KM | KM/DAY | TRIPS/DAY | Rs/TRIP | GROWTH | EV SHARE | PRICE SENS
LEFT = [
    # name,                    avg_km, km_day, trips_day, fare_trip, growth, ev_share, price_sens
    ("Intra-city street hail", 12.7,  95,  7.5,  350,  0.18, 0.10, 0.85),
    ("Daily commute/subscr.",  22.0, 176,  8.0,  550,  0.24, 0.12, 0.90),
    ("Airport transfer",       35.0, 210,  6.0,  600,  0.26, 0.18, 0.35),
    ("Inter-city/outstation", 280.0, 340,  1.5, 4200,  0.20, 0.05, 0.40),
    ("Premium/shared-prem.",   18.0, 144,  8.0,  520,  0.28, 0.15, 0.30),
]

# Right table: USE CASE | KM/DAY | GROWTH | EV SHARE | DRIVER Rs/MO | MACH1 FIT
RIGHT = {
    "Intra-city street hail": (95,  0.18, 0.10, 68_250,  "weak"),
    "Daily commute/subscr.":  (176, 0.24, 0.12, 114_400, "STRONG"),
    "Airport transfer":       (210, 0.26, 0.18, 93_600,  "STRONG"),
    "Inter-city/outstation":  (340, 0.20, 0.05, 163_800, "weak"),
    "Premium/shared-prem.":   (144, 0.28, 0.15, 108_160, "moderate"),
}

DAYS = 26           # implied by the table's arithmetic (see check C3)
TRIPS_PER_DAY = 8   # TOI-cited cab-economics reference used elsewhere in the project
NATIONAL_RIDES_DAY = 840_000 + 460_000 + 320_000  # market_analysis.py proxy

rows: list[dict] = []


def add(check: str, segment: str, metric: str, printed: str, recomputed: str,
        verdict: str, note: str = "") -> None:
    rows.append(dict(check=check, segment=segment, metric=metric, printed=printed,
                     recomputed=recomputed, verdict=verdict, note=note))


# --- C1: does avg_km x trips_day equal the printed km/day? -------------------
for name, avg_km, km_day, trips, fare, *_ in LEFT:
    implied = avg_km * trips
    ok = abs(implied - km_day) < 0.05 * km_day
    add("C1", name, "km/day vs avg_km x trips/day", f"{km_day:g}", f"{implied:g}",
        "PASS" if ok else "FAIL", "" if ok else
        f"gap {implied - km_day:+.0f} km/day ({(implied/km_day-1)*100:+.0f}%); "
        "1.5 trips x 280 km = 420 km driven, table prints 340")

# --- C2: does trips_day x fare x 26 reconstruct the printed driver Rs/month? --
for name, avg_km, km_day, trips, fare, *_ in LEFT:
    printed = RIGHT[name][3]
    implied = trips * fare * DAYS
    ok = abs(implied - printed) < 1
    add("C2", name, "driver Rs/month vs trips x fare x 26d", f"{printed:,}", f"{implied:,.0f}",
        "PASS" if ok else "FAIL")

# --- C3: revenue per vehicle-km, the number the table never shows ------------
for name, avg_km, km_day, trips, fare, *_ in LEFT:
    rev_mo = RIGHT[name][3]
    per_km = rev_mo / (km_day * DAYS)
    add("C3", name, "implied Rs per vehicle-km", "not shown", f"{per_km:.1f}", "INFO",
        f"gross Rs{rev_mo:,}/mo / ({km_day} km/day x {DAYS} d)")

# --- C4: fleet-size anchors used in the project ------------------------------
implied_national_fleet = NATIONAL_RIDES_DAY / TRIPS_PER_DAY
add("C4", "national", "active cars implied by ride-flow proxy",
    "40,000-50,000 (addressable metros)", f"{implied_national_fleet:,.0f} (national)",
    "FAIL",
    f"{NATIONAL_RIDES_DAY:,} rides/day / {TRIPS_PER_DAY} trips per car-day. The project's "
    "addressable-metro fleet is 20-25% of the national total implied by its own ride count; "
    "the two anchors are not from the same measurement.")

add("C5", "national", "EV share of ride-hailing fleet",
    "10% (intra-city) / 18% (airport)",
    f"{8_000/50_000:.0%}-{10_000/40_000:.0%}",
    "CONFLICT",
    "Audience doc: 8,000-10,000 EVs of 40,000-50,000 addressable-metro vehicles.")

# --- C6: do the five segments partition the market? --------------------------
add("C6", "segment set", "orthogonality of the five segments", "partition summing to 100%",
    "not a partition", "FAIL",
    "'Premium/shared-premium' is a service class, not a trip purpose: an airport run can be "
    "premium, an intra-city run can be shared. Summing these rows double-counts trips, so "
    "61% + 19% + 5% cannot be a valid decomposition of any total.")

# --- C7: the volume/margin claim, tested on the table's own numbers ----------
per_km = {n: RIGHT[n][3] / (LEFT[[r[0] for r in LEFT].index(n)][2] * DAYS) for n, *_ in
          [(r[0],) for r in LEFT]}
add("C7", "Airport transfer", "Rs per vehicle-km rank",
    "declared the MARGIN segment", f"rank {sorted(per_km.values(), reverse=True).index(per_km['Airport transfer'])+1} of 5",
    "FAIL", f"Rs{per_km['Airport transfer']:.1f}/km is the lowest of the five segments "
    f"(range Rs{min(per_km.values()):.1f}-{max(per_km.values()):.1f}). The airport 'margin' "
    "claim cannot rest on fare; it must rest on cost, which the table never computes.")

# --- C8: price-sensitivity column, internal ordering -------------------------
add("C8", "intra-city vs commute", "price sensitivity ordering",
    "0.85 called 'highest'; commute printed 0.90", "0.85 < 0.90", "CONFLICT",
    "Already logged as MCH-I-003; also conflicts with slide 11's 0.30-0.35 for the margin "
    "segment, which uses a different, undefined index.")

with (OUT / "segment_table_checks.csv").open("w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

for r in rows:
    print(f"[{r['verdict']:<8}] {r['check']} {r['segment']:<24} {r['metric']:<42} "
          f"printed={r['printed']:<28} recomputed={r['recomputed']}")

print("\n--- revenue per vehicle-km (C3) ---")
for k, v in sorted(per_km.items(), key=lambda kv: -kv[1]):
    print(f"  {k:<24} Rs{v:5.1f}/km")
print(f"\nwrote {OUT/'segment_table_checks.csv'} ({len(rows)} checks)")
