---
declaration: def
origin: cited
lean: TauCeti.DerivationExtension.outerExtClass
statement: formalized
---

# The extension class map of continuous outer derivations

the center-linear map
`OutDer_cont(A) → Ext¹(M, M)` sending the outer class of a continuous derivation `δ` to the class
of the self-extension `E_δ(M)` in the category of discrete modules. It is well defined because an
inner change `δ ↦ δ + ad b` does not change the class. The center acts on Ext through its
canonical scalar action on the category of discrete modules.

```lean
TauCeti.DerivationExtension.outerExtClass.{u, w, u_1} (R : Type u_1) [CommRing R] {A : Type u}
  [Ring A] [Algebra R A] [TopologicalSpace A] [IsTopologicalAddGroup A] [SeparatelyContinuousMul A]
  [ContinuousConstSMul R A] (M : (TauCeti.discreteModules A).FullSubcategory) :
  TauCeti.ContinuousOuterDerivation R A →ₗ[↥(Subalgebra.center R A)]
    CategoryTheory.Abelian.Ext M M 1
```

## Depends on

- [The continuous outer derivations `OutDer_cont(A)`](the-continuous-outer-derivations-outder-cont-a.md)

## Proof depends on

- [TauCeti.enoughInjectives_smoothModules](../affine-lie-algebras-smooth-modules-and-completed/tauceti-enoughinjectives-smoothmodules.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DerivationExtension.outerExtClass`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.html#TauCeti.DerivationExtension.outerExtClass).

## Sources

- [Tau Ceti documentation: `TauCeti.DerivationExtension.outerExtClass`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.html#TauCeti.DerivationExtension.outerExtClass)
- [Source of `TauCeti.DerivationExtension.outerExtClass` in TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.lean#L221)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
