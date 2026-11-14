---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.ProjStrat.failAt_nonneg, MIPRE.BipartiteModel.ProjStrat.failAt_le_one, MIPRE.BipartiteModel.ProjStrat.one_sub_value_eq_sum_failAt, MIPRE.BipartiteModel.ProjStrat.value_le_one, MIPRE.BipartiteModel.ProjStrat.value_nonneg, MIPRE.BipartiteModel.ProjStrat.failAt_adapt_le, MIPRE.BipartiteModel.ProjStrat.value_relabel, MIPRE.BipartiteModel.povmValue_congr_game, MIPRE.POVMIn.map_map, MIPRE.POVMIn.map_id, MIPRE.BipartiteModel.inconsistency_eq_sum_dis, MIPRE.BipartiteModel.inconsistency_uniform, MIPRE.BipartiteModel.sum_dis_le_of_inconsistency, MIPRE.BipartiteModel.inconsistency_uniform_unit, MIPRE.POVMIn.toPOVM_toIn, MIPRE.POVM.toIn_map
statement: formalized
proof: formalized
---

# Operations on projective strategies

The failure of a projective strategy is the average of its conditional failures, each in $[0, 1]$; its value is in $[0, 1]$; played through maps under which every accepted tuple stays accepted, it fails no more often at each question pair; relabelled along equivalences carrying one game onto the other, it keeps its value. On a uniform index the inconsistency is the average disagreement of the two families.

## Depends on

- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)

## Proof depends on

- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)

## Proof

Each statement is its matrix counterpart for tensor-product strategies, whose proof uses of a strategy only its Born probabilities, their nonnegativity and their normalization, which hold in the model (Lemma [Strategies in a model, read in ${\omega^{\mathrm{co}}}$](../part-02/lem-model-strategy-co.md)).

## Lean

Formalized as [`MIPRE.BipartiteModel.ProjStrat.failAt_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.failAt_nonneg), [`MIPRE.BipartiteModel.ProjStrat.failAt_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.failAt_le_one), [`MIPRE.BipartiteModel.ProjStrat.one_sub_value_eq_sum_failAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.one_sub_value_eq_sum_failAt), [`MIPRE.BipartiteModel.ProjStrat.value_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.value_le_one), [`MIPRE.BipartiteModel.ProjStrat.value_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.value_nonneg), [`MIPRE.BipartiteModel.ProjStrat.failAt_adapt_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.failAt_adapt_le), [`MIPRE.BipartiteModel.ProjStrat.value_relabel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.ProjStrat.value_relabel), [`MIPRE.BipartiteModel.povmValue_congr_game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.povmValue_congr_game), [`MIPRE.POVMIn.map_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.map_map), [`MIPRE.POVMIn.map_id`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.map_id), [`MIPRE.BipartiteModel.inconsistency_eq_sum_dis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inconsistency_eq_sum_dis), [`MIPRE.BipartiteModel.inconsistency_uniform`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inconsistency_uniform), [`MIPRE.BipartiteModel.sum_dis_le_of_inconsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_dis_le_of_inconsistency), [`MIPRE.BipartiteModel.inconsistency_uniform_unit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.inconsistency_uniform_unit), [`MIPRE.POVMIn.toPOVM_toIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.toPOVM_toIn), [`MIPRE.POVM.toIn_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.toIn_map).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1625](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1625)
