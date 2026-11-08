---
declaration: theorem
origin: cited
lean: TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow
statement: formalized
proof: formalized
---

# Kedlaya's estimate (4.9.1) in the normalisation `λ_ρ(p) = ρ`

Every
`d ∈ 𝕎 O[1/(p [ϖ])]` is a polynomial `∑_{i ≤ m} zᵢ p^(-(m - i))` in `p⁻¹` whose coefficients `zᵢ`
lie in `𝕎 O[1/[ϖ]]` and satisfy `λ_{ρ₂}(zᵢ) ρ₁^(-(m - i)) ≤ λ_{[ρ₁, ρ₂]}(d)`. Writing
`d = y / (p [ϖ]) ^ m` and splitting `y = ∑_{i < m} [yᵢ] pⁱ + pᵐ b`, one takes `zᵢ = [yᵢ] / [ϖ] ^ m`
for `i < m` and `zₘ = b / [ϖ] ^ m`.

```lean
TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow.{u_1, u_2} (p : ℕ)
  [Fact (Nat.Prime p)] {K : Type u_1} {O : Type u_2} [Field K] [CommRing O] [Algebra O K]
  [CharP O p] [PerfectRing O p] {v : Valuation K NNReal} {ϖ : O} (hv : v.Integers O) (hϖ : ϖ ≠ 0)
  (hϖ' : v ((algebraMap O K) ϖ) < 1) {ρ₁ ρ₂ : NNReal} (hρ₁ : ρ₁ ∈ Set.Ioo 0 1)
  (hρ₂ : ρ₂ ∈ Set.Ioo 0 1) (d : TauCeti.WittVector.IntervalLocalization p hv hϖ hϖ' hρ₁ hρ₂) :
  ∃ m z,
    (∀ i ≤ m, ‖z i‖ * (↑ρ₁)⁻¹ ^ (m - i) ≤ ‖d‖) ∧
      d =
        ∑ i ∈ Finset.range (m + 1),
          (TauCeti.WittVector.RadiusLocalization.toIntervalLocalization p hv hϖ hϖ' hρ₁ hρ₂) (z i) *
            ↑⋯.unit⁻¹ ^ (m - i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/Radius.html#TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/Radius.html#TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow)
- [Source of `TauCeti.WittVector.IntervalLocalization.exists_sum_eq_mul_inv_pow` in TauCeti/RingTheory/WittVector/IntervalRing/Radius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/WittVector/IntervalRing/Radius.lean#L109)
