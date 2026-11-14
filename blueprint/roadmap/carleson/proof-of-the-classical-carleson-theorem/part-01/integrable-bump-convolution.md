---
declaration: lemma
origin: cited
lean: integrable_bump_convolution
statement: formalized
proof: formalized
---

# integrable bump convolution

Let $g,f$ be bounded measurable $2\pi$-periodic functions. Let $0\lt r\lt \pi$. Assume we have for all $x$

$$
|g(x)|\le k_r(x)\, .\qquad\text{(28)}
$$

Let

$$
h(x)= \int_0^{2\pi} f(y)g(x-y)\, dy \, .
$$

Then

$$
\|h\|_{L^2[0, 2\pi]}\le 17\|f\|_{L^2[-\pi, \pi]} \, .
$$

## Depends on

- [Young convolution](young-convolution.md)

## Proof

From monotonicity of the integral and (28),

$$
\|g\|_{L^1[0, 2\pi]} \le \int_0^{2\pi}k_r(x)\, dx\,.
$$

Using the symmetry $k_r(x)=k_r(-x)$, the assumption, and [lower secant bound](lower-secant-bound.md), the last display is equal to

$$
= 2 \int_0^\pi \min\left(\frac 1r, 1+\frac r{|1-e^{ix}|^2}\right)\, dx
$$

$$
\le 2\int_0^{r} \frac 1r \, dx+2\int_r^{\pi}1+\frac {64r}{x^2}\, dx
$$

$$
\le 2+2\pi + 2\left(\frac {4r}r-\frac {4r}{\pi}\right)
\le 17\, .
$$

Together with [Young convolution](young-convolution.md), this proves the lemma.

## Lean

Formalized as [`integrable_bump_convolution`](https://fpvandoorn.github.io/carleson/docs/find/#doc/integrable_bump_convolution).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8708](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8708)
