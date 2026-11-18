---
declaration: theorem
origin: cited
lean: TauCeti.Finance.le_of_pde_le_of_terminal_le
statement: formalized
proof: formalized
---

# The comparison principle for the pricing equation

Let the volatility `σ(s, t)` and the
rate `r(t)` be bounded for `0 < t < T`, by `σ² ≤ Λ` and `|r| ≤ R`. Let `C₁` and `C₂` be continuous
on `s > 0`, `0 ≤ t ≤ T`, twice continuously differentiable in the spot and differentiable in time
for `s > 0`, `0 < t < T`, with `C₁ - C₂ ≤ A (1 + s)`. If the pricing operator
`C_t + σ² s² / 2 C_ss + r (s C_s - C)` of `C₂` is at most that of `C₁` for `0 < t < T`, and
`C₁(s, T) ≤ C₂(s, T)` for every spot `s > 0`, then `C₁ ≤ C₂` for `s > 0` and `0 ≤ t ≤ T`.

```lean
TauCeti.Finance.le_of_pde_le_of_terminal_le {σ : ℝ → ℝ → ℝ} {r : ℝ → ℝ} {C₁ C₂ : ℝ → ℝ → ℝ}
  {T Λ R A : ℝ} (hσ : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → σ s t ^ 2 ≤ Λ)
  (hr : ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → |r t| ≤ R)
  (hC₁ : ContinuousOn (Function.uncurry C₁) (Set.Ioi 0 ×ˢ Set.Icc 0 T))
  (hC₂ : ContinuousOn (Function.uncurry C₂) (Set.Ioi 0 ×ˢ Set.Icc 0 T))
  (hgrowth : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Icc 0 T → C₁ s t - C₂ s t ≤ A * (1 + s))
  (hcd₁ : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → ContDiffAt ℝ 2 (fun x => C₁ x t) s)
  (hcd₂ : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → ContDiffAt ℝ 2 (fun x => C₂ x t) s)
  (hdiff₁ : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → DifferentiableAt ℝ (fun u => C₁ s u) t)
  (hdiff₂ : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → DifferentiableAt ℝ (fun u => C₂ s u) t)
  (hpde :
    ∀ ⦃s : ℝ⦄,
      0 < s →
        ∀ ⦃t : ℝ⦄,
          t ∈ Set.Ioo 0 T →
            deriv (fun u => C₂ s u) t + σ s t ^ 2 * s ^ 2 / 2 * deriv (deriv fun x => C₂ x t) s +
                r t * (s * deriv (fun x => C₂ x t) s - C₂ s t) ≤
              deriv (fun u => C₁ s u) t + σ s t ^ 2 * s ^ 2 / 2 * deriv (deriv fun x => C₁ x t) s +
                r t * (s * deriv (fun x => C₁ x t) s - C₁ s t))
  (hterminal : ∀ ⦃s : ℝ⦄, 0 < s → C₁ s T ≤ C₂ s T) ⦃s : ℝ⦄ :
  0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Icc 0 T → C₁ s t ≤ C₂ s t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Finance.le_of_pde_le_of_terminal_le`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/Comparison.html#TauCeti.Finance.le_of_pde_le_of_terminal_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Finance.le_of_pde_le_of_terminal_le`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/Comparison.html#TauCeti.Finance.le_of_pde_le_of_terminal_le)
- [Source of `TauCeti.Finance.le_of_pde_le_of_terminal_le` in TauCeti/Probability/Finance/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/Comparison.lean#L127)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
