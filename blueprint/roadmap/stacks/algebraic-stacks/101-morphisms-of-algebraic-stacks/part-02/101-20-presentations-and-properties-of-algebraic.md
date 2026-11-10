---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isSeparated_diagonal_of_isSeparated_sourceTarget, AlgebraicGeometry.Stack.isSeparated_diagonal_of_isSeparated_spaces, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_sourceTarget, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_source_target, AlgebraicGeometry.Stack.isSeparatedOver_of_isProper_sourceTarget, AlgebraicGeometry.Stack.isSeparatedOver_of_isProper_source_target, AlgebraicGeometry.Stack.equivalence_sourceTargetRel_points, AlgebraicGeometry.Stack.pointMap_eq_iff_sourceTargetRel
statement: formalized
proof: formalized
---

# 101.20 Presentations and properties of algebraic stacks

Section 101.20 of the Stacks Project, [Tag 0DTX](https://stacks.math.columbia.edu/tag/0DTX). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DTY, a lemma

[Tag 0DTY](https://stacks.math.columbia.edu/tag/0DTY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSeparated_diagonal_of_isSeparated_sourceTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean#L161). The attribute's comment: “part (1): a separated relation gives a separated diagonal, the diagonal being the one over the base scheme of the site”.

> **Stacks 0DTY, part (1).** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` with
> `s` and `t` flat and locally of finite presentation, and let `𝒳` be an algebraic stack equivalent
> over the site to its quotient stack `[U/R]`. If `(t, s) : R ⟶ U ×_S U` is separated, then the
> diagonal of `𝒳` is separated in the sense of Properties of Stacks, Section 04XB.

```lean
theorem isSeparated_diagonal_of_isSeparated_sourceTarget
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack G).p 𝒳.val.val.p))
    (_hsFlat : Space.IsFlat B S hS G.source.hom)
    (_htFlat : Space.IsFlat B S hS G.target.hom)
    (_hsLfp : Space.IsLocallyOfFinitePresentation B S hS G.source.hom)
    (_htLfp : Space.IsLocallyOfFinitePresentation B S hS G.target.hom)
    (hj : Space.IsSeparated B S hS (GroupoidInAlgebraicSpaces.sourceTarget G).hom) :
    Stack.IsSeparated B S hS (diagonal.{u, u, u + 1} B S hS 𝒳.val)
```

**`AlgebraicGeometry.Stack.isSeparated_diagonal_of_isSeparated_spaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean#L182). The attribute's comment: “part (2): separated object and arrow spaces give a separated diagonal, the diagonal being the one over the base scheme of the site”.

> **Stacks 0DTY, part (2).** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` with
> `s` and `t` flat and locally of finite presentation, and let `𝒳` be an algebraic stack equivalent
> over the site to its quotient stack `[U/R]`. If `U` and `R` are separated, then the diagonal of `𝒳`
> is separated in the sense of Properties of Stacks, Section 04XB.

```lean
theorem isSeparated_diagonal_of_isSeparated_spaces
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack G).p 𝒳.val.val.p))
    (_hsFlat : Space.IsFlat B S hS G.source.hom)
    (_htFlat : Space.IsFlat B S hS G.target.hom)
    (_hsLfp : Space.IsLocallyOfFinitePresentation B S hS G.source.hom)
    (_htLfp : Space.IsLocallyOfFinitePresentation B S hS G.target.hom)
    (_hU : Space.IsSeparated B S hS G.objectsToBase.hom)
    (hR : Space.IsSeparated B S hS G.arrowsToBase.hom) :
    Stack.IsSeparated B S hS (diagonal.{u, u, u + 1} B S hS 𝒳.val)
```

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_sourceTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean#L204). The attribute's comment: “part (3): a locally quasi-finite relation gives a quasi-DM quotient”.

> **Stacks 0DTY, part (3).** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` with
> `s` and `t` flat and locally of finite presentation, and let `𝒳` be an algebraic stack equivalent
> over the site to its quotient stack `[U/R]`. If `(t, s) : R ⟶ U ×_S U` is locally quasi-finite, then
> `𝒳` is quasi-DM.

```lean
theorem isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_sourceTarget
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack G).p 𝒳.val.val.p))
    (_hsFlat : Space.IsFlat B S hS G.source.hom)
    (_htFlat : Space.IsFlat B S hS G.target.hom)
    (_hsLfp : Space.IsLocallyOfFinitePresentation B S hS G.source.hom)
    (_htLfp : Space.IsLocallyOfFinitePresentation B S hS G.target.hom)
    (hj : Space.IsLocallyQuasiFinite B S hS
      (GroupoidInAlgebraicSpaces.sourceTarget G).hom) :
    AlgebraicStacks.IsAbsolutelyQuasiDM.{u, w} B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean#L228). The attribute's comment: “part (4): a locally quasi-finite source and target give a quasi-DM quotient”.

> **Stacks 0DTY, part (4).** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` with
> `s` and `t` flat and locally of finite presentation, and let `𝒳` be an algebraic stack equivalent
> over the site to its quotient stack `[U/R]`. If `s` and `t` are locally quasi-finite, then `𝒳` is
> quasi-DM.

```lean
theorem isAbsolutelyQuasiDM_of_isLocallyQuasiFinite_source_target
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack G).p 𝒳.val.val.p))
    (_hsFlat : Space.IsFlat B S hS G.source.hom)
    (_htFlat : Space.IsFlat B S hS G.target.hom)
    (_hsLfp : Space.IsLocallyOfFinitePresentation B S hS G.source.hom)
    (_htLfp : Space.IsLocallyOfFinitePresentation B S hS G.target.hom)
    (hs : Space.IsLocallyQuasiFinite B S hS G.source.hom)
    (_ht : Space.IsLocallyQuasiFinite B S hS G.target.hom) :
    AlgebraicStacks.IsAbsolutelyQuasiDM.{u, w} B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.isSeparatedOver_of_isProper_sourceTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean#L253). The attribute's comment: “part (5): a proper relation gives a quotient separated over the base scheme `S` (Stacks 050D part (3)), the source's `separated` for an algebraic stack over `S`”.

> **Stacks 0DTY, part (5).** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` with
> `s` and `t` flat and locally of finite presentation, and let `𝒳` be an algebraic stack equivalent
> over the site to its quotient stack `[U/R]`. If `(t, s) : R ⟶ U ×_S U` is proper, then `𝒳` is
> separated over the base scheme of the site (Stacks 050D, part (3)).

```lean
theorem isSeparatedOver_of_isProper_sourceTarget
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack G).p 𝒳.val.val.p))
    (_hsFlat : Space.IsFlat B S hS G.source.hom)
    (_htFlat : Space.IsFlat B S hS G.target.hom)
    (_hsLfp : Space.IsLocallyOfFinitePresentation B S hS G.source.hom)
    (_htLfp : Space.IsLocallyOfFinitePresentation B S hS G.target.hom)
    (hj : Space.IsProper B S hS (GroupoidInAlgebraicSpaces.sourceTarget G).hom) :
    IsSeparatedOver.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isSeparatedOver_of_isProper_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackSeparation.lean#L278). The attribute's comment: “part (6): a proper source and target over a separated object space give a quotient separated over the base scheme `S` (Stacks 050D part (3)), the source's `separated` for an algebraic stack over `S`”.

> **Stacks 0DTY, part (6).** Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `S` with
> `s` and `t` flat and locally of finite presentation, and let `𝒳` be an algebraic stack equivalent
> over the site to its quotient stack `[U/R]`. If `s` and `t` are proper and `U` is separated, then
> `𝒳` is separated over the base scheme of the site (Stacks 050D, part (3)).

```lean
theorem isSeparatedOver_of_isProper_source_target
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack G).p 𝒳.val.val.p))
    (_hsFlat : Space.IsFlat B S hS G.source.hom)
    (_htFlat : Space.IsFlat B S hS G.target.hom)
    (_hsLfp : Space.IsLocallyOfFinitePresentation B S hS G.source.hom)
    (_htLfp : Space.IsLocallyOfFinitePresentation B S hS G.target.hom)
    (hs : Space.IsProper B S hS G.source.hom)
    (_ht : Space.IsProper B S hS G.target.hom)
    (hU : Space.IsSeparated B S hS G.objectsToBase.hom) :
    IsSeparatedOver.{u, w} B S hS 𝒳
```

## Tag 0DTZ, a lemma

[Tag 0DTZ](https://stacks.math.columbia.edu/tag/0DTZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.equivalence_sourceTargetRel_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean#L183). The attribute's comment: “the image of |R| in |U| x |U| is an equivalence relation, with no hypothesis on the source and target maps”.

> **Stacks 0DTZ.** For a groupoid in algebraic spaces `(U, R, s, t, c)` the image of
> `|R| → |U| × |U|` is an equivalence relation on the points of the object space: the pair of
> points related by a point of the arrow space is its target and its source, and the arrows over
> each test scheme form a groupoid.
>
> No hypothesis on the source and target maps is needed; the flatness and local finite presentation
> of Stacks 0DTZ enter only through the algebraicity of the quotient stack.

```lean
theorem equivalence_sourceTargetRel_points (G : GroupoidInAlgebraicSpaces C S hS B) :
    Equivalence (Function.SourceTargetRel
      (Space.pointsMap C S hS G.arrows.obj G.source.hom)
      (Space.pointsMap C S hS G.arrows.obj G.target.hom))
```

**`AlgebraicGeometry.Stack.pointMap_eq_iff_sourceTargetRel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean#L416). The attribute's comment: “the fibres of |U| -> |[U/R]| are the classes of the image of |R|, with no hypothesis on the source and target maps”.

> **Stacks 0DTZ.** Two points of the object space of a groupoid in algebraic spaces have the
> same image in the points of the quotient stack exactly when they lie in the image of
> `|R| → |U| × |U|`, that is exactly when some point of the arrow space has the first as its target
> and the second as its source.
>
> No hypothesis on the source and target maps is needed; the flatness and local finite presentation
> of Stacks 0DTZ enter only through the algebraicity of the quotient stack.

```lean
theorem pointMap_eq_iff_sourceTargetRel
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (first second : Space.points C S hS G.objects.obj) :
    quotientStackPointMap G first = quotientStackPointMap G second ↔
      Function.SourceTargetRel
        (Space.pointsMap C S hS G.arrows.obj G.source.hom)
        (Space.pointsMap C S hS G.arrows.obj G.target.hom)
        first second
```

**`AlgebraicGeometry.Stack.surjective_quotientStackPointMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean#L458). The attribute's comment: “|U| surjects onto the points of the quotient stack, with no hypothesis on the source and target maps”.

> **Stacks 0DTZ.** Every point of the quotient stack `[U/R]` of a groupoid in
> algebraic spaces is the image of a point of the object space `U`.
>
> No hypothesis on the groupoid is needed: a point of `|[U/R]|` is represented by an object over
> the spectrum of a field, the projection is surjective on objects by
> `AlgebraicGeometry.Stack.isSurjectiveOnObjects_quotientStackProjection`, and the resulting
> object of the object space over a field extension is dominated by a field-valued point of `U`
> whose image therefore has a common refinement with the chosen representative.

```lean
theorem surjective_quotientStackPointMap (G : GroupoidInAlgebraicSpaces C S hS B) :
    Function.Surjective (quotientStackPointMap G)
```

**`AlgebraicGeometry.Stack.exists_quotientPointsEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuotientStackPoints.lean#L491). The attribute's comment: “|[U/R]| is the quotient of |U| by that equivalence relation, with no hypothesis on the source and target maps”.

> **Stacks 0DTZ.** The points of the quotient stack of a groupoid in algebraic spaces are the
> quotient of the points of the object space by the image of `|R| → |U| × |U|`: there is an
> equivalence of the quotient set with `|[U/R]|` carrying the class of a point of `|U|` to its
> image under the canonical map, so the identification is the canonical one and not merely a
> bijection of underlying sets.
>
> No hypothesis on the source and target maps is needed; the flatness and local finite presentation
> of Stacks 0DTZ enter only through the algebraicity of the quotient stack.

```lean
theorem exists_quotientPointsEquiv (G : GroupoidInAlgebraicSpaces C S hS B) :
    ∃ e : Quotient (arrowSetoid G) ≃
        points C S hS (quotientStack G) (isFiberedInGroupoids_quotientStack G),
      ∀ x : Space.points C S hS G.objects.obj,
        e (Quotient.mk _ x) = quotientStackPointMap G x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.20, Tag 0DTX](https://stacks.math.columbia.edu/tag/0DTX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
