---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.quasiCompact_isLocalAtTarget_fpqc, AlgebraicGeometry.Space.isQuasiSeparated_isLocalAtTarget_fpqc, AlgebraicGeometry.Space.universallyClosed_isLocalAtTarget_fpqc, AlgebraicGeometry.Space.universallyOpen_isLocalAtTarget_fpqc, AlgebraicGeometry.Space.universallySubmersive_isLocalAtTarget_fpqc, AlgebraicGeometry.Space.surjective_isLocalAtTarget_fpqc, AlgebraicGeometry.Space.surjective_isLocalAtTarget_fppf, AlgebraicGeometry.Space.universallyInjective_isLocalAtTarget_fpqc
statement: formalized
proof: formalized
---

# 74.11 Descending properties of morphisms in the fpqc topology

Section 74.11 of the Stacks Project, [Tag 041K](https://stacks.math.columbia.edu/tag/041K). 30 tags here are carried by 39 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 041L, a lemma

[Tag 041L](https://stacks.math.columbia.edu/tag/041L) in the Stacks Project.

**`AlgebraicGeometry.Space.quasiCompact_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactFpqcLocalAtTarget.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactFpqcLocalAtTarget.lean#L218). References: SGA 4 IV (8.5.5), “more general”.

> Quasi-compactness of morphisms of algebraic spaces over `S` is local on
> the base for the fpqc topology.

```lean
instance quasiCompact_isLocalAtTarget_fpqc :
    (quasiCompactProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041N, a lemma

[Tag 041N](https://stacks.math.columbia.edu/tag/041N) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparated_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedFpqcLocalAtTarget.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedFpqcLocalAtTarget.lean#L147). References: EGA IV (2.7.1), “more general”; SGA 4 IV (8.5.5), “more general”.

> **Stacks 041N.** Quasi-separatedness of a morphism of algebraic spaces over `S` is local on
> the target for the fpqc topology.
>
> One direction is stability under base change (**Stacks 03KL**). In the other, quasi-separatedness
> of `f : X ⟶ Y` is quasi-compactness of `Δ_f : X ⟶ X ×_Y X`; the given fpqc covering of `Y` pulls
> back to one of `X ×_Y X` by part (3) of **Stacks 03MR**, the base change of `Δ_f` along each
> member of it is the relative diagonal of the corresponding base change of `f`, and so
> quasi-compactness of `Δ_f` follows from **Stacks 041L**.

```lean
instance isQuasiSeparated_isLocalAtTarget_fpqc :
    (quasiSeparatedProperty B S hS).IsLocalAtTarget
      (Topology.fpqc.precoverage.{u, v} B S hS)
```

## Tag 041O, a lemma

[Tag 041O](https://stacks.math.columbia.edu/tag/041O) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/UniversallyClosed.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/UniversallyClosed.lean#L221).

> **Stacks 041O.** Universal closedness of morphisms of algebraic spaces over `S` is local on
> the base for the fpqc topology.
>
> Universal closedness is being universally a closed morphism, so the ascent half is formal. For
> the descent half, condition (3) of Stacks 03IT reduces the assertion to closedness of the base
> changes along morphisms from the *affine* objects of the site; over such an affine `T` the fpqc
> condition of Stacks 03MQ supplies a finite affine family covering `T` and refining the given
> covering, and closedness of a morphism to a representable algebraic space descends along it.

```lean
instance universallyClosed_isLocalAtTarget_fpqc :
    (universallyClosedProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041P, a lemma

[Tag 041P](https://stacks.math.columbia.edu/tag/041P) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyOpen_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/UniversallyOpen.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/UniversallyOpen.lean#L228). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 041P.** Universal openness of morphisms of algebraic spaces over `S` is local on
> the base for the fpqc topology.

```lean
instance universallyOpen_isLocalAtTarget_fpqc :
    (universallyOpenMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0CFW, a lemma

[Tag 0CFW](https://stacks.math.columbia.edu/tag/0CFW) in the Stacks Project.

**`AlgebraicGeometry.Space.universallySubmersive_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/UniversallySubmersive.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/UniversallySubmersive.lean#L152).

> Universal submersiveness of morphisms of algebraic spaces over `S` is local on the base for the
> fpqc topology.

```lean
instance universallySubmersive_isLocalAtTarget_fpqc :
    (universallySubmersiveMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041Q, a lemma

[Tag 041Q](https://stacks.math.columbia.edu/tag/041Q) in the Stacks Project.

**`AlgebraicGeometry.Space.surjective_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveFpqcLocalAtTarget.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveFpqcLocalAtTarget.lean#L223). References: SGA 4 IV (8.5.5), “more general”.

> Surjectivity of morphisms of algebraic spaces over `S` is local on the base for the fpqc
> topology.

```lean
instance surjective_isLocalAtTarget_fpqc :
    (surjectiveMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

**`AlgebraicGeometry.Space.surjective_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveFpqcLocalAtTarget.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SurjectiveFpqcLocalAtTarget.lean#L252). The attribute's comment: “the fppf precoverage”.

> **Stacks 041Q** at the fppf precoverage: surjectivity of morphisms of algebraic spaces over
> `S` is local at the target for the fppf topology. This is the form in which the relative
> properties of Stacks 03YK ask for it; the comparison of precoverages is Stacks 0DFQ,
> `AlgebraicGeometry.Space.fppfPrecoverage_le_fpqcPrecoverage`.

```lean
instance surjective_isLocalAtTarget_fppf :
    (surjectiveMorphismProperty B S hS).IsLocalAtTarget
      (Topology.fppf.precoverage.{u, v} B S hS)
```

## Tag 041R, a lemma

[Tag 041R](https://stacks.math.columbia.edu/tag/041R) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyInjective_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyInjectiveFpqcLocalAtTarget.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyInjectiveFpqcLocalAtTarget.lean#L145).

> **Stacks 041R.** Universal injectivity of morphisms of algebraic spaces over `S` is local
> on the base for the fpqc topology.

```lean
instance universallyInjective_isLocalAtTarget_fpqc :
    (universallyInjectiveMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0CFX, a lemma

[Tag 0CFX](https://stacks.math.columbia.edu/tag/0CFX) in the Stacks Project.

**`AlgebraicGeometry.Space.universalHomeomorphism_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversalHomeomorphismFpqcLocalAtTarget.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversalHomeomorphismFpqcLocalAtTarget.lean#L264). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 0CFX.** Being a universal homeomorphism is, for morphisms of algebraic spaces over
> `S`, local on the base for the fpqc topology of Stacks 03YH: such a morphism is a universal
> homeomorphism exactly when its base change to every member of some fpqc covering family of its
> target is a universal homeomorphism.
>
> A morphism is a universal homeomorphism exactly when it is surjective, universally injective
> and universally open, surjectivity is fpqc local on the base by **Stacks 041Q**, universal
> injectivity by **Stacks 041R** and universal openness by **Stacks 041P**, so their conjunction
> is.

```lean
instance universalHomeomorphism_isLocalAtTarget_fpqc :
    (universalHomeomorphismMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041S, a lemma

[Tag 041S](https://stacks.math.columbia.edu/tag/041S) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyOfFiniteType_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FinitenessFpqcLocality.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FinitenessFpqcLocality.lean#L54).

> Being locally of finite type is, for morphisms of algebraic spaces over `S`, local on the
> base for the fpqc topology.

```lean
instance locallyOfFiniteType_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsLocallyOfFiniteType B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041T, a lemma

[Tag 041T](https://stacks.math.columbia.edu/tag/041T) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationFpqcLocalAtTarget.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationFpqcLocalAtTarget.lean#L355). References: EGA IV (2.7.1), “more general”; SGA 3 VIB (10.8), “(i)⇒(ii)”; SGA 4 IV (8.5.5), “more general”.

> **Stacks Project, Tag 041T** (Lemma 74.11.10 of Chapter 74, *Descent and Algebraic
> Spaces*). The property `𝒫(f)` = "`f` is locally of finite presentation" of morphisms of
> algebraic spaces over `S` is fpqc local on the base.
>
> The setting is the source's own. By the conventions of that chapter (**Stacks 041I**, Section
> 74.2) every scheme lies in a big fppf site `Sch_fppf`, here `B`, and `S` is one of its objects;
> algebraic spaces over `S` are the objects of `AlgebraicSpaces B S S_mem`, and local finite
> presentation of a morphism of algebraic spaces is that of **Stacks 03XP**, part (1). "Fpqc local
> on the base" is Definition 74.10.1 (**Stacks 03YH**) at the fpqc topology: for every fpqc
> covering `{Yᵢ → Y}` of algebraic spaces in the sense of **Stacks 03MQ**, indexed by a type in any
> universe `v`, and every morphism `f : X ⟶ Y`, the morphism `f` is locally of finite presentation
> if and only if every base change `Yᵢ ×_Y X → Yᵢ` is. That is the class
> `CategoryTheory.MorphismProperty.IsLocalAtTarget` at `Topology.fpqc.precoverage`, whose coverings
> are exactly the families `Presieve.ofArrows Yᵢ gᵢ` with `gᵢ` an fpqc covering of `Y`.
>
> The scheme-level statement, for morphisms of schemes, is Descent, Lemma 35.23.13 (**Stacks
> 02KY**), `Stacks.Descent.locallyOfFinitePresentation_isLocalAtTarget_fpqc`; the proof of the
> source reduces to it, and so does this one.

```lean
instance isLocallyOfFinitePresentation_isLocalAtTarget_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (S_mem : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S S_mem⦄ (f : X ⟶ Y) =>
        IsLocallyOfFinitePresentation B S S_mem f.hom)
      (Topology.fpqc.precoverage.{u, v} B S S_mem)
```

## Tag 041U, a lemma

[Tag 041U](https://stacks.math.columbia.edu/tag/041U) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteType_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeFpqcLocalAtTarget.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeFpqcLocalAtTarget.lean#L81).

> **Stacks 041U.** Being of finite type, as a property of morphisms of algebraic spaces over
> `S`, is local on the target for the fpqc topology.
>
> Being of finite type is being locally of finite type and quasi-compact (**Stacks 03XF**, part
> (3)); the first conjunct is local on the target for the fpqc topology by **Stacks 041S** and the
> second by **Stacks 041L**, so their conjunction is.

```lean
instance isFiniteType_isLocalAtTarget_fpqc :
    (finiteTypeProperty B S hS).IsLocalAtTarget
      (Topology.fpqc.precoverage.{u, v} B S hS)
```

**`AlgebraicGeometry.Space.finiteType_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FinitenessFpqcLocality.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FinitenessFpqcLocality.lean#L66).

> Being of finite type is, for morphisms of algebraic spaces over `S`, local on the base for
> the fpqc topology.

```lean
instance finiteType_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsFiniteType B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041V, a lemma

[Tag 041V](https://stacks.math.columbia.edu/tag/041V) in the Stacks Project.

**`AlgebraicGeometry.Space.finitePresentation_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FinitePresentationFpqcLocality.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/FinitePresentationFpqcLocality.lean#L71). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 041V.** Being of finite presentation is, for morphisms of algebraic spaces over
> `S`, local on the base for the fpqc topology of Stacks 03YH.
>
> Being of finite presentation is being locally of finite presentation (Stacks 041T) together with
> quasi-compactness (Stacks 041L) and quasi-separatedness (Stacks 041N).

```lean
instance finitePresentation_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsFinitePresentation B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041W, a lemma

[Tag 041W](https://stacks.math.columbia.edu/tag/041W) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFpqcLocality.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFpqcLocality.lean#L111).

> **Stacks 041W.** Flatness of a morphism of algebraic spaces over `S` is local on the target
> for the fpqc topology.

```lean
instance isFlat_isLocalAtTarget_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsFlat B S hS f.hom)
      (Topology.fpqc.precoverage.{u, v} B S hS)
```

**`AlgebraicGeometry.Space.isFlat_isLocalAtTarget_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean#L87). The attribute's comment: “the fppf precoverage”.

> **Stacks 041W** at the fppf precoverage: flatness of morphisms of algebraic spaces over `S`
> is local at the target for the fppf topology. It follows from the fpqc form
> `AlgebraicGeometry.Space.isFlat_isLocalAtTarget_fpqc` through
> `AlgebraicGeometry.Space.fppfPrecoverage_le_fpqcPrecoverage`, and it is the form in
> which the relative properties of Stacks 03YK ask for it; it is the exact analogue of
> `AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isLocalAtTarget_fppf` and of
> `AlgebraicGeometry.Space.smooth_isLocalAtTarget_fppf`.

```lean
theorem isFlat_isLocalAtTarget_fppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (g : X ⟶ Y) => IsFlat B S hS g.hom)
      (Topology.fppf.precoverage.{u, v} B S hS)
```

## Tag 041X, a lemma

[Tag 041X](https://stacks.math.columbia.edu/tag/041X) in the Stacks Project.

**`AlgebraicGeometry.Space.openImmersion_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionFpqcLocalAtTarget.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/OpenImmersionFpqcLocalAtTarget.lean#L371).

> **Stacks 041X.** Being an open immersion of algebraic spaces over `S` is local on the base
> for the fpqc topology.

```lean
instance openImmersion_isLocalAtTarget_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (openImmersionProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041Y, a lemma

[Tag 041Y](https://stacks.math.columbia.edu/tag/041Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isomorphisms_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IsomorphismFpqcLocalAtTarget.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IsomorphismFpqcLocalAtTarget.lean#L122). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 041Y.** Being an isomorphism is, for morphisms of algebraic spaces over `S`, local
> on the base for the fpqc topology of Stacks 03YH: such a morphism is an isomorphism exactly
> when its base change to every member of some fpqc covering family of its target is an
> isomorphism.
>
> A morphism is an isomorphism exactly when it is a surjective open immersion, surjectivity is
> fpqc local on the base by **Stacks 041Q** and being an open immersion by **Stacks 041X**, so
> their conjunction is.

```lean
instance isomorphisms_isLocalAtTarget_fpqc :
    (MorphismProperty.isomorphisms (AlgebraicSpaces B S hS)).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 041Z, a lemma

[Tag 041Z](https://stacks.math.columbia.edu/tag/041Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalAtTarget_isAffineHom_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcSheaf.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcSheaf.lean#L86).

> **Affineness of morphisms of algebraic spaces is fpqc local on the base**, which is
> [Stacks, Tag 041Z](https://stacks.math.columbia.edu/tag/041Z).

```lean
theorem isLocalAtTarget_isAffineHom_fpqc (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun {X Y} (f : X ⟶ Y) => IsAffineHom B S hS f.hom :
        MorphismProperty (AlgebraicSpaces B S hS))
      (Topology.fpqc.precoverage.{u, v} B S hS)
```

## Tag 0420, a lemma

[Tag 0420](https://stacks.math.columbia.edu/tag/0420) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionFppfLocalAtTarget.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionFppfLocalAtTarget.lean#L72). The attribute's comment: “the fppf precoverage”.

> **Stacks 0420** at the fppf precoverage: being a closed immersion is local on the base for
> the fppf topology for morphisms of algebraic spaces over `S`, so such a morphism is a closed
> immersion exactly when its base change to every member of some fppf covering of its target is
> one.
>
> The fpqc form is `AlgebraicGeometry.Space.isClosedImmersion_isLocalAtTarget_fpqc`, and the two
> are compared by `AlgebraicGeometry.Space.fppfPrecoverage_le_fpqcPrecoverage` (Stacks 0DFQ). This
> is the form in which the relative properties of Stacks 03YK ask for it.

```lean
instance isClosedImmersion_isLocalAtTarget_fppf :
    (closedImmersionProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fppf B S hS)
```

**`AlgebraicGeometry.Space.isClosedImmersion_isLocalAtTarget_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionFpqcLocalAtTarget.lean, line 758](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionFpqcLocalAtTarget.lean#L758). References: SGA 3 IV (6.4.1), “(N')”.

> **Stacks 0420.** Being a closed immersion is fpqc local on the base for morphisms of
> algebraic spaces over `S`: such a morphism is a closed immersion exactly when its base change
> to every member of some fpqc covering of its target is one.

```lean
theorem isClosedImmersion_isLocalAtTarget_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsClosedImmersion B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0421, a lemma

[Tag 0421](https://stacks.math.columbia.edu/tag/0421) in the Stacks Project.

**`AlgebraicGeometry.Space.separated_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedFpqcLocalAtTarget.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedFpqcLocalAtTarget.lean#L78). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 0421.** Separatedness of morphisms of algebraic spaces over `S` is local on the
> base for the fpqc topology: a morphism is separated exactly when its base change to every member
> of some fpqc covering of its target is separated.
>
> Separatedness of `f : X ⟶ Y` is the relative diagonal `Δ_f : X ⟶ X ×_Y X` being a closed
> immersion. Pulling a covering `{Y i ⟶ Y}` back along `X ×_Y X ⟶ Y` gives a covering of `X ×_Y X`
> whose base changes of `Δ_f` are the relative diagonals of the base changes of `f`, so Stacks
> 0420 for closed immersions applies.

```lean
instance separated_isLocalAtTarget_fpqc :
    (separatedProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0422, a lemma

[Tag 0422](https://stacks.math.columbia.edu/tag/0422) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperULift_of_isPullback_uliftYoneda_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperEtaleDescent.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperEtaleDescent.lean#L87). The attribute's comment: “for a family of morphisms of the site, in the value universe of a formal algebraic space”. References: SGA 1 VIII (4.8), “partial”.

> **Stacks 0422 for a family of morphisms of the site, in the value universe `Type (u + 1)`.**
> Let `p : F ⟶ U` be a morphism of presheaves on the big fppf site of `S` with values in
> `Type (u + 1)` whose source is an algebraic space over `S` and whose target is the
> universe-lifted representable sheaf of an object `U` of the site, and let `{qᵢ : Vᵢ ⟶ U}` be a
> family of morphisms of the site whose Yoneda images form an fppf covering family of `U` in the
> sense of **Stacks 03Y8**. If some base change of `p` along each `qᵢ` is proper, then `p` is
> proper.
>
> The source and the base changes are algebraic spaces, hence universe lifts of presheaves in the
> value universe of the site; there properness of a lift is properness of the presheaf
> (`AlgebraicGeometry.Space.isProperULift_whiskerRight_iff`) and the covering family generates a
> covering family of the fpqc precoverage of Stacks 03YH, at which properness is local on the
> base by **Stacks 0422**.

```lean
theorem isProperULift_of_isPullback_uliftYoneda_family
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)} {U : BigFppfOver B S hS}
    {p : F ⟶ (uliftYoneda.{u + 1}).obj U} {Idx : Type (u + 1)}
    {V : Idx → BigFppfOver B S hS} {q : ∀ i, V i ⟶ U}
    {F' : Idx → ((BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1))}
    {p' : ∀ i, F' i ⟶ (uliftYoneda.{u + 1}).obj (V i)} {k : ∀ i, F' i ⟶ F}
    (sq : ∀ i, IsPullback (k i) (p' i) p ((uliftYoneda.{u + 1}).map (q i)))
    (hF : IsAlgebraicSpaceULift.{u + 1} B S hS F)
    (hcov : IsFppfCovering B S hS (fun i => yoneda.obj (V i)) (fun i => yoneda.map (q i)))
    (hp' : ∀ i, IsProperULift.{u + 1} B S hS (p' i)) :
    IsProperULift.{u + 1} B S hS p
```

**`AlgebraicGeometry.Space.isProperULift_of_isPullback_uliftYoneda_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperEtaleDescent.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperEtaleDescent.lean#L195). The attribute's comment: “for one surjective étale morphism of the site, in the value universe of a formal algebraic space”.

> **Stacks 0422 for a single surjective étale morphism of the site, in the value universe
> `Type (u + 1)`.** Let `p : F ⟶ U` be a morphism of presheaves on the big fppf site of `S` with
> values in `Type (u + 1)` whose source is an algebraic space over `S` and whose target is the
> universe-lifted representable sheaf of an object `U` of the site, and let `q : U' ⟶ U` be a
> morphism of the site which is surjective and étale on underlying schemes. If some base change
> of `p` along `q` is proper, then `p` is proper.
>
> The one-member family consisting of the Yoneda image of `q` is an fppf covering family of its
> target by `AlgebraicGeometry.Space.isFppfCovering_atlas`, so this is the family statement at
> that family.

```lean
theorem isProperULift_of_isPullback_uliftYoneda_map
    {F F' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)} {U U' : BigFppfOver B S hS}
    {p : F ⟶ (uliftYoneda.{u + 1}).obj U} {p' : F' ⟶ (uliftYoneda.{u + 1}).obj U'}
    {k : F' ⟶ F} (q : U' ⟶ U)
    (sq : IsPullback k p' p ((uliftYoneda.{u + 1}).map q))
    (hF : IsAlgebraicSpaceULift.{u + 1} B S hS F)
    (hqs : Surjective ((BigFppfOver.toScheme B S hS).map q))
    (hqe : Etale ((BigFppfOver.toScheme B S hS).map q))
    (hp' : IsProperULift.{u + 1} B S hS p') :
    IsProperULift.{u + 1} B S hS p
```

**`AlgebraicGeometry.Space.proper_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFpqcLocalAtTarget.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFpqcLocalAtTarget.lean#L65). References: SGA 1 VIII (4.8), “more general”; SGA 4 IV (8.5.5), “more general”.

> **Stacks 0422.** Properness of morphisms of algebraic spaces over `S` is local on the base
> for the fpqc topology: a morphism is proper exactly when its base change to every member of some
> fpqc covering family of its target is proper.
>
> Being proper is being separated, of finite type and universally closed (**Stacks 03ZM**); the
> three conjuncts are local on the base for the fpqc topology by **Stacks 0421**, **Stacks 041U**
> and **Stacks 041O**, so their conjunction is.

```lean
instance proper_isLocalAtTarget_fpqc :
    (properProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0423, a lemma

[Tag 0423](https://stacks.math.columbia.edu/tag/0423) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalAtTarget_isQuasiAffineHom_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFpqcChartDescent.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFpqcChartDescent.lean#L647). References: EGA IV (2.7.1), “more general”; SGA 4 IV (8.5.5), “more general”.

> **Stacks 0423** (Lemma 74.11.20 of Chapter 74, *Descent and Algebraic Spaces*). The
> property "`f` is quasi-affine" of morphisms of algebraic spaces over `S` is fpqc local on the
> base, in the sense of Definition 74.10.1 (Stacks 03YH): for every fpqc covering
> `{Yᵢ ⟶ Y}` of algebraic spaces over `S` (Stacks 03MQ) and every morphism of algebraic spaces
> `f : X ⟶ Y`, the morphism `f` is quasi-affine if and only if each base change
> `Yᵢ ×_Y X ⟶ Yᵢ` is quasi-affine.
>
> The setting is that of the conventions of Chapter 74 (Stacks 041I): `S` is a scheme of the big
> fppf site `B`, algebraic spaces over `S` are sheaves on the big fppf site of `S`, and
> quasi-affineness is the notion of Stacks 03WL, `AlgebraicGeometry.Space.IsQuasiAffineHom`:
> every base change to an affine scheme is represented by a quasi-affine scheme. Locality on the
> base is `CategoryTheory.MorphismProperty.IsLocalAtTarget` for the fpqc precoverage
> `AlgebraicGeometry.Space.Topology.precoverage .fpqc` of the category of algebraic spaces over
> `S`, whose covering presieves are those generated by the fpqc coverings, with index sets in any
> universe.

```lean
theorem isLocalAtTarget_isQuasiAffineHom_fpqc (B : BigFppfSite.{u}) (S : Scheme.{u})
    (contains : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun {X Y : AlgebraicSpaces B S contains} (g : X ⟶ Y) ↦
          IsQuasiAffineHom B S contains g.hom :
        MorphismProperty (AlgebraicSpaces B S contains))
      (Topology.fpqc.precoverage.{u, v} B S contains)
```

## Tag 0424, a lemma

[Tag 0424](https://stacks.math.columbia.edu/tag/0424) in the Stacks Project.

**`AlgebraicGeometry.Space.immersion_inf_quasiCompact_isLocalAtTarget_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactImmersionFpqcLocalAtTarget.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiCompactImmersionFpqcLocalAtTarget.lean#L235). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 0424.** Being a quasi-compact immersion is fpqc local on the base for morphisms of
> algebraic spaces over `S`: such a morphism is a quasi-compact immersion exactly when its base
> change to every member of some fpqc covering of its target is a quasi-compact immersion.

```lean
theorem immersion_inf_quasiCompact_isLocalAtTarget_fpqc :
    (immersionProperty B S hS ⊓ quasiCompactProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0425, a lemma

[Tag 0425](https://stacks.math.columbia.edu/tag/0425) in the Stacks Project.

**`AlgebraicGeometry.Space.integralMorphismProperty_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/Integral.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/Fpqc/Integral.lean#L162). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 0425.** Integrality of morphisms of algebraic spaces over `S` is local on the base
> for the fpqc topology of Stacks 03YH.
>
> An integral morphism is an affine universally closed one (Stacks 0415), affineness is fpqc local
> on the base (Stacks 041Z) and so is universal closedness (Stacks 041O), and locality on the base
> passes to an infimum of morphism properties.

```lean
instance integralMorphismProperty_isLocalAtTarget_fpqc :
    (integralMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0426, a lemma

[Tag 0426](https://stacks.math.columbia.edu/tag/0426) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteFpqcLocalAtTarget.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteFpqcLocalAtTarget.lean#L97). References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 0426.** Finiteness of morphisms of algebraic spaces over `S` is local on the base
> for the fpqc topology of Stacks 03YH: a morphism is finite exactly when its base change to every
> member of some fpqc covering family of its target is finite.
>
> A morphism is finite exactly when it is proper and locally quasi-finite (**Stacks 0A4X**),
> properness is fpqc local on the base by **Stacks 0422** and local quasi-finiteness by
> **Stacks 0427**, so their conjunction is.

```lean
instance isFinite_isLocalAtTarget_fpqc :
    (finiteMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0427, a lemma

[Tag 0427](https://stacks.math.columbia.edu/tag/0427) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteFpqcLocalAtTarget.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteFpqcLocalAtTarget.lean#L59). The attribute's comment: “locally quasi-finite case”.

> **Stacks 0427**, the locally quasi-finite case.  Local quasi-finiteness of a morphism of
> algebraic spaces over `S` is local on the base for the fpqc topology of Stacks 03YH.

```lean
instance isLocallyQuasiFinite_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsLocallyQuasiFinite B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

**`AlgebraicGeometry.Space.isQuasiFinite_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteFpqcLocalAtTarget.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiFiniteFpqcLocalAtTarget.lean#L79). The attribute's comment: “quasi-finite case”. References: SGA 4 IV (8.5.5), “more general”.

> **Stacks 0427**, the quasi-finite case.  Quasi-finiteness of a morphism of algebraic spaces
> over `S` is local on the base for the fpqc topology of Stacks 03YH.
>
> Quasi-finiteness is local quasi-finiteness together with quasi-compactness, and quasi-compactness
> is fpqc local on the base by Stacks 041L.

```lean
instance isQuasiFinite_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsQuasiFinite B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0428, a lemma

[Tag 0428](https://stacks.math.columbia.edu/tag/0428) in the Stacks Project.

**`AlgebraicGeometry.Space.syntomic_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SyntomicFpqcLocalAtTarget.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SyntomicFpqcLocalAtTarget.lean#L49).

> **Stacks 0428.**  Syntomicity of a morphism of algebraic spaces over `S` is local on the
> base for the fpqc topology of Stacks 03YH.

```lean
instance syntomic_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsSyntomic B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0429, a lemma

[Tag 0429](https://stacks.math.columbia.edu/tag/0429) in the Stacks Project.

**`AlgebraicGeometry.Space.smooth_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean#L474). The attribute's comment: “the fppf precoverage”.

> **Stacks 0429** at the fppf precoverage: smoothness of morphisms of algebraic spaces over
> `S` is local at the target for the fppf topology. The fpqc form is
> `AlgebraicGeometry.Space.smooth_isLocalAtTarget_fpqc`, and the two are compared by
> `AlgebraicGeometry.Space.fppfPrecoverage_le_fpqcPrecoverage`. This is the form in which Stacks
> 03YK's relative properties ask for it.

```lean
instance smooth_isLocalAtTarget_fppf (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    (smoothMorphismProperty B S hS).IsLocalAtTarget
      (Topology.fppf.precoverage.{u, v} B S hS)
```

**`AlgebraicGeometry.Space.smooth_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothFpqcLocalAtTarget.lean, line 791](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothFpqcLocalAtTarget.lean#L791).

> Smoothness of algebraic-space morphisms is fpqc local on the base.

```lean
instance smooth_isLocalAtTarget_fpqc (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) :
    (smoothMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 042A, a lemma

[Tag 042A](https://stacks.math.columbia.edu/tag/042A) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedFpqcLocalAtTarget.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedFpqcLocalAtTarget.lean#L243).

> Unramifiedness of a morphism of algebraic spaces over `S` is local on the target for the
> fpqc topology.

```lean
public instance isUnramified_isLocalAtTarget_fpqc
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) =>
        IsUnramified B S hS f.hom)
      (Topology.fpqc.precoverage.{u, v} B S hS)
```

**`AlgebraicGeometry.Space.isUnramified_iff_forall_pullbackSnd_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedFpqcLocalAtTarget.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedFpqcLocalAtTarget.lean#L285). The attribute's comment: “Definition 03YH unfolded: f unramified iff every Yᵢ ×_Y X → Yᵢ is”.

> Let `{gᵢ : Yᵢ ⟶ Y}` be an fpqc covering of algebraic spaces over `S`, indexed by a type `I`
> in any universe, and `f : X ⟶ Y` a morphism of algebraic spaces over `S`. Then `f` is unramified
> if and only if every base change `pullback.snd f (g i) : Yᵢ ×_Y X ⟶ Yᵢ` of `f` is unramified.

```lean
theorem isUnramified_iff_forall_pullbackSnd_of_isFpqcCovering
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {I : Type v} {X Y : AlgebraicSpaces B S hS} {Yi : I → AlgebraicSpaces B S hS}
    (g : ∀ i, Yi i ⟶ Y) (hg : IsFpqcCovering B S hS (fun i => (g i).hom)) (f : X ⟶ Y) :
    IsUnramified B S hS f.hom ↔ ∀ i, IsUnramified B S hS (pullback.snd f (g i)).hom
```

## Tag 042B, a lemma

[Tag 042B](https://stacks.math.columbia.edu/tag/042B) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtale_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFpqcLocalAtTarget.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFpqcLocalAtTarget.lean#L54).

> **Stacks 042B.**  Étaleness of a morphism of algebraic spaces over `S` is local on the base
> for the fpqc topology of Stacks 03YH.

```lean
instance isEtale_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) => IsEtale B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 042C, a lemma

[Tag 042C](https://stacks.math.columbia.edu/tag/042C) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFree_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFpqcLocalAtTarget.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFpqcLocalAtTarget.lean#L116).

> **Stacks 042C.** Being finite locally free is, for morphisms of algebraic spaces over `S`,
> local on the base for the fpqc topology of Stacks 03YH: such a morphism is finite locally free
> exactly when its base change to every member of some fpqc covering family of its target is
> finite locally free.
>
> A morphism is finite locally free exactly when it is finite, flat and locally of finite
> presentation (**Stacks 0416**), finiteness is fpqc local on the base by **Stacks 0426**,
> flatness by **Stacks 041W** and local finite presentation by **Stacks 041T**, so their
> conjunction is.

```lean
instance isFiniteLocallyFree_isLocalAtTarget_fpqc :
    (finiteLocallyFreeMorphismProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 042D, a lemma

[Tag 042D](https://stacks.math.columbia.edu/tag/042D) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MonomorphismFpqcLocalAtTarget.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MonomorphismFpqcLocalAtTarget.lean#L133). References: SGA 3 IV (4.5.8), “special case”; SGA 4 IV (8.5.5), “more general”.

> **Stacks 042D.** Monomorphy of morphisms of algebraic spaces over `S` is local on the base for
> the fpqc topology: a morphism is a monomorphism exactly when its base change to every member of
> some fpqc covering of its target is a monomorphism.
>
> Stacks 042Q reduces monomorphy to monomorphy of the base changes along the morphisms out of the
> affine objects of the site, over such an object the covering is refined by a finite family of
> affine objects factoring through its members, and monomorphy descends along the fpqc covering
> sieve that family generates because the fibre product is an fpqc sheaf by Stacks 0APL.

```lean
instance mono_isLocalAtTarget_fpqc :
    (MorphismProperty.monomorphisms (AlgebraicSpaces B S hS)).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.11, Tag 041K](https://stacks.math.columbia.edu/tag/041K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
