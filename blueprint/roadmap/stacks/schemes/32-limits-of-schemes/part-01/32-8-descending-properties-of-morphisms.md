---
declaration: section
origin: cited
lean: AlgebraicGeometry.MorphismLimitSituation, AlgebraicGeometry.exists_isAffineHom_of_isLimit, AlgebraicGeometry.exists_isFinite_baseChange_of_isLimit, AlgebraicGeometry.exists_unramified_baseChange_of_unramified_limitBaseChange, AlgebraicGeometry.exists_isClosedImmersion_baseChange_of_isLimit, AlgebraicGeometry.exists_isSeparated_baseChange_of_isLimit, AlgebraicGeometry.exists_flat_baseChange_of_limitBaseChange, AlgebraicGeometry.exists_isFiniteLocallyFree_baseChange_of_isLimit
statement: formalized
proof: formalized
---

# 32.8 Descending properties of morphisms

Section 32.8 of the Stacks Project, [Tag 081C](https://stacks.math.columbia.edu/tag/081C). 16 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 081D, a situation

[Tag 081D](https://stacks.math.columbia.edu/tag/081D) in the Stacks Project.

**`AlgebraicGeometry.MorphismLimitSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/LimitSituation.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/LimitSituation.lean#L58). The attribute's comment: “the base changes f\_i (i ≥ 0) and f are stageHom and limitHom; toMorphismDescentSituation restricts to the cofinal stages i ≥ 0, which are qcqs”.

> **Stacks 081D.** A directed inverse system `(S_i)` of schemes with affine transition
> morphisms, a chosen limit cone `S = lim S_i`, a chosen index `0`, and a morphism `f₀ : X₀ ⟶ Y₀` of
> schemes over `S₀`, where `S₀`, `X₀` and `Y₀` are quasi-compact and quasi-separated.

```lean
structure MorphismLimitSituation (I : Type v) [Preorder I] [IsDirected I (· ≤ ·)]
```

## Tag 01ZN, a lemma

[Tag 01ZN](https://stacks.math.columbia.edu/tag/01ZN) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineHom_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Affine.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Affine.lean#L177).

> If a morphism over one stage of a cofiltered inverse system becomes affine
> after base change to the limit, it becomes affine at some later stage.

```lean
theorem exists_isAffineHom_of_isLimit
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [IsAffineHom ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (hi : i ⟶ i₀),
      IsAffineHom ((Over.pullback (D.map hi)).map f₀).left
```

## Tag 01ZO, a lemma

[Tag 01ZO](https://stacks.math.columbia.edu/tag/01ZO) in the Stacks Project.

**`AlgebraicGeometry.exists_isFinite_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Finite.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Finite.lean#L327).

> **Stacks Project, Tag 01ZO.** If a morphism over a stage of a cofiltered inverse system is
> locally of finite type and its base change to the limit is finite, then its base change to some
> later stage is finite.

```lean
theorem exists_isFinite_baseChange_of_isLimit
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    [IsFinite ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (hi : i ⟶ i₀), IsFinite ((Over.pullback (D.map hi)).map f₀).left
```

## Tag 0C4W, a lemma

[Tag 0C4W](https://stacks.math.columbia.edu/tag/0C4W) in the Stacks Project.

**`AlgebraicGeometry.exists_unramified_baseChange_of_unramified_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Unramified.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Unramified.lean#L107).

> If a morphism over a stage of a cofiltered inverse system is locally of finite type and its
> base change to the limit is unramified, then its base change to some later stage is
> unramified.

```lean
theorem exists_unramified_baseChange_of_unramified_limitBaseChange
    {I : Type u} [Category.{u} I] (D : I ⥤ Scheme.{u}) (c : Cone D) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [IsCofiltered I]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    (hc : IsLimit c)
    [Unramified ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀),
      Unramified ((Over.pullback (D.map g)).map f₀).left
```

## Tag 01ZP, a lemma

[Tag 01ZP](https://stacks.math.columbia.edu/tag/01ZP) in the Stacks Project.

**`AlgebraicGeometry.exists_isClosedImmersion_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/ClosedImmersion.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/ClosedImmersion.lean#L406).

> If a morphism over a stage is locally of finite type and becomes a closed
> immersion over the inverse limit, it becomes a closed immersion at a later stage.

```lean
theorem exists_isClosedImmersion_baseChange_of_isLimit
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    [IsClosedImmersion ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (hi : i ⟶ i₀),
      IsClosedImmersion ((Over.pullback (D.map hi)).map f₀).left
```

## Tag 01ZQ, a lemma

[Tag 01ZQ](https://stacks.math.columbia.edu/tag/01ZQ) in the Stacks Project.

**`AlgebraicGeometry.exists_isSeparated_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Diagonal.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Diagonal.lean#L129).

> **Stacks Project, Tag 01ZQ.** If a morphism over a stage of a cofiltered inverse system is
> separated after base change to the limit, then it is separated after base change to some later
> stage.

```lean
theorem exists_isSeparated_baseChange_of_isLimit
    {I : Type v} [Category.{v} I] (D : I ⥤ Scheme.{u}) (c : Cone D) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [IsCofiltered I] [EssentiallySmall.{u} I]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    (hc : IsLimit c)
    [IsSeparated ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀), IsSeparated ((Over.pullback (D.map g)).map f₀).left
```

## Tag 04AI, a lemma

[Tag 04AI](https://stacks.math.columbia.edu/tag/04AI) in the Stacks Project.

**`AlgebraicGeometry.exists_flat_baseChange_of_limitBaseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Flat.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Flat.lean#L242).

> **Stacks Project, Tag 04AI.** A locally finitely presented morphism over a stage which
> becomes flat over the inverse limit is flat at some later stage.

```lean
lemma exists_flat_baseChange_of_limitBaseChange
    {I : Type v} [Category.{w} I] [EssentiallySmall.{u} I]
    (D : Functor I Scheme.{u}) (c : Cone D) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [IsCofiltered I]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    (hc : IsLimit c)
    [Flat ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀), Flat ((Over.pullback (D.map g)).map f₀).left
```

## Tag 06AC, a lemma

[Tag 06AC](https://stacks.math.columbia.edu/tag/06AC) in the Stacks Project.

**`AlgebraicGeometry.exists_isFiniteLocallyFree_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/FiniteLocallyFree.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/FiniteLocallyFree.lean#L68). The attribute's comment: “the plain statement; the degree-d refinement is exists\_isFiniteLocallyFreeOfRank\_baseChange\_of\_isLimit. Carries the essential smallness of the index category, a hypothesis of the inputs without which the statement is false and which the source, having no universe hierarchy, states implicitly by indexing on a directed set”.

> A morphism over a stage of a cofiltered inverse system of quasi-compact and quasi-separated
> schemes with affine transition morphisms, essentially small in the universe of the schemes, which
> is locally of finite presentation and whose base change to the limit is finite locally free, is
> finite locally free after base change to some later stage.

```lean
theorem exists_isFiniteLocallyFree_baseChange_of_isLimit
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    [Stacks.Morphisms.IsFiniteLocallyFree ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀),
      Stacks.Morphisms.IsFiniteLocallyFree ((Over.pullback (D.map g)).map f₀).left
```

**`AlgebraicGeometry.exists_isFiniteLocallyFreeOfRank_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/FiniteLocallyFree.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/FiniteLocallyFree.lean#L106). The attribute's comment: “the degree-d refinement. Narrower than the plain statement in the index universes: the objects and the morphisms of the index category are both in the universe of the schemes, which is the form in which the cofiltered Tag 05F4 used to descend the degree stratum along the system of base changes of Y₀ is available, that system being indexed by the over category, which inherits both universes. The plain statement's essential smallness is implied by this narrowing rather than assumed”.

> A morphism over a stage of a cofiltered inverse system of quasi-compact and quasi-separated
> schemes with affine transition morphisms, indexed in the universe of the schemes, which is locally
> of finite presentation and whose base change to the limit is finite locally free of degree `d`, is
> finite locally free of degree `d` after base change to some later stage.

```lean
theorem exists_isFiniteLocallyFreeOfRank_baseChange_of_isLimit
    {I : Type u} [Category.{u} I] [IsCofiltered I] (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀) (d : ℕ)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank
      ((Over.pullback (c.π.app i₀)).map f₀).left d] :
    ∃ (i : I) (g : i ⟶ i₀),
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank
        ((Over.pullback (D.map g)).map f₀).left d
```

**`AlgebraicGeometry.exists_isFiniteLocallyFreeOfRank_overPullbackObj_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/FiniteLocallyFreeRank.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/FiniteLocallyFreeRank.lean#L142). The attribute's comment: “the fixed-degree refinement, for a morphism whose target is the stage itself”.

> **Stacks Project, Tag 06AC, fixed-degree form, for the structure morphism of an object over a
> stage.** Let `D` be a cofiltered inverse system of quasi-compact and quasi-separated schemes with
> affine transition morphisms and limit cone `c`, and let `Z` be of finite presentation over the
> stage `D.obj i₀`. If the base change of `Z` to the limit is finite locally free of degree `d` over
> the limit, then its base change to `D.obj i` is finite locally free of degree `d` over `D.obj i`
> for some later stage `i`.

```lean
theorem exists_isFiniteLocallyFreeOfRank_overPullbackObj_of_isLimit
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u}) [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [∀ i : I, CompactSpace (D.obj i)] [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I) (Z : Over (D.obj i₀))
    (hZ : FinitePresentation Z.hom) (d : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank ((Over.pullback (c.π.app i₀)).obj Z).hom d] :
    ∃ (i : I) (g : i ⟶ i₀),
      Stacks.Morphisms.IsFiniteLocallyFreeOfRank ((Over.pullback (D.map g)).obj Z).hom d
```

## Tag 0C0C, a lemma

[Tag 0C0C](https://stacks.math.columbia.edu/tag/0C0C) in the Stacks Project.

**`AlgebraicGeometry.exists_smooth_baseChange_of_smooth_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Smooth.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Smooth.lean#L350). References: EGA IV (17.7.8), “(ii) smooth”; EGA IV (17.12.6), “f smooth ⇒ ∃λ”.

> **Stacks Project, Tag 0C0C.** If a locally finitely presented morphism over a stage of a
> cofiltered inverse system becomes smooth over the limit, it becomes smooth at some later
> stage.

```lean
theorem exists_smooth_baseChange_of_smooth_limitBaseChange
    {I : Type u} [Category.{u} I] (D : I ⥤ Scheme.{u}) (c : Cone D) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [IsCofiltered I]
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    (hc : IsLimit c)
    [Smooth ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀),
      Smooth ((Over.pullback (D.map g)).map f₀).left
```

## Tag 07RP, a lemma

[Tag 07RP](https://stacks.math.columbia.edu/tag/07RP) in the Stacks Project.

**`AlgebraicGeometry.exists_etale_pullback_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Etale.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Etale.lean#L63). References: EGA IV (17.7.8), “(ii) étale”.

> **Stacks 07RP.** If a locally finitely presented morphism at one stage of a cofiltered
> inverse system becomes étale over the limit, then it is étale at some later stage.

```lean
theorem exists_etale_pullback_of_isLimit
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c) (i₀ : I)
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    [Etale ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ i : Over i₀, Etale ((Over.pullback (D.map i.hom)).map f₀).left
```

## Tag 081E, a lemma

[Tag 081E](https://stacks.math.columbia.edu/tag/081E) in the Stacks Project.

**`AlgebraicGeometry.exists_isIso_baseChange_of_isIso_limitBaseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Isomorphism.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Isomorphism.lean#L173).

> If the base change of a finitely presented morphism to the inverse limit is an isomorphism,
> then its base change to some stage is already an isomorphism.

```lean
lemma exists_isIso_baseChange_of_isIso_limitBaseChange
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (S : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    (c : Cone S) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (S.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (S.obj i₀)] [QuasiSeparatedSpace (S.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    [IsIso ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀), IsIso ((Over.pullback (S.map g)).map f₀).left
```

## Tag 0EUU, a lemma

[Tag 0EUU](https://stacks.math.columbia.edu/tag/0EUU) in the Stacks Project.

**`AlgebraicGeometry.exists_isOpenImmersion_pullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Etale.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Etale.lean#L100).

> **Stacks 0EUU.** An open immersion obtained by base change to the inverse limit of an
> affine-transition inverse system descends to some stage of the system.

```lean
lemma exists_isOpenImmersion_pullback
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (S : I ⥤ Scheme.{u}) (c : Cone S) (hc : IsLimit c)
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    (i₀ : I) [CompactSpace (S.obj i₀)] [QuasiSeparatedSpace (S.obj i₀)]
    (X₀ Y₀ : Over (S.obj i₀))
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    (f₀ : X₀ ⟶ Y₀) [LocallyOfFinitePresentation f₀.left]
    (hf : IsOpenImmersion ((Over.pullback (c.π.app i₀)).map f₀).left) :
    ∃ (i : I) (g : i ⟶ i₀), IsOpenImmersion ((Over.pullback (S.map g)).map f₀).left
```

## Tag 0GTB, a lemma

[Tag 0GTB](https://stacks.math.columbia.edu/tag/0GTB) in the Stacks Project.

**`AlgebraicGeometry.exists_isImmersion_baseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Immersion.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Immersion.lean#L249).

> If a locally finite type morphism becomes an immersion over the inverse limit,
> it becomes an immersion at a later stage.

```lean
theorem exists_isImmersion_baseChange_of_isLimit
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    (c : Cone D) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    [IsImmersion ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (hi : i ⟶ i₀),
      IsImmersion ((Over.pullback (D.map hi)).map f₀).left
```

## Tag 07RQ, a lemma

[Tag 07RQ](https://stacks.math.columbia.edu/tag/07RQ) in the Stacks Project.

**`AlgebraicGeometry.exists_mono_baseChange_of_mono_limitBaseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Monomorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Monomorphism.lean#L78).

> **Stacks 07RQ.** A locally finite type morphism which becomes a monomorphism over the
> inverse limit is a monomorphism at some later stage.

```lean
lemma exists_mono_baseChange_of_mono_limitBaseChange
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (S : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    (c : Cone S) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (S.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (S.obj i₀)] [QuasiSeparatedSpace (S.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFiniteType f₀.left]
    [Mono ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀), Mono ((Over.pullback (S.map g)).map f₀).left
```

## Tag 07RR, a lemma

[Tag 07RR](https://stacks.math.columbia.edu/tag/07RR) in the Stacks Project.

**`AlgebraicGeometry.exists_surjective_baseChange_of_surjective_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Surjective.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Surjective.lean#L90).

> **Stacks Project, Tag 07RR.** If a locally finitely presented morphism over a stage of a
> cofiltered inverse system becomes surjective over the inverse limit, then it is surjective at
> some later stage.

```lean
theorem exists_surjective_baseChange_of_surjective_limitBaseChange
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (S : I ⥤ Scheme.{u})
    [∀ {i j : I} (g : i ⟶ j), IsAffineHom (S.map g)]
    (c : Cone S) (hc : IsLimit c) (i₀ : I)
    (X₀ Y₀ : Over (S.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [CompactSpace (S.obj i₀)] [QuasiSeparatedSpace (S.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left]
    [Surjective ((Over.pullback (c.π.app i₀)).map f₀).left] :
    ∃ (i : I) (g : i ⟶ i₀),
      Surjective ((Over.pullback (S.map g)).map f₀).left
```

## Tag 0C3L, a lemma

[Tag 0C3L](https://stacks.math.columbia.edu/tag/0C3L) in the Stacks Project.

**`AlgebraicGeometry.exists_syntomic_baseChange_of_syntomic_limitBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Finiteness/SyntomicDescentAlongLimit.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Finiteness/SyntomicDescentAlongLimit.lean#L234).

> **Stacks Project, Tag 0C3L.**  If a locally finitely presented morphism over a stage of a
> cofiltered inverse system with affine transition morphisms becomes syntomic over the limit, it
> becomes syntomic at some later stage.

```lean
theorem exists_syntomic_baseChange_of_syntomic_limitBaseChange {I : Type u} [Category.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (i₀ : I) (X₀ Y₀ : Over (D.obj i₀)) (f₀ : X₀ ⟶ Y₀)
    [IsCofiltered I] [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [CompactSpace (D.obj i₀)] [QuasiSeparatedSpace (D.obj i₀)]
    [CompactSpace X₀.left] [QuasiSeparatedSpace X₀.left]
    [CompactSpace Y₀.left] [QuasiSeparatedSpace Y₀.left]
    [LocallyOfFinitePresentation f₀.left] (hc : IsLimit c)
    (hf₀ : Syntomic ((Over.pullback (c.π.app i₀)).map f₀).left) :
    ∃ (i : I) (g : i ⟶ i₀), Syntomic ((Over.pullback (D.map g)).map f₀).left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.8, Tag 081C](https://stacks.math.columbia.edu/tag/081C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
