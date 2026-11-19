---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.essImage_bialgSpec
statement: formalized
proof: formalized
---

# Essential image of Spec on bialgebras

The essential image of $\operatorname{Spec} : \operatorname{Bialg}_R \to \operatorname{GrpSch}_{\operatorname{Spec} R}$ is precisely affine monoid schemes over $\operatorname{Spec} R$.

## Depends on

- [Spec as a functor on bialgebras](0-spec-bialg.md)

## Proof depends on

- [Essential image of a functor on monoid/group objects](../../category-theory/objects/0-ess-image-grp.md)
- [Essential image of Spec on algebras](0-ess-image-spec-alg.md)
- [Spec as a functor on algebras is fully faithful](0-full-faithful-spec-alg.md)

## Proof

Direct consequence of Propositions [Essential image of a functor on monoid/group objects](../../category-theory/objects/0-ess-image-grp.md) and [Essential image of Spec on algebras](0-ess-image-spec-alg.md).

## Lean

Formalized as [`AlgebraicGeometry.essImage_bialgSpec`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.essImage_bialgSpec).

## Sources

- [Toric varieties blueprint: chapters/4-1-affine-group-schemes.tex, line 152](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-1-affine-group-schemes.tex#L152)
