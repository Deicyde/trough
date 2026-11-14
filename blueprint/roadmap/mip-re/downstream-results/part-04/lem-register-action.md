---
declaration: lemma
origin: cited
lean: MIPRE.OperatorMatrix.regActHom, MIPRE.OperatorMatrix.regAct, MIPRE.OperatorMatrix.regActHom_apply, MIPRE.OperatorMatrix.regAct_eq_toCLM, MIPRE.OperatorMatrix.regAct_mul, MIPRE.OperatorMatrix.regAct_one, MIPRE.OperatorMatrix.regAct_conjTranspose, MIPRE.OperatorMatrix.regAct_add, MIPRE.OperatorMatrix.regAct_smul, MIPRE.OperatorMatrix.regAct_sum, MIPRE.OperatorMatrix.isStarProjection_regAct, MIPRE.OperatorMatrix.regAct_apply, MIPRE.OperatorMatrix.regAct_toLp_smul, MIPRE.OperatorMatrix.regAct_vecMulVec, MIPRE.OperatorMatrix.norm_toLp_smul, MIPRE.BipartiteModel.expand_π_πA_smulKron_one, MIPRE.BipartiteModel.expand_π_πB_smulKron_one, MIPRE.BipartiteModel.expand_π_smulKron_one_mul
statement: formalized
proof: formalized
---

# Scalar matrices on a register, and the contraction against a vector

Let $\iota$ be a finite register and $\mathcal{H}$ a Hilbert space. A matrix $R \in M_\iota(\mathbb{C})$ acts on $\mathcal{H} \otimes \mathbb{C}^\iota$ as $R \otimes {I}_\mathcal{H}$, and $R \mapsto R \otimes {I}_\mathcal{H}$ is a unital $*$-homomorphism, under which a self-adjoint idempotent acts as an orthogonal projection. On a product vector $\xi \otimes e$ it acts on the register alone, as $\xi \otimes Re$, and $\|\xi \otimes e\| = \|\xi\|\,\|e\|$. The rank-one matrix $(e_i f_j)_{ij}$ sends a vector $\theta$, with components $\theta_j \in \mathcal{H}$, to the product vector $(\sum_j f_j \theta_j) \otimes e$. At the maximally entangled vector of a pair of registers this is the contraction of the swap isometry of the Pauli basis test: the range of $|\textsc{EPR}\rangle\langle\textsc{EPR}| \otimes {I}$ is the set of products of $|\textsc{EPR}\rangle$ with a vector of $\mathcal{H}$, and the contraction is that vector. In the extension of a bipartite model in a vector, a scalar matrix $P$ on the first player's register times a scalar matrix $Q$ on the second player's acts as the register matrix $P \otimes Q$, whatever the model.

## Depends on

- [Commutation-preserving dilation](../part-02/lem-co-dilation.md)
- [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)

## Proof

The action is the entrywise inclusion of the scalars followed by the action of operator matrices (Lemma [Commutation-preserving dilation](../part-02/lem-co-dilation.md)), a composite of unital $*$-homomorphisms. The formulas are the matrix product in the register's coordinates, and in an extension both players' scalar matrices act on the copies of the Hilbert space alone.

## Lean

Formalized as [`MIPRE.OperatorMatrix.regActHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regActHom), [`MIPRE.OperatorMatrix.regAct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct), [`MIPRE.OperatorMatrix.regActHom_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regActHom_apply), [`MIPRE.OperatorMatrix.regAct_eq_toCLM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_eq_toCLM), [`MIPRE.OperatorMatrix.regAct_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_mul), [`MIPRE.OperatorMatrix.regAct_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_one), [`MIPRE.OperatorMatrix.regAct_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_conjTranspose), [`MIPRE.OperatorMatrix.regAct_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_add), [`MIPRE.OperatorMatrix.regAct_smul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_smul), [`MIPRE.OperatorMatrix.regAct_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_sum), [`MIPRE.OperatorMatrix.isStarProjection_regAct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.isStarProjection_regAct), [`MIPRE.OperatorMatrix.regAct_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_apply), [`MIPRE.OperatorMatrix.regAct_toLp_smul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_toLp_smul), [`MIPRE.OperatorMatrix.regAct_vecMulVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.regAct_vecMulVec), [`MIPRE.OperatorMatrix.norm_toLp_smul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.norm_toLp_smul), [`MIPRE.BipartiteModel.expand_π_πA_smulKron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expand_π_πA_smulKron_one), [`MIPRE.BipartiteModel.expand_π_πB_smulKron_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expand_π_πB_smulKron_one), [`MIPRE.BipartiteModel.expand_π_smulKron_one_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.expand_π_smulKron_one_mul).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2618](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2618)
