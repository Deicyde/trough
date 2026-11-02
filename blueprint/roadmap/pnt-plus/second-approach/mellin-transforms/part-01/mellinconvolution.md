---
declaration: definition
origin: cited
lean: MellinConvolution
statement: formalized
---

# MellinConvolution

Let $f$ and $g$ be functions from $\mathbb{R}_{>0}$ to $\mathbb{C}$. Then we define the Mellin convolution of $f$ and $g$ to be the function $f\ast g$ from $\mathbb{R}_{>0}$ to $\mathbb{C}$ defined by

$$
(f\ast g)(x) = \int_0^\infty f(y)g(x/y)\frac{dy}{y}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MellinConvolution`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinConvolution).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
