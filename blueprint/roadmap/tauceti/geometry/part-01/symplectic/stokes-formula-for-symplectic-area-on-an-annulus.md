---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.integral_fderiv_apply_annulus, TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides, TauCeti.SymplecticForm.integral_fderiv_apply_prod_Icc, TauCeti.SymplecticForm.integral_fderiv_apply_truncation, TauCeti.rectangleIntegral_mextDeriv, TauCeti.SymplecticForm.integral_fderiv_apply_punctured_disc
statement: formalized
proof: formalized
---

# Stokes' formula for symplectic area on an annulus

The pullback area of a `C²` map is
the outer boundary action minus the inner boundary action for the primitive `λₓ(v) = ½ ω(x, v)`.
This identity does not require any regularity on the inner disc or a holomorphicity hypothesis.

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_annulus.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V) {u : ℂ → V} (z₀ : ℂ)
  {a b : ℝ} (ha : 0 < a) (hab : a ≤ b)
  (hu : ∀ z ∈ {z | a ≤ ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b}, ContDiffAt ℝ 2 u z) :
  ∫ (z : ℂ) in {z | a ≤ ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b},
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) 1) ((fderiv ℝ u z) Complex.I) =
    1 / 2 *
      ((∫ (θ : ℝ) in -Real.pi..Real.pi,
          (fun v w => (ω.toBilinForm v) w) (u (circleMap z₀ b θ))
            (deriv (fun θ => u (circleMap z₀ b θ)) θ)) -
        ∫ (θ : ℝ) in -Real.pi..Real.pi,
          (fun v w => (ω.toBilinForm v) w) (u (circleMap z₀ a θ))
            (deriv (fun θ => u (circleMap z₀ a θ)) θ))
```

## Depends on

- [TauCeti.pathIntegral](../differential-geometry-forms-de-rham-cohomology-f/part-01/tauceti-pathintegral.md)

## Proof depends on

- [Green's formula on a closed annulus](../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-01/greens-formula-on-a-closed-annulus.md)
- [Stokes' formula on the boundary of a cube for a closed two-form `ψ` that is C¹ on `(ℝ × ℝ) × ℝ`](../../../analysis/part-01/calculus/part-02/stokes-formula-on-the-boundary-of-a-cube-for-a-c.md)
- [Wirtinger's inequality](../../../analysis/part-02/fourier/wirtingers-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_annulus`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/Basic.html#TauCeti.SymplecticForm.integral_fderiv_apply_annulus).

## Other forms

**Stokes' formula for a homotopy of maps of a rectangle.** Formalized in Tau Ceti as [`TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.html#TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides).

```lean
TauCeti.rectangleIntegral_sub_rectangleIntegral_eq_sides.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [IsManifold I 2 M]
  {φ : TauCeti.RoughForm I M F 2} (hφ : TauCeti.IsSmoothForm I 1 φ) (hdφ : TauCeti.mextDeriv φ = 0)
  {Φ : (ℝ × ℝ) × ℝ → M} (hΦ : ContMDiff (modelWithCornersSelf ℝ ((ℝ × ℝ) × ℝ)) I 2 Φ)
  (a b : ℝ × ℝ) :
  TauCeti.rectangleIntegral φ (fun z => Φ (z, 1)) a b -
      TauCeti.rectangleIntegral φ (fun z => Φ (z, 0)) a b =
    TauCeti.rectangleIntegral φ (fun p => Φ ((a.1, p.1), p.2)) (a.2, 0) (b.2, 1) -
        TauCeti.rectangleIntegral φ (fun p => Φ ((b.1, p.1), p.2)) (a.2, 0) (b.2, 1) -
      (TauCeti.rectangleIntegral φ (fun p => Φ ((p.1, a.2), p.2)) (a.1, 0) (b.1, 1) -
        TauCeti.rectangleIntegral φ (fun p => Φ ((p.1, b.2), p.2)) (a.1, 0) (b.1, 1))
```

**Stokes' formula for symplectic area on a rectangle.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_prod_Icc`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/Basic.html#TauCeti.SymplecticForm.integral_fderiv_apply_prod_Icc).

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_prod_Icc.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V) {u : ℝ × ℝ → V}
  {a b : ℝ × ℝ} (hle : a ≤ b) (hu : ∀ z ∈ Set.Icc a b, ContDiffAt ℝ 2 u z) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b,
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) (1, 0)) ((fderiv ℝ u z) (0, 1)) =
    1 / 2 *
      (((∫ (t : ℝ) in a.2..b.2,
            (fun v w => (ω.toBilinForm v) w) (u (b.1, t)) ((fderiv ℝ u (b.1, t)) (0, 1))) -
          ∫ (t : ℝ) in a.2..b.2,
            (fun v w => (ω.toBilinForm v) w) (u (a.1, t)) ((fderiv ℝ u (a.1, t)) (0, 1))) -
        ((∫ (s : ℝ) in a.1..b.1,
            (fun v w => (ω.toBilinForm v) w) (u (s, b.2)) ((fderiv ℝ u (s, b.2)) (1, 0))) -
          ∫ (s : ℝ) in a.1..b.1,
            (fun v w => (ω.toBilinForm v) w) (u (s, a.2)) ((fderiv ℝ u (s, a.2)) (1, 0))))
```

**Stokes' formula for symplectic area on the truncated thrice-punctured sphere.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_truncation`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/ThricePuncturedSphere.html#TauCeti.SymplecticForm.integral_fderiv_apply_truncation).

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_truncation.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V) {u : ℂ → V}
  (hu : ContDiffOn ℝ 2 u {w | w ≠ 0 ∧ w ≠ 1}) {R : ℝ} (hR : 1 ≤ R) :
  ∫ (w : ℂ) in TauCeti.ThricePuncturedSphere.truncation R,
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u w) 1) ((fderiv ℝ u w) Complex.I) =
    ∑ q,
      q.endSign * ω.loopArea fun t => u (q.cylindricalEndLift (↑(q.endSign * R) + ↑t * Complex.I))
```

**Stokes' formula for the integral over a map of a rectangle.** Formalized in Tau Ceti as [`TauCeti.rectangleIntegral_mextDeriv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialForm/Integration/Homotopy.html#TauCeti.rectangleIntegral_mextDeriv).

```lean
TauCeti.rectangleIntegral_mextDeriv.{u_1, u_2, u_3, u_4} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} {F : Type u_4} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [IsManifold I 2 M] {α : TauCeti.RoughForm I M F 1}
  (hα : TauCeti.IsSmoothForm I 1 α) {u : ℝ × ℝ → M}
  (hu : ContMDiff (modelWithCornersSelf ℝ (ℝ × ℝ)) I 2 u) (a b : ℝ × ℝ) :
  TauCeti.rectangleIntegral (TauCeti.mextDeriv α) u a b =
    TauCeti.pathIntegral α (fun t => u (b.1, t)) a.2 b.2 -
        TauCeti.pathIntegral α (fun t => u (a.1, t)) a.2 b.2 -
      (TauCeti.pathIntegral α (fun s => u (s, b.2)) a.1 b.1 -
        TauCeti.pathIntegral α (fun s => u (s, a.2)) a.1 b.1)
```

**Stokes' formula on a finite-energy punctured disc.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_punctured_disc`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/PuncturedDisc.html#TauCeti.SymplecticForm.integral_fderiv_apply_punctured_disc).

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_punctured_disc.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V)
  {u : ℂ → V} (z₀ : ℂ) {b : ℝ} (hb : 0 < b)
  (hu : ∀ z ∈ {z | 0 < ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b}, ContDiffAt ℝ 2 u z)
  (henergy :
    MeasureTheory.IntegrableOn (fun z => ‖fderiv ℝ u z‖ ^ 2) {z | 0 < ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b}
      MeasureTheory.volume) :
  ∫ (z : ℂ) in {z | 0 < ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b},
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) 1) ((fderiv ℝ u z) Complex.I) =
    1 / 2 *
      ∫ (θ : ℝ) in -Real.pi..Real.pi,
        (fun v w => (ω.toBilinForm v) w) (u (circleMap z₀ b θ))
          (deriv (fun θ => u (circleMap z₀ b θ)) θ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.integral_fderiv_apply_annulus`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/Basic.html#TauCeti.SymplecticForm.integral_fderiv_apply_annulus)
- [Source of `TauCeti.SymplecticForm.integral_fderiv_apply_annulus` in TauCeti/Geometry/Symplectic/Area/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Area/Basic.lean#L213)
