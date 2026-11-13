---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsCategoricalModuliSpace, AlgebraicGeometry.Stack.IsUniformCategoricalModuliSpace, AlgebraicGeometry.Stack.IsCategoricalModuliSpaceIn, AlgebraicGeometry.Stack.IsUniformCategoricalModuliSpaceIn, AlgebraicGeometry.Stack.quotientStackHomEquivInvariant, AlgebraicGeometry.Stack.quotientStackHomEquivInvariant_spec, AlgebraicGeometry.Stack.quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient, AlgebraicGeometry.Stack.quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient_prodLift
statement: formalized
proof: formalized
---

# 106.12 Moduli spaces

Section 106.12 of the Stacks Project, [Tag 0DUF](https://stacks.math.columbia.edu/tag/0DUF). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DUG, a definition

[Tag 0DUG](https://stacks.math.columbia.edu/tag/0DUG) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsCategoricalModuliSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean#L60). The attribute's comment: “part (1)”.

> A 1-morphism from a category fibred in groupoids to the
> category attached to an algebraic space `Y` is a *categorical moduli space* when every
> 1-morphism to the category attached to an algebraic space `W` factors through it by a unique
> morphism `Y ⟶ W` of algebraic spaces, the factorization holding up to an invertible
> 2-morphism.

```lean
abbrev IsCategoricalModuliSpace
    {𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (Y : AlgebraicSpaces B S hS)
    (f : 𝒳 ⟶ fibredCategory B S hS Y.obj) : Prop
```

**`AlgebraicGeometry.Stack.IsUniformCategoricalModuliSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean#L73). The attribute's comment: “part (2)”.

> A categorical moduli space is *uniform* when every base change of it along a flat morphism
> of algebraic spaces, given by any 2-fibre product of the cospan, is again a categorical moduli
> space.

```lean
abbrev IsUniformCategoricalModuliSpace
    {𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (Y : AlgebraicSpaces B S hS)
    (f : 𝒳 ⟶ fibredCategory B S hS Y.obj) : Prop
```

**`AlgebraicGeometry.Stack.IsCategoricalModuliSpaceIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean#L86). The attribute's comment: “part (3)”.

> The universal factorization property with the target algebraic spaces restricted to the full
> subcategory selected by the object predicate `C`, which `Y` is required to meet.

```lean
abbrev IsCategoricalModuliSpaceIn
    (C : AlgebraicSpaces B S hS → Prop)
    {𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (Y : AlgebraicSpaces B S hS)
    (f : 𝒳 ⟶ fibredCategory B S hS Y.obj) : Prop
```

**`AlgebraicGeometry.Stack.IsUniformCategoricalModuliSpaceIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CategoricalModuliSpace.lean#L101). The attribute's comment: “part (4)”.

> A categorical moduli space in the full subcategory selected by
> `C` is *uniform in* `C` when its base change along every flat morphism of that subcategory is
> again a categorical moduli space in `C`.

```lean
abbrev IsUniformCategoricalModuliSpaceIn
    (C : AlgebraicSpaces B S hS → Prop)
    {𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (Y : AlgebraicSpaces B S hS)
    (f : 𝒳 ⟶ fibredCategory B S hS Y.obj) : Prop
```

## Tag 0DUH, a lemma

[Tag 0DUH](https://stacks.math.columbia.edu/tag/0DUH) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStackHomEquivInvariant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/MorphismsToAlgebraicSpaces.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/MorphismsToAlgebraicSpaces.lean#L294).

> For a groupoid in algebraic spaces `(U, R, s, t, c)` over an algebraic space `B` over a scheme
> `S` of a big fppf site, and an algebraic space `Y` over `S`, the 1-morphisms `[U/R] ⟶ Y` of stacks
> over the big fppf site are in 1-to-1 correspondence with the `R`-invariant morphisms `U ⟶ Y`, by
> restriction along the projection `π : U ⟶ [U/R]` of Stacks 044R.

```lean
noncomputable def quotientStackHomEquivInvariant :
    (quotientStack G ⥤ᵇ (fibredCategory C S hS Y.obj).val) ≃
      {φ : G.objects ⟶ Y // Space.IsInvariant (Space.groupoidPreRelation G) φ.hom}
```

**`AlgebraicGeometry.Stack.quotientStackHomEquivInvariant_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/MorphismsToAlgebraicSpaces.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/MorphismsToAlgebraicSpaces.lean#L323). The attribute's comment: “the correspondence is restriction along the projection”.

> The correspondence is restriction along the projection: the 1-morphism `[U/R] ⟶ Y`
> corresponding to an `R`-invariant morphism `φ : U ⟶ Y` restricts along the projection
> `π : U ⟶ [U/R]` to the 1-morphism attached to `φ` by Stacks 0458.

```lean
theorem quotientStackHomEquivInvariant_spec
    (f : quotientStack G ⥤ᵇ (fibredCategory C S hS Y.obj).val) :
    BasedFunctor.comp (quotientStackProjection G) f =
      (associatedMap C S hS (quotientStackHomEquivInvariant G Y f).val.hom).1.hom
```

## Tag 0DUI, a lemma

[Tag 0DUI](https://stacks.math.columbia.edu/tag/0DUI) in the Stacks Project.

**`AlgebraicGeometry.Stack.quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackModuliSpace.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackModuliSpace.lean#L265). The attribute's comment: “the non-uniform case, for a groupoid over the terminal base as in the source”.

> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over a terminal base, let
> `j = (t, s)` be its pre-relation and let `f : [U/R] ⟶ Y` be a 1-morphism to the category attached
> to an algebraic space `Y`. Then `f` is a categorical moduli space exactly when its restriction
> `φ : U ⟶ Y` along the projection is a categorical quotient of `j`.

```lean
theorem quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient (hB : IsTerminal B)
    (hjt : (Space.PreRelation.target j).left = G.target)
    (hjs : (Space.PreRelation.source j).left = G.source)
    (Y : AlgebraicSpaces C S hS)
    (f : quotientStack G ⥤ᵇ (fibredCategory C S hS Y.obj).val) :
    IsBasedCategoricalModuliSpace Y f ↔
      Space.IsCategoricalQuotient j
        (Over.homMk (restrictedMorphism G f) (hB.hom_ext _ _) :
          (Over.mk G.objectsToBase : Over B) ⟶ Over.mk (hB.from Y))
```

**`AlgebraicGeometry.Stack.quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient_prodLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackModuliSpace.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackModuliSpace.lean#L284). The attribute's comment: “the non-uniform case at the pre-relation (t, s) the groupoid cuts out”.

> Let `G` be a groupoid in algebraic spaces over a terminal base and let `f : [U/R] ⟶ Y` be a
> 1-morphism to the category attached to an algebraic space `Y`. Then `f` is a categorical moduli
> space exactly when its restriction `φ : U ⟶ Y` along the projection is a categorical quotient of
> the pre-relation `prod.lift t s` of `G`.

```lean
theorem quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient_prodLift
    (hB : IsTerminal B) (G : GroupoidInAlgebraicSpaces C S hS B)
    (Y : AlgebraicSpaces C S hS)
    (f : quotientStack G ⥤ᵇ (fibredCategory C S hS Y.obj).val) :
    IsBasedCategoricalModuliSpace Y f ↔
      Space.IsCategoricalQuotient
        (prod.lift (Over.homMk G.target G.target_over) (Over.homMk G.source G.source_over) :
          Space.PreRelation (Over.mk G.arrowsToBase) (Over.mk G.objectsToBase))
        (Over.homMk (restrictedMorphism G f) (hB.hom_ext _ _) :
          (Over.mk G.objectsToBase : Over B) ⟶ Over.mk (hB.from Y))
```

**`AlgebraicGeometry.Stack.quotientStack_isCategoricalModuliSpaceIn_iff_isCategoricalQuotientIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackModuliSpace.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackModuliSpace.lean#L303). The attribute's comment: “the non-uniform case in a full subcategory, for a groupoid over the terminal base”.

> With the same data as
> `AlgebraicGeometry.Stack.quotientStack_isCategoricalModuliSpace_iff_isCategoricalQuotient` and a
> full subcategory of the algebraic spaces, selected by a predicate `P` on objects and containing
> the object and arrow spaces of the groupoid, `f` is a categorical moduli space in that
> subcategory exactly when `φ` is a categorical quotient in it.

```lean
theorem quotientStack_isCategoricalModuliSpaceIn_iff_isCategoricalQuotientIn (hB : IsTerminal B)
    (hjt : (Space.PreRelation.target j).left = G.target)
    (hjs : (Space.PreRelation.source j).left = G.source)
    (P : AlgebraicSpaces C S hS → Prop) (hR : P G.arrows) (hU : P G.objects)
    (Y : AlgebraicSpaces C S hS)
    (f : quotientStack G ⥤ᵇ (fibredCategory C S hS Y.obj).val) :
    IsBasedCategoricalModuliSpaceIn P Y f ↔
      Space.IsCategoricalQuotientIn (fun Z : Over B => P Z.left) j
        (Over.homMk (restrictedMorphism G f) (hB.hom_ext _ _) :
          (Over.mk G.objectsToBase : Over B) ⟶ Over.mk (hB.from Y))
```

**`AlgebraicGeometry.Stack.quotientStack_isUniformCategoricalModuliSpace_iff_isUniformCategoricalQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackUniformModuliSpace.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackUniformModuliSpace.lean#L558). The attribute's comment: “the uniform case, for a groupoid over the terminal base as in the source”.

> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over a terminal base, let
> `f : [U/R] ⟶ Y` be a 1-morphism to the category attached to an algebraic space `Y` and let
> `φ : U ⟶ Y` be its restriction along the projection of Stacks 044R. Then `f` is a *uniform*
> categorical moduli space exactly when `φ` is a *uniform* categorical quotient: for every flat
> `a : Y' ⟶ Y`, the base change `Y' ×_Y [U/R] ⟶ Y'` of `f` is a categorical moduli space exactly when
> the base-changed quotient map `U' ⟶ Y'` is a categorical quotient of the base-changed pre-relation
> `(t', s')`, for `U' = Y' ×_Y U` and `R' = Y' ×_Y R`.
>
> The base change is an arbitrary 2-fibre product of the cospan in the 2-category of stacks in
> groupoids of Stacks 02ZK.

```lean
theorem quotientStack_isUniformCategoricalModuliSpace_iff_isUniformCategoricalQuotient :
    (∀ (Y' : AlgebraicSpaces C S hS) (a : Y' ⟶ Y), Space.IsFlat C S hS a.hom →
        ∀ P : Bicategory.TwoCommSq
            (Bicategory.InducedBicategory.mkHom (BasedFunctor.comp f (liftedFibredCategoryUp Y)) :
              quotientStackAsStack G ⟶ spaceAsStack Y)
            (Bicategory.InducedBicategory.mkHom (liftedAssociatedMap a) :
              spaceAsStack Y' ⟶ spaceAsStack Y),
          Bicategory.IsTwoFibreProduct P →
            IsBasedCategoricalModuliSpace Y'
              (BasedFunctor.comp P.snd.hom (liftedFibredCategoryDown Y'))) ↔
      ∀ (Y' : AlgebraicSpaces C S hS) (a : Y' ⟶ Y), Space.IsFlat C S hS a.hom →
        Space.IsCategoricalQuotient
          (baseChangeSituationPreRelation hB G (restrictedMorphism G f)
            (restrictedMorphism_isInvariant G f) a)
          (baseChangeSituationQuotientMap hB G (restrictedMorphism G f)
            (restrictedMorphism_isInvariant G f) a)
```

**`AlgebraicGeometry.Stack.quotientStack_isUniformCategoricalModuliSpaceIn_iff_isUniformCategoricalQuotientIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackUniformModuliSpace.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackUniformModuliSpace.lean#L588). The attribute's comment: “variant: the uniform case in a full subcategory, over every flat Y' ⟶ Y and with the subcategory containing every base change of R and U; the tag is quotientStack\_isUniformModuliSpaceIn\_iff\_isUniformQuotientIn\_of\_isClosedUnderLimitsOfShape”.

> The uniform case in a full subcategory. With the same data as
> `quotientStack_isUniformCategoricalModuliSpace_iff_isUniformCategoricalQuotient` and a full
> subcategory of the algebraic spaces, selected by a predicate `Pr` on objects which contains the
> object and arrow spaces of every base change of the groupoid: for every flat `a : Y' ⟶ Y`, the base
> change `Y' ×_Y [U/R] ⟶ Y'` of `f` is a categorical moduli space in `Pr` exactly when the
> base-changed quotient map `U' ⟶ Y'` is a categorical quotient in `Pr` of the base-changed
> pre-relation `(t', s')`.

```lean
theorem quotientStack_isUniformCategoricalModuliSpaceIn_iff_isUniformCategoricalQuotientIn
    (Pr : AlgebraicSpaces C S hS → Prop)
    (hR : ∀ (Y' : AlgebraicSpaces C S hS) (a : Y' ⟶ Y),
      Pr (baseChangeSituationGroupoid hB G (restrictedMorphism G f)
        (restrictedMorphism_isInvariant G f) a).arrows)
    (hU : ∀ (Y' : AlgebraicSpaces C S hS) (a : Y' ⟶ Y),
      Pr (baseChangeSituationGroupoid hB G (restrictedMorphism G f)
        (restrictedMorphism_isInvariant G f) a).objects) :
    (∀ (Y' : AlgebraicSpaces C S hS) (a : Y' ⟶ Y), Space.IsFlat C S hS a.hom →
        ∀ P : Bicategory.TwoCommSq
            (Bicategory.InducedBicategory.mkHom (BasedFunctor.comp f (liftedFibredCategoryUp Y)) :
              quotientStackAsStack G ⟶ spaceAsStack Y)
            (Bicategory.InducedBicategory.mkHom (liftedAssociatedMap a) :
              spaceAsStack Y' ⟶ spaceAsStack Y),
          Bicategory.IsTwoFibreProduct P →
            IsBasedCategoricalModuliSpaceIn Pr Y'
              (BasedFunctor.comp P.snd.hom (liftedFibredCategoryDown Y'))) ↔
      ∀ (Y' : AlgebraicSpaces C S hS) (a : Y' ⟶ Y), Space.IsFlat C S hS a.hom →
        Space.IsCategoricalQuotientIn (fun Z : Over B => Pr Z.left)
          (baseChangeSituationPreRelation hB G (restrictedMorphism G f)
            (restrictedMorphism_isInvariant G f) a)
          (baseChangeSituationQuotientMap hB G (restrictedMorphism G f)
            (restrictedMorphism_isInvariant G f) a)
```

**`AlgebraicGeometry.Stack.quotientStack_isUniformModuliSpaceIn_iff_isUniformQuotientIn_of_isClosedUnderLimitsOfShape`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackUniformModuliSpace.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuotientStackUniformModuliSpace.lean#L626). The attribute's comment: “uniform, in a full subcategory”.

> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over a terminal base,
> `f : [U/R] ⟶ Y` a 1-morphism to the category attached to an algebraic space `Y`, and `φ : U ⟶ Y`
> its restriction along the projection of Stacks 044R. Let `Pr` be a full subcategory of the
> algebraic spaces which is closed under fibre products and contains `R` and `U`. Then `f` is a
> uniform categorical moduli space in `Pr` (Stacks 0DUG, part (4)) — `Y` lies in `Pr` and for every
> flat `a : Y' ⟶ Y` with `Y'` in `Pr` the base change `Y' ×_Y [U/R] ⟶ Y'` is a categorical moduli
> space in `Pr` — exactly when `φ` is a uniform categorical quotient in `Pr` (Stacks 048L, part (2))
> — `R`, `U` and `Y` lie in `Pr` and for every flat `a : Y' ⟶ Y` with `Y'` in `Pr` the base-changed
> quotient map `U' ⟶ Y'` is the categorical quotient in `Pr` of the base-changed pre-relation
> `(t', s')`, for `U' = Y' ×_Y U` and `R' = Y' ×_Y R`.

```lean
theorem quotientStack_isUniformModuliSpaceIn_iff_isUniformQuotientIn_of_isClosedUnderLimitsOfShape
    (Pr : ObjectProperty (AlgebraicSpaces C S hS)) [Pr.IsClosedUnderLimitsOfShape WalkingCospan]
    (hR : Pr G.arrows) (hU : Pr G.objects) :
    (Pr Y ∧ ∀ (Y' : AlgebraicSpaces C S hS), Pr Y' → ∀ (a : Y' ⟶ Y), Space.IsFlat C S hS a.hom →
        ∀ P : Bicategory.TwoCommSq
            (Bicategory.InducedBicategory.mkHom (BasedFunctor.comp f (liftedFibredCategoryUp Y)) :
              quotientStackAsStack G ⟶ spaceAsStack Y)
            (Bicategory.InducedBicategory.mkHom (liftedAssociatedMap a) :
              spaceAsStack Y' ⟶ spaceAsStack Y),
          Bicategory.IsTwoFibreProduct P →
            IsBasedCategoricalModuliSpaceIn Pr Y'
              (BasedFunctor.comp P.snd.hom (liftedFibredCategoryDown Y'))) ↔
      Pr G.arrows ∧ Pr G.objects ∧ Pr Y ∧
        ∀ (Y' : AlgebraicSpaces C S hS), Pr Y' → ∀ (a : Y' ⟶ Y), Space.IsFlat C S hS a.hom →
          Space.IsCategoricalQuotientIn (fun Z : Over B => Pr Z.left)
            (baseChangeSituationPreRelation hB G (restrictedMorphism G f)
              (restrictedMorphism_isInvariant G f) a)
            (baseChangeSituationQuotientMap hB G (restrictedMorphism G f)
              (restrictedMorphism_isInvariant G f) a)
```

## Tag 0DUJ, a lemma

[Tag 0DUJ](https://stacks.math.columbia.edu/tag/0DUJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUniformCategoricalModuliSpace_of_affineFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniformCategoricalModuliSpaceAffine.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/UniformCategoricalModuliSpaceAffine.lean#L330).

> **Stacks 0DUJ.** A 1-morphism from a category fibred in groupoids over the big fppf site of
> `S` to the category attached to an algebraic space `Y` is a *uniform* categorical moduli space as
> soon as every base change of it along a flat morphism to `Y` from an affine scheme is a
> categorical moduli space.
>
> The source states this for a 1-morphism from an algebraic stack; nothing of `𝒳` beyond being
> fibred in groupoids is used, so it is stated here at that generality.

```lean
theorem isUniformCategoricalModuliSpace_of_affineFlatBaseChange
    {𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (Y : AlgebraicSpaces B S hS) (f : 𝒳 ⟶ fibredCategory B S hS Y.obj)
    (h : ∀ T : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
      ∀ a : (schemeSpace T : AlgebraicSpaces B S hS) ⟶ Y,
        Space.IsFlat B S hS a.hom →
          ∀ P : Bicategory.TwoCommSq (associatedMap B S hS a.hom).1 f,
            Bicategory.IsTwoFibreProduct P →
              IsCategoricalModuliSpace B S hS
                (schemeSpace T : AlgebraicSpaces B S hS)
                P.fst) :
    IsUniformCategoricalModuliSpace B S hS Y f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.12, Tag 0DUF](https://stacks.math.columbia.edu/tag/0DUF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
