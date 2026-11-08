---
declaration: theorem
origin: cited
lean: Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one, Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul, Matrix.IsPrimitive.norm_lt_of_mem_spectrum, Matrix.IsPrimitive.norm_lt_of_mulVec_eq_smul, Matrix.eq_of_norm_eq_of_mulVec_eq_smul, Matrix.spectralRadius_eq_of_mulVec_eq_smul, Matrix.IsIrreducible.exists_mulVec_eq_smul, Matrix.exists_mulVec_eq_smul_of_nonneg, Matrix.exists_mulVec_eq_smul_of_pos
statement: formalized
proof: formalized
---

# Perron–Frobenius

the eigenvalue `r` of a strictly positive eigenvector of an irreducible
real matrix is a simple root of its characteristic polynomial.

```lean
Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one.{u_1} {n : Type u_1} [Fintype n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} [DecidableEq n] [Nonempty n] (hA : A.IsIrreducible)
  (hv : ∀ (i : n), 0 < v i) (hAv : A.mulVec v = r • v) :
  Polynomial.rootMultiplicity r A.charpoly = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Collatz–Wielandt bound](collatz-wielandt-bound.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one).

## Other forms

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.html#Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul).

```lean
Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} {μ : ℂ} (hA : A.IsPrimitive) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) {z : n → ℂ} (hz : z ≠ 0)
  (hAz : (A.map Complex.ofReal).mulVec z = μ • z) (hμ : ‖μ‖ = r) : μ = ↑r
```

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.IsPrimitive.norm_lt_of_mem_spectrum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.html#Matrix.IsPrimitive.norm_lt_of_mem_spectrum).

```lean
Matrix.IsPrimitive.norm_lt_of_mem_spectrum.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} {μ : ℂ} (hA : A.IsPrimitive) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) (hμ : μ ∈ spectrum ℂ (A.map Complex.ofReal)) (hμr : μ ≠ ↑r) : ‖μ‖ < r
```

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.IsPrimitive.norm_lt_of_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.html#Matrix.IsPrimitive.norm_lt_of_mulVec_eq_smul).

```lean
Matrix.IsPrimitive.norm_lt_of_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} {μ : ℂ} (hA : A.IsPrimitive) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) {z : n → ℂ} (hz : z ≠ 0)
  (hAz : (A.map Complex.ofReal).mulVec z = μ • z) (hμ : μ ≠ ↑r) : ‖μ‖ < r
```

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.eq_of_norm_eq_of_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.eq_of_norm_eq_of_mulVec_eq_smul).

```lean
Matrix.eq_of_norm_eq_of_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  {v : n → ℝ} {r : ℝ} (hA : ∀ (i j : n), 0 < A i j) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) {μ : ℂ} {z : n → ℂ} (hz : z ≠ 0)
  (hAz : (A.map Complex.ofReal).mulVec z = μ • z) (hμ : ‖μ‖ = r) : μ = ↑r
```

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.spectralRadius_eq_of_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.spectralRadius_eq_of_mulVec_eq_smul).

```lean
Matrix.spectralRadius_eq_of_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  {v : n → ℝ} {r : ℝ} [Nonempty n] (hA : ∀ (i j : n), 0 ≤ A i j) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) : spectralRadius ℂ (A.map Complex.ofReal) = ENNReal.ofReal r
```

**Perron–Frobenius theorem for irreducible matrices, existence.** Formalized in Tau Ceti as [`Matrix.IsIrreducible.exists_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.exists_mulVec_eq_smul).

```lean
Matrix.IsIrreducible.exists_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  [Nonempty n] (hA : A.IsIrreducible) : ∃ r, 0 < r ∧ ∃ v, (∀ (i : n), 0 < v i) ∧ A.mulVec v = r • v
```

**Perron–Frobenius theorem for nonnegative matrices.** Formalized in Tau Ceti as [`Matrix.exists_mulVec_eq_smul_of_nonneg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.html#Matrix.exists_mulVec_eq_smul_of_nonneg).

```lean
Matrix.exists_mulVec_eq_smul_of_nonneg.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ}
  [Nonempty n] (hA : ∀ (i j : n), 0 ≤ A i j) :
  ∃ r,
    0 ≤ r ∧
      spectralRadius ℂ (A.map Complex.ofReal) = ENNReal.ofReal r ∧
        ∃ v, 0 ≤ v ∧ v ≠ 0 ∧ A.mulVec v = r • v
```

**Perron–Frobenius theorem for positive matrices, existence.** Formalized in Tau Ceti as [`Matrix.exists_mulVec_eq_smul_of_pos`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.exists_mulVec_eq_smul_of_pos).

```lean
Matrix.exists_mulVec_eq_smul_of_pos.{u_1} {n : Type u_1} [Fintype n] {A : Matrix n n ℝ} [Nonempty n]
  (hA : ∀ (i j : n), 0 < A i j) : ∃ r, 0 < r ∧ ∃ v, (∀ (i : n), 0 < v i) ∧ A.mulVec v = r • v
```

## Sources

- [Tau Ceti documentation: `Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one)
- [Source of `Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one` in TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.lean#L243)
