# Linear independence

`LinearIndependent R v` states the family of vectors `v` is linearly independent over `R`.

```lean
LinearIndependent.{u', u_2, u_4} {ι : Type u'} (R : Type u_2) {M : Type u_4} (v : ι → M)
  [Semiring R] [AddCommMonoid M] [_root_.Module R M] : Prop
```

## Depends on

- [Finitely supported function](../../../overview/data-structures/maps/finitely-supported-function.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `LinearIndependent`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/LinearIndependent/Defs.html#LinearIndependent)
- [Source of `LinearIndependent` in Mathlib/LinearAlgebra/LinearIndependent/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/LinearIndependent/Defs.lean#L97)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L14)
