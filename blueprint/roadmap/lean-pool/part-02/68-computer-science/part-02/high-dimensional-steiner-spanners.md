---
declaration: theorem
origin: cited
lean: HighDimSteinerSpanners.thm_1_3_non_metric_steiner_spanner_lower_bound, HighDimSteinerSpanners.thm_1_2_geometric_spanner_lower_bound, HighDimSteinerSpanners.cor_1_4_lp_dvoretzky_lower_bound, HighDimSteinerSpanners.thm_2_3_locally_list_bounded_csp_codes, HighDimSteinerSpanners.prop_3_4_three_hop_hypercube_collapse
statement: formalized
proof: formalized
---

# Polynomial lower bounds for high-dimensional Steiner spanners

> For every real p at least one and constant stretch, some arbitrarily large point sets in real ell-p spaces force polynomial edge overhead in every non-metric Steiner spanner. Includes CSP code constructions, finite Bernoulli moment estimates, nearest terminal projection, Hamming-code hubs, Gaussian concentration, and linear Euclidean-to-ell-p embeddings.

*Quoted from the card [LeanPool/projects/high-dimensional-steiner-spanners.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/high-dimensional-steiner-spanners.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`HighDimSteinerSpanners.thm_1_3_non_metric_steiner_spanner_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/SteinerSpanners.html#HighDimSteinerSpanners.thm_1_3_non_metric_steiner_spanner_lower_bound) (theorem; a main declaration), declared in [LeanPool/SteinerSpanners.lean, line 174](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners.lean#L174): “For every real p at least one and constant stretch C at least one, arbitrarily large bounded-aspect-ratio point sets in dimension proportional to log n require at least a constant times n to the power 1+c edges in every non-metric Steiner spanner, with an explicit positive lower bound on c.”
- [`HighDimSteinerSpanners.thm_1_2_geometric_spanner_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/SteinerSpanners.html#HighDimSteinerSpanners.thm_1_2_geometric_spanner_lower_bound) (theorem; a main declaration), declared in [LeanPool/SteinerSpanners.lean, line 205](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners.lean#L205): “The same polynomial edge lower bound holds for geometric ell-p spanners.”
- [`HighDimSteinerSpanners.cor_1_4_lp_dvoretzky_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/SteinerSpanners.html#HighDimSteinerSpanners.cor_1_4_lp_dvoretzky_lower_bound) (theorem; a main declaration), declared in [LeanPool/SteinerSpanners.lean, line 229](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners.lean#L229): “For p greater than two, a polynomial edge lower bound holds in dimension proportional to the p-over-two power of log n, with an exponent bound independent of p.”
- [`HighDimSteinerSpanners.thm_2_3_locally_list_bounded_csp_codes`](https://leanpool.github.io/lean-pool/LeanPool/SteinerSpanners.html#HighDimSteinerSpanners.thm_2_3_locally_list_bounded_csp_codes) (theorem; a main declaration), declared in [LeanPool/SteinerSpanners.lean, line 154](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners.lean#L154): “Constructs arbitrarily large finite codes with many exact-distance pairs, separation, and bounded local witness lists and overlaps.”
- [`HighDimSteinerSpanners.prop_3_4_three_hop_hypercube_collapse`](https://leanpool.github.io/lean-pool/LeanPool/SteinerSpanners.html#HighDimSteinerSpanners.prop_3_4_three_hop_hypercube_collapse) (theorem; a main declaration), declared in [LeanPool/SteinerSpanners.lean, line 332](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners.lean#L332): “High-rate hypercube subsets admit sparse three-hop Steiner paths in a prescribed Hamming-distance window. Under minimum separation this extends to all terminal pairs. Also constructs a sparse three-hop spanner for the full hypercube.”

## Project

- Authors: Goran Zuzic, David P. Woodruff, Vahab Mirrokni.
- Source: *Constant-Stretch High-Dimensional Spanners Require Polynomial Overhead*.
- Project repository: [goranzuzic/high-dimensional-steiner-spanners](https://github.com/goranzuzic/high-dimensional-steiner-spanners), at commit [e75290d4](https://github.com/goranzuzic/high-dimensional-steiner-spanners/tree/e75290d4a81dc898469a71414edf5bee43dc1b02).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 68R10, 05C12, 46B07.
- In Lean Pool: [LeanPool/SteinerSpanners](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners), from the card [LeanPool/projects/high-dimensional-steiner-spanners.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/high-dimensional-steiner-spanners.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/high-dimensional-steiner-spanners.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/high-dimensional-steiner-spanners.yaml)
- [Lean Pool at bb99e52c: LeanPool/SteinerSpanners](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/SteinerSpanners)
