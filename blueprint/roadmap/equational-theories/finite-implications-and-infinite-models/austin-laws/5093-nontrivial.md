---
declaration: theorem
origin: cited
lean: InfModel.Finite.Equation5093_implies_Equation2
statement: formalized
proof: formalized
---

# Equation 5093 has no non-trivial finite models

[E5093](https://teorth.github.io/equational_theories/implications/?5093) has no non-trivial finite models.

## Depends on

- [Equation 5093](../../selected-laws/part-03/equations-of-order-greater-than-4/eq5093.md)
- [Models](../../basic-theory-of-magmas/models-def.md)

## Proof

From [E5093](https://teorth.github.io/equational_theories/implications/?5093) we see that the map $w \mapsto y \diamond w$ is onto, hence injective in a finite model. Using this injectivity four times in [E5093](https://teorth.github.io/equational_theories/implications/?5093), we see that $z \diamond y$ does not depend on $z$, hence the expression $x \diamond (z \diamond y)$ does not depend on $x$. By [E5093](https://teorth.github.io/equational_theories/implications/?5093) again, this means that $x$ does not depend on $x$, which is absurd in a non-trivial model.

## Lean

Formalized as [`InfModel.Finite.Equation5093_implies_Equation2`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Finite.Equation5093_implies_Equation2).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 72](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L72)
