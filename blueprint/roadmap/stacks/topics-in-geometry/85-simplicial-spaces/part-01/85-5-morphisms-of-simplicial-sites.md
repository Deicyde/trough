---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteMorphism, CategoryTheory.SimplicialSiteMorphism.transitionPushforwardIso, CategoryTheory.SimplicialSite.Morphism.totalFunctor, CategoryTheory.SimplicialSite.Morphism.totalFunctor_isContinuous, CategoryTheory.CocontinuousSimplicialSite.Morphism.totalMorphism, CategoryTheory.CocontinuousSimplicialSite.Morphism.totalComponentPushforwardIso, CategoryTheory.CocontinuousSimplicialSite.Morphism.totalInverseImageRestrictIso, CategoryTheory.CocontinuousSimplicialSite.Morphism.totalPushforwardRestrictIso
statement: formalized
proof: formalized
---

# 85.5 Morphisms of simplicial sites

Section 85.5 of the Stacks Project, [Tag 0D94](https://stacks.math.columbia.edu/tag/0D94). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D95, a remark

[Tag 0D95](https://stacks.math.columbia.edu/tag/0D95) in the Stacks Project.

**`CategoryTheory.SimplicialSiteMorphism`**, an inductive in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Morphism.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/Morphism.lean#L91). The attribute's comment: “morphism\_between\_simplicial\_sites”.

> **Stacks 0D95.** A morphism between simplicial sites: degreewise morphisms of sites commuting
> with the transitions in case (A), or degreewise cocontinuous functors commuting with the
> transitions in case (B).

```lean
inductive SimplicialSiteMorphism :
    SimplicialSiteSituation.{u} → SimplicialSiteSituation.{u} → Type (u + 1)
```

**`CategoryTheory.SimplicialSiteMorphism.transitionPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Morphism.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/Morphism.lean#L126).

> **Stacks 0D95.** The component morphisms of a morphism between simplicial sites commute, up to
> the canonical comparison, with every simplicial transition morphism of topoi.

```lean
noncomputable def transitionPushforwardIso
    {S S' : SimplicialSiteSituation.{u}}
    (h : SimplicialSiteMorphism S S')
    {m n : SimplexCategory} (φ : m ⟶ n) :
    (h.componentMorphism n).pushforward ⋙ (S'.transitionMorphism φ).pushforward ≅
      (S.transitionMorphism φ).pushforward ⋙ (h.componentMorphism m).pushforward
```

## Tag 0D96, a lemma

[Tag 0D96](https://stacks.math.columbia.edu/tag/0D96) in the Stacks Project.

**`CategoryTheory.SimplicialSite.Morphism.totalFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalContinuousFunctor.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalContinuousFunctor.lean#L86). The attribute's comment: “case (A), the functor of total sites”.

> The functor between the total categories attached to a morphism between simplicial sites in
> the continuous case: in each simplicial degree it is the given functor.

```lean
def totalFunctor (h : SimplicialSite.Morphism C C') :
    CoGrothendieck C'.totalPseudofunctor ⥤ CoGrothendieck C.totalPseudofunctor
```

**`CategoryTheory.SimplicialSite.Morphism.totalFunctor_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalContinuousFunctor.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalContinuousFunctor.lean#L194). The attribute's comment: “case (A), continuity of the functor of total sites”. References: SGA 4 VI (7.4.9), “simplicial, continuous”.

> The functor between the total categories is continuous.

```lean
theorem totalFunctor_isContinuous (h : SimplicialSite.Morphism C C') :
    h.totalFunctor.IsContinuous C'.totalTopology C.totalTopology
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.totalMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean#L136). The attribute's comment: “case (B), the morphism of total topoi”. References: SGA 4 VI (7.4.9), “simplicial case, m\_*”.

> The morphism between the total topoi induced by a morphism between simplicial sites in the
> cocontinuous case.

```lean
noncomputable def totalMorphism (h : CocontinuousSimplicialSite.Morphism C C') :
    MorphismOfTopoi
      (Sheaf (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}).totalTopology (Type u))
      (Sheaf (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}).totalTopology (Type u))
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.totalComponentPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean#L154). The attribute's comment: “case (B), the commutative square”.

> The square formed by the total morphism of topoi, the morphism of topoi in simplicial degree
> `n`, and the two component morphisms of that degree commutes, as witnessed by a natural
> isomorphism of direct-image functors.

```lean
noncomputable def totalComponentPushforwardIso
    (h : CocontinuousSimplicialSite.Morphism C C') (n : SimplexCategory) :
    ((SimplicialSiteMorphism.ofCocontinuous h).componentMorphism n).pushforward ⋙
        (SimplicialSiteSituation.componentMorphism
          (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}) n).pushforward ≅
      (SimplicialSiteSituation.componentMorphism
          (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}) n).pushforward ⋙
        h.totalMorphism.pushforward
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.totalInverseImageRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean#L198). The attribute's comment: “case (B), restriction of the inverse image”. References: SGA 4 VI (7.4.9), “simplicial, f^\{-1}”.

> **Stacks 0D96**, case (B). Inverse image to the component of simplicial degree `n`, applied
> to the inverse image along the total morphism, is the inverse image in degree `n` applied to the
> inverse image to the component of that degree: `h_total^{-1}` is degreewise `h_n^{-1}`.
>
> The two composites of inverse images are the left adjoints of the two composites of direct
> images compared by `totalComponentPushforwardIso`, so this is that comparison conjugated by
> uniqueness of left adjoints.

```lean
noncomputable def totalInverseImageRestrictIso
    (h : CocontinuousSimplicialSite.Morphism C C') (n : SimplexCategory) :
    h.totalMorphism.inverseImage ⋙
        (SimplicialSiteSituation.componentMorphism
          (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}) n).inverseImage ≅
      (SimplicialSiteSituation.componentMorphism
          (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}) n).inverseImage ⋙
        ((SimplicialSiteMorphism.ofCocontinuous h).componentMorphism n).inverseImage
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.totalPushforwardRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphism.lean#L219). The attribute's comment: “case (B), restriction of the direct image”. References: SGA 4 VI (7.4.9), “simplicial, (7.4.9.2)”.

> Inverse image to the component of simplicial degree `n`, applied to the direct image along
> the total morphism, is the direct image in degree `n` applied to the inverse image to the
> component of that degree.

```lean
noncomputable def totalPushforwardRestrictIso
    (h : CocontinuousSimplicialSite.Morphism C C') (n : SimplexCategory) :
    h.totalMorphism.pushforward ⋙
        (SimplicialSiteSituation.componentMorphism
          (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}) n).inverseImage ≅
      (SimplicialSiteSituation.componentMorphism
          (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}) n).inverseImage ⋙
        ((SimplicialSiteMorphism.ofCocontinuous h).componentMorphism n).pushforward
```

**`CategoryTheory.SimplicialSite.Morphism.totalInverseImageRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismCaseA.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismCaseA.lean#L380). The attribute's comment: “case (A), restriction of the inverse image”. References: SGA 4 VI (7.4.9), “simplicial, f^\{-1}”.

> **Stacks 0D96**, case (A). Restriction to the component of simplicial degree `n`, applied to
> the inverse image along the total morphism, is the inverse image in degree `n` applied to
> restriction to the component of that degree: `h_total^{-1}` is degreewise `h_n^{-1}`.

```lean
def totalInverseImageRestrictIso (h : SimplicialSite.Morphism C C') (n : SimplexCategory) :
    h.totalInverseImage ⋙ restrict (⟨Sum.inl C⟩ : SimplicialSiteSituation.{u}) n ≅
      restrict (⟨Sum.inl C'⟩ : SimplicialSiteSituation.{u}) n ⋙ h.componentInverseImage n
```

**`CategoryTheory.SimplicialSiteMorphism.totalMorphismSquares`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismOfTopoi.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismOfTopoi.lean#L88). The attribute's comment: “the morphism of total topoi, its commutative squares with the component morphisms, and the restriction of its direct image, in both cases”.

> **Stacks 0D96.** A morphism `h` between simplicial sites, in either case of Stacks 0D95,
> induces a morphism of topoi `h_total : Sh(C_total) → Sh(C'_total)` (`h.totalMorphism`) such that
> for every `n` the square formed by `h_total`, the morphism of topoi `h_n` of degree `n` and the
> morphisms of topoi `g_n`, `g'_n` of the component inclusions commutes, and
> `(g'_n)^{-1} ∘ h_{total,*} = h_{n,*} ∘ g_n^{-1}`.

```lean
def totalMorphismSquares : (h : SimplicialSiteMorphism S S') → h.TotalMorphismSquares
```

## Tag 0D97, a lemma

[Tag 0D97](https://stacks.math.columbia.edu/tag/0D97) in the Stacks Project.

**`CategoryTheory.SimplicialSite.Morphism.derivedTotalPushforwardRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalContinuousMorphismDerivedPushforward.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalContinuousMorphismDerivedPushforward.lean#L344). The attribute's comment: “case (A)”.

> For a morphism between simplicial sites built from morphisms of sites (case (A)), and `K` in
> the unbounded derived category of abelian sheaves on the total site,
> `(g'_n)^{-1} Rh_{total,*} K = Rh_{n,*} g_n^{-1} K`, as a natural isomorphism of functors on the
> derived categories.

```lean
def derivedTotalPushforwardRestrictIso (h : SimplicialSite.Morphism C C')
    (n : SimplexCategory) :
    h.derivedAbelianTotalPushforward ⋙
        (abelianComponent (⟨Sum.inl C'⟩ : SimplicialSiteSituation.{u}) n).mapDerivedCategory ≅
      (abelianComponent (⟨Sum.inl C⟩ : SimplicialSiteSituation.{u}) n).mapDerivedCategory ⋙
        h.derivedAbelianComponentPushforward n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.derivedTotalPushforwardRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismDerivedPushforward.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismDerivedPushforward.lean#L548). The attribute's comment: “case (B)”.

> In case (B), with notation and hypotheses as in Stacks 0D96: the natural isomorphism
> `(g'_n)^{-1} Rh_{total,*} K ≅ Rh_{n,*} g_n^{-1} K` for `K` in the unbounded derived category of
> abelian sheaves on the total site.

```lean
def derivedTotalPushforwardRestrictIso (h : CocontinuousSimplicialSite.Morphism C C')
    (n : SimplexCategory) :
    h.derivedAbelianTotalPushforward ⋙
        (abelianComponent (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}) n).mapDerivedCategory ≅
      (abelianComponent (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}) n).mapDerivedCategory ⋙
        h.derivedAbelianComponentPushforward n
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.derivedTotalPushforwardRestrictIso'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismDerivedPushforward.lean, line 569](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalMorphismDerivedPushforward.lean#L569). The attribute's comment: “case (B)”.

> In case (B), with notation and hypotheses as in Stacks 0D96: the natural isomorphism
> `(g'_n)^{-1} Rh_{total,*} K ≅ Rh_{n,*} g_n^{-1} K` for `K` in the unbounded derived category of
> abelian sheaves on the total site, with restriction written as
> `CategoryTheory.SimplicialSiteSituation.restrictAb`.

```lean
def derivedTotalPushforwardRestrictIso' (h : CocontinuousSimplicialSite.Morphism C C')
    (n : SimplexCategory) :
    h.derivedAbelianTotalPushforward ⋙
        (restrictAb (⟨Sum.inr C'⟩ : SimplicialSiteSituation.{u}) n).mapDerivedCategory ≅
      (restrictAb (⟨Sum.inr C⟩ : SimplicialSiteSituation.{u}) n).mapDerivedCategory ⋙
        h.derivedAbelianComponentPushforward n
```

## Tag 0D98, a remark

[Tag 0D98](https://stacks.math.columbia.edu/tag/0D98) in the Stacks Project.

**`CategoryTheory.SimplicialSiteMorphism.CompatibleWithAugmentations`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentedMorphism.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentedMorphism.lean#L68). The attribute's comment: “compatibility\_with\_augmentations”.

> Compatibility of a morphism of topoi between augmentation sites with a morphism of simplicial
> sites and the two augmentations.

```lean
def CompatibleWithAugmentations
    {S S' : SimplicialSiteSituation.{u}}
    {D D' : Cat.{u, u}} {K : GrothendieckTopology D}
    {K' : GrothendieckTopology D'}
    (h : SimplicialSiteMorphism S S')
    (a : SimplicialSiteSituation.Augmentation S D K)
    (a' : SimplicialSiteSituation.Augmentation S' D' K')
    (g : MorphismOfTopoi (Sheaf K (Type u)) (Sheaf K' (Type u))) : Prop
```

**`CategoryTheory.SimplicialSiteMorphism.augmentationPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentedMorphism.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentedMorphism.lean#L94).

> The degree-zero square of a morphism of augmented simplicial sites commutes, as witnessed by a
> natural isomorphism of direct-image functors.

```lean
noncomputable def augmentationPushforwardIso
    {S S' : SimplicialSiteSituation.{u}}
    {D D' : Cat.{u, u}} {K : GrothendieckTopology D}
    {K' : GrothendieckTopology D'}
    (h : SimplicialSiteMorphism S S')
    (a : SimplicialSiteSituation.Augmentation S D K)
    (a' : SimplicialSiteSituation.Augmentation S' D' K')
    (g : MorphismOfTopoi (Sheaf K (Type u)) (Sheaf K' (Type u)))
    (hg : CompatibleWithAugmentations h a a' g) :
    (h.componentMorphism (SimplexCategory.mk 0)).pushforward ⋙
        (SimplicialSiteSituation.Augmentation.morphismOfTopoi S' D' K' a').pushforward ≅
      (SimplicialSiteSituation.Augmentation.morphismOfTopoi S D K a).pushforward ⋙
        g.pushforward
```

## Tag 0D99, a lemma

[Tag 0D99](https://stacks.math.columbia.edu/tag/0D99) in the Stacks Project.

**`CategoryTheory.SimplicialSiteMorphism.totalAugmentationPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentedTotalMorphismSquare.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/AugmentedTotalMorphismSquare.lean#L245).

> **Stacks 0D99.** Let `h` be a morphism between simplicial sites (Stacks 0D95), in either case
> of Stacks 09WE, let `a`, `a'` be augmentations of its source and target towards sites `D`, `D'`
> (Stacks 0D6Z), and let `g : Sh(D) → Sh(D')` be a morphism of topoi compatible with `h`, `a`, `a'`
> (Stacks 0D98). Then the square formed by the morphism of total topoi `h_total` (Stacks 0D96), the
> morphisms of topoi `a : Sh(C_total) → Sh(D)` and `a' : Sh(C'_total) → Sh(D')` of the total
> augmentations (Stacks 0D70) and `g` commutes: `a' ∘ h_total = g ∘ a`, as witnessed by a natural
> isomorphism of direct-image functors.

```lean
def totalAugmentationPushforwardIso {S S' : SimplicialSiteSituation.{u}}
    {D D' : Cat.{u, u}} {K : GrothendieckTopology D} {K' : GrothendieckTopology D'}
    (h : SimplicialSiteMorphism S S')
    (a : SimplicialSiteSituation.Augmentation S D K)
    (a' : SimplicialSiteSituation.Augmentation S' D' K')
    (g : MorphismOfTopoi (Sheaf K (Type u)) (Sheaf K' (Type u)))
    (hg : h.CompatibleWithAugmentations a a' g) :
    h.totalMorphism.pushforward ⋙
        (SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi S' D' K' a').pushforward ≅
      (SimplicialSiteSituation.Augmentation.totalMorphismOfTopoi S D K a).pushforward ⋙
        g.pushforward
```

**`CategoryTheory.CocontinuousSimplicialSite.Morphism.totalAugmentationPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentedMorphism.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalAugmentedMorphism.lean#L159).

> **Stacks 0D99.** Let a morphism between simplicial sites, augmentations of its source and its
> target, and a morphism of the augmentation topoi compatible with them be given. Then the square
> formed by the total topoi, the augmentation topoi, the total morphism of the simplicial sites and
> that morphism of the augmentation topoi commutes, as witnessed by a natural isomorphism of
> direct-image functors.

```lean
noncomputable def totalAugmentationPushforwardIso
    (h : CocontinuousSimplicialSite.Morphism C C')
    (a : C.Augmentation D K) (a' : C'.Augmentation D' K')
    (g : MorphismOfTopoi (Sheaf K (Type u)) (Sheaf K' (Type u)))
    (hg : SimplicialSiteMorphism.CompatibleWithAugmentations
      (SimplicialSiteMorphism.ofCocontinuous h) a a' g) :
    h.totalMorphism.pushforward ⋙ (Augmentation.totalMorphismOfTopoi a').pushforward ≅
      (Augmentation.totalMorphismOfTopoi a).pushforward ⋙ g.pushforward
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.5, Tag 0D94](https://stacks.math.columbia.edu/tag/0D94)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
