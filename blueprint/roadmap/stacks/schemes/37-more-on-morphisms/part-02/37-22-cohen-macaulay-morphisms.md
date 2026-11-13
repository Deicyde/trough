---
declaration: section
origin: cited
lean: AlgebraicGeometry.flat_of_isCohenMacaulay, AlgebraicGeometry.Scheme.Hom.IsCohenMacaulayAt, AlgebraicGeometry.Scheme.Hom.IsCohenMacaulay, AlgebraicGeometry.isCohenMacaulay_iff_flat_and_fibers, AlgebraicGeometry.topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber, AlgebraicGeometry.isCohenMacaulayAt_comp, AlgebraicGeometry.isCohenMacaulay_comp, AlgebraicGeometry.isCohenMacaulayAt_left_of_comp_of_flatAt
statement: formalized
proof: formalized
---

# 37.22 Cohen-Macaulay morphisms

Section 37.22 of the Stacks Project, [Tag 045Q](https://stacks.math.columbia.edu/tag/045Q). 11 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 045R, a definition

[Tag 045R](https://stacks.math.columbia.edu/tag/045R) in the Stacks Project.

**`AlgebraicGeometry.flat_of_isCohenMacaulay`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaximalSlice.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/MaximalSlice.lean#L379). The attribute's comment: “flatness of a Cohen-Macaulay morphism”.

> A Cohen--Macaulay morphism is flat: flatness of the stalk map at a point is the first
> conjunct of Cohen--Macaulayness there, and flatness of a morphism is flatness of every stalk
> map.

```lean
theorem flat_of_isCohenMacaulay {X Y : Scheme.{u}}
    (f : X ⟶ Y) (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hcm : Scheme.Hom.IsCohenMacaulay f hf) : Flat f
```

**`AlgebraicGeometry.Scheme.Hom.IsCohenMacaulayAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Defs.lean#L73). The attribute's comment: “part (1)”. References: EGA IV (6.8.1), “(ii)”; SGA 1 II (4.19).

> A morphism of schemes with locally Noetherian fibres is Cohen–Macaulay at `x` if it is flat
> at `x` and the local ring of the fibre over `f x` at the point corresponding to `x` is
> Cohen–Macaulay.

```lean
public abbrev IsCohenMacaulayAt {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x : X) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsCohenMacaulay`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Defs.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Defs.lean#L82). The attribute's comment: “part (2)”. References: EGA IV (6.8.1), “(ii), global”.

> A morphism of schemes with locally Noetherian fibres is Cohen–Macaulay if it is
> Cohen–Macaulay at every point of its source.

```lean
public abbrev IsCohenMacaulay {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) : Prop
```

## Tag 045S, a lemma

[Tag 045S](https://stacks.math.columbia.edu/tag/045S) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_iff_flat_and_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Fibres.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Fibres.lean#L59). References: EGA IV (19.2.9), “more general”.

> A morphism with locally Noetherian fibres is Cohen–Macaulay precisely when it is flat and
> every fibre is a Cohen–Macaulay scheme.

```lean
public theorem isCohenMacaulay_iff_flat_and_fibers {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) :
    Scheme.Hom.IsCohenMacaulay f hf ↔
      Flat f ∧ (∀ y : Y, IsCohenMacaulay (f.fiber y))
```

## Tag 0AFG, a lemma

[Tag 0AFG](https://stacks.math.columbia.edu/tag/0AFG) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayDimensionFormula.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/CohenMacaulayDimensionFormula.lean#L225).

> **Stacks Project, Tag 0AFG.** For a Cohen-Macaulay morphism locally of finite type between
> locally Noetherian schemes, the dimension of the source at a point is the dimension of the target
> at its image plus the dimension of the fibre at that point.

```lean
public theorem topologicalKrullDimAt_eq_add_topologicalKrullDimAt_fiber {X Y : Scheme.{u}}
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y] (f : X ⟶ Y) [LocallyOfFiniteType f]
    (hfib : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hcm : Scheme.Hom.IsCohenMacaulay f hfib) (x : X) :
    topologicalKrullDimAt X x =
      topologicalKrullDimAt Y (f x) +
        topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x)
```

## Tag 0C0W, a lemma

[Tag 0C0W](https://stacks.math.columbia.edu/tag/0C0W) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulayAt_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean#L338). The attribute's comment: “part (1)”. References: EGA IV (6.8.3), “(i), Cohen-Macaulay”; EGA IV (6.6.1), “a) of (i)”.

> The composite of morphisms Cohen–Macaulay at the relevant points is Cohen–Macaulay at the
> point of the source.

```lean
public theorem isCohenMacaulayAt_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hgf : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z)) (x : X)
    (hfx : Scheme.Hom.IsCohenMacaulayAt f hf x)
    (hgy : Scheme.Hom.IsCohenMacaulayAt g hg (f x)) :
    Scheme.Hom.IsCohenMacaulayAt (f ≫ g) hgf x
```

**`AlgebraicGeometry.isCohenMacaulay_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean#L352). The attribute's comment: “part (2)”.

> The composite of Cohen–Macaulay morphisms is Cohen–Macaulay.

```lean
public theorem isCohenMacaulay_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hgf : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z))
    (hfm : Scheme.Hom.IsCohenMacaulay f hf)
    (hgm : Scheme.Hom.IsCohenMacaulay g hg) :
    Scheme.Hom.IsCohenMacaulay (f ≫ g) hgf
```

**`AlgebraicGeometry.isCohenMacaulayAt_left_of_comp_of_flatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean#L364). The attribute's comment: “part (3), first conclusion”.

> If the composite is Cohen–Macaulay at `x` and `f` is flat at `x`, then `f` is Cohen–Macaulay
> at `x`.

```lean
public theorem isCohenMacaulayAt_left_of_comp_of_flatAt {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hgf : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z)) (x : X)
    (hcomp : Scheme.Hom.IsCohenMacaulayAt (f ≫ g) hgf x)
    (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    Scheme.Hom.IsCohenMacaulayAt f hf x
```

**`AlgebraicGeometry.isCohenMacaulayAt_right_of_comp_of_flatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean#L380). The attribute's comment: “part (3), second conclusion”.

> If the composite is Cohen–Macaulay at `x` and `f` is flat at `x`, then `g` is Cohen–Macaulay
> at `f x`.

```lean
public theorem isCohenMacaulayAt_right_of_comp_of_flatAt {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hgf : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z)) (x : X)
    (hcomp : Scheme.Hom.IsCohenMacaulayAt (f ≫ g) hgf x)
    (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    Scheme.Hom.IsCohenMacaulayAt g hg (f x)
```

**`AlgebraicGeometry.isCohenMacaulay_left_of_comp_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean#L395). The attribute's comment: “part (4), first conclusion”.

> If the composite is Cohen–Macaulay and `f` is flat, then `f` is Cohen–Macaulay.

```lean
public theorem isCohenMacaulay_left_of_comp_of_flat {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hgf : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z))
    (hcomp : Scheme.Hom.IsCohenMacaulay (f ≫ g) hgf)
    (hflat : Flat f) : Scheme.Hom.IsCohenMacaulay f hf
```

**`AlgebraicGeometry.isCohenMacaulayAt_right_of_comp_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Composition.lean#L408). The attribute's comment: “part (4), second conclusion”. References: EGA IV (6.6.1), “a) of (ii)”; EGA IV (6.8.3), “(ii), Cohen-Macaulay”.

> If the composite is Cohen–Macaulay and `f` is flat, then `g` is Cohen–Macaulay at every
> point in the image of `f`.

```lean
public theorem isCohenMacaulayAt_right_of_comp_of_flat {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hgf : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z))
    (hcomp : Scheme.Hom.IsCohenMacaulay (f ≫ g) hgf)
    (hflat : Flat f) (x : X) :
    Scheme.Hom.IsCohenMacaulayAt g hg (f x)
```

## Tag 0C0X, a lemma

[Tag 0C0X](https://stacks.math.columbia.edu/tag/0C0X) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulay_of_isCohenMacaulay_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FlatSource.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FlatSource.lean#L57). The attribute's comment: “the morphism is Cohen-Macaulay”.

> **Stacks Project, Tag 0C0X.** A flat morphism of locally Noetherian schemes whose source is
> Cohen–Macaulay is a Cohen–Macaulay morphism.

```lean
public theorem isCohenMacaulay_of_isCohenMacaulay_source {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Flat f]
    (hX : IsCohenMacaulay X) :
    f.IsCohenMacaulay (isLocallyNoetherian_fiber f)
```

**`AlgebraicGeometry.isCohenMacaulayLocalRing_targetStalk_of_isCohenMacaulay_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FlatSource.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FlatSource.lean#L99). The attribute's comment: “the target local rings are Cohen-Macaulay”. References: EGA IV (7.5.3), “(iii), special case”.

> **Stacks Project, Tag 0C0X.** For a flat morphism of locally Noetherian schemes whose source
> is Cohen–Macaulay, the local ring of the target at the image of any point of the source is
> Cohen–Macaulay.

```lean
public theorem isCohenMacaulayLocalRing_targetStalk_of_isCohenMacaulay_source {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsLocallyNoetherian X] [IsLocallyNoetherian Y] [Flat f]
    (hX : IsCohenMacaulay X) (x : X) :
    IsCohenMacaulayLocalRing (Y.presheaf.stalk (f x))
```

## Tag 045T, a lemma

[Tag 045T](https://stacks.math.columbia.edu/tag/045T) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulayAt_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/BaseChange.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/BaseChange.lean#L263). The attribute's comment: “part (1)”. References: EGA IV (6.8.3), “(iii) CM, h loc fin type”.

> **Stacks Project, Tag 045T (1).** Cohen–Macaulayness at a point is preserved under locally
> finite-type base change.

```lean
public theorem isCohenMacaulayAt_pullback {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x' : (pullback f g : Scheme))
    (h : Scheme.Hom.IsCohenMacaulayAt f hf ((pullback.fst f g).base x')) :
    Scheme.Hom.IsCohenMacaulayAt (pullback.snd f g)
      (fun y' => isLocallyNoetherian_fiber_pullback f g hf y') x'
```

**`AlgebraicGeometry.isCohenMacaulayAt_of_pullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/BaseChange.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/BaseChange.lean#L276). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 045T (2).** Cohen–Macaulayness descends from a base change when the
> original morphism is flat at the point in question.

```lean
public theorem isCohenMacaulayAt_of_pullback_of_flat {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x' : (pullback f g : Scheme))
    (hflat : IsFlatAt f.toLRSHom.toShHom ((pullback.fst f g).base x'))
    (h : Scheme.Hom.IsCohenMacaulayAt (pullback.snd f g)
      (fun y' => isLocallyNoetherian_fiber_pullback f g hf y') x') :
    Scheme.Hom.IsCohenMacaulayAt f hf ((pullback.fst f g).base x')
```

**`AlgebraicGeometry.isCohenMacaulayAt_of_pullback_of_flat_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/BaseChange.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/BaseChange.lean#L289). The attribute's comment: “part (3)”. References: EGA IV (6.8.3), “(iii) converse, CM”.

> **Stacks Project, Tag 045T (3).** Cohen–Macaulayness descends from a base change flat at the
> relevant base point.

```lean
public theorem isCohenMacaulayAt_of_pullback_of_flat_base {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x' : (pullback f g : Scheme))
    (hflat : IsFlatAt g.toLRSHom.toShHom ((pullback.snd f g).base x'))
    (h : Scheme.Hom.IsCohenMacaulayAt (pullback.snd f g)
      (fun y' => isLocallyNoetherian_fiber_pullback f g hf y') x') :
    Scheme.Hom.IsCohenMacaulayAt f hf ((pullback.fst f g).base x')
```

## Tag 045U, a lemma

[Tag 045U](https://stacks.math.columbia.edu/tag/045U) in the Stacks Project.

**`AlgebraicGeometry.isCohenMacaulayAt_set_eq_fiberLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Locus.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Locus.lean#L47). The attribute's comment: “fibre\_local\_ring\_characterization”.

> The Cohen–Macaulay locus of a flat, locally finitely presented morphism is exactly the locus
> where the local ring of its fibre is Cohen–Macaulay.

```lean
public theorem isCohenMacaulayAt_set_eq_fiberLocalRing
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f] :
    let hf : ∀ y : S, IsLocallyNoetherian (f.fiber y) := fun y =>
      isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f y
    {x : X | Scheme.Hom.IsCohenMacaulayAt f hf x} =
      {x : X | letI := hf (f x)
        IsCohenMacaulayLocalRing ((f.fiber (f x)).presheaf.stalk (f.asFiber x))}
```

**`AlgebraicGeometry.dense_cohenMacaulayAt_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Locus.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/Locus.lean#L122). The attribute's comment: “cm\_locus\_fibrewise\_dense”. References: SGA 4 XVIII (2.3), “fibrewise density”.

> The Cohen–Macaulay locus of a flat, locally finitely presented morphism is dense in every
> fibre.

```lean
public theorem dense_cohenMacaulayAt_fiber
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f] :
    let hf : ∀ s : S, IsLocallyNoetherian (f.fiber s) := fun s =>
      isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f s
    ∀ s : S, Dense ((f.fiberι s) ⁻¹' {x : X | Scheme.Hom.IsCohenMacaulayAt f hf x})
```

**`AlgebraicGeometry.isCohenMacaulayAt_pullback_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/LocusBaseChange.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/LocusBaseChange.lean#L267). The attribute's comment: “cm\_locus\_base\_change”. References: EGA IV (6.8.2), “(ii), special case”.

> **Stacks Project, Tag 045U (base change).** The Cohen–Macaulay locus of a flat, locally
> finitely presented morphism commutes with arbitrary base change.

```lean
public theorem isCohenMacaulayAt_pullback_locus {X S S' : Scheme.{u}}
    (f : X ⟶ S) (g : S' ⟶ S) [Flat f] [LocallyOfFinitePresentation f] :
    let f' := pullback.snd f g
    let g' := pullback.fst f g
    let hf : ∀ s : S, IsLocallyNoetherian (f.fiber s) := fun s =>
      isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f s
    let hf' : ∀ s' : S', IsLocallyNoetherian (f'.fiber s') := fun s' =>
      isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f' s'
    {x' : (pullback f g : Scheme) | Scheme.Hom.IsCohenMacaulayAt f' hf' x'} =
      g'.base ⁻¹' {x : X | Scheme.Hom.IsCohenMacaulayAt f hf x}
```

**`AlgebraicGeometry.isOpen_setOf_isCohenMacaulayAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/LocusOpen.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/LocusOpen.lean#L151). The attribute's comment: “cm\_locus\_open”. References: EGA IV (12.1.7), “(iii), flat case”; EGA IV (6.11.3), “special case”.

> **Stacks Project, Tag 045U (Cohen–Macaulay locus).** For a flat morphism locally of finite
> presentation, the locus of points at which the morphism is Cohen–Macaulay is open.

```lean
public theorem isOpen_setOf_isCohenMacaulayAt
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f] :
    let hf : ∀ y : S, IsLocallyNoetherian (f.fiber y) := fun y =>
      isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f y
    IsOpen {x : X | Scheme.Hom.IsCohenMacaulayAt f hf x}
```

## Tag 0BUU, a lemma

[Tag 0BUU](https://stacks.math.columbia.edu/tag/0BUU) in the Stacks Project.

**`AlgebraicGeometry.exists_nat_topologicalKrullDimAt_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/AffineSpaceCriterion.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/AffineSpaceCriterion.lean#L863). The attribute's comment: “finiteness of the fibre dimension”.

> The local dimension of a fibre of a locally finitely presented morphism is finite.

```lean
public theorem exists_nat_topologicalKrullDimAt_fiber {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (x : X) :
    ∃ n : ℕ,
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (n : WithBot ℕ∞)
```

**`AlgebraicGeometry.isCohenMacaulayAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/AffineSpaceCriterion.lean, line 882](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/AffineSpaceCriterion.lean#L882). The attribute's comment: “the four equivalent conditions”. References: EGA IV (15.4.3), “F = O\_X, f flat”; SGA 4 XVIII (2.4).

> Let `f : X ⟶ S` be flat and locally of finite presentation and let `n` be the dimension of
> the fibre of `f` through `x` at `x`. Then `f` is Cohen–Macaulay at `x` if and only if some open
> neighbourhood of `x` carries a locally quasi-finite `S`-morphism to affine `n`-space over `S`
> that is flat at `x`, if and only if some open neighbourhood carries a locally quasi-finite flat
> such morphism, if and only if every `S`-morphism to affine `n`-space from an open neighbourhood
> of `x` that is quasi-finite at `x` is flat at `x`.

```lean
public theorem isCohenMacaulayAt_tfae {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f] (x : X) (n : ℕ)
    (hn : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (n : WithBot ℕ∞)) :
    List.TFAE [
      Scheme.Hom.IsCohenMacaulayAt f
        (fun s => isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f s) x,
      ∃ (U : X.Opens) (hx : x ∈ U.1)
          (g : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin n)) S),
        (g ≫ (AffineSpace (ULift.{u} (Fin n)) S ↘ S) = U.ι ≫ f) ∧
        (LocallyOfFiniteType g ∧ LocallyQuasiFinite g) ∧
        AlgebraicGeometry.IsFlatAt g.toLRSHom.toShHom ⟨x, hx⟩,
      ∃ (U : X.Opens) (_hx : x ∈ U.1)
          (g : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin n)) S),
        (g ≫ (AffineSpace (ULift.{u} (Fin n)) S ↘ S) = U.ι ≫ f) ∧
        (LocallyOfFiniteType g ∧ LocallyQuasiFinite g) ∧ Flat g,
      ∀ (U : X.Opens) (hx : x ∈ U.1)
          (g : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin n)) S),
        (g ≫ (AffineSpace (ULift.{u} (Fin n)) S ↘ S) = U.ι ≫ f) →
        (AlgebraicGeometry.quasiFiniteAt g ⟨x, hx⟩ →
          AlgebraicGeometry.IsFlatAt g.toLRSHom.toShHom ⟨x, hx⟩)]
```

## Tag 054T, a lemma

[Tag 054T](https://stacks.math.columbia.edu/tag/054T) in the Stacks Project.

**`AlgebraicGeometry.exists_open_relativeDimension_fiberwise_dense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FibrewiseDenseRelativeDimension.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FibrewiseDenseRelativeDimension.lean#L188).

> **Stacks Project, Tag 054T.** A flat morphism locally of finite presentation admits open
> pieces of every nonnegative relative dimension whose union is dense in every fibre.

```lean
public theorem exists_open_relativeDimension_fiberwise_dense
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f] :
    ∃ U : ℕ → X.Opens,
      (∀ s : S, Dense ((f.fiberι s) ⁻¹' (((iSup U : X.Opens) : Set X)))) ∧
        (∀ d : ℕ, RelativeDimension ((U d).ι ≫ f) d)
```

## Tag 054U, a lemma

[Tag 054U](https://stacks.math.columbia.edu/tag/054U) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_fiber_eq_of_specialization_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FibreDimensionSpecialization.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FibreDimensionSpecialization.lean#L52). References: EGA IV (12.2.1.1), “partial”.

> **Stacks Project, Tag 054U.** For a flat morphism locally of finite presentation, local
> dimension in the fibres is constant along a specialization whose endpoint is generic in an
> irreducible component of its fibre.

```lean
public theorem topologicalKrullDimAt_fiber_eq_of_specialization_of_mem_genericPoints
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    {x' x : X} (hxx : x' ⤳ x)
    (hx : f.asFiber x ∈ genericPoints (f.fiber (f x))) :
    topologicalKrullDimAt (f.fiber (f x')) (f.asFiber x') =
      topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x)
```

## Tag 045V, a lemma

[Tag 045V](https://stacks.math.columbia.edu/tag/045V) in the Stacks Project.

**`AlgebraicGeometry.cohenMacaulayWithLocallyNoetherianFibers_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FppfLocalTarget.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FppfLocalTarget.lean#L186). The attribute's comment: “fppf local on the target”.

> **Stacks Project, Tag 045V.** Having locally Noetherian fibres and being Cohen–Macaulay is
> local on the target for the fppf topology.

```lean
public instance cohenMacaulayWithLocallyNoetherianFibers_isLocalAtTarget_fppf :
    (cohenMacaulayWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtTarget
      Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.cohenMacaulayWithLocallyNoetherianFibers_isLocalAtSource_syntomic`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FppfLocalTarget.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FppfLocalTarget.lean#L256). The attribute's comment: “syntomic local on the source”.

> **Stacks Project, Tag 045V.** Having locally Noetherian fibres and being Cohen–Macaulay is
> local on the source for the syntomic topology.

```lean
public instance cohenMacaulayWithLocallyNoetherianFibers_isLocalAtSource_syntomic :
    (cohenMacaulayWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtSource
      (Scheme.precoverage (@Syntomic : MorphismProperty Scheme.{u}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.22, Tag 045Q](https://stacks.math.columbia.edu/tag/045Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
