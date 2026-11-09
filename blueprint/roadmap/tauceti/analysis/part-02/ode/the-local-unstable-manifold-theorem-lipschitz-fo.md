---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image
statement: formalized
proof: formalized
---

# The local unstable-manifold theorem, Lipschitz form

Near a hyperbolic equilibrium the
initial values of backward solutions confined to a fixed small ball, truncated by the norm of
their `1 - P` component, form a graph over a ball in `range (1 - P)`.

```lean
ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X] {K α ε : NNReal}
  {A P : X →L[ℝ] X} {N : X → X} {r : ℝ}
  (hs :
    ∀ (t : ℝ), 0 ≤ t → ∀ (v : X), ‖(NormedSpace.exp (t • A)) (P v)‖ ≤ ↑K * Real.exp (-↑α * t) * ‖v‖)
  (hu : ∀ t ≤ 0, ∀ (v : X), ‖(NormedSpace.exp (t • A)) (v - P v)‖ ≤ ↑K * Real.exp (↑α * t) * ‖v‖)
  (hN : LipschitzOnWith ε N (Metric.closedBall 0 r)) (hsmall : 2 * K * (ε * 2) < α) (hN0 : N 0 = 0)
  (hP : IsIdempotentElem P) (hAP : Commute A P) (hr0 : 0 < r) :
  ∃ ρ > 0,
    {x |
        (∃ y,
            IsIntegralCurveOn y (fun x z => A z + N z) (Set.Iic 0) ∧
              y 0 = x ∧ Set.MapsTo y (Set.Iic 0) (Metric.closedBall 0 r)) ∧
          ‖(ContinuousLinearMap.id ℝ X - P) x‖ ≤ ρ} =
      (fun v => v + A.localUnstableGraphMap P N r hs hu ⋯ hN hsmall v) ''
        (Set.range ⇑(ContinuousLinearMap.id ℝ X - P) ∩ Metric.closedBall 0 ρ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/LyapunovPerron/Local.html#ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/LyapunovPerron/Local.html#ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image)
- [Source of `ContinuousLinearMap.exists_setOf_exists_isIntegralCurveOn_Iic_mapsTo_closedBall_eq_image` in TauCeti/Analysis/ODE/LyapunovPerron/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/ODE/LyapunovPerron/Local.lean#L554)
