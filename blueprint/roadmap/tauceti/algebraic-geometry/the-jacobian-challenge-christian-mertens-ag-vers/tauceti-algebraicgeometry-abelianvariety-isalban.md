---
declaration: structure
origin: cited
lean: TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese
statement: formalized
---

# TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese

A pointed morphism `a : X ⟶ J.toOver` from a scheme `X` over `K` with a `K`-rational point
`x₀` to an abelian variety `J` has the **Albanese property** if every morphism `f : X ⟶ A.toOver`
to an abelian variety sending `x₀` to the identity factors as `f = a ≫ φ` through a unique
homomorphism `φ : J ⟶ A` of abelian varieties.

```lean
TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese.{u} {K : Type u} [Field K]
  {X : CategoryTheory.Over (AlgebraicGeometry.Spec ↧K)}
  (x₀ :
    CategoryTheory.MonoidalCategoryStruct.tensorUnit
        (CategoryTheory.Over (AlgebraicGeometry.Spec ↧K)) ⟶
      X)
  {J : TauCeti.AlgebraicGeometry.AbelianVariety K} (a : X ⟶ J.toOver) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AbelianVariety/Albanese.html#TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AbelianVariety/Albanese.html#TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese)
- [Source of `TauCeti.AlgebraicGeometry.AbelianVariety.IsAlbanese` in TauCeti/AlgebraicGeometry/AbelianVariety/Albanese.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AbelianVariety/Albanese.lean#L89)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
