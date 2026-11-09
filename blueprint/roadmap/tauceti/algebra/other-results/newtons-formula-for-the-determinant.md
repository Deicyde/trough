---
declaration: theorem
origin: cited
lean: TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul, TauCeti.AlbertAlgebra.six_mul_det
statement: formalized
proof: formalized
---

# Newton's formula for the determinant

when `2` and `3` are invertible,
`det A = (T(A)³ - 3 T(A) T(A ∘ A) + 2 T(A ∘ (A ∘ A))) / 6`.

```lean
TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul.{u_1} {R : Type u_1} [CommRing R]
  [Invertible 2] [Invertible 3] (A : TauCeti.AlbertAlgebra R) :
  A.det =
    ⅟2 * ⅟3 *
      (TauCeti.AlbertAlgebra.trace A ^ 3 -
          3 * TauCeti.AlbertAlgebra.trace A * TauCeti.AlbertAlgebra.trace (A * A) +
        2 * TauCeti.AlbertAlgebra.trace (A * (A * A)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/AlbertAlgebra/Determinant.html#TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul).

## Other forms

**Newton's formula for the determinant, without division.** Formalized in Tau Ceti as [`TauCeti.AlbertAlgebra.six_mul_det`](https://taucetiproject.org/docs/TauCeti/Algebra/AlbertAlgebra/Determinant.html#TauCeti.AlbertAlgebra.six_mul_det).

```lean
TauCeti.AlbertAlgebra.six_mul_det.{u_1} {R : Type u_1} [CommRing R] [Invertible 2]
  (A : TauCeti.AlbertAlgebra R) :
  6 * A.det =
    TauCeti.AlbertAlgebra.trace A ^ 3 -
        3 * TauCeti.AlbertAlgebra.trace A * TauCeti.AlbertAlgebra.trace (A * A) +
      2 * TauCeti.AlbertAlgebra.trace (A * (A * A))
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/AlbertAlgebra/Determinant.html#TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul)
- [Source of `TauCeti.AlbertAlgebra.det_eq_invOf_two_mul_invOf_three_mul` in TauCeti/Algebra/AlbertAlgebra/Determinant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlbertAlgebra/Determinant.lean#L317)
