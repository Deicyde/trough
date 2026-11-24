---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.Scheme.cocharTorus
statement: formalized
proof: formalized
---

# Cocharacter lattice of the torus

Let $G$ be a torus of dimension $n$ over a domain $R$. Then $X^*(G) = \operatorname{Hom}({\mathbb Z}^n, {\mathbb Z})$.

## Depends on

- [Cocharacters of a group scheme](0-cochar.md)

## Proof depends on

- [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md)
- [The diagonalisable group scheme torus over $\operatorname{Spec} R$](../diagonalisable-groups/0-diag-spec.md)

## Proof

Immediate from Propositions [The diagonalisable group scheme torus over $\operatorname{Spec} R$](../diagonalisable-groups/0-diag-spec.md) and [Cocharacter lattice of a diagonalisable group scheme](0-cochar-diag.md).

## Lean

Formalized as [`AlgebraicGeometry.Scheme.cocharTorus`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.cocharTorus).

## Sources

- [Toric varieties blueprint: chapters/4-3-torus.tex, line 116](https://github.com/YaelDillies/toric/blob/97b1287db93f2eee84c8bb4e408058d9e721ce5b/blueprint/src/chapters/4-3-torus.tex#L116)
