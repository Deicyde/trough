---
declaration: theorem
origin: cited
lean: TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp
statement: formalized
proof: formalized
---

# Moment determinacy, exponential-moment form

A finite measure on `ℝ` for which some
exponential moment `∫ e^{a|x|} dμ` with `a > 0` is finite is determined by its polynomial moments,
among finite measures for which such an exponential moment is also finite (the hypothesis `hν`).
This is the form the completeness argument consumes: the hypothesis holds for Gaussian decay and
automatically for compactly supported measures.

```lean
TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp
  {μ ν : MeasureTheory.Measure ℝ}
  (hμ : ∃ a, 0 < a ∧ MeasureTheory.Integrable (fun x => Real.exp (a * |x|)) μ)
  (hν : ∃ a, 0 < a ∧ MeasureTheory.Integrable (fun x => Real.exp (a * |x|)) ν)
  (hmom : ∀ (n : ℕ), ∫ (x : ℝ), x ^ n ∂μ = ∫ (x : ℝ), x ^ n ∂ν) : μ = ν
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Determinacy.html#TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp).

## Sources

- [Tau Ceti documentation: `TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Determinacy.html#TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp)
- [Source of `TauCeti.Measure.ext_of_forall_integral_pow_eq_of_exists_integrable_exp` in TauCeti/Probability/Moments/Determinacy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Moments/Determinacy.lean#L242)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OrthogonalL2Bases/STATUS.md)
