---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.tensorExpand, MIPRE.BipartiteModel.tensorExpand_W_ψ, MIPRE.BipartiteModel.tensorUnexpand, MIPRE.BipartiteModel.tensorUnexpand_W_ψ, MIPRE.BipartiteModel.tensorUnexpand_ΦA, MIPRE.BipartiteModel.tensorUnexpand_ΦB, MIPRE.BipartiteModel.tensorIsometry, MIPRE.BipartiteModel.tensorIsometry_W, MIPRE.BipartiteModel.compSymmHom, MIPRE.BipartiteModel.compSymmHom_kronecker_one
statement: formalized
proof: formalized
---

# The ancilla extension of a tensor-product model

The ancilla extension of the tensor-product model of $\xi$ by registers in the vector $e$ is, along unital local isometries in both directions carrying the state to the state, the tensor-product model of the expanded vector $e \otimes \xi$; and a pair of isometries $V_A, V_B$ is a local isometry between tensor-product models, $X \mapsto V_A X V_A^\dagger$ for the first player.

## Depends on

- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)
- [Local isometries of bipartite models](def-local-isometry.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)

## Proof depends on

- [Moving registers along local isometries](lem-ancilla-isometries.md)

## Proof

The $\ell^2$-sum of copies of $\mathbb{C}^{d_A \times d_B}$ is $\mathbb{C}^{(\alpha \times d_A) \times (\beta \times d_B)}$, and block matrices of matrices are matrices on the products of the indices.

## Lean

Formalized as [`MIPRE.BipartiteModel.tensorExpand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorExpand), [`MIPRE.BipartiteModel.tensorExpand_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorExpand_W_ψ), [`MIPRE.BipartiteModel.tensorUnexpand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorUnexpand), [`MIPRE.BipartiteModel.tensorUnexpand_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorUnexpand_W_ψ), [`MIPRE.BipartiteModel.tensorUnexpand_ΦA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorUnexpand_ΦA), [`MIPRE.BipartiteModel.tensorUnexpand_ΦB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorUnexpand_ΦB), [`MIPRE.BipartiteModel.tensorIsometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorIsometry), [`MIPRE.BipartiteModel.tensorIsometry_W`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.tensorIsometry_W), [`MIPRE.BipartiteModel.compSymmHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.compSymmHom), [`MIPRE.BipartiteModel.compSymmHom_kronecker_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.compSymmHom_kronecker_one).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1914](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1914)
