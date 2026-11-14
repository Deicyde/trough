---
declaration: lemma
origin: cited
lean: top_tiles
statement: formalized
proof: formalized
---

# top tiles

We have

$$
\sum_{\mathfrak{m} \in \mathfrak{M}(k,n)} \mu({\mathcal{I}}(\mathfrak{m}))\le 2^{n+k+3}\mu(G).\qquad\text{(33)}
$$

## Depends on

- [John Nirenberg](john-nirenberg.md)

## Proof

We write the left-hand side of (33)

$$
\int \sum_{\mathfrak{m} \in \mathfrak{M}(k,n)} \mathbf{1}_{{\mathcal{I}}(\mathfrak{m})}(x) \, d\mu(x) \le
2^{n+1} \sum_{\lambda=0}^{|\mathfrak{M}|}\mu(A(\lambda, k,n))\,.
$$

Using [John Nirenberg](john-nirenberg.md) and then summing a geometric series, we estimate this by

$$
\le
2^{n+1}\sum_{\lambda=0}^{|\mathfrak{M}|}
2^{k+1-\lambda}\mu(G)
\le
2^{n+1}2^{k+2}\mu(G)\, .
$$

This proves the lemma.

## Lean

Formalized as [`top_tiles`](https://fpvandoorn.github.io/carleson/docs/find/#doc/top_tiles).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2412](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2412)
