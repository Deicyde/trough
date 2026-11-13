---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.Augmentation, CategoryTheory.SimplicialSiteSituation.Augmentation.componentAugmentation, CategoryTheory.SimplicialSiteSituation.Augmentation.transitionPushforwardIso, CategoryTheory.SimplicialSiteSituation.Augmentation.totalPushforwardForkIsLimit, CategoryTheory.SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi, CategoryTheory.SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi_componentMorphism_iso
statement: formalized
proof: formalized
---

# 85.4 Augmentations of simplicial sites

Section 85.4 of the Stacks Project, [Tag 0D93](https://stacks.math.columbia.edu/tag/0D93). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D6Z, a remark

[Tag 0D6Z](https://stacks.math.columbia.edu/tag/0D6Z) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.Augmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Augmentation.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/Augmentation.lean#L100).

> **Stacks 0D6Z.** An augmentation of a simplicial site towards `(D, K)`. In case (A) it is
> a morphism of sites represented by a continuous functor in the opposite direction; in case (B)
> it is represented by a cocontinuous functor. In either case its composite with a vertex functor
> is independent of the chosen vertex.

```lean
def Augmentation (S : SimplicialSiteSituation.{u}) (D : Cat.{u, u})
    (K : GrothendieckTopology D) : Type u
```

## Tag 0D70, a lemma

[Tag 0D70](https://stacks.math.columbia.edu/tag/0D70) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.Augmentation.componentAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationPushforward.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationPushforward.lean#L168). The attribute's comment: “part (1): the morphisms of topoi of the components”.

> **Stacks 0D70, part (1).** The morphism of topoi from the sheaves on the component in
> simplicial degree `n` to the sheaves on the augmentation site, obtained by composing the
> degree-zero morphism of the augmentation with the transition morphism of a vertex.

```lean
public noncomputable def componentAugmentation (n : SimplexCategory) :
    MorphismOfTopoi (Sheaf (S.componentTopology n) (Type u)) (Sheaf K (Type u))
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.transitionPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationPushforward.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentationPushforward.lean#L302). The attribute's comment: “compatibility (1): composition with a simplicial transition”.

> **Stacks 0D70, compatibility (1).** Composing the direct image of a simplicial transition
> with the direct image of the component augmentation of its target agrees canonically with the
> direct image of the component augmentation of its source.

```lean
public noncomputable def transitionPushforwardIso {m n : SimplexCategory} (φ : m ⟶ n) :
    (S.transitionMorphism φ).pushforward ⋙
        (componentAugmentation S D K a m).pushforward ≅
      (componentAugmentation S D K a n).pushforward
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.totalPushforwardForkIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentationEqualizer.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentationEqualizer.lean#L92). The attribute's comment: “compatibility (3): the total direct image is the equalizer”.

> **Stacks 0D70, compatibility (3).** For a sheaf `F` on the total site, the direct image
> `a_* F` along the total augmentation is the equalizer of the two maps
> `a_{0,*} F_0 ⟶ a_{1,*} F_1` attached to the two maps `[0] ⟶ [1]`.

```lean
def totalPushforwardForkIsLimit (F : Sheaf S.totalTopology (Type u)) :
    IsLimit (totalPushforwardFork S D K a F)
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentationMorphism.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentationMorphism.lean#L768). The attribute's comment: “part (2): the morphism of topoi of the total site”.

> **Stacks 0D70, part (2).** The morphism of topoi from the sheaves on the total site to the
> sheaves on the augmentation site induced by an augmentation: its inverse image is the descent of
> the inverse images along the component augmentations, its direct image is the limit of the
> cosimplicial sheaf of their direct images, and the two are adjoint.

```lean
def totalMorphismOfTopoi :
    MorphismOfTopoi (Sheaf S.totalTopology (Type u)) (Sheaf K (Type u))
```

**`CategoryTheory.SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi_componentMorphism_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentationMorphism.lean, line 790](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentationMorphism.lean#L790). The attribute's comment: “compatibility (2): composition with a component inclusion”.

> **Stacks 0D70, compatibility (2), in inverse images.** The inverse image of the total
> augmentation followed by the inverse image of the morphism of topoi which Stacks 09WG attaches
> to the simplicial degree `n` is the inverse image of the augmentation of that degree: the
> augmentation of a simplicial degree is the total augmentation composed with that morphism.

```lean
def totalMorphismOfTopoi_componentMorphism_iso (n : SimplexCategory) :
    (totalMorphismOfTopoi S D K a).inverseImage ⋙ (componentMorphism S n).inverseImage ≅
      (componentAugmentation S D K a n).inverseImage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.4, Tag 0D93](https://stacks.math.columbia.edu/tag/0D93)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
