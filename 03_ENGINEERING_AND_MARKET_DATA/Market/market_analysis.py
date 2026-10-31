#!/usr/bin/env python3
"""Reproduce the transparent ride-market sensitivity and local data inventory.

This script intentionally does not run clustering or regression. The current
evidence has no trip-level/city-segment sample on which those models would be
meaningful. Scenario assumptions are labelled below and in
../MACH1_MARKET_ASSESSMENT.md.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"

# Average daily platform rides, reported by Business Standard (18 Apr 2025),
# citing Motilal Oswal. The story's source definitions and Rapido vehicle-class
# scope are not fully stated. Treat this as a platform ride-flow proxy.
PLATFORM_DAILY_RIDES = {
    "Uber": 840_000,
    "Ola": 460_000,
    "Rapido": 320_000,
}
DAYS_PER_YEAR = 365

# Sensitivity assumptions, not observed segment estimates.
SCENARIOS = [
    ("Low", 0.05, 300),
    ("Central arithmetic case", 0.10, 450),
    ("High", 0.15, 600),
]


def print_market_scenarios() -> None:
    daily = sum(PLATFORM_DAILY_RIDES.values())
    annual = daily * DAYS_PER_YEAR
    print("RIDE-FLOW PROXY (not a national taxi-market census)")
    for platform, rides in PLATFORM_DAILY_RIDES.items():
        print(f"  {platform:<8} {rides:>10,} daily rides")
    print(f"  {'Combined':<8} {daily:>10,} daily rides")
    print(f"  Annualized at 365 days: {annual:,.0f} rides")
    print("\nSCENARIO GMV — target share and fare are assumptions")
    print(f"  {'Case':<25}{'Target share':>14}{'Fare':>12}{'Annual rides':>17}{'GMV (INR cr)':>17}")
    for label, share, fare in SCENARIOS:
        target_rides = annual * share
        gmv_crore = target_rides * fare / 10_000_000
        print(
            f"  {label:<25}{share:>13.0%}{fare:>11,.0f}"
            f"{target_rides:>17,.0f}{gmv_crore:>17,.0f}"
        )
    print("\nFormula: annual rides × target-segment share × realized fare")
    print("Do not call this TAM/SAM/SOM or a forecast until share and fare are measured.")


def inventory_csv(path: Path) -> None:
    if not path.exists():
        print(f"  {path.name}: missing")
        return
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        rows = list(reader)
        fields = reader.fieldnames or []
    dates = [row.get("month", "") for row in rows if row.get("month")]
    states = {row.get("state", "") for row in rows if row.get("state")}
    years = sorted({int(year) for period in dates for year in re.findall(r"20\d{2}", period)})
    period_range = f"{years[0]} to {years[-1]}" if years else "n/a"
    print(
        f"  {path.name}: {len(rows):,} rows; {len(fields)} columns; "
        f"{len(states)} state labels; years represented {period_range}"
    )


def print_local_data_inventory() -> None:
    print("\nLOCAL CSV INVENTORY (file coverage only; not market conclusions)")
    for filename in (
        "vahan_panel.csv",
        "autopunditz_ev.csv",
        "autopunditz_ev_vahan_oem.csv",
        "autopunditz_ev_luxury_monthly.csv",
        "autopunditz_ev_period_aggregates.csv",
        "autopunditz_ev_by_state.csv",
    ):
        inventory_csv(DATA / filename)
    print("  Verify geography, source measure (wholesale vs registration),")
    print("  missing periods, category coverage, and extraction date before analysis.")


def main() -> None:
    print_market_scenarios()
    print()
    print_local_data_inventory()


if __name__ == "__main__":
    main()
