---
declaration: lemma
origin: cited
lean: modulated_averaged_projection
statement: formalized
proof: formalized
---

# modulated averaged projection

We have for every bounded measurable $2\pi$-periodic function $g$

$$
\|L_Ng\|_{L^2[0, 2\pi]}\le \|g\|_{L^2[0, 2\pi]}\,.\qquad\text{(23)}
$$

## Depends on

- [spectral projection bound](spectral-projection-bound.md)

## Proof

We have

$$
\|M_ng\|_{L^2[0, 2\pi]}^2=\int_{0}^{2\pi} |e^{inx}g(x)|^2\, dx
=\int_{0}^{2\pi} |g(x)|^2\, dx=\|g\|_{L^2[0, 2\pi]}^2\, .\qquad\text{(24)}
$$

We have by the triangle inequality, the square root of the identity in (24), and [spectral projection bound](spectral-projection-bound.md)

$$
\|L_ng\|_{L^2[0, 2\pi]}=\|\frac 1N\sum_{n=0}^{N-1}
M_{n+N} S_{N+n}M_{-N-n}g\|_{L^2[0, 2\pi]}
$$

$$
\le \frac 1N\sum_{n=0}^{N-1} \|
M_{n+N} S_{N+n}M_{-N-n}g\|_{L^2[0, 2\pi]}
= \frac 1N\sum_{n=0}^{N-1} \|
S_{N+n}M_{-N-n}g\|_{L^2[0, 2\pi]}
$$

$$
\le \frac 1N\sum_{n=0}^{N-1} \|
M_{-N-n}g\|_{L^2[0, 2\pi]} = \frac 1N\sum_{n=0}^{N-1} \|
g\|_{L^2[0, 2\pi]} =\|g\|_{L^2[0, 2\pi]}\, .
$$

This proves (23) and completes the proof of the lemma.

## Lean

Formalized as [`modulated_averaged_projection`](https://fpvandoorn.github.io/carleson/docs/find/#doc/modulated_averaged_projection).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8594](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8594)
