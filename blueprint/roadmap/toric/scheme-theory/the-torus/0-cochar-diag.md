---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.Scheme.cocharDiag
statement: formalized
proof: formalized
---

# Cocharacter lattice of a diagonalisable group scheme

Let $R$ be a domain and $G$ be a commutative group. Then $X^*(\operatorname{Spec} R[G]) = \operatorname{Hom}(G, {\mathbb Z})$.

## Depends on

- [Cocharacters of a group scheme](0-cochar.md)

## Proof depends on

- [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md)

## Proof

By Propositions [The diagonalisable group scheme torus over $\operatorname{Spec} R$](../diagonalisable-groups/0-diag-spec.md) and [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md) in turn, we have

$$
X^*(G) = \operatorname{Hom}_{\mathsf{GrpSch}}({\mathbb G}_m, G) = \operatorname{Hom}(k[G], k[{\mathbb Z}]) = \operatorname{Hom}(G, {\mathbb Z}).
$$

## Lean

Formalized as [`AlgebraicGeometry.Scheme.cocharDiag`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.cocharDiag).

## Sources

- [Toric varieties blueprint: chapters/4-3-torus.tex, line 79](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-3-torus.tex#L79)
