---
declaration: theorem
origin: cited
lean: TauCeti.isMeagre_or_mem_residual_of_eZero_invariant
statement: formalized
proof: formalized
---

# Generic ergodicity of `E₀`

An `E₀`-invariant set with the Baire property is meagre or
comeagre.

```lean
TauCeti.isMeagre_or_mem_residual_of_eZero_invariant {B : Set (ℕ → Bool)} (hB : BaireMeasurableSet B)
  (hinv : Quotient.mk TauCeti.eZero ⁻¹' Quotient.mk TauCeti.eZero '' B = B) :
  IsMeagre B ∨ B ∈ residual (ℕ → Bool)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isMeagre_or_mem_residual_of_eZero_invariant`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/EZero.html#TauCeti.isMeagre_or_mem_residual_of_eZero_invariant).

## Sources

- [Tau Ceti documentation: `TauCeti.isMeagre_or_mem_residual_of_eZero_invariant`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/EZero.html#TauCeti.isMeagre_or_mem_residual_of_eZero_invariant)
- [Source of `TauCeti.isMeagre_or_mem_residual_of_eZero_invariant` in TauCeti/SetTheory/Descriptive/EZero.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/EZero.lean#L167)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
