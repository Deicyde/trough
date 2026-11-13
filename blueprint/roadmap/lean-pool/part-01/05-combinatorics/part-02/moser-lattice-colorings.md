---
declaration: theorem
origin: cited
lean: LeanPool.MoserLatticeColorings.MoserRing.both_colorings_are_geometric
statement: formalized
proof: formalized
---

# Geometric Four-Colorings of the Moser Lattice and Ring

> Formalizes the two explicit parity colorings from Dúcz's 2026 note on the Moser lattice. The development derives the exact quadratic norm formula, proves that the integer-coordinate embedding is faithful, proves both colorings proper and geometric on the entire lattice, and descends them through localization by powers of three to the Moser ring. As a structural corollary, every unit-distance graph realized entirely in the Moser ring is four-colorable. The uniqueness classification of geometric four-colorings and the chromatic number of the full Euclidean plane are not claimed.

*Quoted from the card [LeanPool/projects/moser-lattice-colorings.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/moser-lattice-colorings.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.MoserLatticeColorings.MoserRing.both_colorings_are_geometric`](https://leanpool.github.io/lean-pool/LeanPool/MoserLatticeColorings/Ring.html#LeanPool.MoserLatticeColorings.MoserRing.both_colorings_are_geometric) (theorem; a main declaration), declared in [LeanPool/MoserLatticeColorings/Ring.lean, line 392](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MoserLatticeColorings/Ring.lean#L392): “The two parity maps defined by Dúcz descend to proper four-colorings of the full Moser ring, and equality of colors for each map depends only on Euclidean distance.” Its source, as the card gives it: “Theorem 3.1 and the Moser-ring extension following it.”
- [`LeanPool.MoserLatticeColorings.MoserRing.graph_colorable_four_of_moserRing_realization`](https://leanpool.github.io/lean-pool/LeanPool/MoserLatticeColorings/Ring.html#LeanPool.MoserLatticeColorings.MoserRing.graph_colorable_four_of_moserRing_realization) (theorem), declared in [LeanPool/MoserLatticeColorings/Ring.lean, line 402](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MoserLatticeColorings/Ring.lean#L402): “Every abstract graph with a realization in the Moser ring that sends each edge to a unit-distance pair is four-colorable.” Its source, as the card gives it: “Corollary of the geometric four-coloring of the Moser ring.”

## Project

- Authors: Egor Lyfar.
- Source: *A note on geometric colorings of the Moser lattice* by Ákos Dúcz, [arXiv:2606.12325](https://arxiv.org/abs/2606.12325).
- Project repository: [lyfar/moser-lattice-colorings-lean](https://github.com/lyfar/moser-lattice-colorings-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C15.
- In Lean Pool: [LeanPool/MoserLatticeColorings](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MoserLatticeColorings), from the card [LeanPool/projects/moser-lattice-colorings.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/moser-lattice-colorings.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/moser-lattice-colorings.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/moser-lattice-colorings.yaml)
- [Lean Pool at 701389c0: LeanPool/MoserLatticeColorings](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/MoserLatticeColorings)
