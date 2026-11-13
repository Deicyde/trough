---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSemiRepresentable.faithful_pullbackModules_simplicialObject, CategoryTheory.SimplicialSemiRepresentable.isCartesianModule_of_mem_essImage_simplicialObject, CategoryTheory.SimplicialSemiRepresentable.full_pullbackModules_simplicialObject, CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulPullbackModulesSimplicialObject, CategoryTheory.SimplicialSemiRepresentable.essImage_pullbackModules_simplicialObject, CategoryTheory.SimplicialSemiRepresentable.mem_essImage_pullbackModules_iff_isCartesianModule_simplicialObject, CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_unit_simplicialObject, CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_counit_app_simplicialObject
statement: formalized
proof: formalized
---

# 85.22 Hypercovering by a simplicial object of the site: modules

Section 85.22 of the Stacks Project, [Tag 0DAA](https://stacks.math.columbia.edu/tag/0DAA). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DAB, a lemma

[Tag 0DAB](https://stacks.math.columbia.edu/tag/0DAB) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.faithful_pullbackModules_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L117). The attribute's comment: “a^* on sheaves of modules is faithful, for a hypercovering of X by a simplicial object of the site. The essential-image inclusion is `isCartesianModule_of_mem_essImage_simplicialObject`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a\_* a quasi-inverse, are not proved”.

> **Stacks 0DAB, the faithfulness half.** Let `C` be a site with fibre products, `X` an object
> of it, `O_C` a sheaf of commutative rings on `C`, and `U` a simplicial object of `C` augmented
> to `X` which is a hypercovering of `X` in the sense of Stacks, Section 85.21: the degree-zero
> augmentation, the canonical map `U_1 ⟶ U_0 ×_X U_0`, and every higher matching map generate
> covering presieves. With `O_X = O_C|_{C/X}` and `O = a⁻¹O_X`, the pullback
> `a^* : Mod(O_X) ⥤ Mod(O)` of sheaves of modules along the augmentation of the total site of `U`
> over `C/X` is faithful.
>
> This is Stacks 0DA4 for the associated simplicial semi-representable object of Stacks 0GM9,
> whose hypercovering condition is exactly the three hypotheses.

```lean
theorem faithful_pullbackModules_simplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left)) :
    (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
      OC).totalRingedHom.toModulesHom.pullbackModules.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianModule_of_mem_essImage_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L138). The attribute's comment: “the essential image of a^* consists of cartesian O-modules, for a hypercovering of X by a simplicial object of the site. Faithfulness of a^* is `faithful_pullbackModules_simplicialObject`; fullness of a^*, and essential surjectivity onto the cartesian O-modules making a\_* a quasi-inverse, are not proved”.

> **Stacks 0DAB, the inclusion of the essential image in the cartesian modules.** In the
> situation above, every sheaf of `O`-modules on the total site of a simplicial object of `C`
> augmented to `X` which is isomorphic to a pullback `a^*F` is a cartesian `O`-module.
>
> This is Stacks 0DA4 for the associated simplicial semi-representable object of Stacks 0GM9, and
> uses no condition on `U`.

```lean
theorem isCartesianModule_of_mem_essImage_simplicialObject
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X)
        (associatedSimplicialObject.{u} U a)).totalTopology))
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O)}
    (hF : (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
      OC).totalRingedHom.toModulesHom.pullbackModules.essImage F) :
    (situation (P.toGrothendieck.over X)
      (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
        (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O F
```

**`CategoryTheory.SimplicialSemiRepresentable.full_pullbackModules_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L157). The attribute's comment: “a^* on sheaves of modules is full, for a hypercovering of X by a simplicial object of the site”.

> **Stacks 0DAB, the fullness half.** In the situation above, the pullback
> `a^* : Mod(O_X) ⥤ Mod(O)` of sheaves of modules is full.
>
> This is Stacks 0DA4 for the associated simplicial semi-representable object of Stacks 0GM9,
> whose hypercovering condition is exactly the three hypotheses.

```lean
theorem full_pullbackModules_simplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left)) :
    (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
      OC).totalRingedHom.toModulesHom.pullbackModules.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulPullbackModulesSimplicialObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L171). The attribute's comment: “a^* on sheaves of modules is fully faithful, for a hypercovering of X by a simplicial object of the site”.

> **Stacks 0DAB, full faithfulness of `a^*` on sheaves of modules.**

```lean
def fullyFaithfulPullbackModulesSimplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left)) :
    (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
      OC).totalRingedHom.toModulesHom.pullbackModules.FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.essImage_pullbackModules_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L188). The attribute's comment: “every cartesian O-module is an a^*M, for a hypercovering of X by a simplicial object of the site”.

> **Stacks 0DAB, essential surjectivity onto the cartesian `O`-modules.** In the situation
> above, every cartesian sheaf of `O`-modules on the total site is a pullback `a^*M`.
>
> This is Stacks 0DA4 for the associated simplicial semi-representable object of Stacks 0GM9.

```lean
theorem essImage_pullbackModules_simplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left))
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X)
        (associatedSimplicialObject.{u} U a)).totalTopology)
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O))}
    (hF : (situation (P.toGrothendieck.over X)
      (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
        (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O F) :
    (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
      OC).totalRingedHom.toModulesHom.pullbackModules.essImage F
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_pullbackModules_iff_isCartesianModule_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L211). The attribute's comment: “the essential image of a^* on sheaves of modules is exactly the cartesian O-modules, for a hypercovering of X by a simplicial object of the site”.

> **Stacks 0DAB, the essential image of `a^*` is exactly the cartesian `O`-modules.** One
> inclusion is `isCartesianModule_of_mem_essImage_simplicialObject`, the other is
> `essImage_pullbackModules_simplicialObject`.

```lean
theorem mem_essImage_pullbackModules_iff_isCartesianModule_simplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left))
    (F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X)
        (associatedSimplicialObject.{u} U a)).totalTopology)
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O))) :
    (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
        OC).totalRingedHom.toModulesHom.pullbackModules.essImage F ↔
      (situation (P.toGrothendieck.over X)
        (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
          (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O F
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_unit_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L234). The attribute's comment: “M = a\_* a^* M on sheaves of modules, for a hypercovering of X by a simplicial object of the site”.

> **Stacks 0DAB, `a_*` is a quasi-inverse on `Mod(O_X)`.** The unit `M ⟶ a_*a^*M` of the
> adjunction of Stacks 03D7 is an isomorphism for every sheaf of `O_X`-modules.

```lean
theorem isIso_pullbackAdjPushforwardModules_unit_simplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left)) :
    IsIso (AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
        OC).totalRingedHom).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_pullbackAdjPushforwardModules_counit_app_simplicialObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleDescent.lean#L251). The attribute's comment: “a^* a\_* F = F for a cartesian O-module F, for a hypercovering of X by a simplicial object of the site”.

> **Stacks 0DAB, `a_*` is a quasi-inverse on the cartesian `O`-modules.** The counit
> `a^*a_*F ⟶ F` of the adjunction of Stacks 03D7 is an isomorphism at every cartesian sheaf of
> `O`-modules.

```lean
theorem isIso_pullbackAdjPushforwardModules_counit_app_simplicialObject
    (h₀ : Presieve.singleton (a.app (op ⦋0⦌)) ∈ P X)
    (h₁ : Presieve.singleton (oneSimplexToFiberProduct U a) ∈
      P (pullback (a.app (op ⦋0⦌)) (a.app (op ⦋0⦌))))
    (hmatch : ∀ n : ℕ, 1 ≤ n → Presieve.singleton (matchingMap U a n) ∈
      P ((((SimplicialObject.cosk n).obj (Over.lift U a)).obj (op ⦋n + 1⦌)).left))
    {F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (situation (P.toGrothendieck.over X)
        (associatedSimplicialObject.{u} U a)).totalTopology)
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O))}
    (hF : (situation (P.toGrothendieck.over X)
      (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
        (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O F) :
    IsIso ((AlgebraicGeometry.RingedToposHom.pullbackAdjPushforwardModules
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
        OC).totalRingedHom).counit.app F)
```

## Tag 0DAC, a lemma

[Tag 0DAC](https://stacks.math.columbia.edu/tag/0DAC) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedPullbackPushforwardUnit_app_of_isHypercoveringAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleCohomologicalDescentUnconditional.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringSimplicialObjectModuleCohomologicalDescentUnconditional.lean#L308).

> **Stacks 0DAC.** Let `C` be a site with fibre products, `X` an object of `C`, `O_C` a sheaf
> of commutative rings on `C` and `a : U ⟶ X` a hypercovering of `X` in `C` by a simplicial
> object `U` of `C` (Stacks, Section 85.21). With `O_X = O_C|_{C/X}`, `O = a⁻¹O_X` on the total
> site of `U` and `a : (Sh((C/U)_total), O) ⟶ (Sh(C/X), O_X)` the ringed augmentation of
> Stacks 0D9X, the canonical map
>
> `E ⟶ R a_* L a^* E`
>
> is an isomorphism for every object `E` of the unbounded derived category `D(O_X)` of sheaves of
> `O_X`-modules.
>
> As in the source this is Stacks 0DA5 for the hypercovering of `X` by semi-representable objects
> with one summand in each degree that `a` determines
> (`CategoryTheory.SimplicialSemiRepresentable.IsHypercoveringAugmentation.isHypercovering`).

```lean
theorem isIso_derivedPullbackPushforwardUnit_app_of_isHypercoveringAugmentation
    (h : IsHypercoveringAugmentation P U a)
    (E : DerivedCategory (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf
      (J := (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
        OC).augmentationRingedTopos.J))
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
        OC).augmentationRingedTopos.O))) :
    IsIso ((AlgebraicGeometry.RingedToposHom.derivedPullbackPushforwardUnit
      (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a)
        OC).totalRingedHom).app E)
```

## Tag 0DAD, a lemma

[Tag 0DAD](https://stacks.math.columbia.edu/tag/0DAD) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.derivedModuleSectionsOverObjectIsoOfIsHypercoveringAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean#L375).

> Let `C` be a site with fibre products, `X` an object of `C`, `O_C` a sheaf of commutative rings
> on `C` and `a : U ⟶ X` a hypercovering of `X` in `C` by a simplicial object `U` of `C`. With
> `O_X = O_C|_{C/X}`, `O = a⁻¹O_X` on the total site `(C/U)_total` and
> `a : (Sh((C/U)_total), O) ⟶ (Sh(C/X), O_X)` the ringed augmentation, there is a canonical
> isomorphism
>
> `RΓ(X, E) = RΓ((C/U)_total, La^*E)`
>
> naturally in `E` in the unbounded derived category `D(O_C)`. Here `RΓ(X, -)` takes values in
> `D(O_C(X))`, `La^*E` is `La^*` of the restriction of `E` to `C/X`, and the right hand side, which
> lives in `D(Γ((C/U)_total, O))`, is read in `D(O_C(X))` through the canonical ring map
> `O_C(X) ⟶ Γ((C/U)_total, O)` (`totalSectionsRingHom`).
>
> This is `derivedModuleSectionsOverObjectIsoOfIsHypercovering` for the hypercovering of `X` by
> semi-representable objects with one summand in each degree that `a` determines
> (`IsHypercoveringAugmentation.isHypercovering`).

```lean
def derivedModuleSectionsOverObjectIsoOfIsHypercoveringAugmentation
    (h : IsHypercoveringAugmentation P U a) :
    derivedModuleSectionsOverObject P X OC ≅
      Stacks.Cohomology.Localization.derivedRestriction (ringedSite P OC) X ⋙
        (RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
          (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
          (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)
          (augmentationHom P (associatedSimplicialObject.{u} U a) OC)).functor ⋙
        derivedTotalGlobalSections P (associatedSimplicialObject.{u} U a) OC ⋙
          (ModuleCat.restrictScalars
            (totalSectionsRingHom P (associatedSimplicialObject.{u} U a) OC)).mapDerivedCategory
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedModuleSectionsOverObjectIsoOfIsHypercoveringAugmentation_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleDerivedSections.lean#L396). The attribute's comment: “the forward map of the isomorphism is the canonical one: RΓ(C/X, -) of the derived unit E|\_X ⟶ Ra\_*La^*(E|\_X), between RΓ(X, E) = RΓ(C/X, E|\_X) and the factorisation of Tag 08J6”.

> At every `E` of `D(O_C)` the forward map of
> `derivedModuleSectionsOverObjectIsoOfIsHypercoveringAugmentation` is `RΓ(C/X, -)` of the derived
> unit `E|_X ⟶ Ra_*La^*(E|_X)` of the ringed augmentation, preceded by the comparison
> `RΓ(X, E) = RΓ(C/X, E|_X)` and followed by the factorisation
> `RΓ(C/X, Ra_*-) = RΓ((C/U)_total, -)`.

```lean
theorem derivedModuleSectionsOverObjectIsoOfIsHypercoveringAugmentation_hom_app
    (h : IsHypercoveringAugmentation P U a)
    (E : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf OC))) :
    (derivedModuleSectionsOverObjectIsoOfIsHypercoveringAugmentation P OC U a h).hom.app E =
      (derivedModuleSectionsOverObjectIsoRestriction P OC).hom.app E ≫
        (derivedModuleSectionsAtId P X OC).map
          ((RingedToposHom.derivedPullbackPushforwardUnit
            (augmentationHom P (associatedSimplicialObject.{u} U a) OC)).app
            ((Stacks.Cohomology.Localization.derivedRestriction (ringedSite P OC) X).obj E)) ≫
        (derivedPushforwardModuleSectionsAtIdIso P (associatedSimplicialObject.{u} U a) OC).hom.app
          ((RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
            (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
            (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)
            (augmentationHom P (associatedSimplicialObject.{u} U a) OC)).functor.obj
              ((Stacks.Cohomology.Localization.derivedRestriction (ringedSite P OC) X).obj E))
```

## Tag 0DAE, a lemma

[Tag 0DAE](https://stacks.math.columbia.edu/tag/0DAE) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.exists_derivedPullbackEquivalence_isHypercoveringAugmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleBoundedBelowEquivalence.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/HypercoveringObjectModuleBoundedBelowEquivalence.lean#L352).

> Let `C` be a site with fibre products, given by a pretopology `P`, let `X` be an object of
> `C`, let `O_C` be a sheaf of commutative rings on `C` and let `a : U ⟶ X` be a hypercovering of
> `X` in `C` by a simplicial object `U` of `C` (`IsHypercoveringAugmentation`). Let
> `O_X = O_C|_{C/X}`, let `O = a⁻¹O_X` on the total site `(C/U)_total` and let
> `a : (Sh((C/U)_total), O) ⟶ (Sh(C/X), O_X)` be the ringed augmentation of Stacks 0D9X. Then
>
> * the cartesian `O`-modules form a weak Serre subcategory `𝒜 ⊂ Mod(O)`, and
> * the functor `La^*` defines an equivalence `D⁺(O_X) ⟶ D⁺_𝒜(O)` with quasi-inverse `R a_*`:
>   there is an equivalence of categories whose functor, followed by the inclusion of `D⁺_𝒜(O)`, is
>   `La^*` on `D⁺(O_X)`, and whose inverse, followed by the inclusion of `D⁺(O_X)`, is `R a_*` on
>   `D⁺_𝒜(O)`.
>
> Here `D⁺(O_X)` is the full subcategory of bounded below objects of `D(O_X)`, and `D⁺_𝒜(O)` that of
> bounded below objects of `D(O)` all of whose cohomology modules are cartesian. The equivalence is
> `derivedPullbackEquivalenceOfIsHypercoveringAugmentation`.

```lean
theorem exists_derivedPullbackEquivalence_isHypercoveringAugmentation
    (h : IsHypercoveringAugmentation P U a) :
    ObjectProperty.IsWeakSerreClass
        ((situation (P.toGrothendieck.over X)
          (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
          (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O) ∧
      ∃ e : (RingedToposHom.derivedPlusTarget
          (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)).FullSubcategory ≌
          (RingedToposHom.derivedPlusProperty
          (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
          ((situation (P.toGrothendieck.over X)
          (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
          (hypercoveringObjectRingedAugmentation P
            (associatedSimplicialObject.{u} U a) OC).O)).FullSubcategory,
        e.functor ⋙ (RingedToposHom.derivedPlusProperty
          (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
          ((situation (P.toGrothendieck.over X)
          (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
          (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O)).ι =
          (RingedToposHom.derivedPlusTarget
          (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)).ι ⋙
            (RingedToposHom.leftDerivedPullbackOfIsIsoFSharp
          (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
          (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)
          (augmentationHom P (associatedSimplicialObject.{u} U a) OC)).functor ∧
        e.inverse ⋙ (RingedToposHom.derivedPlusTarget
          (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)).ι =
          (RingedToposHom.derivedPlusProperty
          (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
          ((situation (P.toGrothendieck.over X)
          (associatedSimplicialObject.{u} U a)).IsModuleFiberTransitionIso
          (hypercoveringObjectRingedAugmentation P (associatedSimplicialObject.{u} U a) OC).O)).ι ⋙
            Stacks.Cohomology.DerivedPushforward.derivedPushforward
          (X := totalTopos P (associatedSimplicialObject.{u} U a) OC)
          (Y := sliceTopos P (associatedSimplicialObject.{u} U a) OC)
          (augmentationHom P (associatedSimplicialObject.{u} U a) OC)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.22, Tag 0DAA](https://stacks.math.columbia.edu/tag/0DAA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
