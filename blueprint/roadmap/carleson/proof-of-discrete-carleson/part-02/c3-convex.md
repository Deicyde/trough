---
declaration: lemma
origin: cited
lean: ordConnected_C3
statement: formalized
proof: formalized
---

# C3 convex

For each $k,n,j$, the collection ${\mathfrak C}_3(k,n,j)$ is convex.

## Depends on

- [C2 convex](../part-01/c2-convex.md)

## Proof

Let ${\mathfrak p} \le {\mathfrak p}' \le {\mathfrak p}''$ with ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}_3(k,n,j)$. By [(15)](../README.md) and [C2 convex](../part-01/c2-convex.md) it follows that ${\mathfrak p}' \in {\mathfrak C}_2(k,n,j)$. By [(15)](../README.md) and [(14)](../README.md), there exists ${\mathfrak u} \in {\mathfrak U}_1(k,n,j)$ with $2{\mathfrak p}'' \lesssim {\mathfrak u}$ and ${\mathcal{I}}({\mathfrak p}'') \subsetneq {\mathcal{I}}({\mathfrak u})$. From ${\mathfrak p}' \le {\mathfrak p}''$, [(39)](../part-01/wiggle-order-3.md) and transitivity of $\lesssim$ we then have $2{\mathfrak p}' \lesssim {\mathfrak u}$ and ${\mathcal{I}}({\mathfrak p}') \subsetneq {\mathcal{I}}({\mathfrak u})$, so ${\mathfrak p}' \in {\mathfrak C}_3(k,n,j)$.

## Lean

Formalized as [`ordConnected_C3`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ordConnected_C3).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2799](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L2799)
