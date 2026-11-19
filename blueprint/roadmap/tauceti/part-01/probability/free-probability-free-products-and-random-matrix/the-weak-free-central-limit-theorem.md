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

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsFreelyIndependentElements.tendsto_apply_inv_sqrt_smul_sum_pow_semicircleReal](tauceti-isfreelyindependentelements-tendsto-appl.md)

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
- [Source of `TauCeti.IsFreelyIndependentElements.tendsto_law_inv_sqrt_smul_sum_semicircleReal` in TauCeti/Probability/FreeProbability/Law/CentralLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Law/CentralLimit.lean#L60)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
