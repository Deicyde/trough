---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.inert, MIPRE.BipartiteModel.inert_W_ψ, MIPRE.BipartiteModel.relabel, MIPRE.BipartiteModel.relabel_W_ψ, MIPRE.BipartiteModel.assoc, MIPRE.BipartiteModel.assoc_W_ψ, MIPRE.BipartiteModel.swapExpand, MIPRE.BipartiteModel.swapExpand_W_ψ, MIPRE.BipartiteModel.expand_π_πA_apply, MIPRE.BipartiteModel.expand_π_πB_apply
statement: formalized
proof: formalized
---

# Moving registers along local isometries

Adjoining an inert ancilla in a unit vector $e$, relabelling the registers of an ancilla extension along bijections, reading an extension of an extension as the extension by the product registers, and exchanging the players of an extension are local isometries between ancilla extensions of a model that carry the state exactly to the state.

## Depends on

- [Local isometries of bipartite models](def-local-isometry.md)
- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)

## Proof

Each is a permutation of the copies of $\mathcal{H}$ in the $\ell^2$-sums, which acts on the players' operators entrywise.

## Lean

Formalized as [`MIPRE.BipartiteModel.inert`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inert), [`MIPRE.BipartiteModel.inert_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inert_W_ψ), [`MIPRE.BipartiteModel.relabel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.relabel), [`MIPRE.BipartiteModel.relabel_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.relabel_W_ψ), [`MIPRE.BipartiteModel.assoc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.assoc), [`MIPRE.BipartiteModel.assoc_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.assoc_W_ψ), [`MIPRE.BipartiteModel.swapExpand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.swapExpand), [`MIPRE.BipartiteModel.swapExpand_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.swapExpand_W_ψ), [`MIPRE.BipartiteModel.expand_π_πA_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expand_π_πA_apply), [`MIPRE.BipartiteModel.expand_π_πB_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expand_π_πB_apply).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1853](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1853)
