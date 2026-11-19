---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.Iso, MIPRE.BipartiteModel.Iso.refl, MIPRE.BipartiteModel.Iso.symm, MIPRE.BipartiteModel.Iso.trans, MIPRE.BipartiteModel.Iso.swap, MIPRE.BipartiteModel.Iso.toLocalIsometry, MIPRE.BipartiteModel.Iso.ofLocalIsometry
statement: formalized
---

# Isomorphisms of bipartite models

An *isomorphism* of bipartite models from $M$ to $M'$ is a unitary $W$ of their Hilbert spaces carrying the state of $M$ to the state of $M'$, with a $*$-algebra isomorphism $\Phi_A$ of the first player's algebra of $M$ onto that of $M'$ and one $\Phi_B$ for the second player, the two representations intertwined by $W$ as in Definition [Local isometries of bipartite models](../part-03/def-local-isometry.md). Isomorphisms have identities, compose, invert and exchange with the players. An isomorphism is a local isometry whose homomorphisms are unital and whose isometry carries the state to the state; conversely, a local isometry carrying the state to the state, whose isometry has a right inverse and whose homomorphisms have two-sided inverses, is an isomorphism.

## Depends on

- [Local isometries of bipartite models](../part-03/def-local-isometry.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.Iso`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso), [`MIPRE.BipartiteModel.Iso.refl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.refl), [`MIPRE.BipartiteModel.Iso.symm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.symm), [`MIPRE.BipartiteModel.Iso.trans`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.trans), [`MIPRE.BipartiteModel.Iso.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.swap), [`MIPRE.BipartiteModel.Iso.toLocalIsometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.toLocalIsometry), [`MIPRE.BipartiteModel.Iso.ofLocalIsometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.Iso.ofLocalIsometry).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2190](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2190)
