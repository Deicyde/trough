---
declaration: theorem
origin: cited
lean: MeasureTheory.MemLp.mgf_le_exp_of_ae_le, ProbabilityTheory.iIndepFun.mgf_sum_le_exp_of_ae_le
statement: formalized
proof: formalized
---

# Bernstein's moment-generating-function bound

If `X` has mean zero, a finite second
moment and `X ≤ b` almost surely, then for `0 ≤ t` with `t * b < 3`,
`E exp (t X) ≤ exp (E X² * t ^ 2 / (2 * (1 - t * b / 3)))`.

```lean
MeasureTheory.MemLp.mgf_le_exp_of_ae_le.{u_1} {Ω : Type u_1} {mΩ : MeasurableSpace Ω}
  {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ] {X : Ω → ℝ} {b t : ℝ}
  (hX : MeasureTheory.MemLp X 2 μ) (hmean : ∫ (x : Ω), X x ∂μ = 0) (hb : ∀ᵐ (ω : Ω) ∂μ, X ω ≤ b)
  (ht : 0 ≤ t) (htb : t * b < 3) :
  ProbabilityTheory.mgf X μ t ≤ Real.exp ((∫ (ω : Ω), X ω ^ 2 ∂μ) * t ^ 2 / (2 * (1 - t * b / 3)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bernstein's exponential bound](../../analysis/part-02/special-functions/bernsteins-exponential-bound.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.MemLp.mgf_le_exp_of_ae_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Bernstein.html#MeasureTheory.MemLp.mgf_le_exp_of_ae_le).

## Other forms

**Bernstein's moment-generating-function bound for independent sums.** Formalized in Tau Ceti as [`ProbabilityTheory.iIndepFun.mgf_sum_le_exp_of_ae_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Bernstein.html#ProbabilityTheory.iIndepFun.mgf_sum_le_exp_of_ae_le).

```lean
ProbabilityTheory.iIndepFun.mgf_sum_le_exp_of_ae_le.{u_1, u_2} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {μ : MeasureTheory.Measure Ω} {ι : Type u_2} {X : ι → Ω → ℝ}
  (h_indep : ProbabilityTheory.iIndepFun X μ) {s : Finset ι} {b t : ℝ}
  (hX : ∀ i ∈ s, MeasureTheory.MemLp (X i) 2 μ) (hmean : ∀ i ∈ s, ∫ (x : Ω), X i x ∂μ = 0)
  (hb : ∀ i ∈ s, ∀ᵐ (ω : Ω) ∂μ, X i ω ≤ b) (ht : 0 ≤ t) (htb : t * b < 3) :
  ProbabilityTheory.mgf (fun ω => ∑ i ∈ s, X i ω) μ t ≤
    Real.exp ((∑ i ∈ s, ∫ (ω : Ω), X i ω ^ 2 ∂μ) * t ^ 2 / (2 * (1 - t * b / 3)))
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.MemLp.mgf_le_exp_of_ae_le`](https://taucetiproject.org/docs/TauCeti/Probability/Moments/Bernstein.html#MeasureTheory.MemLp.mgf_le_exp_of_ae_le)
- [Source of `MeasureTheory.MemLp.mgf_le_exp_of_ae_le` in TauCeti/Probability/Moments/Bernstein.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Moments/Bernstein.lean#L52)
