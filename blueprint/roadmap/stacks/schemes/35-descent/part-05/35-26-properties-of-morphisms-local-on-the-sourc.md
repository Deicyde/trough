---
declaration: section
origin: cited
lean: CategoryTheory.MorphismProperty.IsLocalAtSource, AlgebraicGeometry.precomp_of_flat, AlgebraicGeometry.precomp_of_flat_locallyOfFinitePresentation, AlgebraicGeometry.precomp_of_syntomic, AlgebraicGeometry.precomp_of_smooth, AlgebraicGeometry.precomp_of_etale, AlgebraicGeometry.precomp_of_isOpenImmersion, AlgebraicGeometry.largestOpen
statement: formalized
proof: formalized
---

# 35.26 Properties of morphisms local on the source

Section 35.26 of the Stacks Project, [Tag 036F](https://stacks.math.columbia.edu/tag/036F). 5 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 036G, a definition

[Tag 036G](https://stacks.math.columbia.edu/tag/036G) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsLocalAtSource`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsLocalAtSource#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Defs.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Defs.lean#L55) (StacksFrontier). References: SGA 4 IV (8.5.4).

## Tag 04QV, a lemma

[Tag 04QV](https://stacks.math.columbia.edu/tag/04QV) in the Stacks Project.

**`AlgebraicGeometry.precomp_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean#L84). The attribute's comment: “fpqc case”.

> **Stacks Project, Tag 04QV, fpqc case.** A property of morphisms of schemes which is fpqc
> local on the source is preserved by precomposition with a flat morphism.

```lean
theorem precomp_of_flat (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.fpqcPrecoverage]
    {X' X Y : Scheme.{u}} (a : X' ⟶ X) (f : X ⟶ Y)
    (ha : Flat a) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.precomp_of_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean#L104). The attribute's comment: “fppf case”.

> **Stacks Project, Tag 04QV, fppf case.** A property of morphisms of schemes which is fppf
> local on the source is preserved by precomposition with a flat morphism which is locally of
> finite presentation.

```lean
theorem precomp_of_flat_locallyOfFinitePresentation
    (P : MorphismProperty Scheme.{u}) [P.IsLocalAtSource Scheme.fppfPrecoverage]
    {X' X Y : Scheme.{u}} (a : X' ⟶ X) (f : X ⟶ Y)
    (ha : Flat a) (ha' : LocallyOfFinitePresentation a) (hf : P f) :
    P (a ≫ f)
```

**`AlgebraicGeometry.precomp_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean#L115). The attribute's comment: “syntomic case”.

> **Stacks Project, Tag 04QV, syntomic case.** A property of morphisms of schemes which is
> syntomic local on the source is preserved by precomposition with a syntomic morphism.

```lean
theorem precomp_of_syntomic (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource (Scheme.precoverage (@Syntomic.{u}))]
    {X' X Y : Scheme.{u}} (a : X' ⟶ X) (f : X ⟶ Y)
    (ha : Syntomic a) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.precomp_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean#L125). The attribute's comment: “smooth case”.

> **Stacks Project, Tag 04QV, smooth case.** A property of morphisms of schemes which is
> smooth local on the source is preserved by precomposition with a smooth morphism.

```lean
theorem precomp_of_smooth (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource (Scheme.precoverage @Smooth)]
    {X' X Y : Scheme.{u}} (a : X' ⟶ X) (f : X ⟶ Y)
    (ha : Smooth a) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.precomp_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean#L134). The attribute's comment: “étale case”.

> **Stacks Project, Tag 04QV, étale case.** A property of morphisms of schemes which is étale
> local on the source is preserved by precomposition with an étale morphism.

```lean
theorem precomp_of_etale (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.etalePrecoverage]
    {X' X Y : Scheme.{u}} (a : X' ⟶ X) (f : X ⟶ Y)
    (ha : Etale a) (hf : P f) : P (a ≫ f)
```

**`AlgebraicGeometry.precomp_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Precomposition.lean#L144). The attribute's comment: “Zariski case”.

> **Stacks Project, Tag 04QV, Zariski case.** A property of morphisms of schemes which is
> Zariski local on the source is preserved by precomposition with an open immersion.

```lean
theorem precomp_of_isOpenImmersion (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.zariskiPrecoverage]
    {X' X Y : Scheme.{u}} (a : X' ⟶ X) (f : X ⟶ Y)
    (ha : IsOpenImmersion a) (hf : P f) : P (a ≫ f)
```

## Tag 0CEY, a lemma

[Tag 0CEY](https://stacks.math.columbia.edu/tag/0CEY) in the Stacks Project.

**`AlgebraicGeometry.largestOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L80). The attribute's comment: “open locus”.

> **Stacks Project, Tag 0CEY.** The largest open of the source of `f : X ⟶ Y` on which the
> restriction of `f` has the property `P`, defined as the supremum of all opens `U` of `X` with
> `P (U.ι ≫ f)`.
>
> That this open is itself such a locus requires `P` to be local on the source for one of the
> four topologies of the source lemma; see `largestOpen_isGreatest_fppf` and its variants.

```lean
def largestOpen (P : MorphismProperty Scheme.{u}) {X Y : Scheme.{u}}
    (f : X ⟶ Y) : X.Opens
```

**`AlgebraicGeometry.largestOpen_isGreatest_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L164). The attribute's comment: “fppf largest locus”.

> **Stacks Project, Tag 0CEY** for the fppf topology. For `P` local on the source in the fppf
> topology, `largestOpen P f` is a locus for `P` and is the greatest open that is one.

```lean
theorem largestOpen_isGreatest_fppf (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.fppfPrecoverage] {X Y : Scheme.{u}} (f : X ⟶ Y) :
    IsGreatest {U : X.Opens | P (U.ι ≫ f)} (largestOpen P f)
```

**`AlgebraicGeometry.largestOpen_isGreatest_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L173). The attribute's comment: “syntomic largest locus”.

> **Stacks Project, Tag 0CEY** for the syntomic topology. For `P` local on the source in the
> syntomic topology, `largestOpen P f` is a locus for `P` and is the greatest open that is one.

```lean
theorem largestOpen_isGreatest_syntomic (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource (Scheme.precoverage (@Syntomic.{u}))]
    {X Y : Scheme.{u}} (f : X ⟶ Y) :
    IsGreatest {U : X.Opens | P (U.ι ≫ f)} (largestOpen P f)
```

**`AlgebraicGeometry.largestOpen_isGreatest_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L183). The attribute's comment: “smooth largest locus”.

> **Stacks Project, Tag 0CEY** for the smooth topology. For `P` local on the source in the
> smooth topology, `largestOpen P f` is a locus for `P` and is the greatest open that is one.

```lean
theorem largestOpen_isGreatest_smooth (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))]
    {X Y : Scheme.{u}} (f : X ⟶ Y) :
    IsGreatest {U : X.Opens | P (U.ι ≫ f)} (largestOpen P f)
```

**`AlgebraicGeometry.largestOpen_isGreatest_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L193). The attribute's comment: “étale largest locus”.

> **Stacks Project, Tag 0CEY** for the étale topology. For `P` local on the source in the
> étale topology, `largestOpen P f` is a locus for `P` and is the greatest open that is one.

```lean
theorem largestOpen_isGreatest_etale (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.etalePrecoverage] {X Y : Scheme.{u}} (f : X ⟶ Y) :
    IsGreatest {U : X.Opens | P (U.ι ≫ f)} (largestOpen P f)
```

**`AlgebraicGeometry.preimage_largestOpen_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L203). The attribute's comment: “fppf inverse image”.

> **Stacks Project, Tag 0CEY** for the fppf topology: the largest locus of an fppf-local
> property pulls back to the largest locus of the composite along a flat morphism locally of
> finite presentation.

```lean
theorem preimage_largestOpen_fppf (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.fppfPrecoverage]
    {X' X Y : Scheme.{u}} (g : X' ⟶ X) (f : X ⟶ Y)
    [Flat g] [LocallyOfFinitePresentation g] :
    g ⁻¹ᵁ largestOpen P f = largestOpen P (g ≫ f)
```

**`AlgebraicGeometry.preimage_largestOpen_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L228). The attribute's comment: “syntomic inverse image”.

> **Stacks Project, Tag 0CEY** for the syntomic topology: the largest locus of a
> syntomic-local property pulls back to the largest locus of the composite along a syntomic
> morphism.

```lean
theorem preimage_largestOpen_syntomic (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource (Scheme.precoverage (@Syntomic.{u}))]
    {X' X Y : Scheme.{u}} (g : X' ⟶ X) (f : X ⟶ Y) (hg : Syntomic g) :
    g ⁻¹ᵁ largestOpen P f = largestOpen P (g ≫ f)
```

**`AlgebraicGeometry.preimage_largestOpen_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L243). The attribute's comment: “smooth inverse image”.

> **Stacks Project, Tag 0CEY** for the smooth topology: the largest locus of a smooth-local
> property pulls back to the largest locus of the composite along a smooth morphism.

```lean
theorem preimage_largestOpen_smooth (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource (Scheme.precoverage (@Smooth : MorphismProperty Scheme.{u}))]
    {X' X Y : Scheme.{u}} (g : X' ⟶ X) (f : X ⟶ Y) [Smooth g] :
    g ⁻¹ᵁ largestOpen P f = largestOpen P (g ≫ f)
```

**`AlgebraicGeometry.preimage_largestOpen_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/LargestOpen.lean#L255). The attribute's comment: “étale inverse image”.

> **Stacks Project, Tag 0CEY** for the étale topology: the largest locus of an étale-local
> property pulls back to the largest locus of the composite along an étale morphism.

```lean
theorem preimage_largestOpen_etale (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtSource Scheme.etalePrecoverage]
    {X' X Y : Scheme.{u}} (g : X' ⟶ X) (f : X ⟶ Y) [Etale g] :
    g ⁻¹ᵁ largestOpen P f = largestOpen P (g ≫ f)
```

## Tag 036H, a lemma

[Tag 036H](https://stacks.math.columbia.edu/tag/036H) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtSource_fpqc_of_affine_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/AffineCriteria.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/AffineCriteria.lean#L113). The attribute's comment: “fpqc case”.

> A property of morphisms of schemes which is Zariski local on the source and on the target,
> which is preserved by precomposition with flat morphisms, and which descends along surjective
> flat morphisms of affine schemes, is fpqc local on the source.

```lean
theorem isLocalAtSource_fpqc_of_affine_descent (P : MorphismProperty Scheme.{u})
    [P.RespectsLeft (@Flat.{u})] [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P]
    (hAffine : ∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
      (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → Flat g → P (g ≫ f) → P f) :
    P.IsLocalAtSource Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.isLocalAtSource_fppf_of_affine_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/AffineCriteria.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/AffineCriteria.lean#L138). The attribute's comment: “fppf case”.

> A property of morphisms of schemes which is Zariski local on the source and on the target,
> which is preserved by precomposition with flat morphisms locally of finite presentation, and
> which descends along surjective flat morphisms locally of finite presentation of affine schemes,
> is fppf local on the source.

```lean
theorem isLocalAtSource_fppf_of_affine_descent (P : MorphismProperty Scheme.{u})
    [P.RespectsLeft (@Flat ⊓ @LocallyOfFinitePresentation : MorphismProperty Scheme.{u})]
    [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P]
    (hAffine : ∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
      (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → Flat g → LocallyOfFinitePresentation g →
        P (g ≫ f) → P f) :
    P.IsLocalAtSource Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.isLocalAtSource_smooth_of_affine_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/AffineCriteria.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSourceTopologies/AffineCriteria.lean#L163). The attribute's comment: “smooth case”.

> A property of morphisms of schemes which is Zariski local on the source and on the target,
> which is preserved by precomposition with smooth morphisms, and which descends along surjective
> smooth morphisms of affine schemes, is smooth local on the source.

```lean
theorem isLocalAtSource_smooth_of_affine_descent (P : MorphismProperty Scheme.{u})
    [P.RespectsLeft (@Smooth.{u})] [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P]
    (hAffine : ∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
      (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → Smooth g → P (g ≫ f) → P f) :
    P.IsLocalAtSource (Scheme.precoverage (@Smooth.{u}))
```

**`AlgebraicGeometry.isLocalAtSource_etale_of_affine_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleSourceLocality.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleSourceLocality.lean#L131). The attribute's comment: “étale case”.

> **Stacks Project, Tag 036H, étale case.** A property of morphisms of schemes which is
> Zariski local on the source and on the target, which is preserved by precomposition with étale
> morphisms, and which descends along surjective étale morphisms of affine schemes, is étale
> local on the source.

```lean
theorem isLocalAtSource_etale_of_affine_descent (P : MorphismProperty Scheme.{u})
    [P.RespectsLeft (@Etale.{u})] [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P]
    (hAffine : ∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
      (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → Etale g → P (g ≫ f) → P f) :
    P.IsLocalAtSource Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isLocalAtSource_syntomic_of_affine_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/SyntomicScheme.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/SyntomicScheme.lean#L170). The attribute's comment: “syntomic case”.

> **Stacks Project, Tag 036H, syntomic case.** A property of morphisms of schemes which is
> Zariski local on the source and on the target, which is preserved by precomposition with
> syntomic morphisms, and which descends along surjective syntomic morphisms of affine schemes,
> is syntomic local on the source.

```lean
theorem isLocalAtSource_syntomic_of_affine_descent (P : MorphismProperty Scheme.{u})
    [P.RespectsLeft (@Syntomic.{u})] [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P]
    (hAffine : ∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
      (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → Syntomic g → P (g ≫ f) → P f) :
    P.IsLocalAtSource (Scheme.precoverage (@Syntomic.{u}))
```

## Tag 036I, a remark

[Tag 036I](https://stacks.math.columbia.edu/tag/036I) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtSource_of_standard_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/SourceDescent.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/SourceDescent.lean#L248).

> **Stacks Project, Tag 036I.** In condition (4) of Tag 036H one may assume that the morphism
> is a (surjective) *standard smooth* morphism when `τ = smooth`, a (surjective) *standard
> syntomic* morphism when `τ = syntomic`, and a (surjective) *standard étale* morphism when
> `τ = étale`.
>
> The three conjuncts are the statements of the smooth, syntomic and étale cases of Tag 036H with
> condition (4) so strengthened; they are
> `AlgebraicGeometry.isLocalAtSource_smooth_of_standard_descent`,
> `AlgebraicGeometry.isLocalAtSource_syntomic_of_standard_descent` and
> `AlgebraicGeometry.isLocalAtSource_etale_of_standard_descent`.

```lean
theorem isLocalAtSource_of_standard_descent :
    (∀ (P : MorphismProperty Scheme.{u}) [P.RespectsLeft (@Smooth.{u})]
        [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P],
        (∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
          (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → IsStandardSmooth g → P (g ≫ f) → P f) →
        P.IsLocalAtSource (Scheme.precoverage (@Smooth.{u}))) ∧
      (∀ (P : MorphismProperty Scheme.{u}) [P.RespectsLeft (@Syntomic.{u})]
        [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P],
        (∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
          (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → IsStandardSyntomic g → P (g ≫ f) → P f) →
        P.IsLocalAtSource (Scheme.precoverage (@Syntomic.{u}))) ∧
      ∀ (P : MorphismProperty Scheme.{u}) [P.RespectsLeft (@Etale.{u})]
        [IsZariskiLocalAtSource P] [IsZariskiLocalAtTarget P],
        (∀ {X' X Y : Scheme.{u}} [IsAffine X'] [IsAffine X] [IsAffine Y]
          (g : X' ⟶ X) (f : X ⟶ Y), Surjective g → IsStandardEtale g → P (g ≫ f) → P f) →
        P.IsLocalAtSource Scheme.etalePrecoverage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.26, Tag 036F](https://stacks.math.columbia.edu/tag/036F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
