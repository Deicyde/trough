---
declaration: definition
origin: cited
lean: Eψ.classicalBound
statement: formalized
---

# Definitions 1, 5, FKS2

We say that $E_\psi$ satisfies a *classical bound* with parameters $A, B, C, R, x_0$ if for all $x \geq x_0$ we have

$$
E_\psi(x) \leq A \left(\frac{\log x}{R}\right)^B
\exp\left(-C \left(\frac{\log x}{R}\right)^{1/2}
\right).
$$

We say that it obeys a *numerical bound* with parameter $\varepsilon(x_0)$ if for all $x \geq x_0$ we have

$$
E_\psi(x) \leq \varepsilon(x_0).
$$

## Depends on

- [Equation (2) of FKS2](epsi-def.md)

## Lean

Formalized as [`Eψ.classicalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Eψ.classicalBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Defs.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Defs.lean)
