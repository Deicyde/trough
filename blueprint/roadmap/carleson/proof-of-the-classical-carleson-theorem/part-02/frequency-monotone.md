---
declaration: lemma
origin: cited
lean: frequency_monotone
statement: formalized
proof: formalized
---

# frequency monotone

For any $x, x' \in X$ and $R, R' > 0$ with $B(x,R) \subset B(x, R')$, and for any $n, m \in \mathbb{Z}$

$$
d_{B(x,R)}({\vartheta}_n, {\vartheta}_m) \le d_{B(x',R')}({\vartheta}_n, {\vartheta}_m)\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This follows immediately from the definition [(44)](README.md) and $R \le R'$.

## Lean

Formalized as [`frequency_monotone`](https://fpvandoorn.github.io/carleson/docs/find/#doc/frequency_monotone).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9354](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9354)
