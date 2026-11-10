---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.MorphismDescentSystem, AlgebraicGeometry.Space.MorphismDescentSystem.exists_isEtale_mapAt, AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSmooth_mapAt, AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSmooth_mapAt_op, AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSurjective_mapAt, AlgebraicGeometry.Space.MorphismDescentSystem.exists_universallyInjective_mapAt, AlgebraicGeometry.Space.MorphismDescentSituation.exists_isAffineHom_mapAt_of_isAffineHom_mapLimit_of_siteContainsBaseChangeLimits, AlgebraicGeometry.Space.MorphismDescentData.exists_isAffineHom_mapAt
statement: formalized
proof: formalized
---

# 70.6 Descending properties of morphisms

Section 70.6 of the Stacks Project, [Tag 084V](https://stacks.math.columbia.edu/tag/084V). 14 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 084W, a situation

[Tag 084W](https://stacks.math.columbia.edu/tag/084W) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphisms.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphisms.lean#L111).

> **Stacks 084W.** The standing situation for descending a property of a
> morphism of algebraic spaces along a directed limit: a directed inverse system of algebraic
> spaces over `S` with affine transition morphisms and algebraic limit, a distinguished stage of
> the system, and a morphism of quasi-compact quasi-separated algebraic spaces over that
> stage.

```lean
structure MorphismDescentSystem (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u})) (I : Type u) [Preorder I] [IsDirected I (· ≤ ·)]
```

## Tag 07SL, a lemma

[Tag 07SL](https://stacks.math.columbia.edu/tag/07SL) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isEtale_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1262). References: EGA IV (17.7.8), “(ii) étale”.

> **Stacks 07SL.** In the situation of Stacks 084W, if the base change `f` of `f₀` to the
> limit `B` is étale and `f₀` is locally of finite presentation, then the base change `f_i` of
> `f₀` to some stage `B_i` is étale.

```lean
theorem exists_isEtale_mapAt (D : MorphismDescentSystem B S hS hZ I)
    (etale : IsEtale B S hS D.mapLimit) (fp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), IsEtale B S hS (D.mapAt i le)
```

## Tag 0CN2, a lemma

[Tag 0CN2](https://stacks.math.columbia.edu/tag/0CN2) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSmooth_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1281). References: EGA IV (17.12.6), “f smooth ⇒ ∃λ”; EGA IV (17.7.8), “(ii) smooth”.

> **Stacks 0CN2.** In the situation of Stacks 084W, if the base change `f` of `f₀` to the
> limit `B` is smooth and `f₀` is locally of finite presentation, then the base change `f_i` of
> `f₀` to some stage `B_i` is smooth.

```lean
theorem exists_isSmooth_mapAt (D : MorphismDescentSystem B S hS hZ I)
    (smooth : IsSmooth B S hS D.mapLimit) (fp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), IsSmooth B S hS (D.mapAt i le)
```

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSmooth_mapAt_op`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1435). The attribute's comment: “the cofiltered-covariant form: the conclusion ranges over a morphism of the cofiltered index category Iᵒᵖ carrying the covariant diagram `base`, which is the indexing the library's Stacks 07SK consumes, rather than over an inequality of the directed preorder I; the mathematical content is that of the inequality form beside it”.

> **Stacks 0CN2 in the covariant indexing of Stacks 07SK.** In the situation of Stacks 084W, if
> the base change `f` of `f₀` to the limit `B` is smooth and `f₀` is locally of finite presentation,
> then there is a morphism `j ⟶ 0` of the cofiltered index category `Iᵒᵖ` along which the base
> change of `f₀` is smooth.
>
> This is `AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSmooth_mapAt` with its conclusion
> read over a morphism of `Iᵒᵖ` instead of an inequality of `I`; the transition morphism is the same
> one, by `AlgebraicGeometry.Space.MorphismDescentSystem.base_map_eq_baseAtToInitial`. It is the
> shape in which the conclusions of Stacks 07SK are stated, so the two can be used together.

```lean
theorem exists_isSmooth_mapAt_op (D : MorphismDescentSystem B S hS hZ I)
    (smooth : IsSmooth B S hS D.mapLimit) (fp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (j : Iᵒᵖ) (g : j ⟶ op D.initial),
      IsSmooth B S hS (D.mapAt j.unop (leOfHom g.unop))
```

## Tag 07SN, a lemma

[Tag 07SN](https://stacks.math.columbia.edu/tag/07SN) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSurjective_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1271).

> **Stacks 07SN.** In the situation of Stacks 084W, if the base change `f` of `f₀` to the
> limit `B` is surjective and `f₀` is locally of finite presentation, then the base change `f_i`
> of `f₀` to some stage `B_i` is surjective.

```lean
theorem exists_isSurjective_mapAt
    (D : MorphismDescentSystem B S hS hZ I) (surjective : IsSurjective B S hS D.mapLimit)
    (fp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), IsSurjective B S hS (D.mapAt i le)
```

## Tag 084X, a lemma

[Tag 084X](https://stacks.math.columbia.edu/tag/084X) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_universallyInjective_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1374).

> **Stacks 084X.** In the situation of Stacks 084W, if the base change `f` of `f₀` to the
> limit `B` is universally injective and `f₀` is locally of finite type, then the base change
> `f_i` of `f₀` to some stage `B_i` is universally injective.

```lean
theorem exists_universallyInjective_mapAt
    (D : MorphismDescentSystem B S hS hZ I)
    (injective : UniversallyInjective B S hS D.mapLimit)
    (ft : IsLocallyOfFiniteType B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), UniversallyInjective B S hS (D.mapAt i le)
```

## Tag 084Y, a lemma

[Tag 084Y](https://stacks.math.columbia.edu/tag/084Y) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSituation.exists_isAffineHom_mapAt_of_isAffineHom_mapLimit_of_siteContainsBaseChangeLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineMorphismDescent.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineMorphismDescent.lean#L211).

> Notation and assumptions as in Situation 70.6.1 (tag 084W), carried by
> `AlgebraicGeometry.Space.MorphismDescentSituation`, in the chapter's setting of Section 70.2
> (tag 07SD): `B = lim B_i` a directed inverse limit of algebraic spaces over `S` with affine
> transition morphisms, `f₀ : X₀ ⟶ Y₀` a morphism of algebraic spaces over `B₀` with `B₀`, `X₀`
> and `Y₀` quasi-compact and quasi-separated, and `f_i : X_i ⟶ Y_i`, `f : X ⟶ Y` its base changes
> to `B_i` for `i ≥ 0` and to `B`. If `f` is affine, then `f_i` is affine for some `i ≥ 0`.
>
> The hypothesis `hconv` is the chapter's standing convention that every ring considered has its
> spectrum in the big fppf site, read for the system of bases; nothing is asked of the index. The
> implementation notes of this module show that the statement fails without it; the
> corresponding failure of Stacks 07SQ, on which the proof rests, is
> `AlgebraicGeometry.Space.DescentSituation.not_forall_exists_isAffineSpace_system_obj`.
>
> The proof is the source's:
> `exists_isAffineHom_mapAt_of_descentAffineStage_of_siteContainsBaseChangeLimits` with Stacks
> 07SQ supplied by
> `DescentSituation.exists_isAffineSpace_system_obj_of_siteContainsBaseChangeLimits`.

```lean
theorem exists_isAffineHom_mapAt_of_isAffineHom_mapLimit_of_siteContainsBaseChangeLimits
    (hconv : SiteContainsBaseChangeLimits B S hS D.base) (hf : IsAffineHom B S hS D.mapLimit) :
    ∃ (i : I) (hi : D.initial ≤ i), IsAffineHom B S hS (D.mapAt i hi)
```

**`AlgebraicGeometry.Space.MorphismDescentData.exists_isAffineHom_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean#L205).

> In Situation 084W, under the chapter's convention of Section 70.2, if
> `f : X ⟶ Y` is affine then `f_i : X_i ⟶ Y_i` is affine for some `i ≥ 0`.

```lean
theorem exists_isAffineHom_mapAt (hconv : SiteContainsBaseChangeLimits B S hS D.base)
    (hf : IsAffineHom B S hS (D.toMorphismDescentSituation hconv).mapLimit) :
    ∃ (i : I) (hi : D.initial ≤ i),
      IsAffineHom B S hS ((D.toMorphismDescentSituation hconv).mapAt i hi)
```

## Tag 084Z, a lemma

[Tag 084Z](https://stacks.math.columbia.edu/tag/084Z) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentData.exists_isFinite_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean#L215).

> In Situation 084W, under the chapter's convention of Section 70.2, if `f` is
> finite and `f₀` is locally of finite type, then `f_i` is finite for some `i ≥ 0`.

```lean
theorem exists_isFinite_mapAt (hconv : SiteContainsBaseChangeLimits B S hS D.base)
    (hf : IsFinite B S hS (D.toMorphismDescentSituation hconv).mapLimit)
    (hf₀ : IsLocallyOfFiniteType B S hS D.map₀) :
    ∃ (i : I) (hi : D.initial ≤ i),
      IsFinite B S hS ((D.toMorphismDescentSituation hconv).mapAt i hi)
```

## Tag 0850, a lemma

[Tag 0850](https://stacks.math.columbia.edu/tag/0850) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentData.exists_isClosedImmersion_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean#L227).

> In Situation 084W, under the chapter's convention of Section 70.2, if `f` is
> a closed immersion and `f₀` is locally of finite type, then `f_i` is a closed immersion for some
> `i ≥ 0`.

```lean
theorem exists_isClosedImmersion_mapAt (hconv : SiteContainsBaseChangeLimits B S hS D.base)
    (hf : IsClosedImmersion B S hS (D.toMorphismDescentSituation hconv).mapLimit)
    (hf₀ : IsLocallyOfFiniteType B S hS D.map₀) :
    ∃ (i : I) (hi : D.initial ≤ i),
      IsClosedImmersion B S hS ((D.toMorphismDescentSituation hconv).mapAt i hi)
```

## Tag 0851, a lemma

[Tag 0851](https://stacks.math.columbia.edu/tag/0851) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isSeparated_pullbackMap_of_siteContainsBaseChangeLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSite/SeparatedDescent.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSite/SeparatedDescent.lean#L58). The attribute's comment: “under the chapter's convention of Section 70.2 (tag 07SD) on the system of bases, every stage quasi-compact; proved in an enlarged site”.

> **Stacks 0851.** In the situation of Stacks 084W, if the base change `f : X ⟶ Y` of
> `f₀ : X₀ ⟶ Y₀` to the limit `B = lim B_i` is separated, then the base change `f_i : X_i ⟶ Y_i` of
> `f₀` to some stage `B_i` with `i ≥ 0` is separated.

```lean
theorem exists_isSeparated_pullbackMap_of_siteContainsBaseChangeLimits {I : Type u} [Preorder I]
    [IsDirected I (· ≤ ·)] [Nonempty I] (base : Iᵒᵖ ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hbase : ∀ i, IsAlgebraicSpace B S hS (base.obj i))
    (hAffine : ∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom B S hS (base.map a))
    (hconv : SiteContainsBaseChangeLimits B S hS base)
    (hQc : ∀ i, IsQuasiCompactSpace B S hS (base.obj i)) (i₀ : I)
    {X₀ Y₀ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (p : X₀ ⟶ base.obj (op i₀))
    (q : Y₀ ⟶ base.obj (op i₀)) (f₀ : X₀ ⟶ Y₀) (hf₀ : f₀ ≫ q = p)
    (hX₀ : IsAlgebraicSpace B S hS X₀) (hY₀ : IsAlgebraicSpace B S hS Y₀)
    (hB₀qs : IsAbsolutelyQuasiSeparated B S hS hZ (base.obj (op i₀)))
    (hX₀qc : IsQuasiCompactSpace B S hS X₀) (hX₀qs : IsAbsolutelyQuasiSeparated B S hS hZ X₀)
    (hY₀qc : IsQuasiCompactSpace B S hS Y₀) (hY₀qs : IsAbsolutelyQuasiSeparated B S hS hZ Y₀)
    (hf : IsSeparated B S hS (pullback.map (limit.π base (op i₀)) p (limit.π base (op i₀)) q
      (𝟙 _) f₀ (𝟙 _) (by simp) (by simp [hf₀]))) :
    ∃ (i : I) (hi : i₀ ≤ i), IsSeparated B S hS (pullback.map (base.map (homOfLE hi).op) p
      (base.map (homOfLE hi).op) q (𝟙 _) f₀ (𝟙 _) (by simp) (by simp [hf₀]))
```

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isSeparated_mapAt_of_isSeparated_mapLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedMorphismDescent.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedMorphismDescent.lean#L477).

> **Stacks 0851.** In the situation of Stacks 084W, if the base change `f` of `f₀` to the
> limit `B` is separated, then the base change `f_i` of `f₀` to some stage `B_i` is separated.

```lean
theorem exists_isSeparated_mapAt_of_isSeparated_mapLimit (hf : IsSeparated B S hS D.mapLimit) :
    ∃ (i : I) (hi : D.initial ≤ i), IsSeparated B S hS (D.mapAt i hi)
```

## Tag 0852, a lemma

[Tag 0852](https://stacks.math.columbia.edu/tag/0852) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isIso_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Isomorphism.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Isomorphism.lean#L363). References: EGA IV (8.8.2.5), “f iso ⇒ f\_i iso”.

> **Stacks 0852**, and **Stacks 084S**. In the situation of Stacks 084W, if the base change
> `f` of `f₀` to the limit `B` is an isomorphism and `f₀` is locally of finite presentation, then
> the base change `f_i` of `f₀` to some stage `B_i` is an isomorphism.
>
> This is Stacks 0852. Stacks 084S draws the same conclusion in the limit situation of Stacks
> 084R, with the source and the target in addition assumed representable over the stage;
> hypothesis (a) of that tag is not needed here, since the three properties into which being an
> isomorphism is decomposed all descend without it.

```lean
theorem exists_isIso_mapAt (hf : IsIso D.mapLimit)
    (hfp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (hi : D.initial ≤ i), IsIso (D.mapAt i hi)
```

## Tag 07SM, a lemma

[Tag 07SM](https://stacks.math.columbia.edu/tag/07SM) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_mono_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Monomorphism.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Monomorphism.lean#L137). References: SGA 3 VIB (10.1), “partial”.

> If the base change `f` of `f₀` to the limit `B` is a monomorphism and `f₀` is locally of
> finite type, then the base change `f_i` of `f₀` to some stage `B_i` is a monomorphism.

```lean
theorem exists_mono_mapAt (hf : Mono D.mapLimit)
    (hf₀ : IsLocallyOfFiniteType B S hS D.map₀) :
    ∃ (i : I) (hi : D.initial ≤ i), Mono (D.mapAt i hi)
```

## Tag 08K0, a lemma

[Tag 08K0](https://stacks.math.columbia.edu/tag/08K0) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFlatOver_baseChange_of_chartLimitsInSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingModuleFlatnessUnbounded.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingModuleFlatnessUnbounded.lean#L115). The attribute's comment: “flatness of a module, with no bound on the index: the 07SD convention in place of the index bound of MorphismDescentSystem, which exists\_isFlatOver\_mapAt carries”.

> **Stacks 08K0, flatness of a module, with no bound on the index.** Let `(B_i)` be a
> cofiltered inverse system of algebraic spaces over `S` with affine transition morphisms, let `i`
> be a stage with `B_i` quasi-compact and quasi-separated, and let `f : X ⟶ Y` be a morphism of
> quasi-compact, quasi-separated algebraic spaces over `B_i`. Let `F₀` be a quasi-coherent
> `𝒪_X`-module of finite presentation. Suppose the pullback of `F₀` to `lim B_j ×_{B_i} X` is flat
> over `lim B_j ×_{B_i} Y`, and `f` is locally of finite presentation. Then for some stage `j ⟶ i`
> the pullback of `F₀` to `B_j ×_{B_i} X` is flat over `B_j ×_{B_i} Y`.
>
> This strengthens `AlgebraicGeometry.Space.MorphismDescentSystem.exists_isFlatOver_mapAt`. The
> bound `MorphismDescentSystem.indexSize` on the index is replaced by `hconv`. `hconv` is the
> chapter's convention 07SD: the limits of the base changes of the stages to the affine objects of
> the site lie in the site. It is not an assumption beyond the source. It is equivalent to
> `AlgebraicGeometry.Space.SiteContainsBaseChangeLimits`, which it states unfolded, and the index
> bound implies it (`AlgebraicGeometry.Space.chartLimitsInSite_of_lt_cof`).

```lean
theorem exists_isFlatOver_baseChange_of_chartLimitsInSite
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    (D : I ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hconv : ∀ (i : I) (Z : BigAffineFppf B S hS)
      (g : yoneda.obj ((BigAffineFppf.inclusion B S hS).obj Z) ⟶ D.obj i)
      (W : Over i ⥤ BigAffineFppf B S hS),
      (W ⋙ (BigAffineFppf.inclusion B S hS ⋙ yoneda) ≅
        (Over.post (X := i) D ⋙ Over.pullback g) ⋙
          Over.forget (yoneda.obj ((BigAffineFppf.inclusion B S hS).obj Z))) →
      ∀ c : Cone (((W ⋙ BigAffineFppf.inclusion B S hS) ⋙
          BigFppfOver.forget B S hS) ⋙ B.inclusion),
        IsLimit c → B.Contains c.pt)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (i : I) (hB₀qc : IsQuasiCompactSpace B S hS (D.obj i))
    (hB₀qs : IsAbsolutelyQuasiSeparated B S hS hZ (D.obj i))
    {X Y : Over (D.obj i)} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X.left) (hY : IsAlgebraicSpace B S hS Y.left)
    (hXqc : IsQuasiCompactSpace B S hS X.left) (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.left)
    (hYqc : IsQuasiCompactSpace B S hS Y.left) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.left)
    (F₀ : Modules.{u, u} B S hS X.left hX)
    [F₀.IsQuasicoherentOnSite] [F₀.IsFinitePresentationOnSite]
    (flat : IsFlatOver B S hS
      (isAlgebraicSpace_pullback B S hS (limit.π D i) X.hom
        (isAlgebraicSpace_limit_of_chartLimitsInSite B S hS D hconv hD hAffine i hB₀qc) hX (hD i))
      (pullback.map (limit.π D i) X.hom (limit.π D i) Y.hom (𝟙 _) f.left (𝟙 _) (by simp)
        (by simp))
      ((modulePullback B S hS (ObjectProperty.homMk (pullback.snd (limit.π D i) X.hom) :
          (⟨pullback (limit.π D i) X.hom,
            isAlgebraicSpace_pullback B S hS (limit.π D i) X.hom
              (isAlgebraicSpace_limit_of_chartLimitsInSite B S hS D hconv hD hAffine i hB₀qc) hX
              (hD i)⟩ : AlgebraicSpaces B S hS) ⟶ ⟨X.left, hX⟩)).obj F₀))
    (fp : IsLocallyOfFinitePresentation B S hS f.left) :
    ∃ (j : I) (e : j ⟶ i), IsFlatOver B S hS
      (isAlgebraicSpace_pullback B S hS (D.map e) X.hom (hD j) hX (hD i))
      (pullback.map (D.map e) X.hom (D.map e) Y.hom (𝟙 _) f.left (𝟙 _) (by simp) (by simp))
      ((modulePullback B S hS (ObjectProperty.homMk (pullback.snd (D.map e) X.hom) :
          (⟨pullback (D.map e) X.hom,
            isAlgebraicSpace_pullback B S hS (D.map e) X.hom (hD j) hX (hD i)⟩ :
              AlgebraicSpaces B S hS) ⟶ ⟨X.left, hX⟩)).obj F₀)
```

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isFlat_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1290). The attribute's comment: “in particular: flatness of the morphism”. References: EGA IV (11.2.6), “F = O\_X case”.

> **Stacks 08K0**, flatness of the morphism. In the situation of Stacks 084W, if `f₀` is locally
> of finite presentation and its base change `f : X ⟶ Y` to the limit is flat, then its base change
> `f_i : X_i ⟶ Y_i` to some stage `i ≥ 0` is flat.

```lean
theorem exists_isFlat_mapAt
    (D : MorphismDescentSystem B S hS hZ I) (flat : IsFlat B S hS D.mapLimit)
    (fp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), IsFlat B S hS (D.mapAt i le)
```

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isFlatOver_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1301). The attribute's comment: “flatness of a module”.

> **Stacks 08K0**, flatness of a module. In the situation of Stacks 084W, let `F₀` be a quasi-coherent
> `𝒪_{X₀}`-module, with pullbacks `F_i` to `X_i` and `F` to `X`. If `F` is flat over `Y`, `F₀` is
> of finite presentation and `f₀` is locally of finite presentation, then `F_i` is flat over `Y_i`
> for some stage `i ≥ 0`.

```lean
theorem exists_isFlatOver_mapAt (D : MorphismDescentSystem B S hS hZ I)
    (F₀ : Modules.{u, u} B S hS D.source₀ D.source₀_isAlgebraicSpace)
    [F₀.IsQuasicoherentOnSite] [F₀.IsFinitePresentationOnSite]
    (flat : IsFlatOver B S hS D.sourceLimit_isAlgebraicSpace D.mapLimit
      ((modulePullback B S hS (ObjectProperty.homMk
        (pullback.snd (limit.π D.base (op D.initial)) D.sourceToBase) :
          (⟨D.sourceLimit, D.sourceLimit_isAlgebraicSpace⟩ : AlgebraicSpaces B S hS) ⟶
            ⟨D.source₀, D.source₀_isAlgebraicSpace⟩)).obj F₀))
    (fp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), IsFlatOver B S hS (D.sourceAt_isAlgebraicSpace i le)
      (D.mapAt i le) ((modulePullback B S hS (ObjectProperty.homMk
        (pullback.snd (D.baseAtToInitial i le) D.sourceToBase) :
          (⟨D.sourceAt i le, D.sourceAt_isAlgebraicSpace i le⟩ : AlgebraicSpaces B S hS) ⟶
            ⟨D.source₀, D.source₀_isAlgebraicSpace⟩)).obj F₀)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.MorphismDescentSituation.C1573.exists_isFlatOver_mapAt_of_siteContainsBaseChangeLimits`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/Limits/DescendingMorphismPropertiesSiteConvention.lean#L659), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismPropertiesSiteConvention.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismPropertiesSiteConvention.lean#L138) (StacksFrontier): “flatness of a module, under the convention of Section 70.2 (tag 07SD) and with no condition on the index”.

## Tag 08K1, a lemma

[Tag 08K1](https://stacks.math.columbia.edu/tag/08K1) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentData.exists_isProper_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/MorphismDescentData.lean#L238).

> In Situation 084W, under the chapter's convention of Section 70.2, if `f` is
> proper and `f₀` is locally of finite type, then `f_i` is proper for some `i ≥ 0`.

```lean
theorem exists_isProper_mapAt (hconv : SiteContainsBaseChangeLimits B S hS D.base)
    (hf : IsProper B S hS (D.toMorphismDescentSituation hconv).mapLimit)
    (hf₀ : IsLocallyOfFiniteType B S hS D.map₀) :
    ∃ (i : I) (hi : D.initial ≤ i),
      IsProper B S hS ((D.toMorphismDescentSituation hconv).mapAt i hi)
```

## Tag 0D4K, a lemma

[Tag 0D4K](https://stacks.math.columbia.edu/tag/0D4K) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_hasRelativeDimensionLE_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean, line 1386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendingMorphismProperties.lean#L1386).

> **Stacks 0D4K.** In the situation of Stacks 084W, if the base change `f` of `f₀` to the
> limit `B` has relative dimension at most `d` and `f₀` is locally of finite type, then the base
> change `f_i` of `f₀` to some stage `B_i` has relative dimension at most `d`.

```lean
theorem exists_hasRelativeDimensionLE_mapAt (D : MorphismDescentSystem B S hS hZ I) (d : ℕ)
    (dimension : HasRelativeDimensionLE d B S hS D.mapLimit)
    (ft : IsLocallyOfFiniteType B S hS D.map₀) :
    ∃ (i : I) (le : D.initial ≤ i), HasRelativeDimensionLE d B S hS (D.mapAt i le)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.6, Tag 084V](https://stacks.math.columbia.edu/tag/084V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
