---
declaration: def
origin: cited
lean: AbstractMeasure.towerCoordinatesEquiv
statement: formalized
---

# Integral measures are the compatible families along a tower

For a compact group with a
tower of finite quotients, sending an integral measure to its finite projections at all levels is
a linear equivalence onto the compatible families.

```lean
AbstractMeasure.towerCoordinatesEquiv.{u_1, u_3} {Γ : Type u_1} [Group Γ] [TopologicalSpace Γ]
  [CompactSpace Γ] {A : ℕ → Type u_3} [(n : ℕ) → Group (A n)] [(n : ℕ) → TopologicalSpace (A n)]
  [∀ (n : ℕ), DiscreteTopology (A n)] [∀ (n : ℕ), Finite (A n)]
  (T : TauCeti.FiniteQuotientTower Γ A) {p : ℕ} [Fact (Nat.Prime p)] :
  AbstractMeasure Γ ℤ_[p] ℤ_[p] ≃ₗ[ℤ_[p]] ↥(T.compatibleFamilies ℤ_[p])
```

## Depends on

- [TauCeti.FiniteQuotientTower](tauceti-finitequotienttower.md)
- [TauCeti.FiniteQuotientTower.compatibleFamilies](tauceti-finitequotienttower-compatiblefamilies.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.towerCoordinatesEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.html#AbstractMeasure.towerCoordinatesEquiv).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.towerCoordinatesEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.html#AbstractMeasure.towerCoordinatesEquiv)
- [Source of `AbstractMeasure.towerCoordinatesEquiv` in TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/TowerCoordinates.lean#L156)
- [Tau Ceti roadmap status: P-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
