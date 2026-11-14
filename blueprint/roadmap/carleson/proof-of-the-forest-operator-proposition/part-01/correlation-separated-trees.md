---
declaration: lemma
origin: cited
lean: TileStructure.Forest.correlation_separated_trees
statement: formalized
proof: formalized
---

# correlation separated trees

For any ${\mathfrak u}_1 \ne {\mathfrak u}_2 \in {\mathfrak U}$ and all bounded $g_1, g_2$ with bounded support, we have

$$
\left| \int_X \sum_{{\mathfrak p}_1 \in {\mathfrak T}({\mathfrak u}_1)} \sum_{{\mathfrak p}_2 \in {\mathfrak T}({\mathfrak u}_2)} T^*_{{\mathfrak p}_1}g_1 \overline{T^*_{{\mathfrak p}_2}g_2 }\,\mathrm{d}\mu \right|\qquad\text{(27)}
$$

$$
\le 2^{512a^3-4n} \prod_{j =1}^2 \| S_{2, {\mathfrak u}_j} g_j\|_{L^2({\mathcal{I}}({\mathfrak u}_1) \cap {\mathcal{I}}({\mathfrak u}_2))}\,.\qquad\text{(28)}
$$

## Depends on

- [correlation distant tree parts](correlation-distant-tree-parts.md)
- [correlation near tree parts](correlation-near-tree-parts.md)

## Proof

*Proof of correlation separated trees.* By [adjoint tile support](adjoint-tile-support.md) and [(8)](../../proof-of-metric-space-carleson-overview/README.md), the left hand side (27) is $0$ unless ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$ or ${\mathcal{I}}({\mathfrak u}_2) \subset {\mathcal{I}}({\mathfrak u}_1)$. Without loss of generality we assume that ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$.

Define

$$
\mathfrak{S} := \{{\mathfrak p} \in {\mathfrak T}({\mathfrak u}_1) \cup {\mathfrak T}({\mathfrak u}_2) \ : \ d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \ge 2^{Zn/2}\,\}.\qquad\text{(29)}
$$

correlation separated trees follows by combining the definition [(3)](../../proof-of-metric-space-carleson-overview/README.md) of $Z$ with the following two lemmas.

## Lean

Formalized as [`TileStructure.Forest.correlation_separated_trees`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.correlation_separated_trees).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5298](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5298)
