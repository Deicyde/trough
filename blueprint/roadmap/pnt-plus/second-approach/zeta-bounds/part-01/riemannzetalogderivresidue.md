---
declaration: theorem
origin: cited
lean: riemannZetaLogDerivResidue
statement: formalized
proof: formalized
---

# riemannZetaLogDerivResidue

The log derivative of the Riemann zeta function $\zeta(s)$ has a simple pole at $s=1$ with residue $-1$: $-\frac{\zeta'(s)}{\zeta(s)} - \frac{1}{s-1} = O(1)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [logDerivResidue](logderivresidue.md)
- [nonZeroOfBddAbove](nonzeroofbddabove.md)
- [riemannZetaResidue](riemannzetaresidue.md)

## Proof

This follows from Theorem [logDerivResidue](logderivresidue.md) and Theorem [riemannZetaResidue](riemannzetaresidue.md).

## Lean

Formalized as [`riemannZetaLogDerivResidue`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/riemannZetaLogDerivResidue).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
