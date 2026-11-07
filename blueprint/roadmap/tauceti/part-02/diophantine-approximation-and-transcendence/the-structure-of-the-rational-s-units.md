---
declaration: def
origin: cited
lean: TauCeti.sUnitsRatMulEquiv
statement: formalized
---

# The structure of the rational `S`-units

If `S` consists of primes, the map
`x ↦ (sign x, (v_p(x))_{p ∈ S})` is an isomorphism from the rational `S`-units to
`ℤˣ × Multiplicative (S → ℤ)`; its inverse sends `(ε, z)` to `ε ∏_{p ∈ S} p ^ z_p`
(`TauCeti.coe_sUnitsRatMulEquiv_symm_apply`).

```lean
TauCeti.sUnitsRatMulEquiv {S : Finset ℕ} (hS : ∀ p ∈ S, Nat.Prime p) :
  ↥({v | ↑(Rat.HeightOneSpectrum.primesEquiv v) ∈ S}.unit ℚ) ≃* ℤˣ × Multiplicative (↥S → ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sUnitsRatMulEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SUnits/Rat/Structure.html#TauCeti.sUnitsRatMulEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.sUnitsRatMulEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SUnits/Rat/Structure.html#TauCeti.sUnitsRatMulEquiv)
- [Source of `TauCeti.sUnitsRatMulEquiv` in TauCeti/NumberTheory/NumberField/SUnits/Rat/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/SUnits/Rat/Structure.lean#L192)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
