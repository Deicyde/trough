---
declaration: lemma
origin: cited
lean: TileStructure.Forest.correlation_near_tree_parts
statement: formalized
proof: formalized
---

# correlation near tree parts

We have for all ${\mathfrak u}_1 \ne {\mathfrak u}_2 \in {\mathfrak U}$ with ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$ and all bounded $g_1, g_2$ with bounded support

$$
\left| \int_X \sum_{{\mathfrak p}_1 \in {\mathfrak T}({\mathfrak u}_1)} \sum_{{\mathfrak p}_2 \in {\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}} T^*_{{\mathfrak p}_1}g_1 \overline{T^*_{{\mathfrak p}_2}g_2 }\,\mathrm{d}\mu \right|\qquad\text{(33)}
$$

$$
\le 2^{232a^3+21a+5} 2^{-\frac{25}{101a}Zn\kappa} \prod_{j=1}^2 \|S_{2, {\mathfrak u}_j} g_j\|_{L^2({\mathcal{I}}({\mathfrak u}_1))}\,.\qquad\text{(34)}
$$

## Depends on

- [tree projection estimate](tree-projection-estimate.md)
- [dyadic partition 2](../part-02/dyadic-partition-2.md)
- [bound for tree projection](../part-02/bound-for-tree-projection.md)

## Proof

*Proof of correlation near tree parts.* By [tree projection estimate](tree-projection-estimate.md) and [adjoint tile support](adjoint-tile-support.md), we have

$$
\begin{aligned}
\eqref{eq-lhs-small-sep-tree} \le 2^{130a^3} \|P_{\mathcal{L}({\mathfrak T}({\mathfrak u}_1))} |\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)}g_1| \|_2 \|P_{\mathcal{J}({\mathfrak T}({\mathfrak u}_1) )}|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} T_{{\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}}^* g_2|\|_2\,.
\end{aligned}
$$

It follows from the definition of the projection operator $P$ and Jensen's inequality that

$$
\|P_{\mathcal{L}({\mathfrak T}({\mathfrak u}_1))} |g_1\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)}| \|_2 \le \|g_1 \mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)}\|_2\,.
$$

By [dyadic partition 2](../part-02/dyadic-partition-2.md), a cube $J \in \mathcal{J}({\mathfrak T}({\mathfrak u}_1))$ intersects ${\mathcal{I}}({\mathfrak u}_1)$ if and only if $J \in \mathcal{J}'$. Thus

$$
P_{\mathcal{J}({\mathfrak T}({\mathfrak u}_1) )}|\mathbf{1}_{{\mathcal{I}}({\mathfrak u}_1)} T_{{\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}}^* g_2| = P_{\mathcal{J}'}|T_{{\mathfrak T}({\mathfrak u}_2) \setminus \mathfrak{S}}^* g_2|\,.
$$

Combining this with [bound for tree projection](../part-02/bound-for-tree-projection.md), the definition [(2)](../../proof-of-metric-space-carleson-overview/README.md) and $a \ge 4$ proves the lemma.

## Lean

Formalized as [`TileStructure.Forest.correlation_near_tree_parts`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.correlation_near_tree_parts).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5342](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5342)
