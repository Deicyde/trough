---
declaration: lemma
origin: cited
lean: I7GenBound
statement: formalized
proof: formalized
---

# I7GenBound

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md), we have that

$$
\left|I_7(\nu,\epsilon,X,T)\right|\ll\frac{X}{\epsilon}\, X^{-\frac{A}{(\log T)^{n_1}}}.
$$

## Depends on

- [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md)
- [I₇](../part-01/i7.md)

## Proof depends on

- [I₃](../part-01/i3.md)
- [I3GenBound](i3genbound.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [intervalIntegral-conj](../../zeta-bounds/part-01/intervalintegral-conj.md)
- [deriv-riemannZeta-conj](../../zeta-bounds/part-01/deriv-riemannzeta-conj.md)

## Proof

We deduce this from the corresponding bound for $I_3$, using the symmetry between $I_3$ and $I_7$.

## Lean

Formalized as [`I7GenBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I7GenBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
