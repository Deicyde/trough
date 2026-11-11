---
declaration: def
origin: cited
lean: TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet
statement: formalized
---

# The Dold–Kan description of the right mapping spaces of the differential graded nerve

For objects `X` and `Y` of a differential graded category, `Hom^R_{N_dg(C)}(X, Y)` is isomorphic
to `(cochainToSSet R).obj (dgHomComplex R X Y)`, the underlying simplicial set of the Dold–Kan
construction on the good truncation `τ_{≥ 0} Hom_C(X, Y)`.

```lean
TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet.{v, u} {R : Type v} [CommRing R] {C : Type u}
  [TauCeti.DGCategory R C] (X Y : C) :
  ((TauCeti.dgNerve R C).rightMappingSpace ((TauCeti.dgNerveEquiv R C).symm X)
        ((TauCeti.dgNerveEquiv R C).symm Y)).toSSet ≅
    SSet.uliftFunctor.obj ((TauCeti.cochainToSSet R).obj (TauCeti.dgHomComplex R X Y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGNerve/RightMappingSpace.html#TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet).

## Sources

- [Tau Ceti documentation: `TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGNerve/RightMappingSpace.html#TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet)
- [Source of `TauCeti.dgNerve.rightMappingSpaceIsoCochainToSSet` in TauCeti/AlgebraicTopology/DGNerve/RightMappingSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/DGNerve/RightMappingSpace.lean#L939)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
