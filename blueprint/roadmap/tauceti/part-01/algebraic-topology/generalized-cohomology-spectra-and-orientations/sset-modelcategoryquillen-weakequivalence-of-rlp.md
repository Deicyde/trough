---
declaration: theorem
origin: cited
lean: SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms
statement: formalized
proof: formalized
---

# SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms

A morphism with the right lifting property with respect to all monomorphisms, that is, a
trivial fibration of the Kan–Quillen model structure, is a weak equivalence.

```lean
SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms.{u} {X Y : _root_.SSet} {p : X ⟶ Y}
  (hp : (CategoryTheory.MorphismProperty.monomorphisms _root_.SSet).rlp p) :
  HomotopicalAlgebra.WeakEquivalence p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/PrismRealization.html#SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms).

## Sources

- [Tau Ceti documentation: `SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/PrismRealization.html#SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms)
- [Source of `SSet.modelCategoryQuillen.weakEquivalence_of_rlp_monomorphisms` in TauCeti/AlgebraicTopology/SimplicialSet/PrismRealization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/SimplicialSet/PrismRealization.lean#L615)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
