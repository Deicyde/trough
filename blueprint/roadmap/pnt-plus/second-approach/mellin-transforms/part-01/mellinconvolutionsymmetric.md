---
declaration: lemma
origin: cited
lean: MellinConvolutionSymmetric
statement: formalized
proof: formalized
---

# MellinConvolutionSymmetric

Let $f$ and $g$ be functions from $\mathbb{R}_{>0}$ to $\mathbb{R}$ or $\mathbb{C}$, for $x\neq0$,

$$
(f\ast g)(x)=(g\ast f)(x)
.
$$

## Depends on

- [MellinConvolution](mellinconvolution.md)

## Proof

By Definition [MellinConvolution](mellinconvolution.md),

$$
(f\ast g)(x) = \int_0^\infty f(y)g(x/y)\frac{dy}{y}
$$

in which we change variables to $z=x/y$:

$$
(f\ast g)(x) = \int_0^\infty f(x/z)g(z)\frac{dz}{z}
=(g\ast f)(x)
.
$$

## Lean

Formalized as [`MellinConvolutionSymmetric`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinConvolutionSymmetric).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/MellinCalculus.lean)
