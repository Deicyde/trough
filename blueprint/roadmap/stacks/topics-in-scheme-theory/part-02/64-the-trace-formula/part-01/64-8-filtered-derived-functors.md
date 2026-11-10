---
declaration: section
origin: cited
lean: CategoryTheory.FilteredDerived.filteredProjectiveMinusMapToDerivedMinus, CategoryTheory.FilteredDerived.filteredLeftDerivedFunctor, CategoryTheory.FilteredDerived.filteredLeftDerivedFunctorComparison, CategoryTheory.FilteredDerived.filteredInjectivePlusMapToDerivedPlus, CategoryTheory.FilteredDerived.filteredRightDerivedFunctor, CategoryTheory.FilteredDerived.filteredRightDerivedFunctorComparison, CategoryTheory.FilteredDerived.filteredRightDerivedFunctorGrPIso
statement: formalized
proof: formalized
---

# 64.8 Filtered derived functors

Section 64.8 of the Stacks Project, [Tag 03TC](https://stacks.math.columbia.edu/tag/03TC). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03TD, a definition

[Tag 03TD](https://stacks.math.columbia.edu/tag/03TD) in the Stacks Project.

**`CategoryTheory.FilteredDerived.filteredProjectiveMinusMapToDerivedMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/LeftDerivedFunctor.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/LeftDerivedFunctor.lean#L133). The attribute's comment: “filtered_left_derived_functor”.

> The lower route in the defining diagram: apply `G` termwise to a bounded-above
> complex of filtered projective objects, then pass to the bounded-above filtered
> derived category.

```lean
noncomputable def filteredProjectiveMinusMapToDerivedMinus
    (G : A ⥤ B) [G.Additive] :
    (filteredProjectiveMinus A).FullSubcategory ⥤
      (CochainComplex.FilteredDerivedCategory.minus B).FullSubcategory
```

**`CategoryTheory.FilteredDerived.filteredLeftDerivedFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/LeftDerivedFunctor.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/LeftDerivedFunctor.lean#L162). The attribute's comment: “filtered_left_derived_functor”.

> The filtered left derived functor on bounded-above filtered derived categories.

```lean
noncomputable def filteredLeftDerivedFunctor
    (G : A ⥤ B) [G.Additive] [EnoughProjectives A] :
    (CochainComplex.FilteredDerivedCategory.minus A).FullSubcategory ⥤
      (CochainComplex.FilteredDerivedCategory.minus B).FullSubcategory
```

**`CategoryTheory.FilteredDerived.filteredLeftDerivedFunctorComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/LeftDerivedFunctor.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/LeftDerivedFunctor.lean#L173). The attribute's comment: “filtered_left_derived_functor”.

> The natural isomorphism making the projective-resolution diagram commute.

```lean
noncomputable def filteredLeftDerivedFunctorComparison
    (G : A ⥤ B) [G.Additive] [EnoughProjectives A] :
    filteredProjectiveMinusToDerivedMinus A ⋙ filteredLeftDerivedFunctor G ≅
      filteredProjectiveMinusMapToDerivedMinus G
```

**`CategoryTheory.FilteredDerived.filteredInjectivePlusMapToDerivedPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/RightDerivedFunctor.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/RightDerivedFunctor.lean#L58). The attribute's comment: “filtered_right_derived_functor”.

> The lower route in the defining diagram of the filtered right derived functor: apply `T`
> termwise to a bounded-below complex of filtered injective objects, then pass to the
> bounded-below filtered derived category.

```lean
noncomputable def filteredInjectivePlusMapToDerivedPlus (T : A ⥤ B) [T.Additive] :
    (CochainComplex.FilteredDerivedCategory.filteredInjectivePlus A).FullSubcategory ⥤
      (CochainComplex.FilteredDerivedCategory.plus B).FullSubcategory
```

**`CategoryTheory.FilteredDerived.filteredRightDerivedFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/RightDerivedFunctor.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/RightDerivedFunctor.lean#L80). The attribute's comment: “filtered_right_derived_functor”.

> The filtered right derived functor `RT : DF⁺(A) ⥤ DF⁺(B)` of an additive functor
> `T : A ⥤ B`, defined when `A` has enough injectives.

```lean
noncomputable def filteredRightDerivedFunctor (T : A ⥤ B) [T.Additive] [EnoughInjectives A] :
    (CochainComplex.FilteredDerivedCategory.plus A).FullSubcategory ⥤
      (CochainComplex.FilteredDerivedCategory.plus B).FullSubcategory
```

**`CategoryTheory.FilteredDerived.filteredRightDerivedFunctorComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/RightDerivedFunctor.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/RightDerivedFunctor.lean#L89). The attribute's comment: “filtered_right_derived_functor”.

> The natural isomorphism making the injective-resolution diagram for the filtered right
> derived functor commute.

```lean
noncomputable def filteredRightDerivedFunctorComparison (T : A ⥤ B) [T.Additive]
    [EnoughInjectives A] :
    CochainComplex.FilteredDerivedCategory.toPlus A ⋙ filteredRightDerivedFunctor T ≅
      filteredInjectivePlusMapToDerivedPlus T
```

## Tag 03TE, a proposition

[Tag 03TE](https://stacks.math.columbia.edu/tag/03TE) in the Stacks Project.

**`CategoryTheory.FilteredDerived.filteredRightDerivedFunctorGrPIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/GradedRightDerivedFunctor.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/GradedRightDerivedFunctor.lean#L271).

> Taking the `p`-th graded piece commutes with the filtered right derived functor: for an
> additive functor `T : A ⥤ B` out of an abelian category with enough injectives, there is a
> natural isomorphism `RT ⋙ gr^p ≅ gr^p ⋙ RT` of functors `DF⁺(A) ⥤ D⁺(B)`.
>
> See [Stacks Project, Tag 03TE](https://stacks.math.columbia.edu/tag/03TE).

```lean
noncomputable def filteredRightDerivedFunctorGrPIso (T : A ⥤ B) [T.Additive]
    [EnoughInjectives A] (p : ℤ) :
    filteredRightDerivedFunctor T ⋙
        CochainComplex.FilteredDerivedCategory.liftDFPlus (FiniteFilteredObject.grP p)
          (CochainComplex.FilteredDerivedCategory.grP_inverts p) ≅
      CochainComplex.FilteredDerivedCategory.liftDFPlus (FiniteFilteredObject.grP p)
          (CochainComplex.FilteredDerivedCategory.grP_inverts p) ⋙
        T.rightDerivedFunctorPlus
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.8, Tag 03TC](https://stacks.math.columbia.edu/tag/03TC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
