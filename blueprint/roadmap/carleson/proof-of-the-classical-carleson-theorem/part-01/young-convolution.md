---
declaration: lemma
origin: cited
lean: young_convolution
statement: formalized
proof: formalized
---

# Young convolution

Let $f$ and $g$ be two bounded non-negative measurable $2\pi$-periodic functions on ${\mathbb{R}}$. Then

$$
\left(\int_0^{2\pi} \left(\int_0^{2\pi}
f(y)g(x-y)\, dy\right)^2\, dx\right)^{\frac 12}\le \|f\|_{L^2[0, 2\pi]} \|g\|_{L^1[0, 2\pi]}\, .\qquad\text{(26)}
$$

## Depends on

- [periodic domain shift](periodic-domain-shift.md)

## Proof

Using Fubini and [periodic domain shift](periodic-domain-shift.md), we observe

$$
\int_0^{2\pi}\int_0^{2\pi}f(y)^2g(x-y)\, dy
\, dx=\int_0^{2\pi}f(y)^2\int_0^{2\pi}g(x-y)\, dx
\, dy
$$

$$
=\int_0^{2\pi}f(y)^2\int_0^{2\pi}g(x) \, dx
dy
=\|f\|_{L^2[0, 2\pi]}^2\|g\|_{L^1[0, 2\pi]}\, .\qquad\text{(27)}
$$

Let $h$ be the nonnegative square root of $g$, then $h$ is bounded and $2\pi$-periodic with $h^2=g$. We estimate the square of the left-hand side of (26) with Cauchy-Schwarz and then with (27) by

$$
\int_0^{2\pi} (\int_0^{2\pi}f(y)h(x-y)h(x-y)\, dy)^2\, dx
$$

$$
\le \int_0^{2\pi}\left(\int_0^{2\pi}f(y)^2g(x-y)\, dy\right)
\left(\int_0^{2\pi}g(x-y)\, dy\right)\, dx
$$

$$
= \|f\|_{L^2[0, 2\pi]}^2\|g\|_{L^1[0, 2\pi]}^2\, .
$$

Taking square roots, this proves the lemma.

## Lean

Formalized as [`young_convolution`](https://fpvandoorn.github.io/carleson/docs/find/#doc/young_convolution).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8662](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8662)
