---
declaration: theorem
origin: cited
lean: Matrix.re_det_gram_le_prod_norm_sq, Matrix.abs_det_le_prod_norm_toLp, Matrix.norm_det_le_prod_norm_toLp, Matrix.det_gram_le_prod_norm_sq, Matrix.log_re_det_gram_le, Matrix.log_det_gram_le
statement: formalized
proof: formalized
---

# Hadamard's inequality for Gram determinants, for the real part

the real part of the Gram
determinant of a finite family is at most the product of the squared norms of its vectors.

```lean
Matrix.re_det_gram_le_prod_norm_sq.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι]
  (v : ι → E) : RCLike.re (Matrix.gram 𝕜 v).det ≤ ∏ i, ‖v i‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Hadamard's inequality](hadamards-inequality.md)

## Lean

Formalized in Tau Ceti as [`Matrix.re_det_gram_le_prod_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.re_det_gram_le_prod_norm_sq).

## Other forms

**Hadamard's inequality for a real square matrix.** Formalized in Tau Ceti as [`Matrix.abs_det_le_prod_norm_toLp`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.abs_det_le_prod_norm_toLp).

```lean
Matrix.abs_det_le_prod_norm_toLp.{u_3} {ι : Type u_3} [Fintype ι] [DecidableEq ι]
  (A : Matrix ι ι ℝ) : |A.det| ≤ ∏ i, ‖WithLp.toLp 2 (A i)‖
```

**Hadamard's inequality for a square matrix.** Formalized in Tau Ceti as [`Matrix.norm_det_le_prod_norm_toLp`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.norm_det_le_prod_norm_toLp).

```lean
Matrix.norm_det_le_prod_norm_toLp.{u_1, u_3} {𝕜 : Type u_1} {ι : Type u_3} [RCLike 𝕜] [Fintype ι]
  [DecidableEq ι] (A : Matrix ι ι 𝕜) : ‖A.det‖ ≤ ∏ i, ‖WithLp.toLp 2 (A i)‖
```

**Hadamard's inequality for Gram determinants.** Formalized in Tau Ceti as [`Matrix.det_gram_le_prod_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.det_gram_le_prod_norm_sq).

```lean
Matrix.det_gram_le_prod_norm_sq.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι]
  (v : ι → E) : (Matrix.gram 𝕜 v).det ≤ ∏ i, ↑‖v i‖ ^ 2
```

**Hadamard's inequality for Gram determinants, logarithmic form.** Formalized in Tau Ceti as [`Matrix.log_re_det_gram_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.log_re_det_gram_le).

```lean
Matrix.log_re_det_gram_le.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι] {v : ι → E}
  (hv : LinearIndependent 𝕜 v) :
  Real.log (RCLike.re (Matrix.gram 𝕜 v).det) ≤ ∑ i, 2 * Real.log ‖v i‖
```

**Hadamard's inequality for Gram determinants, real logarithmic form.** Formalized in Tau Ceti as [`Matrix.log_det_gram_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.log_det_gram_le).

```lean
Matrix.log_det_gram_le.{u_3, u_4} {ι : Type u_3} [Fintype ι] [DecidableEq ι] {F : Type u_4}
  [NormedAddCommGroup F] [InnerProductSpace ℝ F] {v : ι → F} (hv : LinearIndependent ℝ v) :
  Real.log (Matrix.gram ℝ v).det ≤ ∑ i, 2 * Real.log ‖v i‖
```

## Sources

- [Tau Ceti documentation: `Matrix.re_det_gram_le_prod_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.re_det_gram_le_prod_norm_sq)
- [Source of `Matrix.re_det_gram_le_prod_norm_sq` in TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.lean#L154)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
