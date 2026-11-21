---
declaration: theorem
origin: cited
lean: FBLOrderContinuousLH.intro_infty, FBLOrderContinuousLH.intro_poe, FBLOrderContinuousLH.cross_parameter_inclusion
statement: formalized
proof: formalized
---

# Order continuity of induced homomorphisms between free Banach lattices

> Characterizes order continuity of the lattice homomorphism induced by a bounded operator between real Banach spaces, for every free convexity exponent from one to infinity. Develops concrete free p-convex Banach lattices, their universal property, operator-extension criteria, compact-support witnesses, and equivalent conditions for canonical inclusions between different exponents.

*Quoted from the card [LeanPool/projects/free-banach-lattice-order-continuity.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/free-banach-lattice-order-continuity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [307e3125](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FBLOrderContinuousLH.intro_infty`](https://leanpool.github.io/lean-pool/LeanPool/FBLOrderContinuity/Order.html#FBLOrderContinuousLH.intro_infty) (theorem; a main declaration), declared in [LeanPool/FBLOrderContinuity/Order.lean, line 1834](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity/Order.lean#L1834): “At exponent infinity, the induced lattice homomorphism is order continuous exactly when the original bounded operator is zero or an isomorphic embedding.” Its source, as the card gives it: “Theorem 1.1. The public manuscript was submitted on 2026-10-30 at 23:06:06 UTC; the completed Lean sources were committed earlier that evening as 167b82ad69724d2ddb2a701fc932e52d445faecc.”
- [`FBLOrderContinuousLH.intro_poe`](https://leanpool.github.io/lean-pool/LeanPool/FBLOrderContinuity/Extension.html#FBLOrderContinuousLH.intro_poe) (theorem; a main declaration), declared in [LeanPool/FBLOrderContinuity/Extension.lean, line 767](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity/Extension.lean#L767): “For a finite exponent p, the induced homomorphism is order continuous exactly when the original operator is zero or is an isomorphic embedding whose range has the POE-p operator-extension property. Equivalently, the induced homomorphism is zero or an isomorphic lattice embedding.” Its source, as the card gives it: “Theorem 1.3.”
- [`FBLOrderContinuousLH.cross_parameter_inclusion`](https://leanpool.github.io/lean-pool/LeanPool/FBLOrderContinuity/Parameters.html#FBLOrderContinuousLH.cross_parameter_inclusion) (theorem; a main declaration), declared in [LeanPool/FBLOrderContinuity/Parameters.lean, line 173](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity/Parameters.lean#L173): “For p less than q, eight conditions on the canonical inclusion between the free p-convex and q-convex lattices are equivalent, including order continuity, surjectivity, equivalence of norms on the algebraic core, and order density.” Its source, as the card gives it: “Theorem 5.1.”
- [`FBLOrderContinuousLH.cross_parameter_above_two`](https://leanpool.github.io/lean-pool/LeanPool/FBLOrderContinuity/Parameters.html#FBLOrderContinuousLH.cross_parameter_above_two) (theorem), declared in [LeanPool/FBLOrderContinuity/Parameters.lean, line 465](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity/Parameters.lean#L465): “When p is less than q and q exceeds two, these conditions hold exactly when the generating Banach space is finite dimensional.” Its source, as the card gives it: “Corollary 5.3.”
- [`FBLOrderContinuousLH.cross_parameter_hilbert`](https://leanpool.github.io/lean-pool/LeanPool/FBLOrderContinuity/Parameters.html#FBLOrderContinuousLH.cross_parameter_hilbert) (theorem), declared in [LeanPool/FBLOrderContinuity/Parameters.lean, line 500](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity/Parameters.lean#L500): “For the real Hilbert sequence space and one at most p less than q at most two, the canonical inclusion is an order-continuous bounded lattice isomorphism onto its target.” Its source, as the card gives it: “Remark 5.4.”

## Project

- Authors: Raúl E. Pariente-Martín, Pedro Tradacete, David Muñoz-Lahoz.
- Source: *Order continuity of induced homomorphisms between free Banach lattices* by Raúl E. Pariente-Martín, Pedro Tradacete, [arXiv:2611.00451](https://arxiv.org/abs/2611.00451).
- Project repository: [pedrotradacete/FBLOrderContinuousLH](https://github.com/pedrotradacete/FBLOrderContinuousLH), at commit [ee3cde50](https://github.com/pedrotradacete/FBLOrderContinuousLH/tree/ee3cde5070125ff2356b7144ff7a940a8dff2a54).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46B42, 46A40, 47B60.
- In Lean Pool: [LeanPool/FBLOrderContinuity](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity), from the card [LeanPool/projects/free-banach-lattice-order-continuity.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/free-banach-lattice-order-continuity.yaml).

## Sources

- [Lean Pool at 307e3125: LeanPool/projects/free-banach-lattice-order-continuity.yaml](https://github.com/LeanPool/lean-pool/blob/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/projects/free-banach-lattice-order-continuity.yaml)
- [Lean Pool at 307e3125: LeanPool/FBLOrderContinuity](https://github.com/LeanPool/lean-pool/tree/307e31252a8b55092789f868afe6238397a6b50c/LeanPool/FBLOrderContinuity)
