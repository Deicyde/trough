---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.smoothGroupoidAlgebraicStack, AlgebraicGeometry.Stack.hasRepresentableDiagonal_quotientStack, AlgebraicGeometry.Stack.QuotientAtlas.isRelativelySmooth, AlgebraicGeometry.Stack.QuotientAtlas.isRelativelySurjective, AlgebraicGeometry.Stack.QuotientAtlas.isRelativelySmooth_isSurjective_of_bootstrap04S6, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_isSmooth, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_isSmooth_unconditional, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStackOfAction_of_isSmooth
statement: formalized
proof: formalized
---

# 94.17 The algebraic stack associated to a smooth groupoid

Section 94.17 of the Stacks Project, [Tag 04TJ](https://stacks.math.columbia.edu/tag/04TJ). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04TJ, the section

[Tag 04TJ](https://stacks.math.columbia.edu/tag/04TJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.smoothGroupoidAlgebraicStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidPresentation.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidPresentation.lean#L89). The attribute's comment: “the section's construction: the algebraic stack associated to a smooth groupoid in algebraic spaces, as one object bundling the quotient stack with its algebraicity. The quotient stack and its fibredness in groupoids are Stacks 044Q; algebraicity is Stacks 04TK”.

> **Stacks 04TJ.** The algebraic stack associated to a smooth groupoid in algebraic spaces
> `G = (U, R, s, t, c)` over an algebraic space over `S`: the quotient stack `[U/R]` of Stacks
> 044Q, fibred in groupoids over the big fppf site of `S`, together with the proof that it is an
> algebraic stack over `S`.
>
> The underlying category over the site is the quotient stack on the nose
> (`AlgebraicGeometry.Stack.smoothGroupoidAlgebraicStack_val`); the algebraicity component is
> Stacks 04TK.

```lean
noncomputable def smoothGroupoidAlgebraicStack
    {G : GroupoidInAlgebraicSpaces C S hS A}
    (hG : GroupoidInAlgebraicSpaces.IsSmooth C S hS G) :
    LargeAlgebraicStack.{u, w} C S hS
```

## Tag 04WZ, a lemma

[Tag 04WZ](https://stacks.math.columbia.edu/tag/04WZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRepresentableDiagonal_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackRepresentableDiagonal.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackRepresentableDiagonal.lean#L204).

> **Stacks 04WZ.** The diagonal of the quotient stack of a groupoid in algebraic spaces over a
> scheme of a big fppf site is representable by algebraic spaces.
>
> The diagonal criterion of **Stacks 045G** reduces this to algebraicity of every isomorphism sheaf
> of a fibre, which is **Stacks 04TB**; that result in turn rests on Stacks 04SK, whose last step is
> the bootstrap theorem.

```lean
theorem hasRepresentableDiagonal_quotientStack
    {C : BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S} {A : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS A) :
    HasRepresentableDiagonal C S hS
      (CatFiberedInGroupoids.mk (quotientStack G) (isFiberedInGroupoids_quotientStack G))
```

## Tag 04X0, a lemma

[Tag 04X0](https://stacks.math.columbia.edu/tag/04X0) in the Stacks Project.

**`AlgebraicGeometry.Stack.QuotientAtlas.isRelativelySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidQuotientAtlas.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidQuotientAtlas.lean#L97). The attribute's comment: “smoothness”.

> **Stacks 04X0, smoothness of the projection.** Let `G = (U, R, s, t, c)` be a smooth
> groupoid in algebraic spaces over `S`. Then the canonical projection `π : S_U ⟶ [U/R]` of
> Stacks 044R is smooth in the sense of Stacks 04XB: it is representable by algebraic spaces, and
> every algebraic space representing a base change of it along a scheme-valued point of `[U/R]` has
> smooth structural morphism.
>
> Only smoothness of the source map `s` is used. The 2-cartesian square of Stacks 04M9 is
> `AlgebraicGeometry.Stack.QuotientAtlas.presentation`, built from the representability of the
> projection, `AlgebraicGeometry.Stack.representable_quotientStackProjectionHom`.

```lean
theorem isRelativelySmooth {G : GroupoidInAlgebraicSpaces C S hS B}
    (hG : GroupoidInAlgebraicSpaces.IsSmooth C S hS G) :
    IsRelativelySmooth C S hS (quotientStackProjectionHom G)
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isRelativelySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidQuotientAtlas.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidQuotientAtlas.lean#L112). The attribute's comment: “surjectivity”.

> **Stacks 04X0, surjectivity of the projection.** Let `G = (U, R, s, t, c)` be a groupoid
> in algebraic spaces over `S`. Then the canonical projection `π : S_U ⟶ [U/R]` of
> Stacks 044R is surjective in the sense of Stacks 04XB: every algebraic space representing a base
> change of it along a scheme-valued point of `[U/R]` has surjective structural morphism.
>
> No smoothness is needed: the source map of a groupoid is surjective because the identity arrow at
> a point of the object space is a preimage of that point.

```lean
theorem isRelativelySurjective {G : GroupoidInAlgebraicSpaces C S hS B} :
    HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
      (Space.surjectiveMorphismProperty C S hS)
      (quotientStackProjectionHom G) (representable_quotientStackProjectionHom G)
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isRelativelySmooth_isSurjective_of_bootstrap04S6`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidQuotientAtlas.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothGroupoidQuotientAtlas.lean#L128).

> **Stacks 04X0.** Let `G = (U, R, s, t, c)` be a smooth groupoid in algebraic spaces over
> `S`. Then the canonical projection `π : S_U ⟶ [U/R]` of Stacks 044R is smooth and surjective in
> the sense of Stacks 04XB: it is representable by algebraic spaces, and every algebraic space
> representing a base change of it along a scheme-valued point of `[U/R]` has smooth and surjective
> structural morphism.
>
> Representability is `AlgebraicGeometry.Stack.representable_quotientStackProjectionHom` (Stacks
> 04WZ and 045G); everything else is built, the 2-cartesian square of Stacks 04M9 by
> `AlgebraicGeometry.Stack.QuotientAtlas.presentation`.

```lean
theorem isRelativelySmooth_isSurjective_of_bootstrap04S6 {G : GroupoidInAlgebraicSpaces C S hS B}
    (hG : GroupoidInAlgebraicSpaces.IsSmooth C S hS G) :
    IsRelativelySmooth C S hS (quotientStackProjectionHom G) ∧
      HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
        (Space.surjectiveMorphismProperty C S hS)
        (quotientStackProjectionHom G) (representable_quotientStackProjectionHom G)
```

## Tag 04TK, a theorem

[Tag 04TK](https://stacks.math.columbia.edu/tag/04TK) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/SmoothQuotientStackAlgebraic.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/SmoothQuotientStackAlgebraic.lean#L472).

> Let `S` be a scheme contained in a big fppf site, and let `G = (U, R, s, t, c)` be a smooth
> groupoid in algebraic spaces over an algebraic space `A` over `S`. Then the quotient stack `[U/R]`
> is an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_quotientStack_of_isSmooth
    {G : GroupoidInAlgebraicSpaces C S hS A}
    (hG : GroupoidInAlgebraicSpaces.IsSmooth C S hS G) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_isSmooth_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/SmoothQuotientStackModel.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/SmoothQuotientStackModel.lean#L132).

> **Stacks 04TK.** Let `S` be a scheme contained in a big fppf site and let
> `G = (U, R, s, t, c)` be a smooth groupoid in algebraic spaces over an algebraic space over `S`.
> Then the quotient stack `[U/R]` is an algebraic stack over `S`.
>
> This is `AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_isSmooth_of_bootstrap` with part
> (3) of Stacks 04S6 supplied by `AlgebraicGeometry.Stack.bootstrap04S6`.

```lean
theorem isAlgebraicStack_quotientStack_of_isSmooth_unconditional
    {G : GroupoidInAlgebraicSpaces C S hS B} (hG : GroupoidInAlgebraicSpaces.IsSmooth C S hS G) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStackOfAction_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothActionQuotientStackAlgebraic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SmoothActionQuotientStackAlgebraic.lean#L59). The attribute's comment: “the quotient stack of an action of a smooth group algebraic space”.

> **Stacks 04TK** for a group action: if the structure morphism `G ⟶ B` of a group object in
> the slice of presheaves over `B` is smooth, then the quotient stack `[X/G]` of Stacks 044Q,
> part (2), is an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_quotientStackOfAction_of_isSmooth
    (B : AlgebraicSpaces C S hS) (G X : Over B.obj) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace C S hS G.left) (hX : IsAlgebraicSpace C S hS X.left)
    (hsm : Space.IsSmooth C S hS G.hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStackOfAction B G X hG hX)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.17, Tag 04TJ](https://stacks.math.columbia.edu/tag/04TJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
