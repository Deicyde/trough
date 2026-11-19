---
declaration: theorem
origin: cited
lean: TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral
statement: formalized
proof: formalized
---

# Arzelà–Ascoli for primitives

A family of primitives `T v = c + ∫_{t₀}^· d v ∂μ` on
`[a, b]`, based at a point `t₀` of `[a, b]`, whose integrands are dominated almost everywhere on
`(a, b)` by a fixed integrable function `B` has relatively compact range.

```lean
TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {a b : ℝ} {X : Type u_2} {μ : MeasureTheory.Measure ℝ}
  [MeasureTheory.NullSingletonClass μ] {t₀ : ℝ} {c : E} [ProperSpace E] {d : X → ℝ → E} {B : ℝ → ℝ}
  {T : X → C(↑(Set.Icc a b), E)} (ht₀ : t₀ ∈ Set.Icc a b)
  (hdi : ∀ (v : X), MeasureTheory.IntegrableOn (d v) (Set.Ioo a b) μ)
  (hBi : MeasureTheory.IntegrableOn B (Set.Ioo a b) μ)
  (hdB : ∀ (v : X), ∀ᵐ (t : ℝ) ∂μ.restrict (Set.Ioo a b), ‖d v t‖ ≤ B t)
  (hT : ∀ (v : X) (t : ↑(Set.Icc a b)), (T v) t = c + ∫ (s : ℝ) in t₀..↑t, d v s ∂μ) :
  IsCompact (closure (Set.range T))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Arzelà–Ascoli along exhausting bands](../../../../part-02/topology/other-results/arzela-ascoli-along-exhausting-bands.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/IntervalIntegral/Primitive.html#TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral).

## Sources

- [Tau Ceti documentation: `TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/IntervalIntegral/Primitive.html#TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral)
- [Source of `TauCeti.intervalIntegral.isCompact_closure_range_of_forall_eq_add_integral` in TauCeti/MeasureTheory/Integral/IntervalIntegral/Primitive.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Integral/IntervalIntegral/Primitive.lean#L203)
