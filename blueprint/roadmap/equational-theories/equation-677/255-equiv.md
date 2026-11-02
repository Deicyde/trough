---
declaration: lemma
origin: cited
---

# 255-equiv

Let $M$ be a finite magma satisfying 677, and let $x \in M$. Then the following are equivalent:

- (i) 255 holds for $x$, that is to say $R_x (Sx \diamond x) = x$.
- (ii) The equation $R_x y = x$ has the unique solution $y = Sx \diamond x$.
- (iii) The equation $R_x y = x$ has a solution.
- (iv) The equation $R_x L_x z = x$ has a solution.
- (v) The equation $L_x R_x z = z$ has a solution.
- (vi) The equation $R_x L_x y = y$ has a solution.
- (vii) The equation $L_x S y = y$ has a solution.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Clearly (ii) implies (i), which implies (iii). If (iii) holds, we apply 677-alt to conclude that

$$
y \diamond x = x = y \diamond (x \diamond (x \diamond y))
$$

and hence by left invertibility

$$
x = x \diamond (x \diamond y).
$$

On the other hand, from 677 with $y$ replaced by $x$ we have

$$
x = x \diamond (x \diamond (Sx \diamond x))
$$

and hence by left invertibility $y = Sx \diamond x$, giving (ii).

From left cancellativity we see that (v) and (vi) are equivalent, as are (iii) and (iv).

If (vii) holds, then $L_x L_y y = y$, but from 677-alt we have $y = L_x L_y R_x L_x y$, so (vi) follows from left-cancellativity; the converse implication follows by reversing the steps. If (v) holds, then we have $L_x L_z x = z$, but from 677-alt one has $z = L_x L_z R_x L_x z$, giving the (iv) by left-cancellativity; the converse implication follows by reversing the steps.

## Sources

- [Equational Theories blueprint: chapter/677.tex, line 37](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/677.tex#L37)
