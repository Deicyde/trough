---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.argCircL_eq, MIPRE.Tailored.AnsRed.Typed.argPrfL_eq, MIPRE.Tailored.AnsRed.Typed.length_seedL_le, MIPRE.Tailored.AnsRed.Typed.lpHdat_pdom, MIPRE.Tailored.AnsRed.Typed.margCallX_pdom, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD_time
statement: formalized
proof: formalized
---

# The running time of the linear-constraints processor

For a parameter routine in polynomial time there are $C$, $M$ and $E$ such that, for every $W \geq (\lambda n + 1)^\mu + \sigma + \lambda + n$, every input verifier with $|\mathsf{V}| \leq \sigma$ whose sampler runs within $(\lambda n + 1)^\mu (|d| + 1)^\mu$ at $n$, and every input $(n, d)$ and $X > |d|$, the processor halts within $(C (W + 1)^M X^E)^{\mu + 1}$ steps.

## Depends on

- [A parameter routine in polynomial time](def-ar-par-time.md)
- [The linear-constraints processor of the answer-reduced verifier](def-ar-lp.md)
- [The typed answer-reduced decider](../../structure-of-the-proof/part-08/lem-ar-typed-decider.md)
- [The running time and the dimension of the answer-reduced sampler](lem-ar-sampler-time.md)

## Proof

As for the MIP\* answer reduction's decider (Lemma [The typed answer-reduced decider](../../structure-of-the-proof/part-08/lem-ar-typed-decider.md)), stage by stage. The parameter program runs within the bound. Each call to the input sampler is on a marginal query of a constant-size header and a question's seed bits, at most linear in $|d|$, so costs $(\lambda n + 1)^\mu (c W X)^\mu$ through the universal machine. The circuit function and the proof check are polynomial-time functions, and their stages' arguments are encodings on every input: the input sampler's questions and the readable answers are read as bit strings. The last stage is a polynomial-time function of the context. Each stage's output is no longer than its running time, so the contexts stay dominated. Neither the input's calculator nor its processor is run: they enter the circuit function's input as data.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.argCircL_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.argCircL_eq), [`MIPRE.Tailored.AnsRed.Typed.argPrfL_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.argPrfL_eq), [`MIPRE.Tailored.AnsRed.Typed.length_seedL_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.length_seedL_le), [`MIPRE.Tailored.AnsRed.Typed.lpHdat_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lpHdat_pdom), [`MIPRE.Tailored.AnsRed.Typed.margCallX_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.margCallX_pdom), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lpD_time).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3971](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3971)
