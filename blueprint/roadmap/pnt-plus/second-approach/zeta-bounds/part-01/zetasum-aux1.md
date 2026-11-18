---
declaration: lemma
origin: cited
lean: ZetaSum_aux1
statement: formalized
proof: formalized
---

# ZetaSum-aux1

Let $0 < a < b$ be natural numbers and $s\in \mathbb{C}$ with $s \ne 1$ and $s \ne 0$. Then

$$
\sum_{a < n \le b} \frac{1}{n^s} =  \frac{b^{1-s} - a^{1-s}}{1-s} + \frac{b^{-s}-a^{-s}}{2}
+ s \int_a^b \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [sum-eq-int-deriv](sum-eq-int-deriv.md)

## Proof

Apply Lemma [sum-eq-int-deriv](sum-eq-int-deriv.md) to the function $x \mapsto x^{-s}$.

## Lean

Formalized as [`ZetaSum_aux1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaSum_aux1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
