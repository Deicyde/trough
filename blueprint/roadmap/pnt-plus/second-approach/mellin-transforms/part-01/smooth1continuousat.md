---
declaration: lemma
origin: cited
lean: Smooth1ContinuousAt
statement: formalized
proof: formalized
---

# Smooth1ContinuousAt

Fix a nonnegative, continuously differentiable function $F$ on $\mathbb{R}$ with support in $[1/2,2]$. Then for any $\epsilon>0$, the function $x \mapsto \int_{(0,\infty)} x^{1+it} \widetilde{1_{\epsilon}}(x) dx$ is continuous at any $y>0$.

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [DeltaSpike](deltaspike.md)
- [MellinConvolution](mellinconvolution.md)
- [MellinConvolutionSymmetric](mellinconvolutionsymmetric.md)

## Proof

Use Lemma MellinconvolutionSymmetric to write $\widetilde{1_{\epsilon}}(x)$ as an integral over an integral near $1$, in particular avoiding the singularity at $0$. The integrand may be bounded by $2^{\epsilon}\nu_\epsilon(t)$ which is independent of $x$ and we can use dominated convergence to prove continuity.

## Lean

Formalized as [`Smooth1ContinuousAt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Smooth1ContinuousAt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
