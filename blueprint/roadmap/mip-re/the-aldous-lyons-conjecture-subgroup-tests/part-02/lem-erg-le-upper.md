---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.exists_rounding, MIPRE.Tailored.Sofic.Measure.exists_feasible_of_irs, MIPRE.Tailored.Sofic.Measure.valOn_le_upperSeq, MIPRE.Tailored.Sofic.Measure.valErg_le_upperSeq
statement: formalized
proof: formalized
---

# The upper value bounds the ergodic value

For every stage $t$, $\mathrm{val}_{\mathrm{erg}}(T) \leq \mathrm{upper}(T, t)/2^t$.

## Depends on

- [Pseudo-subgroup polytopes, discretized; I:927, I:1105](def-pseudo-subgroup-polytope.md)
- [From word indicators to invariant random subgroups](lem-irs-of-good.md)
- [The associated subgroup test; I:2086](../part-01/def-assoc-test.md)
- [Main Theorem I (1): the sofic value is approximable from below; I:594](thm-main-theorem-i-lower.md)

## Proof

Round the restriction of an IRS to the stage's words to the grid: it is feasible, and its value is within $2/2^t$ of the IRS's.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.exists_rounding`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.exists_rounding), [`MIPRE.Tailored.Sofic.Measure.exists_feasible_of_irs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.exists_feasible_of_irs), [`MIPRE.Tailored.Sofic.Measure.valOn_le_upperSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.valOn_le_upperSeq), [`MIPRE.Tailored.Sofic.Measure.valErg_le_upperSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.valErg_le_upperSeq).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 512](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L512)
