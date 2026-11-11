---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub, MeasureTheory.Measure.eq_smul_volume_of_conv_eq_self
statement: formalized
proof: formalized
---

# Choquet–Deny theorem, harmonic functions

Let `ν` be a probability measure on a
seminormed additive group whose support generates a dense additive subgroup. A bounded, uniformly
continuous function `h : E → ℝ` with `h x = ∫ t, h (x - t) ∂ν` for every `x` is constant.

```lean
MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub.{u_1} {E : Type u_1}
  [SeminormedAddCommGroup E] [MeasurableSpace E] [OpensMeasurableSpace E]
  {ν : MeasureTheory.Measure E} [MeasureTheory.IsProbabilityMeasure ν]
  (hν : Dense ↑(AddSubgroup.closure ν.support)) {h : E → ℝ} {C : ℝ} (hC : ∀ (x : E), |h x| ≤ C)
  (hu : UniformContinuous h) (hh : ∀ (x : E), h x = ∫ (t : E), h (x - t) ∂ν) (x y : E) : h x = h y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Choquet–Deny lemma](choquet-deny-lemma.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/ChoquetDeny.html#MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub).

## Other forms

**Choquet–Deny theorem on `ℝ`, harmonic measures.** Formalized in Tau Ceti as [`MeasureTheory.Measure.eq_smul_volume_of_conv_eq_self`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/ChoquetDeny.html#MeasureTheory.Measure.eq_smul_volume_of_conv_eq_self).

```lean
MeasureTheory.Measure.eq_smul_volume_of_conv_eq_self {ν : MeasureTheory.Measure ℝ}
  [MeasureTheory.IsProbabilityMeasure ν] (hν : Dense ↑(AddSubgroup.closure ν.support))
  {η : MeasureTheory.Measure ℝ} {C : NNReal} (hC : ∀ (a : ℝ), η (Set.Icc a (a + 1)) ≤ ↑C)
  (hη : ν.conv η = η) : η = η (Set.Ioc 0 1) • MeasureTheory.volume
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/ChoquetDeny.html#MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub)
- [Source of `MeasureTheory.Measure.apply_eq_of_forall_eq_integral_sub` in TauCeti/MeasureTheory/Group/ChoquetDeny.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Group/ChoquetDeny.lean#L149)
