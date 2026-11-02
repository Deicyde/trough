---
declaration: theorem
origin: cited
lean: Subgraph.Equation14_implies_Equation23
statement: formalized
proof: formalized
---

# 14 implies 23

[E14](https://teorth.github.io/equational_theories/implications/?14) $({x = y \diamond (x \diamond y))})$ is equivalent to [E23](https://teorth.github.io/equational_theories/implications/?23) $({x = (x \diamond x) \diamond x})$.

## Depends on

- [Equation 23](../../../part-01/selected-laws/part-01/eq23.md)
- [Equation 14](../../../part-01/selected-laws/part-01/eq14.md)

## Proof

$$
x = (x \diamond x) \diamond (x \diamond (x \diamond x)) = (x \diamond x) \diamond x
$$

## Lean

Formalized as [`Subgraph.Equation14_implies_Equation23`](https://teorth.github.io/equational_theories/docs/find/#doc/Subgraph.Equation14_implies_Equation23).

## Sources

- [Equational Theories blueprint: chapter/egraphs.tex, line 25](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/egraphs.tex#L25)
