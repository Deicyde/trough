---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_of_diag_of_flat_chart, AlgebraicGeometry.Space.isAlgebraicSpace_of_relativelyRepresentable_diag_of_flat_scheme_chart, AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_quotient_groupoidInAlgebraicSpaces, AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation, AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation, AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation_scheme, AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation_scheme, AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representableDiagonal_surjective_flat_locallyOfFinitePresentation
statement: formalized
proof: formalized
---

# 80.10 Final bootstrap

Section 80.10 of the Stacks Project, [Tag 04S5](https://stacks.math.columbia.edu/tag/04S5). 1 tag here is carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04S6, a theorem

[Tag 04S6](https://stacks.math.columbia.edu/tag/04S6) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_diag_of_flat_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrap.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrap.lean#L90). The attribute's comment: “condition (5)”.

> **Stacks 04S6, condition (5).** Let `F` be a sheaf on the big fppf site of a scheme `S`
> whose absolute diagonal is representable by algebraic spaces, and suppose there is an algebraic
> space `X` over `S` and a morphism `f : X ⟶ F` which is surjective, flat and locally of finite
> presentation.  Then `F` is an algebraic space over `S`.
>
> The chart `f` is not assumed to be representable by algebraic spaces; it is so automatically, by
> `AlgebraicGeometry.Space.isRepresentableByAlgebraicSpaces_of_diagonal`, which is what turns the
> data of condition (5) into the data of condition (3).

```lean
theorem isAlgebraicSpace_of_diag_of_flat_chart
    {F X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS (diag F))
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ F)
    (hSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag hX f))
    (hFlat : HasProperty B S hS (flatProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag hX f))
    (hLfp : HasProperty B S hS (locallyOfFinitePresentationProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag hX f)) :
    IsAlgebraicSpace B S hS F
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_relativelyRepresentable_diag_of_flat_scheme_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrap.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrap.lean#L115). The attribute's comment: “condition (6)”.

> **Stacks 04S6, condition (6).** Let `F` be a sheaf on the big fppf site of a scheme `S`
> whose absolute diagonal is representable, and suppose there is a scheme `U` over `S` and a
> morphism `f : h_U ⟶ F` which is surjective, flat and locally of finite presentation.  Then `F`
> is an algebraic space over `S`.
>
> This is condition (5) for the algebraic space `h_U`: a representable diagonal is representable
> by algebraic spaces by
> `AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces.of_relativelyRepresentable`, and a
> representable presheaf is an algebraic space by **Stacks 025Z**.

```lean
theorem isAlgebraicSpace_of_relativelyRepresentable_diag_of_flat_scheme_chart
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (hdiag : yoneda.relativelyRepresentable (diag F))
    (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F)
    (hSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS
        (IsRepresentableByAlgebraicSpaces.of_relativelyRepresentable hdiag)
        (isAlgebraicSpace_yoneda B S hS U) f))
    (hFlat : HasProperty B S hS (flatProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS
        (IsRepresentableByAlgebraicSpaces.of_relativelyRepresentable hdiag)
        (isAlgebraicSpace_yoneda B S hS U) f))
    (hLfp : HasProperty B S hS (locallyOfFinitePresentationProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS
        (IsRepresentableByAlgebraicSpaces.of_relativelyRepresentable hdiag)
        (isAlgebraicSpace_yoneda B S hS U) f)) :
    IsAlgebraicSpace B S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_quotient_groupoidInAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1154). The attribute's comment: “part (1)”.

> Condition (1): the quotient of a flat, locally finitely presented
> equivalence-relation groupoid in algebraic spaces is an algebraic space.

```lean
public theorem isAlgebraicSpace_quotient_groupoidInAlgebraicSpaces
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology site S hS) (Type u)]
    {base : AlgebraicGeometry.AlgebraicSpaces site S hS}
    (G : AlgebraicGeometry.GroupoidInAlgebraicSpaces site S hS base)
    (hrel : CategoryTheory.IsEquivalenceRelation
      (AlgebraicGeometry.Space.groupoidPreRelation G).target
      (AlgebraicGeometry.Space.groupoidPreRelation G).source)
    (hsflat : AlgebraicGeometry.Space.IsFlat site S hS G.source.hom)
    (htflat : AlgebraicGeometry.Space.IsFlat site S hS G.target.hom)
    (hslfp : AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS G.source.hom)
    (htlfp : AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS G.target.hom) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS
      (AlgebraicGeometry.Space.quotientSheaf
        (AlgebraicGeometry.Space.groupoidPreRelation G)).obj
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1413). The attribute's comment: “part (3), surjectivity on base changes”.

> Condition (3) with surjectivity read, like flatness and local finite presentation, on
> every scheme-valued base change of `f`.
>
> It implies `isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation`,
> since a surjection of presheaves representable by algebraic spaces is surjective on every base
> change.

```lean
public theorem
    isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    (F : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS) F)
    {X : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u}
    (hX : AlgebraicGeometry.IsAlgebraicSpace site S hS X)
    (f : X ⟶ F)
    (hrep : AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces site S hS f)
    (hsurj : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsSurjective site S hS φ.hom) f hrep)
    (hflat : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsFlat site S hS φ.hom) f hrep)
    (hlfp : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS φ.hom)
      f hrep) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1453). The attribute's comment: “part (3)”.

> Condition (3): a representable, surjective, flat, locally finitely
> presented map from an algebraic space presents an algebraic space.

```lean
public theorem isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    (F : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS) F)
    {X : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u}
    (hX : AlgebraicGeometry.IsAlgebraicSpace site S hS X)
    (f : X ⟶ F)
    (hrep : AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces site S hS f)
    (hsurj : AlgebraicGeometry.Space.IsSurjective site S hS f)
    (hflat : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsFlat site S hS φ.hom) f hrep)
    (hlfp : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS φ.hom)
      f hrep) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1476). The attribute's comment: “part (4), surjectivity on base changes”.

> Condition (4) with surjectivity read on every scheme-valued base change of `f`:
> `isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation`
> with a scheme as the source.

```lean
public theorem
    isAlgebraicSpace_of_representable_hasProperty_surjective_flat_locallyOfFinitePresentation_scheme
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    (F : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS) F)
    (U : AlgebraicGeometry.BigFppfOver site S hS)
    (f : yoneda.obj U ⟶ F)
    (hrep : AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces site S hS f)
    (hsurj : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsSurjective site S hS φ.hom) f hrep)
    (hflat : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsFlat site S hS φ.hom) f hrep)
    (hlfp : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS φ.hom)
      f hrep) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1498). The attribute's comment: “part (4)”.

> Condition (4): the preceding criterion with a scheme as the source.

```lean
public theorem isAlgebraicSpace_of_representable_surjective_flat_locallyOfFinitePresentation_scheme
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    (F : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS) F)
    (U : AlgebraicGeometry.BigFppfOver site S hS)
    (f : yoneda.obj U ⟶ F)
    (hrep : AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces site S hS f)
    (hsurj : AlgebraicGeometry.Space.IsSurjective site S hS f)
    (hflat : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsFlat site S hS φ.hom) f hrep)
    (hlfp : AlgebraicGeometry.Space.HasProperty site S hS
      (fun ⦃_ _⦄ φ => AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS φ.hom)
      f hrep) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representableDiagonal_surjective_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1520](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1520). The attribute's comment: “part (5)”.

> Condition (5): a sheaf with diagonal representable by algebraic spaces
> and a surjective flat locally finitely presented algebraic-space presentation
> is an algebraic space.

```lean
public theorem isAlgebraicSpace_of_representableDiagonal_surjective_flat_locallyOfFinitePresentation
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    (F : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS) F)
    (hdiag : AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces site S hS (diag F))
    {X : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u}
    (hX : AlgebraicGeometry.IsAlgebraicSpace site S hS X)
    (f : X ⟶ F)
    (hsurj : AlgebraicGeometry.Space.IsSurjective site S hS f)
    (hflat : ∀ (T : AlgebraicGeometry.BigFppfOver site S hS)
      (ξ : yoneda.obj T ⟶ F),
      AlgebraicGeometry.Space.IsFlat site S hS (pullback.fst ξ f))
    (hlfp : ∀ (T : AlgebraicGeometry.BigFppfOver site S hS)
      (ξ : yoneda.obj T ⟶ F),
      AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS
        (pullback.fst ξ f)) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_of_representableDiagonal_surjective_flat_locallyOfFinitePresentation_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean, line 1550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FinalBootstrapTheorem.lean#L1550). The attribute's comment: “part (6)”.

> Condition (6): a scheme presentation suffices when the diagonal is
> representable by schemes.

```lean
public theorem
    isAlgebraicSpace_of_representableDiagonal_surjective_flat_locallyOfFinitePresentation_scheme
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    (F : (AlgebraicGeometry.BigFppfOver site S hS)ᵒᵖ ⥤ Type u)
    (hF : Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS) F)
    (hdiag : yoneda.relativelyRepresentable (diag F))
    (U : AlgebraicGeometry.BigFppfOver site S hS)
    (f : yoneda.obj U ⟶ F)
    (hsurj : AlgebraicGeometry.Space.IsSurjective site S hS f)
    (hflat : ∀ (T : AlgebraicGeometry.BigFppfOver site S hS)
      (ξ : yoneda.obj T ⟶ F),
      AlgebraicGeometry.Space.IsFlat site S hS (pullback.fst ξ f))
    (hlfp : ∀ (T : AlgebraicGeometry.BigFppfOver site S hS)
      (ξ : yoneda.obj T ⟶ F),
      AlgebraicGeometry.Space.IsLocallyOfFinitePresentation site S hS
        (pullback.fst ξ f)) :
    AlgebraicGeometry.IsAlgebraicSpace site S hS F
```

**`AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_quotientSheaf_groupoidScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FlatRelationQuotient.lean, line 3612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FlatRelationQuotient.lean#L3612). The attribute's comment: “condition (2): the quotient of a scheme by a flat, locally finitely presented equivalence relation groupoid scheme is an algebraic space”.

> **Stacks 04S6, condition (2).** Let `(U, R, s, t, c)` be a groupoid scheme over `S` whose
> object scheme belongs to the big fppf site, such that `s, t` are flat and locally of finite
> presentation and `j = (t, s) : R ⟶ U ×_S U` is an equivalence relation. Then the fppf quotient
> sheaf `U/R` is an algebraic space.

```lean
theorem isAlgebraicSpace_quotientSheaf_groupoidScheme
    (site : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : site.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology site S hS) (Type u)]
    (G : Stacks.Groupoids.GroupoidScheme S) (hU : site.Contains G.objects.left)
    [IsEquivalenceRelation G.target G.source]
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left] :
    AlgebraicGeometry.IsAlgebraicSpace site S hS
      (Stacks.Groupoids.quotientSheaf (AlgebraicGeometry.BigFppfOver.topology site S hS)
        (Over.post site.inclusion) (AlgebraicGeometry.groupoidPreRelation G)).obj
```

**`AlgebraicGeometry.Space.bootstrap04S6QuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FlatRelationQuotient.lean, line 3740](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/FlatRelationQuotient.lean#L3740). The attribute's comment: “condition (1): the quotient of an algebraic space by a flat, locally finitely presented equivalence relation of algebraic spaces is an algebraic space”.

> **Stacks 04S6, condition (1).** Let `j : R ⟶ U ×_Z U` be an equivalence relation of
> algebraic spaces over a presheaf `Z` on the big fppf site of `S`, whose target and source
> `t, s : R ⟶ U` are flat and locally of finite presentation. Then the fppf quotient sheaf `U/R`
> is an algebraic space.
>
> The proof is the source's: `U` is replaced by an étale atlas `h_{U₀} ⟶ U` (Groupoids in Spaces,
> Lemma 046P, `AlgebraicGeometry.Space.isIso_restrictQuotientSheafMap_chartInSliceMap`); the
> restricted relation `R₀ = U₀ ×_U R ×_U U₀` is then an algebraic space with a monomorphism,
> locally of finite type, to `U₀ ×_S U₀`, hence representable by Morphisms of Spaces,
> Proposition 03XX; and the resulting relation of schemes in the site is condition (2),
> `AlgebraicGeometry.Bootstrap04S6.isAlgebraicSpace_quotientSheaf_of_flat_preRelation`.

```lean
theorem bootstrap04S6QuotientSheaf (site : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : site.Contains S) : Bootstrap04S6QuotientSheaf site S hS
```

**`AlgebraicGeometry.Space.isBootstrapAlgebraicSpaceAlongFlatSurjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Unconditional.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Unconditional.lean#L51). The attribute's comment: “condition (3): a sheaf with a surjective, flat, locally finitely presented chart from an algebraic space, representable by algebraic spaces, is an algebraic space”.

> Let `F` be a sheaf on the big fppf site of `S`, and suppose there are an algebraic space `X`
> over `S` and a morphism `X ⟶ F` which is representable by algebraic spaces, surjective, flat and
> locally of finite presentation. Then `F` is an algebraic space over `S`.

```lean
theorem isBootstrapAlgebraicSpaceAlongFlatSurjection :
    IsBootstrapAlgebraicSpaceAlongFlatSurjection B S hS
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_flat_scheme_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Unconditional.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Unconditional.lean#L61). The attribute's comment: “condition (4)”.

> Let `F` be a sheaf on the big fppf site of `S`, and suppose there are a scheme `U` of the site
> and a morphism `h_U ⟶ F` which is representable by algebraic spaces (in particular, one
> representable by schemes), surjective, flat and locally of finite presentation. Then `F` is an
> algebraic space over `S`.

```lean
theorem isAlgebraicSpace_of_flat_scheme_chart
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f)
    (hSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f hf)
    (hFlat : HasProperty B S hS (flatProperty B S hS) f hf)
    (hLfp : HasProperty B S hS (locallyOfFinitePresentationProperty B S hS) f hf) :
    IsAlgebraicSpace B S hS F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.10, Tag 04S5](https://stacks.math.columbia.edu/tag/04S5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
