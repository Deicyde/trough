# Finite-dimensionality

`FiniteDimensional` vector spaces are defined to be finite modules.
Use `Module.Basis.finiteDimensional_of_finite` to prove finite dimension from another definition.

```lean
FiniteDimensional.{u_1, u_2} (K : Type u_1) (V : Type u_2) [DivisionRing K] [AddCommGroup V]
  [_root_.Module K V] : Prop
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)
- [Ring](../../general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `FiniteDimensional`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/FiniteDimensional/Defs.html#FiniteDimensional)
- [Source of `FiniteDimensional` in Mathlib/LinearAlgebra/FiniteDimensional/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/FiniteDimensional/Defs.lean#L72)
- [Mathlib overview: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L184)
- [Mathlib undergraduate list: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L29)
