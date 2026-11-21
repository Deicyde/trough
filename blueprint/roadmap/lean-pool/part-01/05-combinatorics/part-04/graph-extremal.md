---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_isClique_support_le, SimpleGraph.cliqueWeight_le_choose_mul, SimpleGraph.paleyGraph_isSRGWith
statement: formalized
proof: formalized
---

# Weight shifting and extremal graph theory

> General convex weight shifting on nonedges, attained Motzkin–Straus and weighted Zykov bounds, finite bipartite matching-cover duality, lexicographic graph products and Paley graphs with strong regularity, clique bounds and diameter two.

*Quoted from the card [LeanPool/projects/graph-extremal.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/graph-extremal.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SimpleGraph.exists_isClique_support_le`](https://leanpool.github.io/lean-pool/LeanPool/GraphExtremal/Extremal/WeightShifting.html#SimpleGraph.exists_isClique_support_le) (theorem; a main declaration), declared in [LeanPool/GraphExtremal/Extremal/WeightShifting.lean, line 77](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GraphExtremal/Extremal/WeightShifting.lean#L77): “A nonnegative weighting is dominated by one supported on a clique for functions convex along nonedge directions.” Its source, as the card gives it: “Upstream lean-graph-extremal at cdd96c43e8cb0a95eba37eeaf8bf3ecf0e93baf9; proposed in \#721 in the comment of 2026-10-31T14:28:18Z.”
- [`SimpleGraph.cliqueWeight_le_choose_mul`](https://leanpool.github.io/lean-pool/LeanPool/GraphExtremal/Extremal/Zykov.html#SimpleGraph.cliqueWeight_le_choose_mul) (theorem; a main declaration), declared in [LeanPool/GraphExtremal/Extremal/Zykov.lean, line 233](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GraphExtremal/Extremal/Zykov.lean#L233): “Weighted Zykov bounds control every clique count in a clique-free graph.” Its source, as the card gives it: “Upstream lean-graph-extremal at cdd96c43e8cb0a95eba37eeaf8bf3ecf0e93baf9; proposed in \#721 in the comment of 2026-10-31T14:28:18Z.”
- [`SimpleGraph.paleyGraph_isSRGWith`](https://leanpool.github.io/lean-pool/LeanPool/GraphExtremal/Paley.html#SimpleGraph.paleyGraph_isSRGWith) (theorem; a main declaration), declared in [LeanPool/GraphExtremal/Paley.lean, line 346](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GraphExtremal/Paley.lean#L346): “A finite-field Paley graph has the classical strongly regular parameters under the stated characteristic and square conditions.” Its source, as the card gives it: “Upstream lean-graph-extremal at cdd96c43e8cb0a95eba37eeaf8bf3ecf0e93baf9; proposed in \#721 in the comment of 2026-10-31T14:28:18Z.”

## Project

- Authors: Brian Sanders.
- Source: *Weight shifting and extremal graph theory* by Brian Sanders.
- Project repository: [Egly443/lean-graph-extremal](https://github.com/Egly443/lean-graph-extremal), at commit [cdd96c43](https://github.com/Egly443/lean-graph-extremal/tree/cdd96c43e8cb0a95eba37eeaf8bf3ecf0e93baf9).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C55, 05D10.
- In Lean Pool: [LeanPool/GraphExtremal](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GraphExtremal), from the card [LeanPool/projects/graph-extremal.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/graph-extremal.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/graph-extremal.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/graph-extremal.yaml)
- [Lean Pool at 307e3125: LeanPool/GraphExtremal](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/GraphExtremal)
