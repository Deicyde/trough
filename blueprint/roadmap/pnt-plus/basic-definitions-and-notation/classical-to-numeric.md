---
declaration: lemma
origin: cited
lean: Eψ.classicalBound.to_numericalBound, Eθ.classicalBound.to_numericalBound, Eπ.classicalBound.to_numericalBound
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/901
---

# Classic bound implies numerical bound

A classical bound for $x \geq x_0$ implies a numerical bound for $x \geq \max(x_0, \exp( R (2B/C)^2 ))$.

## Depends on

- [Equation (2) of FKS2](epsi-def.md)
- [Definitions 1, 5, FKS2](classical-bound-psi.md)
- [Definitions 1, 5, FKS2](classical-bound-theta.md)
- [Equation (2) of FKS2](etheta-def.md)
- [Definitions 1, 5, FKS2](classical-bound-pi.md)
- [Equation (1) of FKS2](epi-def.md)

## Proof depends on

- [Admissible bound decreasing for large x](admissible-bound-monotone.md)

## Proof

Immediate from previous lemma

## Lean

Formalized as [`Eψ.classicalBound.to_numericalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Eψ.classicalBound.to_numericalBound), [`Eθ.classicalBound.to_numericalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Eθ.classicalBound.to_numericalBound), [`Eπ.classicalBound.to_numericalBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Eπ.classicalBound.to_numericalBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Defs.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Defs.lean)
