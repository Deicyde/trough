---
declaration: lemma
origin: cited
lean: frequency_ball_doubling
statement: formalized
proof: formalized
---

# frequency ball doubling

For any $x,x'\in {\mathbb{R}}$ and $R>0$ with $x\in B(x',2R)$ and any $n,m\in \mathbb{Z}$, we have

$$
d_{B(x',2R)}({\vartheta}_n,{\vartheta}_m)\le 2 d_{B(x,R)}({\vartheta}_n,{\vartheta}_m) \, .\qquad\text{(46)}
$$

## Depends on

- [frequency metric](frequency-metric.md)

## Proof

With [(44)](README.md), both sides of (46) are equal to $4R|n-m|$. This proves the lemma.

## Lean

Formalized as [`frequency_ball_doubling`](https://fpvandoorn.github.io/carleson/docs/find/#doc/frequency_ball_doubling).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9370](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9370)
