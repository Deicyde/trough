---
declaration: theorem
origin: cited
lean: TauCeti.mul_add_mul_ne_zero_of_linearIndependent
statement: formalized
proof: formalized
---

# Gelfond–Schneider for two logarithms

If `λ₁, λ₂ ∈ 𝓛` are linearly independent over `ℚ`,
then `β₁ λ₁ + β₂ λ₂ ≠ 0` for all algebraic numbers `β₁, β₂` that are not both zero.

```lean
TauCeti.mul_add_mul_ne_zero_of_linearIndependent {l₁ l₂ β₁ β₂ : ℂ}
  (hl₁ : l₁ ∈ TauCeti.algebraicLogs) (hl₂ : l₂ ∈ TauCeti.algebraicLogs)
  (hl : LinearIndependent ℚ ![l₁, l₂]) (hβ₁ : IsAlgebraic ℚ β₁) (hβ₂ : IsAlgebraic ℚ β₂)
  (hβ : β₁ ≠ 0 ∨ β₂ ≠ 0) : β₁ * l₁ + β₂ * l₂ ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gelfond–Schneider theorem (Karatarakis–Wiedijk, §3)](the-gelfond-schneider-theorem-karatarakis-wiedij.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mul_add_mul_ne_zero_of_linearIndependent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.html#TauCeti.mul_add_mul_ne_zero_of_linearIndependent).

## Sources

- [Tau Ceti documentation: `TauCeti.mul_add_mul_ne_zero_of_linearIndependent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.html#TauCeti.mul_add_mul_ne_zero_of_linearIndependent)
- [Source of `TauCeti.mul_add_mul_ne_zero_of_linearIndependent` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Corollaries.lean#L73)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
