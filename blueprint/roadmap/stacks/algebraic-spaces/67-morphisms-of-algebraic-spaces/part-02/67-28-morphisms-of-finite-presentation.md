---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsLocallyOfFinitePresentation, AlgebraicGeometry.Space.IsFinitePresentationAt, AlgebraicGeometry.Space.IsFinitePresentation, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_comp, AlgebraicGeometry.Space.isFinitePresentation_comp, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isStableUnderBaseChange, AlgebraicGeometry.Space.isFinitePresentation_isStableUnderBaseChange, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_tfae
statement: formalized
proof: formalized
---

# 67.28 Morphisms of finite presentation

Section 67.28 of the Stacks Project, [Tag 03XO](https://stacks.math.columbia.edu/tag/03XO). 12 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03XP, a definition

[Tag 03XP](https://stacks.math.columbia.edu/tag/03XP) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocallyOfFinitePresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean#L91). The attribute's comment: “part (1): locally of finite presentation”.

> **Stacks 03XP, part (1).** A morphism of algebraic spaces over `S` is *locally of
> finite presentation* when every commuting square of étale scheme charts induces a scheme
> morphism which is locally of finite presentation.

```lean
abbrev IsLocallyOfFinitePresentation (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsFinitePresentationAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean#L105). The attribute's comment: “part (2): finite presentation at a point”.

> **Stacks 03XP, part (2).** A morphism of algebraic spaces over `S` is *of finite
> presentation at* a point `x` of its source when it is locally of finite presentation on an
> open subspace of the source containing `x`.
>
> Ten predicates of this library share this signature, among them
> `AlgebraicGeometry.Space.IsFiniteTypeAt` and `AlgebraicGeometry.Space.IsSmoothAt`: each applies
> the same "holds on an open subspace through `x`" schema to a different property of morphisms of
> schemes, and each is a different part of a different tag of the source. The shape is shared, the
> content is not.

```lean
abbrev IsFinitePresentationAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

**`AlgebraicGeometry.Space.IsFinitePresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation.lean#L115). The attribute's comment: “part (3): finite presentation”.

> **Stacks 03XP, part (3).** A morphism of algebraic spaces over `S` is *of finite
> presentation* when it is locally of finite presentation, quasi-compact and
> quasi-separated.

```lean
abbrev IsFinitePresentation (f : X ⟶ Y) : Prop
```

## Tag 03XQ, a lemma

[Tag 03XQ](https://stacks.math.columbia.edu/tag/03XQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartComposition.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartComposition.lean#L161). The attribute's comment: “locally of finite presentation”.

> **Stacks 03XQ**, the case of being locally of finite presentation: the composite of two
> morphisms of algebraic spaces over `S` which are locally of finite presentation is locally of
> finite presentation.
>
> Being locally of finite presentation is étale local on the source and target (Stacks 04R3) and
> stable under composition (Stacks 01TR), so this is an instance of Stacks 0AML.

```lean
theorem isLocallyOfFinitePresentation_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsLocallyOfFinitePresentation B S hS f)
    (hg : IsLocallyOfFinitePresentation B S hS g) :
    IsLocallyOfFinitePresentation B S hS (f ≫ g)
```

**`AlgebraicGeometry.Space.isFinitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationComposition.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationComposition.lean#L54). The attribute's comment: “finite presentation”.

> **Stacks 03XQ**, the case of being of finite presentation: the composite of two morphisms
> of algebraic spaces over `S` which are of finite presentation is of finite presentation.
>
> Finite presentation is local finite presentation together with quasi-compactness and
> quasi-separatedness, and each of the three is stable under composition.

```lean
theorem isFinitePresentation_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hf : IsFinitePresentation B S hS f)
    (hg : IsFinitePresentation B S hS g) :
    IsFinitePresentation B S hS (f ≫ g)
```

## Tag 03XR, a lemma

[Tag 03XR](https://stacks.math.columbia.edu/tag/03XR) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoveringComparison.lean#L118). The attribute's comment: “locally of finite presentation”.

> **Stacks 03XR**, the case of being locally of finite presentation: that property of
> morphisms of algebraic spaces over `S` is stable under base change.
>
> Being locally of finite presentation is étale local on the source and target (Stacks 04R3) and
> stable under base change, so this is the instance of Stacks 0AMM at that property.

```lean
theorem isLocallyOfFinitePresentation_isStableUnderBaseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsLocallyOfFinitePresentation B S hS f.hom)
```

**`AlgebraicGeometry.Space.isFinitePresentation_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationBaseChange.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationBaseChange.lean#L83). The attribute's comment: “finite presentation”. References: SGA 1 VIII (3.6), “more general”.

> Being of finite presentation is a property of morphisms of algebraic spaces over `S` that is
> stable under base change.

```lean
instance isFinitePresentation_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsFinitePresentation B S hS f.hom)
```

## Tag 0410, a lemma

[Tag 0410](https://stacks.math.columbia.edu/tag/0410) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L342).

> **Stacks 0410.** Nine criteria for a morphism of algebraic spaces over `S` to be locally
> of finite presentation: pointwise finite presentation, local finite presentation of every base
> change to a scheme or to an affine scheme or to one surjective étale chart of the target, local
> finite presentation of the composite with one surjective étale chart of the source, local
> finite presentation of the morphism of schemes in every — or in one surjective — commuting
> square of étale charts, or over a pair of Zariski coverings.
>
> Local finite presentation of morphisms of schemes is étale local on the source and target
> (Stacks 04R3), stable under composition and base change, and implied by étaleness, so this is
> the instance of `AlgebraicGeometry.Space.holdsOnEveryEtaleChart_tfae` at that property.

```lean
theorem isLocallyOfFinitePresentation_tfae
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      IsLocallyOfFinitePresentation B S hS f,
      ∀ x : points B S hS X, IsFinitePresentationAt B S hS f x,
      ∀ (W : BigFppfOver B S hS) (g : yoneda.obj W ⟶ Y),
        IsLocallyOfFinitePresentation B S hS (pullback.fst g f),
      ∀ (W : BigFppfOver B S hS) (g : yoneda.obj W ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj W) →
          IsLocallyOfFinitePresentation B S hS (pullback.fst g f),
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        IsSurjective B S hS g ∧ IsEtale B S hS g ∧
          IsLocallyOfFinitePresentation B S hS (pullback.fst g f),
      ∃ (U : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X),
        IsSurjective B S hS p ∧ IsEtale B S hS p ∧
          IsLocallyOfFinitePresentation B S hS (p ≫ f),
      ∀ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p → IsEtale B S hS q → p ≫ f = yoneda.map a ≫ q →
          IsLocallyOfFinitePresentation B S hS (yoneda.map a),
      ∃ (U V : BigFppfOver B S hS) (p : yoneda.obj U ⟶ X) (q : yoneda.obj V ⟶ Y) (a : U ⟶ V),
        IsEtale B S hS p ∧ IsEtale B S hS q ∧ IsSurjective B S hS p ∧
          p ≫ f = yoneda.map a ≫ q ∧ IsLocallyOfFinitePresentation B S hS (yoneda.map a),
      ∃ (I : Type u) (Yopen : I → Subfunctor Y) (J : I → Type u)
        (Xopen : ∀ i, J i → Subfunctor (pullback f (Yopen i).ι)),
        IsZariskiCover B S hS I Yopen ∧ (∀ i, IsZariskiCover B S hS (J i) (Xopen i)) ∧
          ∀ i j, IsLocallyOfFinitePresentation B S hS
            ((Xopen i j).ι ≫ pullback.snd f (Yopen i).ι)
    ]
```

## Tag 0464, a lemma

[Tag 0464](https://stacks.math.columbia.edu/tag/0464) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L105).

> **Stacks 0464**, first assertion. A morphism of algebraic spaces over `S` which is locally of
> finite presentation is locally of finite type.

```lean
theorem isLocallyOfFiniteType_of_isLocallyOfFinitePresentation
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsLocallyOfFinitePresentation B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

**`AlgebraicGeometry.Space.isFiniteType_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeProperties.lean#L116).

> **Stacks 0464**, second assertion. A morphism of algebraic spaces over `S` of finite
> presentation is of finite type.

```lean
theorem isFiniteType_of_isFinitePresentation
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G}
    (hf : IsFinitePresentation B S hS f) :
    IsFiniteType B S hS f
```

## Tag 04ZL, a lemma

[Tag 04ZL](https://stacks.math.columbia.edu/tag/04ZL) in the Stacks Project.

**`AlgebraicGeometry.Space.isNoetherian_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L206).

> **Stacks 04ZL.** A morphism of algebraic spaces over `S` of finite presentation whose
> target is Noetherian has Noetherian source.
>
> Noetherianity of an algebraic space (Stacks 03EA) is quasi-compactness, quasi-separatedness
> and local Noetherianity. The first two of the three are exactly Stacks 06G5 applied to the
> quasi-compact and quasi-separated target, and local Noetherianity of the source comes from
> Stacks 04ZK, the morphism being locally of finite type by Stacks 0464.

```lean
theorem isNoetherian_of_isFinitePresentation (hZ : B.Contains (⊤_ Scheme.{u})) (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsFinitePresentation B S hS f) (hYnoeth : IsNoetherian B S hS hZ Y) :
    IsNoetherian B S hS hZ X
```

## Tag 06G4, a lemma

[Tag 06G4](https://stacks.math.columbia.edu/tag/06G4) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L245). The attribute's comment: “part (1)”. References: SGA 3 VIA (2.5.4), “more general”.

> **Stacks 06G4, part (1).** A morphism of algebraic spaces over `S` which is locally of
> finite type and whose target is locally Noetherian is locally of finite presentation.
>
> The surjective étale atlas of the target witnessing its local Noetherianity lifts, by Stacks
> 02X1, to a surjective étale chart of the source together with a morphism of the site making
> the square commute. Local finite type of the morphism tests exactly such squares, so the
> underlying scheme morphism is locally of finite type with locally Noetherian target and hence
> locally of finite presentation; one surjective chart square suffices by Stacks 03MJ.

```lean
theorem isLocallyOfFinitePresentation_of_isLocallyOfFiniteType
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hN : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

**`AlgebraicGeometry.Space.isFinitePresentation_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L268). The attribute's comment: “part (2)”.

> **Stacks 06G4, part (2).** A morphism of algebraic spaces over `S` which is of finite type
> and quasi-separated and whose target is locally Noetherian is of finite presentation.
>
> Finite presentation is local finite presentation, quasi-compactness and quasi-separatedness
> (Stacks 03XP, part (3)) and finite type is local finite type together with quasi-compactness
> (Stacks 03XF, part (3)), so only the first conjunct has content and that is part (1).

```lean
theorem isFinitePresentation_of_isFiniteType
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hN : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hf : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    IsFinitePresentation B S hS f
```

## Tag 06G5, a lemma

[Tag 06G5](https://stacks.math.columbia.edu/tag/06G5) in the Stacks Project.

**`AlgebraicGeometry.Space.qcqs_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L187).

> **Stacks 06G5.** If `Y` is a quasi-compact and quasi-separated algebraic space over `S`
> and `X` is of finite presentation over `Y`, then `X` is quasi-compact and quasi-separated.
>
> The two conclusions are independent of each other and each comes from one conjunct of finite
> presentation (Stacks 03XP, part (3)): quasi-compactness of `X` from quasi-compactness of `f`,
> and quasi-separatedness of `X` from quasi-separatedness of `f`. As everywhere in this
> development, a quasi-compact and quasi-separated algebraic space is one which is quasi-compact
> in the sense of Stacks 03E3 and quasi-separated in the absolute sense of Stacks 03BS, part
> (3), that is, quasi-separated over the terminal scheme.

```lean
theorem qcqs_of_isFinitePresentation (hZ : B.Contains (⊤_ Scheme.{u})) {f : X ⟶ Y}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y)
    (hf : IsFinitePresentation B S hS f) :
    IsQuasiCompactSpace B S hS X ∧ IsAbsolutelyQuasiSeparated B S hS hZ X
```

## Tag 05WT, a lemma

[Tag 05WT](https://stacks.math.columbia.edu/tag/05WT) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationCancellation.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationCancellation.lean#L127).

> **Stacks 05WT.** If a composite of morphisms of algebraic spaces over `S` is locally of
> finite presentation and its second factor is locally of finite type, then its first factor is
> locally of finite presentation.
>
> Being locally of finite presentation is étale local on the source and target by **Stacks 04R3**
> and cancels against being locally of finite type at the level of schemes by **Stacks 02FV**,
> part (1), so this is the two-property cancellation of the chart condition at those two
> properties.

```lean
theorem isLocallyOfFinitePresentation_of_comp
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (hH : IsAlgebraicSpace B S hS H)
    (f : F ⟶ G) (g : G ⟶ H)
    (hfg : IsLocallyOfFinitePresentation B S hS (f ≫ g))
    (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyOfFinitePresentation B S hS f
```

## Tag 084P, a lemma

[Tag 084P](https://stacks.math.columbia.edu/tag/084P) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L300). The attribute's comment: “the local assertion”. References: EGA IV (1.4.3.1), “more general”; EGA IV (17.4.1.2), “more general”.

> **Stacks 084P**, the local assertion. The relative diagonal of a morphism of algebraic
> spaces over `S` which is locally of finite type is locally of finite presentation.
>
> The diagonal is the first factor of a factorisation of the identity of the source through the
> fibre square. The identity is locally of finite presentation because it is étale (Stacks
> 0468), and the second projection is locally of finite type by base change, so Stacks 05WT
> applies.

```lean
theorem isLocallyOfFinitePresentation_pullbackDiagonal (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFinitePresentation B S hS (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.isFinitePresentation_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L318). The attribute's comment: “the global assertion”.

> **Stacks 084P**, the global assertion. The relative diagonal of a quasi-separated morphism
> of algebraic spaces over `S` which is locally of finite type is of finite presentation.
>
> Quasi-compactness of the diagonal is quasi-separatedness of the morphism (Stacks 03HL, part
> (3)). Quasi-separatedness of the diagonal follows from its separatedness by Stacks 03KK, and
> the diagonal is separated because it is so after every represented base change (Stacks 03HK,
> part (4)) and the two readings agree for a representable morphism (Stacks 03KY), the diagonal
> being representable by Stacks 03HK, part (1).

```lean
theorem isFinitePresentation_pullbackDiagonal (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    IsFinitePresentation B S hS (pullback.diagonal f)
```

## Tag 06CN, a lemma

[Tag 06CN](https://stacks.math.columbia.edu/tag/06CN) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FinitePresentation.lean#L225).

> **Stacks 06CN.** An open immersion of algebraic spaces over `S` is locally of finite
> presentation.
>
> An open immersion is relatively étale, so in a commuting square of étale charts the composite
> of the chart of the source with the immersion is an étale chart of the target and Stacks 03EC
> makes the morphism of the site étale; an étale morphism of schemes is locally of finite
> presentation. Neither the source nor the target has to be an algebraic space.

```lean
theorem isLocallyOfFinitePresentation_of_isOpenImmersion {f : X ⟶ Y}
    (hf : IsOpenImmersion B S hS f) : IsLocallyOfFinitePresentation B S hS f
```

## Tag 084Q, a lemma

[Tag 084Q](https://stacks.math.columbia.edu/tag/084Q) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentation_iff_isFiniteTypeOnSite_kernelIdealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersionFinitePresentation.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersionFinitePresentation.lean#L282). The attribute's comment: “finite type of the ideal sheaf on the small étale site of the target”. References: EGA IV (1.4.5), “closed immersion case”; EGA IV (8.6.1), “more general”; SGA 3 XI (6.4), “more general”.

> **Stacks 084Q.** A closed immersion `i : Z ⟶ X` of algebraic spaces over `S` is of finite
> presentation if and only if the associated quasi-coherent sheaf of ideals
> `𝓘 = Ker(𝒪_X ⟶ i_*𝒪_Z)` is of finite type as an `𝒪_X`-module, that is, of finite type on the
> small étale site of `X` in the sense of Stacks 03DL (5), which is how Properties of Spaces,
> Section 66.30 reads the condition.
>
> Both implications go through the affine étale charts of `X`.  On such a chart `C` the sections
> of `𝓘` are the ideal cut out by the cartesian projection `Z ×_X C ⟶ C`
> (`AlgebraicGeometry.Space.ker_structureSharp_app_eq_ker_appTop`, Stacks 03G8 part (2)), and
> finite type of `𝓘` is finite generation of those ideals
> (`AlgebraicGeometry.Space.isFiniteTypeOnSite_kernelIdealSheaf_iff_forall_affine_fg_ker`); on the
> other side, finite generation of that ideal over an affine chart is local finite presentation of
> the projection, by the case of schemes (Stacks 01TV) together with
> `AlgebraicGeometry.Scheme.IdealSheafData.isFiniteType_of_fg_ideal_top`.  Local finite
> presentation on all affine charts is local finite presentation of `i`, and the two remaining
> conjuncts of finite presentation hold for every closed immersion.

```lean
theorem isFinitePresentation_iff_isFiniteTypeOnSite_kernelIdealSheaf (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    IsFinitePresentation B S hS i.hom ↔
      SheafOfModules.IsFiniteTypeOnSite (kernelIdealSheaf B S hS i).toSheafOfModules
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.28, Tag 03XO](https://stacks.math.columbia.edu/tag/03XO)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
