---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.Scheme.charTorus
statement: formalized
proof: formalized
---

# Character lattice of the torus

Let $G$ be a torus of dimension $n$ over a domain $R$. Then $X(G) = {\mathbb Z}^n$.

## Depends on

- [Characters of a group scheme](0-char.md)

## Proof depends on

- [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md)
- [The diagonalisable group scheme torus over $\operatorname{Spec} R$](../diagonalisable-groups/0-diag-spec.md)

## Proof

Immediate from Propositions [The diagonalisable group scheme torus over $\operatorname{Spec} R$](../diagonalisable-groups/0-diag-spec.md) and [Character lattice of a diagonalisable group scheme](0-char-diag.md).

## Lean

Formalized as [`AlgebraicGeometry.Scheme.charTorus`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.charTorus).

## Sources

- [Toric varieties blueprint: chapters/4-3-torus.tex, line 99](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-3-torus.tex#L99)
