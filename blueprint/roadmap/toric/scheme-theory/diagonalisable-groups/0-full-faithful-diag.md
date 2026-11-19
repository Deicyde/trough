---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.full_diagFunctor, AlgebraicGeometry.Scheme.faithful_diagFunctor
statement: formalized
proof: formalized
---

# 0-full-faithful-diag

Let $R$ be a domain. The functor $D_R(G) := G \rightsquigarrow \operatorname{Spec} R[G]$ from the category of groups to the category of group schemes over $\operatorname{Spec} R$ is fully faithful.

## Depends on

- [The diagonalisable group scheme functor](0-diag.md)

## Proof depends on

- [Spec as a functor on Hopf algebras is fully faithful](../correspondence-between-affine-group-schemes-and/0-full-faithful-spec-hopf.md)
- [The group algebra functor is fully faithful](../../algebra/hopf-algebras/0-full-faithful-grp-alg.md)

## Proof

Compose Propositions [Spec as a functor on Hopf algebras is fully faithful](../correspondence-between-affine-group-schemes-and/0-full-faithful-spec-hopf.md) and [The group algebra functor is fully faithful](../../algebra/hopf-algebras/0-full-faithful-grp-alg.md).

Also see Theorem 12.9(a) in (Milne 2017). See SGA III Exposé VIII for a proof that works for $R$ an arbitrary commutative ring.

## Lean

Formalized as [`AlgebraicGeometry.Scheme.full_diagFunctor`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.full_diagFunctor), [`AlgebraicGeometry.Scheme.faithful_diagFunctor`](https://yaeldillies.github.io/toric/docs/find/#doc/AlgebraicGeometry.Scheme.faithful_diagFunctor).

## Sources

- [Toric varieties blueprint: chapters/4-2-diag.tex, line 59](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/4-2-diag.tex#L59)
