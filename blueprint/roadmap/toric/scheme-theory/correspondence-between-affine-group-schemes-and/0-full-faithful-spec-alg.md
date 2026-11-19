---
declaration: proposition
origin: cited
lean: AlgebraicGeometry.preservesLimitsOfSize_algSpec, AlgebraicGeometry.algSpec.instFull, AlgebraicGeometry.algSpec.instFaithful, AlgebraicGeometry.algSpec.fullyFaithful
statement: formalized
proof: formalized
---

# Spec as a functor on algebras is fully faithful

Spec is a fully faithful contravariant functor from the category of $R$-algebras to the category of schemes over $\operatorname{Spec}_R$, preserving all limits.

## Depends on

- [Spec as a functor on algebras](0-spec-alg.md)

## Proof depends on

- [Sliced adjoint functors](../../category-theory/over-category/0-slice-adj.md)
- [Limit-preserving functors lift to over categories](../../category-theory/over-category/0-over-lim.md)

## Proof

$\operatorname{Spec} : \operatorname{Ring} \to \operatorname{Sch}$ is a fully faithful contravariant functor which preserves all limits, hence so is $\operatorname{Spec} : \operatorname{Ring}_R \to \operatorname{Sch}_{\operatorname{Spec} R}$ by Proposition [Limit-preserving functors lift to over categories](../../category-theory/over-category/0-over-lim.md) (alternatively, by Proposition [Sliced adjoint functors](../../category-theory/over-category/0-slice-adj.md)).

## Lean

Formalized as [`AlgebraicGeometry.preservesLimitsOfSize_algSpec`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.preservesLimitsOfSize_algSpec), [`AlgebraicGeometry.algSpec.instFull`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.algSpec.instFull), [`AlgebraicGeometry.algSpec.instFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.algSpec.instFaithful), [`AlgebraicGeometry.algSpec.fullyFaithful`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.algSpec.fullyFaithful).

## Sources

- [Toric varieties blueprint: chapters/4-1-affine-group-schemes.tex, line 31](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-1-affine-group-schemes.tex#L31)
