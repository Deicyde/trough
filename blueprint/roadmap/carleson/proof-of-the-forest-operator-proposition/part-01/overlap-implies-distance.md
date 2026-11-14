---
declaration: lemma
origin: cited
lean: TileStructure.Forest.𝔗_subset_𝔖₀, TileStructure.Forest.overlap_implies_distance
statement: formalized
proof: formalized
---

# overlap implies distance

Let ${\mathfrak u}_1 \ne {\mathfrak u}_2 \in {\mathfrak U}$ with ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$. If ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_1) \cup {\mathfrak T}({\mathfrak u}_2)$ with ${\mathcal{I}}({\mathfrak p}) \cap {\mathcal{I}}({\mathfrak u}_1) \ne \emptyset$, then ${\mathfrak p} \in \mathfrak{S}$. In particular, we have ${\mathfrak T}({\mathfrak u}_1) \subset \mathfrak{S}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose first that ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_1)$. Then ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak u}_2)$, by [(30)](../../proof-of-metric-space-carleson-overview/README.md). Thus we have by the separation condition [(34)](../../proof-of-metric-space-carleson-overview/README.md), [(15)](../../proof-of-metric-space-carleson-overview/README.md), [(30)](../../proof-of-metric-space-carleson-overview/README.md) and the triangle inequality

$$
\begin{aligned}
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) &\ge d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}_2)) - d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), {\mathcal{Q}}({\mathfrak u}_1))\\
&\ge 2^{Z(n+1)} - 4\\
&\ge 2^{Zn/2}\,,
\end{aligned}
$$

using that $Z= 2^{12a}\ge 4$. Hence ${\mathfrak p} \in \mathfrak{S}$.

Suppose now that ${\mathfrak p} \in {\mathfrak T}({\mathfrak u}_2)$. If ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}_1)$, then the same argument as above with ${\mathfrak u}_1$ and ${\mathfrak u}_2$ swapped shows ${\mathfrak p} \in \mathfrak{S}$. If ${\mathcal{I}}({\mathfrak p}) \not \subset {\mathcal{I}}({\mathfrak u}_1)$ then, by [(8)](../../proof-of-metric-space-carleson-overview/README.md), ${\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak p})$. Pick ${\mathfrak p}' \in {\mathfrak T}({\mathfrak u}_1)$, we have ${\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak u}_1) \subset {\mathcal{I}}({\mathfrak p})$. Hence, by [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md) and the first paragraph

$$
d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \ge d_{{\mathfrak p}'}({\mathcal{Q}}({\mathfrak u}_1), {\mathcal{Q}}({\mathfrak u}_2)) \ge 2^{Zn}\,,
$$

so ${\mathfrak p} \in \mathfrak{S}$.

## Lean

Formalized as [`TileStructure.Forest.𝔗_subset_𝔖₀`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.𝔗_subset_𝔖₀), [`TileStructure.Forest.overlap_implies_distance`](https://fpvandoorn.github.io/carleson/docs/find/#doc/TileStructure.Forest.overlap_implies_distance).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 5360](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L5360)
