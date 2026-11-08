---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le
statement: formalized
proof: formalized
---

# The full strong-type Calderón–Zygmund theorem

An `L²`-bounded operator for which both
it and its adjoint satisfy the cancellation estimate with finite constants extends to a bounded
operator on `Lᵖ(ℝⁿ; H) → Lᵖ(ℝⁿ; K)` for every `1 < p < ∞`. On `L² ∩ Lᵖ`, the extended map agrees
almost everywhere with the given operator.

```lean
ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le.{u_1, u_2, u_3}
  {ι : Type u_1} [Fintype ι] [Nonempty ι] {H : Type u_2} {K : Type u_3} [NormedAddCommGroup H]
  [InnerProductSpace ℝ H] [CompleteSpace H] [NormedAddCommGroup K] [InnerProductSpace ℝ K]
  [CompleteSpace K] {p : ENNReal} [Fact (1 ≤ p)]
  (T :
    ↥(MeasureTheory.Lp H 2 MeasureTheory.volume) →L[ℝ] ↥(MeasureTheory.Lp K 2 MeasureTheory.volume))
  {B B' : ENNReal} (hB : B ≠ ⊤) (hB' : B' ≠ ⊤)
  (hT :
    ∀ (b : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∫ (x : ι → ℝ), ↑↑b x = 0 →
          ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (2 * r))ᶜ, ‖↑↑(T b) x‖ₑ ≤
            B * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ)
  (hT' :
    ∀ (b : ↥(MeasureTheory.Lp K 2 MeasureTheory.volume)) (y : ι → ℝ) (r : ℝ),
      (∀ᵐ (x : ι → ℝ), x ∉ Metric.closedBall y r → ↑↑b x = 0) →
        ∫ (x : ι → ℝ), ↑↑b x = 0 →
          ∫⁻ (x : ι → ℝ) in (Metric.closedBall y (2 * r))ᶜ,
              ‖↑↑((ContinuousLinearMap.adjoint T) b) x‖ₑ ≤
            B' * ∫⁻ (x : ι → ℝ), ‖↑↑b x‖ₑ)
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C S,
    ‖S‖ ≤ ↑C ∧
      ∀ (f : ↥(MeasureTheory.Lp H 2 MeasureTheory.volume))
        (hf : MeasureTheory.MemLp (↑↑f) p MeasureTheory.volume),
        ↑↑(S (MeasureTheory.MemLp.toLp (↑↑f) hf)) =ᵐ[MeasureTheory.volume] ↑↑(T f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Calderón–Zygmund theorem, weak type `(1, 1)`](the-calderon-zygmund-theorem-weak-type-1-1.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/Extension.html#ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/CalderonZygmund/Extension.html#ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le)
- [Source of `ContinuousLinearMap.exists_strongTypeExtension_of_setLIntegral_compl_closedBall_le` in TauCeti/MeasureTheory/Integral/CalderonZygmund/Extension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/CalderonZygmund/Extension.lean#L40)
