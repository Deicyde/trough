---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_morphism_after_baseChange, AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq, AlgebraicGeometry.Space.exists_model_of_finitePresentation, AlgebraicGeometry.Space.exists_morphism_after_baseChange_of_chartLimitsInSite, AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq_of_chartLimitsInSite, AlgebraicGeometry.Space.exists_model_of_finitePresentation_of_chartLimitsInSite, AlgebraicGeometry.Space.eventually_eq_of_modulePullback_limitProjection_eq, AlgebraicGeometry.Space.finitePresentationModule_isColimit_of_isLimit
statement: formalized
proof: formalized
---

# 70.7 Descending relative objects

Section 70.7 of the Stacks Project, [Tag 07SJ](https://stacks.math.columbia.edu/tag/07SJ). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07SK, a lemma

[Tag 07SK](https://stacks.math.columbia.edu/tag/07SK) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_morphism_after_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean, line 3551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean#L3551). The attribute's comment: “fullness”.

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

**`AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean, line 3726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean#L3726). The attribute's comment: “faithfulness”.

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

**`AlgebraicGeometry.Space.exists_model_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean, line 4598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescent.lean#L4598). The attribute's comment: “essential surjectivity”.

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

**`AlgebraicGeometry.Space.exists_morphism_after_baseChange_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean#L188). The attribute's comment: “fullness, with no bound on the index: the 07SD convention in place of the cardinality bounds of exists\_morphism\_after\_baseChange”.

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

**`AlgebraicGeometry.Space.eventually_eq_of_baseChange_eq_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean#L247). The attribute's comment: “faithfulness, with no bound on the index: the 07SD convention in place of the cardinality bounds of eventually\_eq\_of\_baseChange\_eq”.

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
    (hQs : ∀ i, AlgebraicGeometry.Space.IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i))
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

**`AlgebraicGeometry.Space.exists_model_of_finitePresentation_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationDescentUnbounded.lean#L293). The attribute's comment: “essential surjectivity, with no bound on the index: the 07SD convention in place of the cardinality bounds of exists\_model\_of\_finitePresentation”.

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

**`AlgebraicGeometry.Space.eventually_eq_of_modulePullback_limitProjection_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationModuleColimit.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationModuleColimit.lean#L392). The attribute's comment: “the faithfulness clause of the colimit assertion: two morphisms of finitely presented modules on a stage whose inverse images to the limit agree already agree at a later stage. Granted `haffine`, the same clause for an inverse system of affine schemes of the site, which is Stacks 01ZR(3) read on their small étale ringed sites — this tree proves Stacks 01ZR(3) only for Mathlib's `Scheme.Modules` on the Zariski site of opens, and the comparison with the small étale modules of the algebraic space a scheme represents is a functor with no inverse: the notes of `StacksFrontier/AlgebraicGeometry/Spaces/RepresentedZariskiRestriction.lean` record that neither composite is identified with an identity, that being Stacks 03DX(2), which is proved only over the essential surjectivity `AlgebraicGeometry.SmallEtale.QuasicoherentIsEssImageAssociatedModule` that `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleEssentialImage.lean` does not have; the carried statement is about systems of affine schemes and the conclusion about systems of quasi-compact algebraic spaces, so it is not the universally quantified form of this conclusion. The essential surjectivity and fullness clauses of Stacks 07V7 are not covered: both need the equivalence `QCoh(𝒪_X) = QCoh(U, R, s, t, c)` of Stacks 03M3, of which this tree has only the functor in one direction”.

> **Stacks 07V7, the faithfulness clause of the colimit assertion.** Two morphisms of
> finitely presented `𝒪_{X_i}`-modules on a stage of the system whose inverse images along the
> projection of the limit agree already have equal inverse images along a transition morphism
> from a later stage.
>
> The proof is the source's reduction to an affine chart. Choose a surjective étale chart
> `f₀ : U₀ ⟶ X_i` with `U₀` affine, available because `X_i` is quasi-compact, and base change the
> later stages along it: this is a cofiltered system of affine schemes of the site whose limit is
> the chart `U₀ ×_{X_i} X` of the limit, so the carried affine case applies to the inverse images
> of the two morphisms to that chart and produces a later stage at which they agree over the
> corresponding chart. The chart of that stage is again surjective and étale, so the inverse image
> along it is faithful and the two morphisms agree over the stage itself.

```lean
theorem eventually_eq_of_modulePullback_limitProjection_eq
    (haffine : EventualModuleMapEqOverAffineSystem B S hS) (i : I)
    (hQc : IsQuasiCompactSpace B S hS (D.obj i))
    (M N : Modules.{u, u} B S hS (stageAlgebraicSpace B S hS D hD i).1
      (stageAlgebraicSpace B S hS D hD i).2)
    (hM : M.IsFinitePresentationOnSite) (hN : N.IsFinitePresentationOnSite) (φ ψ : M ⟶ N)
    (h : (modulePullback B S hS
          (limitProjection B S hS D hSize hHomSize hD hAffine i)).map φ =
        (modulePullback B S hS
          (limitProjection B S hS D hSize hHomSize hD hAffine i)).map ψ) :
    ∃ (j : I) (e : j ⟶ i),
      (modulePullback B S hS (stageTransition B S hS D hD e)).map φ =
        (modulePullback B S hS (stageTransition B S hS D hD e)).map ψ
```

**`AlgebraicGeometry.Space.finitePresentationModule_isColimit_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationModuleColimitTheorem.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationModuleColimitTheorem.lean#L168). The attribute's comment: “the category of finitely presented modules on the limit is the colimit of the categories of finitely presented modules on the stages: faithfulness, fullness through the canonical identification of iterated inverse images, and essential surjectivity of the comparison; for a given limit of the system at any cofiltered index category, under the source's own standing convention 07SD that the limits of its affine charts lie in the site; without that convention the statement fails in a size-bounded site (see the notes of ChartLimitsInSite)”.

> **Stacks 07V7.** Let `X = lim X_i` be the limit of a cofiltered inverse system of
> quasi-compact and quasi-separated algebraic spaces over `S` with affine transition morphisms:
> an algebraic space `X = c.pt` with a cone `c` over the system that is limiting in presheaves on
> the big fppf site of `S`, whose affine charts `X_j ×_{X_i} U` have their limits, in schemes,
> inside the site (the chapter's convention, Stacks 07SD, so that the limit `X` is the one
> Stacks 07SF constructs). Then the category of finitely
> presented `𝒪_X`-modules is the colimit of the categories of finitely presented
> `𝒪_{X_i}`-modules: inverse image along the projections `X ⟶ X_i` is
>
> 1. faithful in the colimit sense: two morphisms on a stage with equal inverse images to `X` have
>    equal inverse images to a later stage;
> 2. full in the colimit sense: a morphism between inverse images to `X` is, at a later stage, the
>    restriction along `X ⟶ X_j` of a morphism between the inverse images to `X_j`;
> 3. essentially surjective in the colimit sense: every finitely presented `𝒪_X`-module is the
>    inverse image of a finitely presented module on some stage.
>
> The index category is any cofiltered category in the universe of the site; no size bound is
> imposed on it.

```lean
theorem finitePresentationModule_isColimit_of_isLimit [IsCofiltered I]
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (hQc : ∀ i, IsQuasiCompactSpace B S hS (D.obj i))
    (hQs : ∀ i, IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i))
    (hc : IsLimit c) (hL : SiteContainsBaseChangeLimits B S hS D) :
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

**`AlgebraicGeometry.Space.exists_isFiniteLocallyFreeOnSite_stage_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean#L89). The attribute's comment: “(1)”.

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

**`AlgebraicGeometry.Space.exists_isInvertibleModule_stage_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FiniteLocallyFreeStageModel.lean#L111). The attribute's comment: “(2)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
