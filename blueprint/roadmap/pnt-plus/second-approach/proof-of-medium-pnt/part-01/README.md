---
navigation: transparent
---

# ChebyshevPsi to SmoothedChebyshevPull1-aux-integ…

- [ChebyshevPsi](chebyshevpsi.md)

It has already been established that zeta doesn't vanish on the 1 line, and has a pole at $s=1$ of order 1. We also have the following.

- [LogDerivativeDirichlet](logderivativedirichlet.md)

The main object of study is the following inverse Mellin-type transform, which will turn out to be a smoothed Chebyshev function.

- [SmoothedChebyshev](smoothedchebyshev.md)
- [SmoothedChebyshevDirichlet-aux-integrable](smoothedchebyshevdirichlet-aux-integrable.md)
- [SmoothedChebyshevDirichlet-aux-tsum-integral](smoothedchebyshevdirichlet-aux-tsum-integral.md)
- [SmoothedChebyshevDirichlet](smoothedchebyshevdirichlet.md)

The smoothed Chebyshev function is close to the actual Chebyshev function.

- [SmoothedChebyshevClose](smoothedchebyshevclose.md)
- [LogDerivZetaHasBound](logderivzetahasbound.md)

Suppose we have an estimate of the form in Definition [LogDerivZetaHasBound](logderivzetahasbound.md). Returning to the definition of $\psi_{\epsilon}$, fix a large $T$ to be chosen later, and set $\sigma_0 = 1 + 1 / log X$, $\sigma_1 = 1- A/ \log T^{n_1}$ (where $n_1$ comes from our estimate from Definition [LogDerivZetaHasBound](logderivzetahasbound.md)), and $\sigma_2\lt \sigma_1$ a constant. Pull contours (via rectangles!) to go from $\sigma_0-i\infty$ up to $\sigma_0-iT$, then over to $\sigma_1-iT$, up to $\sigma_1-3i$, over to $\sigma_2-3i$, up to $\sigma_2+3i$, back over to $\sigma_1+3i$, up to $\sigma_1+iT$, over to $\sigma_0+iT$, and finally up to $\sigma_0+i\infty$.

In the process, we will pick up the residue at $s=1$. We will do this in several stages. Here the interval integrals are defined as follows:

- [I₁](i1.md)
- [I₂](i2.md)
- [I₃₇](i37.md)
- [I₈](i8.md)
- [I₉](i9.md)
- [I₃](i3.md)
- [I₇](i7.md)
- [I₄](i4.md)
- [I₆](i6.md)
- [I₅](i5.md)
- [dlog-riemannZeta-bdd-on-vertical-lines](dlog-riemannzeta-bdd-on-vertical-lines.md)
- [SmoothedChebyshevPull1-aux-integrable](smoothedchebyshevpull1-aux-integrable.md)
