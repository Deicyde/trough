---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_morphism_after_baseChange, AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq, AlgebraicGeometry.Space.exists_model_of_finitePresentation, AlgebraicGeometry.Space.exists_morphism_after_baseChange_of_chartLimitsInSite, AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq_of_chartLimitsInSite, AlgebraicGeometry.Space.exists_model_of_finitePresentation_of_chartLimitsInSite, AlgebraicGeometry.Space.finitePresentationModule_isColimit_of_isLimit_of_baseChangeLimits, AlgebraicGeometry.Space.exists_isFiniteLocallyFreeOnSite_stage_model
statement: formalized
proof: formalized
---

# 70.7 Descending relative objects

Section 70.7 of the Stacks Project, [Tag 07SJ](https://stacks.math.columbia.edu/tag/07SJ). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07SK, a lemma

[Tag 07SK](https://stacks.math.columbia.edu/tag/07SK) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_morphism_after_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean, line 3570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean#L3570). The attribute's comment: “fullness”.

> A morphism between base changes of finite-presentation algebraic spaces
> is defined at a sufficiently late stage.

```lean
public theorem exists_morphism_after_baseChange
    (i : I) (Yᵢ Zᵢ : Over (D.obj i))
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Yᵢ.left)
    (hZ' : AlgebraicGeometry.IsAlgebraicSpace B S hS Zᵢ.left)
    (hYfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Yᵢ.hom)
    (hZfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Zᵢ.hom)
    (f : (Over.pullback (limit.π D i)).obj Yᵢ ⟶
      (Over.pullback (limit.π D i)).obj Zᵢ) :
    ∃ (j : I) (e : j ⟶ i)
      (g : (Over.pullback (D.map e)).obj Yᵢ ⟶
        (Over.pullback (D.map e)).obj Zᵢ)
      (α : (Over.pullback (limit.π D j)).obj
          ((Over.pullback (D.map e)).obj Yᵢ) ≅
        (Over.pullback (limit.π D i)).obj Yᵢ)
      (β : (Over.pullback (limit.π D j)).obj
          ((Over.pullback (D.map e)).obj Zᵢ) ≅
        (Over.pullback (limit.π D i)).obj Zᵢ),
      (α.hom.left ≫ pullback.fst Yᵢ.hom (limit.π D i) =
        pullback.fst ((Over.pullback (D.map e)).obj Yᵢ).hom (limit.π D j) ≫
          pullback.fst Yᵢ.hom (D.map e)) ∧
      (β.hom.left ≫ pullback.fst Zᵢ.hom (limit.π D i) =
        pullback.fst ((Over.pullback (D.map e)).obj Zᵢ).hom (limit.π D j) ≫
          pullback.fst Zᵢ.hom (D.map e)) ∧
      α.hom ≫ f = (Over.pullback (limit.π D j)).map g ≫ β.hom
```

**`AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean, line 3746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean#L3746). The attribute's comment: “faithfulness”.

> Two finite-stage morphisms that agree over the limit agree at a sufficiently
> late stage.

```lean
public theorem eventually_eq_of_baseChange_eq
    (i : I) (Yᵢ Zᵢ : Over (D.obj i))
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Yᵢ.left)
    (hZ' : AlgebraicGeometry.IsAlgebraicSpace B S hS Zᵢ.left)
    (hYfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Yᵢ.hom)
    (hZfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Zᵢ.hom)
    (f g : Yᵢ ⟶ Zᵢ)
    (hfg : (Over.pullback (limit.π D i)).map f =
      (Over.pullback (limit.π D i)).map g) :
    ∃ (j : I) (e : j ⟶ i),
      (Over.pullback (D.map e)).map f =
        (Over.pullback (D.map e)).map g
```

**`AlgebraicGeometry.Space.exists_model_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean, line 4618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean#L4618). The attribute's comment: “essential surjectivity”.

> Every algebraic space of finite presentation over the limit descends to a
> finite stage.

```lean
public theorem exists_model_of_finitePresentation
    (Y : Over (limit D))
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y.left)
    (hFp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Y.hom) :
    ∃ (i : I) (Yᵢ : Over (D.obj i)),
      AlgebraicGeometry.IsAlgebraicSpace B S hS Yᵢ.left ∧
        AlgebraicGeometry.Space.IsFinitePresentation B S hS Yᵢ.hom ∧
        Nonempty (Y ≅ (Over.pullback (limit.π D i)).obj Yᵢ)
```

**`AlgebraicGeometry.Space.exists_morphism_after_baseChange_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean#L188). The attribute's comment: “fullness, with no bound on the index: the 07SD convention in place of the cardinality bounds of exists\_morphism\_after\_baseChange”.

> **Stacks 07SK, fullness, with no bound on the index.** A morphism between the base changes
> to the limit of two algebraic spaces of finite presentation over a stage comes from a morphism
> at a later stage.
>
> This strengthens `AlgebraicGeometry.Space.exists_morphism_after_baseChange`: the cardinality
> bounds on the index category are replaced by `hconv`. `hconv` is the convention 07SD of the
> chapter: the limits of the base changes of the stages to the affine objects of the site lie in
> the site. It is not an assumption beyond the source. It is
> `AlgebraicGeometry.Space.SiteContainsBaseChangeLimits` unfolded, and the index bounds imply it.
>
> It is `AlgebraicGeometry.Space.exists_morphism_after_baseChange_of_siteContainsBaseChangeLimits`
> without the hypothesis that the limit is an algebraic space, which Stacks 07SF under the
> convention supplies.

```lean
public theorem exists_morphism_after_baseChange_of_chartLimitsInSite
    (hconv : ∀ (i : I) (Z : AlgebraicGeometry.BigAffineFppf B S hS)
      (g : yoneda.obj ((AlgebraicGeometry.BigAffineFppf.inclusion B S hS).obj Z) ⟶ D.obj i)
      (W : Over i ⥤ AlgebraicGeometry.BigAffineFppf B S hS),
      (W ⋙ (AlgebraicGeometry.BigAffineFppf.inclusion B S hS ⋙ yoneda) ≅
        (Over.post (X := i) D ⋙ Over.pullback g) ⋙
          Over.forget (yoneda.obj ((AlgebraicGeometry.BigAffineFppf.inclusion B S hS).obj Z))) →
      ∀ c : Cone (((W ⋙ AlgebraicGeometry.BigAffineFppf.inclusion B S hS) ⋙
          AlgebraicGeometry.BigFppfOver.forget B S hS) ⋙ B.inclusion),
        IsLimit c → B.Contains c.pt)
    (hD : ∀ i, AlgebraicGeometry.IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), AlgebraicGeometry.Space.IsAffineHom B S hS (D.map f))
    (hQc : ∀ i, AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS (D.obj i))
    (hQs : ∀ i, AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i))
    (i : I) (Yᵢ Zᵢ : Over (D.obj i))
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Yᵢ.left)
    (hZ' : AlgebraicGeometry.IsAlgebraicSpace B S hS Zᵢ.left)
    (hYfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Yᵢ.hom)
    (hZfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Zᵢ.hom)
    (f : (Over.pullback (limit.π D i)).obj Yᵢ ⟶
      (Over.pullback (limit.π D i)).obj Zᵢ) :
    ∃ (j : I) (e : j ⟶ i)
      (g : (Over.pullback (D.map e)).obj Yᵢ ⟶
        (Over.pullback (D.map e)).obj Zᵢ)
      (α : (Over.pullback (limit.π D j)).obj
          ((Over.pullback (D.map e)).obj Yᵢ) ≅
        (Over.pullback (limit.π D i)).obj Yᵢ)
      (β : (Over.pullback (limit.π D j)).obj
          ((Over.pullback (D.map e)).obj Zᵢ) ≅
        (Over.pullback (limit.π D i)).obj Zᵢ),
      (α.hom.left ≫ pullback.fst Yᵢ.hom (limit.π D i) =
        pullback.fst ((Over.pullback (D.map e)).obj Yᵢ).hom (limit.π D j) ≫
          pullback.fst Yᵢ.hom (D.map e)) ∧
      (β.hom.left ≫ pullback.fst Zᵢ.hom (limit.π D i) =
        pullback.fst ((Over.pullback (D.map e)).obj Zᵢ).hom (limit.π D j) ≫
          pullback.fst Zᵢ.hom (D.map e)) ∧
      α.hom ≫ f = (Over.pullback (limit.π D j)).map g ≫ β.hom
```

**`AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean#L247). The attribute's comment: “faithfulness, with no bound on the index: the 07SD convention in place of the cardinality bounds of eventually\_eq\_of\_baseChange\_eq”.

> **Stacks 07SK, faithfulness, with no bound on the index.** Two morphisms between
> algebraic spaces of finite presentation over a stage whose base changes to the limit agree
> already agree at a later stage.
>
> This strengthens `AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq`: the cardinality
> bounds on the index category are replaced by `hconv`. `hconv` is the convention 07SD of the
> chapter: the limits of the base changes of the stages to the affine objects of the site lie in
> the site. It is not an assumption beyond the source. It is
> `AlgebraicGeometry.Space.SiteContainsBaseChangeLimits` unfolded, and the index bounds imply it.
> Without it the statement is false; see the notes opening this section.
>
> It is `AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq_of_siteContainsBaseChangeLimits`
> with the convention written out.

```lean
public theorem eventually_eq_of_baseChange_eq_of_chartLimitsInSite
    (hconv : ∀ (i : I) (Z : AlgebraicGeometry.BigAffineFppf B S hS)
      (g : yoneda.obj ((AlgebraicGeometry.BigAffineFppf.inclusion B S hS).obj Z) ⟶ D.obj i)
      (W : Over i ⥤ AlgebraicGeometry.BigAffineFppf B S hS),
      (W ⋙ (AlgebraicGeometry.BigAffineFppf.inclusion B S hS ⋙ yoneda) ≅
        (Over.post (X := i) D ⋙ Over.pullback g) ⋙
          Over.forget (yoneda.obj ((AlgebraicGeometry.BigAffineFppf.inclusion B S hS).obj Z))) →
      ∀ c : Cone (((W ⋙ AlgebraicGeometry.BigAffineFppf.inclusion B S hS) ⋙
          AlgebraicGeometry.BigFppfOver.forget B S hS) ⋙ B.inclusion),
        IsLimit c → B.Contains c.pt)
    (hD : ∀ i, AlgebraicGeometry.IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), AlgebraicGeometry.Space.IsAffineHom B S hS (D.map f))
    (hQc : ∀ i, AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS (D.obj i))
    (i : I) (Yᵢ Zᵢ : Over (D.obj i))
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Yᵢ.left)
    (hZ' : AlgebraicGeometry.IsAlgebraicSpace B S hS Zᵢ.left)
    (hYfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Yᵢ.hom)
    (hZfp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Zᵢ.hom)
    (f g : Yᵢ ⟶ Zᵢ)
    (hfg : (Over.pullback (limit.π D i)).map f =
      (Over.pullback (limit.π D i)).map g) :
    ∃ (j : I) (e : j ⟶ i),
      (Over.pullback (D.map e)).map f =
        (Over.pullback (D.map e)).map g
```

**`AlgebraicGeometry.Space.exists_model_of_finitePresentation_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean#L292). The attribute's comment: “essential surjectivity, with no bound on the index: the 07SD convention in place of the cardinality bounds of exists\_model\_of\_finitePresentation”.

> **Stacks 07SK, essential surjectivity, with no bound on the index.** Every algebraic space
> of finite presentation over the limit is the base change of an algebraic space of finite
> presentation over some stage.
>
> This strengthens `AlgebraicGeometry.Space.exists_model_of_finitePresentation`: the cardinality
> bounds on the index category are replaced by `hconv`. `hconv` is the convention 07SD of the
> chapter: the limits of the base changes of the stages to the affine objects of the site lie in
> the site. It is not an assumption beyond the source. It is
> `AlgebraicGeometry.Space.SiteContainsBaseChangeLimits` unfolded, and the index bounds imply it.
>
> It is `AlgebraicGeometry.Space.exists_model_of_finitePresentation_of_siteContainsBaseChangeLimits`
> without the hypothesis that the limit is an algebraic space, which Stacks 07SF under the
> convention supplies.

```lean
public theorem exists_model_of_finitePresentation_of_chartLimitsInSite
    (hconv : ∀ (i : I) (Z : AlgebraicGeometry.BigAffineFppf B S hS)
      (g : yoneda.obj ((AlgebraicGeometry.BigAffineFppf.inclusion B S hS).obj Z) ⟶ D.obj i)
      (W : Over i ⥤ AlgebraicGeometry.BigAffineFppf B S hS),
      (W ⋙ (AlgebraicGeometry.BigAffineFppf.inclusion B S hS ⋙ yoneda) ≅
        (Over.post (X := i) D ⋙ Over.pullback g) ⋙
          Over.forget (yoneda.obj ((AlgebraicGeometry.BigAffineFppf.inclusion B S hS).obj Z))) →
      ∀ c : Cone (((W ⋙ AlgebraicGeometry.BigAffineFppf.inclusion B S hS) ⋙
          AlgebraicGeometry.BigFppfOver.forget B S hS) ⋙ B.inclusion),
        IsLimit c → B.Contains c.pt)
    (hD : ∀ i, AlgebraicGeometry.IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), AlgebraicGeometry.Space.IsAffineHom B S hS (D.map f))
    (hQc : ∀ i, AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS (D.obj i))
    (hQs : ∀ i, AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i))
    (Y : Over (limit D))
    (hY : AlgebraicGeometry.IsAlgebraicSpace B S hS Y.left)
    (hFp : AlgebraicGeometry.Space.IsFinitePresentation B S hS Y.hom) :
    ∃ (i : I) (Yᵢ : Over (D.obj i)),
      AlgebraicGeometry.IsAlgebraicSpace B S hS Yᵢ.left ∧
        AlgebraicGeometry.Space.IsFinitePresentation B S hS Yᵢ.hom ∧
        Nonempty (Y ≅ (Over.pullback (limit.π D i)).obj Yᵢ)
```

## Tag 07V7, a lemma

[Tag 07V7](https://stacks.math.columbia.edu/tag/07V7) in the Stacks Project.

**`AlgebraicGeometry.Space.finitePresentationModule_isColimit_of_isLimit_of_baseChangeLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationModuleColimitTheorem.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationModuleColimitTheorem.lean#L286). The attribute's comment: “the category of finitely presented modules on the limit is the colimit of the categories of finitely presented modules on the stages: faithfulness, fullness through the canonical identification of iterated inverse images, and essential surjectivity of the comparison; for any limiting cone over the system, its cone point being an algebraic space by Stacks 07SF, indexed by any cofiltered category in the universe of the site, under the chapter's standing convention 07SD that the limits of its affine charts lie in the site; without that convention the statement fails in a size-bounded site (see the notes of ChartLimitsInSite)”.

> **Stacks 07V7.** Let `X = lim X_i` be the limit of a cofiltered inverse system of
> quasi-compact and quasi-separated algebraic spaces over `S` with affine transition morphisms:
> `X = c.pt` for a cone `c` over the system that is limiting in presheaves on the big fppf site of
> `S`, the affine charts `X_j ×_{X_i} U` of the system having their limits, in schemes, inside the
> site (the chapter's convention, Stacks 07SD). Then `X` is an algebraic space
> (`AlgebraicGeometry.Space.isAlgebraicSpace_conePt_of_isLimit`, Stacks 07SF), and the category of
> finitely presented `𝒪_X`-modules is the colimit of the categories of finitely presented
> `𝒪_{X_i}`-modules: inverse image along the projections `X ⟶ X_i` is
>
> 1. faithful in the colimit sense: two morphisms on a stage with equal inverse images to `X` have
>    equal inverse images to a later stage;
> 2. full in the colimit sense: a morphism between inverse images to `X` is, at a later stage, the
>    restriction along `X ⟶ X_j` of a morphism between the inverse images to `X_j`;
> 3. essentially surjective in the colimit sense: every finitely presented `𝒪_X`-module is the
>    inverse image of a finitely presented module on some stage.
>
> The index category is any cofiltered category in the universe of the site.

```lean
theorem finitePresentationModule_isColimit_of_isLimit_of_baseChangeLimits
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (hQc : ∀ i, IsQuasiCompactSpace B S hS (D.obj i))
    (hQs : ∀ i, IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i))
    (hc : IsLimit c) (hL : SiteContainsBaseChangeLimits B S hS D) :
    let hX := isAlgebraicSpace_conePt_of_isLimit B S hS D hD c hAffine hQc hc hL
    (∀ (i : I) (M N : Modules.{u, u} B S hS (stageAlgebraicSpace B S hS D hD i).1
        (stageAlgebraicSpace B S hS D hD i).2),
      M.IsFinitePresentationOnSite → N.IsFinitePresentationOnSite → ∀ φ ψ : M ⟶ N,
        (modulePullback B S hS (coneProjection B S hS D hD c hX i)).map φ =
          (modulePullback B S hS (coneProjection B S hS D hD c hX i)).map ψ →
        ∃ (j : I) (e : j ⟶ i),
          (modulePullback B S hS (stageTransition B S hS D hD e)).map φ =
            (modulePullback B S hS (stageTransition B S hS D hD e)).map ψ) ∧
    (∀ (i : I) (M N : Modules.{u, u} B S hS (stageAlgebraicSpace B S hS D hD i).1
        (stageAlgebraicSpace B S hS D hD i).2),
      M.IsFinitePresentationOnSite → N.IsFinitePresentationOnSite →
      ∀ φ : (modulePullback B S hS (coneProjection B S hS D hD c hX i)).obj M ⟶
        (modulePullback B S hS (coneProjection B S hS D hD c hX i)).obj N,
        ∃ (j : I) (e : j ⟶ i)
          (ψ : (modulePullback B S hS (stageTransition B S hS D hD e)).obj M ⟶
            (modulePullback B S hS (stageTransition B S hS D hD e)).obj N),
          moduleHomRestrict M N (coneProjection B S hS D hD c hX j)
            (stageTransition B S hS D hD e) (coneProjection B S hS D hD c hX i)
            (coneProjection_comp B S hS D hD c hX e) ψ = φ) ∧
    (∀ P : Modules.{u, u} B S hS c.pt hX, P.IsFinitePresentationOnSite →
        ∃ (k : I) (Q : Modules.{u, u} B S hS (stageAlgebraicSpace B S hS D hD k).1
            (stageAlgebraicSpace B S hS D hD k).2),
          Q.IsFinitePresentationOnSite ∧
            Nonempty (P ≅ (modulePullback B S hS (coneProjection B S hS D hD c hX k)).obj Q))
```

## Tag 0D2X, a lemma

[Tag 0D2X](https://stacks.math.columbia.edu/tag/0D2X) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFiniteLocallyFreeOnSite_stage_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean#L89). The attribute's comment: “(1)”.

> **Stacks 0D2X, part (1).** Let `X = lim Xᵢ` be the limit of a cofiltered system of
> quasi-compact and quasi-separated algebraic spaces over `S` with affine transition morphisms, as
> in Stacks 07SK.  Every finite locally free `𝒪_X`-module is the pullback of a finite locally free
> `𝒪_{Xᵢ}`-module for some `i`.

```lean
theorem exists_isFiniteLocallyFreeOnSite_stage_model
    (F : Modules.{u, u} B S hS
      (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine).1
      (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine).2)
    (hF : SheafOfModules.IsFiniteLocallyFreeOnSite F) :
    ∃ (i : I) (Fᵢ : Modules.{u, u} B S hS (stageAlgebraicSpace B S hS D hD i).1
        (stageAlgebraicSpace B S hS D hD i).2),
      SheafOfModules.IsFiniteLocallyFreeOnSite Fᵢ ∧
        Nonempty (F ≅ (modulePullback B S hS
          (limitProjection B S hS D hSize hHomSize hD hAffine i)).obj Fᵢ)
```

**`AlgebraicGeometry.Space.exists_isInvertibleModule_stage_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean#L111). The attribute's comment: “(2)”.

> **Stacks 0D2X, part (2).** Let `X = lim Xᵢ` be the limit of a cofiltered system of
> quasi-compact and quasi-separated algebraic spaces over `S` with affine transition morphisms, as
> in Stacks 07SK.  Every invertible `𝒪_X`-module is the pullback of an invertible
> `𝒪_{Xᵢ}`-module for some `i`.

```lean
theorem exists_isInvertibleModule_stage_model
    (L : Modules.{u, u} B S hS
      (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine).1
      (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine).2)
    (hL : IsInvertibleModule (limitAlgebraicSpace B S hS D hSize hHomSize hD hAffine) L) :
    ∃ (i : I) (Lᵢ : Modules.{u, u} B S hS (stageAlgebraicSpace B S hS D hD i).1
        (stageAlgebraicSpace B S hS D hD i).2),
      IsInvertibleModule (stageAlgebraicSpace B S hS D hD i) Lᵢ ∧
        Nonempty (L ≅ (modulePullback B S hS
          (limitProjection B S hS D hSize hHomSize hD hAffine i)).obj Lᵢ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.7, Tag 07SJ](https://stacks.math.columbia.edu/tag/07SJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
