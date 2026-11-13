---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_of_flatCover
statement: formalized
proof: formalized
---

# 97.16 Bootstrapping algebraic stacks

Section 97.16 of the Stacks Project, [Tag 06DB](https://stacks.math.columbia.edu/tag/06DB). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06DC, a theorem

[Tag 06DC](https://stacks.math.columbia.edu/tag/06DC) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_flatCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatCoverAlgebraic.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatCoverAlgebraic.lean#L96). The attribute's comment: “a 1-morphism `F : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big fppf site of `S` with `𝒴` a stack; `𝒳` is a stack because it is representable by an algebraic space, and `𝒴` is a stack in groupoids by Stacks 02ZJ; clause (2) is read on every base change to an algebraic space; the diagonal of `𝒴` (Stacks 05XW) and the smooth surjective cover by the lci loci of the relative finite Hilbert stacks are proved, not assumed”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.16, Tag 06DB](https://stacks.math.columbia.edu/tag/06DB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
