---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.valΩ, MIPRE.Tailored.Sofic.Measure.Good, MIPRE.Tailored.Sofic.Measure.wordEval, MIPRE.Tailored.Sofic.Measure.evW, MIPRE.Tailored.Sofic.Measure.conjW, MIPRE.Tailored.Sofic.Measure.toSub, MIPRE.Tailored.Sofic.Measure.irs_of_good, MIPRE.Tailored.Sofic.Measure.valOn_eq_valΩ
statement: formalized
proof: formalized
---

# From word indicators to invariant random subgroups

Index the indicator of a subgroup by words rather than group elements. A probability measure on word indicators carried by the indicators that respect free reduction and the subgroup axioms, and invariant under conjugation by each letter, is the image of an IRS with the same value against every test.

## Depends on

- [The value of a measure, and the ergodic value; I:486–499](../part-01/def-erg-value.md)
- [The associated subgroup test; I:2086](../part-01/def-assoc-test.md)

## Proof

The good indicators are the complement of a countable union of clopen sets, and on them evaluation at a reduced word is a subgroup indicator; push forward and check invariance on generators.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.valΩ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.valΩ), [`MIPRE.Tailored.Sofic.Measure.Good`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.Good), [`MIPRE.Tailored.Sofic.Measure.wordEval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.wordEval), [`MIPRE.Tailored.Sofic.Measure.evW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.evW), [`MIPRE.Tailored.Sofic.Measure.conjW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.conjW), [`MIPRE.Tailored.Sofic.Measure.toSub`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.toSub), [`MIPRE.Tailored.Sofic.Measure.irs_of_good`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.irs_of_good), [`MIPRE.Tailored.Sofic.Measure.valOn_eq_valΩ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.valOn_eq_valΩ).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 471](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L471)
