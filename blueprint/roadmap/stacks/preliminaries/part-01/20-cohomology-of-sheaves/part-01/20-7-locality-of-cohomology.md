---
declaration: section
origin: cited
lean: AlgebraicGeometry.cohomologyOverNatIsoRestriction, AlgebraicGeometry.cohomologyOverModuleNatIsoRestriction, Stacks.Perfect.LocalCohomologyExcision.restrictFunctor_preservesInjectiveObjects, Stacks.Cohomology.HigherDirectImage.restMod_preservesInjective, Hrestrict, locality_of_cohomology, Stacks.Cohomology.HigherDirectImagePresheaf.preimageCohomologyPresheaf_evaluation_iso, Stacks.Cohomology.HigherDirectImagePresheaf.preimageCohomologyPresheaf_map_eq_Hrestrict
statement: formalized
proof: formalized
---

# 20.7 Locality of cohomology

Section 20.7 of the Stacks Project, [Tag 01E0](https://stacks.math.columbia.edu/tag/01E0). 5 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01E1, a lemma

[Tag 01E1](https://stacks.math.columbia.edu/tag/01E1) in the Stacks Project.

**`AlgebraicGeometry.cohomologyOverNatIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ColimitsHigherDirect/CohomologyOfOpen.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/ColimitsHigherDirect/CohomologyOfOpen.lean#L133). The attribute's comment: “cohomology_of_open”.

> The cohomology of a sheaf of modules over an open is naturally isomorphic
> to the cohomology of its restriction to that open subspace.

```lean
public noncomputable def cohomologyOverNatIsoRestriction (X : SheafedSpace RingCat.{u})
    (U : Opens X.carrier) (p : ℕ) :
    ((SheafOfModules.evaluation (OXSh X) (op U) ⋙
        forget₂ (ModuleCat.{u} ((OXSh X).obj.obj (op U))) AddCommGrpCat.{u}).rightDerived p) ≅
      restMod X U ⋙
        ((SheafOfModules.evaluation (OUSh X U) (op (⊤ : Opens U)) ⋙
          forget₂ (ModuleCat.{u} ((OUSh X U).obj.obj (op (⊤ : Opens U))))
            AddCommGrpCat.{u}).rightDerived p)
```

**`AlgebraicGeometry.cohomologyOverModuleNatIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ColimitsHigherDirect/CohomologyOfOpen.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/ColimitsHigherDirect/CohomologyOfOpen.lean#L172). The attribute's comment: “cohomology_of_open, as modules over the sections on the open”.

> The cohomology of a sheaf of modules over an open is naturally isomorphic, as a module over
> the sections of `𝒪_X` on that open, to the cohomology of its restriction to the open subspace.

```lean
public noncomputable def cohomologyOverModuleNatIsoRestriction (X : SheafedSpace RingCat.{u})
    (U : Opens X.carrier) (p : ℕ) :
    ((SheafOfModules.evaluation (OXSh X)
          (op ((jFun X U).obj (⊤ : Opens ((Opens.toTopCat X.carrier).obj U)))) :
        SheafOfModules.{u} (OXSh X) ⥤ _).rightDerived p) ≅
      restMod X U ⋙ ((SheafOfModules.evaluation (OUSh X U)
          (op (⊤ : Opens ((Opens.toTopCat X.carrier).obj U))) :
        SheafOfModules.{u} (OUSh X U) ⥤ _).rightDerived p)
```

**`Stacks.Perfect.LocalCohomologyExcision.restrictFunctor_preservesInjectiveObjects`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/LocalCohomologyExcision.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/LocalCohomologyExcision.lean#L167). The attribute's comment: “restriction of modules to an open subscheme preserves injective objects”.

> **[Stacks, Tag 01E1]: restriction to an open subscheme preserves injective objects.**  This
> is `Stacks.Cohomology.HigherDirectImage.jStar_preservesInjectiveObjects` read through
> `restrictFunctor_eq_jStar`.

```lean
instance restrictFunctor_preservesInjectiveObjects :
    (Scheme.Modules.restrictFunctor U.ι).PreservesInjectiveObjects
```

**`Stacks.Cohomology.HigherDirectImage.restMod_preservesInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/RestrictionPreservesInjectives.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/RestrictionPreservesInjectives.lean#L49). The attribute's comment: “restriction_preserves_injectives”.

> The restriction of an injective sheaf of modules to an open subspace is injective.

```lean
public theorem restMod_preservesInjective (X : SheafedSpace.{u + 1, u, u} RingCat.{u})
    (U : Opens X.carrier) (I : SheafOfModules.{u} (OXSh X)) [Injective I] :
    Injective ((restMod X U).obj I)
```

## Tag 01E2, an equation

[Tag 01E2](https://stacks.math.columbia.edu/tag/01E2) in the Stacks Project.

Declarations registered for the tag:

- [`Hrestrict`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Locality/CohomologyVanishesLocally.lean#L124), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L95) (StacksFrontier).

## Tag 01E3, a lemma

[Tag 01E3](https://stacks.math.columbia.edu/tag/01E3) in the Stacks Project.

**`locality_of_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Locality/CohomologyVanishesLocally.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Locality/CohomologyVanishesLocally.lean#L464). References: SGA 4 V (3.1), “special case”.

> **Stacks Project Tag 01E3 (Lemma 20.7.2), Locality of cohomology.**
> For a ringed space with structure sheaf `R`, a sheaf of `O_X`-modules `F`, an open `U`, a positive
> degree `n`, and a cohomology class `ξ ∈ H^n(U, F)`, there exists an open covering
> `U = ⨆ i, cover i` (each `cover i ⊆ U`) on which `ξ` restricts to `0`.
>
> Rigorous argument (assembly).
> Choose the canonical injective resolution `I := InjectiveResolution.of F` of `F`. The iso
> `e_W : Hgroup R W n F ≅ (secCx R I W).homology n` from `InjectiveResolution.isoRightDerivedObj`
> identifies cohomology with section-complex homology, naturally in the open `W` in the following
> precise
> sense (`InjectiveResolution.rightDerived_app_eq`): for `h : V ≤ U`,
> `Hrestrict R h n F = e_U.hom ≫ homologyMap (r_V) n ≫ e_V.inv`, where
> `r_V = (NatTrans.mapHomologicalComplex (secRestrict R h) _).app I.cocomplex`.
>
> Transport `ξ` to `ξ' := e_U.hom ξ ∈ (secCx R I U).homology n`. Apply
> `exists_cover_homologyMap_eq_zero`
> to `ξ'` (using `n > 0`) to get a cover `U = ⨆ i, cover i`, `hle i : cover i ≤ U`, with
> `homologyMap (r_{cover i}) n ξ' = 0` for each `i`. Then, for each `i`,
> `Hrestrict R (hle i) n F ξ = e_{cover i}.inv (homologyMap (r_{cover i}) n (e_U.hom ξ))
>   = e_{cover i}.inv (homologyMap (r_{cover i}) n ξ') = e_{cover i}.inv 0 = 0`,
> using that `e_{cover i}.inv` is an additive group hom (sends `0` to `0`). This is the required
> cover.

```lean
theorem locality_of_cohomology
    (F : SheafOfModules R) (U : Opens X) (n : ℕ) (hn : 0 < n)
    (ξ : Hgroup R U n F) :
    ∃ (I : Type u) (cover : I → Opens X) (hle : ∀ i, cover i ≤ U),
      ((⨆ i, cover i) = U) ∧
      ∀ i, Hrestrict R (hle i) n F ξ = 0
```

## Tag 01E4, a lemma

[Tag 01E4](https://stacks.math.columbia.edu/tag/01E4) in the Stacks Project.

**`Stacks.Cohomology.HigherDirectImagePresheaf.preimageCohomologyPresheaf_evaluation_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 1122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L1122). The attribute's comment: “values on opens”.

> The value on `V` of the cohomology presheaf is canonically and naturally isomorphic
> to `Hⁿ(f⁻¹(V), -)`.

```lean
public noncomputable def preimageCohomologyPresheaf_evaluation_iso
    (f : X ⟶ Y) (V : Opens Y.carrier) (n : ℕ) :
    (cohFunctor.{u, u, u, u, u, u} (opensMap f) (structureSheafRing X) (structureSheafRing Y)
        (structureSheafHom f)).rightDerived n ⋙
        PresheafOfModules.toPresheaf (structureSheafRing Y).obj ⋙
        (evaluation (Opens Y.carrier)ᵒᵖ AddCommGrpCat.{u}).obj (op V) ≅
    Hfunctor (structureSheafRing X) ((opensMap f).obj V) n
```

**`Stacks.Cohomology.HigherDirectImagePresheaf.preimageCohomologyPresheaf_map_eq_Hrestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 1139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L1139). The attribute's comment: “restriction mappings”.

> Under the canonical identifications of its values with cohomology, the map of the
> cohomology presheaf along `U ⊆ V` is the restriction map of Tag 01E2.

```lean
public theorem preimageCohomologyPresheaf_map_eq_Hrestrict
    (f : X ⟶ Y) {U V : Opens Y.carrier} (h : U ≤ V) (n : ℕ)
    (F : SheafOfModules.{u} (structureSheafRing X)) :
    ((PresheafOfModules.toPresheaf (structureSheafRing Y).obj).obj
          (cohPresheafModule.{u, u, u, u}
            (opensMap f) (structureSheafRing X) (structureSheafRing Y)
            (structureSheafHom f) n F)).map (homOfLE h).op ≫
        (preimageCohomologyPresheaf_evaluation_iso f U n).hom.app F =
    (preimageCohomologyPresheaf_evaluation_iso f V n).hom.app F ≫
        Hrestrict (structureSheafRing X) (leOfHom ((opensMap f).map (homOfLE h))) n F
```

**`Stacks.Cohomology.HigherDirectImagePresheaf.higherDirectImage_iso_sheafify_preimageCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 1167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L1167). The attribute's comment: “associated sheaf”.

> The `n`-th higher direct image is naturally isomorphic to the sheafification of the
> presheaf `V ↦ Hⁿ(f⁻¹(V), -)`.

```lean
public noncomputable def higherDirectImage_iso_sheafify_preimageCohomology
    (f : X ⟶ Y) (n : ℕ) :
    (modulePushforward f).rightDerivedPlus n ≅
      (cohFunctor.{u, u, u, u, u, u} (opensMap f) (structureSheafRing X) (structureSheafRing Y)
          (structureSheafHom f)).rightDerived n ⋙
        PresheafOfModules.sheafification (𝟙 (structureSheafRing Y).obj)
```

**`Stacks.Cohomology.HigherDirectImagePresheaf.preimageHypercohomologyPresheaf_evaluation_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 1211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L1211). The attribute's comment: “bounded below values on opens”.

> The value on `V` of the bounded-below hypercohomology presheaf is canonically and
> naturally isomorphic to the `i`-th hypercohomology of `K` on `f⁻¹(V)`.

```lean
public noncomputable def preimageHypercohomologyPresheaf_evaluation_iso
    (f : X ⟶ Y) (V : Opens Y.carrier) (i : ℤ) :
    (modulePushforward f ⋙ SheafOfModules.forget (structureSheafRing Y)).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor _ i ⋙
        PresheafOfModules.toPresheaf (structureSheafRing Y).obj ⋙
        (evaluation (Opens Y.carrier)ᵒᵖ AddCommGrpCat.{u}).obj (op V) ≅
      (secF (structureSheafRing X) ((opensMap f).obj V)).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u} i
```

**`Stacks.Cohomology.HigherDirectImagePresheaf.preimageHypercohomologyPresheaf_map_eq_hypercohomologyRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 1255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L1255). The attribute's comment: “bounded below restriction mappings”.

> Under the canonical identifications of its values with hypercohomology, the map of
> the bounded-below hypercohomology presheaf along `U ⊆ V` is the restriction map
> induced by restriction of sections.

```lean
public theorem preimageHypercohomologyPresheaf_map_eq_hypercohomologyRestrict
    (f : X ⟶ Y) {U V : Opens Y.carrier} (h : U ≤ V) (i : ℤ)
    (K : DerivedCategory.Plus (SheafOfModules.{u} (structureSheafRing X))) :
    ((PresheafOfModules.toPresheaf (structureSheafRing Y).obj).obj
          (preimageHypercohomologyPresheaf f K i)).map (homOfLE h).op ≫
        (preimageHypercohomologyPresheaf_evaluation_iso f U i).hom.app K =
      (preimageHypercohomologyPresheaf_evaluation_iso f V i).hom.app K ≫
        (hypercohomologyRestrict (structureSheafRing X)
          (leOfHom ((opensMap f).map (homOfLE h))) i).app K
```

**`Stacks.Cohomology.HigherDirectImagePresheaf.derivedPushforwardPlus_homology_iso_sheafify_preimageHypercohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean, line 1282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/SheafifiedCohomologyPresheaf.lean#L1282). The attribute's comment: “bounded below associated sheaf”. References: EGA 0 (12.4.3), “special case”.

> For a bounded below complex, the `i`-th cohomology sheaf of its derived pushforward
> is naturally isomorphic to the sheafification of `V ↦ Hⁱ(f⁻¹(V), K)`.

```lean
public noncomputable def
    derivedPushforwardPlus_homology_iso_sheafify_preimageHypercohomology
    (f : X ⟶ Y) (i : ℤ) :
    (modulePushforward f).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor _ i ≅
      (modulePushforward f ⋙ SheafOfModules.forget (structureSheafRing Y)).rightDerivedFunctorPlus ⋙
        DerivedCategory.Plus.homologyFunctor _ i ⋙
          PresheafOfModules.sheafification (𝟙 (structureSheafRing Y).obj)
```

## Tag 01E5, a lemma

[Tag 01E5](https://stacks.math.columbia.edu/tag/01E5) in the Stacks Project.

**`Stacks.Cohomology.HigherDirectImage.rightDerivedPushforwardRestrictIso_ofLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationCocycle.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationCocycle.lean#L112). The attribute's comment: “compatibility across nested opens, every degree”.

> The comparison `rightDerivedPushforwardRestrictIso` attached to `V'` is the comparison
> attached to `V`, whiskered by restriction along `V' ≤ V` and followed by the derived middle
> comparison, read through the transitivity isomorphism `moduleRestrictionOfLEIso` on the `Y` side.
>
> Equivalently: the two routes from `R^p f_* ℱ` restricted to `V'`, namely restricting to `V` and
> then along `V' ≤ V` or restricting to `V'` directly, induce the same identification of
> `(R^p f_* ℱ)|_{V'}` with the `p`-th right derived functor of
> `ℱ ↦ (f|_{f⁻¹(V')})_*(ℱ|_{f⁻¹(V')})`.

```lean
theorem rightDerivedPushforwardRestrictIso_ofLE (p : ℕ) :
    Functor.whiskerRight (rightDerivedPushforwardRestrictIso f V p).hom
          (moduleRestrictionOfLE Y h) ≫
        (rightDerivedPushforwardRestrictionOfLEIso f h p).hom =
      Functor.whiskerLeft ((modulePushforward f).rightDerived p)
          (moduleRestrictionOfLEIso Y h).hom ≫
        (rightDerivedPushforwardRestrictIso f V' p).hom
```

**`Stacks.Cohomology.HigherDirectImage.higherDirectImageRestrictIsoSucc_ofLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationCocycle.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationCocycle.lean#L168). The attribute's comment: “higher direct images, compatibility across nested opens”.

> The comparison `higherDirectImageRestrictIsoSucc` attached to `V`, whiskered by restriction
> along `V' ≤ V` and followed by the transitivity isomorphism `moduleRestrictionOfLEIso` on the
> `Y` side, agrees with `higherDirectImageRestrictIsoSuccOfLE` followed by the comparison attached
> to `V'`.

```lean
theorem higherDirectImageRestrictIsoSucc_ofLE (p : ℕ) :
    Functor.whiskerRight (higherDirectImageRestrictIsoSucc f V p).hom
          (moduleRestrictionOfLE Y h) ≫
        Functor.whiskerLeft ((modulePushforward f).rightDerived p)
          (moduleRestrictionOfLEIso Y h).hom =
      (higherDirectImageRestrictIsoSuccOfLE f h p).hom ≫
        (higherDirectImageRestrictIsoSucc f V' p).hom
```

**`Stacks.Cohomology.HigherDirectImage.higherDirectImageRestrictIso_injectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationInDegreeZero.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationInDegreeZero.lean#L251). The attribute's comment: “compatibility with injective resolutions”.

> **Stacks 01E5, compatibility with injective resolutions.**  On injective resolutions,
> localization of a higher direct image is obtained by restricting the resolution and applying
> the identity-on-sections comparison before taking cohomology.  The augmentation condition `hφ`
> says that the comparison of resolutions descends the identity of the restricted module.
>
> `higherDirectImageRestrictIso` is defined by cases on the degree; in positive degree this is
> `higherDirectImageRestrictIso_injectiveResolution_succ` and in degree zero it is
> `higherDirectImageRestrictIso_injectiveResolution_zero`.

```lean
theorem higherDirectImageRestrictIso_injectiveResolution (p : ℕ)
    (M : SheafOfModules.{u} (structureSheafRing X)) (I : InjectiveResolution M)
    (J : InjectiveResolution ((moduleRestriction X (preimageOpen f V)).obj M))
    (φ : J.cocomplex ⟶
      ((moduleRestriction X (preimageOpen f V)).mapHomologicalComplex
        (ComplexShape.up ℕ)).obj I.cocomplex)
    (hφ : J.ι.f 0 ≫ φ.f 0 =
      (moduleRestriction X (preimageOpen f V)).map (I.ι.f 0)) :
    (higherDirectImageRestrictIso f V p).hom.app M ≫
        (moduleRestriction Y V).map
          (I.isoRightDerivedObj (modulePushforward f) p).hom =
      (J.isoRightDerivedObj (modulePushforward (restrictedMorphism f V)) p).hom ≫
        (HomologicalComplex.homologyFunctor _ (ComplexShape.up ℕ) p).map
          (((modulePushforward (restrictedMorphism f V)).mapHomologicalComplex
            (ComplexShape.up ℕ)).map φ) ≫
        (HomologicalComplex.homologyFunctor _ (ComplexShape.up ℕ) p).map
          (((modulePushforwardRestrictIso f V).hom.mapHomologicalComplex
            (ComplexShape.up ℕ)).app I.cocomplex) ≫
        (((((modulePushforward f).mapHomologicalComplex (ComplexShape.up ℕ)).obj
          I.cocomplex).sc p).mapHomologyIso (moduleRestriction Y V)).hom
```

**`Stacks.Cohomology.HigherDirectImage.higherDirectImageRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean#L189). The attribute's comment: “higher direct images”. References: SGA 4 V (5.1), “Clause 3, special case”.

> **Stacks 01E5, higher direct images.**  Higher direct images commute naturally with
> restriction to an open subspace: for `U = f⁻¹(V)`, restricting a sheaf of `𝒪_X`-modules to `U`
> and taking the `p`-th higher direct image along `f|_U` agrees with taking the `p`-th higher
> direct image along `f` and restricting to `V`.
>
> In positive degree this is `higherDirectImageRestrictIsoSucc`, which rests on Stacks 01E1; in
> degree zero it is the normalized comparison `higherDirectImageRestrictIsoZero`, so that the
> degree-zero compatibility below holds by construction.

```lean
noncomputable def higherDirectImageRestrictIso (p : ℕ) :
    moduleRestriction X (preimageOpen f V) ⋙
          (modulePushforward (restrictedMorphism f V)).rightDerived p ≅
        (modulePushforward f).rightDerived p ⋙ moduleRestriction Y V
```

**`Stacks.Cohomology.HigherDirectImage.higherDirectImageRestrictIso_zero_compatibility`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean#L201). The attribute's comment: “degree-zero compatibility”.

> **Stacks 01E5, degree-zero compatibility.**  In degree zero the higher-direct-image
> comparison is the ordinary restriction comparison, after the canonical maps to the zeroth right
> derived functors.  This rules out multiplying the degree-zero comparison by an automorphism.

```lean
theorem higherDirectImageRestrictIso_zero_compatibility :
    Functor.whiskerLeft
          (moduleRestriction X (preimageOpen f V))
          (modulePushforward (restrictedMorphism f V)).toRightDerivedZero ≫
        (higherDirectImageRestrictIso f V 0).hom =
      (modulePushforwardRestrictIso f V).hom ≫
        Functor.whiskerRight (modulePushforward f).toRightDerivedZero
          (moduleRestriction Y V)
```

**`Stacks.Cohomology.HigherDirectImage.derivedPushforwardPlusRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean#L318). The attribute's comment: “bounded below derived image”.

> **Stacks 01E5, bounded below derived image.**  The total right derived pushforward of a
> bounded below complex commutes naturally with restriction to an open subspace: deriving
> restriction to `U = f⁻¹(V)` and then pushforward along `f|_U` agrees with deriving pushforward
> along `f` and then restriction to `V`.
>
> Both sides are right derived functors, along `DerivedCategory.Plus.Qh` and relative to
> quasi-isomorphisms, of the two composites of termwise functors; the isomorphism is the one
> induced by `modulePushforwardRestrictHomotopyIso` through uniqueness of right derived
> functors.

```lean
noncomputable def derivedPushforwardPlusRestrictIso :
    (moduleRestriction X (preimageOpen f V)).rightDerivedFunctorPlus ⋙
          (modulePushforward (restrictedMorphism f V)).rightDerivedFunctorPlus ≅
        (modulePushforward f).rightDerivedFunctorPlus ⋙
          (moduleRestriction Y V).rightDerivedFunctorPlus
```

**`Stacks.Cohomology.HigherDirectImage.derivedPushforwardPlusRestrictIso_unit_compatibility`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationIsomorphisms.lean#L340). The attribute's comment: “compatibility with derived units”.

> **Stacks 01E5, compatibility with derived units.**  The derived localization isomorphism is
> the one induced by the undeived comparison: after precomposition with the localization functor
> its hom intertwines the two composite derived-functor units.  This is the defining
> factorization of `Functor.rightDerivedNatTrans`.

```lean
theorem derivedPushforwardPlusRestrictIso_unit_compatibility :
    Functor.whiskerRight (modulePushforwardRestrictHomotopyIso f V).hom
          DerivedCategory.Plus.Qh ≫
        successiveRightDerivedFunctorPlusUnit (modulePushforward f) (moduleRestriction Y V) =
      successiveRightDerivedFunctorPlusUnit (moduleRestriction X (preimageOpen f V))
          (modulePushforward (restrictedMorphism f V)) ≫
        Functor.whiskerLeft DerivedCategory.Plus.Qh
          (derivedPushforwardPlusRestrictIso f V).hom
```

**`Stacks.Cohomology.HigherDirectImage.modulePushforwardRestrictIso_ofLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationNaturality.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationNaturality.lean#L493). The attribute's comment: “compatibility across nested opens, before deriving”.

> **Stacks 01E5, compatibility across nested opens, before deriving.**  Stacks 01E5 asserts
> an *equality* of
> sheaves, so the comparisons it attaches to two nested opens `V' ≤ V` of `Y` must agree.  Before
> deriving that is this cocycle identity: the comparison
> `(f|_{f⁻¹(V')})_*(ℱ|_{f⁻¹(V')}) ≅ (f_* ℱ)|_{V'}` is the comparison for `V`, whiskered by
> restriction along `V' ≤ V`, composed with the middle comparison
> `modulePushforwardRestrictionOfLEIso` and the two transitivity isomorphisms
> `moduleRestrictionOfLEIso` on the `X` and the `Y` side.  Equivalently: the two routes from
> `ℱ|_{f⁻¹(V)} ↦ ((f|_{f⁻¹(V)})_*(ℱ|_{f⁻¹(V)}))|_{V'}` to `(f_* ℱ)|_{V'}` agree.
>
> This is the "localizing" input to the construction Stacks 02O7 calls *localizing and then
> sheafifying*: it is what makes the comparisons over the opens of `Y` fit together into a
> statement about sheaves on `Y`, rather than one open at a time.
>
> Every factor is, on sections, a restriction map along an equality of opens, hence the identity
> up to the transport of the type of sections; both sides are maps between the same two types, so
> `heq_val_map_of_hom` four times forces them to agree.

```lean
theorem modulePushforwardRestrictIso_ofLE :
    (modulePushforwardRestrictIso f V').hom =
      Functor.whiskerRight (moduleRestrictionOfLEIso X (preimageOpen_mono f h)).inv
          (modulePushforward (restrictedMorphism f V')) ≫
        Functor.whiskerLeft (moduleRestriction X (preimageOpen f V))
          (modulePushforwardRestrictionOfLEIso f h).hom ≫
        Functor.whiskerRight (modulePushforwardRestrictIso f V).hom
          (moduleRestrictionOfLE Y h) ≫
        Functor.whiskerLeft (modulePushforward f) (moduleRestrictionOfLEIso Y h).hom
```

**`Stacks.Cohomology.HigherDirectImage.higherDirectImageRestrictIso_zero_ofLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationNaturality.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HigherDirectImage/LocalizationNaturality.lean#L526). The attribute's comment: “compatibility across nested opens, degree zero”.

> **Stacks 01E5, compatibility across nested opens in degree zero.**  The degree-zero
> derived comparison `higherDirectImageRestrictIso f V' 0` is compatible with shrinking `V` to
> `V'`: after the canonical maps to the zeroth right derived functors it is the degree-zero
> comparison for `V`, carried along the three isomorphisms of
> `modulePushforwardRestrictIso_ofLE`.
>
> In degree zero both pushforwards are left exact, so the derived comparison is normalized to the
> undeived one (`higherDirectImageRestrictIso_zero_compatibility`) and the clause reduces to the
> cocycle identity before deriving.  No analogue of Stacks 01E1 for an inclusion of opens is
> needed; see the implementation notes for why positive degree is not proved here.

```lean
theorem higherDirectImageRestrictIso_zero_ofLE :
    Functor.whiskerLeft (moduleRestriction X (preimageOpen f V'))
          (modulePushforward (restrictedMorphism f V')).toRightDerivedZero ≫
        (higherDirectImageRestrictIso f V' 0).hom =
      Functor.whiskerRight (moduleRestrictionOfLEIso X (preimageOpen_mono f h)).inv
          (modulePushforward (restrictedMorphism f V')) ≫
        Functor.whiskerLeft (moduleRestriction X (preimageOpen f V))
          (modulePushforwardRestrictionOfLEIso f h).hom ≫
        Functor.whiskerRight (modulePushforwardRestrictIso f V).hom
          (moduleRestrictionOfLE Y h) ≫
        Functor.whiskerLeft (modulePushforward f) (moduleRestrictionOfLEIso Y h).hom ≫
        Functor.whiskerRight (modulePushforward f).toRightDerivedZero
          (moduleRestriction Y V')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.7, Tag 01E0](https://stacks.math.columbia.edu/tag/01E0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
