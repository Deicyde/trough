---
declaration: lemma
origin: cited
lean: Real.volume_ball
statement: formalized
proof: formalized
---

# real line ball measure

We have for every $x\in {\mathbb{R}}$ and $R>0$

$$
\mu(B(x,R))=2R\, .
$$

## Depends on

- [real line ball](real-line-ball.md)

## Proof

We have with [real line ball](real-line-ball.md)

$$
\mu(B(x,R))=\mu((x-R,x+R))=2R\, .
$$

## Lean

Formalized as [`Real.volume_ball`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Real.volume_ball).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9265](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9265)
