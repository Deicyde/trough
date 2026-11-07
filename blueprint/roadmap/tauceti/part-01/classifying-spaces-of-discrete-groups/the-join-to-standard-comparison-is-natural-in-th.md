---
declaration: theorem
origin: cited
lean: MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality
statement: formalized
proof: formalized
---

# The join-to-standard comparison is natural in the group

Relabelling simplices before
forgetting their indices agrees with first forgetting indices and then relabelling the tuples.
This is an equality of chain maps in `Rep k G`, with target actions restricted along `φ`.

```lean
MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality.{u} {k G H : Type u} [Group G]
  [Group H] [CommRing k] (φ : G →* H) :
  CategoryTheory.CategoryStruct.comp φ.universalGSpaceChainMap
      (((Rep.resFunctor φ).mapHomologicalComplex (ComplexShape.down ℕ)).map
        (TauCeti.universalGSpaceChainComplexToStandardComplex k H)) =
    CategoryTheory.CategoryStruct.comp (TauCeti.universalGSpaceChainComplexToStandardComplex k G)
      φ.standardComplexMap
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Naturality.html#MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality).

## Sources

- [Tau Ceti documentation: `MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Naturality.html#MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality)
- [Source of `MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality` in TauCeti/AlgebraicTopology/ClassifyingSpace/Naturality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/Naturality.lean#L115)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
