---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_affine_etale_completeDevissage_cover, AlgebraicGeometry.Space.exists_affineChart_hasCompleteDevissageCover, AlgebraicGeometry.Space.isOpen_flatLocus_setFibre, AlgebraicGeometry.Space.isWeaklyAssociatedPoint_tensor_modulePullback_iff_of_finiteType, AlgebraicGeometry.Space.weaklyAssociatedPoints_tensor_modulePullback_eq_inter_preimage, AlgebraicGeometry.Space.isOpen_flatLocus_of_isSurjectiveChart, AlgebraicGeometry.Space.isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart, AlgebraicGeometry.Space.flatLocus
statement: formalized
proof: formalized
---

# 77.4 Flat finite type modules

Section 77.4 of the Stacks Project, [Tag 0CVJ](https://stacks.math.columbia.edu/tag/0CVJ). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CWJ, a lemma

[Tag 0CWJ](https://stacks.math.columbia.edu/tag/0CWJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_etale_completeDevissage_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/CompleteDevissageEtaleCover.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/CompleteDevissageEtaleCover.lean#L318). The attribute's comment: “the full statement, proved from the source's hypotheses; nothing is assumed”.

> **Stacks Project, Tag 0CWJ.** Let `X ⟶ Y` be a finite type morphism of algebraic spaces over
> `S`, let `F` be a finite type quasi-coherent `𝒪_X`-module and let `y` be a point of `Y`. There
> are an étale morphism `q : (Y', y') ⟶ (Y, y)` with `Y'` an affine scheme, and étale morphisms
> `hᵢ : Wᵢ ⟶ X_{Y'} = Y' ×_Y X`, `i = 1, …, n`, from schemes `Wᵢ`, such that for each `i` the
> pullback `Fᵢ` of `F` to `Wᵢ` (its restriction to the étale chart `Wᵢ ⟶ X_{Y'} ⟶ X`) has a
> complete dévissage `Fᵢ/Wᵢ/Y'` over `y'`, the morphism `Wᵢ ⟶ Y'` being the `aᵢ` with
> `hᵢ ≫ pr₁ = aᵢ`, and such that every point of `X_{Y'}` lying over `y'` is in the image of some
> `hᵢ`, that is, `|(X_{Y'})_{y'}| ⊆ ⋃ hᵢ(Wᵢ)`.

```lean
theorem exists_affine_etale_completeDevissage_cover (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsFiniteType B S hS f) (F : Modules.{u, u} B S hS X hX)
    (hFq : F.IsQuasicoherentOnSite) (hFt : SheafOfModules.IsFiniteTypeOnSite F)
    (y : points B S hS Y) :
    ∃ (Y' : BigFppfOver B S hS) (q : yoneda.obj Y' ⟶ Y) (y' : points B S hS (yoneda.obj Y')),
      IsAffine ((BigFppfOver.toScheme B S hS).obj Y') ∧ IsEtale B S hS q ∧
      pointsMap B S hS (yoneda.obj Y') q y' = y ∧
      ∃ (n : ℕ) (W : Fin n → BigFppfOver B S hS)
        (h : ∀ i, yoneda.obj (W i) ⟶ pullback q f) (_ : ∀ i, IsEtale B S hS (h i))
        (hW : ∀ i, IsEtaleChart B S hS X (CostructuredArrow.mk (h i ≫ pullback.snd q f)))
        (a : ∀ i, W i ⟶ Y') (_ : ∀ i, h i ≫ pullback.fst q f = yoneda.map (a i))
        (hl : ∀ i, LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map (a i)))
        (hq : ∀ i, (restrictToChart B S hS hX F ⟨_, hW i⟩).IsQuasicoherent)
        (ht : ∀ i, (restrictToChart B S hS hX F ⟨_, hW i⟩).IsFiniteType),
        (∀ i, Nonempty (@CompleteDevissage _ _ ((BigFppfOver.toScheme B S hS).map (a i))
          (restrictToChart B S hS hX F ⟨_, hW i⟩) (pointsToScheme B S hS Y' y')
          (hl i) (hq i) (ht i))) ∧
        ∀ x : points B S hS (pullback q f),
          pointsMap B S hS _ (pullback.fst q f) x = y' →
            ∃ (i : Fin n) (z : points B S hS (yoneda.obj (W i))),
              pointsMap B S hS _ (h i) z = x
```

**`AlgebraicGeometry.Space.exists_affineChart_hasCompleteDevissageCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ExistenceCompleteDevissage.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ExistenceCompleteDevissage.lean#L183). The attribute's comment: “the elementary étale neighbourhood of the point, the covering family and its dévissages are delivered for the affine étale chart of the base change rather than for the base change as an algebraic space: the sources of the covering étale morphisms carry no size bound, so they are not objects of the big fppf site”.

> **Stacks Project, Tag 0CWJ**, delivered at an affine étale chart of the base change.
>
> Let `X ⟶ Y` be a finite type morphism of algebraic spaces over `S`, let `F` be a finite type
> quasi-coherent `𝒪_X`-module, and let `y` be a point of `Y`. Then there are
>
> * an object `Y₁` of the site whose scheme is affine, an étale morphism `q : Y₁ ⟶ Y`, and a
>   point `w` of `Y₁` above `y` — the source's `(Y', y') ⟶ (Y, y)` before the passage to an
>   elementary étale neighbourhood;
> * an étale chart `U` of `X` whose scheme is affine, and a morphism `ĝ : U ⟶ Y₁` of the site
>   making the square over `q` commute, such that the induced morphism from `U` to the base
>   change `X ×_Y Y₁` is surjective on points — the source's affine surjective étale cover `X'`
>   of `X`, after the reduction to an affine base;
> * the morphism of schemes underlying `ĝ` is locally of finite type and quasi-compact, and the
>   conclusion of Stacks 05HU holds for it, for the restriction of `F` to `U`, and for the
>   point of the scheme of `Y₁` determined by `w`.
>
> The finitely many étale morphisms `hᵢ : Wᵢ ⟶ X_{Y'}` of the source's conclusion, their
> complete dévissages and the inclusion of the fibre in the union of their images are bound
> inside `AlgebraicGeometry.HasCompleteDevissageCover`. See the implementation notes of this
> file for why they are delivered at the chart `U` rather than at `X_{Y'}`.

```lean
theorem exists_affineChart_hasCompleteDevissageCover (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsFiniteType B S hS f) (F : Modules.{u, u} B S hS X hX)
    (hFq : F.IsQuasicoherentOnSite) (hFt : SheafOfModules.IsFiniteTypeOnSite F)
    (y : points B S hS Y) :
    ∃ (Y₁ : BigFppfOver B S hS) (q : yoneda.obj Y₁ ⟶ Y) (U : SmallEtale B S hS X)
      (ĝ : U.obj.left ⟶ Y₁) (hsq : yoneda.map ĝ ≫ q = U.obj.hom ≫ f)
      (w : points B S hS (yoneda.obj Y₁)),
      IsAffine ((BigFppfOver.toScheme B S hS).obj Y₁) ∧
      IsAffine (etaleChartScheme B S hS U) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q ∧
      pointsMap B S hS (yoneda.obj Y₁) q w = y ∧
      IsSurjective B S hS (Limits.pullback.lift (yoneda.map ĝ) U.obj.hom hsq) ∧
      LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map ĝ) ∧
      QuasiCompact ((BigFppfOver.toScheme B S hS).map ĝ) ∧
      HasCompleteDevissageCover ((BigFppfOver.toScheme B S hS).map ĝ)
        (restrictToChart B S hS hX F U) (pointsToScheme B S hS Y₁ w)
```

## Tag 0CWK, a lemma

[Tag 0CWK](https://stacks.math.columbia.edu/tag/0CWK) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_flatLocus_setFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleFibre.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleFibre.lean#L453). The attribute's comment: “the statement in full, at the Stacks erratum: the point y of the target has a quasi-compact field-valued representative, condition (5) of Stacks 03JV, which holds at every point of a decent algebraic space. The tag as published asks nothing of y and is false that way, refuted by the theorem Stacks.Examples.NonOpenFlatLocusSpace.not\_isOpen\_flatLocus\_setFibre\_of\_free\_shift of StacksFrontier/Examples/Flatness/NonOpenFlatLocusSpace.lean”.

> **Stacks 0CWK.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, let `F` be a quasi-coherent `𝒪_X`-module of finite type and let `y` be
> a point of `|Y|` with a quasi-compact field-valued representative. In the set-theoretic fibre
> `f^{-1}({y}) ⊆ |X|`, with its subspace topology, the points at which `F` is flat over `Y` form
> an open subset.
>
> The hypothesis on `y` is condition (5) of Stacks 03JV; by Stacks 0AC8 it provides an étale
> scheme chart of `Y` with exactly one point above `y`, which is what makes the fibre of a chart
> of `X` map openly onto the set-theoretic fibre. It holds at every point of a decent algebraic
> space, which is `AlgebraicGeometry.Space.isOpen_flatLocus_setFibre_of_isDecentSpace`.
>
> The hypothesis on `y` corrects Stacks 0CWK, which as published asks nothing of `y`; the corrected
> statement adds condition (5) of Stacks 03JV at `y`. The published form is false:
> `Stacks.Examples.NonOpenFlatLocusSpace.not_isOpen_flatLocus_setFibre_of_free_shift` takes no
> hypotheses and produces a big fppf site, an algebraic space `Y = Spec A/ℤ` for
> `A = ℚ[t, u_i]/((t - i)u_i)`, the étale quotient morphism `f : Spec A ⟶ Y`, the cyclic module
> `A ⧸ (u_i : i ≥ 1)` on its source and a point `y` of `|Y|`, satisfying every hypothesis of this
> theorem except the one on `y`, and for which the conclusion below is false. Its companion
> `Stacks.Examples.NonOpenFlatLocusSpace.not_hasQuasiCompactFieldRepresentative_ybase` deduces from
> that failure that the point it produces has no quasi-compact field-valued representative, so the
> hypothesis on `y` is exactly what the source is missing.
>
> Flatness at a point is `AlgebraicGeometry.Space.flatLocus`, the some-chart form of Stacks 05VV
> part (1), which Stacks 05VU shows is independent of the chart.

```lean
theorem isOpen_flatLocus_setFibre (f : X ⟶ Y)
    (Fm : Modules.{u, u} B S hS X.1 X.2) [Fm.IsQuasicoherentOnSite]
    (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hft : IsFiniteTypeOnCharts B S hS X.2 Fm)
    (y : points B S hS Y.1) (hy : HasQuasiCompactFieldRepresentative B S hS Y.1 y) :
    IsOpen {x : (pointsMap B S hS X.1 f.hom ⁻¹' {y} : Set (points B S hS X.1)) |
      (x : points B S hS X.1) ∈ flatLocus B S hS X.2 f.hom Fm}
```

## Tag 0CVK, a lemma

[Tag 0CVK](https://stacks.math.columbia.edu/tag/0CVK) in the Stacks Project.

**`AlgebraicGeometry.Space.isWeaklyAssociatedPoint_tensor_modulePullback_iff_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/BourbakiFiniteTypePointwise.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/BourbakiFiniteTypePointwise.lean#L144).

> Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type, let `x` be a point of `|X|`, let `𝓕` be a finite type quasi-coherent
> `𝒪_X`-module and let `𝓖` be a quasi-coherent `𝒪_Y`-module.  If `𝓕` is flat at `x` over `Y`, then
> `x` is weakly associated to `𝓕 ⊗_{𝒪_X} f^*𝓖` if and only if the image of `x` is weakly associated
> to `𝓖` and `x` lies in the relative weak assassin `WeakAss_{X/Y}(𝓕)` of Stacks 0CV0 — which, the
> fibres of `f` being locally Noetherian by Stacks 0CUY, is the set the source writes
> `Ass_{X/Y}(𝓕)`.
>
> This is the source's proof.  A commuting square of étale scheme charts over `f` through `x`
> exists by `AlgebraicGeometry.Space.exists_chartDiagram_chartSchemeToPoints_eq`; on it the two
> sides of the formula become the Zariski conditions of the scheme case by
> `AlgebraicGeometry.Space.isWeaklyAssociatedPoint_tensor_modulePullback_iff_of_chartDiagram`,
> whose comparison of `(𝓕 ⊗_{𝒪_X} f^*𝓖)|_U` with `𝓕|_U ⊗_{𝒪_U} q^*(𝓖|_V)` is
> `AlgebraicGeometry.Space.nonempty_restrictToChart_tensor_modulePullback_chartDiagram` and whose
> identification of the relative assassins is the two chart-diagram comparisons of
> `StacksFrontier.AlgebraicGeometry.Divisors.MorphismWeaklyAssociated.ChartDiagramRelativeAssassin`
> joined by Stacks 05F2, available because the chart morphism inherits local finite type from `f`.
> The chart restrictions are quasi-coherent and, on the source, of finite type, the chart morphism
> is locally of finite type, and the chart restriction of `𝓕` is flat over the target chart at the
> chart point by Stacks 05VU; so the scheme case,
> `Stacks.Divisors.isWeaklyAssociatedPoint_tensorPullback_iff_of_finiteType`, applies with no
> further hypothesis.

```lean
theorem isWeaklyAssociatedPoint_tensor_modulePullback_iff_of_finiteType (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (G : Modules.{u, u} B S hS Y.1 Y.2)
    [F.IsQuasicoherentOnSite] [F.IsFiniteType] [G.IsQuasicoherentOnSite]
    (x : points B S hS X.1)
    (hflat : IsFlatOverAtPoint B S hS X.2 f.hom F x) :
    IsWeaklyAssociatedPoint B S hS X (F ⊗ (modulePullback B S hS f).obj G) x ↔
      (IsWeaklyAssociatedPoint B S hS Y G (pointsMap B S hS X.1 f.hom x) ∧
        x ∈ relativeWeaklyAssociatedPoints B S hS f F)
```

## Tag 0CVL, a lemma

[Tag 0CVL](https://stacks.math.columbia.edu/tag/0CVL) in the Stacks Project.

**`AlgebraicGeometry.Space.weaklyAssociatedPoints_tensor_modulePullback_eq_inter_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTensorPullbackFiniteType.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/WeaklyAssociatedTensorPullbackFiniteType.lean#L209). The attribute's comment: “the full set equality, in the intersection-with-a-preimage form the tag writes, under the tag's own assumptions and with the source's own proof: the statement is an immediate consequence of its pointwise form, Stacks 0CVK, proved in its own generality as Space.isWeaklyAssociatedPoint\_tensor\_modulePullback\_iff\_of\_finiteType and is applied here through Space.isBourbakiFormulaAtFlatPoints\_of\_finiteType, the two differing by and\_comm. The sets are Space.relativeWeaklyAssociatedPoints of Stacks 0CV0, the Ass\_\{X/Y}(F) of the tag once the fibres of f are locally Noetherian as they are here by Stacks 0CUY, and Space.weaklyAssociatedPoints of Stacks 0CTX. The tag's flatness assumption hF is used, through Space.isFlatOverAtPoint\_forall\_of\_isFlatOver, to discharge the pointwise flatness side condition of Stacks 0CVK at every point. Nothing beyond the tag's own assumptions is used: every binder of this theorem is one of them, namely f locally of finite type, F quasi-coherent of finite type, G quasi-coherent, and F flat over Y”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S` which is locally of
> finite type, let `F` be a finite type quasi-coherent `𝒪_X`-module which is flat over `Y`, and let
> `G` be a quasi-coherent `𝒪_Y`-module. Then the weakly associated points of `F ⊗_{𝒪_X} f^*G` are
> exactly the points of `Ass_{X/Y}(F)` lying over weakly associated points of `G`.
>
> This is the source's own proof, which is that the statement is an immediate consequence of its
> pointwise form, Stacks 0CVK, available here as
> `AlgebraicGeometry.Space.isBourbakiFormulaAtFlatPoints_of_finiteType`. The tag's flatness
> hypothesis is what makes the pointwise flatness side condition hold at every point, by
> `AlgebraicGeometry.Space.isFlatOverAtPoint_forall_of_isFlatOver`.

```lean
theorem weaklyAssociatedPoints_tensor_modulePullback_eq_inter_preimage (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (G : Modules.{u, u} B S hS Y.1 Y.2)
    [F.IsQuasicoherentOnSite] [F.IsFiniteType] [G.IsQuasicoherentOnSite]
    (hF : IsFlatOver B S hS X.2 f.hom F) :
    weaklyAssociatedPoints B S hS X (F ⊗ (modulePullback B S hS f).obj G) =
      relativeWeaklyAssociatedPoints B S hS f F ∩
        pointsMap B S hS X.1 f.hom ⁻¹' weaklyAssociatedPoints B S hS Y G
```

## Tag 0DLR, a theorem

[Tag 0DLR](https://stacks.math.columbia.edu/tag/0DLR) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_flatLocus_of_isSurjectiveChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartRestrictionFromSite.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartRestrictionFromSite.lean#L145). The attribute's comment: “openness of the locus U, with all three conditions of the statement in the source's own shape: the module quasi-coherent of finite type on the small etale site, and the weakly associated points of the target locally finite on one surjective etale scheme chart”.

> For a morphism `f : X ⟶ Y` of algebraic spaces locally of finite presentation and a module
> which is quasi-coherent and of finite type on the small étale site of `X`, the relative flat locus
> is open in the point space of `X` as soon as the weakly associated points of the scheme of one
> surjective étale chart of `Y` are locally finite there.

```lean
theorem isOpen_flatLocus_of_isSurjectiveChart (f : X.1 ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (hf : IsLocallyOfFinitePresentation B S hS f)
    (hqc : F.IsQuasicoherentOnSite) (hft : SheafOfModules.IsFiniteTypeOnSite F)
    (V₀ : SmallEtale B S hS Y) (hV₀ : IsSurjectiveChart B S hS V₀)
    (h₀ : ∀ v : etaleChartScheme B S hS V₀,
      ∃ W : (etaleChartScheme B S hS V₀).Opens, v ∈ W ∧
        (Stacks.Divisors.schemeWeaklyAssociatedPoints (etaleChartScheme B S hS V₀) ∩
          (W : Set (etaleChartScheme B S hS V₀))).Finite) :
    IsOpen (flatLocus B S hS X.2 f F)
```

**`AlgebraicGeometry.Space.isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartRestrictionFromSite.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartRestrictionFromSite.lean#L164). The attribute's comment: “the locus U cuts out an open subspace of X in the sense of Tag 03BZ, with all three conditions of the statement in the source's own shape, condition (3) read on one surjective etale scheme chart”.

> For a morphism `f : X ⟶ Y` of algebraic spaces locally of finite presentation and a module
> which is quasi-coherent and of finite type on the small étale site of `X`, the relative flat locus
> cuts out an open subspace of `X` as soon as the weakly associated points of the scheme of one
> surjective étale chart of `Y` are locally finite there.

```lean
theorem isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart (f : X.1 ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (hf : IsLocallyOfFinitePresentation B S hS f)
    (hqc : F.IsQuasicoherentOnSite) (hft : SheafOfModules.IsFiniteTypeOnSite F)
    (V₀ : SmallEtale B S hS Y) (hV₀ : IsSurjectiveChart B S hS V₀)
    (h₀ : ∀ v : etaleChartScheme B S hS V₀,
      ∃ W : (etaleChartScheme B S hS V₀).Opens, v ∈ W ∧
        (Stacks.Divisors.schemeWeaklyAssociatedPoints (etaleChartScheme B S hS V₀) ∩
          (W : Set (etaleChartScheme B S hS V₀))).Finite) :
    IsOpenSubspace B S hS (flatLocusOpenSubspace B S hS X.2 f F)
```

**`AlgebraicGeometry.Space.flatLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleLocus.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleLocus.lean#L209). The attribute's comment: “the locus U of the statement: the points of the source at which the module is flat over the target, which is Tag 05VV (1), i.e. clause (1) of Tag 05VU”.

> The relative flat locus of a module on an algebraic space: the set of points `x` of the
> source such that some commuting square of étale scheme charts through `x` witnesses flatness of
> the restricted module over the target chart.

```lean
noncomputable def flatLocus (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X hX) : Set (points B S hS X)
```

**`AlgebraicGeometry.Space.isFinitePresentationOnCharts_flatLocusRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleOnFlatLocus.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleOnFlatLocus.lean#L309). The attribute's comment: “F|\_U is an O\_U-module of finite presentation, for U the open subspace cut out by the flat locus, at all three conditions of the statement in the source's own shape -- the module quasi-coherent of finite type on the small etale site and the weakly associated points of the target locally finite on one surjective etale scheme chart, as the source's proof reads condition (3); the conclusion is read on the etale scheme charts of U, as every property of a module on an algebraic space is in this development”.

> **Stacks 0DLR: `F|_U` is an `𝒪_U`-module of finite presentation.**  For a morphism of
> algebraic spaces locally of finite presentation, a module quasi-coherent of finite type on the
> small étale site and a target whose weakly associated points are locally finite on the scheme of
> one surjective étale chart, the module `F|_U` on the open subspace
> `U = {x ∈ |X| : F flat at x over Y}` is of finite presentation.
>
> All three conditions are the source's own, the local finiteness of the weakly associated points
> of `Y` read on one *surjective* étale scheme chart as the source's proof reads it; the every-chart
> reading the proof consumes is derived from it by
> `AlgebraicGeometry.Space.hasLocallyFiniteWeaklyAssociatedPointsOnCharts_of_isSurjectiveChart`.
>
> The conclusion is read on the étale scheme charts of `U`, as every property of a module on an
> algebraic space is in this development.  The proof is the source's: the condition is étale local,
> so it is enough to read it on one chart of `U` surjective on points, and such a chart may be
> chosen to lie over a chart of `Y` (Tag 02X1), where the scheme-level theorem Stacks 05IK applies;
> the passage back to every chart is
> `AlgebraicGeometry.Space.isFinitePresentation_restrictToChartScheme_of_isSurjective`.

```lean
theorem isFinitePresentationOnCharts_flatLocusRestrict (f : Xs ⟶ Ys)
    (F : Modules.{u, u} B S hS Xs.1 Xs.2) [hqc : F.IsQuasicoherentOnSite]
    (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hft : SheafOfModules.IsFiniteTypeOnSite F) (V₀ : SmallEtale B S hS Ys.1)
    (hV₀ : IsSurjectiveChart B S hS V₀)
    (h₀ : ∀ v : etaleChartScheme B S hS V₀,
      ∃ W : (etaleChartScheme B S hS V₀).Opens, v ∈ W ∧
        (Stacks.Divisors.schemeWeaklyAssociatedPoints (etaleChartScheme B S hS V₀) ∩
          (W : Set (etaleChartScheme B S hS V₀))).Finite) :
    IsFinitePresentationOnCharts B S hS
      (flatLocusSpace B S hS f F
        (isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart B S hS Xs f.hom F hf hqc hft
          V₀ hV₀ h₀)).2
      (flatLocusRestrict B S hS f F
        (isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart B S hS Xs f.hom F hf hqc hft
          V₀ hV₀ h₀))
```

**`AlgebraicGeometry.Space.isFlatOver_flatLocusRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleOnFlatLocus.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFiniteTypeModuleOnFlatLocus.lean#L375). The attribute's comment: “F|\_U is flat over Y along the composite U -> X -> Y, for U the open subspace cut out by the flat locus, at all three conditions of the statement in the source's own shape, condition (3) read on one surjective etale scheme chart of the target; flatness of a module on an algebraic space over the target is Tag 05VV, read on the commuting squares of etale scheme charts”.

> **Stacks 0DLR: `F|_U` is flat over `Y`.**  For a morphism of algebraic spaces locally of
> finite presentation, a module quasi-coherent of finite type on the small étale site and a target
> whose weakly associated points are locally finite on the scheme of one surjective étale chart,
> the module `F|_U` on the open subspace `U = {x ∈ |X| : F flat at x over Y}` is flat over `Y` along
> the composite `U ⟶ X ⟶ Y`, in the sense of Tag 05VV.
>
> All three conditions are the source's own, condition (3) read on one *surjective* étale scheme
> chart of the target as the source's proof reads it.
>
> On a commuting square of étale scheme charts of `U ⟶ Y`, the chart of `U` is a chart of `X` whose
> points all lie in the relative flat locus, so the square witnesses flatness at each of them by
> Stacks 05VU.

```lean
theorem isFlatOver_flatLocusRestrict (f : Xs ⟶ Ys) (F : Modules.{u, u} B S hS Xs.1 Xs.2)
    [hqc : F.IsQuasicoherentOnSite] (hf : IsLocallyOfFinitePresentation B S hS f.hom)
    (hft : SheafOfModules.IsFiniteTypeOnSite F) (V₀ : SmallEtale B S hS Ys.1)
    (hV₀ : IsSurjectiveChart B S hS V₀)
    (h₀ : ∀ v : etaleChartScheme B S hS V₀,
      ∃ W : (etaleChartScheme B S hS V₀).Opens, v ∈ W ∧
        (Stacks.Divisors.schemeWeaklyAssociatedPoints (etaleChartScheme B S hS V₀) ∩
          (W : Set (etaleChartScheme B S hS V₀))).Finite) :
    IsFlatOver B S hS
      (flatLocusSpace B S hS f F
        (isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart B S hS Xs f.hom F hf hqc hft
          V₀ hV₀ h₀)).2
      ((flatLocusSpaceι B S hS f F
        (isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart B S hS Xs f.hom F hf hqc hft
          V₀ hV₀ h₀)).hom ≫ f.hom)
      (flatLocusRestrict B S hS f F
        (isOpenSubspace_flatLocusOpenSubspace_of_isSurjectiveChart B S hS Xs f.hom F hf hqc hft
          V₀ hV₀ h₀))
```

## Tag 0CVW, a lemma

[Tag 0CVW](https://stacks.math.columbia.edu/tag/0CVW) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affineChart_hasFreeSectionsAlongFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ExistenceFreeSectionsAlongFibre.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ExistenceFreeSectionsAlongFibre.lean#L205). The attribute's comment: “the etale neighbourhood, the affine scheme and its free sections are delivered; reduced to the affine etale chart of the target”.

> **Stacks Project, Tag 0CVW**, reduced to the affine étale chart of the target at the
> prescribed point.
>
> Let `f : X ⟶ Y` be a finite type morphism of algebraic spaces over `S`, let `F` be a
> quasi-coherent `𝒪_X`-module whose restriction to every étale chart of `X` is quasi-coherent of
> finite type, and let `y` be a point of `|Y|` at which `F` is flat over `Y` along the whole
> set-theoretic fibre `f^{-1}({y})`. Then there are
>
> * an object `Y₁` of the site whose scheme is affine, an étale morphism `q : Y₁ ⟶ Y` and a
>   point `w` of `Y₁` above `y` — the source's `(Y', y') ⟶ (Y, y)` before the passage to an
>   elementary étale neighbourhood;
> * an étale chart `U` of `X` whose scheme is affine, and a morphism `ĝ : U ⟶ Y₁` of the site
>   making the square over `q` commute, such that the induced morphism from `U` to the base
>   change `X ×_Y Y₁` is surjective on points — the source's affine surjective étale cover `X'`
>   of `X ×_Y Y'`;
> * the morphism of schemes underlying `ĝ` is locally of finite type and quasi-compact, and the
>   conclusion of Stacks 05L1 holds for it, for the restriction of `F` to `U`, and for the point
>   of the scheme of `Y₁` determined by `w` — with the covering clause of that conclusion read
>   on the point space of `X`, where it says that the set-theoretic fibre `f^{-1}({y})` is the
>   image of the fibre of the affine scheme Stacks 05L1 produces.
>
> The hypothesis `hFt` is the source's "`F` of finite type", on the small étale site of `X`.
> The chartwise finite type it gives is
> `AlgebraicGeometry.Space.isFiniteTypeOnCharts_of_isFiniteTypeOnSite`, and chartwise
> quasi-coherence follows from `SheafOfModules.IsQuasicoherentOnSite` by
> `AlgebraicGeometry.Space.isQuasicoherent_restrictToChart`.

```lean
theorem exists_affineChart_hasFreeSectionsAlongFibre {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsFiniteType B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hFt : SheafOfModules.IsFiniteTypeOnSite F)
    (y : points B S hS Y.1)
    (hflat : ∀ x : points B S hS X.1, pointsMap B S hS X.1 f.hom x = y →
      x ∈ flatLocus B S hS X.2 f.hom F) :
    ∃ (Y₁ : BigFppfOver B S hS) (q : yoneda.obj Y₁ ⟶ Y.1) (U : SmallEtale B S hS X.1)
      (ĝ : U.obj.left ⟶ Y₁) (hsq : yoneda.map ĝ ≫ q = U.obj.hom ≫ f.hom)
      (w : points B S hS (yoneda.obj Y₁)),
      IsAffine ((BigFppfOver.toScheme B S hS).obj Y₁) ∧
      IsAffine (etaleChartScheme B S hS U) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf q ∧
      pointsMap B S hS (yoneda.obj Y₁) q w = y ∧
      IsSurjective B S hS (pullback.lift (yoneda.map ĝ) U.obj.hom hsq) ∧
      LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map ĝ) ∧
      QuasiCompact ((BigFppfOver.toScheme B S hS).map ĝ) ∧
      HasFreeSectionsAlongFibreOver ((BigFppfOver.toScheme B S hS).map ĝ)
        (chartModule B S hS X.2 F U) (pointsToScheme B S hS Y₁ w)
        (pointOfEtaleChart B S hS U) (pointsMap B S hS X.1 f.hom ⁻¹' {y})
```

**`AlgebraicGeometry.Space.exists_affineChart_hasFreeSectionsAlongFibre_of_isFiniteTypeOnSite`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/ExistenceFreeSectionsAlongFibreOnSite.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/ExistenceFreeSectionsAlongFibreOnSite.lean#L48). The attribute's comment: “the etale neighbourhood, the affine scheme and its free sections are delivered, reduced to the affine etale chart of the target. At the source's own hypotheses: `F` of finite type on the small etale site of `X`, from which the finite type of each chart restriction follows by isFiniteTypeOnCharts\_of\_isFiniteTypeOnSite, which is proved”.

> **Stacks 0CVW**, at the source's own hypotheses.  Let `f : X ⟶ Y` be a finite type morphism
> of algebraic spaces over `S`, let `F` be a finite type quasi-coherent `𝒪_X`-module and let `y`
> be a point of `|Y|` at which `F` is flat along the fibre.  Then there is an affine étale
> neighbourhood of `y` in `Y` and an affine étale chart of `X` over it, surjective onto the
> fibre, over which `F` has free sections along the fibre.
>
> This is `AlgebraicGeometry.Space.exists_affineChart_hasFreeSectionsAlongFibre`, which takes `F`
> of finite type on the small étale site of `X` and derives the finite type of each chart
> restriction by `AlgebraicGeometry.Space.isFiniteTypeOnCharts_of_isFiniteTypeOnSite`.

```lean
alias exists_affineChart_hasFreeSectionsAlongFibre_of_isFiniteTypeOnSite
```

**`AlgebraicGeometry.Space.exists_etale_affine_free_sections_along_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/FreeSectionsAlongFibreDiagram.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/FreeSectionsAlongFibreDiagram.lean#L270).

> **Stacks Project, Tag 0CVW.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let
> `𝓕` be a quasi-coherent `𝒪_X`-module and let `y ∈ |Y|`, with fibre `F = f^{-1}({y}) ⊆ |X|`.
> Assume
>
> 1. `f` is of finite type (`hf`),
> 2. `𝓕` is of finite type (`hFt`), and
> 3. `𝓕` is flat over `Y` at every point of `F` (`hflat`).
>
> Then there are a scheme `Y'` with a point `y'` and an étale morphism `e : Y' ⟶ Y` sending `y'`
> to `y`, an affine scheme `X'` with morphisms `g : X' ⟶ X` and `k : X' ⟶ Spec 𝒪_{Y', y'}` making
> the square over `f` commute, such that the induced `X' ⟶ X ×_Y Spec 𝒪_{Y', y'}` is étale, `F`
> is the image under `g` of the fibre `X'_{y'}` of `X'` over the closed point of
> `Spec 𝒪_{Y', y'}` (so `|X'_{y'}| ⟶ F` is surjective), and `Γ(X', g^*𝓕)` is a free
> `𝒪_{Y', y'}`-module, the module structure coming from `k`.
>
> The schemes `Y'`, `Spec 𝒪_{Y', y'}` (`AlgebraicGeometry.BigFppfOver.specStalk`) and `X'` are
> objects of the big fppf site of `S`, morphisms of algebraic spaces out of them are morphisms out
> of the presheaves they represent, and `Γ(X', g^*𝓕)` is the module of global sections of the
> restriction of `g^*𝓕` to the scheme `X'`, its identity chart.

```lean
theorem exists_etale_affine_free_sections_along_fibre {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsFiniteType B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    [F.IsQuasicoherentOnSite] (hFt : SheafOfModules.IsFiniteTypeOnSite F)
    (y : points B S hS Y.1)
    (hflat : ∀ x : points B S hS X.1, pointsMap B S hS X.1 f.hom x = y →
      x ∈ flatLocus B S hS X.2 f.hom F) :
    ∃ (Y' : BigFppfOver B S hS) (y' : (BigFppfOver.toScheme B S hS).obj Y')
      (e : yoneda.obj Y' ⟶ Y.1) (X' : BigFppfOver B S hS) (g : yoneda.obj X' ⟶ X.1)
      (k : X' ⟶ BigFppfOver.specStalk B S hS Y' y')
      (hcomm : yoneda.map k ≫ yoneda.map (BigFppfOver.specStalkTo B S hS Y' y') ≫ e =
        g ≫ f.hom),
      IsEtale B S hS e ∧
      pointsMap B S hS (yoneda.obj Y') e ((pointsEquivScheme B S hS Y').symm y') = y ∧
      IsEtale B S hS (pullback.lift (yoneda.map k) g hcomm) ∧
      pointsMap B S hS X.1 f.hom ⁻¹' {y} =
        pointsMap B S hS (yoneda.obj X') g ''
          (pointsMap B S hS (yoneda.obj X') (yoneda.map k) ⁻¹'
            {BigFppfOver.specStalkClosedPoint B S hS Y' y'}) ∧
      IsAffine ((BigFppfOver.toScheme B S hS).obj X') ∧
      (let M := restrictToChart B S hS (isAlgebraicSpace_yoneda B S hS X')
          ((modulePullback B S hS (X := ⟨yoneda.obj X', isAlgebraicSpace_yoneda B S hS X'⟩)
            (Y := X) (ObjectProperty.homMk g)).obj F)
          (idEtaleChart B S hS X')
       letI : Module (((BigFppfOver.toScheme B S hS).obj Y').presheaf.stalk y') Γ(M, ⊤) :=
         globalSectionsModuleOfSpecBase ((BigFppfOver.toScheme B S hS).map k) M
       Module.Free (((BigFppfOver.toScheme B S hS).obj Y').presheaf.stalk y') Γ(M, ⊤))
```

## Tag 0CWL, a theorem

[Tag 0CWL](https://stacks.math.columbia.edu/tag/0CWL) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOverAtPoint_of_forall_isRelativeWeaklyAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/FlatnessAtRelativeAssassin.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/FlatnessAtRelativeAssassin.lean#L161). The attribute's comment: “the implication (2) => (1), which the tag asserts holds with no decency hypothesis: for f locally of finite type and F a finite type quasi-coherent module, flatness of F over Y at every point of the fibre over y which lies in Ass\_\{X/Y}(F) and specializes to x gives flatness of F over Y at x. UNCONDITIONAL -- nothing is carried: the case of schemes is More on Flatness Theorem 05UA (2) => (1), proved in this library as AlgebraicGeometry.isFlatOverAt\_of\_forall\_mem\_relativeAssassin\_specializes, and the reduction to a commuting square of etale scheme charts is proved here”.

> **Stacks 0CWL, the implication (2) ⟹ (1).** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` which is locally of finite type, let `𝓕` be a quasi-coherent `𝒪_X`-module of
> finite type and let `x` be a point of `|X|` with image `y` under `|f|`. If `𝓕` is flat over `Y`
> at every point `x'` of `|X|` which lies over `y`, lies in the relative weak assassin
> `WeakAss_{X/Y}(𝓕)` of Stacks 0CV0 — which is `Ass_{X/Y}(𝓕)` here, the fibres of `f` being
> locally Noetherian — and specializes to `x`, then `𝓕` is flat over `Y` at `x`.
>
> No decency is required, as the source records. Nothing is carried: the case of schemes is
> `AlgebraicGeometry.isFlatOverAt_of_forall_mem_relativeAssassin_specializes`, More on Flatness
> Theorem 05UA (2) ⟹ (1) in relative-assassin form, and the reduction to a commuting square of
> étale scheme charts of `f` is what is proved here.

```lean
theorem isFlatOverAtPoint_of_forall_isRelativeWeaklyAssociatedPoint (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (hFft : SheafOfModules.IsFiniteTypeOnSite F)
    (x : points B S hS X.1)
    (h2 : ∀ x' : points B S hS X.1,
      pointsMap B S hS X.1 f.hom x' = pointsMap B S hS X.1 f.hom x →
      IsRelativeWeaklyAssociatedPoint B S hS f F x' → x' ⤳ x →
        IsFlatOverAtPoint B S hS X.2 f.hom F x') :
    IsFlatOverAtPoint B S hS X.2 f.hom F x
```

**`AlgebraicGeometry.Space.isFlatOverAtPoint_of_specializes_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/FlatnessAtRelativeAssassin.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/FlatnessAtRelativeAssassin.lean#L217). The attribute's comment: “the implication (1) => (2) for decent X, UNCONDITIONALLY -- nothing is carried: flatness of F over Y at x gives flatness of F over Y at every point of |X| which specializes to x. This is stronger than the tag's clause (2) in four ways: the point is not required to lie in Ass\_\{X/Y}(F), it is not required to lie in the set-theoretic fibre through x, decency of Y is not needed, and f locally of finite type and F of finite type are not needed and are not hypotheses; quasi-coherence of F and decency of X are”.

> **Stacks 0CWL, the implication (1) ⟹ (2), for decent `X`.** Let `f : X ⟶ Y` be a morphism
> of algebraic spaces over `S` with `X` decent and let `𝓕` be a quasi-coherent `𝒪_X`-module which
> is flat over `Y` at a point `x` of `|X|`. Then `𝓕` is flat over `Y` at every point `x'` of `|X|`
> which specializes to `x`.
>
> This is clause (2) of the tag and more, in four ways: the relative-assassin condition on `x'` is
> not needed; `x'` is not required to lie in the set-theoretic fibre of `f` through `x`; decency
> of `Y` is not needed; and neither local finiteness of the type of `f` nor finiteness of the type
> of `𝓕` is a hypothesis. Decency of `X` lifts the specialization to an étale scheme chart
> (Stacks 03IL), and the case of schemes is then
> `AlgebraicGeometry.isFlatOverAt_of_specializes_acrossFibres`, which propagates relative flatness
> to an arbitrary generalization and so asks nothing about the images of the two lifted points in the
> target chart scheme.

```lean
theorem isFlatOverAtPoint_of_specializes_of_isDecentSpace (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (hXdec : IsDecentSpace B S hS X.1)
    {x x' : points B S hS X.1} (hflat : IsFlatOverAtPoint B S hS X.2 f.hom F x)
    (hspec : x' ⤳ x) :
    IsFlatOverAtPoint B S hS X.2 f.hom F x'
```

## Tag 0CWM, a lemma

[Tag 0CWM](https://stacks.math.columbia.edu/tag/0CWM) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOver_of_forall_specializes_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Flat/FlatnessOverLocalBase.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Flat/FlatnessOverLocalBase.lean#L349). The attribute's comment: “the lemma's implication: from its hypotheses (1) and (2) to flatness of ℱ over the local base. UNCONDITIONAL -- nothing is carried and no decency of X is assumed: the step the source's proof invokes, the implication (2) => (1) of Stacks 0CWL, is proved here for arbitrary X and Y as isFlatOverAtPoint\_of\_forall\_isRelativeWeaklyAssociatedPoint, and the passage of flatness from a point of the closed fibre to a point of Ass\_\{X/S}(F) specializing to it is proved here as isFlatOverAtPoint\_of\_specializes\_of\_isRelativeWeaklyAssociatedPoint, using only that the local base is a decent space. The closedness of s is a hypothesis of the statement that the implication does not use”.

> **Stacks Project, Tag 0CWM.** Let `S` be a local scheme with closed point `s`, read as the
> target `Y` of a morphism of algebraic spaces: the target is represented by a scheme of the site
> isomorphic to the spectrum of a local ring, and `s` is a closed point of `|Y|`. Let
> `f : X ⟶ Y` be locally of finite type and let `F` be a finite type quasi-coherent
> `𝒪_X`-module. Assume
>
> 1. every point of `Ass_{X/S}(F)` specializes to a point of the closed fibre `X_s` (`hass`),
>    and
> 2. `F` is flat over `S` at every point of `X_s` (`hflat`).
>
> Then `F` is flat over `S`.
>
> The conclusion is the tag's, with no clause dropped and nothing carried. The representability
> of the target in `hlocal` is consumed: a representable algebraic space is decent, which is what
> `AlgebraicGeometry.Space.isFlatOver_of_forall_specializes_fibre` asks of the target. The
> closedness of `s` is a hypothesis of the tag that the implication does not use.

```lean
theorem isFlatOver_of_forall_specializes_closedFibre {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (s : points B S hS Y.1)
    (hlocal : ∃ (T : BigFppfOver B S hS) (A : CommRingCat.{u}), IsLocalRing A ∧
      Nonempty (Spec A ≅ (BigFppfOver.toScheme B S hS).obj T) ∧ Nonempty (yoneda.obj T ≅ Y.1))
    (_hs : IsClosed ({s} : Set (points B S hS Y.1)))
    (hlft : IsLocallyOfFiniteType B S hS f.hom) (hqc : F.IsQuasicoherentOnSite)
    (hft : SheafOfModules.IsFiniteTypeOnSite F)
    (hass : ∀ x' ∈ relativeWeaklyAssociatedPoints B S hS f F,
      ∃ θ : points B S hS X.1, x' ⤳ θ ∧ pointsMap B S hS X.1 f.hom θ = s)
    (hflat : ∀ θ : points B S hS X.1, pointsMap B S hS X.1 f.hom θ = s →
      IsFlatOverAtPoint B S hS X.2 f.hom F θ) :
    IsFlatOver B S hS X.2 f.hom F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.4, Tag 0CVJ](https://stacks.math.columbia.edu/tag/0CVJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
