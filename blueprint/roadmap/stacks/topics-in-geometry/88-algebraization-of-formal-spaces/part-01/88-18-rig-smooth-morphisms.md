---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsRigSmooth, AlgebraicGeometry.FormalSpace.isRigSmooth_iff_hasPropertyOnEveryAffineEtaleDiagram, AlgebraicGeometry.FormalSpace.isRigSmooth_tfae, AlgebraicGeometry.FormalSpace.isRigSmooth_tfae_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.isRigSmooth_pullback_snd, AlgebraicGeometry.FormalSpace.isRigSmooth_comp_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.isRigFlat_of_isRigSmooth
statement: formalized
proof: formalized
---

# 88.18 Rig-smooth morphisms

Section 88.18 of the Stacks Project, [Tag 0GCN](https://stacks.math.columbia.edu/tag/0GCN). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GCP, a definition

[Tag 0GCP](https://stacks.math.columbia.edu/tag/0GCP) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmooth.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmooth.lean#L66).

> **Stacks 0GCP.** A morphism of formal algebraic spaces over `S` is *rig-smooth* when every
> morphism between affine, representable, étale charts of its source and target is induced by a
> rig-smooth continuous homomorphism of adic Noetherian topological rings.

```lean
abbrev IsRigSmooth (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0GCQ, a lemma

[Tag 0GCQ](https://stacks.math.columbia.edu/tag/0GCQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_iff_hasPropertyOnEveryAffineEtaleDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmooth.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmooth.lean#L97). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0GCQ, conditions (1) and (2).** A morphism of formal algebraic spaces over `S` is
> rig-smooth exactly when rig-smoothness as a property of arrows of `WAdm^{Noeth}` holds on every
> affine étale diagram over it: the two conditions are the same, which is what Definition 0GCP
> says.

```lean
theorem isRigSmooth_iff_hasPropertyOnEveryAffineEtaleDiagram (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsRigSmooth B S hS f ↔
      HasPropertyOnEveryAffineEtaleDiagram B S hS
        (fun R ↦ TopologicalRing.IsAdic R ∧ IsNoetherianRing R)
        (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
          [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
          RingHom.IsRigSmoothArrow φ) f
```

**`AlgebraicGeometry.FormalSpace.isRigSmooth_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothCharacterization.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothCharacterization.lean#L81).

> **Stacks 0GCQ.** For a morphism `f : X ⟶ Y` of locally Noetherian formal algebraic spaces
> over `S`, the following are equivalent: `f` is rig-smooth (Definition 0GCP); every commutative
> square with affine formal algebraic spaces `U`, `V` and representable étale maps `U ⟶ X`,
> `V ⟶ Y` has `U ⟶ V` given by a rig-smooth arrow of `WAdm^{Noeth}`; there are an affine étale
> covering `{Yⱼ ⟶ Y}` and, for each `j`, an affine étale covering `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` with every
> `Xⱼᵢ ⟶ Yⱼ` given by a rig-smooth arrow of `WAdm^{Noeth}`; and there is an affine étale covering
> `{Xᵢ ⟶ X}` with factorizations `Xᵢ ⟶ Yᵢ ⟶ Y` through affine formal algebraic spaces
> representable étale over `Y` with every `Xᵢ ⟶ Yᵢ` given by a rig-smooth arrow of
> `WAdm^{Noeth}`.

```lean
theorem isRigSmooth_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y) :
    List.TFAE
      [IsRigSmooth B S hS f,
        HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic
          (fun φ ↦ RingHom.IsRigSmoothArrow φ) f,
        HasPropertyAfterTargetCover B S hS TopologicalRing.IsNoetherianAdic
          (fun φ ↦ RingHom.IsRigSmoothArrow φ) f,
        HasPropertyAfterSourceCover B S hS TopologicalRing.IsNoetherianAdic
          (fun φ ↦ RingHom.IsRigSmoothArrow φ) f]
```

**`AlgebraicGeometry.FormalSpace.isRigSmooth_tfae_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothLocalCharacterization.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothLocalCharacterization.lean#L103).

> **Stacks 0GCQ.** Let `f : X ⟶ Y` be a morphism of locally Noetherian formal algebraic spaces
> over `S`. The following are equivalent:
>
> 1. `f` is rig-smooth (Definition 0GCP);
> 2. for every commutative square with `U`, `V` affine formal algebraic spaces and `U ⟶ X`,
>    `V ⟶ Y` representable by algebraic spaces and étale, the morphism `U ⟶ V` corresponds to a
>    rig-smooth map in `WAdm^{Noeth}`;
> 3. there exist a covering `{Yⱼ ⟶ Y}` as in Definition 0AIM and for each `j` a covering
>    `{Xⱼᵢ ⟶ Yⱼ ×_Y X}` as in Definition 0AIM such that each `Xⱼᵢ ⟶ Yⱼ` corresponds to a
>    rig-smooth map in `WAdm^{Noeth}`;
> 4. there exist a covering `{Xᵢ ⟶ X}` as in Definition 0AIM and for each `i` a factorization
>    `Xᵢ ⟶ Yᵢ ⟶ Y` where `Yᵢ` is an affine formal algebraic space, `Yᵢ ⟶ Y` is representable by
>    algebraic spaces and étale, and `Xᵢ ⟶ Yᵢ` corresponds to a rig-smooth map in
>    `WAdm^{Noeth}`.
>
> In (2), (3) and (4) "corresponds to a rig-smooth map in `WAdm^{Noeth}`" is
> `CorrespondsToNoetherianMap` for rig-smoothness: source and target are formal spectra of
> Noetherian adic rings and the map is the formal spectrum of a rig-smooth homomorphism.

```lean
theorem isRigSmooth_tfae_of_isLocallyNoetherian {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y) :
    List.TFAE
      [IsRigSmooth B S hS f,
        CorrespondsToNoetherianMapOnEveryAffineEtaleDiagram B S hS
          (fun φ ↦ RingHom.IsRigSmoothArrow φ) f,
        CorrespondsToNoetherianMapAfterTargetCover B S hS (fun φ ↦ RingHom.IsRigSmoothArrow φ) f,
        CorrespondsToNoetherianMapAfterSourceCover B S hS
          (fun φ ↦ RingHom.IsRigSmoothArrow φ) f]
```

## Tag 0GCR, a lemma

[Tag 0GCR](https://stacks.math.columbia.edu/tag/0GCR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothPullback.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothPullback.lean#L60).

> **Stacks 0GCR.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `f` is rig-smooth and `g` is adic, then the base change
> `X ×_Y Z ⟶ Z` is rig-smooth.

```lean
theorem isRigSmooth_pullback_snd {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z) (hf : IsRigSmooth B S hS f)
    (hg : IsAdicMorphism B S hS g) :
    IsRigSmooth B S hS (pullback.snd f g)
```

## Tag 0GCS, a lemma

[Tag 0GCS](https://stacks.math.columbia.edu/tag/0GCS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothCompositionLocallyNoetherian.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothCompositionLocallyNoetherian.lean#L57).

> **Stacks 0GCS.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `f` and `g` are rig-smooth, then so is `g ∘ f`.

```lean
theorem isRigSmooth_comp_of_isLocallyNoetherian (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsRigSmooth B S hS f) (hg : IsRigSmooth B S hS g) :
    IsRigSmooth B S hS (f ≫ g)
```

## Tag 0GH3, a lemma

[Tag 0GH3](https://stacks.math.columbia.edu/tag/0GH3) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigFlat_of_isRigSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigFlat.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigFlat.lean#L46).

> **Stacks 0GH3.** A rig-smooth morphism of locally Noetherian formal algebraic spaces over
> `S` is rig-flat.

```lean
theorem isRigFlat_of_isRigSmooth (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hf : IsRigSmooth B S hS f) : IsRigFlat B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.18, Tag 0GCN](https://stacks.math.columbia.edu/tag/0GCN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
