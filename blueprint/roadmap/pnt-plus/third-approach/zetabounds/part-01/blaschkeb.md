---
declaration: definition
origin: cited
lean: BlaschkeB
statement: formalized
---

# BlaschkeB

Let $0 < r < R < 1$, and $f:\mathbb{C}\to\mathbb{C}$ be analytic $\overline{\mathbb{D}_1}$ with $f(0)\neq 0$. We define a function $B_f:\mathbb{C}\to\mathbb{C}$ as follows.

$$
B_f(z)=C_f(z)\prod_{\rho\in\mathcal{K}_f(r)}
\left(R-\frac{z\overline{\rho}}{R}\right)^{m_f(\rho)}
$$

## Depends on

- [CFunction](cfunction.md)
- [SetOfZeros](setofzeros.md)

## Lean

Formalized as [`BlaschkeB`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/BlaschkeB).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
