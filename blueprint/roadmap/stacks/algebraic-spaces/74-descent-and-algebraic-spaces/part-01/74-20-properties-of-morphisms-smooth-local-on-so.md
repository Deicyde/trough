---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsSmoothLocalOnSourceAndTarget, AlgebraicGeometry.Space.isSmoothLocalAtSource, AlgebraicGeometry.Space.isSmoothLocalAtTarget, AlgebraicGeometry.Space.comp_smooth, AlgebraicGeometry.Space.smoothLocalOnSourceAndTarget_tfae, AlgebraicGeometry.Space.isSmoothLocalOnSourceAndTarget, AlgebraicGeometry.Space.isSyntomic_isSmoothLocalOnSourceAndTarget, AlgebraicGeometry.Space.universallyOpen_isSmoothLocalOnSourceAndTarget
statement: formalized
proof: formalized
---

# 74.20 Properties of morphisms smooth local on source-and-target

Section 74.20 of the Stacks Project, [Tag 06F7](https://stacks.math.columbia.edu/tag/06F7). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06F8, a definition

[Tag 06F8](https://stacks.math.columbia.edu/tag/06F8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSmoothLocalOnSourceAndTarget`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalOnSourceAndTarget.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalOnSourceAndTarget.lean#L55).

> **Stacks 06F8.** A property of morphisms of algebraic spaces over `S` is *smooth local on
> the source-and-target* when it is stable under smooth precomposition and smooth base change, and
> can be checked in smooth neighbourhoods of every point of the source.

```lean
structure IsSmoothLocalOnSourceAndTarget
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) : Prop
```

## Tag 06F9, a lemma

[Tag 06F9](https://stacks.math.columbia.edu/tag/06F9) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmoothLocalAtSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean#L163). The attribute's comment: “smooth\_local\_source”.

> **Stacks 06F9**, smooth locality on the source. A property of morphisms of algebraic spaces
> over `S` which is smooth local on the source-and-target is local at the source for the smooth
> precoverage.

```lean
theorem isSmoothLocalAtSource
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : IsSmoothLocalOnSourceAndTarget B S hS P) :
    (P.inverseImage (ObjectProperty.ι
      (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
        IsAlgebraicSpace B S hS F))).IsLocalAtSource
      (Topology.precoverage.{u, v} .smooth B S hS)
```

**`AlgebraicGeometry.Space.isSmoothLocalAtTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean#L212). The attribute's comment: “smooth\_local\_target”.

> **Stacks 06F9**, smooth locality on the target. A property of morphisms of algebraic spaces
> over `S` which is smooth local on the source-and-target is local at the target for the smooth
> precoverage.

```lean
theorem isSmoothLocalAtTarget
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : IsSmoothLocalOnSourceAndTarget B S hS P) :
    (P.inverseImage (ObjectProperty.ι
      (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
        IsAlgebraicSpace B S hS F))).IsLocalAtTarget
      (Topology.precoverage.{u, v} .smooth B S hS)
```

**`AlgebraicGeometry.Space.comp_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean#L272). The attribute's comment: “smooth\_postcomposition”.

> **Stacks 06F9**, smooth postcomposition. A property of morphisms of algebraic spaces over
> `S` which is smooth local on the source-and-target is preserved by postcomposition with a smooth
> morphism.

```lean
theorem comp_smooth
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : IsSmoothLocalOnSourceAndTarget B S hS P)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z)
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : P f) (hg : IsSmooth B S hS g) : P (f ≫ g)
```

## Tag 06FA, a lemma

[Tag 06FA](https://stacks.math.columbia.edu/tag/06FA) in the Stacks Project.

**`AlgebraicGeometry.Space.smoothLocalOnSourceAndTarget_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalProperties.lean#L337).

> **Stacks 06FA.** Seven equivalent criteria for a morphism of algebraic spaces over `S` to
> have a property which is smooth local on the source-and-target: the property itself; a smooth
> neighbourhood of every point of the source on which it holds; one smooth diagram surjective on
> the source; every smooth comparison into a fibre product over a smooth base change; a smooth
> covering of the target over which the base changes have it; a smooth covering of the source whose
> composites have it; and a smooth covering of the target refined by smooth coverings of the
> corresponding fibre products.

```lean
theorem smoothLocalOnSourceAndTarget_tfae
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (hP : IsSmoothLocalOnSourceAndTarget B S hS P)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      P f,
      (∀ x : points B S hS X,
        ∃ (U V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (_hU : IsAlgebraicSpace B S hS U)
          (_hV : IsAlgebraicSpace B S hS V)
          (a : U ⟶ X) (b : V ⟶ Y) (h : U ⟶ V)
          (u : points B S hS U),
          IsSmooth B S hS a ∧
            IsSmooth B S hS b ∧
            pointsMap B S hS U a u = x ∧
            h ≫ b = a ≫ f ∧ P h),
      (∃ (U V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (_hU : IsAlgebraicSpace B S hS U)
          (_hV : IsAlgebraicSpace B S hS V)
          (a : U ⟶ X) (b : V ⟶ Y) (h : U ⟶ V),
          IsSmooth B S hS a ∧
            IsSurjective B S hS a ∧
            IsSmooth B S hS b ∧
            h ≫ b = a ≫ f ∧ P h),
      (∀ (U V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (_hU : IsAlgebraicSpace B S hS U)
          (_hV : IsAlgebraicSpace B S hS V)
          (b : V ⟶ Y) (k : U ⟶ pullback f b),
          IsSmooth B S hS b →
          IsSmooth B S hS k →
          P (k ≫ pullback.snd f b)),
      (∃ (I : Type v)
          (V : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (b : ∀ i, V i ⟶ Y),
          IsSmoothCovering B S hS V b ∧
          ∀ i, P (pullback.snd f (b i))),
      (∃ (I : Type v)
          (U : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (a : ∀ i, U i ⟶ X),
          IsSmoothCovering B S hS U a ∧
          ∀ i, P (a i ≫ f)),
      (∃ (I : Type v)
          (V : I → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (b : ∀ i, V i ⟶ Y)
          (J : I → Type w)
          (U : ∀ i, J i → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
          (a : ∀ i j, U i j ⟶ pullback f (b i)),
          IsSmoothCovering B S hS V b ∧
          (∀ i, IsSmoothCovering B S hS (U i) (a i)) ∧
          (∀ i j, P (a i j ≫ pullback.snd f (b i))))
    ]
```

## Tag 06FB, a lemma

[Tag 06FB](https://stacks.math.columbia.edu/tag/06FB) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmoothLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/SmoothCriterion.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/SmoothCriterion.lean#L75).

> **Stacks 06FB.** A property of morphisms of algebraic spaces over `S` which is local at the
> source and at the target for the smooth topology, and is preserved by postcomposition with a
> smooth morphism, is smooth local on the source-and-target.

```lean
theorem isSmoothLocalOnSourceAndTarget
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    [hSource : (P.inverseImage (ObjectProperty.ι
      (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
        IsAlgebraicSpace B S hS F))).IsLocalAtSource
      (Topology.precoverage.{u, u + 1} .smooth B S hS)]
    [hTarget : (P.inverseImage (ObjectProperty.ι
      (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
        IsAlgebraicSpace B S hS F))).IsLocalAtTarget
      (Topology.precoverage.{u, u + 1} .smooth B S hS)]
    (hcomp : ∀ {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
      (_hX : IsAlgebraicSpace B S hS X)
      (_hY : IsAlgebraicSpace B S hS Y)
      (_hZ : IsAlgebraicSpace B S hS Z)
      (f : X ⟶ Y) (g : Y ⟶ Z),
      P f → IsSmooth B S hS g → P (f ≫ g)) :
    IsSmoothLocalOnSourceAndTarget B S hS P
```

## Tag 06FC, a remark

[Tag 06FC](https://stacks.math.columbia.edu/tag/06FC) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_isSmoothLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/Syntomic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/Syntomic.lean#L66). The attribute's comment: “syntomic”.

> **Stacks 06FC**, the syntomic case. Syntomicity of morphisms of algebraic spaces over `S`
> is smooth local on the source-and-target.
>
> The source locality hypothesis of Stacks 06FB comes from the syntomic one, Stacks 06F0, along
> `AlgebraicGeometry.Space.Topology.precoverage_smooth_le_syntomic`; the target locality one
> comes from the fpqc one, Stacks 0428, along
> `AlgebraicGeometry.Space.Topology.precoverage_smooth_le_fpqc`; and the postcomposition
> hypothesis is composition of syntomic morphisms (Stacks 03Z8) applied to the fact that a
> smooth morphism is syntomic.

```lean
theorem isSyntomic_isSmoothLocalOnSourceAndTarget :
    IsSmoothLocalOnSourceAndTarget B S hS (fun _ _ f => IsSyntomic B S hS f)
```

**`AlgebraicGeometry.Space.universallyOpen_isSmoothLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/UniversallyOpen.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/LocalOnSourceAndTarget/UniversallyOpen.lean#L77). The attribute's comment: “universally open”.

> **Stacks 06FC**, the universally-open case. Being universally open is, for morphisms of
> algebraic spaces over `S`, smooth local on the source-and-target.
>
> The source locality hypothesis of Stacks 06FB comes from the fppf one, Stacks 06EY, along
> `AlgebraicGeometry.Space.Topology.precoverage_smooth_le_fppf`; the target locality one comes
> from the fpqc one, Stacks 041P, along
> `AlgebraicGeometry.Space.Topology.precoverage_smooth_le_fpqc`; and the postcomposition
> hypothesis is composition of universally open morphisms (Stacks 03Z4) applied to
> `AlgebraicGeometry.Space.universallyOpen_of_isSmooth`.

```lean
theorem universallyOpen_isSmoothLocalOnSourceAndTarget :
    IsSmoothLocalOnSourceAndTarget B S hS
      (fun _ _ f => UniversallyOpen B S hS f)
```

**`AlgebraicGeometry.Space.isSmoothLocalOnSourceAndTarget_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalityCriterion.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalityCriterion.lean#L187). The attribute's comment: “flat”.

> **Stacks 06FC**, the flat case. Flatness of morphisms of algebraic spaces over `S` is smooth
> local on the source-and-target.
>
> The two locality hypotheses of Stacks 06FB come from the fpqc ones (Stacks 06ET and 041W) along
> `AlgebraicGeometry.Space.smooth_precoverage_le_fpqc`, and the postcomposition hypothesis is
> composition of flat morphisms (Stacks 03MN) applied to the flatness of a smooth morphism
> (Stacks 04TA).

```lean
theorem isSmoothLocalOnSourceAndTarget_flat :
    IsSmoothLocalOnSourceAndTarget B S hS (fun _ _ f => IsFlat B S hS f)
```

**`AlgebraicGeometry.Space.isSmoothLocalOnSourceAndTarget_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalityFiniteness.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalityFiniteness.lean#L150). The attribute's comment: “locally\_of\_finite\_type”.

> **Stacks 06FC**, the locally-of-finite-type case. Being locally of finite type for morphisms
> of algebraic spaces over `S` is smooth local on the source-and-target.
>
> The source locality hypothesis of Stacks 06FB is
> `AlgebraicGeometry.Space.isLocallyOfFiniteType_isLocalAtSource_smooth`; the target locality one
> comes from the fpqc statement of Stacks 041S along
> `AlgebraicGeometry.Space.smooth_precoverage_le_fpqc`, and the postcomposition hypothesis is
> composition of morphisms locally of finite type (Stacks 03XG) applied to the fact that a smooth
> morphism is locally of finite type (Stacks 06MH).

```lean
theorem isSmoothLocalOnSourceAndTarget_locallyOfFiniteType :
    IsSmoothLocalOnSourceAndTarget B S hS
      (fun _ _ f => IsLocallyOfFiniteType B S hS f)
```

**`AlgebraicGeometry.Space.isSmoothLocalOnSourceAndTarget_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalityFiniteness.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothLocalityFiniteness.lean#L178). The attribute's comment: “locally\_of\_finite\_presentation”.

> **Stacks 06FC**, the locally-of-finite-presentation case. Being locally of finite
> presentation for morphisms of algebraic spaces over `S` is smooth local on the
> source-and-target.
>
> The source locality hypothesis of Stacks 06FB is
> `AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isLocalAtSource_smooth`; the target
> locality one comes from the fpqc statement of Stacks 041T along
> `AlgebraicGeometry.Space.smooth_precoverage_le_fpqc`, and the postcomposition hypothesis is
> composition of morphisms locally of finite presentation (Stacks 03XQ) applied to the fact that a
> smooth morphism is locally of finite presentation (Stacks 04AJ).

```lean
theorem isSmoothLocalOnSourceAndTarget_locallyOfFinitePresentation :
    IsSmoothLocalOnSourceAndTarget B S hS
      (fun _ _ f => IsLocallyOfFinitePresentation B S hS f)
```

**`AlgebraicGeometry.Space.isSmoothLocalOnSourceAndTarget_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothSourceLocalityTransfer.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothSourceLocalityTransfer.lean#L446). The attribute's comment: “smooth”.

> **Stacks 06FC**, the smooth case. Smoothness of morphisms of algebraic spaces over `S` is
> smooth local on the source-and-target.
>
> The source locality hypothesis of Stacks 06FB is Stacks 06F2; the target locality one comes from
> the fpqc one (Stacks 0429) along `AlgebraicGeometry.Space.smooth_precoverage_le_fpqc`, and the
> postcomposition hypothesis is composition of smooth morphisms (Stacks 03ZD).

```lean
theorem isSmoothLocalOnSourceAndTarget_smooth :
    IsSmoothLocalOnSourceAndTarget B S hS (fun _ _ f => IsSmooth B S hS f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.20, Tag 06F7](https://stacks.math.columbia.edu/tag/06F7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
