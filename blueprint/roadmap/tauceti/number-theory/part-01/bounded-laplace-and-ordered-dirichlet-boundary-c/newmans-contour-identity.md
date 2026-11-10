---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel
statement: formalized
proof: formalized
---

# Newman's contour identity

Let `G` be holomorphic on an open convex set `U` containing
the right semicircle of radius `R > 0` and the detour `newmanDetour R δ` with `δ > 0`, and let
`G_T z = ∫ t in 0..T, f t * exp (-z t)`. Against Newman's kernel
`k_T z = exp (T z) (1 + z² / R²) / z`, the right semicircle integral of `(G - G_T) k_T`
(counterclockwise from `-R * I` to `R * I`) plus the detour integral of `G k_T` (from `R * I`
back to `-R * I`) equals `2πi (G 0 - ∫ t in 0..T, f t)` plus the left semicircle integral of
`G_T k_T` (counterclockwise from `R * I` to `-R * I`). All integrals include the velocity of
their parametrization.

```lean
TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel {f : ℝ → ℂ}
  {G : ℂ → ℂ} {T R δ : ℝ} {U : Set ℂ} (hf : IntervalIntegrable f MeasureTheory.volume 0 T)
  (hR : 0 < R) (hδ : 0 < δ) (hU : IsOpen U) (hconv : Convex ℝ U) (hG : DifferentiableOn ℂ G U)
  (hcirc : ∀ θ ∈ Set.Icc (-Real.pi / 2) (Real.pi / 2), circleMap 0 R θ ∈ U)
  (hdet : ∀ s ∈ Set.Icc (-1) 1, TauCeti.LSeries.newmanDetour R δ s ∈ U) :
  (∫ (θ : ℝ) in -Real.pi / 2..Real.pi / 2,
        circleMap 0 R θ * Complex.I *
          ((G (circleMap 0 R θ) - ∫ (t : ℝ) in 0..T, f t * Complex.exp (-circleMap 0 R θ * ↑t)) *
                Complex.exp (↑T * circleMap 0 R θ) *
              (1 + circleMap 0 R θ ^ 2 / ↑R ^ 2) /
            circleMap 0 R θ)) +
      ∫ (s : ℝ) in -1..1,
        deriv (TauCeti.LSeries.newmanDetour R δ) s *
          (G (TauCeti.LSeries.newmanDetour R δ s) *
                Complex.exp (↑T * TauCeti.LSeries.newmanDetour R δ s) *
              (1 + TauCeti.LSeries.newmanDetour R δ s ^ 2 / ↑R ^ 2) /
            TauCeti.LSeries.newmanDetour R δ s) =
    2 * ↑Real.pi * Complex.I * (G 0 - ∫ (t : ℝ) in 0..T, f t) +
      ∫ (θ : ℝ) in Real.pi / 2..3 * Real.pi / 2,
        circleMap 0 R θ * Complex.I *
          ((∫ (t : ℝ) in 0..T, f t * Complex.exp (-circleMap 0 R θ * ↑t)) *
                Complex.exp (↑T * circleMap 0 R θ) *
              (1 + circleMap 0 R θ ^ 2 / ↑R ^ 2) /
            circleMap 0 R θ)
```

## Depends on

- [Newman's left detour](newmans-left-detour.md)

## Proof depends on

- [Cauchy's formula for Newman's contour](cauchys-formula-for-newmans-contour.md)
- [Holomorphic functions have primitives on a star-shaped set](holomorphic-functions-have-primitives-on-a-star.md)
- [Truncated Laplace transforms are entire](truncated-laplace-transforms-are-entire.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Tauberian.html#TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel)
- [Source of `TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour_mul_kernel` in TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Newman/Tauberian.lean#L77)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
