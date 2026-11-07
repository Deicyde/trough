---
declaration: theorem
origin: cited
lean: TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass
statement: formalized
proof: formalized
---

# TauCeti.ContCohomology.smoothTensorInducedDiagonalClass\_eq\_graphClass

The tensor-induced class of the homogeneous degree-one cocycle of a continuous character is
the index-two graph class. The transversal has representatives `1` and `s`, and the coefficient
identification multiplies the two tensor factors. The equality includes only the transport of
degrees from `2` to `card (G ⧸ U) * 1`.

The quotient `Fintype` is a caller parameter: the diagonal class and its graded contraction use
that enumeration. The input `z` and its cocycle data are exactly the inputs of
`smoothTensorInducedDiagonalClass`; `hzα` identifies their explicit homogeneous representative.
The theorem compares the classes associated to this explicit homogeneous representative. The
statement installs local compactness from the compact open subgroup because the existing
`graphClass` requires it.

```lean
TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass.{u} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] (U : OpenSubgroup G) (hU : (↑U).index = 2) (s : G)
  (hs : s ∉ U) (α : ↥↑U →* Multiplicative (ZMod 2)) (hα : Continuous ⇑α) [Fintype (G ⧸ ↑U)]
  [CompactSpace ↥↑U] (z : (TauCeti.trivialF2 ↥↑U).gradedResolutionModule)
  (hz : z ∈ (TauCeti.trivialF2 ↥↑U).gradedResolutionPiece 1)
  (hinv : ∀ (x : ↥↑U), ((TauCeti.trivialF2 ↥↑U).gradedResolutionTopRep.ρ x) z = z)
  (hdz : (TauCeti.trivialF2 ↥↑U).gradedResolutionDifferential z = 0)
  (hzα :
    z =
      (DirectSum.lof ℤ ℕ (fun n => ↑((TauCeti.trivialF2 ↥↑U).resolutionX (n + 1))) 1)
        ↑(TauCeti.ContCohomology.inhomogeneousCochain1 (fun x => Multiplicative.toAdd (α x)) ⋯)) :
  have t := ⟨Set.range ((↑U).indexTwoTransversal s), ⋯⟩;
  let A := { obj := TauCeti.trivialF2 ↥↑U, property := ⋯ };
  (CategoryTheory.ConcreteCategory.hom
        (TauCeti.ContinuousCohomology.coeffMap
          (TauCeti.smoothTensorInducedTrivialF2Iso G ↑U ⋯ t).hom.hom (Fintype.card (G ⧸ ↑U) * 1)))
      (TauCeti.smoothTensorInducedDiagonalClass ↑U ⋯ t A ⋯ z hz hinv hdz) =
    (TopModuleCat.Hom.hom (CategoryTheory.eqToHom ⋯)) (TauCeti.ContCohomology.graphClass U hU α hα)
```

## Depends on

- [The Evens norm of a cocycle](the-evens-norm-of-a-cocycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/TensorInduction.html#TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/TensorInduction.html#TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass)
- [Source of `TauCeti.ContCohomology.smoothTensorInducedDiagonalClass_eq_graphClass` in TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/TensorInduction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/TensorInduction.lean#L527)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
