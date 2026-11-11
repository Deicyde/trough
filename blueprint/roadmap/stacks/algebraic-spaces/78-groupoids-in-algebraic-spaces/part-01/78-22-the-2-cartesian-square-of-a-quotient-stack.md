---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isomPresheaf_equiv_arrowFiber, AlgebraicGeometry.Stack.isomPresheaf_iso_pullback, AlgebraicGeometry.Stack.isomPresheafPullbackIso_inv_app, AlgebraicGeometry.Stack.isomPresheafPullbackIso_hom_app, AlgebraicGeometry.Stack.quotientStack_twoFibreProduct, AlgebraicGeometry.Stack.isomPresheaf_locallyAlgebraicSpace
statement: formalized
proof: formalized
---

# 78.22 The 2-cartesian square of a quotient stack

Section 78.22 of the Stacks Project, [Tag 04M8](https://stacks.math.columbia.edu/tag/04M8). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 044V, a lemma

[Tag 044V](https://stacks.math.columbia.edu/tag/044V) in the Stacks Project.

**`AlgebraicGeometry.Stack.isomPresheaf_equiv_arrowFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean#L547).

> The canonical map from pointwise groupoid arrows to isomorphisms between
> their images in the quotient stack is an isomorphism of presheaves on the
> fppf slice site. The pointwise-groupoid morphism presheaf is the fibre of
> the arrow space over the chosen pair of object-space points.

```lean
theorem isomPresheaf_equiv_arrowFiber
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (T : BigFppfOver C S hS)
    (x y : (quotientPrestack G).p.Fiber T) :
    IsIso ((isFibredOneMorphism_toQuotientStack G).morPresheafMap x y)
```

**`AlgebraicGeometry.Stack.isomPresheaf_iso_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean, line 885](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean#L885). The attribute's comment: “pullback description of the isomorphism sheaf”.

> The isomorphism sheaf of two presented objects is canonically the slice
> pullback of the arrow space along their two points. The identification sends
> pointwise prestack arrows to their images under `pointwiseToQuotientStack`.

```lean
theorem isomPresheaf_iso_pullback
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (T : BigFppfOver C S hS)
    (x' y' : G.objects.obj.obj (Opposite.op T))
    (x y : (quotientStack G).p.Fiber T)
    (hx : x.1 = (pointwiseToQuotientStack G).obj ⟨T, x'⟩)
    (hy : y.1 = (pointwiseToQuotientStack G).obj ⟨T, y'⟩) :
    ∃ e : (arrowFiberOver G T x' y' ⋙ uliftFunctor.{u + 1, u}) ≅
        (quotientStack G).p.isomPresheaf x y,
      IsCanonicalArrowFiberIso G T x' y' x y hx hy e
```

**`AlgebraicGeometry.Stack.isomPresheafPullbackIso_inv_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean, line 931](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean#L931). The attribute's comment: “canonical inverse comparison on prestack arrows”.

> The inverse comparison recovers the arrow-space section of each pointwise
> prestack arrow from its canonical image in the quotient stack.

```lean
theorem isomPresheafPullbackIso_inv_app (V : Over T)
    (r : (show G.toGroupoidInFunctors.Evaluation (op V.left) from
        G.objects.obj.map V.hom.op x') ⟶ G.objects.obj.map V.hom.op y') :
    arrowFiberOverSectionArrow G T x' y' V
      ((isomPresheafPullbackIso G T x' y' x y hx hy).inv.app (op V)
        (pointwiseArrowSection G T x' y' x y hx hy V r)).down =
      (G.toGroupoidInFunctors.evaluationArrowEquiv (op V.left) _ _ r).1
```

**`AlgebraicGeometry.Stack.isomPresheafPullbackIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean, line 944](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheaf.lean#L944). The attribute's comment: “canonical forward comparison on prestack arrows”.

> The forward comparison sends an arrow-space section to the isomorphism
> induced by that very prestack arrow. This rules out translating the identification
> by a nonidentity automorphism.

```lean
theorem isomPresheafPullbackIso_hom_app (V : Over T)
    (r : (show G.toGroupoidInFunctors.Evaluation (op V.left) from
        G.objects.obj.map V.hom.op x') ⟶ G.objects.obj.map V.hom.op y')
    (s : (arrowFiberOver G T x' y').obj (op V))
    (hs : arrowFiberOverSectionArrow G T x' y' V s =
      (G.toGroupoidInFunctors.evaluationArrowEquiv (op V.left) _ _ r).1) :
    (isomPresheafPullbackIso G T x' y' x y hx hy).hom.app (op V) (ULift.up s) =
      pointwiseArrowSection G T x' y' x y hx hy V r
```

## Tag 04M9, a lemma

[Tag 04M9](https://stacks.math.columbia.edu/tag/04M9) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStack_twoFibreProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoFibreProduct.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/TwoFibreProduct.lean#L1033).

> The canonical square of the quotient stack is a two-fibre product of
> stacks in groupoids over the big fppf site.

```lean
noncomputable def quotientStack_twoFibreProduct
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Bicategory.IsTwoFibreProduct (quotientStackSquare G)
```

## Tag 044W, a lemma

[Tag 044W](https://stacks.math.columbia.edu/tag/044W) in the Stacks Project.

**`AlgebraicGeometry.Stack.isomPresheaf_locallyAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheafAlgebraic.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackSquares/IsomorphismSheafAlgebraic.lean#L439).

> The isomorphism sheaf of two quotient-stack objects is locally
> representable by an algebraic space in the fppf topology.

```lean
theorem isomPresheaf_locallyAlgebraicSpace
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (T : BigFppfOver C S hS)
    (x y : (quotientStack G).p.Fiber T) :
    ∃ R ∈ BigFppfOver.topology C S hS T,
      ∀ ⦃V : BigFppfOver C S hS⦄ ⦃f : V ⟶ T⦄,
        R.arrows f →
          ∃ F : (BigFppfOver C V.left.1 V.left.2)ᵒᵖ ⥤ Type u,
            IsAlgebraicSpace C V.left.1 V.left.2 F ∧
              Nonempty (F ⋙ uliftFunctor.{u + 1, u} ≅
                (Over.iteratedSliceBackward V).op ⋙ (Over.map f).op ⋙
                  (quotientStack G).p.isomPresheaf x y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.22, Tag 04M8](https://stacks.math.columbia.edu/tag/04M8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
