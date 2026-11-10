---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.NormalizationInData.isOpenSubspace_quasiFiniteImage, AlgebraicGeometry.Space.NormalizationInData.isIso_fromPreimage_quasiFiniteImage, AlgebraicGeometry.Space.NormalizationInData.preimage_quasiFiniteImage_eq, AlgebraicGeometry.Space.NormalizationInData.range_pointsMap_preimage_quasiFiniteImage, AlgebraicGeometry.Space.exists_isOpenSubspace_isIso_fromPreimage_and_range_pointsMap_preimage_eq, AlgebraicGeometry.Space.zariskiMainTheorem
statement: formalized
proof: formalized
---

# 67.52 Zariski's Main Theorem (representable case)

Section 67.52 of the Stacks Project, [Tag 0ABQ](https://stacks.math.columbia.edu/tag/0ABQ). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ABR, a lemma

[Tag 0ABR](https://stacks.math.columbia.edu/tag/0ABR) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizationInData.isOpenSubspace_quasiFiniteImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean#L481). The attribute's comment: “the open subspace”.

> **Stacks 0ABR, the open subspace.** For a representable morphism of algebraic spaces over `S`
> which is of finite type and separated, the image in the normalization of `Y` in `X` of the
> quasi-finite locus of `f` is an open subspace of that normalization.
>
> Over a surjective étale scheme chart `W ⟶ Y` the quasi-finite locus base changes to the
> quasi-finite locus of the induced morphism of schemes (part (2) of Tag 0ABM), and Zariski's main
> theorem for schemes — Tag 03GW, Mathlib's
> `AlgebraicGeometry.Scheme.Hom.exists_isIso_morphismRestrict_toNormalization` — says that locus
> maps by an open immersion into the relative normalization of the chart, which by the chart
> description of the normalization datum is the base change of `ν`. So the restriction of `f'` to
> the quasi-finite locus is an open immersion after base change along one surjective étale chart
> of `Y'`, hence an open immersion, by Tag 03M4 for open immersions; its image is therefore an
> open subspace.

```lean
theorem isOpenSubspace_quasiFiniteImage (N : NormalizationInData B S hS f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hrep : yoneda.relativelyRepresentable f)
    (hft : IsLocallyOfFiniteType B S hS f) (hqc : IsQuasiCompact B S hS f)
    (hsep : IsSeparated B S hS f) :
    IsOpenSubspace B S hS N.quasiFiniteImage
```

**`AlgebraicGeometry.Space.NormalizationInData.isIso_fromPreimage_quasiFiniteImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean#L492). The attribute's comment: “part (1): the inverse image of the open subspace maps isomorphically onto it”.

> **Stacks 0ABR, part (1).** The inverse image of the open subspace under `f'` maps
> isomorphically onto it.

```lean
theorem isIso_fromPreimage_quasiFiniteImage (N : NormalizationInData B S hS f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hrep : yoneda.relativelyRepresentable f)
    (hft : IsLocallyOfFiniteType B S hS f) (hqc : IsQuasiCompact B S hS f)
    (hsep : IsSeparated B S hS f) :
    IsIso (N.quasiFiniteImage.fromPreimage N.toNorm)
```

**`AlgebraicGeometry.Space.NormalizationInData.preimage_quasiFiniteImage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean#L503). The attribute's comment: “part (2): the inverse image is the quasi-finite locus, as a subspace”.

> **Stacks 0ABR, part (2).** The inverse image of the open subspace under `f'` is the
> quasi-finite locus of `f`, as a subspace of `X`.

```lean
theorem preimage_quasiFiniteImage_eq (N : NormalizationInData B S hS f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hrep : yoneda.relativelyRepresentable f)
    (hft : IsLocallyOfFiniteType B S hS f) (hqc : IsQuasiCompact B S hS f)
    (hsep : IsSeparated B S hS f) :
    N.quasiFiniteImage.preimage N.toNorm = quasiFiniteLocusSubspace B S hS f
```

**`AlgebraicGeometry.Space.NormalizationInData.range_pointsMap_preimage_quasiFiniteImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean#L515). The attribute's comment: “part (2): the inverse image is the set of points of quasi-finiteness”.

> **Stacks 0ABR, part (2), on points.** The point set of the inverse image of the open subspace
> under `f'` is the set of points of `X` at which `f` is quasi-finite. This is the form in which
> the source states part (2).

```lean
theorem range_pointsMap_preimage_quasiFiniteImage (N : NormalizationInData B S hS f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hrep : yoneda.relativelyRepresentable f)
    (hft : IsLocallyOfFiniteType B S hS f) (hqc : IsQuasiCompact B S hS f)
    (hsep : IsSeparated B S hS f) :
    Set.range (pointsMap B S hS (N.quasiFiniteImage.preimage N.toNorm).toFunctor
        (N.quasiFiniteImage.preimage N.toNorm).ι) =
      {x : points B S hS X | IsQuasiFiniteAt B S hS f x}
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isIso_fromPreimage_and_range_pointsMap_preimage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationQuasiFiniteLocus.lean#L536). The attribute's comment: “the existence statement”.

> **Stacks 0ABR.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> representable, of finite type and separated, and let `X ⟶ Y' ⟶ Y` be the normalization of `Y`
> in `X`. Then there is an open subspace `U' ⊆ Y'` such that `(f')⁻¹(U') ⟶ U'` is an isomorphism
> and `(f')⁻¹(U') ⊆ X` is the set of points at which `f` is quasi-finite.
>
> The open subspace is `AlgebraicGeometry.Space.NormalizationInData.quasiFiniteImage`, the image of
> the quasi-finite locus.

```lean
theorem exists_isOpenSubspace_isIso_fromPreimage_and_range_pointsMap_preimage_eq
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y} (N : NormalizationInData B S hS f)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hrep : yoneda.relativelyRepresentable f)
    (hft : IsLocallyOfFiniteType B S hS f) (hqc : IsQuasiCompact B S hS f)
    (hsep : IsSeparated B S hS f) :
    ∃ U' : Subfunctor N.space, IsOpenSubspace B S hS U' ∧
      IsIso (U'.fromPreimage N.toNorm) ∧
      Set.range (pointsMap B S hS (U'.preimage N.toNorm).toFunctor
          (U'.preimage N.toNorm).ι) =
        {x : points B S hS X | IsQuasiFiniteAt B S hS f x}
```

## Tag 0ABS, a lemma

[Tag 0ABS](https://stacks.math.columbia.edu/tag/0ABS) in the Stacks Project.

**`AlgebraicGeometry.Space.zariskiMainTheorem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremGeneral.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiMainTheoremGeneral.lean#L211). References: EGA III (4.4.12), “more general”.

> **Zariski's main theorem for algebraic spaces.** Let `f : X ⟶ Y` be a quasi-finite
> separated morphism of algebraic spaces over a scheme `S`. Then `f` is quasi-affine, and the
> normalization of `Y` in `X` exists: there is a factorization `X --f'--> Y' --ν--> Y` of `f`
> whose base change along every étale scheme chart of `Y` is the relative normalization of that
> chart, in which `f'` is a quasi-compact open immersion and `ν` is integral.
>
> Neither side is required to be representable and no bound on sizes is assumed: the datum is
> glued along a surjective étale chart of the target in
> `AlgebraicGeometry.Space.NormalizationGluing.nonempty_normalizationInData`, and the four
> assertions about it are the theorems of
> `StacksFrontier.AlgebraicGeometry.Spaces.ZariskiMainTheoremQuasiFinite`.

```lean
theorem zariskiMainTheorem (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hqf : IsQuasiFinite B S hS f) (hsep : IsSeparated B S hS f) :
    IsQuasiAffineHom B S hS f ∧
      ∃ N : NormalizationInData B S hS f,
        N.toNorm ≫ N.fromNorm = f ∧
        IsOpenImmersion B S hS N.toNorm ∧
        IsQuasiCompact B S hS N.toNorm ∧
        IsIntegralHom B S hS N.fromNorm
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.52, Tag 0ABQ](https://stacks.math.columbia.edu/tag/0ABQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
