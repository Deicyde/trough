---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det
statement: formalized
---

# TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det

The **determinant** `det E = ⋀^{rank E} E` of a finite locally free sheaf `E`: over each open
set where `E` has rank `n` it is the top exterior power `⋀ⁿ E`. It has rank `(rank E).choose
(rank E) = 1` everywhere, so it is an invertible sheaf.

```lean
TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det.{u} {X : AlgebraicGeometry.Scheme}
  (E : TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf X) :
  TauCeti.AlgebraicGeometry.InvertibleSheaf X
```

## Depends on

- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](tauceti-algebraicgeometry-finitelocallyfreesheaf-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/LocallyConstantRank.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/LocallyConstantRank.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det)
- [Source of `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det` in TauCeti/AlgebraicGeometry/VectorBundle/Determinant/LocallyConstantRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/LocallyConstantRank.lean#L59)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
