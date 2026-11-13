---
declaration: section
origin: cited
lean: Stacks.Descent.quasiCompact_descendsAlong_surjective_inf_flat_inf_quasiCompact, Stacks.Descent.quasiCompact_isLocalAtTarget_fpqc, AlgebraicGeometry.quasiSeparated_isLocalAtTarget_fpqc, AlgebraicGeometry.universallyClosed_isLocalAtTarget_fpqc, AlgebraicGeometry.universallyOpen_isLocalAtTarget_fpqc, AlgebraicGeometry.universallyQuotientMap_isLocalAtTarget_fpqc, AlgebraicGeometry.isSeparated_isLocalAtTarget_fpqc, Stacks.Descent.surjective_isLocalAtTarget_fpqc
statement: formalized
proof: formalized
---

# 35.23 Properties of morphisms local in the fpqc topology on the target

Section 35.23 of the Stacks Project, [Tag 02YJ](https://stacks.math.columbia.edu/tag/02YJ). 34 tags here are carried by 58 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02KQ, a lemma

[Tag 02KQ](https://stacks.math.columbia.edu/tag/02KQ) in the Stacks Project.

**`Stacks.Descent.quasiCompact_descendsAlong_surjective_inf_flat_inf_quasiCompact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L327). The attribute's comment: “the descent step”. References: EGA IV (1.1.4), “special case”.

> **Stacks Project, Tag 02KQ.** Quasi-compact morphisms satisfy fpqc descent: if the base change
> of `g` along a surjective flat quasi-compact morphism is quasi-compact, then so is `g`.

```lean
instance quasiCompact_descendsAlong_surjective_inf_flat_inf_quasiCompact :
    MorphismProperty.DescendsAlong (@QuasiCompact : MorphismProperty Scheme.{u})
      (@Surjective ⊓ @Flat ⊓ @QuasiCompact)
```

**`Stacks.Descent.quasiCompact_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L351). References: SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02KQ.** Quasi-compactness of a morphism of schemes is fpqc local on the
> base.

```lean
instance quasiCompact_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@QuasiCompact : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02KR, a lemma

[Tag 02KR](https://stacks.math.columbia.edu/tag/02KR) in the Stacks Project.

**`AlgebraicGeometry.quasiSeparated_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/FinitePresentation.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/FinitePresentation.lean#L71). References: EGA IV (2.7.1), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02KR.** Quasi-separatedness of morphisms of schemes is fpqc local on
> the base.

```lean
instance quasiSeparated_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@QuasiSeparated : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02KS, a lemma

[Tag 02KS](https://stacks.math.columbia.edu/tag/02KS) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ProperFpqcLocalAtTarget.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ProperFpqcLocalAtTarget.lean#L96). References: EGA IV (2.6.4), “more general”.

> **Stacks Project, Tag 02KS.** Universal closedness of morphisms of schemes is fpqc local on
> the target.

```lean
instance universallyClosed_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@UniversallyClosed : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02KT, a lemma

[Tag 02KT](https://stacks.math.columbia.edu/tag/02KT) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/UniversalHomeomorphism.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/UniversalHomeomorphism.lean#L56). References: EGA IV (2.4.3), “more general”; EGA IV (2.6.4), “more general”; SGA 1 VIII (4.7), “more general”; SGA 3 VIB (2.1.2), “partial”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02KT.** Universal openness of morphisms of schemes is fpqc local on
> the base.

```lean
instance universallyOpen_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@UniversallyOpen : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 0CEW, a lemma

[Tag 0CEW](https://stacks.math.columbia.edu/tag/0CEW) in the Stacks Project.

**`AlgebraicGeometry.universallyQuotientMap_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Submersive.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Submersive.lean#L151). References: EGA IV (15.7.11.1), “partial”.

> **Stacks Project, Tag 0CEW.** Universal submersiveness of morphisms of schemes is fpqc local
> on the base.

```lean
instance universallyQuotientMap_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      ((topologically @Topology.IsQuotientMap : MorphismProperty Scheme.{u}).universally)
      Scheme.fpqcPrecoverage
```

## Tag 02KU, a lemma

[Tag 02KU](https://stacks.math.columbia.edu/tag/02KU) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ProperFpqcLocalAtTarget.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ProperFpqcLocalAtTarget.lean#L106). References: EGA IV (2.7.1), “more general”; SGA 1 VIII (4.8), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02KU.** Separatedness of morphisms of schemes is fpqc local on the
> target.

```lean
instance isSeparated_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsSeparated : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02KV, a lemma

[Tag 02KV](https://stacks.math.columbia.edu/tag/02KV) in the Stacks Project.

**`Stacks.Descent.surjective_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L362). References: SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02KV.** Surjectivity of a morphism of schemes is fpqc local on the
> base.

```lean
instance surjective_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Surjective : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 0H8H, a lemma

[Tag 0H8H](https://stacks.math.columbia.edu/tag/0H8H) in the Stacks Project.

**`AlgebraicGeometry.quasiCompact_isDominant_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Dominant.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Dominant.lean#L83). References: SGA 3 VIB (2.1.2), “qc+dominant example”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 0H8H.** Being quasi-compact and dominant is fpqc local on the base.

```lean
instance quasiCompact_isDominant_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@QuasiCompact ⊓ @IsDominant : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage
```

## Tag 0H8I, a lemma

[Tag 0H8I](https://stacks.math.columbia.edu/tag/0H8I) in the Stacks Project.

**`AlgebraicGeometry.isDominant_iff_baseChange_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/DominantFieldExtension.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/DominantFieldExtension.lean#L43).

> **Stacks Project, Tag 0H8I.** A morphism of schemes over a field is dominant exactly
> when its base change along a field extension is dominant.

```lean
theorem isDominant_iff_baseChange_fieldExtension
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    {X Y : Scheme.{u}} (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    (f : X ⟶ Y) (h : f ≫ pY = pX) :
    let g : Spec (.of K) ⟶ Spec (.of k) :=
      Spec.map (CommRingCat.ofHom (algebraMap k K))
    let fK : pullback pX g ⟶ pullback pY g :=
      pullback.map pX g pY g f (𝟙 _) (𝟙 _) (by simpa using h.symm) (by simp)
    IsDominant f ↔ IsDominant fK
```

## Tag 02KW, a lemma

[Tag 02KW](https://stacks.math.columbia.edu/tag/02KW) in the Stacks Project.

**`AlgebraicGeometry.universallyInjective_iff_of_fpqcCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjectiveFpqcLocalBase.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/UniversallyInjectiveFpqcLocalBase.lean#L62).

> **Stacks Project, Tag 02KW.** Universal injectivity is fpqc local on the base: for an fpqc
> covering `𝒰` of `Y`, a morphism `f : X ⟶ Y` is universally injective if and only if each base
> change `𝒰.X i ×_Y X ⟶ 𝒰.X i` is universally injective.

```lean
theorem universallyInjective_iff_of_fpqcCover {X Y : Scheme.{u}} (f : X ⟶ Y)
    (𝒰 : Precoverage.ZeroHypercover.{w} Scheme.fpqcPrecoverage Y) :
    UniversallyInjective f ↔ ∀ i, UniversallyInjective (pullback.snd f (𝒰.f i))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyInjective.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean#L47) (StacksFrontier). References: SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIB (2.6), “more general”.
- [`AlgebraicGeometry.universallyInjective_isZariskiLocalAtTarget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyInjective_isZariskiLocalAtTarget#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean#L51) (StacksFrontier).
- [`AlgebraicGeometry.universallyInjective_isLocalAtTarget_fpqc`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L224), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/FpqcLocal.lean#L248) (StacksFrontier): “universal injectivity is fpqc local on the target”.

## Tag 0CEX, a lemma

[Tag 0CEX](https://stacks.math.columbia.edu/tag/0CEX) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/UniversalHomeomorphism.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/UniversalHomeomorphism.lean#L110). References: EGA IV (2.6.2), “(iv), special case”; EGA IV (2.6.4), “more general”; SGA 1 VIII (4.7), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 0CEX.** Being a universal homeomorphism of schemes is fpqc local on
> the base.

```lean
instance universalHomeomorphism_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@UniversalHomeomorphism : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage
```

## Tag 02KX, a lemma

[Tag 02KX](https://stacks.math.columbia.edu/tag/02KX) in the Stacks Project.

**`Stacks.Descent.locallyOfFiniteType_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L371).

> **Stacks Project, Tag 02KX.** Being locally of finite type is fpqc local on the base.

```lean
instance locallyOfFiniteType_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@LocallyOfFiniteType : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02KY, a lemma

[Tag 02KY](https://stacks.math.columbia.edu/tag/02KY) in the Stacks Project.

**`Stacks.Descent.locallyOfFinitePresentation_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcDescent.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcDescent.lean#L108). References: EGA IV (2.7.1), “(iv)”; SGA 4 IV (8.5.5), “fpqc target locality”.

> **Stacks Project, Tag 02KY.** Being locally of finite presentation is fpqc local on the
> base.

```lean
instance locallyOfFinitePresentation_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@LocallyOfFinitePresentation : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage
```

## Tag 02KZ, a lemma

[Tag 02KZ](https://stacks.math.columbia.edu/tag/02KZ) in the Stacks Project.

**`Stacks.Descent.finiteType_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L382).

> **Stacks Project, Tag 02KZ.** Being of finite type is fpqc local on the target for scheme
> morphisms.

```lean
instance finiteType_isLocalAtTarget_fpqc :
    IsLocalAtTarget (@LocallyOfFiniteType ⊓ @QuasiCompact : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02L0, a lemma

[Tag 02L0](https://stacks.math.columbia.edu/tag/02L0) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_isLocalAtTarget`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/FinitePresentation.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/FinitePresentation.lean#L81). References: SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L0.** Being of finite presentation is fpqc local on the base.

```lean
instance finitePresentation_isLocalAtTarget :
    MorphismProperty.IsLocalAtTarget
      (@FinitePresentation : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage
```

## Tag 02L1, a lemma

[Tag 02L1](https://stacks.math.columbia.edu/tag/02L1) in the Stacks Project.

**`AlgebraicGeometry.isProper_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ProperFpqcLocalAtTarget.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ProperFpqcLocalAtTarget.lean#L117). References: EGA IV (2.7.1), “more general”; SGA 1 VIII (4.8), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L1.** Properness of morphisms of schemes is fpqc local on the
> target.

```lean
instance isProper_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsProper : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02L2, a lemma

[Tag 02L2](https://stacks.math.columbia.edu/tag/02L2) in the Stacks Project.

**`Stacks.Descent.flat_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcDescent.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcDescent.lean#L97). References: SGA 4 IV (8.5.5), “partial”.

> **Stacks Project, Tag 02L2.** Flatness of a morphism of schemes is fpqc local on the
> base.

```lean
instance flat_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Flat : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02L3, a lemma

[Tag 02L3](https://stacks.math.columbia.edu/tag/02L3) in the Stacks Project.

**`Stacks.Descent.isOpenImmersion_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcOpenImmersion.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcOpenImmersion.lean#L54). References: EGA IV (2.7.1), “descent direction of (x)”; SGA 1 VIII (5.5), “open-immersion clause”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L3.** Being an open immersion is fpqc local on the base: `f` is an
> open immersion if and only if its base change along every member of an fpqc covering of its
> target is one.

```lean
instance isOpenImmersion_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsOpenImmersion : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02L4, a lemma

[Tag 02L4](https://stacks.math.columbia.edu/tag/02L4) in the Stacks Project.

**`Stacks.Descent.isomorphisms_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcIsomorphism.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcIsomorphism.lean#L50).

> **Stacks Project, Tag 02L4.** Being an isomorphism is fpqc local on the base: for every fpqc
> covering `{Yᵢ ⟶ Y}` and every morphism of schemes `f : X ⟶ Y`, the morphism `f` is an
> isomorphism if and only if each base change `Yᵢ ×_Y X ⟶ Yᵢ` is an isomorphism.

```lean
instance isomorphisms_isLocalAtTarget_fpqc :
    (MorphismProperty.isomorphisms Scheme.{u}).IsLocalAtTarget Scheme.fpqcPrecoverage
```

## Tag 02L5, a lemma

[Tag 02L5](https://stacks.math.columbia.edu/tag/02L5) in the Stacks Project.

**`Stacks.Descent.isAffineHom_descendsAlong_surjective_inf_flat_inf_quasiCompact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcAffine.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcAffine.lean#L119). The attribute's comment: “the descent step”.

> Affine morphisms satisfy fpqc descent: if the base change of `g` along a surjective flat
> quasi-compact morphism is affine, then so is `g`.

```lean
instance isAffineHom_descendsAlong_surjective_inf_flat_inf_quasiCompact :
    MorphismProperty.DescendsAlong (@IsAffineHom : MorphismProperty Scheme.{u})
      (@Surjective ⊓ @Flat ⊓ @QuasiCompact)
```

**`Stacks.Descent.isAffineHom_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcAffine.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcAffine.lean#L145). References: SGA 4 IV (8.5.5).

> Being an affine morphism of schemes is fpqc local on the base.

```lean
instance isAffineHom_isLocalAtTarget_fpqc :
    (show MorphismProperty Scheme.{u} from @IsAffineHom).IsLocalAtTarget
      Scheme.fpqcPrecoverage
```

## Tag 02L6, a lemma

[Tag 02L6](https://stacks.math.columbia.edu/tag/02L6) in the Stacks Project.

**`Stacks.Descent.isClosedImmersion_descendsAlong_surjective_inf_flat_inf_quasiCompact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L402). The attribute's comment: “the descent step”. References: EGA IV (2.7.1), “(xii)”; SGA 1 VIII (5.5), “closed-immersion clause”; SGA 3 IV (4.7), “partial”; SGA 4 IV (8.5.5), “partial”.

> Closed immersions satisfy fpqc descent: if the base change of `g` along a surjective flat
> quasi-compact morphism is a closed immersion, then so is `g`.

```lean
instance isClosedImmersion_descendsAlong_surjective_inf_flat_inf_quasiCompact :
    MorphismProperty.DescendsAlong (@IsClosedImmersion : MorphismProperty Scheme.{u})
      (@Surjective ⊓ @Flat ⊓ @QuasiCompact)
```

**`Stacks.Descent.isClosedImmersion_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcLocalAtTarget.lean#L454). References: EGA IV (2.7.1), “(xii)”; SGA 3 VIB (12.1), “more general”; SGA 3 VIII (1.7.3), “Closed immersion clause”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L6.** Being a closed immersion is fpqc local on the base.

```lean
instance isClosedImmersion_isLocalAtTarget_fpqc :
    (show MorphismProperty Scheme.{u} from @IsClosedImmersion).IsLocalAtTarget
      Scheme.fpqcPrecoverage
```

## Tag 02L7, a lemma

[Tag 02L7](https://stacks.math.columbia.edu/tag/02L7) in the Stacks Project.

**`Stacks.Descent.isQuasiAffineHom_descendsAlong_surjective_inf_flat_inf_quasiCompact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiAffine.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiAffine.lean#L133). The attribute's comment: “the descent step”.

> **Stacks Project, Tag 02L7.** Quasi-affine morphisms satisfy fpqc descent: if the base change
> of `g` along a surjective flat quasi-compact morphism is quasi-affine, then so is `g`.

```lean
instance isQuasiAffineHom_descendsAlong_surjective_inf_flat_inf_quasiCompact :
    MorphismProperty.DescendsAlong (@IsQuasiAffineHom : MorphismProperty Scheme.{u})
      (@Surjective ⊓ @Flat ⊓ @QuasiCompact)
```

**`Stacks.Descent.isQuasiAffineHom_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiAffine.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiAffine.lean#L153). References: SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L7.** Being a quasi-affine morphism of schemes is fpqc local on the
> base.

```lean
instance isQuasiAffineHom_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsQuasiAffineHom : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02L8, a lemma

[Tag 02L8](https://stacks.math.columbia.edu/tag/02L8) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtTarget_isImmersion_inf_quasiCompact_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Immersion.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Immersion.lean#L159). References: EGA IV (2.7.1), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L8.** Quasi-compact immersions are fpqc local on the target.

```lean
instance isLocalAtTarget_isImmersion_inf_quasiCompact_fpqc :
    MorphismProperty.IsLocalAtTarget
      (@IsImmersion ⊓ @QuasiCompact : MorphismProperty Scheme.{u}) Scheme.fpqcPrecoverage
```

## Tag 02L9, a lemma

[Tag 02L9](https://stacks.math.columbia.edu/tag/02L9) in the Stacks Project.

**`Stacks.Descent.isIntegralHom_descendsAlong_surjective_inf_flat_inf_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcIntegral.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcIntegral.lean#L91). The attribute's comment: “the descent step”. References: EGA IV (2.7.1), “(xvii)”; SGA 1 VIII (5.7), “detection (integral)”.

> **Stacks Project, Tag 02L9**, the descent step. Integral morphisms satisfy fpqc descent: if
> the base change of `g` along a surjective flat quasi-compact morphism is integral, then so is
> `g`.
>
> Integrality is universal closedness together with affineness
> (`AlgebraicGeometry.IsIntegralHom.eq_universallyClosed_inf_isAffineHom`), and both factors
> descend along surjective flat quasi-compact morphisms, the second by Tag 02L5.

```lean
theorem isIntegralHom_descendsAlong_surjective_inf_flat_inf_quasiCompact :
    MorphismProperty.DescendsAlong (@IsIntegralHom.{u} : MorphismProperty Scheme.{u})
      (@Surjective ⊓ @Flat ⊓ @QuasiCompact)
```

**`Stacks.Descent.isIntegralHom_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcIntegral.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcIntegral.lean#L100). References: EGA IV (2.7.1), “(xvii)”; SGA 1 VIII (5.7), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02L9.** Integrality of a morphism of schemes is fpqc local on the
> base.

```lean
instance isIntegralHom_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsIntegralHom.{u} : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02LA, a lemma

[Tag 02LA](https://stacks.math.columbia.edu/tag/02LA) in the Stacks Project.

**`Stacks.Morphisms.isFinite_isLocalAtTarget_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FiniteFpqcLocalAtTarget.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FiniteFpqcLocalAtTarget.lean#L105). References: EGA II (6.3.10), “Locality on X”; EGA IV (2.7.1), “(xv)”; SGA 1 VIII (5.7), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02LA.** Finiteness of a morphism of schemes is local on the base for
> the fpqc topology.
>
> A finite morphism is an integral morphism which is locally of finite type, integrality is
> universal closedness together with affineness, and of those three constituents only affineness
> was missing; it is Tag 02L5, `Stacks.Descent.isAffineHom_isLocalAtTarget_fpqc`. So this is
> `Stacks.Morphisms.isFinite_isLocalAtTarget_fpqc_of_isAffineHom` with its hypothesis
> discharged.

```lean
theorem isFinite_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsFinite.{u} : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02VI, a lemma

[Tag 02VI](https://stacks.math.columbia.edu/tag/02VI) in the Stacks Project.

**`Stacks.Descent.locallyOfFiniteType_inf_locallyQuasiFinite_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiFinite.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiFinite.lean#L88). The attribute's comment: “locally quasi-finite case”. References: SGA 1 VIII (3.5), “special case”.

> **Stacks Project, Tag 02VI.** Local quasi-finiteness of a scheme morphism is fpqc local on the
> base.

```lean
instance locallyOfFiniteType_inf_locallyQuasiFinite_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      ((@LocallyOfFiniteType : MorphismProperty Scheme.{u}) ⊓ @LocallyQuasiFinite)
      Scheme.fpqcPrecoverage
```

**`Stacks.Descent.finiteType_inf_locallyQuasiFinite_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiFinite.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FpqcQuasiFinite.lean#L100). The attribute's comment: “quasi-finite case”. References: SGA 1 VIII (3.5), “more general”; SGA 3 VIB (2.1.2), “partial”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02VI.** Quasi-finiteness of a scheme morphism is fpqc local on the
> base.

```lean
instance finiteType_inf_locallyQuasiFinite_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (((@LocallyOfFiniteType : MorphismProperty Scheme.{u}) ⊓ @QuasiCompact) ⊓
        @LocallyQuasiFinite) Scheme.fpqcPrecoverage
```

## Tag 02VJ, a lemma

[Tag 02VJ](https://stacks.math.columbia.edu/tag/02VJ) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFiniteTypeRelativeDimension_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/FibreDimension.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/FibreDimension.lean#L201).

> **Stacks Project, Tag 02VJ.** Being locally of finite type of relative dimension `d` is fpqc
> local on the base.

```lean
instance locallyOfFiniteTypeRelativeDimension_isLocalAtTarget_fpqc (d : ℕ) :
    (locallyOfFiniteTypeRelativeDimension.{u} d).IsLocalAtTarget Scheme.fpqcPrecoverage
```

## Tag 02VK, a lemma

[Tag 02VK](https://stacks.math.columbia.edu/tag/02VK) in the Stacks Project.

**`AlgebraicGeometry.syntomic_isLocalAtTarget`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Syntomic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Syntomic.lean#L90).

> **Stacks Project, Tag 02VK.** Syntomicity of a morphism of schemes is fpqc local on the
> base.

```lean
instance syntomic_isLocalAtTarget :
    MorphismProperty.IsLocalAtTarget (@Syntomic : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02VL, a lemma

[Tag 02VL](https://stacks.math.columbia.edu/tag/02VL) in the Stacks Project.

**`Stacks.Descent.smooth_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SmoothFpqcLocalAtTarget.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SmoothFpqcLocalAtTarget.lean#L51). References: SGA 3 VIB (2.1.2), “partial”; SGA 3 VIIA (8.3.1), “Final descent step”.

> **Stacks 02VL.** Smoothness of morphisms of schemes is local on the base for the fpqc
> topology.

```lean
instance smooth_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Smooth : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02VM, a lemma

[Tag 02VM](https://stacks.math.columbia.edu/tag/02VM) in the Stacks Project.

**`AlgebraicGeometry.unramified_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Unramified.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Unramified.lean#L65). The attribute's comment: “unramified”. References: EGA IV (17.7.3), “special case”.

> **Stacks Project, Tag 02VM.** Unramifiedness of morphisms of schemes is fpqc local on the
> base.

```lean
instance unramified_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Unramified : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.gUnramified_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Unramified.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/Unramified.lean#L78). The attribute's comment: “g\_unramified”. References: EGA IV (17.7.3), “special case”; SGA 3 VIB (2.1.2), “Remark 2.1.2”; SGA 4 IV (8.5.5), “partial”.

> **Stacks Project, Tag 02VM.** G-unramifiedness of morphisms of schemes is fpqc local on the
> base.

```lean
instance gUnramified_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@GUnramified : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02VN, a lemma

[Tag 02VN](https://stacks.math.columbia.edu/tag/02VN) in the Stacks Project.

**`AlgebraicGeometry.etale_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleFpqcLocalAtTarget.lean#L73). References: SGA 3 VIB (2.1.2), “partial”.

> Étaleness of morphisms of schemes is fpqc local on the base.

```lean
instance etale_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@Etale : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

## Tag 02VO, a lemma

[Tag 02VO](https://stacks.math.columbia.edu/tag/02VO) in the Stacks Project.

**`Stacks.Morphisms.isFiniteLocallyFree_descendsAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FiniteFpqcLocalAtTarget.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FiniteFpqcLocalAtTarget.lean#L119). The attribute's comment: “the descent step, finite locally free”. References: SGA 1 VIII (5.7), “partial”.

> **The first assertion of Stacks Project, Tag 02VO**, the descent step. Finite locally free
> morphisms satisfy fpqc descent: if the base change of `g` along a surjective flat quasi-compact
> morphism is finite locally free, then so is `g`.
>
> Being finite locally free is being finite, flat and locally of finite presentation, and each
> factor descends: the first is
> `AlgebraicGeometry.Space.isFinite_descendsAlong_surjective_inf_flat_inf_quasiCompact`, which is
> the descent step of Tag 02LA, and the other two are Mathlib's.

```lean
theorem isFiniteLocallyFree_descendsAlong :
    MorphismProperty.DescendsAlong
      (@IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      ((@Surjective.{u} ⊓ @Flat.{u} ⊓ @QuasiCompact.{u} : MorphismProperty Scheme.{u}))
```

**`Stacks.Morphisms.isFiniteLocallyFreeOfRank_descendsAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FiniteFpqcLocalAtTarget.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/FiniteFpqcLocalAtTarget.lean#L150). The attribute's comment: “the descent step, fixed degree”. References: SGA 1 VIII (5.7), “special case”.

> **The second assertion of Stacks Project, Tag 02VO**, the descent step. Morphisms which are
> finite locally free of a fixed degree `r` satisfy fpqc descent: if the base change of `g` along
> a surjective flat quasi-compact morphism is finite locally free of degree `r`, then so is `g`.
>
> The degree-free case makes `g` finite, flat and locally of finite presentation, so the rank
> criterion `Stacks.Morphisms.isFiniteLocallyFreeOfRank_iff_forall_finrank_eq` applies to both `g`
> and its base change and turns the statement into one about the rank function
> `AlgebraicGeometry.Scheme.Hom.finrank`. That function is compatible with base change by
> `AlgebraicGeometry.Scheme.Hom.finrank_of_isPullback`, and the covering morphism is surjective
> on points, so the rank of `g` at an arbitrary point of its target is the rank of the base
> change at a point above it, which is `r`.

```lean
theorem isFiniteLocallyFreeOfRank_descendsAlong (r : ℕ) :
    MorphismProperty.DescendsAlong (IsFiniteLocallyFreeOfRank.property.{u} r)
      ((@Surjective.{u} ⊓ @Flat.{u} ⊓ @QuasiCompact.{u} : MorphismProperty Scheme.{u}))
```

**`Stacks.Morphisms.isFiniteLocallyFree_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcLocalAtTarget.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcLocalAtTarget.lean#L122). The attribute's comment: “finite locally free”.

> **Stacks Project, Tag 02VO.** Being finite locally free is fpqc local on the base.

```lean
instance isFiniteLocallyFree_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget (@IsFiniteLocallyFree : MorphismProperty Scheme.{u})
      Scheme.fpqcPrecoverage
```

**`Stacks.Morphisms.isFiniteLocallyFreeOfRank_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcLocalAtTarget.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FpqcLocalAtTarget.lean#L131). The attribute's comment: “finite locally free of fixed degree”.

> **Stacks Project, Tag 02VO.** For `d : ℕ`, being finite locally free of degree `d` is fpqc
> local on the base.

```lean
instance isFiniteLocallyFreeOfRank_isLocalAtTarget_fpqc (d : ℕ) :
    MorphismProperty.IsLocalAtTarget (IsFiniteLocallyFreeOfRank.property.{u} d)
      Scheme.fpqcPrecoverage
```

## Tag 02YK, a lemma

[Tag 02YK](https://stacks.math.columbia.edu/tag/02YK) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtTarget_monomorphisms_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/SchemeProperty/FpqcLocal.lean#L55). References: EGA IV (2.7.1), “more general”; SGA 4 IV (8.5.5).

> **Stacks Project, Tag 02YK.** Monomorphisms of schemes are fpqc local on the target.

```lean
instance isLocalAtTarget_monomorphisms_fpqc :
    (MorphismProperty.monomorphisms Scheme.{u}).IsLocalAtTarget Scheme.fpqcPrecoverage
```

## Tag 0694, a lemma

[Tag 0694](https://stacks.math.columbia.edu/tag/0694) in the Stacks Project.

**`AlgebraicGeometry.isLocalAtTarget_koszulRegularImmersion_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/RegularImmersion.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/RegularImmersion.lean#L311). The attribute's comment: “koszul\_regular, étale topology”.

> **Stacks Project, Tag 0694, the Koszul-regular clause, for the étale topology.** Being a
> Koszul-regular immersion of schemes is local on the target for the étale topology.

```lean
theorem isLocalAtTarget_koszulRegularImmersion_etale :
    MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @IsKoszulRegularImmersion _ _ f hf)
      Scheme.etalePrecoverage.{u}
```

**`AlgebraicGeometry.isLocalAtTarget_h1RegularImmersion_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/RegularImmersion.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/RegularImmersion.lean#L329). The attribute's comment: “h1\_regular, étale topology”.

> **Stacks Project, Tag 0694, the `H₁`-regular clause, for the étale topology.** Being an
> `H₁`-regular immersion of schemes is local on the target for the étale topology.

```lean
theorem isLocalAtTarget_h1RegularImmersion_etale :
    MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @IsH1RegularImmersion _ _ f hf)
      Scheme.etalePrecoverage.{u}
```

**`AlgebraicGeometry.isLocalAtTarget_quasiRegularImmersion_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/RegularImmersion.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/RegularImmersion.lean#L347). The attribute's comment: “quasi\_regular, étale topology”.

> **Stacks Project, Tag 0694, the quasi-regular clause, for the étale topology.** Being a
> quasi-regular immersion of schemes is local on the target for the étale topology.

```lean
theorem isLocalAtTarget_quasiRegularImmersion_etale :
    MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f,
        @RegularIdealSheaf.IsQuasiRegularImmersion _ _ f hf)
      Scheme.etalePrecoverage.{u}
```

**`AlgebraicGeometry.isLocalAtTarget_koszulRegularImmersion_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFppf.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFppf.lean#L215). The attribute's comment: “koszul\_regular, erratum: fppf in place of fpqc; counterexample Stacks.Descent.counterexampleHom”. References: SGA 6 VII (1.5), “special case”.

> **Stacks Project, Tag 0694, the Koszul-regular clause, for the fppf topology.** Being a
> Koszul-regular immersion of schemes is local on the target for the fppf topology, with no
> quasi-compactness and no hypothesis that the morphism is an immersion.
>
> The tag asserts this for the fpqc topology, where it is false.

```lean
theorem isLocalAtTarget_koszulRegularImmersion_fppf :
    MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @IsKoszulRegularImmersion _ _ f hf)
      Scheme.fppfPrecoverage.{u}
```

**`AlgebraicGeometry.isLocalAtTarget_h1RegularImmersion_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFppf.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFppf.lean#L235). The attribute's comment: “h1\_regular, erratum: fppf in place of fpqc; counterexample Stacks.Descent.counterexampleHom”.

> **Stacks Project, Tag 0694, the `H₁`-regular clause, for the fppf topology.** Being an
> `H₁`-regular immersion of schemes is local on the target for the fppf topology, with no
> quasi-compactness and no hypothesis that the morphism is an immersion.
>
> The tag asserts this for the fpqc topology, where it is false.

```lean
theorem isLocalAtTarget_h1RegularImmersion_fppf :
    MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @IsH1RegularImmersion _ _ f hf)
      Scheme.fppfPrecoverage.{u}
```

**`AlgebraicGeometry.isLocalAtTarget_quasiRegularImmersion_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFppf.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFppf.lean#L256). The attribute's comment: “quasi\_regular, erratum: fppf in place of fpqc; counterexample Stacks.Descent.counterexampleHom”. References: EGA IV (19.1.5), “(ii), special case”.

> **Stacks Project, Tag 0694, the quasi-regular clause, for the fppf topology.** Being a
> quasi-regular immersion of schemes is local on the target for the fppf topology, with no
> quasi-compactness and no hypothesis that the morphism is an immersion.
>
> The tag asserts this for the fpqc topology, where it is false.

```lean
theorem isLocalAtTarget_quasiRegularImmersion_fppf :
    MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f,
        @RegularIdealSheaf.IsQuasiRegularImmersion _ _ f hf)
      Scheme.fppfPrecoverage.{u}
```

**`AlgebraicGeometry.isLocalAtTarget_koszulRegularImmersion_inf_quasiCompact_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqc.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqc.lean#L716). The attribute's comment: “koszul\_regular”. References: SGA 6 VII (1.5), “special case”.

> **Stacks Project, Tag 0694, the Koszul-regular clause.** Being a quasi-compact Koszul-regular
> immersion of schemes is local on the target for the fpqc topology.

```lean
theorem isLocalAtTarget_koszulRegularImmersion_inf_quasiCompact_fpqc :
    MorphismProperty.IsLocalAtTarget
      ((fun _ _ f => ∃ hf : IsImmersion f, @IsKoszulRegularImmersion _ _ f hf) ⊓
        (@QuasiCompact : MorphismProperty Scheme.{u})) Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.isLocalAtTarget_h1RegularImmersion_inf_quasiCompact_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqc.lean, line 734](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqc.lean#L734). The attribute's comment: “h1\_regular”.

> **Stacks Project, Tag 0694, the `H₁`-regular clause.** Being a quasi-compact `H₁`-regular
> immersion of schemes is local on the target for the fpqc topology.

```lean
theorem isLocalAtTarget_h1RegularImmersion_inf_quasiCompact_fpqc :
    MorphismProperty.IsLocalAtTarget
      ((fun _ _ f => ∃ hf : IsImmersion f, @IsH1RegularImmersion _ _ f hf) ⊓
        (@QuasiCompact : MorphismProperty Scheme.{u})) Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.isLocalAtTarget_quasiRegularImmersion_inf_quasiCompact_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqc.lean, line 752](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqc.lean#L752). The attribute's comment: “quasi\_regular”. References: EGA IV (19.1.5), “(ii), special case”.

> **Stacks Project, Tag 0694, the quasi-regular clause.** Being a quasi-compact quasi-regular
> immersion of schemes is local on the target for the fpqc topology.

```lean
theorem isLocalAtTarget_quasiRegularImmersion_inf_quasiCompact_fpqc :
    MorphismProperty.IsLocalAtTarget
      ((fun _ _ f => ∃ hf : IsImmersion f,
          @RegularIdealSheaf.IsQuasiRegularImmersion _ _ f hf) ⊓
        (@QuasiCompact : MorphismProperty Scheme.{u})) Scheme.fpqcPrecoverage
```

**`AlgebraicGeometry.isKoszulRegularImmersion_iff_of_fpqcZeroHypercover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqcOfImmersion.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqcOfImmersion.lean#L177). The attribute's comment: “koszul\_regular, erratum: morphisms that are immersions; fpqc, no quasi-compactness”. References: SGA 6 VII (1.5).

> **Stacks Project, Tag 0694, the Koszul-regular clause, for an immersion.** An immersion of
> schemes is Koszul-regular if and only if its base changes along the members of an fpqc covering
> of the target are, with no quasi-compactness.

```lean
theorem isKoszulRegularImmersion_iff_of_fpqcZeroHypercover
    {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (𝒰 : Precoverage.ZeroHypercover.{w} Scheme.fpqcPrecoverage X) :
    IsKoszulRegularImmersion i ↔ ∀ k, IsKoszulRegularImmersion (pullback.snd i (𝒰.f k))
```

**`AlgebraicGeometry.isH1RegularImmersion_iff_of_fpqcZeroHypercover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqcOfImmersion.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqcOfImmersion.lean#L197). The attribute's comment: “h1\_regular, erratum: morphisms that are immersions; fpqc, no quasi-compactness”.

> **Stacks Project, Tag 0694, the `H₁`-regular clause, for an immersion.** An immersion of
> schemes is `H₁`-regular if and only if its base changes along the members of an fpqc covering of
> the target are, with no quasi-compactness.

```lean
theorem isH1RegularImmersion_iff_of_fpqcZeroHypercover
    {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (𝒰 : Precoverage.ZeroHypercover.{w} Scheme.fpqcPrecoverage X) :
    IsH1RegularImmersion i ↔ ∀ k, IsH1RegularImmersion (pullback.snd i (𝒰.f k))
```

**`AlgebraicGeometry.isQuasiRegularImmersion_iff_of_fpqcZeroHypercover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqcOfImmersion.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionFpqcOfImmersion.lean#L218). The attribute's comment: “quasi\_regular, erratum: morphisms that are immersions; fpqc, no quasi-compactness”. References: EGA IV (19.1.5), “more general”.

> **Stacks Project, Tag 0694, the quasi-regular clause, for an immersion.** An immersion of
> schemes is quasi-regular if and only if its base changes along the members of an fpqc covering of
> the target are, with no quasi-compactness.

```lean
theorem isQuasiRegularImmersion_iff_of_fpqcZeroHypercover
    {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (𝒰 : Precoverage.ZeroHypercover.{w} Scheme.fpqcPrecoverage X) :
    RegularIdealSheaf.IsQuasiRegularImmersion i ↔
      ∀ k, RegularIdealSheaf.IsQuasiRegularImmersion (pullback.snd i (𝒰.f k))
```

**`Stacks.Descent.not_isLocalAtTarget_koszulRegularImmersion_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionNotFpqcLocal.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionNotFpqcLocal.lean#L224). The attribute's comment: “koszul\_regular, counterexample: false for fpqc coverings without quasi-compactness”.

> **Stacks Project, Tag 0694, the Koszul-regular clause, is false for the fpqc topology.**
> Being a Koszul-regular immersion is not local on the target for the fpqc precoverage.

```lean
theorem not_isLocalAtTarget_koszulRegularImmersion_fpqc :
    ¬ MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @IsKoszulRegularImmersion _ _ f hf)
      Scheme.fpqcPrecoverage.{0}
```

**`Stacks.Descent.not_isLocalAtTarget_h1RegularImmersion_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionNotFpqcLocal.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionNotFpqcLocal.lean#L241). The attribute's comment: “h1\_regular, counterexample: false for fpqc coverings without quasi-compactness”.

> **Stacks Project, Tag 0694, the `H₁`-regular clause, is false for the fpqc topology.**
> Being an `H₁`-regular immersion is not local on the target for the fpqc precoverage.

```lean
theorem not_isLocalAtTarget_h1RegularImmersion_fpqc :
    ¬ MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @IsH1RegularImmersion _ _ f hf)
      Scheme.fpqcPrecoverage.{0}
```

**`Stacks.Descent.not_isLocalAtTarget_quasiRegularImmersion_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionNotFpqcLocal.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/LocalOnTarget/RegularImmersionNotFpqcLocal.lean#L258). The attribute's comment: “quasi\_regular, counterexample: false for fpqc coverings without quasi-compactness”.

> **Stacks Project, Tag 0694, the quasi-regular clause, is false for the fpqc topology.**
> Being a quasi-regular immersion is not local on the target for the fpqc precoverage.

```lean
theorem not_isLocalAtTarget_quasiRegularImmersion_fpqc :
    ¬ MorphismProperty.IsLocalAtTarget
      (fun _ _ f => ∃ hf : IsImmersion f, @RegularIdealSheaf.IsQuasiRegularImmersion _ _ f hf)
      Scheme.fpqcPrecoverage.{0}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.23, Tag 02YJ](https://stacks.math.columbia.edu/tag/02YJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
