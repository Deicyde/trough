---
declaration: theorem
origin: cited
lean: ZetaShiftFiniteZeros
statement: formalized
proof: formalized
---

# ZetaShiftFiniteZeros

For all $|t|\geq 2$, if $f(z)=\zeta(z+3/2+it)$, then $f(z)$ has a finite number of zeros in $\overline{\mathbb{D}_1}$.

## Depends on

- [SetOfZeros](../part-01/setofzeros.md)

## Proof

If we suppose the opposite, i.e. that there are an infinite number of zeros in this region, then $f\equiv 0$ by the identity theorem. This is a contradiction, so the statement must be true.

## Lean

Formalized as [`ZetaShiftFiniteZeros`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaShiftFiniteZeros).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
