---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsFiltered, CategoryTheory.Functor.isFiltered_id_iff, CategoryTheory.Limits.colimitLimitToLimitColimit_isIso, CategoryTheory.Limits.filtered_colim_preservesFiniteLimits_of_types, CategoryTheory.IsFiltered.of_exists_of_isFiltered_of_fullyFaithful, CategoryTheory.Functor.final_of_exists_of_isFiltered_of_fullyFaithful, CategoryTheory.Limits.surjective_prodComparison_colim, CategoryTheory.Limits.colim_prod_surjective_and_not_injective
statement: formalized
proof: formalized
---

# 4.19 Filtered colimits

Section 4.19 of the Stacks Project, [Tag 04AX](https://stacks.math.columbia.edu/tag/04AX). 9 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 002V, a definition

[Tag 002V](https://stacks.math.columbia.edu/tag/002V) in the Stacks Project.

**`CategoryTheory.Functor.IsFiltered`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/Defs.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/Defs.lean#L42).

> **Stacks 002V.** A diagram `M : I ⥤ C` is *filtered* (or *directed*) if
> `I` is nonempty, every pair of objects of `I` admits morphisms into a common
> object, and every pair of parallel morphisms of `I` is equalized, after
> applying `M`, by composition with a further morphism.

```lean
structure Functor.IsFiltered {I : Type u₁} [Category.{v₁} I] {C : Type u₂} [Category.{v₂} C]
    (M : I ⥤ C) : Prop
```

**`CategoryTheory.Functor.isFiltered_id_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/Defs.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/Defs.lean#L60).

> **Stacks 002V.** An index category `I` is filtered in the sense of Stacks —
> the identity diagram `𝟭 I` is a filtered diagram — exactly when it is filtered
> in the sense of Mathlib's `CategoryTheory.IsFiltered`. Since `(𝟭 I).map f = f`,
> condition (3) for `𝟭 I` reads `a ≫ c = b ≫ c` in `I`, so both directions are a
> repackaging of the same data.

```lean
theorem Functor.isFiltered_id_iff (I : Type u₁) [Category.{v₁} I] :
    (𝟭 I).IsFiltered ↔ _root_.CategoryTheory.IsFiltered I
```

## Tag 002W, a lemma

[Tag 002W](https://stacks.math.columbia.edu/tag/002W) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.colimitLimitToLimitColimit_isIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.colimitLimitToLimitColimit_isIso#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch04.lean#L48) (StacksFrontier): “colim over filtered commutes with finite lim”.
- [`CategoryTheory.Limits.filtered_colim_preservesFiniteLimits_of_types`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.filtered_colim_preservesFiniteLimits_of_types#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch04.lean#L50) (StacksFrontier): “finite products, fibre products, equalizers”. References: SGA 4 I (2.8), “more general”; SGA 4 I (3.3), “special case”.

## Tag 0BUC, a lemma

[Tag 0BUC](https://stacks.math.columbia.edu/tag/0BUC) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsFiltered.of_exists_of_isFiltered_of_fullyFaithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsFiltered.of_exists_of_isFiltered_of_fullyFaithful#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Filtered/AbsorbingSubcategory.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/AbsorbingSubcategory.lean#L22) (StacksFrontier): “the subcategory is filtered”. References: SGA 4 I (8.1.3), “c)”.
- [`CategoryTheory.Functor.final_of_exists_of_isFiltered_of_fullyFaithful`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.final_of_exists_of_isFiltered_of_fullyFaithful#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Filtered/AbsorbingSubcategory.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/AbsorbingSubcategory.lean#L25) (StacksFrontier): “the inclusion is cofinal, i.e. final”. References: SGA 4 I (8.1.3), “c)”; SGA 4 I (8.1.4), “cofinal subset ⇒ final”.

## Tag 09WQ, a lemma

[Tag 09WQ](https://stacks.math.columbia.edu/tag/09WQ) in the Stacks Project.

**`CategoryTheory.Limits.surjective_prodComparison_colim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/FiniteProducts.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/FiniteProducts.lean#L51). The attribute's comment: “(1)”.

> **Stacks 09WQ (1).** If every pair of objects of `I` admits a common upper bound,
> then for all set-valued diagrams `M, N : I ⥤ Type v` the canonical comparison
> `colim (M ⨯ N) ⟶ colim M ⨯ colim N` is surjective.
>
> Given a pair of elements, choose representatives at indices `i` and `j`, push both
> along arrows into a common `k`, and pair them there; the resulting element of
> `colim (M ⨯ N)` maps to the original pair.

```lean
theorem surjective_prodComparison_colim [HasColimitsOfShape I (Type v)]
    (h : ∀ x y : I, ∃ (z : I) (_ : x ⟶ z) (_ : y ⟶ z), True)
    (M N : I ⥤ Type v) :
    Function.Surjective (prodComparison (colim : (I ⥤ Type v) ⥤ Type v) M N)
```

**`CategoryTheory.Limits.colim_prod_surjective_and_not_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/FiniteProductsNotInjective.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/FiniteProductsNotInjective.lean#L155).

> **Stacks 09WQ.** Let `I` be a category in which every pair of objects `x, y` admits
> an object `z` with morphisms `x ⟶ z` and `y ⟶ z`. Then
>
> 1. for all diagrams of sets `M, N` over `I`, the comparison
>    `colim (M ⨯ N) ⟶ colim M ⨯ colim N` is surjective;
> 2. in general colimits of diagrams of sets over such index categories do not commute
>    with finite nonempty products: there are such an `I` and diagrams `M, N` for which
>    the comparison is not injective.
>
> Part (1) is `surjective_prodComparison_colim`, part (2) is
> `exists_not_injective_prodComparison_colim`. The instance `HasColimitsOfShape I (Type v)`
> in part (1) only makes the colimit functor available; it holds for every small `I`.

```lean
theorem colim_prod_surjective_and_not_injective :
    (∀ (I : Type u) [Category.{v} I] [HasColimitsOfShape I (Type v)],
      (∀ x y : I, ∃ (z : I) (_ : x ⟶ z) (_ : y ⟶ z), True) →
      ∀ M N : I ⥤ Type v,
        Function.Surjective (prodComparison (colim : (I ⥤ Type v) ⥤ Type v) M N)) ∧
    ∃ (I : Type) (_ : SmallCategory I),
      (∀ x y : I, ∃ (z : I) (_ : x ⟶ z) (_ : y ⟶ z), True) ∧
      ∃ M N : I ⥤ Type v,
        ¬ Function.Injective (prodComparison (colim : (I ⥤ Type v) ⥤ Type v) M N)
```

## Tag 09WR, a lemma

[Tag 09WR](https://stacks.math.columbia.edu/tag/09WR) in the Stacks Project.

**`CategoryTheory.Limits.surjective_setColimit_to_addCommGrpColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/AbelianGroups.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/AbelianGroups.lean#L118).

> **Stacks 09WR.** Let `I` be a nonempty category in which every pair of objects
> has a common upper bound. Then for any diagram `M : I ⥤ AddCommGrpCat` the canonical
> comparison from the colimit of the underlying sets to the underlying set of the
> colimit in `AddCommGrpCat` is surjective.

```lean
theorem surjective_setColimit_to_addCommGrpColimit
    {I : Type u} [Category.{v} I] [Nonempty I]
    (hI : ∀ x y : I, ∃ (z : I) (_ : x ⟶ z) (_ : y ⟶ z), True)
    (M : I ⥤ AddCommGrpCat.{w})
    [HasColimit (M ⋙ forget AddCommGrpCat)] [HasColimit M] :
    Function.Surjective
      (colimit.desc (M ⋙ forget AddCommGrpCat)
        ((forget AddCommGrpCat).mapCocone (colimit.cocone M)))
```

## Tag 09WS, a lemma

[Tag 09WS](https://stacks.math.columbia.edu/tag/09WS) in the Stacks Project.

**`CategoryTheory.hasSpanCocone_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/ConnectedComponents.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/ConnectedComponents.lean#L43).

> **Stacks 09WS.** Each connected component of a category with span cocones again has
> span cocones. Together with `CategoryTheory.instIsConnectedComponent` and
> `CategoryTheory.decomposedTo` this exhibits such a category as a disjoint union of
> connected categories with span cocones.

```lean
theorem hasSpanCocone_component {J : Type u} [Category.{v} J] (h : HasSpanCocone J)
    (j : ConnectedComponents J) : HasSpanCocone j.Component
```

## Tag 09WT, a lemma

[Tag 09WT](https://stacks.math.columbia.edu/tag/09WT) in the Stacks Project.

**`CategoryTheory.Limits.colimMap_injective_of_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/Injectivity.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/Injectivity.lean#L75). The attribute's comment: “(1)”.

> **Stacks 09WT (1).** If every span in `I` admits a commutative completion, then a
> componentwise-injective natural transformation between `Type`-valued diagrams over `I`
> induces an injective map on colimits.

```lean
theorem colimMap_injective_of_span
    {I : Type u} [Category.{v} I] (hI : HasSpanCocone I)
    {M N : I ⥤ Type w} [HasColimit M] [HasColimit N]
    (α : M ⟶ N) (hα : ∀ i : I, Function.Injective (α.app i)) :
    Function.Injective (colimMap α : colimit M ⟶ colimit N)
```

**`CategoryTheory.Limits.exists_diagram_addCommGrp_colimMap_not_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/Injectivity.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/Injectivity.lean#L262). The attribute's comment: “(2)”.

> **Stacks 09WT (2).** The analogue of part (1) fails for `AddCommGrp`-valued diagrams:
> there is a span-completing index category and a componentwise-injective natural
> transformation of diagrams of abelian groups whose induced map on colimits is not
> injective.

```lean
theorem exists_diagram_addCommGrp_colimMap_not_injective :
    ∃ (I : Type) (_ : SmallCategory I) (_ : HasSpanCocone I)
      (M N : I ⥤ AddCommGrpCat.{0}) (α : M ⟶ N)
      (_ : ∀ i : I, Function.Injective (α.app i)),
      ¬ Function.Injective (colimMap α)
```

## Tag 002X, a lemma

[Tag 002X](https://stacks.math.columbia.edu/tag/002X) in the Stacks Project.

**`CategoryTheory.isFiltered_component_of_cocone_and_coequaliser`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/SpanCocones.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/SpanCocones.lean#L71). References: SGA 4 I (2.7.1), “pseudo-filtered part”.

> A category with span cocones and coequalizing morphisms is a disjoint union of filtered
> categories: every connected component of it is filtered.

```lean
theorem isFiltered_component_of_cocone_and_coequaliser
    (h1 : HasSpanCocone J) (h2 : HasCoequalizingHom J) (j : ConnectedComponents J) :
    IsFiltered j.Component
```

## Tag 002Y, a lemma

[Tag 002Y](https://stacks.math.columbia.edu/tag/002Y) in the Stacks Project.

**`CategoryTheory.Limits.preservesLimitsOfShape_colim_of_isConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/AlmostDirected.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/AlmostDirected.lean#L395). References: SGA 4 I (2.8), “finite connected limits”.

> For an almost-directed index category `I` and every finite connected shape `L`, the colimit
> functor `colim : (I ⥤ Type v) ⥤ Type v` commutes with `L`-shaped limits.

```lean
theorem preservesLimitsOfShape_colim_of_isConnected (I : Type u) [Category.{v'} I] [Small.{v} I]
    [IsAlmostDirected.{v'} I] (L : Type w) [SmallCategory L] [FinCategory L] [IsConnected L] :
    PreservesLimitsOfShape L (colim : (I ⥤ Type v) ⥤ Type v)
```

**`CategoryTheory.Limits.preservesLimitsOfShape_walkingCospan_colim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/AlmostDirected.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/AlmostDirected.lean#L403). References: SGA 4 I (2.8), “fibre products only”.

> Colimits over an almost-directed index category commute with fibre products of sets.

```lean
theorem preservesLimitsOfShape_walkingCospan_colim (I : Type u) [Category.{v'} I] [Small.{v} I]
    [IsAlmostDirected.{v'} I] :
    PreservesLimitsOfShape WalkingCospan (colim : (I ⥤ Type v) ⥤ Type v)
```

**`CategoryTheory.Limits.preservesLimitsOfShape_walkingParallelPair_colim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/AlmostDirected.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/AlmostDirected.lean#L410). References: SGA 4 I (2.8), “equalizers only”.

> Colimits over an almost-directed index category commute with equalizers of sets.

```lean
theorem preservesLimitsOfShape_walkingParallelPair_colim (I : Type u) [Category.{v'} I]
    [Small.{v} I] [IsAlmostDirected.{v'} I] :
    PreservesLimitsOfShape WalkingParallelPair (colim : (I ⥤ Type v) ⥤ Type v)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.19, Tag 04AX](https://stacks.math.columbia.edu/tag/04AX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
