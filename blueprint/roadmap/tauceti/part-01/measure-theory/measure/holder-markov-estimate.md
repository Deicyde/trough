---
declaration: theorem
origin: cited
lean: TauCeti.measure_continuity_modulus_le_lintegral_curveAction
statement: formalized
proof: formalized
---

# Hölder–Markov estimate

Let `P` be a measure on `C([a, b], X)` concentrated on curves
absolutely continuous on `[a, b]`, and `1 ≤ p`. For `η > 0` and every `δ`, the curves with two
times closer than `δ` at which their values are at least `η` apart have `P`-measure at most
`δ ^ (p - 1) * (∫ A_p dP) / η ^ p`, where `A_p` is the `p`-action over `[a, b]`.

```lean
TauCeti.measure_continuity_modulus_le_lintegral_curveAction.{u_1} {X : Type u_1}
  [PseudoMetricSpace X] {a b p : ℝ} (hab : a ≤ b) {P : MeasureTheory.Measure C(↑(Set.Icc a b), X)}
  (hp : 1 ≤ p)
  (hAC :
    ∀ᵐ (γ : C(↑(Set.Icc a b), X)) ∂P, AbsolutelyContinuousOnInterval (Set.IccExtend hab ⇑γ) a b)
  {η : ℝ} (hη : 0 < η) (δ : ℝ) :
  P {γ | ∃ s t, dist s t < δ ∧ η ≤ dist (γ s) (γ t)} ≤
    (ENNReal.ofReal δ ^ (p - 1) *
        ∫⁻ (γ : C(↑(Set.Icc a b), X)), TauCeti.curveAction p (Set.IccExtend hab ⇑γ) a b ∂P) /
      ENNReal.ofReal η ^ p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder estimate along a curve](../function/part-01/holder-estimate-along-a-curve.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measure_continuity_modulus_le_lintegral_curveAction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Tight/CurveAction.html#TauCeti.measure_continuity_modulus_le_lintegral_curveAction).

## Sources

- [Tau Ceti documentation: `TauCeti.measure_continuity_modulus_le_lintegral_curveAction`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Tight/CurveAction.html#TauCeti.measure_continuity_modulus_le_lintegral_curveAction)
- [Source of `TauCeti.measure_continuity_modulus_le_lintegral_curveAction` in TauCeti/MeasureTheory/Measure/Tight/CurveAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Tight/CurveAction.lean#L85)
