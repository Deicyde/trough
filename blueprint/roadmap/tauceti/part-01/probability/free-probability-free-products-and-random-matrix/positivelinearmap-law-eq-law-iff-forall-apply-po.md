---
declaration: theorem
origin: cited
lean: PositiveLinearMap.law_eq_law_iff_forall_apply_pow
statement: formalized
proof: formalized
---

# PositiveLinearMap.law_eq_law_iff_forall_apply_pow

Two selfadjoint elements, possibly in different C⋆-algebras and with respect to different
positive functionals, have the same law exactly when they have the same moments:
`μ_a = μ_b ↔ ∀ n, φ (a ^ n) = ψ (b ^ n)`.

```lean
PositiveLinearMap.law_eq_law_iff_forall_apply_pow.{u_1, u_2} {A : Type u_1} [CStarAlgebra A]
  [PartialOrder A] [StarOrderedRing A] (φ : A →ₚ[ℂ] ℂ) {a : A} {B : Type u_2} [CStarAlgebra B]
  [PartialOrder B] [StarOrderedRing B] (ψ : B →ₚ[ℂ] ℂ) {b : B} (ha : IsSelfAdjoint a)
  (hb : IsSelfAdjoint b) : φ.law a = ψ.law b ↔ ∀ (n : ℕ), φ (a ^ n) = ψ (b ^ n)
```

## Depends on

- [PositiveLinearMap.law](positivelinearmap-law.md)

## Lean

Formalized in Tau Ceti as [`PositiveLinearMap.law_eq_law_iff_forall_apply_pow`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.law_eq_law_iff_forall_apply_pow).

## Sources

- [Tau Ceti documentation: `PositiveLinearMap.law_eq_law_iff_forall_apply_pow`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.law_eq_law_iff_forall_apply_pow)
- [Source of `PositiveLinearMap.law_eq_law_iff_forall_apply_pow` in TauCeti/Probability/FreeProbability/Law/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/FreeProbability/Law/Basic.lean#L282)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeProbability/STATUS.md)
