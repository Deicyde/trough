---
declaration: theorem
origin: cited
lean: TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal
statement: formalized
proof: formalized
---

# TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal

After identifying tensor-induced trivial `𝔽₂` coefficients with the ambient trivial
coefficient object, the class of an invariant diagonal cocycle does not depend on the transversal.

```lean
TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal.{v} (G : Type v) [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (U : Subgroup G) (hU : IsOpen ↑U)
  (s t : U.LeftTransversal) [U.FiniteIndex] [CompactSpace ↥U] [Fintype (G ⧸ U)] {n : ℕ}
  (z : (TauCeti.trivialF2 ↥U).gradedResolutionModule)
  (hz : z ∈ (TauCeti.trivialF2 ↥U).gradedResolutionPiece ↑n)
  (hinv : ∀ (u : ↥U), ((TauCeti.trivialF2 ↥U).gradedResolutionTopRep.ρ u) z = z)
  (hdz : (TauCeti.trivialF2 ↥U).gradedResolutionDifferential z = 0) :
  (CategoryTheory.ConcreteCategory.hom
        (TauCeti.ContinuousCohomology.coeffMap
          (TauCeti.smoothTensorInducedTrivialF2Iso G U hU t).hom.hom (Fintype.card (G ⧸ U) * n)))
      (TauCeti.smoothTensorInducedDiagonalClass U hU t
        { obj := TauCeti.trivialF2 ↥U, property := ⋯ } ⋯ z hz hinv hdz) =
    (CategoryTheory.ConcreteCategory.hom
        (TauCeti.ContinuousCohomology.coeffMap
          (TauCeti.smoothTensorInducedTrivialF2Iso G U hU s).hom.hom (Fintype.card (G ⧸ U) * n)))
      (TauCeti.smoothTensorInducedDiagonalClass U hU s
        { obj := TauCeti.trivialF2 ↥U, property := ⋯ } ⋯ z hz hinv hdz)
```

## Depends on

- [The Evens norm of a cocycle](the-evens-norm-of-a-cocycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Tensor/Induction/ChangeTransversal/Resolution.html#TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal).

## Sources

- [Tau Ceti documentation: `TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Tensor/Induction/ChangeTransversal/Resolution.html#TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal)
- [Source of `TauCeti.smoothTensorInducedDiagonalClass_trivialF2_changeTransversal` in TauCeti/RepresentationTheory/Tensor/Induction/ChangeTransversal/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Tensor/Induction/ChangeTransversal/Resolution.lean#L247)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
