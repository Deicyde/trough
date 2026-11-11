---
declaration: theorem
origin: cited
lean: LinearMap.exists_norm_apply_le_of_tsupport_subset
statement: formalized
proof: formalized
---

# Peetre's estimate on punctured balls

Let `P` be local on the open set `U` with `P u`
continuous on `U` for every `u`. Then near each `x₀ ∈ U` there are `ρ > 0`, an order `r` and a
constant `C` such that `‖(P φ) y‖ ≤ C * M` at every `y ∈ U`, for every smooth `φ` supported in
`ball x₀ ρ \ {x₀}` whose derivatives of order at most `r` are bounded by `M`.

```lean
LinearMap.exists_norm_apply_le_of_tsupport_subset.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2}
  {G : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {U : Set E} [CompleteSpace F]
  (P : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤ →ₗ[ℝ] E → G)
  (hU : IsOpen U)
  (hloc :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ∀ x ∈ U, ⇑u =ᶠ[nhds x] 0 → P u x = 0)
  (hcont :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ContinuousOn (P u) U)
  {x₀ : E} (hx₀ : x₀ ∈ U) :
  ∃ ρ > 0,
    Metric.ball x₀ ρ ⊆ U ∧
      ∃ r C,
        ∀ (φ : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
          tsupport ⇑φ ⊆ Metric.ball x₀ ρ \ {x₀} →
            ∀ (M : ℝ),
              (∀ i ≤ r, ∀ (z : E), ‖iteratedFDeriv ℝ i (⇑φ) z‖ ≤ M) → ∀ y ∈ U, ‖P φ y‖ ≤ C * M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_norm_apply_le_of_tsupport_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalOperator.html#LinearMap.exists_norm_apply_le_of_tsupport_subset).

## Sources

- [Tau Ceti documentation: `LinearMap.exists_norm_apply_le_of_tsupport_subset`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalOperator.html#LinearMap.exists_norm_apply_le_of_tsupport_subset)
- [Source of `LinearMap.exists_norm_apply_le_of_tsupport_subset` in TauCeti/Analysis/Calculus/LocalOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/LocalOperator.lean#L186)
