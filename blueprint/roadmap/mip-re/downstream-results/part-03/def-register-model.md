---
declaration: definition
origin: cited
lean: MIPRE.Introspection.registerEPR, MIPRE.BipartiteModel.reg, MIPRE.BipartiteModel.regRelabel, MIPRE.BipartiteModel.regSplit, MIPRE.BipartiteModel.regExtend, MIPRE.BipartiteModel.regSwap, MIPRE.Introspection.regSplitHom, MIPRE.Introspection.regExtendHom
statement: formalized
---

# The register model

The *register model* of a bipartite model $N$ on a finite register $I$ is its ancilla extension by the maximally entangled vector $|\mathrm{EPR}_I\rangle$: each player holds a copy of $I$, and the state is $|\mathrm{EPR}_I\rangle \otimes \psi_N$. In the tensor-product model of a vector $\xi$ it is the tensor-product model of the register state $|\mathrm{EPR}_I\rangle \otimes |\xi\rangle$. Relabelling the register, splitting it as a product, extending it by a spectator factor and exchanging the players are local isometries between register models.

## Depends on

- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)
- [Local isometries of bipartite models](def-local-isometry.md)
- [Moving registers along local isometries](lem-ancilla-isometries.md)

## Lean

Formalized as [`MIPRE.Introspection.registerEPR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.registerEPR), [`MIPRE.BipartiteModel.reg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.reg), [`MIPRE.BipartiteModel.regRelabel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regRelabel), [`MIPRE.BipartiteModel.regSplit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regSplit), [`MIPRE.BipartiteModel.regExtend`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regExtend), [`MIPRE.BipartiteModel.regSwap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.regSwap), [`MIPRE.Introspection.regSplitHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.regSplitHom), [`MIPRE.Introspection.regExtendHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.regExtendHom).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1873](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1873)
