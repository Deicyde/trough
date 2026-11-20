---
declaration: theorem
origin: cited
lean: CoboundaryK3.h1_eq_all, CoboundaryK3.k_div_three_le_h1, CoboundaryK3.stair_gaugeDist, CoboundaryK3.h1_eq_four_mul, CoboundaryK3.witness_k8
statement: formalized
proof: formalized
---

# The Sym(3) permutation coboundary constant of the complete complex

> Defines the Sym(3) permutation coboundary constant h1 k of the complete complex K_k as the infimum of the moved-point ratio N/D over Sym(3)-valued non-coboundaries, where N counts points moved by triangle holonomies and D is the minimum moved-point cost over Sym(3) gauges. Proves h1 k = k/3 for every k ≥ 3. The lower bound is the star-gauge double count (Chapman–Lubotzky, Proposition 3.2), proved here only for Sym(3) in this same-degree counting convention. The upper bound comes from balanced replication of a k = 4 witness and of Kozlov's staircase seeds. Explicit witnesses for k = 4, ..., 8 are checked by kernel-evaluated gauge exhaustions. Not formalized, and only cited, are the general symmetric-group form of the Chapman–Lubotzky bound, the paper's cross-degree convention and its comparison (Proposition 10), the coefficient-subgroup minima (Proposition 5), and Section 5 beyond the displacement Gram formula.

*Quoted from the card [LeanPool/projects/coboundary-k3.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/coboundary-k3.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CoboundaryK3.h1_eq_all`](https://leanpool.github.io/lean-pool/LeanPool/CoboundaryK3/Staircase.html#CoboundaryK3.h1_eq_all) (theorem; a main declaration), declared in [LeanPool/CoboundaryK3/Staircase.lean, line 568](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3/Staircase.lean#L568): “For every k ≥ 3, the Sym(3) permutation coboundary constant h1 k of the complete complex K_k, in the same-degree moved-point counting convention, equals k/3.” Its source, as the card gives it: “Theorem 8 of doi:10.5281/zenodo.23245792 (stated there for k ≥ 4).”
- [`CoboundaryK3.k_div_three_le_h1`](https://leanpool.github.io/lean-pool/LeanPool/CoboundaryK3/Constant.html#CoboundaryK3.k_div_three_le_h1) (theorem; a main declaration), declared in [LeanPool/CoboundaryK3/Constant.lean, line 358](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3/Constant.lean#L358): “If K_k carries a Sym(3)-valued non-coboundary, then k/3 ≤ h1 k; the star gauges at the k vertices cost three times the triangle defect in total.” Its source, as the card gives it: “Proposition 1 of doi:10.5281/zenodo.23245792, which is Chapman–Lubotzky, arXiv:2311.06706, Proposition 3.2, here only for Sym(3) in the counting convention.”
- [`CoboundaryK3.stair_gaugeDist`](https://leanpool.github.io/lean-pool/LeanPool/CoboundaryK3/Staircase.html#CoboundaryK3.stair_gaugeDist) (theorem; a main declaration), declared in [LeanPool/CoboundaryK3/Staircase.lean, line 467](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3/Staircase.lean#L467): “Kozlov's staircase cochain on K\_{2t+1} has Sym(3) gauge distance exactly t(t+1).” Its source, as the card gives it: “Kozlov, arXiv:1610.07136, Definition 3.2 and Lemma 3.8, with the Sym(3) parity transfer of doi:10.5281/zenodo.23245792.”
- [`CoboundaryK3.h1_eq_four_mul`](https://leanpool.github.io/lean-pool/LeanPool/CoboundaryK3/Replication.html#CoboundaryK3.h1_eq_four_mul) (theorem; a main declaration), declared in [LeanPool/CoboundaryK3/Replication.lean, line 282](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3/Replication.lean#L282): “Balanced replication of the k = 4 witness gives h1 (4q) = 4q/3 for every q ≥ 1.” Its source, as the card gives it: “Corollary 7 of doi:10.5281/zenodo.23245792.”
- [`CoboundaryK3.witness_k8`](https://leanpool.github.io/lean-pool/LeanPool/CoboundaryK3/Witnesses.html#CoboundaryK3.witness_k8) (theorem; a main declaration), declared in [LeanPool/CoboundaryK3/Witnesses.lean, line 279](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3/Witnesses.lean#L279): “The explicit k = 8 witness of Appendix A has triangle defect 72, every Sym(3) gauge costs at least 27, and the identity gauge costs exactly 27.” Its source, as the card gives it: “Theorem 4 and Appendix A of doi:10.5281/zenodo.23245792.”

## Project

- Authors: Jeromie Beasley.
- Source: *The Permutation Coboundary Constant of the Complete Complex Is k/3 for Every k ≥ 4* by Jeromie Beasley, [doi:10.5281/zenodo.23245792](https://doi.org/10.5281/zenodo.23245792).
- Project repository: [dicipler-pixel/coboundary-k3-lean](https://github.com/dicipler-pixel/coboundary-k3-lean), at commit [70a2b3de](https://github.com/dicipler-pixel/coboundary-k3-lean/tree/70a2b3de40f88f3bbe25b63e581e1fc84e88d841).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 05E45, 20B30, 55U10.
- In Lean Pool: [LeanPool/CoboundaryK3](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3), from the card [LeanPool/projects/coboundary-k3.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/coboundary-k3.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/coboundary-k3.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/coboundary-k3.yaml)
- [Lean Pool at 307e3125: LeanPool/CoboundaryK3](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/CoboundaryK3)
