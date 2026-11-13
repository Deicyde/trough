---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.quotientPointwiseMapData, AlgebraicGeometry.Stack.quotientStackMap, AlgebraicGeometry.Stack.quotientStackMap_commutes, AlgebraicGeometry.Stack.isFinalTwoCommSq_auxQuotientSquare
statement: formalized
proof: formalized
---

# 78.21 Functoriality of quotient stacks

Section 78.21 of the Stacks Project, [Tag 04Y3](https://stacks.math.columbia.edu/tag/04Y3). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 046Q, a lemma

[Tag 046Q](https://stacks.math.columbia.edu/tag/046Q) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientPointwiseMapData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Functoriality.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Functoriality.lean#L132). The attribute's comment: “the strict map on the presenting groupoids”.

> The strict natural map between the presenting pseudofunctors of the two pointwise groupoid
> fibrations: its component at a test object is the evaluated functor of the given groupoid
> morphism, and its naturality isomorphisms are transports.

```lean
noncomputable def quotientPointwiseMapData {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H) :
    { α : (evaluationGroupoidFunctor G.toGroupoidInFunctors ⋙
            Grpd.forgetToCat).toPseudofunctor' ⟶
          (evaluationGroupoidFunctor H.toGroupoidInFunctors ⋙
            Grpd.forgetToCat).toPseudofunctor' //
      (∀ T : BigFppfOver C S hS,
        (α.app ⟨op T⟩).toFunctor = f.toGroupoidHom.evaluation (op T)) ∧
      (∀ {a b} (g : a ⟶ b),
        ∃ h : ((evaluationGroupoidFunctor G.toGroupoidInFunctors ⋙
              Grpd.forgetToCat).toPseudofunctor').map g ≫ α.app b =
            α.app a ≫ ((evaluationGroupoidFunctor H.toGroupoidInFunctors ⋙
              Grpd.forgetToCat).toPseudofunctor').map g,
          α.naturality g = eqToIso h) }
```

**`AlgebraicGeometry.Stack.quotientStackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Functoriality.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Functoriality.lean#L265). The attribute's comment: “the induced morphism”.

> The canonical 1-morphism `[f] : [U/R] ⟶ [U'/R']` of quotient stacks induced
> by a morphism of groupoids in algebraic spaces over the same base.

```lean
noncomputable def quotientStackMap {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H) :
    BasedFunctor (quotientStack G) (quotientStack H)
```

**`AlgebraicGeometry.Stack.quotientStackMap_commutes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Functoriality.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Functoriality.lean#L279). The attribute's comment: “compatibility with the presentations”.

> The induced 1-morphism intertwines the pointwise groupoid map with the two
> stackification maps, naturally and over the site.

```lean
noncomputable def quotientStackMap_commutes {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H) :
    BasedFunctor.comp (quotientPointwiseMap f) (pointwiseToQuotientStackBased H) ≅
      BasedFunctor.comp (pointwiseToQuotientStackBased G) (quotientStackMap f)
```

## Tag 04Y4, a lemma

[Tag 04Y4](https://stacks.math.columbia.edu/tag/04Y4) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFinalTwoCommSq_auxQuotientSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FunctorialityQuotientStackTwoFibreProduct.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FunctorialityQuotientStackTwoFibreProduct.lean#L154). The attribute's comment: “the 2-commutative square of Section 78.21 and the identification of the quotient stack of the auxiliary groupoid with the 2-fibre product of the cospan”.

> **Stacks 04Y4.** Let `φ : (U, R, s, t, c) ⟶ (U', R', s', t', c')` be a morphism of groupoids in
> algebraic spaces over an algebraic space `B` over a scheme `S` of a big fppf site, written
> `f : U ⟶ U'` on object spaces, and let `(U'', R'', s'', t'', c'')` be the groupoid in algebraic
> spaces over `B` of Section 78.21, with `U'' = U ×_{f, U', t'} R'`, `R'' = R ×_{f ∘ s, U', t'} R'`,
> `s''(r, r') = (s(r), r')`, `t''(r, r') = (t(r), c'(f(r), r'))` and
> `c''((r₁, r'₁), (r₂, r'₂)) = (c(r₁, r₂), r'₂)`. Then the square
>
> ```
> [U''/R''] ---[g]---> [U/R]
>     |                  |
>     |                 [φ]
>     v                  v
>   𝒮_{U'} ----π'----> [U'/R']
> ```
>
> — whose horizontal arrow is the 1-morphism `[g]` of Stacks 046Q induced by the projection
> `g : (U'', R'', s'', t'', c'') ⟶ (U, R, s, t, c)`, whose vertical arrow on the left is the descent
> to `[U''/R'']` of the `R''`-invariant morphism `U'' ⟶ U'`, `(u, r') ↦ s'(r')`, whose vertical
> arrow on the right is the 1-morphism `[φ]` of Stacks 046Q, whose lower horizontal arrow is the
> canonical projection `π'` of Stacks 044R, and whose filler
> `AlgebraicGeometry.Stack.auxSquareCell` is the arrow `r'` of the evaluated groupoid of `G'` at a
> point `(u, r')` of `U''` — **is a 2-fibre product** in the sense of Stacks 003Q in the
> 2-category of stacks in groupoids over the big fppf site (a final object of the 2-category of
> 2-commutative diagrams over the cospan, with the uniqueness of the 2-isomorphism of
> Stacks 003P (2)), so it identifies `[U''/R'']` with `[U/R] ×_{[φ], [U'/R'], π'} 𝒮_{U'}`. The
> legs of the explicit 2-fibre product of the cospan detect 2-cells, and detection passes to every
> terminal object of the quotient category of squares.

```lean
noncomputable def isFinalTwoCommSq_auxQuotientSquare (φ : Hom G G') :
    Bicategory.IsFinalTwoCommSq (auxQuotientSquare φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.21, Tag 04Y3](https://stacks.math.columbia.edu/tag/04Y3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
