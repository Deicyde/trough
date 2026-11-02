---
declaration: lemma
origin: cited
---

# Basic properties of 677 magma

Let $M$ be a finite magma satisfying 677.

- (i) The left multiplication operators $L_y: M \to M$ are all invertible, with $L_y^{-1} x = x \diamond R_y L_y x$.
- (ii) If $x,y \in M$ and $y \diamond x = x$, then $y = Sx \diamond x$. In particular, 255 holds if and only if the equation $y \diamond x = x$ is solvable for every $x$.
- (iii) For all $x,y \in M$, we have $x = L_y x \diamond R_y L_y^2 x$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

From 677-alt we see that $L_y$ is surjective, hence invertible on finite magmas, giving (i) (the formula for $L_y^{-1} x$ being immediate from 677-alt).

For (ii), using the fact that $L_y x = x$, (i) becomes $x = x \diamond R_y x = L_x L_x y$, then, using the invertibility of $L_x$ given by (i) we have

$$
y = L_x^{-1} L_x^{-1} x \stackrel{(i)}{=} L_x^{-1} (x \diamond R_x L_x x) = L_x^{-1} (L_x R_x L_x x) =
R_x L_x x = Sx \diamond x.
$$

For (iii), we apply (i) with $x$ replaced by $L_y x$.

## Sources

- [Equational Theories blueprint: chapter/677.tex, line 18](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/677.tex#L18)
