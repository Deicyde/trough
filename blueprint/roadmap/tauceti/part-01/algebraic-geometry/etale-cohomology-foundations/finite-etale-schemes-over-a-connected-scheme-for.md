---
declaration: theorem
origin: cited
lean: TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat
statement: formalized
proof: formalized
---

# Finite étale schemes over a connected scheme form a Galois category

A fibre functor is
the geometric fibre at an algebraic closure of a residue field.

```lean
TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat.{u}
  {S : AlgebraicGeometry.Scheme} [ConnectedSpace ↥S] :
  CategoryTheory.GaloisCategory (TauCeti.FiniteEtaleScheme S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.html#TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.html#TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat)
- [Source of `TauCeti.FiniteEtaleScheme.instGaloisCategoryOfConnectedSpaceCarrierCarrierCommRingCat` in TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.lean#L109)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
