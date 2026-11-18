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
- [Source of `LinearIndependent` in Mathlib/LinearAlgebra/LinearIndependent/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/LinearIndependent/Defs.lean#L95)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L14)
