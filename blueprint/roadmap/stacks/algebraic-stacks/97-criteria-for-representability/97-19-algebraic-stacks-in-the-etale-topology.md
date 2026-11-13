---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale_of_smoothAtlas
statement: formalized
proof: formalized
---

# 97.19 Algebraic stacks in the étale topology

Section 97.19 of the Stacks Project, [Tag 076U](https://stacks.math.columbia.edu/tag/076U). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 076V, a lemma

[Tag 076V](https://stacks.math.columbia.edu/tag/076V) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_of_isStackInGroupoids_etale_of_smoothAtlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleStackCriterion.lean, line 456](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/EtaleStackCriterion.lean#L456). The attribute's comment: “the criterion, with hypotheses (2) and (3) in the topology-independent form of the corresponding clauses of Stacks 026O”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.19, Tag 076U](https://stacks.math.columbia.edu/tag/076U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
