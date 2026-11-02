---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: LinearMap.range
mathlib_file: Mathlib/Algebra/Module/Submodule/Range.lean
---

# Range of a linear map

The range of a linear map `f : M → M₂` is a submodule of `M₂`.
See Note [range copy pattern].

```lean
LinearMap.range.{u_1, u_2, u_5, u_6} {R : Type u_1} {R₂ : Type u_2} {M : Type u_5} {M₂ : Type u_6}
  [Semiring R] [Semiring R₂] [AddCommMonoid M] [AddCommMonoid M₂] [_root_.Module R M]
  [_root_.Module R₂ M₂] {τ₁₂ : R →+* R₂} [RingHomSurjective τ₁₂] (f : M →ₛₗ[τ₁₂] M₂) :
  Submodule R₂ M₂
```

## Depends on

- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `LinearMap.range`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Submodule/Range.html#LinearMap.range)
- [Source of `LinearMap.range` in Mathlib/Algebra/Module/Submodule/Range.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Module/Submodule/Range.lean#L55)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L19)
