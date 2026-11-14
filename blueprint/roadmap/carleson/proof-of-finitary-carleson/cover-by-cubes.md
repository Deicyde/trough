---
declaration: lemma
origin: cited
lean: cover_by_cubes
statement: formalized
proof: formalized
---

# cover by cubes

Let $-S\le l\le k\le S$ and $y\in Y_k$. We have

$$
I_3(y,k)\subset \bigcup_{y'\in Y_l} I_3(y',l)\, .\qquad\text{(13)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $-S\le l\le k\le S$ and $y\in Y_k$. If $l=k$, the inclusion (13) is true from the definition of set union. We may then assume inductively that $k>l$ and the statement of the lemma is true if $k$ is replaced by $k-1$. Let $x\in I_3(y,k)$. By definition [(9)](README.md), $x\in I_j(y,k)$ for some $j\in \{1,2\}$. By [(8)](README.md), $x\in I_3(w,k-1)$ for some $w\in Y_{k-1}$. We conclude (13) by induction.

## Lean

Formalized as [`cover_by_cubes`](https://fpvandoorn.github.io/carleson/docs/find/#doc/cover_by_cubes).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1472](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1472)
