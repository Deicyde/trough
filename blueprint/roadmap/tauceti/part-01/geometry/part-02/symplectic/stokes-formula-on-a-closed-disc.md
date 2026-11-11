---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.integral_fderiv_apply_closedBall, TauCeti.SymplecticForm.integral_fderiv_apply_prod_Icc, TauCeti.SymplecticForm.integral_fderiv_apply_annulus, TauCeti.SymplecticForm.integral_fderiv_apply_truncation, TauCeti.SymplecticForm.integral_fderiv_apply_preimage_closedBall, TauCeti.SymplecticForm.integral_fderiv_apply_punctured_disc, TauCeti.SymplecticForm.integral_symplecticForm_fderiv_closedBall_eq_neg_loopArea
statement: formalized
proof: formalized
---

# Stokes' formula on a closed disc

For a map which is `C²` at every point of the closed
disc `‖z - z₀‖ ≤ b`, the integral over the disc of the pullback of a constant symplectic form is
half the integral of `ω(u, ∂_θ u)` along the boundary circle.

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_closedBall.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V) {u : ℂ → V} (z₀ : ℂ)
  {b : ℝ} (hb : 0 < b) (hu : ∀ z ∈ Metric.closedBall z₀ b, ContDiffAt ℝ 2 u z) :
  ∫ (z : ℂ) in Metric.closedBall z₀ b,
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) 1) ((fderiv ℝ u z) Complex.I) =
    1 / 2 *
      ∫ (θ : ℝ) in -Real.pi..Real.pi,
        (fun v w => (ω.toBilinForm v) w) (u (circleMap z₀ b θ))
          (deriv (fun θ => u (circleMap z₀ b θ)) θ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Green's formula on a closed annulus](../../../measure-theory/integral/part-01/greens-formula-on-a-closed-annulus.md)
- [Wirtinger's inequality](../../../analysis/part-02/fourier/wirtingers-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_closedBall`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/PuncturedDisc.html#TauCeti.SymplecticForm.integral_fderiv_apply_closedBall).

## Other forms

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

**Stokes' formula for symplectic area on an annulus.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_annulus`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/Basic.html#TauCeti.SymplecticForm.integral_fderiv_apply_annulus).

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_annulus.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V) {u : ℂ → V} (z₀ : ℂ)
  {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b)
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

**Stokes' formula on a closed disc, in real coordinates.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_fderiv_apply_preimage_closedBall`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/PuncturedDisc.html#TauCeti.SymplecticForm.integral_fderiv_apply_preimage_closedBall).

```lean
TauCeti.SymplecticForm.integral_fderiv_apply_preimage_closedBall.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V] (ω : TauCeti.SymplecticForm V)
  {u : ℝ × ℝ → V} (z₀ : ℂ) {b : ℝ} (hb : 0 < b)
  (hu : ∀ z ∈ ⇑Complex.equivRealProdCLM.symm ⁻¹' Metric.closedBall z₀ b, ContDiffAt ℝ 2 u z) :
  ∫ (z : ℝ × ℝ) in ⇑Complex.equivRealProdCLM.symm ⁻¹' Metric.closedBall z₀ b,
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) TauCeti.stdComplexLineReal)
        ((fderiv ℝ u z) TauCeti.stdComplexLineImag) =
    1 / 2 *
      ∫ (θ : ℝ) in -Real.pi..Real.pi,
        (fun v w => (ω.toBilinForm v) w) (u (Complex.equivRealProdCLM (circleMap z₀ b θ)))
          (deriv (fun θ => u (Complex.equivRealProdCLM (circleMap z₀ b θ))) θ)
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

**Stokes' formula on the discs of the negative plane.** Formalized in Tau Ceti as [`TauCeti.SymplecticForm.integral_symplecticForm_fderiv_closedBall_eq_neg_loopArea`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/PlaneAction.html#TauCeti.SymplecticForm.integral_symplecticForm_fderiv_closedBall_eq_neg_loopArea).

```lean
TauCeti.SymplecticForm.integral_symplecticForm_fderiv_closedBall_eq_neg_loopArea.{u_1}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  (ω : TauCeti.SymplecticForm V) {u : ℝ × ℝ → V} (hu : ContDiff ℝ 2 u) (R : ℝ) :
  ∫ (z : ℝ × ℝ) in
      ⇑Complex.equivRealProdCLM.symm ⁻¹' Metric.closedBall 0 (2 * Real.exp (2 * Real.pi * R)),
      (fun v w => (ω.toBilinForm v) w) ((fderiv ℝ u z) TauCeti.stdComplexLineReal)
        ((fderiv ℝ u z) TauCeti.stdComplexLineImag) =
    -ω.loopArea fun t =>
        u
          (Complex.equivRealProdCLM
            (TauCeti.ThricePuncturedSphere.Puncture.inf.cylindricalEndLift (-↑R + ↑t * Complex.I)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.integral_fderiv_apply_closedBall`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Area/PuncturedDisc.html#TauCeti.SymplecticForm.integral_fderiv_apply_closedBall)
- [Source of `TauCeti.SymplecticForm.integral_fderiv_apply_closedBall` in TauCeti/Geometry/Symplectic/Area/PuncturedDisc.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Area/PuncturedDisc.lean#L172)
