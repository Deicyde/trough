---
declaration: def
origin: cited
lean: AbstractMeasure.completedGroupAlgebraEquiv
statement: formalized
---

# Integral measures are the completed group algebra

The canonical algebra equivalence
between integral measures on a profinite group and its completed group algebra.

```lean
AbstractMeasure.completedGroupAlgebraEquiv.{u_1} {Γ : Type u_1} [Group Γ] [TopologicalSpace Γ]
  [CompactSpace Γ] [IsTopologicalGroup Γ] {p : ℕ} [Fact (Nat.Prime p)]
  [TotallyDisconnectedSpace Γ] :
  AbstractMeasure Γ ℤ_[p] ℤ_[p] ≃ₐ[ℤ_[p]] TauCeti.completedGroupAlgebra ℤ_[p] Γ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.completedGroupAlgebraEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.html#AbstractMeasure.completedGroupAlgebraEquiv).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.completedGroupAlgebraEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.html#AbstractMeasure.completedGroupAlgebraEquiv)
- [Source of `AbstractMeasure.completedGroupAlgebraEquiv` in TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.lean#L446)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
