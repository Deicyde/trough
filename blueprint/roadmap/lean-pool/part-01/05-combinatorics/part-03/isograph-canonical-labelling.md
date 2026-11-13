---
declaration: theorem
origin: cited
lean: IsoGraph.Canon.canonAdj_eq_iff, IsoGraph.Canon.canonAdj_relabel
statement: formalized
proof: formalized
---

# Verified canonical labelling of finite graphs

> Implements an individualisation-refinement canonical-labelling algorithm in the style of nauty and proves that its canonical adjacency form is invariant under vertex relabelling and classifies finite graphs up to isomorphism. The imported core includes the executable search, refinement, orbit-pruning and backjumping machinery together with its equivariance, termination, soundness and optimality proofs.

*Quoted from the card [LeanPool/projects/isograph-canonical-labelling.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/isograph-canonical-labelling.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`IsoGraph.Canon.canonAdj_eq_iff`](https://leanpool.github.io/lean-pool/LeanPool/IsoGraph/Canon/Spec.html#IsoGraph.Canon.canonAdj_eq_iff) (theorem; a main declaration), declared in [LeanPool/IsoGraph/Canon/Spec.lean, line 464](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsoGraph/Canon/Spec.lean#L464): “Two Boolean adjacency functions on Fin n have equal canonical forms exactly when one is a relabelling of the other by a vertex permutation.”
- [`IsoGraph.Canon.canonAdj_relabel`](https://leanpool.github.io/lean-pool/LeanPool/IsoGraph/Canon/Spec.html#IsoGraph.Canon.canonAdj_relabel) (theorem; a main declaration), declared in [LeanPool/IsoGraph/Canon/Spec.lean, line 430](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsoGraph/Canon/Spec.lean#L430): “Relabelling a finite graph by any permutation leaves its canonical adjacency form unchanged.”
- [`IsoGraph.Canon.exists_relabel_of_canonAdj_eq`](https://leanpool.github.io/lean-pool/LeanPool/IsoGraph/Canon/Spec.html#IsoGraph.Canon.exists_relabel_of_canonAdj_eq) (theorem), declared in [LeanPool/IsoGraph/Canon/Spec.lean, line 264](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsoGraph/Canon/Spec.lean#L264): “Equality of canonical adjacency forms yields an explicit permutation relating the original adjacency functions.”

## Project

- Authors: Alex Meiburg.
- Source: *IsoGraph* by Alex Meiburg.
- Project repository: [Timeroot/IsoGraph](https://github.com/Timeroot/IsoGraph), at commit [bbfcefd1](https://github.com/Timeroot/IsoGraph/tree/bbfcefd15087d1dcb63ebdad015a087e1d6890a1).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 05C60, 68R10.
- In Lean Pool: [LeanPool/IsoGraph](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsoGraph), from the card [LeanPool/projects/isograph-canonical-labelling.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/isograph-canonical-labelling.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/isograph-canonical-labelling.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/isograph-canonical-labelling.yaml)
- [Lean Pool at 701389c0: LeanPool/IsoGraph](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/IsoGraph)
