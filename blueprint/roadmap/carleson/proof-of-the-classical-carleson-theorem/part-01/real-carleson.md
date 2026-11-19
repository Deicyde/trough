---
declaration: lemma
origin: cited
lean: rcarleson
statement: formalized
proof: formalized
---

# real Carleson

Let $F,G$ be Borel subsets of ${\mathbb{R}}$ with finite measure. Let $f$ be a bounded measurable function on ${\mathbb{R}}$ with $|f|\le \mathbf{1}_F$. Then

$$
\left|\int _G Tf(x) \, dx\right| \le C_{4,2} |F|^{\frac 12} |G|^{\frac 12} \, ,
$$

where

$$
T f(x)=\sup_{n\in \mathbb{Z}}
\sup_{r>0}\left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right|\, .\qquad\text{(9)}
$$

## Depends on

- [two-sided metric space Carleson](../../two-sided-metric-space-carleson/two-sided-metric-space-carleson.md)
- [real line doubling](../part-02/real-line-doubling.md)
- [real line metric](../part-02/real-line-metric.md)
- [real line measure](../part-02/real-line-measure.md)
- [oscillation control](../part-02/oscillation-control.md)
- [frequency monotone](../part-02/frequency-monotone.md)
- [frequency ball doubling](../part-02/frequency-ball-doubling.md)
- [frequency ball growth](../part-02/frequency-ball-growth.md)
- [integer ball cover](../part-02/integer-ball-cover.md)
- [real van der Corput](../part-02/real-van-der-corput.md)
- [Hilbert strong 2 2](hilbert-strong-2-2.md)
- [Hilbert kernel regularity](hilbert-kernel-regularity.md)
- [Hilbert kernel bound](hilbert-kernel-bound.md)

## Proof

*Proof of real Carleson.* The preceding chain of lemmas establishes that ${\Theta}$ is a cancellative, compatible collection of functions on $({\mathbb{R}}, \rho, \mu, 4)$. Again, some of the statements in these lemmas are stronger than what is needed for $a=4$, but can be relaxed to give the desired conclusion for $a=4$.

With $\kappa$ as near [(7)](README.md), define the function $K:{\mathbb{R}}\times {\mathbb{R}}\to \mathbb{C}$ as in Theorem [metric space Carleson](../../introduction/metric-space-carleson.md) by

$$
K(x,y):=\kappa(x-y)\, .
$$

The function $K$ is continuous outside the diagonal $x=y$ and vanishes on the diagonal. Hence it is measurable.

By [Hilbert kernel bound](hilbert-kernel-bound.md) and [Hilbert kernel regularity](hilbert-kernel-regularity.md), it follows that $K$ is a two-sided Calderón–Zygmund kernel on $({\mathbb{R}},\rho,\mu,4)$. [Hilbert strong 2 2](hilbert-strong-2-2.md) verifies [(3)](../../two-sided-metric-space-carleson/two-sided-metric-space-carleson.md). Thus the assumptions of [two-sided metric space Carleson](../../two-sided-metric-space-carleson/two-sided-metric-space-carleson.md) are all satisfied. Applying the Theorem, real Carleson follows.

## Lean

Formalized as [`rcarleson`](https://fpvandoorn.github.io/carleson/docs/find/#doc/rcarleson).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8283](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8283)
