---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.isPiSystem_cylinders, MIPRE.Tailored.Sofic.Measure.eventually_valΩ_le, MIPRE.Tailored.Sofic.Measure.liftStage, MIPRE.Tailored.Sofic.Measure.valΩ_liftStage, MIPRE.Tailored.Sofic.Measure.tendsto_upperSeq
statement: formalized
proof: formalized
---

# The upper value converges to the ergodic value

$\mathrm{upper}(T, t)/2^t \to \mathrm{val}_{\mathrm{erg}}(T)$.

## Depends on

- [The upper value bounds the ergodic value](lem-erg-le-upper.md)
- [From word indicators to invariant random subgroups](lem-irs-of-good.md)
- [The associated subgroup test; I:2086](../part-01/def-assoc-test.md)
- [The value is a continuous functional; I:550](lem-val-on-continuous.md)
- [Main Theorem I (1): the sofic value is approximable from below; I:594](thm-main-theorem-i-lower.md)

## Proof

Lift the optimal feasible point of each stage to a measure on word indicators. The probability measures on word indicators form a compact space, so a subsequence converges; the limit is carried by the good indicators and is invariant, because the cylinder sets are a generating $\pi$-system and the stage's conditions hold on ever more of them. By Lemma [From word indicators to invariant random subgroups](lem-irs-of-good.md) it is an IRS, and the value is continuous.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.isPiSystem_cylinders`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.isPiSystem_cylinders), [`MIPRE.Tailored.Sofic.Measure.eventually_valΩ_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.eventually_valΩ_le), [`MIPRE.Tailored.Sofic.Measure.liftStage`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.liftStage), [`MIPRE.Tailored.Sofic.Measure.valΩ_liftStage`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.valΩ_liftStage), [`MIPRE.Tailored.Sofic.Measure.tendsto_upperSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.tendsto_upperSeq).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 529](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L529)
