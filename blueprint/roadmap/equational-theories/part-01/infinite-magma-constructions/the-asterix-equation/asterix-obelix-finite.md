---
declaration: proposition
origin: cited
---

# Asterix implies Obelix for finite magmas

Any finite magma satisfying the Asterix law ([E65](https://teorth.github.io/equational_theories/implications/?65)) also is left-cancellative and satisfies the Obelix law ([E1491](https://teorth.github.io/equational_theories/implications/?1491)).

## Depends on

- [Equation 65](../../selected-laws/part-02/eq65.md)
- [Equation 1491](../../selected-laws/part-02/eq1491.md)

## Proof

From [E65](https://teorth.github.io/equational_theories/implications/?65) we see the map $z \mapsto y \diamond z$ is surjective, hence injective on a finite magma; thus the magma is left-cancellative. Replacing $x$ by $y \diamond x$ in this law, we see that

$$
y \diamond x = y \diamond ((y\diamond x) \diamond (y \diamond (y \diamond x)));
$$

using injectivity, we conclude

$$
x = (y\diamond x) \diamond (y \diamond (y \diamond x))
$$

which is [E1491](https://teorth.github.io/equational_theories/implications/?1491).

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 188](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L188)
