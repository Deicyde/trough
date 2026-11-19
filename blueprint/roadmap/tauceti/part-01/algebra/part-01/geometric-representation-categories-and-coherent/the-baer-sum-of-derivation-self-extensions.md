---
declaration: theorem
origin: cited
lean: TauCeti.DerivationExtension.extClass_baerSum
statement: formalized
proof: formalized
---

# The Baer sum of derivation self-extensions

The Baer sum of `E_δ(M)` and `E_η(M)`, the
pushout along the codiagonal of their pullback along the diagonal, has the native `Ext¹` class
of `E_(δ + η)(M)`.

```lean
TauCeti.DerivationExtension.extClass_baerSum.{u, w, u_1} {R : Type u_1} [CommRing R] {A : Type u}
  [Ring A] [Algebra R A] [TopologicalSpace A] {δ η : ↥(TauCeti.derivationLieAlgebra R A)}
  [SeparatelyContinuousAdd A] (hδ : Continuous ⇑↑δ) (hη : Continuous ⇑↑η)
  (hδη : Continuous ⇑↑(δ + η)) (M : (TauCeti.discreteModules A).FullSubcategory) :
  ⋯.extClass = TauCeti.DerivationExtension.extClass hδη M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [CategoryTheory.ShortComplex.ShortExact.extClass_baerSum](categorytheory-shortcomplex-shortexact-extclass.md)
- [TauCeti.enoughInjectives_smoothModules](../affine-lie-algebras-smooth-modules-and-completed/tauceti-enoughinjectives-smoothmodules.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DerivationExtension.extClass_baerSum`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/BaerSum.html#TauCeti.DerivationExtension.extClass_baerSum).

## Sources

- [Tau Ceti documentation: `TauCeti.DerivationExtension.extClass_baerSum`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/BaerSum.html#TauCeti.DerivationExtension.extClass_baerSum)
- [Source of `TauCeti.DerivationExtension.extClass_baerSum` in TauCeti/Algebra/Category/ModuleCat/DerivationExtension/BaerSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/BaerSum.lean#L211)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
