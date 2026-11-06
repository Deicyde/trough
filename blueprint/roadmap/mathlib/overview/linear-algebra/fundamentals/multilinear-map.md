# Multilinear map

Multilinear maps over the ring `R`, from `∀ i, M₁ i` to `M₂` where `M₁ i` and `M₂` are modules
over `R`.

```lean
MultilinearMap.{uR, uι, v₁, v₂} (R : Type uR) {ι : Type uι} (M₁ : ι → Type v₁) (M₂ : Type v₂)
  [Semiring R] [(i : ι) → AddCommMonoid (M₁ i)] [AddCommMonoid M₂]
  [(i : ι) → _root_.Module R (M₁ i)] [_root_.Module R M₂] : Type (max (max uι v₁) v₂)
```

## Depends on

- [Module](module.md)

## Sources

- [Mathlib documentation: `MultilinearMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Multilinear/Basic.html#MultilinearMap)
- [Source of `MultilinearMap` in Mathlib/LinearAlgebra/Multilinear/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Multilinear/Basic.lean#L88)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L177)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L36)
