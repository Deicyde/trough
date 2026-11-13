---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.toLocalizationSheaf, AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.isUnit_toLocalizationSheaf, AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.existsUnique_lift_toLocalizationSheaf, AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.existsUnique_lift_localizationModuleSheaf, AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.localizationModuleSheafIsoTensor, AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.unit_comp_localizationModuleSheafIsoTensor
statement: formalized
proof: formalized
---

# 18.44 Localizing sheaves of rings

Section 18.44 of the Stacks Project, [Tag 0EMB](https://stacks.math.columbia.edu/tag/0EMB). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EMC, a lemma

[Tag 0EMC](https://stacks.math.columbia.edu/tag/0EMC) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.toLocalizationSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/StructureSheafLocalization.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/StructureSheafLocalization.lean#L110). The attribute's comment: “canonical homomorphism of sheaves of rings”.

> The canonical map from the ring sheaf to the sheafified localization.

```lean
noncomputable def toLocalizationSheaf (S : MultiplicativeSubpresheaf X)
    [HasWeakSheafify X.J CommRingCat.{w}] :
    X.O ⟶ (presheafToSheaf X.J CommRingCat.{w}).obj S.localizationPresheaf
```

**`AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.isUnit_toLocalizationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/StructureSheafLocalization.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/StructureSheafLocalization.lean#L154). The attribute's comment: “inversion of the prescribed sections”.

> The canonical map sends each prescribed section to a unit.

```lean
theorem isUnit_toLocalizationSheaf (S : MultiplicativeSubpresheaf X)
    [HasWeakSheafify X.J CommRingCat.{w}]
    (U : X.Cᵒᵖ) (s : S.obj U) :
    IsUnit (((S.toLocalizationSheaf).hom.app U).hom (s : X.O.obj.obj U))
```

**`AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.existsUnique_lift_toLocalizationSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/StructureSheafLocalization.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/StructureSheafLocalization.lean#L165). The attribute's comment: “universal property”.

> A morphism inverting every prescribed section factors uniquely through the
> sheafified sectionwise localization.

```lean
theorem existsUnique_lift_toLocalizationSheaf (S : MultiplicativeSubpresheaf X)
    [HasWeakSheafify X.J CommRingCat.{w}]
    (A : Sheaf X.J CommRingCat.{w}) (f : X.O ⟶ A)
    (hf : ∀ (U : X.Cᵒᵖ) (s : S.obj U),
      IsUnit ((f.hom.app U).hom (s : X.O.obj.obj U))) :
    ∃! g : (presheafToSheaf X.J CommRingCat.{w}).obj S.localizationPresheaf ⟶ A,
      S.toLocalizationSheaf ≫ g = f
```

## Tag 0EMD, a lemma

[Tag 0EMD](https://stacks.math.columbia.edu/tag/0EMD) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.existsUnique_lift_localizationModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ModuleSheafLocalization.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/ModuleSheafLocalization.lean#L443). The attribute's comment: “localization\_universal\_property”. References: EGA 0 (1.2.4), “more general”.

> **The universal property of `(S⁻¹F)^#`.**  A map of sheaves of `O_X`-modules `φ : F ⟶ G`
> such that each prescribed local section of `S` acts invertibly on `G` factors uniquely through
> the canonical map `F ⟶ (S⁻¹F)^#`.

```lean
theorem existsUnique_lift_localizationModuleSheaf
    {F G : SheafOfModules.{max w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)} (φ : F ⟶ G)
    (hG : ∀ (U : X.Cᵒᵖ) (s : S.obj U),
      letI : Module (X.O.obj.obj U) (G.val.obj U) := (G.val.obj U).isModule
      Function.Bijective fun t : G.val.obj U ↦ (s : X.O.obj.obj U) • t) :
    ∃! ψ : S.localizationModuleSheaf F ⟶ G, S.toLocalizationModuleSheaf F ≫ ψ = φ
```

**`AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.localizationModuleSheafIsoTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ModuleSheafLocalization.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/ModuleSheafLocalization.lean#L478). The attribute's comment: “localization\_tensor\_iso”.

> **`(S⁻¹F)^# = (S⁻¹O_X)^# ⊗_{O_X} F` as sheaves of `(S⁻¹O_X)^#`-modules.**  The
> sheafification of the sectionwise localization of `F` is the extension of scalars of `F` along
> `O_X ⟶ (S⁻¹O_X)^#`.

```lean
def localizationModuleSheafIsoTensor
    (F : SheafOfModules.{max w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (PresheafOfModules.sheafification σ).obj (S.localizationModulePresheaf F.val) ≅
      (SheafOfModules.pullback (S.localizationRingSheafHom σ)).obj F
```

**`AlgebraicGeometry.RingedSite.MultiplicativeSubpresheaf.unit_comp_localizationModuleSheafIsoTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ModuleSheafLocalization.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/ModuleSheafLocalization.lean#L489). The attribute's comment: “localization\_tensor\_iso”.

> The identification `(S⁻¹F)^# = (S⁻¹O_X)^# ⊗_{O_X} F` is compatible with the canonical maps
> out of `F`: the unit of the pullback--pushforward adjunction corresponds to the sectionwise
> localization map followed by the sheafification unit.

```lean
theorem unit_comp_localizationModuleSheafIsoTensor
    (F : SheafOfModules.{max w z} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (SheafOfModules.pullbackPushforwardAdjunction
        (S.localizationRingSheafHom σ)).unit.app F ≫
      (SheafOfModules.pushforward (S.localizationRingSheafHom σ)).map
        (S.localizationModuleSheafIsoTensor σ F).inv =
      toPushforwardSheafification _ σ (changeOfRingsAdjunction S.toLocalizationPresheaf) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.44, Tag 0EMB](https://stacks.math.columbia.edu/tag/0EMB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
