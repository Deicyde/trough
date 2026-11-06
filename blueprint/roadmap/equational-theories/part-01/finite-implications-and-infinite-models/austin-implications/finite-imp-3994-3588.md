---
declaration: proposition
origin: cited
lean: InfModel.Finite.Equation3994_implies_Equation3588
statement: formalized
proof: formalized
---

# 3994 implies 3588 for finite models

All finite magmas which satisfy [E3994](https://teorth.github.io/equational_theories/implications/?3994) $({x \diamond y = (z \diamond (x \diamond y)) \diamond z})$ also satisfy [E3588](https://teorth.github.io/equational_theories/implications/?3588) $({x \diamond y = z \diamond ((x \diamond y) \diamond z)})$.

## Depends on

- [Equation 3588](../../selected-laws/part-03/eq3588.md)
- [Models](../../basic-theory-of-magmas/models-def.md)

## Proof

For a finite magma $M$, consider the set $S = \{x \diamond y | x, y \in M\}$. Now $f_z : x \mapsto z \diamond x$ and $g_z : x \mapsto x \diamond z$. They both map $S$ to $S$, and due to the hypothesis $g_z \diamond f_z$ is the identity on $S$, so because $S$ is finite $f_z$ and $g_z$ must be inverse bijections on it, and therefore they commute.

## Lean

Formalized as [`InfModel.Finite.Equation3994_implies_Equation3588`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Finite.Equation3994_implies_Equation3588).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 113](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L113)
