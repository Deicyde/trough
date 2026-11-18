---
declaration: module
origin: cited
lean: LinearMap.IsTracial, LinearMap.isTracial_iff_star_mul_self_eq_mul_star_self
statement: formalized
proof: formalized
---

# Tracial functionals

The module `Physlib.ProbabilisticTheory.StarAlgebra.Traciality`, [Physlib/ProbabilisticTheory/StarAlgebra/Traciality.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/Traciality.lean): 2 declarations, 2 with a docstring.

> A functional on an algebra is tracial if the order of a product does not change its value.

## i. Overview

> A functional `f` on an algebra is tracial if `f (x y) = f (y x)` for all `x` and `y`. The order
> of a product does not change its value.
>
> On an algebra with an adjoint it is enough to check `f (x⋆ x) = f (x x⋆)`. An operator and its
> adjoint then give the same value in both orders.

## ii. Key results

> - `LinearMap.IsTracial` : a complex-linear functional with `f (x * y) = f (y * x)`.
> - `LinearMap.isTracial_iff_star_mul_self_eq_mul_star_self` : `f` is tracial if and only if
>   `f (x⋆ * x) = f (x * x⋆)` for all `x`.

## iv. References

## A. Tracial functionals

**`LinearMap.IsTracial`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/Traciality.lean#L54).

> A complex-linear functional is tracial if `f (x * y) = f (y * x)` for all `x` and `y`.

```lean
def IsTracial (f : 𝒜 →ₗ[ℂ] ℂ) : Prop
```

## B. Checking on `x⋆ x`

> Apply the hypothesis to `x⋆ + y` and `x⋆ + i y`. The cross terms leave `C - C' = 0` and
> `C + C' = 0` for the commutators `C = f [x, y]` and `C' = f [x⋆, y⋆]`, so `C = 0`.

**`LinearMap.isTracial_iff_star_mul_self_eq_mul_star_self`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/Traciality.lean#L69).

> A functional is tracial if and only if `f (x⋆ x) = f (x x⋆)` for all `x`.

```lean
lemma isTracial_iff_star_mul_self_eq_mul_star_self (f : 𝒜 →ₗ[ℂ] ℂ) :
    f.IsTracial ↔ ∀ x : 𝒜, f (star x * x) = f (x * star x)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/ProbabilisticTheory/StarAlgebra/Traciality.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/StarAlgebra/Traciality.lean)
