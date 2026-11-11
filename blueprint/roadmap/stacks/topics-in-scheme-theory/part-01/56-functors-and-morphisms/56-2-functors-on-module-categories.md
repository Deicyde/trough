---
declaration: section
origin: cited
lean: ModuleCat.filteredColimitExtension, ModuleCat.FilteredColimitExtension.existsUnique_iso, ModuleCat.filteredColimitExtension_additive, ModuleCat.filteredColimitExtension_preservesCoproducts, ModuleCat.filteredColimitExtension_functor_additive, ModuleCat.filteredColimitExtension_functor_preservesFiniteColimits, ModuleCat.filteredColimitExtension_functor_preservesCoproducts, ModuleCat.filteredColimitExtension_preservesFiniteLimits
statement: formalized
proof: formalized
---

# 56.2 Functors on module categories

Section 56.2 of the Stacks Project, [Tag 0GNI](https://stacks.math.columbia.edu/tag/0GNI). 6 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GNJ, a lemma

[Tag 0GNJ](https://stacks.math.columbia.edu/tag/0GNJ) in the Stacks Project.

**`ModuleCat.filteredColimitExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean#L71). The attribute's comment: “existence”. References: SGA 4 I (8.7.3), “existence, C=Mod^fp\_A”.

> A functor on finitely presented modules has an extension to all modules which preserves
> filtered colimits.

```lean
public noncomputable def filteredColimitExtension
    [HasFilteredColimitsOfSize.{max u v, max u v} B]
    (F : CategoryTheory.Functor (FinitelyPresentedModuleCat.{u, max u v} A) B) :
    FilteredColimitExtension A F
```

**`ModuleCat.FilteredColimitExtension.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Extension.lean#L89). The attribute's comment: “uniqueness”. References: SGA 4 I (8.7.3), “uniqueness, C=Mod^fp\_A”; SGA 4 I (8.7.2), “special case”.

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

## Tag 0GNK, a lemma

[Tag 0GNK](https://stacks.math.columbia.edu/tag/0GNK) in the Stacks Project.

**`ModuleCat.filteredColimitExtension_additive`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean#L215). The attribute's comment: “additivity”.

> A filtered-colimit-preserving extension of an additive functor from finitely presented
> modules is additive.

```lean
public lemma filteredColimitExtension_additive
    (E : FilteredColimitExtension A F) [F.Additive] :
    E.functor.Additive
```

**`ModuleCat.filteredColimitExtension_preservesCoproducts`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean#L222). The attribute's comment: “arbitrary direct sums”.

> A filtered-colimit-preserving extension of an additive functor from finitely presented
> modules preserves arbitrary direct sums.

```lean
public lemma filteredColimitExtension_preservesCoproducts
    (E : FilteredColimitExtension A F) [F.Additive]
    (J : Type (max u v)) :
    PreservesColimitsOfShape (Discrete J) E.functor
```

## Tag 0GNL, a lemma

[Tag 0GNL](https://stacks.math.columbia.edu/tag/0GNL) in the Stacks Project.

**`ModuleCat.filteredColimitExtension_functor_additive`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean#L620). The attribute's comment: “additivity”.

> The extension of a right exact functor on finitely presented modules to all modules is
> additive.

```lean
public lemma filteredColimitExtension_functor_additive :
    (filteredColimitExtension A G).functor.Additive
```

**`ModuleCat.filteredColimitExtension_functor_preservesFiniteColimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean#L627). The attribute's comment: “right exactness”.

> The extension of a right exact functor on finitely presented modules to all modules is
> right exact.

```lean
public lemma filteredColimitExtension_functor_preservesFiniteColimits :
    PreservesFiniteColimits (filteredColimitExtension A G).functor
```

**`ModuleCat.filteredColimitExtension_functor_preservesCoproducts`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RightExact.lean#L634). The attribute's comment: “arbitrary direct sums”.

> The extension of a right exact functor on finitely presented modules to all modules
> commutes with arbitrary direct sums.

```lean
public lemma filteredColimitExtension_functor_preservesCoproducts (J : Type (max u v)) :
    PreservesColimitsOfShape (Discrete J) (filteredColimitExtension A G).functor
```

## Tag 0GNM, a lemma

[Tag 0GNM](https://stacks.math.columbia.edu/tag/0GNM) in the Stacks Project.

**`ModuleCat.filteredColimitExtension_preservesFiniteLimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/LeftExact.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/LeftExact.lean#L385). The attribute's comment: “left exactness”.

> If filtered colimits commute with kernels in the target, the filtered-colimit extension
> of a left exact functor on finitely presented modules is left exact.

```lean
public lemma filteredColimitExtension_preservesFiniteLimits
    [IsCoherentRing A] (E : FilteredColimitExtension A F) [HasKernels B]
    [PreservesFiniteLimits F]
    [HasFilteredColimitsOfSize.{max u v, max u v} B]
    [∀ (J : Type (max u v)) [Category.{max u v} J] [IsFiltered J],
      ∀ {X Y : J ⥤ B} (f : X ⟶ Y),
        PreservesLimit (parallelPair f 0) (colim : (J ⥤ B) ⥤ B)] :
    PreservesFiniteLimits E.functor
```

Declarations registered for the tag:

- [`ModuleCat.filteredColimitExtension_additive`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean#L215), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/LeftExact.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/LeftExact.lean#L379) (StacksFrontier): “additivity”.
- [`ModuleCat.filteredColimitExtension_preservesCoproducts`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/Additivity.lean#L222), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/LeftExact.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/LeftExact.lean#L380) (StacksFrontier): “arbitrary direct sums”.

## Tag 0GNN, a lemma

[Tag 0GNN](https://stacks.math.columbia.edu/tag/0GNN) in the Stacks Project.

**`ModuleCat.rightExactFunctor_additive`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/ModuleAction.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/ModuleAction.lean#L235). The attribute's comment: “automatic additivity”.

> A right exact functor on finitely presented modules is automatically additive.

```lean
public lemma rightExactFunctor_additive (A : Type u) (B : Type v) [Ring A]
    [Category.{w} B] [Preadditive B] [HasFiniteBiproducts B]
    (F : FPModule A ⥤ᵣ B) : F.obj.Additive
```

**`ModuleCat.evaluationFunctor_isEquivalence`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/ModuleActionEquivalence.lean, line 889](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/ModuleActionEquivalence.lean#L889).

> Evaluation on the rank-one free module, with its natural action, classifies right
> exact functors on finitely presented modules.

```lean
public lemma evaluationFunctor_isEquivalence (A : Type u) (B : Type v) [Ring A]
    [Category.{w} B] [Preadditive B] [HasFiniteBiproducts B] [HasCokernels B] :
    (evaluationFunctor A B).IsEquivalence
```

## Tag 0GNQ, a lemma

[Tag 0GNQ](https://stacks.math.columbia.edu/tag/0GNQ) in the Stacks Project.

**`ModuleCat.functorToRingActions_isEquivalence`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RingActions.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FunctorsAndMorphisms/FunctorsModuleCategories/RingActions.lean#L475). References: EGA III (7.2.6).

> Evaluation on the right regular module, with its natural `A`-action, classifies right exact
> functors which preserve arbitrary coproducts.

```lean
public lemma functorToRingActions_isEquivalence :
    (functorToRingActions A B).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 56.2, Tag 0GNI](https://stacks.math.columbia.edu/tag/0GNI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
