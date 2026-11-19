---
declaration: lemma
origin: cited
lean: ordConnected_C5
statement: formalized
proof: formalized
---

# C5 convex

For each $k,n,j$, the collection ${\mathfrak C}_5(k,n,j)$ is convex.

## Depends on

- [C4 convex](c4-convex.md)

## Proof

Let ${\mathfrak p} \le {\mathfrak p}' \le{\mathfrak p}''$ with ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}_5(k,n,j)$. Then ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}_4(k,n,j)$ by [(20)](../README.md), and thus by [C4 convex](c4-convex.md) ${\mathfrak p}' \in {\mathfrak C}_4(k,n,j)$. It suffices to show that if ${\mathfrak p}' \in {\mathfrak L}_4(k,n,j)$ then ${\mathfrak p} \in {\mathfrak L}_4(k,n,j)$ by contraposition; this is true by [(19)](../README.md) and ${\mathfrak p}\le{\mathfrak p}'$.

## Lean

Formalized as [`ordConnected_C5`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ordConnected_C5).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2831](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2831)
