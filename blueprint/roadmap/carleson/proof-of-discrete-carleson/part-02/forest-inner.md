---
declaration: lemma
origin: cited
lean: forest_inner
statement: formalized
proof: formalized
---

# forest inner

For each ${\mathfrak u}\in {\mathfrak U}_3(k,n,j)$ and each ${\mathfrak p} \in \mathfrak{T}_2({\mathfrak u})$ we have

$$
B({\mathrm{c}}({\mathfrak p}), 8 D^{{\mathrm{s}}({\mathfrak p})}) \subset {\mathcal{I}}({\mathfrak u}).
$$

## Depends on

- [relation geometry](relation-geometry.md)

## Proof

Let ${\mathfrak p} \in \mathfrak{T}_2({\mathfrak u})$. Then ${\mathfrak p} \in {\mathfrak C}_4(k,n,j)$, hence there exists a chain

$$
{\mathfrak p} \le {\mathfrak p}_{Z(n+1)} \le \dotsb \le {\mathfrak p}_0
$$

of distinct tiles in ${\mathfrak C}_3(n,k,j)$. We pick such a chain and set ${\mathfrak q} = {\mathfrak p}_0$. Then we have from distinctness of the tiles in the chain that ${\mathrm{s}}({\mathfrak p}) \le {\mathrm{s}}({\mathfrak q}) - Z(n+1)$. By [(15)](../README.md) there exists ${\mathfrak u}'' \in {\mathfrak U}_1(k,n,j)$ with $2{\mathfrak q} \lesssim {\mathfrak u}''$ and ${\mathrm{s}}({\mathfrak q}) < {\mathrm{s}}({\mathfrak u}'')$. Then we have in particular by [wiggle order 1](../part-01/wiggle-order-1.md) that $10 {\mathfrak p} \lesssim {\mathfrak u}''$. Let ${\mathfrak u}' \sim {\mathfrak u}$ be such that ${\mathfrak p} \in \mathfrak{T}_1({\mathfrak u}')$. By the definition of $\sim$, it follows that ${\mathfrak u}' \sim {\mathfrak u}''$. By transitivity of $\sim$, we have ${\mathfrak u} \sim {\mathfrak u}''$. By [relation geometry](relation-geometry.md), we have ${\mathrm{s}}({\mathfrak u}'') = {\mathrm{s}}({\mathfrak u})$, hence ${\mathrm{s}}({\mathfrak q}) < {\mathrm{s}}({\mathfrak u})$ and ${\mathrm{s}}({\mathfrak p}) \le {\mathrm{s}}({\mathfrak q}) - Z(n+1) \le {\mathrm{s}}({\mathfrak u}) - Z(n+1) - 1$.

Thus, there exists some cube $I \in \mathcal{D}$ with $s(I) = {\mathrm{s}}({\mathfrak u}) - Z(n+1) - 1$ and $I \subset {\mathcal{I}}({\mathfrak u})$ and ${\mathcal{I}}({\mathfrak p}) \subset I$. Since ${\mathfrak p} \in {\mathfrak C}_5(k,n,j)$, we have that $I \notin \mathcal{L}({\mathfrak u})$, so $B(c(I), 8D^{s(I)}) \subset {\mathcal{I}}({\mathfrak u})$. By the triangle inequality, [(1)](../../proof-of-metric-space-carleson-overview/README.md) and $a \ge 4$, the same then holds for the subcube ${\mathcal{I}}({\mathfrak p}) \subset I$.

## Lean

Formalized as [`forest_inner`](https://fpvandoorn.github.io/carleson/docs/find/#doc/forest_inner).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3139](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3139)
