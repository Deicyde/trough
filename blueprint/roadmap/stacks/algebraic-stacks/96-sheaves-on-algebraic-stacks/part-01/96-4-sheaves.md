---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.associatedTopology, AlgebraicGeometry.BigFppfOver.IsSheaf, AlgebraicGeometry.BigFppfOver.AssociatedSheaf, AlgebraicGeometry.BigFppfOver.isSheaf_comp_op_and_isSheaf_ran_obj, AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf, AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf_pushforwardCompSheafToPresheafIso, AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf_inverseImageCompSheafToPresheafIso, AlgebraicGeometry.BigFppfOver.isContinuous_and_isCocontinuous_associatedTopology
statement: formalized
proof: formalized
---

# 96.4 Sheaves

Section 96.4 of the Stacks Project, [Tag 06TN](https://stacks.math.columbia.edu/tag/06TN). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06TP, a definition

[Tag 06TP](https://stacks.math.columbia.edu/tag/06TP) in the Stacks Project.

**`AlgebraicGeometry.Stack.associatedTopology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSite.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSite.lean#L53).

> The site associated to a category `p : 𝒳 ⥤ (Sch/S)` over the big fppf category of `S` and a
> topology `τ` on the underlying category of schemes of `B`: the topology `𝒳` inherits from the
> localization of `τ` at `S`.

```lean
abbrev associatedTopology {X : Type v} [Category.{w} X] (p : X ⥤ BigFppfOver B S hS)
    (τ : GrothendieckTopology B.Schemes) : GrothendieckTopology X
```

## Tag 06TR, a definition

[Tag 06TR](https://stacks.math.columbia.edu/tag/06TR) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.IsSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L99). The attribute's comment: “sheaf conditions for the five topologies”.

> **Stacks 06TR.** A presheaf of sets on a category `p : 𝒳 ⥤ (Sch/S)` over the big fppf
> category of `S` is a *sheaf for the topology `τ`* when it is a sheaf on the associated site
> `𝒳_τ` of Stacks 06TP. The five values of `τ` give the Zariski, étale, smooth, syntomic and
> fppf sheaf conditions of the source.

```lean
abbrev IsSheaf (τ : SiteKind) (F : Xᵒᵖ ⥤ Type t) : Prop
```

**`AlgebraicGeometry.BigFppfOver.AssociatedSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L106). The attribute's comment: “categories and morphisms of sheaves”.

> **Stacks 06TR.** The category `Sh(𝒳_τ)` of sheaves of sets on the associated site `𝒳_τ`
> of Stacks 06TP, for `τ` one of the five topologies. Its morphisms are morphisms of the
> underlying presheaves.

```lean
abbrev AssociatedSheaf (τ : SiteKind)
```

## Tag 06TS, a lemma

[Tag 06TS](https://stacks.math.columbia.edu/tag/06TS) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isSheaf_comp_op_and_isSheaf_ran_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean#L101). The attribute's comment: “the functors f^p and {}_pf of presheaves of sets transform tau sheaves into tau sheaves”.

> **Stacks 06TS**, preservation of sheaves. For a 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred in
> groupoids over the big fppf category of `S` and `τ` one of the five topologies, the pullback
> `G^p 𝒢 = 𝒢 ∘ G` of a `τ` sheaf of sets `𝒢` on `𝒴` is a `τ` sheaf on `𝒳`, and the pushforward
> `{}_pG ℱ`, the right Kan extension of `ℱ` along `G`, of a `τ` sheaf of sets `ℱ` on `𝒳` is a `τ`
> sheaf on `𝒴`.

```lean
theorem isSheaf_comp_op_and_isSheaf_ran_obj :
    (∀ 𝒢 : 𝒴.val.objᵒᵖ ⥤ Type t, IsSheaf B S hS 𝒴.val.p τ 𝒢 →
      IsSheaf B S hS 𝒳.val.p τ ((CatFiberedInGroupoids.homFunctor G).op ⋙ 𝒢)) ∧
    ∀ ℱ : 𝒳.val.objᵒᵖ ⥤ Type (max v w t), IsSheaf B S hS 𝒳.val.p τ ℱ →
      IsSheaf B S hS 𝒴.val.p τ ((CatFiberedInGroupoids.homFunctor G).op.ran.obj ℱ)
```

**`AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean#L121). The attribute's comment: “the morphism of topoi f : Sh(X_tau) -> Sh(Y_tau) defined by f^p and {}_pf, for sheaves of sets”.

> **Stacks 06TS**, the morphism of topoi. A 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred in
> groupoids over the big fppf category of `S` defines, for each of the five topologies `τ`, a
> morphism of topoi `f : Sh(𝒳_τ) ⟶ Sh(𝒴_τ)` between the categories of sheaves of sets of Stacks
> 06TR: its inverse image `f⁻¹` is the pullback `G^p` of sheaves, its direct image `f_*` is the
> pushforward `{}_pG` of sheaves, `f⁻¹` is left adjoint to `f_*`, and `f⁻¹` is left exact.

```lean
noncomputable def morphismOfTopoi_associatedSheaf :
    MorphismOfTopoi (AssociatedSheaf.{u, v, w, max v w t} B S hS 𝒳.val.p τ)
      (AssociatedSheaf.{u, v, w, max v w t} B S hS 𝒴.val.p τ)
```

**`AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf_pushforwardCompSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean#L137). The attribute's comment: “the direct image of the morphism of topoi is the pushforward {}_pf of presheaves”.

> **Stacks 06TS**, `f_* = {}_pG`. The direct image of the morphism of topoi
> `AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf` is the pushforward of presheaves:
> on underlying presheaves it is the right Kan extension along `G.op`.

```lean
noncomputable def morphismOfTopoi_associatedSheaf_pushforwardCompSheafToPresheafIso :
    (morphismOfTopoi_associatedSheaf.{u, v, w, t} B S hS G τ).pushforward ⋙
        sheafToPresheaf (associatedTopology B S hS 𝒴.val.p τ) (Type max v w t) ≅
      sheafToPresheaf (associatedTopology B S hS 𝒳.val.p τ) (Type max v w t) ⋙
        (CatFiberedInGroupoids.homFunctor G).op.ran
```

**`AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf_inverseImageCompSheafToPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean#L148). The attribute's comment: “the inverse image of the morphism of topoi is the pullback f^p of presheaves”.

> **Stacks 06TS**, `f⁻¹ = G^p`. The inverse image of the morphism of topoi
> `AlgebraicGeometry.BigFppfOver.morphismOfTopoi_associatedSheaf` is the pullback of presheaves:
> on underlying presheaves it is precomposition with `G.op`.

```lean
noncomputable def morphismOfTopoi_associatedSheaf_inverseImageCompSheafToPresheafIso :
    (morphismOfTopoi_associatedSheaf.{u, v, w, t} B S hS G τ).inverseImage ⋙
        sheafToPresheaf (associatedTopology B S hS 𝒳.val.p τ) (Type max v w t) ≅
      sheafToPresheaf (associatedTopology B S hS 𝒴.val.p τ) (Type max v w t) ⋙
        (Functor.whiskeringLeft _ _ _).obj (CatFiberedInGroupoids.homFunctor G).op
```

**`AlgebraicGeometry.BigFppfOver.isContinuous_and_isCocontinuous_associatedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L169). The attribute's comment: “preservation of sheaves by both functors”.

> **Stacks 06TS**, preservation of sheaves by both functors. For each of the five topologies
> `τ`, the functor underlying a 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the
> big fppf category of `S` is continuous and cocontinuous between the associated sites `𝒳_τ` and
> `𝒴_τ` of Stacks 06TP. Continuity says that `G^p` carries `τ` sheaves on `𝒴` to `τ` sheaves on
> `𝒳` and cocontinuity that `{}_pG` carries `τ` sheaves on `𝒳` to `τ` sheaves on `𝒴`, which is the
> first assertion of the source.
>
> This is the instance of **Stacks 06NW**
> (`CategoryTheory.Functor.IsFibredOneMorphism.isContinuous_and_isCocontinuous_inheritedTopology`)
> at the base site `(Sch/S)_{fppf}` with the localized topology of `τ`.

```lean
public theorem isContinuous_and_isCocontinuous_associatedTopology (G : 𝒳 ⟶ 𝒴) (τ : SiteKind) :
    (CatFiberedInGroupoids.homFunctor G).IsContinuous
        (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ) ∧
      (CatFiberedInGroupoids.homFunctor G).IsCocontinuous
        (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ)
```

**`AlgebraicGeometry.BigFppfOver.inverseImageCompSheafToPresheafIso_associatedTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L187). The attribute's comment: “inverse image is restriction”.

> **Stacks 06TS**, `f⁻¹ = G^p`. The inverse image of the induced morphism of topoi
> `Sh(𝒳_τ) ⟶ Sh(𝒴_τ)` is plain restriction along `G.op`: as a functor to presheaves on `𝒳` it is
> `sheafToPresheaf` followed by precomposition with `G.op`, with no sheafification intervening.
>
> This is the instance of **Stacks 06NW**
> (`CategoryTheory.Functor.IsFibredOneMorphism.inverseImageCompSheafToPresheafIso`) at the five
> associated sites.

```lean
public def inverseImageCompSheafToPresheafIso_associatedTopology :
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).1
    (CatFiberedInGroupoids.homFunctor G).sheafPushforwardContinuous A
          (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ) ⋙
        sheafToPresheaf (associatedTopology B S hS 𝒳.val.p τ) A ≅
      sheafToPresheaf (associatedTopology B S hS 𝒴.val.p τ) A ⋙
        (Functor.whiskeringLeft _ _ _).obj (CatFiberedInGroupoids.homFunctor G).op
```

**`AlgebraicGeometry.BigFppfOver.inverseImage_obj_obj_obj_associatedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L206). The attribute's comment: “objectwise inverse image formula”.

> **Stacks 06TS**, the objectwise formula `f⁻¹(𝒢)(x) = 𝒢(G x)`: the sections of the inverse
> image of a `τ` sheaf `𝒢` on `𝒴` over an object `x` of `𝒳` are the sections of `𝒢` over `G x`.
>
> This is the instance of **Stacks 06NW**
> (`CategoryTheory.Functor.IsFibredOneMorphism.inverseImage_obj_obj_obj`) at the five associated
> sites.

```lean
public theorem inverseImage_obj_obj_obj_associatedTopology :
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).1
    ∀ (𝒢 : Sheaf (associatedTopology B S hS 𝒴.val.p τ) A) (x : 𝒳.val.obj),
      (((CatFiberedInGroupoids.homFunctor G).sheafPushforwardContinuous A
            (associatedTopology B S hS 𝒳.val.p τ)
            (associatedTopology B S hS 𝒴.val.p τ)).obj 𝒢).obj.obj (Opposite.op x) =
        𝒢.obj.obj (Opposite.op ((CatFiberedInGroupoids.homFunctor G).obj x))
```

**`AlgebraicGeometry.BigFppfOver.preservesFiniteLimits_inverseImage_associatedTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L223). The attribute's comment: “left exactness of inverse image”.

> **Stacks 06TS**, exactness of the inverse image. The inverse image of the induced morphism of
> topoi preserves finite limits, which is the remaining clause in "morphism of topoi".
>
> This is the instance of **Stacks 06NW**
> (`CategoryTheory.Functor.IsFibredOneMorphism.preservesFiniteLimits_inverseImage`) at the five
> associated sites.

```lean
public theorem preservesFiniteLimits_inverseImage_associatedTopology [Limits.HasFiniteLimits A] :
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).1
    Limits.PreservesFiniteLimits ((CatFiberedInGroupoids.homFunctor G).sheafPushforwardContinuous A
      (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ))
```

**`AlgebraicGeometry.BigFppfOver.directImageCompSheafToPresheafIso_associatedTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L238). The attribute's comment: “direct image is right Kan extension”.

> **Stacks 06TS**, `f_* = {}_pG`. The direct image of the induced morphism of topoi is the
> right Kan extension along `G.op`, taken on sheaves: as a functor to presheaves on `𝒴` it is
> `sheafToPresheaf` followed by `G.op.ran`.
>
> This is the instance of **Stacks 06NW**
> (`CategoryTheory.Functor.IsFibredOneMorphism.directImageCompSheafToPresheafIso`) at the five
> associated sites.

```lean
public noncomputable def directImageCompSheafToPresheafIso_associatedTopology
    [∀ (F : 𝒳.val.objᵒᵖ ⥤ A),
      (CatFiberedInGroupoids.homFunctor G).op.HasPointwiseRightKanExtension F] :
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).2
    (CatFiberedInGroupoids.homFunctor G).sheafPushforwardCocontinuous A
          (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ) ⋙
        sheafToPresheaf (associatedTopology B S hS 𝒴.val.p τ) A ≅
      sheafToPresheaf (associatedTopology B S hS 𝒳.val.p τ) A ⋙
        (CatFiberedInGroupoids.homFunctor G).op.ran
```

**`AlgebraicGeometry.BigFppfOver.sheafAdjunction_associatedTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L264). The attribute's comment: “adjunction defining the morphism of topoi”.

> **Stacks 06TS**, the morphism of topoi itself. A 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred
> in groupoids over the big fppf category of `S` induces, for each of the five topologies `τ`, a
> morphism of topoi `f : Sh(𝒳_τ) ⟶ Sh(𝒴_τ)`: this is the adjunction `f⁻¹ ⊣ f_*` between the two
> associated sites of Stacks 06TP, with `f⁻¹ = G^p` the restriction and `f_* = {}_pG` the right Kan
> extension. It is the actual adjunction, not an existence claim; together with
> `AlgebraicGeometry.BigFppfOver.preservesFiniteLimits_inverseImage_associatedTopology` it is a
> morphism of topoi in the source's sense.
>
> This is the instance of **Stacks 06NW**
> (`CategoryTheory.Functor.IsFibredOneMorphism.sheafAdjunctionInheritedTopology`) at the five
> associated sites.

```lean
public noncomputable def sheafAdjunction_associatedTopology
    [∀ (F : 𝒳.val.objᵒᵖ ⥤ A),
      (CatFiberedInGroupoids.homFunctor G).op.HasPointwiseRightKanExtension F] :
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).1
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).2
    (CatFiberedInGroupoids.homFunctor G).sheafPushforwardContinuous A
        (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ) ⊣
      (CatFiberedInGroupoids.homFunctor G).sheafPushforwardCocontinuous A
        (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ)
```

## Tag 06TT, a definition

[Tag 06TT](https://stacks.math.columbia.edu/tag/06TT) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.sheafAdjunction_associatedSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedSheaves.lean#L341). The attribute's comment: “the associated morphism of tau topoi f = (f^{-1}, f_*), for each of the five”.

> **Stacks 06TT.** The *associated morphism of `τ` topoi*
> `f = (f⁻¹, f_*) : Sh(𝒳_τ) ⟶ Sh(𝒴_τ)` of a 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred in
> groupoids over the big fppf category of `S`, for each of the five topologies `τ` — the Zariski,
> étale, smooth, syntomic and fppf ones. It is the adjunction `f⁻¹ ⊣ f_*` between the two categories
> `AlgebraicGeometry.BigFppfOver.AssociatedSheaf` of sheaves of sets on the associated sites of
> Stacks 06TP, with `f⁻¹ = G^p` the restriction along `G` and `f_* = {}_pG` the right Kan extension
> along `G.op`.
>
> The limits that compute `f_*` are supplied by
> `AlgebraicGeometry.BigFppfOver.hasPointwiseRightKanExtension_op_homFunctor`, a `Type (max v w)`
> having limits of the shapes that index them by `CategoryTheory.Limits.Types.hasLimitsOfSize`, so
> the data a reader must provide to obtain this morphism of topoi is a 1-morphism of categories
> fibred in groupoids over `(Sch/S)_fppf` and a choice among the five topologies, which is what the
> source provides. Left exactness of `f⁻¹`,
> the remaining clause of "morphism of topoi", is
> `AlgebraicGeometry.BigFppfOver.preservesFiniteLimits_inverseImage_associatedTopology` at these
> same coefficients.

```lean
public noncomputable def sheafAdjunction_associatedSheaf :
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).1
    letI := (isContinuous_and_isCocontinuous_associatedTopology B S hS G τ).2
    (CatFiberedInGroupoids.homFunctor G).sheafPushforwardContinuous (Type max v w)
        (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ) ⊣
      (CatFiberedInGroupoids.homFunctor G).sheafPushforwardCocontinuous (Type max v w)
        (associatedTopology B S hS 𝒳.val.p τ) (associatedTopology B S hS 𝒴.val.p τ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.4, Tag 06TN](https://stacks.math.columbia.edu/tag/06TN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
