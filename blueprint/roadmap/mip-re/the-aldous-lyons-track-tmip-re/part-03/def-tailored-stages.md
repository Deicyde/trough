---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredIntrospection, MIPRE.Tailored.TailoredAnswerReduction, MIPRE.Tailored.TailoredRepetition, MIPRE.Tailored.TailoredRepetition.arg
statement: formalized
---

# The three stage contracts

Question reduction (II:5712), answer reduction (II:6883) and parallel repetition (II:11103) for tailored verifiers, each in value form, with the parameters, budgets and soundness losses of the corresponding contracts of the existing pipeline (Definitions [Ambient introspection contract](../../structure-of-the-proof/part-06/def-introspection-contract.md) and [Ambient answer-reduction contract](../../structure-of-the-proof/part-09/def-answer-reduction-contract.md), Theorem [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md)): tailored verifiers in and out, the output's answer-length calculator part of the data, completeness read in perfect ZPC strategies, and repetition's soundness loss depending on a bound on the input's lengths in place of a parse length.

## Depends on

- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)
- [Ambient introspection contract](../../structure-of-the-proof/part-06/def-introspection-contract.md)
- [Ambient answer-reduction contract](../../structure-of-the-proof/part-09/def-answer-reduction-contract.md)
- [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredIntrospection`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredIntrospection), [`MIPRE.Tailored.TailoredAnswerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredAnswerReduction), [`MIPRE.Tailored.TailoredRepetition`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredRepetition), [`MIPRE.Tailored.TailoredRepetition.arg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredRepetition.arg).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1061](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1061)
