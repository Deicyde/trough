---
declaration: lemma
origin: cited
lean: forest_stacking
statement: formalized
proof: formalized
---

# forest stacking

It holds for $k\le n$ that

$$
\sum_{{\mathfrak u} \in {\mathfrak U}_3(k,n,j)} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})} \le (4n+12)2^{n}\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose that a point $x$ is contained in more than $(4n + 12)2^n$ cubes ${\mathcal{I}}({\mathfrak u})$ with ${\mathfrak u} \in {\mathfrak U}_3(k,n,j)$. Since ${\mathfrak U}_3(k,n,j) \subset {\mathfrak C}_1(k,n,j)$ for each such ${\mathfrak u}$, there exists $\mathfrak{m} \in \mathfrak{M}(k,n)$ such that $100{\mathfrak u} \lesssim \mathfrak{m}$. We fix such an $\mathfrak{m}({\mathfrak u}) := \mathfrak{m}$ for each ${\mathfrak u}$, and claim that the map ${\mathfrak u} \mapsto\mathfrak{m}({\mathfrak u})$ is injective. Indeed, assume for ${\mathfrak u}\neq {\mathfrak u}'$ there is $\mathfrak{m} \in \mathfrak{M}(k,n)$ such that $100{\mathfrak u} \lesssim \mathfrak{m}$ and $100{\mathfrak u}' \lesssim \mathfrak{m}$. By [(8)](../../proof-of-metric-space-carleson-overview/README.md), either ${\mathcal{I}}({\mathfrak u}) \subset {\mathcal{I}}({\mathfrak u}')$ or ${\mathcal{I}}({\mathfrak u}') \subset {\mathcal{I}}({\mathfrak u})$. By [(13)](../README.md), $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),100) \cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100) = \emptyset$. This contradicts $\Omega(\mathfrak{m})$ being contained in both sets by [(15)](../../proof-of-metric-space-carleson-overview/README.md). Thus $x$ is contained in more than $(4n + 12)2^n$ cubes ${\mathcal{I}}(\mathfrak{m})$, $\mathfrak{m} \in \mathfrak{M}(k,n)$. Consequently, we have by [(22)](../README.md) that $x \in A(2n + 6, k,n) \subset G_2$. Let ${\mathcal{I}}({\mathfrak u})$ be an inclusion minimal cube among the ${\mathcal{I}}({\mathfrak u}'), {\mathfrak u}' \in {\mathfrak U}_3(k,n,j)$ with $x \in {\mathcal{I}}({\mathfrak u})$. By the dyadic property [(8)](../../proof-of-metric-space-carleson-overview/README.md), we have ${\mathcal{I}}({\mathfrak u}) \subset {\mathcal{I}}({\mathfrak u}')$ for all cubes ${\mathcal{I}}({\mathfrak u}')$ containing $x$. Thus

$$
{\mathcal{I}}({\mathfrak u}) \subset \{y \ : \ \sum_{{\mathfrak u} \in {\mathfrak U}_3(k,n,j)} \mathbf{1}_{{\mathcal{I}}({\mathfrak u})}(y) > 1 + (4n+12)2^{n}\} \subset G_2\,.
$$

Thus $\mathfrak{T}_1({\mathfrak u}) \cap {\mathfrak C}_6(k,n,j) = \emptyset$. This contradicts ${\mathfrak u} \in {\mathfrak U}_2(k,n,j)$.

## Lean

Formalized as [`forest_stacking`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_stacking).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3174](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3174)
