---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_restriction, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_restrictionAlong, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_iff_restrictionAlong, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff_exists_cover, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_groupoidOfAction_iff_exists_cover, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff, AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_trivialAction, AlgebraicGeometry.Stack.isFlat_and_isLocallyOfFinitePresentation_of_isAlgebraicStack_trivialAction
statement: formalized
proof: formalized
---

# 97.18 When is a quotient stack algebraic?

Section 97.18 of the Stacks Project, [Tag 06PI](https://stacks.math.columbia.edu/tag/06PI). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06PJ, a lemma

[Tag 06PJ](https://stacks.math.columbia.edu/tag/06PJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GroupoidPresentationQuotientAlgebraic.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GroupoidPresentationQuotientAlgebraic.lean#L268). The attribute's comment: “the implication from the existence of the restriction to algebraicity, for a groupoid exhibited by `hrestriction` as the restriction along `g`, with Stacks 06FI carried as a hypothesis; the converse, which needs Stacks 044X, 044V, 04T4, 046N and 04WY, is not proved”.

> **Stacks 06PJ**, the implication from the existence of a suitable restriction to
> algebraicity. Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `B` and let
> `f : (U', R', s', t', c') ⟶ (U, R, s, t, c)` exhibit its source as the restriction of its target
> along `g = f_U : U' ⟶ U`. If the saturation map `U' ×_{g, U, t} R ⟶ R ⟶ U` is a surjection of
> fppf sheaves and `s', t'` are flat and locally of finite presentation, then the quotient stack
> `[U/R]` is an algebraic stack.
>
> Stacks 06FI, which is not in the library, is carried as the hypothesis `h06FI`.

```lean
theorem isAlgebraicStack_quotientStack_of_restriction
    (G G' : GroupoidInAlgebraicSpaces C S hS B)
    (f : GroupoidInAlgebraicSpaces.Hom G' G)
    (h06FI : ∀ H : GroupoidInAlgebraicSpaces C S hS B,
      Space.IsFlat C S hS H.source.hom → Space.IsFlat C S hS H.target.hom →
        Space.IsLocallyOfFinitePresentation C S hS H.source.hom →
          Space.IsLocallyOfFinitePresentation C S hS H.target.hom →
            IsAlgebraicStack.{u, w} C S hS (quotientStack H))
    (hrestriction : IsPullback f.toGroupoidHom.mapArrows
      (prod.lift G'.toGroupoidInFunctors.source G'.toGroupoidInFunctors.target)
      (prod.lift G.toGroupoidInFunctors.source G.toGroupoidInFunctors.target)
      (prod.map f.toGroupoidHom.mapObjects f.toGroupoidHom.mapObjects))
    (hsaturation : Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
      ((GroupoidInAlgebraicSpaces.fiberProductSnd
        (ObjectProperty.homMk f.toGroupoidHom.mapObjects : G'.objects ⟶ G.objects)
        G.target ≫ G.source).hom))
    (hsource : Space.IsFlat C S hS G'.source.hom)
    (htarget : Space.IsFlat C S hS G'.target.hom)
    (hsourceFP : Space.IsLocallyOfFinitePresentation C S hS G'.source.hom)
    (htargetFP : Space.IsLocallyOfFinitePresentation C S hS G'.target.hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_of_restrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GroupoidPresentationQuotientAlgebraic.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GroupoidPresentationQuotientAlgebraic.lean#L307). The attribute's comment: “the implication from the existence of the restriction to algebraicity, for the canonical restriction of Stacks 044B along `g`, with Stacks 06FI carried as a hypothesis; the converse, which needs Stacks 044X, 044V, 04T4, 046N and 04WY, is not proved”.

> **Stacks 06PJ**, the implication from the existence of the restriction to algebraicity, in
> the form the source states it. Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `B`
> and let `g : U' ⟶ U` be a morphism of algebraic spaces such that the saturation map
> `U' ×_{g, U, t} R ⟶ R ⟶ U` is a surjection of fppf sheaves and the source and target of the
> restriction `(U', R', s', t', c')` of `(U, R, s, t, c)` along `g` are flat and locally of finite
> presentation. Then the quotient stack `[U/R]` is an algebraic stack.
>
> Stacks 06FI, which is not in the library, is carried as the hypothesis `h06FI`.

```lean
theorem isAlgebraicStack_quotientStack_of_restrictionAlong
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {U' : AlgebraicSpaces C S hS} (g : U' ⟶ G.objects)
    (h06FI : ∀ H : GroupoidInAlgebraicSpaces C S hS B,
      Space.IsFlat C S hS H.source.hom → Space.IsFlat C S hS H.target.hom →
        Space.IsLocallyOfFinitePresentation C S hS H.source.hom →
          Space.IsLocallyOfFinitePresentation C S hS H.target.hom →
            IsAlgebraicStack.{u, w} C S hS (quotientStack H))
    (hsaturation : Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
      ((GroupoidInAlgebraicSpaces.fiberProductSnd g G.target ≫ G.source).hom))
    (hsource : Space.IsFlat C S hS
      (GroupoidInAlgebraicSpaces.restrictionSource G g).hom)
    (htarget : Space.IsFlat C S hS
      (GroupoidInAlgebraicSpaces.restrictionTarget G g).hom)
    (hsourceFP : Space.IsLocallyOfFinitePresentation C S hS
      (GroupoidInAlgebraicSpaces.restrictionSource G g).hom)
    (htargetFP : Space.IsLocallyOfFinitePresentation C S hS
      (GroupoidInAlgebraicSpaces.restrictionTarget G g).hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack G)
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_iff_restrictionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraicIffRestriction.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/QuotientStackAlgebraicIffRestriction.lean#L289).

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

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff_exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean#L67). The attribute's comment: “for any action groupoid construction of Stacks 0444”.

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

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_groupoidOfAction_iff_exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/ActionQuotientStackAlgebraicIff.lean#L95). The attribute's comment: “for the action groupoid of Stacks 0444 that the library builds”.

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

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_action_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GerbeGroupDescent.lean, line 874](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GerbeGroupDescent.lean#L874). The attribute's comment: “with Stacks 06PJ, the same criterion for an arbitrary groupoid in algebraic spaces, carried as the explicit hypothesis h06PJ”.

> **Stacks 06PK.** Let a group algebraic space `G` over an algebraic space `B` act on an
> algebraic space `X` over `B`. The quotient stack `[X/G]` of the action groupoid is an algebraic
> stack exactly when there is a morphism `φ : X' ⟶ X` of algebraic spaces over `B` for which
> `G ×_B X' ⟶ X`, `(g, x') ↦ g • φ x'`, is a surjection of fppf sheaves and both projections to
> `X'` of the space of triples `{(x₁, g, x₂) : φ x₁ = g • φ x₂}` are flat and locally of finite
> presentation.
>
> Stacks 06PJ, the same criterion for an arbitrary groupoid in algebraic spaces, is not in the
> library and is carried as the hypothesis `h06PJ`.

```lean
theorem isAlgebraicStack_quotientStack_action_iff
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
    (G X : Over B.obj) [GrpObj G] [ModObj G X]
    (hG : IsAlgebraicSpace C S hS G.left) (hX : IsAlgebraicSpace C S hS X.left)
    (A : Space.ActionGroupoidConstruction B G X hG hX)
    (h06PJ : ∀ H : GroupoidInAlgebraicSpaces C S hS B,
      IsAlgebraicStack.{u, w} C S hS (quotientStack H) ↔
        ∃ (U' : AlgebraicSpaces C S hS) (g : U' ⟶ H.objects),
          Presheaf.IsLocallySurjective (BigFppfOver.topology C S hS)
            ((GroupoidInAlgebraicSpaces.fiberProductSnd g H.target ≫ H.source).hom) ∧
          Space.IsFlat C S hS
            (GroupoidInAlgebraicSpaces.restrictionSource H g).hom ∧
          Space.IsFlat C S hS
            (GroupoidInAlgebraicSpaces.restrictionTarget H g).hom ∧
          Space.IsLocallyOfFinitePresentation C S hS
            (GroupoidInAlgebraicSpaces.restrictionSource H g).hom ∧
          Space.IsLocallyOfFinitePresentation C S hS
            (GroupoidInAlgebraicSpaces.restrictionTarget H g).hom) :
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

## Tag 06PL, a lemma

[Tag 06PL](https://stacks.math.columbia.edu/tag/06PL) in the Stacks Project.

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_trivialAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraic.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraic.lean#L128). The attribute's comment: “the implication from flat and locally of finite presentation to algebraic, with Stacks 06FI carried as a hypothesis; the converse, which rests on Stacks 06PK, is not proved”.

> **Stacks 06PL**, the implication from flatness and local finite presentation to
> algebraicity. Let `G` be a group algebraic space over an algebraic space `B` over `S` and endow
> `B` with the trivial action of `G`. If `G` is flat and locally of finite presentation over `B`,
> then the quotient stack `[B/G]` is an algebraic stack.
>
> Stacks 06FI, which is not in the library, is carried as the hypothesis `h06FI`.

```lean
theorem isAlgebraicStack_quotientStack_trivialAction
    (B : AlgebraicSpaces C S hS) (G : Over B.obj) [GrpObj G]
    (hG : IsAlgebraicSpace C S hS G.left)
    (A : Space.ActionGroupoidConstruction B G (𝟙_ (Over B.obj)) hG B.property)
    (h06FI : ∀ H : GroupoidInAlgebraicSpaces C S hS B,
      Space.IsFlat C S hS H.source.hom → Space.IsFlat C S hS H.target.hom →
        Space.IsLocallyOfFinitePresentation C S hS H.source.hom →
          Space.IsLocallyOfFinitePresentation C S hS H.target.hom →
            IsAlgebraicStack.{u, w} C S hS (quotientStack H))
    (hflat : Space.IsFlat C S hS G.hom)
    (hlfp : Space.IsLocallyOfFinitePresentation C S hS G.hom) :
    IsAlgebraicStack.{u, w} C S hS (quotientStack A.groupoid)
```

**`AlgebraicGeometry.Stack.isFlat_and_isLocallyOfFinitePresentation_of_isAlgebraicStack_trivialAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraicIff.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraicIff.lean#L153). The attribute's comment: “the converse implication, from algebraicity to flat and locally of finite presentation, with nothing carried”.

> **Stacks 06PL, the converse implication.** Let `G` be a group algebraic space over an
> algebraic space `B` over `S`, endow `B` with the trivial action of `G`, and suppose the quotient
> stack `[B/G]` is an algebraic stack. Then `G ⟶ B` is flat and locally of finite presentation.
>
> The converse of **Stacks 06PJ**,
> `AlgebraicGeometry.Stack.exists_restrictionAlong_of_isAlgebraicStack`, supplies the citation of
> **Stacks 06PK** that the source's proof makes, and
> `AlgebraicGeometry.Stack.isFlat_and_isLocallyOfFinitePresentation_of_trivialActionCriterion` is the
> rest of the argument; see the module docstring.

```lean
theorem isFlat_and_isLocallyOfFinitePresentation_of_isAlgebraicStack_trivialAction
    (B : AlgebraicSpaces C S hS) (G : Over B.obj) [GrpObj G]
    (hG : IsAlgebraicSpace C S hS G.left)
    (A : Space.ActionGroupoidConstruction B G (𝟙_ (Over B.obj)) hG B.property)
    (h : IsAlgebraicStack.{u, w} C S hS (quotientStack A.groupoid)) :
    Space.IsFlat C S hS G.hom ∧ Space.IsLocallyOfFinitePresentation C S hS G.hom
```

**`AlgebraicGeometry.Stack.isAlgebraicStack_quotientStack_trivialAction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraicIff.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionAlgebraicIff.lean#L217).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
