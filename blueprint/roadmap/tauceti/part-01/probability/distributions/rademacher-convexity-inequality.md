---
declaration: theorem
origin: cited
lean: Finset.norm_le_integral_norm_sum_smul_rademacher, Seminorm.seminorm_le_integral_seminorm_sum_smul_rademacher
statement: formalized
proof: formalized
---

# Rademacher convexity inequality

Every summand's norm is bounded by the expected
norm of the signed sum. Pairwise independence of the Rademacher signs suffices.

```lean
Finset.norm_le_integral_norm_sum_smul_rademacher.{u_1, u_2, u_3} {Ω : Type u_1} {ι : Type u_2}
  {E : Type u_3} [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} [SeminormedAddCommGroup E]
  [NormedSpace ℝ E] {ε : ι → Ω → ℝ} (s : Finset ι) (v : ι → E)
  (hε : ∀ i ∈ s, ProbabilityTheory.HasLaw (ε i) TauCeti.Probability.rademacherMeasure P)
  (hind : (↑s).Pairwise fun i j => ProbabilityTheory.IndepFun (ε i) (ε j) P) {j : ι} (hj : j ∈ s) :
  ‖v j‖ ≤ ∫ (ω : Ω), ‖∑ i ∈ s, ε i ω • v i‖ ∂P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.norm_le_integral_norm_sum_smul_rademacher`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Rademacher/Norm.html#Finset.norm_le_integral_norm_sum_smul_rademacher).

## Other forms

**Rademacher convexity inequality for seminorms.** Formalized in Tau Ceti as [`Seminorm.seminorm_le_integral_seminorm_sum_smul_rademacher`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Rademacher/Norm.html#Seminorm.seminorm_le_integral_seminorm_sum_smul_rademacher).

```lean
Seminorm.seminorm_le_integral_seminorm_sum_smul_rademacher.{u_1, u_2, u_3} {Ω : Type u_1}
  {ι : Type u_2} {E : Type u_3} [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} [AddCommGroup E]
  [_root_.Module ℝ E] {ε : ι → Ω → ℝ} (p : Seminorm ℝ E) (s : Finset ι) (v : ι → E)
  (hε : ∀ i ∈ s, ProbabilityTheory.HasLaw (ε i) TauCeti.Probability.rademacherMeasure P)
  (hind : (↑s).Pairwise fun i j => ProbabilityTheory.IndepFun (ε i) (ε j) P) {j : ι} (hj : j ∈ s) :
  p (v j) ≤ ∫ (ω : Ω), p (∑ i ∈ s, ε i ω • v i) ∂P
```

## Sources

- [Tau Ceti documentation: `Finset.norm_le_integral_norm_sum_smul_rademacher`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Rademacher/Norm.html#Finset.norm_le_integral_norm_sum_smul_rademacher)
- [Source of `Finset.norm_le_integral_norm_sum_smul_rademacher` in TauCeti/Probability/Distributions/Rademacher/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/Rademacher/Norm.lean#L161)
