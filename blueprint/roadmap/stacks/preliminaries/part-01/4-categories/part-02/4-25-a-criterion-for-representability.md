---
declaration: section
origin: cited
lean: CategoryTheory.isCorepresentable_of_solutionSet, CategoryTheory.bijective_comp_freeGroup_of, CategoryTheory.closure_range_freeGroup_of, CategoryTheory.colimitHomEquiv, isRightAdjoint_of_preservesLimits_of_solutionSetCondition
statement: formalized
proof: formalized
---

# 4.25 A criterion for representability

Section 4.25 of the Stacks Project, [Tag 0AHM](https://stacks.math.columbia.edu/tag/0AHM). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AHN, a lemma

[Tag 0AHN](https://stacks.math.columbia.edu/tag/0AHN) in the Stacks Project.

**`CategoryTheory.isCorepresentable_of_solutionSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Representable/SolutionSet.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Representable/SolutionSet.lean#L273). References: SGA 4 I (8.12.8.1), “Sufficiency direction”.

> **Stacks 0AHN** (Brown representability criterion).
>
> Let `C` be a category with all (small) limits and `F : C ⥤ Type v` a functor that
> preserves limits. Suppose there is a family `{xᵢ}` of objects together with elements
> `fᵢ ∈ F xᵢ` such that for every `y : C` and every `g ∈ F y` there exists an `i` and
> a morphism `φ : xᵢ ⟶ y` with `F.map φ fᵢ = g`. Then `F` is corepresentable.

```lean
theorem isCorepresentable_of_solutionSet
    {C : Type u} [Category.{v} C] [HasLimitsOfSize.{v, v} C]
    (F : C ⥤ Type v) [PreservesLimitsOfSize.{v, v} F]
    {I : Type v} (x : I → C) (f : ∀ i, F.obj (x i))
    (hsurj : ∀ (y : C) (g : F.obj y), ∃ i, ∃ φ : x i ⟶ y, F.map φ (f i) = g) :
    F.IsCorepresentable
```

## Tag 0AHP, a remark

[Tag 0AHP](https://stacks.math.columbia.edu/tag/0AHP) in the Stacks Project.

**`CategoryTheory.bijective_comp_freeGroup_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Representable/Applications.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Representable/Applications.lean#L56). The attribute's comment: “the free group on a set”.

> **Stacks 0AHP**, the free group on a set.
> The free group on `E` represents the functor `G ↦ Map(E, G)` on groups: composing a group
> homomorphism `F_E → G` with the canonical map `FreeGroup.of : E → F_E` is a bijection from
> `Mor_{Groups}(F_E, G)` to `Map(E, G)`.

```lean
theorem bijective_comp_freeGroup_of (E : Type u) (G : Type v) [Group G] :
    Function.Bijective fun f : FreeGroup E →* G => (f : FreeGroup E → G) ∘ FreeGroup.of
```

**`CategoryTheory.closure_range_freeGroup_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Representable/Applications.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Representable/Applications.lean#L63). The attribute's comment: “the free group on a set”.

> **Stacks 0AHP**, the free group on a set: the map `E → F_E` corresponding to the identity of
> `F_E` generates `F_E`, so no relations have been imposed.

```lean
theorem closure_range_freeGroup_of (E : Type u) :
    Subgroup.closure (Set.range (FreeGroup.of : E → FreeGroup E)) = ⊤
```

**`CategoryTheory.colimitHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Representable/Applications.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Representable/Applications.lean#L74). The attribute's comment: “colimits of topological spaces”.

> **Stacks 0AHP**, colimits of topological spaces.
> For a diagram `X : 𝓘 ⥤ Top` of topological spaces, a morphism out of the colimit of `X` is the
> same thing as an element of `lim_𝓘 Mor_{Top}(X_i, Y)`, i.e. a family of morphisms
> `φ_i : X_i ⟶ Y` compatible with the transition maps of the diagram. So the colimit — which exists
> because `Top` has limits and the criterion of Stacks 0AHN applies — is precisely a space
> representing the functor `Y ↦ lim_𝓘 Mor_{Top}(X_i, Y)` of the source.

```lean
noncomputable def colimitHomEquiv {𝓘 : Type u} [SmallCategory 𝓘] (X : 𝓘 ⥤ TopCat.{u})
    (Y : TopCat.{u}) :
    (colimit X ⟶ Y) ≃ (X ⟶ (Functor.const 𝓘).obj Y)
```

## Tag 0AHQ, a theorem

[Tag 0AHQ](https://stacks.math.columbia.edu/tag/0AHQ) in the Stacks Project.

Declarations registered for the tag:

- [`isRightAdjoint_of_preservesLimits_of_solutionSetCondition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isRightAdjoint_of_preservesLimits_of_solutionSetCondition#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/AdjointFunctors.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/AdjointFunctors.lean#L62) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.25, Tag 0AHM](https://stacks.math.columbia.edu/tag/0AHM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
