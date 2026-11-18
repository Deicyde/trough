---
declaration: lemma
origin: cited
lean: I9Bound
statement: formalized
proof: formalized
---

# I9Bound

We have that

$$
\left|I_{1}(\nu, \epsilon, X, T)\
\right| \ll \frac{X}{\epsilon T}
.
$$

## Depends on

- [I₉](../part-01/i9.md)

## Proof depends on

- [I₁](../part-01/i1.md)
- [I1Bound](i1bound.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [deriv-riemannZeta-conj](../../zeta-bounds/part-01/deriv-riemannzeta-conj.md)

## Proof

We deduce this from the corresponding bound for $I_1$, using the symmetry between $I_1$ and $I_9$.

## Lean

Formalized as [`I9Bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I9Bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MediumPNT.lean)
