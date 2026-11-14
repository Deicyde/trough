---
declaration: lemma
origin: cited
lean: smul_C2_1_2
statement: formalized
proof: formalized
---

# wiggle order 2

Let $n, m \ge 1$ and $k > 0$. If ${\mathfrak p}, {\mathfrak p}' \in {\mathfrak P}$ with ${\mathcal{I}}({\mathfrak p}) \ne {\mathcal{I}}({\mathfrak p}')$ and

$$
n {\mathfrak p} \lesssim k {\mathfrak p}'\qquad\text{(37)}
$$

then

$$
(n + 2^{-95 a} m) {\mathfrak p} \lesssim m{\mathfrak p}'\,.\qquad\text{(38)}
$$

## Depends on

- [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

## Proof

The assumption (37) together with the definition [(23)](../../proof-of-metric-space-carleson-overview/README.md) of $\lesssim$ implies that ${\mathcal{I}}({\mathfrak p}) \subsetneq {\mathcal{I}}({\mathfrak p}')$. Let ${\vartheta} \in B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), m)$. Then we have by the triangle inequality

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\vartheta}) \le d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak p}')) + d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}'), {\vartheta})
$$

The first summand is bounded by $n$ since

$$
{\mathcal{Q}}({\mathfrak p}') \in B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), k) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), n),
$$

using [(23)](../../proof-of-metric-space-carleson-overview/README.md). For the second summand we use [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) to show that the sum is estimated by

$$
n + 2^{-95a} d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'), {\vartheta}) < n + 2^{-95a} m\,.
$$

Thus $B_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak p}'),m) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),n + 2^{-95a}m)$. Combined with ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak p}')$, this yields (38).

## Lean

Formalized as [`smul_C2_1_2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/smul_C2_1_2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2645](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2645)
