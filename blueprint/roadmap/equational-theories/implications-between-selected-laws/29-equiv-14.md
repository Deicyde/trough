---
declaration: theorem
origin: cited
lean: Subgraph.Equation29_implies_Equation14
statement: formalized
proof: formalized
---

# 29 equivalent to 14

[E29](https://teorth.github.io/equational_theories/implications/?29) $({x = (y \diamond x) \diamond y)})$ is equivalent to [E14](https://teorth.github.io/equational_theories/implications/?14) $({x = y \diamond (x \diamond y))})$.

## Depends on

- [Equation 29](../selected-laws/part-01/eq29.md)
- [Equation 14](../selected-laws/part-01/eq14.md)

## Proof depends on

- [Duality of laws](../general-implications/duality.md)

## Proof

By [Duality of laws](../general-implications/duality.md) it suffices to show that [E29](https://teorth.github.io/equational_theories/implications/?29) implies [E14](https://teorth.github.io/equational_theories/implications/?14). From [E29](https://teorth.github.io/equational_theories/implications/?29) one has

$$
x = ((x \diamond y) \diamond x) \diamond (x \diamond y)
$$

and also

$$
y = (x \diamond y) \diamond x
$$

giving $x = y \diamond (x \diamond y)$, which is [E14](https://teorth.github.io/equational_theories/implications/?14).

## Lean

Formalized as [`Subgraph.Equation29_implies_Equation14`](https://teorth.github.io/equational_theories/docs/find/#doc/Subgraph.Equation29_implies_Equation14).

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 29](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/implications.tex#L29)
