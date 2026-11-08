---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.integral_floerEnergyDensity
statement: formalized
proof: formalized
---

# The energy identity on a rectangle

For a map `u` and perturbation data that are `C¹` over
an open neighbourhood of a rectangle `[a₁, b₁] × [a₂, b₂]`, the integral of the Floer energy
density over the rectangle is the symplectic area, plus the integral of the pulled-back one-form
`K(u) = K_s(u) ds + K_t(u) dt` over the positively oriented boundary, minus the integral of the
curvature `R_K(u)`.

```lean
TauCeti.SymplecticForm.integral_floerEnergyDensity.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] {Ks Kt : ℝ × ℝ → V → ℝ} {u : ℝ × ℝ → V}
  (ω : TauCeti.SymplecticForm V) {U : Set (ℝ × ℝ)} (hU : IsOpen U) (hu : ContDiffOn ℝ 1 u U)
  (hKs : ContDiffOn ℝ 1 (Function.uncurry Ks) (U ×ˢ Set.univ))
  (hKt : ContDiffOn ℝ 1 (Function.uncurry Kt) (U ×ˢ Set.univ)) {a b : ℝ × ℝ} (hab : a ≤ b)
  (habU : Set.Icc a b ⊆ U) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b, ω.floerEnergyDensity Ks Kt u z =
    (∫ (z : ℝ × ℝ) in Set.Icc a b,
          (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) TauCeti.stdComplexLineReal)
            ((fderiv ℝ u z) TauCeti.stdComplexLineImag)) +
        ((((∫ (s : ℝ) in a.1..b.1, Ks (s, a.2) (u (s, a.2))) +
              ∫ (t : ℝ) in a.2..b.2, Kt (b.1, t) (u (b.1, t))) -
            ∫ (s : ℝ) in a.1..b.1, Ks (s, b.2) (u (s, b.2))) -
          ∫ (t : ℝ) in a.2..b.2, Kt (a.1, t) (u (a.1, t))) -
      ∫ (z : ℝ × ℝ) in Set.Icc a b, ω.hamiltonianCurvature Ks Kt z (u z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Green's theorem on a rectangle](../../../analysis/part-02/calculus/part-01/greens-theorem-on-a-rectangle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_floerEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Energy.html#TauCeti.SymplecticForm.integral_floerEnergyDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.integral_floerEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Energy.html#TauCeti.SymplecticForm.integral_floerEnergyDensity)
- [Source of `TauCeti.SymplecticForm.integral_floerEnergyDensity` in TauCeti/Geometry/Symplectic/Floer/Energy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/Energy.lean#L559)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
