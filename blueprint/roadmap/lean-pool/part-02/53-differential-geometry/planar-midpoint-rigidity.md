---
declaration: theorem
origin: cited
lean: PlanarMidpoint.planar_dual_midpoint_rigidity
statement: formalized
proof: formalized
---

# Planar Euclidean dual-geodesic midpoint rigidity

> Complementary canonical local midpoints for two Euclidean dual torsion-free connections force their symmetric cubic tensor to be constant on a connected open planar domain. The proof constructs the local geodesic germs and derives the fourth-order obstruction, including its exceptional tensors. A differential strengthening needs only differentiability; five fixed direction tests suffice.

*Quoted from the card [LeanPool/projects/planar-midpoint-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/planar-midpoint-rigidity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PlanarMidpoint.planar_dual_midpoint_rigidity`](https://leanpool.github.io/lean-pool/LeanPool/PlanarMidpoint/MidpointRigidity.html#PlanarMidpoint.planar_dual_midpoint_rigidity) (theorem; a main declaration), declared in [LeanPool/PlanarMidpoint/MidpointRigidity.lean, line 44](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PlanarMidpoint/MidpointRigidity.lean#L44): “On an open preconnected Euclidean planar domain, a smooth symmetric cubic tensor field whose canonical local dual geodesic midpoints sum to the endpoints is constant.”
- [`PlanarMidpoint.planar_midpoint_rigidity_C2`](https://leanpool.github.io/lean-pool/LeanPool/PlanarMidpoint/MidpointRigidity.html#PlanarMidpoint.planar_midpoint_rigidity_C2) (theorem), declared in [LeanPool/PlanarMidpoint/MidpointRigidity.lean, line 31](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PlanarMidpoint/MidpointRigidity.lean#L31): “The geometric midpoint rigidity theorem already holds for C2 coefficient fields.”
- [`PlanarMidpoint.planar_obstruction_rigidity`](https://leanpool.github.io/lean-pool/LeanPool/PlanarMidpoint/DifferentialRigidity.html#PlanarMidpoint.planar_obstruction_rigidity) (theorem), declared in [LeanPool/PlanarMidpoint/DifferentialRigidity.lean, line 109](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PlanarMidpoint/DifferentialRigidity.lean#L109): “A differentiable planar cubic coefficient field is constant if its quartic midpoint obstruction vanishes at every point and in every direction.”
- [`PlanarMidpoint.planar_five_direction_rigidity`](https://leanpool.github.io/lean-pool/LeanPool/PlanarMidpoint/FiveDirections.html#PlanarMidpoint.planar_five_direction_rigidity) (theorem), declared in [LeanPool/PlanarMidpoint/FiveDirections.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PlanarMidpoint/FiveDirections.lean#L28): “The differential obstruction criterion needs only the five directions (j, 1) for j = 0, 1, 2, 3, 4 at every point.”

## Project

- Authors: JD Jones.
- Source: [arXiv:2609.07551](https://arxiv.org/abs/2609.07551).
- The card's note on its source: “The upstream MIT-licensed original proof settles the dimension-two case of Nielsen–Okamura Conjecture 9.1 (v2, Section 9); the cited paper poses the general-dimensional conjecture and does not contain this planar necessity proof. Public completed source was released on 2026-10-08. Proofs and mathematical arguments were produced by OpenAI Codex agents under JD Jones's supervision.”
- Project repository: [JD-Jones-ASES/PlanarMidpoint](https://github.com/JD-Jones-ASES/PlanarMidpoint), at commit [f277b89a](https://github.com/JD-Jones-ASES/PlanarMidpoint/tree/f277b89a3b0db20872101fd61580ecced748e7c1).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 53B12, 39B22.
- In Lean Pool: [LeanPool/PlanarMidpoint](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PlanarMidpoint), from the card [LeanPool/projects/planar-midpoint-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/planar-midpoint-rigidity.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/planar-midpoint-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/planar-midpoint-rigidity.yaml)
- [Lean Pool at 701389c0: LeanPool/PlanarMidpoint](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/PlanarMidpoint)
