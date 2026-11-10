---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale_of_smoothAtlas, AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale
statement: formalized
proof: formalized
---

# 97.19 Algebraic stacks in the étale topology

Section 97.19 of the Stacks Project, [Tag 076U](https://stacks.math.columbia.edu/tag/076U). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 076V, a lemma

[Tag 076V](https://stacks.math.columbia.edu/tag/076V) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale_of_smoothAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleStackCriterion.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleStackCriterion.lean#L456). The attribute's comment: “the criterion, with hypotheses (2) and (3) in the topology-independent form of the corresponding clauses of Stacks 026O”.

> **Stacks 076V.** Let `S` be a scheme of a big fppf site and let `𝒳` be a category over the
> common underlying category of the big fppf and big étale sites of `S` such that
>
> 1. `𝒳` is a stack in groupoids for the étale topology,
> 2. the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is representable by algebraic spaces, and
> 3. there are a scheme `U` over `S` and a 1-morphism `(Sch/U) ⟶ 𝒳` which is representable by
>    algebraic spaces, surjective and smooth.
>
> Then `𝒳` is an algebraic stack over `S` in the sense of Stacks 026O.
>
> Conditions (2) and (3) are stated exactly as the corresponding clauses of
> `AlgebraicGeometry.Stack.IsAlgebraicStack`, which, as the source's proof notes, are independent of
> the topology; condition (1) is Stacks 02ZI for the étale topology localised at `S`, at the index
> universe of the families of the site. The fppf stack clause is
> `AlgebraicGeometry.Stack.isStack_of_isStack_etale_of_smoothAtlas`.

```lean
theorem isAlgebraicStack_of_isStackInGroupoids_etale_of_smoothAtlas
    (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (hstack : 𝒳.p.IsStackInGroupoids.{u + 1} ((etaleTopology B).over (B.obj hS)))
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS
      (diagonalBasedFunctor B S hS (CatFiberedInGroupoids.mk 𝒳 hstack.isFiberedInGroupoids)))
    (U : BigFppfOver B S hS)
    (f : (schemeFibredCategory B S hS U).val ⥤ᵇ 𝒳)
    (hfrep : IsRepresentableByAlgebraicSpaces B S hS f)
    (hfprop : ∀ (V : BigFppfOver B S hS)
        (y : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒳.obj)
        (_hy : y ⋙ 𝒳.p = Over.map V.hom)
        (F : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B V.left.1 V.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map V.hom)
            (schemeFibredCategory B S hS U).val.p 𝒳.p y f.toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        (let g := (algebraicSpaceMap B S hS V
          ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨F, hF⟩)).hom
         Space.IsSurjective B S hS g ∧ Space.IsSmooth B S hS g)) :
    IsAlgebraicStack.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidPresentation.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidPresentation.lean#L211). The attribute's comment: “the criterion, with hypotheses (2) and (3) in the topology-independent form of the corresponding clauses of Stacks 026O. Carried as explicit hypotheses are part (1) of Stacks 04T4 (`_eR`: the self-intersection of the atlas is representable by the arrow space of the carried groupoid), part (4) of Stacks 04T4 (`_hobjects`: its object space is the space the atlas represents) and part (6) of Stacks 04T4 together with part (2) of Stacks 04T5 read at the étale index (`e`: the quotient stack of the carried groupoid is equivalent over the site to `𝒳`); the carried groupoid is not assumed smooth, so none of the three contains algebraicity of `𝒳`. What is discharged is the fppf stack clause, by Stacks 044Q for the quotient stack of a groupoid in algebraic spaces, Stacks 042W to transport it along the equivalence and Stacks 02ZJ for the family-indexed conjunct, together with clause (1) of Stacks 026O out of the étale hypothesis”.

> **Stacks 076V.** Let `𝒳` be a category over the common underlying category of the big fppf
> and big étale sites of `S` such that
>
> 1. `𝒳` is a stack in groupoids for the étale topology,
> 2. the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is representable by algebraic spaces, and
> 3. there are a scheme `U` over `S` and a 1-morphism `(Sch/U) ⟶ 𝒳` which is representable by
>    algebraic spaces, surjective and smooth.
>
> Then `𝒳` is an algebraic stack over `S` in the sense of Stacks 026O.
>
> Conditions (2) and (3) are stated exactly as the corresponding clauses of
> `AlgebraicGeometry.Stack.IsAlgebraicStack`, which is legitimate because, as the source's proof
> notes, both are independent of the topology. Three hypotheses carry the chain Stacks 04T4 (1),
> (4), (6) and Stacks 04T5 (2) that the source's proof goes through; see the implementation notes
> for why none of them is the conclusion restated.

```lean
theorem isAlgebraicStack_of_isStackInGroupoids_etale
    (𝒳 : BasedCategory.{u, u + 1} (BigFppfOver B S hS))
    (hstack : 𝒳.p.IsStackInGroupoids.{w} ((etaleTopology B).over (B.obj hS)))
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS
      (diagonalBasedFunctor B S hS (CatFiberedInGroupoids.mk 𝒳 hstack.isFiberedInGroupoids)))
    (U : BigFppfOver B S hS)
    (f : (schemeFibredCategory B S hS U).val ⥤ᵇ 𝒳)
    (hfrep : IsRepresentableByAlgebraicSpaces B S hS f)
    (hfprop : ∀ (V : BigFppfOver B S hS)
        (y : BigFppfOver B V.left.1 V.left.2 ⥤ 𝒳.obj)
        (_hy : y ⋙ 𝒳.p = Over.map V.hom)
        (F : (BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B V.left.1 V.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map V.hom)
            (schemeFibredCategory B S hS U).val.p 𝒳.p y f.toFunctor)
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        (let g := (algebraicSpaceMap B S hS V
          ((spacesOverSmallerBaseFunctor B V.left.1 S V.left.2 hS V.hom).obj ⟨F, hF⟩)).hom
         Space.IsSurjective B S hS g ∧ Space.IsSmooth B S hS g))
    {A : AlgebraicSpaces B S hS} (G : GroupoidInAlgebraicSpaces B S hS A)
    (_eR : StacksRepresentableCFG.EquivalenceOver
      (SelfIntersection.relation B S hS (schemeFibredCategory B S hS U)
        (CatFiberedInGroupoids.mk 𝒳 hstack.isFiberedInGroupoids) f).val.p
      (presheafOfCategories (G.arrows.obj ⋙ typeToCat)).p)
    (_hobjects : G.objects = Space.representedAlgebraicSpace B S hS U)
    (e : BasedCategory.Equivalence (quotientStack G) 𝒳) :
    IsAlgebraicStack.{u, w} B S hS 𝒳
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.19, Tag 076U](https://stacks.math.columbia.edu/tag/076U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
