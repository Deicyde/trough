---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsAffineFormalAlgebraicSpace, AlgebraicGeometry.IsAffineFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.diagonal_isClosedImmersion, AlgebraicGeometry.FormalSpace.relativelyRepresentable_colimitι, AlgebraicGeometry.FormalSpace.isThickening_colimitι, AlgebraicGeometry.exists_factor_through_thickening', AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_iff, AlgebraicGeometry.FormalSpace.exists_isPresentingRing_of_hasAffineClosedImmersionCriterion
statement: formalized
proof: formalized
---

# 87.9 Affine formal algebraic spaces

Section 87.9 of the Stacks Project, [Tag 0AI6](https://stacks.math.columbia.edu/tag/0AI6). 11 tags here are carried by 74 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AI7, a definition

[Tag 0AI7](https://stacks.math.columbia.edu/tag/0AI7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsAffineFormalAlgebraicSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine.lean#L85).

> An *affine formal algebraic space* over `S` is an fppf sheaf on the big fppf site of `S`
> which satisfies the set-theoretic condition
> `AlgebraicGeometry.FormalSpace.SatisfiesSetTheoreticCondition` and which is the colimit of a
> directed diagram of affine schemes over `S` all of whose transition morphisms are thickenings.

```lean
abbrev IsAffineFormalAlgebraicSpace (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.IsAffineFormalAlgebraicSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Defs.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Defs.lean#L70).

> An *affine formal algebraic space* over `S` is a sheaf on the big fppf site of `S` which
> satisfies the set-theoretic condition and is a directed colimit of sheaves represented by affine
> schemes whose transition morphisms are thickenings.

```lean
abbrev IsAffineFormalAlgebraicSpace (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))) : Prop
```

## Tag 0AI8, a lemma

[Tag 0AI8](https://stacks.math.columbia.edu/tag/0AI8) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.diagonal_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Diagonal.lean, line 646](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Diagonal.lean#L646).

> The diagonal of an affine formal algebraic space is representable and a
> closed immersion.

```lean
public theorem diagonal_isClosedImmersion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type (u + 1)} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ BigAffineFppf B S hS)
    (hD : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      Stacks.Thickenings.IsThickening
        ((BigAffineFppf.toScheme B S hS).map (D.map f)))
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (e : colimit
      (D ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda
          (BigFppfOver.topology B S hS)) ≅ X) :
    (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) (diag X)
```

## Tag 0AI9, a lemma

[Tag 0AI9](https://stacks.math.columbia.edu/tag/0AI9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_colimitι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/ThickeningStage.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/ThickeningStage.lean#L300). The attribute's comment: “representability”.

> **Stacks 0AI9.** A stage of a directed presentation of an affine formal algebraic space by
> affine schemes with thickening transition morphisms maps representably to the colimit: every
> base change of `X_i ⟶ X` along a morphism from a represented sheaf is again represented by an
> object of the site.

```lean
theorem relativelyRepresentable_colimitι (i : I) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (colimit.ι
        (D ⋙ BigAffineFppf.inclusion B S hS ⋙
          Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) i ≫ e.hom)
```

**`AlgebraicGeometry.FormalSpace.isThickening_colimitι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/ThickeningStage.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/ThickeningStage.lean#L318). The attribute's comment: “thickening”.

> **Stacks 0AI9.** A stage of a directed presentation of an affine formal algebraic space by
> affine schemes with thickening transition morphisms maps to the colimit by a thickening: the
> map `X_i ⟶ X` is representable, and each of its base changes along a represented sheaf is a
> thickening of schemes.

```lean
theorem isThickening_colimitι (i : I) :
    (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)))
      (colimit.ι
        (D ⋙ BigAffineFppf.inclusion B S hS ⋙
          Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) i ≫ e.hom)
```

## Tag 0AIA, a lemma

[Tag 0AIA](https://stacks.math.columbia.edu/tag/0AIA) in the Stacks Project.

**`AlgebraicGeometry.exists_factor_through_thickening'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Factorization.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Factorization.lean#L189).

> A morphism from a quasi-compact algebraic space to a presented affine formal
> algebraic space factors through one of its affine stages.
>
> Two of the hypotheses of Stacks 0AIA are not asked for, because the argument does not use them.
> Of the target, only the presentation `D`, `hD`, `e` is used, so the set-theoretic condition of
> Stacks 0AIS -- the other half of being an affine formal algebraic space, and for a formal
> spectrum a condition on the size of the site -- is not assumed. Of the transition morphisms of
> the presentation, only that they are closed immersions is used, not that they are thickenings:
> surjectivity plays no part. The index of the presentation may lie in any universe, provided it
> is `u + 1`-small, the colimit being taken in sheaves of `Type (u + 1)`. Of the source, only the
> surjective étale cover by a quasi-compact scheme that quasi-compactness provides is used, so `Y`
> is not assumed to be an algebraic space.

```lean
theorem exists_factor_through_thickening'
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (I : Type w₁) [Preorder I] [Small.{u + 1} I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ BigAffineFppf B S hS)
    (hD : ∀ ⦃i j : I⦄ (g : i ⟶ j),
      IsClosedImmersion ((BigAffineFppf.toScheme B S hS).map (D.map g)))
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (e : X ≅ colimit
      (D ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)))
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hYqc : Space.IsQuasiCompactSpace B S hS Y)
    (f : (presheafToSheaf (BigFppfOver.topology B S hS)
      (Type (u + 1))).obj (Y ⋙ uliftFunctor.{u + 1, u}) ⟶ X) :
    ∃ i : I, ∃ g : (presheafToSheaf (BigFppfOver.topology B S hS)
        (Type (u + 1))).obj (Y ⋙ uliftFunctor.{u + 1, u}) ⟶
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
          ((BigAffineFppf.inclusion B S hS).obj (D.obj i)),
      g ≫ colimit.ι
      (D ⋙ BigAffineFppf.inclusion B S hS ⋙
        Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) i ≫
        e.inv = f
```

## Tag 0AIB, a lemma

[Tag 0AIB](https://stacks.math.columbia.edu/tag/0AIB) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Characterization.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Characterization.lean#L580).

> **Stacks 0AIB.** A sheaf on the big fppf site of `S` is an affine formal algebraic space if
> and only if every morphism to it from a sheaf represented by an affine scheme over `S` factors
> through a morphism from an affine scheme over `S` which is representable and a thickening, and
> the sheaf satisfies the set-theoretic condition of Stacks 0AIS.

```lean
theorem isAffineFormalAlgebraicSpace_iff
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))) :
    IsAffineFormalAlgebraicSpace B S hS X ↔
      ((∀ U : BigAffineFppf B S hS,
          ∀ f : (Sheaf.sheafifiedYoneda
            (BigFppfOver.topology B S hS)).obj
              ((BigAffineFppf.inclusion B S hS).obj U) ⟶ X,
          ∃ T : BigAffineFppf B S hS,
            ∃ g : (Sheaf.sheafifiedYoneda
              (BigFppfOver.topology B S hS)).obj
                ((BigAffineFppf.inclusion B S hS).obj U) ⟶
              (Sheaf.sheafifiedYoneda
                (BigFppfOver.topology B S hS)).obj
                  ((BigAffineFppf.inclusion B S hS).obj T),
            ∃ h : (Sheaf.sheafifiedYoneda
              (BigFppfOver.topology B S hS)).obj
                ((BigAffineFppf.inclusion B S hS).obj T) ⟶ X,
              (Sheaf.sheafifiedYoneda
                (BigFppfOver.topology B S hS)).relativelyRepresentable h ∧
              (MorphismProperty.relative
                (Sheaf.sheafifiedYoneda
                  (BigFppfOver.topology B S hS))
                (MorphismProperty.inverseImage
                  (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
                  (BigFppfOver.toScheme B S hS))) h ∧
              g ≫ h = f) ∧
        SatisfiesSetTheoreticCondition B S hS X)
```

## Tag 0AIC, a lemma

[Tag 0AIC](https://stacks.math.columbia.edu/tag/0AIC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isPresentingRing_of_hasAffineClosedImmersionCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCriterionPresentation.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCriterionPresentation.lean#L77). The attribute's comment: “(2) implies (1)”.

> **Stacks 0AIC, condition (2) implies condition (1).** If some morphism from an affine formal
> algebraic space `X` to an affine scheme turns every closed immersion of an affine scheme
> into `X` into a closed immersion, then `X` is presented by a weakly admissible topological ring:
> the inverse limit of the section rings of any presentation of `X` by affine thickenings.
>
> The stage rings are quotients of the sections of the given affine scheme, so that inverse limit
> is a ring in the universe of the schemes; its projections to the stage rings are surjective, and
> their kernels are weak ideals of definition forming a fundamental system of neighbourhoods of
> `0`.

```lean
theorem exists_isPresentingRing_of_hasAffineClosedImmersionCriterion
    {X : FppfSheaf B S hS} (hX : HasAffineClosedImmersionCriterionMapToSpec B S hS X) :
    ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
      (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

**`AlgebraicGeometry.FormalSpace.exists_isPresentingRing_of_hasSchemeClosedImmersionCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCriterionPresentation.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionCriterionPresentation.lean#L132). The attribute's comment: “(3) implies (1)”.

> **Stacks 0AIC, condition (3) implies condition (1).** The criterion for closed immersions of
> arbitrary schemes restricts to affine schemes, and then condition (2) gives condition (1).

```lean
theorem exists_isPresentingRing_of_hasSchemeClosedImmersionCriterion
    {X : FppfSheaf B S hS} (hX : HasSchemeClosedImmersionCriterionMapToSpec B S hS X) :
    ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
      (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

**`AlgebraicGeometry.FormalSpace.HasAffineClosedImmersionCriterion.hasSchemeClosedImmersionCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean#L268). The attribute's comment: “part (2) implies part (3)”.

> **Stacks 0AIC, condition (2) implies condition (3).** If some morphism from `X` to an affine
> scheme over `S` turns every closed immersion of an *affine* scheme into `X` into a closed
> immersion of schemes, then it does so for every *scheme* of the site: a scheme closed-immersed in
> an affine formal algebraic space is already affine.

```lean
theorem HasAffineClosedImmersionCriterion.hasSchemeClosedImmersionCriterion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : HasAffineClosedImmersionCriterion B S hS X) :
    HasSchemeClosedImmersionCriterion B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasAffineClosedImmersionCriterion.hasAllSurjectivePresentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean#L374). The attribute's comment: “part (2) implies part (5), and with it part (2) implies part (4). No hypothesis beyond condition (2) is carried. What remains open in this tag is the implication (4) implies (1) for a presentation indexed by an arbitrary directed type in Type (u + 1): the ring it asks for is the limit of the section rings of the presentation, which then lies in Type (u + 1) rather than Type u, so a smallness argument on the index is needed that this development does not have. The sequential case is exists\_quotientSystem\_formalSpectrum\_iso and the countably indexed case is isPresentingRing\_of\_isCountablyIndexed. The implication (1) implies (2) is open for the reason recorded in the implementation notes above: conditions (2) and (3) ask for an affine scheme over S, and the ring of a presentation carries structure morphisms only on its quotients”.

> **Stacks 0AIC, condition (2) implies condition (5).** Condition (2) is read on every
> presentation of `X` by affine thickenings at once, which is condition (5).

```lean
theorem HasAffineClosedImmersionCriterion.hasAllSurjectivePresentations
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : HasAffineClosedImmersionCriterion B S hS X) :
    HasAllSurjectivePresentations B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasAffineClosedImmersionCriterion.hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean#L387). The attribute's comment: “part (2) implies part (4)”.

> **Stacks 0AIC, condition (2) implies condition (4).** The presentation by affine thickenings
> that affineness of `X` supplies has surjective section-ring projections.

```lean
theorem HasAffineClosedImmersionCriterion.hasSomeSurjectivePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : HasAffineClosedImmersionCriterion B S hS X) :
    HasSomeSurjectivePresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasSchemeClosedImmersionCriterion.hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterion.lean#L396). The attribute's comment: “part (3) implies part (4)”.

> **Stacks 0AIC, condition (3) implies condition (4).** The criterion for all schemes
> of the site restricts to the affine ones, which is already enough.

```lean
theorem HasSchemeClosedImmersionCriterion.hasSomeSurjectivePresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : HasSchemeClosedImmersionCriterion B S hS X) :
    HasSomeSurjectivePresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasAffineClosedImmersionCriterionMapToSpec.hasAllSurjectivePresentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionPresentation.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionPresentation.lean#L160). The attribute's comment: “(2) implies (5)”.

> **Stacks 0AIC, condition (2) implies condition (5).** If some morphism from `X` to an affine
> scheme turns every closed immersion of an affine scheme into `X` into a closed immersion, then
> every presentation of `X` by affine thickenings has surjective section-ring projections.

```lean
theorem HasAffineClosedImmersionCriterionMapToSpec.hasAllSurjectivePresentations
    {X : FppfSheaf B S hS} (hX : HasAffineClosedImmersionCriterionMapToSpec B S hS X) :
    HasAllSurjectivePresentations B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasSchemeClosedImmersionCriterionMapToSpec.hasAllSurjectivePresentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionPresentation.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionPresentation.lean#L170). The attribute's comment: “(3) implies (5)”.

> **Stacks 0AIC, condition (3) implies condition (5).** The criterion for closed immersions of
> arbitrary schemes restricts to affine schemes, and then condition (2) gives condition (5).

```lean
theorem HasSchemeClosedImmersionCriterionMapToSpec.hasAllSurjectivePresentations
    {X : FppfSheaf B S hS} (hX : HasSchemeClosedImmersionCriterionMapToSpec B S hS X) :
    HasAllSurjectivePresentations B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasSchemeClosedImmersionCriterionMapToSpec.hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionPresentation.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionPresentation.lean#L179). The attribute's comment: “(3) implies (4)”.

> **Stacks 0AIC, condition (3) implies condition (4).** Every presentation of `X` by affine
> thickenings has surjective section-ring projections, and `X` has one.

```lean
theorem HasSchemeClosedImmersionCriterionMapToSpec.hasSomeSurjectivePresentation
    {X : FppfSheaf B S hS} (hX : HasSchemeClosedImmersionCriterionMapToSpec B S hS X) :
    HasSomeSurjectivePresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasAffineClosedImmersionCriterionMapToSpec.hasSchemeClosedImmersionCriterionMapToSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionSupplement.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanCriterionSupplement.lean#L28). The attribute's comment: “part (2) implies part (3)”.

> **Stacks 0AIC, condition (2) implies condition (3)**, for the conditions with the morphism
> to `Spec A` recorded as a `AlgebraicGeometry.FormalSpace.MapToScheme`. If some morphism from `X`
> to an affine scheme turns every closed immersion of an *affine* scheme into `X` into a closed
> immersion of schemes, then it does so for every *scheme* of the site: a scheme closed-immersed in
> an affine formal algebraic space is already affine.

```lean
theorem HasAffineClosedImmersionCriterionMapToSpec.hasSchemeClosedImmersionCriterionMapToSpec
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : HasAffineClosedImmersionCriterionMapToSpec B S hS X) :
    HasSchemeClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.HasSchemeClosedImmersionCriterionMapToSpec.hasAffineClosedImmersionCriterionMapToSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanSupplement.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillanSupplement.lean#L89). The attribute's comment: “(3) implies (2)”.

> **Stacks 0AIC, condition (3) implies condition (2)**, for the conditions with the morphism
> to `Spec A` recorded as a `AlgebraicGeometry.FormalSpace.MapToScheme`. The affine schemes of the
> site are among its schemes, so the criterion for all schemes restricts to them.

```lean
theorem HasSchemeClosedImmersionCriterionMapToSpec.hasAffineClosedImmersionCriterionMapToSpec
    {X : FppfSheaf B S hS} (hX : HasSchemeClosedImmersionCriterionMapToSpec B S hS X) :
    HasAffineClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.exists_continuous_ringEquiv_sections_of_weakIdealColimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/PresentingRingSectionLimit.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/PresentingRingSectionLimit.lean#L341). The attribute's comment: “the associated ring is A = lim Γ(X\_λ, 𝒪), with its limit topology, for an arbitrary presentation”.

> **Stacks 0AIC, the concluding clause.** If `X` is the colimit of the spectra of the
> quotients of a weakly admissible topological ring `A` by its weak ideals of definition, then for
> *any* presentation `X = colim Xᵢ` of `X` by affine thickenings the ring `A` is the inverse limit
> `lim Γ(Xᵢ, 𝒪)` of the section rings of that presentation, *as a topological ring*: the comparison
> map is an isomorphism of rings which is a homeomorphism for the limit topology of
> `AlgebraicGeometry.FormalSpace.topologicalSpaceSections`.
>
> Reduction modulo the weak ideals of definition `Jᵢ` cut out by the stages is the comparison
> homomorphism; it is injective because those ideals are cofinal and `A` is separated, surjective
> because `A` is complete, continuous because each `Jᵢ` is open, and open because the `Jᵢ` are
> cofinal.

```lean
theorem exists_continuous_ringEquiv_sections_of_weakIdealColimitPresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (A : Type u) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A) {X : FppfSheaf B S hS}
    (P : WeakIdealColimitPresentation B S hS A X)
    (I : Type (u + 1)) [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ BigAffineFppf B S hS)
    (hD : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      Stacks.Thickenings.IsThickening ((BigAffineFppf.toScheme B S hS).map (D.map f)))
    (eD : X ≅ colimit (D ⋙ BigAffineFppf.inclusion B S hS ⋙
      Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))) :
    ∃ e : A ≃+* (sectionDiagram B S hS D ⋙ forget CommRingCat.{u}).sections,
      Continuous e ∧ Continuous e.symm
```

**`AlgebraicGeometry.FormalSpace.exists_continuous_ringEquiv_of_isPresentingRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/PresentingRingUniqueness.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/PresentingRingUniqueness.lean#L332). The attribute's comment: “the associated ring of a McQuillan affine formal algebraic space is well defined: two rings presenting one affine formal algebraic space are isomorphic as topological rings”.

> **Stacks 0AIC: the presenting ring of a McQuillan affine formal algebraic space is unique
> up to isomorphism of topological rings.** If the weakly admissible topological rings `A` and
> `C` over `S` both present the affine formal algebraic space `X` — each exhibiting `X` as the
> colimit of the spectra of its quotients by weak ideals of definition — then `A` and `C` are
> isomorphic as topological rings.

```lean
theorem exists_continuous_ringEquiv_of_isPresentingRing {X : FppfSheaf B S hS}
    (hAX : IsPresentingRing B S hS A X) (hCX : IsPresentingRing B S hS C X) :
    ∃ φ : A ≃+* C, Continuous φ ∧ Continuous φ.symm
```

**`AlgebraicGeometry.FormalSpace.SequentialQuotients.exists_quotientSystem_formalSpectrum_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SectionLimitPresentation.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SectionLimitPresentation.lean#L359). The attribute's comment: “(4) implies (1), for a sequential presentation”.

> A sheaf presented as the colimit of a sequence of affine thickenings whose section rings are
> the quotients of a linearly topologized ring `A` by a fundamental system of weak ideals of
> definition is the formal spectrum of `A`.

```lean
theorem exists_quotientSystem_formalSpectrum_iso :
    ∃ Q : QuotientSystem B S hS A, Nonempty (X ≅ formalSpectrum Q)
```

**`AlgebraicGeometry.FormalSpace.SequentialQuotients.exists_quotientSystem_formalSpectrum_iso'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SectionLimitPresentationRefined.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SectionLimitPresentationRefined.lean#L79). The attribute's comment: “(4) implies (1), for a sequential presentation”.

> A sheaf presented as the colimit of a sequence of affine thickenings whose section rings are
> the quotients of a linearly topologized ring `A` by a fundamental system of weak ideals of
> definition is the formal spectrum of `A`.

```lean
theorem exists_quotientSystem_formalSpectrum_iso' (P : SequentialQuotients B S hS X A) :
    ∃ Q : QuotientSystem B S hS A, Nonempty (X ≅ formalSpectrum Q)
```

**`AlgebraicGeometry.FormalSpace.HasSomeSurjectivePresentation.hasAllSurjectivePresentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SectionsIndependentOfPresentation.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SectionsIndependentOfPresentation.lean#L619). The attribute's comment: “part (4) implies part (5)”.

> If *some* presentation of an affine formal algebraic space by affine thickenings has all its
> section-ring projections surjective, then *every* such presentation does.

```lean
public theorem HasSomeSurjectivePresentation.hasAllSurjectivePresentations
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : HasSomeSurjectivePresentation B S hS X) :
    HasAllSurjectivePresentations B S hS X
```

**`AlgebraicGeometry.FormalSpace.exists_isPresentingRing_of_hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean#L187). The attribute's comment: “(4) implies (1)”.

> **Stacks 0AIC, condition (4) implies condition (1).** An affine formal algebraic space with a
> presentation by affine thickenings whose section-ring projections are surjective is presented by
> a weakly admissible topological ring, namely the inverse limit of the section rings of that
> presentation.
>
> The presentation has only `u`-many stages up to isomorphism over `X`, so a polynomial ring on the
> sections of a `u`-small cofinal family of stages surjects compatibly onto every stage ring; the
> weakly admissible completion of that polynomial ring is the presenting ring.

```lean
theorem exists_isPresentingRing_of_hasSomeSurjectivePresentation
    {X : FppfSheaf B S hS} (hX : HasSomeSurjectivePresentation B S hS X) :
    ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
      (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

**`AlgebraicGeometry.FormalSpace.exists_isPresentingRing_of_hasAllSurjectivePresentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean#L239). The attribute's comment: “(5) implies (1)”.

> **Stacks 0AIC, condition (5) implies condition (1).** A presentation whose section-ring
> projections are all surjective exists as soon as every presentation has that property.

```lean
theorem exists_isPresentingRing_of_hasAllSurjectivePresentations
    {X : FppfSheaf B S hS} (hX : HasAllSurjectivePresentations B S hS X) :
    ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
      (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_iff_exists_isPresentingRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean#L253). The attribute's comment: “(1), (4) and (5) are equivalent”.

> **Stacks 0AIC, conditions (1), (4) and (5) are equivalent.** For an fppf sheaf satisfying the
> set-theoretic condition of Stacks 0AIS, being presented by a weakly admissible topological ring
> is the same as having one presentation by affine thickenings with surjective section-ring
> projections, and the same as having that property for every presentation. This is the form a
> consumer wants: McQuillan's condition and the existence of the presenting ring may be exchanged
> freely, with no ring and no structure morphism given in advance.

```lean
theorem hasSomeSurjectivePresentation_iff_exists_isPresentingRing
    {X : FppfSheaf B S hS} (hX : SatisfiesSetTheoreticCondition B S hS X) :
    HasSomeSurjectivePresentation B S hS X ↔
      ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
        (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

**`AlgebraicGeometry.FormalSpace.hasAllSurjectivePresentations_iff_exists_isPresentingRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SurjectivePresentationRing.lean#L265). The attribute's comment: “(1), (4) and (5) are equivalent”.

> **Stacks 0AIC, conditions (4) and (5) are equivalent to condition (1).** The statement above
> for the "every presentation" form of McQuillan's condition.

```lean
theorem hasAllSurjectivePresentations_iff_exists_isPresentingRing
    {X : FppfSheaf B S hS} (hX : SatisfiesSetTheoreticCondition B S hS X) :
    HasAllSurjectivePresentations B S hS X ↔
      ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
        (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

**`AlgebraicGeometry.FormalSpace.isThickening_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean#L507). The attribute's comment: “thickening\_classification”.

> Every weak ideal of definition gives a thickening of the formal space.

```lean
public theorem isThickening_quotient
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (J : WeakIdeals A) :
    (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)))
      (quotientMap B S hS A X P J)
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean#L538). The attribute's comment: “thickening\_classification”.

> Every weak ideal of definition gives a representable morphism from its
> quotient scheme to the formal space.

```lean
public theorem relativelyRepresentable_quotient
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (J : WeakIdeals A) :
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (quotientMap B S hS A X P J)
```

**`AlgebraicGeometry.FormalSpace.existsUnique_weakIdeal_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean#L547). The attribute's comment: “thickening\_classification”.

> Any representable thickening from a scheme into the formal space is,
> uniquely up to its weak ideal, a quotient stage of the canonical presentation.

```lean
public theorem existsUnique_weakIdeal_quotient
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (T : BigFppfOver B S hS)
    (f : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).obj T ⟶ X)
    (_hf_repr : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).relativelyRepresentable f)
    (hf_thick : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f) :
    ∃! J : WeakIdeals A,
      ∃ e : T ≅ (BigAffineFppf.inclusion B S hS).obj (P.diagram.obj J),
      (Sheaf.sheafifiedYoneda
          (BigFppfOver.topology B S hS)).map e.hom ≫
          quotientMap B S hS A X P J = f
```

**`AlgebraicGeometry.FormalSpace.inducedSectionHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean, line 712](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean#L712). The attribute's comment: “thickening\_classification”.

> The homomorphism on global sections induced by a representable thickening
> into the formal space. The uniqueness and compatibility statements below show
> that this construction does not depend on the chosen quotient description.

```lean
public noncomputable def inducedSectionHom
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (T : BigFppfOver B S hS)
    (f : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).obj T ⟶ X)
    (hf_repr : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).relativelyRepresentable f)
    (hf_thick : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f) :
    A →+* Γ((BigFppfOver.toScheme B S hS).obj T, ⊤)
```

**`AlgebraicGeometry.FormalSpace.inducedSectionHom_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean, line 734](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean#L734). The attribute's comment: “thickening\_classification”.

> At every quotient description compatible with the morphism to the formal
> space, the induced map on sections is the canonical quotient map followed by
> the affine global-sections isomorphism and transport to `T`.

```lean
public theorem inducedSectionHom_quotient
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (T : BigFppfOver B S hS)
    (f : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).obj T ⟶ X)
    (hf_repr : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).relativelyRepresentable f)
    (hf_thick : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (J : WeakIdeals A)
    (e : T ≅ (BigAffineFppf.inclusion B S hS).obj (P.diagram.obj J))
    (he : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).map e.hom ≫
        quotientMap B S hS A X P J = f) :
    inducedSectionHom B S hS A X P hA T f hf_repr hf_thick =
      sectionHomOfQuotientIso B S hS A X P J T e
```

**`AlgebraicGeometry.FormalSpace.quotient_ker_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean, line 777](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ThickeningClassification.lean#L777). The attribute's comment: “thickening\_classification”.

> The classifying ideal of a representable thickening is the kernel of the
> homomorphism from the associated ring to its global sections.

```lean
public theorem quotient_ker_sections
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (T : BigFppfOver B S hS)
    (f : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).obj T ⟶ X)
    (hf_repr : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).relativelyRepresentable f)
    (hf_thick : (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f)
    (J : WeakIdeals A)
    (e : T ≅ (BigAffineFppf.inclusion B S hS).obj (P.diagram.obj J))
    (he : (Sheaf.sheafifiedYoneda
      (BigFppfOver.topology B S hS)).map e.hom ≫
        quotientMap B S hS A X P J = f) :
    RingHom.ker (inducedSectionHom B S hS A X P hA T f hf_repr hf_thick) = J.1
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_toSpec_of_weakIdealColimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealClosedImmersionCriterion.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealClosedImmersionCriterion.lean#L84). The attribute's comment: “(1) implies (2)”.

> **Stacks 0AIC, condition (1) implies condition (2).** Let `A` be a weakly admissible
> topological ring and let the fppf sheaf `X`, satisfying the set-theoretic condition of
> Stacks 0AIS, be the colimit of the spectra of the quotients of `A` by its weak ideals of
> definition. Then `X` is an affine formal algebraic space, and every closed immersion of an
> affine scheme `T` of the site into `X` factors through the spectrum of a quotient `A ⧸ K` in
> such a way that the resulting morphism `T ⟶ Spec A` — which is the composition of `T ⟶ X` with
> the canonical `X ⟶ Spec A` — is a closed immersion of schemes.

```lean
theorem isClosedImmersion_toSpec_of_weakIdealColimitPresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (A : Type u) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A) {X : FppfSheaf B S hS}
    (hset : SatisfiesSetTheoreticCondition B S hS X)
    (P : WeakIdealColimitPresentation B S hS A X) :
    IsAffineFormalAlgebraicSpace B S hS X ∧
      ∀ (T : BigAffineFppf B S hS)
        (g : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj
            ((BigAffineFppf.inclusion B S hS).obj T) ⟶ X),
        IsClosedImmersionInto B S hS g →
        ∃ (K : WeakIdeals A) (c : T ⟶ P.diagram.obj K),
          (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map
              ((BigAffineFppf.inclusion B S hS).map c) ≫
            colimit.ι (P.diagram ⋙ BigAffineFppf.inclusion B S hS ⋙
              Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) K ≫ P.colimitIso.inv = g ∧
          IsClosedImmersion ((BigAffineFppf.toScheme B S hS).map c ≫
            (P.quotientIso K).hom ≫
              Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk K.1)))
```

**`AlgebraicGeometry.FormalSpace.hasAffineClosedImmersionCriterion_of_weakIdealColimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean#L336). The attribute's comment: “(1) implies (2)”.

> **Stacks 0AIC, condition (1) implies condition (2).** Let `A` be a weakly admissible
> topological ring and let the fppf sheaf `X`, satisfying the set-theoretic condition of
> Stacks 0AIS, be the colimit of the spectra of the quotients of `A` by its weak ideals of
> definition. Then `X` is an affine formal algebraic space, and there are a ring and a morphism of
> sheaves from `X` to its spectrum such that every closed immersion of an affine scheme of the
> site into `X` composes to a closed immersion of schemes; the witnesses are `A` itself and
> `AlgebraicGeometry.FormalSpace.weakIdealToSpecPoints`.
>
> This is the library's `AlgebraicGeometry.FormalSpace.HasAffineClosedImmersionCriterionMapToSpec`:
> the morphism to `Spec A` is given at every object of the site, not only at those carrying a closed
> immersion into `X`. The implication is unconditional — no morphism `Spec A ⟶ S` and no
> compatibility with the structure morphisms of the stages is assumed — because condition (2),
> like the source's, asks for none.

```lean
theorem hasAffineClosedImmersionCriterion_of_weakIdealColimitPresentation
    (hA : TopologicalRing.IsWeaklyAdmissible A) {X : FppfSheaf B S hS}
    (hset : SatisfiesSetTheoreticCondition B S hS X)
    (P : WeakIdealColimitPresentation B S hS A X) :
    HasAffineClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasSchemeClosedImmersionCriterion_of_weakIdealColimitPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean#L349). The attribute's comment: “(1) implies (3)”.

> **Stacks 0AIC, condition (1) implies condition (3).** Condition (1) gives condition (2), and
> a scheme closed-immersed in an affine formal algebraic space is affine, so the criterion extends
> from the affine schemes of the site to all of them.

```lean
theorem hasSchemeClosedImmersionCriterion_of_weakIdealColimitPresentation
    (hA : TopologicalRing.IsWeaklyAdmissible A) {X : FppfSheaf B S hS}
    (hset : SatisfiesSetTheoreticCondition B S hS X)
    (P : WeakIdealColimitPresentation B S hS A X) :
    HasSchemeClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasAffineClosedImmersionCriterion_of_hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean#L373). The attribute's comment: “(4) implies (2)”.

> **Stacks 0AIC, condition (4) implies condition (2).** An affine formal algebraic space with
> *some* presentation by affine thickenings whose section-ring projections are surjective admits a
> ring `A` and a morphism `X ⟶ Spec A` through which every closed immersion of an affine scheme of
> the site into `X` composes to a closed immersion of schemes.
>
> The ring is the one condition (4) produces, namely the inverse limit of the section rings of the
> presentation, and the morphism is the global family built above. No structure morphism
> `Spec A ⟶ S` is involved anywhere, which is what makes this arrow available: that limit carries
> none, so a condition (2) demanding one would have no arrow out of condition (4).

```lean
theorem hasAffineClosedImmersionCriterion_of_hasSomeSurjectivePresentation
    {X : FppfSheaf B S hS} (hX : HasSomeSurjectivePresentation B S hS X) :
    HasAffineClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasSchemeClosedImmersionCriterion_of_hasSomeSurjectivePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean#L388). The attribute's comment: “(4) implies (3)”.

> **Stacks 0AIC, condition (4) implies condition (3).** Condition (4) gives condition (2), and
> a scheme closed-immersed in an affine formal algebraic space is affine, so the criterion extends
> from the affine schemes of the site to all of them.

```lean
theorem hasSchemeClosedImmersionCriterion_of_hasSomeSurjectivePresentation
    {X : FppfSheaf B S hS} (hX : HasSomeSurjectivePresentation B S hS X) :
    HasSchemeClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasAffineClosedImmersionCriterion_of_hasAllSurjectivePresentations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealMapToSpec.lean#L398). The attribute's comment: “(5) implies (2)”.

> **Stacks 0AIC, condition (5) implies condition (2).** Condition (5) gives condition (4) by
> instantiating its quantifier at the presentation an affine formal algebraic space comes with,
> and condition (4) gives condition (2).

```lean
theorem hasAffineClosedImmersionCriterion_of_hasAllSurjectivePresentations
    {X : FppfSheaf B S hS} (hX : HasAllSurjectivePresentations B S hS X) :
    HasAffineClosedImmersionCriterionMapToSpec B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasAllSurjectivePresentations_of_exists_weaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealPresentation.lean, line 1410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealPresentation.lean#L1410). The attribute's comment: “(1) implies (5)”.

> **Stacks 0AIC, (1) ⇒ (5).** Condition (1) of Stacks 0AIC — the existence of a weakly
> admissible topological ring over `S` presenting `X` as the colimit of the spectra of its
> quotients by weak ideals of definition — implies condition (5): `X` is an affine formal
> algebraic space and *every* presentation of it by affine thickenings has surjective section-ring
> projections.

```lean
theorem hasAllSurjectivePresentations_of_exists_weaklyAdmissible
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) {X : FppfSheaf B S hS}
    (hX : SatisfiesSetTheoreticCondition B S hS X)
    (h : ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A)
        (_ : IsTopologicalRing A) (_ : IsLinearTopology A A),
      letI : CommRing A := ‹CommRing A›
      letI : TopologicalSpace A := ‹TopologicalSpace A›
      letI : IsTopologicalRing A := ‹IsTopologicalRing A›
      letI : IsLinearTopology A A := ‹IsLinearTopology A A›
      TopologicalRing.IsWeaklyAdmissible A ∧
        Nonempty (WeakIdealColimitPresentation B S hS A X)) :
    HasAllSurjectivePresentations B S hS X
```

## Tag 0AID, a definition

[Tag 0AID](https://stacks.math.columbia.edu/tag/0AID) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsClassical`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean#L84). The attribute's comment: “classical”.

> **Stacks 0AID (1).** A McQuillan affine formal algebraic space is *classical* when its
> associated weakly admissible topological ring is admissible, that is has an ideal of
> definition and is complete.

```lean
abbrev IsClassical (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsWeaklyAdic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean#L94). The attribute's comment: “weakly adic”.

> **Stacks 0AID (2).** A McQuillan affine formal algebraic space is *weakly adic* when its
> associated weakly admissible topological ring is weakly adic, that is the closed powers of a
> single ideal form a fundamental system of open ideals.

```lean
abbrev IsWeaklyAdic (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsAdic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean#L104). The attribute's comment: “adic”.

> **Stacks 0AID (3).** A McQuillan affine formal algebraic space is *adic* when its
> associated weakly admissible topological ring is adic, that is its topology is the adic
> topology of an ideal of definition and it is complete.

```lean
abbrev IsAdic (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsAdicStar`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean#L114). The attribute's comment: “adic star”.

> **Stacks 0AID (4).** A McQuillan affine formal algebraic space is *adic\** when its
> associated weakly admissible topological ring is adic and moreover has a finitely generated
> ideal of definition.

```lean
abbrev IsAdicStar (X : FppfSheaf B S hS) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsNoetherian`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean#L124). The attribute's comment: “Noetherian”.

> **Stacks 0AID (5).** A McQuillan affine formal algebraic space is *Noetherian* when its
> associated weakly admissible topological ring is both a Noetherian ring and adic.

```lean
abbrev IsNoetherian (X : FppfSheaf B S hS) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.FormalSpace.HasSomeSurjectivePresentation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/McQuillan.lean#L141), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean#L69) (StacksFrontier): “McQuillan”.

## Tag 0AIE, a remark

[Tag 0AIE](https://stacks.math.columbia.edu/tag/0AIE) in the Stacks Project.

**`AlgebraicGeometry.surjective_spfQuotientPointsColimitMap_app_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsAffine.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsAffine.lean#L390). The attribute's comment: “the comparison map of the colimit formula is surjective at an affine test scheme”.

> **Stacks 0AIE**, the affine case of the colimit formula. The comparison map
> `colim h_{Spec (A/I)} → h_{Spf A}` is surjective on the points over an affine scheme: such a
> point factors through one of the quotients by
> `AlgebraicGeometry.exists_factor_spfQuotientPointOn`.

```lean
theorem surjective_spfQuotientPointsColimitMap_app_of_isAffine (hA : IsAdmissible A)
    (T : Scheme.{u}) [IsAffine T] :
    Function.Surjective ((spfQuotientPointsColimitMap A hA).app (op T))
```

**`AlgebraicGeometry.isLocallySurjective_spfQuotientPointsColimitMap_of_isAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsAffine.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsAffine.lean#L414). The attribute's comment: “the comparison map of the colimit formula is locally surjective, with no hypothesis beyond admissibility”.

> **Stacks 0AIE**, the colimit formula, with no hypothesis beyond admissibility: the
> comparison map `colim h_{Spec (A/I)} → h_{Spf A}` is locally surjective for the Zariski
> topology. Together with
> `AlgebraicGeometry.isLocallyInjective_spfQuotientPointsColimitMap` this is the source's
> `h_{Spf A} = colim h_{Spec (A/I)}`, read — as it must be — as an isomorphism of the associated
> sheaves.
>
> This discharges the hypothesis of
> `AlgebraicGeometry.isLocallySurjective_spfQuotientPointsColimitMap`, which was the affine case,
> i.e. the surjectivity half of Stacks 0AHZ.

```lean
theorem isLocallySurjective_spfQuotientPointsColimitMap_of_isAdmissible (hA : IsAdmissible A) :
    Presheaf.IsLocallySurjective Scheme.zariskiTopology.{u}
      (spfQuotientPointsColimitMap A hA)
```

**`AlgebraicGeometry.spfQuotientPointsColimitMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean#L263). The attribute's comment: “the comparison map h\_colim → h\_Spf A of the colimit formula”.

> **Stacks 0AIE.** The comparison map of the source's colimit formula
> `h_{Spf A} = colim h_{Spec (A/I)}`: the morphism out of the colimit of the functors of points of
> the quotient spectra determined by the morphisms `Spec (A/I) → Spf A`.

```lean
noncomputable def spfQuotientPointsColimitMap [IsLinearTopology A A] (hA : IsAdmissible A) :
    colimit (spfQuotientPointsDiagram A) ⟶ formalSchemePoints (spfFormalScheme A hA)
```

**`AlgebraicGeometry.injective_spfQuotientPointsColimitMap_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean#L294). The attribute's comment: “the comparison map of the colimit formula is injective at every test scheme”.

> **Stacks 0AIE.** The comparison map of the colimit formula is injective on the points over
> every scheme: two morphisms `T → Spec (A/I)` and `T → Spec (A/J)` inducing the same point of
> `Spf A` already agree over `Spec (A/(I ∩ J))`.

```lean
theorem injective_spfQuotientPointsColimitMap_app [IsLinearTopology A A] (hA : IsAdmissible A)
    (T : Scheme.{u}) :
    Function.Injective ((spfQuotientPointsColimitMap A hA).app (op T))
```

**`AlgebraicGeometry.mono_spfQuotientPointsColimitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean#L351). The attribute's comment: “the comparison map of the colimit formula is a monomorphism of presheaves”.

> **Stacks 0AIE.** The colimit of the functors of points of the quotient spectra is a
> subfunctor of the functor of points of `Spf A`: the comparison map is a monomorphism of
> presheaves, being injective on the points over every scheme.

```lean
theorem mono_spfQuotientPointsColimitMap [IsLinearTopology A A] (hA : IsAdmissible A) :
    Mono (spfQuotientPointsColimitMap A hA)
```

**`AlgebraicGeometry.isLocallyInjective_spfQuotientPointsColimitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean#L361). The attribute's comment: “the comparison map of the colimit formula is locally injective”.

> **Stacks 0AIE.** The comparison map of the colimit formula is locally injective for the
> Zariski topology on schemes, being injective on the points over every scheme.

```lean
theorem isLocallyInjective_spfQuotientPointsColimitMap [IsLinearTopology A A]
    (hA : IsAdmissible A) :
    Presheaf.IsLocallyInjective Scheme.zariskiTopology.{u}
      (spfQuotientPointsColimitMap A hA)
```

**`AlgebraicGeometry.isLocallySurjective_spfQuotientPointsColimitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsColimit.lean#L380). The attribute's comment: “the colimit formula is locally surjective, assuming its affine case (the surjectivity half of Stacks 0AHZ)”.

> **Stacks 0AIE.** The reduction of the colimit formula to the affine case. If every point of
> `Spf A` over an affine scheme factors through one of the quotients `Spec (A/I)`, then the
> comparison map of the colimit formula is locally surjective for the Zariski topology, because
> every scheme has an affine open cover.
>
> The hypothesis is the surjectivity half of the identification
> `Mor(Spec B, Spf A) = Hom_cont(A, Γ(Spec B, 𝒪))` of Stacks 0AHZ. It is proved in
> `AlgebraicGeometry.exists_factor_spfQuotientPointOn`, so the conclusion holds with no hypothesis
> beyond admissibility; that is
> `AlgebraicGeometry.isLocallySurjective_spfQuotientPointsColimitMap_of_isAdmissible`.

```lean
theorem isLocallySurjective_spfQuotientPointsColimitMap [IsLinearTopology A A]
    (hA : IsAdmissible A)
    (haff : ∀ T : Scheme.{u}, IsAffine T →
      Function.Surjective ((spfQuotientPointsColimitMap A hA).app (op T))) :
    Presheaf.IsLocallySurjective Scheme.zariskiTopology.{u}
      (spfQuotientPointsColimitMap A hA)
```

**`AlgebraicGeometry.FormalSpace.isClassical_formalSchemePointsFppfSheaf_of_contains`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFormalSchemeEquivalence.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFormalSchemeEquivalence.lean#L368). The attribute's comment: “if the coproduct of the Spec(A/I) over the ideals of definition belongs to the site, then h\_X is a classical affine formal algebraic space”.

> **Stacks 0AIE.** Over a terminal base, the functor of points of an affine formal scheme
> `Spf A` is a classical affine formal algebraic space as soon as the coproduct of the schemes
> `Spec (A/I)`, over the ideals of definition of `A`, belongs to the big fppf site.

```lean
theorem isClassical_formalSchemePointsFppfSheaf_of_contains (hterm : IsTerminal S)
    (hA : TopologicalRing.IsAdmissible A) {X : FormalScheme.{u}} (e : X ≅ spfFormalScheme A hA)
    (hB : B.Contains (∐ fun I : IdealsOfDefinition A => Spec (spfQuotient A I))) :
    IsClassical B S hS (formalSchemePointsFppfSheaf B S hS X)
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_formalSchemePointsFppfSheaf_of_contains`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFormalSchemeEquivalence.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFormalSchemeEquivalence.lean#L382). The attribute's comment: “if the coproduct of the Spec(A/I) over the ideals of definition belongs to the site, then h\_X is an affine formal algebraic space”.

> **Stacks 0AIE.** Over a terminal base, the functor of points of an affine formal scheme
> `Spf A` is an affine formal algebraic space as soon as the coproduct of the schemes
> `Spec (A/I)`, over the ideals of definition of `A`, belongs to the big fppf site.

```lean
theorem isAffineFormalAlgebraicSpace_formalSchemePointsFppfSheaf_of_contains
    (hterm : IsTerminal S) (hA : TopologicalRing.IsAdmissible A) {X : FormalScheme.{u}}
    (e : X ≅ spfFormalScheme A hA)
    (hB : B.Contains (∐ fun I : IdealsOfDefinition A => Spec (spfQuotient A I))) :
    IsAffineFormalAlgebraicSpace B S hS (formalSchemePointsFppfSheaf B S hS X)
```

**`AlgebraicGeometry.FormalSpace.isEquivalence_smallAffineFormalSchemePointsFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFormalSchemeEquivalence.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineFormalSchemeEquivalence.lean#L460). The attribute's comment: “the category of affine formal schemes is equivalent to the category of classical affine formal algebraic spaces, by the functor of points”.

> **Stacks 0AIE**, the equivalence. Over a terminal base `S` (the source's `Spec(ℤ)`), the
> functor of points `𝔛 ↦ h_𝔛` is an equivalence from the category of affine formal schemes
> `Spf A` whose coproduct `∐_I Spec (A/I)` belongs to the big fppf site `B` (the source's
> "compatible choices of big site") to the category of classical affine formal algebraic spaces
> over `S`.

```lean
theorem isEquivalence_smallAffineFormalSchemePointsFunctor (hterm : IsTerminal S) :
    (smallAffineFormalSchemePointsFunctor B S hS hterm).IsEquivalence
```

**`AlgebraicGeometry.FormalSpace.isClassical_iff_exists_admissible_quotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClassicalCharacterization.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ClassicalCharacterization.lean#L94). The attribute's comment: “the objects: a sheaf is a classical affine formal algebraic space exactly when it is the formal spectrum of an admissible topological ring”.

> **Stacks 0AIE, the objects.** An fppf sheaf over `S` satisfying the set-theoretic condition
> of Stacks 0AIS is a *classical* affine formal algebraic space in the sense of Stacks 0AID (1)
> exactly when it is isomorphic to the formal spectrum of Stacks 0AIF of an admissible topological
> ring over `S`.
>
> This is the object half of the correspondence the source's remark describes, read on the
> formal-space side of the bridge: the classical affine formal algebraic spaces are the `Spf A`
> for `A` admissible, and nothing else. Both directions hold, with no hypothesis beyond the
> set-theoretic condition, which the left-hand side implies.
>
> The correspondence with affine formal *schemes*, and the equivalence of categories the source
> concludes with, need in addition the identification of the formal spectrum with the functor of
> points of `Spf A` and the full faithfulness of Stacks 0AI1; see the implementation notes of
> this file.

```lean
theorem isClassical_iff_exists_admissible_quotientSystem {X : FppfSheaf B S hS}
    (hX : SatisfiesSetTheoreticCondition B S hS X) :
    IsClassical B S hS X ↔
      ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
        (_ : IsLinearTopology A A),
        TopologicalRing.IsAdmissible A ∧
          ∃ D : QuotientSystem B S hS A, Nonempty (X ≅ formalSpectrum D)
```

**`AlgebraicGeometry.FormalSpace.final_idealOfDefinitionIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparison.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparison.lean#L196). The attribute's comment: “the ideals of definition are cofinal among the weak ideals of definition, so the colimit of the remark and the formal spectrum of Stacks 0AIF have the same index”.

> **Stacks 0AIE**, the index reconciliation. In a pre-admissible topological ring the ideals of
> definition are cofinal below the weak ideals of definition — the intersection of a weak ideal of
> definition with an ideal of definition is an ideal of definition — so the functor they induce on
> index categories is final, and colimits may be computed over either index.
>
> This is what reconciles the colimit of Stacks 0AIE, taken over the ideals of definition of an
> admissible ring, with the formal spectrum of Stacks 0AIF, taken over the weak ideals of
> definition.

```lean
theorem final_idealOfDefinitionIndex (hA : TopologicalRing.IsPreAdmissible A) :
    (idealOfDefinitionIndex A).monotone.functor.Final
```

**`AlgebraicGeometry.FormalSpace.QuotientSystem.formalSpectrumIsoIdealOfDefinitionColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparison.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparison.lean#L225). The attribute's comment: “the colimit over the ideals of definition is the formal spectrum of Stacks 0AIF”.

> **Stacks 0AIE**, the colimit of the remark. The colimit of the represented quotient spectra
> over the *ideals of definition* of a pre-admissible topological ring is the formal spectrum of
> Stacks 0AIF, whose colimit runs over the *weak* ideals of definition. The two indices have the
> same colimit by `AlgebraicGeometry.FormalSpace.final_idealOfDefinitionIndex`.

```lean
def QuotientSystem.formalSpectrumIsoIdealOfDefinitionColimit
    (hA : TopologicalRing.IsPreAdmissible A) (D : QuotientSystem B S hS A) :
    colimit D.idealOfDefinitionDiagram ≅ formalSpectrum D
```

**`AlgebraicGeometry.FormalSpace.isIso_spfFormalSchemeFppfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparisonIso.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparisonIso.lean#L406). The attribute's comment: “h\_\{Spf A} = colim h\_\{Spec (A/I)} as fppf sheaves: the comparison morphism from the formal spectrum to the functor of points of the affine formal scheme is an isomorphism”.

> **Stacks 0AIE, the colimit formula.** The comparison morphism from the formal spectrum of an
> admissible topological ring `A` over a terminal base to the functor of points of the affine
> formal scheme `Spf A` is an isomorphism of fppf sheaves over `S`.

```lean
theorem isIso_spfFormalSchemeFppfComparison (hterm : IsTerminal S)
    (hA : TopologicalRing.IsAdmissible A) (D : QuotientSystem B S hS A) :
    IsIso (spfFormalSchemeFppfComparison hA D)
```

**`AlgebraicGeometry.FormalSpace.isClassical_formalSchemePointsFppfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparisonIso.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparisonIso.lean#L446). The attribute's comment: “the functor of points of an affine formal scheme over a terminal base is a classical affine formal algebraic space”.

> **Stacks 0AIE, the type of the functor of points.** The functor of points of the affine
> formal scheme `Spf A` of an admissible topological ring `A` over a terminal base is a
> *classical* affine formal algebraic space over `S` in the sense of Stacks 0AID (1).
>
> Nothing is assumed beyond admissibility of `A` and the source's own size conditions: that the
> quotient spectra lie in the chosen big fppf site, which is part of the datum of a quotient
> system, and that their coproduct does, which is
> `AlgebraicGeometry.FormalSpace.QuotientSystem.HasLargeSite`. The fppf sheaf condition on the
> functor of points is `AlgebraicGeometry.FormalSpace.isFppfSheafFormalSchemePoints_formalScheme`
> and the identification with the formal spectrum is
> `AlgebraicGeometry.FormalSpace.isIso_spfFormalSchemeFppfComparison`.

```lean
theorem isClassical_formalSchemePointsFppfSheaf (hterm : IsTerminal S)
    (hA : TopologicalRing.IsAdmissible A) (D : QuotientSystem B S hS A)
    (hB : D.HasLargeSite) :
    IsClassical B S hS (formalSchemePointsFppfSheaf B S hS (spfFormalScheme A hA))
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_formalSchemePointsFppfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparisonIso.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeSpectrumComparisonIso.lean#L458). The attribute's comment: “the functor of points of an affine formal scheme over a terminal base is an affine formal algebraic space”.

> **Stacks 0AIE.** The functor of points of an affine formal scheme over a terminal base is an
> affine formal algebraic space over `S`; it is the affineness half of
> `AlgebraicGeometry.FormalSpace.isClassical_formalSchemePointsFppfSheaf`.

```lean
theorem isAffineFormalAlgebraicSpace_formalSchemePointsFppfSheaf (hterm : IsTerminal S)
    (hA : TopologicalRing.IsAdmissible A) (D : QuotientSystem B S hS A)
    (hB : D.HasLargeSite) :
    IsAffineFormalAlgebraicSpace B S hS
      (formalSchemePointsFppfSheaf B S hS (spfFormalScheme A hA))
```

**`AlgebraicGeometry.FormalSpace.isClassical_formalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumClassical.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrumClassical.lean#L137). The attribute's comment: “the formal spectrum of an admissible topological ring is a classical affine formal algebraic space”.

> **Stacks 0AIE.** Let `A` be an admissible topological ring over `S`. If the coproduct of the
> spectra of the quotients of `A` by its weak ideals of definition lies in the chosen big fppf
> site, then the formal spectrum `Spf A` is a *classical* affine formal algebraic space over `S`
> in the sense of Stacks 0AID (1).
>
> This is the second conclusion of the source's remark, for the object its colimit formula
> produces. The size hypothesis is the source's own: the source needs the coproduct of the
> quotient spectra to lie in the chosen big fppf site, which is what supplies the representable
> atlas demanded by the set-theoretic condition of Stacks 0AIS. The source's colimit runs over the
> ideals of definition of `A` and this one over its weak ideals of definition; the two agree,
> because in a pre-admissible ring the ideals of definition are cofinal below the weak ideals of
> definition (`TopologicalRing.exists_isIdealOfDefinition_le_of_isWeakIdealOfDefinition`).
>
> Only this direction holds: see the implementation notes of this file.

```lean
theorem isClassical_formalSpectrum (hA : TopologicalRing.IsAdmissible A)
    (D : QuotientSystem B S hS A) (hB : D.HasLargeSite) :
    IsClassical B S hS (formalSpectrum D)
```

## Tag 0AIF, a definition

[Tag 0AIF](https://stacks.math.columbia.edu/tag/0AIF) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.formalSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean#L260). The attribute's comment: “construction”.

> The formal spectrum of a weakly admissible topological ring over `S`: the
> fppf-sheaf colimit of its quotient spectra by weak ideals of definition.

```lean
public def formalSpectrum (D : QuotientSystem B S hS A) :
    Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_formalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean#L385). The attribute's comment: “affine formal algebraic space”.

> The formal spectrum is affine as a formal algebraic space over the base.

```lean
public theorem isAffineFormalAlgebraicSpace_formalSpectrum
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (D : QuotientSystem B S hS A) (hB : D.HasLargeSite) :
    IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D)
```

**`AlgebraicGeometry.FormalSpace.existsUnique_formalSpectrumMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean, line 786](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean#L786). The attribute's comment: “quotient-stage characterization”.

> The map of formal spectra is uniquely characterized by its effect on every
> quotient stage. This is the universal-property construction of `Spf(f)`.

```lean
public theorem existsUnique_formalSpectrumMap
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C}
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (f : ContinuousHom D E) :
    ∃! φ : formalSpectrum E ⟶ formalSpectrum D,
      ∀ (J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I })
        (K : { I : Ideal C // TopologicalRing.IsWeakIdealOfDefinition I })
        (h : J.1 ≤ Ideal.comap f.toRingHom K.1),
        formalSpectrumInclusion E (OrderDual.toDual K) ≫ φ =
          (Sheaf.sheafifiedYoneda
            (BigFppfOver.topology B S hS)).map
              ((BigAffineFppf.inclusion B S hS).map
                (f.stageMap J K h)) ≫
        formalSpectrumInclusion D (OrderDual.toDual J)
```

**`AlgebraicGeometry.FormalSpace.formalSpectrumMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean#L814). The attribute's comment: “functorial map”.

> The canonical contravariant map on formal spectra.

```lean
public noncomputable def formalSpectrumMap
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C}
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (f : ContinuousHom D E) : formalSpectrum E ⟶ formalSpectrum D
```

**`AlgebraicGeometry.FormalSpace.formalSpectrumMap_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean, line 840](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean#L840). The attribute's comment: “identity law”.

> The formal-spectrum map of the identity homomorphism is the identity.

```lean
public theorem formalSpectrumMap_id
    {D : QuotientSystem B S hS A}
    [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (f : ContinuousHom D D) (hf : f.toRingHom = RingHom.id A) :
    formalSpectrumMap hA f = 𝟙 (formalSpectrum D)
```

**`AlgebraicGeometry.FormalSpace.formalSpectrumMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean, line 876](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSpectrum.lean#L876). The attribute's comment: “composition law”.

> Formal spectrum reverses composition of continuous maps over the base.

```lean
public theorem formalSpectrumMap_comp
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C}
    {G : Type u} [CommRing G] [TopologicalSpace G]
    {F : QuotientSystem B S hS G}
    [IsTopologicalRing A] [IsLinearTopology A A]
    [IsTopologicalRing C] [IsLinearTopology C C]
    (hA : TopologicalRing.IsWeaklyAdmissible A)
    (hC : TopologicalRing.IsWeaklyAdmissible C)
    (f : ContinuousHom D E) (g : ContinuousHom E F)
    (gf : ContinuousHom D F)
    (hgf : gf.toRingHom = g.toRingHom.comp f.toRingHom) :
    formalSpectrumMap hC g ≫ formalSpectrumMap hA f =
      formalSpectrumMap hA gf
```

**`AlgebraicGeometry.FormalSpace.formalSpectrumMap_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatComposition.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatComposition.lean#L181). The attribute's comment: “composition law for the composite continuous hom”.

> **Stacks 0AIF.** The formal spectrum turns `ContinuousHom.comp` into composition of
> morphisms of formal spectra, in the direction that reverses the order.

```lean
theorem formalSpectrumMap_comp_eq (hw₂ : TopologicalRing.IsWeaklyAdmissible A₂)
    (hw₃ : TopologicalRing.IsWeaklyAdmissible A₃)
    (q : ContinuousHom D₂ D₁) (r : ContinuousHom D₃ D₂) :
    formalSpectrumMap hw₂ q ≫ formalSpectrumMap hw₃ r =
      formalSpectrumMap hw₃ (ContinuousHom.comp hw₂ hw₃ q r)
```

## Tag 0AN0, a lemma

[Tag 0AN0](https://stacks.math.columbia.edu/tag/0AN0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_continuous_ringEquiv_of_formalSpectrum_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/PresentingRingUniqueness.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/PresentingRingUniqueness.lean#L299). The attribute's comment: “the isomorphism of topological rings underlying an isomorphism of formal spectra, from the existence and uniqueness of the two continuous homomorphisms”.

> **Stacks 0AN0, applied in both directions.** An isomorphism of the formal spectra of two
> weakly admissible topological rings over `S` is the formal spectrum of a ring equivalence
> which is continuous in both directions. Each direction of the isomorphism is `Spf` of a unique
> continuous ring map over `S`, and each composite is a continuous ring map over `S` whose formal
> spectrum is the identity, hence by uniqueness is the identity ring map. The equivalence is the
> one those two ring maps make: its two directions are `g` and `g'`, whose formal spectra are the
> two directions of the given isomorphism.

```lean
theorem exists_continuous_ringEquiv_of_formalSpectrum_iso
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C}
    (e : formalSpectrum E ≅ formalSpectrum D) :
    ∃ (g : ContinuousHom D E) (g' : ContinuousHom E D) (φ : A ≃+* C),
      formalSpectrumMap hA g = e.hom ∧ formalSpectrumMap hC g' = e.inv ∧
        ⇑φ = ⇑g.toRingHom ∧ ⇑φ.symm = ⇑g'.toRingHom ∧
          Continuous φ ∧ Continuous φ.symm
```

**`AlgebraicGeometry.FormalSpace.existsUnique_continuousHom_formalSpectrumMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFullyFaithful.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/SpectrumFullyFaithful.lean#L549). References: EGA I (10.4.6), “X affine formal”.

> **Stacks 0AN0.** Let `A` and `C` be weakly admissible topological rings over `S`. Every
> morphism `f : Spf C ⟶ Spf A` of affine formal algebraic spaces over `S` is `Spf (f^♯)` for a
> unique continuous ring map `f^♯ : A → C` over `S`.

```lean
theorem existsUnique_continuousHom_formalSpectrumMap_eq
    (hA : TopologicalRing.IsWeaklyAdmissible A) (hC : TopologicalRing.IsWeaklyAdmissible C)
    {D : QuotientSystem B S hS A} {E : QuotientSystem B S hS C}
    (f : formalSpectrum E ⟶ formalSpectrum D) :
    ∃! g : ContinuousHom D E, formalSpectrumMap hA g = f
```

## Tag 0AIG, a lemma

[Tag 0AIG](https://stacks.math.columbia.edu/tag/0AIG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_of_isAffineFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/QuasiFiniteRepresentable.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/QuasiFiniteRepresentable.lean#L331).

> Let `S` be a scheme contained in a big fppf site `B` and let
> `f : X ⟶ Y` be a morphism of presheaves on the big fppf site of `S`. If `X` is an affine
> formal algebraic space and `f` is representable by algebraic spaces and locally quasi-finite,
> then `f` is representable by schemes.
>
> `X` is a sheaf of `Type u`, the universe of the schemes, and the hypothesis that it is an
> affine formal algebraic space is imposed on the sheaf obtained from it by lifting its values
> one universe up. Local quasi-finiteness of a morphism which is only representable by
> algebraic spaces is the assertion that each of its base changes along a scheme-valued point
> of the target, an algebraic space over `S`, is locally quasi-finite over that point.

```lean
theorem relativelyRepresentable_of_isAffineFormalAlgebraicSpace
    (X : Sheaf (BigFppfOver.topology B S hS) (Type u))
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : X.1 ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS
      ((presheafToSheaf (BigFppfOver.topology B S hS) (Type (u + 1))).obj
        (X.1 ⋙ uliftFunctor.{u + 1, u})))
    (hf : Space.IsRepresentableByAlgebraicSpaces B S hS f)
    (hlqf : ∀ (T : BigFppfOver B S hS) (ξ : yoneda.obj T ⟶ Y),
      Space.IsLocallyQuasiFinite B S hS (pullback.fst ξ f)) :
    yoneda.relativelyRepresentable f
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_of_isAffineFormalAlgebraicSpaceULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/QuasiFiniteRepresentableULift.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/QuasiFiniteRepresentableULift.lean#L112). The attribute's comment: “the tag read at the value universe Type (u+1), where a formal algebraic space and the affine formal algebraic spaces of its atlas of Definition 0AIM live, so that the tag applies to an atlas member. Nothing is assumed beyond the Type u reading: the smallness that one asks of its affine formal algebraic space is supplied by the set-theoretic condition of Stacks 0AIS, which an affine formal algebraic space carries, and the smallness of the base change by its being an algebraic space”.

> Let `S` be a scheme contained in a big fppf site `B`, let `X` be an affine formal algebraic
> space over `S` and let `f : X ⟶ Y` be a morphism to a presheaf of `Type (u + 1)` on the big fppf
> site of `S` which is representable by algebraic spaces and whose represented base changes are
> locally quasi-finite. Then `f` is representable by objects of the site.

```lean
theorem relativelyRepresentable_of_isAffineFormalAlgebraicSpaceULift
    {X : FppfSheaf B S hS} {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)} (f : X.obj ⟶ Y)
    (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hf : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f)
    (hlqf : ∀ (T : BigFppfOver B S hS) (ξ : uliftYoneda.{u + 1}.obj T ⟶ Y),
      Space.HoldsOnEveryEtaleChartULift.{u + 1} B S hS
        ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
          (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
        (pullback.fst ξ f)) :
    uliftYoneda.{u + 1}.relativelyRepresentable f
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_of_isEtale_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AtlasChartRepresentable.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AtlasChartRepresentable.lean#L49). The attribute's comment: “the case of an etale morphism, at the value universe Type (u+1) where a formal algebraic space and the affine formal algebraic spaces of its atlas of Definition 0AIM live. Nothing is assumed beyond the tag: an etale morphism of schemes is locally of finite type and locally quasi-finite by Stacks 03WS, which is the tag's hypothesis”.

> A morphism `g : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose source is an affine
> formal algebraic space, which is representable by algebraic spaces and étale, is representable by
> objects of the site.

```lean
theorem relativelyRepresentable_of_isEtale_of_isAffineFormal {X Y : FppfSheaf B S hS}
    (g : X ⟶ Y) (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS g.hom)
    (het : Space.HasPropertyULift.{u + 1} B S hS
      (fun _ _ k ↦ Space.IsEtaleULift.{u + 1} B S hS k.hom) g.hom hrep) :
    uliftYoneda.{u + 1}.relativelyRepresentable g.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.9, Tag 0AI6](https://stacks.math.columbia.edu/tag/0AI6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
