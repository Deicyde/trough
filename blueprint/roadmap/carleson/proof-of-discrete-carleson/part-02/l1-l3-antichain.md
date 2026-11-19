---
declaration: lemma
origin: cited
lean: antichain_L1, antichain_L3
statement: formalized
proof: formalized
---

# L1 L3 antichain

Each of the sets ${\mathfrak L}_1(k,n,j,l)$ and ${\mathfrak L}_3(k,n,j,l)$ is an antichain.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By its definition [(11)](../README.md), each set ${\mathfrak L}_1(k,n,j,l)$ is a set of minimal elements in some set of tiles with respect to $\le$. If there were distinct ${\mathfrak p}, {\mathfrak q} \in {\mathfrak L}_1(k,n,j,l)$ with ${\mathfrak p} \le {\mathfrak q}$, then ${\mathfrak q}$ would not be minimal. Hence such ${\mathfrak p}, {\mathfrak q}$ do not exist. Similarly, by [(16)](../README.md), each set ${\mathfrak L}_3(k,n,j,l)$ is a set of maximal elements in some set of tiles with respect to $\le$. If there were distinct ${\mathfrak p}, {\mathfrak q} \in {\mathfrak L}_3(k,n,j,l)$ with ${\mathfrak p} \le {\mathfrak q}$, then ${\mathfrak p}$ would not be maximal.

## Lean

Formalized as [`antichain_L1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/antichain_L1), [`antichain_L3`](https://fpvandoorn.github.io/carleson/docs/find/#doc/antichain_L3).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3352](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3352)
