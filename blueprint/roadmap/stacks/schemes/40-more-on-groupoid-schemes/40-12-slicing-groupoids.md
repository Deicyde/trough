---
declaration: section
origin: cited
lean: AlgebraicGeometry.SliceSituation, AlgebraicGeometry.SliceSituation.sliceFiberComparison, AlgebraicGeometry.SliceSituation.sliceIdentityPoints, AlgebraicGeometry.stabilizerArrow_isImmersion, AlgebraicGeometry.exists_affine_slice_dim_sub_one, Module.IsMaximalCohenMacaulay.exists_mem_notMem_minimalPrimes_of_ringKrullDim_quotient_lt, Module.IsMaximalCohenMacaulay.exists_mem_isSMulRegular_map_quotient_isMaximalCohenMacaulay, IsCohenMacaulayLocalRing.exists_mem_maximalIdeal_isSMulRegular_map_of_ringKrullDim_lt
statement: formalized
proof: formalized
---

# 40.12 Slicing groupoids

Section 40.12 of the Stacks Project, [Tag 04LV](https://stacks.math.columbia.edu/tag/04LV). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04MY, a situation

[Tag 04MY](https://stacks.math.columbia.edu/tag/04MY) in the Stacks Project.

**`AlgebraicGeometry.SliceSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean#L61). The attribute's comment: “the slice situation”.

> The standing data for the slice situation: a groupoid scheme, a morphism
> to its object scheme, and points lying over one another.

```lean
public structure SliceSituation
```

**`AlgebraicGeometry.SliceSituation.sliceFiberComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean#L259). The attribute's comment: “the fibre comparison”.

> **Stacks Project, Tag 04MY.** The source fibre in the restricted groupoid
> is canonically the base change of `h⁻¹(u)` along
> `Spec(κ(u')) ⟶ Spec(κ(u))`.

```lean
noncomputable def sliceFiberComparison (D : SliceSituation) :
    SliceFiberComparison D
```

**`AlgebraicGeometry.SliceSituation.sliceIdentityPoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean, line 628](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean#L628). The attribute's comment: “the compatible identity points”.

> **Stacks Project, Tag 04MY.** The identity arrows determine compatible
> points of the stabilizer and source fibres before and after restriction; the
> canonical maps of fibres carry each restricted identity point to the original
> one.

```lean
noncomputable def sliceIdentityPoints (D : SliceSituation) :
    SliceIdentityPoints D
```

**`AlgebraicGeometry.stabilizerArrow_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean, line 637](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceSituation.lean#L637). The attribute's comment: “the stabilizer is locally closed”.

> **Stacks Project, Tag 04MY.** The stabilizer of a groupoid scheme is a
> locally closed subscheme of its arrow scheme.

```lean
public theorem stabilizerArrow_isImmersion {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsImmersion (stabilizerArrow G)
```

## Tag 0461, a lemma

[Tag 0461](https://stacks.math.columbia.edu/tag/0461) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_slice_dim_sub_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceDimensionDrop.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SliceDimensionDrop.lean#L543).

> **Stacks Project, Tag 0461.** Let `(U, R, s, t, c)` be a groupoid scheme with `s` and `t`
> Cohen--Macaulay and locally of finite presentation, let `u` be a finite type point of `U`, and
> suppose the source fibre `F_u` has larger dimension at the identity arrow than the stabilizer
> fibre `G_u`. Then there are an affine scheme `U'` and a morphism `g : U' ⟶ U` which is an
> immersion through `u` and locally of finite presentation, such that `h : U' ×_{g,U,t} R ⟶ U`
> is Cohen--Macaulay at the identity arrow and the restricted source fibre has dimension one
> less at the restricted identity arrow.

```lean
public theorem exists_affine_slice_dim_sub_one {S : Scheme.{u}}
    (G : GroupoidScheme S) (u : G.objects.left)
    (hs : ∃ h : ∀ y : G.objects.left, IsLocallyNoetherian (G.source.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.source.left h)
    (_ht : ∃ h : ∀ y : G.objects.left, IsLocallyNoetherian (G.target.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.target.left h)
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left]
    (hu : IsFiniteTypePoint u)
    (hdim : topologicalKrullDim ((stabilizer G).hom.fiber u) <
      topologicalKrullDimAt (G.source.left.fiber u) (sourceFiberIdentity G u))
    :
    ∃ (U' : Over S) (g : U' ⟶ G.objects) (u' : U'.left) (hu' : g.left u' = u),
      let E : SliceSituation := ⟨S, G, U', g, u, u', hu'⟩
      IsAffine U'.left ∧ IsImmersion g.left ∧ LocallyOfFinitePresentation g.left ∧
        (∃ (x : E.arrowSource.left)
          (_ : (pullback.fst E.g E.groupoid.target).left x = u')
          (_ : (pullback.snd E.g E.groupoid.target).left x = E.groupoid.identity.left E.u)
          (hnoeth : ∀ y : E.groupoid.objects.left,
            IsLocallyNoetherian (E.sourceMap.left.fiber y)),
          Scheme.Hom.IsCohenMacaulayAt E.sourceMap.left hnoeth x) ∧
        topologicalKrullDimAt E.restrictedSourceFiber
            E.sliceIdentityPoints.restrictedSourceIdentity + 1 =
          topologicalKrullDimAt (G.source.left.fiber u) (sourceFiberIdentity G u)
```

**`Module.IsMaximalCohenMacaulay.exists_mem_notMem_minimalPrimes_of_ringKrullDim_quotient_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/SliceDimensionDrop.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/SliceDimensionDrop.lean#L189). The attribute's comment: “step 2 of the proof: the minimal-prime avoidance, from equidimensionality of a Cohen--Macaulay local ring (Tag 00NA) and prime avoidance (Tag 00DS). The ideal is not assumed maximal and the source ring is not assumed Noetherian or local”. References: EGA 0 (16.5.5), “special case”.

> **Minimal-prime avoidance in a Cohen–Macaulay local ring.** Let `R` be a Noetherian local
> Cohen–Macaulay ring, `u : A →+* R` a ring map and `I` an ideal of `A` such that the ideal
> `u(I)R` already cuts the dimension, `dim(R/u(I)R) < dim(R)`. Then there is `f ∈ I` whose image
> `u f` lies in no minimal prime of `R`.

```lean
theorem Module.IsMaximalCohenMacaulay.exists_mem_notMem_minimalPrimes_of_ringKrullDim_quotient_lt
    {A R : Type u} [CommRing A] [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hR : Module.IsMaximalCohenMacaulay R R) (u : A →+* R) (I : Ideal A)
    (hlt : ringKrullDim (R ⧸ I.map u) < ringKrullDim R) :
    ∃ f ∈ I, ∀ p ∈ minimalPrimes R, u f ∉ p
```

**`Module.IsMaximalCohenMacaulay.exists_mem_isSMulRegular_map_quotient_isMaximalCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/SliceDimensionDrop.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/SliceDimensionDrop.lean#L239). The attribute's comment: “the commutative-algebra core, conclusions (a), (b) and (c), over an abstract Noetherian local Cohen--Macaulay ring and a ring map into it; no groupoid, scheme or localisation data appears, and the dimension drop is stated additively”. References: EGA 0 (16.5.5), “special case”.

> **Slicing a Cohen–Macaulay local ring, the commutative-algebra core of Stacks 0461.** Let
> `(R, 𝔪_R)` be a Noetherian local Cohen–Macaulay ring, let `u : A →+* R` be a ring map and let `I`
> be an ideal of `A` with `u(I)R ⊆ 𝔪_R` and `dim(R/u(I)R) < dim(R)`. Then there is `f ∈ I` such
> that `dim(R/u(f)R) < dim(R)`, the element `u f` is a nonzerodivisor on `R`, and `R/u(f)R` is a
> Cohen–Macaulay local ring of dimension `dim(R) - 1`.

```lean
theorem Module.IsMaximalCohenMacaulay.exists_mem_isSMulRegular_map_quotient_isMaximalCohenMacaulay
    {A R : Type u} [CommRing A] [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hR : Module.IsMaximalCohenMacaulay R R) (u : A →+* R) (I : Ideal A)
    (hu : I.map u ≤ IsLocalRing.maximalIdeal R)
    (hlt : ringKrullDim (R ⧸ I.map u) < ringKrullDim R) :
    ∃ f ∈ I, ringKrullDim (R ⧸ Ideal.span {u f}) < ringKrullDim R ∧ IsSMulRegular R (u f) ∧
      ∃ _ : IsLocalRing (R ⧸ Ideal.span {u f}),
        Module.IsMaximalCohenMacaulay (R ⧸ Ideal.span {u f}) (R ⧸ Ideal.span {u f}) ∧
          ringKrullDim (R ⧸ Ideal.span {u f}) + 1 = ringKrullDim R
```

**`IsCohenMacaulayLocalRing.exists_mem_maximalIdeal_isSMulRegular_map_of_ringKrullDim_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/SliceDimensionDrop.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/SliceDimensionDrop.lean#L263). The attribute's comment: “the commutative-algebra core along a local homomorphism, at the maximal ideal of the source, in the Tag 00N8 spelling of Cohen--Macaulayness; this is the form the geometric argument consumes”.

> **Slicing along a local homomorphism.** Let `φ : A →+* C` be a local homomorphism of local
> rings with `C` Noetherian and Cohen–Macaulay, and suppose the ideal `φ(𝔪_A)C` already cuts the
> dimension, `dim(C/φ(𝔪_A)C) < dim(C)`. Then some `a ∈ 𝔪_A` has `φ a` a nonzerodivisor on `C` with
> `dim(C/φ(a)C) + 1 = dim(C)`.

```lean
theorem IsCohenMacaulayLocalRing.exists_mem_maximalIdeal_isSMulRegular_map_of_ringKrullDim_lt
    (A C : Type u) [CommRing A] [IsLocalRing A] [CommRing C] [IsLocalRing C]
    [IsNoetherianRing C] (hC : IsCohenMacaulayLocalRing C) (φ : A →+* C) (hφ : IsLocalHom φ)
    (hlt : ringKrullDim (C ⧸ Ideal.map φ (IsLocalRing.maximalIdeal A)) < ringKrullDim C) :
    ∃ a ∈ IsLocalRing.maximalIdeal A, IsSMulRegular C (φ a) ∧
      ringKrullDim (C ⧸ Ideal.span {φ a}) + 1 = ringKrullDim C
```

## Tag 04MZ, a lemma

[Tag 04MZ](https://stacks.math.columbia.edu/tag/04MZ) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_slice_dim_eq_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaximalSlice.lean, line 1276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaximalSlice.lean#L1276).

> **Stacks Project, Tag 04MZ.** Let `(U, R, s, t, c, e, i)` be a groupoid scheme whose source
> and target maps are Cohen--Macaulay and locally of finite presentation, and let `u` be a finite
> type point of `U`. Then there are an affine scheme `U'` and a morphism `g : U' ⟶ U` which is an
> immersion through `u` and locally of finite presentation, such that `h : U' ×_{g,U,t} R ⟶ U`
> and the source and target maps of the restricted groupoid are again Cohen--Macaulay and locally
> of finite presentation, and the restricted source fibre `F'_u` has at the identity arrow exactly
> the dimension of the restricted stabilizer fibre `G'_u`.

```lean
public theorem exists_affine_slice_dim_eq_stabilizer {S : Scheme.{u}}
    (G : GroupoidScheme S) (u : G.objects.left)
    (hu : AlgebraicGeometry.IsFiniteTypePoint u)
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left]
    (hs : ∃ hf : ∀ y : G.objects.left,
      IsLocallyNoetherian (G.source.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.source.left hf)
    (_ht : ∃ hf : ∀ y : G.objects.left,
      IsLocallyNoetherian (G.target.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.target.left hf) :
    ∃ (U' : Over S) (g : U' ⟶ G.objects) (u' : U'.left)
      (hgu : g.left u' = u),
      let D : SliceSituation :=
        { S := S, groupoid := G, U' := U', g := g,
          u := u, u' := u', mapsTo := hgu }
      IsAffine U'.left ∧
      IsImmersion g.left ∧
      LocallyOfFinitePresentation g.left ∧
      LocallyOfFinitePresentation D.sourceMap.left ∧
      (∃ hf : ∀ y : G.objects.left,
        IsLocallyNoetherian (D.sourceMap.left.fiber y),
        Scheme.Hom.IsCohenMacaulay D.sourceMap.left hf) ∧
      LocallyOfFinitePresentation D.restrictedGroupoid.source.left ∧
      (∃ hf : ∀ y : D.restrictedGroupoid.objects.left,
        IsLocallyNoetherian (D.restrictedGroupoid.source.left.fiber y),
        Scheme.Hom.IsCohenMacaulay D.restrictedGroupoid.source.left hf) ∧
      LocallyOfFinitePresentation D.restrictedGroupoid.target.left ∧
      (∃ hf : ∀ y : D.restrictedGroupoid.objects.left,
        IsLocallyNoetherian (D.restrictedGroupoid.target.left.fiber y),
        Scheme.Hom.IsCohenMacaulay D.restrictedGroupoid.target.left hf) ∧
      topologicalKrullDimAt D.restrictedSourceFiber
          D.sliceIdentityPoints.restrictedSourceIdentity =
        topologicalKrullDim D.restrictedStabilizerFiber
```

## Tag 04N0, a lemma

[Tag 04N0](https://stacks.math.columbia.edu/tag/04N0) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_slice_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaxSliceQuasiFinite.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaxSliceQuasiFinite.lean#L121). The attribute's comment: “conclusions (1)-(5) with the fibre products of schemes: `g` an affine immersion locally of finite presentation, `h`, `s'`, `t'` flat, locally finitely presented, quasi-finite”.

> **Stacks Project, Tag 04N0.** A finite type point of a groupoid scheme whose source and
> target maps are Cohen--Macaulay and locally of finite presentation and whose stabilizer group
> scheme is locally quasi-finite has an affine slice `g : U' ⟶ U`, an immersion locally of finite
> presentation, for which `h : U' ×_{g, U, t} R ⟶ U` and the source and target maps of the
> restricted groupoid are flat, locally of finite presentation and locally quasi-finite.

```lean
public theorem exists_affine_slice_locallyQuasiFinite {S : Scheme.{u}}
    (G : GroupoidScheme S) (u : G.objects.left)
    (hu : AlgebraicGeometry.IsFiniteTypePoint u)
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left]
    (hs : ∃ hf : ∀ y : G.objects.left, IsLocallyNoetherian (G.source.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.source.left hf)
    (ht : ∃ hf : ∀ y : G.objects.left, IsLocallyNoetherian (G.target.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.target.left hf)
    [LocallyQuasiFinite (stabilizer G).hom] :
    ∃ (U' : Scheme.{u}) (g : U' ⟶ G.objects.left) (u' : U'),
      g u' = u ∧ IsAffine U' ∧ IsImmersion g ∧ LocallyOfFinitePresentation g ∧
      Flat (pullback.snd g G.target.left ≫ G.source.left) ∧
      LocallyOfFinitePresentation (pullback.snd g G.target.left ≫ G.source.left) ∧
      LocallyQuasiFinite (pullback.snd g G.target.left ≫ G.source.left) ∧
      Flat (GroupoidScheme.restrict G
        (Over.homMk g : Over.mk (g ≫ G.objects.hom) ⟶ G.objects)).groupoid.source.left ∧
      LocallyOfFinitePresentation (GroupoidScheme.restrict G
        (Over.homMk g : Over.mk (g ≫ G.objects.hom) ⟶ G.objects)).groupoid.source.left ∧
      LocallyQuasiFinite (GroupoidScheme.restrict G
        (Over.homMk g : Over.mk (g ≫ G.objects.hom) ⟶ G.objects)).groupoid.source.left ∧
      Flat (GroupoidScheme.restrict G
        (Over.homMk g : Over.mk (g ≫ G.objects.hom) ⟶ G.objects)).groupoid.target.left ∧
      LocallyOfFinitePresentation (GroupoidScheme.restrict G
        (Over.homMk g : Over.mk (g ≫ G.objects.hom) ⟶ G.objects)).groupoid.target.left ∧
      LocallyQuasiFinite (GroupoidScheme.restrict G
        (Over.homMk g : Over.mk (g ≫ G.objects.hom) ⟶ G.objects)).groupoid.target.left
```

**`AlgebraicGeometry.exists_affine_slice_locallyQuasiFinite_of_isFiniteTypePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/QuasiFiniteSlice.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/QuasiFiniteSlice.lean#L308). The attribute's comment: “conclusions (1)-(5): an affine immersion locally of finite presentation whose `h`, `s'` and `t'` are flat, locally of finite presentation and locally quasi-finite”.

> **Stacks Project, Tag 04N0.** Let `(U, R, s, t, c, e, i)` be a groupoid scheme with `s` and
> `t` Cohen-Macaulay and locally of finite presentation, let `u` be a finite type point of `U`,
> and assume the stabilizer group scheme is locally quasi-finite.  Then there are an affine scheme
> `U'` and a morphism `g : U' ⟶ U` such that `g` is an immersion, `u` lies in `U'`, `g` is locally
> of finite presentation, the morphism `h : U' ×_{g, U, t} R ⟶ U` is flat, locally of finite
> presentation and locally quasi-finite, and the structure maps `s', t' : R' ⟶ U'` of the
> restricted groupoid are flat, locally of finite presentation and locally quasi-finite.

```lean
public theorem exists_affine_slice_locallyQuasiFinite_of_isFiniteTypePoint {S : Scheme.{u}}
    (G : GroupoidScheme S) (u : G.objects.left)
    (hu : AlgebraicGeometry.IsFiniteTypePoint u)
    [LocallyOfFinitePresentation G.source.left]
    [LocallyOfFinitePresentation G.target.left]
    (hs : ∃ hf : ∀ y : G.objects.left, IsLocallyNoetherian (G.source.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.source.left hf)
    (ht : ∃ hf : ∀ y : G.objects.left, IsLocallyNoetherian (G.target.left.fiber y),
      Scheme.Hom.IsCohenMacaulay G.target.left hf)
    [LocallyQuasiFinite (stabilizer G).hom] :
    ∃ (U' : Over S) (g : U' ⟶ G.objects) (u' : U'.left) (hgu : g.left u' = u),
      let D : SliceSituation :=
        { S := S, groupoid := G, U' := U', g := g, u := u, u' := u', mapsTo := hgu }
      IsAffine U'.left ∧ IsImmersion g.left ∧ LocallyOfFinitePresentation g.left ∧
        (Flat D.sourceMap.left ∧ LocallyOfFinitePresentation D.sourceMap.left ∧
          LocallyQuasiFinite D.sourceMap.left) ∧
        (Flat D.restrictedGroupoid.source.left ∧
          LocallyOfFinitePresentation D.restrictedGroupoid.source.left ∧
          LocallyQuasiFinite D.restrictedGroupoid.source.left) ∧
        (Flat D.restrictedGroupoid.target.left ∧
          LocallyOfFinitePresentation D.restrictedGroupoid.target.left ∧
          LocallyQuasiFinite D.restrictedGroupoid.target.left)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.12, Tag 04LV](https://stacks.math.columbia.edu/tag/04LV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
