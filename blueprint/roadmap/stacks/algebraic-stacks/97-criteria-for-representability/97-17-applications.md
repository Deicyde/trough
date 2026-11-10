---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.QuotientAtlas.isFlat_relativeProperty, AlgebraicGeometry.Stack.QuotientAtlas.isLocallyOfFinitePresentation_relativeProperty, AlgebraicGeometry.Stack.QuotientAtlas.isSurjective_relativeProperty, AlgebraicGeometry.Stack.QuotientAtlas.isFlat, AlgebraicGeometry.Stack.QuotientAtlas.isLocallyOfFinitePresentation, AlgebraicGeometry.Stack.QuotientAtlas.isSurjective, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack, AlgebraicGeometry.Stack.forall_isAlgebraicStack_quotientStack
statement: formalized
proof: formalized
---

# 97.17 Applications

Section 97.17 of the Stacks Project, [Tag 06FG](https://stacks.math.columbia.edu/tag/06FG). 2 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06FH, a lemma

[Tag 06FH](https://stacks.math.columbia.edu/tag/06FH) in the Stacks Project.

**`AlgebraicGeometry.Stack.QuotientAtlas.isFlat_relativeProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasArrowSquare.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasArrowSquare.lean#L225). The attribute's comment: “flatness”.

> **The quotient-stack projection is flat.** Let `G = (U, R, s, t, c)` be a groupoid in algebraic
> spaces over a scheme `S` of a big fppf site and assume its source and target maps `s`, `t` are flat
> and locally of finite presentation. Then the canonical projection `π : S_U ⟶ [U/R]` of Stacks 044R
> is flat in the sense of Stacks 03YK: every algebraic space representing a base change of `π` along
> a scheme-valued point of `[U/R]` has flat structural morphism.

```lean
theorem isFlat_relativeProperty (G : GroupoidInAlgebraicSpaces C S hS B)
    (hsflat : Space.IsFlat C S hS G.source.hom)
    (_htflat : Space.IsFlat C S hS G.target.hom)
    (_hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (_htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom) :
    RelativeProperty.{u, u + 1, u + 1} C S hS
      (fun ⦃X Y : AlgebraicSpaces C S hS⦄ (f : X ⟶ Y) => Space.IsFlat C S hS f.hom)
      (quotientStackProjectionHom G)
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isLocallyOfFinitePresentation_relativeProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasArrowSquare.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasArrowSquare.lean#L242). The attribute's comment: “locally of finite presentation”.

> **The quotient-stack projection is locally of finite presentation.** Let `G = (U, R, s, t, c)`
> be a groupoid in algebraic spaces over a scheme `S` of a big fppf site and assume its source and
> target maps `s`, `t` are flat and locally of finite presentation. Then the canonical projection
> `π : S_U ⟶ [U/R]` of Stacks 044R is locally of finite presentation in the sense of Stacks 03YK:
> every algebraic space representing a base change of `π` along a scheme-valued point of `[U/R]` has
> structural morphism locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentation_relativeProperty (G : GroupoidInAlgebraicSpaces C S hS B)
    (_hsflat : Space.IsFlat C S hS G.source.hom)
    (_htflat : Space.IsFlat C S hS G.target.hom)
    (hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (_htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom) :
    RelativeProperty.{u, u + 1, u + 1} C S hS
      (fun ⦃X Y : AlgebraicSpaces C S hS⦄ (f : X ⟶ Y) =>
        Space.IsLocallyOfFinitePresentation C S hS f.hom)
      (quotientStackProjectionHom G)
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isSurjective_relativeProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasArrowSquare.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasArrowSquare.lean#L259). The attribute's comment: “surjectivity”.

> **The quotient-stack projection is surjective.** Let `G = (U, R, s, t, c)` be a groupoid in
> algebraic spaces over a scheme `S` of a big fppf site and assume its source and target maps `s`,
> `t` are flat and locally of finite presentation. Then the canonical projection `π : S_U ⟶ [U/R]` of
> Stacks 044R is surjective in the sense of Stacks 03YK: every algebraic space representing a base
> change of `π` along a scheme-valued point of `[U/R]` has surjective structural morphism.

```lean
theorem isSurjective_relativeProperty (G : GroupoidInAlgebraicSpaces C S hS B)
    (_hsflat : Space.IsFlat C S hS G.source.hom)
    (_htflat : Space.IsFlat C S hS G.target.hom)
    (_hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (_htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom) :
    RelativeProperty.{u, u + 1, u + 1} C S hS
      (Space.surjectiveMorphismProperty C S hS)
      (quotientStackProjectionHom G)
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasFlat.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasFlat.lean#L263). The attribute's comment: “flatness; Stacks 04M9 and the representability of the projection carried as the hypothesis `Presentation`, and only the source map constrained”.

> **Stacks 06FH, flatness.** Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over
> `S` presented as in Stacks 04M9. If the source map `s` is flat, then the canonical projection
> `π : S_U ⟶ [U/R]` of Stacks 044R is flat in the relative sense of Stacks 03YK.

```lean
theorem isFlat {G : GroupoidInAlgebraicSpaces C S hS B} (A : Presentation G)
    (hs : Space.IsFlat C S hS G.source.hom) :
    HasRelativeProperty.{u, u + 1, u + 1, max u t} C S hS
      (fun ⦃X Y : AlgebraicSpaces C S hS⦄ (f : X ⟶ Y) => Space.IsFlat C S hS f.hom)
      (quotientStackProjectionHom G) A.representable
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasFlat.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasFlat.lean#L276). The attribute's comment: “locally of finite presentation; Stacks 04M9 and the representability of the projection carried as the hypothesis `Presentation`, and only the source map constrained”.

> **Stacks 06FH, local finite presentation.** Let `G = (U, R, s, t, c)` be a groupoid in
> algebraic spaces over `S` presented as in Stacks 04M9. If the source map `s` is locally of finite
> presentation, then the canonical projection `π : S_U ⟶ [U/R]` of Stacks 044R is locally of finite
> presentation in the relative sense of Stacks 03YK.

```lean
theorem isLocallyOfFinitePresentation {G : GroupoidInAlgebraicSpaces C S hS B}
    (A : Presentation G) (hs : Space.IsLocallyOfFinitePresentation C S hS G.source.hom) :
    HasRelativeProperty.{u, u + 1, u + 1, max u t} C S hS
      (fun ⦃X Y : AlgebraicSpaces C S hS⦄ (f : X ⟶ Y) =>
        Space.IsLocallyOfFinitePresentation C S hS f.hom)
      (quotientStackProjectionHom G) A.representable
```

**`AlgebraicGeometry.Stack.QuotientAtlas.isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasFlat.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientAtlasFlat.lean#L291). The attribute's comment: “surjectivity; Stacks 04M9 and the representability of the projection carried as the hypothesis `Presentation`, and no hypothesis on the groupoid”.

> **Stacks 06FH, surjectivity.** Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces
> over `S` presented as in Stacks 04M9. The canonical projection `π : S_U ⟶ [U/R]` of Stacks 044R
> is surjective in the relative sense of Stacks 03YK, with no hypothesis on the groupoid: the
> source map is surjective because the identity arrow at a point of the object space is a preimage
> of it.

```lean
theorem isSurjective {G : GroupoidInAlgebraicSpaces C S hS B} (A : Presentation G) :
    HasRelativeProperty.{u, u + 1, u + 1, max u t} C S hS
      (Space.surjectiveMorphismProperty C S hS)
      (quotientStackProjectionHom G) A.representable
```

## Tag 06FI, a theorem

[Tag 06FI](https://stacks.math.columbia.edu/tag/06FI) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraic.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraic.lean#L254). The attribute's comment: “Artin's theorem Stacks 06DC, Stacks 06FH and Stacks 04TB are carried as the hypotheses h06DC, h06FH and h04TB; what is discharged is the representability of the source and of the projection (Stacks 04SV and Stacks 04WZ) and the four stack clauses”.

> **Stacks 06FI.** Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over an algebraic
> space `A` over a scheme `S` of a big fppf site. If the source and the target of `G` are flat and
> locally of finite presentation, then the quotient stack `[U/R]` is an algebraic stack over `S`.
>
> Artin's theorem **Stacks 06DC** is carried as `h06DC`, **Stacks 06FH** as `h06FH`, and
> **Stacks 04TB** as `h04TB`.

```lean
theorem isAlgebraicStack_quotientStack {A : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS A)
    (h06DC : Theorem06DC.{u, w} C S hS) (h06FH : Lemma06FH C S hS)
    (h04TB : QuotientStackIsomSheavesAlgebraic C S hS G)
    (hsflat : Space.IsFlat C S hS G.source.hom)
    (htflat : Space.IsFlat C S hS G.target.hom)
    (hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G)
```

**`AlgebraicGeometry.Stack.forall_isAlgebraicStack_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraic.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraic.lean#L282). The attribute's comment: “quantified over the groupoids on a fixed base; Artin's theorem Stacks 06DC, Stacks 06FH and Stacks 04TB are carried as the hypotheses h06DC, h06FH and h04TB”.

> **Stacks 06FI, quantified over the groupoids on a fixed base.** Every groupoid in algebraic
> spaces over `A` whose source and target are flat and locally of finite presentation has an
> algebraic quotient stack.
>
> This is `AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack` with the three carried
> hypotheses pulled in front of the quantifier, which is the shape a consumer of Stacks 06FI — for
> instance Stacks 06PL for the trivial action — takes it in.

```lean
theorem forall_isAlgebraicStack_quotientStack (A : AlgebraicSpaces C S hS)
    (h06DC : Theorem06DC.{u, w} C S hS) (h06FH : Lemma06FH C S hS)
    (h04TB : Lemma04TB C S hS) :
    ∀ H : GroupoidInAlgebraicSpaces C S hS A,
      Space.IsFlat C S hS H.source.hom → Space.IsFlat C S hS H.target.hom →
        Space.IsLocallyOfFinitePresentation C S hS H.source.hom →
          Space.IsLocallyOfFinitePresentation C S hS H.target.hom →
            IsAlgebraicStack.{u, w} C S hS (quotientStack H)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatQuotientStackAlgebraic.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatQuotientStackAlgebraic.lean#L43). The attribute's comment: “stated for a groupoid in algebraic spaces over an algebraic space over S, which contains the source's groupoid over S”.

> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over an algebraic space `A` over
> a scheme `S` of a big fppf site. If the source and the target of `G` are flat and locally of finite
> presentation, then the quotient stack `[U/R]` is an algebraic stack over `S`.
>
> The source states it for a groupoid over `S`; a groupoid over `A` is the more general statement,
> `S` itself being an algebraic space over `S`.

```lean
theorem isAlgebraicStack_quotientStack_of_flat {A : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS A)
    (hsflat : Space.IsFlat C S hS G.source.hom)
    (htflat : Space.IsFlat C S hS G.target.hom)
    (hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.17, Tag 06FG](https://stacks.math.columbia.edu/tag/06FG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
