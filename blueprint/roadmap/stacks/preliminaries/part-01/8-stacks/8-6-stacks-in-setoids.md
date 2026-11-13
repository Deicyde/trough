---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsStackInSetoids, CategoryTheory.Functor.IsStackInSets, CategoryTheory.Functor.isStackInSets_iff_isSheaf_objPresheaf, CategoryTheory.BasedCategory.isStackInSetoids_iff_isStackInSets_of_equivalence, CategoryTheory.BasedCategory.isStackInSetoids_iff_isSheaf_objPresheaf_of_equivalence, CategoryTheory.BasedCategory.isStackInSetoids_iff_of_equivalence, CategoryTheory.StackInSetoids, CategoryTheory.StackInSetoids.bicategory
statement: formalized
proof: formalized
---

# 8.6 Stacks in setoids

Section 8.6 of the Stacks Project, [Tag 042Y](https://stacks.math.columbia.edu/tag/042Y). 11 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 042Z, a definition

[Tag 042Z](https://stacks.math.columbia.edu/tag/042Z) in the Stacks Project.

**`CategoryTheory.Functor.IsStackInSetoids`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean#L91). The attribute's comment: “(1)”.

> **Stacks 042Z**.
> A *stack in setoids* over the site `(𝒞, J)`: a stack over `𝒞` all of whose fibre categories are
> setoids, that is groupoids in which there is at most one morphism between any two objects.

```lean
structure Functor.IsStackInSetoids (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) : Prop
```

**`CategoryTheory.Functor.IsStackInSets`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean#L104). The attribute's comment: “(2)”.

> **Stacks 042Z**.
> A *stack in sets*, also called a *stack in discrete categories*, over the site `(𝒞, J)`: a stack
> over `𝒞` all of whose fibre categories are discrete.

```lean
structure Functor.IsStackInSets (p : 𝒮 ⥤ 𝒞) (J : GrothendieckTopology 𝒞) : Prop
```

## Tag 0430, a lemma

[Tag 0430](https://stacks.math.columbia.edu/tag/0430) in the Stacks Project.

**`CategoryTheory.Functor.isStackInSets_iff_isSheaf_objPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FiberedInSets.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/FiberedInSets.lean#L272).

> Let `(𝒞, J)` be a site. Under the equivalence of Categories, Stacks 02Y2 between presheaves of
> sets on `𝒞` and categories fibred in sets over `𝒞`, the stacks in sets correspond precisely to the
> sheaves: a category fibred in sets `p : 𝒮 ⥤ 𝒞` is a stack in sets over `(𝒞, J)` if and only if its
> presheaf of objects `U ↦ Ob(𝒮_U)` is a sheaf.

```lean
theorem isStackInSets_iff_isSheaf_objPresheaf (J : GrothendieckTopology 𝒞) :
    p.IsStackInSets J ↔ Presheaf.IsSheaf J (objPresheaf p)
```

## Tag 0432, a lemma

[Tag 0432](https://stacks.math.columbia.edu/tag/0432) in the Stacks Project.

**`CategoryTheory.BasedCategory.isStackInSetoids_iff_isStackInSets_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/SetoidToSets.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/SetoidToSets.lean#L117).

> Let `(𝒞, J)` be a site, let `𝒳` be a category fibred in setoids over `𝒞`, and let `𝒴` be a
> category fibred in sets equivalent to `𝒳` as a category over `𝒞`. Then `𝒳` is a stack in setoids if
> and only if `𝒴` is a stack in sets.

```lean
theorem BasedCategory.isStackInSetoids_iff_isStackInSets_of_equivalence
    {𝒞 : Type u₁} [Category.{v₁} 𝒞] {𝒳 𝒴 : BasedCategory.{v₂, u₂} 𝒞}
    (e : BasedCategory.Equivalence 𝒳 𝒴) [𝒳.p.IsFiberedInSetoids] [𝒴.p.IsFiberedInSets]
    (J : GrothendieckTopology 𝒞) :
    𝒳.p.IsStackInSetoids J ↔ 𝒴.p.IsStackInSets J
```

**`CategoryTheory.BasedCategory.isStackInSetoids_iff_isSheaf_objPresheaf_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/SetoidToSets.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/SetoidToSets.lean#L131). The attribute's comment: “the "in other words" sentence: iff the presheaf `U ↦ Ob(𝒮_U)/≅` is a sheaf”.

> Let `(𝒞, J)` be a site, let `𝒳` be a category fibred in setoids over `𝒞`, and let `𝒴` be a
> category fibred in sets equivalent to `𝒳` as a category over `𝒞`. Then `𝒳` is a stack in setoids if
> and only if the presheaf of objects `U ↦ Ob(𝒴_U)` of `𝒴` is a sheaf. Its value at `U` is identified
> with the set `Ob(𝒳_U)/≅` of isomorphism classes of the fibre of `𝒳` over `U` by
> `CategoryTheory.BasedCategory.Equivalence.fiberQuotientEquiv`.

```lean
theorem BasedCategory.isStackInSetoids_iff_isSheaf_objPresheaf_of_equivalence
    {𝒞 : Type u₁} [Category.{v₁} 𝒞] {𝒳 𝒴 : BasedCategory.{v₂, u₂} 𝒞}
    (e : BasedCategory.Equivalence 𝒳 𝒴) [𝒳.p.IsFiberedInSetoids] [𝒴.p.IsFiberedInSets]
    (J : GrothendieckTopology 𝒞) :
    𝒳.p.IsStackInSetoids J ↔ Presheaf.IsSheaf J (Functor.objPresheaf 𝒴.p)
```

## Tag 0431, a lemma

[Tag 0431](https://stacks.math.columbia.edu/tag/0431) in the Stacks Project.

**`CategoryTheory.BasedCategory.isStackInSetoids_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Transport.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/Transport.lean#L40).

> Let `(𝒞, J)` be a site and let `𝒳`, `𝒴` be categories over `𝒞`. If `𝒳` and `𝒴` are equivalent
> as categories over `𝒞`, then `𝒳` is a stack in setoids over `𝒞` if and only if `𝒴` is.

```lean
theorem BasedCategory.isStackInSetoids_iff_of_equivalence
    (e : BasedCategory.Equivalence 𝒳 𝒴) (J : GrothendieckTopology 𝒞) :
    𝒳.p.IsStackInSetoids J ↔ 𝒴.p.IsStackInSetoids J
```

## Tag 0433, a definition

[Tag 0433](https://stacks.math.columbia.edu/tag/0433) in the Stacks Project.

**`CategoryTheory.StackInSetoids`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean#L134).

> **Stacks 0433**.
> An object of the 2-category of stacks in setoids over the site `(𝒞, J)`: a category over `𝒞`
> whose structure functor is a stack in setoids.

```lean
structure StackInSetoids (𝒞 : Type u₁) [Category.{v₁} 𝒞] (J : GrothendieckTopology 𝒞)
```

**`CategoryTheory.StackInSetoids.bicategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/Setoid.lean#L148).

> **Stacks 0433**.
> The 2-category of stacks in setoids over the site `(𝒞, J)`: the full sub-2-category of the
> 2-category `BasedCategory 𝒞` of categories over `𝒞` spanned by the stacks in setoids. A
> 1-morphism `𝒳 ⟶ 𝒴` is a functor `G` over `𝒞`, that is with `p' ∘ G = p`, and a 2-morphism
> `F ⟶ G` is a morphism of functors `t` with `p'(t_x) = 𝟙 (p x)` for every object `x`.

```lean
instance StackInSetoids.bicategory : Bicategory (StackInSetoids.{v₁, v₂, u₁, u₂} 𝒞 J)
```

## Tag 0434, a lemma

[Tag 0434](https://stacks.math.columbia.edu/tag/0434) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isStackInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/SetoidTwoFibreProduct.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/SetoidTwoFibreProduct.lean#L144).

> **Stacks 0434.** The 2-fibre product of stacks in setoids over a site `(𝒞, J)` is a stack in
> setoids: the construction of Stacks 0040 does not leave the 2-category of stacks in setoids.
>
> Its three conditions are Stacks 026G (`isStack_structureFunctor`), Stacks 0041
> (`fiber_isGroupoid`) and thinness of the fibres (`fiber_isThin`). Nothing is asked of `F` and `G`
> beyond being strictly over `𝒞`, since a functor over `𝒞` into a category fibred in groupoids
> automatically preserves strongly cartesian morphisms.

```lean
theorem isStackInSetoids {J : GrothendieckTopology 𝒞} (h𝒳 : p𝒳.IsStackInSetoids J)
    (h𝒴 : p𝒴.IsStackInSetoids J) (h𝒮 : p𝒮.IsStackInSetoids J)
    (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) :
    (structureFunctor p𝒳 p𝒴 p𝒮 F G).IsStackInSetoids J
```

## Tag 05UI, a lemma

[Tag 05UI](https://stacks.math.columbia.edu/tag/05UI) in the Stacks Project.

**`CategoryTheory.Functor.isStackInSetoids_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/TwoFibreProductSetoid.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/TwoFibreProductSetoid.lean#L98).

> Let `𝒯` be a stack in groupoids and `𝒮` a stack over the site `(𝒞, J)`, and let `ℛ` be a
> stack in setoids. Let `f : 𝒯 ⥤ 𝒮` and `g : ℛ ⥤ 𝒮` be 1-morphisms with `f` faithful. Then the
> 2-fibre product `𝒯 ×_{f, 𝒮, g} ℛ` is a stack in setoids.

```lean
theorem Functor.isStackInSetoids_twoFibreProduct (J : GrothendieckTopology 𝒞)
    (h𝒯 : Functor.IsStack p𝒯 J) (g𝒯 : p𝒯.IsFiberedInGroupoids)
    (hℛ : pℛ.IsStackInSetoids J) (h𝒮 : Functor.IsStack p𝒮 J)
    (hF : p𝒯.IsFibredOneMorphism p𝒮 f) (hG : pℛ.IsFibredOneMorphism p𝒮 g) [f.Faithful] :
    (TwoFibreProductOver.structureFunctor p𝒯 pℛ p𝒮 f g).IsStackInSetoids J
```

## Tag 05UJ, a lemma

[Tag 05UJ](https://stacks.math.columbia.edu/tag/05UJ) in the Stacks Project.

**`CategoryTheory.Functor.isStackInSetoids_twoFibreProduct_of_isStackInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/TwoFibreProductSetoid.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/InheritedTopology/TwoFibreProductSetoid.lean#L109).

> Let `𝒮` be a stack over the site `(𝒞, J)` and let `𝒮₁`, `𝒮₂` be stacks in setoids, with
> 1-morphisms `f_i : 𝒮_i ⥤ 𝒮`. Then `𝒮₁ ×_{f₁, 𝒮, f₂} 𝒮₂` is a stack in setoids.

```lean
theorem Functor.isStackInSetoids_twoFibreProduct_of_isStackInSetoids
    (J : GrothendieckTopology 𝒞)
    (h𝒯 : p𝒯.IsStackInSetoids J) (hℛ : pℛ.IsStackInSetoids J)
    (h𝒮 : Functor.IsStack p𝒮 J)
    (hF : p𝒯.IsFibredOneMorphism p𝒮 f) (hG : pℛ.IsFibredOneMorphism p𝒮 g) :
    (TwoFibreProductOver.structureFunctor p𝒯 pℛ p𝒮 f g).IsStackInSetoids J
```

## Tag 06DV, a lemma

[Tag 06DV](https://stacks.math.columbia.edu/tag/06DV) in the Stacks Project.

**`CategoryTheory.Functor.faithful_of_faithful_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FaithfulDescent.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/FaithfulDescent.lean#L253).

> **Stacks 06DV**. In a 2-cartesian diagram of categories fibred in groupoids over a site with
> `𝒯₁` a stack, if every object of a fibre of `𝒮₁` is locally in the essential image of
> `F : 𝒮₂ ⥤ 𝒮₁` and the first projection `𝒮₂ ×_{𝒮₁} 𝒯₁ ⥤ 𝒮₂` is faithful, then `G : 𝒯₁ ⥤ 𝒮₁` is
> faithful.
>
> By Stacks 003Z faithfulness may be checked on the fibres; there the fibres of `𝒯₁` are groupoids,
> so two morphisms `α`, `β : y ⟶ y'` with `G α = G β` differ by the endomorphism `β ∘ α⁻¹` of `y`,
> which `G` sends to the identity and which is therefore the identity by
> `CategoryTheory.Functor.eq_id_of_map_eq_id_of_locallyEssSurj`.

```lean
theorem faithful_of_faithful_fst (hFeq : F ⋙ p𝒮₁ = p𝒮₂) (hGeq : G ⋙ p𝒮₁ = p𝒯₁)
    (hgpd₁ : p𝒮₁.IsFiberedInGroupoids) (hgpdT : p𝒯₁.IsFiberedInGroupoids)
    {J : GrothendieckTopology 𝒞} (hstack : p𝒯₁.IsStack J)
    (hloc : LocallyEssSurjOnFibers hgpd₁.isFibered hFeq J)
    (hfst : (TwoFibreProductOver.fst p𝒮₂ p𝒯₁ p𝒮₁ F G).Faithful) :
    G.Faithful
```

## Tag 05W9, a lemma

[Tag 05W9](https://stacks.math.columbia.edu/tag/05W9) in the Stacks Project.

**`CategoryTheory.Functor.isStackInSetoids_of_isStackInSetoids_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/SetoidDescent.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/SetoidDescent.lean#L124).

> **Stacks 05W9**. In a 2-cartesian diagram of stacks in groupoids over a site, if `F` is fully
> faithful, every object of a fibre of `𝒮₁` is locally in the essential image of `F`, and the 2-fibre
> product `𝒮₂ ×_{𝒮₁} 𝒯₁` is a stack in setoids, then `𝒯₁` is a stack in setoids.
>
> Being a stack and having groupoid fibres are hypotheses — they are what makes `𝒯₁` a stack in
> groupoids — so the content is thinness of the fibres of `𝒯₁`, and that is
> `CategoryTheory.Functor.eq_id_of_fibre_isThin_of_locallyEssSurj` applied to `β ∘ α⁻¹`, the fibres
> of `𝒯₁` being groupoids.

```lean
theorem isStackInSetoids_of_isStackInSetoids_twoFibreProduct (hFeq : F ⋙ p𝒮₁ = p𝒮₂)
    (hGeq : G ⋙ p𝒮₁ = p𝒯₁) (hgpd₁ : p𝒮₁.IsFiberedInGroupoids)
    (hgpd₂ : p𝒮₂.IsFiberedInGroupoids) (hgpdT : p𝒯₁.IsFiberedInGroupoids)
    [F.Full] [F.Faithful] {J : GrothendieckTopology 𝒞} (hstack : p𝒯₁.IsStack J)
    (hloc : LocallyEssSurjOnFibers hgpd₁.isFibered hFeq J)
    (hT₂ : (TwoFibreProductOver.structureFunctor p𝒮₂ p𝒯₁ p𝒮₁ F G).IsStackInSetoids J) :
    p𝒯₁.IsStackInSetoids J
```

## Tag 0CKJ, a lemma

[Tag 0CKJ](https://stacks.math.columbia.edu/tag/0CKJ) in the Stacks Project.

**`CategoryTheory.Functor.isStack_of_faithful_of_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FaithfulGroupoidDescent.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Stack/FaithfulGroupoidDescent.lean#L320).

> **Descent along a faithful 1-morphism into a stack in groupoids.** Let `(𝒞, J)` be a site and
> let `F : 𝒮 ⥤ 𝒯` be a 1-morphism of categories fibred in groupoids over `𝒞`, that is a functor
> with `F ⋙ q = p`. Assume that (1) `𝒯` is a stack in groupoids over `𝒞`, (2) for every object `U`
> of `𝒞` the functor `𝒮_U ⥤ 𝒯_U` of fibre categories is faithful, and (3) for every object `y` of
> `𝒯` over `U` the presheaf on `𝒞/U` sending `h : V ⟶ U` to the isomorphism classes of pairs
> `(x, f)` with `x` an object of `𝒮_V` and `f : F(x) ⟶ h^* y` a morphism of `𝒯_V` is a sheaf. Then
> `𝒮` is a stack in groupoids over `𝒞`.
>
> Condition (3) is the two hypotheses `hsep` and `hglue`, in which a pair over `h` is a morphism
> `f : F.obj x ⟶ y` lying over `h`, and the class of `(x₂, f₂)` is the restriction of the class of
> `(x₁, f₁)` along `g : W ⟶ V` when `F.map c ≫ f₁ = f₂` for some lift `c : x₂ ⟶ x₁` of `g`.

```lean
public theorem isStack_of_faithful_of_isSheaf {p : 𝒮 ⥤ 𝒞} {q : 𝒯 ⥤ 𝒞} {F : 𝒮 ⥤ 𝒯}
    {J : GrothendieckTopology 𝒞} (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (hF : F ⋙ q = p) (hT : q.IsStack J)
    (hfaithful : ∀ U : 𝒞, (Fiber.fiberInclusion (p := p) (S := U) ⋙ F).Faithful)
    (hsep : ∀ (y : 𝒯) ⦃V : 𝒞⦄ (h : V ⟶ q.obj y) (R : Sieve V), R ∈ J V →
      ∀ ⦃x x' : 𝒮⦄ (f : F.obj x ⟶ y) (f' : F.obj x' ⟶ y),
        q.IsHomLift h f → q.IsHomLift h f' →
        (∀ ⦃W : 𝒞⦄ (g : W ⟶ V), R g → ∃ (z : 𝒮) (c : z ⟶ x) (c' : z ⟶ x'),
          p.IsHomLift g c ∧ p.IsHomLift g c' ∧ F.map c ≫ f = F.map c' ≫ f') →
        ∃ e : x ⟶ x', p.IsHomLift (𝟙 V) e ∧ F.map e ≫ f' = f)
    (hglue : ∀ (y : 𝒯) ⦃V : 𝒞⦄ (h : V ⟶ q.obj y) (R : Sieve V), R ∈ J V →
      ∀ (x : ∀ ⦃W : 𝒞⦄ (g : W ⟶ V), R g → 𝒮)
        (f : ∀ ⦃W : 𝒞⦄ (g : W ⟶ V) (hg : R g), F.obj (x g hg) ⟶ y),
        (∀ ⦃W : 𝒞⦄ (g : W ⟶ V) (hg : R g), q.IsHomLift (g ≫ h) (f g hg)) →
        (∀ ⦃W W' : 𝒞⦄ (g : W ⟶ V) (hg : R g) (k : W' ⟶ W),
          ∃ c : x (k ≫ g) (R.downward_closed hg k) ⟶ x g hg,
            p.IsHomLift k c ∧ F.map c ≫ f g hg = f (k ≫ g) (R.downward_closed hg k)) →
        ∃ (x₀ : 𝒮) (f₀ : F.obj x₀ ⟶ y), q.IsHomLift h f₀ ∧
          ∀ ⦃W : 𝒞⦄ (g : W ⟶ V) (hg : R g), ∃ c : x g hg ⟶ x₀,
            p.IsHomLift g c ∧ F.map c ≫ f₀ = f g hg) :
    p.IsStack J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.6, Tag 042Y](https://stacks.math.columbia.edu/tag/042Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
