---
declaration: lemma
origin: cited
lean: I1Bound
statement: formalized
proof: formalized
---

# I1Bound

We have that

$$
\left|I_{1}(\nu, \epsilon, X, T)\
\right| \ll \frac{X\log X}{\epsilon T}
.
$$

## Depends on

- [I₁](../part-01/i1.md)

## Proof depends on

- [SmoothedChebyshevPull1-aux-integrable](../part-01/smoothedchebyshevpull1-aux-integrable.md)
- [riemannZetaLogDerivResidue](../../zeta-bounds/part-01/riemannzetalogderivresidue.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md)

## Proof

Unfold the definitions and apply the triangle inequality.

$$
\left|I_{1}(\nu, \epsilon, X, T)\right| =
\left|
\frac{1}{2\pi i} \int_{-\infty}^{-T}
\left(
\frac{-\zeta'}\zeta(\sigma_0 + t i)
\right)
\mathcal M(\widetilde 1_\epsilon)(\sigma_0 + t i)
X^{\sigma_0 + t i}
\ i \ dt
\right|
$$

By Theorem [dlog-riemannZeta-bdd-on-vertical-lines](../part-01/dlog-riemannzeta-bdd-on-vertical-lines.md), $\zeta'/\zeta (\sigma_0 + t i)$ is bounded by $\zeta'/\zeta(\sigma_0)$, and Theorem [riemannZetaLogDerivResidue](../../zeta-bounds/part-01/riemannzetalogderivresidue.md) gives $\ll 1/(\sigma_0-1)$ for the latter. This gives:

$$
\leq
\frac{1}{2\pi}
\left|
\int_{-\infty}^{-T}
C \log X\cdot
\frac{C'}{\epsilon|\sigma_0 + t i|^2}
X^{\sigma_0}
\ dt
\right|
,
$$

where we used Theorem [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md). Continuing the calculation, we have

$$
\leq
\log X \cdot
C'' \frac{X^{\sigma_0}}{\epsilon}
\int_{-\infty}^{-T}
\frac{1}{t^2}
\ dt
\ \leq \
C''' \frac{X\log X}{\epsilon T}
,
$$

where we used that $\sigma_0=1+1/\log X$, and $X^{\sigma_0} = X\cdot X^{1/\log X}=e \cdot X$.

## Lean

Formalized as [`I1Bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I1Bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
