---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigFppfOver.isSheaf_sectionsPresheafOfModules_baseOverTopology, AlgebraicGeometry.BigFppfOver.baseAssociatedSheafIsoPiPullback, AlgebraicGeometry.BigFppfOver.baseAssociatedSheafIsoAPullback, AlgebraicGeometry.BigFppfOver.pushforward_baseAssociatedSheaf, AlgebraicGeometry.BigFppfOver.pushforward_smallEtaleAssociatedSheaf, AlgebraicGeometry.BigFppfOver.isZero_rightDerived_epsilonPushforward, AlgebraicGeometry.BigFppfOver.isZero_rightDerived_aPushforward, AlgebraicGeometry.smallEtaleBigEtaleQuasicoherentEquivalence'
statement: formalized
proof: formalized
---

# 59.101 Comparing fppf and étale topologies: modules

Section 59.101 of the Stacks Project, [Tag 0DEV](https://stacks.math.columbia.edu/tag/0DEV). 3 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DEW, a lemma

[Tag 0DEW](https://stacks.math.columbia.edu/tag/0DEW) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isSheaf_sectionsPresheafOfModules_baseOverTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean#L105). The attribute's comment: “clause (1) only: 𝓕ᵃ satisfies the sheaf condition for fppf and a fortiori étale coverings; 𝓕 on S\_étale is the associated module of a quasi-coherent module on the scheme S, the source's first reduction”.

> **Stacks 03DT on each of the five big sites of `S`.**  The pullback-sections presheaf of
> modules of a quasi-coherent module `F` on `S` is a sheaf for each of the five localized
> topologies, with no hypothesis.
>
> Each of the five topologies is coarser than the fppf one, so this is the fppf statement
> `AlgebraicGeometry.BigFppfOver.isSheaf_sectionsPresheafOfModules` — whose hypothesis is
> discharged by `AlgebraicGeometry.fpqcDescentOfQuasicoherentHoms` — read through
> `CategoryTheory.Presheaf.IsSheaf.of_le`.

```lean
public theorem isSheaf_sectionsPresheafOfModules_baseOverTopology (τ : SiteKind)
    (F : S.Modules) [F.IsQuasicoherent] :
    Presheaf.IsSheaf (baseOverTopology B S hS τ)
      (sectionsPresheafOfModules B S hS F).presheaf
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedSheafIsoPiPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPullback.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPullback.lean#L274). The attribute's comment: “clause (2) only: 𝓕ᵃ = π\_S^*𝓕 on (Sch/S)\_étale, with 𝓕 on S\_étale the associated module of a quasi-coherent module on the scheme S as in the source's first reduction”.

> **Stacks 0DEW, clause (2).**  On `(Sch/S)_étale` the associated module `𝓕ᵃ` of a
> quasi-coherent module is the inverse image `π_S^*𝓕` of its associated module on `S_étale`, along
> the morphism of ringed sites `π_S : ((Sch/S)_étale, 𝒪) ⟶ (S_étale, 𝒪)`.

```lean
public def baseAssociatedSheafIsoPiPullback :
    (smallEtaleToBaseModulePullback B S hS .etale).obj (smallEtaleAssociatedSheaf B S hS F) ≅
      baseAssociatedSheaf B S hS F .etale
```

**`AlgebraicGeometry.BigFppfOver.baseAssociatedSheafIsoAPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPullback.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPullback.lean#L284). The attribute's comment: “clause (3) only: 𝓕ᵃ = a\_S^*𝓕 on (Sch/S)\_fppf, with 𝓕 on S\_étale the associated module of a quasi-coherent module on the scheme S as in the source's first reduction”.

> **Stacks 0DEW, clause (3).**  On `(Sch/S)_fppf` the associated module `𝓕ᵃ` of a
> quasi-coherent module is the inverse image `a_S^*𝓕` of its associated module on `S_étale`, along
> the morphism of ringed sites `a_S : ((Sch/S)_fppf, 𝒪) ⟶ (S_étale, 𝒪)`.

```lean
public def baseAssociatedSheafIsoAPullback :
    (SheafOfModules.pullback.{u} (aStructureMap B S hS)).obj
        (smallEtaleAssociatedSheaf B S hS F) ≅
      baseAssociatedSheaf B S hS F .fppf
```

**`AlgebraicGeometry.BigFppfOver.pushforward_baseAssociatedSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean#L253). The attribute's comment: “clause (6), first half, as documented above”.

> **Stacks 0DEW, clause (6), first half.**  The direct image along
> `ε_S : ((Sch/S)_fppf, 𝒪) ⟶ ((Sch/S)_τ, 𝒪)` of the associated module `𝓕ᵃ = a_S^*𝓕` is the
> associated module `𝓕ᵃ = π_S^*𝓕` of the big `τ`-site; at `τ = étale` this is
> `ε_{S,*}a_S^*𝓕 = π_S^*𝓕`.
>
> Both sides are the presheaf `(f : T → S) ↦ Γ(T, f⁺𝓕)` of Stacks 03DS with its two sheaf
> conditions, and the direct image along the identity functor is restriction of sections along
> it.

```lean
public theorem pushforward_baseAssociatedSheaf (τ : SiteKind) :
    (epsilonPushforward B S hS τ).obj (baseAssociatedSheaf B S hS F .fppf) =
      baseAssociatedSheaf B S hS F τ
```

**`AlgebraicGeometry.BigFppfOver.pushforward_smallEtaleAssociatedSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean#L313). The attribute's comment: “clause (6), second half, as documented above”.

> **Stacks 0DEW, clause (6), second half.**  The direct image along
> `a_S : ((Sch/S)_fppf, 𝒪) ⟶ (S_étale, 𝒪_S)` of the associated module `𝓕ᵃ = a_S^*𝓕` is `𝓕`
> itself, read on the small étale site as its own associated module: `a_{S,*}a_S^*𝓕 = 𝓕`.
>
> Both sides are the presheaf `(f : T → S) ↦ Γ(T, f⁺𝓕)` of Stacks 03DS, the right-hand side
> restricted along the inclusion of the small étale site, and the direct image is exactly that
> restriction.

```lean
public theorem pushforward_smallEtaleAssociatedSheaf :
    (aPushforward B S hS).obj (baseAssociatedSheaf B S hS F .fppf) =
      smallEtaleAssociatedSheaf B S hS F
```

**`AlgebraicGeometry.BigFppfOver.isZero_rightDerived_epsilonPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean#L419). The attribute's comment: “clause (7), first half, as documented above”.

> **Stacks 0DEW, clause (7), first half.**  The higher direct images along
> `ε_S : ((Sch/S)_fppf, 𝒪) ⟶ ((Sch/S)_étale, 𝒪)` of the associated module `𝓕ᵃ = a_S^*𝓕` vanish:
> `R^p ε_{S,*}(a_S^*𝓕) = 0` for `p > 0`.
>
> Every object of the big site is covered étale-locally by objects with affine total space, and
> there the fppf cohomology of `𝓕ᵃ` vanishes in positive degrees by [Stacks, Tag 03P2]; so the
> module-valued criterion
> `Stacks.Cohomology.ModuleDirectImageOnACover.isZero_rightDerived_pushforward_of_presieve`
> applies.

```lean
public theorem isZero_rightDerived_epsilonPushforward (p : ℕ) (hp : 0 < p) :
    IsZero (((epsilonPushforward B S hS .etale).rightDerived p).obj
      (baseAssociatedSheaf B S hS F .fppf))
```

**`AlgebraicGeometry.BigFppfOver.isZero_rightDerived_aPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean#L475). The attribute's comment: “clause (7), second half, as documented above”.

> **Stacks 0DEW, clause (7), second half.**  The higher direct images along
> `a_S : ((Sch/S)_fppf, 𝒪) ⟶ (S_étale, 𝒪_S)` of the associated module `𝓕ᵃ = a_S^*𝓕` vanish:
> `R^p a_{S,*}(a_S^*𝓕) = 0` for `p > 0`.
>
> Every object of the small étale site is covered by its affine objects (Stacks 04HR), and over an
> object of the big site with affine total space the fppf cohomology of `𝓕ᵃ` vanishes in positive
> degrees by [Stacks, Tag 03P2].

```lean
public theorem isZero_rightDerived_aPushforward (p : ℕ) (hp : 0 < p) :
    IsZero (((aPushforward B S hS).rightDerived p).obj
      (baseAssociatedSheaf B S hS F .fppf))
```

**`AlgebraicGeometry.smallEtaleBigEtaleQuasicoherentEquivalence'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSmallEtaleBigSite.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSmallEtaleBigSite.lean#L273). The attribute's comment: “clause (4): 𝓕 ↦ 𝓕ᵃ is an equivalence between QCoh(S\_étale, 𝒪) and QCoh((Sch/S)\_étale, 𝒪)”.

> **Stacks 0DEW, clause (4).**  The rule `𝓕 ↦ 𝓕^a` is an equivalence between the
> quasi-coherent `𝒪_S`-modules on `S_étale` and the quasi-coherent modules on
> `((Sch/S)_étale, 𝒪)`.
>
> The source's proof of this clause cites Descent, Proposition 03DX twice, and both citations are
> theorems of this library.  The small-étale one is
> `AlgebraicGeometry.SmallEtale.quasicoherentIsEssImageAssociatedModule`; the big-site one at
> `τ = étale` is `AlgebraicGeometry.BigFppfOver.baseQuasicoherentIsEssImageAssociatedModule`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseEssentialSurjectivity.lean`).

```lean
public noncomputable def smallEtaleBigEtaleQuasicoherentEquivalence'
    (BE : BigEtaleSite.{u}) (BF : BigFppfSite.{u}) (S : Scheme.{u})
    (hE : BE.Contains S) (hF : BF.Contains S) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (SmallEtale.structureSheaf BE S hE)).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.baseRingStructureSheaf BF S hF .etale)).FullSubcategory
```

**`AlgebraicGeometry.smallEtaleBigFppfQuasicoherentEquivalence'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSmallEtaleBigSite.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/QuasiCoherentSmallEtaleBigSite.lean#L310). The attribute's comment: “clause (5): 𝓕 ↦ 𝓕ᵃ is an equivalence between QCoh(S\_étale, 𝒪) and QCoh((Sch/S)\_fppf, 𝒪)”.

> **Stacks 0DEW, clause (5).**  The rule `𝓕 ↦ 𝓕^a` is an equivalence between the
> quasi-coherent `𝒪_S`-modules on `S_étale` and the quasi-coherent modules on
> `((Sch/S)_fppf, 𝒪)`.
>
> The source's proof of this clause cites Descent, Proposition 03DX twice, and both citations are
> theorems of this library.  The small-étale one is
> `AlgebraicGeometry.SmallEtale.quasicoherentIsEssImageAssociatedModule`; the big-site one, at
> `τ = fppf`, is `AlgebraicGeometry.BigFppfOver.quasicoherentIsEssImageAssociatedModule'`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/EffectiveGlueAgreementTransport.lean`
> `:512`).  The equivalence used below is the `τ`-indexed one, whose essential surjectivity is
> `AlgebraicGeometry.BigFppfOver.baseQuasicoherentIsEssImageAssociatedModule`; that theorem is
> proved by reducing the `τ` case to this `fppf` one.

```lean
public noncomputable def smallEtaleBigFppfQuasicoherentEquivalence'
    (BE : BigEtaleSite.{u}) (BF : BigFppfSite.{u}) (S : Scheme.{u})
    (hE : BE.Contains S) (hF : BF.Contains S) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (SmallEtale.structureSheaf BE S hE)).FullSubcategory ≌
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.baseRingStructureSheaf BF S hF .fppf)).FullSubcategory
```

## Tag 0DEX, a lemma

[Tag 0DEX](https://stacks.math.columbia.edu/tag/0DEX) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.rightAcyclic_epsilonPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean#L510). The attribute's comment: “first half, as documented above”.

> **Stacks 0DEX, first half.**  The canonical map
> `π_S^*𝓕 = ε_{S,*}(a_S^*𝓕) ⟶ Rε_{S,*}(a_S^*𝓕)` is an isomorphism, that is, `a_S^*𝓕` is right
> acyclic for `ε_{S,*}`.
>
> This is the criterion of [Stacks, Tag 015C] applied to clauses (6) and (7) of
> [Stacks, Tag 0DEW]: clause (6) identifies the source of the map with `π_S^*𝓕`
> (`pushforward_baseAssociatedSheaf`, an equality), and clause (7) supplies the vanishing of the
> higher direct images, which is what right acyclicity amounts to for a left exact functor.

```lean
public theorem rightAcyclic_epsilonPushforward :
    (SheafOfModules.pushforward (F := 𝟭 (BigFppfOver B S hS))
        (epsilonStructureMap B S hS .etale)).rightAcyclic
      (baseAssociatedSheaf B S hS F .fppf)
```

**`AlgebraicGeometry.BigFppfOver.rightAcyclic_aPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FppfEtaleComparison/QuasiCoherentPushforward.lean#L531). The attribute's comment: “second half, as documented above”.

> **Stacks 0DEX, second half.**  The canonical map
> `𝓕 = a_{S,*}(a_S^*𝓕) ⟶ Ra_{S,*}(a_S^*𝓕)` is an isomorphism, that is, `a_S^*𝓕` is right acyclic
> for `a_{S,*}`.
>
> Clause (6) of [Stacks, Tag 0DEW] identifies the source of the map with `𝓕` itself
> (`pushforward_smallEtaleAssociatedSheaf`, an equality), and clause (7) supplies the vanishing of
> the higher direct images.

```lean
public theorem rightAcyclic_aPushforward :
    (SheafOfModules.pushforward (F := smallEtaleToFppf B S hS)
        (aStructureMap B S hS)).rightAcyclic
      (baseAssociatedSheaf B S hS F .fppf)
```

## Tag 0H0U, a lemma

[Tag 0H0U](https://stacks.math.columbia.edu/tag/0H0U) in the Stacks Project.

**`AlgebraicGeometry.BigAffineFppf.isIso_derivedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeDerived.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeDerived.lean#L787). The attribute's comment: “the canonical map to derived global sections is a quasi-isomorphism”.

> **Stacks 0H0U.** For a complex `M^•` of `A`-modules the canonical map
> `M^• ⟶ RΓ((Aff/S)_fppf, F^•)` is a quasi-isomorphism, where `F^•` is the complex of sheaves of
> `𝒪`-modules `U ↦ M^• ⊗_A Γ(U, 𝒪_U)` on the big affine fppf site of `S = Spec A`.

```lean
public theorem isIso_derivedComparison
    (RGamma : DerivedCategory (SheafOfModules.{u} (structureSheaf B A hS)) ⥤
      DerivedCategory (ModuleCat.{u} A))
    (unit : homotopyGlobalSections B A hS ⟶ DerivedCategory.Qh ⋙ RGamma)
    (hRGamma : RGamma.IsRightDerivedFunctor unit
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheaf B A hS))
        (ComplexShape.up ℤ)))
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    IsIso (derivedComparison B A hS RGamma unit M)
```

**`AlgebraicGeometry.BigAffineFppf.isIso_derivedComparison_totalRightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeDerivedExistence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeDerivedExistence.lean#L123). The attribute's comment: “the canonical map M^• ⟶ RΓ((Aff/S)\_fppf, F^•) is a quasi-isomorphism, for the canonical total right derived functor of global sections -- no derived-functor parameter assumed”.

> **Stacks 0H0U for the canonical derived functor.** The conclusion of
> `AlgebraicGeometry.BigAffineFppf.isIso_derivedComparison` with no derived-functor parameter
> left: for the total right derived functor of global sections supplied by
> `CategoryTheory.Functor.totalRightDerived`, the canonical map
> `M^• ⟶ RΓ((Aff/S)_fppf, F^•)` is a quasi-isomorphism.

```lean
public theorem isIso_derivedComparison_totalRightDerived
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    IsIso (derivedComparison B A hS
      ((homotopyGlobalSections B A hS).totalRightDerived DerivedCategory.Qh
        (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheaf B A hS))
          (ComplexShape.up ℤ)))
      ((homotopyGlobalSections B A hS).totalRightDerivedUnit DerivedCategory.Qh
        (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheaf B A hS))
          (ComplexShape.up ℤ))) M)
```

**`AlgebraicGeometry.BigAffineFppf.baseChangePresheaf_map_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeModule.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeModule.lean#L179). The attribute's comment: “the rule is a presheaf of modules”.

> **Stacks 0H0U.** Restriction in the base-change presheaf is semilinear over restriction of
> functions: the rule `U ↦ M ⊗_A Γ(U, 𝒪_U)` is a presheaf of `𝒪`-modules.

```lean
public theorem baseChangePresheaf_map_smul (M : ModuleCat.{u} A)
    ⦃X Y : (BigAffineFppf B (Spec A) hS)ᵒᵖ⦄ (φ : X ⟶ Y)
    (r : (Stacks.Sites.structurePresheaf (Spec A) (toOver B A hS)).obj X)
    (m : (baseChangePresheaf B A hS M).obj X) :
    (baseChangePresheaf B A hS M).map φ (r • m) =
        (Stacks.Sites.structurePresheaf (Spec A) (toOver B A hS)).map φ r •
        (baseChangePresheaf B A hS M).map φ m
```

**`AlgebraicGeometry.BigAffineFppf.baseChangePresheaf_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeModule.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeModule.lean#L600). The attribute's comment: “the rule is a complex of modules, not only of presheaves of modules”.

> **Stacks 0H0U.** Each term of the rule `U ↦ M ⊗_A Γ(U, 𝒪_U)` is a sheaf: a complex of
> `A`-modules gives a complex of modules, not merely a complex of presheaves of modules.

```lean
public theorem baseChangePresheaf_isSheaf (M : ModuleCat.{u} A) :
    Presheaf.IsSheaf (affineTopology B A hS) (baseChangePresheaf B A hS M)
```

**`AlgebraicGeometry.BigAffineFppf.baseChangeComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeModule.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/AffineBaseChangeModule.lean#L636). The attribute's comment: “the displayed rule on a complex is a complex of modules”.

> **Stacks 0H0U.** The complex `F^•` of sheaves of `𝒪`-modules attached to a complex `M^•`
> of `A`-modules: in degree `n` it is the rule `U ↦ M^n ⊗_A Γ(U, 𝒪_U)`, with the base changes of
> the differentials of `M^•`.

```lean
public abbrev baseChangeComplex : CochainComplex (ModuleCat.{u} A) ℤ ⥤
    CochainComplex (SheafOfModules.{u} (structureSheaf B A hS)) ℤ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.101, Tag 0DEV](https://stacks.math.columbia.edu/tag/0DEV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
