---
declaration: section
origin: cited
lean: Stacks.Presheaf.Localization.isLocalization_stalk_localizationSheaf, Stacks.Presheaf.Localization.existsUnique_lift_localizationPresheaf, Stacks.Presheaf.Localization.toLocalizationSheaf, Stacks.Presheaf.Localization.isUnit_toLocalizationSheaf, Stacks.Presheaf.Localization.existsUnique_lift_localizationSheaf, Stacks.Presheaf.Localization.localizationPresheaf_stalk_isLocalization, TopCat.Presheaf.SubmonoidPresheaf.toLocalizationPresheaf, IsLocalization.map_units
statement: formalized
proof: formalized
---

# 17.27 Localizing sheaves of rings

Section 17.27 of the Stacks Project, [Tag 01CZ](https://stacks.math.columbia.edu/tag/01CZ). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01D0, a lemma

[Tag 01D0](https://stacks.math.columbia.edu/tag/01D0) in the Stacks Project.

**`Stacks.Presheaf.Localization.isLocalization_stalk_localizationSheaf`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean#L177). The attribute's comment: “sheaf\_localization\_stalk”.

> At every point, the stalk of the sheafification of the sectionwise localization is the
> localization of the original stalk at the germs of the prescribed denominators.

```lean
lemma isLocalization_stalk_localizationSheaf (D : PresheafLocalizationData.{u}) (x : D.X) :
    letI : Algebra (D.O.stalk x) ((localizationSheaf D).presheaf.stalk x) :=
      (toLocalizationSheafStalk D x).hom.toAlgebra
    IsLocalization (D.S.stalk x) ((localizationSheaf D).presheaf.stalk x)
```

**`Stacks.Presheaf.Localization.existsUnique_lift_localizationPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L80). The attribute's comment: “presheaf\_universal\_property”. References: EGA 0 (1.2.4), “more general”.

> **Stacks 01D0.** A morphism of presheaves of commutative rings which inverts every section
> of the multiplicative subpresheaf `S` factors uniquely through the sectionwise localization at
> `S`.

```lean
theorem existsUnique_lift_localizationPresheaf (S : O.SubmonoidPresheaf) (f : O ⟶ A)
    (hf : ∀ (U : (Opens X)ᵒᵖ) (s : S.obj U), IsUnit ((f.app U).hom (s : O.obj U))) :
    ∃! g : S.localizationPresheaf ⟶ A, S.toLocalizationPresheaf ≫ g = f
```

**`Stacks.Presheaf.Localization.toLocalizationSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L112). The attribute's comment: “sheaf\_universal\_property”.

> The canonical map from the sheafification of a presheaf of commutative rings to the
> sheafification of its sectionwise localization.

```lean
noncomputable def toLocalizationSheaf (S : O.SubmonoidPresheaf) :
    (presheafToSheaf (Opens.grothendieckTopology X) CommRingCat.{u}).obj O ⟶
      (presheafToSheaf (Opens.grothendieckTopology X) CommRingCat.{u}).obj
        S.localizationPresheaf
```

**`Stacks.Presheaf.Localization.isUnit_toLocalizationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L130). The attribute's comment: “sheaf\_universal\_property”.

> **Stacks 01D0.** Every prescribed local denominator becomes invertible in the sheafified
> localization.

```lean
theorem isUnit_toLocalizationSheaf (S : O.SubmonoidPresheaf) (U : (Opens X)ᵒᵖ) (s : S.obj U) :
    IsUnit (((toLocalizationSheaf S).hom.app U).hom
      (((toSheafify (Opens.grothendieckTopology X) O).app U).hom (s : O.obj U)))
```

**`Stacks.Presheaf.Localization.existsUnique_lift_localizationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L140). The attribute's comment: “sheaf\_universal\_property”.

> **Stacks 01D0.** A morphism out of the sheafification of `O` which inverts every prescribed
> section factors uniquely through the sheafified localization.

```lean
theorem existsUnique_lift_localizationSheaf (S : O.SubmonoidPresheaf) (A : X.Sheaf CommRingCat.{u})
    (f : (presheafToSheaf (Opens.grothendieckTopology X) CommRingCat.{u}).obj O ⟶ A)
    (hf : ∀ (U : (Opens X)ᵒᵖ) (s : S.obj U),
      IsUnit ((f.hom.app U).hom
        (((toSheafify (Opens.grothendieckTopology X) O).app U).hom (s : O.obj U)))) :
    ∃! g : (presheafToSheaf (Opens.grothendieckTopology X) CommRingCat.{u}).obj
        S.localizationPresheaf ⟶ A,
      toLocalizationSheaf S ≫ g = f
```

Declarations registered for the tag:

- [`Stacks.Presheaf.Localization.localizationPresheaf_stalk_isLocalization`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean#L202) (StacksFrontier): “presheaf\_localization\_stalk: the stalk of the localization presheaf”.
- [`TopCat.Presheaf.SubmonoidPresheaf.toLocalizationPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.SubmonoidPresheaf.toLocalizationPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L168) (StacksFrontier): “localization\_map: the canonical morphism to the sectionwise localization”.
- [`IsLocalization.map_units`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.map_units#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L170) (StacksFrontier): “localization\_map: every prescribed section becomes a unit”.

## Tag 01D1, a lemma

[Tag 01D1](https://stacks.math.columbia.edu/tag/01D1) in the Stacks Project.

**`Stacks.Presheaf.Localization.isoTensorOfIsSectionwiseLocalizedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean#L338). The attribute's comment: “presheaf assertion, in every universe”.

> **Stacks Project, Tag 01D1, presheaf assertion.**
>
> Any sectionwise localization of a presheaf of modules is canonically isomorphic to extension
> of scalars from the original presheaf of rings to its sectionwise localization. The space, the
> rings and the modules live in an arbitrary universe `u`.

```lean
noncomputable def isoTensorOfIsSectionwiseLocalizedModule {X : TopCat.{u}}
    (O Oₛ : TopCat.Presheaf CommRingCat.{u} X) (α : O ⟶ Oₛ)
    (S : (U : (TopologicalSpace.Opens X)ᵒᵖ) → Submonoid (O.obj U))
    (F : PresheafOfModules.{u} (ringPresheaf O))
    (Fₛ : PresheafOfModules.{u} (ringPresheaf Oₛ))
    (ι : F ⟶ Stacks.Sheafify.ChangeOfRingsAdjunction.restrictPresheaf O Oₛ α Fₛ)
    (hO : IsSectionwiseLocalization O Oₛ α S)
    (hF : IsSectionwiseLocalizedModule O Oₛ α S F Fₛ ι) :
    Fₛ ≅ tensorPresheafOfModules O Oₛ α F
```

**`Stacks.Presheaf.Localization.sheafificationIsoTensorOfIsSectionwiseLocalizedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean#L389). The attribute's comment: “sheaf assertion, in every universe”.

> **Stacks Project, Tag 01D1, sheaf assertion.**
>
> If `O` and `F` are sheaves, sheafifying a sectionwise localization `Fₛ` along a
> sheafification `Oₛ ⟶ Oₛ♯` gives the tensor product of `F` with `Oₛ♯` over `O`. The space, the
> rings and the modules live in an arbitrary universe `u`.

```lean
noncomputable def sheafificationIsoTensorOfIsSectionwiseLocalizedModule {X : TopCat.{u}}
    (O : TopCat.Sheaf CommRingCat.{u} X) (Oₛ : TopCat.Presheaf CommRingCat.{u} X)
    (Oₛ' : TopCat.Sheaf CommRingCat.{u} X) (α : O.presheaf ⟶ Oₛ) (σ : Oₛ ⟶ Oₛ'.presheaf)
    (S : (U : (TopologicalSpace.Opens X)ᵒᵖ) → Submonoid (O.presheaf.obj U))
    (F : SheafOfModules.{u} (ringSheaf O))
    (Fₛ : PresheafOfModules.{u} (ringPresheaf Oₛ))
    (ι : F.val ⟶ Stacks.Sheafify.ChangeOfRingsAdjunction.restrictPresheaf O.presheaf Oₛ α Fₛ)
    (hO : IsSectionwiseLocalization O.presheaf Oₛ α S)
    (hF : IsSectionwiseLocalizedModule O.presheaf Oₛ α S F.val Fₛ ι)
    (hσi : Presheaf.IsLocallyInjective (Opens.grothendieckTopology X)
      (Stacks.Sheafify.ChangeOfRingsAdjunction.ringPresheafMap Oₛ Oₛ'.presheaf σ))
    (hσs : Presheaf.IsLocallySurjective (Opens.grothendieckTopology X)
      (Stacks.Sheafify.ChangeOfRingsAdjunction.ringPresheafMap Oₛ Oₛ'.presheaf σ)) :
    (moduleSheafificationAlong' (Stacks.Sheafify.ChangeOfRingsAdjunction.ringPresheafMap Oₛ
      Oₛ'.presheaf σ) hσi hσs).obj Fₛ ≅
      tensorSheaf O Oₛ'
        ((fullyFaithfulSheafToPresheaf (Opens.grothendieckTopology X) CommRingCat.{u}).homEquiv.symm
          (α ≫ σ)) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.27, Tag 01CZ](https://stacks.math.columbia.edu/tag/01CZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
