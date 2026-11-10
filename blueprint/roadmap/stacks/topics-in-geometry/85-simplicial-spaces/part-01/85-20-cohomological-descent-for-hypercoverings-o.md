---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSemiRepresentable.faithful_pullbackModules_over, CategoryTheory.SimplicialSemiRepresentable.isCartesianModule_of_mem_essImage_over, CategoryTheory.SimplicialSemiRepresentable.full_pullbackModules_over, CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulPullbackModulesOver, CategoryTheory.SimplicialSemiRepresentable.essImage_pullbackModules_over, CategoryTheory.SimplicialSemiRepresentable.mem_essImage_pullbackModules_iff_isCartesianModule_over, CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_unit_over, CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_counit_app_over
statement: formalized
proof: formalized
---

# 85.20 Cohomological descent for hypercoverings of an object: modules

Section 85.20 of the Stacks Project, [Tag 0DA3](https://stacks.math.columbia.edu/tag/0DA3). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DA4, a lemma

[Tag 0DA4](https://stacks.math.columbia.edu/tag/0DA4) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.faithful_pullbackModules_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L290). The attribute's comment: “a^* on sheaves of modules is faithful. The essential-image inclusion is `isCartesianModule_of_mem_essImage_over`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a_* a quasi-inverse, are not proved”.

> **Stacks 0DA4, the faithfulness half.** Let `C` be a site with fibre products, `X` an object
> of it, `O_C` a sheaf of commutative rings on `C` and `K` a hypercovering of `X`. With
> `O_X = O_C|_{C/X}` and `O = a⁻¹O_X`, the pullback `a^* : Mod(O_X) ⥤ Mod(O)` of sheaves of
> modules along the augmentation of the total site of `K` over `C/X` is faithful.

```lean
theorem faithful_pullbackModules_over (hK : IsHypercovering P K) :
    (hypercoveringObjectRingedAugmentation P K
      OC).totalRingedHom.toModulesHom.pullbackModules.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianModule_of_mem_essImage_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L306). The attribute's comment: “the essential image of a^* consists of cartesian O-modules. Faithfulness of a^* is `faithful_pullbackModules_over`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a_* a quasi-inverse, are not proved”.

> **Stacks 0DA4, the inclusion of the essential image in the cartesian modules.** In the
> situation above, every sheaf of `O`-modules on the total site isomorphic to a pullback `a^*F` is
> a cartesian `O`-module.
>
> This is Stacks 0D7H (3) together with invariance of the cartesian condition under
> isomorphism, and uses no condition on `K`.

```lean
theorem isCartesianModule_of_mem_essImage_over
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X) K).totalTopology))
      (hypercoveringObjectRingedAugmentation P K OC).O)}
    (hF : (hypercoveringObjectRingedAugmentation P K
      OC).totalRingedHom.toModulesHom.pullbackModules.essImage F) :
    (situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
      (hypercoveringObjectRingedAugmentation P K OC).O F
```

**`CategoryTheory.SimplicialSemiRepresentable.full_pullbackModules_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L324). The attribute's comment: “a^* on sheaves of modules is full”.

> **Stacks 0DA4, the fullness half.** In the situation above, the pullback
> `a^* : Mod(O_X) ⥤ Mod(O)` of sheaves of modules is full.
>
> Because the structure map of `a` is the identification `O = a⁻¹O_X`, the pullback of modules is
> the Stacks 03D2 inverse image of modules followed by an equivalence; fullness then descends from
> Stacks 0D8K (1), full faithfulness of `a⁻¹` on sheaves of sets over `C/X`.

```lean
theorem full_pullbackModules_over (hK : IsHypercovering P K) :
    (hypercoveringObjectRingedAugmentation P K
      OC).totalRingedHom.toModulesHom.pullbackModules.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulPullbackModulesOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L334). The attribute's comment: “a^* on sheaves of modules is fully faithful”.

> **Stacks 0DA4, full faithfulness of `a^*` on sheaves of modules.**

```lean
def fullyFaithfulPullbackModulesOver (hK : IsHypercovering P K) :
    (hypercoveringObjectRingedAugmentation P K
      OC).totalRingedHom.toModulesHom.pullbackModules.FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_pullbackModules_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L348). The attribute's comment: “every cartesian O-module is an a^*M”.

> **Stacks 0DA4, essential surjectivity onto the cartesian `O`-modules.** In the situation
> above, every cartesian sheaf of `O`-modules on the total site is a pullback `a^*M`.
>
> The underlying sheaf of sets of a cartesian sheaf of modules is cartesian — the structure sheaf
> itself being cartesian because it is `a⁻¹O_X` — hence an inverse image by Stacks 0D8K (1); and a
> sheaf of modules whose underlying sheaf of sets is an inverse image is a pullback.

```lean
theorem essImage_pullbackModules_over (hK : IsHypercovering P K)
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X) K).totalTopology)
      (hypercoveringObjectRingedAugmentation P K OC).O))}
    (hF : (situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
      (hypercoveringObjectRingedAugmentation P K OC).O F) :
    (hypercoveringObjectRingedAugmentation P K
      OC).totalRingedHom.toModulesHom.pullbackModules.essImage F
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_pullbackModules_iff_isCartesianModule_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L367). The attribute's comment: “the essential image of a^* on sheaves of modules is exactly the cartesian O-modules”.

> **Stacks 0DA4, the essential image of `a^*` is exactly the cartesian `O`-modules.** One
> inclusion is `isCartesianModule_of_mem_essImage_over`, which is Stacks 0D7H (3); the other is
> `essImage_pullbackModules_over`.

```lean
theorem mem_essImage_pullbackModules_iff_isCartesianModule_over (hK : IsHypercovering P K)
    (F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X) K).totalTopology)
      (hypercoveringObjectRingedAugmentation P K OC).O))) :
    (hypercoveringObjectRingedAugmentation P K
      OC).totalRingedHom.toModulesHom.pullbackModules.essImage F ↔
      (situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
        (hypercoveringObjectRingedAugmentation P K OC).O F
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_unit_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L381). The attribute's comment: “M = a_* a^* M on sheaves of modules”.

> **Stacks 0DA4, `a_*` is a quasi-inverse on `Mod(O_X)`.** The unit `M ⟶ a_*a^*M` of the
> adjunction of Stacks 03D7 is an isomorphism for every sheaf of `O_X`-modules: a fully faithful
> left adjoint has invertible unit.

```lean
theorem isIso_pullbackAdjPushforwardModules_unit_over (hK : IsHypercovering P K) :
    IsIso (RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringObjectRingedAugmentation P K OC).totalRingedHom).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_counit_app_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDescent.lean#L396). The attribute's comment: “a^* a_* F = F for a cartesian O-module F”.

> **Stacks 0DA4, `a_*` is a quasi-inverse on the cartesian `O`-modules.** The counit
> `a^*a_*F ⟶ F` of the adjunction of Stacks 03D7 is an isomorphism at every cartesian sheaf of
> `O`-modules: a fully faithful left adjoint has invertible counit exactly on its essential image,
> which by `mem_essImage_pullbackModules_iff_isCartesianModule_over` is the cartesian
> `O`-modules.

```lean
theorem isIso_pullbackAdjPushforwardModules_counit_app_over (hK : IsHypercovering P K)
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X) K).totalTopology)
      (hypercoveringObjectRingedAugmentation P K OC).O))}
    (hF : (situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
      (hypercoveringObjectRingedAugmentation P K OC).O F) :
    IsIso ((RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringObjectRingedAugmentation P K OC).totalRingedHom).counit.app F)
```

## Tag 0DA5, a lemma

[Tag 0DA5](https://stacks.math.columbia.edu/tag/0DA5) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.isIso_derivedPullbackPushforwardUnit_app_of_hypercovering_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescent.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescent.lean#L399). The attribute's comment: “granted the module form of Tag 0D8E as hunit and the Ra_*-acyclicity of a^* of a K-injective complex as hacyclic -- the same two inputs this library's Tag 0DA0, `isIso_derivedPullbackPushforwardUnit_app_of_hypercovering`, is itself granted”.

> **Stacks 0DA5.** Let `C` be a site with fibre products, `X` an object of it, `O_C` a sheaf of
> rings and `K` a hypercovering of `X`. Writing `O_X = O_C|_{C/X}` and `a` for the augmentation of
> the total site of `K` over the slice site `C/X`, the canonical map `E ⟶ Ra_*La^*E` is an
> isomorphism for every `E` in the derived category of `O_X`-modules.
>
> The slice site `C/X` has a terminal object and inherits fibre products from `C`, so it has all
> finite limits; this is why the source asks only for fibre products on `C` here, where Stacks
> 0DA0 asks for equalizers as well. The augmentation is the ringed one of Stacks 0D9X, and the two
> pinning lemmas `hypercoveringObjectRingedAugmentation_augmentationRingedTopos_J` and `_O` certify
> that the coefficients are the sheaves of `O_X`-modules on `C/X`. The hypercovering condition on
> `K` is recorded as `hK`, and, exactly as in Stacks 0DA0, it is absorbed into the two deferred
> inputs rather than consumed directly.

```lean
theorem isIso_derivedPullbackPushforwardUnit_app_of_hypercovering_over
    (_hK : IsHypercovering P K)
    (hunit : IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringObjectRingedAugmentation P K O).totalRingedHom).unit)
    (hacyclic : AlgebraicGeometry.RingedToposHom.PullbackComputesDerivedPushforward.{u}
      (hypercoveringObjectRingedAugmentation P K O).totalRingedHom)
    (E : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (hypercoveringObjectRingedAugmentation P K O).augmentationRingedTopos.J))
      (hypercoveringObjectRingedAugmentation P K O).augmentationRingedTopos.O))) :
    IsIso ((AlgebraicGeometry.RingedToposHom.derivedPullbackPushforwardUnit
      (hypercoveringObjectRingedAugmentation P K O).totalRingedHom).app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedPullbackPushforwardUnit_app_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleCohomologicalDescentUnconditional.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleCohomologicalDescentUnconditional.lean#L264).

> **Stacks 0DA5.** Let `C` be a site with fibre products, `X` an object of `C`, `O_C` a sheaf
> of commutative rings on `C` and `K` a hypercovering of `X`. With `O_X = O_C|_{C/X}`,
> `O = a⁻¹O_X` on the total site of `K` and `a : (Sh((C/K)_total), O) ⟶ (Sh(C/X), O_X)` the ringed
> augmentation of Stacks 0D9X, the canonical map
>
> `E ⟶ R a_* L a^* E`
>
> is an isomorphism for every object `E` of the unbounded derived category `D(O_X)` of sheaves of
> `O_X`-modules.

```lean
theorem isIso_derivedPullbackPushforwardUnit_app_of_isHypercovering (hK : IsHypercovering P K)
    (E : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (hypercoveringObjectRingedAugmentation P K OC).augmentationRingedTopos.J))
      (hypercoveringObjectRingedAugmentation P K OC).augmentationRingedTopos.O))) :
    IsIso ((AlgebraicGeometry.RingedToposHom.derivedPullbackPushforwardUnit
      (hypercoveringObjectRingedAugmentation P K OC).totalRingedHom).app E)
```

## Tag 0DA6, a lemma

[Tag 0DA6](https://stacks.math.columbia.edu/tag/0DA6) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.derivedModuleSectionsOverObjectIsoOfIsHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean#L321).

> Let `C` be a site with fibre products, given by a pretopology `P`, let `X` be an object of
> `C`, let `O_C` be a sheaf of commutative rings on `C` and let `K` be a hypercovering of `X` (a
> simplicial object of `SR(C, X)` whose degree-zero family covers `X` and whose matching maps
> `K_{n+1} ⟶ (cosk_n sk_n K)_{n+1}` are covering). With `O_X = O_C|_{C/X}`, `O = a⁻¹O_X` on the
> total site `(C/K)_total` and `a : (Sh((C/K)_total), O) ⟶ (Sh(C/X), O_X)` the ringed
> augmentation, there is a canonical isomorphism
>
> `RΓ(X, E) = RΓ((C/K)_total, La^*E)`
>
> naturally in `E` in the unbounded derived category `D(O_C)`. Here `RΓ(X, -)` is the total right
> derived functor of sections over `X`, with values in `D(O_C(X))`; `La^*E` is `La^*` of the
> restriction of `E` to `C/X` (the target of `a` being `(Sh(C/X), O_X)`); and
> `RΓ((C/K)_total, -)`, with values in `D(Γ((C/K)_total, O))`, is read in `D(O_C(X))` through the
> canonical ring map `O_C(X) ⟶ Γ((C/K)_total, O)` (`totalSectionsRingHom`).

```lean
def derivedModuleSectionsOverObjectIsoOfIsHypercovering (hK : IsHypercovering P K) :
    derivedModuleSectionsOverObject P X OC ≅
      Stacks.Cohomology.Localization.derivedRestriction (ringedSite P OC) X ⋙
        (RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
          (X := totalTopos P K OC) (Y := sliceTopos P K OC) (augmentationHom P K OC)).functor ⋙
        derivedTotalGlobalSections P K OC ⋙
          (ModuleCat.restrictScalars (totalSectionsRingHom P K OC)).mapDerivedCategory
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedModuleSectionsOverObjectIsoOfIsHypercovering_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean#L337). The attribute's comment: “the forward map of the isomorphism is the canonical one: RΓ(C/X, -) of the derived unit E|_X ⟶ Ra_*La^*(E|_X), between RΓ(X, E) = RΓ(C/X, E|_X) and the factorisation of Tag 08J6”.

> The forward map of `derivedModuleSectionsOverObjectIsoOfIsHypercovering` at `E` is
> `RΓ(C/X, -)` of the derived unit `E|_X ⟶ Ra_*La^*(E|_X)` of the ringed augmentation, between the
> comparison `RΓ(X, E) = RΓ(C/X, E|_X)` and the factorisation
> `RΓ(C/X, Ra_*-) = RΓ((C/K)_total, -)`.

```lean
theorem derivedModuleSectionsOverObjectIsoOfIsHypercovering_hom_app (hK : IsHypercovering P K)
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf OC))) :
    (derivedModuleSectionsOverObjectIsoOfIsHypercovering P K OC hK).hom.app E =
      (derivedModuleSectionsOverObjectIsoRestriction P OC).hom.app E ≫
        (derivedModuleSectionsAtId P X OC).map
          ((RingedToposHom.derivedPullbackPushforwardUnit (augmentationHom P K OC)).app
            ((Stacks.Cohomology.Localization.derivedRestriction (ringedSite P OC) X).obj E)) ≫
        (derivedPushforwardModuleSectionsAtIdIso P K OC).hom.app
          ((RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
            (X := totalTopos P K OC) (Y := sliceTopos P K OC) (augmentationHom P K OC)).functor.obj
              ((Stacks.Cohomology.Localization.derivedRestriction (ringedSite P OC) X).obj E))
```

## Tag 0DA7, a lemma

[Tag 0DA7](https://stacks.math.columbia.edu/tag/0DA7) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.exists_derivedPullbackEquivalence_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleBoundedBelowDescent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleBoundedBelowDescent.lean#L84).

> Let `C` be a site with fibre products, given by a pretopology `P`, let `X` be an object of
> `C`, let `O_C` be a sheaf of commutative rings on `C` and let `K` be a hypercovering of `X`
> (Stacks 01G5: a simplicial object of `SR(C, X)` whose degree-zero family covers `X` and
> whose matching maps `K_{n+1} ⟶ (cosk_n sk_n K)_{n+1}` are covering). Let `O_X = O_C|_{C/X}`, let
> `O = a⁻¹O_X` on the total site `(C/K)_total` and let `a : (Sh((C/K)_total), O) ⟶ (Sh(C/X), O_X)`
> be the ringed augmentation of Remarks 0D9V and 0D9X. Then
>
> * the cartesian `O`-modules form a weak Serre subcategory `𝒜 ⊂ Mod(O)`, and
> * the functor `La^*` defines an equivalence `D⁺(O_X) ⟶ D⁺_𝒜(O)` with quasi-inverse `R a_*`:
>   there is an equivalence of categories whose functor, followed by the inclusion of `D⁺_𝒜(O)`, is
>   `La^*` on `D⁺(O_X)`, and whose inverse, followed by the inclusion of `D⁺(O_X)`, is `R a_*` on
>   `D⁺_𝒜(O)`.
>
> Here `D⁺(O_X)` is the full subcategory of bounded below objects of `D(O_X)`, and `D⁺_𝒜(O)` that of
> bounded below objects of `D(O)` all of whose cohomology modules are cartesian. Nothing is assumed
> beyond the hypotheses of the source; the equivalence is
> `derivedPullbackEquivalenceOfIsHypercovering`.

```lean
theorem exists_derivedPullbackEquivalence_isHypercovering (hK : IsHypercovering P K) :
    ObjectProperty.IsWeakSerreClass
        ((situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
          (hypercoveringObjectRingedAugmentation P K OC).O) ∧
      ∃ e : (RingedToposHom.derivedPlusTarget (Y := sliceTopos P K OC)).FullSubcategory ≌
          (RingedToposHom.derivedPlusProperty (X := totalTopos P K OC)
            ((situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
              (hypercoveringObjectRingedAugmentation P K OC).O)).FullSubcategory,
        e.functor ⋙ (RingedToposHom.derivedPlusProperty (X := totalTopos P K OC)
            ((situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
              (hypercoveringObjectRingedAugmentation P K OC).O)).ι =
          (RingedToposHom.derivedPlusTarget (Y := sliceTopos P K OC)).ι ⋙
            (RingedToposHom.leftDerivedPullbackOfIsIsoFSharp (X := totalTopos P K OC)
              (Y := sliceTopos P K OC) (augmentationHom P K OC)).functor ∧
        e.inverse ⋙ (RingedToposHom.derivedPlusTarget (Y := sliceTopos P K OC)).ι =
          (RingedToposHom.derivedPlusProperty (X := totalTopos P K OC)
            ((situation (P.toGrothendieck.over X) K).IsModuleFiberTransitionIso
              (hypercoveringObjectRingedAugmentation P K OC).O)).ι ⋙
            Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := totalTopos P K OC)
              (Y := sliceTopos P K OC) (augmentationHom P K OC)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.20, Tag 0DA3](https://stacks.math.columbia.edu/tag/0DA3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
