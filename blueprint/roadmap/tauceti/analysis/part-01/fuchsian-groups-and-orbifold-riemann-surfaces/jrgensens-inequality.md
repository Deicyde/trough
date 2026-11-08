---
declaration: theorem
origin: cited
lean: Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two, Subgroup.one_le_four_mul_sinh_sq_mul_of_dilation_mem, Subgroup.one_le_four_sub_trace_sq_mul_cosh_sq_of_smul_eq_self, Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_abs_trace_lt_two, Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_two_lt_abs_trace, Subgroup.one_le_abs_trace_commutatorElement_sub_two_of_isParabolic
statement: formalized
proof: formalized
---

# Jørgensen's inequality

Let `Γ ≤ PSL(2, ℝ)` be a discrete subgroup and let
`A, B ∈ SL(2, ℝ)` lift elements of `Γ`. Unless `B` conjugates the class of `A` to itself or to
its inverse, `|tr² A - 4| + |tr [A, B] - 2| ≥ 1`.

```lean
Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)}
  {B : Matrix.SpecialLinearGroup (Fin 2) ℝ} [DiscreteTopology ↥Γ]
  {A : Matrix.SpecialLinearGroup (Fin 2) ℝ} (hA : ↑A ∈ Γ) (hB : ↑B ∈ Γ) (h₁ : ↑B * ↑A * (↑B)⁻¹ ≠ ↑A)
  (h₂ : ↑B * ↑A * (↑B)⁻¹ ≠ (↑A)⁻¹) : 1 ≤ |(↑A).trace ^ 2 - 4| + |(↑⁅A, B⁆).trace - 2|
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimizu's lemma](shimizus-lemma.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two).

## Other forms

**Jørgensen's inequality for a dilation.** Formalized in Tau Ceti as [`Subgroup.one_le_four_mul_sinh_sq_mul_of_dilation_mem`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_four_mul_sinh_sq_mul_of_dilation_mem).

```lean
Subgroup.one_le_four_mul_sinh_sq_mul_of_dilation_mem
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} {s : ℝ}
  {B : Matrix.SpecialLinearGroup (Fin 2) ℝ} [DiscreteTopology ↥Γ]
  (hD : ↑(Matrix.SpecialLinearGroup.dilation s) ∈ Γ) (hB : ↑B ∈ Γ)
  (h₁ :
    ↑B * ↑(Matrix.SpecialLinearGroup.dilation s) * (↑B)⁻¹ ≠ ↑(Matrix.SpecialLinearGroup.dilation s))
  (h₂ :
    ↑B * ↑(Matrix.SpecialLinearGroup.dilation s) * (↑B)⁻¹ ≠
      ↑(Matrix.SpecialLinearGroup.dilation (-s))) :
  1 ≤ 4 * Real.sinh (s / 2) ^ 2 * (1 + |↑B 0 1 * ↑B 1 0|)
```

**Jørgensen's inequality for an element fixing a point.** Formalized in Tau Ceti as [`Subgroup.one_le_four_sub_trace_sq_mul_cosh_sq_of_smul_eq_self`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_four_sub_trace_sq_mul_cosh_sq_of_smul_eq_self).

```lean
Subgroup.one_le_four_sub_trace_sq_mul_cosh_sq_of_smul_eq_self
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  {A : Matrix.SpecialLinearGroup (Fin 2) ℝ} {B : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ}
  {z : UpperHalfPlane} (hA : ↑A ∈ Γ) (hB : B ∈ Γ) (hAz : A • z = z) (hA₁ : ↑A ≠ 1)
  (hBz : B • z ≠ z) : 1 ≤ (4 - (↑A).trace ^ 2) * Real.cosh (dist (B • z) z / 2) ^ 2
```

**Jørgensen's inequality for elliptic elements.** Formalized in Tau Ceti as [`Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_abs_trace_lt_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_abs_trace_lt_two).

```lean
Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_abs_trace_lt_two
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)}
  {B : Matrix.SpecialLinearGroup (Fin 2) ℝ} [DiscreteTopology ↥Γ]
  {A : Matrix.SpecialLinearGroup (Fin 2) ℝ} (hA : ↑A ∈ Γ) (hB : ↑B ∈ Γ) (hell : |(↑A).trace| < 2)
  (h₁ : ↑B * ↑A * (↑B)⁻¹ ≠ ↑A) : 1 ≤ |(↑A).trace ^ 2 - 4| + |(↑⁅A, B⁆).trace - 2|
```

**Jørgensen's inequality for hyperbolic elements.** Formalized in Tau Ceti as [`Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_two_lt_abs_trace`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_two_lt_abs_trace).

```lean
Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two_of_two_lt_abs_trace
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)}
  {B : Matrix.SpecialLinearGroup (Fin 2) ℝ} [DiscreteTopology ↥Γ]
  {A : Matrix.SpecialLinearGroup (Fin 2) ℝ} (hA : ↑A ∈ Γ) (hB : ↑B ∈ Γ) (hhyp : 2 < |(↑A).trace|)
  (h₁ : ↑B * ↑A * (↑B)⁻¹ ≠ ↑A) (h₂ : ↑B * ↑A * (↑B)⁻¹ ≠ (↑A)⁻¹) :
  1 ≤ |(↑A).trace ^ 2 - 4| + |(↑⁅A, B⁆).trace - 2|
```

**Jørgensen's inequality for parabolic elements.** Formalized in Tau Ceti as [`Subgroup.one_le_abs_trace_commutatorElement_sub_two_of_isParabolic`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_commutatorElement_sub_two_of_isParabolic).

```lean
Subgroup.one_le_abs_trace_commutatorElement_sub_two_of_isParabolic
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)}
  {B : Matrix.SpecialLinearGroup (Fin 2) ℝ} [DiscreteTopology ↥Γ]
  {A : Matrix.SpecialLinearGroup (Fin 2) ℝ} (hA : ↑A ∈ Γ) (hB : ↑B ∈ Γ)
  (hpar : Matrix.ProjectiveSpecialLinearGroup.IsParabolic ↑A) (h₁ : ↑B * ↑A * (↑B)⁻¹ ≠ ↑A) :
  1 ≤ |(↑⁅A, B⁆).trace - 2|
```

## Sources

- [Tau Ceti documentation: `Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two)
- [Source of `Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two` in TauCeti/Analysis/Complex/Fuchsian/Jorgensen.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.lean#L503)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
