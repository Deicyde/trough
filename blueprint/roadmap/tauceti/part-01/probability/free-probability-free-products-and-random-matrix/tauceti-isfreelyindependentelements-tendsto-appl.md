---
declaration: theorem
origin: cited
lean: TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal
statement: formalized
proof: formalized
---

# TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal

*The free central limit theorem*: if the elements `a j` are freely independent for a
normalised `φ`, centred, with moments `φ (a j ^ k)` bounded uniformly in `j` for each `k`, and
with average variance `N⁻¹ ∑_{j < N} φ (a j ^ 2) → v` for a real `v ≥ 0`, then the moments of
`(√N)⁻¹ • ∑_{j < N} a j` tend to those of the centred semicircle law `semicircleReal 0 v`.

```lean
TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal.{u_1, u_2}
  {𝕜 : Type u_1} {A : Type u_2} [RCLike 𝕜] [Semiring A] [Algebra 𝕜 A] {φ : A →ₗ[𝕜] 𝕜} {a : ℕ → A}
  (h : TauCeti.IsFreelyIndependentElements φ a) (hφ : φ 1 = 1) (hcen : ∀ (j : ℕ), φ (a j) = 0)
  (hbdd : ∀ (k : ℕ), ∃ M, ∀ (j : ℕ), ‖φ (a j ^ k)‖ ≤ M) {v : NNReal}
  (hvar :
    Filter.Tendsto (fun N => (↑N)⁻¹ * ∑ j ∈ Finset.range N, φ (a j ^ 2)) Filter.atTop (nhds ↑↑v))
  (n : ℕ) :
  Filter.Tendsto (fun N => φ (((↑√↑N)⁻¹ • ∑ j ∈ Finset.range N, a j) ^ n)) Filter.atTop
    (nhds ↑(∫ (x : ℝ), x ^ n ∂TauCeti.Probability.semicircleReal 0 v))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant](tauceti-apply-prod-offn-eq-sum-prod-freecumulant.md)
- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/CentralLimit.html#TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/CentralLimit.html#TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal)
- [Source of `TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal` in TauCeti/Probability/FreeProbability/CentralLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/CentralLimit.lean#L207)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
