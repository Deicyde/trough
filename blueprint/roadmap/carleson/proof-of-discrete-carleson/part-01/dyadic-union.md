---
declaration: lemma
origin: cited
lean: dyadic_union
statement: formalized
proof: formalized
---

# dyadic union

For each $x\in A(\lambda,k,n)$, there is a dyadic cube $I$ that contains $x$ and is a subset of $A(\lambda,k,n)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Fix $k,n,\lambda,x$ as in the lemma such that $x\in A(\lambda,k,n)$. Let $\mathcal{M}$ be the set of dyadic cubes ${\mathcal{I}}({\mathfrak p})$ with ${\mathfrak p}$ in $\mathfrak{M}(k,n)$ and $x\in {\mathcal{I}}({\mathfrak p})$. By definition of $A(\lambda,k,n)$, the cardinality of $\mathcal{M}$ is at least $1+\lambda 2^{n+1}$. Let $I$ be a cube of smallest scale in $\mathcal{M}$. Then $I$ is contained in all cubes of $\mathcal{M}$. It follows that $I\subset A(\lambda,k,n)$.

## Lean

Formalized as [`dyadic_union`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dyadic_union).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2294](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L2294)
