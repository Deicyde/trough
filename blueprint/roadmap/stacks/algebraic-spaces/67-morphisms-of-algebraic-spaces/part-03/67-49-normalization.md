---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_surjective_etale_chart_iff_hasLocallyFiniteIrreducibleComponents, AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_finite_codimensionZeroPoints, AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_finite_irreducibleComponents, AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_of_isRepresentable, AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian, AlgebraicGeometry.mem_genericPoints_of_flat, AlgebraicGeometry.Space.localRingDimension_eq_zero_of_isFlat, AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_and_codimensionZero_of_isFlat_of_isLocallyOfFiniteType
statement: formalized
proof: formalized
---

# 67.49 Normalization

Section 67.49 of the Stacks Project, [Tag 07U3](https://stacks.math.columbia.edu/tag/07U3). 9 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BB1, a lemma

[Tag 0BB1](https://stacks.math.columbia.edu/tag/0BB1) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_surjective_etale_chart_iff_hasLocallyFiniteIrreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L213). The attribute's comment: “conditions (1) and (2)”.

> An algebraic space has a surjective étale scheme chart with finitely many irreducible
> components over each of its quasi-compact opens if and only if every étale scheme chart has that
> property.

```lean
theorem exists_surjective_etale_chart_iff_hasLocallyFiniteIrreducibleComponents
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F) :
    (∃ (U : BigFppfOver B S hS) (f : yoneda.obj U ⟶ F),
        IsSurjective B S hS f ∧ IsEtale B S hS f ∧
          ∀ V : ((BigFppfOver.toScheme B S hS).obj U).Opens,
            IsCompact (V : Set ((BigFppfOver.toScheme B S hS).obj U)) →
              (irreducibleComponents V).Finite) ↔
      HasLocallyFiniteIrreducibleComponents B S hS F
```

**`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_finite_codimensionZeroPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L240). The attribute's comment: “conditions (2) and (3)”.

> Every étale scheme chart of `F` has finitely many irreducible components over each of its
> quasi-compact opens exactly when every quasi-compact algebraic space étale over `F` has finitely
> many points of codimension zero.

```lean
theorem hasLocallyFiniteIrreducibleComponents_iff_finite_codimensionZeroPoints
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} :
    HasLocallyFiniteIrreducibleComponents B S hS F ↔
      ∀ (G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS G →
        IsQuasiCompactSpace B S hS G → ∀ g : G ⟶ F, IsEtale B S hS g →
          {x : points B S hS G | localRingDimension B S hS x = 0}.Finite
```

**`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_finite_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L282). The attribute's comment: “conditions (2) and (4)”.

> Every étale scheme chart of `F` has finitely many irreducible components over each of its
> quasi-compact opens exactly when the space of points of every quasi-compact algebraic space étale
> over `F` has finitely many irreducible components.

```lean
theorem hasLocallyFiniteIrreducibleComponents_iff_finite_irreducibleComponents
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} :
    HasLocallyFiniteIrreducibleComponents B S hS F ↔
      ∀ (G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS G →
        IsQuasiCompactSpace B S hS G → ∀ g : G ⟶ F, IsEtale B S hS g →
          (irreducibleComponents (points B S hS G)).Finite
```

**`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_of_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L310). The attribute's comment: “representable case”.

> For an algebraic space represented by a scheme of the site,
> `HasLocallyFiniteIrreducibleComponents` is finiteness of the irreducible components of the
> quasi-compact opens of that scheme.

```lean
theorem hasLocallyFiniteIrreducibleComponents_iff_of_isRepresentable
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} [F.IsRepresentable]
    (hF : IsAlgebraicSpace B S hS F) :
    HasLocallyFiniteIrreducibleComponents B S hS F ↔
      ∀ V : ((BigFppfOver.toScheme B S hS).obj F.reprX).Opens,
        IsCompact (V : Set ((BigFppfOver.toScheme B S hS).obj F.reprX)) →
          (irreducibleComponents V).Finite
```

## Tag 0GMB, a lemma

[Tag 0GMB](https://stacks.math.columbia.edu/tag/0GMB) in the Stacks Project.

**`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationFiniteness.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationFiniteness.lean#L88).

> A locally Noetherian algebraic space over `S` has finitely many irreducible components over
> every quasi-compact open of every étale scheme chart.

```lean
theorem hasLocallyFiniteIrreducibleComponents_of_isLocallyNoetherian
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hN : HasEtaleLocalProperty B S hS F (fun T : Scheme.{u} ↦ IsLocallyNoetherian T)) :
    HasLocallyFiniteIrreducibleComponents B S hS F
```

## Tag 0GMC, a lemma

[Tag 0GMC](https://stacks.math.columbia.edu/tag/0GMC) in the Stacks Project.

**`AlgebraicGeometry.mem_genericPoints_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/FlatCodimensionZero.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/FlatCodimensionZero.lean#L183). The attribute's comment: “representable case”.

> **Stacks Project, Tag 0GMC, representable case.** A flat morphism of schemes carries a
> generic point of an irreducible component of its source to a generic point of an irreducible
> component of its target. Equivalently, it carries codimension-zero points to
> codimension-zero points, which is the second conclusion of Tag 0GMD.

```lean
public theorem mem_genericPoints_of_flat {X Y : Scheme.{u}} (f : X ⟶ Y) [Flat f]
    {x : X} (hx : x ∈ genericPoints X) : f x ∈ genericPoints Y
```

**`AlgebraicGeometry.Space.localRingDimension_eq_zero_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L460).

> A flat morphism of algebraic spaces takes points of codimension zero to points of codimension
> zero.

```lean
theorem localRingDimension_eq_zero_of_isFlat
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsFlat B S hS f)
    (x : points B S hS X) (hx : localRingDimension B S hS x = 0) :
    localRingDimension B S hS (pointsMap B S hS X f x) = 0
```

## Tag 0GMD, a lemma

[Tag 0GMD](https://stacks.math.columbia.edu/tag/0GMD) in the Stacks Project.

**`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_and_codimensionZero_of_isFlat_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationFlatFiniteType.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationFlatFiniteType.lean#L56).

> **Stacks 0GMD.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is flat and
> locally of finite type, and assume `Y` satisfies the equivalent conditions of Stacks 0BB1. Then
> `X` satisfies those conditions too, and for every point `x` of `X` of codimension zero the image
> `f x` has codimension zero in `Y`.

```lean
theorem hasLocallyFiniteIrreducibleComponents_and_codimensionZero_of_isFlat_of_isLocallyOfFiniteType
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsFlat B S hS f)
    (hft : IsLocallyOfFiniteType B S hS f)
    (hYfinite : HasLocallyFiniteIrreducibleComponents B S hS Y) :
    HasLocallyFiniteIrreducibleComponents B S hS X ∧
      ∀ x : points B S hS X, localRingDimension B S hS x = 0 →
        localRingDimension B S hS (pointsMap B S hS X f x) = 0
```

## Tag 07U4, a lemma

[Tag 07U4](https://stacks.math.columbia.edu/tag/07U4) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizationData.existsUnique_normalizationLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationFunctoriality.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationFunctoriality.lean#L68). The attribute's comment: “part (3), for arbitrary normalization data of the two spaces: the unique lift of a morphism preserving codimension-zero points”.

> **Stacks 07U4, part (3).** Let `f : F ⟶ G` be a morphism of algebraic spaces over `S`
> carrying every point of codimension zero to a point of codimension zero, and let `ν : F^ν ⟶ F`
> and `μ : G^ν ⟶ G` be normalizations. Then there is a unique morphism `f^ν : F^ν ⟶ G^ν` with
> `μ ∘ f^ν = f ∘ ν`.
>
> This is the universal property of the normalization of `G`, part (4) of Stacks 0BB4, applied to
> the composite `F^ν ⟶ F ⟶ G`. Its two hypotheses on that composite are normality of `F^ν`, which
> is part (1) of Stacks 0BB4, and preservation of codimension-zero points, which holds for `ν` by
> part (3) of Stacks 0BB4 and for `f` by assumption.

```lean
theorem existsUnique_normalizationLift {G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (D : NormalizationData B S hS F) (D' : NormalizationData B S hS G)
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G) (f : F ⟶ G)
    (hgeneric : ∀ x : points B S hS F, localRingDimension B S hS x = 0 →
      localRingDimension B S hS (pointsMap B S hS F f x) = 0) :
    ∃! g : D.space ⟶ D'.space, g ≫ D'.hom = D.hom ≫ f
```

**`AlgebraicGeometry.Space.NormalizationData.isIso_pullbackLift_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationFunctoriality.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationFunctoriality.lean#L173). The attribute's comment: “part (4), for a smooth morphism and arbitrary normalization data of the two spaces”. References: SGA 3 X (8.9), “partial”.

> **Stacks 07U4, part (4).** Let `f : F ⟶ G` be a smooth — in particular an étale — morphism
> of algebraic spaces over `S` with `G` satisfying the equivalent conditions of Stacks 0BB1, and
> let `ν : F^ν ⟶ F` and `μ : G^ν ⟶ G` be normalizations. Then `F` satisfies the equivalent
> conditions of Stacks 0BB1 and `f` carries points of codimension zero to points of codimension
> zero — these are the hypotheses of part (3) — and the morphism `f^ν` of part (3) induces an
> isomorphism `F^ν ⟶ F ×_G G^ν`.
>
> The two hypotheses of part (3) are Stacks 0GMD and Stacks 0GMC for the flat, locally
> finite-type morphism `f`.
>
> For the isomorphism, `F ×_G G^ν` is terminal among normal algebraic spaces over `F` preserving
> codimension zero in the same way `F^ν` is, and the comparison morphisms are therefore mutually
> inverse. That `F ×_G G^ν` is such an object is read off one chart:
> `AlgebraicGeometry.Space.NormalizationData.exists_chart_pullback_snd_of_isSmooth` exhibits a
> surjective étale scheme chart of `F` over which `pullback.snd μ f` is the normalization of the
> chart, which makes `F ×_G G^ν` normal — the chart of it so produced has a normal scheme — and
> makes `pullback.snd μ f` preserve codimension zero, codimension zero being tested on that
> chart. The universal property of `F^ν`, part (4) of Stacks 0BB4, then supplies the morphism
> `F ×_G G^ν ⟶ F^ν` over `F`; its two composites with the canonical `F^ν ⟶ F ×_G G^ν` are
> identities by the uniqueness halves of that property for `F` and for `G`.

```lean
theorem isIso_pullbackLift_of_isSmooth {G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (D : NormalizationData B S hS F) (D' : NormalizationData B S hS G)
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    {f : F ⟶ G} (hf : IsSmooth B S hS f)
    (hGfin : HasLocallyFiniteIrreducibleComponents B S hS G) :
    HasLocallyFiniteIrreducibleComponents B S hS F ∧
      (∀ x : points B S hS F, localRingDimension B S hS x = 0 →
        localRingDimension B S hS (pointsMap B S hS F f x) = 0) ∧
      ∀ (g : D.space ⟶ D'.space) (hg : g ≫ D'.hom = D.hom ≫ f),
        IsIso (pullback.lift g D.hom hg)
```

**`AlgebraicGeometry.Space.NormalizationData.exists_iso_yoneda_normalizationScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationComparison.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationComparison.lean#L96). The attribute's comment: “part (2): the normalization of a scheme as an algebraic space”.

> Let `X` be an object of the big fppf site of `S` every
> quasi-compact open of whose underlying scheme has finitely many irreducible components, and let
> `D` be normalization data for the algebraic space it represents. Then `D.space` is represented
> by an object `Xν` of the site whose underlying scheme is the normalization scheme of the
> underlying scheme of `X`, and under that identification `D.hom` is the normalization
> morphism.

```lean
theorem exists_iso_yoneda_normalizationScheme {X : BigFppfOver B S hS}
    (D : NormalizationData B S hS (yoneda.obj X))
    (hX : ∀ V : ((BigFppfOver.toScheme B S hS).obj X).Opens,
      IsCompact (V : Set ((BigFppfOver.toScheme B S hS).obj X)) →
        (irreducibleComponents V).Finite) :
    ∃ (Xν : BigFppfOver B S hS) (p : Xν ⟶ X)
      (e : ((BigFppfOver.toScheme B S hS).obj Xν) ≅
        Scheme.normalizationScheme ((BigFppfOver.toScheme B S hS).obj X) hX)
      (φ : D.space ≅ yoneda.obj Xν),
      (BigFppfOver.toScheme B S hS).map p =
          e.hom ≫ Scheme.normalization ((BigFppfOver.toScheme B S hS).obj X) hX ∧
        φ.hom ≫ yoneda.map p = D.hom
```

**`AlgebraicGeometry.Space.NormalizationData.isNormal_and_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationIntegral.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationIntegral.lean#L114). The attribute's comment: “part (1)”.

> **Stacks 07U4, part (1).** Let `F` be an algebraic space over `S` equipped with
> normalization data. Then the normalization of `F` is a normal algebraic space over `S` and the
> normalization morphism is integral.
>
> The two halves are `AlgebraicGeometry.Space.NormalizationData.isNormal` and
> `AlgebraicGeometry.Space.NormalizationData.isIntegralHom`. The hypotheses of Stacks 0BB1 are
> carried by the chart field of `AlgebraicGeometry.Space.NormalizationData`, which produces for
> every surjective étale scheme chart the finiteness of the sets of irreducible components of its
> quasi-compact opens.

```lean
theorem isNormal_and_isIntegralHom {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (D : NormalizationData B S hS F) (hF : IsAlgebraicSpace B S hS F) :
    Space.IsNormal B S hS D.space ∧ Space.IsIntegralHom B S hS D.hom
```

**`AlgebraicGeometry.Space.isNormal_and_isIntegralHom_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean#L83). The attribute's comment: “part (1)”.

> **Stacks 07U4, part (1).** Let `F` be an algebraic space over `S` satisfying the equivalent
> conditions of Tag 0BB1. Then its normalization `F^ν` is a normal algebraic space and the
> normalization morphism `ν_F : F^ν ⟶ F` is integral.

```lean
theorem isNormal_and_isIntegralHom_normalization {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS F) :
    Space.IsNormal B S hS (normalizationPresheaf B S hS hF hfin) ∧
      Space.IsIntegralHom B S hS (normalization B S hS hF hfin)
```

**`AlgebraicGeometry.Space.exists_iso_yoneda_normalizationScheme_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean#L97). The attribute's comment: “part (2)”.

> **Stacks 07U4, part (2).** Let `X` be an object of the big fppf site of `S` every
> quasi-compact open of whose underlying scheme has finitely many irreducible components, so that
> the algebraic space `X` represents satisfies the conditions of Tag 0BB1. Then the normalization
> `X^ν` of that algebraic space is represented by an object `Xν` of the site whose underlying
> scheme is the normalization scheme of the underlying scheme of `X`, and under that
> identification `ν_X` is the normalization morphism of Tag 035E.

```lean
theorem exists_iso_yoneda_normalizationScheme_normalization (X : BigFppfOver B S hS)
    (hX : ∀ V : ((BigFppfOver.toScheme B S hS).obj X).Opens,
      IsCompact (V : Set ((BigFppfOver.toScheme B S hS).obj X)) →
        (irreducibleComponents V).Finite) :
    ∃ (Xν : BigFppfOver B S hS) (p : Xν ⟶ X)
      (e : ((BigFppfOver.toScheme B S hS).obj Xν) ≅
        Scheme.normalizationScheme ((BigFppfOver.toScheme B S hS).obj X) hX)
      (φ : normalizationPresheaf B S hS (isAlgebraicSpace_yoneda B S hS X)
        (hasLocallyFiniteIrreducibleComponents_yoneda B S hS X hX) ≅ yoneda.obj Xν),
      (BigFppfOver.toScheme B S hS).map p =
          e.hom ≫ Scheme.normalization ((BigFppfOver.toScheme B S hS).obj X) hX ∧
        φ.hom ≫ yoneda.map p = normalization B S hS (isAlgebraicSpace_yoneda B S hS X)
          (hasLocallyFiniteIrreducibleComponents_yoneda B S hS X hX)
```

**`AlgebraicGeometry.Space.existsUnique_comp_normalization_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean#L119). The attribute's comment: “part (3)”.

> **Stacks 07U4, part (3).** Let `f : F ⟶ G` be a morphism of algebraic spaces over `S` both
> satisfying the equivalent conditions of Tag 0BB1, such that every point of codimension zero of
> `F` maps to a point of codimension zero of `G`. Then there is a unique morphism
> `f^ν : F^ν ⟶ G^ν` with `ν_G ∘ f^ν = f ∘ ν_F`.

```lean
theorem existsUnique_comp_normalization_eq {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hFfin : HasLocallyFiniteIrreducibleComponents B S hS F)
    (hG : IsAlgebraicSpace B S hS G) (hGfin : HasLocallyFiniteIrreducibleComponents B S hS G)
    (f : F ⟶ G)
    (hgeneric : ∀ x : points B S hS F, localRingDimension B S hS x = 0 →
      localRingDimension B S hS (pointsMap B S hS F f x) = 0) :
    ∃! g : normalizationPresheaf B S hS hF hFfin ⟶ normalizationPresheaf B S hS hG hGfin,
      g ≫ normalization B S hS hG hGfin = normalization B S hS hF hFfin ≫ f
```

**`AlgebraicGeometry.Space.isIso_pullbackLift_normalization_of_isEtale_or_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationProperties.lean#L144). The attribute's comment: “part (4)”.

> **Stacks 07U4, part (4).** Let `f : F ⟶ G` be an étale or a smooth morphism of algebraic
> spaces over `S` with `G` satisfying the equivalent conditions of Tag 0BB1. Then the hypotheses of
> part (3) hold — `F` satisfies the conditions of Tag 0BB1 too, and `f` carries points of
> codimension zero to points of codimension zero — and the morphism `f^ν : F^ν ⟶ G^ν` of part (3)
> induces an isomorphism `F^ν ⟶ F ×_G G^ν`.
>
> The third conjunct is the existence and uniqueness of `f^ν`, part (3) at the hypotheses just
> established, and the fourth is the isomorphism `(f^ν, ν_F) : F^ν ⟶ F ×_G G^ν`.
>
> The condition of Tag 0BB1 on `F` is stated as an existential because the normalization `F^ν`
> is only defined given it; by proof irrelevance the witness does not matter. The isomorphism is
> asserted for every `g` with `ν_G ∘ g = f ∘ ν_F`, and by the third conjunct there is exactly one
> such `g`, namely `f^ν`.

```lean
theorem isIso_pullbackLift_normalization_of_isEtale_or_isSmooth
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hGfin : HasLocallyFiniteIrreducibleComponents B S hS G) {f : F ⟶ G}
    (hf : IsEtale B S hS f ∨ IsSmooth B S hS f) :
    ∃ hFfin : HasLocallyFiniteIrreducibleComponents B S hS F,
      (∀ x : points B S hS F, localRingDimension B S hS x = 0 →
        localRingDimension B S hS (pointsMap B S hS F f x) = 0) ∧
      (∃! g : normalizationPresheaf B S hS hF hFfin ⟶ normalizationPresheaf B S hS hG hGfin,
        g ≫ normalization B S hS hG hGfin = normalization B S hS hF hFfin ≫ f) ∧
      ∀ (g : normalizationPresheaf B S hS hF hFfin ⟶ normalizationPresheaf B S hS hG hGfin)
        (hg : g ≫ normalization B S hS hG hGfin = normalization B S hS hF hFfin ≫ f),
        IsIso (pullback.lift g (normalization B S hS hF hFfin) hg)
```

**`AlgebraicGeometry.Space.exists_normalizationData_isNormal_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSiteChart.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSiteChart.lean#L106). The attribute's comment: “the construction and part (1) at the hypotheses of the tag: an algebraic space satisfying condition (2) of Tag 0BB1 has normalization data, its normalization is normal, and its normalization morphism is integral”.

> **Stacks 07U4, the construction together with part (1), at the hypotheses of the tag.** Let
> `F` be an algebraic space over `S` satisfying condition (2) of Tag 0BB1: every quasi-compact
> open of every étale scheme chart of `F` has finitely many irreducible components. Then there
> *is* normalization data for `F` — an algebraic space `F^ν` over `S` together with a morphism
> `ν_F : F^ν ⟶ F` whose base change along every surjective étale scheme chart of `F` is the
> normalization of that chart — with `F^ν` normal and `ν_F` integral.
>
> Nothing is assumed beyond the two hypotheses the tag itself carries: no normalization data is
> given, `F` is not assumed representable, and no bound on sizes is imposed. The datum is
> `AlgebraicGeometry.Space.nonempty_normalizationData`, which forms `F^ν` as the quotient of a
> normalized étale presentation, and the two properties are
> `AlgebraicGeometry.Space.NormalizationData.isNormal_and_isIntegralHom`.
>
> The other three parts of the tag are stated for an arbitrary
> `AlgebraicGeometry.Space.NormalizationData` and so are unconditional as they stand; what this
> statement adds to them is that their hypothesis is always satisfiable. Part (2), the
> identification of the normalization of a representable algebraic space with the normalization
> scheme of the representing scheme, is
> `AlgebraicGeometry.Space.NormalizationData.exists_iso_yoneda_normalizationScheme`. Part (3), the
> unique lift of a morphism carrying points of codimension zero to points of codimension zero, is
> `AlgebraicGeometry.Space.NormalizationData.existsUnique_normalizationLift`. Part (4), the
> identification of the normalization of the source of a smooth — in particular an étale —
> morphism with the base change of the normalization of the target, is
> `AlgebraicGeometry.Space.NormalizationData.isIso_pullbackLift_of_isSmooth`.

```lean
theorem exists_normalizationData_isNormal_isIntegralHom (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS F) :
    ∃ D : NormalizationData B S hS F,
      Space.IsNormal B S hS D.space ∧ Space.IsIntegralHom B S hS D.hom
```

**`AlgebraicGeometry.Space.NormalizationData.isPullback_hom_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSmoothBaseChange07U4.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSmoothBaseChange07U4.lean#L172). The attribute's comment: “part (4) for a smooth morphism of algebraic spaces, with given normalizations”.

> **Stacks 07U4, part (4), for a smooth morphism of algebraic spaces: the normalization square
> is cartesian.** Let `φ : F ⟶ G` be a smooth morphism of algebraic spaces over `S`, let `D` be
> normalization data for `G` and `D'` normalization data for `F`. Then there is a morphism
> `F^ν ⟶ G^ν` over `φ` exhibiting `F^ν` as the fibre product `F ×_G G^ν`.
>
> The morphism `F^ν ⟶ G^ν` and its inverse comparison `F ×_G G^ν ⟶ F^ν` both come from the
> universal property of the normalization, Stacks 0BB4 part (4): `F^ν` is normal, and so is
> `F ×_G G^ν`, being smooth over the normal space `G^ν`; the relevant morphisms carry codimension
> zero to codimension zero because flat morphisms do (Stacks 0GMC), because the normalization
> morphisms do (Stacks 0BB4 part (3)), and because the projection `F ×_G G^ν ⟶ F` does
> (`AlgebraicGeometry.Space.NormalizationData.localRingDimension_pullback_snd_eq_zero`). The two
> composites are identities by the uniqueness half of the same universal property.

```lean
theorem isPullback_hom_of_isSmooth (D : NormalizationData B S hS G)
    (D' : NormalizationData B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hF : IsAlgebraicSpace B S hS F) (φ : F ⟶ G) (hφ : IsSmooth B S hS φ) :
    ∃ m : D'.space ⟶ D.space, IsPullback m D'.hom D.hom φ
```

**`AlgebraicGeometry.Space.NormalizationData.exists_isPullback_hom_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSmoothBaseChange07U4.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSmoothBaseChange07U4.lean#L229). The attribute's comment: “part (4) for a smooth morphism of algebraic spaces”.

> **Stacks 07U4, part (4), for a smooth morphism, with the normalization of the source
> produced.** Only normalization data for the target is given: the source satisfies the condition
> of Stacks 0BB1 because the target does and the morphism is flat and locally of finite type
> (Stacks 0GMD), so it has normalization data by Stacks 07U4, and
> `AlgebraicGeometry.Space.NormalizationData.isPullback_hom_of_isSmooth` applies to it.

```lean
theorem exists_isPullback_hom_of_isSmooth (D : NormalizationData B S hS G)
    (hG : IsAlgebraicSpace B S hS G) (hF : IsAlgebraicSpace B S hS F) (φ : F ⟶ G)
    (hφ : IsSmooth B S hS φ) (hGfin : HasLocallyFiniteIrreducibleComponents B S hS G) :
    ∃ (D' : NormalizationData B S hS F) (m : D'.space ⟶ D.space),
      IsPullback m D'.hom D.hom φ
```

**`AlgebraicGeometry.Space.nonempty_normalizationData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSpaceConstruction.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSpaceConstruction.lean#L202). The attribute's comment: “the existence of the normalization”.

> **Tag 07U4, the existence of the normalization.** An algebraic space over `S` every
> quasi-compact open of every étale scheme chart of which has finitely many irreducible
> components — condition (2) of Tag 0BB1 — has normalization data: an algebraic space `F^ν` over
> `S` with a morphism `F^ν ⟶ F` whose base change along every surjective étale scheme chart of
> `F` is the normalization of that chart.
>
> The datum is glued along a surjective étale chart `w : h_U ⟶ F`: the normalizations of the
> charts along `R = U ×_F U` form an étale equivalence relation, the quotient sheaf is an
> algebraic space by Tag 02WW, and the chart condition is checked at `w` by a computation with
> the kernel pair of the quotient map and at every other chart by descent along the refinement.
> No representability and no bound on sizes is assumed.
>
> The four numbered parts of Tag 07U4 are not proved here; they are the subject of
> `StacksFrontier.AlgebraicGeometry.Spaces.Normal`,
> `StacksFrontier.AlgebraicGeometry.Spaces.NormalizationIntegral` and
> `StacksFrontier.AlgebraicGeometry.Spaces.NormalizationEtaleChart`, which assume the datum this
> theorem produces.

```lean
theorem nonempty_normalizationData {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS F) :
    Nonempty (NormalizationData B S hS F)
```

## Tag 0BB2, a definition

[Tag 0BB2](https://stacks.math.columbia.edu/tag/0BB2) in the Stacks Project.

**`AlgebraicGeometry.Space.normalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSiteChart.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationSiteChart.lean#L188). The attribute's comment: “the normalization ν_F : F^ν ⟶ F of an algebraic space satisfying the conditions of Tag 0BB1, defined as the construction of Tag 07U4 (the quotient of the normalized étale presentation); unique up to unique isomorphism over F by existsUnique_iso_normalization”.

> **Stacks 0BB2, the normalization of an algebraic space.** Let `F` be an algebraic space over
> `S` satisfying the equivalent conditions of Tag 0BB1. The *normalization* of `F` is the morphism
>
> `ν_F : F^ν ⟶ F`
>
> constructed in Tag 07U4. Concretely it is the morphism of the normalization datum
> `AlgebraicGeometry.Space.normalizationData`, which is the construction of Tag 07U4,
> `AlgebraicGeometry.Space.NormSpaceGluing.normalizationDataOfPresentation`, run on a chosen
> surjective étale scheme chart `w : h_U ⟶ F` and its kernel pair `R = U ×_F U`: the
> normalizations of the charts `R^ν ⇉ U^ν` form an étale equivalence relation,
> `F^ν = U^ν / R^ν` (`AlgebraicGeometry.Space.normalizationPresheaf`) is its quotient, an
> algebraic space by Tag 02WW, and `ν_F` is the morphism `F^ν ⟶ F` through which the
> normalization `U^ν ⟶ U ⟶ F` of the chart descends. No normalization datum or other structure is
> an input: the definition depends on `F` and on the two hypotheses of the tag only.
>
> **Defining properties.** `ν_F` is characterised, up to unique isomorphism over `F`, by its
> *chart condition*: along every surjective étale scheme chart `U ⟶ F` its base change is the
> normalization `U^ν ⟶ U` of the chart (`AlgebraicGeometry.Space.normalization_chart`). Any
> morphism with this property — any `AlgebraicGeometry.Space.NormalizationData` for `F` — is
> identified with `ν_F` by a unique isomorphism over `F`
> (`AlgebraicGeometry.Space.existsUnique_iso_normalization`), so the choice of the chart made by
> the construction affects nothing up to unique isomorphism, as in the source. `ν_F` is moreover
> the universal morphism to `F` from a normal algebraic space which carries points of codimension
> zero to points of codimension zero (`AlgebraicGeometry.Space.existsUnique_lift_normalization`).
>
> **The theorems of Tag 07U4 about it.** Part (1): `F^ν` is an algebraic space
> (`AlgebraicGeometry.Space.isAlgebraicSpace_normalizationPresheaf`), normal
> (`AlgebraicGeometry.Space.isNormal_normalizationPresheaf`), and `ν_F` is integral
> (`AlgebraicGeometry.Space.isIntegralHom_normalization`); at the hypotheses of the tag this is
> also `AlgebraicGeometry.Space.exists_normalizationData_isNormal_isIntegralHom`. Parts (2) to (4)
> — the comparison with the normalization of a scheme, the unique lift `f^ν` of a morphism
> preserving codimension-zero points, and `X^ν ≅ X ×_Y Y^ν` along a smooth morphism — are
> `AlgebraicGeometry.Space.NormalizationData.exists_iso_yoneda_normalizationScheme`,
> `AlgebraicGeometry.Space.NormalizationData.existsUnique_normalizationLift` and
> `AlgebraicGeometry.Space.NormalizationData.isIso_pullbackLift_of_isSmooth`, which hold for every
> normalization datum and so in particular for `AlgebraicGeometry.Space.normalizationData`, whose
> morphism this is. Surjectivity and the bijection on codimension-zero points (Tag 0BB4) are
> `AlgebraicGeometry.Space.isSurjective_normalization` and
> `AlgebraicGeometry.Space.bijOn_codimensionZeroPoints_normalization`.
>
> The hypothesis carried is condition (2) of Tag 0BB1,
> `AlgebraicGeometry.Space.HasLocallyFiniteIrreducibleComponents`, which the comparisons of that
> tag —
> `AlgebraicGeometry.Space.exists_surjective_etale_chart_iff_hasLocallyFiniteIrreducibleComponents`,
> `AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_finite_codimensionZeroPoints`,
> `AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_finite_irreducibleComponents`
> and `AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_iff_of_isRepresentable` —
> identify with each of the other conditions, so it is the hypothesis Tag 0BB2 itself carries.
> Nothing further is assumed: `F` is not assumed representable and no bound on sizes is
> imposed.

```lean
def normalization (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS F) :
    normalizationPresheaf B S hS hF hfin ⟶ F
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.NormalizationData.hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Space.NormalizationData.hom#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 1144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L1144) (StacksFrontier).

## Tag 0BB3, a lemma

[Tag 0BB3](https://stacks.math.columbia.edu/tag/0BB3) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizationData.existsUnique_lift_hom_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 1078](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L1078). The attribute's comment: “the factorization through the reduction”.

> The normalization morphism of an algebraic space factors uniquely through any closed subspace
> whose points are all the points of the space, in particular through the reduction.

```lean
theorem existsUnique_lift_hom_reduction (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) (R : Subfunctor F) (hR : IsClosedSubspace B S hS R)
    (hfull : Set.range (pointsMap B S hS R.toFunctor R.ι) = Set.univ) :
    ∃! g : D.space ⟶ R.toFunctor, g ≫ R.ι = D.hom
```

**`AlgebraicGeometry.Space.NormalizationData.existsUnique_iso_of_hom_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 1097](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L1097). The attribute's comment: “the normalization of the reduction”.

> The factorization of the normalization morphism through the reduction exhibits the
> normalization of an algebraic space as the normalization of its reduction: it is carried to any
> normalization morphism of the reduction by a unique isomorphism.

```lean
theorem existsUnique_iso_of_hom_reduction (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) (R : Subfunctor F) (hR : IsClosedSubspace B S hS R)
    (hfull : Set.range (pointsMap B S hS R.toFunctor R.ι) = Set.univ)
    (D' : NormalizationData B S hS R.toFunctor) (g : D.space ⟶ R.toFunctor)
    (hg : g ≫ R.ι = D.hom) :
    ∃! e : D.space ≅ D'.space, e.hom ≫ D'.hom = g
```

**`AlgebraicGeometry.Space.NormalizationData.onReduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationReductionData.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/NormalizationReductionData.lean#L414). The attribute's comment: “the normalization of the reduction: the factorization is normalization data”.

> **Stacks 0BB3, the normalization of the reduction.** The normalization of an algebraic
> space *is* the normalization of its reduction: the factorization of the normalization morphism
> through any closed subspace whose points are all the points of the space — in particular
> through the reduced one — is itself normalization data for that subspace, on the same
> algebraic space.
>
> The morphism is the unique factorization of
> `AlgebraicGeometry.Space.NormalizationData.existsUnique_lift_hom_reduction`, and the chart
> condition is `AlgebraicGeometry.Space.NormalizationData.chart_of_hom_reduction`. Nothing is
> assumed about the subspace beyond being closed and carrying every point: no normalization of
> it is given, it is constructed.

```lean
noncomputable def onReduction (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) (R : Subfunctor F) (hR : IsClosedSubspace B S hS R)
    (hfull : Set.range (pointsMap B S hS R.toFunctor R.ι) = Set.univ) :
    NormalizationData B S hS R.toFunctor
```

**`AlgebraicGeometry.Space.existsUnique_comp_ι_reduction_eq_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationReduction.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationReduction.lean#L101). The attribute's comment: “the normalization morphism ν_X of Tag 0BB2 factors uniquely through the reduction X_red ⟶ X”.

> **Stacks 0BB3, the factorization.** Let `X` be an algebraic space over `S` satisfying the
> equivalent conditions of Tag 0BB1. The normalization morphism `ν_X : X^ν ⟶ X` of Tag 0BB2
> factors through the reduction `X_red ⟶ X` of Tag 047X, and the factorization is unique.
>
> This is `AlgebraicGeometry.Space.NormalizationData.existsUnique_lift_hom_reduction` at the
> normalization datum Tag 0BB2 constructs and at the reduction.

```lean
theorem existsUnique_comp_ι_reduction_eq_normalization
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X) :
    ∃! g : normalizationPresheaf B S hS hX hfin ⟶ (reduction B S hS X hX).toFunctor,
      g ≫ (reduction B S hS X hX).ι = normalization B S hS hX hfin
```

**`AlgebraicGeometry.Space.existsUnique_iso_normalization_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NormalizationReduction.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NormalizationReduction.lean#L147). The attribute's comment: “the factorization X^ν ⟶ X_red is the normalization ν_{X_red} of Tag 0BB2: they are isomorphic over X_red by a unique isomorphism”.

> **Stacks 0BB3, the factorization is the normalization of the reduction.** Let `X` be an
> algebraic space over `S` satisfying the equivalent conditions of Tag 0BB1, so that its reduction
> `X_red` satisfies them too
> (`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_reduction`). Then the
> factorization `X^ν ⟶ X_red` of the normalization morphism through the reduction is the
> normalization `ν_{X_red} : X_red^ν ⟶ X_red` of Tag 0BB2: there is a unique isomorphism
> `X^ν ≅ X_red^ν` over `X_red`.
>
> Nothing is assumed about the normalization of `X_red`: it is the one Tag 0BB2 constructs. The
> statement is `AlgebraicGeometry.Space.NormalizationData.existsUnique_iso_of_hom_reduction` at the
> two normalization data Tag 0BB2 constructs, for `X` and for `X_red`.

```lean
theorem existsUnique_iso_normalization_reduction {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hfin : HasLocallyFiniteIrreducibleComponents B S hS X) :
    ∃! e : normalizationPresheaf B S hS hX hfin ≅
        normalizationPresheaf B S hS (isAlgebraicSpace_reduction B S hS hX)
          (hasLocallyFiniteIrreducibleComponents_reduction B S hS hX hfin),
      e.hom ≫ normalization B S hS (isAlgebraicSpace_reduction B S hS hX)
          (hasLocallyFiniteIrreducibleComponents_reduction B S hS hX hfin) =
        normalizationToReduction B S hS hX hfin
```

## Tag 0BB4, a lemma

[Tag 0BB4](https://stacks.math.columbia.edu/tag/0BB4) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizationData.hasEtaleLocalProperty_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L566). The attribute's comment: “part (1): the normalization is normal”.

> The normalization of an algebraic space is normal.

```lean
theorem hasEtaleLocalProperty_isNormal (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) :
    HasEtaleLocalProperty B S hS D.space (fun X : Scheme.{u} => IsNormal X)
```

**`AlgebraicGeometry.Space.NormalizationData.isSurjective_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L589). The attribute's comment: “part (2): the normalization morphism is surjective”.

> The normalization morphism of an algebraic space is surjective.

```lean
theorem isSurjective_hom (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) : IsSurjective B S hS D.hom
```

**`AlgebraicGeometry.Space.NormalizationData.isIntegralHom_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L618). The attribute's comment: “part (2): the normalization morphism is integral”.

> The normalization morphism of an algebraic space is an integral morphism of algebraic
> spaces.

```lean
theorem isIntegralHom_hom (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) : IsIntegralHom B S hS D.hom
```

**`AlgebraicGeometry.Space.NormalizationData.bijOn_codimensionZeroPoints_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L629). The attribute's comment: “part (3): bijection on codimension-zero points”.

> The normalization morphism induces a bijection between the codimension-zero points of the
> normalization and those of the algebraic space.

```lean
theorem bijOn_codimensionZeroPoints_hom (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) :
    Set.BijOn (pointsMap B S hS D.space D.hom)
      {x : points B S hS D.space | localRingDimension B S hS x = 0}
      {x : points B S hS F | localRingDimension B S hS x = 0}
```

**`AlgebraicGeometry.Space.NormalizationData.existsUnique_lift_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L703). The attribute's comment: “part (4): the universal property”. References: SGA 3 X (8.9), “partial”.

> A morphism to `F` from a normal algebraic space which carries points of codimension zero to
> points of codimension zero factors uniquely through the normalization of `F`.

```lean
theorem existsUnique_lift_hom (D : NormalizationData B S hS F)
    (hF : IsAlgebraicSpace B S hS F) {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hZ : IsAlgebraicSpace B S hS Z)
    (hZnormal : HasEtaleLocalProperty B S hS Z fun Y : Scheme.{u} => IsNormal Y) (f : Z ⟶ F)
    (hgeneric : ∀ z : points B S hS Z, localRingDimension B S hS z = 0 →
      localRingDimension B S hS (pointsMap B S hS Z f z) = 0) :
    ∃! g : Z ⟶ D.space, g ≫ D.hom = f
```

## Tag 0BB5, a lemma

[Tag 0BB5](https://stacks.math.columbia.edu/tag/0BB5) in the Stacks Project.

**`AlgebraicGeometry.Space.NormalizationData.isFinite_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean, line 955](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Normalization.lean#L955).

> The normalization morphism of a Nagata algebraic space over `S` is a finite morphism of
> algebraic spaces.

```lean
theorem isFinite_hom
    (D : NormalizationData B S hS F) (hF : IsAlgebraicSpace B S hS F)
    (hNagata : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsNagataScheme X)) :
    IsFinite B S hS D.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.49, Tag 07U3](https://stacks.math.columbia.edu/tag/07U3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
