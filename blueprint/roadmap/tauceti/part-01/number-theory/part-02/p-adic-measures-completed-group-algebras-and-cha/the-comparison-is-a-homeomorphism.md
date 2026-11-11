---
declaration: theorem
origin: cited
lean: AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak
statement: formalized
proof: formalized
---

# The comparison is a homeomorphism

For a profinite group `Γ`, the comparison of integral
measures with the completed group algebra `ℤ_p[[Γ]]` is a homeomorphism from the weak topology on
measures to the inverse-limit topology.

```lean
AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak.{u_1} {Γ : Type u_1} [Group Γ]
  [TopologicalSpace Γ] [CompactSpace Γ] [IsTopologicalGroup Γ] {p : ℕ} [Fact (Nat.Prime p)]
  [TotallyDisconnectedSpace Γ] : IsHomeomorph ⇑AbstractMeasure.toCompletedGroupAlgebra
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.html#AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.html#AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak)
- [Source of `AbstractMeasure.isHomeomorph_toCompletedGroupAlgebra_weak` in TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/CompletedGroupAlgebra.lean#L461)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
