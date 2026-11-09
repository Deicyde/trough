---
declaration: theorem
origin: cited
lean: TauCeti.circleLIntegral_sq_le
statement: formalized
proof: formalized
---

# Cauchy–Schwarz on a circle

The square of the circle integral of `g` is at most
`2 π ρ` — for `ρ > 0` the circumference of the circle — times the circle integral of `g ^ 2`.

Only the angular trace of `g` along the circle at hand need be measurable; nothing is assumed of
`g` off that circle. Both sides vanish for a nonpositive radius, so no positivity is assumed.

```lean
TauCeti.circleLIntegral_sq_le {g : ℂ → ENNReal} (ζ : ℂ) (ρ : ℝ)
  (hg :
    AEMeasurable (fun θ => g (circleMap ζ ρ θ))
      (MeasureTheory.volume.restrict (Set.Ioo (-Real.pi) Real.pi))) :
  TauCeti.circleLIntegral g ζ ρ ^ 2 ≤
    ENNReal.ofReal (2 * Real.pi * ρ) * TauCeti.circleLIntegral (fun z => g z ^ 2) ζ ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../function/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.circleLIntegral_sq_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.circleLIntegral_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.circleLIntegral_sq_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.circleLIntegral_sq_le)
- [Source of `TauCeti.circleLIntegral_sq_le` in TauCeti/MeasureTheory/Integral/Circle/LIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/Circle/LIntegral.lean#L305)
