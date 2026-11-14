---
declaration: lemma
origin: cited
lean: ordConnected_C1
statement: formalized
proof: formalized
---

# C1 convex

For each $k,n,j$, the collection ${\mathfrak C}_1(k,n,j)$ is convex.

## Depends on

- [C convex](c-convex.md)

## Proof

Let ${\mathfrak p}\le{\mathfrak p}'\le{\mathfrak p}''$ with ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}_1(k,n,j)$. By [C convex](c-convex.md) and the inclusion ${\mathfrak C}_1(k,n,j) \subset {\mathfrak C}(k,n)$, which holds by definition [(9)](../README.md), we have ${\mathfrak p}' \in {\mathfrak C}(k,n)$. By [(39)](wiggle-order-3.md) and transitivity of $\lesssim$ we have that ${\mathfrak q} \le {\mathfrak q}'$ and $100 {\mathfrak q}' \lesssim \mathfrak{m}$ imply $100 {\mathfrak q} \lesssim \mathfrak{m}$. So, by [(8)](../README.md), $\mathfrak{B}({\mathfrak p}'') \subset \mathfrak{B}({\mathfrak p}') \subset \mathfrak{B}({\mathfrak p})$. Consequently, by [(9)](../README.md)

$$
2^j \le |\mathfrak{B}({\mathfrak p}'')|\le |\mathfrak{B}({\mathfrak p}')| \le |\mathfrak{B}({\mathfrak p})| < 2^{j+1}\,,
$$

thus ${\mathfrak p}' \in {\mathfrak C}_1(k,n,j)$.

## Lean

Formalized as [`ordConnected_C1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ordConnected_C1).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2761](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2761)
