---
declaration: theorem
origin: cited
lean: MIPRE.Halting.mipco_eq_core_of, MIPRE.Halting.core_subset_mipco_of, MIPRE.Halting.core_subset_mipclass_of_reduction, MIPRE.Halting.mipclass_eq_core_of_reduction
statement: formalized
proof: formalized
---

# $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from co-soundness

Assume a gap compression is sound in the model ${\omega^{\mathrm{co}}}$. Then $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, for the class of Definition [The class $\mathrm{MIP}^{\mathrm{co}}$](../part-01/def-mipco.md). The inclusion $\mathrm{MIP}^{\mathrm{co}} \subseteq \mathrm{coRE}$ holds without the hypothesis. More generally $\mathrm{MIP}(\omega) = \mathrm{coRE}$ for every value model $\omega$ that is r.e. from above and has a halting reduction of $\mathrm{coRE}$ shape.

## Depends on

- [Halting reduces to the commuting-operator value, from co-soundness](thm-halting-co.md)
- [$\mathrm{MIP}^{\mathrm{co}} \subseteq \mathrm{coRE}$](../part-01/lem-mipco-sub-core.md)
- [The class $\mathrm{MIP}^{\mathrm{co}}$](../part-01/def-mipco.md)
- [Co-recursively enumerable](../part-01/def-core.md)
- [Turing](../../background-results/part-03/thm-halting-undecidable.md)
- [Value models](../part-01/def-value-model.md)

## Proof

$\mathrm{MIP}(\omega) \subseteq \mathrm{coRE}$ is Lemma [$\mathrm{MIP}^{\mathrm{co}} \subseteq \mathrm{coRE}$](../part-01/lem-mipco-sub-core.md). For the converse, the complement of a co-r.e. language many-one reduces to halting on the empty input (Theorem [Turing](../../background-results/part-03/thm-halting-undecidable.md); in Lean `MIPRE.Halting.exists_code_halts_of_isRE`, applied to the complement), and composing with the map of Theorem [Halting reduces to the commuting-operator value, from co-soundness](thm-halting-co.md) sends the members of $L$, whose machines do not halt, to games of value $1$ and the non-members to games of value at most $\frac12$. This is the argument of Theorem [$\mathrm{MIP}^* = \mathrm{RE}$](../../the-main-theorem/thm-mipstar-eq-re.md) with the two verdicts exchanged, and in Lean the two are the same theorem in the two shapes.

## Lean

Formalized as [`MIPRE.Halting.mipco_eq_core_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipco_eq_core_of), [`MIPRE.Halting.core_subset_mipco_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.core_subset_mipco_of), [`MIPRE.Halting.core_subset_mipclass_of_reduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.core_subset_mipclass_of_reduction), [`MIPRE.Halting.mipclass_eq_core_of_reduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.mipclass_eq_core_of_reduction).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 955](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L955)
