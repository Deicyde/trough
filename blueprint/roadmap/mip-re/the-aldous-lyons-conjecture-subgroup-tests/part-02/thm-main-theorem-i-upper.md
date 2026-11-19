---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.primrec_upperSeq, MIPRE.Tailored.Sofic.Measure.upperMin, MIPRE.Tailored.Sofic.Measure.primrec_upperMin, MIPRE.Tailored.Sofic.Measure.valErg_le_upperMin, MIPRE.Tailored.Sofic.Measure.antitone_upperMin, MIPRE.Tailored.Sofic.Measure.mainTheoremI_two, MIPRE.Tailored.Sofic.Measure.ErgUpperApprox, MIPRE.Tailored.Sofic.Measure.MainTheoremITwo, MIPRE.Tailored.Sofic.Measure.ergUpperApprox, MIPRE.Tailored.Sofic.Measure.mainTheoremITwo
statement: formalized
proof: formalized
---

# Main Theorem I (2): the ergodic value is approximable from above; I:594

There is a primitive recursive $\beta(T, t)$ such that $\beta(T,t)/2^t$ is non-increasing in $t$, at least $\mathrm{val}_{\mathrm{erg}}(T)$, and converges to it.

## Depends on

- [The upper value bounds the ergodic value](lem-erg-le-upper.md)
- [The upper value converges to the ergodic value](lem-upper-converge.md)
- [The associated subgroup test; I:2086](../part-01/def-assoc-test.md)
- [The associated test is computable from the game](../part-01/lem-assoc-test-primrec.md)
- [Main Theorem I (1): the sofic value is approximable from below; I:594](thm-main-theorem-i-lower.md)

## Proof

The running minimum of the upper values, which is primitive recursive because the stage search is.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.primrec_upperSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.primrec_upperSeq), [`MIPRE.Tailored.Sofic.Measure.upperMin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.upperMin), [`MIPRE.Tailored.Sofic.Measure.primrec_upperMin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.primrec_upperMin), [`MIPRE.Tailored.Sofic.Measure.valErg_le_upperMin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.valErg_le_upperMin), [`MIPRE.Tailored.Sofic.Measure.antitone_upperMin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.antitone_upperMin), [`MIPRE.Tailored.Sofic.Measure.mainTheoremI_two`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.mainTheoremI_two), [`MIPRE.Tailored.Sofic.Measure.ErgUpperApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.ErgUpperApprox), [`MIPRE.Tailored.Sofic.Measure.MainTheoremITwo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.MainTheoremITwo), [`MIPRE.Tailored.Sofic.Measure.ergUpperApprox`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.ergUpperApprox), [`MIPRE.Tailored.Sofic.Measure.mainTheoremITwo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.mainTheoremITwo).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 548](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L548)
