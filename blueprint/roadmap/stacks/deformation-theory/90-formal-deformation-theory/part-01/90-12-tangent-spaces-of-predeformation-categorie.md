---
declaration: section
origin: cited
lean: Deformation.predeformationTangentSpace, Deformation.associatedTangentSpaceModuleStructure, Deformation.associatedTangentSpaceFunctor_iso_tensorLeft, Deformation.associatedTangentSpaceFunctor_iso_tensorLeft_pure, Deformation.associatedTangentSpaceFunctor_iso_tensorLeft_naturality, Deformation.associatedTangentSpaceFunctorConditions, associatedTangentSpaceAddCommGroupUnlifted, associatedTangentSpaceModuleUnlifted
statement: formalized
proof: formalized
---

# 90.12 Tangent spaces of predeformation categories

Section 90.12 of the Stacks Project, [Tag 06I1](https://stacks.math.columbia.edu/tag/06I1). 8 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06IG, a definition

[Tag 06IG](https://stacks.math.columbia.edu/tag/06IG) in the Stacks Project.

**`Deformation.predeformationTangentSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/DerivationAction.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/DerivationAction.lean#L207). References: SGA 7 VI (1.18).

> The tangent space of a predeformation category, formed from its associated functor of
> isomorphism classes.

```lean
noncomputable abbrev predeformationTangentSpace
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p) : Type u₁
```

## Tag 06IH, a lemma

[Tag 06IH](https://stacks.math.columbia.edu/tag/06IH) in the Stacks Project.

**`Deformation.associatedTangentSpaceModuleStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean#L638). The attribute's comment: “natural vector space structure”.

> **Stacks Project, Tag 06IH.** The natural `k`-linear structure on the values of the
> associated functor at finite-dimensional square-zero extensions. In particular its value on
> `k[ε]` is the tangent space of the predeformation category.

```lean
noncomputable def associatedTangentSpaceModuleStructure
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) :
    LinearFunctorLift k
      (squareZeroExtensionArtinian.{u, w, max v w} Λ k ⋙
        isomorphismClasses 𝓕 h𝓕.cofibered)
```

**`Deformation.associatedTangentSpaceFunctor_iso_tensorLeft`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean#L863). The attribute's comment: “tensor equivalence”. References: SGA 7 VI (1.3(c)), “T ⊗ V ≅ [A(k[V])]”; SGA 7 VI (1.18), “(1)”.

> **Stacks Project, Tag 06IH.** The canonical equivalence from tangent vectors tensored
> with `V` to the associated functor evaluated on `k[V]`.

```lean
noncomputable def associatedTangentSpaceFunctor_iso_tensorLeft
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) :
    let L := (associatedTangentSpaceModuleStructure.{u, v, w} 𝓕 h𝓕 hS2).functor
    letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨h𝓕⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) := ⟨hS2⟩
    let T := tangentSpaceArtinian.{u, w, v} Λ k (isomorphismClasses 𝓕 h𝓕.cofibered)
    ∀ V : FGModuleCat.{max v w} k,
      LinearEquiv (RingHom.id k) (TensorProduct k T V)
        ((L.obj V : ModuleCat.{u₁} k) : Type u₁)
```

**`Deformation.associatedTangentSpaceFunctor_iso_tensorLeft_pure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean, line 879](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean#L879). The attribute's comment: “pure-tensor formula”.

> **Stacks Project, Tag 06IH.** On pure tensors, the canonical equivalence is induced by the
> map `ULift k → V` carrying `1` to `v`.

```lean
theorem associatedTangentSpaceFunctor_iso_tensorLeft_pure
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) :
    let L := (associatedTangentSpaceModuleStructure.{u, v, w} 𝓕 h𝓕 hS2).functor
    letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨h𝓕⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) := ⟨hS2⟩
    let T := tangentSpaceArtinian.{u, w, v} Λ k (isomorphismClasses 𝓕 h𝓕.cofibered)
    ∀ (V : FGModuleCat.{max v w} k) (t : T) (v : V),
      associatedTangentSpaceFunctor_iso_tensorLeft.{u, v, w} 𝓕 h𝓕 hS2 V (t ⊗ₜ[k] v) =
        (L.map (FGModuleCat.ofHom
          (LinearMap.smulRight (ULift.moduleEquiv : ULift.{v} k ≃ₗ[k] k).toLinearMap v))).hom
          (cast (associatedTangentSpaceModuleStructure_carrier.{u, v, w}
            𝓕 h𝓕 hS2).symm t)
```

**`Deformation.associatedTangentSpaceFunctor_iso_tensorLeft_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean, line 906](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/TangentVectorSpace.lean#L906). The attribute's comment: “naturality”.

> **Stacks Project, Tag 06IH.** The canonical tensor equivalences commute with every linear
> map between finite-dimensional vector spaces.

```lean
theorem associatedTangentSpaceFunctor_iso_tensorLeft_naturality
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) :
    let L := (associatedTangentSpaceModuleStructure.{u, v, w} 𝓕 h𝓕 hS2).functor
    letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨h𝓕⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) := ⟨hS2⟩
    let T := tangentSpaceArtinian.{u, w, v} Λ k (isomorphismClasses 𝓕 h𝓕.cofibered)
    ∀ (V W : FGModuleCat.{max v w} k) (f : V ⟶ W) (z : TensorProduct k T V),
      (L.map f).hom
          (associatedTangentSpaceFunctor_iso_tensorLeft.{u, v, w} 𝓕 h𝓕 hS2 V z) =
        associatedTangentSpaceFunctor_iso_tensorLeft.{u, v, w} 𝓕 h𝓕 hS2 W
          (TensorProduct.map (LinearMap.id : T →ₗ[k] T) f.hom.hom z)
```

**`Deformation.associatedTangentSpaceFunctorConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/AssociatedTangentSpace.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/AssociatedTangentSpace.lean#L546). The attribute's comment: “tangent-space functor conditions”.

> **Stacks Project, Tag 06IH.** Schlessinger's condition (S2) for the associated functor
> of a predeformation category supplies the singleton and binary-product conditions that the
> natural module structure of Stacks 06IA requires.

```lean
theorem associatedTangentSpaceFunctorConditions
    (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsPredeformationCategory 𝓕.p)
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) :
    TangentSpaceFunctorConditions Λ k (artinianLocalOver Λ k)
      (squareZeroExtension_mem_artinianLocalOver Λ k)
      (artinianLocalOverToArtinian Λ k ⋙ isomorphismClasses 𝓕 h𝓕.cofibered)
```

Declarations registered for the tag:

- [`associatedTangentSpaceAddCommGroupUnlifted`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=associatedTangentSpaceAddCommGroupUnlifted#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Schlessinger/AssociatedTangentSpace.lean, line 573](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/AssociatedTangentSpace.lean#L573) (StacksFrontier): “additive structure”.
- [`associatedTangentSpaceModuleUnlifted`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=associatedTangentSpaceModuleUnlifted#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Schlessinger/AssociatedTangentSpace.lean, line 575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Schlessinger/AssociatedTangentSpace.lean#L575) (StacksFrontier): “scalar structure”.

## Tag 06II, a definition

[Tag 06II](https://stacks.math.columbia.edu/tag/06II) in the Stacks Project.

**`Deformation.differential`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Predeformation.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Predeformation.lean#L96).

> **Stacks Project, Tag 06II.** The differential is the map on associated
> isomorphism-class functors evaluated at the dual numbers.

```lean
noncomputable abbrev differential
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p)
    (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) :
    artinianTangentSpace Λ k (isomorphismClasses 𝓕 h𝓕) →
      artinianTangentSpace Λ k (isomorphismClasses 𝓖 h𝓖)
```

## Tag 06IJ, a lemma

[Tag 06IJ](https://stacks.math.columbia.edu/tag/06IJ) in the Stacks Project.

**`Deformation.differential_isLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/DifferentialLinear.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/DifferentialLinear.lean#L168).

> **Stacks Project, Tag 06IJ.** The differential of a morphism of predeformation categories
> is `k`-linear for the natural tangent-space vector structures when both associated functors
> satisfy (S2).

```lean
theorem differential_isLinearMap
    (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsPredeformationCategory 𝓕.p)
    (h𝓖 : IsPredeformationCategory 𝓖.p)
    (hS2𝓕 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered)))
    (hS2𝓖 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓖 h𝓖.cofibered)))
    (φ : BasedFunctor 𝓕 𝓖) :
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨h𝓕⟩
    letI : Fact (IsPredeformationCategory 𝓖.p) := ⟨h𝓖⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) := ⟨hS2𝓕⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓖 h𝓖.cofibered))) := ⟨hS2𝓖⟩
    IsLinearMap k (differential h𝓕.cofibered h𝓖.cofibered φ)
```

**`Deformation.mapIsomorphismClasses_isLinearMap_artinianDualNumbers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean#L134). The attribute's comment: “lifted dual numbers”.

> **Stacks Project, Tag 06IJ.** The map induced on associated functors of isomorphism classes
> by a morphism of predeformation categories is `k`-linear at the universe-lifted dual numbers,
> when both associated functors satisfy (S2).
>
> This is `Deformation.differential_isLinearMap` for the universe-lifted presentation of the
> dual numbers used by the tangent space at a point.

```lean
theorem mapIsomorphismClasses_isLinearMap_artinianDualNumbers
    (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (h𝓕 : IsPredeformationCategory.{u, v, w} 𝓕.p)
    (h𝓖 : IsPredeformationCategory.{u, v, w} 𝓖.p)
    (hS2𝓕 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered)))
    (hS2𝓖 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓖 h𝓖.cofibered)))
    (φ : BasedFunctor 𝓕 𝓖) :
    letI : Fact (IsPredeformationCategory.{u, v, w} 𝓕.p) := ⟨h𝓕⟩
    letI : Fact (IsPredeformationCategory.{u, v, w} 𝓖.p) := ⟨h𝓖⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered))) := ⟨hS2𝓕⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓖 h𝓖.cofibered))) := ⟨hS2𝓖⟩
    IsLinearMap k (mapIsomorphismClasses h𝓕.cofibered h𝓖.cofibered φ
      (artinianDualNumbers.{u, w, v} Λ k))
```

## Tag 06IK, a remark

[Tag 06IK](https://stacks.math.columbia.edu/tag/06IK) in the Stacks Project.

**`Deformation.tangentSpaceAtPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Predeformation.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Predeformation.lean#L118). The attribute's comment: “tangent\_space\_at\_a\_point”.

> The tangent space of a category cofibered over `𝒞_Λ` at a point over `k`:
> the tangent space of its slice predeformation category.

```lean
noncomputable abbrev tangentSpaceAtPoint
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) : Type (max u₁ v₁)
```

**`Deformation.sliceBasedFunctorAtPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Predeformation.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Predeformation.lean#L154). The attribute's comment: “differential\_at\_point”.

> The morphism of slice predeformation categories induced by a based functor:
> it sends an arrow `y ⟶ x` to its image arrow `φ(y) ⟶ φ(x)`.

```lean
def sliceBasedFunctorAtPoint
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    BasedFunctor
      (BasedCategory.ofFunctor
        (objectsOverFunctor p x.1))
      (BasedCategory.ofFunctor
        (objectsOverFunctor q (imagePoint φ x).1))
```

**`Deformation.differentialAtPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Predeformation.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Predeformation.lean#L175). The attribute's comment: “differential\_at\_point”.

> The differential of a morphism of cofibered categories at a point over `k`:
> the differential of its induced morphism between slice predeformation categories.

```lean
noncomputable abbrev differentialAtPoint
    (hp : IsCofiberedInGroupoids p)
    (hq : IsCofiberedInGroupoids q)
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    tangentSpaceAtPoint p hp x →
      tangentSpaceAtPoint q hq (imagePoint φ x)
```

**`Deformation.tangentSpaceAtPointAddCommGroup`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean#L90). The attribute's comment: “vector\_space\_structure”.

> **Stacks Project, Tag 06IK.** The additive group underlying the natural `k`-vector space
> structure on the tangent space of a category cofibered in groupoids at a point over the
> residue field, available when the category satisfies Schlessinger's condition (S2).

```lean
noncomputable instance tangentSpaceAtPointAddCommGroup
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    [hS2 : Fact (SchlessingerConditionS2 p)]
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    AddCommGroup (tangentSpaceAtPoint.{u, v, w} p hp x)
```

**`Deformation.tangentSpaceAtPointModule`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean#L105). The attribute's comment: “vector\_space\_structure”.

> **Stacks Project, Tag 06IK.** The natural action of the residue field on the tangent space
> of a category cofibered in groupoids at a point over the residue field, available when the
> category satisfies Schlessinger's condition (S2).

```lean
noncomputable instance tangentSpaceAtPointModule
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    [hS2 : Fact (SchlessingerConditionS2 p)]
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    Module k (tangentSpaceAtPoint.{u, v, w} p hp x)
```

**`Deformation.differentialAtPoint_isLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean#L231). The attribute's comment: “differential\_at\_point\_linear”.

> **Stacks Project, Tag 06IK.** If both categories cofibered in groupoids satisfy
> Schlessinger's condition (S2), then the differential of a morphism between them at a point over
> the residue field is `k`-linear for the natural vector space structures on the tangent spaces
> at that point and its image.

```lean
theorem differentialAtPoint_isLinearMap
    (hp : IsCofiberedInGroupoids p)
    (hq : IsCofiberedInGroupoids q)
    (hS2p : SchlessingerConditionS2 p)
    (hS2q : SchlessingerConditionS2 q)
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    letI : Fact (SchlessingerConditionS2 p) := ⟨hS2p⟩
    letI : Fact (SchlessingerConditionS2 q) := ⟨hS2q⟩
    IsLinearMap k (differentialAtPoint.{u, v, w} hp hq φ x)
```

## Tag 06SU, a lemma

[Tag 06SU](https://stacks.math.columbia.edu/tag/06SU) in the Stacks Project.

**`Deformation.action_eq_add_gamma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/DerivationActionTranslation.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/DerivationActionTranslation.lean#L78). The attribute's comment: “action\_translation”.

> **Stacks Project, Tag 06SU.** The derivation action on deformations over `k[V]` is
> translation by the image of the derivation under the canonical derivation map.

```lean
theorem action_eq_add_gamma
    (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsPredeformationCategory 𝓕.p)
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered)))
    (V : FGModuleCat.{w} k)
    (A₀ : ArtinianLocalAlgCat.{u, w, w} Λ k)
    (i₀ : A₀ ≃ₐ[Λ] k)
    (hi₀ : ∀ a : A₀, A₀.residueEquiv (IsLocalRing.residue A₀ a) = i₀ a)
    (x₀ : 𝓕.obj) (hx₀ : 𝓕.p.obj x₀ = A₀)
    (hiV : ∀ a : (squareZeroExtensionArtinian.{u, w, w} Λ k).obj V,
      ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V).residueEquiv
        (IsLocalRing.residue ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V) a) =
          (TrivSqZeroExt.fstHom Λ k V) (squareZeroCoordinates.{u, w, w} V a))
    (a : DerivationMapAndAction 𝓕.p A₀
      ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V) i₀
      (squareZeroCoordinates.{u, w, w} V) hi₀ hiV x₀ hx₀)
    (D : Derivation Λ k V)
    (x : Skeleton (𝓕.p.Fiber ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V))) :
    let L := associatedTangentSpaceModuleStructureUnlifted 𝓕 h𝓕 hS2
    let e : Skeleton (𝓕.p.Fiber ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V)) ≃
        ((L.functor.obj V : ModuleCat.{u₁} k) : Type u₁) :=
      Equiv.cast (by
        calc
          Skeleton (𝓕.p.Fiber ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V)) =
              (isomorphismClasses 𝓕 h𝓕.cofibered).obj
                ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V) :=
            (isomorphismClasses_obj 𝓕 h𝓕.cofibered _).symm
          _ = ((L.functor.obj V : ModuleCat.{u₁} k) : Type u₁) :=
            (congrArg (fun H : FGModuleCat.{w} k ⥤ Type u₁ => H.obj V) L.forget_comp).symm)
    e (a.action D x) = e x + e (a.gamma D)
```

**`Deformation.derivationMap_linear`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/DerivationMapLinear.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/DerivationMapLinear.lean#L157). The attribute's comment: “gamma\_linear”.

> **Stacks Project, Tag 06SU.** The map `γ_V` defined by pushforward along derivations is
> linear for the canonical vector-space structure on the associated functor.

```lean
theorem derivationMap_linear
    (hS2 : SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.cofibered)))
    (V : FGModuleCat.{w} k)
    (hiV : ∀ a : (squareZeroExtensionArtinian.{u, w, w} Λ k).obj V,
      ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V).residueEquiv
        (IsLocalRing.residue ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V) a) =
          (TrivSqZeroExt.fstHom Λ k V) (squareZeroCoordinates.{u, w, w} V a))
    (d : DerivationMapAndAction 𝓕.p A₀
      ((squareZeroExtensionArtinian.{u, w, w} Λ k).obj V) i₀
      (squareZeroCoordinates.{u, w, w} V) hi₀ hiV x₀ hx₀) :
    let L := (associatedTangentSpaceModuleStructureUnlifted 𝓕 h𝓕 hS2).functor
    let AV := (squareZeroExtensionArtinian.{u, w, w} Λ k).obj V
    let hcarrier : ((L.obj V : ModuleCat.{u₁} k) : Type u₁) =
        (isomorphismClasses 𝓕 h𝓕.cofibered).obj AV :=
      congrArg (fun H : FGModuleCat.{w} k ⥤ Type u₁ ↦ H.obj V)
        (associatedTangentSpaceModuleStructureUnlifted 𝓕 h𝓕 hS2).forget_comp
    ∃ γ : Derivation Λ k V →ₗ[k] ((L.obj V : ModuleCat.{u₁} k) : Type u₁),
      ∀ D : Derivation Λ k V,
        γ D = cast hcarrier.symm
          (cast (isomorphismClasses_obj 𝓕 h𝓕.cofibered AV).symm (d.gamma D))
```

## Tag 06SV, an equation

[Tag 06SV](https://stacks.math.columbia.edu/tag/06SV) in the Stacks Project.

**`Deformation.derivationToTangentSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Predeformation.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Predeformation.lean#L379). The attribute's comment: “the map”.

> The canonical map `Der_Λ(k,k) → T𝓕`.

```lean
noncomputable def derivationToTangentSpace :
    Derivation Λ k k → tangentSpaceArtinian Λ k
      (isomorphismClasses (BasedCategory.ofFunctor p) hp.cofibered)
```

**`Deformation.derivationToTangentSpace_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Predeformation.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Predeformation.lean#L399). The attribute's comment: “naturality”.

> A morphism of predeformation categories commutes with the derivation maps on
> tangent spaces.

```lean
theorem derivationToTangentSpace_naturality
    {G : Type u₂} [Category.{v₂} G]
    (q : G ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hq : IsPredeformationCategory q)
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (D : Derivation Λ k k) :
    mapIsomorphismClasses hp.cofibered hq.cofibered φ
      (artinianDualNumbers.{u, w, v} Λ k)
      (derivationToTangentSpace p hp D) =
        derivationToTangentSpace q hq D
```

## Tag 06SW, an equation

[Tag 06SW](https://stacks.math.columbia.edu/tag/06SW) in the Stacks Project.

**`Deformation.derivationAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/DerivationAction.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/DerivationAction.lean#L245). References: SGA 7 VI (1.18), “partial”.

> **Stacks Project, Tag 06SW.** Residue-field derivations act on the tangent space of any
> predeformation category by the twisting automorphisms of the dual numbers.

```lean
noncomputable def derivationAction
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p) : DerivationActionData.{u, v, w} p hp
```

**`Deformation.derivationAction_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/PredeformationTangent/DerivationAction.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/PredeformationTangent/DerivationAction.lean#L298). The attribute's comment: “naturality”.

> **Stacks Project, Tag 06SW.** The tangent map induced by a morphism of predeformation
> categories commutes with the action of residue-field derivations.

```lean
theorem derivationAction_natural
    {G : Type u₁} [Category.{v₁} G]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (q : G ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p) (hq : IsPredeformationCategory q)
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (D : Derivation Λ k k)
    (x : predeformationTangentSpace.{u, v, w} p hp) :
    mapIsomorphismClasses hp.cofibered hq.cofibered φ
        (artinianDualNumbers.{u, w, v} Λ k)
        ((derivationAction.{u, v, w} p hp).action (D, x)) =
      (derivationAction.{u, v, w} q hq).action
        (D, mapIsomorphismClasses hp.cofibered hq.cofibered φ
          (artinianDualNumbers.{u, w, v} Λ k) x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.12, Tag 06I1](https://stacks.math.columbia.edu/tag/06I1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
