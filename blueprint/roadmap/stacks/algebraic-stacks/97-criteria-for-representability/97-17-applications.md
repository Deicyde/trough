---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_hasRelativeProperty_flat_lfp_surjective_quotientStackProjectionHom, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_flat
statement: formalized
proof: formalized
---

# 97.17 Applications

Section 97.17 of the Stacks Project, [Tag 06FG](https://stacks.math.columbia.edu/tag/06FG). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06FH, a lemma

[Tag 06FH](https://stacks.math.columbia.edu/tag/06FH) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_hasRelativeProperty_flat_lfp_surjective_quotientStackProjectionHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDiagonalUnconditional.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackDiagonalUnconditional.lean#L133).

> **The atlas of the quotient stack of a flat, locally finitely presented groupoid.** Let
> `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over an algebraic space `A` over a scheme
> `S` of a big fppf site, and assume its source and target maps `s`, `t` are flat and locally of
> finite presentation. Then the canonical projection `π : S_U ⟶ [U/R]` of Stacks 044R is
> representable by algebraic spaces and is flat, locally of finite presentation and surjective in
> the sense of Stacks 03YK.

```lean
theorem exists_hasRelativeProperty_flat_lfp_surjective_quotientStackProjectionHom
    {A : AlgebraicSpaces C S hS} (G : GroupoidInAlgebraicSpaces C S hS A)
    (hsflat : Space.IsFlat C S hS G.source.hom)
    (htflat : Space.IsFlat C S hS G.target.hom)
    (hslfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (htlfp : Space.IsLocallyOfFinitePresentation C S hS G.target.hom) :
    ∃ hπ : IsRepresentableByAlgebraicSpaces C S hS (quotientStackProjectionHom G).hom,
      HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
          (fun ⦃X Y : AlgebraicSpaces C S hS⦄ (f : X ⟶ Y) => Space.IsFlat C S hS f.hom)
          (quotientStackProjectionHom G) hπ ∧
        HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
          (fun ⦃X Y : AlgebraicSpaces C S hS⦄ (f : X ⟶ Y) =>
            Space.IsLocallyOfFinitePresentation C S hS f.hom)
          (quotientStackProjectionHom G) hπ ∧
        HasRelativeProperty.{u, u + 1, u + 1, u} C S hS
          (Space.surjectiveMorphismProperty C S hS) (quotientStackProjectionHom G) hπ
```

## Tag 06FI, a theorem

[Tag 06FI](https://stacks.math.columbia.edu/tag/06FI) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatQuotientStackAlgebraic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FlatQuotientStackAlgebraic.lean#L48). The attribute's comment: “stated for a groupoid in algebraic spaces over an arbitrary algebraic space A over S, the source's groupoid over S being the case A = S; Stacks 06DC, 06FH and 04TB are proved”.

> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over an algebraic space `A` over
> a scheme `S` of a big fppf site. If the source and the target of `G` are flat and locally of finite
> presentation, then the quotient stack `[U/R]` is an algebraic stack over `S`.
>
> The source states it for a groupoid over `S`; a groupoid over `A` is the more general statement,
> the source's case being `A = S`, with `S` the final algebraic space over `S`. Nothing is assumed:
> the proof is Artin's theorem **Stacks 06DC**,
> `AlgebraicGeometry.Stack.isAlgebraicStack_of_flatCover`, applied to the projection
> `S_U ⟶ [U/R]` of Stacks 044R, read with the morphisms of `[U/R]` shrunk to the site's universe.
> The projection is representable by algebraic spaces by Stacks 04WZ and Stacks 04TB, and it is
> surjective, flat and locally of finite presentation by **Stacks 06FH**.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
