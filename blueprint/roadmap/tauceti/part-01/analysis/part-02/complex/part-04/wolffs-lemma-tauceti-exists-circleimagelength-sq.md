---
declaration: theorem
origin: cited
lean: TauCeti.exists_circleImageLength_sq_lt, TauCeti.exists_circleImageLength_sq_lt_of_volume_image
statement: formalized
proof: formalized
---

# Wolff's lemma (`TauCeti.exists_circleImageLength_sq_lt`)

If `2 π` times the Dirichlet integral of `f` over `s` is smaller than
`c * log (R / r)`, then some circle of radius `ρ` between `r` and `R` has `ℓ ρ ^ 2 < c`.

Since `log (R / r)` grows without bound as the annulus is made longer while the Dirichlet integral
stays fixed, this makes `ℓ` arbitrarily small at arbitrarily small radii; for a holomorphic `f`
that is the geometric statement that a map of finite Dirichlet integral cannot keep every circular
arc about `ζ` long.

```lean
TauCeti.exists_circleImageLength_sq_lt {s : Set ℂ} (f : ℂ → ℂ) (ζ : ℂ) {r R : ℝ} (hr : 0 < r)
  (hrR : r < R) {c : ENNReal}
  (hc :
    ENNReal.ofReal (2 * Real.pi) * ∫⁻ (z : ℂ) in s, ‖deriv f z‖ₑ ^ 2 <
      c * ENNReal.ofReal (Real.log (R / r))) :
  ∃ ρ ∈ Set.Ioo r R, TauCeti.circleImageLength f s ζ ρ ^ 2 < c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wolff's lemma (`TauCeti.exists_circleLIntegral_sq_lt`)](../../../../measure-theory/integral/part-02/wolffs-lemma-tauceti-exists-circlelintegral-sq-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_circleImageLength_sq_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/LengthArea.html#TauCeti.exists_circleImageLength_sq_lt).

## Other forms

**Wolff's lemma, area form.** Formalized in Tau Ceti as [`TauCeti.exists_circleImageLength_sq_lt_of_volume_image`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/LengthArea.html#TauCeti.exists_circleImageLength_sq_lt_of_volume_image).

```lean
TauCeti.exists_circleImageLength_sq_lt_of_volume_image {s : Set ℂ} {f : ℂ → ℂ}
  (hf : ∀ z ∈ s, DifferentiableAt ℂ f z)
  (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume) (hinj : Set.InjOn f s) (ζ : ℂ)
  {r R : ℝ} (hr : 0 < r) (hrR : r < R) {c : ENNReal}
  (hc :
    ENNReal.ofReal (2 * Real.pi) * MeasureTheory.volume (f '' s) <
      c * ENNReal.ofReal (Real.log (R / r))) :
  ∃ ρ ∈ Set.Ioo r R, TauCeti.circleImageLength f s ζ ρ ^ 2 < c
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_circleImageLength_sq_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/LengthArea.html#TauCeti.exists_circleImageLength_sq_lt)
- [Source of `TauCeti.exists_circleImageLength_sq_lt` in TauCeti/Analysis/Complex/Conformal/LengthArea.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/LengthArea.lean#L220)
