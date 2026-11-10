---
declaration: section
origin: cited
lean: CategoryTheory.PresheafOfCategories.elementsMapEquiv, CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isPullback, CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isLimit_binaryFan, CategoryTheory.presheafOfGroupoids, CategoryTheory.isFiberedInGroupoids_presheafOfGroupoids, CategoryTheory.Functor.IsSplitFiberedInGroupoids, CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfGroupoids, CategoryTheory.PresheafOfCategories.isFiberedInSets_discreteProjection
statement: formalized
proof: formalized
---

# 94.7 Split categories fibred in groupoids

Section 94.7 of the Stacks Project, [Tag 04SU](https://stacks.math.columbia.edu/tag/04SU). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04SU, the section

[Tag 04SU](https://stacks.math.columbia.edu/tag/04SU) in the Stacks Project.

**`CategoryTheory.PresheafOfCategories.elementsMapEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L95). The attribute's comment: “(e) maps of presheaves F ⟶ G are the 1-morphisms S\_F ⥤ S\_G over the base”.

> **Tag 04SU (e).** The rule `F ↦ 𝒮_F` is fully faithful on presheaves of sets: maps of
> presheaves `F ⟶ G` are in bijection with the 1-morphisms `𝒮_F ⥤ 𝒮_G` strictly over `C`, by
> `m ↦ El m`.

```lean
def elementsMapEquiv (F G : Cᵒᵖ ⥤ Type v) :
    (F ⟶ G) ≃ {θ : (presheafOfCategories (F ⋙ typeToCat)).obj ⥤
        (presheafOfCategories (G ⋙ typeToCat)).obj //
      θ ⋙ discreteProjection G = discreteProjection F}
```

**`CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L117). The attribute's comment: “(f) S\_\{F ×\_H G} = S\_F ×\_\{S\_H} S\_G for maps F → H ← G of presheaves of sets”.

> **Tag 04SU (f), fibre products.** For maps `α : F ⟶ H` and `β : G ⟶ H` of presheaves of sets
> and a fibre product `P = F ×_H G`, the category of elements `𝒮_P` is equivalent to the 2-fibre
> product `𝒮_F ×_{𝒮_H} 𝒮_G` over `C`, by an equivalence which is strictly over `C` and whose
> composites with the two projections are the 1-morphisms induced by the projections of `P`.

```lean
theorem exists_elementsOp_equivalence_of_isPullback {α : F ⟶ H} {β : G ⟶ H} {pF : P ⟶ F}
    {pG : P ⟶ G} (h : IsPullback pF pG α β) :
    ∃ e : P.Elementsᵒᵖ ≌
        TwoFibreProductOver (CategoryOfElements.π F).leftOp (CategoryOfElements.π G).leftOp
          (CategoryOfElements.π H).leftOp (CategoryOfElements.map α).op
          (CategoryOfElements.map β).op,
      e.functor ⋙ structureFunctor _ _ _ _ _ = (CategoryOfElements.π P).leftOp ∧
      e.functor ⋙ fst _ _ _ _ _ = (CategoryOfElements.map pF).op ∧
      e.functor ⋙ snd _ _ _ _ _ = (CategoryOfElements.map pG).op
```

**`CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isLimit_binaryFan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L135). The attribute's comment: “(f) S\_\{F × G} = S\_F ×\_C S\_G for presheaves of sets F, G”.

> **Tag 04SU (f), products.** For a product `P = F × G` of presheaves of sets, the category of
> elements `𝒮_P` is equivalent to the 2-fibre product `𝒮_F ×_C 𝒮_G` over `C` (taken along the two
> structure functors and the identity of `C`), by an equivalence which is strictly over `C` and
> whose composites with the two projections are the 1-morphisms induced by the projections of
> `P`.

```lean
theorem exists_elementsOp_equivalence_of_isLimit_binaryFan {pF : P ⟶ F} {pG : P ⟶ G}
    (h : IsLimit (BinaryFan.mk pF pG)) :
    ∃ e : P.Elementsᵒᵖ ≌
        TwoFibreProductOver (CategoryOfElements.π F).leftOp (CategoryOfElements.π G).leftOp
          (𝟭 C) (CategoryOfElements.π F).leftOp (CategoryOfElements.π G).leftOp,
      e.functor ⋙ structureFunctor _ _ _ _ _ = (CategoryOfElements.π P).leftOp ∧
      e.functor ⋙ fst _ _ _ _ _ = (CategoryOfElements.map pF).op ∧
      e.functor ⋙ snd _ _ _ _ _ = (CategoryOfElements.map pG).op
```

Declarations registered for the tag:

- [`CategoryTheory.presheafOfGroupoids`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Split.lean#L80), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L70) (StacksFrontier): “(a) the category fibred in groupoids S\_F attached to a presheaf of groupoids F”.
- [`CategoryTheory.isFiberedInGroupoids_presheafOfGroupoids`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/OfPresheaf.lean#L100), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L72) (StacksFrontier): “(a) S\_F is fibred in groupoids”.
- [`CategoryTheory.Functor.IsSplitFiberedInGroupoids`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Split.lean#L89), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L74) (StacksFrontier): “(b) split categories fibred in groupoids: isomorphic over the base to some S\_F”.
- [`CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfGroupoids`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean#L955), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L76) (StacksFrontier): “(c) every category fibred in groupoids is equivalent to a split one”.
- [`CategoryTheory.PresheafOfCategories.isFiberedInSets_discreteProjection`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/PresheafElementsStack.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L78) (StacksFrontier): “(d) for a presheaf of sets F, S\_F is fibred in sets”.
- [`CategoryTheory.Functor.twoMorphisms_are_identity`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategoryIsCategory.lean#L137), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L80) (StacksFrontier): “(e) the only 2-morphisms into a category fibred in sets are identities”.
- [`CategoryTheory.overEquivElementsOp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Elements.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L82) (StacksFrontier): “(g) S\_\{h\_X} is the slice category over X”.
- [`CategoryTheory.overEquivElementsOpForget`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Elements.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L84) (StacksFrontier): “(g) the identification of S\_\{h\_X} with the slice category is over the base”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.7, Tag 04SU](https://stacks.math.columbia.edu/tag/04SU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
