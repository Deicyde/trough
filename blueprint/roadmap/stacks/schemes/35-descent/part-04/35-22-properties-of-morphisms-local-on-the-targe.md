---
declaration: section
origin: cited
lean: CategoryTheory.MorphismProperty.IsLocalAtTarget, AlgebraicGeometry.pullbackSnd_of_flat, AlgebraicGeometry.pullbackSnd_of_flat_locallyOfFinitePresentation, AlgebraicGeometry.pullbackSnd_of_syntomic, AlgebraicGeometry.pullbackSnd_of_smooth, AlgebraicGeometry.pullbackSnd_of_etale, AlgebraicGeometry.pullbackSnd_of_isOpenImmersion, AlgebraicGeometry.largestTargetOpen
statement: formalized
proof: formalized
---

# 35.22 Properties of morphisms local on the target

Section 35.22 of the Stacks Project, [Tag 02KN](https://stacks.math.columbia.edu/tag/02KN). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02KO, a definition

[Tag 02KO](https://stacks.math.columbia.edu/tag/02KO) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsLocalAtTarget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsLocalAtTarget#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnSource/Defs.lean#L51) (StacksFrontier). References: SGA 3 IV (4.6.3), “(e\_T)”; SGA 3 VIB (2.0), “b)”.

## Tag 04QU, a lemma

[Tag 04QU](https://stacks.math.columbia.edu/tag/04QU) in the Stacks Project.

**`AlgebraicGeometry.pullbackSnd_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean#L60). The attribute's comment: “fpqc case”.

> A property of morphisms of schemes which is fpqc local on the target is preserved by flat base
> change.

```lean
theorem pullbackSnd_of_flat
    (P : MorphismProperty Scheme.{u}) [P.IsLocalAtTarget Scheme.fpqcPrecoverage]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f) (hg : Flat g) : P (pullback.snd f g)
```

**`AlgebraicGeometry.pullbackSnd_of_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean#L86). The attribute's comment: “fppf case”.

> A property of morphisms of schemes which is fppf local on the target is preserved by base
> change along a flat morphism which is locally of finite presentation.

```lean
theorem pullbackSnd_of_flat_locallyOfFinitePresentation
    (P : MorphismProperty Scheme.{u}) [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f) (hg : Flat g) (hlfp : LocallyOfFinitePresentation g) :
    P (pullback.snd f g)
```

**`AlgebraicGeometry.pullbackSnd_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean#L98). The attribute's comment: “syntomic case”.

> A property of morphisms of schemes which is syntomic local on the target is preserved by
> syntomic base change.

```lean
theorem pullbackSnd_of_syntomic (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtTarget (Scheme.precoverage (@Syntomic.{u}))]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f) (hg : Syntomic g) : P (pullback.snd f g)
```

**`AlgebraicGeometry.pullbackSnd_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean#L109). The attribute's comment: “smooth case”.

> A property of morphisms of schemes which is smooth local on the target is preserved by smooth
> base change.

```lean
theorem pullbackSnd_of_smooth (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtTarget (Scheme.precoverage (@Smooth))]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f) (hg : Smooth g) : P (pullback.snd f g)
```

**`AlgebraicGeometry.pullbackSnd_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean#L119). The attribute's comment: “étale case”.

> A property of morphisms of schemes which is étale local on the target is preserved by étale
> base change.

```lean
theorem pullbackSnd_of_etale (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtTarget Scheme.etalePrecoverage]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f) (hg : Etale g) : P (pullback.snd f g)
```

**`AlgebraicGeometry.pullbackSnd_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/BaseChange.lean#L129). The attribute's comment: “Zariski case”.

> A property of morphisms of schemes which is Zariski local on the target is preserved by base
> change along an open immersion.

```lean
theorem pullbackSnd_of_isOpenImmersion (P : MorphismProperty Scheme.{u})
    [P.IsLocalAtTarget Scheme.zariskiPrecoverage]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : P f) (hg : IsOpenImmersion g) : P (pullback.snd f g)
```

## Tag 06QP, a lemma

[Tag 06QP](https://stacks.math.columbia.edu/tag/06QP) in the Stacks Project.

**`AlgebraicGeometry.largestTargetOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean#L212). The attribute's comment: “largest open”.

> The supremum of the opens of the target over which `f` has the property `P`.

```lean
noncomputable def largestTargetOpen (P : MorphismProperty Scheme.{u}) {X Y : Scheme.{u}}
    (f : X ⟶ Y) : Y.Opens
```

**`AlgebraicGeometry.property_largestTargetOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean#L218). The attribute's comment: “existence”. References: SGA 3 VIB (2.1), “partial”.

> **Stacks Project, Tag 06QP.** A target-local property holds over the largest open.

```lean
lemma property_largestTargetOpen (P Q : MorphismProperty Scheme.{u})
    (hQ : IsDescentMorphismClass Q) [P.IsLocalAtTarget (Scheme.precoverage Q)]
    {X Y : Scheme.{u}} (f : X ⟶ Y) : P (f ∣_ largestTargetOpen P f)
```

**`AlgebraicGeometry.le_largestTargetOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean#L244). The attribute's comment: “maximality”.

> **Stacks Project, Tag 06QP.** Every open over which the property holds lies in the
> largest open.

```lean
lemma le_largestTargetOpen (P : MorphismProperty Scheme.{u}) {X Y : Scheme.{u}} (f : X ⟶ Y)
    (U : Y.Opens) (hU : P (f ∣_ U)) : U ≤ largestTargetOpen P f
```

**`AlgebraicGeometry.range_le_largestTargetOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean#L250). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 06QP.** The image of a morphism of the chosen class whose base
> change has the property lies in the largest open.

```lean
lemma range_le_largestTargetOpen (P Q : MorphismProperty Scheme.{u})
    (hQ : IsDescentMorphismClass Q) [P.IsLocalAtTarget (Scheme.precoverage Q)]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y) (hg : Q g)
    (hfg : P (pullback.snd f g)) : Set.range g ⊆ (largestTargetOpen P f).1
```

**`AlgebraicGeometry.largestTargetOpen_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean#L280). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 06QP.** The largest open commutes with base change along a
> morphism of the chosen class.

```lean
lemma largestTargetOpen_baseChange (P Q : MorphismProperty Scheme.{u})
    (hQ : IsDescentMorphismClass Q) [P.IsLocalAtTarget (Scheme.precoverage Q)]
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y) (hg : Q g) :
    largestTargetOpen P (pullback.snd f g) = g ⁻¹ᵁ largestTargetOpen P f
```

**`AlgebraicGeometry.largestTargetOpen_covering`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/LocalProperties/LargestTargetOpen.lean#L298). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 06QP.** The largest opens of the members of a covering family are
> the inverse images of the largest open downstairs.

```lean
lemma largestTargetOpen_covering (P Q : MorphismProperty Scheme.{u})
    (hQ : IsDescentMorphismClass Q) [P.IsLocalAtTarget (Scheme.precoverage Q)]
    {X Y : Scheme.{u}} {I : Type v} (f : X ⟶ Y) (Y' : I → Scheme.{u})
    (g : ∀ i, Y' i ⟶ Y) (hg : Presieve.ofArrows Y' g ∈ Scheme.precoverage Q Y) (i : I) :
    largestTargetOpen P (pullback.snd f (g i)) = (g i) ⁻¹ᵁ largestTargetOpen P f
```

## Tag 02KP, a lemma

[Tag 02KP](https://stacks.math.columbia.edu/tag/02KP) in the Stacks Project.

**`Stacks.Descent.isLocalAtTarget_fpqcPrecoverage_of_affineDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L298). The attribute's comment: “the fpqc case”.

> **Stacks Project, Tag 02KP** for the fpqc topology. Let `P` be a property of morphisms of
> schemes. Assume that
>
> 1. `P` is stable under base change along flat morphisms;
> 2. `P` is Zariski local on the base;
> 3. for every surjective flat morphism `g : S' ⟶ S` of affine schemes and every morphism of
>    schemes `f : X ⟶ S`, the property `P` holds for `f` if it holds for the base change
>    `S' ×_S X ⟶ S'`.
>
> Then `P` is fpqc local on the base.

```lean
theorem isLocalAtTarget_fpqcPrecoverage_of_affineDescent
    (hdesc : ∀ {S S' T : Scheme.{u}} [IsAffine S] [IsAffine S'] (g : S' ⟶ S), Surjective g →
      Flat g → ∀ f : T ⟶ S, P (pullback.snd f g) → P f) :
    P.IsLocalAtTarget Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.isLocalAtTarget_precoverage_of_affineDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/MorphismPropertyTopology/CoveringTopologyLocalAtTarget.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/MorphismPropertyTopology/CoveringTopologyLocalAtTarget.lean#L109). The attribute's comment: “the fppf, étale, smooth and syntomic cases”.

> **Stacks Project, Tag 02KP** for the fppf, étale, smooth and syntomic topologies. Let `P` be
> a property of morphisms of schemes and let `τ` be one of fppf, étale, smooth and syntomic.
> Assume that
>
> 1. `P` is preserved by base change along the morphisms belonging to `τ`, that is along flat
>    morphisms locally of finite presentation, syntomic, smooth or étale morphisms depending on
>    whether `τ` is fppf, syntomic, smooth or étale;
> 2. `P` is Zariski local on the base;
> 3. for every surjective morphism `g : S' ⟶ S` of affine schemes belonging to `τ` and every
>    morphism of schemes `f : X ⟶ S`, the property `P` holds for `f` if it holds for the base
>    change `S' ×_S X ⟶ S'`.
>
> Then `P` is `τ` local on the base.

```lean
theorem isLocalAtTarget_precoverage_of_affineDescent (P : MorphismProperty Scheme.{u})
    (τ : CoveringTopology) (hτ : τ ≠ .zariski)
    [P.IsStableUnderBaseChangeAgainst (coveringMorphismProperty τ)]
    [IsZariskiLocalAtTarget P]
    (hdesc : ∀ {S S' X : Scheme.{u}} [IsAffine S] [IsAffine S'] (g : S' ⟶ S), Surjective g →
      coveringMorphismProperty τ g → ∀ f : X ⟶ S, P (pullback.snd f g) → P f) :
    P.IsLocalAtTarget (Scheme.precoverage (coveringMorphismProperty τ))
```

## Tag 034G, a remark

[Tag 034G](https://stacks.math.columbia.edu/tag/034G) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtTarget_etale_of_standard_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/Descent.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/Descent.lean#L253). The attribute's comment: “étale case”.

> **Stacks Project, Tag 034G, étale case.** A property of morphisms of schemes which is
> Zariski local on the target and stable under étale base change is étale local on the target as
> soon as it descends along surjective standard étale morphisms of affine schemes.

```lean
theorem isLocalAtTarget_etale_of_standard_descent
    [P.IsStableUnderBaseChangeAgainst (@Etale)]
    [P.IsLocalAtTarget Scheme.zariskiPrecoverage]
    (h : ∀ {S S' X : Scheme.{u}} [IsAffine S] [IsAffine S']
      (g : S' ⟶ S) [Surjective g] (_hg : IsStandardEtale g)
      (f : X ⟶ S), P (pullback.snd f g) → P f) :
    P.IsLocalAtTarget Scheme.etalePrecoverage
```

**`AlgebraicGeometry.isLocalAtTarget_smooth_of_standard_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/Descent.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/Descent.lean#L279). The attribute's comment: “smooth case”.

> **Stacks Project, Tag 034G, smooth case.** A property of morphisms of schemes which is
> Zariski local on the target and stable under smooth base change is smooth local on the target as
> soon as it descends along surjective standard smooth morphisms of affine schemes.

```lean
theorem isLocalAtTarget_smooth_of_standard_descent
    [P.IsStableUnderBaseChangeAgainst (@Smooth)]
    [P.IsLocalAtTarget Scheme.zariskiPrecoverage]
    (h : ∀ {S S' X : Scheme.{u}} [IsAffine S] [IsAffine S']
      (g : S' ⟶ S) [Surjective g] (_hg : IsStandardSmooth g)
      (f : X ⟶ S), P (pullback.snd f g) → P f) :
    P.IsLocalAtTarget (Scheme.precoverage (@Smooth))
```

**`AlgebraicGeometry.isLocalAtTarget_syntomic_of_standard_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/Descent.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/StandardForm/Descent.lean#L306). The attribute's comment: “syntomic case”.

> **Stacks Project, Tag 034G, syntomic case.** A property of morphisms of schemes which is
> Zariski local on the target and stable under syntomic base change is syntomic local on the
> target as soon as it descends along surjective standard syntomic morphisms of affine
> schemes.

```lean
theorem isLocalAtTarget_syntomic_of_standard_descent
    [P.IsStableUnderBaseChangeAgainst (@Syntomic)]
    [P.IsLocalAtTarget Scheme.zariskiPrecoverage]
    (h : ∀ {S S' X : Scheme.{u}} [IsAffine S] [IsAffine S']
      (g : S' ⟶ S) [Surjective g] (_hg : IsStandardSyntomic g)
      (f : X ⟶ S), P (pullback.snd f g) → P f) :
    P.IsLocalAtTarget (Scheme.precoverage (@Syntomic))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.22, Tag 02KN](https://stacks.math.columbia.edu/tag/02KN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
