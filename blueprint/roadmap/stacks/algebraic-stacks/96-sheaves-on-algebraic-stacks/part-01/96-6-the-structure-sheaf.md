---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.structureSheaf, AlgebraicGeometry.FibredSite.inverseImageStructureSheaf_eq, AlgebraicGeometry.FibredSite.ringedToposMorphism, AlgebraicGeometry.FibredSite.ringedToposMorphism_inverseImage, AlgebraicGeometry.FibredSite.ringedToposMorphism_fSharpInverseImage, AlgebraicGeometry.FibredSite.ringedToposMorphism_isIso_fSharpInverseImage, AlgebraicGeometry.Stack.sheafPushforwardContinuous_structureSheaf, AlgebraicGeometry.Stack.structureSheafInverseImageIso
statement: formalized
proof: formalized
---

# 96.6 The structure sheaf

Section 96.6 of the Stacks Project, [Tag 06TU](https://stacks.math.columbia.edu/tag/06TU). 3 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06TV, a definition

[Tag 06TV](https://stacks.math.columbia.edu/tag/06TV) in the Stacks Project.

**`AlgebraicGeometry.Stack.structureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheaf.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheaf.lean#L108).

> The structure sheaf of a category fibred in groupoids, given by inverse image of the
> commutative ring sheaf of the big site of schemes.

```lean
noncomputable def structureSheaf {X : Type v} [Category.{w} X]
    (p : X ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids)
    (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology) :
    Sheaf (associatedTopology B S hS p τ) CommRingCat.{u}
```

## Tag 06TW, a lemma

[Tag 06TW](https://stacks.math.columbia.edu/tag/06TW) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.inverseImageStructureSheaf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean#L64). The attribute's comment: “canonical identification of structure sheaves”.

> For a 1-morphism `F` of categories fibred in groupoids over the big fppf site, the inverse
> image along `F` of the structure sheaf of the target is the structure sheaf of the source, as a
> sheaf of commutative rings and on the nose.

```lean
theorem inverseImageStructureSheaf_eq
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v} [Category.{w} X] {Y : Type v'} [Category.{w'} Y]
    (p : X ⥤ BigFppfOver B S hS)
    (q : Y ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : X ⥤ Y) (hF : p.IsFibredOneMorphism q F)
    (τ : SiteKind) :
    letI := hp.isFibered
    letI := hq.isFibered
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology
      ((B.baseTopology τ).over (B.obj hS))).1
    (F.sheafPushforwardContinuous CommRingCat.{u}
      (BigFppfOver.associatedTopology B S hS p τ)
      (BigFppfOver.associatedTopology B S hS q τ)).obj
        (FibredSite.structureSheaf B S hS q hq τ) =
      FibredSite.structureSheaf B S hS p hp τ
```

**`AlgebraicGeometry.FibredSite.ringedToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean#L135). The attribute's comment: “morphism of ringed topoi”.

> A 1-morphism `F` of categories fibred in groupoids over the big fppf site induces a morphism
> of ringed topoi in the sense of `AlgebraicGeometry.RingedToposHom`, between the two associated
> ringed topoi: the underlying morphism of topoi is the one `F` induces, and its structure map is
> the adjoint of the canonical identification
> `AlgebraicGeometry.FibredSite.inverseImageStructureSheaf_eq`.

```lean
noncomputable def ringedToposMorphism
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v} [Category.{w} X] {Y : Type v'} [Category.{w'} Y]
    (p : X ⥤ BigFppfOver B S hS)
    (q : Y ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : X ⥤ Y) (hF : p.IsFibredOneMorphism q F)
    (τ : SiteKind)
    [∀ (G : Xᵒᵖ ⥤ Type u), F.op.HasPointwiseRightKanExtension G] :
    RingedToposHom
      (associatedRingedTopos B S hS p hp τ)
      (associatedRingedTopos B S hS q hq τ)
```

**`AlgebraicGeometry.FibredSite.ringedToposMorphism_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean#L173). The attribute's comment: “inverse image of the underlying geometric morphism”.

> The morphism of ringed topoi `AlgebraicGeometry.FibredSite.ringedToposMorphism` sits over
> the morphism of topoi that `F` itself induces: its inverse image is restriction of sheaves along
> `F` for the two inherited topologies.

```lean
theorem ringedToposMorphism_inverseImage
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v} [Category.{w} X] {Y : Type v'} [Category.{w'} Y]
    (p : X ⥤ BigFppfOver B S hS)
    (q : Y ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : X ⥤ Y) (hF : p.IsFibredOneMorphism q F)
    (τ : SiteKind)
    [∀ (G : Xᵒᵖ ⥤ Type u), F.op.HasPointwiseRightKanExtension G] :
    letI := hp.isFibered
    letI := hq.isFibered
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology
      ((B.baseTopology τ).over (B.obj hS))).1
    (ringedToposMorphism B S hS p q hp hq F hF τ).toToposHom.inverseImage =
      F.sheafPushforwardContinuous (Type u)
        (BigFppfOver.associatedTopology B S hS p τ)
        (BigFppfOver.associatedTopology B S hS q τ)
```

**`AlgebraicGeometry.FibredSite.ringedToposMorphism_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean#L196). The attribute's comment: “canonical structure map”.

> The inverse-image form of the structure map of
> `AlgebraicGeometry.FibredSite.ringedToposMorphism` is the canonical identification itself: the
> comparison of the inverse image of a sheaf of commutative rings with its restriction, followed
> by the equality `AlgebraicGeometry.FibredSite.inverseImageStructureSheaf_eq`.

```lean
theorem ringedToposMorphism_fSharpInverseImage
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v} [Category.{w} X] {Y : Type v'} [Category.{w'} Y]
    (p : X ⥤ BigFppfOver B S hS)
    (q : Y ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : X ⥤ Y) (hF : p.IsFibredOneMorphism q F)
    (τ : SiteKind)
    [∀ (G : Xᵒᵖ ⥤ Type u), F.op.HasPointwiseRightKanExtension G] :
    letI := hp.isFibered
    letI := hq.isFibered
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology
      ((B.baseTopology τ).over (B.obj hS))).1
    (ringedToposMorphism B S hS p q hp hq F hF τ).fSharpInverseImage =
      (restrictionCommRingIso
        (BigFppfOver.associatedTopology B S hS p τ)
        (BigFppfOver.associatedTopology B S hS q τ) F
        (FibredSite.structureSheaf B S hS q hq τ)).hom ≫
        eqToHom (inverseImageStructureSheaf_eq B S hS p q hp hq F hF τ)
```

**`AlgebraicGeometry.FibredSite.ringedToposMorphism_isIso_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StructureSheafFunctoriality.lean#L233). The attribute's comment: “canonical identification gives an isomorphism of structure sheaves”.

> The inverse-image form of the structure map of
> `AlgebraicGeometry.FibredSite.ringedToposMorphism` is an isomorphism.

```lean
theorem ringedToposMorphism_isIso_fSharpInverseImage
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v} [Category.{w} X] {Y : Type v'} [Category.{w'} Y]
    (p : X ⥤ BigFppfOver B S hS)
    (q : Y ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : X ⥤ Y) (hF : p.IsFibredOneMorphism q F)
    (τ : SiteKind)
    [∀ (G : Xᵒᵖ ⥤ Type u), F.op.HasPointwiseRightKanExtension G] :
    IsIso (ringedToposMorphism B S hS p q hp hq F hF τ).fSharpInverseImage
```

**`AlgebraicGeometry.Stack.sheafPushforwardContinuous_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean#L85). The attribute's comment: “the canonical identification of structure sheaves”.

> **Stacks 06TW.** The inverse image of the structure sheaf of `𝒴` along a 1-morphism `F` is
> the structure sheaf of `𝒳`, as an equality of sheaves of commutative rings: being a 1-morphism
> means `p = F ⋙ q` on the nose, and both structure sheaves are restrictions of one and the same
> structure sheaf of the base.

```lean
theorem sheafPushforwardContinuous_structureSheaf (hF : F ⋙ q = p)
    [F.IsContinuous (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)] :
    (F.sheafPushforwardContinuous CommRingCat.{u} (associatedTopology B S hS p τ)
          (associatedTopology B S hS q τ)).obj (structureSheaf B S hS q hq τ hτ) =
      structureSheaf B S hS p hp τ hτ
```

**`AlgebraicGeometry.Stack.structureSheafInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean#L141). The attribute's comment: “the structure sheaves are identified by the morphism of topoi”.

> **Stacks 06TW.** The inverse image of the structure sheaf of `𝒴` is the structure sheaf of
> `𝒳`, as sheaves of commutative rings on the associated site of `𝒳`: the inverse image of a
> sheaf of commutative rings along a morphism of topoi presented by restriction is restriction,
> and restriction of the structure sheaf of `𝒴` along `F` is the structure sheaf of `𝒳`.

```lean
noncomputable def structureSheafInverseImageIso :
    (inverseImageCommRingFunctor
          (associatedToposMorphism B S hS p q F hp hq τ hF)).obj (structureSheaf B S hS q hq τ hτ) ≅
      structureSheaf B S hS p hp τ hτ
```

**`AlgebraicGeometry.Stack.associatedRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean#L156). The attribute's comment: “the morphism of ringed topoi”.

> **Stacks 06TW.** The morphism of ringed topoi induced by a 1-morphism of categories fibred
> in groupoids: the morphism of topoi of Stacks 06NW together with the structure map adjoint to
> the identification of the structure sheaves.

```lean
noncomputable def associatedRingedToposHom :
    RingedToposHom (associatedRingedTopos B S hS p hp τ hτ)
      (associatedRingedTopos B S hS q hq τ hτ)
```

**`AlgebraicGeometry.Stack.fSharpInverseImage_associatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean#L173). The attribute's comment: “the structure map is the canonical identification”.

> **Stacks 06TW.** The structure map of the induced morphism of ringed topoi is, in
> inverse-image form, exactly the identification of the structure sheaves.

```lean
theorem fSharpInverseImage_associatedRingedToposHom :
    (associatedRingedToposHom B S hS p q F hp hq τ hτ hF).fSharpInverseImage =
      (structureSheafInverseImageIso B S hS p q F hp hq τ hτ hF).hom
```

**`AlgebraicGeometry.Stack.isIso_fSharpInverseImage_associatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctoriality.lean#L183). The attribute's comment: “the structure map is an isomorphism”.

> **Stacks 06TW.** The structure map of the induced morphism of ringed topoi is an
> isomorphism, so the morphism of ringed topoi is a morphism of ringed topoi with invertible
> structure map.

```lean
theorem isIso_fSharpInverseImage_associatedRingedToposHom :
    IsIso (associatedRingedToposHom B S hS p q F hp hq τ hτ hF).fSharpInverseImage
```

## Tag 06TX, a remark

[Tag 06TX](https://stacks.math.columbia.edu/tag/06TX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFlat_associatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctorialityFlat.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctorialityFlat.lean#L113). The attribute's comment: “flatness of the morphism of ringed topoi of a 1-morphism”.

> **Stacks 06TX.** The morphism of ringed topoi `f : Sh(𝒳_τ) → Sh(𝒴_τ)` induced by a 1-morphism
> of categories fibred in groupoids is flat: its structure map in inverse-image form is the
> identification `f⁻¹O_𝒴 = O_𝒳` of Stacks 06TW, and an isomorphism of sheaves of commutative rings
> makes its target a flat module over its source.

```lean
theorem isFlat_associatedRingedToposHom :
    RingedToposHom.IsFlat
      (X := associatedRingedTopos B S hS p hp τ hτ)
      (Y := associatedRingedTopos B S hS q hq τ hτ)
      (associatedRingedToposHom B S hS p q F hp hq τ hτ hF)
```

**`AlgebraicGeometry.Stack.isFlat_associatedRingedToposHom_overMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctorialityFlat.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafFunctorialityFlat.lean#L172). The attribute's comment: “flatness of the morphism of big τ-sites of a morphism of schemes”.

> **Stacks 06TX**, the second assertion. For a morphism `i : X ⟶ Y` of schemes over `S` the
> induced morphism of ringed big `τ`-sites `i : (Sch/X)_τ → (Sch/Y)_τ` is flat, for the same reason:
> the two structure sheaves are restrictions of one and the same structure sheaf of the base, so the
> inverse-image structure map is an isomorphism.
>
> The source states this for a closed immersion; no hypothesis on `i` is used, which is the point
> the remark makes.

```lean
theorem isFlat_associatedRingedToposHom_overMap :
    RingedToposHom.IsFlat
      (X := associatedRingedTopos B S hS (Over.map X.hom) (.over_map X.hom) τ hτ)
      (Y := associatedRingedTopos B S hS (Over.map Y.hom) (.over_map Y.hom) τ hτ)
      (associatedRingedToposHom B S hS (Over.map X.hom) (Over.map Y.hom) (Over.map i.left)
        (.over_map X.hom) (.over_map Y.hom) τ hτ (isFibredOneMorphism_overMap X Y i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.6, Tag 06TU](https://stacks.math.columbia.edu/tag/06TU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
