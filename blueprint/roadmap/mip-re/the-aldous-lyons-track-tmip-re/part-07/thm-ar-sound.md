---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.roleFamily_liftedCl_eval, MIPRE.Tailored.AnsRed.Typed.inCL_toGame, MIPRE.Tailored.AnsRed.Typed.decB, MIPRE.Tailored.AnsRed.Typed.valStar_presented_ar_le, MIPRE.Tailored.AnsRed.Typed.valStar_ar_sound
statement: formalized
proof: formalized
---

# Soundness of the answer-reduced game

Under the hypotheses of Definition [The honest answers](../part-06/def-ar-honest-answers.md), for $d \geq 1$, an answer bound at least the types' lengths, $q \geq 2 (M + 1) d$ and $q \geq 2 m (5 + 6 (d + 1))$: if the answer-reduced game presented by the typed data on the typed game of an answer-reduced sampler has $\mathrm{val}^* > 1 - \varepsilon$, then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - 24 \sqrt{e(16^9 \varepsilon)}$.

## Depends on

- [The failure of the decoded strategy](lem-ar-decoded-value.md)
- [The honest strategy of the answer-reduced game](../part-06/def-ar-honest-strategy.md)
- [Presenting a detyped game by a detyped tailored game](../part-04/lem-presentation.md)
- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)
- [Oracularization is sound in both models](../../downstream-results/part-02/thm-oracularization-in-model.md)
- [The low-individual-degree test is sound in the tensor-product model](../../downstream-results/part-03/lem-lidt-sound-in-tensor.md)

## Proof

The presented game's $\mathrm{val}^*$ is at most the detyped game's (Lemma [Presenting a detyped game by a detyped tailored game](../part-04/lem-presentation.md)), whose typed game then has $\mathrm{val}^* > 1 - 16^9 \varepsilon$, there being nine types (Lemma [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)). $\mathrm{val}^*$ is approached by projective strategies in tensor-product models, where the test is sound and which $\mathrm{val}^*$ dominates (Lemma [The low-individual-degree test is sound in the tensor-product model](../../downstream-results/part-03/lem-lidt-sound-in-tensor.md)); take one, $T$, of value more than $1 - 16^9 \varepsilon$. Its decoded strategy has value at least $1 - e(16^9 \varepsilon)$ (Lemma [The failure of the decoded strategy](lem-ar-decoded-value.md)), the typed oracularized game's value is at most the oracularization's, and oracularization is sound (Theorem [Oracularization is sound in both models](../../downstream-results/part-02/thm-oracularization-in-model.md)), the oracularized input's game being the input's.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.roleFamily_liftedCl_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.roleFamily_liftedCl_eval), [`MIPRE.Tailored.AnsRed.Typed.inCL_toGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.inCL_toGame), [`MIPRE.Tailored.AnsRed.Typed.decB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.decB), [`MIPRE.Tailored.AnsRed.Typed.valStar_presented_ar_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.valStar_presented_ar_le), [`MIPRE.Tailored.AnsRed.Typed.valStar_ar_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.valStar_ar_sound).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3441](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3441)
