# Linear map

A map `f` between an `R`-module and an `S`-module over a ring homomorphism `σ : R →+* S`
is semilinear if it satisfies the two properties `f (x + y) = f x + f y` and
`f (c • x) = (σ c) • f x`. Elements of `LinearMap σ M M₂` (available under the notation
`M →ₛₗ[σ] M₂`) are bundled versions of such maps. For plain linear maps (i.e. for which
`σ = RingHom.id R`), the notation `M →ₗ[R] M₂` is available. An unbundled version of plain linear
maps is available with the predicate `IsLinearMap`, but it should be avoided most of the time.

```lean
LinearMap.{u_14, u_15, u_16, u_17} {R : Type u_14} {S : Type u_15} [Semiring R] [Semiring S]
  (σ : R →+* S) (M : Type u_16) (M₂ : Type u_17) [AddCommMonoid M] [AddCommMonoid M₂]
  [_root_.Module R M] [_root_.Module S M₂] : Type (max u_16 u_17)
```

## Depends on

- [Module](module.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `LinearMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/LinearMap/Defs.html#LinearMap)
- [Source of `LinearMap` in Mathlib/Algebra/Module/LinearMap/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Module/LinearMap/Defs.lean#L78)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L170)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L18)
