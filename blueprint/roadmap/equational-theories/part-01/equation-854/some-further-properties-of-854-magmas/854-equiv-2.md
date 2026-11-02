---
declaration: lemma
origin: cited
---

# 854 equivalences, II

For $x,y$ in a 854 magma, the following are equivalent.

- (i) $y \leq x$.
- (ii) $x \diamond y \to x$.
- (iii) For all $z$, $y \to z$ implies $x \to z$.
- (iv) $x \to x \diamond y$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The equivalence of (i) and (ii) is by definition. If (ii) holds and $y \to z$, then by [854 equivalences, I](854-equiv.md) we have $x = u \diamond (x \diamond y)$ and $z = v \diamond y$ for some $u,v$, hence

$$
z \diamond x = z \diamond (x \diamond ((v \diamond y) \diamond (x \diamond y))) = z \diamond ((u \diamond (x \diamond y)) \diamond (z \diamond (x \diamond y))) = z,
$$

giving the desired claim $x \to z$. Now if (iii) holds, note from [854 equivalences, I](854-equiv.md) that $y \to x \diamond y$, hence $x \to x \diamond y$ by (iii), so that $(x \diamond y) \diamond x = x \diamond y$, giving (iv). Finally, if (iv) holds, note that

$$
\begin{aligned}
x \diamond ((x \diamond y) \diamond x) &= x \diamond ( ((x \diamond y) \diamond ((y \diamond y) \diamond ((x \diamond y) \diamond y))) \diamond x) \\
&= x \diamond (((x \diamond y) \diamond ((y \diamond y) \diamond (x \diamond y))) \diamond (x \diamond ((y \diamond y) \diamond (x \diamond y)))) \\
&= x
\end{aligned}
$$

and hence by (iv) $x \diamond (x \diamond y) = x$, giving (ii).

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 150](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L150)
