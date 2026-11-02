---
declaration: theorem
origin: cited
lean: MellinConvolutionTransform
statement: formalized
proof: formalized
---

# MellinConvolutionTransform

Let $f$ and $g$ be functions from $\mathbb{R}_{>0}$ to $\mathbb{C}$ such that

$$
(x,y)\mapsto f(y)\frac{g(x/y)}yx^{s-1}\qquad\text{(1)}
$$

is absolutely integrable on $[0,\infty)^2$. Then

$$
\mathcal{M}(f\ast g)(s) = \mathcal{M}(f)(s)\mathcal{M}(g)(s).
$$

## Depends on

- [MellinConvolution](mellinconvolution.md)

## Proof

By Definitions MellinTransform and [MellinConvolution](mellinconvolution.md)

$$
\mathcal M(f\ast g)(s)=
\int_0^\infty \int_0^\infty f(y)g(x/y)x^{s-1}\frac{dy}ydx
$$

By (1) and Fubini's theorem,

$$
\mathcal M(f\ast g)(s)=
\int_0^\infty \int_0^\infty f(y)g(x/y)x^{s-1}dx\frac{dy}y
$$

in which we change variables from $x$ to $z=x/y$:

$$
\mathcal M(f\ast g)(s)=
\int_0^\infty \int_0^\infty f(y)g(z)y^{s-1}z^{s-1}dzdy
$$

which, by Definition MellinTransform, is

$$
\mathcal M(f\ast g)(s)=
\mathcal M(f)(s)\mathcal M(g)(s)
.
$$

## Lean

Formalized as [`MellinConvolutionTransform`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinConvolutionTransform).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
