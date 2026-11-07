---
declaration: theorem
origin: cited
lean: AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq
statement: formalized
proof: formalized
---

# Integral measures on `ℤ_pˣ` from unit coordinates

For every family of coefficients
`c n : (ℤ/p^nℤ)ˣ →₀ ℤ_p` compatible under the reductions `(ℤ/p^nℤ)ˣ → (ℤ/p^mℤ)ˣ`, there is a
unique integral measure on `ℤ_pˣ` whose finite projection along the reduction
`ℤ_pˣ → (ℤ/p^nℤ)ˣ` is `c n` for every `n`.

```lean
AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq {p : ℕ} [Fact (Nat.Prime p)]
  {c : (n : ℕ) → (ZMod (p ^ n))ˣ →₀ ℤ_[p]}
  (hc : ∀ ⦃m n : ℕ⦄ (h : m ≤ n), Finsupp.mapDomain (⇑(ZMod.unitsMap ⋯)) (c n) = c m) :
  ∃! μ, ∀ (n : ℕ), (AbstractMeasure.finiteProjection ↑(PadicInt.unitsToZModPow n)) μ = c n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Integral measures are the compatible families along a tower](integral-measures-are-the-compatible-families-al.md)
- [TauCeti.FiniteQuotientTower](tauceti-finitequotienttower.md)
- [TauCeti.FiniteQuotientTower.compatibleFamilies](tauceti-finitequotienttower-compatiblefamilies.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.html#AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.html#AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq)
- [Source of `AbstractMeasure.existsUnique_finiteProjection_unitsToZModPow_eq` in TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.lean#L195)
- [Tau Ceti roadmap status: P-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
