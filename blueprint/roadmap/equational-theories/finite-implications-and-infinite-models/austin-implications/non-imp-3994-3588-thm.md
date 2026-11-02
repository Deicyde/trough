---
declaration: proposition
origin: cited
lean: InfModel.Equation3994_not_implies_Equation3588
statement: formalized
proof: formalized
---

# 3994 does not imply 3588 for infinite models

There exists a magma which satisfies [E3994](https://teorth.github.io/equational_theories/implications/?3994) and not [E3588](https://teorth.github.io/equational_theories/implications/?3588).

## Depends on

- [Equation 3994](../../selected-laws/part-03/eq3994.md)
- [Equation 3588](../../selected-laws/part-03/eq3588.md)
- [Models](../../basic-theory-of-magmas/models-def.md)

## Proof

Consider $\mathbb{N}$, with $x \diamond y$ defined as $x \oplus y$ (bitwise XOR) if $x$ and $y$ are even, $y+2$ if only $y$ is even, $x \dot - 2$ if only $x$ is even, and $0$ if both are odd. Note that the range of the operation is the set of even naturals. [E3994](https://teorth.github.io/equational_theories/implications/?3994) is satisfied, because for even $z$ we get $z \oplus (x \diamond y) \oplus z = x \diamond y$ and for odd $z$ we get $(x \diamond y) + 2 \dot - 2 = x \diamond y$. Setting $x = y = z = 1$, [E3588](https://teorth.github.io/equational_theories/implications/?3588) isn't satisfied.

## Lean

Formalized as [`InfModel.Equation3994_not_implies_Equation3588`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Equation3994_not_implies_Equation3588).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 126](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L126)
