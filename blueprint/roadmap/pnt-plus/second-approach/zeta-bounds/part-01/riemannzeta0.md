---
declaration: definition
origin: cited
lean: riemannZeta0
statement: formalized
---

# riemannZeta0

For any natural $N\ge1$, we define

$$
\zeta_0(N,s) :=
\sum_{1\le n \le N} \frac1{n^s}
+
\frac{- N^{1-s}}{1-s} + \frac{-N^{-s}}{2} + s \int_N^\infty \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`riemannZeta0`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/riemannZeta0).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
