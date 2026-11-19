---
declaration: lemma
origin: cited
lean: forest_convex
statement: formalized
proof: formalized
---

# forest convex

For each ${\mathfrak u}\in {\mathfrak U}_3(k,n,j)$, the set $\mathfrak{T}_2({\mathfrak u})$ satisfies the convexity condition [(31)](../../proof-of-metric-space-carleson-overview/README.md).

## Depends on

- [C5 convex](c5-convex.md)

## Proof

Let ${\mathfrak p}, {\mathfrak p}'' \in \mathfrak{T}_2({\mathfrak u})$ and ${\mathfrak p}' \in {\mathfrak P}$ with ${\mathfrak p} \le {\mathfrak p}' \le {\mathfrak p}''$. By [(48)](README.md) we have ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}_6(k,n,j) \subset {\mathfrak C}_5(k,n,j)$. By [C5 convex](c5-convex.md), we have ${\mathfrak p}' \in {\mathfrak C}_5(k,n,j)$. Since ${\mathfrak p} \in {\mathfrak C}_6(k,n,j)$ we have ${\mathcal{I}}({\mathfrak p}) \not \subset G'$, so ${\mathcal{I}}({\mathfrak p}') \not \subset G'$ and therefore also ${\mathfrak p}' \in {\mathfrak C}_6(k,n,j)$.

By [(48)](README.md) there exists ${\mathfrak u}' \in {\mathfrak U}_2(k,n,j)$ with ${\mathfrak p}'' \in \mathfrak{T}_1({\mathfrak u}')$ and hence $2{\mathfrak p}'' \lesssim {\mathfrak u}'$ and ${\mathcal{I}}({\mathfrak p}'') \ne {\mathcal{I}}({\mathfrak u}')$. Together this implies ${\mathcal{I}}({\mathfrak p}'') \subsetneq {\mathcal{I}}({\mathfrak u}')$. With the inclusion ${\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p}'')$ from ${\mathfrak p}' \le {\mathfrak p}''$, it follows that ${\mathcal{I}}({\mathfrak p}') \subsetneq {\mathcal{I}}({\mathfrak u}')$ and hence ${\mathcal{I}}({\mathfrak p}') \ne {\mathcal{I}}({\mathfrak u}')$. By [(39)](../part-01/wiggle-order-3.md) and transitivity of $\lesssim$ we further have $2{\mathfrak p}' \lesssim {\mathfrak u}'$, so ${\mathfrak p}' \in \mathfrak{T}_1({\mathfrak u}')$. It follows that ${\mathfrak p}' \in \mathfrak{T}_2({\mathfrak u})$, which shows [(31)](../../proof-of-metric-space-carleson-overview/README.md).

## Lean

Formalized as [`forest_convex`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_convex).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3089](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3089)
