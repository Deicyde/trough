---
declaration: theorem
origin: cited
lean: TauCeti.Green.green_ac_jordan
statement: formalized
proof: formalized
---

# Green's theorem for a simple closed absolutely continuous curve

with no supplied index
hypothesis, both the boundary circulation and the interior curl are integrable and the circulation
equals `Contour.jordanSign γ a b ∈ {1, -1}` times the integral of `curl P Q` over the bounded inside
`filledHull (γ '' uIcc a b) \ (γ '' uIcc a b)`.

```lean
TauCeti.Green.green_ac_jordan {γ : ℝ → ℂ} {a b : ℝ} {U : Set ℂ} {P Q : ℂ → ℝ} (hab : a < b)
  (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b)) (hU : IsOpen U)
  (hregion : TauCeti.filledHull (γ '' Set.uIcc a b) ⊆ U) (hP : ContDiffOn ℝ 1 P U)
  (hQ : ContDiffOn ℝ 1 Q U) :
  IntervalIntegrable (TauCeti.Green.circulationFun P Q γ) MeasureTheory.volume a b ∧
    MeasureTheory.IntegrableOn (TauCeti.Green.curl P Q)
        (TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b) MeasureTheory.volume ∧
      ∫ (t : ℝ) in a..b, TauCeti.Green.circulationFun P Q γ t =
        ↑(TauCeti.Contour.jordanSign γ a b) *
          ∫ (z : ℂ) in TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b,
            TauCeti.Green.curl P Q z
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Jordan index theorem (orientation sign dichotomy)](../../part-02/contour/jordan-index-theorem-orientation-sign-dichotomy.md)
- [TauCeti.Green.green_ac_winding](../../../geometry/part-01/differential-geometry-forms-stokes-flows-de-rham/tauceti-green-green-ac-winding.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Green.green_ac_jordan`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Jordan.html#TauCeti.Green.green_ac_jordan).

## Sources

- [Tau Ceti documentation: `TauCeti.Green.green_ac_jordan`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Jordan.html#TauCeti.Green.green_ac_jordan)
- [Source of `TauCeti.Green.green_ac_jordan` in TauCeti/Analysis/Green/Jordan.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Green/Jordan.lean#L54)
