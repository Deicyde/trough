---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.quotientStackSquare, AlgebraicGeometry.Stack.quotientStack_twoCartesian_source_target
statement: formalized
proof: formalized
---

# 79.1 Introduction

Section 79.1 of the Stacks Project, [Tag 04P5](https://stacks.math.columbia.edu/tag/04P5). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04P6, an equation

[Tag 04P6](https://stacks.math.columbia.edu/tag/04P6) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoFibreProduct.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoFibreProduct.lean#L144). The attribute's comment: “the displayed square of a groupoid over its quotient stack”.

> The canonical source-target square over the quotient stack.

```lean
noncomputable def quotientStackSquare
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    let J := BigFppfOver.topology C S hS
    let U : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨liftedFibredCategory G.objects,
        isStackInGroupoids_liftedFibredCategory G.objects⟩
    let Q : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨quotientStack G,
        isStackInGroupoids_quotientStack G⟩
    Bicategory.TwoCommSq
      (Bicategory.InducedBicategory.mkHom
        (liftedQuotientStackProjection G) : U ⟶ Q)
      (Bicategory.InducedBicategory.mkHom
        (liftedQuotientStackProjection G) : U ⟶ Q)
```

**`AlgebraicGeometry.Stack.quotientStack_twoCartesian_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoFibreProduct.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoFibreProduct.lean#L1080). The attribute's comment: “the 2-cartesian square R ⇉ U → [U/R]: legs s, t, π twice, 2-arrow of 044S”.

> **The 2-cartesian square `R ⇉ U → [U/R]`.** Take the square whose apex is the arrow space
> `R`, whose two legs `R ⟶ U` are the source `s` and the target `t`, whose two maps `U ⟶ [U/R]` are
> both the projection `π`, and whose filler is the canonical 2-arrow `π ∘ s ⟶ π ∘ t` of
> Stacks 044S. That 2-arrow is invertible, so the square 2-commutes through it, and the square is
> 2-cartesian. Here `R` and `U` stand for the stacks in groupoids attached to the two spaces.

```lean
theorem quotientStack_twoCartesian_source_target
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    let J := BigFppfOver.topology C S hS
    let R : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨liftedFibredCategory G.arrows, isStackInGroupoids_liftedFibredCategory G.arrows⟩
    let U : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨liftedFibredCategory G.objects, isStackInGroupoids_liftedFibredCategory G.objects⟩
    let Q : StackInGroupoids (BigFppfOver C S hS) J :=
      ⟨quotientStack G, isStackInGroupoids_quotientStack G⟩
    let s : R ⟶ U := Bicategory.InducedBicategory.mkHom (liftedAssociatedMap G.source)
    let t : R ⟶ U := Bicategory.InducedBicategory.mkHom (liftedAssociatedMap G.target)
    let π : U ⟶ Q := Bicategory.InducedBicategory.mkHom (liftedQuotientStackProjection G)
    ∃ γ : s ≫ π ≅ t ≫ π,
      γ.hom = Bicategory.InducedBicategory.mkHom₂ (liftedQuotientStackTwoArrow G) ∧
      Nonempty (Bicategory.IsTwoFibreProduct
        ({ pt := R, fst := s, snd := t, iso := γ } : Bicategory.TwoCommSq π π))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.1, Tag 04P5](https://stacks.math.columbia.edu/tag/04P5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
