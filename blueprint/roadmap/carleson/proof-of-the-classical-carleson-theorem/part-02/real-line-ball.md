---
declaration: lemma
origin: cited
lean: Real.ball_eq_Ioo
statement: formalized
proof: formalized
---

# real line ball

For $x\in R$ and $R>0$, the ball $B(x,R)$ is the interval $(x-R,x+R)$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $x'\in B(x,R)$. By definition of the ball, $|x'-x|\lt R$. It follows that $x'-x\lt R$ and $x-x'\lt R$. It follows $x'\lt x+R$ and $x'>x-R$. This implies $x'\in (x-R,x+R)$. Conversely, let $x'\in (x-R,x+R)$. Then $x'\lt x+R$ and $x'>x-R$. It follows that $x'-x\lt R$ and $x-x'\lt R$. It follows that $|x'-x|\lt R$, hence $x'\in B(x,R)$. This proves the lemma.

## Lean

Formalized as [`Real.ball_eq_Ioo`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Real.ball_eq_Ioo).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9235](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L9235)
