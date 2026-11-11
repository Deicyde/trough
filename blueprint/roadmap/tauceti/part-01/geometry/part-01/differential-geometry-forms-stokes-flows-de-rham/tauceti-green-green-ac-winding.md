---
declaration: theorem
origin: cited
lean: TauCeti.Green.green_ac_winding
statement: formalized
proof: formalized
---

# TauCeti.Green.green_ac_winding

Green's theorem for a closed absolutely continuous curve with index vanishing outside
the open field domain. The winding numbers may be unbounded and the curve may intersect itself.

```lean
TauCeti.Green.green_ac_winding {γ : ℝ → ℂ} {a b : ℝ} {U : Set ℂ} {P Q : ℂ → ℝ} (hab : a < b)
  (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b) (hU : IsOpen U)
  (htrace : γ '' Set.uIcc a b ⊆ U) (hP : ContDiffOn ℝ 1 P U) (hQ : ContDiffOn ℝ 1 Q U)
  (hindex : ∀ z ∉ U, TauCeti.Contour.windingNumber γ a b z = 0) :
  IntervalIntegrable (TauCeti.Green.circulationFun P Q γ) MeasureTheory.volume a b ∧
    MeasureTheory.IntegrableOn
        (fun z => TauCeti.Green.windingWeight γ a b z * TauCeti.Green.curl P Q z) U
        MeasureTheory.volume ∧
      ∫ (t : ℝ) in a..b, TauCeti.Green.circulationFun P Q γ t =
        ∫ (z : ℂ) in U, TauCeti.Green.windingWeight γ a b z * TauCeti.Green.curl P Q z
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../../analysis/part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [TauCeti.Green.green_ac_winding_sum](tauceti-green-green-ac-winding-sum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Green.green_ac_winding`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Winding.html#TauCeti.Green.green_ac_winding).

## Sources

- [Tau Ceti documentation: `TauCeti.Green.green_ac_winding`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/Winding.html#TauCeti.Green.green_ac_winding)
- [Source of `TauCeti.Green.green_ac_winding` in TauCeti/Analysis/Green/Winding.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Green/Winding.lean#L28)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
