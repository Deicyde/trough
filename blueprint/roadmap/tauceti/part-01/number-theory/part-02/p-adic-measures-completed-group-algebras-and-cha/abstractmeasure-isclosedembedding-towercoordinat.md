---
declaration: theorem
origin: cited
lean: AbstractMeasure.isClosedEmbedding_towerCoordinates_weak
statement: formalized
proof: formalized
---

# AbstractMeasure.isClosedEmbedding_towerCoordinates_weak

Integral tower coordinates give a closed embedding for the weak topology into the product
of the coefficient functions.

```lean
AbstractMeasure.isClosedEmbedding_towerCoordinates_weak.{u_1, u_2} {Γ : Type u_1} [Group Γ]
  [TopologicalSpace Γ] [CompactSpace Γ] {A : ℕ → Type u_2} [(n : ℕ) → Group (A n)]
  [(n : ℕ) → TopologicalSpace (A n)] [∀ (n : ℕ), DiscreteTopology (A n)] [∀ (n : ℕ), Finite (A n)]
  (T : TauCeti.FiniteQuotientTower Γ A) {p : ℕ} [Fact (Nat.Prime p)] :
  Topology.IsClosedEmbedding fun μ n a => (↑((AbstractMeasure.towerCoordinates T) μ) n) a
```

## Depends on

- [TauCeti.FiniteQuotientTower](tauceti-finitequotienttower.md)

## Proof depends on

- [The comparison is a homeomorphism](the-comparison-is-a-homeomorphism.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.isClosedEmbedding_towerCoordinates_weak`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Topology/TowerCoordinates.html#AbstractMeasure.isClosedEmbedding_towerCoordinates_weak).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.isClosedEmbedding_towerCoordinates_weak`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Topology/TowerCoordinates.html#AbstractMeasure.isClosedEmbedding_towerCoordinates_weak)
- [Source of `AbstractMeasure.isClosedEmbedding_towerCoordinates_weak` in TauCeti/NumberTheory/Padics/Measure/Topology/TowerCoordinates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/Topology/TowerCoordinates.lean#L52)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
