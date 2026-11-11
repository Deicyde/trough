---
declaration: theorem
origin: cited
lean: TauCeti.periodic_of_forall_eq_integral_sub
statement: formalized
proof: formalized
---

# Choquet–Deny lemma

Let `μ` be a probability measure on a seminormed additive group. A
bounded, uniformly continuous function `h : E → ℝ` with `h x = ∫ t, h (x - t) ∂μ` for every `x`
is periodic with period `s` for every point `s` of the support of `μ`.

```lean
TauCeti.periodic_of_forall_eq_integral_sub.{u_1} {E : Type u_1} [SeminormedAddCommGroup E]
  [MeasurableSpace E] [OpensMeasurableSpace E] {μ : MeasureTheory.Measure E}
  [MeasureTheory.IsProbabilityMeasure μ] {h : E → ℝ} {C : ℝ} (hC : ∀ (x : E), |h x| ≤ C)
  (hu : UniformContinuous h) (hh : ∀ (x : E), h x = ∫ (t : E), h (x - t) ∂μ) {s : E}
  (hs : s ∈ μ.support) : Function.Periodic h s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.periodic_of_forall_eq_integral_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/ChoquetDeny.html#TauCeti.periodic_of_forall_eq_integral_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.periodic_of_forall_eq_integral_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/ChoquetDeny.html#TauCeti.periodic_of_forall_eq_integral_sub)
- [Source of `TauCeti.periodic_of_forall_eq_integral_sub` in TauCeti/MeasureTheory/Group/ChoquetDeny.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Group/ChoquetDeny.lean#L127)
