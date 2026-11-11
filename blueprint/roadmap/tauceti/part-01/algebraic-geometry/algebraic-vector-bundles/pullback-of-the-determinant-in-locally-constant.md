---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso
statement: formalized
---

# Pullback of the determinant in locally constant rank

For a morphism of schemes
`f : X ⟶ Y` and a finite locally free sheaf `E` on `Y`, the pullback of `det E = ⋀^{rank E} E`
is the determinant of `f^* E`. The forward map is the exterior-power comparison
`f^* (⋀^{rank E} E) ⟶ ⋀^{rank E ∘ f} (f^* E)`, an isomorphism because `E` is quasicoherent,
followed by the identification `rank (f^* E) = rank E ∘ f`.

```lean
TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso.{u} {X Y : AlgebraicGeometry.Scheme}
  (f : X ⟶ Y) (E : TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf Y) :
  (TauCeti.AlgebraicGeometry.InvertibleSheaf.pullback f).obj E.det ≅
    ((TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullback f).obj E).det
```

## Depends on

- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](tauceti-algebraicgeometry-finitelocallyfreesheaf-2.md)
- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.det](tauceti-algebraicgeometry-finitelocallyfreesheaf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.html#TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso)
- [Source of `TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf.pullbackDetIso` in TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/VectorBundle/Determinant/Pullback.lean#L151)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
