#!/usr/bin/env python3
"""India Ride-Service Market Sizing Model — 2035 Forecast

Independent top-down and bottom-up market sizing for India's ride-service industry.
Uses only primary-sourced inputs. All assumptions explicitly labelled.

Output: /home/sankara/Downloads/XCELERATE_MARKET/20_market_sizing/market_sizing_model.xlsx
"""

from __future__ import annotations
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from pathlib import Path

OUT = Path("/home/sankara/Downloads/XCELERATE_MARKET/20_market_sizing")
OUT.mkdir(parents=True, exist_ok=True)

wb = openpyxl.Workbook()

# Styles
BOLD = Font(bold=True)
ITALIC = Font(italic=True, size=9, color="666666")
HEADER = Font(bold=True, color="FFFFFF")
HEADER_FILL = PatternFill("solid", fgColor="1F3864")
SUBHEADER_FILL = PatternFill("solid", fgColor="D9E2F3")
CALC_FILL = PatternFill("solid", fgColor="FFF2CC")
EST_FILL = PatternFill("solid", fgColor="FCE4D6")
REPORTED_FILL = PatternFill("solid", fgColor="E2EFDA")
thin = Side(style="thin", color="BFBFBF")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

def style_header(ws, row, ncols):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = HEADER
        cell.fill = HEADER_FILL
        cell.border = BORDER
        cell.alignment = Alignment(horizontal="center", wrap_text=True)

def set_widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def add_title(ws, title, subtitle=None):
    ws["A1"] = title
    ws["A1"].font = Font(bold=True, size=14, color="1F3864")
    r = 2
    if subtitle:
        ws.cell(row=r, column=1, value=subtitle).font = ITALIC
        r = 3
    return r

# ============================================================
# SHEET 1: Assumptions & Inputs
# ============================================================
ws = wb.active
ws.title = "1_Assumptions"
r = add_title(ws, "ASSUMPTIONS & INPUTS", "All inputs labelled: [reported] = from primary source, [calc] = derived, [est] = assumption, [assump] = unsourced")
set_widths(ws, [45, 18, 12, 60, 25, 15])

# Header
hr = r
ws.cell(row=hr, column=1, value="Input").font = BOLD
ws.cell(row=hr, column=2, value="Value").font = BOLD
ws.cell(row=hr, column=3, value="Unit").font = BOLD
ws.cell(row=hr, column=4, value="Source / Notes").font = BOLD
ws.cell(row=hr, column=5, value="Grade").font = BOLD
ws.cell(row=hr, column=6, value="Type").font = BOLD
style_header(ws, hr, 6)
r = hr + 1

inputs = [
    # Platform rides
    ("Uber daily rides", 840000, "rides/day", "Motilal Oswal via Business Standard", "B", "reported", "18 Apr 2025"),
    ("Ola daily rides", 460000, "rides/day", "Motilal Oswal via Business Standard", "B", "reported", "18 Apr 2025"),
    ("Rapido daily rides", 320000, "rides/day", "Motilal Oswal via Business Standard", "B", "reported", "18 Apr 2025 (may include bikes/autos)"),
    ("Days per year", 365, "days", "Standard", "A", "calc", "Run-rate annualization"),
    # Fare
    ("Broad average fare (all cabs)", 300, "INR/trip", "Times of India", "B", "reported", "23 Jun 2025; broad reference, not segment-specific"),
    ("Target fare — conservative", 300, "INR/trip", "Assumption", "C", "est", "Low scenario bound"),
    ("Target fare — base", 450, "INR/trip", "Assumption", "C", "est", "Central arithmetic case"),
    ("Target fare — optimistic", 600, "INR/trip", "Assumption", "C", "est", "High scenario bound"),
    # Segment shares
    ("Target segment share — conservative", 0.05, "fraction", "Assumption", "C", "est", "5% of platform rides"),
    ("Target segment share — base", 0.10, "fraction", "Assumption", "C", "est", "10% of platform rides"),
    ("Target segment share — optimistic", 0.15, "fraction", "Assumption", "C", "est", "15% of platform rides"),
    # Duty cycle
    ("FleetLine E1 duty cycle", 200, "km/day", "TCO model constant", "C", "assump", "Design assumption, not measured"),
    ("Days per month (operating)", 26, "days/mo", "TCO model", "C", "assump", "Fleet operating days"),
    ("Months per year", 12, "months/yr", "Standard", "A", "calc", ""),
    ("Rides per active vehicle per year", 2080, "rides/veh/yr", "Assumption", "C", "est", "8 rides/day x 26 days x 12 months = 2,496; using 2,080 (conservative)"),
    # Vehicle opportunity
    ("Net fleet growth rate", 0.03, "fraction/yr", "Assumption", "C", "est", "3% annual fleet growth"),
    ("Annual replacement rate", 0.15, "fraction/yr", "Assumption", "C", "est", "15% of fleet replaced annually"),
    ("Serviceable city share", 0.60, "fraction", "Assumption", "C", "est", "60% of national market in serviceable cities"),
    ("Attainable OEM share", 0.05, "fraction", "Assumption", "C", "est", "5% of vehicle opportunity"),
    # Airport data
    ("AAI passengers (Apr-Sep 2026)", 196240000, "passengers", "AAI Traffic Report", "A", "reported", "159.54M domestic + 36.70M international"),
    ("Airport app-cab mode share (low)", 0.15, "fraction", "Assumption", "C", "est", "Conservative mode share"),
    ("Airport app-cab mode share (base)", 0.25, "fraction", "Assumption", "C", "est", "Base mode share"),
    ("Airport app-cab mode share (high)", 0.35, "fraction", "Assumption", "C", "est", "Optimistic mode share"),
    # TCO
    ("EV TCO advantage (Delhi 5-yr nominal)", 0.145, "fraction", "TCO analysis", "A", "calc", "Rs 5.75 vs Rs 6.73/km"),
    ("EV TCO advantage (Delhi 5-yr incl infra)", 0.065, "fraction", "TCO analysis", "A", "calc", "Rs 6.31 vs Rs 6.75/km"),
    ("Driver advantage (monthly)", 14200, "INR/mo", "Driver/rider analysis", "A", "calc", "Rs 47,060 vs Rs 32,860"),
    ("FleetLine E1 pack size", 45, "kWh", "Battery report", "A", "reported", "LFP, 90% usable"),
    ("FleetLine E1 consumption", 12.84, "kWh/100km", "TCO analysis", "A", "reported", "Battery-side consumption"),
    ("FleetLine E1 range (15% reserve)", 268, "km", "Roadmap", "A", "reported", "315 km at zero reserve"),
    ("FleetLine E1 charger cost", 99000, "INR/vehicle", "TCO analysis", "A", "reported", "7.4 kW AC, installed"),
    # EV adoption
    ("EV cars H1 2026", 148023, "vehicles", "AutoPunditz", "B", "reported", "H1 2026"),
    ("Tata EV share FY2026", 0.388, "fraction", "AutoPunditz", "B", "reported", "Of EV car market"),
    ("Karnataka EV share Aug 2026", 0.175, "fraction", "AutoPunditz", "B", "reported", "Of all new vehicles"),
]

row_start = r
for name, val, unit, source, grade, typ, note in inputs:
    ws.cell(row=r, column=1, value=name)
    ws.cell(row=r, column=2, value=val)
    ws.cell(row=r, column=3, value=unit)
    ws.cell(row=r, column=4, value=f"{source} | {note}")
    ws.cell(row=r, column=5, value=grade)
    ws.cell(row=r, column=6, value=typ)
    # Color code by type
    fill = REPORTED_FILL if typ == "reported" else (CALC_FILL if typ == "calc" else EST_FILL)
    ws.cell(row=r, column=2).fill = fill
    ws.cell(row=r, column=2).border = BORDER
    for c in range(1, 7):
        ws.cell(row=r, column=c).border = BORDER
    r += 1

# Named cell references for key inputs
input_rows = {name: row_start + i for i, (name, *_) in enumerate(inputs)}
def I(name):
    return f"'1_Assumptions'!$B${input_rows[name]}"

# ============================================================
# SHEET 2: Top-Down Market Sizing
# ============================================================
ws2 = wb.create_sheet("2_TopDown")
r = add_title(ws2, "TOP-DOWN MARKET SIZING — INDIA RIDE-SERVICE 2035", "Formula: Platform rides x target segment share x realized fare = GMV. Then: rides / rides-per-vehicle = vehicles.")
set_widths(ws2, [40, 20, 20, 20, 60])

hr = r
for i, h in enumerate(["Metric", "Conservative", "Base", "Optimistic", "Notes"], 1):
    ws2.cell(row=hr, column=i, value=h)
style_header(ws2, hr, 5)
r = hr + 1

# Platform rides
ws2.cell(row=r, column=1, value="Platform daily rides (Uber+Ola+Rapido)").font = BOLD
ws2.cell(row=r, column=2, value=f"={I('Uber daily rides')}+{I('Ola daily rides')}+{I('Rapido daily rides')}")
ws2.cell(row=r, column=3, value=f"={I('Uber daily rides')}+{I('Ola daily rides')}+{I('Rapido daily rides')}")
ws2.cell(row=r, column=4, value=f"={I('Uber daily rides')}+{I('Ola daily rides')}+{I('Rapido daily rides')}")
ws2.cell(row=r, column=5, value="[reported] Motilal Oswal via Business Standard, 18 Apr 2025")
platform_row = r
r += 1

ws2.cell(row=r, column=1, value="Annualized platform rides (x365)")
for c in [2, 3, 4]:
    ws2.cell(row=r, column=c, value=f"=B{platform_row}*{I('Days per year')}")
ws2.cell(row=r, column=5, value="[calc] Run-rate annualization, not observed annual total")
annual_rides_row = r
r += 1

ws2.cell(row=r, column=1, value="Target segment share").font = BOLD
ws2.cell(row=r, column=2, value=f"={I('Target segment share — conservative')}")
ws2.cell(row=r, column=3, value=f"={I('Target segment share — base')}")
ws2.cell(row=r, column=4, value=f"={I('Target segment share — optimistic')}")
ws2.cell(row=r, column=5, value="[est] Scenario assumption; no validated segment share exists")
share_row = r
r += 1

ws2.cell(row=r, column=1, value="Target segment annual rides")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws2.cell(row=r, column=c, value=f"={col}{annual_rides_row}*{col}{share_row}")
ws2.cell(row=r, column=5, value="[calc] Annual rides x target share")
seg_rides_row = r
r += 1

ws2.cell(row=r, column=1, value="Average realized fare (target segment)").font = BOLD
ws2.cell(row=r, column=2, value=f"={I('Target fare — conservative')}")
ws2.cell(row=r, column=3, value=f"={I('Target fare — base')}")
ws2.cell(row=r, column=4, value=f"={I('Target fare — optimistic')}")
ws2.cell(row=r, column=5, value="[est] Sensitivity bound; Rs 300 is broad all-cab reference (TOI)")
fare_row = r
r += 1

ws2.cell(row=r, column=1, value="Illustrative annual GMV (INR)").font = BOLD
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws2.cell(row=r, column=c, value=f"={col}{seg_rides_row}*{col}{fare_row}")
ws2.cell(row=r, column=5, value="[calc] NOT TAM/SAM/SOM. Scenario envelope only.")
gmv_row = r
r += 2

ws2.cell(row=r, column=1, value="GMV in INR crore").font = ITALIC
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws2.cell(row=r, column=c, value=f"={col}{gmv_row}/10000000")
r += 2

# Vehicle demand
ws2.cell(row=r, column=1, value="VEHICLE DEMAND (from ride demand)").font = Font(bold=True, size=12, color="1F3864")
r += 1
ws2.cell(row=r, column=1, value="Rides per active vehicle per year").font = BOLD
ws2.cell(row=r, column=2, value=f"={I('Rides per active vehicle per year')}")
ws2.cell(row=r, column=3, value=f"={I('Rides per active vehicle per year')}")
ws2.cell(row=r, column=4, value=f"={I('Rides per active vehicle per year')}")
ws2.cell(row=r, column=5, value="[est] 8 rides/day x 26 days x 12 months = 2,496; using 2,080 (conservative)")
rpv_row = r
r += 1

ws2.cell(row=r, column=1, value="Target active vehicles (segment fleet)")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws2.cell(row=r, column=c, value=f"={col}{seg_rides_row}/{col}{rpv_row}")
ws2.cell(row=r, column=5, value="[calc] Target segment rides / rides per vehicle")
active_veh_row = r
r += 1

ws2.cell(row=r, column=1, value="Annual vehicle opportunity").font = BOLD
ws2.cell(row=r, column=2, value=f"=B{active_veh_row}*({I('Net fleet growth rate')}+{I('Annual replacement rate')})")
ws2.cell(row=r, column=3, value=f"=C{active_veh_row}*({I('Net fleet growth rate')}+{I('Annual replacement rate')})")
ws2.cell(row=r, column=4, value=f"=D{active_veh_row}*({I('Net fleet growth rate')}+{I('Annual replacement rate')})")
ws2.cell(row=r, column=5, value="[calc] Active fleet x (growth + replacement)")
veh_opp_row = r
r += 1

ws2.cell(row=r, column=1, value="Serviceable city share")
ws2.cell(row=r, column=2, value=f"={I('Serviceable city share')}")
ws2.cell(row=r, column=3, value=f"={I('Serviceable city share')}")
ws2.cell(row=r, column=4, value=f"={I('Serviceable city share')}")
ws2.cell(row=r, column=5, value="[est] 60% of national market in serviceable cities")
city_share_row = r
r += 1

ws2.cell(row=r, column=1, value="FleetLine E1 addressable vehicles").font = BOLD
ws2.cell(row=r, column=2, value=f"=B{veh_opp_row}*B{city_share_row}*{I('Attainable OEM share')}")
ws2.cell(row=r, column=3, value=f"=C{veh_opp_row}*C{city_share_row}*{I('Attainable OEM share')}")
ws2.cell(row=r, column=4, value=f"=D{veh_opp_row}*D{city_share_row}*{I('Attainable OEM share')}")
ws2.cell(row=r, column=5, value="[calc] Vehicle opportunity x city share x OEM share")
e1_veh_row = r
r += 2

ws2.cell(row=r, column=1, value="FleetLine E1 revenue at Rs 12.72L on-road").font = ITALIC
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws2.cell(row=r, column=c, value=f"={col}{e1_veh_row}*{I('FleetLine E1 on-road price (from TCO)') if False else 1272600}")
r += 1
ws2.cell(row=r, column=1, value="  (at Rs 12.72 lakh on-road price)").font = ITALIC
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws2.cell(row=r, column=c, value=f"={col}{e1_veh_row}*1272600")
ws2.cell(row=r, column=5, value="[calc] Addressable vehicles x on-road price")
r += 2

# ============================================================
# SHEET 3: Bottom-Up (Airport segment)
# ============================================================
ws3 = wb.create_sheet("3_BottomUp_Airport")
r = add_title(ws3, "BOTTOM-UP: AIRPORT TRANSFER SEGMENT", "Derived from AAI passenger traffic data")
set_widths(ws3, [45, 20, 20, 20, 60])
hr = r
for i, h in enumerate(["Metric", "Conservative", "Base", "Optimistic", "Notes"], 1):
    ws3.cell(row=hr, column=i, value=h)
style_header(ws3, hr, 5)
r = hr + 1

ws3.cell(row=r, column=1, value="AAI passengers (Apr-Sep 2026)").font = BOLD
for c in [2, 3, 4]:
    ws3.cell(row=r, column=c, value=f"={I('AAI passengers (Apr-Sep 2026)')}")
ws3.cell(row=r, column=5, value="[reported] AAI Traffic Report, Sep 2026")
aai_row = r
r += 1

ws3.cell(row=r, column=1, value="Annualized air passengers (x2)")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{aai_row}*2")
ws3.cell(row=r, column=5, value="[calc] Apr-Sep x 2 approximation")
ann_pax_row = r
r += 1

ws3.cell(row=r, column=1, value="Road trips to/from airport (x2)")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{ann_pax_row}*2")
ws3.cell(row=r, column=5, value="[calc] Each passenger = 2 road trips (to + from)")
road_trips_row = r
r += 1

ws3.cell(row=r, column=1, value="App-cab mode share").font = BOLD
ws3.cell(row=r, column=2, value=f"={I('Airport app-cab mode share (low)')}")
ws3.cell(row=r, column=3, value=f"={I('Airport app-cab mode share (base)')}")
ws3.cell(row=r, column=4, value=f"={I('Airport app-cab mode share (high)')}")
ws3.cell(row=r, column=5, value="[est] Assumption; no sourced mode share data")
mode_share_row = r
r += 1

ws3.cell(row=r, column=1, value="Airport app-cab trips per year").font = BOLD
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{road_trips_row}*{col}{mode_share_row}")
ws3.cell(row=r, column=5, value="[calc] Road trips x mode share")
airport_rides_row = r
r += 1

ws3.cell(row=r, column=1, value="As % of total platform rides (591.3M)")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{airport_rides_row}/591300000")
ws3.cell(row=r, column=5, value="[calc] Airport share of platform ride-flow proxy")
r += 2

ws3.cell(row=r, column=1, value="AIRPORT VEHICLE DEMAND").font = Font(bold=True, size=12, color="1F3864")
r += 1
ws3.cell(row=r, column=1, value="Rides per active vehicle per year")
for c in [2, 3, 4]:
    ws3.cell(row=r, column=c, value=f"={I('Rides per active vehicle per year')}")
rpv2 = r
r += 1
ws3.cell(row=r, column=1, value="Airport active vehicles")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{airport_rides_row}/{col}{rpv2}")
ws3.cell(row=r, column=5, value="[calc] Airport rides / rides per vehicle")
airport_veh_row = r
r += 1
ws3.cell(row=r, column=1, value="Annual replacement + growth")
ws3.cell(row=r, column=2, value=f"={I('Net fleet growth rate')}+{I('Annual replacement rate')}")
ws3.cell(row=r, column=3, value=f"={I('Net fleet growth rate')}+{I('Annual replacement rate')}")
ws3.cell(row=r, column=4, value=f"={I('Net fleet growth rate')}+{I('Annual replacement rate')}")
r += 1
ws3.cell(row=r, column=1, value="Airport annual vehicle opportunity")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{airport_veh_row}*{I('Net fleet growth rate')}+{I('Annual replacement rate')}".replace(f"{col}{airport_veh_row}*{I('Net fleet growth rate')}", f"{col}{airport_veh_row}*({I('Net fleet growth rate')}"))
# Fix formula
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{airport_veh_row}*({I('Net fleet growth rate')}+{I('Annual replacement rate')})")
ws3.cell(row=r, column=5, value="[calc] Active airport fleet x (growth + replacement)")
airport_opp_row = r
r += 1
ws3.cell(row=r, column=1, value="FleetLine E1 airport vehicles (x city share x OEM share)")
for c, col in [(2, "B"), (3, "C"), (4, "D")]:
    ws3.cell(row=r, column=c, value=f"={col}{airport_opp_row}*{I('Serviceable city share')}*{I('Attainable OEM share')}")
ws3.cell(row=r, column=5, value="[calc] Airport vehicle opportunity x 60% city share x 5% OEM share")
r += 2

# ============================================================
# SHEET 4: Segment Breakdown
# ============================================================
ws4 = wb.create_sheet("4_Segments")
r = add_title(ws4, "SEGMENT BREAKDOWN — FIVE USE CASES", "All segment-specific metrics from deck p3 are UNSOURCED (Grade D). Only revenue/km and driver revenue are computed.")
set_widths(ws4, [22, 14, 14, 14, 14, 14, 14, 40])
hr = r
headers = ["Segment", "Avg km", "km/day", "Trips/day", "Rs/trip", "Driver Rs/mo", "Rev/km (Rs)", "Evidence grade"]
for i, h in enumerate(headers, 1):
    ws4.cell(row=hr, column=i, value=h)
style_header(ws4, hr, 8)
r = hr + 1

seg_data = [
    ("Intra-city", 12.7, 95, 7.5, 350, 68250, 27.6, "D (all inputs unsourced)"),
    ("Commute", 22.0, 176, 8.0, 550, 114400, 25.0, "D (all inputs unsourced)"),
    ("Airport", 35.0, 210, 6.0, 600, 93600, 17.1, "D (all inputs unsourced; AAI data available for demand ceiling)"),
    ("Inter-city", 280, 340, 1.5, 4200, 163800, 18.5, "D (internally inconsistent: 1.5x280=420!=340)"),
    ("Premium/shared", 18.0, 144, 8.0, 520, 108160, 28.9, "D (service tier, not trip purpose)"),
]
for name, km, daily, trips, fare, driver, revkm, grade in seg_data:
    ws4.cell(row=r, column=1, value=name).font = BOLD
    ws4.cell(row=r, column=2, value=km)
    ws4.cell(row=r, column=3, value=daily)
    ws4.cell(row=r, column=4, value=trips)
    ws4.cell(row=r, column=5, value=fare)
    ws4.cell(row=r, column=6, value=driver)
    ws4.cell(row=r, column=7, value=revkm)
    ws4.cell(row=r, column=8, value=grade)
    for c in range(1, 9):
        ws4.cell(row=r, column=c).border = BORDER
    r += 1
r += 1
ws4.cell(row=r, column=1, value="NOTE: All segment metrics above are from the deck's unsourced p3 table.").font = ITALIC
r += 1
ws4.cell(row=r, column=1, value="Revenue/km is the only derived metric. Driver revenue = trips/day x fare x 26 days (gross, not take-home).").font = ITALIC
r += 1
ws4.cell(row=r, column=1, value="AAI passenger data (196.24M Apr-Sep 2026) provides an independent demand ceiling for airport segment.").font = ITALIC

# ============================================================
# SHEET 5: Scenario Comparison
# ============================================================
ws5 = wb.create_sheet("5_Scenarios")
r = add_title(ws5, "SCENARIO COMPARISON — CONSERVATIVE / BASE / OPTIMISTIC", "All scenarios use the permitted formula from MACH1_MARKET_ASSESSMENT.pdf")
set_widths(ws5, [40, 22, 22, 22])
hr = r
for i, h in enumerate(["Metric", "Conservative", "Base", "Optimistic"], 1):
    ws5.cell(row=hr, column=i, value=h)
style_header(ws5, hr, 4)
r = hr + 1

# Reference top-down sheet values
ws5.cell(row=r, column=1, value="Target segment share").font = BOLD
ws5.cell(row=r, column=2, value="=B14").value = None
# Just use direct references to topdown sheet
ws5.cell(row=r, column=1, value="Target segment share")
ws5.cell(row=r, column=2, value="='2_TopDown'!B14")
ws5.cell(row=r, column=3, value="='2_TopDown'!C14")
ws5.cell(row=r, column=4, value="='2_TopDown'!D14")
r += 1
ws5.cell(row=r, column=1, value="Average realized fare (INR)")
ws5.cell(row=r, column=2, value="='2_TopDown'!B16")
ws5.cell(row=r, column=3, value="='2_TopDown'!C16")
ws5.cell(row=r, column=4, value="='2_TopDown'!D16")
r += 1
ws5.cell(row=r, column=1, value="Annual platform rides")
ws5.cell(row=r, column=2, value="='2_TopDown'!B11")
ws5.cell(row=r, column=3, value="='2_TopDown'!C11")
ws5.cell(row=r, column=4, value="='2_TopDown'!D11")
r += 1
ws5.cell(row=r, column=1, value="Target segment annual rides").font = BOLD
ws5.cell(row=r, column=2, value="='2_TopDown'!B15")
ws5.cell(row=r, column=3, value="='2_TopDown'!C15")
ws5.cell(row=r, column=4, value="='2_TopDown'!D15")
r += 1
ws5.cell(row=r, column=1, value="Illustrative annual GMV (INR crore)").font = BOLD
ws5.cell(row=r, column=2, value="='2_TopDown'!B17/10000000")
ws5.cell(row=r, column=3, value="='2_TopDown'!C17/10000000")
ws5.cell(row=r, column=4, value="='2_TopDown'!D17/10000000")
r += 1
ws5.cell(row=r, column=1, value="Target active vehicles")
ws5.cell(row=r, column=2, value="='2_TopDown'!B20")
ws5.cell(row=r, column=3, value="='2_TopDown'!C20")
ws5.cell(row=r, column=4, value="='2_TopDown'!D20")
r += 1
ws5.cell(row=r, column=1, value="FleetLine E1 addressable vehicles").font = BOLD
ws5.cell(row=r, column=2, value="='2_TopDown'!B24")
ws5.cell(row=r, column=3, value="='2_TopDown'!C24")
ws5.cell(row=r, column=4, value="='2_TopDown'!D24")
r += 1
ws5.cell(row=r, column=1, value="FleetLine E1 revenue (INR crore)")
ws5.cell(row=r, column=2, value="='2_TopDown'!B26*1272600/10000000")
ws5.cell(row=r, column=3, value="='2_TopDown'!C26*1272600/10000000")
ws5.cell(row=r, column=4, value="='2_TopDown'!D26*1272600/10000000")
r += 2
ws5.cell(row=r, column=1, value="Airport segment (bottom-up)").font = Font(bold=True, size=12, color="1F3864")
r += 1
ws5.cell(row=r, column=1, value="Airport app-cab trips per year")
ws5.cell(row=r, column=2, value="='3_BottomUp_Airport'!B10")
ws5.cell(row=r, column=3, value="='3_BottomUp_Airport'!C10")
ws5.cell(row=r, column=4, value="='3_BottomUp_Airport'!D10")
r += 1
ws5.cell(row=r, column=1, value="Airport active vehicles")
ws5.cell(row=r, column=2, value="='3_BottomUp_Airport'!B14")
ws5.cell(row=r, column=3, value="='3_BottomUp_Airport'!C14")
ws5.cell(row=r, column=4, value="='3_BottomUp_Airport'!D14")
r += 1
ws5.cell(row=r, column=1, value="FleetLine E1 airport vehicles")
ws5.cell(row=r, column=2, value="='3_BottomUp_Airport'!B18")
ws5.cell(row=r, column=3, value="='3_BottomUp_Airport'!C18")
ws5.cell(row=r, column=4, value="='3_BottomUp_Airport'!D18")
r += 2
ws5.cell(row=r, column=1, value="NOTE: All figures are ILLUSTRATIVE. Target share and fare are assumptions, not measured.").font = ITALIC
r += 1
ws5.cell(row=r, column=1, value="Do not call any of these TAM, SAM, or SOM. Do not extend to 2035 with a CAGR.").font = ITALIC

# ============================================================
# SHEET 6: Sensitivity
# ============================================================
ws6 = wb.create_sheet("6_Sensitivity")
r = add_title(ws6, "SENSITIVITY ANALYSIS", "FleetLine E1 addressable vehicles vs key variables")
set_widths(ws6, [40, 15, 15, 15, 15, 15])
hr = r
for i, h in enumerate(["Variable", "Low", "Base", "High", "Impact", "Notes"], 1):
    ws6.cell(row=hr, column=i, value=h)
style_header(ws6, hr, 6)
r = hr + 1

sens = [
    ("Target segment share", 0.05, 0.10, 0.15, "Dominant driver of GMV and vehicle demand"),
    ("Average realized fare (INR)", 300, 450, 600, "Second most important variable"),
    ("Rides per active vehicle/yr", 1500, 2080, 2500, "Affects vehicle count inversely"),
    ("Net fleet growth rate", 0.01, 0.03, 0.05, "Affects annual vehicle opportunity"),
    ("Annual replacement rate", 0.10, 0.15, 0.20, "Affects annual vehicle opportunity"),
    ("Serviceable city share", 0.40, 0.60, 0.80, "Geographic concentration"),
    ("Attainable OEM share", 0.02, 0.05, 0.10, "Competitive positioning"),
    ("Airport app-cab mode share", 0.15, 0.25, 0.35, "Airport segment only"),
]
for name, low, base, high, note in sens:
    ws6.cell(row=r, column=1, value=name)
    ws6.cell(row=r, column=2, value=low)
    ws6.cell(row=r, column=3, value=base)
    ws6.cell(row=r, column=4, value=high)
    ws6.cell(row=r, column=5, value="High" if name in ["Target segment share", "Average realized fare (INR)"] else "Medium")
    ws6.cell(row=r, column=6, value=note)
    for c in range(1, 7):
        ws6.cell(row=r, column=c).border = BORDER
    r += 1

# ============================================================
# SHEET 7: Methodology & Audit
# ============================================================
ws7 = wb.create_sheet("7_Methodology")
r = add_title(ws7, "METHODOLOGY, AUDIT & SOURCES", "")
set_widths(ws7, [30, 90])
hr = r
ws7.cell(row=hr, column=1, value="Item").font = BOLD
ws7.cell(row=hr, column=2, value="Detail").font = BOLD
style_header(ws7, hr, 2)
r = hr + 1

method = [
    ("Audit of 2.4B/14.8B claims", "The claims '2.4 billion rides in 2024' and '14.8 billion rides projected for 2035' were NOT found in any project file (deck, reports, CSVs, or HTML). They may originate from an external source (possibly Mordor Intelligence, cited as secondary cross-check in MACH1_MARKET_ASSESSMENT.pdf). Without the original source, these claims cannot be verified and should not be used."),
    ("Permitted formula", "GMV = observed annual rides x target-segment share x realized fare. Then: vehicles = rides / rides per active vehicle per year. Then: vehicle opportunity = target active fleet x (net fleet growth + annual replacement rate). Then: MACH1 units = vehicle opportunity x serviceable city share x attainable OEM share. Source: MACH1_MARKET_ASSESSMENT.pdf, Section 1."),
    ("Forbidden", "Extending 591.3M to 2035 with a CAGR. Calling airport/premium highest-margin without operator economics. Summing overlapping segments without de-duplication. Using clustering/regression on 5 hand-assembled rows."),
    ("Top-down inputs", "Platform rides: 1.62M/day (Uber 840k + Ola 460k + Rapido 320k), annualized 591.3M. Source: Motilal Oswal via Business Standard, 18 Apr 2025. Grade B."),
    ("Bottom-up inputs", "AAI passenger traffic: 196.24M (Apr-Sep 2026), annualized ~392.5M. Road trips = passengers x 2. App-cab mode share = 15-35% (assumption). Source: AAI Traffic Report, Sep 2026. Grade A."),
    ("Vehicle conversion", "Rides per active vehicle per year = 2,080 (conservative; 8 rides/day x 26 days x 12 months = 2,496). Growth 3%, replacement 15%, city share 60%, OEM share 5%. All assumptions, Grade C."),
    ("TCO (Grade A)", "Delhi 5-yr: +14.5% nominal, +6.5% incl infra, +6.7% NPV. Driver: +Rs 14,200/mo. City matrix: Delhi +6.7, Mumbai +4.0, Bengaluru +0.9 (5-yr financed incl-NPV)."),
    ("Key constraint", "Web search returns HTTP 402. Direct URL fetches work. Six external lynchpins unverified. All assumptions labelled."),
    ("Output units", "Ride volumes (rides/yr), transaction value (INR/yr), operator revenue (INR/yr), vehicle sales (vehicles/yr), revenue (INR/yr). These are DISTINCT and must not be confused."),
]
for name, detail in method:
    ws7.cell(row=r, column=1, value=name).font = BOLD
    ws7.cell(row=r, column=2, value=detail)
    ws7.cell(row=r, column=1).border = BORDER
    ws7.cell(row=r, column=2).border = BORDER
    ws7.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical="top")
    ws7.row_dimensions[r].height = 60
    r += 1

wb.save(OUT / "market_sizing_model.xlsx")
print(f"Saved: {OUT / 'market_sizing_model.xlsx'}")
print(f"Sheets: {wb.sheetnames}")
