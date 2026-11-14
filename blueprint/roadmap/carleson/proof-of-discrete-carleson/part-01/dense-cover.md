---
declaration: lemma
origin: cited
lean: dense_cover
statement: formalized
proof: formalized
---

# dense cover

For each $k\ge 0$, the union of all dyadic cubes in $\mathcal{C}(G,k)$ has measure at most $2^{k+1} \mu(G)$ .

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The union of dyadic cubes in $\mathcal{C}(G,k)$ is contained the union of elements of the set $\mathcal{M}(k)$ of all dyadic cubes $J$ with ${\mu(G \cap J)} > 2^{-k-1}{\mu(J)}$. The union of elements in the set $\mathcal{M}(k)$ is contained in the union of elements in the set $\mathcal{M}^*(k)$ of maximal elements in $\mathcal{M}(k)$ with respect to set inclusion. Hence

$$
\mu (\bigcup \mathcal{C}(G,k))\le \mu (\bigcup \mathcal{M}^*(k))\le
\sum_{J\in \mathcal{M}^*(k)}\mu(J)\qquad\text{(27)}
$$

Using the definition of $\mathcal{M}(k)$ and then the pairwise disjointedness of elements in $\mathcal{M}^*(k)$, we estimate (27) by

$$
\le
2^{k+1}\sum_{J\in \mathcal{M}^*(k)}\mu(J\cap G)
\le 2^{k+1}\mu(G).
$$

This proves the lemma.

## Lean

Formalized as [`dense_cover`](https://fpvandoorn.github.io/carleson/docs/find/#doc/dense_cover).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2238](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2238)
