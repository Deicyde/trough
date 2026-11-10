---
declaration: section
origin: cited
lean: Stacks.Groupoids.finiteStratification, Stacks.Groupoids.finiteStratification_zero, Stacks.Groupoids.finiteStratification_mono, Stacks.Groupoids.finiteStratification_exhaustive, Stacks.Groupoids.finiteStratification_invariant, Stacks.Groupoids.finiteStratification_rank, AlgebraicGeometry.exists_invariant_thickening_finiteLocallyFree_restriction, AlgebraicGeometry.finitePresentation_layerThickeningInclusion
statement: formalized
proof: formalized
---

# 40.14 Finite groupoids

Section 40.14 of the Stacks Project, [Tag 0AB8](https://stacks.math.columbia.edu/tag/0AB8). 10 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AB9, a lemma

[Tag 0AB9](https://stacks.math.columbia.edu/tag/0AB9) in the Stacks Project.

**`Stacks.Groupoids.finiteStratification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean#L51). The attribute's comment: “the Fitting stratification”.

> The canonical Fitting stratification associated to source of a groupoid scheme.

```lean
noncomputable def finiteStratification {S : Scheme.{u}} (G : GroupoidScheme S) (n : ℕ) :
    G.objects.left.IdealSheafData
```

**`Stacks.Groupoids.finiteStratification_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean#L57). The attribute's comment: “the first closed subscheme”.

> The identity arrows force the zeroth Fitting closed subscheme to be all objects.

```lean
theorem finiteStratification_zero {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left] :
    finiteStratification G 0 = ⊥
```

**`Stacks.Groupoids.finiteStratification_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean#L65). The attribute's comment: “decreasing closed subschemes”.

> The Fitting closed subschemes form a decreasing sequence.

```lean
theorem finiteStratification_mono {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left] (n : ℕ) :
    finiteStratification G n ≤ finiteStratification G (n + 1)
```

**`Stacks.Groupoids.finiteStratification_exhaustive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteStratification.lean#L72). The attribute's comment: “empty intersection”.

> No point lies in all Fitting closed subschemes.

```lean
theorem finiteStratification_exhaustive {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left] (x : G.objects.left) :
    ∃ n, x ∉ (finiteStratification G n).support
```

**`Stacks.Groupoids.finiteStratification_invariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteStratificationInvariant.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteStratificationInvariant.lean#L195). The attribute's comment: “invariance”.

> Every member of the Fitting stratification is invariant under the groupoid.
>
> The second projection of the scheme of composable pairs is simultaneously the base change of
> source along target and the base change of source along source, by the two cartesian lower
> squares of the diagram of Stacks Tag 04LF. So both inverse images of a member of the
> stratification are the Fitting ideal sheaf of the pushforward of the structure sheaf along that
> single projection.

```lean
theorem finiteStratification_invariant {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left] (n : ℕ) :
    IsInvariantClosedSubscheme G (finiteStratification G n)
```

**`Stacks.Groupoids.finiteStratification_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteStratificationRankSheaf.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteStratificationRankSheaf.lean#L81). The attribute's comment: “rank of each stratum”.

> **Stacks Project, Tag 0AB9: the rank of each stratum.** For a groupoid scheme with finite
> source and target there is an open subscheme `W` of the closed subscheme cut out by the
> `(r-1)`st Fitting ideal sheaf of `s_* 𝒪_R` whose image in the object scheme is the difference of
> the supports of the `(r-1)`st and `r`th Fitting ideal sheaves, and the base change of source to
> `W` is finite locally free of rank `r`.
>
> The open subscheme is `Stacks.Groupoids.exists_opens_finiteStratification_stratum`. Finite local
> freeness is checked affine-locally by
> `Stacks.Groupoids.module_isFiniteLocallyFreeOfRank_finiteStratification_stratum` and assembled
> into the sheaf-level statement by
> `Stacks.Modules.isFiniteLocallyFreeOfRank_of_module_affineOpens` and
> `Stacks.Modules.isFiniteLocallyFreeOfRank_iff_localGenerators`.

```lean
theorem finiteStratification_rank {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left] (r : ℕ) (hr : 0 < r) :
    ∃ W : (finiteStratification G (r - 1)).subscheme.Opens,
      Set.range (W.ι ≫ (finiteStratification G (r - 1)).subschemeι) =
          ((finiteStratification G (r - 1)).support : Set G.objects.left) \
            ((finiteStratification G r).support : Set G.objects.left) ∧
        IsFiniteLocallyFreeOfRank
          (pullback.snd G.source.left
            (W.ι ≫ (finiteStratification G (r - 1)).subschemeι)) r
```

## Tag 0ABA, a lemma

[Tag 0ABA](https://stacks.math.columbia.edu/tag/0ABA) in the Stacks Project.

**`AlgebraicGeometry.exists_invariant_thickening_finiteLocallyFree_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/FiniteGroupoidThickening.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/FiniteGroupoidThickening.lean#L1081).

> **Stacks Project, Tag 0ABA.** A groupoid scheme with finite source and target has an
> invariant open subscheme `W` carrying an invariant closed thickening `W'` such that the source
> and target maps of the restriction of the groupoid to `W'` are finite locally free, and such
> that the saturation of the closure of `W` is the whole object scheme.

```lean
public theorem exists_invariant_thickening_finiteLocallyFree_restriction {S : Scheme.{u}}
    (G : GroupoidScheme S) [IsFinite G.source.left] [IsFinite G.target.left] :
    ∃ (W : G.objects.left.Opens) (W' : Scheme.{u}) (i : W' ⟶ W.toScheme)
      (hmono : Mono (i ≫ W.ι)),
      letI : Mono (i ≫ W.ι) := hmono
      IsInvariantOpen G W ∧
      IsInvariantMonomorphism G (i ≫ W.ι) ∧
      (G.target.left.base ''
        (G.source.left.base ⁻¹' closure (W : Set G.objects.left)) = Set.univ) ∧
      IsThickening i ∧
      (let g : Over.mk (i ≫ W.ι ≫ G.objects.hom) ⟶ G.objects := Over.homMk (i ≫ W.ι)
       IsFiniteLocallyFree (restrictionSource G g).left ∧
       IsFiniteLocallyFree (restrictionTarget G g).left)
```

## Tag 0ABB, a lemma

[Tag 0ABB](https://stacks.math.columbia.edu/tag/0ABB) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_layerThickeningInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/FinitePresentationThickening.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/FinitePresentationThickening.lean#L58). The attribute's comment: “finite_presentation”.

> **Stacks Project, Tag 0ABB (1).** For a groupoid scheme with finite source and target whose
> source map is of finite presentation, the inclusion of the invariant closed thickening into the
> invariant open is of finite presentation: on each stage it is the base change of one member of
> the Fitting stratification along the inclusion of the open chosen there.

```lean
theorem finitePresentation_layerThickeningInclusion {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left]
    (hs : FinitePresentation G.source.left) :
    FinitePresentation (layerThickeningInclusion G)
```

**`AlgebraicGeometry.mem_layerUnionOpen_of_orbit_subset_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/FinitePresentationThickening.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/FinitePresentationThickening.lean#L119). The attribute's comment: “generic_orbit_mem”.

> **Stacks Project, Tag 0ABB (2).** For a groupoid scheme with finite source and target whose
> source map is of finite presentation, a point whose orbit consists of generic points of
> irreducible components of the object scheme lies in the invariant open constructed for the
> groupoid.

```lean
theorem mem_layerUnionOpen_of_orbit_subset_genericPoints {S : Scheme.{u}}
    (G : GroupoidScheme S) [IsFinite G.source.left] [IsFinite G.target.left]
    (hs : FinitePresentation G.source.left) (x : G.objects.left)
    (hx : ∀ y : G.objects.left,
      (∃ r : G.arrows.left, G.source.left r = x ∧ G.target.left r = y) →
        y ∈ genericPoints G.objects.left) :
    x ∈ layerUnionOpen G
```

## Tag 0ABC, a lemma

[Tag 0ABC](https://stacks.math.columbia.edu/tag/0ABC) in the Stacks Project.

**`AlgebraicGeometry.exists_invariant_affine_open_with_finiteLocallyFree_thickening'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/GenericOrbitInvariantAffine.lean, line 1302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/GenericOrbitInvariantAffine.lean#L1302).

> **[Stacks, Tag 0ABC].** Let `G` be a groupoid scheme whose source and target are finite and
> of finite presentation, with quasi-separated object scheme, and let `x : ι → U` be finitely many
> points whose orbits consist of generic points of irreducible components of the object scheme.
> Then there is an invariant affine open `V` of the object scheme and an ideal sheaf `Z` on it such
> that the closed subscheme `V(Z)` is an affine invariant thickening of finite presentation inside
> `V` containing the images of the `x i`, over which the source and target of the restricted
> groupoid are finite locally free.
>
> Nothing is assumed beyond the hypotheses of the tag. This is
> `AlgebraicGeometry.exists_invariant_affine_open_with_finiteLocallyFree_thickening`, which carries
> [Stacks, Tag 06AD] as the hypothesis `H06AD`, with that hypothesis discharged by
> `Stacks.Thickenings.forall_isAffine_of_isThickening`, the library's 06AD.

```lean
theorem exists_invariant_affine_open_with_finiteLocallyFree_thickening'
    {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left]
    (hs : FinitePresentation G.source.left)
    (ht : FinitePresentation G.target.left)
    [QuasiSeparatedSpace G.objects.left]
    {ι : Type v} [Finite ι] (x : ι → G.objects.left)
    (hx : ∀ i y, (∃ r : G.arrows.left,
      G.source.left r = x i ∧ G.target.left r = y) →
        ∃ Z ∈ irreducibleComponents G.objects.left, IsGenericPoint y Z) :
    ∃ (V : G.objects.left.Opens) (Z : V.toScheme.IdealSheafData),
      (∀ i, x i ∈ Set.range (Z.subschemeι ≫ V.ι)) ∧
      Stacks.Groupoids.IsInvariantOpen G V ∧
      IsAffineOpen V ∧
      Stacks.Groupoids.IsInvariantMonomorphism G (Z.subschemeι ≫ V.ι) ∧
      IsAffine Z.subscheme ∧
      IsThickening Z.subschemeι ∧
      FinitePresentation Z.subschemeι ∧
      (let U' : Over S := Over.mk (Z.subschemeι ≫ V.ι ≫ G.objects.hom)
       let g : U' ⟶ G.objects := Over.homMk (Z.subschemeι ≫ V.ι) (by rfl)
       Stacks.Morphisms.IsFiniteLocallyFree
          (AlgebraicGeometry.GroupoidScheme.restrict G g).groupoid.source.left ∧
       Stacks.Morphisms.IsFiniteLocallyFree
          (AlgebraicGeometry.GroupoidScheme.restrict G g).groupoid.target.left)
```

## Tag 0ABD, a lemma

[Tag 0ABD](https://stacks.math.columbia.edu/tag/0ABD) in the Stacks Project.

**`AlgebraicGeometry.exists_invariant_affine_finiteLocallyFree_thickening_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/GenericOrbitInvariantAffine.lean, line 1392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/GenericOrbitInvariantAffine.lean#L1392).

> **[Stacks, Tag 0ABD].** Let `G` be a groupoid scheme whose source and target are finite, with
> locally Noetherian object scheme, and let `x : ι → U` be finitely many points whose orbits consist
> of generic points of irreducible components of the object scheme. Then there is an invariant
> affine open `V` of the object scheme and an ideal sheaf `Z` on it such that the closed subscheme
> `V(Z)` is an affine invariant thickening inside `V` containing the images of the `x i`, over which
> the source and target of the restricted groupoid are finite locally free.
>
> Nothing is assumed beyond the hypotheses: the affineness of `V` comes from [Stacks, Tag 01YQ]
> through
> `AlgebraicGeometry.exists_isAffineOpen_preimage_eq_of_isThickening_of_isLocallyNoetherian`.

```lean
theorem exists_invariant_affine_finiteLocallyFree_thickening_of_isLocallyNoetherian
    {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left]
    [IsLocallyNoetherian G.objects.left]
    {ι : Type v} [Finite ι] (x : ι → G.objects.left)
    (hx : ∀ i y, (∃ r : G.arrows.left,
      G.source.left r = x i ∧ G.target.left r = y) →
        ∃ Z ∈ irreducibleComponents G.objects.left, IsGenericPoint y Z) :
    ∃ (V : G.objects.left.Opens) (Z : V.toScheme.IdealSheafData),
      (∀ i, x i ∈ Set.range (Z.subschemeι ≫ V.ι)) ∧
      Stacks.Groupoids.IsInvariantOpen G V ∧
      IsAffineOpen V ∧
      Stacks.Groupoids.IsInvariantMonomorphism G (Z.subschemeι ≫ V.ι) ∧
      IsAffine Z.subscheme ∧
      IsThickening Z.subschemeι ∧
      (let U' : Over S := Over.mk (Z.subschemeι ≫ V.ι ≫ G.objects.hom)
       let g : U' ⟶ G.objects := Over.homMk (Z.subschemeι ≫ V.ι) (by rfl)
       Stacks.Morphisms.IsFiniteLocallyFree
          (AlgebraicGeometry.GroupoidScheme.restrict G g).groupoid.source.left ∧
       Stacks.Morphisms.IsFiniteLocallyFree
          (AlgebraicGeometry.GroupoidScheme.restrict G g).groupoid.target.left)
```

## Tag 0ABE, a lemma

[Tag 0ABE](https://stacks.math.columbia.edu/tag/0ABE) in the Stacks Project.

**`AlgebraicGeometry.exists_invariant_affine_open_of_restriction_integral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantAffineOpenDescent.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantAffineOpenDescent.lean#L186).

> **[Stacks, Tag 0ABE]**.  Let `G` be a groupoid scheme over `S` whose source and target maps
> are integral, let `g : U' ⟶ G.objects` be integral with image meeting every orbit of `G`, and
> let `R` be the restriction of `G` along `g`.  A point of the object scheme of `R` contained in
> an invariant affine open has its image in `G.objects` contained in an invariant affine open.

```lean
theorem exists_invariant_affine_open_of_restriction_integral
    (G : Stacks.Groupoids.GroupoidScheme S) [IsIntegralHom G.source.left]
    [IsIntegralHom G.target.left] {U' : Over S} {g : U' ⟶ G.objects} [IsIntegralHom g.left]
    (R : GroupoidScheme.Restriction G g)
    (horbit : ∀ u : G.objects.left, ∃ u' : U'.left, ∃ r : G.arrows.left,
      G.source.left r = u ∧ G.target.left r = g.left u')
    (u' : R.groupoid.objects.left) (W' : R.groupoid.objects.left.Opens)
    (hW'inv : Stacks.Groupoids.IsInvariantOpen R.groupoid W') (hW'aff : IsAffineOpen W')
    (hu' : u' ∈ W') :
    ∃ W : G.objects.left.Opens, Stacks.Groupoids.IsInvariantOpen G W ∧ IsAffineOpen W ∧
      R.hom.mapObjects.left u' ∈ W
```

## Tag 0ABF, a lemma

[Tag 0ABF](https://stacks.math.columbia.edu/tag/0ABF) in the Stacks Project.

**`AlgebraicGeometry.exists_mem_ideal_invariant_affine_preimage_basicOpen'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantPrincipalOpenGenericOrbits.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantPrincipalOpenGenericOrbits.lean#L850).

> **[Stacks, Tag 0ABF].** Let `G` be a groupoid scheme whose source and target are finite and
> of finite presentation, let `x : ι → U` be finitely many points whose orbits consist of generic
> points of irreducible components of the object scheme, let `j : U ⟶ Spec A` be an immersion, and
> let `I` be an ideal of `A` whose vanishing locus misses the image of `j` and whose union with
> that image is closed. Then some `h ∈ I` has `j ⁻¹ D(h)` an invariant affine open of the object
> scheme containing all the `x i`.
>
> Nothing is assumed beyond the hypotheses of the tag. This is
> `AlgebraicGeometry.exists_mem_ideal_invariant_affine_preimage_basicOpen`, which carries
> [Stacks, Tag 06AD] as the hypothesis `H06AD`, with that hypothesis discharged by
> `Stacks.Thickenings.forall_isAffine_of_isThickening`, which is Tag 06AD.

```lean
theorem exists_mem_ideal_invariant_affine_preimage_basicOpen'
    {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left]
    (hs : FinitePresentation G.source.left)
    (ht : FinitePresentation G.target.left)
    {ι : Type v} [Finite ι] (x : ι → G.objects.left)
    (hx : ∀ i y, (∃ r : G.arrows.left,
      G.source.left r = x i ∧ G.target.left r = y) →
        ∃ Z ∈ irreducibleComponents G.objects.left, IsGenericPoint y Z)
    {A : Type u} [CommRing A]
    (j : G.objects.left ⟶ Spec (CommRingCat.of A)) [IsImmersion j]
    (I : Ideal A)
    (hdisj : Disjoint (Set.range (j : G.objects.left → Spec (CommRingCat.of A)))
      (PrimeSpectrum.zeroLocus (I : Set A)))
    (hclosed : IsClosed (PrimeSpectrum.zeroLocus (I : Set A) ∪
      Set.range (j : G.objects.left → Spec (CommRingCat.of A)))) :
    ∃ h : A, h ∈ I ∧
      (let W := j ⁻¹ᵁ PrimeSpectrum.basicOpen h
       Stacks.Groupoids.IsInvariantOpen G W ∧ IsAffineOpen W ∧ ∀ i, x i ∈ W)
```

## Tag 0ABG, a lemma

[Tag 0ABG](https://stacks.math.columbia.edu/tag/0ABG) in the Stacks Project.

**`AlgebraicGeometry.not_specialization_of_exists_arrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/FiniteGroupoid.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/FiniteGroupoid.lean#L63).

> Distinct points joined by an arrow of a groupoid scheme with finite source and target cannot
> be related by specialization.

```lean
theorem not_specialization_of_exists_arrow {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFinite G.source.left] [IsFinite G.target.left]
    {u u' : G.objects.left} (hne : u ≠ u')
    (horbit : ∃ r : G.arrows.left, G.source.left r = u ∧ G.target.left r = u') :
    ¬ (u ⤳ u')
```

## Tag 0ABH, a lemma

[Tag 0ABH](https://stacks.math.columbia.edu/tag/0ABH) in the Stacks Project.

**`AlgebraicGeometry.isAffine_of_isImmersion_of_isAffineOpen_preimage_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/AffineQuasiCompactImmersion.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/AffineQuasiCompactImmersion.lean#L46).

> **Stacks Project, Tag 0ABH.** A quasi-compact immersion into an affine scheme whose
> restriction over a standard open is affine and the remainder of whose image is closed has an
> affine source.

```lean
theorem isAffine_of_isImmersion_of_isAffineOpen_preimage_basicOpen {A : Type u} [CommRing A]
    {V : Scheme.{u}} (j : V ⟶ Spec (CommRingCat.of A)) [IsImmersion j] [QuasiCompact j]
    (f : A) (hD : IsAffineOpen (j ⁻¹ᵁ PrimeSpectrum.basicOpen f))
    (hclosed : IsClosed (Set.range (j : V → Spec (CommRingCat.of A)) ∩
      ((Spec (CommRingCat.of A)).basicOpen
        ((Scheme.ΓSpecIso (CommRingCat.of A)).inv f) :
          Set (Spec (CommRingCat.of A)))ᶜ)) : IsAffine V
```

## Tag 0ABI, a lemma

[Tag 0ABI](https://stacks.math.columbia.edu/tag/0ABI) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_isAffineOpen_mem_of_krullDimLE_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantAffineOpenDimensionOne.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantAffineOpenDimensionOne.lean#L125).

> Let `G` be a groupoid scheme whose source and target maps are finite and whose object scheme
> is separated and locally Noetherian, and let `u` be a point of the object scheme such that every
> point of the orbit of `u` has a stalk of Krull dimension at most one. Then `u` lies in an
> invariant affine open of the object scheme.

```lean
theorem exists_isInvariantOpen_isAffineOpen_mem_of_krullDimLE_one
    (G : GroupoidScheme S) [IsFinite G.source.left] [IsFinite G.target.left]
    [G.objects.left.IsSeparated] [IsLocallyNoetherian G.objects.left]
    (u : G.objects.left)
    (hdim : ∀ u' : G.objects.left,
      (∃ r : G.arrows.left, G.source.left.base r = u ∧ G.target.left.base r = u') →
        Ring.KrullDimLE 1 (G.objects.left.presheaf.stalk u')) :
    ∃ W : G.objects.left.Opens, IsInvariantOpen G W ∧ IsAffineOpen W ∧ u ∈ W
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.14, Tag 0AB8](https://stacks.math.columbia.edu/tag/0AB8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
