---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.expandA, MIPRE.BipartiteModel.inertA, MIPRE.BipartiteModel.LocalIsometry.expand, MIPRE.BipartiteModel.LocalIsometry.expandA, MIPRE.BipartiteModel.layerSwap, MIPRE.BipartiteModel.exchange
statement: formalized
---

# The one-sided ancilla extension

The *one-sided extension* of a bipartite model $M$ by a finite register $T$ in a basis state $t_0$ adjoins $T$ to the first player only: the first player's algebra becomes $M_T({\mathscr{A}}_A)$, the second player's is unchanged, and the state is $\psi \otimes e_{t_0}$. The inert embedding of $M$ into it carries $a$ to $a \otimes {I}$. Local isometries extend along registers, and extending a register model on one side is, up to exchanging the two layers of block matrices, the register model of the extension.

## Depends on

- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)
- [Local isometries of bipartite models](def-local-isometry.md)
- [Moving registers along local isometries](lem-ancilla-isometries.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expandA), [`MIPRE.BipartiteModel.inertA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inertA), [`MIPRE.BipartiteModel.LocalIsometry.expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.expand), [`MIPRE.BipartiteModel.LocalIsometry.expandA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.expandA), [`MIPRE.BipartiteModel.layerSwap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.layerSwap), [`MIPRE.BipartiteModel.exchange`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.exchange).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1936](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1936)
