---
declaration: lemma
origin: cited
lean: I3GenBound
statement: formalized
proof: formalized
---

# I3GenBound

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md), we have that

$$
\left|I_3(\nu,\epsilon,X,T)\right|\ll\frac{X}{\epsilon}\, X^{-\frac{A}{(\log T)^{n_1}}}.
$$

## Depends on

- [I₃](../part-01/i3.md)
- [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md)

## Proof depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md)
- [log-pow-over-xsq-integral-bounded](log-pow-over-xsq-integral-bounded.md)

## Proof

Unfold the definitions and apply the triangle inequality.

$$
\left|I_{3}(\nu, \epsilon, X, T, \sigma_1)\right| =
\left|\frac{1}{2\pi i} \int_{-T}^3
\left(\frac{-\zeta'}\zeta(\sigma_1 + t i) \right)
\mathcal M(\widetilde 1_\epsilon)(\sigma_1 + t i)
X^{\sigma_1 + t i}
\ i \ dt
\right|
$$

$$
\leq
\frac{1}{2\pi}
\int_{-T}^3
C \cdot\log t^{n_2}
\frac{C'}{\epsilon|\sigma_1 + t i|^2}
X^{\sigma_1}
\ dt
,
$$

where we used Theorems [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md) and the hypothesised bound on zeta. Now we estimate $X^{\sigma_1} = X \cdot X^{-A/ \log T^{n_1}}$, and the integral is absolutely bounded.

## Lean

Formalized as [`I3GenBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I3GenBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
