---
declaration: lemma
origin: cited
lean: Smooth1LeOne
statement: formalized
proof: formalized
---

# Smooth1LeOne

If $\nu$ is nonnegative and has mass one, then $\widetilde{1_{\epsilon}}(x)\le 1$, $\forall x>0$.

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

and since $1_{(0,1]}(y)\le 1$, and all the factors in the integrand are nonnegative,

$$
\widetilde{1_\epsilon}(x)\le\int_0^\infty \frac1\epsilon\nu((x/y)^{\frac1\epsilon}) \frac{dy}y
$$

(because in mathlib the integral of a non-integrable function is $0$, for the inequality above to be true, we must prove that $\nu((x/y)^{\frac1\epsilon})/y$ is integrable; this follows from the computation below). We then change variables to $z=(x/y)^{\frac1\epsilon}$:

$$
\widetilde{1_\epsilon}(x)\le\int_0^\infty \nu(z) \frac{dz}z
$$

which by Theorem [SmoothExistence](../part-02/smoothexistence.md) is 1.

## Lean

Formalized as [`Smooth1LeOne`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Smooth1LeOne).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
