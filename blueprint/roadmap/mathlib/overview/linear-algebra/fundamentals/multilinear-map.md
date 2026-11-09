# Multilinear map

Multilinear maps from the `R`-module `Π i, M i` to the `S`-module `N`
over a ring homomorphism `σ : R →+* S`.

```lean
MultilinearMap.{uR, uS, uι, u, v} {R : Type uR} {S : Type uS} [Semiring R] [Semiring S]
  (σ : R →+* S) {ι : Type uι} (M : ι → Type u) (N : Type v) [(i : ι) → AddCommMonoid (M i)]
  [AddCommMonoid N] [(i : ι) → _root_.Module R (M i)] [_root_.Module S N] : Type (max (max u uι) v)
```

## Depends on

- [Module](module.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `MultilinearMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Multilinear/Basic.html#MultilinearMap)
- [Source of `MultilinearMap` in Mathlib/LinearAlgebra/Multilinear/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Multilinear/Basic.lean#L89)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L177)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L36)
