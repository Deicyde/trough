---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour, TauCeti.LSeries.circleIntegral_intervalIntegral_mul_kernel
statement: formalized
proof: formalized
---

# Cauchy's formula for Newman's contour

Let `g` be holomorphic on an open convex set `U`
containing the right semicircle of radius `R > 0` and the detour `newmanDetour R δ` with
`δ > 0`. Then the integral of `g z / z` over the right semicircle, counterclockwise from
`-R * I` to `R * I`, plus its integral over the detour, back from `R * I` to `-R * I` through the
left half-plane, is `2πi g 0`. Both integrals include the velocity of their parametrization.

```lean
TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour {R δ : ℝ} {U : Set ℂ}
  {g : ℂ → ℂ} (hR : 0 < R) (hδ : 0 < δ) (hU : IsOpen U) (hconv : Convex ℝ U)
  (hg : DifferentiableOn ℂ g U)
  (hcirc : ∀ θ ∈ Set.Icc (-Real.pi / 2) (Real.pi / 2), circleMap 0 R θ ∈ U)
  (hdet : ∀ s ∈ Set.Icc (-1) 1, TauCeti.LSeries.newmanDetour R δ s ∈ U) :
  (∫ (θ : ℝ) in -Real.pi / 2..Real.pi / 2,
        circleMap 0 R θ * Complex.I * (g (circleMap 0 R θ) / circleMap 0 R θ)) +
      ∫ (s : ℝ) in -1..1,
        deriv (TauCeti.LSeries.newmanDetour R δ) s *
          (g (TauCeti.LSeries.newmanDetour R δ s) / TauCeti.LSeries.newmanDetour R δ s) =
    2 * ↑Real.pi * Complex.I * g 0
```

## Depends on

- [Newman's left detour](newmans-left-detour.md)

## Proof depends on

- [Holomorphic functions have primitives on a star-shaped set](holomorphic-functions-have-primitives-on-a-star.md)
- [Truncated Laplace transforms are entire](truncated-laplace-transforms-are-entire.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour).

## Other forms

**Cauchy's formula for a truncated transform.** Formalized in Tau Ceti as [`TauCeti.LSeries.circleIntegral_intervalIntegral_mul_kernel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Transform.html#TauCeti.LSeries.circleIntegral_intervalIntegral_mul_kernel).

```lean
TauCeti.LSeries.circleIntegral_intervalIntegral_mul_kernel {f : ℝ → ℂ} {T R : ℝ} (hR : 0 < R) :
  ∮ (z : ℂ) in C(0, R),
      (∫ (t : ℝ) in 0..T, f t * Complex.exp (-z * ↑t)) * Complex.exp (↑T * z) *
          (1 + z ^ 2 / ↑R ^ 2) /
        z =
    2 * ↑Real.pi * Complex.I * ∫ (t : ℝ) in 0..T, f t
```

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour)
- [Source of `TauCeti.LSeries.integral_right_semicircle_add_integral_newmanDetour` in TauCeti/NumberTheory/LSeries/Newman/Detour.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/Newman/Detour.lean#L253)
