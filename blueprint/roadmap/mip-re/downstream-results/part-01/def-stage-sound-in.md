---
declaration: definition
origin: cited
lean: MIPRE.Introspection.SoundIn, MIPRE.Introspection.soundIn_tensor, MIPRE.AnswerReduction.SoundIn, MIPRE.AnswerReduction.soundIn_tensor, MIPRE.Repetition.SoundIn, MIPRE.Repetition.soundIn_tensor
statement: formalized
---

# The stages' soundness clauses in a value model

The soundness clause of introspection, of answer reduction or of parallel repetition *in the value model $\omega$* is that stage's soundness clause (Definitions [Ambient introspection contract](../../structure-of-the-proof/part-06/def-introspection-contract.md) and [Ambient answer-reduction contract](../../structure-of-the-proof/part-09/def-answer-reduction-contract.md), Theorem [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md)) with the value $\mathrm{val}^*$ replaced by $\omega$ on both sides, at the same parameters, error functions and answer bounds. In the model $\mathrm{val}^*$ it is the stage's own clause.

## Depends on

- [Value models](def-value-model.md)
- [Ambient introspection contract](../../structure-of-the-proof/part-06/def-introspection-contract.md)
- [Ambient answer-reduction contract](../../structure-of-the-proof/part-09/def-answer-reduction-contract.md)
- [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md)

## Lean

Formalized as [`MIPRE.Introspection.SoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SoundIn), [`MIPRE.Introspection.soundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.soundIn_tensor), [`MIPRE.AnswerReduction.SoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.SoundIn), [`MIPRE.AnswerReduction.soundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.soundIn_tensor), [`MIPRE.Repetition.SoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.SoundIn), [`MIPRE.Repetition.soundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.soundIn_tensor).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 848](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L848)
