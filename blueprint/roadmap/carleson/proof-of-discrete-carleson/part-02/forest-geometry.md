---
declaration: lemma
origin: cited
lean: forest_geometry
statement: formalized
proof: formalized
---

# forest geometry

For each ${\mathfrak u}\in {\mathfrak U}_3(k,n,j)$, the set $\mathfrak{T}_2({\mathfrak u})$ satisfies [(30)](../../proof-of-metric-space-carleson-overview/README.md).

## Depends on

- [relation geometry](relation-geometry.md)

## Proof

Let ${\mathfrak p} \in \mathfrak{T}_2({\mathfrak u})$. By [(48)](README.md), there exists ${\mathfrak u}' \sim {\mathfrak u}$ with ${\mathfrak p} \in \mathfrak{T}_1({\mathfrak u}')$. Then we have $2{\mathfrak p} \lesssim {\mathfrak u}'$ and ${\mathcal{I}}({\mathfrak p}) \ne {\mathcal{I}}({\mathfrak u}')$, so by [(41)](../part-01/wiggle-order-3.md) $4{\mathfrak p} \lesssim 500{\mathfrak u}'$. Further, by [relation geometry](relation-geometry.md), we have that ${\mathcal{I}}({\mathfrak u}') = {\mathcal{I}}({\mathfrak u})$ and there exists ${\vartheta} \in B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'),100) \cap B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),100)$. Let ${\theta} \in B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 1)$. Using the triangle inequality and the fact that ${\mathcal{I}}({\mathfrak u}') ={\mathcal{I}}({\mathfrak u})$, we obtain

$$
\begin{aligned}
d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), {\theta}) &\le d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), {\vartheta}) + d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}), {\vartheta}) + d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}), {\theta})\\
&= d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), {\vartheta}) + d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), {\vartheta}) + d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), {\theta})\\
&< 100 + 100 + 1 < 500\,.
\end{aligned}
$$

Combining this with $4{\mathfrak p} \lesssim 500{\mathfrak u}'$, we obtain

$$
B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 1) \subset B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 500) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 4)\,.
$$

Together with ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}') = {\mathcal{I}}({\mathfrak u})$, this gives $4{\mathfrak p} \lesssim {\mathfrak u}$, which is [(30)](../../proof-of-metric-space-carleson-overview/README.md).

## Lean

Formalized as [`forest_geometry`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_geometry).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3062](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3062)
