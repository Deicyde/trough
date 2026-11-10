---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_isAffineHom_app, AlgebraicGeometry.Space.isAffineHom_limitπ_comp_app, AlgebraicGeometry.Space.exists_isAffine_representation_limit, AlgebraicGeometry.Space.isAlgebraicSpace_limit, AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_isSiteSmall, AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_limitInSite, AlgebraicGeometry.Space.isLimitPullbackLimitOverPost, AlgebraicGeometry.Space.isAffineHom_limitπ
statement: formalized
proof: formalized
---

# 70.4 Limits of algebraic spaces

Section 70.4 of the Stacks Project, [Tag 07SE](https://stacks.math.columbia.edu/tag/07SE). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07SE, the section

[Tag 07SE](https://stacks.math.columbia.edu/tag/07SE) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_isAffineHom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineOverBase.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineOverBase.lean#L141). The attribute's comment: “the content the section is cited for: a cofiltered inverse limit of algebraic spaces affine over a base is an algebraic space; the section's own numbered results 07SF, 07SG, 07SH, 0CUH, 0CUI and 0CP4 are not proved here”.

> **Stacks 07SE.** The inverse limit of a cofiltered inverse system of algebraic spaces
> over `S`, each affine over one fixed algebraic space `T`, is an algebraic space over `S`,
> provided the index category is small enough for the site.
>
> Affineness of the transition morphisms, which is what Stacks 07SF asks for, is supplied by
> `AlgebraicGeometry.Space.isAffineHom_map_of_isAffineHom_app`.

```lean
theorem isAlgebraicSpace_limit_of_isAffineHom_app (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i)) (hT : IsAlgebraicSpace B S hS T)
    (hτ : ∀ i, IsAffineHom B S hS (τ.app i)) :
    IsAlgebraicSpace B S hS (limit D)
```

**`AlgebraicGeometry.Space.isAffineHom_limitπ_comp_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineOverBase.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineOverBase.lean#L157). The attribute's comment: “the content the section is cited for: the structure morphism of a cofiltered inverse limit of algebraic spaces affine over a base is affine; the section's own numbered results 07SF, 07SG, 07SH, 0CUH, 0CUI and 0CP4 are not proved here”.

> **Stacks 07SE.** The structure morphism of the inverse limit of a cofiltered inverse
> system of algebraic spaces each affine over one fixed algebraic space `T` is affine over `T`.
>
> It factors as the projection to a stage, which is affine by Stacks 07SF, part (1), followed
> by the structure morphism of that stage.

```lean
theorem isAffineHom_limitπ_comp_app (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i)) (hT : IsAlgebraicSpace B S hS T)
    (hτ : ∀ i, IsAffineHom B S hS (τ.app i)) (i : I) :
    IsAffineHom B S hS (limit.π D i ≫ τ.app i)
```

**`AlgebraicGeometry.Space.exists_isAffine_representation_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineOverBase.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineOverBase.lean#L187). The attribute's comment: “the content the section is cited for, combined with Limits, Section 01YV: a cofiltered inverse limit of algebraic spaces affine over an affine base is represented by an affine object of the site; the section's own numbered results 07SF, 07SG, 07SH, 0CUH, 0CUI and 0CP4 are not proved here”.

> **Stacks 07SE, over an affine base.** The inverse limit of a cofiltered inverse system of
> algebraic spaces over `S`, each affine over one fixed affine object `Z` of the site, is
> represented by an affine object of the site, by an isomorphism carrying the structure
> morphism of the limit to a morphism of the site.
>
> The structure morphism of the limit is affine, so its base change along the identity of
> `yoneda Z` is represented by an affine object of the site; a base change along an identity is
> an isomorphism.

```lean
theorem exists_isAffine_representation_limit (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hτ : ∀ i, IsAffineHom B S hS (τ.app i)) (i₀ : I) :
    ∃ (W : BigAffineFppf B S hS)
      (e : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj W) ≅ limit D)
      (q : (BigAffineFppf.inclusion B S hS).obj W ⟶
        (BigAffineFppf.inclusion B S hS).obj Z),
      e.hom ≫ limit.π D i₀ ≫ τ.app i₀ = yoneda.map q
```

## Tag 07SF, a lemma

[Tag 07SF](https://stacks.math.columbia.edu/tag/07SF) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLimitExistence.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLimitExistence.lean#L599). The attribute's comment: “existence”.

> **Stacks 07SF, existence.** The inverse limit of a cofiltered inverse system of algebraic
> spaces over `S` with affine transition morphisms is an algebraic space over `S`, provided the
> index category is small enough for the site: its object type and all of its morphism types
> have cardinality below the cofinality of the site's size cutoff.
>
> The limit is a sheaf by `AlgebraicGeometry.Space.isSheaf_limit`, and the remaining two
> conditions of Stacks 025Y follow from Stacks 02WY applied to the projection to any one stage,
> which is relatively representable by
> `AlgebraicGeometry.Space.relativelyRepresentable_limitπ`.

```lean
theorem isAlgebraicSpace_limit (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f)) :
    IsAlgebraicSpace B S hS (limit D)
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_isSiteSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLimitExistence.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLimitExistence.lean#L707). The attribute's comment: “existence”.

> **Stacks 07SF, existence.** The inverse limit of a cofiltered inverse system of algebraic
> spaces over `S` with affine transition morphisms is an algebraic space over `S`, provided the
> system is small for the site: either its index category is small compared with the cofinality
> of the site's size cutoff, its object type and all of its morphism types, or its transition
> morphisms are monomorphisms. See `AlgebraicGeometry.Space.IsSiteSmall`.
>
> The limit is a sheaf by `AlgebraicGeometry.Space.isSheaf_limit`, and the remaining two
> conditions of Stacks 025Y follow from Stacks 02WY applied to the projection to any one stage,
> which is relatively representable by
> `AlgebraicGeometry.Space.relativelyRepresentable_limitπ_of_isSiteSmall`.

```lean
theorem isAlgebraicSpace_limit_of_isSiteSmall (hb : IsSiteSmall B S hS D)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f)) :
    IsAlgebraicSpace B S hS (limit D)
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_limitInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLimitExistence.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLimitExistence.lean#L729). The attribute's comment: “existence”.

> **Stacks 07SF, existence, under the chapter's standing convention.** The inverse limit of a
> cofiltered inverse system of algebraic spaces over `S` with affine transition morphisms is an
> algebraic space over `S`.
>
> This is the faithful statement of the tag. The source states no condition on the index: it
> assumes only the convention of Section 70.2 that every ring considered has its spectrum in the
> big fppf site, which for this proof says that each limit of a diagram of base changes, to a
> test object of the site, of the stages over one stage lies in the site. That is
> `AlgebraicGeometry.BigFppfOver.LimitInSite` of a lift of such a diagram through the Yoneda
> embedding. The proof is the one of `AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_isSiteSmall`,
> which
> proves the same conclusion from the strictly stronger `AlgebraicGeometry.Space.IsSiteSmall`,
> with the appeal to smallness replaced by the convention at the stage, test object and point in
> hand.

```lean
theorem isAlgebraicSpace_limit_of_limitInSite
    (hconv : ∀ (i : I) (Z : BigFppfOver B S hS) (g : yoneda.obj Z ⟶ D.obj i)
      (W : Over i ⥤ BigFppfOver B S hS),
      (W ⋙ yoneda ≅ (Over.post (X := i) D ⋙ Over.pullback g) ⋙
        Over.forget (yoneda.obj Z)) → BigFppfOver.LimitInSite W)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f)) :
    IsAlgebraicSpace B S hS (limit D)
```

**`AlgebraicGeometry.Space.isLimitPullbackLimitOverPost`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean#L483). The attribute's comment: “part (2)”.

> For a cofiltered inverse system `D` of presheaves on the big fppf site of `S`, a stage `i`
> and a morphism `g : T ⟶ D i`, the base changes of the stages over `i` along `g` form an inverse
> system whose limit is the base change of `limit D` along `g`. The cone is the limit cone of `D`,
> restricted to the stages over `i` and base changed along `g`.

```lean
noncomputable def isLimitPullbackLimitOverPost (i : I)
    {T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : T ⟶ D.obj i) :
    IsLimit ((Over.forget T).mapCone
      ((Over.pullback g).mapCone ((limit.cone D).overPost i)))
```

**`AlgebraicGeometry.Space.isAffineHom_limitπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean#L548). The attribute's comment: “part (1)”.

> Every projection from the inverse limit of a cofiltered inverse system of algebraic spaces
> with affine transition morphisms is affine, provided the index category is small enough for the
> site: its object type and all of its morphism types have cardinality below the cofinality of the
> site's size cutoff.

```lean
theorem isAffineHom_limitπ (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (i : I) : IsAffineHom B S hS (limit.π D i)
```

**`AlgebraicGeometry.Space.isAffineHom_limitπ_of_siteContainsBaseChangeLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean, line 1082](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean#L1082). The attribute's comment: “part (1)”.

> Every projection from the inverse limit of a cofiltered inverse system of algebraic spaces
> with affine transition morphisms is affine, provided the system satisfies
> `AlgebraicGeometry.Space.SiteContainsBaseChangeLimits`.

```lean
theorem isAffineHom_limitπ_of_siteContainsBaseChangeLimits
    (hconv : SiteContainsBaseChangeLimits B S hS D)
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (i : I) : IsAffineHom B S hS (limit.π D i)
```

**`AlgebraicGeometry.Space.isAffineHom_limitπ_of_isSiteSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean, line 1095](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean#L1095). The attribute's comment: “part (1)”. References: SGA 3 XI (4.3), “partial”.

> Every projection from the inverse limit of a cofiltered inverse system of algebraic spaces
> with affine transition morphisms is affine, provided the system is small for the site in the
> sense of `AlgebraicGeometry.Space.IsSiteSmall`.

```lean
theorem isAffineHom_limitπ_of_isSiteSmall (hb : IsSiteSmall B S hS D)
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (i : I) : IsAffineHom B S hS (limit.π D i)
```

**`AlgebraicGeometry.Space.AffineChartSystem.limitBridge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineChartSystem.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineChartSystem.lean#L338). The attribute's comment: “limit of the affine charts at a stage”.

> **The limit of a chart system.** A chart system indexed by a slice of a sufficiently small
> index category has a limit in the big fppf site of `S`, whose underlying scheme is a limit of
> the underlying schemes of the charts and which represents the base change of `limit.π D i₀`
> along `f₀`.

```lean
noncomputable def limitBridge [IsCofiltered I] (C : AffineChartSystem B S hS i₀ D U₀ f₀)
    (hSize : #I < B.cutoff.ord.cof) (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof) :
    LimitBridge C
```

**`AlgebraicGeometry.Space.AffineChartSystem.limitBridgeOfLimitInSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineChartSystem.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineChartSystem.lean#L629). The attribute's comment: “limit of the affine charts at a stage”.

> **The limit of a chart system whose limit of charts lies in the site.** A chart system whose
> limit of charts lies in the site has a limit in the big fppf site of `S`, whose underlying
> scheme is a limit of the underlying schemes of the charts and which represents the base change
> of `limit.π D i₀` along `f₀`.

```lean
noncomputable def limitBridgeOfLimitInSite [IsCofiltered I]
    (C : AffineChartSystem B S hS i₀ D U₀ f₀)
    (hL : BigFppfOver.LimitInSite C.siteDiagram) :
    LimitBridge C
```

**`AlgebraicGeometry.Space.AffineChartSystem.limitBridgeOfIsSiteSmall`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineChartSystem.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/AffineChartSystem.lean#L660). The attribute's comment: “limit of the affine charts at a stage”.

> **The limit of a chart system of a system small for the site.** A chart system of a system
> which is small for the site has a limit in the big fppf site of `S`, whose underlying scheme is
> a limit of the underlying schemes of the charts and which represents the base change of
> `limit.π D i₀` along `f₀`.

```lean
noncomputable def limitBridgeOfIsSiteSmall [IsCofiltered I]
    (C : AffineChartSystem B S hS i₀ D U₀ f₀)
    (hb : Space.IsSiteSmall B S hS D) :
    LimitBridge C
```

## Tag 07SG, an equation

[Tag 07SG](https://stacks.math.columbia.edu/tag/07SG) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_quotient_presentation_of_affine_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuotientPresentation.lean, line 1354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuotientPresentation.lean#L1354).

> Let `D` be a cofiltered inverse system of algebraic spaces over `S` with affine transition
> morphisms and `p₀ : U₀ ⟶ D i₀` a surjective étale atlas of one stage. Then there are a scheme
> `U` over `S` with `f : U ⟶ U₀` and `q : U ⟶ lim D` making `U = U₀ ×_{D i₀} lim D`, and an étale
> equivalence relation `R` on `U` that is the kernel pair of `q`, such that the canonical map from
> `U/R` to the limit of the inverse system is an isomorphism of fppf sheaves.
>
> The atlas `U₀` is required to be one of the site's schemes (`hU₀mem`), as in Stacks 07SG, which
> chooses a scheme `U₀` together with a surjective étale morphism `U₀ → X₀`; an atlas of an
> algebraic space is an object of the site by construction, cf.
> `AlgebraicGeometry.IsAlgebraicSpace.exists_atlas`.

```lean
public theorem exists_quotient_presentation_of_affine_transition
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ Sheaf (BigFppfOver.topology B S hS) (Type u))
    [HasLimit D] [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (hD : ∀ i, AlgebraicGeometry.IsAlgebraicSpace B S hS (D.obj i).obj)
    (hAffine : ∀ {i j : I} (f : i ⟶ j),
      AlgebraicGeometry.Space.IsAffineHom B S hS (D.map f).hom)
    (i₀ : I) (U₀ : Over S) (hU₀mem : B.Contains U₀.left)
    (hU₀ : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
      (Stacks.Groupoids.points (BigFppfOver.toOver B S hS) U₀))
    (p₀ : representedSheaf B S hS U₀ hU₀ ⟶ D.obj i₀)
    (hp₀ : Epi p₀)
    (hp₀Etale :
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@Etale.{u} : MorphismProperty Scheme.{u})
        (AlgebraicGeometry.BigFppfOver.toScheme B S hS))) p₀.hom)
    : ∃ (U : Over S)
        (hU : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
          (Stacks.Groupoids.points (BigFppfOver.toOver B S hS) U))
        (R : Over S) (j : Stacks.Groupoids.PreRelation R U)
        (q : representedSheaf B S hS U hU ⟶ limit D)
        (f : U ⟶ U₀),
        IsPullback
          ((BigFppfOver.toOver B S hS).op.whiskerLeft (yoneda.map f))
          q.hom p₀.hom (limit.π D i₀).hom ∧
        ∃ (hq : Stacks.Groupoids.sourceMap (BigFppfOver.toOver B S hS) j ≫ q.hom =
            Stacks.Groupoids.targetMap (BigFppfOver.toOver B S hS) j ≫ q.hom),
          IsPullback
            (Stacks.Groupoids.sourceMap (BigFppfOver.toOver B S hS) j)
            (Stacks.Groupoids.targetMap (BigFppfOver.toOver B S hS) j)
            q.hom q.hom ∧
          Stacks.Groupoids.IsEtaleEquivalenceRelation j ∧
          IsIso (canonicalQuotientToLimit B S hS D j hU q hq)
```

## Tag 07SH, a lemma

[Tag 07SH](https://stacks.math.columbia.edu/tag/07SH) in the Stacks Project.

**`AlgebraicGeometry.Space.isLimitPullbackLimitOverPost`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ApproximationSteps.lean#L483). The attribute's comment: “base change of the limit is the limit of the base changes”.

> For a cofiltered inverse system `D` of presheaves on the big fppf site of `S`, a stage `i`
> and a morphism `g : T ⟶ D i`, the base changes of the stages over `i` along `g` form an inverse
> system whose limit is the base change of `limit D` along `g`. The cone is the limit cone of `D`,
> restricted to the stages over `i` and base changed along `g`.

```lean
noncomputable def isLimitPullbackLimitOverPost (i : I)
    {T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : T ⟶ D.obj i) :
    IsLimit ((Over.forget T).mapCone
      ((Over.pullback g).mapCone ((limit.cone D).overPost i)))
```

## Tag 0CUH, a lemma

[Tag 0CUH](https://stacks.math.columbia.edu/tag/0CUH) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_limitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LimitClosedImmersion.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LimitClosedImmersion.lean#L111).

> A stagewise closed immersion between inverse systems of algebraic spaces with affine
> transition morphisms induces a closed immersion of their inverse limits.

```lean
theorem isClosedImmersion_limitMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    {X Y : I ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (η : X ⟶ Y)
    (hX : ∀ i, IsAlgebraicSpace B S hS (X.obj i))
    (hY : ∀ i, IsAlgebraicSpace B S hS (Y.obj i))
    (hXAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (X.map f))
    (hYAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (Y.map f))
    (hClosed : ∀ i, IsClosedImmersion B S hS (η.app i)) :
    IsClosedImmersion B S hS (limMap η)
```

## Tag 0CUI, a lemma

[Tag 0CUI](https://stacks.math.columbia.edu/tag/0CUI) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/Reduced.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/Reduced.lean#L495).

> A cofiltered inverse limit of reduced algebraic spaces with affine
> transition morphisms is reduced.

```lean
public theorem Space.isReduced_limit
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hSize : Cardinal.mk I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, Cardinal.mk (i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, AlgebraicGeometry.IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j),
      AlgebraicGeometry.Space.IsAffineHom B S hS (D.map f))
    (hReduced : ∀ i, AlgebraicGeometry.Space.HasEtaleLocalProperty B S hS (D.obj i)
      (fun X : Scheme.{u} => IsReduced X)) :
    AlgebraicGeometry.Space.HasEtaleLocalProperty B S hS (limit D)
      (fun X : Scheme.{u} => IsReduced X)
```

## Tag 0CP4, a lemma

[Tag 0CP4](https://stacks.math.columbia.edu/tag/0CP4) in the Stacks Project.

**`AlgebraicGeometry.Space.affineLimitSquare_iff_qcqsLimitSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/QcqsCriterion.lean, line 1116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/QcqsCriterion.lean#L1116).

> **Stacks 0CP4.** For a morphism of algebraic spaces over `S`, the affine-limit
> comparison square is cartesian for every sufficiently small cofiltered inverse system of
> affine objects exactly when the comparison square of morphism sets is cartesian for every
> sufficiently small cofiltered inverse system of quasi-compact and quasi-separated algebraic
> spaces with affine transition morphisms.

```lean
theorem affineLimitSquare_iff_qcqsLimitSquare (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) :
    AffineLimitSquare B S hS f ↔ QcqsLimitSquare B S hS hZ f
```

**`AlgebraicGeometry.Space.qcqsLimitSquare_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/QcqsCriterion.lean, line 1141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/QcqsCriterion.lean#L1141). The attribute's comment: “the implication from locally of finite presentation”.

> **Stacks 0CP4.** A morphism of algebraic spaces over `S` which is locally of finite
> presentation satisfies the comparison condition for cofiltered limits of quasi-compact and
> quasi-separated algebraic spaces with affine transition morphisms.

```lean
theorem qcqsLimitSquare_of_isLocallyOfFinitePresentation (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFinitePresentation B S hS f) :
    QcqsLimitSquare B S hS hZ f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.4, Tag 07SE](https://stacks.math.columbia.edu/tag/07SE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
