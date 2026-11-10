---
declaration: section
origin: cited
lean: Stacks.Presheaf.Localization.isLocalization_stalk_localizationSheaf, Stacks.Presheaf.Localization.existsUnique_lift_localizationPresheaf, Stacks.Presheaf.Localization.toLocalizationSheaf, Stacks.Presheaf.Localization.isUnit_toLocalizationSheaf, Stacks.Presheaf.Localization.existsUnique_lift_localizationSheaf, Stacks.Presheaf.Localization.localizationPresheaf_stalk_isLocalization, TopCat.Presheaf.SubmonoidPresheaf.toLocalizationPresheaf, IsLocalization.map_units
statement: formalized
proof: formalized
---

# 17.27 Localizing sheaves of rings

Section 17.27 of the Stacks Project, [Tag 01CZ](https://stacks.math.columbia.edu/tag/01CZ). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01D0, a lemma

[Tag 01D0](https://stacks.math.columbia.edu/tag/01D0) in the Stacks Project.

**`Stacks.Presheaf.Localization.isLocalization_stalk_localizationSheaf`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean#L177). The attribute's comment: “sheaf_localization_stalk”.

> At every point, the stalk of the sheafification of the sectionwise localization is the
> localization of the original stalk at the germs of the prescribed denominators.

```lean
lemma isLocalization_stalk_localizationSheaf (D : PresheafLocalizationData.{u}) (x : D.X) :
    letI : Algebra (D.O.stalk x) ((localizationSheaf D).presheaf.stalk x) :=
      (toLocalizationSheafStalk D x).hom.toAlgebra
    IsLocalization (D.S.stalk x) ((localizationSheaf D).presheaf.stalk x)
```

**`Stacks.Presheaf.Localization.existsUnique_lift_localizationPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L80). The attribute's comment: “presheaf_universal_property”. References: EGA 0 (1.2.4), “more general”.

> **Stacks 01D0.** A morphism of presheaves of commutative rings which inverts every section
> of the multiplicative subpresheaf `S` factors uniquely through the sectionwise localization at
> `S`.

```lean
theorem existsUnique_lift_localizationPresheaf (S : O.SubmonoidPresheaf) (f : O ⟶ A)
    (hf : ∀ (U : (Opens X)ᵒᵖ) (s : S.obj U), IsUnit ((f.app U).hom (s : O.obj U))) :
    ∃! g : S.localizationPresheaf ⟶ A, S.toLocalizationPresheaf ≫ g = f
```

**`Stacks.Presheaf.Localization.toLocalizationSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L112). The attribute's comment: “sheaf_universal_property”.

> The canonical map from the sheafification of a presheaf of commutative rings to the
> sheafification of its sectionwise localization.

```lean
noncomputable def toLocalizationSheaf (S : O.SubmonoidPresheaf) :
    (presheafToSheaf (Opens.grothendieckTopology X) CommRingCat.{u}).obj O ⟶
      (presheafToSheaf (Opens.grothendieckTopology X) CommRingCat.{u}).obj
        S.localizationPresheaf
```

**`Stacks.Presheaf.Localization.isUnit_toLocalizationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L130). The attribute's comment: “sheaf_universal_property”.

> **Stacks 01D0.** Every prescribed local denominator becomes invertible in the sheafified
> localization.

```lean
theorem isUnit_toLocalizationSheaf (S : O.SubmonoidPresheaf) (U : (Opens X)ᵒᵖ) (s : S.obj U) :
    IsUnit (((toLocalizationSheaf S).hom.app U).hom
      (((toSheafify (Opens.grothendieckTopology X) O).app U).hom (s : O.obj U)))
```

**`Stacks.Presheaf.Localization.existsUnique_lift_localizationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L140). The attribute's comment: “sheaf_universal_property”.

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

- [`Stacks.Presheaf.Localization.localizationPresheaf_stalk_isLocalization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationStalk.lean#L202) (StacksFrontier): “presheaf_localization_stalk: the stalk of the localization presheaf”.
- [`TopCat.Presheaf.SubmonoidPresheaf.toLocalizationPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.SubmonoidPresheaf.toLocalizationPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L168) (StacksFrontier): “localization_map: the canonical morphism to the sectionwise localization”.
- [`IsLocalization.map_units`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.map_units#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationUniversalProperty.lean#L170) (StacksFrontier): “localization_map: every prescribed section becomes a unit”.

## Tag 01D1, a lemma

[Tag 01D1](https://stacks.math.columbia.edu/tag/01D1) in the Stacks Project.

**`Stacks.Presheaf.Localization.sectionwiseLocalizedModuleIsoTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean#L245). The attribute's comment: “presheaf assertion”.

> **Stacks Project, Tag 01D1, presheaf assertion.**
>
> Any sectionwise localization of a presheaf of modules is canonically isomorphic to extension
> of scalars from the original presheaf of rings to its sectionwise localization.

```lean
noncomputable def sectionwiseLocalizedModuleIsoTensor
    (O Oₛ : TopCat.Presheaf CommRingCat X) (α : O ⟶ Oₛ)
    (S : (U : (TopologicalSpace.Opens X)ᵒᵖ) → Submonoid (O.obj U))
    (F : PresheafOfModules.{0} (ringPresheaf O))
    (Fₛ : PresheafOfModules.{0} (ringPresheaf Oₛ))
    (ι : F ⟶ Stacks.Sheafify.ChangeOfRingsAdjunction.restrictPresheaf O Oₛ α Fₛ)
    (hO : IsSectionwiseLocalization O Oₛ α S)
    (hF : IsSectionwiseLocalizedModule O Oₛ α S F Fₛ ι) :
    Fₛ ≅ tensorPresheafOfModules O Oₛ α F
```

**`Stacks.Presheaf.Localization.sheafificationSectionwiseLocalizedModuleIsoTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/LocalizationModule.lean#L295). The attribute's comment: “sheaf assertion”.

> **Stacks Project, Tag 01D1, sheaf assertion.**
>
> If `O` and `F` are sheaves, sheafifying a sectionwise localization `Fₛ` along a
> sheafification `Oₛ ⟶ Oₛ♯` gives the tensor product of `F` with `Oₛ♯` over `O`.

```lean
noncomputable def sheafificationSectionwiseLocalizedModuleIsoTensor
    (O : TopCat.Sheaf CommRingCat X) (Oₛ : TopCat.Presheaf CommRingCat X)
    (Oₛ' : TopCat.Sheaf CommRingCat X) (α : O.presheaf ⟶ Oₛ) (σ : Oₛ ⟶ Oₛ'.presheaf)
    (S : (U : (TopologicalSpace.Opens X)ᵒᵖ) → Submonoid (O.presheaf.obj U))
    (F : SheafOfModules (ringSheaf O))
    (Fₛ : PresheafOfModules (ringPresheaf Oₛ))
    (ι : F.val ⟶ Stacks.Sheafify.ChangeOfRingsAdjunction.restrictPresheaf O.presheaf Oₛ α Fₛ)
    (hO : IsSectionwiseLocalization O.presheaf Oₛ α S)
    (hF : IsSectionwiseLocalizedModule O.presheaf Oₛ α S F.val Fₛ ι)
    (hσi : Presheaf.IsLocallyInjective (Opens.grothendieckTopology X)
      (Stacks.Sheafify.ChangeOfRingsAdjunction.ringPresheafMap Oₛ Oₛ'.presheaf σ))
    (hσs : Presheaf.IsLocallySurjective (Opens.grothendieckTopology X)
      (Stacks.Sheafify.ChangeOfRingsAdjunction.ringPresheafMap Oₛ Oₛ'.presheaf σ)) :
    (moduleSheafificationAlong (Stacks.Sheafify.ChangeOfRingsAdjunction.ringPresheafMap Oₛ
      Oₛ'.presheaf σ) hσi hσs).obj Fₛ ≅
      tensorSheaf O Oₛ'
        ((fullyFaithfulSheafToPresheaf (Opens.grothendieckTopology X) CommRingCat).homEquiv.symm
          (α ≫ σ)) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.27, Tag 01CZ](https://stacks.math.columbia.edu/tag/01CZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
