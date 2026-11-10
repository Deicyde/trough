---
declaration: lemma
origin: cited
lean: Smooth1Properties_below
statement: formalized
proof: formalized
---

# Smooth1Properties-below

Fix $\epsilon>0$. There is an absolute constant $c>0$ so that: If $0 < x \leq (1-c\epsilon)$, then

$$
\widetilde{1_{\epsilon}}(x) = 1.
$$

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [DeltaSpikeMass](deltaspikemass.md)
- [DeltaSpike](deltaspike.md)
- [MellinConvolution](mellinconvolution.md)

## Proof

Opening the definition, we have that the Mellin convolution of $1_{(0,1]}$ with $\nu_\epsilon$ is

$$
\int_0^\infty 1_{(0,1]}(y)\nu_\epsilon(x/y)\frac{dy}{y}
=
\int_0^1 \nu_\epsilon(x/y)\frac{dy}{y}.
$$

The support of $\nu_\epsilon$ is contained in $[1/2^\epsilon,2^\epsilon]$, so it suffices to consider $y \in [1/2^\epsilon x,2^\epsilon x]$ for nonzero contributions. If $x < 2^{-\epsilon}$, then the integral is the same as that over $(0,\infty)$:

$$
\int_0^1 \nu_\epsilon(x/y)\frac{dy}{y}
=
\int_0^\infty \nu_\epsilon(x/y)\frac{dy}{y},
$$

in which we change variables to $z=x/y$ (using $x>0$):

$$
\int_0^\infty \nu_\epsilon(x/y)\frac{dy}{y}
=
\int_0^\infty \nu_\epsilon(z)\frac{dz}{z},
$$

which is equal to one by Lemma [DeltaSpikeMass](deltaspikemass.md). We then choose

$$
c:=\log 2,
$$

which satisfies

$$
c > \frac{1-2^{-\epsilon}}\epsilon
$$

by Lemma Smooth1Properties_estimate, so

$$
1-c\epsilon < 2^{-\epsilon}.
$$

## Lean

Formalized as [`Smooth1Properties_below`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Smooth1Properties_below).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
