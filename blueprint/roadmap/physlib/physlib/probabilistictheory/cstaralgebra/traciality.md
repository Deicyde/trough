---
declaration: module
origin: cited
lean: LinearMap.map_mul_comm_iff_star_mul_self_eq_mul_star_self
statement: formalized
proof: formalized
---

# Tracial functionals

The module `Physlib.ProbabilisticTheory.CStarAlgebra.Traciality`, [Physlib/ProbabilisticTheory/CStarAlgebra/Traciality.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Traciality.lean): 1 declaration, 1 with a docstring.

> A functional on an algebra is tracial if the order of a product does not change its value.

## i. Overview

> A functional `f` on an algebra is tracial if `f (x y) = f (y x)` for all `x` and `y`. The order
> of a product does not change its value.
>
> On an algebra with an adjoint it is enough to check `f (x⋆ x) = f (x x⋆)`. An operator and its
> adjoint then give the same value in both orders.

## ii. Key results

> - `LinearMap.map_mul_comm_iff_star_mul_self_eq_mul_star_self` : `f` is tracial if and only if
>   `f (x⋆ * x) = f (x * x⋆)` for all `x`.

## iv. References

## A. Checking cyclicity on `x⋆ x`

**`LinearMap.map_mul_comm_iff_star_mul_self_eq_mul_star_self`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Traciality.lean#L51).

> A functional is tracial if and only if `f (x⋆ x) = f (x x⋆)` for all `x`.

```lean
lemma map_mul_comm_iff_star_mul_self_eq_mul_star_self [StarRing 𝒜] [IsScalarTower ℂ 𝒜 𝒜]
    [SMulCommClass ℂ 𝒜 𝒜] [StarModule ℂ 𝒜] (f : 𝒜 →ₗ[ℂ] ℂ) :
    (∀ x y : 𝒜, f (x * y) = f (y * x)) ↔ ∀ x : 𝒜, f (star x * x) = f (x * star x)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ProbabilisticTheory/CStarAlgebra/Traciality.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Traciality.lean)
