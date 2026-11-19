---
declaration: def
origin: cited
lean: CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph
statement: formalized
---

# CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph

The fat classifying space of a saturated open restriction is homeomorphic to the
actual coarse-map preimage, with its subspace topology.

```lean
CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph.{u} {C : Type u}
  [CategoryTheory.Category.{u, u} C] [CategoryTheory.IsGroupoid C] [TopologicalSpace C]
  [TopologicalSpace (Quiver.Total C)] (P : CategoryTheory.ObjectProperty C)
  [P.IsClosedUnderIsomorphisms] (hs : Continuous Quiver.Total.left) (hP : IsOpen {x | P x}) :
  ↑(TauCeti.fatClassifyingSpace P.FullSubcategory) ≃ₜ
    ↑(⇑(CategoryTheory.ConcreteCategory.hom (TauCeti.fatClassifyingSpace.coarseMap hs)) ⁻¹'
        Quotient.mk (CategoryTheory.isIsomorphicSetoid C) '' {x | P x})
```

## Depends on

- [TauCeti.fatClassifyingSpace](tauceti-fatclassifyingspace.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/CoarseSpace/Restrict.html#CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph).

## Sources

- [Tau Ceti documentation: `CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/CategoryTheory/CoarseSpace/Restrict.html#CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph)
- [Source of `CategoryTheory.ObjectProperty.fatClassifyingSpaceRestrictionHomeomorph` in TauCeti/Topology/CategoryTheory/CoarseSpace/Restrict.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/CategoryTheory/CoarseSpace/Restrict.lean#L125)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
