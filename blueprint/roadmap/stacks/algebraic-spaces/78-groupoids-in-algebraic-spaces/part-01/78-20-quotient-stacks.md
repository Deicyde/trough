---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.toGroupoidInFunctors, Deformation.evaluationFunctor, Deformation.evaluationFunctor_groupoid, AlgebraicGeometry.Space.quotientStackOfPointsAction, AlgebraicGeometry.Space.isStackInGroupoids_quotientStackOfPointsAction, AlgebraicGeometry.Stack.quotientStack, AlgebraicGeometry.Stack.quotientStackOfAction, AlgebraicGeometry.Stack.quotientStackProjection
statement: formalized
proof: formalized
---

# 78.20 Quotient stacks

Section 78.20 of the Stacks Project, [Tag 044O](https://stacks.math.columbia.edu/tag/044O). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 044P, an equation

[Tag 044P](https://stacks.math.columbia.edu/tag/044P) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.GroupoidInAlgebraicSpaces.toGroupoidInFunctors`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean#L89), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/PointwiseGroupoid.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/PointwiseGroupoid.lean#L40) (StacksFrontier): “the groupoid data on the fppf site”.
- [`Deformation.evaluationFunctor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Groupoid/Basic.lean#L712), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/PointwiseGroupoid.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/PointwiseGroupoid.lean#L42) (StacksFrontier): “the functor of pointwise groupoids”.
- [`Deformation.evaluationFunctor_groupoid`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Groupoid/Basic.lean#L743), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/PointwiseGroupoid.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/PointwiseGroupoid.lean#L43) (StacksFrontier): “each pointwise value is a groupoid”.

## Tag 044Q, a definition

[Tag 044Q](https://stacks.math.columbia.edu/tag/044Q) in the Stacks Project.

**`AlgebraicGeometry.Space.quotientStackOfPointsAction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean#L137). The attribute's comment: “part (2) for an action given on points”.

> **Stacks Project, Tag 044Q, part (2)** for an action given on points: the quotient stack
> `[X/G]` of a presheaf of groups acting on a presheaf, both represented by objects of the big
> fppf site over `S`, read over an algebraic space `B` over `S`.

```lean
noncomputable abbrev quotientStackOfPointsAction (B : AlgebraicSpaces 𝒞 S hS)
    (F : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ GrpCat.{u}) (P : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    [ModObj (F ⋙ forget GrpCat) P] {a b : BigFppfOver 𝒞 S hS}
    (r : (F ⋙ forget GrpCat).RepresentableBy a) (s : P.RepresentableBy b) :
    BasedCategory (BigFppfOver 𝒞 S hS)
```

**`AlgebraicGeometry.Space.isStackInGroupoids_quotientStackOfPointsAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/ActionInSite.lean#L150). The attribute's comment: “part (2) for an action given on points”.

> The quotient stack of an action given on points is a stack in groupoids over the big fppf
> site.

```lean
theorem isStackInGroupoids_quotientStackOfPointsAction (B : AlgebraicSpaces 𝒞 S hS)
    (F : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ GrpCat.{u}) (P : (BigFppfOver 𝒞 S hS)ᵒᵖ ⥤ Type u)
    [ModObj (F ⋙ forget GrpCat) P] {a b : BigFppfOver 𝒞 S hS}
    (r : (F ⋙ forget GrpCat).RepresentableBy a) (s : P.RepresentableBy b) :
    Functor.IsStackInGroupoids (quotientStackOfPointsAction 𝒞 S hS B F P r s).p
      (BigFppfOver.topology 𝒞 S hS)
```

**`AlgebraicGeometry.Stack.quotientStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStack.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStack.lean#L173). The attribute's comment: “part (1): quotient stack of a groupoid”.

> **Stacks 044Q, part (1).** The quotient stack `[U/R]` of a groupoid in algebraic spaces, as a
> category over the original big fppf site: the stackification of the pointwise groupoid
> fibration.

```lean
noncomputable def quotientStack
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    BasedCategory (BigFppfOver C S hS)
```

**`AlgebraicGeometry.Stack.quotientStackOfAction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackOfAction.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackOfAction.lean#L84). The attribute's comment: “part (2): quotient stack of an action”.

> **Stacks 044Q, part (2).** The quotient stack `[X/G]` of an action of a group algebraic
> space `G` over `B` on an algebraic space `X` over `B`, as a category over the big fppf site: the
> quotient stack of part (1) of the action groupoid `(X, G ×_B X, pr₁, a, m)` of Stacks 0444, that
> is, the stackification of the pointwise groupoid fibration of that groupoid.

```lean
noncomputable abbrev quotientStackOfAction
    (B : AlgebraicSpaces C S hS) (G X : Over B.obj) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace C S hS G.left) (hX : IsAlgebraicSpace C S hS X.left) :
    BasedCategory (BigFppfOver C S hS)
```

## Tag 044R, a lemma

[Tag 044R](https://stacks.math.columbia.edu/tag/044R) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean#L148). The attribute's comment: “the canonical projection”.

> The canonical arrow from the object space of a groupoid in algebraic spaces
> to its quotient stack, viewed as a functor over the big fppf site.

```lean
noncomputable def quotientStackProjection
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    BasedFunctor
      (fibredCategory C S hS G.objects.obj).val
      (quotientStack G)
```

**`AlgebraicGeometry.Stack.quotientStackProjection_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean#L163). The attribute's comment: “pointwise description of the projection”.

> The projection sends a point of the object space to its image under the
> canonical map from the pointwise groupoid to its stackification.

```lean
theorem quotientStackProjection_obj
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (x : (fibredCategory C S hS G.objects.obj).val.obj) :
    (quotientStackProjection G).obj x =
        (pointwiseToQuotientStack G).obj
        ⟨x.base, Discrete.as x.fiber⟩
```

**`AlgebraicGeometry.Stack.quotientStackProjection_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean#L174). The attribute's comment: “pointwise description on morphisms”.

> The projection sends every arrow of the object-space fibration to the
> corresponding identity-in-the-fibre arrow of the pointwise groupoid, followed by
> stackification.

```lean
theorem quotientStackProjection_map
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {x y : (fibredCategory C S hS G.objects.obj).val.obj}
    (f : x ⟶ y) :
    ∃ g : (⟨x.base, Discrete.as x.fiber⟩ :
        (presheafOfGroupoids
          (evaluationGroupoidFunctor G.toGroupoidInFunctors)).obj) ⟶
        ⟨y.base, Discrete.as y.fiber⟩,
      g.base = f.base ∧
      (G.toGroupoidInFunctors.evaluationArrowEquiv
        (Opposite.op x.base) _ _ g.fiber).1 =
          G.toGroupoidInFunctors.identity
            (Opposite.op x.base) (Discrete.as x.fiber) ∧
      (quotientStackProjection G).map f =
        eqToHom (quotientStackProjection_obj G x) ≫
          (pointwiseToQuotientStack G).map g ≫
            eqToHom (quotientStackProjection_obj G y).symm
```

**`AlgebraicGeometry.Stack.quotientStackToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean#L416). The attribute's comment: “the canonical map to the base”.

> The second canonical 1-morphism, the structure arrow `[U/R] ⟶ B` from the
> quotient stack to the base: the descent of the structure morphism `U ⟶ B` of the object space,
> which is invariant because the source and the target of the groupoid are morphisms over `B`.

```lean
noncomputable def quotientStackToBase (G : GroupoidInAlgebraicSpaces C S hS B) :
    quotientStack G ⥤ᵇ (fibredCategory C S hS B.obj).val
```

**`AlgebraicGeometry.Stack.quotientStackProjection_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackProjection.lean#L423). The attribute's comment: “composition with the base map”.

> The composition `U ⟶ [U/R] ⟶ B` is the 1-morphism associated to the
> structure morphism `U ⟶ B`.

```lean
theorem quotientStackProjection_comp_toBase (G : GroupoidInAlgebraicSpaces C S hS B) :
    BasedFunctor.comp (quotientStackProjection G) (quotientStackToBase G) =
      (associatedMap C S hS G.objectsToBase.hom).1.hom
```

## Tag 044S, a lemma

[Tag 044S](https://stacks.math.columbia.edu/tag/044S) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackTwoArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean#L665).

> **Stacks 044S.** The canonical 2-morphism between the source and target maps to a quotient
> stack, making the square of Stacks 044R 2-commutative. Its components are the images of the
> groupoid arrows.

```lean
noncomputable def quotientStackTwoArrow
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    BasedFunctor.comp (associatedMap C S hS G.source.hom).1.hom
        (quotientStackProjection G) ⟶
      BasedFunctor.comp (associatedMap C S hS G.target.hom).1.hom
        (quotientStackProjection G)
```

**`AlgebraicGeometry.Stack.quotientStackTwoArrow_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean, line 676](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean#L676). The attribute's comment: “pointwise description”.

> **Stacks 044S.** At a point of the arrow space, the canonical 2-morphism is the image of
> that groupoid arrow under the pointwise-groupoid map to the quotient stack.

```lean
theorem quotientStackTwoArrow_app
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (x : (fibredCategory C S hS G.arrows.obj).val.obj) :
    ∃ g : (⟨x.base, G.source.hom.app (Opposite.op x.base) (Discrete.as x.fiber)⟩ :
          (presheafOfGroupoids
            (evaluationGroupoidFunctor G.toGroupoidInFunctors)).obj) ⟶
        ⟨x.base, G.target.hom.app (Opposite.op x.base) (Discrete.as x.fiber)⟩,
      g.base = 𝟙 x.base ∧
      (G.toGroupoidInFunctors.evaluationArrowEquiv
        (Opposite.op x.base) _ _ g.fiber).1 = Discrete.as x.fiber ∧
      HEq ((quotientStackTwoArrow G).app x) ((pointwiseToQuotientStack G).map g)
```

## Tag 04M7, a remark

[Tag 04M7](https://stacks.math.columbia.edu/tag/04M7) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackTwoArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean#L665). The attribute's comment: “remark restating the 2-commutative square in the X-for-S_X notation”.

> **Stacks 044S.** The canonical 2-morphism between the source and target maps to a quotient
> stack, making the square of Stacks 044R 2-commutative. Its components are the images of the
> groupoid arrows.

```lean
noncomputable def quotientStackTwoArrow
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    BasedFunctor.comp (associatedMap C S hS G.source.hom).1.hom
        (quotientStackProjection G) ⟶
      BasedFunctor.comp (associatedMap C S hS G.target.hom).1.hom
        (quotientStackProjection G)
```

Declarations registered for the tag:

- [`quotientStackTwoArrow`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=quotientStackTwoArrow#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean, line 741](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ProjectionTwoArrow.lean#L741) (StacksFrontier): “the two-commutative square of Stacks 044S, in the abbreviated notation that writes U for the stack in sets associated to U”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.20, Tag 044O](https://stacks.math.columbia.edu/tag/044O)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
