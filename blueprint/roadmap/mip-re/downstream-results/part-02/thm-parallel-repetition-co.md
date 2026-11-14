---
declaration: theorem
origin: cited
lean: MIPRE.val_repVerifier, MIPRE.val_repVerifier_le, MIPRE.Repetition.soundBound_anti, MIPRE.Repetition.withConst, MIPRE.Repetition.SoundIn.withConst, MIPRE.repetition_withConst_soundIn, MIPRE.Repetition.repConstBoth, MIPRE.repetitionCo, MIPRE.repetitionCo_soundIn_commuting
statement: formalized
proof: formalized
---

# Parallel repetition is sound in ${\omega^{\mathrm{co}}}$

The procedure of Theorem [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md), at the constant $\min(c', c'')$ of the two repetition bounds (Lemma [The repetition bound in ${\omega^{\mathrm{co}}}$, for answers of bounded length](lem-repetition-sound-bound-co.md)), is sound in the model $\mathrm{val}^*$ and in the model ${\omega^{\mathrm{co}}}$ (Definition [The stages' soundness clauses in a value model](../part-01/def-stage-sound-in.md)): for all $0 < \varepsilon \leq 1$, ${\omega^{\mathrm{co}}}(\mathsf{V}_n) \leq 1 - \varepsilon$ at the parse length gives ${\omega^{\mathrm{co}}}(\mathsf{V}^{\textsc{Rep}}_n) \leq \exp(-\min(c', c'')\, \varepsilon^{13} k(n) / (B(n) + 1))$. More generally, in every value model the value of $\mathsf{V}^{\textsc{Rep}}_n$ is that of the $k(n)$-fold direct repetition of $\mathsf{V}_n$ at the parse length, so the procedure is sound in every model with the repetition bound at a constant at least its own.

## Depends on

- [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md)
- [The repetition bound in ${\omega^{\mathrm{co}}}$, for answers of bounded length](lem-repetition-sound-bound-co.md)
- [The stages' soundness clauses in a value model](../part-01/def-stage-sound-in.md)
- [Value models](../part-01/def-value-model.md)

## Proof

The value of $\mathsf{V}^{\textsc{Rep}}_n$ is the value of the repeated game in every model: the proof of Theorem [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md) identifies the two games up to an equivalence of the questions and the padding of the answers by always-rejected ones, and a value model is invariant under both (Definition [Value models](../part-01/def-value-model.md)). So soundness in a model is the repetition bound in that model. Lowering the constant of the procedure keeps every clause, the bound being antitone in the constant; the procedure at $\min(c', c'')$ is the same verifier. The main theorem keeps the constant $c'$, so $\mathrm{MIP}^* = \mathrm{RE}$ does not depend on Theorem [Direct parallel repetition for commuting-operator strategies](../../parallel-repetition/thm-direct-repetition-co.md).

## Lean

Formalized as [`MIPRE.val_repVerifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.val_repVerifier), [`MIPRE.val_repVerifier_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.val_repVerifier_le), [`MIPRE.Repetition.soundBound_anti`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.soundBound_anti), [`MIPRE.Repetition.withConst`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.withConst), [`MIPRE.Repetition.SoundIn.withConst`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.SoundIn.withConst), [`MIPRE.repetition_withConst_soundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.repetition_withConst_soundIn), [`MIPRE.Repetition.repConstBoth`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.repConstBoth), [`MIPRE.repetitionCo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.repetitionCo), [`MIPRE.repetitionCo_soundIn_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.repetitionCo_soundIn_commuting).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1397](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1397)
