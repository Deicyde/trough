---
declaration: lemma
origin: cited
lean: smaller_boundary
statement: formalized
proof: formalized
---

# smaller boundary

Let $K = 2^{4a+1}$ and let $n\ge 0$ be an integer. Then for each $-S+nK\le k\le S$ we have

$$
\sum_{y'\in Y_{k-nK}: (y',k-nK|y,k)}\mu(I_3(y',k-nK)) \le 2^{-n} \mu(I_3(y,k))\,.\qquad\text{(24)}
$$

## Depends on

- [small boundary](small-boundary.md)

## Proof

We prove this by induction on $n$. If $n=0$, both sides of (24) are equal to $\mu(I_3(y,k))$ by [(10)](basic-grid-structure.md). If $n=1$, this follows from [small boundary](small-boundary.md).

Assume $n>1$ and (24) has been proven for $n-1$. We write (24)

$$
\sum_{y''\in Y_{k-nK}: (y'',k-nK|y,k)}\mu(I_3(y'',k-nK))
$$

$$
= \sum_{y'\in Y_{k-K}:(y',k-K|y,k)} \left[ \sum_{y''\in Y_{k-nK}: (y'',k-nK|y',k-K)}\mu(I_3(y'',k-nK)) \right]
$$

Applying the induction hypothesis, this is bounded by

$$
= \sum_{y'\in Y_{k-K}:(y',k-K|y,k)} 2^{1-n}\mu(I_3(y',k-K))
$$

Applying [(18)](small-boundary.md) gives (24), and proves the lemma.

## Lean

Formalized as [`smaller_boundary`](https://fpvandoorn.github.io/carleson/docs/find/#doc/smaller_boundary).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1648](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1648)
