---
declaration: def
origin: cited
lean: TauCeti.NumberField.Units.boundedDivisors
statement: formalized
---

# TauCeti.NumberField.Units.boundedDivisors

The divisors `γ` of `α` with `house γ ≤ exp c₁ * |N(α)| ^ (1 / d)`, where
`c₁ = rank K * ∑ j, ‖log u j‖` and `d = [K : ℚ]`. When `u` has maximal rank and `α ≠ 0`, every
divisor of `α` is a unit times a member of this set (`exists_mem_boundedDivisors_of_dvd`), and the
set is finite (`boundedDivisors_finite`).

```lean
TauCeti.NumberField.Units.boundedDivisors.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (u : Fin (NumberField.Units.rank K) → (NumberField.RingOfIntegers K)ˣ)
  (α : NumberField.RingOfIntegers K) : Set (NumberField.RingOfIntegers K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Units.boundedDivisors`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Balanced.html#TauCeti.NumberField.Units.boundedDivisors).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Units.boundedDivisors`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Balanced.html#TauCeti.NumberField.Units.boundedDivisors)
- [Source of `TauCeti.NumberField.Units.boundedDivisors` in TauCeti/NumberTheory/NumberField/Units/Balanced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Units/Balanced.lean#L176)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
