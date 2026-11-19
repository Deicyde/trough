---
declaration: theorem
origin: cited
lean: MIPRE.AnswerReduction.answerReduction_soundIn_commuting_fin, MIPRE.LIDT.Simul.approxSoundIn_commuting_of_fin
statement: formalized
proof: formalized
---

# Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the test in dyadic pairs

If ${\omega^{\mathrm{co}}}$ is approached in dyadic pairs (Definition [Dyadic pairs](def-dyadic-pair.md)) and the seeded CL test is sound in dyadic pairs (Definition [The low-individual-degree test is sound in dyadic pairs](def-lidt-sound-fin.md)), then the answer reduction of Theorem [Answer reduction](../../structure-of-the-proof/part-09/thm-answer-reduction.md) is sound in ${\omega^{\mathrm{co}}}$, at the constants of Theorem [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](../part-03/thm-ar-sound-co.md). The first hypothesis is Lemma [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](lem-co-value-finite-pair.md).

## Depends on

- [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](../part-03/thm-ar-sound-co.md)
- [The low-individual-degree test is sound in dyadic pairs](def-lidt-sound-fin.md)
- [Projective strategies in the two models](../part-03/lem-model-proj-strategy-values.md)

## Proof

${\omega^{\mathrm{co}}}$ is then approached by projective strategies in dyadic pairs, where the test is sound, and it dominates every model on a Hilbert space (Lemma [Projective strategies in the two models](../part-03/lem-model-proj-strategy-values.md)). So Theorem [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the low-individual-degree test](../part-03/thm-ar-sound-co.md) applies.

## Lean

Formalized as [`MIPRE.AnswerReduction.answerReduction_soundIn_commuting_fin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.answerReduction_soundIn_commuting_fin), [`MIPRE.LIDT.Simul.approxSoundIn_commuting_of_fin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.approxSoundIn_commuting_of_fin).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3117](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3117)
