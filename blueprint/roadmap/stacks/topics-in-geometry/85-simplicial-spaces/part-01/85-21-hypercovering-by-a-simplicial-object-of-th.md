---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.IsHypercoveringAugmentation, CategoryTheory.SimplicialOver.homEquivCommSq, CategoryTheory.SimplicialOver.toAssociatedTotal_comp_totalForget, CategoryTheory.SimplicialOver.associatedTotalEquivalence, CategoryTheory.SimplicialOver.associatedTotalEquivalence_isDenseSubsite, CategoryTheory.SimplicialOver.augmentationPushforwardIsoAssociated, CategoryTheory.SimplicialOver.augmentationInverseImageIsoAssociated, Stacks.CategoryTheory.Hypercovering.associatedSimplicialObject
statement: formalized
proof: formalized
---

# 85.21 Hypercovering by a simplicial object of the site

Section 85.21 of the Stacks Project, [Tag 09X8](https://stacks.math.columbia.edu/tag/09X8). 6 tags here are carried by 51 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09X8, the section

[Tag 09X8](https://stacks.math.columbia.edu/tag/09X8) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.IsHypercoveringAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L90). The attribute's comment: “the definition of the section: an augmentation of a simplicial object of the site is a hypercovering of `X` in `C` when the three displayed families are coverings”.

> An augmentation `a : U ⟶ X` of a simplicial object `U` of the site given by
> the pretopology `J` is a *hypercovering of `X` in `C`* when `{U₀ ⟶ X}` is a covering, the
> canonical morphism `U₁ ⟶ U₀ ×_X U₀` generates a covering, and the canonical morphism
> `U_{n+1} ⟶ (cosk_n sk_n U)_{n+1}` generates a covering for every `n ≥ 1`, the coskeleton being
> formed in the slice category `C/X`.

```lean
def IsHypercoveringAugmentation (J : Pretopology C) (U : SimplicialObject C)
    (a : U ⟶ (SimplicialObject.const C).obj X) : Prop
```

**`CategoryTheory.SimplicialOver.homEquivCommSq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L143). The attribute's comment: “a morphism (φ, f) : V/U_n → W/U_m of (C/U)_total is φ : [m] → [n] and f : V → W with commutative square”.

> A morphism `V/U_n ⟶ W/U_m` of `(C/U)_total` is a pair `(φ, f)` of a simplex map
> `φ : [m] ⟶ [n]` and a morphism `f : V ⟶ W` of `C` such that the square formed with `V ⟶ U_n`,
> `W ⟶ U_m` and `f_φ : U_n ⟶ U_m` commutes.

```lean
def homEquivCommSq (A B : Grothendieck (slices U)) :
    (A ⟶ B) ≃ {p : (A.base ⟶ B.base) × ((A.fiber : Over (U.obj A.base)).left ⟶
        (B.fiber : Over (U.obj B.base)).left) //
      p.2 ≫ (B.fiber : Over (U.obj B.base)).hom = (A.fiber : Over (U.obj A.base)).hom ≫ U.map p.1}
```

**`CategoryTheory.SimplicialOver.toAssociatedTotal_comp_totalForget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L296). The attribute's comment: “the morphism of topoi a is given by the cocontinuous functor V/U_n ↦ V/X: j_total of (C/K)_total is V/U_n ↦ V/X under the identification”.

> Under the identification of `(C/U)_total` with `(C/K)_total`, the localization functor
> `j_total : (C/K)_total ⥤ C/X` is the functor `V/U_n ↦ V/X`: precomposed with
> `(C/U)_total ⥤ (C/K)_total` it is `augmentationFunctor` on the nose.

```lean
theorem toAssociatedTotal_comp_totalForget :
    toAssociatedTotal U a ⋙
        SimplicialSemiRepresentable.totalForget (associatedSimplicialObject.{u} U a) =
      augmentationFunctor U a
```

**`CategoryTheory.SimplicialOver.associatedTotalEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L392). The attribute's comment: “the site (C/U)_total, with objects V/U_n and morphisms (φ, f), is (C/K)_total of Remark 0D8C: the equivalence of categories”.

> The equivalence of categories `(C/K)_total ≌ (C/U)_total` between the total site attached
> to `K` and the category whose objects are the `V/U_n` and whose morphisms are the pairs `(φ, f)`.
> Its functor is `fromAssociatedTotal`, and its inverse is `toAssociatedTotal` by
> `associatedTotalEquivalenceInverseIso`.

```lean
def associatedTotalEquivalence :
    Grothendieck (SimplicialSemiRepresentable.slices (associatedSimplicialObject.{u} U a)) ≌
      Grothendieck (slices U)
```

**`CategoryTheory.SimplicialOver.associatedTotalEquivalence_isDenseSubsite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L410). The attribute's comment: “the site (C/U)_total is (C/K)_total of Remark 0D8C: the coverings agree”.

> The equivalence `(C/K)_total ≌ (C/U)_total` identifies the topologies: it is a dense subsite
> inclusion, so a sieve is covering exactly when its image is.

```lean
theorem associatedTotalEquivalence_isDenseSubsite :
    (associatedTotalEquivalence U a).functor.IsDenseSubsite
      (associatedTotalTopology U a J) (SimplicialOver.totalTopology J U)
```

**`CategoryTheory.SimplicialOver.augmentationPushforwardIsoAssociated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L495). The attribute's comment: “the augmentation morphism of topoi a : Sh((C/U)_total) → Sh(C/X): the one of Remark 0D8C and the one of V/U_n ↦ V/X agree, direct images”.

> The direct image of the augmentation `a : Sh((C/U)_total) ⟶ Sh(C/X)` given by
> `V/U_n ↦ V/X` is the direct image of the morphism of topoi `Sh((C/K)_total) ⟶ Sh(C/X)` induced
> by the total site of `K`, transported along `associatedTotalSheafEquivalence`.

```lean
def augmentationPushforwardIsoAssociated :
    (augmentationMorphismOfTopoi J U a).pushforward ≅
      (associatedTotalSheafEquivalence U a J).inverse ⋙
        (SimplicialSemiRepresentable.totalLocalizationMorphism (J.over X)
          (associatedSimplicialObject.{u} U a)).pushforward
```

**`CategoryTheory.SimplicialOver.augmentationInverseImageIsoAssociated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L508). The attribute's comment: “the augmentation morphism of topoi a : Sh((C/U)_total) → Sh(C/X): the one of Remark 0D8C and the one of V/U_n ↦ V/X agree, inverse images”.

> The inverse image of the augmentation `a : Sh((C/U)_total) ⟶ Sh(C/X)` is the inverse image
> of the morphism of topoi `Sh((C/K)_total) ⟶ Sh(C/X)` followed by
> `associatedTotalSheafEquivalence`.

```lean
def augmentationInverseImageIsoAssociated :
    (augmentationMorphismOfTopoi J U a).inverseImage ≅
      (SimplicialSemiRepresentable.totalLocalizationMorphism (J.over X)
          (associatedSimplicialObject.{u} U a)).inverseImage ⋙
        (associatedTotalSheafEquivalence U a J).functor
```

Declarations registered for the tag:

- [`Stacks.CategoryTheory.Hypercovering.associatedSimplicialObject`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/FromSimplicialObject.lean#L172), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L525) (StacksFrontier): “the simplicial object K of SR(C, X) with K_n = {U_n → X}”.
- [`CategoryTheory.SimplicialSemiRepresentable.totalSituation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L528) (StacksFrontier): “the simplicial site (C/U)_total obtained from K by Remark 0D8C, that is (C/K)_total”.
- [`CategoryTheory.SimplicialSemiRepresentable.augmentationMorphismOfTopoi`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L144), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L532) (StacksFrontier): “the augmentation morphism of topoi a : Sh((C/U)_total) → Sh(C/X) obtained from K by Remark 0D8C”.
- [`CategoryTheory.SimplicialOver.totalTopology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean#L131), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L536) (StacksFrontier): “the site (C/U)_total with objects V/U_n and morphisms (φ, f): its topology”.
- [`CategoryTheory.SimplicialOver.situation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L510), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 539](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L539) (StacksFrontier): “the site (C/U)_total with objects V/U_n and morphisms (φ, f), as a simplicial site”.
- [`CategoryTheory.SimplicialOver.augmentationFunctor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L664), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L543) (StacksFrontier): “the cocontinuous functor V/U_n ↦ V/X”.
- [`CategoryTheory.SimplicialOver.augmentationMorphismOfTopoi`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L713), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L546) (StacksFrontier): “the morphism of topoi a : Sh((C/U)_total) → Sh(C/X) given by the cocontinuous functor V/U_n ↦ V/X”.
- [`CategoryTheory.SimplicialOver.augmentationMorphismOfTopoi_pushforward`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L722), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L550) (StacksFrontier): “the morphism of topoi a is given by the cocontinuous functor V/U_n ↦ V/X: direct images”.
- [`Stacks.CategoryTheory.Hypercovering.isHypercoveringAugmentation_iff_isHypercovering`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L104), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectTotalSite.lean#L554) (StacksFrontier): “being a hypercovering of X in C is equivalent to K being a hypercovering of X, Example 0GM9”.

## Tag 0DA8, a lemma

[Tag 0DA8](https://stacks.math.columbia.edu/tag/0DA8) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.faithful_inverseImage_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L224). The attribute's comment: “part (1): a^{-1} on sheaves of sets is faithful”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` the inverse image
> `a^{-1} : Sh(C/X) ⥤ Sh((C/U)_total)` of the augmentation is faithful.

```lean
theorem faithful_inverseImage_augmented (h : IsHypercoveringAugmentation P U a) :
    (augmentationMorphismOfTopoi P U a).inverseImage.Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.full_inverseImage_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L232). The attribute's comment: “part (1): a^{-1} on sheaves of sets is full, carrying local fullness of j_total”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` such that `j_total` is locally full for
> the topology of `C/X`, the inverse image `a^{-1} : Sh(C/X) ⥤ Sh((C/U)_total)` is full.

```lean
theorem full_inverseImage_augmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X)) :
    (augmentationMorphismOfTopoi P U a).inverseImage.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.full_inverseImage_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L242). The attribute's comment: “part (1): a^{-1} on sheaves of sets is full”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` the inverse image
> `a^{-1} : Sh(C/X) ⥤ Sh((C/U)_total)` is full.

```lean
theorem full_inverseImage_augmented' (h : IsHypercoveringAugmentation P U a) :
    (augmentationMorphismOfTopoi P U a).inverseImage.Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulInverseImageAugmented`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L249). The attribute's comment: “part (1): a^{-1} on sheaves of sets is fully faithful, carrying local fullness”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` such that `j_total` is locally full,
> the inverse image `a^{-1} : Sh(C/X) ⥤ Sh((C/U)_total)` is fully faithful.

```lean
def fullyFaithfulInverseImageAugmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X)) :
    (augmentationMorphismOfTopoi P U a).inverseImage.FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulInverseImageAugmented'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L259). The attribute's comment: “part (1): a^{-1} on sheaves of sets is fully faithful”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` the inverse image
> `a^{-1} : Sh(C/X) ⥤ Sh((C/U)_total)` is fully faithful.

```lean
def fullyFaithfulInverseImageAugmented' (h : IsHypercoveringAugmentation P U a) :
    (augmentationMorphismOfTopoi P U a).inverseImage.FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_unit_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L268). The attribute's comment: “part (1): E = a_* a^{-1} E on sheaves of sets, carrying local fullness”.

> For a hypercovering augmentation such that `j_total` is locally full, the canonical map
> `E ⟶ a_* a^{-1} E` is an isomorphism for every sheaf of sets `E` on `C/X`.

```lean
theorem isIso_unit_augmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X)) :
    IsIso (augmentationMorphismOfTopoi P U a).adj.unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_unit_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L278). The attribute's comment: “part (1): E = a_* a^{-1} E on sheaves of sets”.

> For a hypercovering augmentation, the canonical map `E ⟶ a_* a^{-1} E` is an
> isomorphism for every sheaf of sets `E` on `C/X`.

```lean
theorem isIso_unit_augmented' (h : IsHypercoveringAugmentation P U a) :
    IsIso (augmentationMorphismOfTopoi P U a).adj.unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianSheaf_of_mem_essImage_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L285). The attribute's comment: “part (1): the essential image of a^{-1} consists of cartesian sheaves of sets”.

> Every sheaf of sets on `(C/U)_total` isomorphic to an inverse image along the
> augmentation is cartesian.

```lean
theorem isCartesianSheaf_of_mem_essImage_augmented
    {F : Sheaf (totalSituation P U a).totalTopology (Type u)}
    (hF : (augmentationMorphismOfTopoi P U a).inverseImage.essImage F) :
    (totalSituation P U a).IsCartesianSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianSheaf_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L295). The attribute's comment: “part (1): essential image = cartesian sheaves of sets, carrying surjectivity”.

> If every cartesian sheaf of sets on `(C/U)_total` lies in the essential image of
> `a^{-1}`, then the essential image of `a^{-1}` is exactly the cartesian sheaves of sets.

```lean
theorem mem_essImage_iff_isCartesianSheaf_augmented
    (hsurj : ∀ G : Sheaf (totalSituation P U a).totalTopology (Type u),
      (totalSituation P U a).IsCartesianSheaf G →
        (augmentationMorphismOfTopoi P U a).inverseImage.essImage G)
    (F : Sheaf (totalSituation P U a).totalTopology (Type u)) :
    (augmentationMorphismOfTopoi P U a).inverseImage.essImage F ↔
      (totalSituation P U a).IsCartesianSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianSheaf_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L307). The attribute's comment: “part (1): the essential image of a^{-1} is exactly the cartesian sheaves of sets”.

> For a hypercovering augmentation, the essential image of
> `a^{-1} : Sh(C/X) ⥤ Sh((C/U)_total)` is exactly the cartesian sheaves of sets.

```lean
theorem mem_essImage_iff_isCartesianSheaf_augmented' (h : IsHypercoveringAugmentation P U a)
    (F : Sheaf (totalSituation P U a).totalTopology (Type u)) :
    (augmentationMorphismOfTopoi P U a).inverseImage.essImage F ↔
      (totalSituation P U a).IsCartesianSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_counit_app_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L318). The attribute's comment: “part (1): a^{-1} a_* F = F for cartesian F, carrying the two clauses of 0D8E”.

> For a hypercovering augmentation such that `j_total` is locally full and every cartesian
> sheaf of sets on `(C/U)_total` lies in the essential image of `a^{-1}`, the canonical map
> `a^{-1} a_* F ⟶ F` is an isomorphism for every cartesian sheaf of sets `F` on `(C/U)_total`.

```lean
theorem isIso_counit_app_augmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X))
    (hsurj : ∀ G : Sheaf (totalSituation P U a).totalTopology (Type u),
      (totalSituation P U a).IsCartesianSheaf G →
        (augmentationMorphismOfTopoi P U a).inverseImage.essImage G)
    {F : Sheaf (totalSituation P U a).totalTopology (Type u)}
    (hF : (totalSituation P U a).IsCartesianSheaf F) :
    IsIso ((augmentationMorphismOfTopoi P U a).adj.counit.app F)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_counit_app_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L334). The attribute's comment: “part (1): a^{-1} a_* F = F for a cartesian sheaf of sets F”.

> For a hypercovering augmentation, the canonical map `a^{-1} a_* F ⟶ F` is an
> isomorphism for every cartesian sheaf of sets `F` on `(C/U)_total`.

```lean
theorem isIso_counit_app_augmented' (h : IsHypercoveringAugmentation P U a)
    {F : Sheaf (totalSituation P U a).totalTopology (Type u)}
    (hF : (totalSituation P U a).IsCartesianSheaf F) :
    IsIso ((augmentationMorphismOfTopoi P U a).adj.counit.app F)
```

**`CategoryTheory.SimplicialSemiRepresentable.faithful_abelianInverseImage_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L346). The attribute's comment: “part (2): a^{-1} on abelian sheaves is faithful”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` the inverse image
> `a^{-1} : Ab(C/X) ⥤ Ab((C/U)_total)` of the augmentation is faithful.

```lean
theorem faithful_abelianInverseImage_augmented (h : IsHypercoveringAugmentation P U a) :
    (abelianInverseImage P U a).Faithful
```

**`CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L354). The attribute's comment: “part (2): a^{-1} on abelian sheaves is full, carrying local fullness of j_total”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` such that `j_total` is locally full,
> the inverse image `a^{-1} : Ab(C/X) ⥤ Ab((C/U)_total)` is full.

```lean
theorem full_abelianInverseImage_augmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X)) :
    (abelianInverseImage P U a).Full
```

**`CategoryTheory.SimplicialSemiRepresentable.full_abelianInverseImage_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L364). The attribute's comment: “part (2): a^{-1} on abelian sheaves is full”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` the inverse image
> `a^{-1} : Ab(C/X) ⥤ Ab((C/U)_total)` is full.

```lean
theorem full_abelianInverseImage_augmented' (h : IsHypercoveringAugmentation P U a) :
    (abelianInverseImage P U a).Full
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulAbelianInverseImageAugmented`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L371). The attribute's comment: “part (2): a^{-1} on abelian sheaves is fully faithful, carrying local fullness”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` such that `j_total` is locally full,
> the inverse image `a^{-1} : Ab(C/X) ⥤ Ab((C/U)_total)` is fully faithful.

```lean
def fullyFaithfulAbelianInverseImageAugmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X)) :
    (abelianInverseImage P U a).FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.fullyFaithfulAbelianInverseImageAugmented'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L381). The attribute's comment: “part (2): a^{-1} on abelian sheaves is fully faithful”.

> For a hypercovering `a : U ⟶ X` of `X` in `C` the inverse image
> `a^{-1} : Ab(C/X) ⥤ Ab((C/U)_total)` is fully faithful.

```lean
def fullyFaithfulAbelianInverseImageAugmented' (h : IsHypercoveringAugmentation P U a) :
    (abelianInverseImage P U a).FullyFaithful
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L390). The attribute's comment: “part (2): E = a_* a^{-1} E on abelian sheaves, carrying local fullness”.

> For a hypercovering augmentation such that `j_total` is locally full, the canonical map
> `E ⟶ a_* a^{-1} E` is an isomorphism for every sheaf of abelian groups `E` on `C/X`.

```lean
theorem isIso_abelianUnit_augmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X)) :
    IsIso (abelianAdjunction P U a).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L400). The attribute's comment: “part (2): E = a_* a^{-1} E on abelian sheaves”.

> For a hypercovering augmentation, the canonical map `E ⟶ a_* a^{-1} E` is an
> isomorphism for every sheaf of abelian groups `E` on `C/X`.

```lean
theorem isIso_abelianUnit_augmented' (h : IsHypercoveringAugmentation P U a) :
    IsIso (abelianAdjunction P U a).unit
```

**`CategoryTheory.SimplicialSemiRepresentable.isCartesianAbSheaf_of_mem_essImage_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L407). The attribute's comment: “part (2): the essential image of a^{-1} consists of cartesian abelian sheaves”.

> Every sheaf of abelian groups on `(C/U)_total` isomorphic to an inverse image along the
> augmentation is cartesian.

```lean
theorem isCartesianAbSheaf_of_mem_essImage_augmented
    {F : Sheaf (totalSituation P U a).totalTopology Ab.{u}}
    (hF : (abelianInverseImage P U a).essImage F) :
    (totalSituation P U a).IsCartesianAbSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianAbSheaf_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L417). The attribute's comment: “part (2): essential image = cartesian abelian sheaves, carrying surjectivity”.

> If every cartesian sheaf of abelian groups on `(C/U)_total` lies in the essential image
> of `a^{-1}`, then the essential image of `a^{-1}` is exactly the cartesian abelian sheaves.

```lean
theorem mem_essImage_iff_isCartesianAbSheaf_augmented
    (hsurj : ∀ G : Sheaf (totalSituation P U a).totalTopology Ab.{u},
      (totalSituation P U a).IsCartesianAbSheaf G → (abelianInverseImage P U a).essImage G)
    (F : Sheaf (totalSituation P U a).totalTopology Ab.{u}) :
    (abelianInverseImage P U a).essImage F ↔
      (totalSituation P U a).IsCartesianAbSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.mem_essImage_iff_isCartesianAbSheaf_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L428). The attribute's comment: “part (2): the essential image of a^{-1} is exactly the cartesian abelian sheaves”.

> For a hypercovering augmentation, the essential image of
> `a^{-1} : Ab(C/X) ⥤ Ab((C/U)_total)` is exactly the cartesian abelian sheaves.

```lean
theorem mem_essImage_iff_isCartesianAbSheaf_augmented' (h : IsHypercoveringAugmentation P U a)
    (F : Sheaf (totalSituation P U a).totalTopology Ab.{u}) :
    (abelianInverseImage P U a).essImage F ↔
      (totalSituation P U a).IsCartesianAbSheaf F
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianCounit_app_augmented`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L439). The attribute's comment: “part (2): a^{-1} a_* F = F for cartesian F, carrying the two clauses of 0D8E”.

> For a hypercovering augmentation such that `j_total` is locally full and every cartesian
> sheaf of abelian groups on `(C/U)_total` lies in the essential image of `a^{-1}`, the canonical
> map `a^{-1} a_* F ⟶ F` is an isomorphism for every cartesian sheaf of abelian groups `F`.

```lean
theorem isIso_abelianCounit_app_augmented (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X))
    (hsurj : ∀ G : Sheaf (totalSituation P U a).totalTopology Ab.{u},
      (totalSituation P U a).IsCartesianAbSheaf G → (abelianInverseImage P U a).essImage G)
    {F : Sheaf (totalSituation P U a).totalTopology Ab.{u}}
    (hF : (totalSituation P U a).IsCartesianAbSheaf F) :
    IsIso ((abelianAdjunction P U a).counit.app F)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_abelianCounit_app_augmented'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObject.lean#L454). The attribute's comment: “part (2): a^{-1} a_* F = F for a cartesian abelian sheaf F”.

> For a hypercovering augmentation, the canonical map `a^{-1} a_* F ⟶ F` is an
> isomorphism for every cartesian sheaf of abelian groups `F` on `(C/U)_total`.

```lean
theorem isIso_abelianCounit_app_augmented' (h : IsHypercoveringAugmentation P U a)
    {F : Sheaf (totalSituation P U a).totalTopology Ab.{u}}
    (hF : (totalSituation P U a).IsCartesianAbSheaf F) :
    IsIso ((abelianAdjunction P U a).counit.app F)
```

## Tag 0D8N, a lemma

[Tag 0D8N](https://stacks.math.columbia.edu/tag/0D8N) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitAugmented_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedPushforward.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedPushforward.lean#L290). The attribute's comment: “granted two inputs this library does not have: local fullness of j_total, which is the unproved clause of Tag 0D8E, and the Ra_*-acyclicity of a⁻¹ of a K-injective complex, which is the content of the spectral sequence of Tag 0D7A; the isomorphism is not proved unconditionally”.

> **Stacks Project, Tag 0D8N**, granted the two inputs this library does not have. For a site
> `C` with fibre products, an object `X` of `C` and a hypercovering `a : U ⟶ X` of `X` in `C` by a
> simplicial object `U` of `C`, the canonical map `E ⟶ Ra_* a^{-1} E` is an isomorphism for every
> object `E` of the unbounded derived category of abelian sheaves on `C/X`.
>
> `E` is arbitrary: no boundedness is assumed and the coefficients are all abelian sheaves. The
> source deduces this from Stacks 0D8L for the associated simplicial semi-representable object
> over `X`, and that is the deduction performed, the hypercovering conditions on `a` entering
> through cover density of `j_total`.
>
> The two carried hypotheses are the ones discussed in the module docstring. `hlf`, local fullness
> of `j_total`, is the clause of Stacks 0D8E which the library does not prove; together with the
> degree-zero clause of `h` it supplies the underived unit `F ⟶ a_* a^{-1} F` of Stacks 0DA8 (2),
> which is the first input of Stacks 0D8L. `hacyclic` says that the direct image of `a^{-1}` of a
> K-injective complex needs no derivation, that is, that `R^p a_* a^{-1}` vanishes in positive
> degrees; the source reads that off the spectral sequence of Stacks 0D7A, which this library
> builds but without the convergence to `R^{p+q} a_*` that the reading needs. No unconditional
> invertibility is claimed.

```lean
theorem isIso_derivedAugmentationUnitAugmented_app
    (h : IsHypercoveringAugmentation P U a)
    (hlf : (totalForget (associatedSimplicialObject.{u} U a)).IsLocallyFull
      (P.toGrothendieck.over X))
    (hacyclic : ∀ I : CochainComplex (AbelianSheavesOver P.toGrothendieck X) ℤ,
      I.IsKInjective →
        IsIso ((derivedAbelianTotalPushforwardOverUnit P.toGrothendieck X
          (associatedSimplicialObject.{u} U a)).app
            (((abelianTotalInverseImageOver P.toGrothendieck X
              (associatedSimplicialObject.{u} U a)).mapHomotopyCategory
                (ComplexShape.up ℤ)).obj
                  ((HomotopyCategory.quotient (AbelianSheavesOver P.toGrothendieck X)
                    (ComplexShape.up ℤ)).obj I))))
    (E : DerivedCategory (AbelianSheavesOver P.toGrothendieck X)) :
    IsIso ((derivedAugmentationUnitAugmented P U a).app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitAugmented_app'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedPushforwardUnconditional.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedPushforwardUnconditional.lean#L249). The attribute's comment: “with the Ra_*-acyclicity of a⁻¹ of a K-injective complex taken as an explicit input. It is discharged, and this tag carried unconditionally, by ...SimplicialSemiRepresentable.isIso_derivedAugmentationUnitAugmented_app_unconditional”.

> **Stacks Project, Tag 0D8N**, granted the one input this library does not have. For a site
> `C` with fibre products, an object `X` of `C` and a hypercovering `a : U ⟶ X` of `X` in `C` by a
> simplicial object `U` of `C`, the canonical map `E ⟶ Ra_* a^{-1} E` is an isomorphism for every
> object `E` of the unbounded derived category of abelian sheaves on `C/X`.
>
> `E` is arbitrary: no boundedness is assumed and the coefficients are all abelian sheaves. The
> source deduces this from Stacks 0D8L for the associated simplicial semi-representable object
> over `X`, and that is the deduction performed, the hypercovering conditions on `a` entering
> through cover density and local fullness of `j_total`.
>
> The first input of Stacks 0D8L is discharged from the hypercovering conditions alone: it is the
> underived unit `F ⟶ a_* a^{-1} F` of Stacks 0DA8 (2),
> `CategoryTheory.SimplicialSemiRepresentable.isIso_abelianUnit_augmented'`. What remains carried
> is the hypothesis discussed in the module docstring: `hacyclic` says that the direct image of
> `a^{-1}` of a K-injective complex needs no derivation, that is, that `R^p a_* a^{-1}` vanishes in
> positive degrees; the source reads that off the spectral sequence of Stacks 0D7A, which this
> library builds but without the convergence to `R^{p+q} a_*` that the reading needs. No
> unconditional invertibility is claimed.

```lean
theorem isIso_derivedAugmentationUnitAugmented_app'
    (h : IsHypercoveringAugmentation P U a)
    (hacyclic : ∀ I : CochainComplex (AbelianSheavesOver P.toGrothendieck X) ℤ,
      I.IsKInjective →
        IsIso ((derivedAbelianTotalPushforwardOverUnit P.toGrothendieck X
          (associatedSimplicialObject.{u} U a)).app
            (((abelianTotalInverseImageOver P.toGrothendieck X
              (associatedSimplicialObject.{u} U a)).mapHomotopyCategory
                (ComplexShape.up ℤ)).obj
                  ((HomotopyCategory.quotient (AbelianSheavesOver P.toGrothendieck X)
                    (ComplexShape.up ℤ)).obj I))))
    (E : DerivedCategory (AbelianSheavesOver P.toGrothendieck X)) :
    IsIso ((derivedAugmentationUnitAugmented P U a).app E)
```

**`CategoryTheory.SimplicialSemiRepresentable.isIso_derivedAugmentationUnitAugmented_app_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringObjectDerivedPushforwardUnconditional.lean#L151).

> For a hypercovering augmentation `a : U ⟶ X` of a simplicial object of `C`, the canonical map
> `E ⟶ Ra_* a⁻¹ E` is invertible at every object `E` of `D(C/X)`.

```lean
theorem isIso_derivedAugmentationUnitAugmented_app_unconditional (P : Pretopology C) {X : C}
    (U : SimplicialObject C) (a : U ⟶ (SimplicialObject.const C).obj X)
    (h : IsHypercoveringAugmentation P U a)
    (E : DerivedCategory (AbelianSheavesOver P.toGrothendieck X)) :
    IsIso ((derivedAugmentationUnitAugmented P U a).app E)
```

## Tag 09X9, a lemma

[Tag 09X9](https://stacks.math.columbia.edu/tag/09X9) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.derivedGlobalSectionsInverseImageIsoAugmented'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean#L87).

> **Stacks Project, Tag 09X9.** For a site `C` with fibre products, an object `X` of `C` and
> a hypercovering `a : U ⟶ X` of `X` in `C` by a simplicial object `U` of `C`, with
> `a : Sh((C/U)_total) ⟶ Sh(C/X)` the augmentation of Stacks 09X8, derived global sections over `X`
> are derived global sections on the total site of the inverse image:
>
> `RΓ(X, E) = RΓ((C/U)_total, a⁻¹E)`.
>
> The statement is an isomorphism of functors on the unbounded derived category of abelian sheaves
> on `C/X`, so it holds at every object `E` of `D(C/X)`.

```lean
def derivedGlobalSectionsInverseImageIsoAugmented'
    (h : IsHypercoveringAugmentation P U a) :
    Augmentation.derivedGlobalSectionsBase (Cat.of (Over X)) (P.toGrothendieck.over X) ≅
      Augmentation.derivedTotalInverseImage (totalSituation P U a) (Cat.of (Over X))
          (P.toGrothendieck.over X) (augmentationAugmented P U a) ⋙
        Augmentation.derivedGlobalSectionsTotal (totalSituation P U a)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedGlobalSectionsInverseImageIsoAugmented_hom_app'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean#L102). The attribute's comment: “the forward map of the isomorphism is the canonical one — RΓ(X, -) of the canonical map E ⟶ Ra_*a⁻¹E of Tag 0D8L followed by the derived factorisation of Tag 08J6”.

> **Stacks 09X9, the isomorphism is invertibility of the canonical comparison map.** At every
> object `E` of `D(C/X)` the forward map of the isomorphism of Stacks 09X9 is derived global
> sections over `X` applied to the canonical map `E ⟶ Ra_*a⁻¹E` of Stacks 0D8L, followed by the
> derived factorisation `Ra_* ⋙ RΓ(X, -) ≅ RΓ((C/U)_total, -)` of Stacks 08J6.

```lean
theorem derivedGlobalSectionsInverseImageIsoAugmented_hom_app'
    (h : IsHypercoveringAugmentation P U a)
    (E : DerivedCategory (Sheaf (P.toGrothendieck.over X) AddCommGrpCat.{u})) :
    (derivedGlobalSectionsInverseImageIsoAugmented' P U a h).hom.app E =
      (Augmentation.derivedGlobalSectionsBase (Cat.of (Over X))
          (P.toGrothendieck.over X)).map
        ((Augmentation.derivedAugmentationUnit (totalSituation P U a) (Cat.of (Over X))
          (P.toGrothendieck.over X) (augmentationAugmented P U a)).app E) ≫
        (Augmentation.derivedGlobalSectionsPushforwardIso (totalSituation P U a)
          (Cat.of (Over X)) (P.toGrothendieck.over X) (augmentationAugmented P U a)
            (abelianTotalPushforwardGammaIsoOver P
              (associatedSimplicialObject.{u} U a))).hom.app
            ((Augmentation.derivedTotalInverseImage (totalSituation P U a) (Cat.of (Over X))
              (P.toGrothendieck.over X) (augmentationAugmented P U a)).obj E)
```

## Tag 0DA9, a lemma

[Tag 0DA9](https://stacks.math.columbia.edu/tag/0DA9) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceAugmented'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean#L136).

> **Stacks Project, Tag 0DA9.** For a site `C` with fibre products, an object `X` of `C`, a
> hypercovering `a : U ⟶ X` of `X` in `C` by a simplicial object `U` of `C`, the augmentation
> `a : Sh((C/U)_total) ⟶ Sh(C/X)` of Stacks 09X8, and the weak Serre subcategory
> `𝒜 ⊂ Ab((C/U)_total)` of cartesian abelian sheaves of Stacks 0D7J, the derived inverse image is
> an equivalence
>
> `a⁻¹ : D⁺(C/X) ⟶ D⁺_𝒜((C/U)_total)`
>
> with quasi-inverse `Ra_*`.

```lean
def derivedTotalInverseImageEquivalenceAugmented'
    (h : IsHypercoveringAugmentation P U a) :
    (DerivedCategoryB.derivedCategoryBPlus
        (⊤ : ObjectProperty
          (Sheaf (P.toGrothendieck.over X) AddCommGrpCat.{u}))).FullSubcategory ≌
      (DerivedCategoryB.derivedCategoryBPlus
        ((totalSituation P U a).IsCartesianAbSheaf)).FullSubcategory
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceAugmented_functor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean#L149). The attribute's comment: “the forward functor of the equivalence is a⁻¹”.

> **Stacks 0DA9, the forward functor of the equivalence is `a⁻¹`:** it is the restriction of
> the derived inverse image along the augmentation to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceAugmented_functor'
    (h : IsHypercoveringAugmentation P U a) :
    (derivedTotalInverseImageEquivalenceAugmented' P U a h).functor =
      Augmentation.derivedTotalInverseImagePlus (totalSituation P U a) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationAugmented P U a)
```

**`CategoryTheory.SimplicialSemiRepresentable.derivedTotalInverseImageEquivalenceAugmented_inverse'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/HypercoveringBySimplicialObjectDerivedDescentUnconditional.lean#L159). The attribute's comment: “the quasi-inverse of the equivalence is Ra_*”.

> **Stacks 0DA9, the quasi-inverse of the equivalence is `Ra_*`:** it is the restriction of the
> derived direct image along the augmentation to the bounded below subcategories.

```lean
theorem derivedTotalInverseImageEquivalenceAugmented_inverse'
    (h : IsHypercoveringAugmentation P U a) :
    (derivedTotalInverseImageEquivalenceAugmented' P U a h).inverse =
      Augmentation.derivedTotalPushforwardPlus (totalSituation P U a) (Cat.of (Over X))
        (P.toGrothendieck.over X) (augmentationAugmented P U a)
```

## Tag 09WL, a lemma

[Tag 09WL](https://stacks.math.columbia.edu/tag/09WL) in the Stacks Project.

**`CategoryTheory.SimplicialOver.isMorphismOfSites_pullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean#L161). The attribute's comment: “part (1), each transition is a morphism of sites”.

> **Stacks 09WL part (1).** For a simplex map `φ : [m] ⟶ [n]` the base change functor
> `v_φ = Over.pullback f_φ : C/U_m ⥤ C/U_n` along `f_φ : U_n ⟶ U_m` represents a morphism of
> sites `C/U_n ⟶ C/U_m` between the localizations of `(C, J)` in the two degrees: it is
> continuous and the induced pullback on sheaves of sets is exact.
>
> This is Stacks 09W9 applied to `f_φ`, and it is the datum making the localizations `C/U_n`
> into a simplicial object in the category whose objects are sites and whose morphisms are
> morphisms of sites.

```lean
theorem isMorphismOfSites_pullbackMap {m n : SimplexCategory} (φ : m ⟶ n) :
    (Over.pullback (U.map φ.op)).IsMorphismOfSites
      (J.over (U.obj (op m))) (J.over (U.obj (op n)))
```

**`CategoryTheory.SimplicialOver.pullbackMapId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean#L170). The attribute's comment: “part (1), the identity isomorphism”.

> **Stacks 09WL part (1).** The transition morphism of sites attached to an identity simplex
> map is the identity: base change along `f_{𝟙} = 𝟙 U_n` is isomorphic to the identity functor
> of `C/U_n`.

```lean
def pullbackMapId (n : SimplexCategory) :
    Over.pullback (U.map (𝟙 n).op) ≅ 𝟭 (Over (U.obj (op n)))
```

**`CategoryTheory.SimplicialOver.pullbackMapComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean#L179). The attribute's comment: “part (1), the composition isomorphism”.

> **Stacks 09WL part (1).** The transition morphisms of sites are compatible with
> composition of simplex maps: base change along `f_{ψ ≫ φ} = f_φ ≫ f_ψ` is isomorphic to base
> change along `f_ψ` followed by base change along `f_φ`, by the canonical isomorphism
> `W ×_{U_l} U_n ≅ (W ×_{U_l} U_m) ×_{U_m} U_n` of chosen fibre products.

```lean
def pullbackMapComp {l m n : SimplexCategory} (ψ : l ⟶ m) (φ : m ⟶ n) :
    Over.pullback (U.map (ψ ≫ φ).op) ≅
      Over.pullback (U.map ψ.op) ⋙ Over.pullback (U.map φ.op)
```

**`CategoryTheory.SimplicialOver.sheafPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObject.lean#L190). The attribute's comment: “part (1), the transitions induce the localization morphisms of topoi”.

> **Stacks 09WL part (1).** The morphism of topoi `Sh(C/U_n) ⟶ Sh(C/U_m)` attached to the
> transition morphism of sites of a simplex map `φ : [m] ⟶ [n]` is the one attached to the
> localization functor `j = Over.map f_φ`: the direct image of the cocontinuous functor `j` is
> the direct image of the continuous functor `v_φ = Over.pullback f_φ`.

```lean
def sheafPushforwardIso {m n : SimplexCategory} (φ : m ⟶ n) :
    (Over.map (U.map φ.op)).sheafPushforwardCocontinuous (Type u)
        (J.over (U.obj (op n))) (J.over (U.obj (op m))) ≅
      (Over.pullback (U.map φ.op)).sheafPushforwardContinuous (Type u)
        (J.over (U.obj (op m))) (J.over (U.obj (op n)))
```

**`CategoryTheory.SimplicialOver.totalComparisonEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L352). The attribute's comment: “part (2), the comparison of the two total categories”.

> **Stacks 09WL part (2).** The construction of Stacks 09WC applied to the simplicial object
> in sites of part (1) reproduces the category `(C/U)_total`: the comparison functor, which is
> the identity on objects and the bijection `totalHomEquiv` on morphisms, is an isomorphism of
> categories.

```lean
def totalComparisonEquivalence : Grothendieck (slices U) ≌ PullbackTotal U
```

**`CategoryTheory.SimplicialOver.pullbackTotalCoverings_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L389). The attribute's comment: “part (2), the coverings of the two total sites agree”.

> **Stacks 09WL part (2).** The two sites have the same covering families: a family of the
> total category of Stacks 09WC is covering exactly when it is the image under the comparison of
> a covering family of `(C/U)_total`. Both topologies are generated by these families.

```lean
theorem pullbackTotalCoverings_iff (𝒱 : Covering.{u, u, u} (PullbackTotal U)) :
    pullbackTotalCoverings J U 𝒱 ↔
      ∃ 𝒰 : Covering.{u, u, u} (Grothendieck (slices U)),
        SimplicialCoverings.total (slices U) (sliceCoverings J U) 𝒰 ∧
          𝒱 = ⟨(totalComparison U).obj 𝒰.1, 𝒰.2.map (totalComparison U)⟩
```

**`CategoryTheory.SimplicialOver.totalTopology_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L525). The attribute's comment: “part (2), the generic total site is (C/U)_total”.

> **Stacks 09WL part (2).** The total site of that situation is the site `(C/U)_total`: the
> generic construction of the total site, applied to the simplicial family of sites `n ↦ C/U_n`,
> gives the category `(C/U)_total` and the topology `totalTopology` on the nose.

```lean
theorem totalTopology_eq : (situation J U).totalTopology = SimplicialOver.totalTopology J U
```

**`CategoryTheory.SimplicialOver.isMorphismOfSites_augmentationPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L547). The attribute's comment: “part (3), a_0 is a morphism of sites”.

> **Stacks 09WL part (3).** For an augmentation `a : U → X`, base change along
> `a_0 : U_0 ⟶ X` is continuous with exact pullback on sheaves of sets, that is, it represents a
> morphism of sites `a_0 : C/U_0 → C/X`. This is Stacks 09W9 applied to `a_0`.

```lean
theorem isMorphismOfSites_augmentationPullback :
    (Over.pullback (augmentationApp U a (op (SimplexCategory.mk 0)))).IsMorphismOfSites
      (J.over X) (J.over (U.obj (op (SimplexCategory.mk 0))))
```

**`CategoryTheory.SimplicialOver.augmentationVertexCompat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L567). The attribute's comment: “part (3), the vertex compatibility of the augmentation”.

> **Stacks 09WL part (3).** The functor `u_0 = Over.pullback a_0` representing the
> augmentation satisfies the compatibility of Stacks 0D6Z part (A): the composites `u_φ ∘ u_0`
> for the vertices `φ : [0] ⟶ [n]` of a simplicial degree agree, both being canonically
> isomorphic to base change along `a_n`. Chosen fibre products make this an isomorphism rather
> than the equality of functors the source writes, exactly as in part (1).

```lean
def augmentationVertexCompat (n : SimplexCategory) (φ ψ : SimplexCategory.mk 0 ⟶ n) :
    Over.pullback (augmentationApp U a (op (SimplexCategory.mk 0))) ⋙
        Over.pullback (U.map φ.op) ≅
      Over.pullback (augmentationApp U a (op (SimplexCategory.mk 0))) ⋙
        Over.pullback (U.map ψ.op)
```

**`CategoryTheory.SimplicialOver.augmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L616). The attribute's comment: “part (3), a_0 is an augmentation of the simplicial site C/U”.

> **Stacks 09WL part (3).** The augmentation `a_0 : C/U_0 → C/X` of the simplicial family of
> sites `n ↦ C/U_n`: the localization functor `j_{a_0} = Over.map a_0` is cocontinuous and its
> composite with the functor of any vertex of a simplicial degree is `j_{a_n}`, which does not
> mention the vertex. By `isMorphismOfSites_augmentationPullback` and
> `augmentationSheafPushforwardIso` this is the augmentation given by the morphism of sites
> `a_0` of Stacks 0D6Z part (A): the two presentations of `a_0` give the same morphism of topoi
> `Sh(C/U_0) ⟶ Sh(C/X)`.

```lean
def augmentation : (simplicialSite J U).Augmentation (Cat.of (Over X)) (J.over X)
```

**`CategoryTheory.SimplicialOver.augmentationMorphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L713). The attribute's comment: “part (3), the morphism of topoi Sh((C/U)_total) to Sh(C/X) of the augmentation”.

> **Stacks 09WL part (3).** The morphism of topoi `a : Sh((C/U)_total) ⟶ Sh(C/X)` which the
> augmentation `a_0` gives: the morphism of topoi of Stacks 0D70 attached to the augmentation of
> the simplicial family of sites `n ↦ C/U_n` determined by `a_0`.

```lean
noncomputable def augmentationMorphismOfTopoi :
    MorphismOfTopoi (Sheaf (SimplicialOver.totalTopology J U) (Type u))
      (Sheaf (J.over X) (Type u))
```

**`CategoryTheory.SimplicialOver.augmentationMorphismOfTopoi_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/OverSimplicialObjectTotalSite.lean#L722). The attribute's comment: “part (3), the augmentation gives the morphism of topoi above”.

> **Stacks 09WL part (3).** That morphism of topoi is the one above: its direct image is the
> direct image of the cocontinuous functor `V/U_n ↦ V/X` of Stacks 09X8. The two are *equal*,
> not merely isomorphic.

```lean
theorem augmentationMorphismOfTopoi_pushforward :
    (augmentationMorphismOfTopoi J U a).pushforward =
      (augmentationFunctor U a).sheafPushforwardCocontinuous (Type u)
        (SimplicialOver.totalTopology J U) (J.over X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.21, Tag 09X8](https://stacks.math.columbia.edu/tag/09X8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
