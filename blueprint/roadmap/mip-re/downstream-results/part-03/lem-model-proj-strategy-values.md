---
declaration: lemma
origin: cited
lean: MIPRE.TensorProductStrategy.toModel, MIPRE.TensorProductStrategy.value_toModel, MIPRE.TensorProductStrategy.failAt_toModel, MIPRE.star_dotProduct_self_eq_one, MIPRE.BipartiteModel.ProjStrat.toTensor, MIPRE.BipartiteModel.ProjStrat.value_toTensor, MIPRE.BipartiteModel.ProjStrat.value_le_commutingOperatorValue, MIPRE.exists_projStrat_lt_commutingOperatorValue, MIPRE.ValueModel.tensor_dominates, MIPRE.ValueModel.commuting_dominates, MIPRE.inconsistency_eq_tensor
statement: formalized
proof: formalized
---

# Projective strategies in the two models

A tensor-product strategy is a projective strategy in its tensor-product model, of the same value and the same conditional failures, and conversely a projective strategy in the tensor-product model of a state on $\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}$ is a tensor-product strategy of the same value, so $\mathrm{val}^*$ dominates that model. The value of a projective strategy in a model on a Hilbert space is at most ${\omega^{\mathrm{co}}}$, so ${\omega^{\mathrm{co}}}$ dominates every such model, and for every $t \geq 0$ with $t < {\omega^{\mathrm{co}}}(\mathfrak{G})$ there is a commuting-operator strategy with a projective strategy of value greater than $t$ in its model. The matrix inconsistency of Definition [Inconsistency](../../foundations/part-02/def-inconsistency.md) is the inconsistency in the tensor-product model.

## Depends on

- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)
- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](../part-02/lem-model-strategy-co.md)
- [Value models](../part-01/def-value-model.md)
- [Inconsistency](../../foundations/part-02/def-inconsistency.md)

## Proof

The measurements of a tensor-product strategy are projective, the matrix algebras are the players' algebras of its model and the value is computed by the same Born rule. For ${\omega^{\mathrm{co}}}$, both statements are Lemma [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](../part-02/lem-model-strategy-co.md).

## Lean

Formalized as [`MIPRE.TensorProductStrategy.toModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.toModel), [`MIPRE.TensorProductStrategy.value_toModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.value_toModel), [`MIPRE.TensorProductStrategy.failAt_toModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.failAt_toModel), [`MIPRE.star_dotProduct_self_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.star_dotProduct_self_eq_one), [`MIPRE.BipartiteModel.ProjStrat.toTensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.toTensor), [`MIPRE.BipartiteModel.ProjStrat.value_toTensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.value_toTensor), [`MIPRE.BipartiteModel.ProjStrat.value_le_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.value_le_commutingOperatorValue), [`MIPRE.exists_projStrat_lt_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_projStrat_lt_commutingOperatorValue), [`MIPRE.ValueModel.tensor_dominates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.tensor_dominates), [`MIPRE.ValueModel.commuting_dominates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.commuting_dominates), [`MIPRE.inconsistency_eq_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.inconsistency_eq_tensor).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1653](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1653)
