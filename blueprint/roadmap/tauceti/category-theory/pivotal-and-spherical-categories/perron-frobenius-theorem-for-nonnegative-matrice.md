---
declaration: theorem
origin: cited
lean: Matrix.exists_mulVec_eq_smul_of_nonneg, Matrix.IsIrreducible.exists_mulVec_eq_smul, Matrix.exists_mulVec_eq_smul_of_pos
statement: formalized
proof: formalized
---

# Perron–Frobenius theorem for nonnegative matrices

an entrywise nonnegative real square
matrix has its spectral radius `r`, viewed as a complex matrix, as an eigenvalue, with an
eigenvector whose entries are nonnegative and not all zero.

Unlike the strictly positive and irreducible cases (`Matrix.exists_mulVec_eq_smul_of_pos` and
`Matrix.IsIrreducible.exists_mulVec_eq_smul`), the eigenvector may have zero entries and need not be
unique up to scalars, and `r` may be zero.

```lean
Matrix.exists_mulVec_eq_smul_of_nonneg.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  [Nonempty n] (hA : ∀ (i j : n), 0 ≤ A i j) :
  ∃ r,
    0 ≤ r ∧
      spectralRadius ℂ (A.map Complex.ofReal) = ENNReal.ofReal r ∧
        ∃ v, 0 ≤ v ∧ v ≠ 0 ∧ A.mulVec v = r • v
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Collatz–Wielandt bound](collatz-wielandt-bound.md)

## Lean

Formalized in Tau Ceti as [`Matrix.exists_mulVec_eq_smul_of_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.html#Matrix.exists_mulVec_eq_smul_of_nonneg).

## Other forms

**Perron–Frobenius theorem for irreducible matrices, existence.** Formalized in Tau Ceti as [`Matrix.IsIrreducible.exists_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.exists_mulVec_eq_smul).

```lean
Matrix.IsIrreducible.exists_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  [Nonempty n] (hA : A.IsIrreducible) : ∃ r, 0 < r ∧ ∃ v, (∀ (i : n), 0 < v i) ∧ A.mulVec v = r • v
```

**Perron–Frobenius theorem for positive matrices, existence.** Formalized in Tau Ceti as [`Matrix.exists_mulVec_eq_smul_of_pos`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.exists_mulVec_eq_smul_of_pos).

```lean
Matrix.exists_mulVec_eq_smul_of_pos.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ} [Nonempty n]
  (hA : ∀ (i j : n), 0 < A i j) : ∃ r, 0 < r ∧ ∃ v, (∀ (i : n), 0 < v i) ∧ A.mulVec v = r • v
```

## Sources

- [Tau Ceti documentation: `Matrix.exists_mulVec_eq_smul_of_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.html#Matrix.exists_mulVec_eq_smul_of_nonneg)
- [Source of `Matrix.exists_mulVec_eq_smul_of_nonneg` in TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.lean#L142)
