---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.moduleRestriction_obj, AlgebraicGeometry.RingedSite.localizationPullbackIsoRestriction_exists, AlgebraicGeometry.RingedSite.over, AlgebraicGeometry.RingedSite.localizationMorphism, AlgebraicGeometry.RingedSite.localizationDirectImage, SheafOfModules.pullback, SheafOfModules.pullbackPushforwardAdjunction, Stacks.Sites.ExtensionByZero.extensionByZero_exact
statement: formalized
proof: formalized
---

# 18.19 Localization of ringed sites

Section 18.19 of the Stacks Project, [Tag 03DH](https://stacks.math.columbia.edu/tag/03DH). 9 tags here are carried by 38 declarations of the repository (all in StacksFrontier) and 17 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04IX, a definition

[Tag 04IX](https://stacks.math.columbia.edu/tag/04IX) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.moduleRestriction_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean#L82). The attribute's comment: “module\_restriction”.

> The sections of a restricted sheaf of modules over an object `V ⟶ U` of the localized site
> are the sections of the original sheaf over `V`: restriction is reindexing along
> `Over.forget U`.

```lean
theorem moduleRestriction_obj {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    {R : Sheaf J RingCat.{w}} (F : SheafOfModules.{w} R) (U : C) (V : (Over U)ᵒᵖ) :
    ((F.over U).val.presheaf.obj V : Type w) =
      (F.val.presheaf.obj (Opposite.op V.unop.left) : Type w)
```

**`AlgebraicGeometry.RingedSite.localizationPullbackIsoRestriction_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Pullback.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Pullback.lean#L215). The attribute's comment: “module\_restriction”.

> Pullback of sheaves of modules along the localization morphism of ringed topoi at `U` is
> isomorphic to restriction to the localized site.

```lean
theorem localizationPullbackIsoRestriction_exists :
    Nonempty ((X.localizationMorphism U).pullbackModules ≅
      SheafOfModules.overFunctor (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSite.over`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/RingedSiteLocalization.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean#L55) (StacksFrontier): “localized\_ringed\_site”.
- [`AlgebraicGeometry.RingedSite.localizationMorphism`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Morphism.lean#L79), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean#L56) (StacksFrontier): “localization\_morphism”.
- [`AlgebraicGeometry.RingedSite.localizationDirectImage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean#L57) (StacksFrontier): “localization\_direct\_image”.
- [`SheafOfModules.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean#L59) (StacksFrontier): “extension\_by\_zero”. References: EGA IV (11.9.16), “more general”; EGA IV (2.5.1), “partial”; EGA IV (4.8.2), “more general”; EGA IV (9.4.9); SGA 3 I (4.6.1), “more general”; SGA 3 III (0.1.4), “more general”; SGA 4 VI (8.7.1), “partial”; SGA 4 XVII (4.1); SGA 7 XIV (4.5), “more general”.
- [`SheafOfModules.pullbackPushforwardAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullbackPushforwardAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean#L60) (StacksFrontier): “extension\_by\_zero”. References: SGA 3 VIIA (1.3), “more general”.
- [`Stacks.Sites.ExtensionByZero.extensionByZero_exact`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean#L394), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/Basic.lean#L61) (StacksFrontier): “extension\_by\_zero”.
- [`SheafOfModules.over`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.over#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean#L55) (StacksFrontier): “module\_restriction”. References: SGA 3 I (3.1.4), “more general”; SGA 4 IV (11.2.2); SGA 4 Vbis (1.3.7), “special case”.
- [`SheafOfModules.overFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.overFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocalizationRingedSites/DirectImage.lean#L59) (StacksFrontier): “module\_restriction”. References: SGA 3 I (3.1.4), “more general”; SGA 4 IV (11.2.2); SGA 4 Vbis (1.3.7), “special case”.

## Tag 03DI, a lemma

[Tag 03DI](https://stacks.math.columbia.edu/tag/03DI) in the Stacks Project.

**`Stacks.Sites.ExtensionByZero.OverElements.extensionByZeroPresheafSectionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean#L284). The attribute's comment: “for the site of elements of a presheaf of sets”.

> The presheaf whose sheafification is extension by zero has over `V` the direct sum of the
> sections of `G` at the objects `(V, t)` of the site of elements, over all sections `t` of `K`
> over `V`.

```lean
noncomputable def extensionByZeroPresheafSectionIso
    (G : SheafOfModules.{u} (restrictedRingSheaf K J JD R)) (V : C) :
    ((PresheafOfModules.pullback.{u} (F := proj K) (R := R.obj)
      (S := (restrictedRingSheaf K J JD R).obj)
      (𝟙 (restrictedRingSheaf K J JD R) :
        (restrictedRingSheaf K J JD R) ⟶ (restrictedRingSheaf K J JD R)).hom).obj
          G.val).obj (op V) ≅
      (∐ extensionByZeroSummands K J JD R G V)
```

**`Stacks.Sites.ExtensionByZero.extensionByZeroPresheafSectionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean#L332). The attribute's comment: “direct-sum formula”.

> The presheaf whose sheafification is extension by zero has over `V` the direct sum of
> the sections over all maps from `V` to `U`.

```lean
noncomputable def extensionByZeroPresheafSectionIso
    (G : SheafOfModules.{u} (R.over U)) (V : C) :
    ((PresheafOfModules.pullback.{u} (F := Over.forget U) (R := R.obj)
      (S := (R.over U).obj)
      (𝟙 (R.over U) : (R.over U) ⟶ (R.over U)).hom).obj G.val).obj (op V) ≅
      (∐ extensionByZeroSummands J R U G V)
```

**`Stacks.Sites.ExtensionByZero.extensionByZeroPresheafSectionIso_inv_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean#L356). The attribute's comment: “canonical direct-sum comparison”.

> The direct-sum comparison is the canonical one: on the summand indexed by
> `φ : V ⟶ U`, its inverse is the unit of the presheaf adjunction at `φ`.

```lean
theorem extensionByZeroPresheafSectionIso_inv_ι
    [HasWeakSheafify J AddCommGrpCat.{u}] [J.WEqualsLocallyBijective AddCommGrpCat.{u}]
    (G : SheafOfModules.{u} (R.over U)) (V : C) (φ : V ⟶ U) :
    HEq (Limits.Sigma.ι (extensionByZeroSummands J R U G V) φ ≫
      (extensionByZeroPresheafSectionIso J R U G V).inv)
    (((PresheafOfModules.pullbackPushforwardAdjunction.{u}
      (F := Over.forget U) (R := R.obj) (S := (R.over U).obj)
      (𝟙 (R.over U) : (R.over U) ⟶ (R.over U)).hom).unit.app G.val).app
        (op (Over.mk φ)))
```

**`Stacks.Sites.ExtensionByZero.extensionByZeroHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroDirectSumSheafification.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroDirectSumSheafification.lean#L74). The attribute's comment: “Mor(G, j\_U^* F) = Mor(j\_\{U!} G, F)”.

> **Stacks 03DI**, the displayed bijection: morphisms of sheaves of `O_U`-modules
> `G ⟶ j_U^* F` correspond to morphisms of sheaves of `O`-modules `j_{U!} G ⟶ F`.
>
> This is the transpose of the adjunction `j_{U!} ⊣ j_U^*`, which is available with no
> adjointness hypothesis because `sheafRestrictionIsRightAdjoint` discharges it.

```lean
noncomputable def extensionByZeroHomEquiv (G : SheafOfModules.{u} (R.over U))
    (F : SheafOfModules.{u} R) :
    (G ⟶ (SheafOfModules.pushforward.{u} (F := Over.forget U)
        (𝟙 (R.over U) : (R.over U) ⟶ (R.over U))).obj F) ≃
      ((SheafOfModules.pullback.{u} (F := Over.forget U)
        (𝟙 (R.over U) : (R.over U) ⟶ (R.over U))).obj G ⟶ F)
```

**`Stacks.Sites.ExtensionByZero.extensionByZeroIsoSheafifyDirectSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroDirectSumSheafification.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroDirectSumSheafification.lean#L106). The attribute's comment: “j\_\{U!} G is the sheaf associated to V ↦ ⨁\_\{φ : V ⟶ U} G(φ)”.

> **Stacks 03DI**, the direct-sum formula: the extension by zero `j_{U!} G` of a sheaf of
> `O_U`-modules `G` is the sheaf associated to the presheaf whose sections over `V` are
> `⨁_{φ ∈ Mor_C(V, U)} G(V →φ U)`.
>
> That presheaf is `directSumPresheaf U R.obj G.val`; its sections over `V` are the displayed
> direct sum by `directSumPresheaf_obj`, and its restriction maps are the restriction maps of `G`
> between the summands by `presheafRestriction_ι_apply`.

```lean
noncomputable def extensionByZeroIsoSheafifyDirectSum (G : SheafOfModules.{u} (R.over U)) :
    (SheafOfModules.pullback.{u} (F := Over.forget U)
        (𝟙 (R.over U) : (R.over U) ⟶ (R.over U))).obj G ≅
      (PresheafOfModules.sheafification (R₀ := R.obj) (𝟙 R.obj)).obj
        (directSumPresheaf U R.obj G.val)
```

**`Stacks.Sites.ExtensionByZero.overMap_isRightAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroOverMap.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroOverMap.lean#L81). The attribute's comment: “extension by zero along a relocalization C/V ⥤ C/U”.

> **Stacks 03DI for a relocalization.** Restriction of sheaves of modules along
> `Over.map f : C/V ⥤ C/U` has a left adjoint.

```lean
instance overMap_isRightAdjoint : (SheafOfModules.overMap.{u} R f).IsRightAdjoint
```

Declarations registered for the tag:

- [`SheafOfModules.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean#L91) (StacksFrontier): “extension-by-zero functor”. References: EGA IV (11.9.16), “more general”; EGA IV (2.5.1), “partial”; EGA IV (4.8.2), “more general”; EGA IV (9.4.9); SGA 3 I (4.6.1), “more general”; SGA 3 III (0.1.4), “more general”; SGA 4 VI (8.7.1), “partial”; SGA 4 XVII (4.1); SGA 7 XIV (4.5), “more general”.
- [`SheafOfModules.pullbackPushforwardAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullbackPushforwardAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean#L101) (StacksFrontier): “adjunction”. References: SGA 3 VIIA (1.3), “more general”.
- [`SheafOfModules.pullbackIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullbackIso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroAdjunction.lean#L103) (StacksFrontier): “sheafification”.
- [`Stacks.Sites.ExtensionByZero.sheafRestrictionIsRightAdjoint`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean#L234), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroDirectSumSheafification.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroDirectSumSheafification.lean#L65) (StacksFrontier): “restriction to C/U has a left adjoint”.

## Tag 0G1V, an equation

[Tag 0G1V](https://stacks.math.columbia.edu/tag/0G1V) in the Stacks Project.

**`Stacks.SheafOfModules.extensionByZeroUnitHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnit.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnit.lean#L342). The attribute's comment: “for the sheafified-free-module spelling of `j_{U!} O_U`”.

> Morphisms from the extension by zero of the structure sheaf of the localised site `C/U` to a
> sheaf of modules `N` are canonically the sections of `N` over `U`.

```lean
noncomputable def extensionByZeroUnitHomEquiv (R : Sheaf J RingCat.{w}) (U : C)
    (N : SheafOfModules.{max u₁ v₁ w t} R) :
    (extensionByZeroUnit.{u₁, v₁, w, t} R U ⟶ N) ≃ ToType (N.val.obj (op U))
```

**`Stacks.SheafOfModules.extensionByZeroUnitHomEquiv_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnit.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnit.lean#L359). The attribute's comment: “naturality in the target”.

> The bijection `extensionByZeroUnitHomEquiv` is natural in the target module.

```lean
lemma extensionByZeroUnitHomEquiv_naturality (R : Sheaf J RingCat.{w}) (U : C)
    {M N : SheafOfModules.{max u₁ v₁ w t} R}
    (ψ : extensionByZeroUnit.{u₁, v₁, w, t} R U ⟶ M) (φ : M ⟶ N) :
    extensionByZeroUnitHomEquiv.{u₁, v₁, w, t} R U N (ψ ≫ φ) =
      ((SheafOfModules.evaluation R (op U)).map φ)
        (extensionByZeroUnitHomEquiv.{u₁, v₁, w, t} R U M ψ)
```

**`Stacks.SheafOfModules.extensionByZeroUnitCorepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnit.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnit.lean#L376). The attribute's comment: “corepresentability”.

> The extension by zero of the structure sheaf of `C/U` corepresents the functor sending a
> sheaf of modules to its sections over `U`.

```lean
noncomputable def extensionByZeroUnitCorepresentableBy (R : Sheaf J RingCat.{w}) (U : C) :
    (SheafOfModules.evaluation R (op U) ⋙
        forget (ModuleCat.{max u₁ v₁ w t} (R.obj.obj (op U)))).CorepresentableBy
      (extensionByZeroUnit.{u₁, v₁, w, t} R U)
```

**`Stacks.Sites.OverModules.extensionByZeroUnitCorepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnitSliceComparison.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroUnitSliceComparison.lean#L77). The attribute's comment: “corepresentability of the extension-by-zero spelling”.

> **Stacks 0G1V as a corepresentability statement, for the extension by zero of the rank-one
> module.** `Stacks.Sites.OverModules.extensionByZeroUnit` corepresents the sections over `U`;
> this is `extensionByZeroHomEquiv` together with its naturality.

```lean
def extensionByZeroUnitCorepresentableBy (O : Sheaf J RingCat.{w}) (U : C) :
    (SheafOfModules.evaluation O (op U) ⋙
        forget (ModuleCat.{max u₁ v₁ w t} (O.obj.obj (op U)))).CorepresentableBy
      (extensionByZeroUnit.{v₁, u₁, w, t} J O U)
```

**`Stacks.Sites.ExtensionByZero.extensionByZeroUnitHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroUnitSections.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroUnitSections.lean#L75).

> **Stacks 0G1V.** Morphisms `j_{U!} O_U ⟶ F` are canonically the sections of `F` over `U`:
> transpose along the extension-by-zero adjunction, then read the resulting morphism out of the
> unit sheaf of modules on `C/U` as a section at the terminal object `U ⟶ U`.

```lean
noncomputable def extensionByZeroUnitHomEquiv (F : SheafOfModules.{w} R) :
    ((SheafOfModules.pullback.{w} (F := Over.forget U)
      (𝟙 (R.over U) : (R.over U) ⟶ (R.over U))).obj
        (SheafOfModules.unit (R.over U)) ⟶ F) ≃
      (F.val.obj (op U) : Type w)
```

**`Stacks.Sites.ExtensionByZero.extensionByZeroUnitHomEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroUnitSections.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroUnitSections.lean#L91). The attribute's comment: “naturality”.

> **Stacks 0G1V.** The identification of `Hom_O(j_{U!} O_U, F)` with `F(U)` is natural in
> `F`: composing with `g : F ⟶ G` corresponds to applying `g` to sections over `U`.

```lean
theorem extensionByZeroUnitHomEquiv_naturality {F G : SheafOfModules.{w} R}
    (f : (SheafOfModules.pullback.{w} (F := Over.forget U)
      (𝟙 (R.over U) : (R.over U) ⟶ (R.over U))).obj
        (SheafOfModules.unit (R.over U)) ⟶ F)
    (g : F ⟶ G) :
    extensionByZeroUnitHomEquiv J R U G (f ≫ g) =
      ((SheafOfModules.evaluation R (op U)).map g)
        (extensionByZeroUnitHomEquiv J R U F f)
```

## Tag 03DJ, a lemma

[Tag 03DJ](https://stacks.math.columbia.edu/tag/03DJ) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesFiniteLimits_etaleModuleLowerShriek`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModuleExtensionByZeroExact.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModuleExtensionByZeroExact.lean#L47). The attribute's comment: “left exactness for modules along an étale morphism of algebraic spaces”. References: SGA 4 IV (11.3.1), “partial”.

> Extension by zero of sheaves of modules along an étale morphism of algebraic spaces is left
> exact.

```lean
instance preservesFiniteLimits_etaleModuleLowerShriek :
    PreservesFiniteLimits (etaleModuleLowerShriek B S hS f hf)
```

**`AlgebraicGeometry.Space.etaleModuleLowerShriek_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleModuleExtensionByZeroExact.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleModuleExtensionByZeroExact.lean#L66). The attribute's comment: “exactness for modules along an étale morphism of algebraic spaces”.

> Extension by zero of sheaves of modules along an étale morphism of algebraic spaces is
> exact.

```lean
theorem etaleModuleLowerShriek_exact :
    exactFunctor _ _ (etaleModuleLowerShriek B S hS f hf)
```

**`AlgebraicGeometry.Space.preservesFiniteLimits_abelianEtaleExtensionByZero`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroExact.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroExact.lean#L97). The attribute's comment: “left exactness for abelian sheaves along an étale morphism of algebraic spaces”.

> Extension by zero of abelian sheaves along an étale morphism of algebraic spaces is left
> exact.

```lean
instance preservesFiniteLimits_abelianEtaleExtensionByZero :
    PreservesFiniteLimits (abelianEtaleExtensionByZero B S hS f hf)
```

**`AlgebraicGeometry.Space.abelianEtaleExtensionByZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroExact.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianExtensionByZeroExact.lean#L108). The attribute's comment: “exactness for abelian sheaves along an étale morphism of algebraic spaces”.

> Extension by zero of abelian sheaves along an étale morphism of algebraic spaces is
> exact.

```lean
theorem abelianEtaleExtensionByZero_exact :
    exactFunctor _ _ (abelianEtaleExtensionByZero B S hS f hf)
```

**`Stacks.Sites.ExtensionByZero.OverElements.extensionByZero_preservesMonomorphisms`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ElementSiteExtensionByZero.lean#L430). The attribute's comment: “for the site of elements of a presheaf of sets, monomorphisms”.

> Extension by zero along the projection of the site of elements preserves monomorphisms.

```lean
lemma extensionByZero_preservesMonomorphisms :
    Functor.PreservesMonomorphisms (SheafOfModules.pullback.{u}
      (F := proj K) (𝟙 (restrictedRingSheaf K J JD R) :
        (restrictedRingSheaf K J JD R) ⟶ (restrictedRingSheaf K J JD R)))
```

**`Stacks.Sites.ExtensionByZero.extensionByZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean#L394).

> **Stacks 03DJ.** Extension by zero of sheaves of modules along the localization `C/U ⟶ C`
> is exact.

```lean
theorem extensionByZero_exact :
    exactFunctor _ _ (SheafOfModules.pullback.{u}
      (F := Over.forget U) (𝟙 (R.over U) : (R.over U) ⟶ (R.over U)))
```

**`SheafOfModules.extensionByZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactnessGeneral.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactnessGeneral.lean#L137). The attribute's comment: “exactness of extension by zero, with the site, morphism, ring-section and module universes independent; this is the statement the semi-representable lower shrieks consume, their structure sheaves having sections in a universe larger than their sites”.

> **Stacks 03DJ.** Extension by zero of sheaves of modules along the localization `C/U ⟶ C`
> is exact, with the universe of the site, the universe of its morphisms, the universe of the
> sections of the sheaf of rings and the extra module universe all independent.

```lean
theorem extensionByZero_exact :
    exactFunctor _ _ (extensionByZero.{m, w, v, u} R U)
```

**`Stacks.Sites.ExtensionByZero.overMap_extensionByZero_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroOverMap.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroOverMap.lean#L120). The attribute's comment: “extension by zero along a relocalization C/V ⥤ C/U is exact”.

> **Stacks 03DJ for a relocalization.** Extension by zero of sheaves of modules along
> `Over.map f : C/V ⥤ C/U` is exact: it is the slice equivalence, which is exact, followed by
> extension by zero along the localization of `C/U` at `Over.mk f`, which is exact by
> Stacks 03DJ.

```lean
theorem overMap_extensionByZero_exact :
    exactFunctor _ _ (SheafOfModules.overMap.{u} R f).leftAdjoint
```

**`AlgebraicGeometry.RingedSite.familyComponentLowerShriek_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L413). The attribute's comment: “the extension by zero of a component of a semi-representable object”.

> **Stacks 03DJ.** The extension by zero `j_{i,!}` of a component is exact. This is the
> exactness of extension by zero along a localization `C / U ⥤ C`, which asks the site,
> its morphisms and the module sections to share a universe — the generality at which parts (1)
> and (2) of this tag are formalized, namely `RingedSite.{u, u, u}`.

```lean
theorem familyComponentLowerShriek_exact (X : RingedSite.{u, u, u})
    (K : FormalCoproduct.{u} X.C) (i : K.I) :
    exactFunctor _ _ (familyComponentLowerShriek X K i)
```

## Tag 0E8G, a lemma

[Tag 0E8G](https://stacks.math.columbia.edu/tag/0E8G) in the Stacks Project.

**`Stacks.Sites.ExtensionByZero.extensionByZero_exact_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean, line 790](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean#L790).

> **Stacks 0E8G.** Extension by zero from the slice site reflects, as well as preserves,
> exactness of complexes of sheaves of modules.

```lean
theorem extensionByZero_exact_iff
    (S : ShortComplex (SheafOfModules.{u} (R.over U))) :
    (S.map (SheafOfModules.pullback.{u} (F := Over.forget U)
      (𝟙 (R.over U) : (R.over U) ⟶ (R.over U)))).Exact ↔ S.Exact
```

**`Stacks.Sites.ExtensionByZero.OfEssentiallySmall.extensionByZero_exact_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactnessEssentiallySmall.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactnessEssentiallySmall.lean#L198). The attribute's comment: “for a site essentially u-small, objects in Type c, morphisms and modules in u”.

> Extension by zero from the slice site reflects, as well as preserves, exactness of
> complexes of sheaves of modules, over a site whose objects need not lie in the universe of its
> morphisms: objects in an arbitrary universe `c`, morphisms and modules in `u`, and `C`
> essentially `u`-small.

```lean
theorem extensionByZero_exact_iff
    (S : ShortComplex (SheafOfModules.{u} (R.over U))) :
    (S.map (SheafOfModules.pullback.{u} (F := Over.forget U)
      (𝟙 (R.over U) : (R.over U) ⟶ (R.over U)))).Exact ↔ S.Exact
```

**`Stacks.Sites.ExtensionByZero.FreeModuleUniverse.extensionByZero_exact_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactnessFreeModuleUniverse.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactnessFreeModuleUniverse.lean#L323). The attribute's comment: “objects in Type u, morphisms in v, ring sections in w, modules in max v a”.

> **Stacks 0E8G at a free module universe.** Extension by zero from the slice site reflects,
> as well as preserves, exactness of complexes of sheaves of modules, over a site whose module
> sections need not lie in the universe of its morphisms.
>
> The attribute records the universe shape: the objects of `C` in an arbitrary universe `u`, its
> morphisms in `v`, the sections of `R` in `w` and the module sections in `max v a`. The tag is
> carried in full by `Stacks.Sites.ExtensionByZero.extensionByZero_exact_iff`, the
> single-universe statement, which this one generalises; that registration stands and this one
> does not replace it.

```lean
theorem extensionByZero_exact_iff
    (S : ShortComplex (SheafOfModules.{max v a} (R.over U))) :
    (S.map (SheafOfModules.pullback.{max v a} (F := Over.forget U)
      (𝟙 (R.over U) : R.over U ⟶ R.over U))).Exact ↔ S.Exact
```

## Tag 04IY, a lemma

[Tag 04IY](https://stacks.math.columbia.edu/tag/04IY) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.relocalizationRingedToposHom_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean#L63). The attribute's comment: “structure map of localization at V/U”.

> **Stacks 04IY.** The structure map of the relocalization along `f : V ⟶ U`, in
> inverse-image form and on sheaves of commutative rings, is the canonical comparison of the
> inverse image of `O|_U` with its restriction along `Over.map f`, followed by the change-of-slice
> identification of that restriction with `O|_V`.

```lean
theorem relocalizationRingedToposHom_fSharpInverseImage :
    (X.relocalizationRingedToposHom f).fSharpInverseImage =
      (restrictionCommRingIso (X.J.over V) (X.J.over U) (Over.map f) (X.O.over U)).hom ≫
        (X.O.pushforwardOverMapIso f).hom
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSite.relocalizationRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/RingedLocalization/Relocalization.lean#L386), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean#L81) (StacksFrontier): “relocalization morphism”.
- [`AlgebraicGeometry.RingedSite.overMap_inverseImage_iteratedSlice`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/RingedLocalization/Relocalization.lean#L295), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean#L84) (StacksFrontier): “identification with localization at V/U”.
- [`AlgebraicGeometry.RingedSite.iteratedSlice_structureSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/RingedLocalization/Relocalization.lean#L329), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean#L87) (StacksFrontier): “structure sheaf under iterated slice”.
- [`AlgebraicGeometry.RingedSite.localizationMorphism_comp_relocalizationMorphism`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/RingedLocalization/Relocalization.lean#L503), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean#L90) (StacksFrontier): “commutative triangle”.
- [`CategoryTheory.instIsContinuousOverLeftIteratedSliceForwardOver`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.instIsContinuousOverLeftIteratedSliceForwardOver#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/RelocalizationTriangle.lean#L93) (StacksFrontier): “iterated-slice site equivalence”.

## Tag 08P4, a remark

[Tag 08P4](https://stacks.math.columbia.edu/tag/08P4) in the Stacks Project.

**`Stacks.Sites.ExtensionByZero.extensionByZeroCompToSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroExactness.lean#L436).

> **Stacks 08P4.** Extension by zero commutes with forgetting the module structure: the
> square formed by extension by zero for modules, extension by zero for abelian sheaves and the
> two forgetful functors commutes up to natural isomorphism.

```lean
noncomputable def extensionByZeroCompToSheafIso :
    SheafOfModules.pullback.{u}
        (F := Over.forget U) (S := R.over U) (R := R)
        (𝟙 (R.over U)) ⋙ SheafOfModules.toSheaf.{u} R ≅
      SheafOfModules.toSheaf.{u} (R.over U) ⋙
        Functor.sheafPullbackConstruction.sheafPullback
          (Over.forget U) AddCommGrpCat.{u} (J.over U) J
```

## Tag 03EJ, a remark

[Tag 03EJ](https://stacks.math.columbia.edu/tag/03EJ) in the Stacks Project.

**`Stacks.Sites.OverModules.restrictionFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean#L92). The attribute's comment: “`j_U^* : PMod(O) ⥤ PMod(O_U)`”.

> Restriction of presheaves of modules along `Over.forget U`, i.e. `j_U^*`.

```lean
abbrev restrictionFunctor (O : Cᵒᵖ ⥤ RingCat.{w}) (U : C) :
    PresheafOfModules.{a, v, u, w} O ⥤
      PresheafOfModules.{a, v, max u v, w} (overRingPresheaf O U)
```

**`Stacks.Sites.OverModules.extensionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean#L260). The attribute's comment: “`j_{U!} : PMod(O_U) ⥤ PMod(O)`”.

> Extension of presheaves of modules from the slice category over `U`, as a functor: the
> functor `j_{U!}` whose value at `M` is the direct-sum presheaf `extensionPresheaf O U M` and
> whose action on morphisms is forced by the hom-set bijection `extensionHomEquiv`.

```lean
noncomputable def extensionFunctor :
    PresheafOfModules.{a, v, max u v, w} (overRingPresheaf O U) ⥤
      PresheafOfModules.{a, v, u, w} O
```

**`Stacks.Sites.OverModules.extensionFunctorAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean#L269). The attribute's comment: “`j_{U!}` is left adjoint to `j_U^*`”.

> Extension from the slice category is left adjoint to restriction.

```lean
noncomputable def extensionFunctorAdjunction :
    extensionFunctor.{v, u, w, a} O U ⊣ restrictionFunctor O U
```

**`Stacks.Sites.OverModules.directImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean#L595). The attribute's comment: “`j_{U*} : PMod(O_U) ⥤ PMod(O)`”.

> The direct-image functor `j_{U*}` on presheaves of modules.

```lean
noncomputable def directImage :
    PresheafOfModules.{a, v, max u v, w} (overRingPresheaf O U) ⥤
      PresheafOfModules.{a, v, u, w} O
```

**`Stacks.Sites.OverModules.restrictionDirectImageAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean, line 824](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean#L824). The attribute's comment: “`j_{U*}` is right adjoint to `j_U^*`”.

> Restriction along `Over.forget U` is left adjoint to the direct image.

```lean
noncomputable def restrictionDirectImageAdjunction :
    restrictionFunctor O U ⊣ directImage O U
```

**`Stacks.Sites.OverModules.presheafModuleAdjunctionsOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean, line 876](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceAdjunctions.lean#L876). The attribute's comment: “the adjoint triple `j_{U!} ⊣ j_U^* ⊣ j_{U*}`”.

> Restriction of presheaves of modules to `C/U` has both an extension left adjoint and a
> direct-image right adjoint: the coproduct construction `extensionFunctor` and the limit
> construction `directImage`, with their adjunctions.

```lean
noncomputable def presheafModuleAdjunctionsOver (O : Cᵒᵖ ⥤ RingCat.{w}) (U : C) :
    PresheafModuleAdjunctionsOver.{v, u, w, m} O U
```

**`Stacks.Sites.OverModules.extension_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceExtensionExact.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceExtensionExact.lean#L168). The attribute's comment: “`j_{U!}` is exact”.

> **Stacks 03EJ.** Extension of presheaves of modules from a slice category is exact.

```lean
theorem extension_exact (A : PresheafModuleAdjunctionsOver.{v, u, w, m} O U) :
    exactFunctor
      (PresheafOfModules.{max u v m} (overRingPresheaf O U))
      (PresheafOfModules.{max u v m} O) A.extension
```

**`Stacks.Sites.OverModules.extensionObjLinearEquivDirectSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceExtensionFormula.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/SliceExtensionFormula.lean#L293). The attribute's comment: “`j_{U!}G : V ↦ ⨁_{φ ∈ Mor(V, U)} G(V →^φ U)`”.

> Extension of a presheaf of modules from `C/U` has, at `V`, the direct sum of its values
> on all arrows `V ⟶ U`. These identifications commute with every restriction map.

```lean
theorem extensionObjLinearEquivDirectSum (O : Cᵒᵖ ⥤ RingCat.{w}) (U : C)
    (A : PresheafModuleAdjunctionsOver.{v, u, w, m} O U)
    (G : PresheafOfModules.{max u v m} (overRingPresheaf O U)) :
    ∃ e : ∀ V : C,
        (A.extension.obj G).obj (op V) ≃ₗ[O.obj (op V)]
          extensionFormula.{v, u, w, max u m} O U V G,
      ∀ {V W : C} (f : V ⟶ W) (x : (A.extension.obj G).obj (op W)),
        e V ((A.extension.obj G).map f.op x) =
          extensionFormulaMap.{v, u, w, max u m} O U G f (e W x)
```

**`Stacks.Sites.OverModules.extensionSheafificationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroSheafification.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExtensionByZeroSheafification.lean#L101). The attribute's comment: “the square `j_{U!} ∘ forget = ( )^# ∘ j_{U!}`”.

> Extension by zero of a sheaf of modules is naturally the sheafification of its extension
> as a presheaf of modules from the slice category over `U`.

```lean
noncomputable def extensionSheafificationIso :
    SheafOfModules.pullback.{u}
        (F := Over.forget U) (𝟙 (R.over U) : (R.over U) ⟶ (R.over U)) ≅
      SheafOfModules.forget.{u} (R.over U) ⋙ A.extension ⋙
        PresheafOfModules.sheafification (𝟙 R.obj)
```

## Tag 0F6Z, a lemma

[Tag 0F6Z](https://stacks.math.columbia.edu/tag/0F6Z) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.isIso_unit_and_counit_of_isSubterminal_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/MoreLocalization.lean#L106).

> Let `C` be a site and `U` an object of `C` such that every object of `C` has at most one
> morphism to `U`. For an abelian sheaf `F` on `C/U` the canonical maps
> `F ⟶ j_U^{-1}j_{U!}F` and `j_U^{-1}j_{U*}F ⟶ F` are isomorphisms.

```lean
public theorem isIso_unit_and_counit_of_isSubterminal_addCommGrpCat {C : Type u}
    [Category.{v} C] (J : GrothendieckTopology C) (U : C) (hU : IsSubterminal U)
    [∀ (F : (Over U)ᵒᵖ ⥤ AddCommGrpCat.{w}),
      (Over.forget U).op.HasPointwiseRightKanExtension F]
    {L : Sheaf (J.over U) AddCommGrpCat.{w} ⥤ Sheaf J AddCommGrpCat.{w}}
    (adj : L ⊣ J.overPullback AddCommGrpCat.{w} U) :
    IsIso adj.unit ∧
      IsIso ((Over.forget U).sheafAdjunctionCocontinuous AddCommGrpCat.{w}
        (J.over U) J).counit
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.19, Tag 03DH](https://stacks.math.columbia.edu/tag/03DH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
