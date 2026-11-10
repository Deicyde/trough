---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsFiberedInGroupoids.existsUnique_vertical_factorisation, CategoryTheory.Functor.IsFiberedInGroupoids.twoStepLiftIso, CategoryTheory.Functor.IsFiberedInGroupoids.isIso_of_vertical_comp_eq, CategoryTheory.Functor.IsFiberedInGroupoids.iff_isFibered_and_fiber_isGroupoid, stronglyCartesianOver_isMultiplicative, CategoryTheory.CatFiberedInGroupoids, CategoryTheory.TwoFibreProductOver.isFiberedInGroupoids, CategoryTheory.Functor.IsFiberedInGroupoids.faithful_iff_forall_fiber
statement: formalized
proof: formalized
---

# 4.35 Categories fibred in groupoids

Section 4.35 of the Stacks Project, [Tag 003S](https://stacks.math.columbia.edu/tag/003S). 14 tags here are carried by 20 declarations of the repository (1 in StacksCore and 19 in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03WP, an equation

[Tag 03WP](https://stacks.math.columbia.edu/tag/03WP) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.existsUnique_vertical_factorisation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Lifts.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Lifts.lean#L52).

> **Stacks 03WP.**
> The two-step lift `ψ ∘ φ : z ⟶ x` of `g ∘ f` factors through the direct lift `γ : z' ⟶ x` by a
> unique morphism `χ : z ⟶ z'` of the fibre over `W`, i.e. a unique `χ` lying over `id_W`.

```lean
theorem existsUnique_vertical_factorisation :
    ∃! χ : z ⟶ z', p.IsHomLift (𝟙 W) χ ∧ χ ≫ γ = ψ ≫ φ
```

**`CategoryTheory.Functor.IsFiberedInGroupoids.twoStepLiftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Lifts.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Lifts.lean#L62).

> **Stacks 03WP.**
> The comparison isomorphism `z ≅ z'` between the domain of the two-step lift of `g ∘ f` and the
> domain of a direct lift of `g ∘ f`. Both lifts are cartesian, so this is the canonical
> isomorphism between the domains of two cartesian lifts of one morphism of the base.

```lean
noncomputable def twoStepLiftIso : z ≅ z'
```

**`CategoryTheory.Functor.IsFiberedInGroupoids.isIso_of_vertical_comp_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Lifts.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Lifts.lean#L83).

> **Stacks 03WP.**
> Every morphism `χ : z ⟶ z'` of the fibre over `W` filling the diagram is an isomorphism: by
> uniqueness it is the comparison isomorphism `CategoryTheory.Functor.twoStepLiftIso`.

```lean
lemma isIso_of_vertical_comp_eq (χ : z ⟶ z') [p.IsHomLift (𝟙 W) χ] (hχ : χ ≫ γ = ψ ≫ φ) :
    IsIso χ
```

## Tag 003V, a lemma

[Tag 003V](https://stacks.math.columbia.edu/tag/003V) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.iff_isFibered_and_fiber_isGroupoid`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/FiberedInGroupoidsEquiv.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/FiberedInGroupoidsEquiv.lean#L165).

> **Stacks 003V (Lemma 4.35.2).** A functor `p : 𝒮 ⥤ 𝒞` is fibred in groupoids
> if and only if it is a fibred category all of whose fibres are groupoids.

```lean
theorem iff_isFibered_and_fiber_isGroupoid :
    p.IsFiberedInGroupoids ↔ p.IsFibered ∧ ∀ S, IsGroupoid (p.Fiber S)
```

## Tag 03WQ, a lemma

[Tag 03WQ](https://stacks.math.columbia.edu/tag/03WQ) in the Stacks Project.

**`stronglyCartesianOver_isMultiplicative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/MultiplicativeClass.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/MultiplicativeClass.lean#L96). References: SGA 1 VI (6.13); SGA 1 VI (6.8), “Well-definedness of F̃”; SGA 4 VI (6.4), “Fr1”.

> **Stacks tag 03WQ** (auxiliary multiplicativity).
> The morphism property `stronglyCartesianOver p` (strongly cartesian morphisms over
> their image) contains identities and is closed under composition — this is the
> content of the first sentence of the Stacks proof, namely that the subcategory
> `𝒮'` of strongly cartesian morphisms is well-defined as a subcategory.

```lean
theorem stronglyCartesianOver_isMultiplicative
    {𝒞 : Type*} [Category 𝒞] {𝒮 : Type*} [Category 𝒮]
    (p : 𝒮 ⥤ 𝒞) [p.IsFibered] :
    (stronglyCartesianOver p).IsMultiplicative
```

## Tag 02XS, a definition

[Tag 02XS](https://stacks.math.columbia.edu/tag/02XS) in the Stacks Project.

**`CategoryTheory.CatFiberedInGroupoids`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/TwoCategory.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/TwoCategory.lean#L116).

> The 2-category of categories fibred in groupoids over `𝒞`: the full sub-2-category of the
> 2-category `BasedCategory 𝒞` of categories over `𝒞` (Stacks 003Y) spanned by the categories fibred
> in groupoids. Explicitly:
>
> 1. its objects are the categories `p : 𝒮 ⥤ 𝒞` over `𝒞` that are fibred in groupoids;
> 2. its 1-morphisms `(𝒮, p) ⟶ (𝒮', p')` are the functors `G : 𝒮 ⥤ 𝒮'` with `p' ∘ G = p`
>    (no condition on strongly cartesian morphisms is needed: see
>    `CatFiberedInGroupoids.isStronglyCartesian_map`);
> 3. its 2-morphisms `t : G ⟶ H` are the morphisms of functors with `p'(t_x) = 𝟙 (p x)` for every
>    object `x` of `𝒮`.

```lean
abbrev CatFiberedInGroupoids (𝒞 : Type u₁) [Category.{v₁} 𝒞]
```

## Tag 0041, a lemma

[Tag 0041](https://stacks.math.columbia.edu/tag/0041) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/TwoFibreProduct.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/TwoFibreProduct.lean#L132).

> **Stacks 0041.** The 2-category of categories fibred in groupoids over `𝒞` has 2-fibre
> products, given by the construction of Stacks 0040: if `p𝒳`, `p𝒴`, `p𝒮` are fibred in groupoids
> and `F`, `G` are strictly over `𝒞`, then the structure functor of `𝒳 ×_𝒮 𝒴` is fibred in
> groupoids.

```lean
theorem isFiberedInGroupoids (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒮 : 𝒮 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒮) (G : 𝒴 ⥤ 𝒮)
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (h𝒮 : p𝒮.IsFiberedInGroupoids) (hF : F ⋙ p𝒮 = p𝒳) (hG : G ⋙ p𝒮 = p𝒴) :
    (structureFunctor p𝒳 p𝒴 p𝒮 F G).IsFiberedInGroupoids
```

## Tag 003Z, a lemma

[Tag 003Z](https://stacks.math.columbia.edu/tag/003Z) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.faithful_iff_forall_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean#L207). The attribute's comment: “(1)”. References: SGA 1 VI (6.10), “fibred in groupoids”.

> **Stacks 003Z (1).** `G` is faithful if and only if for every object `U` of `C` the
> induced functor `G_U : S_U ⥤ S'_U` on fibres is faithful.

```lean
theorem IsFiberedInGroupoids.faithful_iff_forall_fiber (p : S ⥤ C) (p' : S' ⥤ C)
    (hp : p.IsFiberedInGroupoids) (hp' : p'.IsFiberedInGroupoids) (G : S ⥤ S')
    (hG : G ⋙ p' = p) : G.Faithful ↔ ∀ U : C, (Fiber.mapOfComp p p' G hG U).Faithful
```

**`CategoryTheory.Functor.IsFiberedInGroupoids.full_and_faithful_iff_forall_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean#L216). The attribute's comment: “(1)”. References: SGA 1 VI (6.10), “fibred in groupoids”.

> **Stacks 003Z (1).** `G` is full and faithful if and only if for every object `U` of `C` the
> induced functor `G_U : S_U ⥤ S'_U` on fibres is full and faithful.

```lean
theorem IsFiberedInGroupoids.full_and_faithful_iff_forall_fiber (p : S ⥤ C) (p' : S' ⥤ C)
    (hp : p.IsFiberedInGroupoids) (hp' : p'.IsFiberedInGroupoids) (G : S ⥤ S')
    (hG : G ⋙ p' = p) : (G.Full ∧ G.Faithful) ↔
      ∀ U : C, ((Fiber.mapOfComp p p' G hG U).Full ∧ (Fiber.mapOfComp p p' G hG U).Faithful)
```

**`CategoryTheory.Functor.IsFiberedInGroupoids.isEquivalence_iff_forall_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean#L279). The attribute's comment: “(1)”. References: SGA 1 VI (6.10), “fibred in groupoids”; SGA 1 VI (4.2), “(iii)”.

> **Stacks 003Z (1).** `G` is an equivalence of categories if and only if for every object
> `U` of `C` the induced functor `G_U : S_U ⥤ S'_U` on fibres is an equivalence.

```lean
theorem IsFiberedInGroupoids.isEquivalence_iff_forall_fiber (p : S ⥤ C) (p' : S' ⥤ C)
    (hp : p.IsFiberedInGroupoids) (hp' : p'.IsFiberedInGroupoids) (G : S ⥤ S')
    (hG : G ⋙ p' = p) :
    G.IsEquivalence ↔ ∀ U : C, (Fiber.mapOfComp p p' G hG U).IsEquivalence
```

**`CategoryTheory.Functor.IsFiberedInGroupoids.isEquivalence_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Fibrewise.lean#L367). The attribute's comment: “(2)”.

> **Stacks 003Z (2).** If `G` is an equivalence of categories, then `G` is an equivalence
> in the 2-category of categories fibred in groupoids over `C`: there are a functor
> `F : S' ⥤ S` over `C` (that is, `F ⋙ p = p'`) and natural isomorphisms `G ⋙ F ≅ 𝟭 S` and
> `F ⋙ G ≅ 𝟭 S'` all of whose components lie over identity morphisms of `C`.

```lean
theorem IsFiberedInGroupoids.isEquivalence_over (p : S ⥤ C) (p' : S' ⥤ C)
    (hp : p.IsFiberedInGroupoids) (hp' : p'.IsFiberedInGroupoids)
    (G : S ⥤ S') (hG : G ⋙ p' = p) (hGequiv : G.IsEquivalence) :
    ∃ (F : S' ⥤ S) (_ : F ⋙ p = p') (η : G ⋙ F ≅ 𝟭 S) (ε : F ⋙ G ≅ 𝟭 S'),
      (∀ x : S, p.IsHomLift (𝟙 (p.obj x)) (η.hom.app x)) ∧
      (∀ x' : S', p'.IsHomLift (𝟙 (p'.obj x')) (ε.hom.app x'))
```

## Tag 04Z7, a lemma

[Tag 04Z7](https://stacks.math.columbia.edu/tag/04Z7) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.full_and_faithful_iff_isEquivalence_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Diagonal.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Diagonal.lean#L252).

> **Stacks 04Z7.** Let `p𝒮 : 𝒮 ⥤ 𝒞` and `p𝒮' : 𝒮' ⥤ 𝒞` be categories fibred in groupoids and
> let `G : 𝒮 ⥤ 𝒮'` be a 1-morphism over `𝒞`. Then `G` is fully faithful if and only if the diagonal
> `Δ_G : 𝒮 ⥤ 𝒮 ×_{G, 𝒮', G} 𝒮` is an equivalence.

```lean
theorem full_and_faithful_iff_isEquivalence_diagonal (h𝒮 : p𝒮.IsFiberedInGroupoids)
    (h𝒮' : p𝒮'.IsFiberedInGroupoids) (hG : G ⋙ p𝒮' = p𝒮) :
    (G.Full ∧ G.Faithful) ↔ (diagonal hG).IsEquivalence
```

## Tag 03YT, a lemma

[Tag 03YT](https://stacks.math.columbia.edu/tag/03YT) in the Stacks Project.

**`main_theorem03YT`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Conjugation.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Conjugation.lean#L132). References: SGA 1 VI (4.5), “both displayed maps”.

> **Stacks 03YT.** For `𝒮₁, …, 𝒮₄` over `𝒞` and equivalences `φ : 𝒮₁ ⟶ 𝒮₂`,
> `ψ : 𝒮₃ ⟶ 𝒮₄` over `𝒞`, conjugation `α ↦ ψ ∘ α ∘ φ` is an equivalence of hom-categories
> `Mor_{Cat/𝒞}(𝒮₂, 𝒮₃) ⥤ Mor_{Cat/𝒞}(𝒮₁, 𝒮₄)`.
>
> The source additionally assumes each `𝒮ᵢ` is fibred in groupoids over `𝒞`.  Conjugation by
> equivalences is an equivalence in any bicategory, so that hypothesis is unused; it is
> omitted here and the statement proved is correspondingly more general than the tag.

```lean
theorem main_theorem03YT
    (𝒮₁ 𝒮₂ 𝒮₃ 𝒮₄ : BasedCategory 𝒞)
    (eφ : Bicategory.Equivalence 𝒮₁ 𝒮₂)
    (eψ : Bicategory.Equivalence 𝒮₃ 𝒮₄) :
    (conjugationFunctor eφ.hom eψ.hom).IsEquivalence
```

## Tag 042I, a lemma

[Tag 042I](https://stacks.math.columbia.edu/tag/042I) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.absoluteInertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Inertia.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Inertia.lean#L59).

> **Stacks 042I.** If `p : S ⥤ C` is fibred in groupoids, then so is the inertia fibred
> category `I_S ⥤ C`.

```lean
theorem absoluteInertia (p : S ⥤ C) (hp : p.IsFiberedInGroupoids) :
    (relativeInertiaStruct p p).IsFiberedInGroupoids
```

## Tag 02XT, a lemma

[Tag 02XT](https://stacks.math.columbia.edu/tag/02XT) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.of_comp_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Slice.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Slice.lean#L89).

> **Stacks 02XT.** If `p : 𝒮 ⥤ 𝒞` is fibred in groupoids and factors through the slice
> category `Over U` as `p' ⋙ Over.forget U = p`, then `p' : 𝒮 ⥤ Over U` is fibred in
> groupoids: lifts of morphisms of `Over U` and unique fill-ins for `p'` are obtained from those
> for `p`, because the structure morphism of a lifted object is forced and `Over.forget U` is
> faithful.

```lean
theorem IsFiberedInGroupoids.of_comp_over
    {𝒮 𝒞 : Type*} [Category 𝒮] [Category 𝒞] (U : 𝒞)
    (p : 𝒮 ⥤ 𝒞) (p' : 𝒮 ⥤ Over U)
    (h : p' ⋙ Over.forget U = p) (hp : p.IsFiberedInGroupoids) :
    p'.IsFiberedInGroupoids
```

## Tag 09WW, a lemma

[Tag 09WW](https://stacks.math.columbia.edu/tag/09WW) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Comp.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Comp.lean#L50).

> **Stacks 09WW.** The composition of two functors that are fibred in groupoids is
> fibred in groupoids.

```lean
theorem IsFiberedInGroupoids.comp (p : 𝒜 ⥤ ℬ) (q : ℬ ⥤ 𝒞)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids) :
    (p ⋙ q).IsFiberedInGroupoids
```

## Tag 06N6, a lemma

[Tag 06N6](https://stacks.math.columbia.edu/tag/06N6) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.hasPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/FibreProducts.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/FibreProducts.lean#L132). The attribute's comment: “(1)”.

> Let `p` be fibred in groupoids and let `gx : x ⟶ y`, `gz : z ⟶ y` be morphisms of `S`. If
> the fibre product of `p.map gx` and `p.map gz` exists in `C`, then the fibre product of `gx` and
> `gz` exists in `S`.

```lean
theorem IsFiberedInGroupoids.hasPullback
    (p : S ⥤ C) (hp : p.IsFiberedInGroupoids)
    {x y z : S} (gx : x ⟶ y) (gz : z ⟶ y)
    [Limits.HasPullback (p.map gx) (p.map gz)] :
    Limits.HasPullback gx gz
```

**`CategoryTheory.Functor.IsFiberedInGroupoids.map_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/FibreProducts.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/FibreProducts.lean#L145). The attribute's comment: “(2)”.

> For any fibre product `x ×_y z` in `S`, realized by a pullback square with vertex `P` and
> projections `pr₁ : P ⟶ x`, `pr₂ : P ⟶ z`, the image `p.obj P` together with `p.map pr₁` and
> `p.map pr₂` is a fibre product of `p.map gx` and `p.map gz` in `C`: `p` carries the pullback
> square of `S` to a pullback square of `C`.

```lean
theorem IsFiberedInGroupoids.map_isPullback
    (p : S ⥤ C) (hp : p.IsFiberedInGroupoids)
    {x y z : S} (gx : x ⟶ y) (gz : z ⟶ y)
    [Limits.HasPullback (p.map gx) (p.map gz)]
    {P : S} (pr₁ : P ⟶ x) (pr₂ : P ⟶ z)
    (hP : IsPullback pr₁ pr₂ gx gz) :
    IsPullback (p.map pr₁) (p.map pr₂) (p.map gx) (p.map gz)
```

## Tag 06N7, a lemma

[Tag 06N7](https://stacks.math.columbia.edu/tag/06N7) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInGroupoids.exists_factorization_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Factorization.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Factorization.lean#L450).

> **Stacks 06N7 (Lemma 4.35.16).** Let `𝒞` be a category and let `𝒳`, `𝒴` be categories
> fibred in groupoids over `𝒞` via `p : 𝒳 ⥤ 𝒞` and `q : 𝒴 ⥤ 𝒞`. Let `F : 𝒳 ⥤ 𝒴` be a
> 1-morphism over `𝒞` (`F ⋙ q = p`). Then there exist a category `𝒳'`, a structure functor
> `r : 𝒳' ⥤ 𝒞` and functors `a : 𝒳 ⥤ 𝒳'`, `t : 𝒳' ⥤ 𝒴` such that
>
> 1. `r` is fibred in groupoids over `𝒞`;
> 2. `a` is a 1-morphism over `𝒞` (`a ⋙ r = p`) and an equivalence over `𝒞`;
> 3. `t` is a 1-morphism over `𝒞` (`t ⋙ q = r`) and is fibred in groupoids over `𝒴`;
> 4. `a ⋙ t = F`.

```lean
theorem IsFiberedInGroupoids.exists_factorization_isFiberedInGroupoids
    {𝒞 : Type u₂} [Category.{v₂} 𝒞]
    {𝒳 : Type u₁} [Category.{v₁} 𝒳] (p : 𝒳 ⥤ 𝒞) (hp : p.IsFiberedInGroupoids)
    {𝒴 : Type u₃} [Category.{v₃} 𝒴] (q : 𝒴 ⥤ 𝒞) (hq : q.IsFiberedInGroupoids)
    (F : 𝒳 ⥤ 𝒴) (hF : F ⋙ q = p) :
    ∃ (𝒳' : Type (max u₁ u₃ v₁ v₃)) (_ : Category.{max v₁ v₃} 𝒳')
      (r : 𝒳' ⥤ 𝒞) (a : 𝒳 ⥤ 𝒳') (t : 𝒳' ⥤ 𝒴),
      r.IsFiberedInGroupoids ∧
      (a ⋙ r = p) ∧ Nonempty (IsEquivalenceOver p r a) ∧
      (t ⋙ q = r) ∧ t.IsFiberedInGroupoids ∧
      (a ⋙ t = F)
```

## Tag 06N8, a lemma

[Tag 06N8](https://stacks.math.columbia.edu/tag/06N8) in the Stacks Project.

**`amelioration_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/AmeliorationUniqueness.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/AmeliorationUniqueness.lean#L42).

> **Stacks 06N8** (uniqueness of the factorization of 4.35.16 / 06N7).
>
> Let `F : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in groupoids over `𝒞`. Suppose `F`
> is factored in two ways through categories fibred in groupoids over `𝒞`:
> `𝒳 ⟶[a] 𝒳' ⟶[f] 𝒴` and `𝒳 ⟶[b] 𝒳'' ⟶[g] 𝒴`, where
>
> * `a`, `b` are equivalences (over `𝒞`);
> * the two factorizations agree with `F`: `a ⋙ f ≅ F` and `b ⋙ g ≅ F`.
>
> Then there is an equivalence `h : 𝒳'' ⥤ 𝒳'` **over `𝒴`** (i.e. `h.IsEquivalence` together
> with `h ⋙ f ≅ g`) such that `b ⋙ h ≅ a`. In particular the intermediate category is unique
> up to equivalence over `𝒴`, compatibly with the first legs.
>
> The conclusion uses none of the remaining data of 06N8 — the structure functors
> `p : 𝒳 ⥤ 𝒞`, `q : 𝒴 ⥤ 𝒞`, `p' : 𝒳' ⥤ 𝒞`, `p'' : 𝒳'' ⥤ 𝒞`, their fiberedness in
> groupoids, that of `f` and `g`, and the compatibilities `a ⋙ p' = p`, `b ⋙ p'' = p`,
> `f ⋙ q = p'`, `g ⋙ q = p''` — so it is stated in the general form below, which
> specializes to 06N8 in the fibred setting.

```lean
theorem amelioration_unique
    {𝒞 : Type u₁} [Category.{v₁} 𝒞]
    {𝒳 : Type u₂} [Category.{v₂} 𝒳]
    {𝒴 : Type u₃} [Category.{v₃} 𝒴]
    {𝒳' : Type u₄} [Category.{v₄} 𝒳']
    {𝒳'' : Type u₅} [Category.{v₅} 𝒳'']
    (F : 𝒳 ⥤ 𝒴) (a : 𝒳 ⥤ 𝒳') (b : 𝒳 ⥤ 𝒳'')
    (f : 𝒳' ⥤ 𝒴) (g : 𝒳'' ⥤ 𝒴)
    (ha_equiv : a.IsEquivalence) (hb_equiv : b.IsEquivalence)
    (hleft : a ⋙ f ≅ F) (hright : b ⋙ g ≅ F) :
    ∃ (h : 𝒳'' ⥤ 𝒳') (_ : h.IsEquivalence) (_ : h ⋙ f ≅ g),
      Nonempty (b ⋙ h ≅ a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.35, Tag 003S](https://stacks.math.columbia.edu/tag/003S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
