---
declaration: section
origin: cited
lean: Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction, Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction_unit_fac, Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction_counit_fac, Stacks.Cohomology.DerivedPushforwardComposition.isIso_derivedPushforwardComparison_unconditional, Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap, Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap_adjoint, Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap_comp, Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap_comp_horizontal
statement: formalized
proof: formalized
---

# 20.28 Cohomology of unbounded complexes

Section 20.28 of the Stacks Project, [Tag 079V](https://stacks.math.columbia.edu/tag/079V). 7 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 079W, a lemma

[Tag 079W](https://stacks.math.columbia.edu/tag/079W) in the Stacks Project.

**`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean#L255). The attribute's comment: “derived adjunction”. References: SGA 4 XVII (2.3.7), “ringed spaces case”.

> **The adjunction `Lf^* ⊣ Rf_*`** on the unbounded derived categories of sheaves of modules
> over ringed spaces, for an arbitrary morphism of ringed spaces.

```lean
def derivedAdjunction : derivedPullback f ⊣ derivedPushforward f
```

**`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction_unit_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean#L263). The attribute's comment: “canonical unit”.

> The derived unit agrees with the ordinary unit after applying the canonical comparison
> maps.

```lean
theorem derivedAdjunction_unit_fac
    (M : HomotopyCategory (SheafOfModules.{u} (structureSheafRing Y)) (ComplexShape.up ℤ)) :
    (derivedAdjunction f).unit.app (DerivedCategory.Qh.obj M) ≫
        (derivedPushforward f).map ((derivedPullbackComparison f).app M) =
      DerivedCategory.Qh.map ((homotopyPullbackPushforwardAdjunction f).unit.app M) ≫
        (derivedPushforwardUnit f).app
          (((modulePullback f).mapHomotopyCategory (ComplexShape.up ℤ)).obj M)
```

**`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction_counit_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean#L278). The attribute's comment: “canonical counit”.

> The derived counit agrees with the ordinary counit after applying the canonical comparison
> maps.

```lean
theorem derivedAdjunction_counit_fac
    (K : HomotopyCategory (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)) :
    (derivedPullback f).map ((derivedPushforwardUnit f).app K) ≫
        (derivedAdjunction f).counit.app (DerivedCategory.Qh.obj K) =
      (derivedPullbackComparison f).app
          (((modulePushforward f).mapHomotopyCategory (ComplexShape.up ℤ)).obj K) ≫
        DerivedCategory.Qh.map
          ((homotopyPullbackPushforwardAdjunction f).counit.app K)
```

## Tag 0D5T, a lemma

[Tag 0D5T](https://stacks.math.columbia.edu/tag/0D5T) in the Stacks Project.

**`Stacks.Cohomology.DerivedPushforwardComposition.isIso_derivedPushforwardComparison_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CompositionUnconditional.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/CompositionUnconditional.lean#L473).

> **Stacks 0D5T.**  For composable morphisms `f : X ⟶ Y` and `g : Y ⟶ Z` of ringed spaces, the
> canonical comparison from a right derived pushforward along `f ≫ g` to the composite of right
> derived pushforwards along `f` and `g` is an isomorphism.
>
> No hypothesis beyond the two morphisms and the three derived functors: the condition
> `PushforwardComputesDerived`, which `isIso_derivedPushforwardComparison_iff` shows to be
> equivalent to this statement, is discharged by `pushforwardComputesDerived`.

```lean
theorem isIso_derivedPushforwardComparison_unconditional
    [Rf.IsRightDerivedFunctor αf
      (HomotopyCategory.quasiIso (ModuleSheaves.{u} X) (ComplexShape.up ℤ))]
    [Rg.IsRightDerivedFunctor αg
      (HomotopyCategory.quasiIso (ModuleSheaves.{u} Y) (ComplexShape.up ℤ))]
    [Rgf.IsRightDerivedFunctor αgf
      (HomotopyCategory.quasiIso (ModuleSheaves.{u} X) (ComplexShape.up ℤ))] :
    IsIso (derivedPushforwardComparison f g Rf Rg Rgf αf αg αgf)
```

## Tag 08HY, a remark

[Tag 08HY](https://stacks.math.columbia.edu/tag/08HY) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangeMap.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangeMap.lean#L286). The attribute's comment: “derived\_base\_change\_map”. References: SGA 4 XVII (4.1.5), “ringed spaces”; SGA 4 XVII (4.1.4), “ringed spaces case”.

> **The derived base change map** `Lg^* (Rf_* K) ⟶ Rf'_* (Lg'^* K)` of a commutative square
> of ringed spaces, at an object of the unbounded derived category.  It is adjoint to the derived
> pullback along `g'` of the derived counit `Lf^* (Rf_* K) ⟶ K`, after identifying the two
> iterated derived pullbacks.

```lean
def derivedBaseChangeMap (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g).obj
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K) ⟶
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f').obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g').obj K)
```

**`Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap_adjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangeMap.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangeMap.lean#L299). The attribute's comment: “adjoint characterization of the canonical map”.

> Under the derived adjunction `Lf'^* ⊣ Rf'_*`, the base change map is the derived pullback
> of the counit, transported across the two composition isomorphisms.

```lean
theorem derivedBaseChangeMap_adjoint
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction f').homEquiv
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g).obj
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K))
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g').obj K)).symm
        (derivedBaseChangeMap g' f' f g sq K) =
      (derivedPullbackCompIsoLeft g' f' f g sq).hom.app
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K) ≫
        (derivedPullbackCompIsoCanonical g' f).inv.app
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K) ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback g').map
          ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction f).counit.app K)
```

## Tag 0ATL, a remark

[Tag 0ATL](https://stacks.math.columbia.edu/tag/0ATL) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangePasting.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangePasting.lean#L590).

> **Tag 0ATL.**  Derived base change for an outer rectangle is the composite of derived base
> change for its two constituent squares.
>
> For two vertically composable commutative squares of ringed spaces, the composite of the derived
> pullback along the lower horizontal morphism of the inverse composition isomorphism of Tag 079W,
> the derived base change map of the lower square, the derived pushforward along the upper
> square's right-hand vertical of the derived base change map of the upper square, and the
> composition isomorphism of Tag 079W for the rectangle's left-hand verticals, is the derived base
> change map of the rectangle.

```lean
theorem derivedBaseChangeMap_comp (sq₁ : k ≫ f = f' ≫ l) (sq₂ : l ≫ g = g' ≫ m)
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    (derivedPullback m).map ((derivedPushforwardCompIso f g).inv.app K) ≫
        derivedBaseChangeMap l g' g m sq₂ ((derivedPushforward f).obj K) ≫
        (derivedPushforward g').map (derivedBaseChangeMap k f' f l sq₁ K) ≫
        (derivedPushforwardCompIso f' g').hom.app ((derivedPullback k).obj K) =
      derivedBaseChangeMap k (f' ≫ g') (f ≫ g) m (comp_square k f' f l g' g m sq₁ sq₂) K
```

## Tag 0ATM, a remark

[Tag 0ATM](https://stacks.math.columbia.edu/tag/0ATM) in the Stacks Project.

**`Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap_comp_horizontal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangePasting.lean, line 846](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/BaseChangePasting.lean#L846).

> **Tag 0ATM.**  Derived base change for an outer rectangle is the composite of derived base
> change for its two constituent squares.
>
> For two horizontally composable commutative squares of ringed spaces, the composite of the
> inverse composition isomorphism of Tag 0D5S for `h' ≫ h`, the derived pullback along `h'` of the
> derived base change map of the right-hand square, the derived base change map of the left-hand
> square, and the derived pushforward along `f''` of the composition isomorphism of Tag 0D5S for
> `g' ≫ g`, is the derived base change map of the rectangle.

```lean
theorem derivedBaseChangeMap_comp_horizontal (sq₁ : g ≫ f = f' ≫ h)
    (sq₂ : g' ≫ f' = f'' ≫ h')
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    (derivedPullbackCompIsoCanonical h' h).inv.app ((derivedPushforward f).obj K) ≫
        (derivedPullback h').map (derivedBaseChangeMap g f' f h sq₁ K) ≫
        derivedBaseChangeMap g' f'' f' h' sq₂ ((derivedPullback g).obj K) ≫
        (derivedPushforward f'').map ((derivedPullbackCompIsoCanonical g' g).hom.app K) =
      derivedBaseChangeMap (g' ≫ g) f'' f (h' ≫ h)
        (hcomp_square g' g f'' f' f h' h sq₁ sq₂) K
```

## Tag 0FP1, a lemma

[Tag 0FP1](https://stacks.math.columbia.edu/tag/0FP1) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedAdjunction_counit_fac`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/AdjunctionUnconditional.lean#L278), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/OrdinaryAndDerivedCounit.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/OrdinaryAndDerivedCounit.lean#L38) (StacksFrontier): “the square of the ordinary and the derived counit commutes”.

## Tag 0B68, a remark

[Tag 0B68](https://stacks.math.columbia.edu/tag/0B68) in the Stacks Project.

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean#L173).

> **The relative cup product** `Rf_*K ⊗^L_{𝒪_Y} Rf_*M ⟶ Rf_*(K ⊗^L_{𝒪_X} M)`: the adjoint
> transpose of the derived pullback-tensor comparison of Stacks 079U followed by the counit of
> `Lf^* ⊣ Rf_*` in both tensor factors.  It is defined for arbitrary `K, M ∈ D(𝒪_X)`.

```lean
def relativeCupProduct
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K)).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj M) ⟶
      (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj
        (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).obj K).obj M)
```

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean#L227). The attribute's comment: “naturality in both complexes”.

> The relative cup product is natural in both derived modules on the source.

```lean
theorem relativeCupProduct_natural
    {K K' M M' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (k : K ⟶ K') (m : M ⟶ M') :
    (Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf)).map
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map k ×ₘ
          (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map m) ≫
        relativeCupProduct f K' M' =
      relativeCupProduct f K M ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          ((Functor.uncurry.obj
            (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf)).map
              (k ×ₘ m))
```

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean#L250). The attribute's comment: “naturality in the first complex”.

> The relative cup product is natural in the first derived module.

```lean
theorem relativeCupProduct_natural_left
    {K K' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (k : K ⟶ K')
    (M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf).map
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map k)).app
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj M) ≫
        relativeCupProduct f K' M =
      relativeCupProduct f K M ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).map k).app M)
```

**`Stacks.Cohomology.DerivedRelativeCupProduct.relativeCupProduct_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/RelativeCupProduct.lean#L271). The attribute's comment: “naturality in the second complex”.

> The relative cup product is natural in the second derived module.

```lean
theorem relativeCupProduct_natural_right
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    {M M' : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    (m : M ⟶ M') :
    ((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.sheaf).obj
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).obj K)).map
        ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map m) ≫
        relativeCupProduct f K M' =
      relativeCupProduct f K M ≫
        (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPushforward f).map
          (((Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.sheaf).obj K).map m)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.28, Tag 079V](https://stacks.math.columbia.edu/tag/079V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
