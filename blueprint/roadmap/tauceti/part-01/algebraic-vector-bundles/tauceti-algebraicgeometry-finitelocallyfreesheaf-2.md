---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso
statement: formalized
---

# TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso

Pulling back the determinant of a finite locally free sheaf of constant rank `r` is naturally
isomorphic to taking the determinant of its pullback: `f^* (det E) ≅ det (f^* E)`. The forward map
is the canonical exterior-power comparison `f^* (⋀ʳ E) ⟶ ⋀ʳ (f^* E)`, which is invertible because
`E` is quasicoherent.

```lean
TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso.{u}
  {X Y : AlgebraicGeometry.Scheme} (f : X ⟶ Y) (r : ℕ) :
  (TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.determinant Y r).comp
      (TauCeti.AlgebraicGeometry.InvertibleSheaf.pullback f) ≅
    (TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.FixedRank.pullback f).comp
      (TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.determinant X r)
```

## Depends on

- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](tauceti-algebraicgeometry-finitelocallyfreesheaf-3.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso)
- [Source of `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDeterminantIso` in TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.lean#L72)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
