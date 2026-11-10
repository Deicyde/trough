---
declaration: section
origin: cited
lean: RingHom.eqLocus, AlgebraicGeometry.GroupoidScheme.det_lmul_targetMap_mem_invariantRing, AlgebraicGeometry.norm_targetMap_mem_invariantRing, AlgebraicGeometry.GroupoidScheme.exists_disjoint_invariant_rank_decomposition, AlgebraicGeometry.GroupoidScheme.isIntegral_invariantRing, AlgebraicGeometry.isIntegral_over_invariantRing, AlgebraicGeometry.GroupoidScheme.canonicalMapToInvariantFunctions_bijective_of_flat, AlgebraicGeometry.GroupoidScheme.exists_affineInvariantBaseChange
statement: formalized
proof: formalized
---

# 39.23 Finite flat groupoids, affine case

Section 39.23 of the Stacks Project, [Tag 03BE](https://stacks.math.columbia.edu/tag/03BE). 9 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03BF, an equation

[Tag 03BF](https://stacks.math.columbia.edu/tag/03BF) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.eqLocus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.eqLocus#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch39.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch39.lean#L16) (StacksFrontier). References: EGA IV (5.6.11); SGA 3 V (4.1).

## Tag 03BH, a lemma

[Tag 03BH](https://stacks.math.columbia.edu/tag/03BH) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.det_lmul_targetMap_mem_invariantRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantNorm.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantNorm.lean#L158).

> **Stacks Project, Tag 03BH.** For a groupoid scheme with affine object scheme and finite
> locally free source map, the norm along the source map of a function pulled back along the
> target map is an invariant function.

```lean
theorem det_lmul_targetMap_mem_invariantRing {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsFiniteLocallyFree G.source.left] (f : Γ(G.objects.left, ⊤)) :
    letI := (sourceMap G).toAlgebra
    ∃ (hfinite : Module.Finite Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤))
      (hprojective : Module.Projective Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤)),
      letI := hfinite
      letI := hprojective
      ProjectiveDeterminant.det
          (Algebra.lmul Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤) (targetMap G f)) ∈
        invariantRing G
```

**`AlgebraicGeometry.norm_targetMap_mem_invariantRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineNorm.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineNorm.lean#L183).

> For a groupoid scheme with affine object scheme and finite locally free source map, the
> arrow ring is a finite projective module over the object ring along the source map, and the
> norm along the source map of a function pulled back along the target map is an invariant
> function.

```lean
theorem norm_targetMap_mem_invariantRing {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsFiniteLocallyFree G.source.left]
    (f : Γ(G.objects.left, ⊤)) :
    letI := (sourceMap G).toAlgebra
    ∃ (hfinite : Module.Finite Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤))
      (hprojective : Module.Projective Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤)),
      letI := hfinite
      letI := hprojective
      ProjectiveDeterminant.det
        (Algebra.lmul Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤) (targetMap G f)) ∈
          invariantRing G
```

## Tag 03BI, a lemma

[Tag 03BI](https://stacks.math.columbia.edu/tag/03BI) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_disjoint_invariant_rank_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/RankDecomposition.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/RankDecomposition.lean#L389).

> **Stacks Project, Tag 03BI.** A groupoid scheme whose source map is finite locally free
> decomposes by the rank into invariant opens. On each restricted groupoid, both the source and
> the target map are finite locally free of that rank, and the rank-zero piece is empty.

```lean
theorem exists_disjoint_invariant_rank_decomposition {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsFiniteLocallyFree G.source.left] :
    ∃ U : ℕ → G.objects.left.Opens,
      U 0 = ⊥ ∧
      (∀ r, IsClosed (U r : Set G.objects.left)) ∧
      Pairwise (Disjoint on U) ∧
      (⨆ r, U r) = ⊤ ∧
      ∀ r, IsInvariantOpen G (U r) ∧
        let g : Over.mk ((U r).ι ≫ G.objects.hom) ⟶ G.objects := Over.homMk (U r).ι
        let H := GroupoidScheme.restrict G g
        IsFiniteLocallyFreeOfRank H.groupoid.source.left r ∧
          IsFiniteLocallyFreeOfRank H.groupoid.target.left r
```

## Tag 03BJ, a lemma

[Tag 03BJ](https://stacks.math.columbia.edu/tag/03BJ) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.isIntegral_invariantRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/IntegralInvariants.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/IntegralInvariants.lean#L216). References: SGA 3 V (4.1), “more general”.

> For an affine groupoid scheme with finite locally free source and target, the ring of global
> functions on the object scheme is integral over its subring of invariant functions.

```lean
theorem isIntegral_invariantRing {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left] :
    (Subring.subtype (invariantRing G)).IsIntegral
```

**`AlgebraicGeometry.isIntegral_over_invariantRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineIntegral.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineIntegral.lean#L337). References: SGA 3 V (4.1), “more general”.

> For an affine groupoid scheme with finite locally free source and target, the ring of global
> functions on the object scheme is integral over its subring of invariant functions.

```lean
theorem isIntegral_over_invariantRing {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left] :
    (invariantRing G).subtype.IsIntegral
```

## Tag 03BK, a lemma

[Tag 03BK](https://stacks.math.columbia.edu/tag/03BK) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.canonicalMapToInvariantFunctions_bijective_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/FlatInvariants.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/FlatInvariants.lean#L133). The attribute's comment: “flat\_invariants”.

> For a flat extension of the invariant ring of an affine groupoid scheme, the canonical map
> from the new base ring to the invariant functions of the base-changed groupoid is bijective.

```lean
theorem canonicalMapToInvariantFunctions_bijective_of_flat {S : Scheme.{u}}
    {G : GroupoidScheme S} {C' : Type u} [CommRing C'] [Algebra (invariantRing G) C']
    [Module.Flat (invariantRing G) C'] (G' : AffineInvariantBaseChange G C') :
    Function.Bijective G'.canonicalMapToInvariantFunctions
```

**`AlgebraicGeometry.GroupoidScheme.exists_affineInvariantBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantBaseChange.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantBaseChange.lean#L571). The attribute's comment: “base\_changed\_groupoid”.

> **Stacks Project, Tag 03BK.** Extending the coordinate rings of an affine groupoid scheme
> from its invariant ring produces the indicated groupoid scheme, with finite locally free source
> and target.

```lean
theorem exists_affineInvariantBaseChange {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    (C' : Type u) [CommRing C'] [Algebra (invariantRing G) C'] :
    Nonempty (AffineInvariantBaseChange G C')
```

**`AlgebraicGeometry.GroupoidScheme.isNilpotent_of_mem_ker_canonicalMapToInvariantFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/NilpotentKernel.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/NilpotentKernel.lean#L48). The attribute's comment: “nilpotent\_kernel”.

> Each element killed by the canonical map from the base ring to the invariant functions of the
> base-changed groupoid is nilpotent.

```lean
theorem isNilpotent_of_mem_ker_canonicalMapToInvariantFunctions {S : Scheme.{u}}
    (G : GroupoidScheme S) [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left] {C' : Type u}
    [CommRing C'] [Algebra (invariantRing G) C'] (G' : AffineInvariantBaseChange G C') (f : C')
    (hf : f ∈ RingHom.ker G'.canonicalMapToInvariantFunctions) : IsNilpotent f
```

**`AlgebraicGeometry.GroupoidScheme.exists_polynomial_map_eq_pow_X_sub_C`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/PolynomialDescent.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/PolynomialDescent.lean#L479). The attribute's comment: “polynomial\_descent”.

> A positive power of the linear polynomial of an invariant function after base change comes
> from the new base ring.

```lean
theorem exists_polynomial_map_eq_pow_X_sub_C {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    {C' : Type u} [CommRing C'] [Algebra (invariantRing G) C']
    (G' : AffineInvariantBaseChange G C') (f : G'.invariantFunctions) :
    ∃ (n : ℕ) (_hn : 0 < n) (P : Polynomial C'),
      P.map G'.canonicalMapToInvariantFunctions = (Polynomial.X - Polynomial.C f) ^ n
```

**`AlgebraicGeometry.canonicalMapToInvariantFunctions_bijective_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineInvariantFlat.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineInvariantFlat.lean#L204). The attribute's comment: “part (3), flat extensions of the invariant ring”.

> For a flat extension of the invariant ring, the canonical map from the extension ring to the
> invariant functions of the base-changed groupoid scheme is bijective.

```lean
theorem canonicalMapToInvariantFunctions_bijective_of_flat
    {S : Scheme.{u}} {G : GroupoidScheme S}
    {C' : Type u} [CommRing C'] [Algebra (invariantRing G) C']
    [Module.Flat (invariantRing G) C']
    (G' : AffineInvariantBaseChange G C') :
    Function.Bijective G'.canonicalMapToInvariantFunctions
```

## Tag 03BL, a lemma

[Tag 03BL](https://stacks.math.columbia.edu/tag/03BL) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.surjective_objectsToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean#L172). The attribute's comment: “part (1), surjectivity”. References: SGA 1 V (1.1), “more general”.

> **Stacks Project, Tag 03BL.** The morphism from the object scheme to the spectrum of the
> invariant functions is surjective on underlying topological points.

```lean
theorem surjective_objectsToInvariantSpectrum {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left] :
    Function.Surjective (objectsToInvariantSpectrum G).base
```

**`AlgebraicGeometry.GroupoidScheme.surjective_comp_objectsToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean#L193). The attribute's comment: “part (2), surjectivity”. References: SGA 1 V (1.1), “more general”.

> **Stacks Project, Tag 03BL.** Over an algebraically closed field, every point of the
> spectrum of the invariant functions lifts to the object scheme.

```lean
theorem surjective_comp_objectsToInvariantSpectrum {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    (k : Type u) [Field k] [IsAlgClosed k] :
    Function.Surjective
      fun x : Spec (.of k) ⟶ G.objects.left ↦ x ≫ objectsToInvariantSpectrum G
```

**`AlgebraicGeometry.GroupoidScheme.comp_objectsToInvariantSpectrum_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean#L217). The attribute's comment: “part (2), fibres”.

> **Stacks Project, Tag 03BL.** Over an algebraically closed field, two points of the object
> scheme have the same image in the spectrum of the invariant functions exactly when they are
> the target and the source of a common arrow.

```lean
theorem comp_objectsToInvariantSpectrum_eq_iff {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    (k : Type u) [Field k] [IsAlgClosed k] (u₀ u₁ : Spec (.of k) ⟶ G.objects.left) :
    u₀ ≫ objectsToInvariantSpectrum G = u₁ ≫ objectsToInvariantSpectrum G ↔
      ∃ r : Spec (.of k) ⟶ G.arrows.left,
        r ≫ G.target.left = u₀ ∧ r ≫ G.source.left = u₁
```

**`AlgebraicGeometry.GroupoidScheme.base_objectsToInvariantSpectrum_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotientPoints.lean#L348). The attribute's comment: “part (1), fibres”.

> **Stacks Project, Tag 03BL.** Two topological points of the object scheme have the same
> image in the spectrum of the invariant functions exactly when they are the target and the
> source of a common arrow.

```lean
theorem base_objectsToInvariantSpectrum_eq_iff {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    (u₀ u₁ : G.objects.left) :
    (objectsToInvariantSpectrum G).base u₀ = (objectsToInvariantSpectrum G).base u₁ ↔
      ∃ r : G.arrows.left,
        G.target.left.base r = u₀ ∧ G.source.left.base r = u₁
```

## Tag 0DT9, a lemma

[Tag 0DT9](https://stacks.math.columbia.edu/tag/0DT9) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.etale_invariantRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/EtaleInvariantRingMapAssembly.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/EtaleInvariantRingMapAssembly.lean#L384). The attribute's comment: “the FIRST conclusion: the map C -> C' from the R-invariant functions on U to the R'-invariant functions on U' is etale. Together with isPullback\_mapObjects, which is the second conclusion, this is the whole statement of the tag”.

> **The first conclusion of [Stacks Project, Tag 0DT9]: the map `C ⟶ C'` from the `R`-invariant
> functions on `U` to the `R'`-invariant functions on `U'` is étale.**
>
> The four hypotheses of the source are all present: that `U`, `R`, `U'`, `R'` are affine is the four
> `IsAffine` instances; that `s`, `t`, `s'`, `t'` are finite locally free is the four
> `IsFiniteLocallyFree` instances; the three cartesian squares are `hsource`, `htarget` and `hstab`;
> and that `f : U' → U` is étale is `[Etale F.mapObjects.left]`.
>
> Étaleness is checked point by point with the source-cover criterion
> `AlgebraicGeometry.etale_of_forall_exists_etale_comp`, whose covering family is supplied by
> `AlgebraicGeometry.GroupoidScheme.exists_etale_comp_invariantRingMap`. No finite presentation
> hypothesis on `Spec C' ⟶ Spec C` is needed, which matters because local finite presentation is
> itself part of the conclusion.

```lean
theorem etale_invariantRingMap
    (hsource : IsPullback F.mapArrows.left G'.source.left G.source.left F.mapObjects.left)
    (htarget : IsPullback F.mapArrows.left G'.target.left G.target.left F.mapObjects.left)
    (hstab : IsPullback (stabilizerMap F).left (stabilizer G').hom (stabilizer G).hom
      F.mapObjects.left) :
    (invariantRingMap F).Etale
```

**`AlgebraicGeometry.GroupoidScheme.isPullback_mapObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/EtaleInvariantRingMapAssembly.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/EtaleInvariantRingMapAssembly.lean#L404). The attribute's comment: “the SECOND conclusion: U' is the fibre product of Spec C' and U over Spec C. Unconditional: the premise that C -> C' is etale is supplied by etale\_invariantRingMap, the tag's first conclusion”.

> **The second conclusion of [Stacks Project, Tag 0DT9]: `U' = Spec C' ×_{Spec C} U`.**
>
> This is `AlgebraicGeometry.GroupoidScheme.isPullback_mapObjects_of_etale_invariantRingMap` with its
> hypothesis `hC` discharged by
> `AlgebraicGeometry.GroupoidScheme.etale_invariantRingMap`, the first conclusion of the tag. The
> cartesian `s'/s` square is not needed for the implication from the first conclusion to the second,
> but it is a hypothesis of the first, so it appears here too.

```lean
theorem isPullback_mapObjects
    (hsource : IsPullback F.mapArrows.left G'.source.left G.source.left F.mapObjects.left)
    (htarget : IsPullback F.mapArrows.left G'.target.left G.target.left F.mapObjects.left)
    (hstab : IsPullback (stabilizerMap F).left (stabilizer G').hom (stabilizer G).hom
      F.mapObjects.left) :
    IsPullback F.mapObjects.left (objectsToInvariantSpectrum G')
      (objectsToInvariantSpectrum G) (Spec.map (CommRingCat.ofHom (invariantRingMap F)))
```

## Tag 03C8, a lemma

[Tag 03C8](https://stacks.math.columbia.edu/tag/03C8) in the Stacks Project.

**`AlgebraicGeometry.basis_over_invariantRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineBasis.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineBasis.lean#L280). The attribute's comment: “the basis over invariant functions”.

> A basis of the arrow ring over the object ring pulled back along the source descends to a
> basis of the object ring over the invariant ring.

```lean
theorem basis_over_invariantRing {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    {I : Type v} (x : I → Γ(G.objects.left, ⊤))
    (h : letI := (sourceMap G).toAlgebra
      ∃ b : Module.Basis I Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤),
        ∀ i, b i = targetMap G (x i)) :
    ∃ b : Module.Basis I (invariantRing G) Γ(G.objects.left, ⊤), ∀ i, b i = x i
```

**`AlgebraicGeometry.tensorProduct_equiv_arrowRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineBasis.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineBasis.lean#L314). The attribute's comment: “the tensor-product description”.

> Under the same basis hypothesis, the canonical map from the tensor square of the object
> ring over its invariant ring to the arrow ring is an isomorphism.

```lean
theorem tensorProduct_equiv_arrowRing {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    {I : Type v} (x : I → Γ(G.objects.left, ⊤))
    (h : letI := (sourceMap G).toAlgebra
      ∃ b : Module.Basis I Γ(G.objects.left, ⊤) Γ(G.arrows.left, ⊤),
        ∀ i, b i = targetMap G (x i)) :
    let A := Γ(G.objects.left, ⊤)
    let B := Γ(G.arrows.left, ⊤)
    let C := invariantRing G
    ∃ e : RingEquiv (A ⊗[C] A) B,
      ∀ a a', e (a ⊗ₜ[C] a') = sourceMap G a * targetMap G a'
```

## Tag 03BM, a proposition

[Tag 03BM](https://stacks.math.columbia.edu/tag/03BM) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.isFiniteLocallyFree_objectsToInvariantSpectrum`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean, line 784](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean#L784). The attribute's comment: “finite locally free quotient map”. References: SGA 3 V (4.1), “affine case, (iv)”.

> The morphism from the object scheme to the spectrum of the invariant functions is finite
> locally free.

```lean
instance isFiniteLocallyFree_objectsToInvariantSpectrum {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left] [IsFiniteLocallyFree G.source.left]
    [IsFiniteLocallyFree G.target.left] [IsEquivalenceRelation G.target G.source] :
    IsFiniteLocallyFree (objectsToInvariantSpectrum G)
```

**`AlgebraicGeometry.GroupoidScheme.isPullback_objectsToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean, line 804](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean#L804). The attribute's comment: “the relation is the kernel pair”.

> The source and target maps exhibit the arrow scheme as the kernel pair of the morphism to
> the spectrum of the invariant functions.

```lean
theorem isPullback_objectsToInvariantSpectrum {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left] [IsFiniteLocallyFree G.source.left]
    [IsFiniteLocallyFree G.target.left] [IsEquivalenceRelation G.target G.source] :
    IsPullback G.target.left G.source.left (objectsToInvariantSpectrum G)
      (objectsToInvariantSpectrum G)
```

**`AlgebraicGeometry.GroupoidScheme.invariantSpectrumBaseMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean#L814). The attribute's comment: “descent of the quotient over the base”.

> The structure morphism of the object scheme descends along the morphism to the spectrum of
> the invariant functions.

```lean
def invariantSpectrumBaseMap {S : Scheme.{u}} (G : GroupoidScheme S) [IsAffine G.objects.left]
    [IsAffine G.arrows.left] [IsFiniteLocallyFree G.source.left]
    [IsFiniteLocallyFree G.target.left] [IsEquivalenceRelation G.target G.source] :
    { f : Spec (.of (invariantRing G)) ⟶ S //
      objectsToInvariantSpectrum G ≫ f = G.objects.hom }
```

**`AlgebraicGeometry.GroupoidScheme.isIso_quotientSheafToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean, line 899](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/AffineQuotient.lean#L899). The attribute's comment: “representation of the fppf quotient sheaf”. References: SGA 3 V (4.1), “affine case, (iv) fppf”.

> The spectrum of the invariant functions represents the fppf quotient sheaf of the
> relation, and the representing isomorphism is compatible with the canonical projection from the
> object scheme.

```lean
theorem isIso_quotientSheafToInvariantSpectrum {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left] [IsFiniteLocallyFree G.source.left]
    [IsFiniteLocallyFree G.target.left] [IsEquivalenceRelation G.target G.source]
    (B : BigFppfSite.{u}) (hS : B.Contains S)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)] :
    ∃ hM : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
        (points (Over.post B.inclusion) (invariantSpectrumOver G)),
      IsIso (quotientSheafToPoints (BigFppfOver.topology B S hS) (Over.post B.inclusion)
        (prod.lift G.target G.source : PreRelation G.arrows G.objects)
        (toInvariantSpectrumOver G)
        (target_comp_toInvariantSpectrumOver G) hM)
```

**`AlgebraicGeometry.GroupoidScheme.isField_invariantRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/FieldObjectDivision.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatQuotient/FieldObjectDivision.lean#L155). The attribute's comment: “the ring of invariants of a groupoid on the spectrum of a field is a field”.

> **Stacks Project, Tag 03BM.** The ring of invariant functions of an affine groupoid scheme
> with finite locally free source and target is a field as soon as the ring of functions on the
> object scheme is one.  The ring of functions on the object scheme is integral over the invariant
> ring by **Stacks 03BJ**, and the invariant ring is a subring, so the extension is injective; an
> injective integral extension of a field comes from a field.

```lean
theorem isField_invariantRing {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    (h : IsField Γ(G.objects.left, ⊤)) : IsField (invariantRing G)
```

**`AlgebraicGeometry.objectsToInvariantSpectrum_isFiniteLocallyFree`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean#L529). The attribute's comment: “finite locally free quotient map”.

> The canonical map to the spectrum of invariant functions is finite locally free.

```lean
public instance objectsToInvariantSpectrum_isFiniteLocallyFree {S : Scheme.{u}}
    (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source] :
    IsFiniteLocallyFree (objectsToInvariantSpectrum G)
```

**`AlgebraicGeometry.isPullback_objectsToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean#L553). The attribute's comment: “the relation is the kernel pair”.

> The source and target maps exhibit the arrow scheme as the kernel pair of the quotient.

```lean
public theorem isPullback_objectsToInvariantSpectrum {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source] :
    IsPullback G.target.left G.source.left (objectsToInvariantSpectrum G)
      (objectsToInvariantSpectrum G)
```

**`AlgebraicGeometry.quotientBaseMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean#L564). The attribute's comment: “descent of the quotient over the base”.

> The map from the affine invariant quotient to the base scheme, specified by descent of
> the original structure map.

```lean
public def quotientBaseMap {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source] :
    { f : Spec (.of (invariantRing G)) ⟶ S //
        objectsToInvariantSpectrum G ≫ f = G.objects.hom }
```

**`AlgebraicGeometry.quotientSheaf_isRepresented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean, line 642](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/AffineQuotient/FppfQuotient.lean#L642). The attribute's comment: “representation of the fppf quotient sheaf”.

> The spectrum of invariant functions represents the fppf quotient sheaf, with the
> representing isomorphism compatible with the canonical projection from the objects.

```lean
public theorem quotientSheaf_isRepresented {S : Scheme.{u}} (G : GroupoidScheme S)
    [IsAffine G.objects.left] [IsAffine G.arrows.left]
    [IsFiniteLocallyFree G.source.left] [IsFiniteLocallyFree G.target.left]
    [IsEquivalenceRelation G.target G.source]
    (B : AlgebraicGeometry.BigFppfSite.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B S hS) (Type u)] :
    let F : AlgebraicGeometry.BigFppfOver B S hS ⥤ Over S := Over.post B.inclusion
    let J := AlgebraicGeometry.BigFppfOver.topology B S hS
    let j : Stacks.Groupoids.PreRelation G.arrows G.objects := prod.lift G.target G.source
    ∃ hM : Presheaf.IsSheaf J (Stacks.Groupoids.points F (quotientOver G)),
      ∃ q : Stacks.Groupoids.quotientSheaf J F j ⟶
          (⟨Stacks.Groupoids.points F (quotientOver G), hM⟩ : Sheaf J (Type u)),
        IsIso q ∧
          Stacks.Groupoids.toQuotientSheaf J F j ≫ q.hom =
            F.op.whiskerLeft (yoneda.map (quotientProjection G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.23, Tag 03BE](https://stacks.math.columbia.edu/tag/03BE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
