---
declaration: theorem
origin: cited
lean: Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two
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

## Lean

Formalized in Tau Ceti as [`Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two).

## Sources

- [Tau Ceti documentation: `Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.html#Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two)
- [Source of `Subgroup.one_le_abs_trace_sq_sub_four_add_abs_trace_commutatorElement_sub_two` in TauCeti/Analysis/Complex/Fuchsian/Jorgensen.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Jorgensen.lean#L503)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
