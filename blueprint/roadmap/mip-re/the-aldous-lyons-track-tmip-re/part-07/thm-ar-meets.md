---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.hasPerfectZPC_of_arMeets, MIPRE.Tailored.AnsRed.Typed.valStar_sound_of_arMeets
statement: formalized
proof: formalized
---

# Completeness and soundness of an output verifier meeting the presented game

Let a tailored verifier $\mathsf{V}'$ meet at $n$ the answer-reduced game presented on the typed game of an answer-reduced sampler, under the hypotheses of Definition [The honest answers](../part-06/def-ar-honest-answers.md), with an answer bound at least the types' lengths. If $d \geq 17$ and the input's $n$-th game has a perfect ZPC strategy, so has $\mathsf{V}'_n$. If $d \geq 1$, $q \geq 2 (M + 1) d$, $q \geq 2 m (5 + 6 (d + 1))$ and $\mathrm{val}^*(\mathsf{V}'_n) > 1 - \varepsilon$, then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - 24 \sqrt{e(16^9 \varepsilon)}$, with $e$ the error of Lemma [The failure of the decoded strategy](lem-ar-decoded-value.md).

## Depends on

- [The presented answer-reduced game, and meeting it](def-ar-meets.md)
- [A tailored verifier meeting a game extends it](lem-tailored-meets.md)
- [ZPC completeness of the answer-reduced game](../part-06/thm-ar-zpc-complete.md)
- [Soundness of the answer-reduced game](thm-ar-sound.md)

## Proof

$\mathsf{V}'_n$ extends the presented game (Lemma [A tailored verifier meeting a game extends it](lem-tailored-meets.md)), so it has the presented game's $\mathrm{val}^*$ and its perfect ZPC strategies. Theorems [ZPC completeness of the answer-reduced game](../part-06/thm-ar-zpc-complete.md) and [Soundness of the answer-reduced game](thm-ar-sound.md) conclude.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.hasPerfectZPC_of_arMeets`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.hasPerfectZPC_of_arMeets), [`MIPRE.Tailored.AnsRed.Typed.valStar_sound_of_arMeets`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.valStar_sound_of_arMeets).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3528](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3528)
