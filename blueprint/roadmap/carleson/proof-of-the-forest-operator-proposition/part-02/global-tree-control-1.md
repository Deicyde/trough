---
declaration: lemma
origin: cited
lean: TileStructure.Forest.global_tree_control1_edist_left, TileStructure.Forest.global_tree_control1_edist_right, TileStructure.Forest.global_tree_control1_supbound
statement: formalized
proof: formalized
---

# global tree control 1

Let ${\mathfrak C}_1 = {\mathfrak T}({\mathfrak u}_1)$ and ${\mathfrak C}_2 = {\mathfrak T}({\mathfrak u}_2) \cap \mathfrak{S}$. Then for $i = 1,2$ and each $J \in \mathcal{J}'$ and all bounded $g$ with bounded support, we have

$$
\begin{aligned}
\sup_{B'(J)} |T_{{\mathfrak C}_i}^*g| \leq \inf_{B^\circ{}(J)} |T^*_{{\mathfrak C}_i} g| + 2^{128a^3+4a+3} \inf_{J} M_{\mathcal{B}, 1} |g|\qquad\text{(53)}\end{aligned}
$$

and for all $y,y' \in B'(J)$

$$
|e({\mathcal{Q}}({\mathfrak u}_i)(y)) T_{{\mathfrak C}_i}^* g(y) - e({\mathcal{Q}}({\mathfrak u}_i)(y')) T_{{\mathfrak C}_i}^* g(y')|
$$

$$
\le 2^{128a^3+4a+1} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} \inf_J M_{\mathcal{B},1} |g|\,.\qquad\text{(54)}
$$

## Depends on

- [Holder correlation tile](holder-correlation-tile.md)
- [scales impacting interval](scales-impacting-interval.md)

## Proof

Note that (53) follows from (54), since for $y'\in B^\circ{}(J)$, by the triangle inequality,

$$
\left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a}\le \Big(16 + \frac{1}8\Big)^{1/a}\le 2^2.
$$

By the triangle inequality, [adjoint tile support](../part-01/adjoint-tile-support.md) and [Holder correlation tile](holder-correlation-tile.md), we have for all $y, y' \in B'(J)$

$$
|e({\mathcal{Q}}({\mathfrak u}_i)(y)) T_{{\mathfrak C}_i}^* g(y) - e({\mathcal{Q}}({\mathfrak u}_i)(y')) T_{{\mathfrak C}_i}^* g(y')|\qquad\text{(55)}
$$

$$
\le \sum_{\substack{{\mathfrak p} \in {\mathfrak C}_i\\ B({\mathcal{I}}({\mathfrak p})) \cap B'(J) \neq \emptyset}} |e({\mathcal{Q}}({\mathfrak u}_i)(y)) T_{{\mathfrak p}}^* g(y) - e({\mathcal{Q}}({\mathfrak u}_i)(y')) T_{{\mathfrak p}}^* g(y')|
$$

$$
\le 2^{128a^3}\rho(y,y')^{1/a} \sum_{\substack{{\mathfrak p} \in {\mathfrak C}_i\\ B({\mathcal{I}}({\mathfrak p})) \cap B'(J) \neq \emptyset}} \frac{D^{- {\mathrm{s}}({\mathfrak p})/a}}{\mu(B({\mathrm{c}}({\mathfrak p}), 4D^{{\mathrm{s}}({\mathfrak p})}))} \int_{E({\mathfrak p})} |g| \, \mathrm{d}\mu\,.
$$

By [scales impacting interval](scales-impacting-interval.md), we have ${\mathrm{s}}({\mathfrak p}) \ge s(J)$ for all ${\mathfrak p}$ occurring in the sum. Further, for each $s \ge s(J)$, the sets $E({\mathfrak p})$ for ${\mathfrak p} \in {\mathfrak P}$ with ${\mathrm{s}}({\mathfrak p}) = s$ are pairwise disjoint by [(19)](../../proof-of-metric-space-carleson-overview/discrete-carleson.md) and [(13)](../../proof-of-metric-space-carleson-overview/README.md), and contained in $B(c(J), 32D^{s})$ by [(10)](../../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality. Using also the doubling estimate [(5)](../../introduction/README.md), we obtain that the expression in the last display can be estimated by

$$
2^{128a^3}\rho(y,y')^{1/a} \sum_{S \ge s \ge s(J)} D^{-s/a} \frac{2^{4a}}{\mu(B(c(J), 32D^{s}))} \int_{B(c(J), 32D^{s})} |g| \, \mathrm{d}\mu
$$

$$
\le 2^{128a^3+4a} \left(\frac{\rho(y,y')}{D^{s(J)}}\right)^{1/a} \sum_{S \ge s \ge s(J)} D^{(s(J) - s)/a} \inf_J M_{\mathcal{B},1} |g|\,.
$$

Since $D^{-1/a}\le\frac12$, we have

$$
\sum_{S \ge s \ge s(J)} D^{(s(J) - s)/a} \le 2.
$$

Estimate (54), and therefore the lemma, follow.

## Lean

Formalized as [`TileStructure.Forest.global_tree_control1_edist_left`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.global_tree_control1_edist_left), [`TileStructure.Forest.global_tree_control1_edist_right`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.global_tree_control1_edist_right), [`TileStructure.Forest.global_tree_control1_supbound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.global_tree_control1_supbound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5802](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5802)
