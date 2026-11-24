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

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ZetaBounds.lean)
