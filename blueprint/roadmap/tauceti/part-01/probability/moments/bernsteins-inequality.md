---
declaration: theorem
origin: cited
lean: ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le, ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_abs_le
statement: formalized
proof: formalized
---

# Bernstein's inequality

Let the `Xᵢ`, `i ∈ s`, be independent with mean zero, finite
second moments and `Xᵢ ≤ b` almost surely, and let `v = ∑ i ∈ s, E Xᵢ²`. Then for `0 ≤ ε`,
`P(ε ≤ ∑ i ∈ s, Xᵢ) ≤ exp (-ε ^ 2 / (2 * (v + b * ε / 3)))`.

```lean
ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le.{u_1, u_2} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} {ι : Type u_2} {X : ι → Ω → ℝ}
  (h_indep : ProbabilityTheory.iIndepFun X μ) {s : Finset ι} {b ε : ℝ}
  (hX : ∀ i ∈ s, MeasureTheory.MemLp (X i) 2 μ) (hmean : ∀ i ∈ s, ∫ (x : Ω), X i x ∂μ = 0)
  (hb : ∀ i ∈ s, ∀ᵐ (ω : Ω) ∂μ, X i ω ≤ b) (hε : 0 ≤ ε) :
  μ.real {ω | ε ≤ ∑ i ∈ s, X i ω} ≤
    Real.exp (-ε ^ 2 / (2 * (∑ i ∈ s, ∫ (ω : Ω), X i ω ^ 2 ∂μ + b * ε / 3)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bernstein's moment-generating-function bound](bernsteins-moment-generating-function-bound.md)

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Bernstein.html#ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le).

## Other forms

**Bernstein's inequality, two-sided form.** Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_abs_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Bernstein.html#ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_abs_le).

```lean
ProbabilityTheory.iIndepFun.measureReal_abs_sum_ge_le_of_abs_le.{u_1, u_2} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} {ι : Type u_2} {X : ι → Ω → ℝ}
  (h_indep : ProbabilityTheory.iIndepFun X μ) {s : Finset ι} {b ε : ℝ}
  (hX : ∀ i ∈ s, AEMeasurable (X i) μ) (hmean : ∀ i ∈ s, ∫ (x : Ω), X i x ∂μ = 0)
  (hb : ∀ i ∈ s, ∀ᵐ (ω : Ω) ∂μ, |X i ω| ≤ b) (hε : 0 ≤ ε) :
  μ.real {ω | ε ≤ |∑ i ∈ s, X i ω|} ≤
    2 * Real.exp (-ε ^ 2 / (2 * (∑ i ∈ s, ∫ (ω : Ω), X i ω ^ 2 ∂μ + b * ε / 3)))
```

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Bernstein.html#ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le)
- [Source of `ProbabilityTheory.iIndepFun.measureReal_sum_ge_le_of_ae_le` in TauCeti/Probability/Moments/Bernstein.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Moments/Bernstein.lean#L105)
