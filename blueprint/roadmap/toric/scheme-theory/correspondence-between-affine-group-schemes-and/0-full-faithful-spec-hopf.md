---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.hopfSpec.instFull, AlgebraicGeometry.hopfSpec.instFaithful, AlgebraicGeometry.hopfSpec.fullyFaithful
statement: formalized
proof: formalized
---

# Spec as a functor on Hopf algebras is fully faithful

Spec is a fully faithful contravariant functor from the category of $R$-Hopf algebras to the category of group schemes over $\operatorname{Spec}_R$.

## Depends on

- [Spec as a functor on Hopf algebras](0-spec-hopf.md)

## Proof depends on

- [Fully faithful product-preserving functors lift to monoid/group objects](../../category-theory/objects/0-full-faithful-grp.md)
- [Spec as a functor on algebras is fully faithful](0-full-faithful-spec-alg.md)

## Proof

$\operatorname{Spec} : \operatorname{Ring}_R \to \operatorname{Sch}_{\operatorname{Spec} R}$ is a fully faithful contravariant functor preserving all limits according to Proposition [Spec as a functor on algebras](0-spec-alg.md), therefore $\operatorname{Spec} : \operatorname{Hopf}_R \to \operatorname{GrpSch}_{\operatorname{Spec} R}$ too is fully faithful according to [Fully faithful product-preserving functors lift to monoid/group objects](../../category-theory/objects/0-full-faithful-grp.md).

## Lean

Formalized as [`AlgebraicGeometry.hopfSpec.instFull`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.hopfSpec.instFull), [`AlgebraicGeometry.hopfSpec.instFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.hopfSpec.instFaithful), [`AlgebraicGeometry.hopfSpec.fullyFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.hopfSpec.fullyFaithful).

## Sources

- [Toric varieties blueprint: chapters/4-1-affine-group-schemes.tex, line 113](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-1-affine-group-schemes.tex#L113)
