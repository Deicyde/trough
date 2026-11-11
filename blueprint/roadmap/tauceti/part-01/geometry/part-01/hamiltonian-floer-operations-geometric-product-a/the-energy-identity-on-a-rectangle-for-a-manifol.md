---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity
statement: formalized
proof: formalized
---

# The energy identity on a rectangle, for a manifold target

Let `u` and the perturbation
data `K = K_s ds + K_t dt` be `C¹` over an open neighbourhood `U` of a rectangle
`[a₁, b₁] × [a₂, b₂]`, for a nondegenerate two-form on a finite-dimensional manifold. If the
energy density and the curvature `R_K(u)` are integrable over the rectangle, then the energy over
the rectangle is the symplectic area `∫ u^* ω`, plus the integral of the pulled-back one-form
`K(u) = K_s(u) ds + K_t(u) dt` over the positively oriented boundary, minus the integral of
`R_K(u)`. Closedness of the two-form is not used.

```lean
TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {ω : TauCeti.SmoothTwoForm I M} {Ks Kt : ℝ × ℝ → M → ℝ} {u : ℝ × ℝ → M} [FiniteDimensional ℝ E]
  (hω : ω.IsNondegenerate) {U : Set (ℝ × ℝ)} (hU : IsOpen U)
  (hu : ContMDiffOn (modelWithCornersSelf ℝ (ℝ × ℝ)) I 1 u U)
  (hKs :
    ContMDiffOn ((modelWithCornersSelf ℝ (ℝ × ℝ)).prod I) (modelWithCornersSelf ℝ ℝ) 1
      (Function.uncurry Ks) (U ×ˢ Set.univ))
  (hKt :
    ContMDiffOn ((modelWithCornersSelf ℝ (ℝ × ℝ)).prod I) (modelWithCornersSelf ℝ ℝ) 1
      (Function.uncurry Kt) (U ×ˢ Set.univ))
  {a b : ℝ × ℝ} (hab : a ≤ b) (habU : Set.Icc a b ⊆ U)
  (hE :
    MeasureTheory.IntegrableOn (ω.floerEnergyDensity Ks Kt u) (Set.Icc a b) MeasureTheory.volume)
  (hR :
    MeasureTheory.IntegrableOn (fun z => ω.hamiltonianCurvature Ks Kt z (u z)) (Set.Icc a b)
      MeasureTheory.volume) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b, ω.floerEnergyDensity Ks Kt u z =
    (∫ (z : ℝ × ℝ) in Set.Icc a b,
          TauCeti.SmoothBundleForm.eval₂ ω (u z) ((mfderiv% u z) TauCeti.stdComplexLineReal)
            ((mfderiv% u z) TauCeti.stdComplexLineImag)) +
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

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Manifold.html#TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Manifold.html#TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity)
- [Source of `TauCeti.SmoothTwoForm.IsNondegenerate.integral_floerEnergyDensity` in TauCeti/Geometry/Symplectic/Floer/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Floer/Manifold.lean#L719)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
