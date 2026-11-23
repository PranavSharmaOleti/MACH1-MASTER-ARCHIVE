# 05 — Professor discussion brief

*Prepared for an academic methodology discussion. Self-contained; no repository navigation required.*

## 1. Project background

MACH1 was a student case submission for Maruti Suzuki XCELerate 2026 (E-Track). The proposed vehicle, **FleetLine E1**, was a sub-4-metre, ~45 kWh electric fleet sedan for India's ride-service market by 2035. Our task was to justify which market segment the vehicle should target and who would buy it.

## 2. Original research objective

We set out to show that two operating environments — **airport transfers** and **contracted corporate employee commute** — were attractive entry points because they are pre-booked, predictable and depot-chargeable, unlike on-demand intra-city work. The evidence was secondary desk research: press reports, operator websites, government data and our own models. No primary interviews or trip-level data were collected.

## 3. How we approached market segmentation

We built a five-row comparison table on one presentation slide: intra-city, daily commute, airport, inter-city, premium/shared-premium. Each row had seven numbers: average trip km, km/day, trips/day, fare, growth, EV share and a "price sensitivity" index. All were hand-assembled; none carried a source. We then ran a weighted 11-criteria scoring model on the same five segments, producing Airport 380.95 and Commute 371.43 out of 500.

## 4. How the dendrogram was constructed

The slide carried a figure titled **"Agglomerative Hierarchical Clustering — average linkage, Euclidean distance, 7 z-scored features"**, with four merge heights. It was a real computed dendrogram, produced outside the repository (no script or distance matrix survives). Its input was the five-row, seven-column table above, z-scored across five rows.

Crucially, the figure groups **Airport with Premium**, and **Commute with Intra-city** at the first merge. The slide's adjacent text label — "CLUSTER A = airport + corporate-commute" — does not match the figure. Also, recomputing from the visible table with the stated method gives merge heights 1.454 / 1.971 / 3.202 / 5.630, not the displayed 1.000 / 1.63 / 2.64 / 5.036; we could not reproduce the original figure.

## 5. What went wrong and why it was challenged

An external market assessment (18 Oct 2026) withdrew the earlier analysis: five manually constructed rows and seven columns, no rider/city/trip/vehicle observations, several inputs unsupported or not measured on a common basis. Z-scoring seven features across five rows cannot convert judgments into sampled market behaviour. The assessment recommended removing the dendrogram and not substituting another clustering algorithm on the same five rows. It separately criticised a five-row regression for having only two residual degrees of freedom.

Statistically, the problem is not hierarchical clustering itself but the **unit of analysis**: we clustered five invented segment profiles, not observations. There is no within-segment variance, no way to assess stability, and p=7 features against n=5 rows makes distances extremely sensitive to coding choices. The interpretation was also inconsistent with the computed branches.

## 6. What we did afterwards

We corrected the deck text and panel Q&A to call the dendrogram "illustrative, not statistically derived" and removed the claim. We rebuilt the market work: a 42-source register, operator/airport/corporate/procurement datasets, red-team reports v2–v6.1, and cleaned data files with explicit evidence grades. The strategic recommendation survived — but via the scoring model, not clustering, and reframed as **candidate market-entry environments** rather than a proven profit segment. Two further caveats: the scoring ratings are analyst-assigned (not measured), and under equal weights Airport and Commute **tie** (354.55 each).

## 7. What research and datasets remain available

Secondary datasets (Vahan registrations, AutoPunditz sales, 591.3M platform-ride proxy, ~810M Redseer estimate), operator intelligence (Everest, Lithium, Evera, Refex, OHM and others, mostly company-reported), procurement relationships, source register with URLs and evidence grades, a transparent scoring script, and audit/correction records. What is absent: trip-level or operator-month data, measured segment shares or margins, verified fleet sizes and procurement behaviour.

## 8. What we want to rebuild

Not the entire project — only the segmentation claim and its slide. We want a defensible method for deciding whether airport and corporate commute merit a shared vehicle platform, using the existing evidence honestly and stating clearly what cannot be concluded.

## 9. Questions for the professor

1. Given no observation-level data, is any clustering defensible here, or should we replace it entirely with a transparent multi-criteria framework with published weights and sensitivity?
2. If clustering remains appropriate, what should the observation be (city × use case × month?) and what minimum sample and feature set would be defensible?
3. How should we handle mixed numerical/categorical variables, scaling and distance/linkage choice — and how much stability testing would a panel require?
4. Is it methodologically acceptable to retain a strategic shortlist that was originally justified by clustering, once that clustering is withdrawn, provided the shortlist is re-derived from a scoring model with explicit judgment-based ratings?
5. How should we present the equal-weight tie between Airport and Commute — as a genuine ambiguity or as grounds to keep both as co-equal candidates?
6. What is the academically correct way to describe the original dendrogram in a methods section: "mathematically generated but invalid inputs", or simply "not a valid analysis"?
