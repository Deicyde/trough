---
declaration: lemma
origin: cited
lean: I4GenBound
statement: formalized
proof: formalized
---

# I4GenBound

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md), we have that

$$
\left|I_4(\nu,\epsilon,X,\sigma_1,\sigma_2)\right|
\ll\frac{X}{\epsilon}\,X^{-\frac{A}{(\log T)^{n_1}}}.
$$

## Depends on

- [I₄](../part-01/i4.md)

## Proof depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md)

## Proof

The analysis of $I_4$ is similar to that of $I_2$, (in Lemma I2Bound) but even easier. Let $C$ be the sup of $-\zeta'/\zeta$ on the curve $\sigma_2 + 3 i$ to $1+ 3i$ (this curve is compact, and away from the pole at $s=1$). Apply Theorem [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md) to get the bound $1/(\epsilon |s|^2)$, which is bounded by $C'/\epsilon$. And $X^s$ is bounded by $X^{\sigma_1}=X \cdot X^{-A/ \log T^{n_1}}$. Putting these together gives the result.

## Lean

Formalized as [`I4GenBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I4GenBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
