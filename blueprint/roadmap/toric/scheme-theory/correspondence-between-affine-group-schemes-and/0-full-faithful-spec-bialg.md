---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.bialgSpec.instFull, AlgebraicGeometry.bialgSpec.instFaithful, AlgebraicGeometry.bialgSpec.fullyFaithful
statement: formalized
proof: formalized
---

# Spec as a functor on bialgebras is fully faithful

Spec is a fully faithful contravariant functor from the category of $R$-bialgebras to the category of monoid schemes over $\operatorname{Spec}_R$.

## Depends on

- [Spec as a functor on bialgebras](0-spec-bialg.md)

## Proof depends on

- [Fully faithful product-preserving functors lift to monoid/group objects](../../category-theory/objects/0-full-faithful-grp.md)
- [Spec as a functor on algebras is fully faithful](0-full-faithful-spec-alg.md)

## Proof

$\operatorname{Spec} : \operatorname{Ring}_R \to \operatorname{Sch}_{\operatorname{Spec} R}$ is a fully faithful contravariant functor preserving all limits according to Proposition [Spec as a functor on algebras](0-spec-alg.md), therefore $\operatorname{Spec} : \operatorname{Bialg}_R \to \operatorname{GrpSch}_{\operatorname{Spec} R}$ too is fully faithful according to [Fully faithful product-preserving functors lift to monoid/group objects](../../category-theory/objects/0-full-faithful-grp.md).

## Lean

Formalized as [`AlgebraicGeometry.bialgSpec.instFull`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.bialgSpec.instFull), [`AlgebraicGeometry.bialgSpec.instFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.bialgSpec.instFaithful), [`AlgebraicGeometry.bialgSpec.fullyFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.bialgSpec.fullyFaithful).

## Sources

- [Toric varieties blueprint: chapters/4-1-affine-group-schemes.tex, line 64](https://github.com/YaelDillies/toric/blob/97b1287db93f2eee84c8bb4e408058d9e721ce5b/blueprint/src/chapters/4-1-affine-group-schemes.tex#L64)
