---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.totalSpaceHomIso
statement: formalized
---

# The section-valued universal property of the total space

**The section-valued universal property of the total space**, natural in the vector bundle
`E` and in the scheme `T` over `X`: morphisms `T ⟶ 𝕍(E) = Spec_X (Sym E^∨)` over `X` correspond to
sections `𝒪_T ⟶ q^* E`. Its components are `totalSpaceHomEquiv`.

```lean
TauCeti.AlgebraicGeometry.totalSpaceHomIso.{u} (X : AlgebraicGeometry.Scheme) :
  (TauCeti.AlgebraicGeometry.totalSpaceScheme X).comp
      ((CategoryTheory.MorphismProperty.Over.forget @AlgebraicGeometry.IsAffineHom ⊤ X).comp
        CategoryTheory.yoneda) ≅
    TauCeti.AlgebraicGeometry.pullbackSectionsPresheaf X
```

## Depends on

- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](tauceti-algebraicgeometry-finitelocallyfreesheaf-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.totalSpaceHomIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/TotalSpace/FunctorOfPoints.html#TauCeti.AlgebraicGeometry.totalSpaceHomIso).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.totalSpaceHomIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/VectorBundle/TotalSpace/FunctorOfPoints.html#TauCeti.AlgebraicGeometry.totalSpaceHomIso)
- [Source of `TauCeti.AlgebraicGeometry.totalSpaceHomIso` in TauCeti/AlgebraicGeometry/VectorBundle/TotalSpace/FunctorOfPoints.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/VectorBundle/TotalSpace/FunctorOfPoints.lean#L180)
- [Tau Ceti roadmap status: Algebraic vector bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicVectorBundles/STATUS.md)
