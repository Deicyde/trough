---
declaration: section
origin: cited
lean: AlgebraicGeometry.isGorensteinLocalRing_stalk_iff_of_essFiniteType_fieldExtension, AlgebraicGeometry.isGorensteinLocalRing_stalk_iff_of_locallyOfFiniteType, AlgebraicGeometry.Scheme.Hom.IsGorensteinAt, AlgebraicGeometry.Scheme.Hom.IsGorenstein, AlgebraicGeometry.Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber, AlgebraicGeometry.Scheme.Hom.isCohenMacaulay_of_isGorenstein, AlgebraicGeometry.isGorenstein_of_syntomic, AlgebraicGeometry.isGorenstein_of_flat_of_isLocalCompleteIntersectionMorphism
statement: formalized
proof: formalized
---

# 48.25 Gorenstein morphisms

Section 48.25 of the Stacks Project, [Tag 0C02](https://stacks.math.columbia.edu/tag/0C02). 12 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C03, a lemma

[Tag 0C03](https://stacks.math.columbia.edu/tag/0C03) in the Stacks Project.

**`AlgebraicGeometry.isGorensteinLocalRing_stalk_iff_of_essFiniteType_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/FieldExtension.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/FieldExtension.lean#L306). The attribute's comment: “finitely generated field extension”.

> **Stacks Project, Tag 0C03.** Gorensteinness of local rings is unchanged after a finitely
> generated extension of the ground field of a locally Noetherian scheme.

```lean
public theorem isGorensteinLocalRing_stalk_iff_of_essFiniteType_fieldExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K] [Algebra.EssFiniteType k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsLocallyNoetherian X] (x : X)
    (x' : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hx' : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base x' = x) :
    letI : IsLocallyNoetherian
        (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}) :=
      (AlgebraicGeometry.isLocallyNoetherian_baseChange_iff k K X f).mp inferInstance
    Dualizing.IsGorensteinLocalRing (X.presheaf.stalk x) ↔
      Dualizing.IsGorensteinLocalRing
        ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk
          x')
```

**`AlgebraicGeometry.isGorensteinLocalRing_stalk_iff_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/FieldExtension.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinSchemes/FieldExtension.lean#L389). The attribute's comment: “arbitrary field extension for a locally finite type scheme”.

> **Stacks Project, Tag 0C03.** Gorensteinness of local rings is unchanged after an arbitrary
> extension of the ground field when the scheme is locally of finite type over that field.

```lean
public theorem isGorensteinLocalRing_stalk_iff_of_locallyOfFiniteType
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] (x : X)
    (x' : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hx' : (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base x' = x) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    Dualizing.IsGorensteinLocalRing (X.presheaf.stalk x) ↔
      Dualizing.IsGorensteinLocalRing
        ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk
          x')
```

## Tag 0C04, a definition

[Tag 0C04](https://stacks.math.columbia.edu/tag/0C04) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsGorensteinAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Basic.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Basic.lean#L38). The attribute's comment: “part (1)”.

> A scheme morphism with locally Noetherian fibres is Gorenstein at `x` if it
> is flat at `x` and the local ring of the fibre over `f x` is Gorenstein.

```lean
public abbrev IsGorensteinAt {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x : X) : Prop
```

**`AlgebraicGeometry.Scheme.Hom.IsGorenstein`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Basic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Basic.lean#L48). The attribute's comment: “part (2)”.

> A scheme morphism with locally Noetherian fibres is Gorenstein when it is
> Gorenstein at every point of the source.

```lean
public abbrev IsGorenstein {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) : Prop
```

## Tag 0C05, a lemma

[Tag 0C05](https://stacks.math.columbia.edu/tag/0C05) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isGorenstein_iff_flat_and_isGorenstein_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Fibres.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Fibres.lean#L70).

> A morphism of schemes with locally Noetherian fibres is Gorenstein if and only if it is flat
> and all of its fibres are Gorenstein schemes.

```lean
public theorem isGorenstein_iff_flat_and_isGorenstein_fiber
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) :
    IsGorenstein f hf ↔ Flat f ∧ ∀ y : Y, AlgebraicGeometry.IsGorenstein (f.fiber y)
```

## Tag 0C06, a lemma

[Tag 0C06](https://stacks.math.columbia.edu/tag/0C06) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isCohenMacaulay_of_isGorenstein`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/CohenMacaulay.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/CohenMacaulay.lean#L46).

> **Stacks Project, Tag 0C06.** A Gorenstein morphism is Cohen--Macaulay.

```lean
public theorem isCohenMacaulay_of_isGorenstein
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (h : IsGorenstein f hf) :
    IsCohenMacaulay f hf
```

## Tag 0C15, a lemma

[Tag 0C15](https://stacks.math.columbia.edu/tag/0C15) in the Stacks Project.

**`AlgebraicGeometry.isGorenstein_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Syntomic.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Syntomic.lean#L110). The attribute's comment: “a syntomic morphism is Gorenstein”.

> **Stacks 0C15.** A syntomic morphism of schemes is a Gorenstein morphism.

```lean
public theorem isGorenstein_of_syntomic {X S : Scheme.{u}} (f : X ⟶ S) (hf : Syntomic f) :
    f.IsGorenstein (isLocallyNoetherian_fiber_of_syntomic hf)
```

**`AlgebraicGeometry.isGorenstein_of_flat_of_isLocalCompleteIntersectionMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Syntomic.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Syntomic.lean#L120). The attribute's comment: “a flat local complete intersection morphism is Gorenstein”.

> **Stacks 0C15.** A flat local complete intersection morphism of schemes is a Gorenstein
> morphism; this is the second formulation of the lemma, equivalent to the first by Stacks
> 069K.

```lean
public theorem isGorenstein_of_flat_of_isLocalCompleteIntersectionMorphism {X S : Scheme.{u}}
    (f : X ⟶ S) (hflat : Flat f) (hlci : IsLocalCompleteIntersectionMorphism f) :
    f.IsGorenstein (isLocallyNoetherian_fiber_of_syntomic
      (syntomic_of_flat_of_isLocalCompleteIntersectionMorphism hflat hlci))
```

**`AlgebraicGeometry.syntomic_le_gorensteinWithLocallyNoetherianFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/SyntomicMorphismProperty.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/SyntomicMorphismProperty.lean#L62). The attribute's comment: “a syntomic morphism is Gorenstein, as an inclusion of morphism properties”.

> **Stacks 0C15.** A syntomic morphism of schemes is a Gorenstein morphism: the syntomic
> morphisms are contained in the morphism property of having locally Noetherian fibres and being
> Gorenstein.

```lean
public theorem syntomic_le_gorensteinWithLocallyNoetherianFibers :
    (@Syntomic : MorphismProperty Scheme.{u}) ≤ gorensteinWithLocallyNoetherianFibers
```

**`AlgebraicGeometry.flat_inf_lci_le_gorensteinWithLocallyNoetherianFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/SyntomicMorphismProperty.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/SyntomicMorphismProperty.lean#L71). The attribute's comment: “a flat lci morphism is Gorenstein, as an inclusion of morphism properties”.

> **Stacks 0C15.** A flat local complete intersection morphism of schemes is a Gorenstein
> morphism: the meet of flatness and being a local complete intersection morphism is contained in
> the morphism property of having locally Noetherian fibres and being Gorenstein. This is the second
> formulation of the lemma, equivalent to the first by Stacks 069K.

```lean
public theorem flat_inf_lci_le_gorensteinWithLocallyNoetherianFibers :
    (@Flat ⊓ @IsLocalCompleteIntersectionMorphism : MorphismProperty Scheme.{u}) ≤
      gorensteinWithLocallyNoetherianFibers
```

## Tag 0C11, a lemma

[Tag 0C11](https://stacks.math.columbia.edu/tag/0C11) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean#L208). The attribute's comment: “part (1)”.

> Gorensteinness at a point is preserved by composition.

```lean
public theorem isGorensteinAt_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hfg : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z)) (x : X)
    (hfx : IsGorensteinAt f hf x) (hgy : IsGorensteinAt g hg (f x)) :
    IsGorensteinAt (f ≫ g) hfg x
```

**`AlgebraicGeometry.Scheme.Hom.isGorenstein_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean#L218). The attribute's comment: “part (2)”.

> The composite of Gorenstein morphisms is Gorenstein.

```lean
public theorem isGorenstein_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hfg : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z))
    (hF : IsGorenstein f hf) (hG : IsGorenstein g hg) :
    IsGorenstein (f ≫ g) hfg
```

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean#L229). The attribute's comment: “part (3), first morphism”.

> If a composite is Gorenstein at a point and the first map is flat there, then the first map is
> Gorenstein at that point.

```lean
public theorem isGorensteinAt_left_of_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hfg : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z)) (x : X)
    (hcomp : IsGorensteinAt (f ≫ g) hfg x)
    (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    IsGorensteinAt f hf x
```

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_right_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean#L241). The attribute's comment: “part (3), second morphism”.

> If a composite is Gorenstein at a point and the first map is flat there, then the second map is
> Gorenstein at the image point.

```lean
public theorem isGorensteinAt_right_of_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hfg : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z)) (x : X)
    (hcomp : IsGorensteinAt (f ≫ g) hfg x)
    (hflat : IsFlatAt f.toLRSHom.toShHom x) :
    IsGorensteinAt g hg (f x)
```

**`AlgebraicGeometry.Scheme.Hom.isGorenstein_left_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean#L252). The attribute's comment: “part (4), first morphism”.

> If the composite is Gorenstein and the first map is flat, the first map is Gorenstein.

```lean
public theorem isGorenstein_left_of_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hfg : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z))
    (hcomp : IsGorenstein (f ≫ g) hfg) (hflat : Flat f) :
    IsGorenstein f hf
```

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_image_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Composition.lean#L263). The attribute's comment: “part (4), second morphism on the image”.

> If the composite is Gorenstein and the first map is flat, the second map is Gorenstein at each
> point in the image of the first.

```lean
public theorem isGorensteinAt_image_of_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hg : ∀ z : Z, IsLocallyNoetherian (g.fiber z))
    (hfg : ∀ z : Z, IsLocallyNoetherian ((f ≫ g).fiber z))
    (hcomp : IsGorenstein (f ≫ g) hfg) (hflat : Flat f) (x : X) :
    IsGorensteinAt g hg (f x)
```

## Tag 0C12, a lemma

[Tag 0C12](https://stacks.math.columbia.edu/tag/0C12) in the Stacks Project.

**`Stacks.Duality.isGorensteinLocalRing_stalk_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Dualizing.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/Dualizing.lean#L135). The attribute's comment: “Gorenstein local rings of the base”.

> **Stacks Project, Tag 0C12.** The local ring of the base at any point in the image of a flat
> morphism of locally Noetherian schemes with Gorenstein source is Gorenstein.
>
> The map of local rings `𝒪_{Y, f x} → 𝒪_{X, x}` induced by a flat morphism is a flat local
> homomorphism of Noetherian local rings, so `isGorensteinLocalRing_of_flat` applies.

```lean
theorem isGorensteinLocalRing_stalk_of_flat {X Y : Scheme.{u}} (f : X ⟶ Y)
    [AlgebraicGeometry.IsGorenstein X] [IsLocallyNoetherian Y] [Flat f] (x : X) :
    Dualizing.IsGorensteinLocalRing (Y.presheaf.stalk (f x))
```

**`Stacks.Duality.isGorenstein_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphismOfFlat.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphismOfFlat.lean#L85). The attribute's comment: “Gorenstein morphism”.

> **Stacks Project, Tag 0C12.** A flat morphism of locally Noetherian schemes with Gorenstein
> source is a Gorenstein morphism.
>
> The local Noetherianity of the fibres that `Scheme.Hom.IsGorenstein` requires is supplied here
> rather than assumed: it follows from local Noetherianity of the source.

```lean
theorem isGorenstein_of_flat {X Y : Scheme.{u}} (f : X ⟶ Y)
    [AlgebraicGeometry.IsGorenstein X] [IsLocallyNoetherian Y] [Flat f] :
    ∃ hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y),
      AlgebraicGeometry.Scheme.Hom.IsGorenstein f hf
```

## Tag 0C07, a lemma

[Tag 0C07](https://stacks.math.columbia.edu/tag/0C07) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean#L298). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0C07 (1).** Gorensteinness at a point is preserved under a base change
> locally of finite type.

```lean
public theorem isGorensteinAt_pullback {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x' : (pullback f g : Scheme.{u}))
    (h : IsGorensteinAt f hf ((pullback.fst f g).base x')) :
    IsGorensteinAt (pullback.snd f g)
      (fun y' => isLocallyNoetherian_fiber_pullback f g hf y') x'
```

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_of_pullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean#L320). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0C07 (2).** Gorensteinness descends from a base change locally of
> finite type when the original morphism is flat at the point in question.

```lean
public theorem isGorensteinAt_of_pullback_of_flat {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x' : (pullback f g : Scheme.{u}))
    (hflat : IsFlatAt f.toLRSHom.toShHom ((pullback.fst f g).base x'))
    (h : IsGorensteinAt (pullback.snd f g)
      (fun y' => isLocallyNoetherian_fiber_pullback f g hf y') x') :
    IsGorensteinAt f hf ((pullback.fst f g).base x')
```

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_of_pullback_of_flat_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean#L342). The attribute's comment: “part (3)”.

> **Stacks Project, Tag 0C07 (3).** Gorensteinness descends from a base change locally of
> finite type that is flat at the image of the point in the new base.

```lean
public theorem isGorensteinAt_of_pullback_of_flat_base {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [LocallyOfFiniteType g]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) (x' : (pullback f g : Scheme.{u}))
    (hflat : IsFlatAt g.toLRSHom.toShHom ((pullback.snd f g).base x'))
    (h : IsGorensteinAt (pullback.snd f g)
      (fun y' => isLocallyNoetherian_fiber_pullback f g hf y') x') :
    IsGorensteinAt f hf ((pullback.fst f g).base x')
```

## Tag 0E0Q, a lemma

[Tag 0E0Q](https://stacks.math.columbia.edu/tag/0E0Q) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.setOf_isGorensteinAt_pullback_eq_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChange.lean#L457).

> **Stacks Project, Tag 0E0Q.** Let `f : X ⟶ Y` be flat and locally of finite type, and let
> `g : Y' ⟶ Y` be an arbitrary morphism. Then the set of points of `X ×_Y Y'` at which the base
> change of `f` along `g` is Gorenstein is the inverse image, under the projection to `X`, of the
> set of points of `X` at which `f` is Gorenstein; that is, formation of the Gorenstein locus of
> `f` commutes with arbitrary base change.

```lean
public theorem setOf_isGorensteinAt_pullback_eq_preimage {X Y Y' : Scheme.{u}}
    (f : X ⟶ Y) (g : Y' ⟶ Y) [Flat f] [LocallyOfFiniteType f]
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y))
    (hf' : ∀ y' : Y', IsLocallyNoetherian ((pullback.snd f g).fiber y')) :
    {x' : (pullback f g : Scheme.{u}) | IsGorensteinAt (pullback.snd f g) hf' x'} =
      (pullback.fst f g).base ⁻¹' {x : X | IsGorensteinAt f hf x}
```

**`AlgebraicGeometry.Scheme.Hom.setOf_isGorensteinAt_pullback_eq_preimage_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChangeLocus.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/BaseChangeLocus.lean#L55).

> Let `f : X ⟶ Y` be flat and locally of finite type and let `g : Y' ⟶ Y` be an arbitrary
> morphism of schemes. Then the set of points of `X ×_Y Y'` at which the base change of `f` along
> `g` is Gorenstein is the inverse image, under the projection to `X`, of the set of points of `X`
> at which `f` is Gorenstein: formation of the Gorenstein locus of `f` commutes with arbitrary base
> change. The locally Noetherian fibres that the Gorenstein-at-a-point predicate needs as data are
> theorems here, so nothing is assumed beyond flatness of `f` and its being locally of finite
> type.

```lean
public theorem setOf_isGorensteinAt_pullback_eq_preimage_of_locallyOfFiniteType
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y) [Flat f] [LocallyOfFiniteType f] :
    {x' : (pullback f g : Scheme.{u}) |
        IsGorensteinAt (pullback.snd f g)
          (fun y' => LocallyOfFiniteType.isLocallyNoetherian
            ((pullback.snd f g).fiberToSpecResidueField y')) x'} =
      (pullback.fst f g).base ⁻¹'
        {x : X |
          IsGorensteinAt f
            (fun y => LocallyOfFiniteType.isLocallyNoetherian
              (f.fiberToSpecResidueField y)) x}
```

## Tag 0C08, a lemma

[Tag 0C08](https://stacks.math.columbia.edu/tag/0C08) in the Stacks Project.

**`Stacks.Duality.isGorensteinAt_iff_isGorensteinFiberStalkAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/FibreStalkCriterion.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/FibreStalkCriterion.lean#L52). The attribute's comment: “proof chain (1) ↔ (2); (2)↔…↔(6) needs 0A9Y, 0BZZ, 0BFQ invertibility”.

> **Stacks Project, Tag 0C08**, the first equivalence of its proof. A flat morphism with
> locally Noetherian fibres is Gorenstein at a point exactly when the local ring of its fibre
> through that point is Gorenstein.

```lean
theorem isGorensteinAt_iff_isGorensteinFiberStalkAt (f : X ⟶ Y)
    (hf : ∀ y : Y, IsLocallyNoetherian (f.fiber y)) [Flat f] (x : X) :
    f.IsGorensteinAt hf x ↔ IsGorensteinFiberStalkAt f hf x
```

**`Stacks.Duality.isGorensteinAt_iff_exists_isInvertible_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekChartConsequences.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekChartConsequences.lean#L54).

> Let `S` be Noetherian, `f : X ⟶ Y` a flat morphism of `FTS S` and `x ∈ X`. Then `f` is
> Gorenstein at `x` if and only if `f^!𝒪_Y` is isomorphic to an invertible object in a
> neighbourhood of `x`. In particular the set of points where `f` is Gorenstein is open in `X`.
> Here `f^!` is computed at any compactification `j`.

```lean
theorem isGorensteinAt_iff_exists_isInvertible_upperShriek [Flat f.left] :
    (∀ x : X.left, f.left.IsGorensteinAt (isLocallyNoetherian_fiber_left f) x ↔
      ∃ W : X.left.Opens, x ∈ W ∧
        letI := Scheme.Modules.derivedMonoidal W.toScheme
        MonoidalCategory.IsInvertible
          ((Scheme.Modules.restrictFunctor W.ι).mapDerivedCategory.obj
            (relativeDualizingComplexObj f j))) ∧
      IsOpen {x : X.left | f.left.IsGorensteinAt (isLocallyNoetherian_fiber_left f) x}
```

## Tag 0C09, a lemma

[Tag 0C09](https://stacks.math.columbia.edu/tag/0C09) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isGorensteinAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/AffineSpace.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/AffineSpace.lean#L72). The attribute's comment: “the equivalence of (1), (2), (3) and (4)”.

> **Stacks Project, Tag 0C09.** Let `f : X ⟶ S` be flat and locally of finite presentation,
> let `x ∈ X` and let `d = dim_x(X_{f x})`. The following are equivalent:
> 1. `f` is Gorenstein at `x`;
> 2. there are an open neighbourhood `U` of `x` and a locally quasi-finite morphism
>    `U ⟶ 𝔸ᵈ_S` over `S` which is Gorenstein at `x`;
> 3. there are an open neighbourhood `U` of `x` and a locally quasi-finite Gorenstein morphism
>    `U ⟶ 𝔸ᵈ_S` over `S`;
> 4. every `S`-morphism `g : U ⟶ 𝔸ᵈ_S` from an open neighbourhood `U` of `x` which is
>    quasi-finite at `x` is Gorenstein at `x`.

```lean
theorem isGorensteinAt_tfae {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (x : X) (d : ℕ)
    (hd : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞)) :
    List.TFAE [
      f.IsGorensteinAt (isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f) x,
      ∃ (U : X.Opens) (hx : x ∈ U) (g : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin d)) S)
          (hg : g ≫ (AffineSpace (ULift.{u} (Fin d)) S ↘ S) = U.ι ≫ f),
        (LocallyOfFiniteType g ∧ LocallyQuasiFinite g) ∧
          g.IsGorensteinAt (isLocallyNoetherian_fiber_of_comp_eq hg) ⟨x, hx⟩,
      ∃ (U : X.Opens) (_ : x ∈ U) (g : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin d)) S)
          (hg : g ≫ (AffineSpace (ULift.{u} (Fin d)) S ↘ S) = U.ι ≫ f),
        (LocallyOfFiniteType g ∧ LocallyQuasiFinite g) ∧
          g.IsGorenstein (isLocallyNoetherian_fiber_of_comp_eq hg),
      ∀ (U : X.Opens) (hx : x ∈ U) (g : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin d)) S)
          (hg : g ≫ (AffineSpace (ULift.{u} (Fin d)) S ↘ S) = U.ι ≫ f),
        AlgebraicGeometry.quasiFiniteAt g ⟨x, hx⟩ →
          g.IsGorensteinAt (isLocallyNoetherian_fiber_of_comp_eq hg) ⟨x, hx⟩]
```

**`AlgebraicGeometry.Scheme.Hom.isOpen_setOf_isGorensteinAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/OpenLocus.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/OpenLocus.lean#L279). The attribute's comment: “the set of points where f is Gorenstein is open in X”.

> **Stacks Project, Tag 0C09, last assertion.** For a flat morphism of schemes `f : X ⟶ S`
> locally of finite presentation, the set of points of `X` at which `f` is Gorenstein is open.

```lean
theorem isOpen_setOf_isGorensteinAt {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] :
    IsOpen {x : X | IsGorensteinAt f
      (isLocallyNoetherian_fiber_of_locallyOfFinitePresentation f) x}
```

## Tag 0C0A, a lemma

[Tag 0C0A](https://stacks.math.columbia.edu/tag/0C0A) in the Stacks Project.

**`AlgebraicGeometry.gorensteinWithLocallyNoetherianFibers_isLocalAtTarget_fppf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Locality.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Locality.lean#L130). The attribute's comment: “local in the fppf topology on the target”.

> **Stacks Project, Tag 0C0A.** Having locally Noetherian fibres and being Gorenstein is local
> on the target for the fppf topology.

```lean
public instance gorensteinWithLocallyNoetherianFibers_isLocalAtTarget_fppf :
    (gorensteinWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtTarget
      Scheme.fppfPrecoverage
```

**`AlgebraicGeometry.gorensteinWithLocallyNoetherianFibers_isLocalAtSource_syntomic`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Locality.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/GorensteinMorphisms/Locality.lean#L188). The attribute's comment: “local in the syntomic topology on the source”.

> **Stacks Project, Tag 0C0A.** Having locally Noetherian fibres and being Gorenstein is local
> on the source for the syntomic topology.

```lean
public instance gorensteinWithLocallyNoetherianFibers_isLocalAtSource_syntomic :
    (gorensteinWithLocallyNoetherianFibers : MorphismProperty Scheme.{u}).IsLocalAtSource
      (Scheme.precoverage (@Syntomic : MorphismProperty Scheme.{u}))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.25, Tag 0C02](https://stacks.math.columbia.edu/tag/0C02)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
