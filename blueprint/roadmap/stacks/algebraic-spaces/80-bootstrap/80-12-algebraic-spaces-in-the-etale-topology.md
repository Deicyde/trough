---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale, AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas_unconditional, AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas, AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas_unconditional, AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas, AlgebraicGeometry.Space.isAlgebraicSpace_of_etaleSheaf_of_smooth_surjection
statement: formalized
proof: formalized
---

# 80.12 Algebraic spaces in the étale topology

Section 80.12 of the Stacks Project, [Tag 076L](https://stacks.math.columbia.edu/tag/076L). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 076M, a lemma

[Tag 076M](https://stacks.math.columbia.edu/tag/076M) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafAlgebraicCriterionTag076M.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafAlgebraicCriterionTag076M.lean#L80).

> **Stacks 076M.** A presheaf of sets on the big fppf category over `S` which is a sheaf for
> the chosen étale topology, whose diagonal is representable and which admits a surjective étale
> atlas by a scheme is an algebraic space over `S`.
>
> Only the fppf sheaf condition is at issue, and it comes from a comparison with the fppf
> quotient sheaf `U/R` of the étale equivalence relation `R = U ×_F U`: the atlas and the
> quotient map are both locally surjective for the étale topology and have the same kernel pair,
> so `F` and `U/R` are the same coequalizer of `h_R ⇉ h_U` in étale sheaves, and `F` inherits the
> fppf sheaf condition from `U/R`. The comparison is
> `AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_isLocallySurjective_quotientMap`;
> the étale-local surjectivity of the quotient map is Stacks 02WW.

```lean
theorem isAlgebraicSpace_of_isSheaf_etale (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf ((etaleTopology B).over (B.obj hS)) F)
    (hdiag : yoneda.relativelyRepresentable (diag F))
    (hatlas : ∃ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F),
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f) :
    IsAlgebraicSpace B S hS F
```

## Tag 0BH4, a lemma

[Tag 0BH4](https://stacks.math.columbia.edu/tag/0BH4) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafAtlasCriteria.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafAtlasCriteria.lean#L111).

> **Stacks 0BH4.** Let `F` be a presheaf of sets on the big category over `S`, which is the
> common underlying category of the chosen big fppf and big étale sites. If `F` is a sheaf for the
> étale topology and there are an algebraic space `X` over `S` and a morphism `X ⟶ F` which is
> representable by algebraic spaces, surjective and étale, then `F` is an algebraic space over `S`
> in the sense of Algebraic Spaces, Definition 025Y.
>
> This is `AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas` with its
> Stacks 04S6 input discharged by `AlgebraicGeometry.Space.bootstrap04S6QuotientSheaf`.

```lean
theorem isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas_unconditional
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf ((etaleTopology B).over (B.obj hS)) F)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (a : X ⟶ F)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hsurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) a ha)
    (hetale : HasProperty B S hS (etaleMorphisms B S hS) a ha) :
    IsAlgebraicSpace B S hS F
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafSpaceCoverCriterion.lean, line 734](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafSpaceCoverCriterion.lean#L734). The attribute's comment: “granted Stacks 04S6 part (1), the algebraicity of the fppf quotient sheaf of a flat locally finitely presented equivalence relation of algebraic spaces, carried as the hypothesis `h04S6`; the library's Stacks 04S6 is conditions (5) and (6), which need the quotient's diagonal and are themselves conditional on condition (3), so neither discharges it”.

> **Stacks 0BH4.** Let `F` be a presheaf of sets on the big category over `S`, which is the
> common underlying category of the chosen big fppf and big étale sites. If `F` is a sheaf for the
> étale topology and there are an algebraic space `X` over `S` and a morphism `X ⟶ F` which is
> representable by algebraic spaces, surjective and étale, then `F` is an algebraic space over `S`
> in the sense of Algebraic Spaces, Definition 025Y.
>
> The étale cover is smooth, so the criterion is the smooth one of
> `AlgebraicGeometry.Space.coreCriterion`.

```lean
theorem isAlgebraicSpace_of_isSheaf_etale_of_etale_space_atlas
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf ((etaleTopology B).over (B.obj hS)) F)
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) (a : X ⟶ F)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hsurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) a ha)
    (hetale : HasProperty B S hS (etaleMorphisms B S hS) a ha)
    (h04S6 : Bootstrap04S6QuotientSheaf B S hS) :
    IsAlgebraicSpace B S hS F
```

## Tag 07WF, a lemma

[Tag 07WF](https://stacks.math.columbia.edu/tag/07WF) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafAtlasCriteria.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafAtlasCriteria.lean#L135).

> **Stacks 07WF.** Let `F` be a presheaf of sets on the big category over `S`, which is the
> common underlying category of the chosen big fppf and big étale sites. If `F` is a sheaf for the
> étale topology, its diagonal `Δ : F ⟶ F × F` is representable by algebraic spaces, and there are
> an object `U` of the category over `S` and a morphism `h_U ⟶ F` which is surjective and smooth,
> then `F` is an algebraic space over `S` in the sense of Algebraic Spaces, Definition 025Y.
>
> The representability by algebraic spaces of the cover is not a further hypothesis: it follows
> from the representable diagonal by
> `AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_diagonal`, and the surjectivity and
> smoothness are asked of that witness. This is
> `AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas` with its
> Stacks 04S6 input discharged by `AlgebraicGeometry.Space.bootstrap04S6QuotientSheaf`.

```lean
theorem isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas_unconditional
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf ((etaleTopology B).over (B.obj hS)) F)
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS (diag F))
    (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F)
    (hsurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) a
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag
        (isAlgebraicSpace_yoneda B S hS U) a))
    (hsmooth : HasProperty B S hS (smoothMorphismProperty B S hS) a
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag
        (isAlgebraicSpace_yoneda B S hS U) a)) :
    IsAlgebraicSpace B S hS F
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafSpaceCoverCriterion.lean, line 760](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleSheafSpaceCoverCriterion.lean#L760). The attribute's comment: “granted Stacks 04S6 part (1), the algebraicity of the fppf quotient sheaf of a flat locally finitely presented equivalence relation of algebraic spaces, carried as the hypothesis `h04S6`; the library's Stacks 04S6 is conditions (5) and (6), which need the quotient's diagonal and are themselves conditional on condition (3), so neither discharges it”.

> **Stacks 07WF.** Let `F` be a presheaf of sets on the big category over `S`, which is the
> common underlying category of the chosen big fppf and big étale sites. If `F` is a sheaf for the
> étale topology, its diagonal `Δ : F ⟶ F × F` is representable by algebraic spaces, and there are
> an object `U` of the category over `S` and a morphism `h_U ⟶ F` which is surjective and smooth,
> then `F` is an algebraic space over `S` in the sense of Algebraic Spaces, Definition 025Y.
>
> The representability by algebraic spaces of the cover is not a further hypothesis: it follows
> from the representable diagonal by
> `AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_diagonal`, and the surjectivity and
> smoothness are asked of that witness.

```lean
theorem isAlgebraicSpace_of_isSheaf_etale_of_smooth_scheme_atlas
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf ((etaleTopology B).over (B.obj hS)) F)
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS (diag F))
    (U : BigFppfOver B S hS) (a : yoneda.obj U ⟶ F)
    (hsurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) a
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag
        (isAlgebraicSpace_yoneda B S hS U) a))
    (hsmooth : HasProperty B S hS (smoothMorphismProperty B S hS) a
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag
        (isAlgebraicSpace_yoneda B S hS U) a))
    (h04S6 : Bootstrap04S6QuotientSheaf B S hS) :
    IsAlgebraicSpace B S hS F
```

## Tag 0GE0, a lemma

[Tag 0GE0](https://stacks.math.columbia.edu/tag/0GE0) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_etaleSheaf_of_smooth_surjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleTopologyBootstrap.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleTopologyBootstrap.lean#L101).

> Let `S` be a scheme contained in a big fppf site `B` and let `F` be a
> presheaf on the common underlying category `Sch_α/S` of the big fppf and the big étale site of
> `S`. Assume
>
> 1. `F` is a sheaf for the étale topology, and
> 2. there are an algebraic space `U` over `S` and a morphism `f : U ⟶ F` which is representable
>    by algebraic spaces, surjective and smooth.
>
> Then `F` is an algebraic space over `S`.

```lean
theorem isAlgebraicSpace_of_etaleSheaf_of_smooth_surjection
    {F U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigEtaleOver.topology (associatedBigEtaleSite B) S hS) F)
    (hU : IsAlgebraicSpace B S hS U) (f : U ⟶ F)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f)
    (hsurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f hf)
    (hsmooth : HasProperty B S hS (smoothMorphismProperty B S hS) f hf) :
    IsAlgebraicSpace B S hS F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.12, Tag 076L](https://stacks.math.columbia.edu/tag/076L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
