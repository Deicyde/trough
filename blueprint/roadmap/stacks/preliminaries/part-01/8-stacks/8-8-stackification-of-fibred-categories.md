---
declaration: section
origin: cited
lean: CategoryTheory.Functor.exists_isStackification, CategoryTheory.Functor.Stackification.extend, CategoryTheory.Functor.Stackification.extend_isFibredOneMorphism, CategoryTheory.Functor.Stackification.unit, CategoryTheory.Functor.Stackification.isHomLift_unit_app, CategoryTheory.Functor.Stackification.restrict_isEquivalence, CategoryTheory.Functor.Stackification.restrictEquivalence, CategoryTheory.TwoFibreProductOver.isStackification_stackifyMap
statement: formalized
proof: formalized
---

# 8.8 Stackification of fibred categories

Section 8.8 of the Stacks Project, [Tag 02ZM](https://stacks.math.columbia.edu/tag/02ZM). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02ZN, a lemma

[Tag 02ZN](https://stacks.math.columbia.edu/tag/02ZN) in the Stacks Project.

**`CategoryTheory.Functor.exists_isStackification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/Stackification.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/Stackification.lean#L80).

> Let `(𝒞, J)` be a site and let `q : 𝒴 ⥤ 𝒞` be a fibred category. There exist
> a stack `q' : 𝒴' ⥤ 𝒞` over `(𝒞, J)` and a 1-morphism `G : 𝒴 ⥤ 𝒴'` of fibred categories over `𝒞`
> such that
>
> 1. for every `U` and all `x`, `y` in the fibre `𝒴_U` the map `Mor(x, y) ⟶ Mor(G x, G y)` of
>    presheaves on `𝒞/U` exhibits its target as the sheafification of its source, and
> 2. every object of a fibre of `𝒴'` is, along a covering sieve of the base, in the essential image
>    of the functor induced by `G` on fibres.
>
> The objects and morphisms of `𝒴'` live in `Type (max t₁ t₂ w vb)`, the morphism universe of
> `𝒴`.

```lean
theorem exists_isStackification :
    ∃ (𝒴' : Type (max t₁ t₂ w vb)) (inst : Category.{max t₁ t₂ w vb} 𝒴'),
      letI := inst
      ∃ (q' : 𝒴' ⥤ 𝒞) (instq : q'.IsFibered),
        letI := instq
        ∃ (G : 𝒴 ⥤ 𝒴') (hG : q.IsFibredOneMorphism q' G),
          q'.IsStack J ∧
            (∀ (U : 𝒞) (x y : q.Fiber U),
                Presheaf.IsLocallyInjective (J.over U) (hG.morPresheafMap x y) ∧
                  Presheaf.IsLocallySurjective (J.over U) (hG.morPresheafMap x y)) ∧
              ∀ (U : 𝒞) (x' : q'.Fiber U), ∃ R ∈ J U, ∀ ⦃V : 𝒞⦄ ⦃f : V ⟶ U⦄, R.arrows f →
                (fiberFunctorOfCompEq hG.comp_eq V).essImage (pullbackFiber q' x' f)
```

## Tag 0435, a lemma

[Tag 0435](https://stacks.math.columbia.edu/tag/0435) in the Stacks Project.

**`CategoryTheory.Functor.Stackification.extend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean, line 989](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean#L989).

> **The functor underlying the extension of `F` along `G`**, Stacks 0435. Its value on an object
> `X` of `𝒮'` is the object of `𝒳` to which the images under `F` of a chosen local presentation of
> `X` descend, and its value on a morphism is the morphism glued from the transfers along `G` of the
> transition morphisms of the chosen presentations.

```lean
noncomputable def extend : 𝒮' ⥤ 𝒳
```

**`CategoryTheory.Functor.Stackification.extend_isFibredOneMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean, line 1006](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean#L1006).

> **The extension is a 1-morphism of fibred categories over `𝒞`**: it is strictly over `𝒞` and
> preserves strongly cartesian morphisms.

```lean
theorem extend_isFibredOneMorphism :
    p'.IsFibredOneMorphism q (extend hG hF hmor hqmor hobj hdesc)
```

**`CategoryTheory.Functor.Stackification.unit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean, line 1225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean#L1225).

> **The 2-isomorphism `G ⋙ H ≅ F` of Stacks 0435.** Its component at `A` compares the object of
> `𝒳` that the chosen presentation of `G A` descends to with `F A`, and it is an isomorphism because
> both are descents of presentations of one and the same object of `𝒮'`.

```lean
noncomputable def unit : G ⋙ extend hG hF hmor hqmor hobj hdesc ≅ F
```

**`CategoryTheory.Functor.Stackification.isHomLift_unit_app`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean, line 1239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyFunctor.lean#L1239).

> Every component of the 2-isomorphism lies over an identity, so it is a 2-morphism of fibred
> categories over `𝒞`.

```lean
lemma isHomLift_unit_app (A : 𝒮) :
    q.IsHomLift (𝟙 (p.obj A)) ((unit hG hF hmor hqmor hobj hdesc).hom.app A)
```

## Tag 04W9, a lemma

[Tag 04W9](https://stacks.math.columbia.edu/tag/04W9) in the Stacks Project.

**`CategoryTheory.Functor.Stackification.restrict_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyUniqueness.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyUniqueness.lean#L850).

> **Stacks 04W9.** Restriction along a stackification `G : 𝒮 ⥤ 𝒮'` is an equivalence from the
> category of 1-morphisms `𝒮' ⥤ 𝒳` of fibred categories over `𝒞` into a stack, and their
> 2-morphisms, onto the category of 1-morphisms `𝒮 ⥤ 𝒳` and their 2-morphisms.

```lean
theorem restrict_isEquivalence : (restrictMor (q := q) hG).IsEquivalence
```

**`CategoryTheory.Functor.Stackification.restrictEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyUniqueness.lean, line 860](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/UniversalPropertyUniqueness.lean#L860).

> **The canonical equivalence of morphism categories of Stacks 04W9**,
> `Mor_{Stacks/𝒞}(𝒮', 𝒳) ≌ Mor_{Fib/𝒞}(𝒮, 𝒳)`. Its functor is restriction along the stackification
> `G`, and a quasi-inverse is the extension of Stacks 0435.

```lean
noncomputable def restrictEquivalence : FibredMor p' q ≌ FibredMor p q
```

## Tag 04Y1, a lemma

[Tag 04Y1](https://stacks.math.columbia.edu/tag/04Y1) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isStackification_stackifyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stackification/TwoFibreProduct.lean, line 1332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stackification/TwoFibreProduct.lean#L1332).

> **Stacks 04Y1.** Let `(𝒞, J)` be a site, let `f : 𝒳 ⥤ 𝒴` and `g : 𝒵 ⥤ 𝒴` be 1-morphisms of
> fibred categories over `𝒞`, and let `i : 𝒳 ⥤ 𝒳'`, `j : 𝒴 ⥤ 𝒴'`, `k : 𝒵 ⥤ 𝒵'` be stackifications
> (Stacks 02ZP: the targets are stacks over `(𝒞, J)`, the induced maps `Mor(x, y) ⟶ Mor(i x, i y)` of
> presheaves on `𝒞/U` are locally bijective, and every object of the target is locally in the
> essential image), and let `f' : 𝒳' ⥤ 𝒴'`, `g' : 𝒵' ⥤ 𝒴'` be 1-morphisms of fibred categories over
> `𝒞` 2-commuting with `f` and `g` along `i`, `j`, `k` via vertical 2-isomorphisms `α`, `β`. Then the
> stackification of the 2-fibre product is the 2-fibre product of the stackifications: the 2-fibre
> product `𝒳' ×_{𝒴'} 𝒵'` is a stack over `(𝒞, J)` — it is a fibred category by Stacks 02XQ — and the
> canonical 1-morphism `𝒳 ×_𝒴 𝒵 ⥤ 𝒳' ×_{𝒴'} 𝒵'`,
> `CategoryTheory.TwoFibreProductOver.stackifyMap`, is a 1-morphism of fibred categories over `𝒞`
> which is a stackification of `𝒳 ×_𝒴 𝒵`, in the same two clauses.

```lean
theorem isStackification_stackifyMap {J : GrothendieckTopology 𝒞}
    (h𝒳 : p𝒳.IsFibered) (h𝒴 : p𝒴.IsFibered) (h𝒵 : p𝒵.IsFibered)
    (hs𝒳' : p𝒳'.IsStack J) (hs𝒴' : p𝒴'.IsStack J) (hs𝒵' : p𝒵'.IsStack J)
    (hf : p𝒳.IsFibredOneMorphism p𝒴 f) (hg : p𝒵.IsFibredOneMorphism p𝒴 g)
    (hf' : p𝒳'.IsFibredOneMorphism p𝒴' f') (hg' : p𝒵'.IsFibredOneMorphism p𝒴' g')
    (hi : p𝒳.IsFibredOneMorphism p𝒳' i) (hj : p𝒴.IsFibredOneMorphism p𝒴' j)
    (hk : p𝒵.IsFibredOneMorphism p𝒵' k)
    (hmor𝒳 : haveI : p𝒳.IsFibered := h𝒳
      haveI : p𝒳'.IsFibered := hs𝒳'.isFibered
      ∀ (V : 𝒞) (x₁ x₂ : p𝒳.Fiber V),
        Presheaf.IsLocallyInjective (J.over V) (hi.morPresheafMap x₁ x₂) ∧
          Presheaf.IsLocallySurjective (J.over V) (hi.morPresheafMap x₁ x₂))
    (hobj𝒳 : ∀ x' : 𝒳', ∃ R ∈ J (p𝒳'.obj x'), ∀ ⦃V : 𝒞⦄ (u : V ⟶ p𝒳'.obj x'), R.arrows u →
      ∃ (x : 𝒳) (φ : i.obj x ⟶ x'), p𝒳'.IsStronglyCartesian u φ)
    (hmor𝒴 : haveI : p𝒴.IsFibered := h𝒴
      haveI : p𝒴'.IsFibered := hs𝒴'.isFibered
      ∀ (V : 𝒞) (y₁ y₂ : p𝒴.Fiber V),
        Presheaf.IsLocallyInjective (J.over V) (hj.morPresheafMap y₁ y₂) ∧
          Presheaf.IsLocallySurjective (J.over V) (hj.morPresheafMap y₁ y₂))
    (_hobj𝒴 : ∀ y' : 𝒴', ∃ R ∈ J (p𝒴'.obj y'), ∀ ⦃V : 𝒞⦄ (u : V ⟶ p𝒴'.obj y'), R.arrows u →
      ∃ (y : 𝒴) (φ : j.obj y ⟶ y'), p𝒴'.IsStronglyCartesian u φ)
    (hmor𝒵 : haveI : p𝒵.IsFibered := h𝒵
      haveI : p𝒵'.IsFibered := hs𝒵'.isFibered
      ∀ (V : 𝒞) (z₁ z₂ : p𝒵.Fiber V),
        Presheaf.IsLocallyInjective (J.over V) (hk.morPresheafMap z₁ z₂) ∧
          Presheaf.IsLocallySurjective (J.over V) (hk.morPresheafMap z₁ z₂))
    (hobj𝒵 : ∀ z' : 𝒵', ∃ R ∈ J (p𝒵'.obj z'), ∀ ⦃V : 𝒞⦄ (u : V ⟶ p𝒵'.obj z'), R.arrows u →
      ∃ (z : 𝒵) (φ : k.obj z ⟶ z'), p𝒵'.IsStronglyCartesian u φ)
    (α : i ⋙ f' ≅ f ⋙ j) (hα : ∀ x : 𝒳, p𝒴'.IsHomLift (𝟙 (p𝒳.obj x)) (α.hom.app x))
    (β : k ⋙ g' ≅ g ⋙ j) (hβ : ∀ z : 𝒵, p𝒴'.IsHomLift (𝟙 (p𝒵.obj z)) (β.hom.app z)) :
    haveI : p𝒳.IsFibered := h𝒳
    haveI : p𝒴.IsFibered := h𝒴
    haveI : p𝒵.IsFibered := h𝒵
    haveI : p𝒳'.IsFibered := hs𝒳'.isFibered
    haveI : p𝒴'.IsFibered := hs𝒴'.isFibered
    haveI : p𝒵'.IsFibered := hs𝒵'.isFibered
    haveI : (structureFunctor p𝒳 p𝒵 p𝒴 f g).IsFibered :=
      isFibered_structureFunctor p𝒳 p𝒵 p𝒴 f g hf hg
    haveI : (structureFunctor p𝒳' p𝒵' p𝒴' f' g').IsFibered :=
      isFibered_structureFunctor p𝒳' p𝒵' p𝒴' f' g' hf' hg'
    (structureFunctor p𝒳' p𝒵' p𝒴' f' g').IsStack J ∧
      ∃ hH : Functor.IsFibredOneMorphism (structureFunctor p𝒳 p𝒵 p𝒴 f g)
          (structureFunctor p𝒳' p𝒵' p𝒴' f' g') (stackifyMap hi hj hk α hα β hβ),
        (∀ (U : 𝒞) (P Q : (structureFunctor p𝒳 p𝒵 p𝒴 f g).Fiber U),
            Presheaf.IsLocallyInjective (J.over U) (hH.morPresheafMap P Q) ∧
              Presheaf.IsLocallySurjective (J.over U) (hH.morPresheafMap P Q)) ∧
          ∀ P' : TwoFibreProductOver p𝒳' p𝒵' p𝒴' f' g', ∃ R ∈ J P'.base,
            ∀ ⦃V : 𝒞⦄ (u : V ⟶ P'.base), R.arrows u →
              ∃ (P : TwoFibreProductOver p𝒳 p𝒵 p𝒴 f g)
                (Φ : (stackifyMap hi hj hk α hα β hβ).obj P ⟶ P'),
                (structureFunctor p𝒳' p𝒵' p𝒴' f' g').IsStronglyCartesian u Φ
```

## Tag 06NS, a lemma

[Tag 06NS](https://stacks.math.columbia.edu/tag/06NS) in the Stacks Project.

**`CategoryTheory.RelativeInertia.isStackification_functoriality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/InertiaStackification.lean, line 1333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/InertiaStackification.lean#L1333).

> **The stackification of the inertia is the inertia of the stackification.** Let `(𝒞, J)` be a
> site, let `p : 𝒳 ⥤ 𝒞` be a fibred category over `𝒞` and let `G : 𝒳 ⥤ 𝒳'` be the stackification
> of `𝒳` (Stacks 02ZN): a 1-morphism `hG` of fibred categories over `𝒞` whose target `p'` is a
> stack, such that (`hmor`) for every `U` and all `x`, `y` in `𝒳_U` the induced map
> `Mor(x, y) ⟶ Mor(G x, G y)` of presheaves on `𝒞/U` is locally injective and locally surjective,
> its target being a sheaf, and such that (`hobj`) every object `x'` of `𝒳'` admits a covering
> sieve `R` of `p'.obj x'` with `x'|_V` in the essential image of `𝒳_V ⥤ 𝒳'_V` for every
> `f : V ⟶ p'.obj x'` in `R`.
>
> Then the inertia `I_{𝒳'}` is a stack over `𝒞`, and the functoriality 1-morphism
> `I_G : I_𝒳 ⥤ I_{𝒳'}`, `(x, α) ↦ (G x, G α)`, is a stackification of the inertia `I_𝒳`: it is a
> 1-morphism of fibred categories over `𝒞` and it satisfies the same two conditions.

```lean
public theorem RelativeInertia.isStackification_functoriality
    {p : 𝒳 ⥤ 𝒞} {p' : 𝒳' ⥤ 𝒞} {G : 𝒳 ⥤ 𝒳'} {J : GrothendieckTopology 𝒞} [p.IsFibered]
    (hG : p.IsFibredOneMorphism p' G) (hp' : p'.IsStack J)
    (hmor : haveI : p'.IsFibered := hp'.isFibered
      ∀ (U : 𝒞) (x y : p.Fiber U),
        Presheaf.IsLocallyInjective (J.over U)
            (Functor.IsFibredOneMorphism.morPresheafMap hG x y) ∧
          Presheaf.IsLocallySurjective (J.over U)
            (Functor.IsFibredOneMorphism.morPresheafMap hG x y))
    (hobj : ∀ x' : 𝒳', ∃ R ∈ J (p'.obj x'), ∀ ⦃V : 𝒞⦄ (f : V ⟶ p'.obj x'), R f →
      ∃ (y : 𝒳) (φ : G.obj y ⟶ x'), p'.IsStronglyCartesian f φ) :
    haveI : p'.IsFibered := hp'.isFibered
    haveI : (RelativeInertia.toBase p).IsFibered :=
      RelativeInertia.isFibered p p (𝟭 𝒞) inferInstance (Functor.isFibredOneMorphism_id p)
    haveI : (RelativeInertia.toBase p').IsFibered :=
      RelativeInertia.isFibered p' p' (𝟭 𝒞) hp'.isFibered (Functor.isFibredOneMorphism_id p')
    (RelativeInertia.toBase p').IsStack J ∧
      ∃ hIG : (RelativeInertia.toBase p).IsFibredOneMorphism (RelativeInertia.toBase p')
          (RelativeInertia.functoriality p p' G hG.comp_eq),
        (∀ (U : 𝒞) (A B : (RelativeInertia.toBase p).Fiber U),
            Presheaf.IsLocallyInjective (J.over U)
                (Functor.IsFibredOneMorphism.morPresheafMap hIG A B) ∧
              Presheaf.IsLocallySurjective (J.over U)
                (Functor.IsFibredOneMorphism.morPresheafMap hIG A B)) ∧
          ∀ A' : RelativeInertia p', ∃ R ∈ J ((RelativeInertia.toBase p').obj A'),
            ∀ ⦃V : 𝒞⦄ (f : V ⟶ (RelativeInertia.toBase p').obj A'), R f →
              ∃ (A : RelativeInertia p)
                (φ : (RelativeInertia.functoriality p p' G hG.comp_eq).obj A ⟶ A'),
                (RelativeInertia.toBase p').IsStronglyCartesian f φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.8, Tag 02ZM](https://stacks.math.columbia.edu/tag/02ZM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
