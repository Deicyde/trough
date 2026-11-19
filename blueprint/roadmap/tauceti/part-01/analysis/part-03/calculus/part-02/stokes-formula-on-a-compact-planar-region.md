---
declaration: theorem
origin: cited
lean: TauCeti.integral_oneForm_of_isCompact, TauCeti.integral2_slice_sub_eq_sides, TauCeti.integral_oneForm_jordan
statement: formalized
proof: formalized
---

# Stokes' formula on a compact planar region

If a compact set with nonempty interior
has frontier equal to the trace of a simple closed absolutely continuous curve, a real one-form
that is `C¹` near the set integrates around the curve to its Jordan orientation sign times
the integral of its exterior derivative over the compact set. Both integrals exist.

```lean
TauCeti.integral_oneForm_of_isCompact {D : Set ℂ} (hD : IsCompact D) (hint : (interior D).Nonempty)
  {ω : ℂ → ℂ [⋀^Fin 1]→L[ℝ] ℝ} {γ : ℝ → ℂ} {a b : ℝ} {U : Set ℂ} (hab : a < b)
  (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b)) (htrace : γ '' Set.uIcc a b = frontier D) (hU : IsOpen U)
  (hregion : D ⊆ U) (hω : ContDiffOn ℝ 1 ω U) :
  IntervalIntegrable (fun t => (ω (γ t)) fun x => deriv γ t) MeasureTheory.volume a b ∧
    MeasureTheory.IntegrableOn (fun z => (extDeriv ω z) ![1, Complex.I]) D MeasureTheory.volume ∧
      (∫ (t : ℝ) in a..b, (ω (γ t)) fun x => deriv γ t) =
        ↑(TauCeti.Contour.jordanSign γ a b) * ∫ (z : ℂ) in D, (extDeriv ω z) ![1, Complex.I]
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Green's theorem for a simple closed absolutely continuous curve](../../../part-04/other-results/greens-theorem-for-a-simple-closed-absolutely-co.md)
- [The Jordan curve theorem](../../../part-01/conformal-mapping-and-the-geometric-theory-of-ho/the-jordan-curve-theorem.md)
- [The Jordan separation theorem](../../complex/part-02/the-jordan-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_oneForm_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes/Jordan.html#TauCeti.integral_oneForm_of_isCompact).

## Other forms

**Stokes' formula on the boundary of a cube for a closed two-form `ψ` that is C¹ on `(ℝ × ℝ) × ℝ`.** Formalized in Tau Ceti as [`TauCeti.integral2_slice_sub_eq_sides`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes.html#TauCeti.integral2_slice_sub_eq_sides).

```lean
TauCeti.integral2_slice_sub_eq_sides.{u_1} {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℝ F]
  {ψ : (ℝ × ℝ) × ℝ → ((ℝ × ℝ) × ℝ) [⋀^Fin 2]→L[ℝ] F} (hψ : ContDiff ℝ 1 ψ) (hdψ : extDeriv ψ = 0)
  (a b : ℝ × ℝ) :
  (∫ (s : ℝ) in a.1..b.1, ∫ (t : ℝ) in a.2..b.2, (ψ ((s, t), 1)) ![((1, 0), 0), ((0, 1), 0)]) -
      ∫ (s : ℝ) in a.1..b.1, ∫ (t : ℝ) in a.2..b.2, (ψ ((s, t), 0)) ![((1, 0), 0), ((0, 1), 0)] =
    ((∫ (t : ℝ) in a.2..b.2, ∫ (c : ℝ) in 0..1, (ψ ((a.1, t), c)) ![((0, 1), 0), (0, 1)]) -
        ∫ (t : ℝ) in a.2..b.2, ∫ (c : ℝ) in 0..1, (ψ ((b.1, t), c)) ![((0, 1), 0), (0, 1)]) -
      ((∫ (s : ℝ) in a.1..b.1, ∫ (c : ℝ) in 0..1, (ψ ((s, a.2), c)) ![((1, 0), 0), (0, 1)]) -
        ∫ (s : ℝ) in a.1..b.1, ∫ (c : ℝ) in 0..1, (ψ ((s, b.2), c)) ![((1, 0), 0), (0, 1)])
```

**Stokes' formula on the inside of a simple closed absolutely continuous curve.** Formalized in Tau Ceti as [`TauCeti.integral_oneForm_jordan`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes/Jordan.html#TauCeti.integral_oneForm_jordan).

```lean
TauCeti.integral_oneForm_jordan {ω : ℂ → ℂ [⋀^Fin 1]→L[ℝ] ℝ} {γ : ℝ → ℂ} {a b : ℝ} {U : Set ℂ}
  (hab : a < b) (hγ : AbsolutelyContinuousOnInterval γ a b) (hclosed : γ a = γ b)
  (hinj : Set.InjOn γ (Set.Ico a b)) (hU : IsOpen U)
  (hregion : TauCeti.filledHull (γ '' Set.uIcc a b) ⊆ U) (hω : ContDiffOn ℝ 1 ω U) :
  IntervalIntegrable (fun t => (ω (γ t)) fun x => deriv γ t) MeasureTheory.volume a b ∧
    MeasureTheory.IntegrableOn (fun z => (extDeriv ω z) ![1, Complex.I])
        (TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b) MeasureTheory.volume ∧
      (∫ (t : ℝ) in a..b, (ω (γ t)) fun x => deriv γ t) =
        ↑(TauCeti.Contour.jordanSign γ a b) *
          ∫ (z : ℂ) in TauCeti.filledHull (γ '' Set.uIcc a b) \ γ '' Set.uIcc a b,
            (extDeriv ω z) ![1, Complex.I]
```

## Sources

- [Tau Ceti documentation: `TauCeti.integral_oneForm_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/DifferentialForm/Stokes/Jordan.html#TauCeti.integral_oneForm_of_isCompact)
- [Source of `TauCeti.integral_oneForm_of_isCompact` in TauCeti/Analysis/Calculus/DifferentialForm/Stokes/Jordan.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/DifferentialForm/Stokes/Jordan.lean#L81)
