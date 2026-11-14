---
declaration: lemma
origin: cited
lean: cover_big_ball
statement: formalized
proof: formalized
---

# cover big ball

For each $-S\le k\le S$, the ball $B(o, 4D^S-D^k)$ is contained in the union of the balls $B(y,2D^k)$ with $y\in Y_k$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $x$ be any point of $B(o, 4D^S-D^k)$. By maximality of $|Y_k|$, the ball $B(x, D^k)$ intersects one of the balls $B(y, D^k)$ with $y\in Y_k$. By the triangle inequality, $x\in B(y,2D^k)$.

## Lean

Formalized as [`cover_big_ball`](https://fpvandoorn.github.io/carleson/docs/find/#doc/cover_big_ball).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1378](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1378)
