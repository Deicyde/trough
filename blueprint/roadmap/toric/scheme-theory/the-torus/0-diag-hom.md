---
declaration: lemma
origin: cited
lean: AlgebraicGeometry.Scheme.diagHomEquiv
statement: formalized
proof: formalized
---

# Diag is a group isomorphism on hom sets

Let $R$ be a domain. The functor $G \rightsquigarrow \operatorname{Spec} R[G]$ from the category of groups to the category of group schemes over $\operatorname{Spec} R$ is a group isomorphism on hom sets.

## Depends on

- [The diagonalisable group scheme functor](../diagonalisable-groups/0-diag.md)

## Proof depends on

- [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md)
- [A fully faithful functor product-preserving is a group isomorphism on hom sets](../../category-theory/objects/0-full-faithful-grp-hom.md)

## Proof

Toddlers and streets by Lemmas [0-full-faithful-diag](../diagonalisable-groups/0-full-faithful-diag.md) and [A fully faithful functor product-preserving is a group isomorphism on hom sets](../../category-theory/objects/0-full-faithful-grp-hom.md).

## Lean

Formalized as [`AlgebraicGeometry.Scheme.diagHomEquiv`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.diagHomEquiv).

## Sources

- [Toric varieties blueprint: chapters/4-3-torus.tex, line 14](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-3-torus.tex#L14)
