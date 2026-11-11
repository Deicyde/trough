---
declaration: section
origin: cited
lean: RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sheafHomExactSupport, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.modulePushforwardSheafHomExactSupportIsoHomSheaf, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.modulePushforwardSheafHomExactSupportAdjunction, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.modulePushforwardSheafHomExactSupportAdjunction_counit_app, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv_apply, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv_naturality, RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv_restrict
statement: formalized
proof: formalized
---

# 48.9 Right adjoint of pushforward for closed immersions

Section 48.9 of the Stacks Project, [Tag 0A74](https://stacks.math.columbia.edu/tag/0A74). 8 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A75, a lemma

[Tag 0A75](https://stacks.math.columbia.edu/tag/0A75) in the Stacks Project.

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sheafHomExactSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean#L91). The attribute's comment: “the functor”.

> **Stacks Project, Tag 0A75 (the functor).** The sheaf Hom from `𝒪_Z` with exact support,
> regarded as a functor from `𝒪_X`-modules to `𝒪_Z`-modules.  It is the internal Hom
> `SheafHom_{𝒪_X}(i_* 𝒪_Z, -)`, which is annihilated by the kernel ideal and therefore descends
> to `Z`.

```lean
noncomputable def sheafHomExactSupport :
    SheafOfModules.{u} (structureSheafRing S.X) ⥤ SheafOfModules.{u} (structureSheafRing S.Z)
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.modulePushforwardSheafHomExactSupportIsoHomSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean#L99). The attribute's comment: “the internal Hom identification”.

> **Stacks Project, Tag 0A75 (the internal Hom identification).** After pushforward to `X`,
> sheaf Hom with exact support is naturally the internal Hom `SheafHom_{𝒪_X}(i_* 𝒪_Z, -)`,
> regarded as an `𝒪_X`-module.

```lean
noncomputable def modulePushforwardSheafHomExactSupportIsoHomSheaf :
    S.sheafHomExactSupport ⋙ modulePushforward S.i ≅
      homSheaf (structureSheafHom S.i) ⋙
        SheafOfModules.restrictScalars (structureSheafHom S.i)
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.modulePushforwardSheafHomExactSupportAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean#L110). The attribute's comment: “the adjunction”.

> **Stacks Project, Tag 0A75 (adjunction).** Pushforward from a closed quotient ringed
> subspace is left adjoint to sheaf Hom with exact support.

```lean
noncomputable def modulePushforwardSheafHomExactSupportAdjunction :
    modulePushforward S.i ⊣ S.sheafHomExactSupport
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.modulePushforwardSheafHomExactSupportAdjunction_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupport.lean#L117). The attribute's comment: “the counit is evaluation at one”.

> The counit of the exact-support adjunction is, under the internal Hom identification,
> evaluation of a local homomorphism at the section `1`.

```lean
theorem modulePushforwardSheafHomExactSupportAdjunction_counit_app
    (F : SheafOfModules.{u} (structureSheafRing S.X)) (U : Opens S.X)
    (s : ((modulePushforward S.i).obj (S.sheafHomExactSupport.obj F)).val.obj (op U)) :
    (S.modulePushforwardSheafHomExactSupportAdjunction.counit.app F).val.app (op U) s =
      Stacks.PresheafOfModules.CoextendScalars.invSecVal (structureSheafHom S.i).hom F.val (op U)
        ((S.modulePushforwardSheafHomExactSupportIsoHomSheaf.hom.app F).val.app (op U) s)
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean#L376). The attribute's comment: “the description of sections”.

> **Stacks Project, Tag 0A75 (sections).** If `V ⊆ Z` is the inverse image of `U ⊆ X`, sections
> over `V` of sheaf Hom with exact support are canonically the sections of `F` over `U` annihilated
> by the kernel ideal.  The map is `ψ ↦ ψ(1)|_U`.

```lean
noncomputable def sectionsSheafHomExactSupportEquiv (U : Opens S.X) (V : Opens S.Z)
    (hUV : (opensMap S.i).obj U = V) :
    ((S.sheafHomExactSupport.obj F).val.obj (op V) : Type u) ≃+
      S.sectionsLocallyAnnihilatedByKernelIdeal F U
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean#L408). The attribute's comment: “evaluation characterization of the description of sections”.

> **Stacks Project, Tag 0A75.** The section equivalence is the map induced by the adjunction
> counit; equivalently, after the internal Hom identification it evaluates a local homomorphism
> at `1`.

```lean
theorem sectionsSheafHomExactSupportEquiv_apply
    (F : SheafOfModules.{u} (structureSheafRing S.X)) (U : Opens S.X) (V : Opens S.Z)
    (hUV : (opensMap S.i).obj U = V)
    (s : (S.sheafHomExactSupport.obj F).val.obj (op V)) :
    (S.sectionsSheafHomExactSupportEquiv F U V hUV s).1 =
      (S.modulePushforwardSheafHomExactSupportAdjunction.counit.app F).val.app (op U)
        (by
          change (S.sheafHomExactSupport.obj F).val.obj
            (op ((opensMap S.i).obj U))
          exact hUV.symm ▸ s)
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean#L429). The attribute's comment: “naturality of the description of sections”.

> **Stacks Project, Tag 0A75.** The section identification for sheaf Hom with exact support is
> natural in the `𝒪_X`-module.

```lean
theorem sectionsSheafHomExactSupportEquiv_naturality
    {F G : SheafOfModules.{u} (structureSheafRing S.X)} (f : F ⟶ G)
    (U : Opens S.X) (V : Opens S.Z) (hUV : (opensMap S.i).obj U = V)
    (s : (S.sheafHomExactSupport.obj F).val.obj (op V)) :
    ((S.sectionsSheafHomExactSupportEquiv G U V hUV
      ((S.sheafHomExactSupport.map f).val.app (op V) s)).1) =
        f.val.app (op U) ((S.sectionsSheafHomExactSupportEquiv F U V hUV s).1)
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.sectionsSheafHomExactSupportEquiv_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Module/ExactSupportEquiv.lean#L446). The attribute's comment: “restriction naturality of the description of sections”.

> **Stacks Project, Tag 0A75.** The section identification commutes with restriction to a
> smaller open subset.

```lean
theorem sectionsSheafHomExactSupportEquiv_restrict
    (F : SheafOfModules.{u} (structureSheafRing S.X))
    (U U' : Opens S.X) (hUU' : U' ≤ U)
    (V V' : Opens S.Z) (hVV' : V' ≤ V)
    (hUV : (opensMap S.i).obj U = V) (hU'V' : (opensMap S.i).obj U' = V')
    (s : (S.sheafHomExactSupport.obj F).val.obj (op V)) :
    (S.sectionsSheafHomExactSupportEquiv F U' V' hU'V'
      ((S.sheafHomExactSupport.obj F).val.map (homOfLE hVV').op s)).1 =
        F.val.map (homOfLE hUU').op
          ((S.sectionsSheafHomExactSupportEquiv F U V hUV s).1)
```

## Tag 0A76, a lemma

[Tag 0A76](https://stacks.math.columbia.edu/tag/0A76) in the Stacks Project.

**`Stacks.Duality.LocallySmall.derivedModulePushforwardSheafHomExactSupportAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageLocallySmall.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageLocallySmall.lean#L200). The attribute's comment: “at the locally small derived categories, the model at which the direct-sum and Brown-representability statements about D(O\_X) have content; the standard-model form is RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardSheafHomExactSupportAdjunction, which is about a different pair of categories”.

> **Stacks Project, Tag 0A76, at the locally small derived categories.** Derived pushforward
> along a closed immersion of schemes, read as a closed quotient morphism of ringed spaces, is left
> adjoint to the right derived functor of sheaf Hom with exact support: `Ri_* ⊣ R ℰom(𝒪_Z, -)`.
>
> The abstract input `Stacks.DerivedFunctor.derivedAdjunction` is stated at a free
> `[HasDerivedCategory.{w} _]` binder, so the only thing the standard model was supplying is the
> model itself.

```lean
def derivedModulePushforwardSheafHomExactSupportAdjunction :
    (modulePushforward (closedQuotient i).i).mapDerivedCategory ⊣ derivedSheafHomExactSupport i
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardSheafHomExactSupportAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerived.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerived.lean#L110).

> **Stacks Project, Tag 0A76.** Derived pushforward along a closed quotient morphism of
> ringed spaces is left adjoint to the right derived functor of sheaf Hom with exact support:
> `Ri_* ⊣ R ℰom(𝒪_Z, -)`.

```lean
noncomputable def derivedModulePushforwardSheafHomExactSupportAdjunction :
    (modulePushforward S.i).mapDerivedCategory ⊣ S.derivedSheafHomExactSupport
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardSheafHomExactSupportAdjunction_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerived.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerived.lean#L119).

> **Stacks Project, Tag 0A76.** The unit of the derived adjunction is the one induced by the
> unit of the adjunction of [Stacks, Tag 0A75] and the two derived-functor comparison maps.

```lean
theorem derivedModulePushforwardSheafHomExactSupportAdjunction_unit_app
    (M : HomotopyCategory (SheafOfModules.{u} (structureSheafRing S.Z)) (ComplexShape.up ℤ)) :
    S.derivedModulePushforwardSheafHomExactSupportAdjunction.unit.app
          (DerivedCategory.Qh.obj M) ≫
        S.derivedSheafHomExactSupport.map
          ((modulePushforward S.i).mapDerivedCategoryFactorsh.hom.app M) =
      DerivedCategory.Qh.map
          ((Adjunction.mapHomotopyCategoryAdjunction
            S.modulePushforwardSheafHomExactSupportAdjunction (ComplexShape.up ℤ)).unit.app M) ≫
        S.derivedSheafHomExactSupportComparison.app
          (((modulePushforward S.i).mapHomotopyCategory (ComplexShape.up ℤ)).obj M)
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardSheafHomExactSupportAdjunction_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerived.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerived.lean#L136).

> **Stacks Project, Tag 0A76.** The counit of the derived adjunction is the one induced by
> the counit of the adjunction of [Stacks, Tag 0A75] and the two derived-functor comparison
> maps.

```lean
theorem derivedModulePushforwardSheafHomExactSupportAdjunction_counit_app
    (K : HomotopyCategory (SheafOfModules.{u} (structureSheafRing S.X)) (ComplexShape.up ℤ)) :
    (modulePushforward S.i).mapDerivedCategory.map
          (S.derivedSheafHomExactSupportComparison.app K) ≫
        S.derivedModulePushforwardSheafHomExactSupportAdjunction.counit.app
          (DerivedCategory.Qh.obj K) =
      (modulePushforward S.i).mapDerivedCategoryFactorsh.hom.app
          ((S.sheafHomExactSupport.mapHomotopyCategory (ComplexShape.up ℤ)).obj K) ≫
        DerivedCategory.Qh.map
          ((Adjunction.mapHomotopyCategoryAdjunction
            S.modulePushforwardSheafHomExactSupportAdjunction
              (ComplexShape.up ℤ)).counit.app K)
```

## Tag 0A77, a lemma

[Tag 0A77](https://stacks.math.columbia.edu/tag/0A77) in the Stacks Project.

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardDerivedSheafHomExactSupportIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHom.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHom.lean#L202).

> **Stacks Project, Tag 0A77.** For a closed quotient morphism `i : Z ⟶ X` of ringed spaces,
> derived pushforward of the right derived sheaf Hom with exact support is the right derived
> internal Hom from `i_* 𝒪_Z`:
>
> `Ri_* R ℰom(𝒪_Z, K) ≅ R ℰom_{𝒪_X}(i_* 𝒪_Z, K)` naturally in `K ∈ D(𝒪_X)`.
>
> Both sides are right derived functors — the left one because `i_*` is exact, so composing with
> it preserves the property — of the two functors identified on the homotopy category by
> `mapHomotopyCategoryPushforwardSheafHomExactSupportIso`, which is the underived identification
> of [Stacks, Tag 0A75]. The isomorphism is the induced one on right derived functors.

```lean
noncomputable def derivedModulePushforwardDerivedSheafHomExactSupportIso :
    S.derivedSheafHomExactSupport ⋙ (modulePushforward S.i).mapDerivedCategory ≅
      S.derivedHomSheafFromPushforwardStructureSheaf
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardDerivedSheafHomExactSupportIso_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHom.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHom.lean#L214). The attribute's comment: “compatibility of the isomorphism with the comparison maps”.

> **Stacks Project, Tag 0A77.** The isomorphism of [Stacks, Tag 0A77] is compatible with the
> comparison maps out of the homotopy category and with the underived identification of
> [Stacks, Tag 0A75].

```lean
theorem derivedModulePushforwardDerivedSheafHomExactSupportIso_fac :
    S.derivedModulePushforwardComparison ≫
        Functor.whiskerLeft DerivedCategory.Qh
          S.derivedModulePushforwardDerivedSheafHomExactSupportIso.hom =
      S.mapHomotopyCategoryPushforwardSheafHomExactSupportIso.hom ≫
        S.derivedHomSheafFromPushforwardStructureSheafComparison
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardDerivedSheafHomExactSupportIso_uniq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHom.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHom.lean#L240). The attribute's comment: “uniqueness of the isomorphism”.

> **Stacks Project, Tag 0A77.** The isomorphism of [Stacks, Tag 0A77] is the unique one
> compatible with the comparison maps out of the homotopy category.

```lean
theorem derivedModulePushforwardDerivedSheafHomExactSupportIso_uniq
    (e : S.derivedSheafHomExactSupport ⋙ (modulePushforward S.i).mapDerivedCategory ≅
      S.derivedHomSheafFromPushforwardStructureSheaf)
    (he : S.derivedModulePushforwardComparison ≫
        Functor.whiskerLeft DerivedCategory.Qh e.hom =
      S.mapHomotopyCategoryPushforwardSheafHomExactSupportIso.hom ≫
        S.derivedHomSheafFromPushforwardStructureSheafComparison) :
    e = S.derivedModulePushforwardDerivedSheafHomExactSupportIso
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedSheafHomExactSupportPushforwardNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHomBifunctor.lean, line 726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHomBifunctor.lean#L726). The attribute's comment: “via the derived internal Hom bifunctor”.

> **Stacks Project, Tag 0A77.** Derived sheaf Hom with exact support followed by derived
> pushforward is the derived internal Hom out of the derived pushforward of the structure sheaf of
> the closed subspace: `Ri_* R ℰom(𝒪_Z, -) ≅ R ℰom_X(Ri_* 𝒪_Z, -)`.

```lean
def derivedSheafHomExactSupportPushforwardNatIso :
    S.derivedSheafHomExactSupport ⋙ (modulePushforward S.i).mapDerivedCategory ≅
      (Stacks.SheafOfModules.derivedSheafHom S.X.sheaf).obj
        (op ((modulePushforward S.i).mapDerivedCategory.obj
          (RingedSite.derivedStructureSheaf (Stacks.SheafOfModules.ringedSite S.Z.sheaf))))
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedHomSheafFromPushforwardStructureSheafSiteIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportSiteDerivedInternalHom.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportSiteDerivedInternalHom.lean#L82). The attribute's comment: “the two right-hand sides identified: coextension of scalars and the site-level derived internal Hom bifunctor”.

> **The two right-hand sides of [Stacks, Tag 0A77] agree.** For a closed quotient morphism
> `i : Z ⟶ X` of ringed spaces, the right derived functor of coextension of scalars along
> `𝒪_X ⟶ i_* 𝒪_Z` is the derived internal Hom of the ringed site of opens of `X` out of
> `Ri_* 𝒪_Z`:
>
> `R ℰom_{𝒪_X}(i_* 𝒪_Z, -) ≅ RSheafHom(Ri_* 𝒪_Z, -)`.
>
> Both sides are the common value of the two formalized forms of [Stacks, Tag 0A77], whose shared
> left-hand side is `R ℰom(𝒪_Z, -)` followed by `i_*` on derived categories.

```lean
def derivedHomSheafFromPushforwardStructureSheafSiteIso :
    S.derivedHomSheafFromPushforwardStructureSheaf ≅
      (Stacks.SheafOfModules.derivedSheafHom S.X.sheaf).obj
        (op ((modulePushforward S.i).mapDerivedCategory.obj
          (RingedSite.derivedStructureSheaf (Stacks.SheafOfModules.ringedSite S.Z.sheaf))))
```

## Tag 0E2I, a lemma

[Tag 0E2I](https://stacks.math.columbia.edu/tag/0E2I) in the Stacks Project.

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedSheafHomDerivedModulePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedHomPushforward.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedHomPushforward.lean#L259). The attribute's comment: “the derived isomorphism, granted the underived internal Hom identification”.

> **Stacks Project, Tag 0E2I.** For `M` in `D(𝒪_Z)` and `K` in `D(𝒪_X)`,
>
> `R ℋom_{𝒪_X}(Ri_* M, K) ≅ Ri_* R ℋom_{𝒪_Z}(M, R ℰom(𝒪_Z, K))` in `D(𝒪_X)`,
>
> granted the underived identification `hom` of internal Hom complexes. The representatives used
> are the chosen K-injective models of `M` and `K`.

```lean
def derivedSheafHomDerivedModulePushforwardIso
    (hom : ∀ (N : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.closedSite.O)) ℤ)
      (I : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.ambientSite.O)) ℤ),
      (S.siteModulePushforward.mapHomologicalComplex (ComplexShape.up ℤ)).obj
          (RingedSite.sheafHomComplex S.closedSite N
            ((S.siteSheafHomExactSupport.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)).obj ≅
        (RingedSite.sheafHomComplex S.ambientSite
          ((S.siteModulePushforward.mapHomologicalComplex (ComplexShape.up ℤ)).obj N) I).obj)
    (M : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.closedSite.O)))
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf S.ambientSite.O))) :
    ((RingedSite.derivedSheafHomBifunctor S.ambientSite).obj
          (op (S.siteModulePushforward.mapDerivedCategory.obj M))).obj K ≅
      S.siteModulePushforward.mapDerivedCategory.obj
        (((RingedSite.derivedSheafHomBifunctor S.closedSite).obj (op M)).obj
          (S.siteDerivedSheafHomExactSupport.obj K))
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedSheafHomPushforwardNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHomBifunctor.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportDerivedInternalHomBifunctor.lean#L561). The attribute's comment: “the derived isomorphism, unconditionally”.

> **Stacks Project, Tag 0E2I.** For every object `M` of `D(𝒪_Z)`, the derived internal Hom out
> of the derived pushforward `Ri_* M` is derived sheaf Hom with exact support, followed by the
> derived internal Hom out of `M` on `Z`, followed by derived pushforward:
> `R ℰom_X(Ri_* M, -) ≅ Ri_* R ℰom_Z(M, R ℰom(𝒪_Z, -))`.

```lean
def derivedSheafHomPushforwardNatIso
    (M : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.Z))) :
    (Stacks.SheafOfModules.derivedSheafHom S.X.sheaf).obj
        (op ((modulePushforward S.i).mapDerivedCategory.obj M)) ≅
      S.derivedSheafHomExactSupport ⋙
        (Stacks.SheafOfModules.derivedSheafHom S.Z.sheaf).obj (op M) ⋙
          (modulePushforward S.i).mapDerivedCategory
```

## Tag 0A78, a lemma

[Tag 0A78](https://stacks.math.columbia.edu/tag/0A78) in the Stacks Project.

**`AlgebraicGeometry.Scheme.derivedSheafHomExactSupport_mem_derivedCategoryBPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean#L288). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0A78, part (1).** Let `i : Z ⟶ X` be a pseudo-coherent closed
> immersion of schemes. Then `R ℰom(𝒪_Z, -)` maps `D⁺_QCoh(𝒪_X)` into `D⁺_QCoh(𝒪_Z)`.
>
> Boundedness below is `isBoundedBelow_derivedSheafHomExactSupport_obj`. For quasi-coherence, the
> pushforward `Ri_* R ℰom(𝒪_Z, K)` is the derived internal Hom `R ℰom_{𝒪_X}(Ri_* 𝒪_Z, K)` by
> [Stacks, Tag 0A77], and `Ri_* 𝒪_Z` is pseudo-coherent by [Stacks, Tag 0AVX]; part (1) of
> [Stacks, Tag 0A6H] makes the cohomology sheaves of that
> derived internal Hom quasi-coherent. Since `i_*` is exact it commutes with taking cohomology, so
> each cohomology sheaf of `R ℰom(𝒪_Z, K)` has quasi-coherent pushforward, and
> `isQuasicoherent_of_pushforward` descends quasi-coherence to `Z`.

```lean
theorem derivedSheafHomExactSupport_mem_derivedCategoryBPlus (hi : PseudoCoherent i)
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent Z.ringCatSheaf)
      ((Stacks.ClosedImmersion.closedQuotientOfClosedImmersion
        i).derivedSheafHomExactSupport.obj K)
```

**`AlgebraicGeometry.Scheme.derivedSheafHomExactSupport_mem_derivedCategoryBPlus_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean#L307). The attribute's comment: “part (1) for a locally Noetherian target”.

> **Stacks Project, Tag 0A78, part (1), the locally Noetherian case.** For *every* closed
> immersion `i : Z ⟶ X` into a locally Noetherian scheme, `R ℰom(𝒪_Z, -)` maps `D⁺_QCoh(𝒪_X)` into
> `D⁺_QCoh(𝒪_Z)`: a closed immersion is locally of finite type, hence pseudo-coherent over a
> locally Noetherian target by [Stacks, Tag 0684].

```lean
theorem derivedSheafHomExactSupport_mem_derivedCategoryBPlus_of_noetherian
    [IsLocallyNoetherian X]
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBPlus
      (SheafOfModules.isQuasicoherent Z.ringCatSheaf)
      ((Stacks.ClosedImmersion.closedQuotientOfClosedImmersion
        i).derivedSheafHomExactSupport.obj K)
```

**`AlgebraicGeometry.isIso_affineDerivedSheafHomComparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean#L529). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0A78, part (2).** Let `φ : A ⟶ B` be a ring map whose spectrum is a
> pseudo-coherent closed immersion `i : Z = Spec B ⟶ X = Spec A`, and let `L` be a bounded-below
> object of `D(A)`. Then the comparison map of `affineDerivedSheafHomComparison` is invertible at
> `L`:
>
> `(R Hom_A(B, L))^~  ≅  R ℰom(𝒪_Z, L^~)`.
>
> This is the commutativity of the square of part (2): the derived sheafification functors
> `D⁺(A) ⥤ D⁺_QCoh(𝒪_X)` and `D⁺(B) ⥤ D⁺_QCoh(𝒪_Z)` intertwine `R Hom_A(B, -)` with
> `R ℰom(𝒪_Z, -)`.
>
> By the affine case of part (1), `affineDerivedSheafHomExactSupport_mem_derivedCategoryBPlus`, the
> target has quasi-coherent cohomology sheaves, so it is the derived sheafification of an object
> `N` of `D(B)`, and the comparison is the sheafification of a map `ψ` into `N`. For every `T` in
> `D(B)`, composition with `ψ` is, by `map_comp_affineDerivedSheafHomComparison_app`, the composite
> of the adjunction bijection of [Stacks, Tag 0A70], full faithfulness of derived sheafification on
> `Spec A`, composition with an isomorphism, and the adjunction bijection of [Stacks, Tag 0A76]. So
> `ψ` is an isomorphism by Yoneda, and hence so is the comparison.

```lean
theorem isIso_affineDerivedSheafHomComparison_app [IsClosedImmersion (Spec.map φ)]
    (hφ : PseudoCoherent (Spec.map φ))
    (L : DerivedCategory (ModuleCat.{u} A)) (hL : DerivedCategoryB.IsBoundedBelow L) :
    IsIso ((affineDerivedSheafHomComparison A B φ).app L)
```

**`AlgebraicGeometry.isIso_affineDerivedSheafHomComparison_app_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointLemmas/ExactSupportQuasicoherent.lean#L629). The attribute's comment: “part (2) for a locally Noetherian target”.

> **Stacks Project, Tag 0A78, part (2), the locally Noetherian case.** For *every* closed
> immersion `Spec B ⟶ Spec A` with `Spec A` locally Noetherian, the comparison map of
> `affineDerivedSheafHomComparison` is invertible at every bounded-below object of `D(A)`: a closed
> immersion is locally of finite type, hence pseudo-coherent over a locally Noetherian target by
> [Stacks, Tag 0684].

```lean
theorem isIso_affineDerivedSheafHomComparison_app_of_noetherian
    [IsLocallyNoetherian (Spec A)] [IsClosedImmersion (Spec.map φ)]
    (L : DerivedCategory (ModuleCat.{u} A)) (hL : DerivedCategoryB.IsBoundedBelow L) :
    IsIso ((affineDerivedSheafHomComparison A B φ).app L)
```

## Tag 0A79, a lemma

[Tag 0A79](https://stacks.math.columbia.edu/tag/0A79) in the Stacks Project.

**`AlgebraicGeometry.derivedSheafHomExactSupport_mem_derivedCategoryBPlus_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeCoherentDerivedHom.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/SchemeCoherentDerivedHom.lean#L386).

> **Stacks Project, Tag 0A79.** Let `i : Z ⟶ X` be a closed immersion of schemes with `X`
> locally Noetherian. Then `R ℰom(𝒪_Z, -)` carries `D⁺_Coh(𝒪_X)` into `D⁺_Coh(𝒪_Z)`.

```lean
theorem derivedSheafHomExactSupport_mem_derivedCategoryBPlus_coherent
    {Z X : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i] [IsLocallyNoetherian X]
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hK : DerivedCategoryB.derivedCategoryBPlus
      (Stacks.SheafOfModules.coherentModules X.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBPlus
      (Stacks.SheafOfModules.coherentModules Z.ringCatSheaf)
      ((Stacks.ClosedImmersion.closedQuotientOfClosedImmersion
        i).derivedSheafHomExactSupport.obj K)
```

## Tag 0A9X, a lemma

[Tag 0A9X](https://stacks.math.columbia.edu/tag/0A9X) in the Stacks Project.

**`Stacks.Duality.isDerivedSheafHomRightAdjoint_twistedInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointLocallySmall.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointLocallySmall.lean#L104). The attribute's comment: “with the right adjoint a produced rather than assumed: a is the twisted inverse image of Tag 0A9E, which exists at the locally small derived category of Tag 079Q and at no other model, Brown representability needing the direct sums indexed by the morphism universe. The hypotheses are the tag's own, quasi-compactness of the target and pseudo-coherence of the immersion; the quasi-separatedness the source also asks of the target is not needed, being automatic for the closed immersion itself, which is what Tag 0A9E consumes. Nothing is carried”.

> **Stacks Project, Tag 0A9X (Lemma 48.9.7), with the right adjoint produced.** Let
> `i : Z ⟶ W` be a closed immersion into a quasi-compact locally Noetherian scheme. Then the
> twisted inverse image `i^×` of [Stacks, Tag 0A9E] — the right adjoint of
> `Ri_* : D_QCoh(𝒪_Z) ⥤ D_QCoh(𝒪_W)` that Brown representability produces — agrees on
> bounded-below complexes with derived sheaf Hom out of the structure sheaf of the closed
> subscheme: `i^×(K) = R𝓗om_{𝒪_W}(𝒪_Z, K)` for `K` in `D⁺_QCoh(𝒪_W)`.
>
> This is `Stacks.Duality.isDerivedSheafHomRightAdjointAtModel_of_pseudoCoherent` fed with the
> [Stacks, Tag 0A9E] adjunction
> `AlgebraicGeometry.isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward`, which is available only
> at the locally small derived category of [Stacks, Tag 079Q] — the model in force here. The
> hypotheses are the tag's own: quasi-compactness of `W` and pseudo-coherence of `i`. The
> quasi-separatedness the source also asks of `W` is not needed, the morphism `i` being
> quasi-compact and quasi-separated for free.

```lean
theorem isDerivedSheafHomRightAdjoint_twistedInverseImage (hpc : PseudoCoherent i) :
    letI := AlgebraicGeometry.isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward i
    IsDerivedSheafHomRightAdjointAtModel i
      (twistedInverseImage i (isQuasicoherent_homology_derivedPushforward_of_qcqs i))
```

**`Stacks.Duality.isDerivedSheafHomRightAdjoint_twistedInverseImage_of_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointLocallySmall.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointLocallySmall.lean#L119). The attribute's comment: “with the right adjoint a produced rather than assumed, for a closed immersion into a quasi-compact locally Noetherian scheme: pseudo-coherence of i is then automatic by Tag 0684, which is the parenthetical case of the tag. Nothing is carried”.

> **[Stacks, Tag 0A9X] for a closed immersion into a quasi-compact locally Noetherian
> scheme**, the parenthetical case of the tag: pseudo-coherence is then automatic by
> [Stacks, Tag 0684], so the hypothesis is the Noetherian one and nothing about the immersion.

```lean
theorem isDerivedSheafHomRightAdjoint_twistedInverseImage_of_noetherian
    [IsLocallyNoetherian W] :
    letI := AlgebraicGeometry.isLeftAdjoint_qcqsQuasiCoherentDerivedPushforward i
    IsDerivedSheafHomRightAdjointAtModel i
      (twistedInverseImage i (isQuasicoherent_homology_derivedPushforward_of_qcqs i))
```

**`Stacks.Duality.LocallySmall.isDerivedSheafHomRightAdjoint_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointSheafHomLocallySmall.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointSheafHomLocallySmall.lean#L339). The attribute's comment: “at the locally small derived categories, the model at which the right adjoint a of Ri\_* exists (Tag 0A9E); the quasi-compactness and quasi-separatedness of X are dropped, the source using them only to produce a”.

> **Stacks Project, Tag 0A9X (Lemma 48.9.7).** Let `i : Z ⟶ W` be a pseudo-coherent closed
> immersion of schemes and let `a : D_QCoh(𝒪_W) ⥤ D_QCoh(𝒪_Z)` be the right adjoint of
> `Ri_* : D_QCoh(𝒪_Z) ⥤ D_QCoh(𝒪_W)`. Then there is a functorial isomorphism
> `a(K) ≅ R𝓗om_{𝒪_W}(𝒪_Z, K)` for `K` in `D⁺_QCoh(𝒪_W)`.
>
> Here `Ri_*` is the canonical restriction
> `Stacks.Duality.LocallySmall.affineHomQuasiCoherentDerivedPushforward` of the total derived
> direct image to `D_QCoh`: that `Ri_*` carries `D_QCoh(𝒪_Z)` into `D_QCoh(𝒪_W)` is proved
> (part (1) of [Stacks, Tag 08D5] for the affine morphism `i`,
> `Stacks.Duality.LocallySmall.isQuasicoherent_homology_derivedPushforward_of_isAffineHom`), not
> assumed. The right adjoint is quantified over together with its adjunction, which determines it
> up to unique isomorphism. The derived categories are the locally small models
> `AlgebraicGeometry.Scheme.Modules.hasDerivedCategory`, at which the right adjoint exists
> ([Stacks, Tag 0A9E]).
>
> The quasi-compactness and quasi-separatedness of `W` are dropped: the source uses them only to
> produce `a`, and the proof is uniqueness of adjoints against `R𝓗om(𝒪_Z, -)`, the right adjoint of
> `Ri_*` on all of `D(𝒪_W)` ([Stacks, Tag 0A76]) which maps `D⁺_QCoh(𝒪_W)` into `D⁺_QCoh(𝒪_Z)`
> ([Stacks, Tag 0A78]).

```lean
theorem isDerivedSheafHomRightAdjoint_of_isClosedImmersion (hpc : PseudoCoherent i)
    (a : quasiCoherentDerivedCategory W ⥤ quasiCoherentDerivedCategory Z)
    (adj : affineHomQuasiCoherentDerivedPushforward i ⊣ a) :
    IsDerivedSheafHomRightAdjoint i a
```

**`Stacks.Duality.isDerivedSheafHomRightAdjointAtModel_of_pseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointSheafHomSupplement.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionRightAdjointSheafHomSupplement.lean#L201). The attribute's comment: “the quasi-compactness and quasi-separatedness of the target are dropped, the source using them only to produce the right adjoint a, which here is an explicit parameter together with its adjunction”.

> **Stacks Project, Tag 0A9X (Lemma 48.9.7).** Let `i : Z ⟶ W` be a pseudo-coherent closed
> immersion of schemes and let `a` be a right adjoint of `Ri_* : D_QCoh(𝒪_Z) ⥤ D_QCoh(𝒪_W)`. Then
> on bounded-below complexes with quasi-coherent cohomology `a` is derived sheaf Hom out of the
> structure sheaf of the closed subscheme: `a(K) = R𝓗om_{𝒪_W}(𝒪_Z, K)` for `K` in
> `D⁺_QCoh(𝒪_W)`.

```lean
theorem isDerivedSheafHomRightAdjointAtModel_of_pseudoCoherent
    (hpc : PseudoCoherent i)
    (hpush : ∀ (K : quasiCoherentDerivedCategory Z) (n : ℤ),
      ((DerivedCategory.homologyFunctor W.Modules n).obj
        ((derivedPushforward i).obj K.obj)).IsQuasicoherent)
    (a : quasiCoherentDerivedCategory W ⥤ quasiCoherentDerivedCategory Z)
    (adj : quasiCoherentDerivedPushforward i hpush ⊣ a) :
    IsDerivedSheafHomRightAdjointAtModel i a
```

## Tag 0B6M, an example

[Tag 0B6M](https://stacks.math.columbia.edu/tag/0B6M) in the Stacks Project.

**`Stacks.Duality.rightAdjointToDerivedSheafHom_comp_derivedEvaluationAtOne_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceDiagram.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceDiagram.lean#L100). The attribute's comment: “the example, with no hypothesis beyond the closed immersion and the right adjoint: that Ri\_* carries D\_QCoh(O\_Z) into D\_QCoh(O\_W) is Tag 08D5 part (1), and the commutativity holds for every K in D\_QCoh(O\_W), so neither the Noetherian hypothesis of the source nor boundedness of K appears”.

> **Stacks Project, Tag 0B6M (Example 48.9.8).** Let `i : Z ⟶ W` be a closed immersion and let
> `a` be a right adjoint of `Ri_* : D_QCoh(𝒪_Z) ⥤ D_QCoh(𝒪_W)`. Then the trace `Ri_* a(K) ⟶ K` —
> the counit of `a` — is the comparison map of [Stacks, Tag 0A9X] pushed forward, followed by the
> identification of [Stacks, Tag 0A77], followed by the map
> `R ℰom_{𝒪_W}(i_* 𝒪_Z, K) ⟶ K` induced by the unit `𝒪_W ⟶ i_* 𝒪_Z`.
>
> This is the diagram of the source with its quasi-coherence hypothesis discharged by
> [Stacks, Tag 08D5] part (1).

```lean
theorem rightAdjointToDerivedSheafHom_comp_derivedEvaluationAtOne_of_isClosedImmersion
    (a : quasiCoherentDerivedCategory W ⥤ quasiCoherentDerivedCategory Z)
    (adj : closedImmersionQuasiCoherentDerivedPushforward i ⊣ a)
    (K : quasiCoherentDerivedCategory W) :
    (modulePushforward (closedQuotient i).i).mapDerivedCategory.map
          ((rightAdjointToDerivedSheafHom i
            (isQuasicoherent_homology_derivedPushforward_of_isClosedImmersion i) a adj).app K) ≫
        (closedQuotient i).derivedModulePushforwardDerivedSheafHomExactSupportIso.hom.app K.obj ≫
          (closedQuotient i).derivedEvaluationAtOne.app K.obj =
      (closedImmersionPushforwardModelIso i).hom.app ((a.obj K).obj) ≫
        (adj.counit.app K).hom
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.evaluationAtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean#L99). The attribute's comment: “the last arrow of the triangle: the map `R Eom_{O_X}(i_* O_Z, K) ⟶ K` induced by the unit `O_X ⟶ i_* O_Z`, here underived”.

> The map `ℰom_{𝒪_X}(i_* 𝒪_Z, -) ⟶ 𝟭` induced by the unit `𝒪_X ⟶ i_* 𝒪_Z`, that is,
> evaluation of a local homomorphism at the section `1`: the counit of the adjunction of
> [Stacks, Tag 0A75] read through its internal Hom identification.

```lean
noncomputable def evaluationAtOne :
    S.homSheafFromPushforwardStructureSheaf ⟶ 𝟭 (SheafOfModules.{u} (structureSheafRing S.X))
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedEvaluationAtOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean#L169). The attribute's comment: “the last arrow of the triangle, constructed from the underived evaluation at the section `1` by the universal property of the right derived functor”.

> The map `R ℰom_{𝒪_X}(i_* 𝒪_Z, -) ⟶ 𝟭` on `D(𝒪_X)` induced by the unit `𝒪_X ⟶ i_* 𝒪_Z`: the
> transformation out of the right derived functor which restricts to evaluation at one.

```lean
noncomputable def derivedEvaluationAtOne :
    S.derivedHomSheafFromPushforwardStructureSheaf ⟶
      𝟭 (DerivedCategory (SheafOfModules.{u} (structureSheafRing S.X)))
```

**`RingedSpaceModuleAdjunction.ClosedQuotientMorphismOfRingedSpaces.derivedModulePushforwardDerivedSheafHomExactSupportIso_hom_comp_derivedEvaluationAtOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean#L286). The attribute's comment: “the triangle at the level of ringed spaces: the trace of Tag 0A76 is the isomorphism of Tag 0A77 followed by the map induced by the unit `O_X ⟶ i_* O_Z`. Stated for every closed quotient morphism of ringed spaces and all of `D(O_X)`, so neither a Noetherian hypothesis nor boundedness of `K` appears”.

> **The triangle of [Stacks, Tag 0B6M] on all of `D(𝒪_X)`.** The trace `Ri_* R ℰom(𝒪_Z, K) ⟶ K`
> — the counit of [Stacks, Tag 0A76] — is the isomorphism of [Stacks, Tag 0A77] followed by the
> map `R ℰom_{𝒪_X}(i_* 𝒪_Z, K) ⟶ K` induced by the unit `𝒪_X ⟶ i_* 𝒪_Z`.

```lean
theorem derivedModulePushforwardDerivedSheafHomExactSupportIso_hom_comp_derivedEvaluationAtOne :
    S.derivedModulePushforwardDerivedSheafHomExactSupportIso.hom ≫ S.derivedEvaluationAtOne =
      S.derivedModulePushforwardSheafHomExactSupportAdjunction.counit
```

**`Stacks.Duality.rightAdjointToDerivedSheafHom_comp_derivedEvaluationAtOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTraceSheafHom.lean#L325). The attribute's comment: “the example: the trace of a right adjoint `a` of `Ri_*` is the comparison map of Tag 0A9X followed by Tag 0A77 followed by the map induced by the unit `O_W ⟶ i_* O_Z`. Since Tag 0A9X enters as its comparison map rather than as an isomorphism, the statement needs neither pseudo-coherence of `i`, nor part (1) of Tag 0A6H, nor boundedness, and holds for every `K` in `D_QCoh(O_W)`”.

> **Stacks Project, Tag 0B6M (Example 48.9.8).** Let `i : Z ⟶ W` be a closed immersion and let
> `a` be a right adjoint of `Ri_* : D_QCoh(𝒪_Z) ⥤ D_QCoh(𝒪_W)`. The trace `Ri_* a(K) ⟶ K` is the
> comparison map of [Stacks, Tag 0A9X] followed by the isomorphism of [Stacks, Tag 0A77] followed
> by the map `R ℰom_{𝒪_W}(i_* 𝒪_Z, K) ⟶ K` induced by the unit `𝒪_W ⟶ i_* 𝒪_Z`.

```lean
theorem rightAdjointToDerivedSheafHom_comp_derivedEvaluationAtOne
    (K : quasiCoherentDerivedCategory W) :
    (modulePushforward (closedQuotient i).i).mapDerivedCategory.map
          ((rightAdjointToDerivedSheafHom i hpush a adj).app K) ≫
        (closedQuotient i).derivedModulePushforwardDerivedSheafHomExactSupportIso.hom.app K.obj ≫
          (closedQuotient i).derivedEvaluationAtOne.app K.obj =
      (closedImmersionPushforwardModelIso i).hom.app ((a.obj K).obj) ≫
        (adj.counit.app K).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.9, Tag 0A74](https://stacks.math.columbia.edu/tag/0A74)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
