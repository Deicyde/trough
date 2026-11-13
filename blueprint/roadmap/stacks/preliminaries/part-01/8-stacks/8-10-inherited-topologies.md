---
declaration: section
origin: cited
lean: CategoryTheory.Functor.inheritedPrecoverage_hasIsos, CategoryTheory.Functor.inheritedPrecoverage_isStableUnderComposition, CategoryTheory.Functor.inheritedPrecoverage_hasPullbacks_of_hasPullbacks, CategoryTheory.Functor.inheritedPrecoverage_isStableUnderBaseChange_of_hasPullbacks, CategoryTheory.Functor.inheritedTopology, CategoryTheory.Functor.IsFibredOneMorphism.isContinuous_inheritedTopology, CategoryTheory.Functor.IsFibredOneMorphism.isCocontinuous_inheritedTopology, CategoryTheory.Functor.IsFibredOneMorphism.sheafPushforwardContinuousCompSheafToPresheafIso
statement: formalized
proof: formalized
---

# 8.10 Inherited topologies

Section 8.10 of the Stacks Project, [Tag 06NT](https://stacks.math.columbia.edu/tag/06NT). 6 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06NU, a lemma

[Tag 06NU](https://stacks.math.columbia.edu/tag/06NU) in the Stacks Project.

**`CategoryTheory.Functor.inheritedPrecoverage_hasIsos`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L160). The attribute's comment: “Axiom (1): isomorphisms cover.”.

> **Stacks 06NU**, axiom (1) of a site: a family consisting of a single isomorphism of `𝒮` is a
> covering, because an isomorphism is strongly cartesian and its image is an isomorphism of `𝒞`.

```lean
instance inheritedPrecoverage_hasIsos [Precoverage.HasIsos K] :
    Precoverage.HasIsos (p.inheritedPrecoverage K)
```

**`CategoryTheory.Functor.inheritedPrecoverage_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L173). The attribute's comment: “Axiom (2): coverings are stable under composition.”.

> **Stacks 06NU**, axiom (2) of a site: refining a covering by coverings again gives a covering,
> because a composition of strongly cartesian morphisms is strongly cartesian (Stacks 02XL) and the
> images compose to a covering of `𝒞`.

```lean
instance inheritedPrecoverage_isStableUnderComposition
    [Precoverage.IsStableUnderComposition K] :
    Precoverage.IsStableUnderComposition (p.inheritedPrecoverage K)
```

**`CategoryTheory.Functor.inheritedPrecoverage_hasPullbacks_of_hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L197). The attribute's comment: “Axiom (3), existence of the fibre products, for a site with `K.HasPullbacks`.”.

> **Stacks 06NU**, the existence half of axiom (3) of a site: given a covering `{ x i ⟶ x }` of
> `𝒮` and a morphism `y ⟶ x`, the fibre products `x i ×_x y` exist. The site `(𝒞, K)` is only
> assumed to have the fibre products of its own axiom (3), `K.HasPullbacks`: as `{ p (x i) ⟶ p x }`
> is a covering of `𝒞`, the fibre product `p (x i) ×_{p x} p y` exists, and Stacks 06N5, applied to
> the strongly cartesian morphism `x i ⟶ x`, produces `x i ×_x y`.

```lean
instance inheritedPrecoverage_hasPullbacks_of_hasPullbacks [p.IsFibered] [K.HasPullbacks] :
    (p.inheritedPrecoverage K).HasPullbacks
```

**`CategoryTheory.Functor.inheritedPrecoverage_isStableUnderBaseChange_of_hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L212). The attribute's comment: “Axiom (3), base change of a covering is a covering, given `K.HasPullbacks`.”.

> **Stacks 06NU**, the covering half of axiom (3) of a site: the family of projections
> `{ x i ×_x y ⟶ y }` of a covering `{ x i ⟶ x }` along `y ⟶ x` is again a covering. The site
> `(𝒞, K)` is only assumed to have the fibre products along its coverings, `K.HasPullbacks`; both
> conditions transfer from `{ x i ⟶ x }` by the two base-change lemmas above, applied to the fibre
> products `p (x i) ×_{p x} p y`, which exist because `{ p (x i) ⟶ p x }` is a covering.

```lean
instance inheritedPrecoverage_isStableUnderBaseChange_of_hasPullbacks [p.IsFibered]
    [K.HasPullbacks] [Precoverage.IsStableUnderBaseChange K] :
    Precoverage.IsStableUnderBaseChange (p.inheritedPrecoverage K)
```

## Tag 06NV, a definition

[Tag 06NV](https://stacks.math.columbia.edu/tag/06NV) in the Stacks Project.

**`CategoryTheory.Functor.inheritedTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/InheritedSite.lean#L253).

> The Grothendieck topology on a fibred category `p : 𝒮 ⥤ 𝒞` inherited from a topology `J` on the
> base: the topology generated by the collection `CategoryTheory.Functor.inheritedPrecoverage` of
> Stacks 06NU, whose covering families are the families of strongly `p`-cartesian morphisms whose
> family of images covers in `(𝒞, J)`.

```lean
def inheritedTopology (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) : GrothendieckTopology 𝒮
```

## Tag 06NW, a lemma

[Tag 06NW](https://stacks.math.columbia.edu/tag/06NW) in the Stacks Project.

**`CategoryTheory.Functor.IsFibredOneMorphism.isContinuous_inheritedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismContinuity.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismContinuity.lean#L292). The attribute's comment: “continuity of `u` for the inherited topologies; no fibre products in the base”.

> **Stacks 06NW, continuity half, for a 1-morphism of fibred categories, over any base.** A
> 1-morphism `u` of fibred categories over a site `(𝒞, J)` is a continuous functor from the topology
> `𝒳'` inherits from `(𝒞, J)` to the one `𝒳` inherits from it: restriction along `u.op` carries
> sheaves on `𝒳` to sheaves on `𝒳'`. No fibre products of the base are assumed.

```lean
theorem IsFibredOneMorphism.isContinuous_inheritedTopology (J : GrothendieckTopology 𝒞)
    [p'.IsFibered] (hu : p'.IsFibredOneMorphism p u) :
    u.IsContinuous (p'.inheritedTopology J) (p.inheritedTopology J)
```

**`CategoryTheory.Functor.IsFibredOneMorphism.isCocontinuous_inheritedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismContinuity.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismContinuity.lean#L342). The attribute's comment: “cocontinuity of `u` for the inherited topologies; no fibre products in the base”.

> **Stacks 06NW, cocontinuity half, for a 1-morphism of fibred categories, over any base.** A
> 1-morphism `u` of fibred categories over a site `(𝒞, J)` is a cocontinuous functor from the
> topology `𝒳'` inherits from `(𝒞, J)` to the one `𝒳` inherits from it: a covering sieve of
> `u.obj X'` pulls back to a covering sieve of `X'`. No fibre products of the base are
> assumed.

```lean
theorem IsFibredOneMorphism.isCocontinuous_inheritedTopology (J : GrothendieckTopology 𝒞)
    [p'.IsFibered] (hu : p'.IsFibredOneMorphism p u) :
    u.IsCocontinuous (p'.inheritedTopology J) (p.inheritedTopology J)
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafPushforwardContinuousCompSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L73). The attribute's comment: “`f⁻¹ = F^s = F^p`: the inverse image is restriction along `F.op`, unsheafified.”.

> **Stacks 06NW, `f⁻¹ = F^p`, over any base.** The inverse image of the morphism of topoi
> induced by a 1-morphism `F` of fibred categories over a site is plain restriction along `F.op`: as
> a functor to presheaves on `𝒳` it is `sheafToPresheaf` followed by precomposition with `F.op`, with
> no sheafification. No fibre products of the base are assumed.

```lean
def IsFibredOneMorphism.sheafPushforwardContinuousCompSheafToPresheafIso :
    letI := hF.isContinuous_inheritedTopology J
    F.sheafPushforwardContinuous A (p.inheritedTopology J) (q.inheritedTopology J) ⋙
        sheafToPresheaf (p.inheritedTopology J) A ≅
      sheafToPresheaf (q.inheritedTopology J) A ⋙ (whiskeringLeft _ _ _).obj F.op
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafPushforwardContinuous_obj_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L85). The attribute's comment: “The formula `f⁻¹(𝒢)(x) = 𝒢(F(x))`.”.

> **Stacks 06NW, `f⁻¹(𝒢)(x) = 𝒢(F(x))`, over any base.** The sections of the inverse image of
> a sheaf `𝒢` on `𝒴` over an object `x` of `𝒳` are the sections of `𝒢` over `F x`. No fibre
> products of the base are assumed.

```lean
theorem IsFibredOneMorphism.sheafPushforwardContinuous_obj_obj_obj :
    letI := hF.isContinuous_inheritedTopology J
    ∀ (𝒢 : Sheaf (q.inheritedTopology J) A) (x : 𝒳),
      ((F.sheafPushforwardContinuous A (p.inheritedTopology J)
            (q.inheritedTopology J)).obj 𝒢).obj.obj (Opposite.op x) =
        𝒢.obj.obj (Opposite.op (F.obj x))
```

**`CategoryTheory.Functor.IsFibredOneMorphism.preservesFiniteLimits_sheafPushforwardContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L98). The attribute's comment: “Left exactness of `f⁻¹`, part of `f` being a morphism of topoi.”.

> **Stacks 06NW, left exactness of `f⁻¹`, over any base.** The inverse image of the morphism of
> topoi induced by a 1-morphism of fibred categories over a site preserves finite limits. No fibre
> products of the base are assumed.

```lean
theorem IsFibredOneMorphism.preservesFiniteLimits_sheafPushforwardContinuous
    [HasFiniteLimits A] :
    letI := hF.isContinuous_inheritedTopology J
    PreservesFiniteLimits (F.sheafPushforwardContinuous A (p.inheritedTopology J)
      (q.inheritedTopology J))
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafPushforwardCocontinuousCompSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L118). The attribute's comment: “`f_* = {}_sF = {}_pF`: the direct image is the right Kan extension along `F.op`.”.

> **Stacks 06NW, `f_* = {}_pF`, over any base.** The direct image of the morphism of topoi
> induced by a 1-morphism `F` of fibred categories over a site is the right Kan extension along
> `F.op`, taken on sheaves: as a functor to presheaves on `𝒴` it is `sheafToPresheaf` followed by
> `F.op.ran`, with no sheafification. No fibre products of the base are assumed.

```lean
noncomputable def IsFibredOneMorphism.sheafPushforwardCocontinuousCompSheafToPresheafIso
    [∀ (G : 𝒳ᵒᵖ ⥤ A), F.op.HasPointwiseRightKanExtension G] :
    letI := hF.isCocontinuous_inheritedTopology J
    F.sheafPushforwardCocontinuous A (p.inheritedTopology J) (q.inheritedTopology J) ⋙
        sheafToPresheaf (q.inheritedTopology J) A ≅
      sheafToPresheaf (p.inheritedTopology J) A ⋙ F.op.ran
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafAdjunctionCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L132). The attribute's comment: “The adjunction `f⁻¹ ⊣ f_*` between `F^s` and `{}_sF`.”.

> **Stacks 06NW, the adjunction `f⁻¹ ⊣ f_*`, over any base.** For a 1-morphism `F` of fibred
> categories over a site, restriction `F.sheafPushforwardContinuous` along `F.op` is left adjoint to
> the right Kan extension `F.sheafPushforwardCocontinuous` along `F.op`, as functors between the
> sheaf categories of the two inherited sites. No fibre products of the base are assumed.

```lean
noncomputable def IsFibredOneMorphism.sheafAdjunctionCocontinuous
    [∀ (G : 𝒳ᵒᵖ ⥤ A), F.op.HasPointwiseRightKanExtension G] :
    letI := hF.isContinuous_inheritedTopology J
    letI := hF.isCocontinuous_inheritedTopology J
    F.sheafPushforwardContinuous A (p.inheritedTopology J) (q.inheritedTopology J) ⊣
      F.sheafPushforwardCocontinuous A (p.inheritedTopology J) (q.inheritedTopology J)
```

**`CategoryTheory.Functor.IsFibredOneMorphism.morphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L150). The attribute's comment: “The morphism of topoi `f = (F^s, {}_sF) : Sh(𝒳) ⟶ Sh(𝒴)`.”.

> **Stacks 06NW, the morphism of topoi, over any base.** A 1-morphism `F : 𝒳 ⥤ 𝒴` of fibred
> categories over a site `(𝒞, J)` induces a morphism of topoi `f : Sh(𝒳) ⟶ Sh(𝒴)` between the
> inherited sites, whose inverse image `f⁻¹ = F^s` is restriction along `F.op`
> (`IsFibredOneMorphism.sheafPushforwardContinuousCompSheafToPresheafIso`) and whose direct image
> `f_* = {}_sF` is the right Kan extension along `F.op`
> (`IsFibredOneMorphism.sheafPushforwardCocontinuousCompSheafToPresheafIso`). No fibre products of
> the base are assumed.

```lean
noncomputable def IsFibredOneMorphism.morphismOfTopoi [HasFiniteLimits A]
    [∀ (G : 𝒳ᵒᵖ ⥤ A), F.op.HasPointwiseRightKanExtension G] :
    MorphismOfTopoi (Sheaf (p.inheritedTopology J) A) (Sheaf (q.inheritedTopology J) A)
```

**`CategoryTheory.Functor.IsFibredOneMorphism.preservesFiniteLimits_sheafPushforwardContinuous_type`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L198). The attribute's comment: “Left exactness of `f⁻¹` on sheaves of sets, with no hypothesis beyond the source's.”.

> **Stacks 06NW, left exactness of `f⁻¹`, for sheaves of sets.** The inverse image of the
> morphism of topoi induced by a 1-morphism of fibred categories over a site preserves finite limits
> of sheaves of sets. No fibre products of the base are assumed.

```lean
theorem IsFibredOneMorphism.preservesFiniteLimits_sheafPushforwardContinuous_type :
    letI := hF.isContinuous_inheritedTopology J
    PreservesFiniteLimits (F.sheafPushforwardContinuous (Type w) (p.inheritedTopology J)
      (q.inheritedTopology J))
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafPushforwardCocontinuousCompSheafToPresheafIsoType`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L209). The attribute's comment: “`f_* = {}_pF` on sheaves of sets, with no hypothesis beyond the source's.”.

> **Stacks 06NW, `f_* = {}_pF`, for sheaves of sets.** On sheaves of sets, the direct image of
> the morphism of topoi induced by a 1-morphism `F` of fibred categories over a site is the right Kan
> extension along `F.op`, with no sheafification; the Kan extensions exist with no further
> hypothesis. No fibre products of the base are assumed.

```lean
noncomputable def IsFibredOneMorphism.sheafPushforwardCocontinuousCompSheafToPresheafIsoType :
    letI := hF.isCocontinuous_inheritedTopology J
    F.sheafPushforwardCocontinuous (Type (max u₂ v₃ w)) (p.inheritedTopology J)
          (q.inheritedTopology J) ⋙
        sheafToPresheaf (q.inheritedTopology J) (Type (max u₂ v₃ w)) ≅
      sheafToPresheaf (p.inheritedTopology J) (Type (max u₂ v₃ w)) ⋙ F.op.ran
```

**`CategoryTheory.Functor.IsFibredOneMorphism.sheafAdjunctionCocontinuousType`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L221). The attribute's comment: “The adjunction `f⁻¹ ⊣ f_*` on sheaves of sets, no hypothesis beyond the source's.”.

> **Stacks 06NW, the adjunction `f⁻¹ ⊣ f_*`, for sheaves of sets.** On sheaves of sets,
> restriction along `F.op` is left adjoint to the right Kan extension along `F.op`, with no
> hypothesis beyond the source's. No fibre products of the base are assumed.

```lean
noncomputable def IsFibredOneMorphism.sheafAdjunctionCocontinuousType :
    letI := hF.isContinuous_inheritedTopology J
    letI := hF.isCocontinuous_inheritedTopology J
    F.sheafPushforwardContinuous (Type (max u₂ v₃ w)) (p.inheritedTopology J)
        (q.inheritedTopology J) ⊣
      F.sheafPushforwardCocontinuous (Type (max u₂ v₃ w)) (p.inheritedTopology J)
        (q.inheritedTopology J)
```

**`CategoryTheory.Functor.IsFibredOneMorphism.morphismOfTopoiType`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/OneMorphismTopoi.lean#L237). The attribute's comment: “The morphism of topoi `f : Sh(𝒳) ⟶ Sh(𝒴)` of sheaves of sets, with no hypothesis beyond the source's.”.

> **Stacks 06NW, the morphism of topoi, for sheaves of sets.** A 1-morphism `F : 𝒳 ⥤ 𝒴` of
> fibred categories over a site `(𝒞, J)` induces a morphism of topoi `f : Sh(𝒳) ⟶ Sh(𝒴)` between the
> topoi of sheaves of sets on the inherited sites, with `f⁻¹ = F^p` restriction along `F.op` and
> `f_* = {}_pF` the right Kan extension along `F.op`. No hypothesis beyond the source's: in
> particular no fibre products of the base.

```lean
noncomputable def IsFibredOneMorphism.morphismOfTopoiType :
    MorphismOfTopoi (Sheaf (p.inheritedTopology J) (Type (max u₂ v₃ w)))
      (Sheaf (q.inheritedTopology J) (Type (max u₂ v₃ w)))
```

## Tag 0CN0, a lemma

[Tag 0CN0](https://stacks.math.columbia.edu/tag/0CN0) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.isEquivalence_overPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean#L114). The attribute's comment: “the equivalence of categories 𝒳/x ⥤ 𝒞/U”.

> For `p : 𝒳 ⥤ 𝒞` fibred in groupoids and `x` an object of `𝒳`, the functor
> `Over.post p : 𝒳/x ⥤ 𝒞/p x` induced by `p` is an equivalence of categories.

```lean
theorem IsFiberedInGroupoids.isEquivalence_overPost (hp : p.IsFiberedInGroupoids) (x : 𝒳) :
    (Over.post (X := x) p).IsEquivalence
```

**`CategoryTheory.Functor.IsInheritedTopology.mem_over_iff_functorPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Gerbe/Localization.lean#L153). The attribute's comment: “coverings of x' in 𝒳/x correspond to coverings of p x' in 𝒞/U”.

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

**`CategoryTheory.Functor.isStackInGroupoids_of_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/Basic.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/Basic.lean#L35).

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

**`CategoryTheory.Functor.isStack_comp_of_isInheritedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/StackOverStack/IsStack.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/StackOverStack/IsStack.lean#L315).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
