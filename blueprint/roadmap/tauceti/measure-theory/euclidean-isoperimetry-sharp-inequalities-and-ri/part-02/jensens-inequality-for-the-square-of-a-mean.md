---
declaration: theorem
origin: cited
lean: TauCeti.sq_setAverage_norm_le_setAverage_norm_sq, TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le
statement: formalized
proof: formalized
---

# Jensen's inequality for the square of a mean

On a set `s` of finite nonzero measure, the
square of the mean of `‖g‖` is at most the mean of `‖g‖²`.

```lean
TauCeti.sq_setAverage_norm_le_setAverage_norm_sq.{u_1, u_2} {X : Type u_1} {F : Type u_2}
  [MeasurableSpace X] {μ : MeasureTheory.Measure X} [NormedAddCommGroup F] {g : X → F} {s : Set X}
  (hs0 : μ s ≠ 0) (hs : μ s ≠ ⊤) (hg : MeasureTheory.IntegrableOn g s μ)
  (hg2 : MeasureTheory.IntegrableOn (fun x => ‖g x‖ ^ 2) s μ) :
  (⨍ (x : X) in s, ‖g x‖ ∂μ) ^ 2 ≤ ⨍ (x : X) in s, ‖g x‖ ^ 2 ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_setAverage_norm_le_setAverage_norm_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.sq_setAverage_norm_le_setAverage_norm_sq).

## Other forms

**Jensen's inequality for the conditional expectation, as an inequality of `lintegral`s.** Formalized in Tau Ceti as [`TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/ConditionalExpectation.html#TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le).

```lean
TauCeti.MeasureTheory.lintegral_enorm_condExp_rpow_le.{u_1, u_2} {Ω : Type u_1} {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {m m₀ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} {f : Ω → E} (hf : MeasureTheory.AEStronglyMeasurable f μ) {p : ℝ}
  (hp : 1 ≤ p) : ∫⁻ (ω : Ω), ‖μ[f | m] ω‖ₑ ^ p ∂μ ≤ ∫⁻ (ω : Ω), ‖f ω‖ₑ ^ p ∂μ
```

## Sources

- [Tau Ceti documentation: `TauCeti.sq_setAverage_norm_le_setAverage_norm_sq`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Average.html#TauCeti.sq_setAverage_norm_le_setAverage_norm_sq)
- [Source of `TauCeti.sq_setAverage_norm_le_setAverage_norm_sq` in TauCeti/MeasureTheory/Integral/Average.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/Average.lean#L342)
