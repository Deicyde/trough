---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_iff_restrictionAlong, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff_exists_cover, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_groupoidOfAction_iff_exists_cover, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_trivialAction_iff
statement: formalized
proof: formalized
---

# 97.18 When is a quotient stack algebraic?

Section 97.18 of the Stacks Project, [Tag 06PI](https://stacks.math.columbia.edu/tag/06PI). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06PJ, a lemma

[Tag 06PJ](https://stacks.math.columbia.edu/tag/06PJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_iff_restrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraicIffRestriction.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraicIffRestriction.lean#L294).

> Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `B`. The
> quotient stack `[U/R]` is an algebraic stack if and only if there is a morphism `g : U' ⟶ U` of
> algebraic spaces over `S` such that
>
> 1. the saturation map `U' ×_{g, U, t} R ⟶ R ⟶ U` is a surjection of fppf sheaves, and
> 2. the source and target of the restriction of `(U, R, s, t, c)` along `g` are flat and locally of
>    finite presentation.

```lean
theorem isAlgebraicStack_quotientStack_iff_restrictionAlong
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G) ↔
      ∃ (U' : AlgebraicSpaces C S hS) (g : U' ⟶ G.objects),
        Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
          ((GroupoidInAlgebraicSpaces.fiberProductSnd g G.target ≫ G.source).hom) ∧
        Space.IsFlat C S hS (GroupoidInAlgebraicSpaces.restrictionSource G g).hom ∧
        Space.IsFlat C S hS (GroupoidInAlgebraicSpaces.restrictionTarget G g).hom ∧
        Space.IsLocallyOfFinitePresentation C S hS
          (GroupoidInAlgebraicSpaces.restrictionSource G g).hom ∧
        Space.IsLocallyOfFinitePresentation C S hS
          (GroupoidInAlgebraicSpaces.restrictionTarget G g).hom
```

## Tag 06PK, a lemma

[Tag 06PK](https://stacks.math.columbia.edu/tag/06PK) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff_exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean#L67). The attribute's comment: “the full criterion, for any action groupoid construction of Stacks 0444”.

> **Stacks 06PK.** Let a group algebraic space `G` over an algebraic space `B` act on an
> algebraic space `X` over `B`. The quotient stack `[X/G]` of the action groupoid of
> **Stacks 0444** is an algebraic stack exactly when there is a morphism `φ : X' ⟶ X` of algebraic
> spaces over `B` for which
>
> 1. `G ×_B X' ⟶ X`, `(g, x') ↦ g • φ x'`, is a surjection of fppf sheaves, and
> 2. both projections to `X'` of the space of triples `{(x₁, g, x₂) : φ x₁ = g • φ x₂}`, the fibre
>    product `X' ×_{φ, X, a} (G ×_B X')`, are flat and locally of finite presentation.
>
> This is `AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff` with the
> biconditional of **Stacks 06PJ** it takes supplied by
> `AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_iff_restrictionAlong`.

```lean
theorem isAlgebraicStack_quotientStack_action_iff_exists_cover
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
    (G X : Over B.obj) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace C S hS G.left) (hX : IsAlgebraicSpace C S hS X.left)
    (A : Space.ActionGroupoidConstruction B G X hG hX) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack A.groupoid) ↔
      ∃ (X' : Over B.obj) (_ : IsAlgebraicSpace C S hS X'.left) (φ : X' ⟶ X),
        let a : G ⊗ X' ⟶ X := (𝟙 G ⊗ₘ φ) ≫ γ[G, X]
        Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS) a.left ∧
        Space.IsFlat C S hS (pullback.fst φ.left a.left) ∧
        Space.IsLocallyOfFinitePresentation C S hS (pullback.fst φ.left a.left) ∧
        Space.IsFlat C S hS (pullback.snd φ.left a.left ≫ (snd G X').left) ∧
        Space.IsLocallyOfFinitePresentation C S hS
          (pullback.snd φ.left a.left ≫ (snd G X').left)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_groupoidOfAction_iff_exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean#L95). The attribute's comment: “the full criterion, for the action groupoid of Stacks 0444 that the library builds”.

> **Stacks 06PK for the action groupoid of Stacks 0444 that the library builds.** The quotient
> stack `[X/G]` is an algebraic stack exactly when there is a morphism `φ : X' ⟶ X` of algebraic
> spaces over `B` for which `G ×_B X' ⟶ X`, `(g, x') ↦ g • φ x'`, is a surjection of fppf sheaves
> and both projections to `X'` of the space of triples `{(x₁, g, x₂) : φ x₁ = g • φ x₂}` are flat
> and locally of finite presentation.
>
> This is `AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_groupoidOfAction_iff` with the
> biconditional of Stacks 06PJ it takes supplied as in
> `AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff_exists_cover`.

```lean
theorem isAlgebraicStack_quotientStack_groupoidOfAction_iff_exists_cover
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
    (G X : Over B.obj) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace C S hS G.left) (hX : IsAlgebraicSpace C S hS X.left) :
    IsAlgebraicStack.{u, w} C S hS
        (quotientStack (Space.groupoidOfAction B G X hG hX).groupoid) ↔
      ∃ (X' : Over B.obj) (_ : IsAlgebraicSpace C S hS X'.left) (φ : X' ⟶ X),
        let a : G ⊗ X' ⟶ X := (𝟙 G ⊗ₘ φ) ≫ γ[G, X]
        Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS) a.left ∧
        Space.IsFlat C S hS (pullback.fst φ.left a.left) ∧
        Space.IsLocallyOfFinitePresentation C S hS (pullback.fst φ.left a.left) ∧
        Space.IsFlat C S hS (pullback.snd φ.left a.left ≫ (snd G X').left) ∧
        Space.IsLocallyOfFinitePresentation C S hS
          (pullback.snd φ.left a.left ≫ (snd G X').left)
```

## Tag 06PL, a lemma

[Tag 06PL](https://stacks.math.columbia.edu/tag/06PL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_trivialAction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraicIff.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraicIff.lean#L217). The attribute's comment: “both implications; the group algebraic space G over B is a group object of the slice over B, and [B/G] is the quotient stack of the action groupoid of its trivial action on B”.

> **Stacks 06PL.** Let `G` be a group algebraic space over an algebraic space `B` over `S` and
> endow `B` with the trivial action of `G`. The quotient stack `[B/G]` is an algebraic stack if and
> only if `G ⟶ B` is flat and locally of finite presentation.

```lean
theorem isAlgebraicStack_quotientStack_trivialAction_iff
    (B : AlgebraicSpaces C S hS) (G : Over B.obj) [GrpObj G]
    (hG : IsAlgebraicSpace C S hS G.left)
    (A : Space.ActionGroupoidConstruction B G (𝟙_ (Over B.obj)) hG B.property) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack A.groupoid) ↔
      (Space.IsFlat C S hS G.hom ∧
        Space.IsLocallyOfFinitePresentation C S hS G.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.18, Tag 06PI](https://stacks.math.columbia.edu/tag/06PI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
