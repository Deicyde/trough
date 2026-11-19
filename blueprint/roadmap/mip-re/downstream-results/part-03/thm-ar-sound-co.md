---
declaration: theorem
origin: cited
lean: MIPRE.AnswerReduction.arVerifier_soundness_of_approx, MIPRE.AnswerReduction.answerReduction_soundIn_of_approx, MIPRE.AnswerReduction.arVerifier_soundness_commuting, MIPRE.AnswerReduction.answerReduction_soundIn_commuting, MIPRE.LIDT.Simul.approxSoundIn_commuting
statement: formalized
proof: formalized
---

# Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test

The answer reduction of Theorem [Answer reduction](../../structure-of-the-proof/part-09/thm-answer-reduction.md) is sound (Definition [The stages' soundness clauses in a value model](../part-01/def-stage-sound-in.md)), at the constants $a$, $b$ and threshold of its soundness clause in $\mathrm{val}^*$, in every value model in which oracularization is sound (Definition [Oracularization is sound in a value model](../part-02/def-oracular-sound-in.md)) and which is approached in models where the seeded CL test is sound (Definition [The low-individual-degree test is sound in a model](def-lidt-sound-in.md)). In particular, if the seeded CL test is sound in the commuting-operator model, answer reduction is sound in ${\omega^{\mathrm{co}}}$.

## Depends on

- [Answer-reduction quantitative assembly](../../structure-of-the-proof/part-08/lem-ar-error-assembly.md)
- [The low-individual-degree test is sound in a model](def-lidt-sound-in.md)
- [Projective strategies in the two models](lem-model-proj-strategy-values.md)
- [Oracularization is sound in both models](../part-02/thm-oracularization-in-model.md)
- [The stages' soundness clauses in a value model](../part-01/def-stage-sound-in.md)
- [Answer reduction](../../structure-of-the-proof/part-09/thm-answer-reduction.md)

## Proof

Let $\omega$ of the answer-reduced verifier exceed $1 - \varepsilon$, with $\mu \geq 1$ and $\varepsilon < 1$; otherwise the loss is at least $1$. The output verifier rejects answers longer than the answer cut, so $\omega$ at the cut exceeds $1 - \varepsilon$, and the hypothesis gives a projective strategy of value greater than $1 - \varepsilon$ for the game at the cut, in a model where the test is sound and which $\omega$ dominates. The analysis of Lemma [Answer-reduction quantitative assembly](../../structure-of-the-proof/part-08/lem-ar-error-assembly.md), which is stated for a projective strategy in any such model, gives $\omega(\mathsf{V}_n) \geq 1 - \delta(\varepsilon, n)$ at the constants of the clause in $\mathrm{val}^*$, which are explicit. For ${\omega^{\mathrm{co}}}$, oracularization is sound (Theorem [Oracularization is sound in both models](../part-02/thm-oracularization-in-model.md)), and Lemma [Projective strategies in the two models](lem-model-proj-strategy-values.md) gives, below ${\omega^{\mathrm{co}}}$, a projective strategy in the model of a commuting-operator strategy, which ${\omega^{\mathrm{co}}}$ dominates.

## Lean

Formalized as [`MIPRE.AnswerReduction.arVerifier_soundness_of_approx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier_soundness_of_approx), [`MIPRE.AnswerReduction.answerReduction_soundIn_of_approx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.answerReduction_soundIn_of_approx), [`MIPRE.AnswerReduction.arVerifier_soundness_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier_soundness_commuting), [`MIPRE.AnswerReduction.answerReduction_soundIn_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.answerReduction_soundIn_commuting), [`MIPRE.LIDT.Simul.approxSoundIn_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.approxSoundIn_commuting).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1722](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1722)
