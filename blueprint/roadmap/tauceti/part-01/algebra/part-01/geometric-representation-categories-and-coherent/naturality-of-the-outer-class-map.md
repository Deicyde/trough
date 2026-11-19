---
declaration: theorem
origin: cited
lean: TauCeti.DerivationExtension.outerExtClass_naturality
statement: formalized
proof: formalized
---

# Naturality of the outer class map

for a map `f : M ⟶ N` of discrete modules and a
continuous outer derivation `x`, pushforward along `f` of the class of `x` for `M` equals pullback
along `f` of the class of `x` for `N`, in `Ext¹(M, N)`.

```lean
TauCeti.DerivationExtension.outerExtClass_naturality.{u, w, u_1} {R : Type u_1} [CommRing R]
  {A : Type u} [Ring A] [Algebra R A] [TopologicalSpace A] [IsTopologicalAddGroup A]
  [SeparatelyContinuousMul A] [ContinuousConstSMul R A]
  {M N : (TauCeti.discreteModules A).FullSubcategory} (f : M ⟶ N)
  (x : TauCeti.ContinuousOuterDerivation R A) :
  ((TauCeti.DerivationExtension.outerExtClass R M) x).comp (CategoryTheory.Abelian.Ext.mk₀ f) ⋯ =
    (CategoryTheory.Abelian.Ext.mk₀ f).comp ((TauCeti.DerivationExtension.outerExtClass R N) x) ⋯
```

## Depends on

- [The continuous outer derivations `OutDer_cont(A)`](the-continuous-outer-derivations-outder-cont-a.md)
- [The extension class map of continuous outer derivations](the-extension-class-map-of-continuous-outer-deri.md)

## Proof depends on

- [TauCeti.enoughInjectives_smoothModules](../affine-lie-algebras-smooth-modules-and-completed/tauceti-enoughinjectives-smoothmodules.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DerivationExtension.outerExtClass_naturality`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.html#TauCeti.DerivationExtension.outerExtClass_naturality).

## Sources

- [Tau Ceti documentation: `TauCeti.DerivationExtension.outerExtClass_naturality`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.html#TauCeti.DerivationExtension.outerExtClass_naturality)
- [Source of `TauCeti.DerivationExtension.outerExtClass_naturality` in TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/DerivationExtension/Outer.lean#L239)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
