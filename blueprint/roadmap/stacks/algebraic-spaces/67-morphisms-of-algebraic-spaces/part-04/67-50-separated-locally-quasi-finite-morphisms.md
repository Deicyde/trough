---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isOpenSubspace_isQuasiCompactSpace_isRepresentable_image, AlgebraicGeometry.Space.isRepresentable_of_locallyQuasiFinite_separated
statement: formalized
proof: formalized
---

# 67.50 Separated, locally quasi-finite morphisms

Section 67.50 of the Stacks Project, [Tag 0417](https://stacks.math.columbia.edu/tag/0417). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03XW, a lemma

[Tag 03XW](https://stacks.math.columbia.edu/tag/03XW) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenSubspace_isQuasiCompactSpace_isRepresentable_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImageRepresentableInduction.lean, line 898](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ImageRepresentableInduction.lean#L898).

> **Stacks 03XW.** Let `t : T' ⟶ T` be an étale morphism of affine objects of the big fppf
> category over `S`, let `f : X ⟶ yoneda.obj T` be a separated and locally quasi-finite morphism
> of algebraic spaces over `S`, and let `V'` be an open subspace of `T' ×_T X` which is
> quasi-affine over `T'`. Then the image of `V'` in `X` is a quasi-compact open subspace of `X`
> which is representable.
>
> The image is the subspace cut out by the image of the point set of `V'`, whose own point set is
> that image by Tag 03BZ. Openness and quasi-compactness are
> `AlgebraicGeometry.Space.isOpenSubspace_isQuasiCompactSpace_image_of_isQuasiAffineHom` and
> representability is `AlgebraicGeometry.Space.isRepresentable_image_of_isQuasiAffineHom`.

```lean
theorem isOpenSubspace_isQuasiCompactSpace_isRepresentable_image
    {T' T : BigFppfOver B S hS}
    (hT : IsAffine ((BigFppfOver.toScheme B S hS).obj T))
    (hT' : IsAffine ((BigFppfOver.toScheme B S hS).obj T'))
    {t : T' ⟶ T} (ht : Etale ((BigFppfOver.toScheme B S hS).map t))
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    {f : X ⟶ yoneda.obj T} (hsep : IsSeparated B S hS f)
    (hlqf : IsLocallyQuasiFinite B S hS f)
    (V : Subfunctor (pullback (yoneda.map t) f)) (hV : IsOpenSubspace B S hS V)
    (hVqa : IsQuasiAffineHom B S hS (V.ι ≫ pullback.fst (yoneda.map t) f)) :
    IsOpenSubspace B S hS (openSubspaceOfPoints B S hS X
        (Set.range (pointsMap B S hS V.toFunctor
          (V.ι ≫ pullback.snd (yoneda.map t) f)))) ∧
      IsQuasiCompactSpace B S hS (openSubspaceOfPoints B S hS X
        (Set.range (pointsMap B S hS V.toFunctor
          (V.ι ≫ pullback.snd (yoneda.map t) f)))).toFunctor ∧
      (openSubspaceOfPoints B S hS X
        (Set.range (pointsMap B S hS V.toFunctor
          (V.ι ≫ pullback.snd (yoneda.map t) f)))).toFunctor.IsRepresentable
```

## Tag 03XX, a proposition

[Tag 03XX](https://stacks.math.columbia.edu/tag/03XX) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_locallyQuasiFinite_separated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteSeparatedRepresentable.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteSeparatedRepresentable.lean#L414).

> **Stacks 03XX.** A separated, locally quasi-finite algebraic space over a representable
> algebraic space over `S` is representable.

```lean
theorem isRepresentable_of_locallyQuasiFinite_separated
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X T : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hT : IsAlgebraicSpace B S hS T)
    (f : X ⟶ T)
    (hTrep : T.IsRepresentable)
    (hlqf : IsLocallyQuasiFinite B S hS f)
    (hsep : IsSeparated B S hS f) :
    X.IsRepresentable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.50, Tag 0417](https://stacks.math.columbia.edu/tag/0417)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
