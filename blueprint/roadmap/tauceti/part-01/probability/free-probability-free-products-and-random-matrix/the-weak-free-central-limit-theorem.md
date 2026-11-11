---
declaration: theorem
origin: cited
lean: TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal, TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_of_apply_pow_eq
statement: formalized
proof: formalized
---

# The weak free central limit theorem

Centered free selfadjoint elements whose moments
are uniformly bounded in each degree and whose average variance tends to `v ≥ 0` have
normalized-sum laws converging weakly to `semicircleReal 0 v`. No common compact support of the
approximating laws is required.

```lean
TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal.{u_1}
  {A : Type u_1} [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A] {φ : A →ₚ[ℂ] ℂ} {a : ℕ → A}
  (h : TauCeti.IsFreelyIndependentElements φ.toLinearMap a) (hφ : φ 1 = 1)
  (ha : ∀ (j : ℕ), IsSelfAdjoint (a j)) (hcen : ∀ (j : ℕ), φ (a j) = 0)
  (hbdd : ∀ (k : ℕ), ∃ M, ∀ (j : ℕ), ‖φ (a j ^ k)‖ ≤ M) {v : NNReal}
  (hvar :
    Filter.Tendsto (fun N => (↑N)⁻¹ * ∑ j ∈ Finset.range N, φ (a j ^ 2)) Filter.atTop (nhds ↑↑v)) :
  Filter.Tendsto (fun N => ⟨φ.law ((√↑N)⁻¹ • ∑ j ∈ Finset.range N, a j), ⋯⟩) Filter.atTop
    (nhds (TauCeti.Probability.semicircleReal 0 v).toProbabilityMeasure)
```

## Depends on

- [PositiveLinearMap.law](positivelinearmap-law.md)
- [TauCeti.IsFreelyIndependent](tauceti-isfreelyindependent.md)
- [TauCeti.Probability.semicircleReal](../random-matrices/tauceti-probability-semicirclereal.md)

## Proof depends on

- [TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant](tauceti-apply-prod-offn-eq-sum-prod-freecumulant.md)
- [TauCeti.freeCumulant](tauceti-freecumulant.md)
- [TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment](tauceti-freecumulant-eq-sum-mu-mul-partitionmome.md)
- [TauCeti.freeCumulant_fiberProd_eq_sum_prod](tauceti-freecumulant-fiberprod-eq-sum-prod.md)
- [TauCeti.NoncrossingPartition.card_isPairing_fin_eq_catalan](tauceti-noncrossingpartition-card-ispairing-fin.md)
- [TauCeti.partitionCumulant_eq_prod_freeCumulant](tauceti-partitioncumulant-eq-prod-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/CentralLimit.html#TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal).

## Other forms

**The weak free central limit theorem for identically distributed elements.** Formalized in Tau Ceti as [`TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_of_apply_pow_eq`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/CentralLimit.html#TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_of_apply_pow_eq).

```lean
TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_of_apply_pow_eq.{u_1}
  {A : Type u_1} [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A] {φ : A →ₚ[ℂ] ℂ} {a : ℕ → A}
  (h : TauCeti.IsFreelyIndependentElements φ.toLinearMap a) (hφ : φ 1 = 1)
  (ha : ∀ (j : ℕ), IsSelfAdjoint (a j)) (hid : ∀ (j k : ℕ), φ (a j ^ k) = φ (a 0 ^ k))
  (hcen : φ (a 0) = 0) {v : NNReal} (hv : φ (a 0 ^ 2) = ↑↑v) :
  Filter.Tendsto (fun N => ⟨φ.law ((√↑N)⁻¹ • ∑ j ∈ Finset.range N, a j), ⋯⟩) Filter.atTop
    (nhds (TauCeti.Probability.semicircleReal 0 v).toProbabilityMeasure)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/CentralLimit.html#TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal)
- [Source of `TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal` in TauCeti/Probability/FreeProbability/Law/CentralLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/FreeProbability/Law/CentralLimit.lean#L60)
