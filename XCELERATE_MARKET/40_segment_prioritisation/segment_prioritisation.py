"""Segment prioritisation model for XCELerate 2026 E-Track.
Scores five ride-service segments on 11 criteria with transparent weights.
Run: python3 segment_prioritisation.py
Output: segment_scores.csv, sensitivity analysis
"""
import csv, os

OUT = "/home/sankara/Downloads/XCELERATE_MARKET/40_segment_prioritisation"
os.makedirs(OUT, exist_ok=True)

# Criteria and weights (must sum to 100)
CRITERIA = {
    "market_size_volume": 10,
    "revenue_potential": 10,
    "vehicle_utilisation": 10,
    "operating_predictability": 15,
    "customer_requirements": 5,
    "price_sensitivity": 5,
    "fleet_economics": 20,
    "ev_readiness": 15,
    "infrastructure_availability": 5,
    "competitive_intensity": 5,
    "scalability": 5,
}
_tw=sum(CRITERIA.values())
CRITERIA={k:v/_tw*100 for k,v in CRITERIA.items()}

# Segment scores: 1 (worst) to 5 (best) per criterion.
# Every score is justified in the report. Data sources noted.
SCORES = {
    "intra_city_street_hail": {
        "market_size_volume": 5,       # ~58% of platform rides (deck, Grade D)
        "revenue_potential": 4,        # Rs 27.6/vehicle-km (calc from deck)
        "vehicle_utilisation": 1,      # 95 km/day (deck, Grade D) — lowest
        "operating_predictability": 1, # street-hail, unpredictable dispatch
        "customer_requirements": 5,    # simple: short trips, no luggage
        "price_sensitivity": 1,        # 0.85 (deck, Grade D) — highest sensitivity
        "fleet_economics": 2,          # no depot control; high churn
        "ev_readiness": 2,             # 10% EV share (deck); no depot control
        "infrastructure_availability": 5,  # dense urban charging + service
        "competitive_intensity": 1,    # Ola/Uber/Rapido saturated
        "scalability": 5,              # highest volume potential
    },
    "daily_commute_subscription": {
        "market_size_volume": 3,       # unmeasured; 50% cite as primary use (TGM)
        "revenue_potential": 3,        # Rs 25.0/vehicle-km (calc from deck)
        "vehicle_utilisation": 3,     # 176 km/day (deck, Grade D)
        "operating_predictability": 5, # subscription = fixed routes, scheduled
        "customer_requirements": 4,    # regular route, moderate luggage
        "price_sensitivity": 1,        # 0.90 (deck, Grade D) — highest
        "fleet_economics": 4,          # depot charging possible; high utilisation
        "ev_readiness": 4,             # 12% EV share; subscription enables depot
        "infrastructure_availability": 4,  # urban, moderate charging
        "competitive_intensity": 4,    # less contested than intra-city
        "scalability": 4,              # subscription model scales
    },
    "airport_transfer": {
        "market_size_volume": 4,       # 157-236M app-cab trips/yr (AAI, calc)
        "revenue_potential": 1,        # Rs 17.1/vehicle-km (calc) — LOWEST
        "vehicle_utilisation": 4,     # 210 km/day (deck, Grade D)
        "operating_predictability": 5, # pre-booked, flight schedules
        "customer_requirements": 3,    # luggage space needed (400L boot)
        "price_sensitivity": 4,        # 0.35 (deck, Grade D) — low
        "fleet_economics": 4,          # depot charging, zero deadhead
        "ev_readiness": 5,             # 18% EV share (highest); depot charging
        "infrastructure_availability": 3,  # airport depots; moderate
        "competitive_intensity": 3,    # BluSmart gap; Evera/GMR entering
        "scalability": 3,              # limited by airport count
    },
    "inter_city_outstation": {
        "market_size_volume": 2,       # small share of platform rides
        "revenue_potential": 2,        # Rs 18.5/vehicle-km (calc)
        "vehicle_utilisation": 5,     # 340 km/day (deck, Grade D) — highest
        "operating_predictability": 3, # pre-booked but long distance
        "customer_requirements": 2,    # comfort, luggage, long-range
        "price_sensitivity": 3,        # 0.40 (deck, Grade D)
        "fleet_economics": 1,          # sparse charging, long downtime risk
        "ev_readiness": 1,             # 5% EV share (lowest); range anxiety
        "infrastructure_availability": 1,  # sparse highway charging
        "competitive_intensity": 4,    # less contested
        "scalability": 2,              # limited by infra
    },
    "premium_shared": {
        "market_size_volume": 2,       # small share
        "revenue_potential": 5,        # Rs 28.9/vehicle-km (calc) — HIGHEST
        "vehicle_utilisation": 2,     # 144 km/day (deck, Grade D)
        "operating_predictability": 4, # pre-booked
        "customer_requirements": 1,    # high expectations, amenities
        "price_sensitivity": 5,        # 0.30 (deck, Grade D) — lowest
        "fleet_economics": 3,          # pre-booked = depot charging possible
        "ev_readiness": 3,             # 15% EV share
        "infrastructure_availability": 3,  # urban, moderate
        "competitive_intensity": 3,    # moderate
        "scalability": 2,              # limited by willingness to pay
    },
}

SEGMENT_LABELS = {
    "intra_city_street_hail": "Intra-city street-hail",
    "daily_commute_subscription": "Daily commute/subscription",
    "airport_transfer": "Airport transfer",
    "inter_city_outstation": "Inter-city/outstation",
    "premium_shared": "Premium/shared mobility",
}

# Compute weighted scores
results = []
for seg, scores in SCORES.items():
    weighted = {c: scores[c] * CRITERIA[c] for c in CRITERIA}
    total = sum(weighted.values())
    results.append({
        "segment": seg,
        "label": SEGMENT_LABELS[seg],
        "total_score": total,
        **scores,
        **{f"w_{c}": weighted[c] for c in CRITERIA},
    })

results.sort(key=lambda r: r["total_score"], reverse=True)

# Write CSV
cols = ["segment", "label", "total_score"] + list(CRITERIA.keys())
with open(os.path.join(OUT, "segment_scores.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for r in results:
        w.writerow({c: r[c] for c in cols})

# Sensitivity: vary weights
print("=" * 80)
print("SEGMENT PRIORITISATION — BASE WEIGHTS")
print("=" * 80)
print(f"{'Rank':<6}{'Segment':<30}{'Score':<8}{'% of max'}")
for i, r in enumerate(results, 1):
    print(f"{i:<6}{r['label']:<30}{r['total_score']:<8}{r['total_score']/500*100:.1f}%")

print("\n" + "=" * 80)
print("CRITERIA CONTRIBUTION BY SEGMENT (weighted points)")
print("=" * 80)
header = f"{'Criterion':<32}{'Weight':<8}" + "".join(f"{SEGMENT_LABELS[s][:12]:<14}" for s in SCORES)
print(header)
for c in CRITERIA:
    row = f"{c:<32}{CRITERIA[c]:<8}" + "".join(f"{SCORES[s][c]*CRITERIA[c]:<14}" for s in SCORES)
    print(row)

# Sensitivity analysis: 3 alternative weight schemes
print("\n" + "=" * 80)
print("SENSITIVITY ANALYSIS")
print("=" * 80)

alt_weights = {
    "equal_weights": {c: 100//len(CRITERIA) for c in CRITERIA},
    "volume_first": {
        "market_size_volume": 25, "revenue_potential": 15, "vehicle_utilisation": 15,
        "operating_predictability": 10, "customer_requirements": 5, "price_sensitivity": 5,
        "fleet_economics": 10, "ev_readiness": 5, "infrastructure_availability": 3,
        "competitive_intensity": 4, "scalability": 3,
    },
    "fleet_economics_first": {
        "market_size_volume": 5, "revenue_potential": 5, "vehicle_utilisation": 10,
        "operating_predictability": 15, "customer_requirements": 5, "price_sensitivity": 5,
        "fleet_economics": 30, "ev_readiness": 15, "infrastructure_availability": 5,
        "competitive_intensity": 5, "scalability": 0,
    },
}

for scheme_name, weights in alt_weights.items():
    # normalise to 100
    total_w = sum(weights.values())
    norm = {c: w/total_w*100 for c, w in weights.items()}
    print(f"\n--- {scheme_name} (normalised) ---")
    scheme_results = []
    for seg in SCORES:
        sc = sum(SCORES[seg][c] * norm[c] for c in CRITERIA)
        scheme_results.append((seg, sc))
    scheme_results.sort(key=lambda x: x[1], reverse=True)
    for i, (seg, sc) in enumerate(scheme_results, 1):
        print(f"  {i}. {SEGMENT_LABELS[seg]:<30} {sc:.1f}")

print("\nDone. Files written to", OUT)
print("  segment_scores.csv")
