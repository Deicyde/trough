---
declaration: definition
origin: cited
lean: ZeroFactor
statement: formalized
---

# ZeroFactor

Let $f:\mathbb{C}\to\mathbb{C}$ and $\rho\in\mathbb{C}$. Then there exists $h_\rho$ such that

$$
f(z)=(z-\rho)^{m_f(\rho)}\,h_\rho(z).
$$

In LEAN, this corresponds exactly with (-.analyticOrderAt-ne-top.mp -).choose, but this serves as a wrapper of that with the necessary conditions.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ZeroFactor`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZeroFactor).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
