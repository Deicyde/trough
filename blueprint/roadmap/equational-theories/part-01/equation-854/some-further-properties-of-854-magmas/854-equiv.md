---
declaration: lemma
origin: cited
---

# 854 equivalences, I

For $x, y$ in a 854 magma, the following are equivalent.

- (i) $y \to x$.
- (ii) $x = x \diamond y$.
- (iii) $x = z \diamond y$ for some $z$.
- (iv) $z, x \diamond z \to y$ for some $z$.
- (v) $x \diamond y^2 \to y$.
- (vi) $y \diamond (x \diamond y^2) = y$.
- (vii) $y = (w \diamond z) \diamond (x \diamond z)$ for some $w,z$.
- (viii) $y \to x \diamond y^2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The equivalence of (i) and (ii), or (v) and (vi), is by definition. (iii) trivially implies (ii), and the converse comes from [(3)](../README.md). Using [(2)](../README.md) we see that (v) implies (iv). If (iv) is true, then $y = (y \diamond z) \diamond (x \diamond z)$, giving (vii). From [(1)](../README.md) we see that (vii) implies (ii). If (ii) is true, then $y \diamond (x \diamond y^2) = y \diamond ((x \diamond y) \diamond (y \diamond y)) = y$, giving (vi). Finally, to show the equivalence of (i) and (viii), use the already established equivalence of (i) and (v), together with [(3)](../README.md) which gives $(x \diamond y^2) \diamond y^2 = x \diamond y^2$.

## Sources

- [Equational Theories blueprint: chapter/854.tex, line 132](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/854.tex#L132)
