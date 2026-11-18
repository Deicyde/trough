# Isomorphism with bidual

The bijection between a reflexive module and its double dual, bundled as a `LinearEquiv`.

```lean
Module.evalEquiv.{u_1, u_2} (R : Type u_1) (M : Type u_2) [CommSemiring R] [AddCommMonoid M]
  [_root_.Module R M] [Module.IsReflexive R M] : M ≃ₗ[R] Module.Dual R (Module.Dual R M)
```

## Depends on

- [Dual vector space](../duality/dual-vector-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Module.evalEquiv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual/Defs.html#Module.evalEquiv)
- [Source of `Module.evalEquiv` in Mathlib/LinearAlgebra/Dual/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/Dual/Defs.lean#L214)
- [Mathlib overview: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L186)
- [Mathlib undergraduate list: Linear algebra › Finite-dimensional vector spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L34)
