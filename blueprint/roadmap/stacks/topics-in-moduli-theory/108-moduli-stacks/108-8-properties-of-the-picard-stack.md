---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.picardRelativeDiagonal_affine_finitePresentation, AlgebraicGeometry.Space.PicardOverBase.quasiSeparated_limitPreservingOnObjects_picardToBase, AlgebraicGeometry.Space.liftedValuativeCriterionExistence_picardToBase, AlgebraicGeometry.Space.picardInertiaEquivalenceOverMultiplicativeGroupProduct, AlgebraicGeometry.Space.isSmooth_picardStructureMorphism
statement: formalized
proof: formalized
---

# 108.8 Properties of the Picard stack

Section 108.8 of the Stacks Project, [Tag 0DM9](https://stacks.math.columbia.edu/tag/0DM9). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DMA, a lemma

[Tag 0DMA](https://stacks.math.columbia.edu/tag/0DMA) in the Stacks Project.

**`AlgebraicGeometry.Space.picardRelativeDiagonal_affine_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackDiagonal.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackDiagonal.lean#L167).

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is flat, proper and of finite
> presentation (finite presentation is part of the standing data `D`). The diagonal of
> `Picardstack_{X/B}` over `B` is affine and of finite presentation: the relative diagonal of the
> structure morphism `Picardstack_{X/B} ⟶ 𝒮_B` is representable by algebraic spaces (Stacks 02ZW),
> and every algebraic space representing one of its base changes along a scheme-valued point over
> `U` is affine and of finite presentation over `U` (Properties of Stacks, Section 04XB).

```lean
theorem picardRelativeDiagonal_affine_finitePresentation
    (D : CoherentSituation B S hS) (hflat : IsFlat B S hS D.f.hom)
    (hproper : IsProper B S hS D.f.hom) :
    letI π := picardToBase (modulePushforwardCoherence B S hS) D.toPicardSituation
    ∃ _hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS
        (Stack.relativeDiagonal.{u, u + 1, u + 1} B S hS _ _ π).hom,
      ∀ (U : BigFppfOver B S hS)
        (z : BigFppfOver B U.left.1 U.left.2 ⥤
          (Stack.twoFibreProduct B S hS (baseCFG D.Y) _ _ π.hom π.hom).val.obj)
        (_hz : z ⋙ (Stack.twoFibreProduct B S hS (baseCFG D.Y) _ _ π.hom π.hom).val.p =
          Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom)
            (picardCFG (modulePushforwardCoherence B S hS) D.toPicardSituation).val.p
            (Stack.twoFibreProduct B S hS (baseCFG D.Y) _ _ π.hom π.hom).val.p z
            (CatFiberedInGroupoids.homFunctor
              (Stack.relativeDiagonal.{u, u + 1, u + 1} B S hS _ _ π)))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        IsAffineHom B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom ∧
          IsFinitePresentation B S hS (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

## Tag 0DMB, a lemma

[Tag 0DMB](https://stacks.math.columbia.edu/tag/0DMB) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardOverBase.quasiSeparated_limitPreservingOnObjects_picardToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackQuasiSeparatedLimitPreserving.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackQuasiSeparatedLimitPreserving.lean#L63). The attribute's comment: “quasi-separated: the relative diagonal is representable by algebraic spaces, quasi-compact and quasi-separated; locally of finite presentation: limit preserving on objects”.

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is flat, proper and of finite
> presentation. Then the structure morphism `Picardstack_{X/B} ⟶ 𝒮_B` is quasi-separated, i.e. its
> relative diagonal is representable by algebraic spaces, quasi-compact and quasi-separated
> (Stacks 04YW, 04XB), and locally of finite presentation in the sense of categories fibred in
> groupoids, i.e. limit preserving on objects (Stacks 06CU; for a 1-morphism of algebraic stacks
> this is local finite presentation, Stacks 0CMY).

```lean
theorem quasiSeparated_limitPreservingOnObjects_picardToBase
    (s : PicardSituation B S hS) (hfp : IsFinitePresentation B S hS s.f.hom)
    (hflat : IsFlat B S hS s.f.hom) (hproper : IsProper B S hS s.f.hom) :
    (∃ _ : Stack.IsRepresentableByAlgebraicSpaces B S hS
        (Stack.relativeDiagonal.{u, u + 1, u + 1} B S hS _ _
          (picardToBase (modulePushforwardCoherence B S hS) s)).hom,
      Stack.IsQuasiCompact B S hS
          (Stack.relativeDiagonal.{u, u + 1, u + 1} B S hS _ _
            (picardToBase (modulePushforwardCoherence B S hS) s)) ∧
        Stack.IsQuasiSeparated B S hS
          (Stack.relativeDiagonal.{u, u + 1, u + 1} B S hS _ _
            (picardToBase (modulePushforwardCoherence B S hS) s))) ∧
      BigFppfOver.IsLimitPreservingOnObjects.{u, u, u} B S hS _ _
        (picardToBase (modulePushforwardCoherence B S hS) s)
```

## Tag 0DNG, a lemma

[Tag 0DNG](https://stacks.math.columbia.edu/tag/0DNG) in the Stacks Project.

**`AlgebraicGeometry.Space.liftedValuativeCriterionExistence_picardToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackValuativeExistence.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackValuativeExistence.lean#L70).

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is proper, of finite
> presentation and smooth. Then the structure morphism `Picardstack_{X/B} ⟶ B` satisfies the
> existence part of the valuative criterion (Stacks 0CLK).

```lean
theorem liftedValuativeCriterionExistence_picardToBase (s : PicardSituation B S hS)
    (hfp : IsFinitePresentation B S hS s.f.hom) (hproper : IsProper B S hS s.f.hom)
    (hsmooth : IsSmooth B S hS s.f.hom) :
    Stack.LiftedValuativeCriterion.Existence.{u, u + 1} B S hS
      (picardToBase (modulePushforwardCoherence B S hS) s)
```

## Tag 0DNH, a lemma

[Tag 0DNH](https://stacks.math.columbia.edu/tag/0DNH) in the Stacks Project.

**`AlgebraicGeometry.Space.picardInertiaEquivalenceOverMultiplicativeGroupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean, line 828](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackInertia.lean#L828). The attribute's comment: “the inertia stack of the Picard stack is 𝐆\_\{m,S} ×\_S Picardstack\_\{X/B}, as categories over the big fppf site, when 𝒪\_T ⟶ f\_\{T,*}𝒪\_\{X\_T} is an isomorphism for every scheme T over the base”.

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S`, and assume that
> for every scheme `T` over `B` the structure map `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` of the base change
> `f_T : X_T ⟶ T` is an isomorphism.  Then the inertia stack of the Picard stack
> `Picardstack_{X/B}` of Section 0372 is equal to `𝐆_{m, S} ×_S Picardstack_{X/B}`: this is an
> equivalence of the two over `(Sch/S)_fppf`, which is the identity on the
> `Picardstack_{X/B}`-factor and sends a point `(L, α)` of the inertia over `T` to the point of
> `𝐆_{m, S}(T) = H^0(T, 𝒪_T^*)` that the automorphism `α` of `L` is multiplication by.
>
> The hypothesis `h` reads the source's `f_{T, *}𝒪_{X_T} ≅ 𝒪_T`, as in Stacks 0375, as the
> canonical map `𝒪_T ⟶ f_{T, *}𝒪_{X_T}` being an isomorphism for every test scheme over the base.
> The category `Picardstack_{X/B}` is `AlgebraicGeometry.Space.picardCategoryData`, with the
> comparisons of inverse images of Stacks 03LU given by
> `AlgebraicGeometry.Space.modulePushforwardCoherence`. The standing assumptions of the section that
> `f` be flat, proper and of finite presentation are not needed.
>
> "Equal" is read as an equivalence *over the site*
> (`CategoryTheory.StacksRepresentableCFG.EquivalenceOver`), and the product is the 2-fibre product
> `CategoryTheory.inertiaPresheafProduct` of the category of elements of `𝐆_{m, S}` with
> `Picardstack_{X/B}` over the site.

```lean
def picardInertiaEquivalenceOverMultiplicativeGroupProduct (s : PicardSituation B S hS)
    (h : s.StructureSheafMapIso) :
    letI : Category.{u + 1} (PicardObject s) :=
      (picardCategoryData (modulePushforwardCoherence B S hS) s).category
    StacksRepresentableCFG.EquivalenceOver
      (relativeInertiaStruct
        (picardCategoryData (modulePushforwardCoherence B S hS) s).siteProjection
        (picardCategoryData (modulePushforwardCoherence B S hS) s).siteProjection)
      (inertiaPresheafProductStruct
        (picardCategoryData (modulePushforwardCoherence B S hS) s).siteProjection
        (multiplicativeGroupPresheaf B S hS))
```

## Tag 0DPJ, a lemma

[Tag 0DPJ](https://stacks.math.columbia.edu/tag/0DPJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_picardStructureMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackSmoothRegistered.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/PicardStackSmoothRegistered.lean#L46). The attribute's comment: “the full statement: f flat (hflat), proper (hproper), of finite presentation (the field of D) and of relative dimension ≤ 1 (hd); Picardstack\_\{X/B} → B is smooth; the algebraicity of Picardstack\_\{X/B} is Stacks 0D04, proved, not assumed”.

> **Stacks 0DPJ: the Picard stack is smooth in relative dimension `≤ 1`.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S` which is flat, proper, of finite presentation (a field of the
> standing datum `D`) and of relative dimension `≤ 1`. Then the structure morphism
> `Picardstack_{X/Y} ⟶ Y` is smooth, as a 1-morphism of algebraic stacks; the Picard stack is
> algebraic by Stacks 0D04.

```lean
theorem isSmooth_picardStructureMorphism (D : CoherentSituation B S hS)
    (hflat : IsFlat B S hS D.f.hom) (hproper : IsProper B S hS D.f.hom)
    (hd : HasRelativeDimensionLE 1 B S hS D.f.hom) :
    Stack.AlgebraicStacks.IsSmooth B S hS
      (picardStructureMorphism D (isAlgebraicStack_picardCFG.{u, w} D hflat hproper))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.8, Tag 0DM9](https://stacks.math.columbia.edu/tag/0DM9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
