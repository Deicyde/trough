---
declaration: theorem
origin: cited
lean: GenStrengthPNT
statement: formalized
proof: formalized
---

# GenStrengthPNT

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../proof-of-medium-pnt/part-01/logderivzetahasbound.md), we have that

$$
\sum_{n \leq x}\Lambda(n)=x+O(x\exp(-c(\log x)^{1/(1+n_1)})).
$$

## Depends on

- [LogDerivZetaHasBound](../proof-of-medium-pnt/part-01/logderivzetahasbound.md)

## Proof depends on

- [I7GenBound](../proof-of-medium-pnt/part-02/i7genbound.md)
- [I3GenBound](../proof-of-medium-pnt/part-02/i3genbound.md)
- [LogDerivZetaHolcSmallT](../zeta-bounds/part-02/logderivzetaholcsmallt.md)
- [I₄](../proof-of-medium-pnt/part-01/i4.md)
- [I₂](../proof-of-medium-pnt/part-01/i2.md)
- [I₆](../proof-of-medium-pnt/part-01/i6.md)
- [I5Bound](../proof-of-medium-pnt/part-02/i5bound.md)
- [I4GenBound](../proof-of-medium-pnt/part-02/i4genbound.md)
- [SmoothedChebyshevClose](../proof-of-medium-pnt/part-01/smoothedchebyshevclose.md)
- [I₃](../proof-of-medium-pnt/part-01/i3.md)
- [I₁](../proof-of-medium-pnt/part-01/i1.md)
- [Smooth1Nonneg](../mellin-transforms/part-01/smooth1nonneg.md)
- [MellinOfSmooth1c](../mellin-transforms/part-01/mellinofsmooth1c.md)
- [Smooth1ContinuousAt](../mellin-transforms/part-01/smooth1continuousat.md)
- [I6GenBound](../proof-of-medium-pnt/part-02/i6genbound.md)
- [I1Bound](../proof-of-medium-pnt/part-02/i1bound.md)
- [I₃₇](../proof-of-medium-pnt/part-01/i37.md)
- [I₉](../proof-of-medium-pnt/part-01/i9.md)
- [Smooth1Properties-above](../mellin-transforms/part-01/smooth1properties-above.md)
- [Smooth1](../mellin-transforms/part-01/smooth1.md)
- [I₈](../proof-of-medium-pnt/part-01/i8.md)
- [I₅](../proof-of-medium-pnt/part-01/i5.md)
- [I8GenBound](../proof-of-medium-pnt/part-02/i8genbound.md)
- [SmoothedChebyshev](../proof-of-medium-pnt/part-01/smoothedchebyshev.md)
- [SmoothedChebyshevPull2](../proof-of-medium-pnt/part-02/smoothedchebyshevpull2.md)
- [SmoothExistence](../mellin-transforms/part-02/smoothexistence.md)
- [I9Bound](../proof-of-medium-pnt/part-02/i9bound.md)
- [I2GenBound](../proof-of-medium-pnt/part-02/i2genbound.md)
- [I₇](../proof-of-medium-pnt/part-01/i7.md)
- [Smooth1LeOne](../mellin-transforms/part-01/smooth1leone.md)
- [SmoothedChebyshevPull1](../proof-of-medium-pnt/part-02/smoothedchebyshevpull1.md)

## Proof

By Theorems [SmoothedChebyshevPull1](../proof-of-medium-pnt/part-02/smoothedchebyshevpull1.md), [SmoothedChebyshevPull2](../proof-of-medium-pnt/part-02/smoothedchebyshevpull2.md), and [SmoothedChebyshevClose](../proof-of-medium-pnt/part-01/smoothedchebyshevclose.md) we have that

$$
\mathcal{M}(\tilde{1}_\varepsilon)(1)\,x^1+I_1-I_2+I_3-I_4+I_5+I_6+I_7+I_8+I_9
=\psi(x)+O(\varepsilon x\log x).
$$

Applying Theorems [I1Bound](../proof-of-medium-pnt/part-02/i1bound.md), [I2GenBound](../proof-of-medium-pnt/part-02/i2genbound.md), [I3GenBound](../proof-of-medium-pnt/part-02/i3genbound.md), [I4GenBound](../proof-of-medium-pnt/part-02/i4genbound.md), [I5Bound](../proof-of-medium-pnt/part-02/i5bound.md), [I6GenBound](../proof-of-medium-pnt/part-02/i6genbound.md), [I7GenBound](../proof-of-medium-pnt/part-02/i7genbound.md), [I8GenBound](../proof-of-medium-pnt/part-02/i8genbound.md), [I9Bound](../proof-of-medium-pnt/part-02/i9bound.md), and [MellinOfSmooth1c](../mellin-transforms/part-01/mellinofsmooth1c.md) we have

$$
\psi(x)=x+O(\varepsilon x)+O(\varepsilon x\log x)+O\left(\frac{X}{\varepsilon T}\right)+
O\left(\frac{X\log X}{\varepsilon T}\right)+
O\left(\frac{X}{\varepsilon}\,X^{-A/(\log T)^{n_1}}\right)+
O\left(\frac{X^{\sigma_2}}{\varepsilon}\right).
$$

Balancing the error terms in $\varepsilon$ and $T$ completes the proof.

## Lean

Formalized as [`GenStrengthPNT`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/GenStrengthPNT).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
