---
declaration: lemma
origin: cited
---

# The 854 relation

Let $M$ be an $854$ magma, and let $\to$ be the associated operation, thus $x \to y$ if $y \diamond x = y$. Then $x \to y$ holds under any of the following assumptions:

- (i) $y = a \diamond x$ for some $a$.
- (ii) $x = a \diamond (y \diamond b)$ for some $a,b$ with $b \to a$.
- (iii) $y = a \diamond (x \diamond b)$ for some $a,b$ with $b \to a$ and $x \diamond b \to x$.
- (iv) $x = a \diamond y$ for some $a,z$ with $z \to a, y$.
- (v) $x = a \diamond y$ for some $a$, with either $a=y$, $a = y \diamond z$, or $y = a \diamond z$ for some $z$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Case (i) follows from 378. For (ii), we observe

$$
y \diamond x = y \diamond ((a \diamond b) \diamond (y \diamond b)) = y
$$

as required. For (iii), we see from (ii) that $y \to x$, and from (i) we have $x \diamond b \to y$, and then

$$
y \diamond x = y \diamond ((x \diamond (x \diamond b)) \diamond (y \diamond (x \diamond b))) = y
$$

as required. For (iv), we have

$$
y \diamond x = y \diamond ((a \diamond z) \diamond (y \diamond z)) = y
$$

as required. Finally, for (v), in the $a=y$ case we have from 8 that

$$
y \diamond x = y \diamond ((y \diamond y^2) \diamond (y \diamond y^2)) = y,
$$

in the $a = y \diamond z$ case we have from 8 that

$$
y \diamond x = y \diamond (((y \diamond z) \diamond (y \diamond z)^2) \diamond (y \diamond (y \diamond z)^2)) = y,
$$

and finally in the $y = a \diamond z$ case we have from 8 that

$$
y \diamond x = y \diamond ( (a \diamond (a \diamond z)^2) \diamond ((a \diamond z) \diamond (a \diamond z)^2)) = y,
$$

so the claim follows in all cases.

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 264](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L264)
