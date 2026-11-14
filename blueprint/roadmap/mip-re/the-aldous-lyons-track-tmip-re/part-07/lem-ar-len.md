---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.lenPar, MIPRE.Tailored.AnsRed.Typed.lenOfIdx, MIPRE.Tailored.AnsRed.Typed.lenOfIdx_lenPar, MIPRE.Tailored.AnsRed.Typed.idxAt, MIPRE.Tailored.AnsRed.Typed.lenParF, MIPRE.Tailored.AnsRed.Typed.lenParF_arParams, MIPRE.Tailored.AnsRed.Typed.lenF, MIPRE.Tailored.AnsRed.Typed.length_lenF, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenCore, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenPF, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenPF_eq, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_lenIs, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_lenIs_question, MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_presented
statement: formalized
proof: formalized
---

# The answer-length calculator

The answer-length calculator at $(\lambda, \mu, \sigma)$, on $(n, x, \kappa)$, runs the routine's parameter program on $((\lambda, \mu, \sigma), n)$ as a stage, then decodes the graph view of $x$ with $\kappa$ into the two factors of a length by a finite table and multiplies them with $t$ in unary, an undecodable view giving $0$. It halts on every input, at a detyped question it outputs the readable and the linear lengths of the presented answer-reduced game, and its program is computed from $(\lambda, \mu, \sigma)$ in polynomial time.

## Depends on

- [The parameter routine of the answer-reduced verifier](def-ar-routine.md)
- [The presented answer-reduced game, and meeting it](def-ar-meets.md)
- [Detyping a tailored game](../part-03/def-tailored-detyping.md)

## Proof

The stage outputs the parameters. The presented game's lengths at a detyped question are those of the type its graph view decodes to (Definition [Detyping a tailored game](../part-03/def-tailored-detyping.md)), products of a codeword count of the role, the coefficients of a codeword at the type, and $t$.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.lenPar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenPar), [`MIPRE.Tailored.AnsRed.Typed.lenOfIdx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenOfIdx), [`MIPRE.Tailored.AnsRed.Typed.lenOfIdx_lenPar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenOfIdx_lenPar), [`MIPRE.Tailored.AnsRed.Typed.idxAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.idxAt), [`MIPRE.Tailored.AnsRed.Typed.lenParF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenParF), [`MIPRE.Tailored.AnsRed.Typed.lenParF_arParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenParF_arParams), [`MIPRE.Tailored.AnsRed.Typed.lenF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenF), [`MIPRE.Tailored.AnsRed.Typed.length_lenF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.length_lenF), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenCore`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenCore), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenPF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenPF), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenPF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenPF_eq), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_lenIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_lenIs), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_lenIs_question`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_lenIs_question), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_presented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.lenD_presented).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3644](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3644)
