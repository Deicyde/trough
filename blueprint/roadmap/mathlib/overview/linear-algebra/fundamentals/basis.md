# Basis

A `Basis ι R M` for a module `M` is the type of `ι`-indexed `R`-bases of `M`.

The basis vectors are available as `DFunLike.coe (b : Basis ι R M) : ι → M`.
To turn a linear independent family of vectors spanning `M` into a basis, use `Basis.mk`.
They are internally represented as linear equivs `M ≃ₗ[R] (ι →₀ R)`,
available as `Basis.repr`.

```lean
Module.Basis.{u_1, u_3, u_4} (ι : Type u_1) (R : Type u_3) (M : Type u_4) [Semiring R]
  [AddCommMonoid M] [_root_.Module R M] : Type (max (max u_1 u_3) u_4)
```

## Depends on

- [Finitely supported function](../../data-structures/maps/finitely-supported-function.md)
- [Linear map](linear-map.md)

## Sources

- [Mathlib documentation: `Module.Basis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Basis/Defs.html#Module.Basis)
- [Source of `Module.Basis` in Mathlib/LinearAlgebra/Basis/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/Basis/Defs.lean#L81)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L176)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L16)
