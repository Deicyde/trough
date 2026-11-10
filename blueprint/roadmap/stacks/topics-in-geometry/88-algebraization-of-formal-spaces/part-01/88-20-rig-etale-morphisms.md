---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsRigEtale, AlgebraicGeometry.FormalSpace.isRigEtale_tfae_of_isLocallyNoetherian', AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_of_isRigEtale_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.isRigSmooth_of_isRigEtale, AlgebraicGeometry.FormalSpace.isRigEtale_pullback_snd_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.isRigEtale_pullback_snd_of_isAdicMorphism, AlgebraicGeometry.FormalSpace.isRigEtale_comp_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.isRigEtale_of_comp_of_isLocallyNoetherian
statement: formalized
proof: formalized
---

# 88.20 Rig-étale morphisms

Section 88.20 of the Stacks Project, [Tag 0AQK](https://stacks.math.columbia.edu/tag/0AQK). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AQM, a definition

[Tag 0AQM](https://stacks.math.columbia.edu/tag/0AQM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtale.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtale.lean#L73).

> **Stacks 0AQM.** A morphism of formal algebraic spaces over `S` is *rig-étale* when every
> morphism between affine, representable, étale charts of its source and target is induced by a
> rig-étale continuous homomorphism of adic Noetherian topological rings.

```lean
abbrev IsRigEtale (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0GCZ, a lemma

[Tag 0GCZ](https://stacks.math.columbia.edu/tag/0GCZ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigEtale_tfae_of_isLocallyNoetherian'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleLocalCharacterizationCharts.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleLocalCharacterizationCharts.lean#L131).

> **Stacks 0GCZ.** Let `f : X ⟶ Y` be a morphism of locally Noetherian formal algebraic spaces
> over `S`. The following are equivalent:
>
> 1. `f` is rig-étale (Definition 0AQM);
> 2. for every commutative square with `U`, `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    rig-étale map in `WAdm^{Noeth}`;
> 3. there exist a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM such that each `Xⱼᵢ ⟶ Yⱼ` corresponds to a
>    rig-étale map in `WAdm^{Noeth}`;
> 4. there exist a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` where `Yᵢ` is an affine formal algebraic space, `Yᵢ ⟶ Y` is representable by
>    algebraic spaces and étale, and `Xᵢ ⟶ Yᵢ` corresponds to a rig-étale map in
>    `WAdm^{Noeth}`;
> 5. for every commutative square as in (2), every presentation of `U ⟶ V` by Noetherian adic rings
>    is rig-étale.
>
> Conditions (1) to (4) are the source's. In (2) the charts `U` and `V` are formal spectra of
> Noetherian adic rings and `U ⟶ V` is the formal spectrum of a rig-étale homomorphism. Condition
> (5) is the library's reading of Definition 0AQM, the form condition (2) takes in
> `isRigEtale_tfae_of_isLocallyNoetherian`; it is recorded so that this statement contains that
> one. Conditions (2) and (5) agree by `correspondsToRigEtaleMapOnEveryAffineEtaleDiagram_iff`,
> which uses Stacks 0AKX, and the remaining implications are those of
> `isRigEtale_tfae_of_isLocallyNoetherian`.

```lean
theorem isRigEtale_tfae_of_isLocallyNoetherian' {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y) :
    List.TFAE
      [IsRigEtale B S hS f,
        CorrespondsToRigEtaleMapOnEveryAffineEtaleDiagram B S hS f,
        CorrespondsToRigEtaleMapAfterTargetCover B S hS f,
        CorrespondsToRigEtaleMapAfterSourceCover B S hS f,
        HasPropertyOnEveryAffineEtaleDiagram B S hS IsNoetherianAdic IsRigEtaleHom f]
```

## Tag 0AQN, a lemma

[Tag 0AQN](https://stacks.math.columbia.edu/tag/0AQN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_of_isRigEtale_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleLocallyOfFiniteTypeUnconditional.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleLocallyOfFiniteTypeUnconditional.lean#L116).

> **Stacks 0AQN.** A rig-étale morphism of locally Noetherian formal algebraic spaces over
> `S` is locally of finite type.
>
> By the implication (1) ⟹ (4) of Stacks 0ANW it suffices that every affine representable étale
> square over `f` has its upper map given by a taut, topologically of finite type morphism of
> `WAdm^{count}`. The two charts of such a square are Noetherian (Stacks 0AKX), so every weakly
> admissible ring presenting them is Noetherian and adic (Stacks 0AIC); rig-étaleness of `f` then
> says that the presenting homomorphism is rig-étale, hence taut and topologically of finite type
> (Stacks 0GBW).

```lean
theorem isLocallyOfFiniteType_of_isRigEtale_of_isLocallyNoetherian {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hf : IsRigEtale B S hS f) :
    IsLocallyOfFiniteType B S hS f
```

## Tag 0GD0, a lemma

[Tag 0GD0](https://stacks.math.columbia.edu/tag/0GD0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_of_isRigEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtale.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtale.lean#L118).

> **Stacks 0GD0.** A rig-étale morphism of formal algebraic spaces is rig-smooth.

```lean
theorem isRigSmooth_of_isRigEtale (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hf : IsRigEtale B S hS f) :
    IsRigSmooth B S hS f
```

## Tag 0GD1, a lemma

[Tag 0GD1](https://stacks.math.columbia.edu/tag/0GD1) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigEtale_pullback_snd_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleBaseChangeCharts.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleBaseChangeCharts.lean#L212).

> Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally Noetherian formal algebraic spaces
> over `S`. If `f` is rig-étale and `g` is adic, then the base change `X ×_Y Z ⟶ Z` is
> rig-étale.

```lean
theorem isRigEtale_pullback_snd_of_isLocallyNoetherian {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Z ⟶ Y) (hX : IsLocallyNoetherian B S hS X)
    (hY : IsLocallyNoetherian B S hS Y) (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsRigEtale B S hS f) (hg : IsAdicMorphism B S hS g) :
    IsRigEtale B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_pullback_snd_of_isAdicMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleStability.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleStability.lean#L163). The attribute's comment: “granting the locality of the cohomology-annihilation half of rig-étaleness, which is the hypothesis hcond and the only input of Stacks 0AQL, together with the three inputs of Remark 0GBG that the library leaves open: the covering of X ×\_Y Z by fibre products of charts of Stacks 0GBD and 0AN0 (hcover), the implication (3) ⟹ (1) of Stacks 0ANG (h31), and the invariance of rig-étaleness under isomorphism of targets implied by Stacks 0ANI (hiso)”.

> **Stacks 0GD1.** The base change of a rig-étale morphism of locally Noetherian formal
> algebraic spaces over `S` by an adic morphism is rig-étale: if `f : X ⟶ Y` is rig-étale and
> `g : Z ⟶ Y` is adic, then `X ×_Y Z ⟶ Z` is rig-étale.

```lean
theorem isRigEtale_pullback_snd_of_isAdicMorphism (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    (hcond : TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        Rig.RigEtaleCondition φ))
    (hiso : PropertyIsInvariantUnderTargetIso.{u}
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigEtaleArrow φ))
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R)
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigEtaleArrow φ))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hcover : HasBaseChangeCoverOverPullbackSnd B S hS f g)
    (_hX : IsLocallyNoetherian B S hS X) (_hY : IsLocallyNoetherian B S hS Y)
    (_hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsRigEtale B S hS f)
    (hg : IsAdicOnEveryAffineEtaleDiagramNoetherian B S hS g) :
    IsRigEtale B S hS (pullback.snd f g)
```

## Tag 0GD2, a lemma

[Tag 0GD2](https://stacks.math.columbia.edu/tag/0GD2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigEtale_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleCompositionCharts.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleCompositionCharts.lean#L196).

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `f` and `g` are rig-étale, then so is `g ∘ f`.

```lean
theorem isRigEtale_comp_of_isLocallyNoetherian {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z) (hf : IsRigEtale B S hS f)
    (hg : IsRigEtale B S hS g) :
    IsRigEtale B S hS (f ≫ g)
```

## Tag 0GD3, a lemma

[Tag 0GD3](https://stacks.math.columbia.edu/tag/0GD3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigEtale_of_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleCompositionCharts.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleCompositionCharts.lean#L229).

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `g ∘ f` and `g` are rig-étale, then so is `f`.

```lean
theorem isRigEtale_of_comp_of_isLocallyNoetherian {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z) (hfg : IsRigEtale B S hS (f ≫ g))
    (hg : IsRigEtale B S hS g) :
    IsRigEtale B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleStability.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleStability.lean#L137). The attribute's comment: “granting the locality of the cohomology-annihilation half of rig-étaleness, which is the hypothesis hcond and the only input of Stacks 0AQL, and the transfer to formal algebraic spaces of Remark 0GBP, which is the hypothesis htransfer”.

> **Stacks 0GD3.** Rig-étaleness of morphisms of locally Noetherian formal algebraic spaces
> over `S` cancels on the right: if `g ∘ f` and `g` are rig-étale, for `f : X ⟶ Y` and
> `g : Y ⟶ Z`, then `f` is rig-étale.

```lean
theorem isRigEtale_of_comp (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hcond : TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        Rig.RigEtaleCondition φ))
    (htransfer : TransfersCancellationOnAffineEtaleDiagrams B S hS)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (_hX : IsLocallyNoetherian B S hS X) (_hY : IsLocallyNoetherian B S hS Y)
    (_hZ : IsLocallyNoetherian B S hS Z)
    (hfg : IsRigEtale B S hS (f ≫ g)) (hg : IsRigEtale B S hS g) :
    IsRigEtale B S hS f
```

## Tag 0GH4, a lemma

[Tag 0GH4](https://stacks.math.columbia.edu/tag/0GH4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigEtale_of_comp_of_isAdicMorphism_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleAdicMonomorphism.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleAdicMonomorphism.lean#L80). The attribute's comment: “granting the locality of the cohomology-annihilation half of rig-étaleness, which is the hypothesis hcond and the only input of Stacks 0AQL, together with the three inputs of Remark 0GBG that the library leaves open and that Stacks 0GD1, the sole cited input of this tag, is itself carried with: the covering by fibre products of charts of Stacks 0GBD and 0AN0 (hcover), the implication (3) ⟹ (1) of Stacks 0ANG (h31), and the invariance of rig-étaleness under isomorphism of targets implied by Stacks 0ANI (hiso)”.

> **Stacks 0GH4.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `g ∘ f` is rig-étale and `g` is an adic monomorphism, then `f` is
> rig-étale: as `g` is a monomorphism, `f` is the base change of `g ∘ f` along `g`, and the base
> change of a rig-étale morphism along an adic morphism is rig-étale.

```lean
theorem isRigEtale_of_comp_of_isAdicMorphism_of_mono (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    (hcond : TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        Rig.RigEtaleCondition φ))
    (hiso : PropertyIsInvariantUnderTargetIso.{u}
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigEtaleArrow φ))
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS
      (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R)
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigEtaleArrow φ))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hcover : HasBaseChangeCoverOverPullbackSnd B S hS (f ≫ g) g)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hfg : IsRigEtale B S hS (f ≫ g))
    (hgadic : IsAdicOnEveryAffineEtaleDiagramNoetherian B S hS g) (hgmono : Mono g) :
    IsRigEtale B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_of_comp_of_isAdicMorphism_of_mono_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleBaseChangeCharts.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleBaseChangeCharts.lean#L224).

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal algebraic spaces
> over `S`. If `g ∘ f` is rig-étale and `g` is an adic monomorphism, then `f` is rig-étale.

```lean
theorem isRigEtale_of_comp_of_isAdicMorphism_of_mono_of_isLocallyNoetherian
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z) (hX : IsLocallyNoetherian B S hS X)
    (hY : IsLocallyNoetherian B S hS Y) (hZ : IsLocallyNoetherian B S hS Z)
    (hfg : IsRigEtale B S hS (f ≫ g)) (hgadic : IsAdicMorphism B S hS g) (hgmono : Mono g) :
    IsRigEtale B S hS f
```

## Tag 0GD4, a lemma

[Tag 0GD4](https://stacks.math.columbia.edu/tag/0GD4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_tfae_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleClosedImmersion.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleClosedImmersion.lean#L250). The attribute's comment: “the full equivalence of the three conditions, with Stacks 0AQI (the fibre product chart map being a surjection of WAdm^Noeth which is adic of topologically finite type) and Stacks 0GCZ (rig-étaleness need only be checked on the ring maps appearing in condition (3)) carried as the hypotheses `hAQI` and `hGCZ`”.

> **Stacks 0GD4.** For a closed immersion `f : X ⟶ Y` of locally Noetherian formal algebraic
> spaces over `S`, rig-smoothness of `f` (Definition 0GCP), rig-étaleness of `f`
> (Definition 0AQM), and the condition that on every affine representable étale chart `V ⟶ Y` of
> the target the fibre product `X ×_Y V ⟶ V` be given by a surjection of `WAdm^{Noeth}` whose
> kernel `J` has `J / J²` annihilated by an ideal of definition of the source, are all equivalent.
>
> The implication (2) ⟹ (1) is Stacks 0GD0.  The implications (1) ⟹ (3) and (3) ⟹ (2) rest on
> the computation of the completed naive cotangent complex of a surjection, for which both
> rigidity notions reduce to the annihilation of the conormal module.  The hypotheses `hAQI` and
> `hGCZ` carry Stacks 0AQI — that the fibre product chart map is a surjection which is adic of
> topologically finite type — and Stacks 0GCZ in the form in which the source's proof uses it,
> that rig-étaleness need only be checked on the ring maps appearing in (3).

```lean
theorem isRigSmooth_tfae_of_isClosedImmersion {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (_hX : IsLocallyNoetherian B S hS X) (_hY : IsLocallyNoetherian B S hS Y)
    (hf : IsClosedImmersion B S hS f)
    (hAQI : HasAdicQuotientOnPullbackCharts B S hS f)
    (hGCZ : HasRigEtaleOnPullbackCharts B S hS f → IsRigEtale B S hS f) :
    List.TFAE
      [IsRigSmooth B S hS f, IsRigEtale B S hS f,
        HasAnnihilatedConormalOnPullbackCharts B S hS f]
```

**`AlgebraicGeometry.FormalSpace.isRigSmooth_tfae_of_isClosedImmersion'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleClosedImmersionCharts.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigEtaleClosedImmersionCharts.lean#L401).

> **Stacks 0GD4.** For a closed immersion `f : X ⟶ Y` of locally Noetherian formal algebraic
> spaces over `S`, rig-smoothness of `f` (Definition 0GCP), rig-étaleness of `f`
> (Definition 0AQM), and the condition that on every affine representable étale chart `V ⟶ Y` of
> the target the fibre product `X ×_Y V ⟶ V` be given by a surjection of `WAdm^{Noeth}` whose
> kernel `J` has `J / J²` annihilated by an ideal of definition of the source, are all equivalent.
>
> The implication (2) ⟹ (1) is Stacks 0GD0. The implication (1) ⟹ (3) uses the surjectivity of
> the fibre product chart homomorphism, `surjective_of_isClosedImmersion_chart`, and the
> computation of the completed naive cotangent complex of a surjection. The implication
> (3) ⟹ (2) is `isRigEtale_of_hasAnnihilatedConormalOnPullbackCharts`.

```lean
theorem isRigSmooth_tfae_of_isClosedImmersion' {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (_hX : IsLocallyNoetherian B S hS X) (_hY : IsLocallyNoetherian B S hS Y)
    (hf : IsClosedImmersion B S hS f) :
    List.TFAE
      [IsRigSmooth B S hS f, IsRigEtale B S hS f,
        HasAnnihilatedConormalOnPullbackCharts B S hS f]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.20, Tag 0AQK](https://stacks.math.columbia.edu/tag/0AQK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
