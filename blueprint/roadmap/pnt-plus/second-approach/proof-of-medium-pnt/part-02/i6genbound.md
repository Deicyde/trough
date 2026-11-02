---
declaration: lemma
origin: cited
lean: I6GenBound
statement: formalized
proof: formalized
---

# I6GenBound

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md), we have that

$$
\left|I_6(\nu,\epsilon,X,\sigma_1,\sigma_2)\right|
\ll\frac{X}{\epsilon}\,X^{-\frac{A}{(\log T)^{n_1}}}.
$$

## Depends on

- [I₆](../part-01/i6.md)

## Proof depends on

- [I₄](../part-01/i4.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [intervalIntegral-conj](../../zeta-bounds/part-01/intervalintegral-conj.md)
- [deriv-riemannZeta-conj](../../zeta-bounds/part-01/deriv-riemannzeta-conj.md)
- [I4GenBound](i4genbound.md)

## Proof

We deduce this from the corresponding bound for $I_4$, using the symmetry between $I_4$ and $I_6$.

## Lean

Formalized as [`I6GenBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I6GenBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
