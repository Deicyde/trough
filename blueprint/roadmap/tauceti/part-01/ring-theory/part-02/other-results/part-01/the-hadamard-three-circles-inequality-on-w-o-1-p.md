---
declaration: theorem
origin: cited
lean: TauCeti.WittVector.gaussValuationAway_le_max, TauCeti.WittVector.gaussValuation_mul_inv_pow_le_max
statement: formalized
proof: formalized
---

# The Hadamard three circles inequality on `𝕎 O[1/(p [ϖ])]`

For radii
`ρ₁ ≤ ρ ≤ ρ₂`, the Gauss valuation `λ_ρ` is bounded by the larger of `λ_{ρ₁}` and `λ_{ρ₂}`, so
the interval norm of an interval dominates every Gauss valuation at a radius inside it.

```lean
TauCeti.WittVector.gaussValuationAway_le_max.{u_1, u_2, u_3} {p : ℕ} [Fact (Nat.Prime p)]
  {K : Type u_1} {O : Type u_2} [Field K] [CommRing O] [Algebra O K] {v : Valuation K NNReal}
  {ϖ : O} [CharP O p] [PerfectRing O p] {B : Type u_3} [CommRing B] [Algebra (WittVector p O) B]
  [IsLocalization.Away (↑p * (WittVector.teichmuller p) ϖ) B] (hv : v.Integers O) (hϖ : ϖ ≠ 0)
  {ρ ρ₁ ρ₂ : NNReal} (hρ : ρ ∈ Set.Ioo 0 1) (hρ₁ : ρ₁ ∈ Set.Ioo 0 1) (hρ₂ : ρ₂ ∈ Set.Ioo 0 1)
  (h₁ : ρ₁ ≤ ρ) (h₂ : ρ ≤ ρ₂) (x : B) :
  (TauCeti.WittVector.gaussValuationAway p hv hϖ ρ hρ B) x ≤
    max ((TauCeti.WittVector.gaussValuationAway p hv hϖ ρ₁ hρ₁ B) x)
      ((TauCeti.WittVector.gaussValuationAway p hv hϖ ρ₂ hρ₂ B) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WittVector.gaussValuationAway_le_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/Subinterval.html#TauCeti.WittVector.gaussValuationAway_le_max).

## Other forms

**The Hadamard three circles inequality for Gauss valuations.** Formalized in Tau Ceti as [`TauCeti.WittVector.gaussValuation_mul_inv_pow_le_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/GaussValuation.html#TauCeti.WittVector.gaussValuation_mul_inv_pow_le_max).

```lean
TauCeti.WittVector.gaussValuation_mul_inv_pow_le_max.{u_1, u_2} {p : ℕ} [Fact (Nat.Prime p)]
  {K : Type u_1} {O : Type u_2} [Field K] [CommRing O] [Algebra O K] [CharP O p] [PerfectRing O p]
  {v : Valuation K NNReal} {ρ : NNReal} (hv : v.Integers O) {ρ₁ ρ₂ : NNReal} (hρ : ρ < 1)
  (hρ₁ : ρ₁ < 1) (hρ₂ : ρ₂ < 1) (h₀ : 0 < ρ₁) (h₁ : ρ₁ ≤ ρ) (h₂ : ρ ≤ ρ₂) (x : WittVector p O)
  (m : ℕ) :
  (TauCeti.WittVector.gaussValuation p hv ρ hρ) x * (ρ ^ m)⁻¹ ≤
    max ((TauCeti.WittVector.gaussValuation p hv ρ₁ hρ₁) x * (ρ₁ ^ m)⁻¹)
      ((TauCeti.WittVector.gaussValuation p hv ρ₂ hρ₂) x * (ρ₂ ^ m)⁻¹)
```

## Sources

- [Tau Ceti documentation: `TauCeti.WittVector.gaussValuationAway_le_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/Subinterval.html#TauCeti.WittVector.gaussValuationAway_le_max)
- [Source of `TauCeti.WittVector.gaussValuationAway_le_max` in TauCeti/RingTheory/WittVector/IntervalRing/Subinterval.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/WittVector/IntervalRing/Subinterval.lean#L87)
