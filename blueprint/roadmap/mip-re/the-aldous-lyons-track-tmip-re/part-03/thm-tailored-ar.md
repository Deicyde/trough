---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.one_le_delta_mu_zero, MIPRE.Tailored.AnsRed.Typed.one_le_size, MIPRE.Tailored.AnsRed.Typed.arOut, MIPRE.Tailored.AnsRed.Typed.tailoredAnswerReductionOf, MIPRE.Tailored.AnsRed.Typed.arConsts, MIPRE.Tailored.AnsRed.Typed.one_le_arConsts_E₂, MIPRE.Tailored.AnsRed.Typed.tailoredAnswerReduction
statement: formalized
proof: formalized
---

# Answer reduction for tailored verifiers; II:6883

The contract `TailoredAnswerReduction` is inhabited, at input level $5$.

## Depends on

- [The three stage contracts](def-tailored-stages.md)
- [The routine of the answer reduction, fixed](../part-09/lem-ar-routine-fixed.md)
- [The soundness error and the contract's loss](../part-09/lem-ar-error.md)
- [Completeness and soundness of the output verifier](../part-08/thm-ar-output.md)
- [The complexity clause of the answer reduction](../part-08/thm-ar-output-within.md)
- [First facts about the parameters](../part-08/lem-ar-params-basic.md)

## Proof

The output verifier of the routine of Lemma [The routine of the answer reduction, fixed](../part-09/lem-ar-routine-fixed.md), at $E_1 = 2E$, $E_2 = E_{2,0}$ and $c_0$ the size constant of the output indicator: its complexity clause is Theorem [The complexity clause of the answer reduction](../part-08/thm-ar-output-within.md), its completeness that of Theorem [Completeness and soundness of the output verifier](../part-08/thm-ar-output.md) under the honest PCPs' hypotheses, and its soundness that of Theorem [Completeness and soundness of the output verifier](../part-08/thm-ar-output.md) with Lemma [The soundness error and the contract's loss](../part-09/lem-ar-error.md); for $\mu = 0$ the loss is at least $1$.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.one_le_delta_mu_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.one_le_delta_mu_zero), [`MIPRE.Tailored.AnsRed.Typed.one_le_size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.one_le_size), [`MIPRE.Tailored.AnsRed.Typed.arOut`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arOut), [`MIPRE.Tailored.AnsRed.Typed.tailoredAnswerReductionOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.tailoredAnswerReductionOf), [`MIPRE.Tailored.AnsRed.Typed.arConsts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arConsts), [`MIPRE.Tailored.AnsRed.Typed.one_le_arConsts_E₂`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.one_le_arConsts_E₂), [`MIPRE.Tailored.AnsRed.Typed.tailoredAnswerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.tailoredAnswerReduction).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1101](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1101)
