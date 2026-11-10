---
declaration: section
origin: cited
lean: AlgebraicGeometry.hasCohenMacaulayFiberLocalRing_isEtaleLocalOnSourceAndTarget, AlgebraicGeometry.Space.IsCohenMacaulayAt, AlgebraicGeometry.Space.IsCohenMacaulay, AlgebraicGeometry.Space.HasCohenMacaulayFibersOnChart, AlgebraicGeometry.Space.isCohenMacaulay_tfae_etaleCharts, AlgebraicGeometry.Space.isCohenMacaulayAt_iff_etaleLocalRingMap, AlgebraicGeometry.Space.isCohenMacaulayAt_comp, AlgebraicGeometry.Space.isCohenMacaulay_comp
statement: formalized
proof: formalized
---

# 76.26 Cohen-Macaulay morphisms

Section 76.26 of the Stacks Project, [Tag 0E0T](https://stacks.math.columbia.edu/tag/0E0T). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E0U, a lemma

[Tag 0E0U](https://stacks.math.columbia.edu/tag/0E0U) in the Stacks Project.

**`AlgebraicGeometry.hasCohenMacaulayFiberLocalRing_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/CohenMacaulayFiber.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germs/CohenMacaulayFiber.lean#L434).

> Having a Noetherian and Cohen–Macaulay local ring of the fibre is étale local on the source
> and target germs.

```lean
public theorem hasCohenMacaulayFiberLocalRing_isEtaleLocalOnSourceAndTarget :
    MorphismOfGerms.IsEtaleLocalOnSourceAndTarget
      (@HasCohenMacaulayFiberLocalRing.{u})
```

## Tag 0E0V, a definition

[Tag 0E0V](https://stacks.math.columbia.edu/tag/0E0V) in the Stacks Project.

**`AlgebraicGeometry.Space.IsCohenMacaulayAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Defs.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Defs.lean#L38). The attribute's comment: “part (1): at a point”.

> A morphism of algebraic spaces over `S` is *Cohen–Macaulay at* a point `x` of its source
> when it is flat at `x` and the local ring of its fibre is Noetherian and Cohen–Macaulay in every
> pointed étale scheme chart at `x`.

```lean
abbrev IsCohenMacaulayAt (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.IsCohenMacaulay`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Defs.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Defs.lean#L46). The attribute's comment: “part (2): morphism”.

> A morphism of algebraic spaces over `S` is *Cohen–Macaulay* when it is Cohen–Macaulay at
> every point of its source.

```lean
abbrev IsCohenMacaulay (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 0E0W, a lemma

[Tag 0E0W](https://stacks.math.columbia.edu/tag/0E0W) in the Stacks Project.

**`AlgebraicGeometry.Space.HasCohenMacaulayFibersOnChart`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/EtaleCharts.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/EtaleCharts.lean#L186). The attribute's comment: “the fibre condition on an étale scheme chart of the target”.

> **Stacks 0E0W.** The fibres of `f` over the points of the étale scheme chart
> `g : h_V ⟶ Y` are Cohen–Macaulay algebraic spaces.

```lean
abbrev HasCohenMacaulayFibersOnChart {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.isCohenMacaulay_tfae_etaleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/EtaleCharts.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/EtaleCharts.lean#L471). The attribute's comment: “equivalence of conditions (1), (2) and (3)”.

> **Stacks 0E0W.** For a morphism of algebraic spaces over `S` with locally Noetherian
> fibres, Cohen–Macaulayness is equivalent to flatness together with Cohen–Macaulayness of the
> fibres after some, equivalently after every, étale scheme chart of the target.

```lean
theorem isCohenMacaulay_tfae_etaleCharts (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : HasLocallyNoetherianFibers B S hS f) :
    List.TFAE [
      IsCohenMacaulay B S hS f,
      IsFlat B S hS f ∧
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          (MorphismProperty.presheaf (MorphismProperty.inverseImage
            (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS))) g ∧
          IsEtale B S hS g ∧ HasCohenMacaulayFibersOnChart B S hS f V g,
      IsFlat B S hS f ∧
        ∀ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsEtale B S hS g → HasCohenMacaulayFibersOnChart B S hS f V g]
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_iff_etaleLocalRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/EtaleCharts.lean, line 926](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/EtaleCharts.lean#L926). The attribute's comment: “equivalence of conditions (a) and (b)”.

> **Stacks 0E0W.** A morphism of algebraic spaces over `S` is Cohen–Macaulay at the image of
> a geometric point `x` of its source exactly when the canonical homomorphism of étale local
> rings at `x` is flat and its local fibre ring is Noetherian, local and Cohen–Macaulay.

```lean
theorem isCohenMacaulayAt_iff_etaleLocalRingMap (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (x : GeometricPoint B S hS X) :
    IsCohenMacaulayAt B S hS f x.image ↔
      ((etaleLocalRingMap hX f x).Flat ∧
        ∃ (hN : IsNoetherianRing
            (etaleLocalRing B S hS X x ⧸ etaleLocalFiberIdeal B S hS hX hY f x))
          (hL : IsLocalRing
            (etaleLocalRing B S hS X x ⧸ etaleLocalFiberIdeal B S hS hX hY f x)),
          @IsCohenMacaulayLocalRing
            (etaleLocalRing B S hS X x ⧸ etaleLocalFiberIdeal B S hS hX hY f x) _ hN hL)
```

## Tag 0E0X, a lemma

[Tag 0E0X](https://stacks.math.columbia.edu/tag/0E0X) in the Stacks Project.

**`AlgebraicGeometry.Space.isCohenMacaulayAt_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean#L85). The attribute's comment: “part (1)”. References: EGA IV (6.6.1), “a) of (i)”; EGA IV (6.8.3), “(i), Cohen-Macaulay”.

> **Stacks 0E0X, part (1).** The composite of two morphisms of algebraic spaces with
> locally Noetherian fibres is Cohen–Macaulay at a point of its source as soon as the first
> is Cohen–Macaulay there and the second is Cohen–Macaulay at the image of that point.

```lean
theorem isCohenMacaulayAt_comp
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (x : points B S hS X) (hfx : IsCohenMacaulayAt B S hS f x)
    (hgy : IsCohenMacaulayAt B S hS g (pointsMap B S hS X f x)) :
    IsCohenMacaulayAt B S hS (f ≫ g) x
```

**`AlgebraicGeometry.Space.isCohenMacaulay_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean#L106). The attribute's comment: “part (2)”.

> **Stacks 0E0X, part (2).** The composite of two Cohen–Macaulay morphisms of algebraic
> spaces with locally Noetherian fibres is Cohen–Macaulay.

```lean
theorem isCohenMacaulay_comp
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (hfm : IsCohenMacaulay B S hS f) (hgm : IsCohenMacaulay B S hS g) :
    IsCohenMacaulay B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_left_of_comp_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean#L146). The attribute's comment: “part (3), first conclusion”.

> **Stacks 0E0X, part (3), first conclusion.** If the composite is Cohen–Macaulay at `x`
> and the first morphism is flat at `x`, then the first morphism is Cohen–Macaulay at `x`.

```lean
theorem isCohenMacaulayAt_left_of_comp_of_isFlatAt
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (x : points B S hS X) (hcomp : IsCohenMacaulayAt B S hS (f ≫ g) x)
    (hflat : IsFlatAt B S hS f x) : IsCohenMacaulayAt B S hS f x
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_right_of_comp_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean#L160). The attribute's comment: “part (3), second conclusion”.

> **Stacks 0E0X, part (3), second conclusion.** If the composite is Cohen–Macaulay at `x`
> and the first morphism is flat at `x`, then the second morphism is Cohen–Macaulay at the
> image of `x`.

```lean
theorem isCohenMacaulayAt_right_of_comp_of_isFlatAt
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (x : points B S hS X) (hcomp : IsCohenMacaulayAt B S hS (f ≫ g) x)
    (hflat : IsFlatAt B S hS f x) :
    IsCohenMacaulayAt B S hS g (pointsMap B S hS X f x)
```

**`AlgebraicGeometry.Space.isCohenMacaulay_left_of_comp_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean#L174). The attribute's comment: “part (4), first conclusion”.

> **Stacks 0E0X, part (4), first conclusion.** If the composite is Cohen–Macaulay and the
> first morphism is flat, then the first morphism is Cohen–Macaulay.

```lean
theorem isCohenMacaulay_left_of_comp_of_isFlat
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (hcomp : IsCohenMacaulay B S hS (f ≫ g)) (hflat : IsFlat B S hS f) :
    IsCohenMacaulay B S hS f
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_right_of_comp_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/Composition.lean#L191). The attribute's comment: “part (4), second conclusion”. References: EGA IV (6.6.1), “a) of (ii)”; EGA IV (6.8.3), “(ii), Cohen-Macaulay”.

> **Stacks 0E0X, part (4), second conclusion.** If the composite is Cohen–Macaulay and the
> first morphism is flat, then the second morphism is Cohen–Macaulay at every point in the image
> of the first.

```lean
theorem isCohenMacaulayAt_right_of_comp_of_isFlat
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (hcomp : IsCohenMacaulay B S hS (f ≫ g)) (hflat : IsFlat B S hS f)
    (x : points B S hS X) :
    IsCohenMacaulayAt B S hS g (pointsMap B S hS X f x)
```

## Tag 0E0Y, a lemma

[Tag 0E0Y](https://stacks.math.columbia.edu/tag/0E0Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isCohenMacaulay_of_isCohenMacaulay_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Source.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Source.lean#L212). The attribute's comment: “the morphism is Cohen-Macaulay”.

> **Stacks 0E0Y.** A flat morphism of locally Noetherian algebraic spaces over `S` whose
> source is a Cohen–Macaulay algebraic space is a Cohen–Macaulay morphism.

```lean
theorem isCohenMacaulay_of_isCohenMacaulay_source (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hNX : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hNY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hCM : HasEtaleLocalProperty B S hS X
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsCohenMacaulay T))
    (f : X ⟶ Y) (hf : IsFlat B S hS f) :
    IsCohenMacaulay B S hS f
```

**`AlgebraicGeometry.Space.isCohenMacaulayLocalRing_etaleLocalRing_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Source.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Source.lean#L385). The attribute's comment: “the target étale local rings are Cohen-Macaulay”.

> **Stacks 0E0Y.** For a flat morphism of locally Noetherian algebraic spaces over `S` whose
> source is a Cohen–Macaulay algebraic space, the étale local ring of the target at the image of
> any geometric point of the source is Cohen–Macaulay.

```lean
theorem isCohenMacaulayLocalRing_etaleLocalRing_target (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hNX : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hNY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hCM : HasEtaleLocalProperty B S hS X
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsCohenMacaulay T))
    (f : X ⟶ Y) (hf : IsFlat B S hS f) (x : GeometricPoint B S hS X) :
    letI : IsLocalRing (etaleLocalRing B S hS Y (geometricPointMap f x)) :=
      isLocalRing_etaleLocalRing B S hS Y hY (geometricPointMap f x)
    letI : IsNoetherianRing (etaleLocalRing B S hS Y (geometricPointMap f x)) :=
      isNoetherianRing_etaleLocalRing_of_isLocallyNoetherian B S hS Y hY hNY
        (geometricPointMap f x)
    IsCohenMacaulayLocalRing (etaleLocalRing B S hS Y (geometricPointMap f x))
```

## Tag 0E0Z, a lemma

[Tag 0E0Z](https://stacks.math.columbia.edu/tag/0E0Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isCohenMacaulayAt_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/BaseChange.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/BaseChange.lean#L209). The attribute's comment: “part (1)”. References: EGA IV (6.8.3), “(iii) CM, h loc fin type”.

> **Stacks 0E0Z, part (1).** Cohen–Macaulayness of a morphism of algebraic spaces with
> locally Noetherian fibres at a point is preserved by base change along a morphism locally of
> finite type.

```lean
theorem isCohenMacaulayAt_pullback_snd
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) (x' : points B S hS (pullback f g))
    (hcm : IsCohenMacaulayAt B S hS f
      (pointsMap B S hS (pullback f g) (pullback.fst f g) x')) :
    IsCohenMacaulayAt B S hS (pullback.snd f g) x'
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_of_pullback_snd_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/BaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/BaseChange.lean#L227). The attribute's comment: “part (2)”.

> **Stacks 0E0Z, part (2).** Cohen–Macaulayness descends from the base change when the
> original morphism is flat at the point in question.

```lean
theorem isCohenMacaulayAt_of_pullback_snd_of_isFlatAt
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) (x' : points B S hS (pullback f g))
    (hflat : IsFlatAt B S hS f (pointsMap B S hS (pullback f g) (pullback.fst f g) x'))
    (hcm : IsCohenMacaulayAt B S hS (pullback.snd f g) x') :
    IsCohenMacaulayAt B S hS f
      (pointsMap B S hS (pullback f g) (pullback.fst f g) x')
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_of_pullback_snd_of_isFlatAt_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/BaseChange.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulay/BaseChange.lean#L251). The attribute's comment: “part (3)”. References: EGA IV (6.8.3), “(iii) converse, CM”.

> **Stacks 0E0Z, part (3).** Cohen–Macaulayness descends from the base change when the base
> morphism is flat at the corresponding point.

```lean
theorem isCohenMacaulayAt_of_pullback_snd_of_isFlatAt_base
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) (x' : points B S hS (pullback f g))
    (hflat : IsFlatAt B S hS g (pointsMap B S hS (pullback f g) (pullback.snd f g) x'))
    (hcm : IsCohenMacaulayAt B S hS (pullback.snd f g) x') :
    IsCohenMacaulayAt B S hS f
      (pointsMap B S hS (pullback f g) (pullback.fst f g) x')
```

## Tag 0E10, a lemma

[Tag 0E10](https://stacks.math.columbia.edu/tag/0E10) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_setOf_isCohenMacaulayAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Locus.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Locus.lean#L136). The attribute's comment: “openness of the Cohen–Macaulay locus”. References: EGA IV (12.1.1), “(vi), F = O_X”.

> **Stacks 0E10.** The Cohen–Macaulay locus of a flat morphism of algebraic spaces over `S`
> which is locally of finite presentation is open in the canonical topology of Tag 03BX on the
> point space of its source.

```lean
theorem isOpen_setOf_isCohenMacaulayAt {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf_flat : IsFlat B S hS f) (hf_lfp : IsLocallyOfFinitePresentation B S hS f) :
    IsOpen {x : points B S hS X | IsCohenMacaulayAt B S hS f x}
```

**`AlgebraicGeometry.Space.isCohenMacaulayAt_pullback_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Locus.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/Locus.lean#L165). The attribute's comment: “base change of the Cohen–Macaulay locus”. References: EGA IV (6.8.2), “(ii)”.

> **Stacks 0E10.** The Cohen–Macaulay locus of a flat morphism of algebraic spaces over `S`
> which is locally of finite presentation commutes with arbitrary base change: the locus of the
> base change `X ×_Y Y' ⟶ Y'` is the inverse image of the locus of `f : X ⟶ Y` under the
> projection to `X`.

```lean
theorem isCohenMacaulayAt_pullback_locus {X Y Y' : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y' ⟶ Y) (hf_flat : IsFlat B S hS f.hom)
    (hf_lfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    {x' : points B S hS (pullback f.hom g.hom) |
        IsCohenMacaulayAt B S hS (pullback.snd f.hom g.hom) x'} =
      pointsMap B S hS (pullback f.hom g.hom) (pullback.fst f.hom g.hom) ⁻¹'
        {x : points B S hS X.1 | IsCohenMacaulayAt B S hS f.hom x}
```

## Tag 0E11, a lemma

[Tag 0E11](https://stacks.math.columbia.edu/tag/0E11) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_clopen_relativeDimension_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/RelativeDimensionDecomposition.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CohenMacaulay/RelativeDimensionDecomposition.lean#L278).

> **Stacks 0E11.** A locally finitely presented Cohen–Macaulay morphism of algebraic spaces
> over `S` decomposes its source into open-and-closed subspaces of constant relative dimension:
> there is a family `Xd : ℕ → Subfunctor X` of subfunctors which are both open and closed
> subspaces of `X` in the sense of Tag 02YU, whose point sets cover the point space of `X` and are
> pairwise disjoint, and such that the restriction of `f` to the `d`-th piece has relative
> dimension `d`.
>
> The pieces are given by their point sets rather than by a supremum of subfunctors: the ranges of
> their inclusions are subpresheaves, so a section over a test object which the decomposition
> splits into several pieces lies in no single piece before refinement.

```lean
theorem exists_clopen_relativeDimension_decomposition (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hfp : IsLocallyOfFinitePresentation B S hS f) (hCM : IsCohenMacaulay B S hS f) :
    ∃ Xd : ℕ → Subfunctor X,
      (∀ d : ℕ, IsOpenSubspace B S hS (Xd d) ∧ IsClosedSubspace B S hS (Xd d)) ∧
      (∀ x : points B S hS X, ∃ d : ℕ,
        x ∈ Set.range (pointsMap B S hS (Xd d).toFunctor (Xd d).ι)) ∧
      Pairwise (Disjoint on fun d : ℕ =>
        Set.range (pointsMap B S hS (Xd d).toFunctor (Xd d).ι)) ∧
      (∀ d : ℕ, HasRelativeDimension d B S hS ((Xd d).ι ≫ f))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.26, Tag 0E0T](https://stacks.math.columbia.edu/tag/0E0T)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
