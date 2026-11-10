---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_of_flatCover, AlgebraicGeometry.Stack.isAlgebraicStack_of_flatPresentation
statement: formalized
proof: formalized
---

# 97.16 Bootstrapping algebraic stacks

Section 97.16 of the Stacks Project, [Tag 06DB](https://stacks.math.columbia.edu/tag/06DB). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06DC, a theorem

[Tag 06DC](https://stacks.math.columbia.edu/tag/06DC) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_flatCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatCoverAlgebraic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatCoverAlgebraic.lean#L84). The attribute's comment: “stated for categories fibred in groupoids with the target a stack: the source's requirement that `𝒳` and `𝒴` be stacks in groupoids is implied, for `𝒳` by clause (1) and for `𝒴` by Stacks 02ZJ”.

> **Artin's theorem on representability of flat groupoids.** Let `F : 𝒳 ⟶ 𝒴` be a 1-morphism
> of categories fibred in groupoids over the big fppf site of `S`, with `𝒴` a stack. If `𝒳` is
> representable by an algebraic space and `F` is representable by algebraic spaces, surjective,
> flat and locally of finite presentation, then `𝒴` is an algebraic stack.
>
> The source asks `𝒳` and `𝒴` to be stacks in groupoids. `𝒳` is one because it is representable
> by an algebraic space (`AlgebraicGeometry.Stack.isStack_of_isRepresentableByAlgebraicSpace`), and
> `𝒴` is a stack in groupoids at every descent universe because it is a stack (Stacks 02ZJ).

```lean
theorem isAlgebraicStack_of_flatCover
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (F : 𝒳 ⟶ 𝒴)
    (hstack : 𝒴.val.p.IsStack (BigFppfOver.topology B S hS))
    (h𝒳 : IsRepresentableByAlgebraicSpace B S hS 𝒳)
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hFprops : ∀ (V : BigFppfOver B S hS)
      (y : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒴.val.obj)
      (_hy : y ⋙ 𝒴.val.p = Over.map V.hom)
      (G : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
      (hG : IsAlgebraicSpace B V.left.1 V.left.2 G),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map V.hom) 𝒳.val.p 𝒴.val.p y
          (CatFiberedInGroupoids.homFunctor F))
        (presheafOfCategories (G ⋙ typeToCat)).p) →
      (let g := (algebraicSpaceMap B S hS V
        ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨G, hG⟩)).hom
       Space.IsSurjective B S hS g ∧ Space.IsFlat B S hS g ∧
         Space.IsLocallyOfFinitePresentation B S hS g)) :
    IsAlgebraicStack.{u, w} B S hS 𝒴.val
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_flatPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GroupoidPresentationBootstrap.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GroupoidPresentationBootstrap.lean#L129). The attribute's comment: “the bootstrap assembly. Stacks 05XW (representability of the diagonal of the target) and the Hilbert-stack cover of Stacks 06CI, 06CL, 06D9 and 06DA (an algebraic stack with a representable surjective smooth 1-morphism to the target) are carried as the hypotheses `hdiagonal` and `hcover`; neither is in the library. Clause (1) and the flatness and local finite presentation of clause (2) are stated but not used, the carried inputs being exactly what the source draws from them”.

> **Stacks 06DC, Artin's theorem on representability of flat groupoids.** Let `F : 𝒳 ⟶ 𝒴` be a
> 1-morphism of stacks in groupoids over the big fppf site of `S`. If `𝒳` is representable by an
> algebraic space and `F` is representable by algebraic spaces, surjective, flat and locally of
> finite presentation, then `𝒴` is an algebraic stack.
>
> Two inputs of the source's proof are not in the library and are carried as hypotheses:
> representability of the diagonal of `𝒴`, which the source gets from Stacks 05XW, and the
> existence of a smooth surjective cover of `𝒴` by an algebraic stack, which the source gets from
> the locally-complete-intersection locus of the relative Hilbert stack of `F`.

```lean
theorem isAlgebraicStack_of_flatPresentation
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (F : 𝒳 ⟶ 𝒴)
    (hstack : 𝒴.val.p.IsStack (BigFppfOver.topology B S hS))
    (_h𝒳 : IsRepresentableByAlgebraicSpace B S hS 𝒳)
    (_hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (_hFprops : ∀ (V : BigFppfOver B S hS)
      (y : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒴.val.obj)
      (_hy : y ⋙ 𝒴.val.p = Over.map V.hom)
      (G : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
      (hG : IsAlgebraicSpace B V.left.1 V.left.2 G),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map V.hom) 𝒳.val.p 𝒴.val.p y
          (CatFiberedInGroupoids.homFunctor F))
        (presheafOfCategories (G ⋙ typeToCat)).p) →
      (let g := (algebraicSpaceMap B S hS V
        ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨G, hG⟩)).hom
       Space.IsSurjective B S hS g ∧ Space.IsFlat B S hS g ∧
         Space.IsLocallyOfFinitePresentation B S hS g))
    (hdiagonal : IsRepresentableByAlgebraicSpaces B S hS (diagonalBasedFunctor B S hS 𝒴))
    (hcover : ∃ (𝒲 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
      (q : 𝒲 ⟶ 𝒴) (hq : IsRepresentableByAlgebraicSpaces B S hS q.hom),
      IsAlgebraicStack.{u, w} B S hS 𝒲.val ∧
        HasRelativeProperty.{u, u, u + 1, u} B S hS
          (Space.surjectiveMorphismProperty B S hS ⊓ Space.smoothMorphismProperty B S hS)
          q hq) :
    IsAlgebraicStack.{u, w} B S hS 𝒴.val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.16, Tag 06DB](https://stacks.math.columbia.edu/tag/06DB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
