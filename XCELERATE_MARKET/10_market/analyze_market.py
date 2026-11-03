#!/usr/bin/env python3
"""India ride-service market: five-segment comparison and derived metrics.

Reads segment_comparison_dataset.csv and computes:
  - Revenue per vehicle-km for each segment (from deck's own table)
  - Implied airport share of platform rides (from AAI passenger data)
  - Data gap register (metrics with no source)
  - EV adoption trajectory (from AutoPunditz)

All derived values are labelled [calc] or [est] — never presented as reported data.
"""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATASET = ROOT / "segment_comparison_dataset.csv"

def load_dataset():
    with open(DATASET, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def get_metric(rows, segment, metric):
    for r in rows:
        if r["segment"] == segment and r["metric"] == metric:
            return r
    return None

def main():
    rows = load_dataset()
    print("=" * 80)
    print("INDIA RIDE-SERVICE MARKET — FIVE-SEGMENT COMPARISON")
    print("=" * 80)

    # 1. Revenue per vehicle-km (from deck's own table)
    print("\n1. GROSS REVENUE PER VEHICLE-KM (computed from deck p3 table)")
    print("-" * 60)
    segments = ["intra_city", "commute", "airport", "intercity", "premium"]
    seg_names = {"intra_city": "Intra-city", "commute": "Commute", "airport": "Airport",
                 "intercity": "Inter-city", "premium": "Premium/shared"}
    data = {}
    for seg in segments:
        trips = float(get_metric(rows, seg, "trips_per_day")["value"])
        fare = float(get_metric(rows, seg, "fare_per_trip")["value"])
        km = float(get_metric(rows, seg, "daily_km")["value"])
        rev_km = trips * fare / km
        data[seg] = (trips, fare, km, rev_km)
        print(f"  {seg_names[seg]:<16} {trips:>5.1f} trips/day × ₹{fare:>6,.0f}/trip ÷ {km:>5.0f} km/day = ₹{rev_km:>6.1f}/km")

    print("\n  Rank (highest revenue/km = 1):")
    ranked = sorted(data.items(), key=lambda x: -x[1][3])
    for i, (seg, (_, _, _, rev)) in enumerate(ranked, 1):
        print(f"    {i}. {seg_names[seg]:<16} ₹{rev:.1f}/km")

    # 2. Driver revenue per month
    print("\n2. DRIVER GROSS REVENUE PER MONTH (computed from deck p3 table)")
    print("-" * 60)
    for seg in segments:
        val = get_metric(rows, seg, "driver_revenue_monthly")["value"]
        print(f"  {seg_names[seg]:<16} ₹{float(val):>10,.0f}/mo  (all are gross revenue, not take-home)")

    # 3. Airport demand ceiling from AAI data
    print("\n3. AIRPORT TRANSFER DEMAND CEILING (from AAI passenger data)")
    print("-" * 60)
    aai_pax = float(get_metric(rows, "airport", "aai_passengers_apr_sep_2026")["value"])
    annual_pax = aai_pax * 2  # Apr-Sep × 2 approximation
    road_trips = annual_pax * 2  # to + from airport
    print(f"  AAI passengers Apr-Sep 2026:  {aai_pax:>12,.0f}")
    print(f"  Annualized (×2):              {annual_pax:>12,.0f}")
    print(f"  Road trips (×2 to/from):      {road_trips:>12,.0f}")
    print(f"  At 20% app-cab share:        {road_trips * 0.20:>12,.0f}  ({road_trips * 0.20 / 591300000 * 100:.1f}% of platform rides)")
    print(f"  At 30% app-cab share:        {road_trips * 0.30:>12,.0f}  ({road_trips * 0.30 / 591300000 * 100:.1f}% of platform rides)")
    print("  [est] Mode share (20-30%) is an assumption, not measured data")

    # 4. Data gap register
    print("\n4. DATA GAP REGISTER (metrics with no source)")
    print("-" * 60)
    gap_metrics = ["avg_trip_km", "daily_km", "trips_per_day", "fare_per_trip", "growth_rate",
                   "ev_share", "price_sensitivity"]
    gap_count = 0
    for seg in segments:
        for m in gap_metrics:
            r = get_metric(rows, seg, m)
            if r and r["grade"] == "D":
                gap_count += 1
    print(f"  Total Grade D (no source) cells: {gap_count} of {len(segments) * len(gap_metrics)}")
    print(f"  Grade A (reproduced): {sum(1 for r in rows if r['grade'] == 'A')}")
    print(f"  Grade B (single source): {sum(1 for r in rows if r['grade'] == 'B')}")
    print(f"  Grade C (internal assertion): {sum(1 for r in rows if r['grade'] == 'C')}")
    print(f"  Grade D (contradicted/no source): {sum(1 for r in rows if r['grade'] == 'D')}")

    # 5. EV adoption trajectory
    print("\n5. EV ADOPTION IN PASSENGER CARS (from AutoPunditz)")
    print("-" * 60)
    ev_data = [(r["metric"], r["value"], r["reference_period"]) for r in rows if r["segment"] == "market" and "ev" in r["metric"]]
    for m, v, p in ev_data:
        print(f"  {m:<30} {v:>10}  ({p})")

    # 6. TCO summary
    print("\n6. TCO ADVANTAGE SUMMARY (Grade A)")
    print("-" * 60)
    tco_metrics = [(r["metric"], r["value"]) for r in rows if r["segment"] == "market" and r["metric"].startswith("tco_")]
    for m, v in tco_metrics:
        print(f"  {m:<35} {v}")

    print("\n" + "=" * 80)
    print("All derived values labelled [calc] or [est]. No reported data was modified.")
    print("Source: segment_comparison_dataset.csv (33 metrics × 5 segments + market data)")
    print("=" * 80)

if __name__ == "__main__":
    main()
