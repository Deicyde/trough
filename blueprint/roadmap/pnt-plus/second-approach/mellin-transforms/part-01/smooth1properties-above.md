---
declaration: lemma
origin: cited
lean: Smooth1Properties_above
statement: formalized
proof: formalized
---

# Smooth1Properties-above

Fix $0\lt \epsilon<1$. There is an absolute constant $c>0$ so that: if $x\geq (1+c\epsilon)$, then

$$
\widetilde{1_{\epsilon}}(x) = 0.
$$

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [DeltaSpike](deltaspike.md)
- [MellinConvolution](mellinconvolution.md)

## Proof

Again the Mellin convolution is

$$
\int_0^1 \nu_\epsilon(x/y)\frac{dy}{y},
$$

but now if $x > 2^\epsilon$, then the support of $\nu_\epsilon$ is disjoint from the region of integration, and hence the integral is zero. We choose

$$
c:=2\log 2
.
$$

By Lemma Smooth1Properties\_estimate,

$$
c > 2\frac{1-2^{-\epsilon}}\epsilon > 2^\epsilon\frac{1-2^{-\epsilon}}\epsilon
=
\frac{2^\epsilon-1}\epsilon,
$$

so

$$
1+c\epsilon > 2^\epsilon.
$$

## Lean

Formalized as [`Smooth1Properties_above`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Smooth1Properties_above).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
