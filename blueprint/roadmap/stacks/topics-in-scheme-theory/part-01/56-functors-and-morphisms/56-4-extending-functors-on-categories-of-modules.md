---
declaration: section
origin: cited
lean: ModuleCat.filteredColimitExtension, ModuleCat.FilteredColimitExtension.existsUnique_iso, ModuleCat.finitelyPresentedModule_isMonoidal, ModuleCat.filteredColimitExtension_monoidal, ModuleCat.filteredColimitExtension_additive, ModuleCat.filteredColimitExtension_preservesCoproducts, ModuleCat.filteredColimitExtension_preservesFiniteColimits, ModuleCat.filteredColimitExtension_preservesFiniteLimits_moduleValued
statement: formalized
proof: formalized
---

# 56.4 Extending functors on categories of modules

Section 56.4 of the Stacks Project, [Tag 0GP3](https://stacks.math.columbia.edu/tag/0GP3). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GP4, a lemma

[Tag 0GP4](https://stacks.math.columbia.edu/tag/0GP4) in the Stacks Project.

**`ModuleCat.filteredColimitExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean#L71). The attribute's comment: “existence, at the target category of all B-modules”. References: SGA 4 I (8.7.3), “existence, C=Mod^fp\_A”.

> A functor on finitely presented modules has an extension to all modules which preserves
> filtered colimits.

```lean
public noncomputable def filteredColimitExtension
    [HasFilteredColimitsOfSize.{max u v, max u v} B]
    (F : CategoryTheory.Functor (FinitelyPresentedModuleCat.{u, max u v} A) B) :
    FilteredColimitExtension A F
```

**`ModuleCat.FilteredColimitExtension.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean#L89). The attribute's comment: “existence, at the target category of all B-modules”. References: SGA 4 I (8.7.3), “uniqueness, C=Mod^fp\_A”; SGA 4 I (8.7.2), “special case”.

> Two filtered-colimit-preserving extensions are related by a unique natural isomorphism
> compatible with their specified identifications on finitely presented modules.

```lean
public theorem FilteredColimitExtension.existsUnique_iso
    {F : CategoryTheory.Functor (FinitelyPresentedModuleCat.{u, max u v} A) B}
    (E₁ E₂ : FilteredColimitExtension A F) :
    ∃! e : CategoryTheory.Iso E₁.functor E₂.functor,
      Functor.whiskerLeft (finitelyPresentedModule.{u, max u v} A).ι e.hom =
        (CategoryTheory.Iso.trans E₁.iso E₂.iso.symm).hom
```

## Tag 0GP5, a remark

[Tag 0GP5](https://stacks.math.columbia.edu/tag/0GP5) in the Stacks Project.

**`ModuleCat.finitelyPresentedModule_isMonoidal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Monoidal.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Monoidal.lean#L153). The attribute's comment: “monoidal structure on finitely presented modules”.

> Finitely presented modules form a monoidal full subcategory of modules.

```lean
instance finitelyPresentedModule_isMonoidal :
    (finitelyPresentedModule.{u, max u v} R).IsMonoidal
```

**`ModuleCat.filteredColimitExtension_monoidal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Monoidal.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Monoidal.lean#L302). The attribute's comment: “monoidal extension”.

> A monoidal functor on finitely presented modules has a monoidal
> filtered-colimit-preserving extension to all modules.

```lean
theorem filteredColimitExtension_monoidal
    (F : FinitelyPresentedModuleCat.{u, max u v} R ⥤
      FinitelyPresentedModuleCat.{w, max w x} S)
    [F.Monoidal]
    (E : FilteredColimitExtension R
      (F ⋙ (finitelyPresentedModule.{w, max w x} S).ι)) :
    ∃ h : E.functor.Monoidal,
      letI := h
      NatTrans.IsMonoidal E.iso.hom
```

## Tag 0GP6, a lemma

[Tag 0GP6](https://stacks.math.columbia.edu/tag/0GP6) in the Stacks Project.

Declarations registered for the tag:

- [`ModuleCat.filteredColimitExtension_additive`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean#L215), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean#L47) (StacksFrontier): “part (1), additivity”.
- [`ModuleCat.filteredColimitExtension_preservesCoproducts`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean#L222), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean#L48) (StacksFrontier): “part (1), arbitrary direct sums”.
- [`ModuleCat.filteredColimitExtension_preservesFiniteColimits`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean#L438), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean#L50) (StacksFrontier): “part (2)”.

## Tag 0GP8, a lemma

[Tag 0GP8](https://stacks.math.columbia.edu/tag/0GP8) in the Stacks Project.

**`ModuleCat.filteredColimitExtension_preservesFiniteLimits_moduleValued`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/LeftExactness.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/LeftExactness.lean#L204).

> **Stacks Project, Tag 0GP8.** The filtered-colimit-preserving extension of a left exact
> functor on finitely presented modules is left exact when the source ring is coherent. This is
> the module-valued form: the functor takes values in all modules over the second ring, not only
> in the finitely presented ones.

```lean
theorem filteredColimitExtension_preservesFiniteLimits_moduleValued
    (A : Type u) [CommRing A] [IsCoherentRing A]
    (B : Type w) [Ring B]
    (F : FinitelyPresentedModuleCat.{u, max u v} A ⥤
      ModuleCat.{max w x} B)
    (E : FilteredColimitExtension A F)
    [PreservesFiniteLimits F] :
    PreservesFiniteLimits E.functor
```

## Tag 0GP9, a lemma

[Tag 0GP9](https://stacks.math.columbia.edu/tag/0GP9) in the Stacks Project.

**`ModuleCat.fgFilteredColimitExtension_additive`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Additivity.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Additivity.lean#L46). The attribute's comment: “additivity”.

> **Stacks Project, Tag 0GP9.** Every filtered-colimit-preserving extension of an additive
> functor on finite modules is additive.

```lean
instance fgFilteredColimitExtension_additive
    {F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B}
    (E : FGFilteredColimitExtension.{u, v, w} A B F) [F.Additive] :
    E.functor.Additive
```

**`ModuleCat.FGFilteredColimitExtension.preservesCoproducts`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/DirectSums.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/DirectSums.lean#L44). The attribute's comment: “direct\_sums”.

> **Stacks Project, Tag 0GP9.** An additive functor on finite modules has a
> direct-sum-preserving filtered-colimit extension to all modules.

```lean
lemma FGFilteredColimitExtension.preservesCoproducts
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (B : Type w) [CommRing B]
    {F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B}
    (E : FGFilteredColimitExtension.{u, v, w} A B F)
    [F.Additive] (J : Type v) :
    PreservesColimitsOfShape (Discrete J) E.functor
```

**`ModuleCat.FGFilteredColimitExtension.exactFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/ExactFunctor.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/ExactFunctor.lean#L43). The attribute's comment: “exactness”.

> **Stacks Project, Tag 0GP9.** A filtered-colimit extension of an exact functor between
> finite module categories over Noetherian rings is exact.

```lean
theorem FGFilteredColimitExtension.exactFunctor
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (B : Type w) [CommRing B] [IsNoetherianRing B]
    (F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B)
    (E : FGFilteredColimitExtension.{u, v, w} A B F)
    (hF : exactFunctor (FGModuleCat.{v} A) (FGModuleCat.{v} B) F) :
    exactFunctor (ModuleCat.{v} A) (ModuleCat.{v} B) E.functor
```

**`ModuleCat.fgFilteredColimitExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Extension.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Extension.lean#L384). The attribute's comment: “extension”.

> **Stacks Project, Tag 0GP9.** A functor between finite module categories over Noetherian
> rings extends to all modules and commutes with filtered colimits.

```lean
noncomputable def fgFilteredColimitExtension
    [IsNoetherianRing A]
    (F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B) :
    FGFilteredColimitExtension.{u, v, w} A B F
```

**`ModuleCat.FGFilteredColimitExtension.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Extension.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/Extension.lean#L443). The attribute's comment: “extension”.

> **Stacks Project, Tag 0GP9.** Two filtered-colimit-preserving extensions are related by a
> unique natural isomorphism compatible with their specified identifications on finite
> modules.

```lean
theorem FGFilteredColimitExtension.existsUnique_iso
    {F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B}
    (E₁ E₂ : FGFilteredColimitExtension.{u, v, w} A B F) :
    ∃! e : E₁.functor ≅ E₂.functor,
      Functor.whiskerLeft (forget₂ (FGModuleCat.{v} A) (ModuleCat.{v} A)) e.hom =
        (E₁.iso.trans E₂.iso.symm).hom
```

**`ModuleCat.fgFilteredColimitExtension_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/LeftExactness.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/LeftExactness.lean#L262). The attribute's comment: “left\_exactness”.

> **Stacks Project, Tag 0GP9.** A left exact functor on finite modules over Noetherian rings
> has a left exact filtered-colimit-preserving extension to all modules.

```lean
theorem fgFilteredColimitExtension_preservesFiniteLimits
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (B : Type w) [CommRing B] [IsNoetherianRing B]
    (F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B)
    (E : FGFilteredColimitExtension.{u, v, w} A B F)
    [PreservesFiniteLimits F] :
    PreservesFiniteLimits E.functor
```

**`ModuleCat.FGFilteredColimitExtension.preservesFiniteColimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/ExtendingFunctorsCategories/RightExactness.lean#L56). The attribute's comment: “right\_exactness”.

> **Stacks Project, Tag 0GP9.** A filtered-colimit extension of a right exact functor on
> finite modules is right exact. The Noetherian hypothesis on `A` is what supplies the extension
> in the first place; the proof below only uses the extension.

```lean
lemma FGFilteredColimitExtension.preservesFiniteColimits
    (A : Type u) [CommRing A] [IsNoetherianRing A] (B : Type w) [CommRing B]
    {F : FGModuleCat.{v} A ⥤ FGModuleCat.{v} B}
    (E : FGFilteredColimitExtension.{u, v, w} A B F)
    [PreservesFiniteColimits F] :
    PreservesFiniteColimits E.functor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.4, Tag 0GP3](https://stacks.math.columbia.edu/tag/0GP3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
