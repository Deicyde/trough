---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isCartesianModule_of_mem_essImage, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.faithful_pullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.full_pullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.fullyFaithfulPullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.essImage_pullbackModules, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.mem_essImage_pullbackModules_iff_isCartesianModule, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_unit, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_counit_app
statement: formalized
proof: formalized
---

# 85.18 Cohomological descent for hypercoverings: modules

Section 85.18 of the Stacks Project, [Tag 0D9Y](https://stacks.math.columbia.edu/tag/0D9Y). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D9Z, a lemma

[Tag 0D9Z](https://stacks.math.columbia.edu/tag/0D9Z) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isCartesianModule_of_mem_essImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L148). The attribute's comment: “the essential image of a^* consists of cartesian O-modules. Faithfulness of a^* is `faithful_pullbackModules`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a_* a quasi-inverse, are not proved”.

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

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.faithful_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L271). The attribute's comment: “a^* on sheaves of modules is faithful, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C. The essential-image inclusion is `isCartesianModule_of_mem_essImage`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a_* a quasi-inverse, are not proved”.

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

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.full_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L284). The attribute's comment: “a^* on sheaves of modules is full, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C”.

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

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.fullyFaithfulPullbackModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L292). The attribute's comment: “a^* on sheaves of modules is fully faithful, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C”.

> **Stacks 0D9Z, full faithfulness of `a^*` on sheaves of modules.**

```lean
def fullyFaithfulPullbackModules [IsIso A.totalRingedHom.fSharpInverseImage] :
    A.totalRingedHom.toModulesHom.pullbackModules.FullyFaithful
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.essImage_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L306). The attribute's comment: “every cartesian O-module is an a^*M, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C”.

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

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.mem_essImage_pullbackModules_iff_isCartesianModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L321). The attribute's comment: “the essential image of a^* on sheaves of modules is exactly the cartesian O-modules, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C”.

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

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L334). The attribute's comment: “M = a_* a^* M on sheaves of modules, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C”.

> **Stacks 0D9Z, `a_*` is a quasi-inverse on `Mod(O_C)`.** The unit `M ⟶ a_*a^*M` of the
> adjunction of Stacks 03D7 is an isomorphism for every sheaf of `O_C`-modules: a fully faithful
> left adjoint has invertible unit.

```lean
theorem isIso_pullbackAdjPushforwardModules_unit
    [IsIso A.totalRingedHom.fSharpInverseImage] :
    IsIso (RingedToposHom.pullbackAdjPushforwardModules A.totalRingedHom).unit
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.isIso_pullbackAdjPushforwardModules_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleDescent.lean#L348). The attribute's comment: “a^* a_* F = F for a cartesian O-module F, for a ringed augmentation of a hypercovering whose structure map is the identification O = a^{-1}O_C”.

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

**`Stacks.CategoryTheory.Hypercovering.isIso_derivedPullbackPushforwardUnit_app_of_hypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescent.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescent.lean#L364). The attribute's comment: “granted the module form of Tag 0D8E as hunit and the Ra_*-acyclicity of a^* of a K-injective complex as hacyclic -- the two inputs that this library's Tag 0D8G, `isIso_derivedAugmentationUnit_app_of_hypercovering`, is itself granted”.

> **Stacks 0DA0**, granted the two inputs this library's Stacks 0D8G is granted, in their
> module form. Let `C` be a site with equalizers and fibre products, let `O_C` be a sheaf of
> commutative rings on it and let `K` be a hypercovering of `C`. With `O = a⁻¹O_C` on the total
> site and `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` the ringed augmentation of Stacks 0D9W, the
> canonical map
>
> `E ⟶ R a_* L a^* E`
>
> is an isomorphism for every object `E` of the unbounded derived category `D(O_C)` of sheaves of
> `O_C`-modules.
>
> `E` is arbitrary: no boundedness is assumed and the coefficients are the full category of
> sheaves of modules. `La^*` is the degreewise pullback, which is the source's first observation,
> and nothing of Stacks 06YY, 0G6R or 05VD enters.
>
> The two hypotheses are the two of
> `Stacks.CategoryTheory.Hypercovering.isIso_derivedAugmentationUnit_app_of_hypercovering`, read
> for sheaves of modules instead of abelian sheaves. `hunit` is Stacks 0D8E in its module form,
> that the underived unit `M ⟶ a_*a^*M` is an isomorphism; it is not available here because its
> proof needs the abelian form of Stacks 0D86, which this library has for sheaves of sets only.
> `hacyclic` says that `a^*` of a K-injective complex of `O_C`-modules computes `Ra_*`; it is the
> derived content of the source's computation of `Ra_*a^*` by the Čech complex, which rests on the
> spectral sequence of Stacks 0D7A that this library does not build. The source's own route — the
> abelian statement of Stacks 0D8G together with Stacks 0D6J — would carry the same two
> hypotheses through Stacks 0D8G *and* in addition the clause of Stacks 0D6J about the derived
> direct image, which this library does not have; so that route is not taken and the count of
> deferred inputs is exactly two.

```lean
theorem isIso_derivedPullbackPushforwardUnit_app_of_hypercovering
    (hunit : IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringRingedAugmentation J H OC).totalRingedHom).unit)
    (hacyclic : AlgebraicGeometry.RingedToposHom.PullbackComputesDerivedPushforward.{u}
      (hypercoveringRingedAugmentation J H OC).totalRingedHom)
    (E : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos.J))
      (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos.O))) :
    IsIso ((AlgebraicGeometry.RingedToposHom.derivedPullbackPushforwardUnit
      (hypercoveringRingedAugmentation J H OC).totalRingedHom).app E)
```

Declarations registered for the tag:

- [`SimplicialSemiRepresentable.isIso_derivedPullbackPushforwardUnit_of_hypercoveringOfTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SimplicialSemiRepresentable.isIso_derivedPullbackPushforwardUnit_of_hypercoveringOfTerminal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescentTags.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleCohomologicalDescentTags.lean#L23) (StacksFrontier).

## Tag 0DA1, a lemma

[Tag 0DA1](https://stacks.math.columbia.edu/tag/0DA1) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.derivedGlobalSectionsPullbackIsoOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSections.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSections.lean#L290). The attribute's comment: “granted the two inputs of this library's Tag 0DA0 -- the module form of Tag 0D8E as hunit and the Ra_*-acyclicity of a^* of a K-injective complex as hacyclic -- and granted the underived identity Γ(C, a_*M) = Γ(total, M) of Tag 08J6 as hΓ. Unbounded: the isomorphism is of functors on all of D(O_C). Both sides are read in D(Ab), the module structure of global sections over Γ(C, O_C) being forgotten”.

> **Stacks 0DA1**, granted the inputs the library does not have. For a site `C` with equalizers
> and fibre products, a sheaf of commutative rings `O_C` on it, a hypercovering `K` of `C` and the
> ringed augmentation `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` of Stacks 0D9W with `O = a⁻¹O_C`,
> derived global sections on `C` are derived global sections on the total site of the derived
> pullback:
>
> `RΓ(C, E) = RΓ((C/K)_total, La^*E)`.
>
> The statement is an isomorphism of functors on the *unbounded* derived category `D(O_C)` of
> sheaves of `O_C`-modules, so it holds at every object `E` with no boundedness assumption, which
> is the form the source states.
>
> Three hypotheses are carried. `hunit` and `hacyclic` are the two inputs of this library's
> Stacks 0DA0, inherited unchanged from
> `isIso_derivedPullbackPushforwardUnit_app_of_hypercovering`: the first is Stacks 0D8E in its
> module form, that the underived unit `M ⟶ a_*a^*M` is an isomorphism, and the second is that
> `a^*` of a K-injective complex computes `R a_*`. `hΓ` is the underived identity
> `Γ(C, a_*M) = Γ((C/K)_total, M)` on which the factorisation of Stacks 08J6 rests; it is
> unavailable here for the same reason as its abelian counterpart in this library's Stacks 0D8H,
> namely that nothing says the inverse image of a morphism of topoi carries a constant abelian
> sheaf to a constant abelian sheaf. The derived content of Stacks 08J6 is *not* assumed: see the
> module docstring.
>
> Both sides are read in `D(Ab)`: global sections of a sheaf of modules are taken with the module
> structure forgotten, the source's `D(Γ(C, O_C))` reading being unavailable in this library.

```lean
def derivedGlobalSectionsPullbackIsoOfHypercovering
    (hunit : IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringRingedAugmentation J H OC).totalRingedHom).unit)
    (hacyclic : AlgebraicGeometry.RingedToposHom.PullbackComputesDerivedPushforward.{u}
      (hypercoveringRingedAugmentation J H OC).totalRingedHom)
    (hΓ : AlgebraicGeometry.RingedToposHom.pushforwardModules
          (X := (hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
          (hypercoveringRingedAugmentation J H OC).totalRingedHom ⋙
        AlgebraicGeometry.RingedTopos.moduleGlobalSections
          (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos ≅
      AlgebraicGeometry.RingedTopos.moduleGlobalSections
        ((hypercoveringSituation J H).totalRingedTopos
          (hypercoveringRingedAugmentation J H OC).O)) :
    AlgebraicGeometry.RingedTopos.derivedModuleGlobalSections
        (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos ≅
      (AlgebraicGeometry.RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
          (X := (hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
          (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
          (hypercoveringRingedAugmentation J H OC).totalRingedHom).functor ⋙
        AlgebraicGeometry.RingedTopos.derivedModuleGlobalSections
          ((hypercoveringSituation J H).totalRingedTopos
            (hypercoveringRingedAugmentation J H OC).O)
```

**`Stacks.CategoryTheory.Hypercovering.derivedLinearGlobalSectionsPullbackIsoOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean#L205).

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

**`Stacks.CategoryTheory.Hypercovering.derivedLinearGlobalSectionsPullbackIsoOfHypercovering_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleDerivedGlobalSectionsUnconditional.lean#L231). The attribute's comment: “the forward map of the isomorphism is the canonical one: RΓ(C, -) of the derived unit E ⟶ Ra_*La^*E, followed by the factorisation of Tag 08J6”.

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

**`Stacks.CategoryTheory.Hypercovering.derivedPullbackEquivalenceOfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalence.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalence.lean#L602). The attribute's comment: “granted the two inputs of this library's Tag 0DA0 -- the module form of Tag 0D8E as hunit and the Ra_*-acyclicity of a^* of a K-injective complex as hacyclic -- and granted the essential-surjectivity clause of Tag 0D9Z as hsurj. The weak Serre property of the cartesian O-modules, Tag 0D7J (2), is not available in this library and is not used: D^+_A(O) is read as the bounded below objects whose cohomology modules are cartesian”. References: SGA 4 Vbis (2.2.7), “special case”; SGA 4 Vbis (2.4.12), “special case”.

> **Stacks 0DA2**, granted the inputs the library does not have. For a site `C` with equalizers
> and fibre products, a sheaf of commutative rings `O_C` on it, a hypercovering `K` of `C`, the
> ringed augmentation `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` of Stacks 0D9W with `O = a⁻¹O_C`,
> and the class `𝒜 ⊂ Mod(O)` of cartesian `O`-modules, the derived pullback is an equivalence
>
> `La^* : D⁺(O_C) ⟶ D⁺_𝒜(O)`
>
> with quasi-inverse `R a_*`. Both functors of the equivalence are the restrictions of `La^*` and of
> `R a_*` on the nose, since the equivalence is the restricted adjunction.
>
> Three hypotheses are carried. `hunit` and `hacyclic` are the two inputs of this library's
> Stacks 0DA0, inherited unchanged from
> `isIso_derivedPullbackPushforwardUnit_app_of_hypercovering`: the first is Stacks 0D8E in its
> module form, that the underived unit `M ⟶ a_*a^*M` is an isomorphism, and the second is that
> `a^*` of a K-injective complex computes `R a_*`. `hsurj` is the remaining clause of
> Stacks 0D9Z, that every cartesian `O`-module on the total site lies in the essential image of
> `a^*`; the development carries the converse inclusion
> (`RingedAugmentation.isCartesianModule_of_mem_essImage`) and faithfulness of `a^*`, and the
> degree-zero condition on a hypercovering does not supply the rest. The derived content of
> Stacks 0D7U is *not* assumed: see the module docstring.
>
> `𝒜` is read as the class of cartesian `O`-modules, closed under isomorphism; that it is a weak
> Serre subcategory, which is Stacks 0D7J (2) and which this library has only for abelian sheaves,
> is not used anywhere in the argument.

```lean
def derivedPullbackEquivalenceOfHypercovering
    (hunit : IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringRingedAugmentation J H OC).totalRingedHom).unit)
    (hacyclic : AlgebraicGeometry.RingedToposHom.PullbackComputesDerivedPushforward.{u}
      (hypercoveringRingedAugmentation J H OC).totalRingedHom)
    (hsurj : ∀ M, hypercoveringCartesianModules J H OC M →
      (Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
        (X := (hypercoveringSituation J H).totalRingedTopos
          (hypercoveringRingedAugmentation J H OC).O)
        (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
        (hypercoveringRingedAugmentation J H OC).totalRingedHom.toModulesHom).essImage M) :
    (AlgebraicGeometry.RingedToposHom.derivedPlusTarget
        (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)).FullSubcategory ≌
      (AlgebraicGeometry.RingedToposHom.derivedPlusProperty
        (hypercoveringCartesianModules J H OC)).FullSubcategory
```

**`Stacks.CategoryTheory.Hypercovering.derivedPullbackEquivalenceOfHypercovering_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalence.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalence.lean#L639). The attribute's comment: “the forward functor of the equivalence is La^*, under the three hypotheses of `derivedPullbackEquivalenceOfHypercovering`”.

> **Stacks 0DA2, the forward functor of the equivalence is `La^*`:** it is the restriction of
> the derived pullback to the bounded below subcategories.

```lean
theorem derivedPullbackEquivalenceOfHypercovering_functor
    (hunit : IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringRingedAugmentation J H OC).totalRingedHom).unit)
    (hacyclic : AlgebraicGeometry.RingedToposHom.PullbackComputesDerivedPushforward.{u}
      (hypercoveringRingedAugmentation J H OC).totalRingedHom)
    (hsurj : ∀ M, hypercoveringCartesianModules J H OC M →
      (Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
        (X := (hypercoveringSituation J H).totalRingedTopos
          (hypercoveringRingedAugmentation J H OC).O)
        (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
        (hypercoveringRingedAugmentation J H OC).totalRingedHom.toModulesHom).essImage M) :
    (derivedPullbackEquivalenceOfHypercovering J H OC hunit hacyclic hsurj).functor =
      AlgebraicGeometry.RingedToposHom.derivedPullbackPlus
        (X := (hypercoveringSituation J H).totalRingedTopos
          (hypercoveringRingedAugmentation J H OC).O)
        (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
        (hypercoveringRingedAugmentation J H OC).totalRingedHom
        (hypercoveringCartesianModules J H OC)
        (isCartesianModule_pullbackModules_hypercovering J H OC)
```

**`Stacks.CategoryTheory.Hypercovering.derivedPullbackEquivalenceOfHypercovering_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalence.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalence.lean#L664). The attribute's comment: “the quasi-inverse of the equivalence is Ra_*, under the three hypotheses of `derivedPullbackEquivalenceOfHypercovering`”.

> **Stacks 0DA2, the quasi-inverse of the equivalence is `R a_*`:** it is the restriction of the
> derived direct image to the bounded below subcategories.

```lean
theorem derivedPullbackEquivalenceOfHypercovering_inverse
    (hunit : IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringRingedAugmentation J H OC).totalRingedHom).unit)
    (hacyclic : AlgebraicGeometry.RingedToposHom.PullbackComputesDerivedPushforward.{u}
      (hypercoveringRingedAugmentation J H OC).totalRingedHom)
    (hsurj : ∀ M, hypercoveringCartesianModules J H OC M →
      (Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
        (X := (hypercoveringSituation J H).totalRingedTopos
          (hypercoveringRingedAugmentation J H OC).O)
        (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
        (hypercoveringRingedAugmentation J H OC).totalRingedHom.toModulesHom).essImage M) :
    (derivedPullbackEquivalenceOfHypercovering J H OC hunit hacyclic hsurj).inverse =
      AlgebraicGeometry.RingedToposHom.derivedPushforwardPlus
        (X := (hypercoveringSituation J H).totalRingedTopos
          (hypercoveringRingedAugmentation J H OC).O)
        (Y := (hypercoveringRingedAugmentation J H OC).augmentationRingedTopos)
        (hypercoveringRingedAugmentation J H OC).totalRingedHom
        (hypercoveringCartesianModules J H OC)
```

**`Stacks.CategoryTheory.Hypercovering.exists_derivedPullbackEquivalence_hypercoveringOfTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalenceUnconditional.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringModuleBoundedBelowEquivalenceUnconditional.lean#L232).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
