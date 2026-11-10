---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsRigFlat, AlgebraicGeometry.FormalSpace.hasRigFlatSourceCovering_of_hasRigFlatTargetCovering, AlgebraicGeometry.FormalSpace.isRigFlat_tfae_of_isLocallyNoetherian, AlgebraicGeometry.FormalSpace.isRigFlat_pullback_snd, AlgebraicGeometry.FormalSpace.isRigFlat_comp, AlgebraicGeometry.FormalSpace.isRigFlat_comp_of_isLocallyNoetherian
statement: formalized
proof: formalized
---

# 88.16 Rig-flat morphisms

Section 88.16 of the Stacks Project, [Tag 0GGW](https://stacks.math.columbia.edu/tag/0GGW). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GGX, a definition

[Tag 0GGX](https://stacks.math.columbia.edu/tag/0GGX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlat.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlat.lean#L62).

> **Stacks 0GGX.** A morphism of formal algebraic spaces over `S` is *rig-flat* when every
> morphism between affine, representable, étale charts of its source and target is induced by a
> rig-flat continuous homomorphism of adic Noetherian topological rings.

```lean
abbrev IsRigFlat (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0GGY, a lemma

[Tag 0GGY](https://stacks.math.columbia.edu/tag/0GGY) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasRigFlatSourceCovering_of_hasRigFlatTargetCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatCriteria.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatCriteria.lean#L157). The attribute's comment: “(3) ⟹ (4)”.

> **Stacks 0GGY, (3) ⟹ (4).** A target covering witnessing rig-flatness on charts yields a
> source covering witnessing it: the two coverings of condition (3) compose into one covering of
> the source, and each of its members factors through the chart of the target covering it lies
> over.

```lean
theorem hasRigFlatSourceCovering_of_hasRigFlatTargetCovering
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (h : HasRigFlatTargetCovering B S hS f) :
    HasRigFlatSourceCovering B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigFlat_tfae_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatCriteriaLocallyNoetherian.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatCriteriaLocallyNoetherian.lean#L98).

> **Stacks 0GGY.** For a morphism `f : X ⟶ Y` of locally Noetherian formal algebraic spaces
> over `S`, the following are equivalent: `f` is rig-flat (Definition 0GGX); every commutative
> square whose verticals are affine formal algebraic spaces representable étale over `X` and `Y`
> carries a rig-flat arrow of `WAdm^Noeth` on its top side; there are an affine étale covering of
> `Y` and affine étale coverings of the fibre products of its members with `X` whose members map
> to the corresponding chart of `Y` by rig-flat maps of `WAdm^Noeth`; there is an affine étale
> covering of `X` whose members factor through affine formal algebraic spaces representable étale
> over `Y` by rig-flat maps of `WAdm^Noeth`.

```lean
theorem isRigFlat_tfae_of_isLocallyNoetherian {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y) :
    List.TFAE
      [IsRigFlat B S hS f,
        HasPropertyOnEveryAffineEtaleDiagram B S hS TopologicalRing.IsNoetherianAdic
          (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
            [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
            Rig.RingHom.IsRigFlat φ) f,
        HasRigFlatTargetCovering B S hS f,
        HasRigFlatSourceCovering B S hS f]
```

## Tag 0GGZ, a lemma

[Tag 0GGZ](https://stacks.math.columbia.edu/tag/0GGZ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigFlat_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatPullback.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatPullback.lean#L86).

> **Stacks 0GGZ.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `f` is rig-flat and `g` is locally of finite type, then the base
> change `X ×_Y Z ⟶ Z` is rig-flat.

```lean
theorem isRigFlat_pullback_snd {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z) (hf : IsRigFlat B S hS f)
    (hg : IsLocallyOfFiniteType B S hS g) :
    IsRigFlat B S hS (pullback.snd f g)
```

## Tag 0GH0, a lemma

[Tag 0GH0](https://stacks.math.columbia.edu/tag/0GH0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigFlat_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatComposition.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatComposition.lean#L312). The attribute's comment: “the composite is rig-flat, with the geometric half of Stacks 0GBK as a hypothesis”.

> **Stacks 0GH0.** A composite of rig-flat morphisms of locally Noetherian formal algebraic
> spaces is rig-flat: if `f : X ⟶ Y` and `g : Y ⟶ Z` are rig-flat, then so is `g ∘ f`.

```lean
theorem isRigFlat_comp (htransfer : TransfersCompositionOnAffineEtaleDiagrams B S hS)
    (f : X ⟶ Y) (g : Y ⟶ Z) (hf : IsRigFlat B S hS f) (hg : IsRigFlat B S hS g) :
    IsRigFlat B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.isRigFlat_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatCompositionLocallyNoetherian.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/RigFlatCompositionLocallyNoetherian.lean#L63).

> **Stacks 0GH0.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal
> algebraic spaces over `S`. If `f` and `g` are rig-flat, then so is `g ∘ f`.

```lean
theorem isRigFlat_comp_of_isLocallyNoetherian {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z) (hf : IsRigFlat B S hS f) (hg : IsRigFlat B S hS g) :
    IsRigFlat B S hS (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.16, Tag 0GGW](https://stacks.math.columbia.edu/tag/0GGW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
