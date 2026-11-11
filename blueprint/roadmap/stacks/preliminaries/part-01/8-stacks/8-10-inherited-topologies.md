---
declaration: section
origin: cited
lean: CategoryTheory.Functor.inheritedPrecoverage_hasIsos, CategoryTheory.Functor.inheritedPrecoverage_isStableUnderComposition, CategoryTheory.Functor.inheritedPrecoverage_hasPullbacks, CategoryTheory.Functor.inheritedPrecoverage_isStableUnderBaseChange, CategoryTheory.Functor.inheritedTopology, CategoryTheory.Functor.IsFibredOneMorphism.isContinuous_and_isCocontinuous_inheritedTopology, CategoryTheory.Functor.IsFibredOneMorphism.inverseImageCompSheafToPresheafIso, CategoryTheory.Functor.IsFibredOneMorphism.inverseImage_obj_obj_obj
statement: formalized
proof: formalized
---

# 8.10 Inherited topologies

Section 8.10 of the Stacks Project, [Tag 06NT](https://stacks.math.columbia.edu/tag/06NT). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06NU, a lemma

[Tag 06NU](https://stacks.math.columbia.edu/tag/06NU) in the Stacks Project.

**`CategoryTheory.Functor.inheritedPrecoverage_hasIsos`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L137). The attribute's comment: “Axiom (1): isomorphisms cover.”.

> **Stacks 06NU**, axiom (1) of a site: a family consisting of a single isomorphism of `𝒮` is a
> covering, because an isomorphism is strongly cartesian and its image is an isomorphism of `𝒞`.

```lean
instance inheritedPrecoverage_hasIsos [Precoverage.HasIsos K] :
    Precoverage.HasIsos (p.inheritedPrecoverage K)
```

**`CategoryTheory.Functor.inheritedPrecoverage_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L150). The attribute's comment: “Axiom (2): coverings are stable under composition.”.

> **Stacks 06NU**, axiom (2) of a site: refining a covering by coverings again gives a covering,
> because a composition of strongly cartesian morphisms is strongly cartesian (Stacks 02XL) and the
> images compose to a covering of `𝒞`.

```lean
instance inheritedPrecoverage_isStableUnderComposition
    [Precoverage.IsStableUnderComposition K] :
    Precoverage.IsStableUnderComposition (p.inheritedPrecoverage K)
```

**`CategoryTheory.Functor.inheritedPrecoverage_hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L173). The attribute's comment: “Axiom (3), existence of the fibre products.”.

> **Stacks 06NU**, the existence half of axiom (3) of a site: given a covering `{ x i ⟶ x }` of
> `𝒮` and a morphism `y ⟶ x`, the fibre products `x i ×_x y` exist. This is Stacks 06N5, applied to
> the strongly cartesian morphism `x i ⟶ x` and the fibre product of the images, which exists in `𝒞`.

```lean
instance inheritedPrecoverage_hasPullbacks [p.IsFibered] [HasPullbacks 𝒞] :
    (p.inheritedPrecoverage K).HasPullbacks
```

**`CategoryTheory.Functor.inheritedPrecoverage_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L184). The attribute's comment: “Axiom (3), the base change of a covering is a covering.”.

> **Stacks 06NU**, the covering half of axiom (3) of a site: the family of projections
> `{ x i ×_x y ⟶ y }` of a covering `{ x i ⟶ x }` along `y ⟶ x` is again a covering. Both conditions
> transfer from `{ x i ⟶ x }` by the two base-change lemmas above.

```lean
instance inheritedPrecoverage_isStableUnderBaseChange [p.IsFibered] [HasPullbacks 𝒞]
    [Precoverage.IsStableUnderBaseChange K] :
    Precoverage.IsStableUnderBaseChange (p.inheritedPrecoverage K)
```

## Tag 06NV, a definition

[Tag 06NV](https://stacks.math.columbia.edu/tag/06NV) in the Stacks Project.

**`CategoryTheory.Functor.inheritedTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L207).

> The Grothendieck topology on a fibred category `p : 𝒮 ⥤ 𝒞` inherited from a topology `J` on the
> base: the topology generated by the collection `CategoryTheory.Functor.inheritedPrecoverage` of
> Stacks 06NU, whose covering families are the families of strongly `p`-cartesian morphisms whose
> family of images covers in `(𝒞, J)`.

```lean
def inheritedTopology (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) : GrothendieckTopology 𝒮
```

## Tag 06NW, a lemma

[Tag 06NW](https://stacks.math.columbia.edu/tag/06NW) in the Stacks Project.

**`CategoryTheory.Functor.IsFibredOneMorphism.isContinuous_and_isCocontinuous_inheritedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean#L179).

> Let `(𝒞, J)` be a site and let `F : 𝒳 ⥤ 𝒴` be a 1-morphism of fibred categories over `𝒞`
> (Stacks 02XP), so that `F ⋙ q = p` and `F` preserves strongly cartesian morphisms. Then `F` is a
> continuous and a cocontinuous functor between the topologies that `𝒳` and `𝒴` inherit from `𝒞`
> (Stacks 06NV).

```lean
public theorem IsFibredOneMorphism.isContinuous_and_isCocontinuous_inheritedTopology
    [HasPullbacks 𝒞] (J : GrothendieckTopology 𝒞) {p : 𝒳 ⥤ 𝒞} {q : 𝒴 ⥤ 𝒞} {F : 𝒳 ⥤ 𝒴}
    [p.IsFibered] [q.IsFibered] (hF : p.IsFibredOneMorphism q F) :
    F.IsContinuous (p.inheritedTopology J) (q.inheritedTopology J) ∧
      F.IsCocontinuous (p.inheritedTopology J) (q.inheritedTopology J)
```

**`CategoryTheory.Functor.IsFibredOneMorphism.inverseImageCompSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean#L265).

> The inverse image of the morphism of topoi induced by a 1-morphism of fibred categories is
> plain restriction along `F.op`: as a functor to presheaves on `𝒳` it is `sheafToPresheaf` followed
> by precomposition with `F.op`, with no sheafification intervening.

```lean
def IsFibredOneMorphism.inverseImageCompSheafToPresheafIso :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology J).1
    F.sheafPushforwardContinuous A (p.inheritedTopology J) (q.inheritedTopology J) ⋙
        sheafToPresheaf (p.inheritedTopology J) A ≅
      sheafToPresheaf (q.inheritedTopology J) A ⋙ (whiskeringLeft _ _ _).obj F.op
```

**`CategoryTheory.Functor.IsFibredOneMorphism.inverseImage_obj_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean#L276).

> The formula `f⁻¹(𝒢)(x) = 𝒢(F x)`: the sections of the inverse image of a sheaf `𝒢` on `𝒴`
> over an object `x` of `𝒳` are the sections of `𝒢` over `F x`.

```lean
theorem IsFibredOneMorphism.inverseImage_obj_obj_obj :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology J).1
    ∀ (𝒢 : Sheaf (q.inheritedTopology J) A) (x : 𝒳),
      ((F.sheafPushforwardContinuous A (p.inheritedTopology J)
            (q.inheritedTopology J)).obj 𝒢).obj.obj (Opposite.op x) =
        𝒢.obj.obj (Opposite.op (F.obj x))
```

**`CategoryTheory.Functor.IsFibredOneMorphism.preservesFiniteLimits_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean#L288).

> The inverse image `f⁻¹` of the morphism of topoi induced by a 1-morphism of fibred categories
> preserves finite limits.

```lean
theorem IsFibredOneMorphism.preservesFiniteLimits_inverseImage [HasFiniteLimits A] :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology J).1
    PreservesFiniteLimits (F.sheafPushforwardContinuous A (p.inheritedTopology J)
      (q.inheritedTopology J))
```

**`CategoryTheory.Functor.IsFibredOneMorphism.directImageCompSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean#L305).

> The direct image of the morphism of topoi is the right Kan extension along `F.op`, taken on
> sheaves: as a functor to presheaves on `𝒴` it is `sheafToPresheaf` followed by `F.op.ran`.

```lean
noncomputable def IsFibredOneMorphism.directImageCompSheafToPresheafIso
    [∀ (G : 𝒳ᵒᵖ ⥤ A), F.op.HasPointwiseRightKanExtension G] :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology J).2
    F.sheafPushforwardCocontinuous A (p.inheritedTopology J) (q.inheritedTopology J) ⋙
        sheafToPresheaf (q.inheritedTopology J) A ≅
      sheafToPresheaf (p.inheritedTopology J) A ⋙ F.op.ran
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafAdjunctionInheritedTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Functoriality.lean#L319).

> The morphism of topoi `f : Sh(𝒳) ⟶ Sh(𝒴)` induced by a 1-morphism of fibred categories `F`,
> as the adjunction `f⁻¹ ⊣ f_*` between the two inherited sites, with `f⁻¹` the restriction
> `F.sheafPushforwardContinuous` and `f_*` the right Kan extension `F.sheafPushforwardCocontinuous`.

```lean
noncomputable def IsFibredOneMorphism.sheafAdjunctionInheritedTopology
    [∀ (G : 𝒳ᵒᵖ ⥤ A), F.op.HasPointwiseRightKanExtension G] :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology J).1
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology J).2
    F.sheafPushforwardContinuous A (p.inheritedTopology J) (q.inheritedTopology J) ⊣
      F.sheafPushforwardCocontinuous A (p.inheritedTopology J) (q.inheritedTopology J)
```

## Tag 0CN0, a lemma

[Tag 0CN0](https://stacks.math.columbia.edu/tag/0CN0) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.isEquivalence_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean#L114). The attribute's comment: “the equivalence of categories 𝒳/x ⥤ 𝒞/U”.

> For `p : 𝒳 ⥤ 𝒞` fibred in groupoids and `x` an object of `𝒳`, the functor
> `Over.post p : 𝒳/x ⥤ 𝒞/p x` induced by `p` is an equivalence of categories.

```lean
theorem IsFiberedInGroupoids.isEquivalence_overPost (hp : p.IsFiberedInGroupoids) (x : 𝒳) :
    (Over.post (X := x) p).IsEquivalence
```

**`CategoryTheory.Functor.IsInheritedTopology.mem_over_iff_functorPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean#L153). The attribute's comment: “coverings of x' in 𝒳/x correspond to coverings of p x' in 𝒞/U”.

> For `p` fibred in groupoids and `J𝒳` inherited from `(𝒞, J)`, a sieve on an object of `𝒳/x` is
> covering for the topology that `J𝒳` induces on `𝒳/x` exactly when its image under `Over.post p` is
> covering for the topology that `J` induces on `𝒞/p x`.

```lean
theorem IsInheritedTopology.mem_over_iff_functorPushforward (hp : p.IsFiberedInGroupoids)
    {J : GrothendieckTopology 𝒞} {J𝒳 : GrothendieckTopology 𝒳}
    (hJ : _root_.CategoryTheory.Functor.IsInheritedTopology.{max u₂ v₂} p J J𝒳)
    {x : 𝒳} (Y : Over x) (S : Sieve Y) :
    S ∈ (J𝒳.over x) Y ↔
      Sieve.functorPushforward (Over.post p) S ∈
        (J.over (p.obj x)) ((Over.post (X := x) p).obj Y)
```

## Tag 06NX, a lemma

[Tag 06NX](https://stacks.math.columbia.edu/tag/06NX) in the Stacks Project.

**`CategoryTheory.Functor.isStackInGroupoids_of_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Basic.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Basic.lean#L35).

> Let `(𝒞, J)` be a site, let `p : 𝒳 ⥤ 𝒞` and `q : 𝒴 ⥤ 𝒞` be stacks in groupoids over
> `𝒞` and let `F : 𝒳 ⥤ 𝒴` be a 1-morphism of categories over `𝒞`, that is `F ⋙ q = p`.
> If `F` makes `𝒳` a category fibred in groupoids over `𝒴`, then `𝒳` is a stack in
> groupoids over `𝒴` for the topology `J𝒴` inherited from `(𝒞, J)`.

```lean
theorem isStackInGroupoids_of_isFiberedInGroupoids
    (J : GrothendieckTopology 𝒞) (J𝒴 : GrothendieckTopology 𝒴)
    (p : 𝒳 ⥤ 𝒞) (q : 𝒴 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒴)
    (hp : IsStackInGroupoids.{w} p J) (hq : IsStackInGroupoids.{w} q J)
    (hF₁ : F ⋙ q = p)
    (hF₂ : F.IsFiberedInGroupoids)
    (hJ𝒴 : IsInheritedTopology.{w} q J J𝒴) :
    IsStackInGroupoids.{w} F J𝒴
```

## Tag 09WX, a lemma

[Tag 09WX](https://stacks.math.columbia.edu/tag/09WX) in the Stacks Project.

**`CategoryTheory.Functor.isStack_comp_of_isInheritedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/StackOverStack/IsStack.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/StackOverStack/IsStack.lean#L315).

> Let `(𝒞, J)` be a site, let `p : 𝒳 ⥤ 𝒞` be a stack over `𝒞`, endow `𝒳` with the topology `J𝒳`
> inherited from `(𝒞, J)` and let `q : 𝒴 ⥤ 𝒳` be a stack over `(𝒳, J𝒳)`. Then `𝒴` is a stack over
> `𝒞`, along `q ⋙ p`; and if `p` and `q` define stacks in groupoids, that is if both are fibred in
> groupoids, then `𝒴` is a stack in groupoids over `𝒞`.

```lean
public theorem isStack_comp_of_isInheritedTopology (hp : p.IsStack J)
    (hJ𝒳 : IsInheritedTopology.{max u₂ v₂} p J J𝒳) (hq : q.IsStack J𝒳) :
    (q ⋙ p).IsStack J ∧
      (p.IsFiberedInGroupoids →
        q.IsFiberedInGroupoids → (q ⋙ p).IsFiberedInGroupoids ∧ (q ⋙ p).IsStack J)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.10, Tag 06NT](https://stacks.math.columbia.edu/tag/06NT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
