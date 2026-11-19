---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero
statement: formalized
proof: formalized
---

# The pre-gluing error of two Floer cylinders

Under the hypotheses of
`TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le`, suppose moreover that `u`
and `v` solve the Floer equation on `ℝ × [0, 1]`. Then for every large gluing parameter `R`, the
Floer operator of the pre-glued map `w_R` is at most `C' e^{-κ R}` on all of `ℝ × [0, 1]`.

```lean
TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  (ω : TauCeti.SymplecticForm V) {J : ℝ → V → V →L[ℝ] V} {H : ℝ → V → ℝ} {x : ℝ → V}
  {u v : ℝ × ℝ → V} {C κ : ℝ} (hH : ContDiff ℝ 2 (Function.uncurry H))
  (hJ : Continuous (Function.uncurry J))
  (hx : ∀ (t : ℝ), HasDerivAt x (ω.hamiltonianVectorField (H t) (x t)) t) (hκ : 0 < κ)
  (hud : ∀ᶠ (s : ℝ) in Filter.atTop, ∀ t ∈ Set.Icc 0 1, DifferentiableAt ℝ u (s, t))
  (hu : ∀ᶠ (s : ℝ) in Filter.atTop, ∀ t ∈ Set.Icc 0 1, ‖u (s, t) - x t‖ ≤ C * Real.exp (-(κ * s)))
  (hdu :
    ∀ᶠ (s : ℝ) in Filter.atTop,
      ∀ t ∈ Set.Icc 0 1,
        ‖fderiv ℝ u (s, t) -
              (ContinuousLinearMap.snd ℝ ℝ ℝ).smulRight (ω.hamiltonianVectorField (H t) (x t))‖ ≤
          C * Real.exp (-(κ * s)))
  (hvd : ∀ᶠ (s : ℝ) in Filter.atBot, ∀ t ∈ Set.Icc 0 1, DifferentiableAt ℝ v (s, t))
  (hv : ∀ᶠ (s : ℝ) in Filter.atBot, ∀ t ∈ Set.Icc 0 1, ‖v (s, t) - x t‖ ≤ C * Real.exp (κ * s))
  (hdv :
    ∀ᶠ (s : ℝ) in Filter.atBot,
      ∀ t ∈ Set.Icc 0 1,
        ‖fderiv ℝ v (s, t) -
              (ContinuousLinearMap.snd ℝ ℝ ℝ).smulRight (ω.hamiltonianVectorField (H t) (x t))‖ ≤
          C * Real.exp (κ * s))
  (huF :
    ∀ z ∈ Set.univ ×ˢ Set.Icc 0 1,
      ω.floerOperator (fun p => J p.2) (fun x x_1 => 0) (fun p => H p.2) u z = 0)
  (hvF :
    ∀ z ∈ Set.univ ×ˢ Set.Icc 0 1,
      ω.floerOperator (fun p => J p.2) (fun x x_1 => 0) (fun p => H p.2) v z = 0) :
  ∃ C',
    ∀ᶠ (R : ℝ) in Filter.atTop,
      ∀ z ∈ Set.univ ×ˢ Set.Icc 0 1,
        ‖ω.floerOperator (fun p => J p.2) (fun x x_1 => 0) (fun p => H p.2)
              (TauCeti.Floer.preglue x u v R) z‖ ≤
          C' * Real.exp (-(κ * R))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Uniform Lipschitz bound at a compact family of base points](../../../analysis/part-03/calculus/part-03/uniform-lipschitz-bound-at-a-compact-family-of-b.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Pregluing.html#TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Pregluing.html#TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero)
- [Source of `TauCeti.SymplecticForm.exists_eventually_norm_floerOperator_preglue_le_of_floerOperator_eq_zero` in TauCeti/Geometry/Symplectic/Floer/Pregluing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/Pregluing.lean#L529)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
