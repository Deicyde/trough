---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpCore, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpPF, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpPF_eq
statement: formalized
---

# The linear-constraints processor of the answer-reduced verifier

On $(n, x, y, a^R, b^R)$, with the input verifier's programs and $(\lambda, \mu, \sigma)$ stored, the processor runs, as stages that keep their input: the routine's parameter program on $((\lambda, \mu, \sigma), n)$; the input sampler, through the universal machine, on the marginal queries of both players at the seeds of $x$ and $y$; the routine's circuit function at each seed, and then the proof check of each question with that circuit's gates, both on encodings assembled from what the earlier stages output, the input sampler's questions and the readable answers read as bit strings, so that both run on encodings on every input; and finally the program of Lemma [The constraints at two detyped questions, as a program](lem-ar-lp-final.md). No stage decodes a program from data. Its program is computed from the input programs and $(\lambda, \mu, \sigma)$ in polynomial time.

## Depends on

- [The constraints at two detyped questions, as a program](lem-ar-lp-final.md)
- [The parameter routine of the answer-reduced verifier](../part-07/def-ar-routine.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpCore`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpCore), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpPF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpPF), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpPF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpPF_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3838](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3838)
