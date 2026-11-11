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
- [Source of `MonoidHom.universalGSpaceChainComplexToStandardComplex_naturality` in TauCeti/AlgebraicTopology/ClassifyingSpace/Naturality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/ClassifyingSpace/Naturality.lean#L115)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
