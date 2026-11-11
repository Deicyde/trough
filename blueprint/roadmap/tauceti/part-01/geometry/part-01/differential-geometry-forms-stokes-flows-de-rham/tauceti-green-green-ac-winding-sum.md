---
declaration: theorem
origin: cited
lean: TauCeti.Green.green_ac_winding_sum
statement: formalized
proof: formalized
---

# TauCeti.Green.green_ac_winding_sum

Green's theorem for a finite integer-weighted family of closed AC curves.
The domain condition concerns the total index, permitting cancellation between curves.

```lean
TauCeti.Green.green_ac_winding_sum.{u_1} {ι : Type u_1} {s : Finset ι} {γ : ι → ℝ → ℂ} {a b : ι → ℝ}
  {w : ι → ℤ} {U : Set ℂ} {P Q : ℂ → ℝ} (hab : ∀ i ∈ s, a i < b i)
  (hγ : ∀ i ∈ s, AbsolutelyContinuousOnInterval (γ i) (a i) (b i))
  (hclosed : ∀ i ∈ s, γ i (a i) = γ i (b i)) (hU : IsOpen U)
  (htrace : ∀ i ∈ s, γ i '' Set.uIcc (a i) (b i) ⊆ U) (hP : ContDiffOn ℝ 1 P U)
  (hQ : ContDiffOn ℝ 1 Q U)
  (hindex : ∀ z ∉ U, ∑ i ∈ s, ↑(w i) * TauCeti.Contour.windingNumber (γ i) (a i) (b i) z = 0) :
  (∀ i ∈ s,
      IntervalIntegrable (TauCeti.Green.circulationFun P Q (γ i)) MeasureTheory.volume (a i)
        (b i)) ∧
    MeasureTheory.IntegrableOn
        (fun z =>
          (∑ i ∈ s, ↑(w i) * TauCeti.Green.windingWeight (γ i) (a i) (b i) z) *
            TauCeti.Green.curl P Q z)
        U MeasureTheory.volume ∧
      ∑ i ∈ s, ↑(w i) * ∫ (t : ℝ) in a i..b i, TauCeti.Green.circulationFun P Q (γ i) t =
        ∫ (z : ℂ) in U,
          (∑ i ∈ s, ↑(w i) * TauCeti.Green.windingWeight (γ i) (a i) (b i) z) *
            TauCeti.Green.curl P Q z
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../../analysis/part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Fundamental theorem for absolutely continuous curves, integrability](../../../measure-theory/function/part-01/fundamental-theorem-for-absolutely-continuous-cu.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Green.green_ac_winding_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/FiniteSum.html#TauCeti.Green.green_ac_winding_sum).

## Sources

- [Tau Ceti documentation: `TauCeti.Green.green_ac_winding_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/Green/FiniteSum.html#TauCeti.Green.green_ac_winding_sum)
- [Source of `TauCeti.Green.green_ac_winding_sum` in TauCeti/Analysis/Green/FiniteSum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Green/FiniteSum.lean#L100)
- [Tau Ceti roadmap status: Differential geometry — forms, Stokes, flows, de Rham cohomology, degree, planar Green and Riemannian calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DifferentialGeometry/STATUS.md)
