---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.eq_of_specializes_of_pointsMap_eq_of_hasFiniteChartFibers, AlgebraicGeometry.Space.exists_specialization_lift_of_isDecentSpace, AlgebraicGeometry.Space.t0Space_points_of_hasFiniteChartFibers, AlgebraicGeometry.Space.t0Space_points_of_isDecentSpace, AlgebraicGeometry.Space.stacksSober_points_of_isDecentSpace, AlgebraicGeometry.Space.topologicalKrullDimAt_points_eq_dimensionAtPoint_of_isDecentSpace, AlgebraicGeometry.Space.topologicalKrullDim_points_eq_dimension_of_isDecentSpace, AlgebraicGeometry.Space.localRingDimension_le_of_isLocallyQuasiFinite
statement: formalized
proof: formalized
---

# 68.12 Points on decent spaces

Section 68.12 of the Stacks Project, [Tag 03IG](https://stacks.math.columbia.edu/tag/03IG). 8 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03K5, a lemma

[Tag 03K5](https://stacks.math.columbia.edu/tag/03K5) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_specializes_of_pointsMap_eq_of_hasFiniteChartFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Specializations.lean#L406).

> **Stacks 03K5.** Let `X` be an algebraic space over `S` every point of which satisfies
> condition (2) of Stacks 03JS — in particular, a decent one — and let `h_U ⟶ X` be an étale
> chart of `X` by a scheme. Two points of the chart with the same image in `X`, one a
> specialization of the other, are equal.

```lean
theorem eq_of_specializes_of_pointsMap_eq_of_hasFiniteChartFibers
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdecent : HasFiniteChartFibersAtEveryPoint B S hS X)
    (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
    (hφ : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf φ)
    (u u' : points B S hS (yoneda.obj U))
    (huu' : pointsMap B S hS (yoneda.obj U) φ u = pointsMap B S hS (yoneda.obj U) φ u')
    (hs : u' ⤳ u) : u = u'
```

## Tag 03IL, a lemma

[Tag 03IL](https://stacks.math.columbia.edu/tag/03IL) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_specialization_lift_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionFunction.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDimensionFunction.lean#L183).

> **Stacks 03IL.** Let `X` be a decent algebraic space over a scheme `S` and let `x, x'` be
> points of `|X|` with `x' ⤳ x`, that is, `x` a specialization of `x'`. Then for every étale
> `φ : h_U ⟶ X` with `U` an object of the site and every point `p` of `|U|` above `x` there is a
> point `p' ⤳ p` of `|U|` above `x'`.
>
> This is the source's "combine 03JX and 03K2": decency is condition (4) of Stacks 03JV at
> every point, which gives condition (1) at `x'` by, in this namespace,
> `HasQuasiCompactMonomorphicFieldRepresentative.hasFiniteFibresOnEveryAffineEtaleChart`, and
> that is the hypothesis of
> `AlgebraicGeometry.Space.exists_specialization_lift_of_finite_etale_fibers`.

```lean
theorem exists_specialization_lift_of_isDecentSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hXdec : IsDecentSpace B S hS X) (x x' : points B S hS X) (hs : x' ⤳ x)
    (U : BigFppfOver B S hS) (φ : yoneda.obj U ⟶ X)
    (hφ : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) φ)
    (p : points B S hS (yoneda.obj U)) (hp : pointsMap B S hS (yoneda.obj U) φ p = x) :
    ∃ p' : points B S hS (yoneda.obj U),
      p' ⤳ p ∧ pointsMap B S hS (yoneda.obj U) φ p' = x'
```

## Tag 03K3, a lemma

[Tag 03K3](https://stacks.math.columbia.edu/tag/03K3) in the Stacks Project.

**`AlgebraicGeometry.Space.t0Space_points_of_hasFiniteChartFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Points.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Points.lean#L59).

> **Stacks 03K3.** The point space of an algebraic space over `S` all of whose points have
> finite fibres in every étale chart by an affine scheme — in particular, of a decent algebraic
> space — is Kolmogorov.

```lean
theorem t0Space_points_of_hasFiniteChartFibers
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hdecent : HasFiniteChartFibersAtEveryPoint B S hS X) :
    T0Space (points B S hS X)
```

**`AlgebraicGeometry.Space.t0Space_points_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Sober.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Sober.lean#L107).

> **Stacks 03K3.** The point space of a decent algebraic space over `S` is Kolmogorov: decency
> is condition (4) of Stacks 03JV at every point, which gives condition `(α)` of Stacks 03JX, and
> Stacks 03K3 concludes.
>
> Kolmogorov is `T0Space`; `StacksFrontier.Topology.Sober.Defs` identifies Definition 004X's
> Kolmogorov condition with `T0Space` in `kolmogorov_iff`.

```lean
theorem t0Space_points_of_isDecentSpace (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) : T0Space (points B S hS X)
```

## Tag 03K6, a proposition

[Tag 03K6](https://stacks.math.columbia.edu/tag/03K6) in the Stacks Project.

**`AlgebraicGeometry.Space.stacksSober_points_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Sober.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Sober.lean#L155).

> **Stacks 03K6.** The point space of a decent algebraic space over `S` is sober in the sense
> of Stacks 004X: it is Kolmogorov, and every irreducible closed subset of it has a unique
> generic point.

```lean
theorem stacksSober_points_of_isDecentSpace (hX : IsAlgebraicSpace B S hS X)
    (hdec : IsDecentSpace B S hS X) : StacksSober (points B S hS X)
```

## Tag 0A4J, a lemma

[Tag 0A4J](https://stacks.math.columbia.edu/tag/0A4J) in the Stacks Project.

**`AlgebraicGeometry.Space.topologicalKrullDimAt_points_eq_dimensionAtPoint_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean#L96). The attribute's comment: “part (1)”.

> **Stacks 0A4J, part (1)**, and the fourth clause of **Stacks 0AC9**. At every point of a
> decent algebraic space over `S` the local Krull dimension of the point space agrees with the
> dimension of the space at that point, as defined by étale scheme charts.
>
> This equality is what makes conditions (1) and (4) of Stacks 0AC9 — vanishing of the two
> dimensions at the point — equivalent for a decent space.

```lean
theorem topologicalKrullDimAt_points_eq_dimensionAtPoint_of_isDecentSpace
    (hX : IsAlgebraicSpace B S hS X) (hdec : IsDecentSpace B S hS X) (x : points B S hS X) :
    topologicalKrullDimAt (points B S hS X) x = dimensionAtPoint B S hS X hX x
```

**`AlgebraicGeometry.Space.topologicalKrullDim_points_eq_dimension_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean#L133). The attribute's comment: “part (2)”.

> **Stacks 0A4J, part (2).** The Krull dimension of the point space of a decent algebraic
> space over `S` agrees with the dimension of the space, as defined by étale scheme charts.

```lean
theorem topologicalKrullDim_points_eq_dimension_of_isDecentSpace
    (hX : IsAlgebraicSpace B S hS X) (hdec : IsDecentSpace B S hS X) :
    topologicalKrullDim (points B S hS X) = dimension B S hS X hX
```

## Tag 0ABW, a lemma

[Tag 0ABW](https://stacks.math.columbia.edu/tag/0ABW) in the Stacks Project.

**`AlgebraicGeometry.Space.localRingDimension_le_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/GenericPointsAndDimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/GenericPointsAndDimension.lean#L142).

> A locally quasi-finite morphism of algebraic spaces over `S` does not increase the dimension
> of the local ring: for a point `x` of the source, the dimension of the local ring there is at
> most the dimension of the local ring of the target at the image of `x`.

```lean
theorem localRingDimension_le_of_isLocallyQuasiFinite
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyQuasiFinite B S hS f)
    (x : points B S hS X) :
    localRingDimension B S hS x ≤
      localRingDimension B S hS (pointsMap B S hS X f x)
```

## Tag 0ED0, a lemma

[Tag 0ED0](https://stacks.math.columbia.edu/tag/0ED0) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_le_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionQuasiFinite.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionQuasiFinite.lean#L45).

> **Stacks 0ED0.** The dimension of the source of a locally quasi-finite morphism of
> algebraic spaces over `S` is at most the dimension of its target.

```lean
theorem dimension_le_of_isLocallyQuasiFinite
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyQuasiFinite B S hS f) :
    dimension B S hS X hX ≤ dimension B S hS Y hY
```

## Tag 03IK, a lemma

[Tag 03IK](https://stacks.math.columbia.edu/tag/03IK) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_isDecentSpace_of_etale_fieldSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldAtlas.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldAtlas.lean#L76).

> **Stacks Project, Tag 03IK.** Let `S` be a scheme, let `k` be a field and let `F` be an
> algebraic space over `S` admitting a surjective étale morphism from the spectrum of `k`. If `F`
> is decent then `F` is represented by the spectrum of a field `k'` over `S`, with `k` a finite
> separable extension of `k'`, and under that identification the given morphism is the one induced
> by the extension `k/k'`.

```lean
theorem exists_iso_yoneda_spec_of_isDecentSpace_of_etale_fieldSpec
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hdecent : IsDecentSpace B S hS F)
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k))) (b : Spec (.of k) ⟶ S)
    (f : yoneda.obj (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS)) ⟶ F)
    (hsurj : IsSurjective B S hS f)
    (hetale : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k' k) (_ : Module.Finite k' k)
      (_ : Algebra.IsSeparable k' k) (hk' : B.Contains (Spec (.of k')))
      (b' : Spec (.of k') ⟶ S),
      ∃ (hbase : Spec.map (CommRingCat.ofHom (algebraMap k' k)) ≫ b' = b)
        (e : F ≅ yoneda.obj (Over.mk (⟨b'⟩ : B.obj hk' ⟶ B.obj hS))),
        f ≫ e.hom = yoneda.map (Over.homMk
          (ObjectProperty.homMk (Spec.map (CommRingCat.ofHom (algebraMap k' k))) :
            B.obj hk ⟶ B.obj hk') (by
              apply ObjectProperty.hom_ext
              simpa using hbase))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.12, Tag 03IG](https://stacks.math.columbia.edu/tag/03IG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
