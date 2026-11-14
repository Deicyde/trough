---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_time, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_len_pdom, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_total
statement: formalized
proof: formalized
---

# The running time of the answer-length calculator

The answer-length calculator halts on every input. For a parameter routine in polynomial time, it runs at $n$, on every input $(n, d)$, within $(C (W + 1)^M X^E)^{\mu + 1}$ for every $X > |d|$ and $W \geq (\lambda n + 1)^\mu + \sigma + \lambda + n$, and the lengths it outputs are at most $(C (W + 1)^M)^{\mu + 1}$, for $C$, $M$ and $E$ depending only on the routine.

## Depends on

- [A parameter routine in polynomial time](def-ar-par-time.md)
- [The answer-length calculator](../part-07/lem-ar-len.md)
- [The running time and the dimension of the answer-reduced sampler](lem-ar-sampler-time.md)

## Proof

It halts by Lemma [The answer-length calculator](../part-07/lem-ar-len.md). Its two stages are the parameter program and a polynomial-time function of the context. A length is a codeword count, linear in the PCP's dimensions, times a number of coefficients, at most $M d + 1$, times $t$, each below a power of the parameters' size (Lemma [The running time and the dimension of the answer-reduced sampler](lem-ar-sampler-time.md)).

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_time), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_len_pdom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_len_pdom), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_total`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_total).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3950](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3950)
