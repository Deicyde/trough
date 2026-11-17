---
declaration: lemma
origin: cited
lean: ZetaSum_aux2
statement: formalized
proof: formalized
---

# ZetaSum-aux2

Let $N$ be a natural number and $s\in \mathbb{C}$, $\Re(s)>1$. Then

$$
\sum_{N < n} \frac{1}{n^s} =  \frac{- N^{1-s}}{1-s} + \frac{-N^{-s}}{2}
+ s \int_N^\infty \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaSum-aux1](zetasum-aux1.md)

## Proof

Apply Lemma [ZetaSum-aux1](zetasum-aux1.md) with $a=N$ and $b\to \infty$.

## Lean

Formalized as [`ZetaSum_aux2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaSum_aux2).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
