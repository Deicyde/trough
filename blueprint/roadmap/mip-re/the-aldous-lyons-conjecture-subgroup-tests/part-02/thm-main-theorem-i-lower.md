---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.Sofic.Measure.Represents, MIPRE.Tailored.Sofic.Measure.ValidC, MIPRE.Tailored.Sofic.Measure.Represents.value_eq, MIPRE.Tailored.Sofic.Measure.decodeAct, MIPRE.Tailored.Sofic.Measure.codeOf, MIPRE.Tailored.Sofic.Measure.lowerSeq, MIPRE.Tailored.Sofic.Measure.dyadic, MIPRE.Tailored.Sofic.Measure.lowerSeq_le, MIPRE.Tailored.Sofic.Measure.lowerSeq_monotone, MIPRE.Tailored.Sofic.Measure.tendsto_lowerSeq, MIPRE.Tailored.Sofic.Measure.primrec_lowerSeq, MIPRE.Tailored.Sofic.Measure.mainTheoremI_one
statement: formalized
proof: formalized
---

# Main Theorem I (1): the sofic value is approximable from below; I:594

There is a primitive recursive $\alpha(T, t)$ such that $\alpha(T,t)/2^t$ is non-decreasing in $t$, at most $\mathrm{val}_{\mathrm{sof}}(T)$, and converges to it.

## Depends on

- [The value is a continuous functional; I:550](lem-val-on-continuous.md)

## Proof

Enumerate the finite actions by codes; $\alpha(T, t)/2^t$ is the largest value of the first $t$ codes' actions, rounded down to a multiple of $2^{-t}$.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Measure.Represents`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.Represents), [`MIPRE.Tailored.Sofic.Measure.ValidC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.ValidC), [`MIPRE.Tailored.Sofic.Measure.Represents.value_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.Represents.value_eq), [`MIPRE.Tailored.Sofic.Measure.decodeAct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.decodeAct), [`MIPRE.Tailored.Sofic.Measure.codeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.codeOf), [`MIPRE.Tailored.Sofic.Measure.lowerSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.lowerSeq), [`MIPRE.Tailored.Sofic.Measure.dyadic`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.dyadic), [`MIPRE.Tailored.Sofic.Measure.lowerSeq_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.lowerSeq_le), [`MIPRE.Tailored.Sofic.Measure.lowerSeq_monotone`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.lowerSeq_monotone), [`MIPRE.Tailored.Sofic.Measure.tendsto_lowerSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.tendsto_lowerSeq), [`MIPRE.Tailored.Sofic.Measure.primrec_lowerSeq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.primrec_lowerSeq), [`MIPRE.Tailored.Sofic.Measure.mainTheoremI_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Measure.mainTheoremI_one).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 451](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L451)
