---
declaration: lemma
origin: cited
lean: I2GenBound
statement: formalized
proof: formalized
---

# I2GenBound

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md) we have that

$$
\left|I_2(\nu,\epsilon,X,T)\right|\ll\frac{X}{\epsilon T}.
$$

## Depends on

- [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md)
- [I₂](../part-01/i2.md)

## Proof depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [IBound-aux1](ibound-aux1.md)
- [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md)

## Proof

Unfold the definitions and apply the triangle inequality.

$$
\left|I_2(\nu, \epsilon, X, T, \sigma_1)\right|=
\left|\frac{1}{2\pi i}\int_{\sigma_1}^{\sigma_0}
\left(\frac{-\zeta'}\zeta(\sigma - T i) \right) \cdot
\mathcal M(\widetilde 1_\epsilon)(\sigma - T i) \cdot
X^{\sigma - T i}
\ d\sigma
\right|
$$

$$
\leq
\frac{1}{2\pi}
\int_{\sigma_1}^{\sigma_0}
C \cdot \log T ^{n_2}
\frac{C'}{\epsilon|\sigma - T i|^2}
X^{\sigma_0}
\ d\sigma
\leq
C'' \cdot \frac{X\log T^{n_2}}{\epsilon T^2}
,
$$

where we used Theorems [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md), the hypothesised bound on zeta and the fact that $X^\sigma \le X^{\sigma_0} = X\cdot X^{1/\log X}=e \cdot X$. Since $T>3$, we have $\log T^{n_2} \leq C''' T$.

## Lean

Formalized as [`I2GenBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I2GenBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
