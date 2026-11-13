---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FormallyUnramified, AlgebraicGeometry.Space.formallyUnramified_iff_etaleCharts, AlgebraicGeometry.Space.formallyUnramified_iff_surjectiveEtaleChart, AlgebraicGeometry.Space.holdsOnEveryEtaleChart_of_formallyUnramified, AlgebraicGeometry.Space.exists_surjectiveEtaleChart_of_holdsOnEveryEtaleChart, AlgebraicGeometry.Space.formallyUnramified_of_surjectiveEtaleChart, AlgebraicGeometry.Space.FormallyUnramified.lifts_unique_of_firstOrderThickening, AlgebraicGeometry.Space.formallyUnramified_comp
statement: formalized
proof: formalized
---

# 76.14 Formally unramified morphisms

Section 76.14 of the Stacks Project, [Tag 04G6](https://stacks.math.columbia.edu/tag/04G6). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04G7, a definition

[Tag 04G7](https://stacks.math.columbia.edu/tag/04G7) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallyUnramified`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean#L90). The attribute's comment: “formally unramified morphism of algebraic spaces”. References: SGA 3 XI (1.6), “formally unramified”.

> **Stacks 049S, part (3).** Every commutative affine square against a
> square-zero closed immersion admits at most one lift.

```lean
public abbrev FormallyUnramified {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (a : F ⟶ G) :
    Prop
```

## Tag 04G8, a lemma

[Tag 04G8](https://stacks.math.columbia.edu/tag/04G8) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_iff_etaleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedChartCriterion.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedChartCriterion.lean#L102). The attribute's comment: “equivalence of (1) and (2)”.

> **Stacks 04G8, the equivalence of (1) and (2).** A morphism of algebraic spaces over `S` is
> formally unramified exactly when the morphism of schemes underlying every commuting square of
> étale scheme charts is formally unramified.

```lean
public theorem formallyUnramified_iff_etaleCharts
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    FormallyUnramified f ↔
      HoldsOnEveryEtaleChart B S hS
        (@_root_.AlgebraicGeometry.FormallyUnramified.{u} : MorphismProperty Scheme.{u}) f
```

**`AlgebraicGeometry.Space.formallyUnramified_iff_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedChartCriterion.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedChartCriterion.lean#L119). The attribute's comment: “equivalence of (1) and (3)”.

> **Stacks 04G8, the equivalence of (1) and (3).** A morphism of algebraic spaces over `S` is
> formally unramified exactly when there is one commuting square of étale scheme charts, both
> chart maps surjective, whose underlying morphism of schemes is formally unramified.

```lean
public theorem formallyUnramified_iff_surjectiveEtaleChart
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    FormallyUnramified f ↔
      ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (ψ : U ⟶ V),
        (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf b ∧
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf b ∧
        yoneda.map ψ ≫ b = a ≫ f ∧
        _root_.AlgebraicGeometry.FormallyUnramified
          ((BigFppfOver.toScheme B S hS).map ψ)
```

**`AlgebraicGeometry.Space.holdsOnEveryEtaleChart_of_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleCharts.lean, line 561](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleCharts.lean#L561). The attribute's comment: “condition (1) implies condition (2)”.

> **Stacks 04G8, condition (1) implies condition (2).** A formally unramified morphism of
> presheaves on the big fppf site of `S` is formally unramified on every commuting square of
> étale scheme charts.
>
> No algebraicity hypothesis on the source or target is needed, and none is imposed.

```lean
theorem holdsOnEveryEtaleChart_of_formallyUnramified (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : FormallyUnramified f) :
    HoldsOnEveryEtaleChart B S hS
      (@_root_.AlgebraicGeometry.FormallyUnramified.{u} : MorphismProperty Scheme.{u}) f
```

**`AlgebraicGeometry.Space.exists_surjectiveEtaleChart_of_holdsOnEveryEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleCharts.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleCharts.lean#L578). The attribute's comment: “condition (2) implies condition (3)”.

> **Stacks 04G8, condition (2) implies condition (3).** If a morphism of algebraic spaces
> over `S` is formally unramified on every commuting square of étale scheme charts, then
> there is one such square whose two chart morphisms are in addition surjective.
>
> The square is produced from a surjective étale chart of the target, which exists by
> `AlgebraicGeometry.IsAlgebraicSpace.exists_atlas`, and its lift to the source, which is
> [Stacks Project, Tag 02X1].

```lean
theorem exists_surjectiveEtaleChart_of_holdsOnEveryEtaleChart (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hall : HoldsOnEveryEtaleChart B S hS
      (@_root_.AlgebraicGeometry.FormallyUnramified.{u} : MorphismProperty Scheme.{u}) f) :
    ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (h : U ⟶ V),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf b ∧
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a ∧
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf b ∧
      yoneda.map h ≫ b = a ≫ f ∧
      _root_.AlgebraicGeometry.FormallyUnramified
        ((BigFppfOver.toScheme B S hS).map h)
```

**`AlgebraicGeometry.Space.formallyUnramified_of_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleDescent.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedEtaleDescent.lean#L491). The attribute's comment: “condition (3) implies condition (1)”.

> **Stacks 04G8, condition (3) implies condition (1).** If a morphism `f` out of an algebraic
> space over `S` has one commuting square of surjective étale scheme charts whose chart morphism is
> formally unramified as a morphism of schemes, then `f` is formally unramified in the sense of
> [Stacks Project, Tag 049S].
>
> The composite of the chart of the source with `f` is formally unramified by
> `AlgebraicGeometry.Space.formallyUnramified_chart_comp`, and
> `AlgebraicGeometry.Space.formallyUnramified_of_formallyUnramified_comp` descends that along the
> chart. Together with `AlgebraicGeometry.Space.holdsOnEveryEtaleChart_of_formallyUnramified` and
> `AlgebraicGeometry.Space.exists_surjectiveEtaleChart_of_holdsOnEveryEtaleChart` it makes all
> three conditions of the tag equivalent.

```lean
theorem formallyUnramified_of_surjectiveEtaleChart (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (hex : ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y)
      (h : U ⟶ V),
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf b ∧
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf a ∧
      (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf b ∧
      yoneda.map h ≫ b = a ≫ f ∧
      _root_.AlgebraicGeometry.FormallyUnramified
        ((BigFppfOver.toScheme B S hS).map h)) :
    FormallyUnramified f
```

## Tag 05ZY, a lemma

[Tag 05ZY](https://stacks.math.columbia.edu/tag/05ZY) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallyUnramified.lifts_unique_of_firstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedThickenings.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedThickenings.lean#L132).

> **Stacks 05ZY.** A formally unramified morphism `f : X ⟶ Y` of algebraic spaces over `S`
> admits at most one dotted arrow in a solid square over a first-order thickening `T ⊂ T'` of
> algebraic spaces over `S`. In other words the affineness of the test objects in the definition
> of formal unramifiedness, Stacks 049S part (3), may be dropped.

```lean
theorem FormallyUnramified.lifts_unique_of_firstOrderThickening
    {X Y T' : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : FormallyUnramified f.hom)
    (T : Subfunctor T'.obj) (hT : IsFirstOrderThickening B S hS T' T)
    (a : T.toFunctor ⟶ X.obj) (b : T'.obj ⟶ Y.obj) (hsq : a ≫ f.hom = T.ι ≫ b)
    (z₁ z₂ : T'.obj ⟶ X.obj)
    (hz₁a : T.ι ≫ z₁ = a) (hz₁b : z₁ ≫ f.hom = b)
    (hz₂a : T.ι ≫ z₂ = a) (hz₂b : z₂ ≫ f.hom = b) :
    z₁ = z₂
```

## Tag 05ZZ, a lemma

[Tag 05ZZ](https://stacks.math.columbia.edu/tag/05ZZ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.formallyUnramified_comp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean#L64) (StacksFrontier).

## Tag 0600, a lemma

[Tag 0600](https://stacks.math.columbia.edu/tag/0600) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedBaseChange.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/UnramifiedBaseChange.lean#L53). References: EGA IV (17.1.3), “more general”.

> **Stacks 0600.** A base change of a formally unramified morphism of algebraic spaces is
> formally unramified: in a cartesian square with `f` formally unramified, the opposite side `p`
> of the square is formally unramified.
>
> This is also the first assertion of Stacks 060B: in a fibre product diagram
> `Z = X ×_Y W` of algebraic spaces over `S` with `h' : W ⟶ Y` formally unramified (here `f`),
> the morphism `h : Z ⟶ X` (here `p`) is formally unramified.

```lean
theorem formallyUnramified_of_isPullback
    {F G H P : AlgebraicSpaces B S hS}
    (f : F ⟶ G) (g : H ⟶ G) (p : P ⟶ H) (q : P ⟶ F)
    (sq : IsPullback p q g f)
    (unramified : FormallyUnramified f.hom) :
    FormallyUnramified p.hom
```

## Tag 04G9, a lemma

[Tag 04G9](https://stacks.math.columbia.edu/tag/04G9) in the Stacks Project.

**`AlgebraicGeometry.Space.formallyUnramified_iff_isZero_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedSheafOfDifferentials.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FormallyUnramifiedSheafOfDifferentials.lean#L268). References: EGA IV (17.2.1), “more general”.

> **Stacks 04G9.** A morphism `f : X ⟶ Y` of algebraic spaces over `S` is formally unramified
> exactly when its sheaf of differentials `Ω_{X/Y}` is a zero object.
>
> The invertibility clause of Stacks 04CS, read at zero objects for an arbitrary morphism of
> schemes of the site, is `AlgebraicGeometry.Space.sheafOfDifferentialsSchemeVanishing`;
> Stacks 04CU turns it into the chart-square comparison that the proof consumes,
> `AlgebraicGeometry.Space.sheafOfDifferentialsChartComparison`, and
> `AlgebraicGeometry.Space.formallyUnramified_iff_isZero_sheafOfDifferentials_of_chart` is the
> proof proper; see there.

```lean
theorem formallyUnramified_iff_isZero_sheafOfDifferentials {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) :
    FormallyUnramified f.hom ↔ IsZero (sheafOfDifferentials B S hS f)
```

## Tag 04GA, a lemma

[Tag 04GA](https://stacks.math.columbia.edu/tag/04GA) in the Stacks Project.

**`AlgebraicGeometry.Space.isUnramified_tfae_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedSheafOfDifferentials.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedSheafOfDifferentials.lean#L111).

> **Stacks 04GA.**  For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` the
> following are equivalent:
>
> 1. `f` is unramified,
> 2. `f` is locally of finite type and `Ω_{X/Y} = 0`,
> 3. `f` is locally of finite type and formally unramified.
>
> (1) ⟺ (3) is
> `AlgebraicGeometry.Space.isUnramified_iff_isLocallyOfFiniteType_and_formallyUnramified`, and
> (1) ⟺ (2) is
> `AlgebraicGeometry.Space.isUnramified_iff_isLocallyOfFiniteType_and_isZero_sheafOfDifferentials`.

```lean
theorem isUnramified_tfae_sheafOfDifferentials (f : X ⟶ Y) :
    List.TFAE [IsUnramified B S hS f.hom,
      IsLocallyOfFiniteType B S hS f.hom ∧ IsZero (sheafOfDifferentials B S hS f),
      IsLocallyOfFiniteType B S hS f.hom ∧ FormallyUnramified f.hom]
```

## Tag 05W6, a lemma

[Tag 05W6](https://stacks.math.columbia.edu/tag/05W6) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_isLocallyQuasiFinite_of_isLocallyOfFiniteType_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean#L243). The attribute's comment: “separated and locally quasi-finite, from condition (3)”.

> **Stacks 0463.** A monomorphism of algebraic spaces over `S` which is locally of finite type
> is separated and locally quasi-finite.
>
> Separatedness is [Stacks Project, Tag 042N], already available as
> `AlgebraicGeometry.Space.isSeparated_of_mono`; local quasi-finiteness goes through
> unramifiedness, which a monomorphism locally of finite type has by
> `AlgebraicGeometry.Space.isUnramified_of_isLocallyOfFiniteType_of_mono`.
>
> These are two of the three assertions of the "moreover" clause of
> [Stacks Project, Tag 05W6], reached from its condition (3); the equivalence of conditions (1)
> and (3) carries them over to condition (1), and the two unconditional equivalences below carry
> them over to conditions (2) and (4).

```lean
theorem isSeparated_isLocallyQuasiFinite_of_isLocallyOfFiniteType_mono (f : X ⟶ Y)
    (h : IsLocallyOfFiniteType B S hS f ∧ Mono f) :
    IsSeparated B S hS f ∧ IsLocallyQuasiFinite B S hS f
```

**`AlgebraicGeometry.Space.isUnramified_mono_iff_isUnramified_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean#L261). The attribute's comment: “conditions (1) and (2)”. References: EGA IV (17.2.6), “(b) => (a)”.

> **Stacks 05W6, conditions (1) and (2).** A morphism of algebraic spaces over `S` is
> unramified and a monomorphism if and only if it is unramified and universally injective.
>
> The forward implication is
> `AlgebraicGeometry.Space.isUnramified_universallyInjective_of_isUnramified_mono`. The converse
> is `AlgebraicGeometry.Space.mono_of_isOpenImmersion_diagonal_of_universallyInjective`, whose
> open-immersion input is part (1) of [Stacks Project, Tag 05W1], specialised to `f`; that is
> `AlgebraicGeometry.Space.isOpenImmersion_diagonal_of_isUnramified`.

```lean
theorem isUnramified_mono_iff_isUnramified_universallyInjective
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (IsUnramified B S hS f ∧ Mono f) ↔
      (IsUnramified B S hS f ∧ UniversallyInjective B S hS f)
```

**`AlgebraicGeometry.Space.isUnramified_mono_iff_universallyInjective_locallyOfFiniteType_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoCriteria.lean#L287). The attribute's comment: “conditions (1) and (4)”.

> **Stacks 05W6, conditions (1) and (4).** A morphism of algebraic spaces over `S` is
> unramified and a monomorphism if and only if it is universally injective, locally of finite
> type and formally unramified.
>
> The forward implication is, in this namespace,
> `universallyInjective_isLocallyOfFiniteType_formallyUnramified_of_isUnramified_mono`.
> For the converse, local finite type together with formal unramifiedness on étale charts is
> unramifiedness, which is the available half of [Stacks Project, Tag 04GA]; passing from
> `AlgebraicGeometry.Space.FormallyUnramified` to the chart condition is condition (1) implies
> condition (2) of [Stacks Project, Tag 04G8], supplied by
> `AlgebraicGeometry.Space.holdsOnEveryEtaleChart_of_formallyUnramified` of
> `StacksFrontier.AlgebraicGeometry.Spaces.FormallyUnramifiedEtaleCharts`. The monomorphism is then
> obtained as in
> `AlgebraicGeometry.Space.isUnramified_mono_iff_isUnramified_universallyInjective`, from part (1)
> of [Stacks Project, Tag 05W1]. Both inputs being available, this equivalence is unconditional
> and carries the tag.

```lean
theorem isUnramified_mono_iff_universallyInjective_locallyOfFiniteType_formallyUnramified
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (IsUnramified B S hS f ∧ Mono f) ↔
      (UniversallyInjective B S hS f ∧ IsLocallyOfFiniteType B S hS f ∧
        FormallyUnramified (B := B) (S := S) (hS := hS) f)
```

**`AlgebraicGeometry.Space.isUnramified_mono_iff_isLocallyOfFiniteType_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonomorphism.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonomorphism.lean#L202). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 05W6, conditions (1) and (3).** A morphism of algebraic spaces over `S` is
> unramified and a monomorphism if and only if it is locally of finite type and a monomorphism.

```lean
theorem isUnramified_mono_iff_isLocallyOfFiniteType_mono
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (IsUnramified B S hS f ∧ Mono f) ↔ (IsLocallyOfFiniteType B S hS f ∧ Mono f)
```

**`AlgebraicGeometry.Space.isUnramified_mono_tfae_and_relativelyRepresentable_isSeparated_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoRepresentable.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedMonoRepresentable.lean#L89).

> **Stacks 05W6.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`. The
> following are equivalent:
>
> 1. `f` is unramified and a monomorphism,
> 2. `f` is unramified and universally injective,
> 3. `f` is locally of finite type and a monomorphism,
> 4. `f` is universally injective, locally of finite type and formally unramified.
>
> Moreover, in that case `f` is representable, separated and locally quasi-finite.
>
> The equivalences run through condition (1). The "moreover" clause is taken at condition (3):
> separatedness and local quasi-finiteness are [Stacks Project, Tag 0463], and representability
> follows from them by [Stacks Project, Tag 0418].

```lean
theorem isUnramified_mono_tfae_and_relativelyRepresentable_isSeparated_isLocallyQuasiFinite
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE
      [IsUnramified B S hS f ∧ Mono f,
        IsUnramified B S hS f ∧ UniversallyInjective B S hS f,
        IsLocallyOfFiniteType B S hS f ∧ Mono f,
        UniversallyInjective B S hS f ∧ IsLocallyOfFiniteType B S hS f ∧
          FormallyUnramified (B := B) (S := S) (hS := hS) f] ∧
      ((IsUnramified B S hS f ∧ Mono f) →
        yoneda.relativelyRepresentable f ∧ IsSeparated B S hS f ∧
          IsLocallyQuasiFinite B S hS f)
```

## Tag 05W8, a lemma

[Tag 05W8](https://stacks.math.columbia.edu/tag/05W8) in the Stacks Project.

**`AlgebraicGeometry.Space.closedImmersion_conditions_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionCriteria.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionCriteria.lean#L153). References: SGA 3 V (4.1.3).

> The five equivalent conditions characterizing closed immersions of algebraic spaces.

```lean
public theorem closedImmersion_conditions_tfae
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [IsClosedImmersion B S hS f,
       UniversallyClosed B S hS f ∧
         (IsUnramified B S hS f ∧ Mono f),
       UniversallyClosed B S hS f ∧
         (IsUnramified B S hS f ∧
           UniversallyInjective B S hS f),
       UniversallyClosed B S hS f ∧
         (IsLocallyOfFiniteType B S hS f ∧ Mono f),
       UniversallyClosed B S hS f ∧
         (UniversallyInjective B S hS f ∧
           (IsLocallyOfFiniteType B S hS f ∧
             FormallyUnramified f))]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.14, Tag 04G6](https://stacks.math.columbia.edu/tag/04G6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
