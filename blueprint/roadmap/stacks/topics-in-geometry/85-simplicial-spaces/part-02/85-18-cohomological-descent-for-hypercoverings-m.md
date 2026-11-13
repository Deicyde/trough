---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isCartesianModule_of_mem_essImage, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.faithful_pullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.full_pullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.fullyFaithfulPullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.essImage_pullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.mem_essImage_pullbackModules_iff_isCartesianModule, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_unit, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_counit_app
statement: formalized
proof: formalized
---

# 85.18 Cohomological descent for hypercoverings: modules

Section 85.18 of the Stacks Project, [Tag 0D9Y](https://stacks.math.columbia.edu/tag/0D9Y). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D9Z, a lemma

[Tag 0D9Z](https://stacks.math.columbia.edu/tag/0D9Z) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isCartesianModule_of_mem_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L148). The attribute's comment: “the essential image of a^* consists of cartesian O-modules. Faithfulness of a^* is `faithful_pullbackModules`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a\_* a quasi-inverse, are not proved”.

> **Stacks 0D9Z, the inclusion of the essential image in the cartesian modules.** Every sheaf
> of `O`-modules on the total site isomorphic to a pullback `a^*F` along the ringed augmentation is
> a cartesian `O`-module.
>
> This is Stacks 0D7H (3) together with invariance of the cartesian condition under isomorphism.

```lean
theorem isCartesianModule_of_mem_essImage
    {F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf A.O)}
    (hF : A.totalRingedHom.toModulesHom.pullbackModules.essImage F) :
    S.IsModuleFiberTransitionIso A.O F
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.faithful_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L271). The attribute's comment: “a^* on sheaves of modules is faithful, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C. The essential-image inclusion is `isCartesianModule_of_mem_essImage`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a\_* a quasi-inverse, are not proved”.

> **Stacks 0D9Z, the faithfulness half.** Let `C` be a site with equalizers and fibre products,
> `K` a hypercovering of its final presheaf, and `a` the augmentation of the total site of `K`
> towards `C`. For a ringed augmentation along `a` whose structure map is the identification
> `O = a^{-1}O_C` of Stacks 0D9W, the pullback `a^* : Mod(O_C) ⥤ Mod(O)` of sheaves of modules is
> faithful.
>
> Because the structure map is that identification, the underlying sheaf of sets of `a^*M` is the
> inverse image of the underlying sheaf of `M`; faithfulness then descends from Stacks 0D8E (1),
> faithfulness of `a^{-1}` on sheaves of sets.

```lean
theorem faithful_pullbackModules [IsIso A.totalRingedHom.fSharpInverseImage] :
    A.totalRingedHom.toModulesHom.pullbackModules.Faithful
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.full_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L284). The attribute's comment: “a^* on sheaves of modules is full, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C”.

> **Stacks 0D9Z, the fullness half.** For a ringed augmentation of a hypercovering whose
> structure map is the identification `O = a^{-1}O_C` of Stacks 0D9W, the pullback
> `a^* : Mod(O_C) ⥤ Mod(O)` of sheaves of modules is full.
>
> Because the structure map is that identification, the pullback of modules is the Stacks 03D2
> inverse image of modules followed by an equivalence; fullness then descends from Stacks 0D8E (1),
> full faithfulness of `a^{-1}` on sheaves of sets.

```lean
theorem full_pullbackModules [IsIso A.totalRingedHom.fSharpInverseImage] :
    A.totalRingedHom.toModulesHom.pullbackModules.Full
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.fullyFaithfulPullbackModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L292). The attribute's comment: “a^* on sheaves of modules is fully faithful, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C”.

> **Stacks 0D9Z, full faithfulness of `a^*` on sheaves of modules.**

```lean
def fullyFaithfulPullbackModules [IsIso A.totalRingedHom.fSharpInverseImage] :
    A.totalRingedHom.toModulesHom.pullbackModules.FullyFaithful
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.essImage_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L306). The attribute's comment: “every cartesian O-module is an a^*M, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C”.

> **Stacks 0D9Z, essential surjectivity onto the cartesian `O`-modules.** For a ringed
> augmentation of a hypercovering whose structure map is the identification `O = a^{-1}O_C` of
> Stacks 0D9W, every cartesian sheaf of `O`-modules on the total site is a pullback `a^*M`.
>
> The underlying sheaf of sets of a cartesian sheaf of modules is cartesian, hence an inverse image
> by Stacks 0D8E (1); and a sheaf of modules whose underlying sheaf of sets is an inverse image is a
> pullback.

```lean
theorem essImage_pullbackModules [IsIso A.totalRingedHom.fSharpInverseImage]
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation P.toGrothendieck H.toSimplicialObject).totalTopology) A.O))}
    (hF : (situation P.toGrothendieck H.toSimplicialObject).IsModuleFiberTransitionIso A.O F) :
    A.totalRingedHom.toModulesHom.pullbackModules.essImage F
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.mem_essImage_pullbackModules_iff_isCartesianModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L321). The attribute's comment: “the essential image of a^* on sheaves of modules is exactly the cartesian O-modules, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C”.

> **Stacks 0D9Z, the essential image of `a^*` is exactly the cartesian `O`-modules.** One
> inclusion is `isCartesianModule_of_mem_essImage`, which is Stacks 0D7H (3); the other is
> `essImage_pullbackModules`.

```lean
theorem mem_essImage_pullbackModules_iff_isCartesianModule
    [IsIso A.totalRingedHom.fSharpInverseImage]
    (F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation P.toGrothendieck H.toSimplicialObject).totalTopology) A.O))) :
    A.totalRingedHom.toModulesHom.pullbackModules.essImage F ↔
      (situation P.toGrothendieck H.toSimplicialObject).IsModuleFiberTransitionIso A.O F
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L334). The attribute's comment: “M = a\_* a^* M on sheaves of modules, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C”.

> **Stacks 0D9Z, `a_*` is a quasi-inverse on `Mod(O_C)`.** The unit `M ⟶ a_*a^*M` of the
> adjunction of Stacks 03D7 is an isomorphism for every sheaf of `O_C`-modules: a fully faithful
> left adjoint has invertible unit.

```lean
theorem isIso_pullbackAdjPushforwardModules_unit
    [IsIso A.totalRingedHom.fSharpInverseImage] :
    IsIso (RingedToposHom.pullbackAdjPushforwardModules A.totalRingedHom).unit
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L348). The attribute's comment: “a^* a\_* F = F for a cartesian O-module F, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^\{-1}O\_C”.

> **Stacks 0D9Z, `a_*` is a quasi-inverse on the cartesian `O`-modules.** The counit
> `a^*a_*F ⟶ F` of the adjunction of Stacks 03D7 is an isomorphism at every cartesian sheaf of
> `O`-modules: a fully faithful left adjoint has invertible counit exactly on its essential image,
> which by `mem_essImage_pullbackModules_iff_isCartesianModule` is the cartesian `O`-modules.

```lean
theorem isIso_pullbackAdjPushforwardModules_counit_app
    [IsIso A.totalRingedHom.fSharpInverseImage]
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation P.toGrothendieck H.toSimplicialObject).totalTopology) A.O))}
    (hF : (situation P.toGrothendieck H.toSimplicialObject).IsModuleFiberTransitionIso A.O F) :
    IsIso ((RingedToposHom.pullbackAdjPushforwardModules A.totalRingedHom).counit.app F)
```

## Tag 0DA0, a lemma

[Tag 0DA0](https://stacks.math.columbia.edu/tag/0DA0) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedPullbackPushforwardUnit_of_hypercoveringOfTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescentUnconditional.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescentUnconditional.lean#L251).

> **Stacks 0DA0, as an invertible natural transformation.** For a site `C` with equalizers
> and fibre products, a sheaf of commutative rings `O_C` on it and a hypercovering `K` of `C`, the
> canonical map `E ⟶ Ra_*La^*E` along the ringed augmentation of Stacks 0D9W is an isomorphism,
> naturally in `E` in the unbounded derived category `D(O_C)`. Nothing is assumed beyond the
> hypercovering conditions on `K`.

```lean
theorem isIso_derivedPullbackPushforwardUnit_of_hypercoveringOfTerminal :
    IsIso (RingedToposHom.derivedPullbackPushforwardUnit
      (hypercoveringRingedAugmentation P H OC).totalRingedHom)
```

## Tag 0DA1, a lemma

[Tag 0DA1](https://stacks.math.columbia.edu/tag/0DA1) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.derivedLinearGlobalSectionsPullbackIsoOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean#L214).

> **Stacks 0DA1.** Let `C` be a site with equalizers and fibre products, let `O_C` be a sheaf of
> commutative rings on it and let `K` be a hypercovering of `C`. With `O = a⁻¹O_C` on the total
> site and `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` the ringed augmentation of Stacks 0D9W, there
> is a canonical isomorphism
>
> `RΓ(C, E) = RΓ((C/K)_total, La^*E)`
>
> naturally in `E` in the unbounded derived category `D(O_C)`. Here `RΓ(C, -)` takes values in
> `D(Γ(C, O_C))`, and the right hand side, which lives in `D(Γ((C/K)_total, O))`, is read in
> `D(Γ(C, O_C))` through restriction of scalars along the ring map `Γ(C, O_C) ⟶ Γ((C/K)_total, O)`
> induced by `a`. Nothing is assumed beyond the hypercovering conditions on `K`. The forward map is
> pinned to the canonical one by `derivedLinearGlobalSectionsPullbackIsoOfHypercovering_hom_app`.
>
> This is the complete statement of the tag, and it supersedes the conditional
> `derivedGlobalSectionsPullbackIsoOfHypercovering` of `HypercoveringModuleDerivedGlobalSections`,
> which no longer carries the tag: that isomorphism is read only in `D(Ab)` and takes as
> hypotheses `hunit` (the module form of Stacks 0D8E), `hacyclic` (`a^*` of a K-injective complex
> computes `Ra_*`) and `hΓ` (the underived identity `Γ(C, a_*F) = Γ((C/K)_total, F)`). All three
> are theorems, and `derivedGlobalSectionsPullbackIsoOfHypercoveringOfTerminal` below is that
> isomorphism with them supplied.

```lean
def derivedLinearGlobalSectionsPullbackIsoOfHypercovering :
    RingedTopos.derivedLinearGlobalSections
        (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos ≅
      (RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
          (X := (hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
          (hypercoveringRingedAugmentation J H OC).totalRingedHom).functor ⋙
        RingedTopos.derivedLinearGlobalSections
          ((hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O) ⋙
        (ModuleCat.restrictScalars.{u} (globalSectionsRingHom
          (X := (hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
          (hypercoveringRingedAugmentation J H OC).totalRingedHom.toModulesHom)).mapDerivedCategory
```

**`Stacks.CategoryTheory.Hypercovering.derivedLinearGlobalSectionsPullbackIsoOfHypercovering_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean#L240). The attribute's comment: “the forward map of the isomorphism is the canonical one: RΓ(C, -) of the derived unit E ⟶ Ra\_*La^*E, followed by the factorisation of Tag 08J6”.

> **Stacks 0DA1, the isomorphism is the canonical one.** At every `E` of `D(O_C)` its forward
> map is `RΓ(C, -)` of the derived unit `E ⟶ Ra_*La^*E` of the ringed augmentation, followed by the
> factorisation `RΓ(C, Ra_*-) = RΓ((C/K)_total, -)` of Stacks 08J6.

```lean
theorem derivedLinearGlobalSectionsPullbackIsoOfHypercovering_hom_app
    (E : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos.J))
      (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos.O))) :
    (derivedLinearGlobalSectionsPullbackIsoOfHypercovering J H OC).hom.app E =
      (RingedTopos.derivedLinearGlobalSections
          (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos).map
          ((RingedToposHom.derivedPullbackPushforwardUnit
            (hypercoveringRingedAugmentation J H OC).totalRingedHom).app E) ≫
        (RingedToposHom.derivedLinearGlobalSectionsPushforwardIso
          (hypercoveringRingedAugmentation J H OC).totalRingedHom).hom.app
          ((RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
            (X := (hypercoveringSituation J H).totalRingedTopos
              (hypercoveringRingedAugmentation J H OC).O)
            (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
            (hypercoveringRingedAugmentation J H OC).totalRingedHom).functor.obj E)
```

## Tag 0DA2, a lemma

[Tag 0DA2](https://stacks.math.columbia.edu/tag/0DA2) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_derivedPullbackEquivalence_hypercoveringOfTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalenceUnconditional.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalenceUnconditional.lean#L232). The attribute's comment: “cartesian O-modules are weak Serre; La^* : D⁺(O\_C) ≌ D⁺\_𝒜(O), inverse Ra\_*”.

> **Stacks 0DA2.** Let `C` be a site with equalizers and fibre products, let `O_C` be a sheaf
> of commutative rings on it and let `K` be a hypercovering of `C`; let
> `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` be the ringed augmentation of Stacks 0D9W, so
> `O = a⁻¹O_C`. Then the cartesian `O`-modules `𝒜 ⊂ Mod(O)` form a weak Serre subcategory, and the
> functor `La^*` defines an equivalence
>
> `D⁺(O_C) ⟶ D⁺_𝒜(O)`
>
> with quasi-inverse `R a_*`: there is an equivalence of categories whose functor is the restriction
> of the derived pullback `La^*` to the bounded below subcategories and whose inverse is the
> restriction of the derived direct image `R a_*`. Here `D⁺(O_C)` is the full subcategory of
> bounded below objects of `D(O_C)`, and `D⁺_𝒜(O)` that of bounded below objects of `D(O)` all of
> whose cohomology modules are cartesian. Nothing is assumed beyond the hypotheses of the source.

```lean
theorem exists_derivedPullbackEquivalence_hypercoveringOfTerminal :
    (hypercoveringCartesianModules J H OC).IsWeakSerreClass ∧
      ∃ e : (AlgebraicGeometry.RingedToposHom.derivedPlusTarget
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)).FullSubcategory ≌
        (AlgebraicGeometry.RingedToposHom.derivedPlusProperty
          (hypercoveringCartesianModules J H OC)).FullSubcategory,
        e.functor = AlgebraicGeometry.RingedToposHom.derivedPullbackPlus
          (X := (hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
          (hypercoveringRingedAugmentation J H OC).totalRingedHom
          (hypercoveringCartesianModules J H OC)
          (isCartesianModule_pullbackModules_hypercovering J H OC) ∧
        e.inverse = AlgebraicGeometry.RingedToposHom.derivedPushforwardPlus
          (X := (hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
          (hypercoveringRingedAugmentation J H OC).totalRingedHom
          (hypercoveringCartesianModules J H OC)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.18, Tag 0D9Y](https://stacks.math.columbia.edu/tag/0D9Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
