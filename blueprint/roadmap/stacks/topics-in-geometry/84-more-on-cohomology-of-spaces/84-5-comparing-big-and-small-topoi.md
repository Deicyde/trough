---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageFactorizationIso, AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageFactorizationIso_hom_app, AlgebraicGeometry.BigEtaleSpaceSite.smallToBig_inverseImageSectionsIso, AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageSectionsIso, AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageSectionsIso_hom_app, AlgebraicGeometry.BigEtaleSpaceSite.inverseImage_isSheafFor_smooth_syntomic_fppf_fpqc, AlgebraicGeometry.BigPHSpaceSite.isSheaf_bigToSmallEtale_inverseImage, AlgebraicGeometry.BigEtaleSpaceSite.injective_smallEtaleRestriction
statement: formalized
proof: formalized
---

# 84.5 Comparing big and small topoi

Section 84.5 of the Stacks Project, [Tag 0DG6](https://stacks.math.columbia.edu/tag/0DG6). 7 tags here are carried by 39 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DG7, a lemma

[Tag 0DG7](https://stacks.math.columbia.edu/tag/0DG7) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageFactorizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean#L52). The attribute's comment: “transitivity of inverse image”.

> Transitivity of inverse image for `f_small = π_X ∘ i_f`: the adjunction mate of the
> direct-image factorization of Tag 0DF6, part (4).

```lean
noncomputable def bigToSmall_inverseImageFactorizationIso :
    (bigToSmallEtaleMorphism T X).inverseImage ⋙ (smallToBigEtaleMorphism T f).inverseImage ≅
      (smallEtaleMorphism T f).inverseImage
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageFactorizationIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean#L64). The attribute's comment: “the components of the transitivity isomorphism”.

> The transitivity isomorphism is determined by the adjunction unit of `f_small` and the
> direct-image factorization of Tag 0DF6: it is the morphism whose adjoint transpose is the unit
> followed by that factorization.

```lean
theorem bigToSmall_inverseImageFactorizationIso_hom_app
    (F : Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1))) :
    (bigToSmall_inverseImageFactorizationIso T f).hom.app F =
      (((bigToSmallEtaleMorphism T X).comp
        (smallToBigEtaleMorphism T f)).adj.homEquiv _ _).symm
        ((smallEtaleMorphism T f).adj.unit.app F ≫
          (smallEtale_pushforwardIsoDirectFactorization T f).hom.app
            ((smallEtaleMorphism T f).inverseImage.obj F))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.smallToBig_inverseImageSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean#L84). The attribute's comment: “global sections after restriction are evaluation at f”.

> Taking global sections on the spaces-étale site of `Y` after restriction along `i_f` is
> evaluation at the object `f : Y ⟶ X` of the big étale site of `X`.

```lean
noncomputable def smallToBig_inverseImageSectionsIso :
    (smallToBigEtaleMorphism T f).inverseImage ⋙
        Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1)) ≅
      (sheafSections (T.bigEtaleTopology X) (Type (u + 1))).obj (op (Over.mk f))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean#L132). The attribute's comment: “the section rule for the pullback”.

> The sections of the inverse image `π_X⁻¹F` of a sheaf on the spaces-étale site of `X` over the
> object `f : Y ⟶ X` of the big étale site of `X` are the global sections of the small-site pullback
> `f_small⁻¹F` on the spaces-étale site of `Y`, naturally in `F`.

```lean
noncomputable def bigToSmall_inverseImageSectionsIso :
    (bigToSmallEtaleMorphism T X).inverseImage ⋙
        (sheafSections (T.bigEtaleTopology X) (Type (u + 1))).obj (op (Over.mk f)) ≅
      (smallEtaleMorphism T f).inverseImage ⋙
        Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) (Type (u + 1))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImageSectionsIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtalePullback.lean#L146). The attribute's comment: “the components of the section rule”.

> The section rule is the global-sections image of the transitivity isomorphism, after
> identifying evaluation at `f` with global sections of the restriction along `i_f`.

```lean
theorem bigToSmall_inverseImageSectionsIso_hom_app
    (F : Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1))) :
    (bigToSmall_inverseImageSectionsIso T f).hom.app F =
      (smallToBig_inverseImageSectionsIso T f).inv.app
          ((bigToSmallEtaleMorphism T X).inverseImage.obj F) ≫
        (Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
          (Type (u + 1))).map ((bigToSmall_inverseImageFactorizationIso T f).hom.app F)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.inverseImage_isSheafFor_smooth_syntomic_fppf_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleSheafConditions.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleSheafConditions.lean#L73). The attribute's comment: “Moreover: the sheaf condition for smooth, syntomic, fppf and fpqc coverings”.

> **Stacks 0DG7, the sheaf conditions for smooth, syntomic, fppf and fpqc coverings.** Let `F`
> be a sheaf on the spaces-étale site of `X`. Then `π_X⁻¹F` satisfies the sheaf condition for
> every family of the slice over `X` whose underlying family of algebraic spaces is a smooth,
> syntomic, fppf or fpqc covering.

```lean
theorem inverseImage_isSheafFor_smooth_syntomic_fppf_fpqc :
    (∀ (U : Over X) (E : PreZeroHypercover.{v} U),
      Space.IsSmoothCovering T.fppfSite S T.fppf_mem
        (fun i ↦ ((E.map (Over.forget X)).X i).obj) (fun i ↦ ((E.map (Over.forget X)).f i).hom) →
      Presieve.IsSheafFor ((bigToSmallEtaleMorphism T X).inverseImage.obj F).obj E.presieve₀) ∧
    (∀ (U : Over X) (E : PreZeroHypercover.{v} U),
      Space.IsSyntomicCovering T.fppfSite S T.fppf_mem
        (fun i ↦ ((E.map (Over.forget X)).X i).obj) (fun i ↦ ((E.map (Over.forget X)).f i).hom) →
      Presieve.IsSheafFor ((bigToSmallEtaleMorphism T X).inverseImage.obj F).obj E.presieve₀) ∧
    (∀ (U : Over X) (E : PreZeroHypercover.{v} U),
      Space.IsFppfCovering T.fppfSite S T.fppf_mem
        (fun i ↦ ((E.map (Over.forget X)).X i).obj) (fun i ↦ ((E.map (Over.forget X)).f i).hom) →
      Presieve.IsSheafFor ((bigToSmallEtaleMorphism T X).inverseImage.obj F).obj E.presieve₀) ∧
    (∀ (U : Over X) (E : PreZeroHypercover.{v} U),
      Space.IsFpqcCovering T.fppfSite S T.fppf_mem (fun i ↦ ((E.map (Over.forget X)).f i).hom) →
      Presieve.IsSheafFor ((bigToSmallEtaleMorphism T X).inverseImage.obj F).obj E.presieve₀)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.BigPHSpaceSite.isSheaf_bigToSmallEtale_inverseImage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtalePullbackSheaf.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleSheafConditions.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleSheafConditions.lean#L104) (StacksFrontier): “Moreover: the sheaf condition for ph coverings”.

## Tag 0DG8, a lemma

[Tag 0DG8](https://stacks.math.columbia.edu/tag/0DG8) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.injective_smallEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean#L176). The attribute's comment: “part (1), injectives restrict along i\_f”.

> **Stacks 0DG8, part (1).** The inverse image along `i_f` of an injective abelian sheaf on
> the big étale site of `X` is an injective abelian sheaf on the spaces-étale site of `Y`.

```lean
theorem injective_smallEtaleRestriction {X Y : T.Spaces} (f : Y ⟶ X)
    (I : Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) [Injective I] :
    Injective ((smallEtaleRestriction T f).obj I)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.injective_bigToSmallEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean#L195). The attribute's comment: “part (1), injectives restrict to the small site”.

> **Stacks 0DG8, part (1).** The restriction to the spaces-étale site of `X` of an injective
> abelian sheaf on the big étale site of `X` is injective.

```lean
theorem injective_bigToSmallEtaleRestriction (X : T.Spaces)
    (I : Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) [Injective I] :
    Injective ((bigToSmallEtaleRestriction T X).obj I)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.isKInjective_smallEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean#L215). The attribute's comment: “part (2), K-injectivity restricts along i\_f”.

> **Stacks 0DG8, part (2).** The inverse image along `i_f` of a K-injective complex of
> abelian sheaves on the big étale site of `X` is a K-injective complex on the spaces-étale site
> of `Y`.

```lean
theorem isKInjective_smallEtaleRestriction {X Y : T.Spaces} (f : Y ⟶ X)
    (I : CochainComplex (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      (((smallEtaleRestriction T f).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.isKInjective_bigToSmallEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleRestriction.lean#L233). The attribute's comment: “part (2), K-injectivity restricts to the small site”.

> **Stacks 0DG8, part (2).** The restriction to the spaces-étale site of `X` of a K-injective
> complex of abelian sheaves on the big étale site of `X` is K-injective.

```lean
theorem isKInjective_bigToSmallEtaleRestriction (X : T.Spaces)
    (I : CochainComplex (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) ℤ) [I.IsKInjective] :
    ((bigToSmallEtaleRestrictionComplex T X).obj I).IsKInjective
```

**`AlgebraicGeometry.BigEtaleSpaceSite.injective_spacesEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean#L103). The attribute's comment: “injective\_restriction”.

> **Stacks Project, Tag 0DG8, part (1)(b).** Restriction of an injective abelian sheaf
> from the big étale site of `X` to the spaces-étale site of `X` is injective.

```lean
theorem injective_spacesEtaleRestriction (X : T.Spaces)
    (I : Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) [Injective I] :
    Injective
      (((Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X).sheafPushforwardContinuous
        Ab.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
        (T.bigEtaleTopology X)).obj I)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.injective_spacesEtaleRestrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean#L126). The attribute's comment: “injective\_pullback”.

> **Stacks Project, Tag 0DG8, part (1)(a).** Restriction of an injective abelian sheaf
> from the big étale site of `X` to the spaces-étale site of `Y` along a morphism
> `f : Y ⟶ X` — the inverse image of `i_f` — is injective.

```lean
theorem injective_spacesEtaleRestrictionAlong {X Y : T.Spaces} (f : Y ⟶ X)
    (I : Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) [Injective I] :
    Injective
      (((inclusionFunctor T f).sheafPushforwardContinuous Ab.{u + 1}
        (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        (T.bigEtaleTopology X)).obj I)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.isKInjective_spacesEtaleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean#L149). The attribute's comment: “kinjective\_restriction”.

> **Stacks Project, Tag 0DG8, part (2)(b).** Restriction of a K-injective complex of
> abelian sheaves from the big étale site of `X` to the spaces-étale site of `X` is
> K-injective.

```lean
theorem isKInjective_spacesEtaleRestriction (X : T.Spaces)
    (I : CochainComplex (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) ℤ)
    (hI : I.IsKInjective) :
    CochainComplex.IsKInjective
      ((((Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X).sheafPushforwardContinuous
        Ab.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
        (T.bigEtaleTopology X)).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.isKInjective_spacesEtaleRestrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigToSmallEtaleKInjective.lean#L177). The attribute's comment: “kinjective\_pullback”.

> **Stacks Project, Tag 0DG8, part (2)(a).** Restriction of a K-injective complex of
> abelian sheaves from the big étale site of `X` to the spaces-étale site of `Y` along a
> morphism `f : Y ⟶ X` — the inverse image of `i_f` — is K-injective.

```lean
theorem isKInjective_spacesEtaleRestrictionAlong {X Y : T.Spaces} (f : Y ⟶ X)
    (I : CochainComplex (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) ℤ)
    (hI : I.IsKInjective) :
    CochainComplex.IsKInjective
      ((((inclusionFunctor T f).sheafPushforwardContinuous Ab.{u + 1}
        (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        (T.bigEtaleTopology X)).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Tag 0DG9, an equation

[Tag 0DG9](https://stacks.math.columbia.edu/tag/0DG9) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigSmallEtale_restrictPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean#L255). The attribute's comment: “the comparison for sheaves of sets”.

> **Stacks 0DG9.** The restriction to the spaces-étale site of `X` of the big étale direct
> image along `f` is the small étale direct image along `f` of the restriction to the
> spaces-étale site of `Y`.

```lean
def bigSmallEtale_restrictPushforwardIso (f : Y ⟶ X) :
    (bigEtaleMorphism T f).pushforward ⋙ (bigToSmallEtaleMorphism T X).pushforward ≅
      (bigToSmallEtaleMorphism T Y).pushforward ⋙ (smallEtaleMorphism T f).pushforward
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigSmallEtale_restrictPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean#L263). The attribute's comment: “the comparison for sheaves of modules”.

> **Stacks 0DG9.** For a sheaf of `𝒪`-modules the comparison of the previous isomorphism is
> an isomorphism of `𝒪_X`-modules on the spaces-étale site of `X`.

```lean
def bigSmallEtale_restrictPushforwardModulesIso (f : Y ⟶ X) :
    bigEtaleModulePushforward.{u, m} T f ⋙ restrictModules.{u, m} T X ≅
      restrictModules.{u, m} T Y ⋙ smallEtaleModulePushforward.{u, m} T f
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigSmallEtale_restrictPushforwardModulesIso_hom_app_val_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardModules.lean#L275). The attribute's comment: “the comparison for sheaves of modules, on sections”.

> **Stacks 0DG9.** On sections over an algebraic space étale over `X`, the comparison of
> sheaves of modules is restriction along the comparison isomorphism of the two cartesian squares
> of Tag 0DF6.

```lean
theorem bigSmallEtale_restrictPushforwardModulesIso_hom_app_val_app (f : Y ⟶ X)
    (M : BigEtaleModules.{u, m} T Y)
    (U : (Space.SpacesEtale T.fppfSite S T.fppf_mem X)ᵒᵖ) (x) :
    ((bigSmallEtale_restrictPushforwardModulesIso.{u, m} T f).hom.app M).val.app U x =
      M.val.map ((smallBaseChange_comp_inclusionIso T f).hom.app U.unop).op x
```

## Tag 0DGA, a lemma

[Tag 0DGA](https://stacks.math.columbia.edu/tag/0DGA) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.derivedBigEtaleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean#L118). The attribute's comment: “big\_base\_change\_abelian”.

> For a cartesian square of algebraic spaces of the big étale site, the inverse image along
> `g_big` of the derived big étale direct image along `f` agrees naturally with the derived big
> étale direct image along `f'` of the inverse image along `g'_big`.

```lean
def derivedBigEtaleBaseChangeIso {X Y X' Y' : T.Spaces} (f : Y ⟶ X) (g : X' ⟶ X)
    (g' : Y' ⟶ Y) (f' : Y' ⟶ X') (h : IsPullback g' f' f g) :
    ((bigEtalePushforward T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology Y) Ab.{u + 1}) (ComplexShape.up ℤ)) ⋙
        (bigEtalePullback T g).mapDerivedCategory ≅
      (bigEtalePullback T g').mapDerivedCategory ⋙
        ((bigEtalePushforward T f').mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology Y') Ab.{u + 1}) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.derivedSmallEtaleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean#L159). The attribute's comment: “small\_base\_change\_abelian”.

> For a cartesian square of algebraic spaces of the big étale site, the restriction to the
> spaces-étale site of `X'` of the derived big étale direct image along `f` agrees naturally with
> the derived small étale direct image along `f'` of the restriction to the spaces-étale site of
> `Y'`. Both restrictions are the inverse image `i_g^{-1}` resp. `i_{g'}^{-1}` of Tag 0DF2,
> written as the inverse image along `g_big` resp. `g'_big` followed by restriction to the
> spaces-étale site.

```lean
def derivedSmallEtaleBaseChangeIso {X Y X' Y' : T.Spaces} (f : Y ⟶ X) (g : X' ⟶ X)
    (g' : Y' ⟶ Y) (f' : Y' ⟶ X') (h : IsPullback g' f' f g) :
    ((bigEtalePushforward T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology Y) Ab.{u + 1}) (ComplexShape.up ℤ)) ⋙
        (bigEtalePullback T g).mapDerivedCategory ⋙
          (spacesEtaleRestrictionAb T X').mapDerivedCategory ≅
      (bigEtalePullback T g').mapDerivedCategory ⋙
        (spacesEtaleRestrictionAb T Y').mapDerivedCategory ⋙
          ((smallEtalePushforward T f').mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
              (HomotopyCategory.quasiIso
                (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y')
                  Ab.{u + 1}) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.derivedBigEtaleModuleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean#L262). The attribute's comment: “big\_base\_change\_modules”.

> For a cartesian square of algebraic spaces of the big étale site, the inverse image of
> sheaves of `𝒪`-modules along `g_big` of the derived big étale direct image along `f` agrees
> naturally with the derived big étale direct image along `f'` of the inverse image along
> `g'_big`.

```lean
def derivedBigEtaleModuleBaseChangeIso {X Y X' Y' : T.Spaces} (f : Y ⟶ X) (g : X' ⟶ X)
    (g' : Y' ⟶ Y) (f' : Y' ⟶ X') (h : IsPullback g' f' f g) :
    (homotopyToDerived (bigEtaleRelocalizationPushforward T f)).totalRightDerived
          DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (SheafOfModules.{u + 1} ((globalRingSheaf T).over Y)) (ComplexShape.up ℤ)) ⋙
        (bigEtaleModulePullback T g).mapDerivedCategory ≅
      (bigEtaleModulePullback T g').mapDerivedCategory ⋙
        (homotopyToDerived (bigEtaleRelocalizationPushforward T f')).totalRightDerived
          DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (SheafOfModules.{u + 1} ((globalRingSheaf T).over Y')) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.derivedSmallEtaleModuleBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean, line 604](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedBaseChange.lean#L604). The attribute's comment: “small\_base\_change\_modules”.

> For a cartesian square of algebraic spaces of the big étale site, the restriction to the
> spaces-étale site of `X'` of the derived big étale direct image of sheaves of `𝒪`-modules along
> `f` agrees naturally with the derived small étale direct image along `f'` of the restriction to
> the spaces-étale site of `Y'`. The two restrictions are the inverse images `i_g^*` and
> `i_{g'}^*` of Tag 0DF2 on sheaves of `𝒪`-modules.

```lean
def derivedSmallEtaleModuleBaseChangeIso (f : Y ⟶ X) (g : X' ⟶ X) (g' : Y' ⟶ Y) (f' : Y' ⟶ X')
    (h : IsPullback g' f' f g) :
    derivedPushforward.{u + 1} (bigEtaleRingedSiteHom T f) ⋙
        (spacesEtaleRestrictionAlongRingedHom T g).pushforwardTopos.mapDerivedCategory ≅
      (spacesEtaleRestrictionAlongRingedHom T g').pushforwardTopos.mapDerivedCategory ⋙
        derivedPushforward.{u + 1} (smallEtaleRingedSiteHom T f')
```

**`AlgebraicGeometry.BigEtaleSpaceSite.derivedBigSmallEtalePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedPushforward.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedPushforward.lean#L292). The attribute's comment: “big\_small\_abelian”.

> **Derived direct image commutes with restriction to the small étale site.** Derived big-site
> direct image followed by restriction to the small étale site agrees naturally with restriction
> followed by derived small-site direct image.

```lean
public def derivedBigSmallEtalePushforwardIso :
    (((bigEtalePushforward T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (T.bigEtaleTopology Y) Ab.{u + 1})
          (ComplexShape.up ℤ))) ⋙
      ((Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem X).sheafPushforwardContinuous
        Ab.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
        (T.bigEtaleTopology X)).mapDerivedCategory ≅
    ((Space.SpacesEtale.inclusion T.fppfSite S T.fppf_mem Y).sheafPushforwardContinuous
        Ab.{u + 1} (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        (T.bigEtaleTopology Y)).mapDerivedCategory ⋙
      (((smallEtalePushforward T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
              Ab.{u + 1}) (ComplexShape.up ℤ)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.derivedBigSmallEtaleModulePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedPushforwardModules.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleDerivedPushforwardModules.lean#L323). The attribute's comment: “big\_small\_modules”.

> **Stacks Project, Tag 0DGA, part (2).** Derived big étale direct image of sheaves of
> `𝒪`-modules followed by restriction to the small étale site of `X` agrees naturally with
> restriction to the small étale site of `Y` followed by derived small étale direct image.

```lean
def derivedBigSmallEtaleModulePushforwardIso (f : Y ⟶ X) :
    derivedPushforward.{u + 1} (bigEtaleRingedSiteHom T f) ⋙
        (spacesEtaleRestrictionRingedHom T X).pushforwardTopos.mapDerivedCategory ≅
      (spacesEtaleRestrictionRingedHom T Y).pushforwardTopos.mapDerivedCategory ⋙
        derivedPushforward.{u + 1} (smallEtaleRingedSiteHom T f)
```

Declarations registered for the tag:

- [`Stacks.Cohomology.Localization.derivedOverPushforwardBaseChangeIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/AbelianSheavesOnALocalizedSite.lean#L682), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Simplicial/BigEtaleBaseChange.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/BigEtaleBaseChange.lean#L34) (StacksFrontier): “big\_base\_change\_abelian”.

## Tag 0DGB, a lemma

[Tag 0DGB](https://stacks.math.columbia.edu/tag/0DGB) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean#L176). The attribute's comment: “part (5), big-site cohomology over Y of a big complex”.

> Étale cohomology over `Y` of a complex of abelian sheaves on the big étale site of `X` is
> the cohomology on the spaces-étale site of `Y` of its restriction along `i_f`: the right-derived
> sections functor at `f : Y ⟶ X` is restriction followed by derived global sections, naturally in
> the derived coefficient object.

```lean
noncomputable def bigSmallEtaleCohomologyIso :
    (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ))) ≅
    ((smallEtaleRestriction T f).mapDerivedCategory ⋙
      (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
            (ComplexShape.up ℤ))))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigSmallEtaleCohomologyIsoAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean#L232). The attribute's comment: “part (5), in each degree”.

> In every degree, étale cohomology over `Y` of a complex on the big étale site of `X` agrees
> with the cohomology on the spaces-étale site of `Y` of its restriction along `i_f`.

```lean
noncomputable def bigSmallEtaleCohomologyIsoAt
    (M : DerivedCategory (Sheaf (T.bigEtaleTopology X) Ab.{u + 1})) (n : ℤ) :
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      ((((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ))).obj M) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((smallEtaleRestriction T f).mapDerivedCategory ⋙
        (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
          Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
              (ComplexShape.up ℤ)))).obj M)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.pulledSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean#L276). The attribute's comment: “part (3), cohomology of a pullback from the small site”.

> Étale cohomology over `Y` of a complex pulled back from the spaces-étale site of `X` to the
> big étale site of `X` is the cohomology on the spaces-étale site of `Y` of its pullback along
> `f_small`.

```lean
noncomputable def pulledSmallEtaleCohomologyIso :
    ((CategoryTheory.Sites.abelianInverseImage
      (bigToSmallEtaleMorphism T X)).mapDerivedCategory ⋙
      (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))) ≅
    ((CategoryTheory.Sites.abelianInverseImage
      (smallEtaleMorphism T f)).mapDerivedCategory ⋙
      (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
            (ComplexShape.up ℤ))))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.pulledSmallEtaleCohomologyIsoAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean#L300). The attribute's comment: “part (3), in each degree”.

> In every degree, étale cohomology over `Y` of a complex pulled back from the spaces-étale
> site of `X` agrees with the cohomology on the spaces-étale site of `Y` of its pullback along
> `f_small`.

```lean
noncomputable def pulledSmallEtaleCohomologyIsoAt
    (K : DerivedCategory
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})) (n : ℤ) :
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((CategoryTheory.Sites.abelianInverseImage
        (bigToSmallEtaleMorphism T X)).mapDerivedCategory ⋙
        (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))).obj K) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((CategoryTheory.Sites.abelianInverseImage
        (smallEtaleMorphism T f)).mapDerivedCategory ⋙
        (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
          Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
              (ComplexShape.up ℤ)))).obj K)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.overXSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean#L382). The attribute's comment: “part (1), cohomology over X of a pullback”.

> Étale cohomology over `X` of a complex pulled back from the spaces-étale site of `X` to the
> big étale site of `X` is its cohomology on the spaces-étale site of `X`.

```lean
noncomputable def overXSmallEtaleCohomologyIso :
    ((CategoryTheory.Sites.abelianInverseImage
      (bigToSmallEtaleMorphism T X)).mapDerivedCategory ⋙
      (((bigEtaleSections T (𝟙 X)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))) ≅
    (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
      Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso
          (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})
          (ComplexShape.up ℤ)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.overXSmallEtaleCohomologyIsoAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomology.lean#L402). The attribute's comment: “part (1), in each degree”.

> In every degree, étale cohomology over `X` of a complex pulled back from the spaces-étale
> site of `X` agrees with its small-site cohomology.

```lean
noncomputable def overXSmallEtaleCohomologyIsoAt
    (K : DerivedCategory
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})) (n : ℤ) :
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((CategoryTheory.Sites.abelianInverseImage
        (bigToSmallEtaleMorphism T X)).mapDerivedCategory ⋙
        (((bigEtaleSections T (𝟙 X)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))).obj K) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      ((((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
        Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})
            (ComplexShape.up ℤ))).obj K)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.moduleOverXSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModuleOverX.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModuleOverX.lean#L250). The attribute's comment: “part (2), cohomology over X of a derived pullback of modules from the small site”.

> **Stacks 0DGB, part (2).** Étale cohomology over `X` of the derived pullback `Lπ_X^*K` to
> the big étale site of `X` of a complex of sheaves of `𝒪_X`-modules on the spaces-étale site of
> `X` is the cohomology of `K` on that site, naturally in the derived coefficient object.

```lean
def moduleOverXSmallEtaleCohomologyIso :
    (derivedModulePullbackPi T X ⋙
      (SheafOfModules.toSheaf.{u + 1} (bigEtaleRingSheaf T X)).mapDerivedCategory ⋙
      (((bigEtaleSections T (𝟙 X)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))) ≅
    ((SheafOfModules.toSheaf.{u + 1} (spacesEtaleRingSheaf T X)).mapDerivedCategory ⋙
      (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
          Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})
              (ComplexShape.up ℤ))))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.moduleOverXSmallEtaleCohomologyIsoAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModuleOverX.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModuleOverX.lean#L272). The attribute's comment: “part (2), in each degree”.

> **Stacks 0DGB, part (2).** In every degree, étale cohomology over `X` of the derived
> pullback `Lπ_X^*K` of a complex of sheaves of `𝒪_X`-modules on the spaces-étale site of `X`
> agrees with the cohomology of `K` on that site.

```lean
def moduleOverXSmallEtaleCohomologyIsoAt
    (K : DerivedCategory (SpacesEtaleModules.{u, u + 1} T X)) (n : ℤ) :
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      ((derivedModulePullbackPi T X ⋙
        (SheafOfModules.toSheaf.{u + 1} (bigEtaleRingSheaf T X)).mapDerivedCategory ⋙
        (((bigEtaleSections T (𝟙 X)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))).obj K) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((SheafOfModules.toSheaf.{u + 1} (spacesEtaleRingSheaf T X)).mapDerivedCategory ⋙
        (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X)
            Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
              (HomotopyCategory.quasiIso
                (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})
                (ComplexShape.up ℤ)))).obj K)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.modulePulledSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModulePullback.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModulePullback.lean#L267). The attribute's comment: “part (4), cohomology over Y of a derived pullback from the small site”.

> Étale cohomology over `Y` of the derived pullback `Lπ_X^*K` of a complex of sheaves of
> `𝒪_X`-modules on the spaces-étale site of `X` is naturally isomorphic to the cohomology on the
> spaces-étale site of `Y` of `Lf_small^*K`, as total right derived functors.

```lean
noncomputable def modulePulledSmallEtaleCohomologyIso :
    (derivedModulePullbackPi T X ⋙
      (SheafOfModules.toSheaf.{u + 1} (bigEtaleRingSheaf T X)).mapDerivedCategory ⋙
      (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))) ≅
    (derivedModulePullbackSmallEtale T f ⋙
      (SheafOfModules.toSheaf.{u + 1} (spacesEtaleRingSheaf T Y)).mapDerivedCategory ⋙
      (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
          Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
              (ComplexShape.up ℤ))))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.modulePulledSmallEtaleCohomologyIsoAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModulePullback.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModulePullback.lean#L290). The attribute's comment: “part (4), in each degree”.

> In every degree, étale cohomology over `Y` of the derived
> pullback `Lπ_X^*K` of a complex of sheaves of `𝒪_X`-modules on the spaces-étale site of `X`
> agrees with the cohomology on the spaces-étale site of `Y` of `Lf_small^*K`.

```lean
noncomputable def modulePulledSmallEtaleCohomologyIsoAt
    (K : DerivedCategory (SpacesEtaleModules.{u, u + 1} T X)) (n : ℤ) :
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      ((derivedModulePullbackPi T X ⋙
        (SheafOfModules.toSheaf.{u + 1} (bigEtaleRingSheaf T X)).mapDerivedCategory ⋙
        (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))).obj K) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      ((derivedModulePullbackSmallEtale T f ⋙
        (SheafOfModules.toSheaf.{u + 1} (spacesEtaleRingSheaf T Y)).mapDerivedCategory ⋙
        (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
            Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
            DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
              (HomotopyCategory.quasiIso
                (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
                (ComplexShape.up ℤ)))).obj K)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.moduleBigSmallEtaleCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModules.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModules.lean#L107). The attribute's comment: “part (6), big-site cohomology over Y of a complex of modules”.

> **Stacks 0DGB, part (6).** Étale cohomology over `Y` of a complex of sheaves of
> `𝒪`-modules on the big étale site of `X` is the cohomology on the spaces-étale site of `Y` of
> its inverse image along `i_f`: the right-derived sections functor at `f : Y ⟶ X` is `i_f^*`
> followed by derived global sections, naturally in the derived coefficient object.

```lean
noncomputable def moduleBigSmallEtaleCohomologyIso :
    ((SheafOfModules.toSheaf.{u + 1} (bigEtaleRingSheaf T X)).mapDerivedCategory ⋙
      (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))) ≅
    ((restrictModulesAlong T f).mapDerivedCategory ⋙
      (SheafOfModules.toSheaf.{u + 1} (spacesEtaleRingSheaf T Y)).mapDerivedCategory ⋙
      (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
        Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
          (HomotopyCategory.quasiIso
            (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
            (ComplexShape.up ℤ))))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.moduleBigSmallEtaleCohomologyIsoAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModules.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtaleCohomologyModules.lean#L130). The attribute's comment: “part (6), in each degree”.

> **Stacks 0DGB, part (6).** In every degree, étale cohomology over `Y` of a complex of
> sheaves of `𝒪`-modules on the big étale site of `X` agrees with the cohomology on the
> spaces-étale site of `Y` of its inverse image along `i_f`.

```lean
noncomputable def moduleBigSmallEtaleCohomologyIsoAt
    (M : DerivedCategory (BigEtaleModules.{u, u + 1} T X)) (n : ℤ) :
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((SheafOfModules.toSheaf.{u + 1} (bigEtaleRingSheaf T X)).mapDerivedCategory ⋙
        (((bigEtaleSections T f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (T.bigEtaleTopology X) Ab.{u + 1}) (ComplexShape.up ℤ)))).obj M) ≅
    (DerivedCategory.homologyFunctor Ab.{u + 1} n).obj
      (((restrictModulesAlong T f).mapDerivedCategory ⋙
        (SheafOfModules.toSheaf.{u + 1} (spacesEtaleRingSheaf T Y)).mapDerivedCategory ⋙
        (((Sheaf.Γ (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y)
          Ab.{u + 1}).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh).totalRightDerived DerivedCategory.Qh
            (HomotopyCategory.quasiIso
              (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})
              (ComplexShape.up ℤ)))).obj M)
```

## Tag 0DGC, a lemma

[Tag 0DGC](https://stacks.math.columbia.edu/tag/0DGC) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_inverseImage_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleCohomologicalDescent.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleCohomologicalDescent.lean#L88). The attribute's comment: “the composite is the identity, for sheaves of sets”.

> **Stacks 0DGC.** Restricting back to the spaces-étale site of `X` the inverse image of a
> sheaf of sets along `π_X` returns that sheaf: `π_{X,*} ∘ π_X⁻¹` is the identity functor.

```lean
noncomputable def bigToSmall_inverseImage_comp_pushforwardIso :
    (bigToSmallEtaleMorphism T X).inverseImage ⋙ (bigToSmallEtaleMorphism T X).pushforward ≅
      𝟭 (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmall_abelianInverseImage_comp_restrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleCohomologicalDescent.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleCohomologicalDescent.lean#L110). The attribute's comment: “the composite is the identity, for abelian sheaves”.

> **Stacks 0DGC.** The same composite identity for abelian sheaves: restricting the abelian
> inverse image along `π_X` back to the spaces-étale site of `X` returns the sheaf.

```lean
noncomputable def bigToSmall_abelianInverseImage_comp_restrictionIso :
    CategoryTheory.Sites.abelianInverseImage (bigToSmallEtaleMorphism T X) ⋙
        bigToSmallEtaleRestriction T X ≅
      𝟭 (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})
```

**`AlgebraicGeometry.BigEtaleSpaceSite.isIso_bigToSmallEtaleDerivedAdjunction_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleCohomologicalDescent.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/SmallEtaleCohomologicalDescent.lean#L144). The attribute's comment: “the derived unit is an isomorphism”.

> **Stacks 0DGC.** For every complex `K` on the spaces-étale site of `X` the canonical map
> `K ⟶ Rπ_{X,*}π_X⁻¹K` is an isomorphism.

```lean
theorem isIso_bigToSmallEtaleDerivedAdjunction_unit
    (K : DerivedCategory
      (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem X) Ab.{u + 1})) :
    IsIso ((bigToSmallEtaleDerivedAdjunction T X).unit.app K)
```

## Tag 0DGD, a lemma

[Tag 0DGD](https://stacks.math.columbia.edu/tag/0DGD) in the Stacks Project.

**`AlgebraicGeometry.BigEtaleSpaceSite.bigToSmallEtale_pushforward_baseChange_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardBaseChange.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigSmallEtalePushforwardBaseChange.lean#L114).

> **Stacks 0DGD.** Let `S` be a scheme and `f : Y ⟶ X` a proper morphism of algebraic spaces
> over `S` (objects of the big étale site `T` of algebraic spaces over `S`). Write
> `π_X : Sh((Spaces/X)_étale) ⟶ Sh(X_étale)` (`bigToSmallEtaleMorphism T X`) for the comparison
> of the big étale topos with the small étale topos `Sh(X_étale)` (the spaces-étale site of `X`).
> Then:
>
> 1. the canonical base change map `π_X⁻¹ ∘ f_{small,*} ⟶ f_{big,*} ∘ π_Y⁻¹` of functors from
>    sheaves of sets on `Y_étale` to sheaves of sets on `(Spaces/X)_étale`
>    (`bigToSmallEtaleBaseChange T f`; its target `f_{big,*}` is restriction along
>    `Y ×_X - : Spaces/X ⥤ Spaces/Y`) is an isomorphism;
> 2. for every `K` in `D⁺(Y_étale)` (`K.IsGE n` for some `n`) whose cohomology sheaves are torsion,
>    the canonical base change map `π_X⁻¹ R f_{small,*} K ⟶ R f_{big,*} π_Y⁻¹ K` of Stacks 07A7
>    (`bigToSmallEtaleDerivedBaseChange T f`, on the derived categories of abelian sheaves) is an
>    isomorphism;
> 3. if `f` is finite, the canonical base change map `π_X⁻¹ R f_{small,*} K ⟶ R f_{big,*} π_Y⁻¹ K`
>    is an isomorphism for every `K` in the unbounded derived category `D(Y_étale)`.

```lean
theorem bigToSmallEtale_pushforward_baseChange_of_isProper {X Y : T.Spaces} (f : Y ⟶ X)
    (hf : Space.IsProper T.fppfSite S T.fppf_mem f.hom) :
    IsIso (bigToSmallEtaleBaseChange T f) ∧
      (∀ (K : DerivedCategory
          (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1})) (n : ℤ),
        K.IsGE n → HasTorsionCohomology T K →
          IsIso ((bigToSmallEtaleDerivedBaseChange T f).app K)) ∧
      (Space.IsFinite T.fppfSite S T.fppf_mem f.hom →
        ∀ K : DerivedCategory
          (Sheaf (Space.SpacesEtale.topology T.fppfSite S T.fppf_mem Y) Ab.{u + 1}),
          IsIso ((bigToSmallEtaleDerivedBaseChange T f).app K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 84.5, Tag 0DG6](https://stacks.math.columbia.edu/tag/0DG6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
