---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus, ContinuousLinearMap.integral_bilinear_fderiv_sub_prod_Icc
statement: formalized
proof: formalized
---

# Green's formula on a closed annulus

For a `C²` map near the annulus of radii
`0 ≤ a ≤ b`, the integral of the alternating part of a bilinear pairing of its derivatives equals
the outer circle integral of `B u du` minus the inner circle integral. Both circles are
parametrized counterclockwise; their difference gives the boundary orientation.

```lean
ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus.{u_2, u_3} {V : Type u_2} {W : Type u_3}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [NormedAddCommGroup W] [NormedSpace ℝ W]
  (B : V →L[ℝ] V →L[ℝ] W) {u : ℂ → V} (z₀ : ℂ) {a b : ℝ} (ha : 0 ≤ a) (hab : a ≤ b)
  (hu : ∀ z ∈ {z | a ≤ ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b}, ContDiffAt ℝ 2 u z) :
  ∫ (z : ℂ) in {z | a ≤ ‖z - z₀‖ ∧ ‖z - z₀‖ ≤ b},
      (B ((fderiv ℝ u z) 1)) ((fderiv ℝ u z) Complex.I) -
        (B ((fderiv ℝ u z) Complex.I)) ((fderiv ℝ u z) 1) =
    (∫ (θ : ℝ) in -Real.pi..Real.pi,
        (B (u (circleMap z₀ b θ)))
          ((fderiv ℝ u (circleMap z₀ b θ)) (circleMap 0 b θ * Complex.I))) -
      ∫ (θ : ℝ) in -Real.pi..Real.pi,
        (B (u (circleMap z₀ a θ))) ((fderiv ℝ u (circleMap z₀ a θ)) (circleMap 0 a θ * Complex.I))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem.html#ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus).

## Other forms

**Green's formula for a bilinear pairing of partial derivatives.** Formalized in Tau Ceti as [`ContinuousLinearMap.integral_bilinear_fderiv_sub_prod_Icc`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem.html#ContinuousLinearMap.integral_bilinear_fderiv_sub_prod_Icc).

```lean
ContinuousLinearMap.integral_bilinear_fderiv_sub_prod_Icc.{u_2, u_3} {V : Type u_2} {W : Type u_3}
  [NormedAddCommGroup V] [NormedSpace ℝ V] [NormedAddCommGroup W] [NormedSpace ℝ W]
  (B : V →L[ℝ] V →L[ℝ] W) {u : ℝ × ℝ → V} {a b : ℝ × ℝ} (hle : a ≤ b)
  (hu : ∀ z ∈ Set.Icc a b, ContDiffAt ℝ 2 u z) :
  ∫ (z : ℝ × ℝ) in Set.Icc a b,
      (B ((fderiv ℝ u z) (1, 0))) ((fderiv ℝ u z) (0, 1)) -
        (B ((fderiv ℝ u z) (0, 1))) ((fderiv ℝ u z) (1, 0)) =
    ((∫ (t : ℝ) in a.2..b.2, (B (u (b.1, t))) ((fderiv ℝ u (b.1, t)) (0, 1))) -
        ∫ (t : ℝ) in a.2..b.2, (B (u (a.1, t))) ((fderiv ℝ u (a.1, t)) (0, 1))) -
      ((∫ (s : ℝ) in a.1..b.1, (B (u (s, b.2))) ((fderiv ℝ u (s, b.2)) (1, 0))) -
        ∫ (s : ℝ) in a.1..b.1, (B (u (s, a.2))) ((fderiv ℝ u (s, a.2)) (1, 0)))
```

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem.html#ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus)
- [Source of `ContinuousLinearMap.integral_bilinear_fderiv_sub_annulus` in TauCeti/MeasureTheory/Integral/DivergenceTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/DivergenceTheorem.lean#L103)
