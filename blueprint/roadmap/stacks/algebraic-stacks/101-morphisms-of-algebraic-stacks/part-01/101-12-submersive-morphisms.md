---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.representable_universallySubmersive_iff, AlgebraicGeometry.Stack.AlgebraicStacks.IsSubmersive, AlgebraicGeometry.Stack.AlgebraicStacks.IsUniversallySubmersive, AlgebraicGeometry.Stack.AlgebraicStacks.isUniversallySubmersive_baseChange_of_isTwoFibreProduct, AlgebraicGeometry.Stack.AlgebraicStacks.isSubmersive_comp, AlgebraicGeometry.Stack.AlgebraicStacks.isUniversallySubmersive_comp
statement: formalized
proof: formalized
---

# 101.12 Submersive morphisms

Section 101.12 of the Stacks Project, [Tag 06U5](https://stacks.math.columbia.edu/tag/06U5). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CHX, a lemma

[Tag 0CHX](https://stacks.math.columbia.edu/tag/0CHX) in the Stacks Project.

**`AlgebraicGeometry.Stack.representable_universallySubmersive_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallySubmersiveCriterion.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallySubmersiveCriterion.lean#L57).

> **Stacks 0CHX.** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` representable by
> algebraic spaces is universally submersive in the relative sense of Tag 04XB — every algebraic
> space representing a base change of `f` along a scheme-valued point of `𝒴` has universally
> submersive structural morphism — exactly when, for every algebraic stack `𝒵` over `𝒴`, the map
> `|𝒵 ×_𝒴 𝒳| → |𝒵|` of topological spaces is submersive.

```lean
theorem representable_universallySubmersive_iff
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom) :
    (∀ (U : BigFppfOver B S hS) (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.val.obj)
        (_hy : y ⋙ 𝒴.val.val.p = Over.map U.hom)
        (T : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hT : IsAlgebraicSpace B U.left.1 U.left.2 T),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.val.p 𝒴.val.val.p y
            (CatFiberedInGroupoids.homFunctor f.hom))
          (presheafOfCategories (T ⋙ typeToCat)).p) →
        Space.UniversallySubmersive B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨T, hT⟩)).hom) ↔
      AlgebraicStacks.IsUniversallySubmersive B S hS f
```

## Tag 06U6, a definition

[Tag 06U6](https://stacks.math.columbia.edu/tag/06U6) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsSubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubmersiveAlgebraicStack.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubmersiveAlgebraicStack.lean#L77). The attribute's comment: “part (1)”. References: SGA 1 IX (2.1), “submersive”.

> **Stacks 06U6, part (1).** A 1-morphism of algebraic stacks over `S` *is submersive* when the
> map `|𝒳| → |𝒴|` it induces on the topological spaces of points of Stacks 04XG and 04XL is a
> quotient map, which is submersiveness in the sense of Stacks 0406.

```lean
abbrev IsSubmersive {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.IsUniversallySubmersive`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SubmersiveAlgebraicStack.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SubmersiveAlgebraicStack.lean#L88). The attribute's comment: “part (2)”. References: SGA 1 IX (2.1), “univ. submersive”.

> **Stacks 06U6, part (2).** A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks over `S` *is
> universally submersive* when, for every 1-morphism `g : 𝒴' ⟶ 𝒴` of algebraic stacks over `S`, the
> base change `𝒴' ×_{g, 𝒴, f} 𝒳 ⟶ 𝒴'` of `f` by `g` is submersive in the sense of
> `AlgebraicGeometry.Stack.AlgebraicStacks.IsSubmersive`.

```lean
abbrev IsUniversallySubmersive {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) : Prop
```

## Tag 0CHY, a lemma

[Tag 0CHY](https://stacks.math.columbia.edu/tag/0CHY) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUniversallySubmersive_baseChange_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenSubmersiveBaseChange.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyOpenSubmersiveBaseChange.lean#L221).

> **Stacks 0CHY.** Universal submersiveness is stable under base change: let `f : 𝒳 ⟶ 𝒴` be a
> universally submersive 1-morphism of algebraic stacks over `S` and let `R` be a 2-fibre product
> square of the cospan `(g, f)` for some `g : 𝒴' ⟶ 𝒴`. Then the base change `R.fst : R.pt ⟶ 𝒴'` of
> `f` along `g` is universally submersive.
>
> The square is arbitrary, so this applies to any square a consumer has already exhibited as a
> 2-fibre product rather than only to the canonical one of Stacks 04T2.

```lean
theorem isUniversallySubmersive_baseChange_of_isTwoFibreProduct
    {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS} {f : 𝒳 ⟶ 𝒴} {g : 𝒴' ⟶ 𝒴}
    (R : Bicategory.TwoCommSq g f) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : IsUniversallySubmersive B S hS f) :
    IsUniversallySubmersive B S hS R.fst
```

## Tag 0CHZ, a lemma

[Tag 0CHZ](https://stacks.math.columbia.edu/tag/0CHZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isSubmersive_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveComposition.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveComposition.lean#L84). The attribute's comment: “composition_submersive”.

> **Stacks 0CHZ.** The composite of two submersive 1-morphisms of algebraic stacks over `S` is
> submersive.

```lean
theorem isSubmersive_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵) (hf : IsSubmersive B S hS f) (hg : IsSubmersive B S hS g) :
    IsSubmersive B S hS (f ≫ g)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isUniversallySubmersive_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveUniversalComposition.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/OpenSubmersiveUniversalComposition.lean#L132). The attribute's comment: “composition_universally_submersive”.

> **Stacks 0CHZ.** The composite of two universally submersive 1-morphisms of algebraic stacks
> over `S` is universally submersive.

```lean
theorem isUniversallySubmersive_comp {𝒳 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsUniversallySubmersive B S hS f) (hg : IsUniversallySubmersive B S hS g) :
    IsUniversallySubmersive B S hS (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.12, Tag 06U5](https://stacks.math.columbia.edu/tag/06U5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
