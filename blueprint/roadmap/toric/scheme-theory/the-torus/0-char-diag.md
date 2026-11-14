---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.Scheme.charDiag
statement: formalized
proof: formalized
---

# Character lattice of a diagonalisable group scheme

Let $R$ be a domain and $G$ be a commutative group. Then $X(\operatorname{Spec} R[G]) = G$.

## Depends on

- [Characters of a group scheme](0-char.md)

## Proof depends on

- [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md)

## Proof

By Propositions [The diagonalisable group scheme torus over $\operatorname{Spec} R$](../diagonalisable-groups/0-diag-spec.md) and [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md) in turn, we have

$$
X(G) = \operatorname{Hom}_{\mathsf{GrpSch}}(G, {\mathbb G}_m) = \operatorname{Hom}(k[{\mathbb Z}], k[G]) = \operatorname{Hom}({\mathbb Z}, G) = G.
$$

## Lean

Formalized as [`AlgebraicGeometry.Scheme.charDiag`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.charDiag).

## Sources

- [Toric varieties blueprint: chapters/4-3-torus.tex, line 59](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-3-torus.tex#L59)
