---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.eq_callValue_of_pde
statement: formalized
proof: formalized
---

# Uniqueness of the Black–Scholes call price

Let `σ > 0` and `K > 0`. Let `C(s, t)` be
continuous on `s > 0`, `0 ≤ t ≤ T`, twice continuously differentiable in the spot and
differentiable in time for `s > 0`, `0 < t < T`, with `|C(s, t)| ≤ A (1 + s)`. If `C` solves the
Black–Scholes equation `C_t + σ² s² / 2 C_ss + r (s C_s - C) = 0` for `s > 0`, `0 < t < T`, and
`C(s, T) = (s - K)⁺`, then `C` is the Black–Scholes call price:
`C(s, t) = callValue s r σ K (T - t)` for `s > 0` and `0 ≤ t ≤ T`.

```lean
TauCeti.BlackScholes.eq_callValue_of_pde {C : ℝ → ℝ → ℝ} {r σ K T A : ℝ} (hσ : 0 < σ) (hK : 0 < K)
  (hC : ContinuousOn (Function.uncurry C) (Set.Ioi 0 ×ˢ Set.Icc 0 T))
  (hcd : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → ContDiffAt ℝ 2 (fun x => C x t) s)
  (hdiff : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Ioo 0 T → DifferentiableAt ℝ (fun u => C s u) t)
  (hpde :
    ∀ ⦃s : ℝ⦄,
      0 < s →
        ∀ ⦃t : ℝ⦄,
          t ∈ Set.Ioo 0 T →
            deriv (fun u => C s u) t + σ ^ 2 * s ^ 2 / 2 * deriv (deriv fun x => C x t) s +
                r * (s * deriv (fun x => C x t) s - C s t) =
              0)
  (hgrowth : ∀ ⦃s : ℝ⦄, 0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Icc 0 T → |C s t| ≤ A * (1 + s))
  (hterminal : ∀ ⦃s : ℝ⦄, 0 < s → C s T = (s - K)⁺) ⦃s : ℝ⦄ :
  0 < s → ∀ ⦃t : ℝ⦄, t ∈ Set.Icc 0 T → C s t = TauCeti.BlackScholes.callValue s r σ K (T - t)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Black–Scholes call formula](the-black-scholes-call-formula.md)
- [The comparison principle for the pricing equation](the-comparison-principle-for-the-pricing-equatio.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.eq_callValue_of_pde`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Uniqueness.html#TauCeti.BlackScholes.eq_callValue_of_pde).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.eq_callValue_of_pde`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Uniqueness.html#TauCeti.BlackScholes.eq_callValue_of_pde)
- [Source of `TauCeti.BlackScholes.eq_callValue_of_pde` in TauCeti/Probability/Finance/BlackScholes/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/BlackScholes/Uniqueness.lean#L62)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
