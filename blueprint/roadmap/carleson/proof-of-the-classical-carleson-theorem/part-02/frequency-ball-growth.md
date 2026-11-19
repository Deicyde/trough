---
declaration: lemma
origin: cited
lean: frequency_ball_growth
statement: formalized
proof: formalized
---

# frequency ball growth

For any $x,x'\in {\mathbb{R}}$ and $R>0$ with $B(x,R)\subset B(x',2R)$ and any $n,m\in \mathbb{Z}$, we have

$$
2d_{B(x,R)}({\vartheta}_n,{\vartheta}_m)\le d_{B(x',2R)}({\vartheta}_n,{\vartheta}_m) \, .\qquad\text{(47)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

With [(44)](README.md), both sides of [(46)](frequency-ball-doubling.md) are equal to $4R|n-m|$. This proves the lemma.

## Lean

Formalized as [`frequency_ball_growth`](https://fpvandoorn.github.io/carleson/docs/find/#doc/frequency_ball_growth).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9387](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9387)
