---
declaration: lemma
origin: cited
lean: TileStructure.Forest.tree_projection_estimate
statement: formalized
proof: formalized
---

# tree projection estimate

Let ${\mathfrak u} \in {\mathfrak U}$. Then we have for all $f, g$ bounded with bounded support

$$
\Bigg|\int_X \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} \bar g(y) T_{{\mathfrak p}}f(y) \, \mathrm{d}\mu(y) \Bigg|
$$

$$
\le 2^{130a^3}\|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|\|_{2}\|P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))}|g|\|_{2}.\qquad\text{(10)}
$$

## Depends on

- [dyadic partitions](dyadic-partitions.md)
- [pointwise tree estimate](pointwise-tree-estimate.md)
- [nontangential operator bound](nontangential-operator-bound.md)
- [boundary operator bound](boundary-operator-bound.md)

## Proof

*Proof of tree projection estimate.* Let $L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))$. Let $b(x')$ denote the right-hand side of [pointwise tree estimate](pointwise-tree-estimate.md). Apply this lemma to $e({\mathcal{Q}}({\mathfrak u})) f$, to obtain for all $y, x' \in L$

$$
\Bigg| \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(y) \Bigg| \le b(x').
$$

Hence, by taking an infimum, we have for $y \in L$

$$
\Bigg| \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(y) \Bigg| \le \inf_{x' \in L} b(x').
$$

Integrating this estimate yields

$$
\int_L |g(y)| \Bigg| \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(y) \Bigg| \, \mathrm{d}\mu(y)
$$

$$
\le \int_L |g(y)| \times \inf_{x' \in L} b(x') \, \mathrm{d}\mu(y)
$$

$$
=   \int_L P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))}|g|(y) \times \inf_{x' \in L} b(x') \, \mathrm{d}\mu(y)
$$

$$
\le \int_L P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))}|g|(y) \times  b(y) \, \mathrm{d}\mu(y)
$$

By [(20)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md), we have $T_{{\mathfrak p}} f = \mathbf{1}_{{\mathcal{I}}({\mathfrak p})} T_{{\mathfrak p}} f$ for all ${\mathfrak p} \in {\mathfrak P}$, so

$$
\Bigg| \int \bar g(y) \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(y) \, \mathrm{d}\mu(y) \Bigg| = \Bigg| \int_{\bigcup_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} {\mathcal{I}}({\mathfrak p})} \bar g(y) \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(y) \, \mathrm{d}\mu(y) \Bigg|\,.
$$

Since $\mathcal{L}({\mathfrak T}({\mathfrak u}))$ partitions $\bigcup_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} {\mathcal{I}}({\mathfrak p})$ by [dyadic partitions](dyadic-partitions.md), we get from the triangle inequality

$$
\le \sum_{L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))} \int_L |g(y)| \Bigg| \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}} f(y) \Bigg| \, \mathrm{d}\mu(y)
$$

which by the above computation is bounded by

$$
\sum_{L \in \mathcal{L}({\mathfrak T}({\mathfrak u}))} \int_L P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))}|g|(y) \times  b(y) \, \mathrm{d}\mu(y)
$$

$$
= \int_X P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))}|g|(y) \times  b(y) \, \mathrm{d}\mu(y)
$$

Applying Cauchy-Schwarz, this is bounded by $\|P_{\mathcal{L}({\mathfrak T}({\mathfrak u}))}|g|\|_2 \times \|b\|_2$. By Minkowski's inequality, [Hardy–Littlewood](../../proof-of-metric-space-carleson-overview/hardy-littlewood.md), [nontangential operator bound](nontangential-operator-bound.md) and [boundary operator bound](boundary-operator-bound.md), $\|b\|_2$ is at most

$$
2^{129a^3} (2^{2a+1} + 2^{12a})\|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|\|_2 + 2^{103a^3} \|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}[e({\mathcal{Q}}({\mathfrak u}))f]\|_2\,.
$$

By the triangle inequality we have for all $x \in X$ that $|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}[e({\mathcal{Q}}({\mathfrak u}))f]|(x) \le P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|(x)$, thus we can further estimate the above by

$$
(2^{129a^3} (2^{2a+1} + 2^{12a}) + 2^{103a^3}) \|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}))}|f|\|_2\,.
$$

This completes the proof since $a \ge 4$.

## Lean

Formalized as [`TileStructure.Forest.tree_projection_estimate`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.tree_projection_estimate).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 4695](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L4695)
