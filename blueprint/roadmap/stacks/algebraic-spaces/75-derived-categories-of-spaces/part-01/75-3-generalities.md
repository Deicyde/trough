---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.derivedModulePushforwardEtaleRestrictIso, AlgebraicGeometry.Space.derivedModulePushforwardEtaleRestrictIsoOfIsEtale, AlgebraicGeometry.Space.CohomologySupportedOn
statement: formalized
proof: formalized
---

# 75.3 Generalities

Section 75.3 of the Stacks Project, [Tag 08GD](https://stacks.math.columbia.edu/tag/08GD). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08GE, a lemma

[Tag 08GE](https://stacks.math.columbia.edu/tag/08GE) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedModulePushforwardEtaleRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardEtaleRestriction.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardEtaleRestriction.lean#L227).

> **Stacks 08GE.**  Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of algebraic spaces over
> `S`, let `g : Y' ⟶ Y` be an étale morphism, set `X' = Y' ×_Y X` and let `f' : X' ⟶ Y'` be the
> projection.  Then restricting the unbounded derived direct image along `g` agrees with taking the
> derived direct image along `f'` after restricting along `i`:
> `(Rf_*E)|_{Y'} ≅ Rf'_*(E|_{X'})` for `E` in `D(𝒪_X)`.
>
> The four derived functors are arbitrary choices equipped with their canonical units, so the
> result applies in particular to the standard `Rf_*` of
> `AlgebraicGeometry.Space.hasRightDerivedFunctor_modulePushforward` and to the exact restriction
> functors.  Extension by zero along `i` enters as data, for the reason recorded in the
> implementation notes of this file and in Stacks 08HA; it is the only such input, because on the
> `Rf ⋙ Rg` side exactness of restriction along `g` already makes the comparison invertible.

```lean
def derivedModulePushforwardEtaleRestrictIso (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom)
    {iShriek : Modules.{u, u} B S hS X'.1 X'.2 ⥤ Modules.{u, u} B S hS X.1 X.2}
    (adji : iShriek ⊣ etaleModulePullback.{u, u} B S hS i
      (isEtale_of_isPullback B S hS f' i g f sq.flip hg))
    [iShriek.Additive] [PreservesFiniteLimits iShriek] [PreservesFiniteColimits iShriek]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS X.1 X.2)]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS Y.1 Y.2)]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS X'.1 X'.2)]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS Y'.1 Y'.2)]
    (Rf : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
    (Rf' : DerivedCategory (Modules.{u, u} B S hS X'.1 X'.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y'.1 Y'.2))
    (Ri : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS X'.1 X'.2))
    (Rg : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y'.1 Y'.2))
    (αf : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : (modulePushforward B S hS f').mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    (αi : (etaleModulePullback.{u, u} B S hS i
          (isEtale_of_isPullback B S hS f' i g f sq.flip hg)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Ri)
    (αg : (etaleModulePullback.{u, u} B S hS g hg).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rg)
    [Rf.IsRightDerivedFunctor αf
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))]
    [Rf'.IsRightDerivedFunctor αf'
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X'.1 X'.2) (ComplexShape.up ℤ))]
    [Ri.IsRightDerivedFunctor αi
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS Y.1 Y.2) (ComplexShape.up ℤ))] :
    Rf ⋙ Rg ≅ Ri ⋙ Rf'
```

**`AlgebraicGeometry.Space.derivedModulePushforwardEtaleRestrictIsoOfIsEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardEtaleRestrictionNoShriekData.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedPushforwardEtaleRestrictionNoShriekData.lean#L61).

> Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let
> `g : Y' ⟶ Y` be an étale morphism, set `X' = Y' ×_Y X` (the square `sq` is cartesian) and let
> `f' : X' ⟶ Y'` be the projection. Then `(Rf_*E)|_{Y'} ≅ Rf'_*(E|_{X'})` naturally in `E ∈ D(𝒪_X)`,
> where `Rf`, `Rf'`, `Ri` and `Rg` are any right derived functors of the direct images along `f`,
> `f'` and of the restrictions along `i`, `g`, with units `αf`, `αf'`, `αi` and `αg`.

```lean
def derivedModulePushforwardEtaleRestrictIsoOfIsEtale (sq : IsPullback i f' f g)
    (hg : IsEtale B S hS g.hom)
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS X.1 X.2)]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS Y.1 Y.2)]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS X'.1 X'.2)]
    [HasDerivedCategory.{u + 1} (Modules.{u, u} B S hS Y'.1 Y'.2)]
    (Rf : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2))
    (Rf' : DerivedCategory (Modules.{u, u} B S hS X'.1 X'.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y'.1 Y'.2))
    (Ri : DerivedCategory (Modules.{u, u} B S hS X.1 X.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS X'.1 X'.2))
    (Rg : DerivedCategory (Modules.{u, u} B S hS Y.1 Y.2) ⥤
      DerivedCategory (Modules.{u, u} B S hS Y'.1 Y'.2))
    (αf : (modulePushforward B S hS f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf)
    (αf' : (modulePushforward B S hS f').mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rf')
    (αi : (etaleModulePullback.{u, u} B S hS i
          (isEtale_of_isPullback B S hS f' i g f sq.flip hg)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Ri)
    (αg : (etaleModulePullback.{u, u} B S hS g hg).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rg)
    [Rf.IsRightDerivedFunctor αf
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))]
    [Rf'.IsRightDerivedFunctor αf'
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X'.1 X'.2) (ComplexShape.up ℤ))]
    [Ri.IsRightDerivedFunctor αi
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS X.1 X.2) (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg
      (HomotopyCategory.quasiIso (Modules.{u, u} B S hS Y.1 Y.2) (ComplexShape.up ℤ))] :
    Rf ⋙ Rg ≅ Ri ⋙ Rf'
```

## Tag 08GF, a definition

[Tag 08GF](https://stacks.math.columbia.edu/tag/08GF) in the Stacks Project.

**`AlgebraicGeometry.Space.CohomologySupportedOn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedSupport.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DerivedSupport.lean#L77).

> **Stacks 08GF.** An object `E` of `D(𝒪_F)` is *supported on* a subset `T` of `|F|` when
> every one of its cohomology sheaves `Hⁱ(E)` is supported on `T`.

```lean
noncomputable abbrev CohomologySupportedOn
    [HasSheafify (smallEtaleRingedSite B S hS F hF).J AddCommGrpCat.{m}]
    [(smallEtaleRingedSite B S hS F hF).J.WEqualsLocallyBijective AddCommGrpCat.{m}]
    (T : Set (points B S hS F))
    (E : DerivedCategory (Modules.{u, m} B S hS F hF)) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.3, Tag 08GD](https://stacks.math.columbia.edu/tag/08GD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
