---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ArRoutine.ParTime
statement: formalized
---

# A parameter routine in polynomial time

A parameter routine runs *in polynomial time* when there are $c$, $m$ and $e$ such that, for every $W \geq (\lambda n + 1)^\mu + \sigma + \lambda + n$ and every $X \geq 1$, its parameter program halts on $((\lambda, \mu, \sigma), n)$ with the parameters within $(c (W + 1)^m X^e)^{\mu + 1}$ steps.

## Depends on

- [The parameter routine of the answer-reduced verifier](../part-07/def-ar-routine.md)
- [Answer-reduction construction](../../structure-of-the-proof/part-08/lem-ar-construction.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.ParTime`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.ParTime).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3907](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3907)
