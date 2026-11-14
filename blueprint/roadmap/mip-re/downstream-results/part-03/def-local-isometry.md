---
declaration: definition
origin: cited
lean: MIPRE.BipartiteModel.LocalIsometry, MIPRE.BipartiteModel.withState, MIPRE.StateModel.withState, MIPRE.BipartiteModel.LocalIsometry.comp, MIPRE.BipartiteModel.LocalIsometry.swap, MIPRE.BipartiteModel.LocalIsometry.transportOpA, MIPRE.BipartiteModel.LocalIsometry.transportA, MIPRE.BipartiteModel.LocalIsometry.transportB, MIPRE.POVMIn.pushforward, MIPRE.IsPVMIn.toPOVMIn
statement: formalized
---

# Local isometries of bipartite models

A *local isometry* from a bipartite model $M$ to a bipartite model $M'$ is a linear isometry $W$ of their Hilbert spaces with, for each player, a non-unital $*$-homomorphism $\Phi$ of the player's algebra of $M$ into that of $M'$, such that $W$ intertwines the two representations: $\pi'(\pi'_A(\Phi_A(a)))\, W = W\, \pi(\pi_A(a))$, and likewise for the second player. In the tensor-product model, $X \mapsto V_A X V_A^\dagger$ for an isometry $V_A$ is such a $\Phi_A$, not unital since $\Phi_A({I}) = V_A V_A^\dagger$. Local isometries compose and exchange with the players. A projective measurement $\{P_a\}$ of the first player is *transported* to the projective measurement $\{\Phi_A(P_a) + [a = a_0]({I} - \Phi_A({I}))\}$ of $M'$, the complement of the image added at one fixed outcome $a_0$, and likewise for the second player. The model $M$ with its state replaced by a vector $v$ of its Hilbert space is written $M^{v}$.

## Depends on

- [Bipartite model](../part-02/def-bipartite-model.md)

## Lean

Formalized as [`MIPRE.BipartiteModel.LocalIsometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry), [`MIPRE.BipartiteModel.withState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.withState), [`MIPRE.StateModel.withState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.withState), [`MIPRE.BipartiteModel.LocalIsometry.comp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.comp), [`MIPRE.BipartiteModel.LocalIsometry.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.swap), [`MIPRE.BipartiteModel.LocalIsometry.transportOpA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.transportOpA), [`MIPRE.BipartiteModel.LocalIsometry.transportA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.transportA), [`MIPRE.BipartiteModel.LocalIsometry.transportB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.transportB), [`MIPRE.POVMIn.pushforward`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.pushforward), [`MIPRE.IsPVMIn.toPOVMIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVMIn.toPOVMIn).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1798](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1798)
