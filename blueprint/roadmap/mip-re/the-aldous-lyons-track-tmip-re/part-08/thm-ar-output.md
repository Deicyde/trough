---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ArRoutine.arMeets_output, MIPRE.Tailored.AnsRed.Typed.ArRoutine.hasPerfectZPC_output, MIPRE.Tailored.AnsRed.Typed.ArRoutine.valStar_sound_output
statement: formalized
proof: formalized
---

# Completeness and soundness of the output verifier

At every index the output verifier meets the presented answer-reduced game. So, under the hypotheses of Definition [The honest answers](../part-06/def-ar-honest-answers.md) on the routine's circuits and an answer bound at least the types' lengths: if $d \geq 17$ and the input's $n$-th game has a perfect ZPC strategy, so has the output's; and if $d \geq 1$, $q \geq 2 (M + 1) d$, $q \geq 2 m (5 + 6 (d + 1))$ and the output's $n$-th game has $\mathrm{val}^* > 1 - \varepsilon$, then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - 24 \sqrt{e(16^9 \varepsilon)}$.

## Depends on

- [The output verifier of the answer reduction](def-ar-output.md)
- [Completeness and soundness of an output verifier meeting the presented game](../part-07/thm-ar-meets.md)
- [The distribution of the answer-reduced sampler](../part-07/lem-ar-sampler-dist.md)
- [The answer-length calculator](../part-07/lem-ar-len.md)
- [The processor computes the presented constraints](lem-ar-lp.md)

## Proof

The sampler's distribution is the presented game's weights (Lemma [The distribution of the answer-reduced sampler](../part-07/lem-ar-sampler-dist.md)), the calculator outputs its lengths (Lemma [The answer-length calculator](../part-07/lem-ar-len.md)) and the processor its constraints (Lemma [The processor computes the presented constraints](lem-ar-lp.md)). Theorem [Completeness and soundness of an output verifier meeting the presented game](../part-07/thm-ar-meets.md) concludes, the answer-reduced family being an answer-reduced sampler.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.arMeets_output`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.arMeets_output), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.hasPerfectZPC_output`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.hasPerfectZPC_output), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.valStar_sound_output`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.valStar_sound_output).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3884](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3884)
