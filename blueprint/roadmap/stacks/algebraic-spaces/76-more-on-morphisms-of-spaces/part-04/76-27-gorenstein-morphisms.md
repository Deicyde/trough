---
declaration: section
origin: cited
lean: AlgebraicGeometry.hasGorensteinFiberLocalRing_isEtaleLocalOnSourceAndTarget, AlgebraicGeometry.Space.IsGorensteinAt, AlgebraicGeometry.Space.IsGorenstein, AlgebraicGeometry.Space.isGorenstein_tfae_etaleCharts, AlgebraicGeometry.Space.isGorensteinAt_iff_etaleLocalRingMap, AlgebraicGeometry.Space.isGorensteinAt_comp, AlgebraicGeometry.Space.isGorenstein_comp, AlgebraicGeometry.Space.isGorensteinAt_left_of_comp_of_isFlatAt
statement: formalized
proof: formalized
---

# 76.27 Gorenstein morphisms

Section 76.27 of the Stacks Project, [Tag 0E12](https://stacks.math.columbia.edu/tag/0E12). 7 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E13, a lemma

[Tag 0E13](https://stacks.math.columbia.edu/tag/0E13) in the Stacks Project.

**`AlgebraicGeometry.hasGorensteinFiberLocalRing_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/GorensteinFiber.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/GorensteinFiber.lean#L455).

> **Stacks Project, Tag 0E13.** Having a Noetherian and Gorenstein
> local ring of the fibre is étale local on the source and target germs.

```lean
public theorem hasGorensteinFiberLocalRing_isEtaleLocalOnSourceAndTarget :
    MorphismOfGerms.IsEtaleLocalOnSourceAndTarget
      (@HasGorensteinFiberLocalRing.{u})
```

## Tag 0E14, a definition

[Tag 0E14](https://stacks.math.columbia.edu/tag/0E14) in the Stacks Project.

**`AlgebraicGeometry.Space.IsGorensteinAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Defs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Defs.lean#L53). The attribute's comment: “part (1): at a point”.

> **Stacks 0E14, part (1).** A morphism of algebraic spaces over `S` is *Gorenstein at* a
> point `x` of its source when it is flat at `x` and the local ring of its fibre is Noetherian
> and Gorenstein in every pointed étale scheme chart at `x`.

```lean
abbrev IsGorensteinAt (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.IsGorenstein`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Defs.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Defs.lean#L61). The attribute's comment: “part (2): morphism”.

> **Stacks 0E14, part (2).** A morphism of algebraic spaces over `S` is *Gorenstein* when
> it is Gorenstein at every point of its source.

```lean
abbrev IsGorenstein (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 0E15, a lemma

[Tag 0E15](https://stacks.math.columbia.edu/tag/0E15) in the Stacks Project.

**`AlgebraicGeometry.Space.isGorenstein_tfae_etaleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/EtaleCharts.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/EtaleCharts.lean#L216). The attribute's comment: “global\_gorenstein\_equivalence”.

> **Stacks 0E15.** For a morphism of algebraic spaces over `S` with locally Noetherian fibres,
> Gorensteinness is equivalent to flatness together with Gorensteinness of the fibres after some,
> equivalently after every, étale scheme chart of the target.

```lean
theorem isGorenstein_tfae_etaleCharts (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : HasLocallyNoetherianFibers B S hS f) :
    List.TFAE [
      IsGorenstein B S hS f,
      IsFlat B S hS f ∧
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          (MorphismProperty.presheaf (MorphismProperty.inverseImage
            (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS))) g ∧
          IsEtale B S hS g ∧ HasGorensteinFibersOnChart B S hS f V g,
      IsFlat B S hS f ∧
        ∀ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsEtale B S hS g → HasGorensteinFibersOnChart B S hS f V g]
```

**`AlgebraicGeometry.Space.isGorensteinAt_iff_etaleLocalRingMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/EtaleLocalRings.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/EtaleLocalRings.lean#L238). The attribute's comment: “etale\_local\_ring\_criterion”.

> **Stacks 0E15.** A morphism of algebraic spaces over `S` is Gorenstein at the image of a
> geometric point `x` of its source exactly when the canonical homomorphism of étale local rings
> at `x` is flat and its local fibre ring is Noetherian, local and Gorenstein.

```lean
theorem isGorensteinAt_iff_etaleLocalRingMap (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (x : GeometricPoint B S hS X) :
    IsGorensteinAt B S hS f x.image ↔
      ((etaleLocalRingMap hX f x).Flat ∧
        ∃ (hN : IsNoetherianRing
            (etaleLocalRing B S hS X x ⧸ etaleLocalFiberIdeal B S hS hX hY f x))
          (hL : IsLocalRing
            (etaleLocalRing B S hS X x ⧸ etaleLocalFiberIdeal B S hS hX hY f x)),
          @Dualizing.IsGorensteinLocalRing
            (etaleLocalRing B S hS X x ⧸ etaleLocalFiberIdeal B S hS hX hY f x) _ hN hL)
```

## Tag 0E16, a lemma

[Tag 0E16](https://stacks.math.columbia.edu/tag/0E16) in the Stacks Project.

**`AlgebraicGeometry.Space.isGorensteinAt_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean#L90). The attribute's comment: “part (1)”.

> **Stacks 0E16, part (1).** The composite of two morphisms of algebraic spaces with locally
> Noetherian fibres is Gorenstein at a point of its source as soon as the first is Gorenstein
> there and the second is Gorenstein at the image of that point.

```lean
theorem isGorensteinAt_comp
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (x : points B S hS X) (hfx : IsGorensteinAt B S hS f x)
    (hgy : IsGorensteinAt B S hS g (pointsMap B S hS X f x)) :
    IsGorensteinAt B S hS (f ≫ g) x
```

**`AlgebraicGeometry.Space.isGorenstein_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean#L111). The attribute's comment: “part (2)”.

> **Stacks 0E16, part (2).** The composite of two Gorenstein morphisms of algebraic spaces
> with locally Noetherian fibres is Gorenstein.

```lean
theorem isGorenstein_comp
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (hfm : IsGorenstein B S hS f) (hgm : IsGorenstein B S hS g) :
    IsGorenstein B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isGorensteinAt_left_of_comp_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean#L150). The attribute's comment: “part (3), first conclusion”.

> **Stacks 0E16, part (3), first conclusion.** If the composite is Gorenstein at `x` and the
> first morphism is flat at `x`, then the first morphism is Gorenstein at `x`.

```lean
theorem isGorensteinAt_left_of_comp_of_isFlatAt
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (x : points B S hS X) (hcomp : IsGorensteinAt B S hS (f ≫ g) x)
    (hflat : IsFlatAt B S hS f x) : IsGorensteinAt B S hS f x
```

**`AlgebraicGeometry.Space.isGorensteinAt_right_of_comp_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean#L164). The attribute's comment: “part (3), second conclusion”.

> **Stacks 0E16, part (3), second conclusion.** If the composite is Gorenstein at `x` and the
> first morphism is flat at `x`, then the second morphism is Gorenstein at the image of `x`.

```lean
theorem isGorensteinAt_right_of_comp_of_isFlatAt
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (x : points B S hS X) (hcomp : IsGorensteinAt B S hS (f ≫ g) x)
    (hflat : IsFlatAt B S hS f x) :
    IsGorensteinAt B S hS g (pointsMap B S hS X f x)
```

**`AlgebraicGeometry.Space.isGorenstein_left_of_comp_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean#L179). The attribute's comment: “part (4), first conclusion”.

> **Stacks 0E16, part (4), first conclusion.** If the composite is Gorenstein and the first
> morphism is flat, then the first morphism is Gorenstein.

```lean
theorem isGorenstein_left_of_comp_of_isFlat
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (hcomp : IsGorenstein B S hS (f ≫ g)) (hflat : IsFlat B S hS f) :
    IsGorenstein B S hS f
```

**`AlgebraicGeometry.Space.isGorensteinAt_right_of_comp_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Composition.lean#L195). The attribute's comment: “part (4), second conclusion”.

> **Stacks 0E16, part (4), second conclusion.** If the composite is Gorenstein and the first
> morphism is flat, then the second morphism is Gorenstein at every point in the image of the
> first.

```lean
theorem isGorensteinAt_right_of_comp_of_isFlat
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : HasLocallyNoetherianFibersAtPoints B S hS g)
    (hgf : HasLocallyNoetherianFibersAtPoints B S hS (f ≫ g))
    (hcomp : IsGorenstein B S hS (f ≫ g)) (hflat : IsFlat B S hS f)
    (x : points B S hS X) :
    IsGorensteinAt B S hS g (pointsMap B S hS X f x)
```

## Tag 0E17, a lemma

[Tag 0E17](https://stacks.math.columbia.edu/tag/0E17) in the Stacks Project.

**`AlgebraicGeometry.Space.isGorenstein_of_isGorenstein_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/FlatSource.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/FlatSource.lean#L161). The attribute's comment: “the morphism is Gorenstein”.

> **Stacks 0E17.** A flat morphism of locally Noetherian algebraic spaces over `S` whose
> source is a Gorenstein algebraic space is a Gorenstein morphism.

```lean
theorem isGorenstein_of_isGorenstein_source (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hNX : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hNY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hG : HasEtaleLocalProperty B S hS X
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsGorenstein T))
    (f : X ⟶ Y) (hf : IsFlat B S hS f) :
    IsGorenstein B S hS f
```

**`AlgebraicGeometry.Space.isGorensteinLocalRing_etaleLocalRing_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/FlatSource.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/FlatSource.lean#L199). The attribute's comment: “the target étale local rings are Gorenstein”.

> **Stacks 0E17.** For a flat morphism of locally Noetherian algebraic spaces over `S` whose
> source is a Gorenstein algebraic space, the étale local ring of the target at the image of any
> geometric point of the source is Gorenstein.

```lean
theorem isGorensteinLocalRing_etaleLocalRing_target (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hNX : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hNY : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hG : HasEtaleLocalProperty B S hS X
      (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsGorenstein T))
    (f : X ⟶ Y) (hf : IsFlat B S hS f) (x : GeometricPoint B S hS X) :
    letI : IsLocalRing (etaleLocalRing B S hS Y (geometricPointMap f x)) :=
      isLocalRing_etaleLocalRing B S hS Y hY (geometricPointMap f x)
    letI : IsNoetherianRing (etaleLocalRing B S hS Y (geometricPointMap f x)) :=
      isNoetherianRing_etaleLocalRing_of_isLocallyNoetherian B S hS Y hY hNY
        (geometricPointMap f x)
    Dualizing.IsGorensteinLocalRing (etaleLocalRing B S hS Y (geometricPointMap f x))
```

## Tag 0E18, a lemma

[Tag 0E18](https://stacks.math.columbia.edu/tag/0E18) in the Stacks Project.

**`AlgebraicGeometry.Space.isGorensteinAt_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/BaseChange.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/BaseChange.lean#L227). The attribute's comment: “part (1)”.

> **Stacks 0E18, part (1).** Gorensteinness of a morphism of algebraic spaces with locally
> Noetherian fibres at a point is preserved by base change along a morphism locally of finite
> type.

```lean
theorem isGorensteinAt_pullback_snd
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) (x' : points B S hS (pullback f g))
    (hgor : IsGorensteinAt B S hS f
      (pointsMap B S hS (pullback f g) (pullback.fst f g) x')) :
    IsGorensteinAt B S hS (pullback.snd f g) x'
```

**`AlgebraicGeometry.Space.isGorensteinAt_of_pullback_snd_of_isFlatAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/BaseChange.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/BaseChange.lean#L245). The attribute's comment: “part (2)”.

> **Stacks 0E18, part (2).** Gorensteinness descends from the base change when the original
> morphism is flat at the point in question.

```lean
theorem isGorensteinAt_of_pullback_snd_of_isFlatAt
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) (x' : points B S hS (pullback f g))
    (hflat : IsFlatAt B S hS f (pointsMap B S hS (pullback f g) (pullback.fst f g) x'))
    (hgor : IsGorensteinAt B S hS (pullback.snd f g) x') :
    IsGorensteinAt B S hS f
      (pointsMap B S hS (pullback f g) (pullback.fst f g) x')
```

**`AlgebraicGeometry.Space.isGorensteinAt_of_pullback_snd_of_isFlatAt_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/BaseChange.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/BaseChange.lean#L268). The attribute's comment: “part (3)”.

> **Stacks 0E18, part (3).** Gorensteinness descends from the base change when the base
> morphism is flat at the corresponding point.

```lean
theorem isGorensteinAt_of_pullback_snd_of_isFlatAt_base
    {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hY' : IsAlgebraicSpace B S hS Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hf : HasLocallyNoetherianFibersAtPoints B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) (x' : points B S hS (pullback f g))
    (hflat : IsFlatAt B S hS g (pointsMap B S hS (pullback f g) (pullback.snd f g) x'))
    (hgor : IsGorensteinAt B S hS (pullback.snd f g) x') :
    IsGorensteinAt B S hS f
      (pointsMap B S hS (pullback f g) (pullback.fst f g) x')
```

## Tag 0E19, a lemma

[Tag 0E19](https://stacks.math.columbia.edu/tag/0E19) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_setOf_isGorensteinAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Locus.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Locus.lean#L110). The attribute's comment: “openness of the Gorenstein locus”.

> **Stacks 0E19.** The Gorenstein locus of a flat morphism of algebraic spaces over `S` which
> is locally of finite presentation is open in the canonical topology of Tag 03BX on the point
> space of its source.

```lean
theorem isOpen_setOf_isGorensteinAt {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf_flat : IsFlat B S hS f) (hf_lfp : IsLocallyOfFinitePresentation B S hS f) :
    IsOpen {x : points B S hS X | IsGorensteinAt B S hS f x}
```

**`AlgebraicGeometry.Space.isGorensteinAt_pullback_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Locus.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Gorenstein/Locus.lean#L148). The attribute's comment: “base change of the Gorenstein locus”.

> **Stacks 0E19.** The Gorenstein locus of a flat morphism of algebraic spaces over `S` which
> is locally of finite presentation commutes with arbitrary base change: the locus of the base
> change `X ×_Y Y' ⟶ Y'` is the inverse image of the locus of `f : X ⟶ Y` under the projection
> to `X`.

```lean
theorem isGorensteinAt_pullback_locus {X Y Y' : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (g : Y' ⟶ Y) (hf_flat : IsFlat B S hS f.hom)
    (hf_lfp : IsLocallyOfFinitePresentation B S hS f.hom) :
    {x' : points B S hS (pullback f.hom g.hom) |
        IsGorensteinAt B S hS (pullback.snd f.hom g.hom) x'} =
      pointsMap B S hS (pullback f.hom g.hom) (pullback.fst f.hom g.hom) ⁻¹'
        {x : points B S hS X.1 | IsGorensteinAt B S hS f.hom x}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.27, Tag 0E12](https://stacks.math.columbia.edu/tag/0E12)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
