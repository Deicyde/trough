---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsRelativeNormalization.isIso_of_isIntegralHom, AlgebraicGeometry.Space.exists_isOpenSubspace_isIso_fromPreimage_of_isFinite, AlgebraicGeometry.Space.IsRelativeNormalization.exists_isOpenSubspace_isIso_fromPreimage_and_range_pointsMap_preimage_eq, AlgebraicGeometry.Space.exists_isOpenSubspace_isIso_fromPreimage_toNormalizationInQcqs, AlgebraicGeometry.Space.NormalizationInData.isIntegralHom_fromNorm_of_isQuasiFinite_isSeparated, AlgebraicGeometry.Space.NormalizationInData.isOpenImmersion_toNorm_of_isQuasiFinite_isSeparated, AlgebraicGeometry.Space.NormalizationInData.isQuasiCompact_toNorm_of_isQuasiFinite_isSeparated, AlgebraicGeometry.Space.isQuasiAffineHom_of_isQuasiFinite_isSeparated
statement: formalized
proof: formalized
---

# 76.34 Zariski's Main Theorem

Section 76.34 of the Stacks Project, [Tag 05W7](https://stacks.math.columbia.edu/tag/05W7). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 082I, a lemma

[Tag 082I](https://stacks.math.columbia.edu/tag/082I) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativeNormalization.isIso_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQuasiFiniteLocus.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQuasiFiniteLocus.lean#L118). The attribute's comment: “the isomorphism conclusion when f is integral: the canonical morphism to the normalization is an isomorphism, so the open subspace may be taken to be the whole normalization”.

> **Stacks 082I, the isomorphism conclusion for an integral morphism.** Let `f : X ⟶ Y` be an
> integral morphism of algebraic spaces over `S` and let `ν : Y' ⟶ Y`, `f' : X ⟶ Y'` be the
> normalization of `Y` in `X`. Then `f'` is an isomorphism, so the open subspace `U' ⊆ Y'` of the
> tag may be taken to be all of `Y'`.
>
> The identity of `X` factors `f` through the integral morphism `f`, so the universal property
> yields `k : Y' ⟶ X` with `f' ≫ k = 𝟙` and `k ≫ f = ν`; uniqueness in the universal property
> for the factorization `f = f' ≫ ν` identifies `k ≫ f'` with `𝟙`.

```lean
theorem isIso_of_isIntegralHom (h : IsRelativeNormalization B S hS f ν f')
    (hX : IsAlgebraicSpace B S hS X) (hY' : IsAlgebraicSpace B S hS Y')
    (hf : IsIntegralHom B S hS f) : IsIso f'
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isIso_fromPreimage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQuasiFiniteLocus.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationInQuasiFiniteLocus.lean#L141). The attribute's comment: “both numbered conclusions in the case of a finite morphism, with the open subspace the whole normalization”.

> **Stacks 082I for a finite morphism.** Let `f : X ⟶ Y` be a finite morphism of algebraic
> spaces over `S` and let `ν : Y' ⟶ Y`, `f' : X ⟶ Y'` be the normalization of `Y` in `X`. Then
> there is an open subspace `U' ⊆ Y'` such that `(f')⁻¹(U') ⟶ U'` is an isomorphism and the point
> set of `(f')⁻¹(U')` is the set of points of `X` at which `f` is quasi-finite; one may take
> `U' = Y'`.
>
> A finite morphism is integral by Tag 0414, so `f'` is an isomorphism and hence so is its base
> change `(f')⁻¹(Y') ⟶ Y'`; and a finite morphism is locally quasi-finite by Tag 0A4X, hence
> quasi-finite at every point of its source, which is the whole of `(f')⁻¹(Y')`.

```lean
theorem exists_isOpenSubspace_isIso_fromPreimage_of_isFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (h : IsRelativeNormalization B S hS f ν f')
    (hf : IsFinite B S hS f) :
    ∃ U' : Subfunctor Y', IsOpenSubspace B S hS U' ∧ IsIso (U'.fromPreimage f') ∧
      ∀ x : points B S hS X,
        x ∈ Set.range (pointsMap B S hS (U'.preimage f').toFunctor (U'.preimage f').ι) ↔
          IsQuasiFiniteAt B S hS f x
```

**`AlgebraicGeometry.Space.IsRelativeNormalization.exists_isOpenSubspace_isIso_fromPreimage_and_range_pointsMap_preimage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFiniteTypeSeparated.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFiniteTypeSeparated.lean#L284). The attribute's comment: “both numbered conclusions, for every factorization of f with the universal property of Tag 0823 (the normalization of Y in X)”.

> **Stacks 082I.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is of
> finite type and separated, and let `ν : Y' ⟶ Y`, `f' : X ⟶ Y'` be the normalization of `Y` in
> `X`, in the sense of the characterization of Tag 0823. Then there is an open subspace
> `U' ⊆ Y'` such that `(f')⁻¹(U') ⟶ U'` is an isomorphism and the point set of `(f')⁻¹(U')` is
> the set of points of `X` at which `f` is quasi-finite.
>
> The open subspace is the image of the quasi-finite locus. It is covered by the étale
> morphisms of `IsRelativeNormalization.exists_isEtale_isPullback_of_isQuasiFiniteAt`, one for
> each point of quasi-finiteness, which makes it open and identifies its inverse image;
> and `(f')⁻¹(U') ⟶ U'` is an isomorphism after base change to each of them, hence an
> isomorphism by Tag 041Y.

```lean
theorem exists_isOpenSubspace_isIso_fromPreimage_and_range_pointsMap_preimage_eq
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y} {ν : Y' ⟶ Y} {f' : X ⟶ Y'}
    (h : IsRelativeNormalization B S hS f ν f')
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (hft : IsFiniteType B S hS f)
    (hsep : IsSeparated B S hS f) :
    ∃ U' : Subfunctor Y', IsOpenSubspace B S hS U' ∧ IsIso (U'.fromPreimage f') ∧
      Set.range (pointsMap B S hS (U'.preimage f').toFunctor (U'.preimage f').ι) =
        {x : points B S hS X | IsQuasiFiniteAt B S hS f x}
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isIso_fromPreimage_toNormalizationInQcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFiniteTypeSeparated.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFiniteTypeSeparated.lean#L388). The attribute's comment: “both numbered conclusions, at the normalization of Y in X constructed in Definition 0822”.

> **Stacks 082I, at the normalization of Definition 0822.** Let `f : X ⟶ Y` be a morphism of
> algebraic spaces over `S` which is of finite type and separated, and let `X ⟶ Y' ⟶ Y` be the
> normalization of `Y` in `X` constructed in Definition 0822 (it exists since `f` is
> quasi-compact and quasi-separated). Then there is an open subspace `U' ⊆ Y'` such that
> `(f')⁻¹(U') ⟶ U'` is an isomorphism and the point set of `(f')⁻¹(U')` is the set of points of
> `X` at which `f` is quasi-finite.

```lean
theorem exists_isOpenSubspace_isIso_fromPreimage_toNormalizationInQcqs
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hft : IsFiniteType B S hS f.hom)
    (hsep : IsSeparated B S hS f.hom) :
    ∃ U' : Subfunctor (normalizationInQcqs B S hS f hft.2
        (isQuasiSeparated_of_isSeparated B S hS hsep)).obj,
      IsOpenSubspace B S hS U' ∧
      IsIso (U'.fromPreimage (toNormalizationInQcqs f hft.2
        (isQuasiSeparated_of_isSeparated B S hS hsep)).hom) ∧
      Set.range (pointsMap B S hS (U'.preimage (toNormalizationInQcqs f hft.2
          (isQuasiSeparated_of_isSeparated B S hS hsep)).hom).toFunctor
          (U'.preimage (toNormalizationInQcqs f hft.2
            (isQuasiSeparated_of_isSeparated B S hS hsep)).hom).ι) =
        {x : points B S hS X.obj | IsQuasiFiniteAt B S hS f.hom x}
```

## Tag 082J, a lemma

[Tag 082J](https://stacks.math.columbia.edu/tag/082J) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizationInData.isIntegralHom_fromNorm_of_isQuasiFinite_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean#L290). The attribute's comment: “the normalization morphism is integral”.

> **Stacks 0ABS and 082J, integrality of the normalization morphism.** Let `f : X ⟶ Y` be a
> quasi-finite separated morphism of algebraic spaces over `S` and let `ν : Y' ⟶ Y`,
> `f' : X ⟶ Y'` be the normalization of `Y` in `X`. Then `ν` is integral.
>
> Over a surjective étale scheme chart `w : W ⟶ Y` the chart description of the normalization
> identifies the base change of `ν` with the morphism `fromNormalization` of the induced morphism
> of schemes `W ×_Y X ⟶ W`, which is integral; condition (3) of Tag 03ZQ promotes that to
> integrality of `ν`. The chart description is applicable because `f` is representable by
> Tag 0418, quasi-compact, and separated, hence quasi-separated.

```lean
theorem isIntegralHom_fromNorm_of_isQuasiFinite_isSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f) :
    IsIntegralHom B S hS N.fromNorm
```

**`AlgebraicGeometry.Space.NormalizationInData.isOpenImmersion_toNorm_of_isQuasiFinite_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean#L311). The attribute's comment: “the canonical morphism to the normalization is an open immersion”.

> **Stacks 0ABS and 082J, the open immersion.** Let `f : X ⟶ Y` be a quasi-finite separated
> morphism
> of algebraic spaces over `S` and let `ν : Y' ⟶ Y`, `f' : X ⟶ Y'` be the normalization of `Y`
> in `X`. Then `f'` is an open immersion.
>
> By Tag 0ABR the image `U'` in `Y'` of the quasi-finite locus of `f` is an open subspace whose
> inverse image under `f'` is that locus and over which `f'` restricts to an isomorphism. Local
> quasi-finiteness makes the locus the whole of `X`, so both the inclusion of the inverse image
> and the restriction of `f'` are isomorphisms, and `f'` is their composite with the inclusion of
> `U'`.

```lean
theorem isOpenImmersion_toNorm_of_isQuasiFinite_isSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f) :
    IsOpenImmersion B S hS N.toNorm
```

**`AlgebraicGeometry.Space.NormalizationInData.isQuasiCompact_toNorm_of_isQuasiFinite_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean#L342). The attribute's comment: “the canonical morphism to the normalization is quasi-compact”.

> **Stacks 0ABS and 082J, quasi-compactness of the open immersion.** Let `f : X ⟶ Y` be a
> quasi-finite
> separated morphism of algebraic spaces over `S` and let `ν : Y' ⟶ Y`, `f' : X ⟶ Y'` be the
> normalization of `Y` in `X`. Then `f'` is quasi-compact.
>
> This is Tag 03KS applied to the factorization `f = f' ≫ ν`: the composite is quasi-compact
> because `f` is quasi-finite, and `ν` is quasi-separated because an integral morphism is
> separated.

```lean
theorem isQuasiCompact_toNorm_of_isQuasiFinite_isSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f) :
    IsQuasiCompact B S hS N.toNorm
```

**`AlgebraicGeometry.Space.isQuasiAffineHom_of_isQuasiFinite_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremQuasiFinite.lean#L369). The attribute's comment: “a quasi-finite separated morphism is quasi-affine”. References: EGA IV (18.12.12), “more general”; EGA IV (8.11.2), “more general”.

> **Stacks 0ABS and 082J, quasi-affineness.** A quasi-finite separated morphism of algebraic
> spaces
> over `S` is quasi-affine.
>
> Such a morphism is representable by Tag 0418, so each of its represented base changes is a
> morphism of schemes which is separated, locally of finite type, locally quasi-finite and
> quasi-compact, hence quasi-affine by Tag 02LR — the statement for schemes, proved there by
> exactly the factorization through the relative normalization that the source uses here.

```lean
theorem isQuasiAffineHom_of_isQuasiFinite_isSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f) :
    IsQuasiAffineHom B S hS f
```

## Tag 082K, a lemma

[Tag 082K](https://stacks.math.columbia.edu/tag/082K) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenImmersion_isFinite_comp_eq_of_isQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFiniteFactorization.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFiniteFactorization.lean#L75).

> **Stacks 082K, Zariski's main theorem, the finite factorization.** Let
> `f : X ⟶ Y` be a quasi-finite separated morphism of algebraic spaces over `S`, with `Y`
> quasi-compact and quasi-separated. Then `f = π ∘ j` with `j : X ⟶ T` a quasi-compact open
> immersion into an algebraic space `T` and `π : T ⟶ Y` finite.

```lean
theorem exists_isOpenImmersion_isFinite_comp_eq_of_isQuasiFinite
    (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y) :
    ∃ (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (j : X ⟶ T) (π : T ⟶ Y),
      IsAlgebraicSpace B S hS T ∧ IsOpenImmersion B S hS j ∧ IsQuasiCompact B S hS j ∧
        IsFinite B S hS π ∧ j ≫ π = f
```

## Tag 0874, a lemma

[Tag 0874](https://stacks.math.columbia.edu/tag/0874) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenImmersion_isFinitePresentation_comp_eq_of_isQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFinitePresentationUnconditional.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremFinitePresentationUnconditional.lean#L51).

> **Stacks 0874.** Let `f : X ⟶ Y` be a quasi-finite separated morphism of algebraic spaces
> over `S` which is locally of finite presentation, with `Y` quasi-compact and quasi-separated.
> Then `f = π ∘ j` with `j : X ⟶ T` a quasi-compact open immersion into an algebraic space `T`
> and `π : T ⟶ Y` finite and of finite presentation.

```lean
theorem exists_isOpenImmersion_isFinitePresentation_comp_eq_of_isQuasiFinite
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (hfp : IsLocallyOfFinitePresentation B S hS f) :
    ∃ (T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (j : X ⟶ T) (π : T ⟶ Y),
      IsAlgebraicSpace B S hS T ∧ IsOpenImmersion B S hS j ∧ IsQuasiCompact B S hS j ∧
        IsFinite B S hS π ∧ IsFinitePresentation B S hS π ∧ j ≫ π = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.34, Tag 05W7](https://stacks.math.columbia.edu/tag/05W7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
