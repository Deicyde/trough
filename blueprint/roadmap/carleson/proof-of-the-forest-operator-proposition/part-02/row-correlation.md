---
declaration: lemma
origin: cited
lean: TileStructure.Forest.row_correlation
statement: formalized
proof: formalized
---

# row correlation

For all $1 \le j,j' \le 2^n$ with $j\ne j'$ and for all bounded $g_1, g_2$ supported on $G$, it holds that

$$
\left| \int T_{\mathfrak{R}_j}^*g_1 \overline{T_{\mathfrak{R}_{j'}}^*g_2} \, \mathrm{d}\mu \right| \le
2^{876a^3-4n}\|g_1\|_2 \|g_2\|_2\,.
$$

## Depends on

- [adjoint tree control](../part-01/adjoint-tree-control.md)
- [correlation separated trees](../part-01/correlation-separated-trees.md)

## Proof

We have by [adjoint tile support](../part-01/adjoint-tile-support.md) and the triangle inequality that

$$
\left| \int T_{\mathfrak{R}_j}^*g_1 \overline{T_{\mathfrak{R}_{j'}}^*g_2} \, \mathrm{d}\mu \right|
$$

$$
\le \sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak u}' \in {\mathfrak U}_{j'}} \left| \int T^*_{{\mathfrak T}_j({\mathfrak u})} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})} g_1) \overline{T^*_{{\mathfrak T}_{j'}({\mathfrak u}')} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u}')} g_2)} \, \mathrm{d}\mu \right|\,.
$$

By [correlation separated trees](../part-01/correlation-separated-trees.md), this is bounded by

$$
2^{512a^3-4n} \sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak u}' \in {\mathfrak U}_{j'}} \|S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}g_1)\|_{L^2({\mathcal{I}}({\mathfrak u}')\cap {\mathcal{I}}({\mathfrak u})} \|S_{2, {\mathfrak u}'} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u}')}g_2)\|_{L^2({\mathcal{I}}({\mathfrak u}')\cap{\mathcal{I}}({\mathfrak u}))}\,.\qquad\text{(62)}
$$

We apply the Cauchy-Schwarz inequality in the form

$$
\sum_{i \in M} a_i b_i \le (\sum_{i \in M} a_i^2 )^{1/2}(\sum_{i \in M} b_i^2 )^{1/2}
$$

to the outer two sums:

$$
\le 2^{512a^3-4n} \left(\sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak u}' \in {\mathfrak U}_{j'}} \|S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}g_1)\|_{L^2({\mathcal{I}}({\mathfrak u}')\cap {\mathcal{I}}({\mathfrak u}))}^2 \right)^{1/2}
$$

$$
\left(\sum_{{\mathfrak u} \in {\mathfrak U}_j} \sum_{{\mathfrak u}' \in {\mathfrak U}_{j'}} \|S_{2,{\mathfrak u}'} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u}')}g_2)\|_{L^2({\mathcal{I}}({\mathfrak u}')\cap{\mathcal{I}}({\mathfrak u}))}^2 \right)^{1/2}\,.
$$

We can now estimate the factor involving $g_1$ as follows:

$$
\begin{gathered}
\sum_{{\mathfrak u} \in {\mathfrak U}_j}\sum_{{\mathfrak u}' \in {\mathfrak U}_{j'}} \|S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}g_1)\|_{L^2({\mathcal{I}}({\mathfrak u}')\cap {\mathcal{I}}({\mathfrak u}))}^2
\\ = \sum_{{\mathfrak u} \in {\mathfrak U}_j}\sum_{{\mathfrak u}' \in {\mathfrak U}_{j'}} \int_{{\mathcal{I}}({\mathfrak u}) \cap {\mathcal{I}}({\mathfrak u}')} |S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(y)g_1(y))|^2 \, \mathrm{d}\mu(y)
\end{gathered}
$$

By pairwise disjointedness of the sets ${\mathcal{I}}({\mathfrak u}')$ for ${\mathfrak u}' \in {\mathfrak U}_{j'}$, we have

$$
\le \sum_{{\mathfrak u} \in {\mathfrak U}_j}\int_{{\mathcal{I}}({\mathfrak u})} |S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(y)g_1(y))|^2 \, \mathrm{d}\mu(y)
\le \sum_{{\mathfrak u} \in {\mathfrak U}_j}\int_{X} |S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(y)g_1(y))|^2 \, \mathrm{d}\mu(y)
$$

$$
= \sum_{{\mathfrak u} \in {\mathfrak U}_j}\|S_{2,{\mathfrak u}} (\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}g_1)\|_2^2
$$

By [adjoint tree control](../part-01/adjoint-tree-control.md) we now estimate:

$$
\le \sum_{{\mathfrak u} \in {\mathfrak U}_j}(2^{182a^3})^2 \|\mathbf{1}_{{\mathcal{I}}({\mathfrak u})}g_1\|_2^2
$$

By pairwise disjointedness of the sets ${\mathcal{I}}({\mathfrak u})$ for ${\mathfrak u} \in {\mathfrak U}_j$ (and writing out the definition of $L^2$-norms), we have

$$
\le (2^{182a^3})^2 \|g_1\|_2^2
$$

Arguing similarly for $g_2$, we obtain the desired inequality.

## Lean

Formalized as [`TileStructure.Forest.row_correlation`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.row_correlation).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 6309](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L6309)
