---
declaration: theorem
origin: cited
lean: TauCeti.setIntegral_setOf_inner_lt_trace_fderiv, TauCeti.setIntegral_setOf_inner_lt_fderiv_apply
statement: formalized
proof: formalized
---

# The divergence theorem on a half-space (`TauCeti.setIntegral_setOf_inner_lt_trace_fderiv`)

For a unit vector `ν` and a compactly supported
`C¹` vector field `φ`, the integral of the divergence `tr (Dφ)` over the half-space
`{x | ⟪x, ν⟫ < c}` is the flux `∫ ⟪φ, ν⟫` of `φ` through the boundary hyperplane
`{x | ⟪x, ν⟫ = c}` against `(n - 1)`-dimensional Hausdorff measure.

```lean
TauCeti.setIntegral_setOf_inner_lt_trace_fderiv.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {ν : F} [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F]
  (hν : ‖ν‖ = 1) (c : ℝ) {φ : F → F} (hφ : ContDiff ℝ 1 φ) (hφc : HasCompactSupport φ) :
  ∫ (x : F) in {x | inner ℝ x ν < c}, (LinearMap.trace ℝ F) ↑(fderiv ℝ φ x) =
    ∫ (x : F) in {x | inner ℝ x ν = c},
      inner ℝ (φ x) ν ∂MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ F - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The divergence theorem on a half-space (`TauCeti.setIntegral_normalHalfSpace_fderiv_apply`)](../../../analysis/part-03/sobolev/part-01/the-divergence-theorem-on-a-half-space-tauceti-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.setIntegral_setOf_inner_lt_trace_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/InnerHalfSpace.html#TauCeti.setIntegral_setOf_inner_lt_trace_fderiv).

## Other forms

**The divergence theorem on a half-space, directional form.** Formalized in Tau Ceti as [`TauCeti.setIntegral_setOf_inner_lt_fderiv_apply`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/InnerHalfSpace.html#TauCeti.setIntegral_setOf_inner_lt_fderiv_apply).

```lean
TauCeti.setIntegral_setOf_inner_lt_fderiv_apply.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {ν : F} [FiniteDimensional ℝ F] [MeasurableSpace F] [BorelSpace F]
  (hν : ‖ν‖ = 1) (c : ℝ) {g : F → ℝ} (hg : ContDiff ℝ 1 g) (hgc : HasCompactSupport g) (v : F) :
  ∫ (x : F) in {x | inner ℝ x ν < c}, (fderiv ℝ g x) v =
    inner ℝ v ν *
      ∫ (x : F) in {x | inner ℝ x ν = c},
        g x ∂MeasureTheory.Measure.euclideanHausdorffMeasure (Module.finrank ℝ F - 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.setIntegral_setOf_inner_lt_trace_fderiv`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/DivergenceTheorem/InnerHalfSpace.html#TauCeti.setIntegral_setOf_inner_lt_trace_fderiv)
- [Source of `TauCeti.setIntegral_setOf_inner_lt_trace_fderiv` in TauCeti/MeasureTheory/Integral/DivergenceTheorem/InnerHalfSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/DivergenceTheorem/InnerHalfSpace.lean#L100)
