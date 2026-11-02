---
declaration: theorem
origin: cited
---

# Diagonalization

An equational law of the form

$$
F(x_1,\dots,x_n) = G(y_1,\dots,y_m),
$$

where $x_1,\dots,x_n$ and $y_1,\dots,y_m$ are distinct elements of the alphabet, implies the diagonalized law

$$
F(x_1,\dots,x_n) = F(x'_1,\dots,x'_n).
$$

where $x'_1,\dots,x'_n$ are distinct from $x_1,\dots,x_n$ In particular, if $G(y_1,\dots,y_m)$ can be viewed as a specialization of $F(x'_1,\dots,x'_n)$, then these two laws are equivalent.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

From two applications of (prediag) one has

$$
F(x_1,\dots,x_n) = G(y_1,\dots,y_m)
$$

and

$$
F(x'_1,\dots,x'_n) = G(y_1,\dots,y_m)
$$

whence the claim.

## Sources

- [Equational Theories blueprint: chapter/general_implications.tex, line 67](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/general_implications.tex#L67)
