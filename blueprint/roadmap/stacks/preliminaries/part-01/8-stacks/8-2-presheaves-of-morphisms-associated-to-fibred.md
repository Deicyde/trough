---
declaration: section
origin: cited
lean: CategoryTheory.Functor.morRestrict_id, CategoryTheory.Functor.morRestrict_comp, CategoryTheory.Functor.morPresheaf, CategoryTheory.Functor.isomSubpresheaf, CategoryTheory.Functor.IsFibredOneMorphism.morPresheafMap, CategoryTheory.strictMorPresheaf, CategoryTheory.Functor.IsFibredEquivalenceOver.isIso_morPresheafMap, CategoryTheory.Functor.morPresheafIsoStrictMorPresheafGrpd
statement: formalized
proof: formalized
---

# 8.2 Presheaves of morphisms associated to fibred categories

Section 8.2 of the Stacks Project, [Tag 02Z9](https://stacks.math.columbia.edu/tag/02Z9). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 026A, a lemma

[Tag 026A](https://stacks.math.columbia.edu/tag/026A) in the Stacks Project.

**`CategoryTheory.Functor.morRestrict_id`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/MorPresheaf.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/MorPresheaf.lean#L131). The attribute's comment: “restriction along the identity”.

> Restricting a section of `Mor(x, y)` along an identity of `𝒮/U` leaves it unchanged.

```lean
lemma morRestrict_id (x y : p.Fiber U) (g : Over U)
    (m : pullbackFiber p x g.hom ⟶ pullbackFiber p y g.hom) :
    morRestrict p x y (𝟙 g) m = m
```

**`CategoryTheory.Functor.morRestrict_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/MorPresheaf.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/MorPresheaf.lean#L139). The attribute's comment: “compatibility with composition: φ|\_\{V″} = (φ|\_\{V′})|\_\{V″}”.

> Restricting a section of `Mor(x, y)` along a composite is restricting along the two factors in
> turn.

```lean
lemma morRestrict_comp (x y : p.Fiber U) {g₁ g₂ g₃ : Over U} (h₁ : g₁ ⟶ g₂) (h₂ : g₂ ⟶ g₃)
    (m : pullbackFiber p x g₃.hom ⟶ pullbackFiber p y g₃.hom) :
    morRestrict p x y (h₁ ≫ h₂) m = morRestrict p x y h₁ (morRestrict p x y h₂ m)
```

## Tag 02ZB, a definition

[Tag 02ZB](https://stacks.math.columbia.edu/tag/02ZB) in the Stacks Project.

**`CategoryTheory.Functor.morPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/MorPresheaf.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/MorPresheaf.lean#L150).

> The presheaf `Mor(x, y)` on `𝒮/U` of a fibred category `p`: its sections over `f : V ⟶ U` are
> the morphisms `f^* x ⟶ f^* y` of the fibre over `V`, and its restriction maps are
> `CategoryTheory.Functor.morRestrict`.

```lean
noncomputable def morPresheaf (x y : p.Fiber U) : (Over U)ᵒᵖ ⥤ Type v₂
```

**`CategoryTheory.Functor.isomSubpresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/IsomPresheaf.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/IsomPresheaf.lean#L120). The attribute's comment: “The subpresheaf `Isom(x, y)` of `Mor(x, y)`; the presheaf `Mor(x, y)` itself is `CategoryTheory.Functor.morPresheaf`.”.

> **Stacks 02ZB**, the subpresheaf `Isom(x, y)` of `Mor(x, y)`: over `f : V ⟶ U` its sections are
> the morphisms `f^* x ⟶ f^* y` of the fibre over `V` that are isomorphisms. This is a subpresheaf
> because restriction preserves isomorphisms, `CategoryTheory.Functor.isIso_morRestrict`.

```lean
noncomputable def isomSubpresheaf (x y : p.Fiber U) : Subfunctor (morPresheaf p x y)
```

## Tag 042V, a lemma

[Tag 042V](https://stacks.math.columbia.edu/tag/042V) in the Stacks Project.

**`CategoryTheory.Functor.IsFibredOneMorphism.morPresheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/TwoFibreProductMorPresheafMap.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/TwoFibreProductMorPresheafMap.lean#L380).

> The map of presheaves `Mor(x, y) ⟶ Mor(F x, F y)` induced by a 1-morphism of fibred categories
> over `𝒞`: over `g` it applies `F` to a section and conjugates by the comparison isomorphisms
> `IsFibredOneMorphism.mapPullbackFiberIso`.

```lean
noncomputable def morPresheafMap (hF : IsFibredOneMorphism p r₀ F₀) {U : 𝒞} (a b : p.Fiber U) :
    morPresheaf p a b ⟶ morPresheaf r₀ ((fiberFunctorOfCompEq hF.comp_eq U).obj a)
      ((fiberFunctorOfCompEq hF.comp_eq U).obj b)
```

## Tag 02ZA, a remark

[Tag 02ZA](https://stacks.math.columbia.edu/tag/02ZA) in the Stacks Project.

**`CategoryTheory.strictMorPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean, line 1025](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean#L1025). The attribute's comment: “for the fibred category of a functor F : 𝒞ᵒᵖ ⥤ Cat, where g^* ∘ f^* = (f ∘ g)^* on the nose, Lemma 026A with no maps α\_\{g, f}: the presheaf axioms of Mor(x, y) are F.map\_id and F.map\_comp”.

> **The presheaf `Mor(x, y)` of a split fibred category**, Stacks 02ZA. For an honest functor
> `F : 𝒞ᵒᵖ ⥤ Cat` and objects `x`, `y` of `F(U)`, the presheaf on `𝒞/U` whose sections over
> `f : V ⟶ U` are the morphisms `F(f) x ⟶ F(f) y` of `F(V)`, and whose restriction maps are the
> functors `F(h)`. Because `F(h) ∘ F(f) = F(f ∘ h)` holds on the nose, the presheaf axioms are the
> functoriality of `F` and no comparison isomorphisms `α_{g, f}` are needed.

```lean
def strictMorPresheaf (x y : F.obj (op U)) : (Over U)ᵒᵖ ⥤ Type v₃
```

**`CategoryTheory.Functor.IsFibredEquivalenceOver.isIso_morPresheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/StrictMorPresheaf.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/StrictMorPresheaf.lean#L88). The attribute's comment: “Mor(x, y) is unchanged when passing to an equivalent fibred category: the map of 042V along an equivalence of fibred categories is an isomorphism of presheaves”.

> **`Mor(x, y)` is unchanged along an equivalence of fibred categories** (Stacks 02ZA, from
> Stacks 042V). If `G : 𝒳 ⥤ 𝒴` is an equivalence in the 2-category of fibred categories over `𝒞`,
> then the map of presheaves `Mor(x, y) ⟶ Mor(G x, G y)` of Stacks 042V is an isomorphism.

```lean
theorem isIso_morPresheafMap (hG : IsFibredEquivalenceOver p q G) {U : 𝒞} (a b : p.Fiber U) :
    IsIso (hG.isFibredOneMorphism.morPresheafMap a b)
```

**`CategoryTheory.Functor.morPresheafIsoStrictMorPresheafGrpd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/StrictMorPresheaf.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/StrictMorPresheaf.lean#L119). The attribute's comment: “Mor(x, y) of a category fibred in groupoids is the strict Mor presheaf of the split model F : 𝒞ᵒᵖ ⥤ Grpd of 004A, whose restriction maps are the functors F(h) with g^* ∘ f^* = (f ∘ g)^* on the nose”.

> **Stacks 02ZA.** Let `p : 𝒳 ⥤ 𝒞` be fibred in groupoids, and let `x`, `y` be objects of the
> fibre over `U`. By Stacks 02XY (the groupoid case of Stacks 004A) `p` is equivalent to the fibred
> category of the functor `F = splitPresheafGrpd p hp : 𝒞ᵒᵖ ⥤ Grpd`, and the presheaf `Mor(x, y)`
> of `p` is isomorphic to the presheaf `Mor((x, id), (y, id))` of that split model, whose
> restriction maps are the functors `F(h)` and need no comparison isomorphisms.

```lean
noncomputable def morPresheafIsoStrictMorPresheafGrpd (hp : p.IsFiberedInGroupoids)
    (x y : p.Fiber U) :
    morPresheaf p x y ≅
      strictMorPresheaf (splitPresheafGrpd p hp ⋙ Grpd.forgetToCat)
        (SplitFiber.ofFiber p x) (SplitFiber.ofFiber p y)
```

Declarations registered for the tag:

- [`CategoryTheory.Pseudofunctor.LocallyDiscreteOpToCat.pullHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.LocallyDiscreteOpToCat.pullHom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean#L21) (StacksCore): “Remark 8.2.4 observes that a category fibred in groupoids is equivalent to the fibred category of a contravariant functor into groupoids, and that for the latter the restriction maps of the presheaf Mor(x, y) of Definition 8.2.2 need no coherence isomorphisms. Mathlib works in exactly that model: for a pseudofunctor from the locally discrete bicategory on the opposite of the base into Cat, this is the restriction map from a morphism of the fibre over Y to a morphism of the fibre over Y', with the coherence isomorphisms carried by mapComp'.”.
- [`CategoryTheory.Pseudofunctor.LocallyDiscreteOpToCat.pullHom_id`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.LocallyDiscreteOpToCat.pullHom_id#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean#L29) (StacksCore): “Restriction along an identity is the identity, the first half of the functoriality that Remark 8.2.4 says is trivial in this model.”.
- [`CategoryTheory.Pseudofunctor.LocallyDiscreteOpToCat.pullHom_pullHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.LocallyDiscreteOpToCat.pullHom_pullHom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean#L32) (StacksCore): “Restriction respects composition, the second half of that functoriality.”.
- [`CategoryTheory.Pseudofunctor.presheafHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.presheafHom#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Descent/MorphismPresheaf.lean#L34) (StacksCore): “The presheaf Mor(x, y) itself: the presheaf on Over S whose sections over a morphism p : X ⟶ S are the morphisms from the pullback of M along p to the pullback of N along p. Assembling it is Lemma 8.2.1, which Remark 8.2.4 is a remark about; the further ingredient the remark cites, invariance of Mor(x, y) under an equivalence of fibred categories (Lemma 042V), is not covered here.”.

## Tag 04SI, a lemma

[Tag 04SI](https://stacks.math.columbia.edu/tag/04SI) in the Stacks Project.

**`CategoryTheory.Functor.isFiberedInSetoids_and_isoClassPresheaf_iso_isomPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/IsomPresheafTwoFibreProduct.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/IsomPresheafTwoFibreProduct.lean#L582).

> **Stacks 04SI.** Let `𝒞` be a category, let `p : 𝒮 ⥤ 𝒞` be a fibred category, let `U` be an
> object of `𝒞` and let `x`, `y` be objects of the fibre category `𝒮_U`. Denote `x`, `y : 𝒞/U ⥤ 𝒮`
> also the corresponding 1-morphisms `(a : V ⟶ U) ↦ a^* x` (Stacks 004B). Then
>
> 1. the 2-fibre product `𝒮 ×_{𝒮 × 𝒮, (x, y)} 𝒞/U`, whose objects over `a : V ⟶ U` are the triples
>    `(z, α : z ≅ a^* x, β : z ≅ a^* y)` with `z` an object and `α`, `β` isomorphisms of `𝒮_V`, is
>    fibred in setoids over `𝒞/U`, and
> 2. `Isom(x, y)` is the presheaf of sets corresponding to that category fibred in setoids
>    (Stacks 04SC), namely its presheaf of isomorphism classes of objects of the fibres, the
>    identification sending the class of `(z, α, β)` to `β ∘ α⁻¹`.
>
> The second part is an isomorphism of presheaves, hence data: it is
> `CategoryTheory.Functor.IsomPresheafTwoFibreProduct.presheafIso`, pinned by the requirement that
> it send the class of `(z, α, β)` to `β ∘ α⁻¹`, which determines it, every class being the class
> of such a triple.

```lean
noncomputable def isFiberedInSetoids_and_isoClassPresheaf_iso_isomPresheaf
    (p : 𝒮 ⥤ 𝒞) [p.IsFibered] {U : 𝒞} (x y : p.Fiber U) :
    PProd (IsomPresheafTwoFibreProduct.proj p x y).IsFiberedInSetoids
      { e : (IsomPresheafTwoFibreProduct.proj p x y).isoClassPresheaf ≅
          p.isomPresheaf x y ⋙ uliftFunctor.{max u₁ v₁ u₂, v₂} //
        ∀ P : IsomPresheafTwoFibreProduct.Tot p x y,
          (e.hom.app (op P.y) (isoClassMk _ ⟨P, rfl⟩)).down.1.1 = P.iso.inv.1 ≫ P.iso.hom.2 }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.2, Tag 02Z9](https://stacks.math.columbia.edu/tag/02Z9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
