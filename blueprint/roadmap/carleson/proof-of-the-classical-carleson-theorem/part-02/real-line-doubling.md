---
declaration: lemma
origin: cited
lean: MeasureTheory.InnerProductSpace.IsDoubling
statement: formalized
proof: formalized
---

# real line doubling

We have for every $x\in {\mathbb{R}}$ and $R>0$

$$
\mu(B(x,2R))=2\mu(B(x,R))\, .
$$

## Depends on

- [real line ball measure](real-line-ball-measure.md)

## Proof

We have with [real line ball measure](real-line-ball-measure.md)

$$
\mu(B(x,2R)=4R=2\mu(B(x,R))\, .
$$

This proves the lemma.

## Lean

Formalized as [`MeasureTheory.InnerProductSpace.IsDoubling`](https://fpvandoorn.github.io/carleson/docs/find/#doc/MeasureTheory.InnerProductSpace.IsDoubling).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9283](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L9283)
