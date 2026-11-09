---
declaration: theorem
origin: cited
lean: TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow
statement: formalized
proof: formalized
---

# Stampacchia's lemma

Let `φ` be nonnegative and antitone on `[k₀, ∞)`, with

`φ h ≤ (M / (h - k)) ^ α * φ k ^ β` whenever `k₀ ≤ k < h`,

for constants `M > 0`, `α > 0` and `β > 1`. Then `φ (k₀ + d) = 0`, where
`d = M * φ k₀ ^ ((β - 1) / α) * 2 ^ (β / (β - 1))`.

```lean
TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow {φ : ℝ → ℝ} {k₀ M α β : ℝ} (hM : 0 < M)
  (hα : 0 < α) (hβ : 1 < β) (hφ : ∀ (h : ℝ), k₀ ≤ h → 0 ≤ φ h) (hanti : AntitoneOn φ (Set.Ici k₀))
  (hrec : ∀ (k h : ℝ), k₀ ≤ k → k < h → φ h ≤ (M / (h - k)) ^ α * φ k ^ β) :
  φ (k₀ + M * φ k₀ ^ ((β - 1) / α) * 2 ^ (β / (β - 1))) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecificLimits/Stampacchia.html#TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecificLimits/Stampacchia.html#TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow)
- [Source of `TauCeti.apply_add_eq_zero_of_le_div_sub_rpow_mul_rpow` in TauCeti/Analysis/SpecificLimits/Stampacchia.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecificLimits/Stampacchia.lean#L50)
