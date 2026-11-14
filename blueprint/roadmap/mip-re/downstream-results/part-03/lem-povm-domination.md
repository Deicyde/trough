---
declaration: lemma
origin: cited
lean: MIPRE.ValueModel.DominatesPOVM.dominates, MIPRE.ValueModel.tensor_dominatesPOVM, MIPRE.ValueModel.commuting_dominatesPOVM, MIPRE.ValueModel.tensor_projApprox, MIPRE.ValueModel.commuting_projApprox, MIPRE.povmValue_le_quantumValue
statement: formalized
proof: formalized
---

# Domination and approximation in the two models

A value model dominating the POVM strategies of a model dominates its projective strategies. $\mathrm{val}^*$ dominates the POVM strategies of the tensor-product model of every unit vector, and ${\omega^{\mathrm{co}}}$ those of every model on a Hilbert space with a unit state; both are approached by projective strategies.

## Depends on

- [Domination of the POVM strategies, and approximation by projective strategies](def-povm-domination.md)
- [Projective strategies in the two models](lem-model-proj-strategy-values.md)
- [The commuting-operator value is a supremum of model values](../part-02/lem-co-value-model.md)

## Proof depends on

- [Combined $XZ$ point measurements](../../background-results/part-02/lem-qld-combined-points.md)

## Proof

In the tensor-product model, the Naimark dilation of each party's measurements makes the strategy projective on registers extended by the answer sets, at the same value. In a model on a Hilbert space a POVM strategy is a commuting-operator strategy. The approximations are Lemma [Projective strategies in the two models](lem-model-proj-strategy-values.md).

## Lean

Formalized as [`MIPRE.ValueModel.DominatesPOVM.dominates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.DominatesPOVM.dominates), [`MIPRE.ValueModel.tensor_dominatesPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.tensor_dominatesPOVM), [`MIPRE.ValueModel.commuting_dominatesPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.commuting_dominatesPOVM), [`MIPRE.ValueModel.tensor_projApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.tensor_projApprox), [`MIPRE.ValueModel.commuting_projApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.commuting_projApprox), [`MIPRE.povmValue_le_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.povmValue_le_quantumValue).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2003](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2003)
