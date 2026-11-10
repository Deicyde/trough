---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.quotientStackTwoArrow_source_comp_eq, AlgebraicGeometry.Stack.quotientStackTwoArrow_middle_comp_eq, AlgebraicGeometry.Stack.quotientStackTwoArrow_target_comp_eq, AlgebraicGeometry.Stack.quotientStackTwoArrow_cocycle, AlgebraicGeometry.Stack.quotientStack_desc
statement: formalized
proof: formalized
---

# 78.23 The 2-coequalizer property of a quotient stack

Section 78.23 of the Stacks Project, [Tag 04MA](https://stacks.math.columbia.edu/tag/04MA). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 044T, a lemma

[Tag 044T](https://stacks.math.columbia.edu/tag/044T) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackTwoArrow_source_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean#L428). The attribute's comment: “source endpoint equality”.

> **Stacks 044T.** The composite arrow and the second arrow of a composable pair have the same
> source in the quotient stack.

```lean
theorem quotientStackTwoArrow_source_comp_eq
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    let a₁ := (associatedMap C S hS
      (pullback.snd G.source.hom G.target.hom)).1.hom
    let ac := (associatedMap C S hS G.comp.hom).1.hom
    let Fs := BasedFunctor.comp
      (associatedMap C S hS G.source.hom).1.hom
      (quotientStackProjection G)
  BasedFunctor.comp ac Fs = BasedFunctor.comp a₁ Fs
```

**`AlgebraicGeometry.Stack.quotientStackTwoArrow_middle_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean#L442). The attribute's comment: “middle endpoint equality”.

> **Stacks 044T.** The target of the second arrow is the source of the first arrow of a
> composable pair, as 1-morphisms to the quotient stack.

```lean
theorem quotientStackTwoArrow_middle_comp_eq
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    let a₀ := (associatedMap C S hS
      (pullback.fst G.source.hom G.target.hom)).1.hom
    let a₁ := (associatedMap C S hS
      (pullback.snd G.source.hom G.target.hom)).1.hom
    let Fs := BasedFunctor.comp
      (associatedMap C S hS G.source.hom).1.hom
      (quotientStackProjection G)
    let Ft := BasedFunctor.comp
      (associatedMap C S hS G.target.hom).1.hom
      (quotientStackProjection G)
  BasedFunctor.comp a₁ Ft = BasedFunctor.comp a₀ Fs
```

**`AlgebraicGeometry.Stack.quotientStackTwoArrow_target_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean#L460). The attribute's comment: “target endpoint equality”.

> **Stacks 044T.** The first arrow of a composable pair and the composite arrow have the same
> target in the quotient stack.

```lean
theorem quotientStackTwoArrow_target_comp_eq
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    let a₀ := (associatedMap C S hS
      (pullback.fst G.source.hom G.target.hom)).1.hom
    let ac := (associatedMap C S hS G.comp.hom).1.hom
    let Ft := BasedFunctor.comp
      (associatedMap C S hS G.target.hom).1.hom
      (quotientStackProjection G)
  BasedFunctor.comp a₀ Ft = BasedFunctor.comp ac Ft
```

**`AlgebraicGeometry.Stack.quotientStackTwoArrow_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoArrowCocycle.lean#L706). The attribute's comment: “vertical-composition identity”.

> **Stacks 044T.** The canonical 2-morphism of a quotient stack sends composition of groupoid
> arrows to vertical composition of 2-morphisms.

```lean
theorem quotientStackTwoArrow_cocycle
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    let a₀ := (associatedMap C S hS
      (pullback.fst G.source.hom G.target.hom)).1.hom
    let a₁ := (associatedMap C S hS
      (pullback.snd G.source.hom G.target.hom)).1.hom
    let ac := (associatedMap C S hS G.comp.hom).1.hom
    let α := quotientStackTwoArrow G
    BasedCategory.whiskerLeft ac α =
      eqToHom (quotientStackTwoArrow_source_comp_eq G) ≫
        BasedCategory.whiskerLeft a₁ α ≫
          eqToHom (quotientStackTwoArrow_middle_comp_eq G) ≫
            BasedCategory.whiskerLeft a₀ α ≫
              eqToHom (quotientStackTwoArrow_target_comp_eq G)
```

## Tag 044U, a lemma

[Tag 044U](https://stacks.math.columbia.edu/tag/044U) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStack_desc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/Descent.lean, line 917](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/Descent.lean#L917).

> **Stacks 044U.** The quotient stack is a 2-coequalizer of the 2-commutative square of
> Stacks 044S in the 2-category of stacks in groupoids over the big fppf site: given a stack in
> groupoids `X`, a 1-morphism `f : 𝒮_U ⟶ X` out of the object space of a groupoid in algebraic
> spaces and a 2-morphism `β : s ∘ f ⟶ t ∘ f` satisfying the composition cocycle on the arrows,
> there are a 1-morphism `g : [U/R] ⟶ X` out of the quotient stack and a 2-isomorphism
> `α : π ∘ g ≅ f` on the object space which carry the canonical 2-morphism of Stacks 044S to `β`.
>
> The comparison 2-isomorphism is kept as data rather than replaced by the bare existence of some
> 1-morphism, since the compatibility with the 2-morphism of Stacks 044S is a statement about
> it.

```lean
public theorem quotientStack_desc
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (X : BasedCategory (BigFppfOver C S hS))
    (hX : X.p.IsStackInGroupoids.{u + 1} (BigFppfOver.topology C S hS))
    (f : BasedFunctor (fibredCategory C S hS G.objects.obj).val X)
    (β : BasedFunctor.comp
      (associatedMap C S hS G.source.hom).1.hom f ⟶
      BasedFunctor.comp (associatedMap C S hS G.target.hom).1.hom f)
    (hβ : IsCocycle G X f β) :
    ∃ (g : BasedFunctor (quotientStack G) X)
      (α : BasedFunctor.comp (quotientStackProjection G) g ≅ f),
      BasedCategory.whiskerLeft
          (associatedMap C S hS G.source.hom).1.hom α.hom ≫ β =
        BasedCategory.whiskerRight (quotientStackTwoArrow G) g ≫
          BasedCategory.whiskerLeft
            (associatedMap C S hS G.target.hom).1.hom α.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.23, Tag 04MA](https://stacks.math.columbia.edu/tag/04MA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
