# Dual basis

Maps a basis for `V` to a basis for the dual space.

```lean
Module.Basis.dualBasis.{uR, uM, uι} {R : Type uR} {M : Type uM} {ι : Type uι} [CommSemiring R]
  [AddCommMonoid M] [_root_.Module R M] [DecidableEq ι] (b : Module.Basis ι R M) [Finite ι] :
  Module.Basis ι R (Module.Dual R M)
```

## Depends on

- [Basis](../fundamentals/basis.md)
- [Dual vector space](dual-vector-space.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `Module.Basis.dualBasis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual/Basis.html#Module.Basis.dualBasis)
- [Source of `Module.Basis.dualBasis` in Mathlib/LinearAlgebra/Dual/Basis.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Dual/Basis.lean#L131)
- [Mathlib overview: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L182)
- [Mathlib undergraduate list: Linear algebra › Duality](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L25)
