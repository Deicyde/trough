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
- [Source of `AbstractMeasure.completedGroupAlgebraEquiv` in TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.lean#L447)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
