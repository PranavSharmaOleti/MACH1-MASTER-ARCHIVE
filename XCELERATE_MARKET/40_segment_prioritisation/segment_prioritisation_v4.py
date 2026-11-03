"""Segment prioritisation model v4 — XCELerate 2026 E-Track.

Reproduces all scores and sensitivity tests from actual ratings and explicit
weight vectors. Includes rating sensitivity (±1 on each criterion for each
segment) and corrected weight-scheme sensitivity.

Run: python3 segment_prioritisation_v4.py
Output: sensitivity_results_v4.csv, rating_sensitivity_v4.csv
"""
import csv, os, json
from itertools import product

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
_tw = sum(CRITERIA.values())
CRITERIA = {k: v / _tw * 100 for k, v in CRITERIA.items()}

# Segment scores: 1 (worst) to 5 (best) per criterion.
SCORES = {
    "intra_city_street_hail": {
        "market_size_volume": 5, "revenue_potential": 4, "vehicle_utilisation": 1,
        "operating_predictability": 1, "customer_requirements": 5, "price_sensitivity": 1,
        "fleet_economics": 2, "ev_readiness": 2, "infrastructure_availability": 5,
        "competitive_intensity": 1, "scalability": 5,
    },
    "daily_commute_subscription": {
        "market_size_volume": 3, "revenue_potential": 3, "vehicle_utilisation": 3,
        "operating_predictability": 5, "customer_requirements": 4, "price_sensitivity": 1,
        "fleet_economics": 4, "ev_readiness": 4, "infrastructure_availability": 4,
        "competitive_intensity": 4, "scalability": 4,
    },
    "airport_transfer": {
        "market_size_volume": 4, "revenue_potential": 1, "vehicle_utilisation": 4,
        "operating_predictability": 5, "customer_requirements": 3, "price_sensitivity": 4,
        "fleet_economics": 4, "ev_readiness": 5, "infrastructure_availability": 3,
        "competitive_intensity": 3, "scalability": 3,
    },
    "inter_city_outstation": {
        "market_size_volume": 2, "revenue_potential": 2, "vehicle_utilisation": 5,
        "operating_predictability": 3, "customer_requirements": 2, "price_sensitivity": 3,
        "fleet_economics": 1, "ev_readiness": 1, "infrastructure_availability": 1,
        "competitive_intensity": 4, "scalability": 2,
    },
    "premium_shared": {
        "market_size_volume": 2, "revenue_potential": 5, "vehicle_utilisation": 2,
        "operating_predictability": 4, "customer_requirements": 1, "price_sensitivity": 5,
        "fleet_economics": 3, "ev_readiness": 3, "infrastructure_availability": 3,
        "competitive_intensity": 3, "scalability": 2,
    },
}

SEGMENT_LABELS = {
    "intra_city_street_hail": "Intra-city street-hail",
    "daily_commute_subscription": "Daily commute/subscription",
    "airport_transfer": "Airport transfer",
    "inter_city_outstation": "Inter-city/outstation",
    "premium_shared": "Premium/shared mobility",
}

def score_segment(seg, weights):
    return sum(SCORES[seg][c] * weights[c] for c in CRITERIA)

def rank_segments(weights):
    results = [(seg, score_segment(seg, weights)) for seg in SCORES]
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# ============================================================
# 1. BASE WEIGHTS
# ============================================================
print("=" * 80)
print("BASE WEIGHTS (normalised from 10:10:10:15:5:5:20:15:5:5:5)")
print("=" * 80)
base_results = rank_segments(CRITERIA)
for i, (seg, sc) in enumerate(base_results, 1):
    print(f"  {i}. {SEGMENT_LABELS[seg]:<30} {sc:.2f}")

# Why Airport beats Commute: decompose
print("\n--- Why Airport (380.95) beats Commute (371.43): ---")
for c in CRITERIA:
    a = SCORES["airport_transfer"][c] * CRITERIA[c]
    cm = SCORES["daily_commute_subscription"][c] * CRITERIA[c]
    diff = a - cm
    if abs(diff) > 0.01:
        print(f"  {c:<30} Airport={a:6.2f}  Commute={cm:6.2f}  diff={diff:+6.2f}")

# ============================================================
# 2. SENSITIVITY: ALTERNATIVE WEIGHT SCHEMES
# ============================================================
alt_weights = {
    "equal_weights": {c: 100 / len(CRITERIA) for c in CRITERIA},
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

print("\n" + "=" * 80)
print("SENSITIVITY: ALTERNATIVE WEIGHT SCHEMES")
print("=" * 80)
sensitivity_rows = []
for scheme_name, weights in alt_weights.items():
    total_w = sum(weights.values())
    norm = {c: w / total_w * 100 for c, w in weights.items()}
    results = rank_segments(norm)
    print(f"\n--- {scheme_name} (weights sum to {total_w}, normalised to 100) ---")
    for i, (seg, sc) in enumerate(results, 1):
        print(f"  {i}. {SEGMENT_LABELS[seg]:<30} {sc:.2f}")
        sensitivity_rows.append({
            "scheme": scheme_name, "rank": i, "segment": seg,
            "label": SEGMENT_LABELS[seg], "score": round(sc, 2),
        })

# ============================================================
# 3. RATING SENSITIVITY: ±1 on each criterion for each segment
# ============================================================
print("\n" + "=" * 80)
print("RATING SENSITIVITY: ±1 ON EACH CRITERION (BASE WEIGHTS)")
print("=" * 80)
rating_rows = []
flips = 0
for seg in SCORES:
    for crit in CRITERIA:
        for delta in (-1, +1):
            orig = SCORES[seg][crit]
            new_val = orig + delta
            if new_val < 1 or new_val > 5:
                continue
            # Temporarily modify
            SCORES[seg][crit] = new_val
            new_results = rank_segments(CRITERIA)
            new_leader = new_results[0][0]
            new_airport = [s for s, _ in new_results if s == "airport_transfer"][0]
            airport_rank = [i for i, (s, _) in enumerate(new_results, 1) if s == "airport_transfer"][0]
            airport_score = [sc for s, sc in new_results if s == "airport_transfer"][0]
            commute_score = [sc for s, sc in new_results if s == "daily_commute_subscription"][0]
            flipped = (new_leader != "airport_transfer") if seg == "airport_transfer" and delta == -1 else False
            if new_leader != "airport_transfer" and seg in ("airport_transfer",) and delta == -1:
                flips += 1
            rating_rows.append({
                "segment_perturbed": seg, "criterion": crit, "delta": delta,
                "original_rating": orig, "new_rating": new_val,
                "airport_score": round(airport_score, 2),
                "commute_score": round(commute_score, 2),
                "airport_rank": airport_rank,
                "leader": SEGMENT_LABELS[new_leader],
                "flip": "YES" if new_leader != "airport_transfer" and seg == "airport_transfer" and delta == -1 else "",
            })
            # Restore
            SCORES[seg][crit] = orig

# Summary: which perturbations flip the leader from Airport to Commute
print("\nPerturbations that flip leader from Airport to Commute:")
flip_count = 0
for r in rating_rows:
    if r["flip"] == "YES":
        flip_count += 1
        print(f"  {r['segment_perturbed']}: {r['criterion']} {r['delta']:+d} "
              f"({r['original_rating']}->{r['new_rating']}) -> Airport rank {r['airport_rank']}, "
              f"leader: {r['leader']}")
print(f"Total flips: {flip_count}")

# ============================================================
# 4. WRITE OUTPUTS
# ============================================================
# Sensitivity results
with open(os.path.join(OUT, "sensitivity_results_v4.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["scheme", "rank", "segment", "label", "score"])
    w.writeheader()
    w.writerows(sensitivity_rows)

# Rating sensitivity
with open(os.path.join(OUT, "rating_sensitivity_v4.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rating_rows[0].keys()))
    w.writeheader()
    w.writerows(rating_rows)

# Base scores
base_out = []
for seg, sc in base_results:
    base_out.append({"segment": seg, "label": SEGMENT_LABELS[seg], "total_score": round(sc, 2)})
with open(os.path.join(OUT, "base_scores_v4.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["segment", "label", "total_score"])
    w.writeheader()
    w.writerows(base_out)

# Criterion contribution table
contrib_rows = []
for c in CRITERIA:
    row = {"criterion": c, "weight": round(CRITERIA[c], 4)}
    for seg in SCORES:
        row[seg] = SCORES[seg][c] * CRITERIA[c]
    contrib_rows.append(row)
with open(os.path.join(OUT, "criterion_contributions_v4.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["criterion", "weight"] + list(SCORES.keys()))
    w.writeheader()
    w.writerows(contrib_rows)

print(f"\nDone. Files written to {OUT}")
print("  sensitivity_results_v4.csv")
print("  rating_sensitivity_v4.csv")
print("  base_scores_v4.csv")
print("  criterion_contributions_v4.csv")
