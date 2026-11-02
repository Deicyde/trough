---
declaration: corollary
origin: cited
---

# Asterix does not imply Obelix

There exists a magma satisfying the Asterix law ([E65](https://teorth.github.io/equational_theories/implications/?65)) with carrier $\mathbb{Z}$ such that the left-multiplication maps $L_y: x \mapsto y \diamond x$ are not injective for any $y \in \mathbb{Z}$. In particular, it does not satisfy the Obelix law ([E1491](https://teorth.github.io/equational_theories/implications/?1491) $({x = (y \diamond x) \diamond (y \diamond (y \diamond x))})$).

## Depends on

- [Equation 65](../../selected-laws/part-02/eq65.md)
- [Equation 1491](../../selected-laws/part-02/eq1491.md)

## Proof depends on

- [no-inject](no-inject.md)

## Proof

Note that $L_y (y+h) = y + h + f(h)$, so the injectivity of the left-multiplication maps is equivalent to the injectivity of the map $h \mapsto h + f(h)$. The non-injectivity then follows from [Corollary no-inject](no-inject.md). Note that the Obelix law clearly expresses $x$ as a function of $y$ and $L_y x = y \diamond x$, forcing injectivity of left-multiplication, so the Obelix law fails.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 180](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L180)
