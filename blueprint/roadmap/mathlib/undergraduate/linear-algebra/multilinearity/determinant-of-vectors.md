# Determinant of vectors

The determinant of a family of vectors with respect to some basis, as an alternating
multilinear map.

```lean
Module.Basis.det.{u_1, u_2, u_4} {R : Type u_1} [CommRing R] {M : Type u_2} [AddCommGroup M]
  [_root_.Module R M] {ι : Type u_4} [DecidableEq ι] [Fintype ι] (e : Module.Basis ι R M) :
  M [⋀^ι]→ₗ[R] R
```

## Depends on

- [Basis](../../../overview/linear-algebra/fundamentals/basis.md)
- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)

## Sources

- [Mathlib documentation: `Module.Basis.det`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Determinant.html#Module.Basis.det)
- [Source of `Module.Basis.det` in Mathlib/LinearAlgebra/Determinant.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Determinant.lean#L586)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L37)
