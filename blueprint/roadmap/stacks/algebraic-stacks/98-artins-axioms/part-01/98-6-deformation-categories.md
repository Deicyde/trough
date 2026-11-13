---
declaration: section
origin: cited
lean: Deformation.Artin.isDeformationCategory_predeformationCategory, Deformation.Artin.schlessingerConditionS1_isomorphismClasses_of_isDeformationCategory, Deformation.Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory, Deformation.schlessingerConditionS1_of_satisfiesRS, Deformation.schlessingerConditionS2_of_satisfiesRS
statement: formalized
proof: formalized
---

# 98.6 Deformation categories

Section 98.6 of the Stacks Project, [Tag 07WT](https://stacks.math.columbia.edu/tag/07WT). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07WU, a lemma

[Tag 07WU](https://stacks.math.columbia.edu/tag/07WU) in the Stacks Project.

**`Deformation.Artin.isDeformationCategory_predeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/RimSchlessinger/DeformationCategory.lean, line 1184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/RimSchlessinger/DeformationCategory.lean#L1184).

> **Stacks Project, Tag 07WU.** The predeformation category of a
> finite-type field-valued point in a fibred category satisfying (RS) is a
> deformation category.

```lean
public theorem isDeformationCategory_predeformationCategory
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type u₁} [Category.{v₁} 𝒳]
    (p : 𝒳 ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids)
    (hRS : SatisfiesRS B S hS p hp)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ S)
    (x₀ : 𝒳)
    (hx₀ : (p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
      (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact
      (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let D := predeformationCategory iΛ
      (p ⋙ Over.post B.inclusion) x₀ hx₀
    letI := D.category
    Deformation.IsDeformationCategory D.projection
```

## Tag 07WV, a remark

[Tag 07WV](https://stacks.math.columbia.edu/tag/07WV) in the Stacks Project.

**`Deformation.Artin.schlessingerConditionS1_isomorphismClasses_of_isDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Basic.lean#L57). The attribute's comment: “condition (S1) for isomorphism classes”.

> The functor of isomorphism classes associated to a deformation category
> satisfies Schlessinger's condition (S1).

```lean
public theorem schlessingerConditionS1_isomorphismClasses_of_isDeformationCategory
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{v₁, u₁}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p) :
    SchlessingerConditionS1
      (Functor.Elements.π
        (isomorphismClassesData 𝓕 h𝓕.predeformation.cofibered).classes)
```

**`Deformation.Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Basic.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Basic.lean#L73). The attribute's comment: “condition (S2) for isomorphism classes”.

> The functor of isomorphism classes associated to a deformation category
> satisfies Schlessinger's condition (S2).

```lean
public theorem schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{v₁, u₁}
      (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p) :
    SchlessingerConditionS2
      (Functor.Elements.π
        (isomorphismClassesData 𝓕 h𝓕.predeformation.cofibered).classes)
```

Declarations registered for the tag:

- [`Deformation.schlessingerConditionS1_of_satisfiesRS`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L270), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Basic.lean#L47) (StacksFrontier): “condition (S1) for the deformation category”.
- [`Deformation.schlessingerConditionS2_of_satisfiesRS`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L343), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/Basic.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Basic.lean#L49) (StacksFrontier): “condition (S2) for the deformation category”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.6, Tag 07WT](https://stacks.math.columbia.edu/tag/07WT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
