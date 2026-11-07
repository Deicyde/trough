---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso
statement: formalized
---

# TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso

The identity functor on finite locally free sheaves is naturally isomorphic to
internal-Hom dualization applied twice.

```lean
TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso.{u} {X : AlgebraicGeometry.Scheme} :
  CategoryTheory.Functor.id (TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf X) ≅
    TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.dualFunctor.rightOp.comp
      TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.dualFunctor
```

## Depends on

- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](tauceti-algebraicgeometry-finitelocallyfreesheaf-3.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Dual/Bidual.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Dual/Bidual.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso)
- [Source of `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.evalNatIso` in TauCeti/AlgebraicGeometry/VectorBundle/Dual/Bidual.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/VectorBundle/Dual/Bidual.lean#L89)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
