---
declaration: theorem
origin: cited
lean: Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem, Subgroup.im_smul_mul_im_le_abs_mul_of_upperRightHom_mem, Subgroup.im_smul_mul_im_le_sq_of_upperRightHom_mem
statement: formalized
proof: formalized
---

# Shimizu's lemma

Let `Γ ≤ PSL(2, ℝ)` be a discrete subgroup containing the translation
`z ↦ z + w` with `w ≠ 0`, and let `A ∈ SL(2, ℝ)` lift an element of `Γ`. If the lower-left entry
of `A` does not vanish, that is, if the element does not fix `∞`, then that entry has absolute
value at least `|w|⁻¹`. Both lifts of the element give the same absolute value.

```lean
Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} {w : ℝ}
  {A : Matrix.SpecialLinearGroup (Fin 2) ℝ} [DiscreteTopology ↥Γ] (hw : w ≠ 0)
  (hT : Matrix.ProjectiveSpecialLinearGroup.upperRightHom w ∈ Γ) (hA : ↑A ∈ Γ) (hA0 : ↑A 1 0 ≠ 0) :
  |w|⁻¹ ≤ |↑A 1 0|
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Shimizu.html#Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem).

## Other forms

**Shimizu's lemma for two parabolic fixed points, geometric form.** Formalized in Tau Ceti as [`Subgroup.im_smul_mul_im_le_abs_mul_of_upperRightHom_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Shimizu.html#Subgroup.im_smul_mul_im_le_abs_mul_of_upperRightHom_mem).

```lean
Subgroup.im_smul_mul_im_le_abs_mul_of_upperRightHom_mem
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} {w : ℝ} [DiscreteTopology ↥Γ]
  {w' : ℝ} (hw : w ≠ 0) (hw' : w' ≠ 0)
  (hT : Matrix.ProjectiveSpecialLinearGroup.upperRightHom w ∈ Γ)
  {h : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ}
  (hh : h * Matrix.ProjectiveSpecialLinearGroup.upperRightHom w' * h⁻¹ ∈ Γ)
  (hinf : h • OnePoint.infty ≠ OnePoint.infty) (z : UpperHalfPlane) : (h • z).im * z.im ≤ |w * w'|
```

**Shimizu's lemma, geometric form.** Formalized in Tau Ceti as [`Subgroup.im_smul_mul_im_le_sq_of_upperRightHom_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Shimizu.html#Subgroup.im_smul_mul_im_le_sq_of_upperRightHom_mem).

```lean
Subgroup.im_smul_mul_im_le_sq_of_upperRightHom_mem
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} {w : ℝ} [DiscreteTopology ↥Γ]
  (hw : w ≠ 0) (hT : Matrix.ProjectiveSpecialLinearGroup.upperRightHom w ∈ Γ)
  {g : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ} (hg : g ∈ Γ)
  (hginf : g • OnePoint.infty ≠ OnePoint.infty) (z : UpperHalfPlane) : (g • z).im * z.im ≤ w ^ 2
```

## Sources

- [Tau Ceti documentation: `Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Shimizu.html#Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem)
- [Source of `Subgroup.inv_le_abs_apply_one_zero_of_upperRightHom_mem` in TauCeti/Analysis/Complex/Fuchsian/Shimizu.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Shimizu.lean#L229)
