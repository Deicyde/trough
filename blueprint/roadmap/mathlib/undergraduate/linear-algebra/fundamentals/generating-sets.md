# Generating sets

The span of a set `s ⊆ M` is the smallest submodule of M that contains `s`.

```lean
Submodule.span.{u_1, u_2} (R : Type u_1) {M : Type u_2} [Semiring R] [AddCommMonoid M]
  [_root_.Module R M] (s : Set M) : Submodule R M
```

## Depends on

- [Module](../../../overview/linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `Submodule.span`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Span/Defs.html#Submodule.span)
- [Source of `Submodule.span` in Mathlib/LinearAlgebra/Span/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Span/Defs.lean#L45)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L15)
