---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.povmValue_le_postprocess, MIPRE.quantumValue_le_postprocess, MIPRE.commutingOperatorValue_le_postprocess, MIPRE.SampledGame.one_sub_povmValue, MIPRE.CL.Detyping.restrict_condFail_eq, MIPRE.CL.Detyping.typed_failure_povm, MIPRE.CL.Detyping.failure_povm, MIPRE.CL.Detyping.restrict_failure_eq_povm, MIPRE.CL.Detyping.restrict_failure_le_povm, MIPRE.CL.Detyping.restrict_povmValue_ge, MIPRE.one_sub_mul_one_sub_iSup_le, MIPRE.CL.Detyping.quantumValue_typedGame_ge, MIPRE.CL.Detyping.commutingOperatorValue_typedGame_ge
statement: formalized
proof: formalized
---

# Post-processing and detyping, in a model

In a bipartite model with a unit state:

1. for two games on the same questions with the same distribution and maps $r_A(x, \cdot)$, $r_B(y, \cdot)$ of the answers under which every accepted tuple of the first stays accepted in the second, the families coarse-grained along $r_A$, $r_B$ have at least the value in the second game that the original families have in the first;
2. in the setting of Lemma [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md), families of value at least $1 - \varepsilon$ in the detyped game, read at the fixed graph views, have value at least $1 - 16^{|T|}\varepsilon$ in the typed game.

Consequently both inequalities hold between the values $\mathrm{val}^*$, and between the values ${\omega^{\mathrm{co}}}$, of the games.

## Depends on

- [Bipartite model](def-bipartite-model.md)
- [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](lem-model-strategy-co.md)
- [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)

## Proof

Item 1: at each question pair the coarse-grained families accept a superset of the outcome pairs, with the same Born probabilities summed over the fibres. Item 2 is the proof of Lemma [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md), which uses of a strategy only its conditional failures, their nonnegativity and the averaging identity of a sampled game, all of which hold for families in a model. For the values, apply each item in the model of every strategy of the first game and take the supremum; for item 2 the transfer is affine, $v \mapsto 1 - 16^{|T|}(1 - v)$, and passes to the supremum. In ${\omega^{\mathrm{co}}}$ the model is the strategy's own and the output families are a commuting-operator strategy (Lemma [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](lem-model-strategy-co.md)).

## Lean

Formalized as [`MIPRE.BipartiteModel.povmValue_le_postprocess`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.povmValue_le_postprocess), [`MIPRE.quantumValue_le_postprocess`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quantumValue_le_postprocess), [`MIPRE.commutingOperatorValue_le_postprocess`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingOperatorValue_le_postprocess), [`MIPRE.SampledGame.one_sub_povmValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SampledGame.one_sub_povmValue), [`MIPRE.CL.Detyping.restrict_condFail_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_condFail_eq), [`MIPRE.CL.Detyping.typed_failure_povm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.typed_failure_povm), [`MIPRE.CL.Detyping.failure_povm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.failure_povm), [`MIPRE.CL.Detyping.restrict_failure_eq_povm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_failure_eq_povm), [`MIPRE.CL.Detyping.restrict_failure_le_povm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_failure_le_povm), [`MIPRE.CL.Detyping.restrict_povmValue_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_povmValue_ge), [`MIPRE.one_sub_mul_one_sub_iSup_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.one_sub_mul_one_sub_iSup_le), [`MIPRE.CL.Detyping.quantumValue_typedGame_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.quantumValue_typedGame_ge), [`MIPRE.CL.Detyping.commutingOperatorValue_typedGame_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.commutingOperatorValue_typedGame_ge).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1500](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1500)
