import json, shutil
from collections import Counter
from pathlib import Path

ROOT=Path('/home/sankara/Downloads/MACH1_WORKING_FILES')
OUT=ROOT/'MACH1_MASTER_ARCHIVE'
DOC=OUT/'00_MASTER_DOCUMENTATION'
inv=json.loads(Path('/tmp/mach1_audit/inventory.json').read_text())

def destination(rel):
    p=Path(rel); top=p.parts[0]
    if rel in ('Detailed Presentation Report.pdf','Detailed Presentation Virtual.mp4') or top=='drafts': return Path('01_PRESENTATION_AND_REPORTS')/p
    if top=='Key docs': return (Path('07_RESEARCH_AND_REFERENCES') if p.name.endswith('.pdf') and not p.name.startswith('MACH1_') and p.name not in ('Execution.pdf','Why Dzire Tour S — FleetLine E1 Rationale.pdf') else Path('01_PRESENTATION_AND_REPORTS'))/p
    if top in ('Mach1_NITDURGAPUR','MACH1_NITDURGAPUR.pdf'): return Path('02_PRIMARY_SOURCE_DOCUMENTS')/p
    if top in ('data','Market'): return Path('03_ENGINEERING_DATA')/p
    if top in ('tco_engine','battery_model'): return Path('04_CALCULATIONS_AND_ANALYSIS')/p
    if top=='images': return (Path('05_CAD_AND_DESIGN') if p.suffix.lower()=='.dwg' else Path('08_IMAGES_PLOTS_AND_MEDIA'))/p
    if top=='specs': return Path('05_CAD_AND_DESIGN')/p
    if top=='extracted_papers': return Path('07_RESEARCH_AND_REFERENCES')/p
    if top in ('superseded','Mach1_NITDURGAPUR_Round1') or p.name.startswith('Screenshot 2026-10-') or p.name=='MACH1_WORKING_FILES.zip': return Path('90_ARCHIVE_AND_OLD_VERSIONS')/p
    return Path('99_UNCLASSIFIED_REVIEW_REQUIRED')/p

def rec(pid,slide,context,point,shown,unit,file='',location='',original='',method='',status='Unverified',notes=''):
    return {'provenance_id':pid,'slide':slide,'context':context,'data_point':point,'displayed_value':shown,'unit':unit,'source_file':file,'source_location':location,'original_value':original,'methodology':method,'status':status,'notes':notes}

R=[]
def add(*args): R.append(rec(*args))

# id | slide | context | point | shown | unit | source file | location | original | method | status | notes
seed='''
P-002-001|2|Thesis|Contrasted daily duties|95 vs 210|km/day|||Narrative comparison|Unverified|Corrective market assessment withdraws unsupported use-case daily-km claims.
P-002-002|2|Thesis|Flat platform fee|₹67/day|INR/day|Key docs/MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf|page 3 platform-model table|₹67/day|Direct carry-over|Verified|Local report labels it a platform-model assumption.
P-002-003|2|Thesis|Small-car GST and saving|5%; ₹1.5L|percent; INR lakh|||Tax/price assertion|External source|No local primary tax notification.
P-003-001|3|Market|Five use-case table inputs|12.7–280 km/trip; 95–340 km/day; 1.5–8 trips/day; ₹350–4,200; 18–28% growth; 5–18% EV; 0.30–0.90 sensitivity|mixed|Key docs/MACH1_MARKET_ASSESSMENT.pdf|pages 1 and 3|Current assessment says earlier use-case inputs were unsupported|Manual five-row construct|Discrepancy|Current local assessment says these outputs should not appear in the deck.
P-003-002|3|Market|Intra-city share and airport CAGR|61%; 19.14% CAGR|percent|||Market share/growth claim|Unverified|No local supporting dataset/citation.
P-003-003|3|Market|Range sufficiency|315 vs 200|km|Key docs/MACH1_E1_Audience_and_Positioning.pdf|page 2|315 km against 200 km/day|Direct carry-over|Verified|315 is zero-reserve range at corrected consumption.
P-003-004|3|Market|BluSmart residual values|10%; 26%|percent|||Narrative market claim|External source|Underlying evidence absent.
P-004-001|4|Vehicle concept|Battery pack|45|kWh|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|page 10|45 kWh|Direct specification|Verified|Slide 5 calls the pack structural; other reports use detachable/semi-structural.
P-004-002|4|Vehicle concept|Motor rating|80 continuous|bhp|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|page 10|80 continuous / 100 peak|Direct specification|Verified|
P-004-003|4|Vehicle concept|Dimensions|3,995; 1,684; 1,532; 2,450|mm|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|page 15|same dimension set|Direct carry-over|Verified|
P-004-004|4|Vehicle concept|Annual mileage|62,400|km/year|Key docs/MACH1_TCO_ANALYSIS.pdf|page 3|200×26×12=62,400|Derived arithmetic|Verified — Derived|
P-004-005|4|Vehicle concept|Cell design point|48|°C|battery_model/self_audit.py|lines 128-134|48°C internal design point|Model parameter|Partially verified|No thermal test evidence.
P-004-006|4|Vehicle concept|Boot / price / network|400 L; ~₹14L; 3,614 outlets|mixed|Key docs/Why Dzire Tour S — FleetLine E1 Rationale.pdf|page 2|Concept target and external claims|Concept/external|Partially verified|No E1 volume CAD calculation or corporate network source.
P-005-001|5|Powertrain|Motor / pack specification|80/100 bhp; 45 kWh|bhp; kWh|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|page 10|80 continuous/100 peak; 45 kWh|Direct specification|Verified|
P-005-002|5|Powertrain|Usable-energy statements|36 kWh 10–90%; 3% top/bottom|kWh; percent|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|pages 5 and 10|45×90%=40.5 kWh|Conflicting basis|Discrepancy|Displayed reserve windows do not reconcile.
P-005-003|5|Powertrain|Claimed versus corrected range|263 vs 315|km|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|page 5|315 km at 12.84 kWh/100km|Corrected calculation|Discrepancy|263 uses obsolete 15.38 kWh/100km deck consumption.
P-005-004|5|Powertrain|Daily energy and zero-reserve range|25.68; 315.4|kWh/day; km|tco_engine/figures.txt|lines 119-122|45×0.90÷0.1284=315.4; 12.84×200/100=25.68|Derived model calculation|Verified — Derived|
P-005-005|5|Powertrain|AC charge times|4.9 at 7.4kW; 3.3 at 11kW|hours|Key docs/MACH1_POWERTRAIN_SPECS_REPORT.pdf|page 6|36÷7.4=4.86; 36÷11=3.27|Direct arithmetic|Verified — Derived|
P-005-006|5|Powertrain|Charging tariffs|₹5.50–9; ₹18–24|INR/kWh|Key docs/MACH1_TCO_ANALYSIS.pdf|page 12|same external-input ranges|Tariff assumption|Partially verified|Primary tariff notices absent.
P-005-007|5|Powertrain|Public charging / Bio-CNG figures|35,000 ports; 5.7m EVs; 207 plants; 5,000 target|counts|||External statistics|External source|No underlying sources retained.
P-005-008|5|Powertrain|Pack architecture label|structural pack|text|Key docs/MACH1_BATTERY_EXECUTIVE_REPORT.pdf|page 1|detachable pack architecture|Architecture comparison|Discrepancy|Deck vocabulary conflicts with battery report.
P-006-001|6|Sovereign battery strategy|Sodium-ion research/programme figures|80% in 6 min; >3,000 cycles; 80 cells × 5 Ah; ₹18,100cr; ₹16,300cr; ₹18,000cr; 411GWh|mixed|||External results/policy|External source|No underlying research, official notices or parliamentary response retained.
P-006-002|6|Sovereign battery strategy|Automotive sodium-ion scale|23–25|kWh|Key docs/MACH1_BATTERY_EXECUTIVE_REPORT.pdf|page 2|No 45kWh-class layered-oxide supplier|Secondary synthesis|Partially verified|Not supplier primary evidence.
P-006-003|6|Sovereign battery strategy|Chemistry decision timing|2032–33; 2036–38|years|Key docs/MACH1_BATTERY_EXECUTIVE_REPORT.pdf|pages 1 and 3|LFP primary, sodium optional second act|Design decision|Verified|
P-006-004|6|Sovereign battery strategy|Certification/cost/time/geometry|AIS-038; ₹2–3cr/4–6mo vs ₹15–25cr/18–24mo; 256×106×32; 102–108s|mixed|Key docs/MACH1_BATTERY_EXECUTIVE_REPORT.pdf|page 2 for regulatory reading|Secondary reading / unsupported concept estimates|Mixed|Partially verified|Check official standard; no cost model/CAD/BOM.
P-006-005|6|Sovereign battery strategy|Pack/SoH at design condition|44.2 at 48°C; 77.3%|kWh; percent|battery_model/self_audit.py|lines 128-134|Internal script audit|Model output|Partially verified|No experimental validation.
P-007-001|7|TCO|Duty cycle|200; 5,200; 62,400|km/day; km/month; km/year|Key docs/MACH1_TCO_ANALYSIS.pdf|page 3|200×26×12=62,400|Model arithmetic|Verified — Derived|
P-007-002|7|TCO|Consumption / efficiency|12.84; 90|kWh/100km; percent|tco_engine/tco_engine.py|line 12|12.84 kWh/100km; 90% wall-to-battery|Model input|Verified|
P-007-003|7|TCO|Fare calculation|₹11; ₹67/day; ₹10.665; ₹57,200; ₹1,742; ₹55,458|mixed|Key docs/MACH1_TCO_ANALYSIS.pdf|pages 3 and 8|Net fare calculation shown|Model arithmetic|Verified — Derived|
P-007-004|7|TCO|Finance/hurdle|10%; 60 months; 12%|percent; months|Key docs/MACH1_TCO_ANALYSIS.pdf|page 3|same|Model inputs|Verified|
P-007-005|7|TCO|Delhi result excluding charger|₹5.75 vs ₹6.73; +14.5%|INR/km; percent|Key docs/MACH1_TCO_ANALYSIS.pdf|pages 5,7,8|Explicitly nominal excluding infrastructure|Model result|Verified|Do not call charger-inclusive.
P-007-006|7|TCO|Delhi result including charger|₹6.31 vs ₹6.75; +6.5% nominal; +6.7% NPV|INR/km; percent|Key docs/MACH1_TCO_ANALYSIS.pdf|page 8|charger-inclusive result|Model result|Verified|Relevant basis when charger included.
P-007-007|7|TCO|Charger and nightly time|₹99,000; 3.86h|INR/vehicle; hours|tco_engine/figures.txt|lines 39-40|50k+30k+10k with N+1 uplift; 25.68÷(7.4×.90)|Derived model calculation|Verified — Derived|
P-007-008|7|TCO|Downtime headroom|25.4 total; 21.9 beyond baseline|hours/month|Key docs/MACH1_TCO_ANALYSIS.pdf|page 13|same|Model break-even|Verified|
P-007-009|7|TCO|Eight-year Delhi and tariff sensitivity|+28.0% excl infra; +17.4% incl infra; ₹4.50→12=-1.4%; →18=-14.1%|percent; INR/kWh|Key docs/MACH1_TCO_ANALYSIS.pdf|pages 5,8,10|same|Model output|Verified|
P-007-010|7|TCO|Mumbai/Bengaluru table|5.35–7.25 INR/km; 7.6–16.4%|mixed|Key docs/MACH1_TCO_ANALYSIS.pdf|page 7|multiple infrastructure treatments|Model output|Partially verified|Deck needs basis labels.
P-008-001|8|Driver/rider review|Post-loan advantage / take-home|₹14,200/mo; ₹47,060 vs ₹32,860; +43.2%|INR/month; percent|Key docs/MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf|page 2|same table|Model output|Verified|Delhi/200km-day/fare assumptions apply.
P-008-002|8|Driver/rider review|Stress cases|₹10,597 at 150km/day; ₹93,600/₹114,400 gross|INR/month|Key docs/MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf|pages 1 and 3|same|Sensitivity/direct arithmetic|Verified — Derived|
P-008-003|8|Driver/rider review|Rider survey/feature figures|17,993/325; 10,000+; 74/62/53/30/25/6%; 1.2/5|mixed|||External surveys/benchmark|External source|No instrument, raw data, rubric or full citation.
P-008-004|8|Driver/rider review|Reliability mechanism|21.9h/mo; ₹99,000 charger|hours/month; INR|Key docs/MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf|page 6|same|TCO cross-reference|Verified|Not proof of causal rider satisfaction.
P-009-001|9|AI and connected mobility|TPMS/charge control thresholds|32–35psi; 30–50°C; <28/>60; <22/>70; CC ~70–80%|mixed|||Technical proposal|Unverified|No supplier specification, BMS logic or validation.
P-009-002|9|AI and connected mobility|Illustrative pilot targets|≥7 days; 20–30% less downtime; ~15% fewer deadhead km; 15–18% lower charging cost|mixed|Detailed Presentation Report.pdf|page 9, labelled illustrative|Targets subject to validation|Pilot hypothesis|Unverified|Do not present as achieved performance.
P-010-001|10|Roadmap|Dates and scale|2026–27; 2028–30; 2031–35; 1–2k; 15–25k; 100k+|years; vehicles|Key docs/MACH1_ROADMAP_FLOW.pdf|page 1|gated roadmap|Programme plan|Partially verified|Initial volume explicitly indicative/gate-conditional.
P-010-002|10|Roadmap|Infrastructure/gates|7.4kW; 10% N+1; ₹99k; 3.86h; 12mo; 3.6×; 20k; 21.9h|mixed|Key docs/MACH1_ROADMAP_FLOW.pdf|pages 1-2|same|Model/carry-over|Verified — Derived|
P-010-003|10|Roadmap|Range/corridors|268/315; 200/150/170/145/280|km|Key docs/MACH1_ROADMAP_FLOW.pdf|page 2|range model; stated routes|Range/route assertion|Partially verified|Range verified; route distances require authoritative source.
P-010-004|10|Roadmap|State policy figures|₹1L; 15% cap ₹2L; 20–25%; 2030|mixed|||External policy|External source|Official state policy files absent.
P-010-005|10|Roadmap|TCO NPV headline and power break-even|Delhi +6.7/+14.6; Mumbai +4.0/+10.6; Bengaluru +0.9/+9.0; 14.5/8.8/8.7%/yr|percent|Key docs/MACH1_ROADMAP_FLOW.pdf|page 3|12% NPV, escalation, financed 60mo, charger included|Model output|Verified|
P-011-001|11|Synthesis|Market share/adoption values|~58; ~19; ~10; ~18|percent|Key docs/MACH1_MARKET_ASSESSMENT.pdf|pages 1-3|unsupported earlier inputs|Market narrative|Discrepancy|Current assessment withdraws them.
P-011-002|11|Synthesis|Range/dimension|268 at 15%; 315 at zero; 3,995|km; mm|tco_engine/figures.txt|lines 119-123|268.1/315.4; specification dimensions|Derived model calculation|Verified — Derived|
P-011-003|11|Synthesis|Five/eight-year NPV|+6.7/+4.0/+0.9; +14.6/+10.6/+9.0|percent|Key docs/MACH1_ROADMAP_FLOW.pdf|page 3|same|Model output|Verified|
P-011-004|11|Synthesis|Policy/launch volume|₹11,900cr; 15% cap ₹2L; 25k; 31-Mar-2030; 1–2k|mixed|Key docs/MACH1_ROADMAP_FLOW.pdf|page 1 for gated volume|External policy plus programme plan|Partially verified|Policy primary sources absent; volume is not forecast.
'''
for line in seed.strip().splitlines():
    p=line.split('|')
    add(*p)

slides=[(1,'Cover','XCelerate / MACH1 title cover','No technical data; visually reviewed.'),(2,'Thesis','Problem, buyer, initial design thesis','Assumptions need evidence.'),(3,'Market','Use-case segmentation/positioning','Table conflicts with corrective assessment.'),(4,'Vehicle concept proposal','Features, dimensions, rationale','Concept specs plus external claims.'),(5,'Powertrain strategy','Specifications, alternatives, charging/range','Strong calculation trail, conflicting bases.'),(6,'The sovereign’s bet','Sodium-ion option/LFP fallback','Secondary synthesis plus external claims.'),(7,'Total cost of ownership','TCO and sensitivities','Most traceable calculation slide; charger basis critical.'),(8,'Driver rider earnings reviews','Driver P&L and rider evidence','Driver model traceable; survey claims external.'),(9,'AI & connected mobility','TPMS/charging/pilot targets','Targets explicitly unvalidated.'),(10,'Roadmap','Gates, phases, policy, economics','TCO traceable; policy sources absent.'),(11,'Synthesis','Launch recommendation','Mixes verified and unresolved data.')]
claims=[('C-001',2,'Fleet operators are the buyer because operations control utilisation/TCO.','Key docs/MACH1_E1_Audience_and_Positioning.pdf p1','Partially verified','Strategic framing.'),('C-002',3,'Airport/corporate commute is strongest launch position.','Key docs/MACH1_MARKET_ASSESSMENT.pdf pp1-3','Discrepancy','Corrective assessment says it is not proven.'),('C-003',5,'BEV/LFP/single speed is lowest cost for 200km/day depot duty.','Key docs/MACH1_TCO_ANALYSIS.pdf pp3-13','Verified','Conditioned on stated model inputs.'),('C-004',6,'LFP launch with sodium-ion later option.','Key docs/MACH1_BATTERY_EXECUTIVE_REPORT.pdf pp1-3','Verified','Internal design decision.'),('C-005',7,'Depot charging is essential to TCO.','Key docs/MACH1_TCO_ANALYSIS.pdf pp8,12-13','Verified','Model supports conditional claim.'),('C-006',8,'Driver case is more robust than operator case.','Key docs/MACH1_DRIVER_AND_RIDER_ANALYSIS.pdf pp2-3','Partially verified','Internal sensitivity model.'),('C-007',9,'AI layer will predict faults/reduce downtime.','Slide 9','Unverified','Pilot hypothesis.'),('C-008',10,'Measurements should govern scale-up.','Key docs/MACH1_ROADMAP_FLOW.pdf pp1-3','Verified','Programme decision.'),('C-009',11,'All three cities clear at five years.','Key docs/MACH1_ROADMAP_FLOW.pdf p3','Verified','Only at stated NPV/finance/charger basis.')]
