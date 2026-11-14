---
declaration: lemma
origin: cited
lean: integer_ball_cover
statement: formalized
proof: formalized
---

# integer ball cover

For every $x\in {\mathbb{R}}$ and $R>0$ and every $n\in \mathbb{Z}$ and $R'>0$, there exist $m_1, m_2, m_3\in \mathbb{Z}$ such that

$$
B'\subset B_1\cup B_2\cup B_3\, ,\qquad\text{(48)}
$$

where

$$
B'= \{ {\vartheta} \in {\Theta}: d_{B(x,R)}({\vartheta}, {\vartheta}_n)<2R'\}
$$

and for $j=1,2,3$

$$
B_j=
\{ {\vartheta} \in {\Theta}: d_{B(x,R)}({\vartheta}, {\vartheta}_{m_j})\lt R'\}
\, .
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $m_1$ be the largest integer smaller than or equal to $n- \frac {R'} {2R}$. Let $m_2=n$. Let $m_3$ be the smallest integer larger than or equal to $n+ \frac {R'} {2R}$.

Let ${\vartheta}_{n'}\in B'$, then with [(44)](README.md), we have

$$
2R|n-n'|< 2R'\, .\qquad\text{(49)}
$$

Assume first $n'\le m_1$. With (49) we have

$$
R|m_1-n'|=R(m_1-n')=R(m_1-n)+R(n-n')
$$

$$
< -\frac{R'}2+R'=-\frac{R'}2\, .
$$

We conclude ${\vartheta}_{n'}\in B_1$.

Assume next $m_1\lt n'\lt m_3$. Then ${\vartheta}_{n'}\in B_2$.

Assume finally that $m_3\le n'$. With (49) we have

$$
R|m_3-n'|=R(n'-m_3)=R(n'-n)+R(n-m_3)
$$

$$
< R' -\frac{R'}2=-\frac{R'}2\, .
$$

We conclude ${\vartheta}_{n'}\in B_1$. This completes the proof of the lemma.

## Lean

Formalized as [`integer_ball_cover`](https://fpvandoorn.github.io/carleson/docs/find/#doc/integer_ball_cover).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9403](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9403)
