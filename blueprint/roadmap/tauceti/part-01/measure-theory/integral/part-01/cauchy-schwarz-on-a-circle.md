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

No measurability of `g` is assumed, since Hölder's inequality for lower integrals needs none. Both
sides vanish for a nonpositive radius, so no positivity is assumed.

```lean
TauCeti.circleLIntegral_sq_le {g : ℂ → ENNReal} (ζ : ℂ) (ρ : ℝ) :
  TauCeti.circleLIntegral g ζ ρ ^ 2 ≤
    ENNReal.ofReal (2 * Real.pi * ρ) * TauCeti.circleLIntegral (fun z => g z ^ 2) ζ ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for the integral of a product](../../function/part-01/holders-inequality-for-the-integral-of-a-product.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.circleLIntegral_sq_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.circleLIntegral_sq_le).

## Sources

- [Tau Ceti documentation: `TauCeti.circleLIntegral_sq_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Circle/LIntegral.html#TauCeti.circleLIntegral_sq_le)
- [Source of `TauCeti.circleLIntegral_sq_le` in TauCeti/MeasureTheory/Integral/Circle/LIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Circle/LIntegral.lean#L305)
