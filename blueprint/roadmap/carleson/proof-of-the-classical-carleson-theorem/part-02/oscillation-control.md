---
declaration: lemma
origin: cited
lean: oscillation_control
statement: formalized
proof: formalized
---

# oscillation control

For every $R > 0$ and $x \in X$, and for all $n, m \in \mathbb{Z}$, we have

$$
\sup_{y,y'\in B(x,R)}|ny-ny'-my+my'|\le 2|n-m|R\, .\qquad\text{(45)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The right hand side of (45) equals

$$
\sup_{y,y'\in B(x,R)}|(n-m)(y-x)-(n-m)(y'-x)|\,.
$$

The lemma then follows from the triangle inequality.

## Lean

Formalized as [`oscillation_control`](https://fpvandoorn.github.io/carleson/docs/find/#doc/oscillation_control).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9335](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9335)
