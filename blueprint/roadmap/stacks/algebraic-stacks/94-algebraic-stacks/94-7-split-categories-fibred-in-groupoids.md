---
declaration: section
origin: cited
lean: CategoryTheory.PresheafOfCategories.elementsMapEquiv, CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isPullback, CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isLimit_binaryFan, CategoryTheory.presheafOfGroupoids, CategoryTheory.isFiberedInGroupoids_presheafOfGroupoids, CategoryTheory.Functor.IsSplitFiberedInGroupoids, CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfGroupoids, CategoryTheory.PresheafOfCategories.isFiberedInSets_discreteProjection
statement: formalized
proof: formalized
---

# 94.7 Split categories fibred in groupoids

Section 94.7 of the Stacks Project, [Tag 04SU](https://stacks.math.columbia.edu/tag/04SU). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04SU, the section

[Tag 04SU](https://stacks.math.columbia.edu/tag/04SU) in the Stacks Project.

**`CategoryTheory.PresheafOfCategories.elementsMapEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L100). The attribute's comment: “(e) maps of presheaves F ⟶ G are the 1-morphisms S\_F ⥤ S\_G over the base”.

> **Tag 04SU (e).** The rule `F ↦ 𝒮_F` is fully faithful on presheaves of sets: maps of
> presheaves `F ⟶ G` are in bijection with the 1-morphisms `𝒮_F ⥤ 𝒮_G` strictly over `C`, by
> `m ↦ El m`.

```lean
def elementsMapEquiv (F G : Cᵒᵖ ⥤ Type v) :
    (F ⟶ G) ≃ {θ : (presheafOfCategories (F ⋙ typeToCat)).obj ⥤
        (presheafOfCategories (G ⋙ typeToCat)).obj //
      θ ⋙ discreteProjection G = discreteProjection F}
```

**`CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L122). The attribute's comment: “(f) S\_\{F ×\_H G} = S\_F ×\_\{S\_H} S\_G for maps F → H ← G of presheaves of sets”.

> **Tag 04SU (f), fibre products.** For maps `α : F ⟶ H` and `β : G ⟶ H` of presheaves of sets
> and a fibre product `P = F ×_H G`, the category of elements `𝒮_P` is equivalent to the 2-fibre
> product `𝒮_F ×_{𝒮_H} 𝒮_G` over `C`, by an equivalence which is strictly over `C` and whose
> composites with the two projections are the 1-morphisms induced by the projections of `P`.

```lean
theorem exists_elementsOp_equivalence_of_isPullback {α : F ⟶ H} {β : G ⟶ H} {pF : P ⟶ F}
    {pG : P ⟶ G} (h : IsPullback pF pG α β) :
    ∃ e : P.Elementsᵒᵖ ≌
        TwoFibreProductOver (Functor.Elements.π F).leftOp (Functor.Elements.π G).leftOp
          (Functor.Elements.π H).leftOp (NatTrans.mapElements α).op
          (NatTrans.mapElements β).op,
      e.functor ⋙ structureFunctor _ _ _ _ _ = (Functor.Elements.π P).leftOp ∧
      e.functor ⋙ fst _ _ _ _ _ = (NatTrans.mapElements pF).op ∧
      e.functor ⋙ snd _ _ _ _ _ = (NatTrans.mapElements pG).op
```

**`CategoryTheory.TwoFibreProductOver.exists_elementsOp_equivalence_of_isLimit_binaryFan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L140). The attribute's comment: “(f) S\_\{F × G} = S\_F ×\_C S\_G for presheaves of sets F, G”.

> **Tag 04SU (f), products.** For a product `P = F × G` of presheaves of sets, the category of
> elements `𝒮_P` is equivalent to the 2-fibre product `𝒮_F ×_C 𝒮_G` over `C` (taken along the two
> structure functors and the identity of `C`), by an equivalence which is strictly over `C` and
> whose composites with the two projections are the 1-morphisms induced by the projections of
> `P`.

```lean
theorem exists_elementsOp_equivalence_of_isLimit_binaryFan {pF : P ⟶ F} {pG : P ⟶ G}
    (h : IsLimit (BinaryFan.mk pF pG)) :
    ∃ e : P.Elementsᵒᵖ ≌
        TwoFibreProductOver (Functor.Elements.π F).leftOp (Functor.Elements.π G).leftOp
          (𝟭 C) (Functor.Elements.π F).leftOp (Functor.Elements.π G).leftOp,
      e.functor ⋙ structureFunctor _ _ _ _ _ = (Functor.Elements.π P).leftOp ∧
      e.functor ⋙ fst _ _ _ _ _ = (NatTrans.mapElements pF).op ∧
      e.functor ⋙ snd _ _ _ _ _ = (NatTrans.mapElements pG).op
```

Declarations registered for the tag:

- [`CategoryTheory.presheafOfGroupoids`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Split.lean#L83), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L75) (StacksFrontier): “(a) the category fibred in groupoids S\_F attached to a presheaf of groupoids F”.
- [`CategoryTheory.isFiberedInGroupoids_presheafOfGroupoids`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/OfPresheaf.lean#L100), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L77) (StacksFrontier): “(a) S\_F is fibred in groupoids”.
- [`CategoryTheory.Functor.IsSplitFiberedInGroupoids`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInGroupoids/Split.lean#L92), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L79) (StacksFrontier): “(b) split categories fibred in groupoids: isomorphic over the base to some S\_F”.
- [`CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfGroupoids`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean#L961), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L81) (StacksFrontier): “(c) every category fibred in groupoids is equivalent to a split one”.
- [`CategoryTheory.PresheafOfCategories.isFiberedInSets_discreteProjection`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/PresheafElementsStack.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L83) (StacksFrontier): “(d) for a presheaf of sets F, S\_F is fibred in sets”.
- [`CategoryTheory.Functor.twoMorphisms_are_identity`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSets/TwoCategoryIsCategory.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L85) (StacksFrontier): “(e) the only 2-morphisms into a category fibred in sets are identities”.
- [`CategoryTheory.overEquivElementsOp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Elements.lean#L95), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L87) (StacksFrontier): “(g) S\_\{h\_X} is the slice category over X”.
- [`CategoryTheory.overEquivElementsOpForget`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Elements.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SplitCategoriesFibredInGroupoids.lean#L89) (StacksFrontier): “(g) the identification of S\_\{h\_X} with the slice category is over the base”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.7, Tag 04SU](https://stacks.math.columbia.edu/tag/04SU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
