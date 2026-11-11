---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isAffine_etale_chart_square_at_point, AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections, AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_of_isFlatOverAt, AlgebraicGeometry.Space.exists_isAffine_etale_chart_square_along_fibre, AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_along_fibre, AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_along_fibre_of_isFlatOverAtPoint
statement: formalized
proof: formalized
---

# 77.5 Flat finitely presented modules

Section 77.5 of the Stacks Project, [Tag 0CVX](https://stacks.math.columbia.edu/tag/0CVX). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CVY, a proposition

[Tag 0CVY](https://stacks.math.columbia.edu/tag/0CVY) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAffine_etale_chart_square_at_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSections.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSections.lean#L222). The attribute's comment: “the commutative diagram of pointed schemes of the conclusion — affine étale charts of the source and of the target, through the given point and through its image, with a morphism between them over f — and nothing of the projectivity of the sections, which is the case of schemes, Tag 05ID”.

> **Stacks Project, Tag 0CVY: the diagram of the conclusion.** Every point `x` of the source
> of a morphism `f : X ⟶ Y` of algebraic spaces over `S` lies in the image of a commuting square
> of étale scheme charts
>
> ```
> (X, x) ←—— (U, x')
>   |          |
>   ↓          ↓
> (Y, f x) ←— (V, y')
> ```
>
> whose two charts `U` and `V` are **affine**, through a point `x'` of `U` lying over `x`; the
> point `y'` of `V` it induces then lies over the image of `x`.
>
> This is the diagram of pointed schemes which Tag 0CVY asserts, and it is produced here with
> none of the tag's three hypotheses: neither `f` nor any module on `X` enters. What Tag 0CVY
> adds to it is the projectivity of `Γ(U, 𝓕|_U)` over `Γ(V, 𝒪_V)` after a further shrinking,
> which is the case of schemes, Tag 05ID; that is
> `AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections`.
>
> The three conclusions after affineness are, in order: the square of charts commutes over `f`;
> the chart point lies over `x`; and the image of the chart point in the target chart lies over
> the image of `x` in `|Y|`.

```lean
theorem exists_isAffine_etale_chart_square_at_point
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (x : points B S hS X) :
    ∃ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (g : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V)
      (x' : points B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U))),
      IsAffine (chartScheme U) ∧ IsAffine (chartScheme V) ∧
        U.obj.hom ≫ f = yoneda.map g ≫ V.obj.hom ∧
        pointsMap B S hS _ U.obj.hom x' = x ∧
        pointsMap B S hS _ V.obj.hom (pointsMap B S hS _ (yoneda.map g) x') =
          pointsMap B S hS X f x
```

**`AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSections.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSections.lean#L367). The attribute's comment: “the full conclusion — the pointed affine étale diagram and the projectivity of the sections — with the case of schemes, Tag 05ID, supplied by exists\_isAffine\_etale\_hom\_projective\_sections, and with the tag's conditions (2) and (3) on the module in their étale-chartwise form”.

> **Stacks Project, Tag 0CVY.** Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over `S`, let `F` be an `𝒪_X`-module and let `x` be a point of `|X|`. Assume
>
> 1. `f` is locally of finite presentation (`hfp`, Stacks 03XP part (1));
> 2. `F` is quasi-coherent and of finite presentation (`hqc`, `hFfp`), chartwise: its
>    restriction to every étale scheme chart of `X` is;
> 3. `F` is flat at `x` over `Y` (`hflat`), chartwise: on every commuting square of étale charts
>    and at every point of the source chart over `x`, the restriction of `F` to the source chart
>    is flat over the target chart there.
>
> Then there are an étale chart `U` of `X`, an étale chart `V` of `Y`, affine objects `X'`, `Y'`
> of the site with étale morphisms `p : X' ⟶ U` and `q : Y' ⟶ V`, a morphism `k : X' ⟶ Y'` and a
> point `x''` of `|X'|` such that the composites `X' → X` and `Y' → Y` are étale, the square
> commutes over `f`, `x''` lies over `x`, its image in `|Y'|` lies over the image of `x`, and the
> sections `Γ(X', p^*(F|_U))` form a projective `Γ(Y', 𝒪_{Y'})`-module.
>
> The conclusion is the conclusion of Tag 0CVY, with no clause dropped, and nothing is assumed
> beyond the tag's own hypotheses. The source's proof of Tag 0CVY is the remark that the
> statement reduces to the case of schemes, Tag 05ID; that case, read inside the big fppf site,
> is `AlgebraicGeometry.Space.exists_isAffine_etale_hom_projective_sections`. See the module
> docstring on this, and on why the module of the conclusion is named as a pullback of a chart
> restriction.
>
> The hypotheses (2) and (3) are stated chartwise, which is how this development states these
> conditions for a module on an algebraic space: compare
> `AlgebraicGeometry.Space.IsFlatOver`, the definition of Stacks 05VV, which is the chartwise
> condition on every commuting square of étale charts. They are not weakenings: the chartwise
> form is one of the equivalent conditions of Stacks 05VU, which the source's definition
> Stacks 05VV names.
>
> Everything in the conclusion except the projectivity comes from
> `AlgebraicGeometry.Space.exists_isAffine_etale_chart_square_at_point`, which is unconditional;
> the hypotheses are used only to feed the case of schemes.

```lean
theorem exists_isAffine_etale_charts_projective_sections
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (F : Modules.{u, u} B S hS X hX) (x : points B S hS X)
    (hfp : IsLocallyOfFinitePresentation B S hS f)
    (hqc : ∀ U : SmallEtale B S hS X, (restrictToChart B S hS hX F U).IsQuasicoherent)
    (hFfp : ∀ U : SmallEtale B S hS X, (restrictToChart B S hS hX F U).IsFinitePresentation)
    (hflat : ∀ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (g : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V)
      (x' : points B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U))),
      U.obj.hom ≫ f = yoneda.map g ≫ V.obj.hom →
      pointsMap B S hS _ U.obj.hom x' = x →
      AlgebraicGeometry.IsFlatOverAt
        (LocallyRingedSpace.forgetToSheafedSpace.map
          ((BigFppfOver.toScheme B S hS).map g).toLRSHom)
        (restrictToChart B S hS hX F U) (pointsToScheme B S hS _ x')) :
    ∃ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (U' E' : BigFppfOver B S hS)
      (p : U' ⟶ (SmallEtale.toOver B S hS X).obj U)
      (q : E' ⟶ (SmallEtale.toOver B S hS Y).obj V) (k : U' ⟶ E')
      (x'' : points B S hS (yoneda.obj U')),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map p ≫ U.obj.hom) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map q ≫ V.obj.hom) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj U') ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj E') ∧
      (yoneda.map p ≫ U.obj.hom) ≫ f = yoneda.map k ≫ yoneda.map q ≫ V.obj.hom ∧
      pointsMap B S hS _ (yoneda.map p ≫ U.obj.hom) x'' = x ∧
      pointsMap B S hS _ (yoneda.map q ≫ V.obj.hom)
          (pointsMap B S hS _ (yoneda.map k) x'') = pointsMap B S hS X f x ∧
      (let M := (Scheme.Modules.pullback ((BigFppfOver.toScheme B S hS).map p)).obj
           (restrictToChart B S hS hX F U)
       letI : Module Γ((BigFppfOver.toScheme B S hS).obj E', ⊤) Γ(M, ⊤) :=
         Module.compHom Γ(M, ⊤) ((BigFppfOver.toScheme B S hS).map k).appTop.hom
       Module.Projective Γ((BigFppfOver.toScheme B S hS).obj E', ⊤) Γ(M, ⊤))
```

**`AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_of_isFlatOverAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSections.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSections.lean#L435).

> **Stacks Project, Tag 0CVY.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`
> which is locally of finite presentation, let `𝓕` be an `𝒪_X`-module which is quasi-coherent and
> of finite presentation on every étale chart, and let `x` be a point of `X` at which `𝓕` is flat
> over `Y`. Then `x` lies in the image of a commuting square of étale charts, refined by affine
> objects `U'` of `X` and `E'` of `Y` of the site, through a point of `U'`, such that
> `Γ(U', 𝓕|_{U'})` is a projective `Γ(E', 𝒪_{E'})`-module.
>
> This is `AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections`, whose
> proof feeds the case of schemes, Tag 05ID, through
> `AlgebraicGeometry.Space.exists_isAffine_etale_hom_projective_sections`.

```lean
theorem exists_isAffine_etale_charts_projective_sections_of_isFlatOverAt
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (F : Modules.{u, u} B S hS X hX) (x : points B S hS X)
    (hfp : IsLocallyOfFinitePresentation B S hS f)
    (hqc : ∀ U : SmallEtale B S hS X, (restrictToChart B S hS hX F U).IsQuasicoherent)
    (hFfp : ∀ U : SmallEtale B S hS X, (restrictToChart B S hS hX F U).IsFinitePresentation)
    (hflat : ∀ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (g : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V)
      (x' : points B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U))),
      U.obj.hom ≫ f = yoneda.map g ≫ V.obj.hom →
      pointsMap B S hS _ U.obj.hom x' = x →
      AlgebraicGeometry.IsFlatOverAt
        (LocallyRingedSpace.forgetToSheafedSpace.map
          ((BigFppfOver.toScheme B S hS).map g).toLRSHom)
        (restrictToChart B S hS hX F U) (pointsToScheme B S hS _ x')) :
    ∃ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (U' E' : BigFppfOver B S hS)
      (p : U' ⟶ (SmallEtale.toOver B S hS X).obj U)
      (q : E' ⟶ (SmallEtale.toOver B S hS Y).obj V) (k : U' ⟶ E')
      (x'' : points B S hS (yoneda.obj U')),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map p ≫ U.obj.hom) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map q ≫ V.obj.hom) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj U') ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj E') ∧
      (yoneda.map p ≫ U.obj.hom) ≫ f = yoneda.map k ≫ yoneda.map q ≫ V.obj.hom ∧
      pointsMap B S hS _ (yoneda.map p ≫ U.obj.hom) x'' = x ∧
      pointsMap B S hS _ (yoneda.map q ≫ V.obj.hom)
          (pointsMap B S hS _ (yoneda.map k) x'') = pointsMap B S hS X f x ∧
      (let M := (Scheme.Modules.pullback ((BigFppfOver.toScheme B S hS).map p)).obj
           (restrictToChart B S hS hX F U)
       letI : Module Γ((BigFppfOver.toScheme B S hS).obj E', ⊤) Γ(M, ⊤) :=
         Module.compHom Γ(M, ⊤) ((BigFppfOver.toScheme B S hS).map k).appTop.hom
       Module.Projective Γ((BigFppfOver.toScheme B S hS).obj E', ⊤) Γ(M, ⊤))
```

## Tag 0CVZ, a lemma

[Tag 0CVZ](https://stacks.math.columbia.edu/tag/0CVZ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAffine_etale_chart_square_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSectionsAlongFibre.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSectionsAlongFibre.lean#L267). The attribute's comment: “the affine étale diagram covering the fibre — affine étale charts of the source and of the target with a morphism between them over f, through a point of the target chart over y and with the source chart covering the fibre — and nothing of the projectivity of the sections, which is the case of schemes, Tag 05KW”.

> **Stacks Project, Tag 0CVZ: the diagram of the conclusion.** Let `f : X ⟶ Y` be a
> quasi-compact morphism of algebraic spaces over `S` and let `y` be a point of `|Y|`. Then there
> is a commuting square of étale scheme charts
>
> ```
> X ←—— U
> |     |
> ↓     ↓
> Y ←—— V
> ```
>
> whose two charts `U` and `V` are **affine**, together with a point `y'` of `|V|` lying over `y`,
> such that the fibre `F = f^{-1}({y})` is contained in the image of `|U| → |X|`. Moreover every
> point of `F` is the image of a point of `|U|` lying over `y'`.
>
> This is the diagram of Tag 0CVZ, produced with none of the tag's hypotheses on the module and
> with only quasi-compactness of `f`, which is part of the tag's hypothesis (1) and is what makes
> `F` quasi-compact. What Tag 0CVZ adds to it is the projectivity of `Γ(U, 𝓕|_U)` over
> `Γ(V, 𝒪_V)` after a further shrinking, which is the case of schemes, Tag 05KW; that is
> `AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_along_fibre`.
>
> The clauses after affineness are, in order: the square of charts commutes over `f`; the chart
> point lies over `y`; the fibre is contained in the image of the source chart; and the sharpened
> form of that containment, by points of the source chart lying over `y'`.

```lean
theorem exists_isAffine_etale_chart_square_along_fibre
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsQuasiCompact B S hS f) (y : points B S hS Y) :
    ∃ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (k : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V)
      (y' : points B S hS (yoneda.obj ((SmallEtale.toOver B S hS Y).obj V))),
      IsAffine (chartScheme U) ∧ IsAffine (chartScheme V) ∧
        U.obj.hom ≫ f = yoneda.map k ≫ V.obj.hom ∧
        pointsMap B S hS _ V.obj.hom y' = y ∧
        {x : points B S hS X | pointsMap B S hS X f x = y} ⊆
          Set.range (pointsMap B S hS _ U.obj.hom) ∧
        ∀ x : points B S hS X, pointsMap B S hS X f x = y →
          ∃ x' : points B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U)),
            pointsMap B S hS _ U.obj.hom x' = x ∧
            pointsMap B S hS _ (yoneda.map k) x' = y'
```

**`AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSectionsAlongFibre.lean, line 456](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSectionsAlongFibre.lean#L456). The attribute's comment: “the full conclusion — the affine étale diagram covering the fibre and the projectivity of the sections — with quasi-coherence and the tag's conditions (2) and (3) on the module in their étale-chartwise form, for a consumer holding chart data; the case of schemes, Tag 05KW, is discharged inside the big fppf site”.

> **Stacks Project, Tag 0CVZ.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`,
> let `𝓕` be an `𝒪_X`-module and let `y` be a point of `|Y|`. Assume
>
> 1. `f` is of finite presentation (`hfp`, Stacks 03XP part (3));
> 2. `𝓕` is quasi-coherent and of finite presentation (`hqc`, `h𝓕fp`), chartwise: its restriction
>    to every étale scheme chart of `X` is;
> 3. `𝓕` is flat over `Y` at every point of the fibre `F = f^{-1}({y})` (`hflat`), chartwise: on
>    every commuting square of étale charts and at every point of the source chart lying over a
>    point of `F`, the restriction of `𝓕` to the source chart is flat over the target chart there.
>
> Then there are an étale chart `Z` of `X`, an étale chart `V` of `Y`, affine objects `X'`, `Y'`
> of the site with étale morphisms `p : X' ⟶ Z` and `q : Y' ⟶ V`, a morphism `k : X' ⟶ Y'` and a
> point `y'` of `|Y'|` such that the composites `X' → X` and `Y' → Y` are étale, the square
> commutes over `f`, `y'` lies over `y`, the fibre `F` is contained in the image of `|X'| → |X|`,
> and the sections `Γ(X', p^*(𝓕|_Z))` form a projective `Γ(Y', 𝒪_{Y'})`-module.
>
> The conclusion is the conclusion of Tag 0CVZ, with no clause dropped, and nothing is granted as
> a hypothesis: everything except the projectivity is
> `AlgebraicGeometry.Space.exists_isAffine_etale_chart_square_along_fibre`, and the projectivity
> is the case of schemes, Tag 05KW, read inside the site by
> `AlgebraicGeometry.Space.exists_isAffine_etale_hom_projective_sections_along_fibre`.
>
> Quasi-coherence and the hypotheses (2) and (3) are stated chartwise here; compare
> `AlgebraicGeometry.Space.IsFlatOver`, the definition of Stacks 05VV. This is **not** the
> source's reading of them, and it is not comparable to it: chartwise quasi-coherence and
> chartwise finite presentation are weaker than the source's conditions on `X` itself, while the
> chartwise flatness asked here is the every-chart-square form, which is strictly more than
> Stacks 05VV asks at a point. The statement at the source's own three hypotheses, with no
> chartwise condition on the module anywhere, is
> `exists_isAffine_etale_charts_projective_sections_along_fibre_of_isFlatOverAtPoint`, which is
> proved from this one. See the module docstring for the three transfers between the readings.

```lean
theorem exists_isAffine_etale_charts_projective_sections_along_fibre
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (𝓕 : Modules.{u, u} B S hS X hX) (y : points B S hS Y)
    (hfp : IsFinitePresentation B S hS f)
    (hqc : ∀ U : SmallEtale B S hS X, (restrictToChart B S hS hX 𝓕 U).IsQuasicoherent)
    (h𝓕fp : ∀ U : SmallEtale B S hS X, (restrictToChart B S hS hX 𝓕 U).IsFinitePresentation)
    (hflat : ∀ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (g : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V)
      (x' : points B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U))),
      U.obj.hom ≫ f = yoneda.map g ≫ V.obj.hom →
      pointsMap B S hS X f (pointsMap B S hS _ U.obj.hom x') = y →
      AlgebraicGeometry.IsFlatOverAt
        (LocallyRingedSpace.forgetToSheafedSpace.map
          ((BigFppfOver.toScheme B S hS).map g).toLRSHom)
        (restrictToChart B S hS hX 𝓕 U) (pointsToScheme B S hS _ x')) :
    ∃ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (X' Y' : BigFppfOver B S hS)
      (p : X' ⟶ (SmallEtale.toOver B S hS X).obj U)
      (q : Y' ⟶ (SmallEtale.toOver B S hS Y).obj V) (k : X' ⟶ Y')
      (y' : points B S hS (yoneda.obj Y')),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map p ≫ U.obj.hom) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map q ≫ V.obj.hom) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj X') ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj Y') ∧
      (yoneda.map p ≫ U.obj.hom) ≫ f = yoneda.map k ≫ yoneda.map q ≫ V.obj.hom ∧
      pointsMap B S hS _ (yoneda.map q ≫ V.obj.hom) y' = y ∧
      {x : points B S hS X | pointsMap B S hS X f x = y} ⊆
        Set.range (pointsMap B S hS _ (yoneda.map p ≫ U.obj.hom)) ∧
      (let M := (Scheme.Modules.pullback ((BigFppfOver.toScheme B S hS).map p)).obj
           (restrictToChart B S hS hX 𝓕 U)
       letI : Module Γ((BigFppfOver.toScheme B S hS).obj Y', ⊤) Γ(M, ⊤) :=
         Module.compHom Γ(M, ⊤) ((BigFppfOver.toScheme B S hS).map k).appTop.hom
       Module.Projective Γ((BigFppfOver.toScheme B S hS).obj Y', ⊤) Γ(M, ⊤))
```

**`AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_along_fibre_of_isFlatOverAtPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSectionsAlongFibre.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFinitePresentationProjectiveSectionsAlongFibre.lean#L619). The attribute's comment: “the full conclusion — the affine étale diagram covering the fibre and the projectivity of the sections — at the tag's own three conditions throughout: the module quasi-coherent and of finite presentation on the small étale site, and condition (3) in the some-chart form which Stacks 05VV gives it; no chartwise condition on the module appears, and the case of schemes, Tag 05KW, is discharged inside the big fppf site”.

> **Stacks Project, Tag 0CVZ.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`,
> let `𝓕` be a quasi-coherent `𝒪_X`-module and let `y` be a point of `|Y|` with fibre
> `F = f^{-1}({y}) ⊆ |X|`. Assume
>
> 1. `f` is of finite presentation (`hfp`, Stacks 03XP part (3));
> 2. `𝓕` is of finite presentation (`h𝓕fp`), on the small étale site of `X`, which is the
>    property Stacks 05VR item (l) names;
> 3. `𝓕` is flat over `Y` at every point of `F` (`hflat`), in the some-chart sense of
>    Stacks 05VV, which is condition (1) of Stacks 05VU.
>
> Then there are an étale chart `Z` of `X`, an étale chart `V` of `Y`, affine objects `X'`, `Y'`
> of the site with étale morphisms `p : X' ⟶ Z` and `q : Y' ⟶ V`, a morphism `k : X' ⟶ Y'` and a
> point `y'` of `|Y'|` such that the composites `X' → X` and `Y' → Y` are étale, the square
> commutes over `f`, `y'` lies over `y`, the fibre `F` is contained in the image of `|X'| → |X|`,
> and the sections `Γ(X', p^*(𝓕|_Z))` form a projective `Γ(Y', 𝒪_{Y'})`-module.
>
> **Every hypothesis here is the source's own, and no chartwise condition on the module appears.**
> This is `AlgebraicGeometry.Space.exists_isAffine_etale_charts_projective_sections_along_fibre`
> with its three chartwise hypotheses on the module discharged: quasi-coherence on the small étale
> site gives chartwise quasi-coherence by
> `AlgebraicGeometry.Space.isQuasicoherent_restrictToChart`, finite presentation on the small
> étale site gives chartwise finite presentation by
> `AlgebraicGeometry.Space.isFinitePresentationOnCharts_of_isFinitePresentationOnSite`, and the
> some-chart form of condition (3) gives the every-chart form by Stacks 05VU,
> `AlgebraicGeometry.Space.isFlatOverAtOnChartDiagram_of_isFlatOverAtPoint`.

```lean
theorem exists_isAffine_etale_charts_projective_sections_along_fibre_of_isFlatOverAtPoint
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (𝓕 : Modules.{u, u} B S hS X hX) (y : points B S hS Y)
    (hfp : IsFinitePresentation B S hS f)
    (hqc : 𝓕.IsQuasicoherentOnSite)
    (h𝓕fp : SheafOfModules.IsFinitePresentationOnSite 𝓕)
    (hflat : ∀ x : points B S hS X, pointsMap B S hS X f x = y →
      IsFlatOverAtPoint B S hS hX f 𝓕 x) :
    ∃ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
      (X' Y' : BigFppfOver B S hS)
      (p : X' ⟶ (SmallEtale.toOver B S hS X).obj U)
      (q : Y' ⟶ (SmallEtale.toOver B S hS Y).obj V) (k : X' ⟶ Y')
      (y' : points B S hS (yoneda.obj Y')),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map p ≫ U.obj.hom) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (yoneda.map q ≫ V.obj.hom) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj X') ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj Y') ∧
      (yoneda.map p ≫ U.obj.hom) ≫ f = yoneda.map k ≫ yoneda.map q ≫ V.obj.hom ∧
      pointsMap B S hS _ (yoneda.map q ≫ V.obj.hom) y' = y ∧
      {x : points B S hS X | pointsMap B S hS X f x = y} ⊆
        Set.range (pointsMap B S hS _ (yoneda.map p ≫ U.obj.hom)) ∧
      (let M := (Scheme.Modules.pullback ((BigFppfOver.toScheme B S hS).map p)).obj
           (restrictToChart B S hS hX 𝓕 U)
       letI : Module Γ((BigFppfOver.toScheme B S hS).obj Y', ⊤) Γ(M, ⊤) :=
         Module.compHom Γ(M, ⊤) ((BigFppfOver.toScheme B S hS).map k).appTop.hom
       Module.Projective Γ((BigFppfOver.toScheme B S hS).obj Y', ⊤) Γ(M, ⊤))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.5, Tag 0CVX](https://stacks.math.columbia.edu/tag/0CVX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
