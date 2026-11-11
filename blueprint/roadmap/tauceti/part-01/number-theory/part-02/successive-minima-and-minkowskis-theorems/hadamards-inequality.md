---
declaration: theorem
origin: cited
lean: OrthonormalBasis.norm_det_le_prod_norm, exteriorPower.norm_ιMulti_le_prod_norm, exteriorPower.norm_ιMulti_two_le, Matrix.re_det_gram_le_pow
statement: formalized
proof: formalized
---

# Hadamard's inequality

The determinant of a family `v` in the coordinates of an
orthonormal basis has norm at most the product of the norms of the vectors. The family may be
linearly dependent.

```lean
OrthonormalBasis.norm_det_le_prod_norm.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι]
  (b : OrthonormalBasis ι 𝕜 E) (v : ι → E) : ‖b.toBasis.det v‖ ≤ ∏ i, ‖v i‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's inequality for Gram determinants, for the real part](hadamards-inequality-for-gram-determinants-for-t.md)

## Lean

Formalized in Tau Ceti as [`OrthonormalBasis.norm_det_le_prod_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#OrthonormalBasis.norm_det_le_prod_norm).

## Other forms

**Hadamard's inequality for wedges.** Formalized in Tau Ceti as [`exteriorPower.norm_ιMulti_le_prod_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ExteriorPower/Basic.html#exteriorPower.norm_%CE%B9Multi_le_prod_norm).

```lean
exteriorPower.norm_ιMulti_le_prod_norm.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {n : ℕ} (v : Fin n → E) :
  ‖(exteriorPower.ιMulti ℝ n) v‖ ≤ ∏ i, ‖v i‖
```

**Hadamard's inequality for two vectors.** Formalized in Tau Ceti as [`exteriorPower.norm_ιMulti_two_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ExteriorPower/Basic.html#exteriorPower.norm_%CE%B9Multi_two_le).

```lean
exteriorPower.norm_ιMulti_two_le.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] (u w : E) : ‖(exteriorPower.ιMulti ℝ 2) ![u, w]‖ ≤ ‖u‖ * ‖w‖
```

**Hadamard's inequality, uniform form.** Formalized in Tau Ceti as [`Matrix.re_det_gram_le_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#Matrix.re_det_gram_le_pow).

```lean
Matrix.re_det_gram_le_pow.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {ι : Type u_3} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] [DecidableEq ι] {v : ι → E} {D : ℝ}
  (hD : ∀ (i : ι), ‖v i‖ ^ 2 ≤ D) : RCLike.re (Matrix.gram 𝕜 v).det ≤ D ^ Fintype.card ι
```

## Sources

- [Tau Ceti documentation: `OrthonormalBasis.norm_det_le_prod_norm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.html#OrthonormalBasis.norm_det_le_prod_norm)
- [Source of `OrthonormalBasis.norm_det_le_prod_norm` in TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Gram/Hadamard.lean#L74)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
