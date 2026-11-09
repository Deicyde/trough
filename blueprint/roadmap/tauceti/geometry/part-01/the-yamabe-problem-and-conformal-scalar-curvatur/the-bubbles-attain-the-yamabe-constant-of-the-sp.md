---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant
statement: formalized
proof: formalized
---

# The bubbles attain the Yamabe constant of the sphere

in dimension `n > 2`, for Lebesgue
measure, `aₙ ∫ ‖dU_{t,b}‖² = Y(Sⁿ) (∫ U_{t,b} ^ pₙ) ^ (2 / pₙ)`. This is the equality case of the
sharp Euclidean Sobolev inequality.

```lean
TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] (hn : 2 < Module.finrank ℝ E) {t : ℝ} (ht : 0 < t) (b : E) :
  TauCeti.Yamabe.conformalCoefficient (Module.finrank ℝ E) *
      ∫ (x : E), ‖fderiv ℝ (TauCeti.Yamabe.bubble t b) x‖ ^ 2 =
    TauCeti.Yamabe.sphereYamabeConstant (Module.finrank ℝ E) *
      (∫ (x : E),
          TauCeti.Yamabe.bubble t b x ^ TauCeti.Yamabe.criticalExponent (Module.finrank ℝ E)) ^
        (2 / TauCeti.Yamabe.criticalExponent (Module.finrank ℝ E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The area of the unit round sphere](the-area-of-the-unit-round-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/Bubble/SobolevQuotient.html#TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/Bubble/SobolevQuotient.html#TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant)
- [Source of `TauCeti.Yamabe.conformalCoefficient_mul_integral_norm_fderiv_bubble_sq_eq_sphereYamabeConstant` in TauCeti/Analysis/PDE/Yamabe/Bubble/SobolevQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Yamabe/Bubble/SobolevQuotient.lean#L84)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)
