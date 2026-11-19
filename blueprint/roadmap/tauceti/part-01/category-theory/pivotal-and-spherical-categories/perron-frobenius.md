---
declaration: theorem
origin: cited
lean: Matrix.IsPrimitive.norm_lt_of_mem_spectrum, Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one, Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul, Matrix.IsPrimitive.norm_lt_of_mulVec_eq_smul, Matrix.eq_of_norm_eq_of_mulVec_eq_smul, Matrix.spectralRadius_eq_of_mulVec_eq_smul
statement: formalized
proof: formalized
---

# Perron–Frobenius

if `A v = r v` for a primitive real matrix `A` and a vector `v` with
strictly positive entries, then every point `μ ≠ r` of the spectrum of `A`, viewed as a complex
matrix, has `‖μ‖ < r`.

```lean
Matrix.IsPrimitive.norm_lt_of_mem_spectrum.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} {μ : ℂ} (hA : A.IsPrimitive) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) (hμ : μ ∈ spectrum ℂ (A.map Complex.ofReal)) (hμr : μ ≠ ↑r) : ‖μ‖ < r
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Collatz–Wielandt bound](collatz-wielandt-bound.md)
- [Perron–Frobenius theorem for irreducible matrices, existence](perron-frobenius-theorem-for-irreducible-matrice.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsPrimitive.norm_lt_of_mem_spectrum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.html#Matrix.IsPrimitive.norm_lt_of_mem_spectrum).

## Other forms

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Irreducible.html#Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one).

```lean
Matrix.IsIrreducible.rootMultiplicity_charpoly_eq_one.{u_1} {n : Type u_1} [Fintype n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} [DecidableEq n] [Nonempty n] (hA : A.IsIrreducible)
  (hv : ∀ (i : n), 0 < v i) (hAv : A.mulVec v = r • v) :
  Polynomial.rootMultiplicity r A.charpoly = 1
```

**Perron–Frobenius.** Formalized in Tau Ceti as [`Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.html#Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul).

```lean
Matrix.IsPrimitive.eq_of_norm_eq_of_mulVec_eq_smul.{u_1} {n : Type u_1} [Fintype n] [DecidableEq n]
  {A : Matrix n n ℝ} {v : n → ℝ} {r : ℝ} {μ : ℂ} (hA : A.IsPrimitive) (hv : ∀ (i : n), 0 < v i)
  (hAv : A.mulVec v = r • v) {z : n → ℂ} (hz : z ≠ 0)
  (hAz : (A.map Complex.ofReal).mulVec z = μ • z) (hμ : ‖μ‖ = r) : μ = ↑r
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

## Sources

- [Tau Ceti documentation: `Matrix.IsPrimitive.norm_lt_of_mem_spectrum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.html#Matrix.IsPrimitive.norm_lt_of_mem_spectrum)
- [Source of `Matrix.IsPrimitive.norm_lt_of_mem_spectrum` in TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/Matrix/PerronFrobenius/Primitive.lean#L87)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
