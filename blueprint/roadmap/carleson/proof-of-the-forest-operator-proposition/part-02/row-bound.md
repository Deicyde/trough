---
declaration: lemma
origin: cited
lean: TileStructure.Forest.row_bound, TileStructure.Forest.indicator_row_bound
statement: formalized
proof: formalized
---

# row bound

For each $1 \le j \le 2^n$ and each bounded $g$ supported on $G$ we have

$$
\left\| T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{182a^3} 2^{-n/2} \|g\|_2\qquad\text{(60)}
$$

and

$$
\left\| \mathbf{1}_F T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{283a^3} 2^{-n/2} \operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u}))^{1/2} \|g\|_2\,.\qquad\text{(61)}
$$

## Depends on

- [adjoint tile support](../part-01/adjoint-tile-support.md)
- [adjoint tree estimate](../part-01/adjoint-tree-estimate.md)

## Proof

Since for each $j$ the top cubes ${\mathcal{I}}({\mathfrak u})$, ${\mathfrak u} \in {\mathfrak U}_j$ are disjoint, we have for all bounded $g$ supported on $G$ by [adjoint tile support](../part-01/adjoint-tile-support.md)

$$
\left\|\mathbf{1}_F \sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* g\right\|_2^2 = \left\|\mathbf{1}_F \sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} T_{{\mathfrak p}}^* \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} g\right\|_2^2
$$

$$
= \sum_{{\mathfrak u} \in {\mathfrak U}_j} \int_{{\mathcal{I}}({\mathfrak u})} \left| \mathbf{1}_F \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} g\right|^2 \, \mathrm{d}\mu
\le \sum_{{\mathfrak u} \in {\mathfrak U}_j} \left\|\mathbf{1}_F \sum_{{\mathfrak p} \in {\mathfrak T}({\mathfrak u})} T_{{\mathfrak p}}^* \mathbf{1}_G \mathbf{1}_{{\mathcal{I}}({\mathfrak u})}  g\right\|_2^2\,.
$$

Applying [adjoint tree estimate](../part-01/adjoint-tree-estimate.md) and the density assumption [(33)](../../proof-of-metric-space-carleson-overview/README.md), then taking square roots, we obtain

$$
\left\| \mathbf{1}_F T_{\mathfrak{R}_j}^*g \right\|_2 \le 2^{282a^3} 2^{(4a+1-n)/2} \operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u}))^{1/2} \left( \sum_{{\mathfrak u} \in {\mathfrak U}_j} \left\| \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} g\right\|_2^2 \right)^{1/2}\,.
$$

Again by disjointedness of the cubes ${\mathcal{I}}({\mathfrak u})$, this is estimated by

$$
2^{282a^3} 2^{(4a+1-n)/2} \operatorname{\operatorname{dens}}_2(\bigcup_{{\mathfrak u}\in {\mathfrak U}}{\mathfrak T}({\mathfrak u}))^{1/2} \|g\|_2\,.
$$

Thus (61) follows, since $a \ge 4$. The proof of (60) is the same up to replacing $F$ by $X$.

## Lean

Formalized as [`TileStructure.Forest.row_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.row_bound), [`TileStructure.Forest.indicator_row_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.indicator_row_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6271](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6271)
