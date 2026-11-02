---
declaration: lemma
origin: cited
lean: Smooth1Nonneg
statement: formalized
proof: formalized
---

# Smooth1Nonneg

If $\nu$ is nonnegative, then $\widetilde{1_{\epsilon}}(x)$ is nonnegative.

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [DeltaSpike](deltaspike.md)
- [MellinConvolution](mellinconvolution.md)

## Proof

By Definitions [Smooth1](smooth1.md), [MellinConvolution](mellinconvolution.md) and [DeltaSpike](deltaspike.md)

$$
\widetilde{1_\epsilon}(x)
=\int_0^\infty 1_{(0,1]}(y)\frac1\epsilon\nu((x/y)^{\frac1\epsilon}) \frac{dy}y
$$

and all the factors in the integrand are nonnegative.

## Lean

Formalized as [`Smooth1Nonneg`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Smooth1Nonneg).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
