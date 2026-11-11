---
declaration: theorem
origin: cited
lean: Matrix.le_of_smul_le_mulVec, Matrix.ofReal_le_spectralRadius_of_smul_le_mulVec
statement: formalized
proof: formalized
---

# Collatz–Wielandt bound

Let `A` be entrywise nonnegative with `A v ≤ r v` for a vector `v`
all of whose entries are strictly positive. If `t y ≤ A y` entrywise for some nonzero nonnegative
vector `y`, then `t ≤ r`.

```lean
Matrix.le_of_smul_le_mulVec.{u_1, u_2} {n : Type u_1} [Fintype n] {K : Type u_2} [Semifield K]
  [LinearOrder K] [IsStrictOrderedRing K] {A : Matrix n n K} {v y : n → K} {r t : K}
  (hA : ∀ (i j : n), 0 ≤ A i j) (hv : ∀ (i : n), 0 < v i) (hAv : A.mulVec v ≤ r • v) (hy : 0 ≤ y)
  (hy0 : y ≠ 0) (h : t • y ≤ A.mulVec y) : t ≤ r
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Perron–Frobenius theorem for nonnegative matrices](perron-frobenius-theorem-for-nonnegative-matrice.md)

## Lean

Formalized in Tau Ceti as [`Matrix.le_of_smul_le_mulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.le_of_smul_le_mulVec).

## Other forms

**Collatz–Wielandt bound for nonnegative matrices.** Formalized in Tau Ceti as [`Matrix.ofReal_le_spectralRadius_of_smul_le_mulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Nonnegative.html#Matrix.ofReal_le_spectralRadius_of_smul_le_mulVec).

```lean
Matrix.ofReal_le_spectralRadius_of_smul_le_mulVec.{u_1} {n : Type u_1} [Fintype n]
  {A : Matrix n n ℝ} (hA : ∀ (i j : n), 0 ≤ A i j) {y : n → ℝ} {t : ℝ} (hy : 0 ≤ y) (hy0 : y ≠ 0)
  (h : t • y ≤ A.mulVec y) : ENNReal.ofReal t ≤ spectralRadius ℂ (A.map Complex.ofReal)
```

## Sources

- [Tau Ceti documentation: `Matrix.le_of_smul_le_mulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.html#Matrix.le_of_smul_le_mulVec)
- [Source of `Matrix.le_of_smul_le_mulVec` in TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Positive.lean#L98)
