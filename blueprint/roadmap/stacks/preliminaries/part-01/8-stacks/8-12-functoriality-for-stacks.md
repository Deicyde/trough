---
declaration: section
origin: cited
lean: CategoryTheory.StrictPullback.isFibered_structureFunctor, CategoryTheory.StrictPullback.isStack_structureFunctor, CategoryTheory.StrictPullback.isStack_isFiberedInGroupoids_structureFunctor, CategoryTheory.pushforwardFibredCategory, CategoryTheory.Comma.hasRightCalculusOfFractions_stronglyCartesianOver, CategoryTheory.Comma.pullbackLocalization, CategoryTheory.Comma.pullbackProj, CategoryTheory.Comma.isFibered_pullbackProj
statement: formalized
proof: formalized
---

# 8.12 Functoriality for stacks

Section 8.12 of the Stacks Project, [Tag 04WA](https://stacks.math.columbia.edu/tag/04WA). 12 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04WB, a lemma

[Tag 04WB](https://stacks.math.columbia.edu/tag/04WB) in the Stacks Project.

**`CategoryTheory.StrictPullback.isFibered_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/Pushforward.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/Pushforward.lean#L163).

> **Stacks 04WB**.
> If `p : 𝒮 ⥤ 𝒟` is a fibred category, then so is the pushforward `u^p𝒮 ⥤ 𝒞` along any
> functor `u : 𝒞 ⥤ 𝒟`.

```lean
theorem isFibered_structureFunctor (u : 𝒞 ⥤ 𝒟) (p : 𝒮 ⥤ 𝒟) [p.IsFibered] :
    (structureFunctor u p).IsFibered
```

## Tag 04WC, a lemma

[Tag 04WC](https://stacks.math.columbia.edu/tag/04WC) in the Stacks Project.

**`CategoryTheory.StrictPullback.isStack_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PushforwardStack.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PushforwardStack.lean#L66).

> **Stacks 04WC**.
> If `p : 𝒮 ⥤ 𝒟` is a stack over the site `(𝒟, K)`, then the pushforward `u^p𝒮 ⥤ 𝒞` along a
> continuous functor of sites `u : 𝒞 ⥤ 𝒟` is a stack over `(𝒞, J)`.
>
> Continuity of `u` in the sense of Stacks 00WU is `[u.IsContinuous J K]` together with the
> commutation with fibre products, `[HasPullbacks 𝒞]` and `[PreservesLimitsOfShape WalkingCospan u]`;
> see the implementation notes.

```lean
theorem isStack_structureFunctor (J : GrothendieckTopology 𝒞) (K : GrothendieckTopology 𝒟)
    (u : 𝒞 ⥤ 𝒟) [u.IsContinuous J K] [HasPullbacks 𝒞] [PreservesLimitsOfShape WalkingCospan u]
    (p : 𝒮 ⥤ 𝒟) (hp : Functor.IsStack p K) :
    Functor.IsStack (structureFunctor u p) J
```

## Tag 04WD, a lemma

[Tag 04WD](https://stacks.math.columbia.edu/tag/04WD) in the Stacks Project.

**`CategoryTheory.StrictPullback.isStack_isFiberedInGroupoids_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PushforwardStack.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PushforwardStack.lean#L106).

> **Stacks 04WD**.
> If `p : 𝒮 ⥤ 𝒟` is a stack in groupoids over the site `(𝒟, K)`, then the pushforward `u^p𝒮 ⥤ 𝒞`
> along a continuous functor of sites `u : 𝒞 ⥤ 𝒟` is a stack in groupoids over `(𝒞, J)`.

```lean
theorem isStack_isFiberedInGroupoids_structureFunctor (J : GrothendieckTopology 𝒞)
    (K : GrothendieckTopology 𝒟) (u : 𝒞 ⥤ 𝒟) [u.IsContinuous J K] [HasPullbacks 𝒞]
    [PreservesLimitsOfShape WalkingCospan u] (p : 𝒮 ⥤ 𝒟) (hp : Functor.IsStack p K)
    (hp' : p.IsFiberedInGroupoids) :
    Functor.IsStack (structureFunctor u p) J ∧
      (structureFunctor u p).IsFiberedInGroupoids
```

## Tag 04WE, a definition

[Tag 04WE](https://stacks.math.columbia.edu/tag/04WE) in the Stacks Project.

**`CategoryTheory.pushforwardFibredCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/Pushforward.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/Pushforward.lean#L188).

> **Stacks 04WE**.
> Notation: for a morphism of sites `f : 𝒟 → 𝒞` given by a continuous functor
> `u : 𝒞 ⥤ 𝒟` and a fibred category `p : 𝒮 ⥤ 𝒟`, one writes `f_*𝒮` for the fibred category
> `u^p𝒮` over `𝒞` and calls it the *pushforward of `𝒮` along `f`*. The topologies `J` and `K`
> and the continuity of `u` play no role in the construction; they are the data of `f`, which
> is what this notation names.

```lean
def pushforwardFibredCategory (J : GrothendieckTopology 𝒞) (K : GrothendieckTopology 𝒟)
    (u : 𝒞 ⥤ 𝒟) [u.IsContinuous J K] (p : 𝒮 ⥤ 𝒟) [p.IsFibered] :
    StrictPullback u p ⥤ 𝒞
```

## Tag 04WF, a lemma

[Tag 04WF](https://stacks.math.columbia.edu/tag/04WF) in the Stacks Project.

**`CategoryTheory.Comma.hasRightCalculusOfFractions_stronglyCartesianOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFractions.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFractions.lean#L273).

> **The morphisms with identity base component and strongly cartesian fibre component form a
> right multiplicative system.** Let `u : 𝒞 ⥤ 𝒟` be a functor, let `p : 𝒮 ⥤ 𝒞` be a fibred category,
> assume `𝒞` has nonempty finite limits and that `u` commutes with nonempty finite limits. In the
> category `u_pp 𝒮 = Comma (𝟭 𝒟) (p ⋙ u)`, whose objects are the triples
> `(U, φ : V ⟶ u(U), x ∈ 𝒮_U)`, consider the set `R` of morphisms
> `(a, id_V, α) : (U', φ' : V ⟶ u(U'), x') ⟶ (U, φ : V ⟶ u(U), x)` whose `𝒟`-component is an
> identity and whose `α` is strongly cartesian. Then `R` is a right multiplicative system: it
> contains the identities and is stable under composition (RMS1), every left fraction over `R` can
> be turned into a right fraction (RMS2), and two morphisms equalized by postcomposition with an
> element of `R` are equalized by precomposition with an element of `R` (RMS3).

```lean
public theorem Comma.hasRightCalculusOfFractions_stronglyCartesianOver
    (p : 𝒮 ⥤ 𝒞) (u : 𝒞 ⥤ 𝒟) [p.IsFibered] [HasNonemptyFiniteLimits 𝒞]
    (hu : ∀ (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J],
      Limits.PreservesLimitsOfShape J u) :
    MorphismProperty.HasRightCalculusOfFractions
      (fun (X Y : Comma (𝟭 𝒟) (p ⋙ u)) (f : X ⟶ Y) =>
        (∃ h : X.left = Y.left, f.left = eqToHom h) ∧ stronglyCartesianOver p f.right)
```

## Tag 04WG, a lemma

[Tag 04WG](https://stacks.math.columbia.edu/tag/04WG) in the Stacks Project.

**`CategoryTheory.Comma.pullbackLocalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFibred.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFibred.lean#L125).

> **`u_p 𝒮 = R⁻¹ u_pp 𝒮`**, the localization of `u_pp 𝒮 = Comma (𝟭 𝒟) (p ⋙ u)` at the set `R`
> of Stacks 04WF.

```lean
abbrev pullbackLocalization
```

**`CategoryTheory.Comma.pullbackProj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFibred.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFibred.lean#L140).

> **The structure functor `p_p : u_p 𝒮 ⥤ 𝒟`**, the extension of `p_pp` to the localization
> `u_p 𝒮` obtained from the universal property because `p_pp` inverts `R`. This is how `u_p 𝒮` is
> regarded as a category over `𝒟`.

```lean
noncomputable def pullbackProj : pullbackLocalization p u ⥤ 𝒟
```

**`CategoryTheory.Comma.isFibered_pullbackProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFibred.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackFibred.lean#L328).

> **`u_p 𝒮` is a fibred category over `𝒟`** (Stacks 04WG). Let `u : 𝒞 ⥤ 𝒟` be a functor, let
> `p : 𝒮 ⥤ 𝒞` be a fibred category, assume `𝒞` has nonempty finite limits and that `u` commutes
> with nonempty finite limits, so that the set `R` of Stacks 04WF is a right multiplicative system.
> Then the structure functor `p_p : u_p 𝒮 ⥤ 𝒟` of the localization `u_p 𝒮 = R⁻¹ u_pp 𝒮` is a fibred
> category: every morphism `β : V' ⟶ V` of `𝒟` and every object of `u_p 𝒮` over `V` admit a
> strongly cartesian lift, namely the image of the reindexing morphism `(id_U, β, id_x)`.

```lean
theorem isFibered_pullbackProj
    (hu : ∀ (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J],
      Limits.PreservesLimitsOfShape J u) :
    (pullbackProj p u).IsFibered
```

## Tag 04WH, a lemma

[Tag 04WH](https://stacks.math.columbia.edu/tag/04WH) in the Stacks Project.

**`CategoryTheory.Comma.isFiberedInGroupoids_pullbackProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackGroupoid.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackGroupoid.lean#L186).

> **`u_p 𝒮` is fibred in groupoids over `𝒟`** (Stacks 04WH). With notation and assumptions as in
> Stacks 04WG — `u : 𝒞 ⥤ 𝒟` a functor commuting with nonempty finite limits, `𝒞` with nonempty finite
> limits, and `u_p 𝒮 = R⁻¹ u_pp 𝒮` the localization of `u_pp 𝒮 = Comma (𝟭 𝒟) (p ⋙ u)` at the set `R`
> of Stacks 04WF, regarded as a category over `𝒟` through `p_p = Comma.pullbackProj p u` — if
> `p : 𝒮 ⥤ 𝒞` is fibred in groupoids then so is `p_p`.
>
> By Stacks 04WG the functor `p_p` is fibred, and its fibres are groupoids
> (`Comma.isGroupoid_fiber_pullbackProj`), so this is Stacks 003V.

```lean
theorem isFiberedInGroupoids_pullbackProj (hp : p.IsFiberedInGroupoids)
    (hu : ∀ (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J],
      Limits.PreservesLimitsOfShape J u) :
    (pullbackProj p u).IsFiberedInGroupoids
```

## Tag 04WI, a lemma

[Tag 04WI](https://stacks.math.columbia.edu/tag/04WI) in the Stacks Project.

**`CategoryTheory.equivalenceIsFibredOneMorphismStrictPullbackPullbackLocalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackAdjunction.lean, line 1440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackAdjunction.lean#L1440).

> **The pullback of a fibred category along `u` is adjoint to the pushforward along `u`**
> (Stacks 04WI). Let `u : 𝒞 ⥤ 𝒟` be a functor, let `p : 𝒮 ⥤ 𝒞` and `q : 𝒯 ⥤ 𝒟` be fibred
> categories, assume `𝒞` has nonempty finite limits and that `u` commutes with nonempty finite
> limits. Then the morphism category `Mor_{Fib/𝒞}(𝒮, u^p 𝒯)` of 1-morphisms `𝒮 ⟶ u^p 𝒯` of fibred
> categories over `𝒞` is canonically equivalent to the morphism category `Mor_{Fib/𝒟}(u_p 𝒮, 𝒯)` of
> 1-morphisms `u_p 𝒮 ⟶ 𝒯` of fibred categories over `𝒟`, where `u^p 𝒯` is the pushforward of `𝒯`
> along `u` (Stacks 04WB) and `u_p 𝒮` is the pullback of `𝒮` along `u` (Stacks 04WG). Each morphism
> category is realized as the full subcategory of the category of based functors on those which
> preserve strongly cartesian morphisms, its morphisms being the morphisms of functors whose
> components lie over identities of the base.

```lean
noncomputable def equivalenceIsFibredOneMorphismStrictPullbackPullbackLocalization {𝒞 : Type u₁}
    [Category.{v₁} 𝒞] {𝒟 : Type u₂} [Category.{v₂} 𝒟] {𝒮 : Type u₃} [Category.{v₃} 𝒮] {𝒯 : Type u₄}
    [Category.{v₄} 𝒯] (u : 𝒞 ⥤ 𝒟) (p : 𝒮 ⥤ 𝒞) (q : 𝒯 ⥤ 𝒟) [p.IsFibered] [q.IsFibered]
    [HasNonemptyFiniteLimits 𝒞]
    (hu :
      ∀ (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J],
        Limits.PreservesLimitsOfShape J u) :
    ObjectProperty.FullSubcategory
        (fun G :
            BasedCategory.ofFunctor p ⥤ᵇ
              BasedCategory.ofFunctor (StrictPullback.structureFunctor u q) =>
          Functor.IsFibredOneMorphism p (StrictPullback.structureFunctor u q) G.toFunctor) ≌
      ObjectProperty.FullSubcategory
        (fun G : BasedCategory.ofFunctor (Comma.pullbackProj p u) ⥤ᵇ BasedCategory.ofFunctor q =>
          Functor.IsFibredOneMorphism (Comma.pullbackProj p u) q G.toFunctor)
```

## Tag 04WJ, a definition

[Tag 04WJ](https://stacks.math.columbia.edu/tag/04WJ) in the Stacks Project.

**`CategoryTheory.Comma.pullbackStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStack.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStack.lean#L115).

> **The pullback `f⁻¹𝒮` of the stack `𝒮` along the morphism of sites `f`** (Stacks 04WJ), given
> as its structure functor over `𝒟`.
>
> `f : 𝒟 ⟶ 𝒞` is the morphism of sites attached to the continuous functor `u : 𝒞 ⥤ 𝒟` by
> Sites 00X6, `𝒮` is a stack over `(𝒞, J)`, and `f⁻¹𝒮` is the stackification over `(𝒟, K)` of the
> fibred category `u_p 𝒮 = Comma.pullbackLocalization p u` of Stacks 04WG. The stackification is
> supplied: `q : 𝒳 ⥤ 𝒟` is a stack over `(𝒟, K)` and `G : u_p 𝒮 ⥤ 𝒳` is a 1-morphism of fibred
> categories over `𝒟` satisfying the two clauses of Stacks 02ZN — local bijectivity of the induced
> maps of morphism presheaves, and local essential surjectivity on fibres. Relative to that data,
> `f⁻¹𝒮` is `q`.

```lean
def pullbackStack (p : 𝒮 ⥤ 𝒞) (u : 𝒞 ⥤ 𝒟) [p.IsFibered] [HasFiniteLimits 𝒞]
    [PreservesFiniteLimits u] [u.IsContinuous J K] {𝒳 : Type u₄} [Category.{max u₂ u₃ vb v} 𝒳]
    {q : 𝒳 ⥤ 𝒟} [q.IsFibered] {G : pullbackLocalization p u ⥤ 𝒳}
    (_hs : p.IsStack J) (_hq : q.IsStack K)
    (hG : (pullbackProj p u).IsFibredOneMorphism q G)
    (_hmor : ∀ (V : 𝒟) (x y : (pullbackProj p u).Fiber V),
      Presheaf.IsLocallyInjective (K.over V) (hG.morPresheafMap x y) ∧
        Presheaf.IsLocallySurjective (K.over V) (hG.morPresheafMap x y))
    (_hobj : ∀ (V : 𝒟) (x' : q.Fiber V), ∃ R ∈ K V, ∀ ⦃W : 𝒟⦄ ⦃g : W ⟶ V⦄, R.arrows g →
      (Functor.fiberFunctorOfCompEq hG.comp_eq W).essImage (Functor.pullbackFiber q x' g)) :
    𝒳 ⥤ 𝒟
```

**`CategoryTheory.Comma.pullbackStackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStack.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStack.lean#L131).

> **The canonical 1-morphism `u_p 𝒮 ⥤ f⁻¹𝒮`** (Stacks 04WJ), exhibiting the pullback of `𝒮`
> along `f` as the stackification of `u_p 𝒮`.

```lean
def pullbackStackMap (p : 𝒮 ⥤ 𝒞) (u : 𝒞 ⥤ 𝒟) [p.IsFibered] [HasFiniteLimits 𝒞]
    [PreservesFiniteLimits u] [u.IsContinuous J K] {𝒳 : Type u₄} [Category.{max u₂ u₃ vb v} 𝒳]
    {q : 𝒳 ⥤ 𝒟} [q.IsFibered] {G : pullbackLocalization p u ⥤ 𝒳}
    (_hs : p.IsStack J) (_hq : q.IsStack K)
    (hG : (pullbackProj p u).IsFibredOneMorphism q G)
    (_hmor : ∀ (V : 𝒟) (x y : (pullbackProj p u).Fiber V),
      Presheaf.IsLocallyInjective (K.over V) (hG.morPresheafMap x y) ∧
        Presheaf.IsLocallySurjective (K.over V) (hG.morPresheafMap x y))
    (_hobj : ∀ (V : 𝒟) (x' : q.Fiber V), ∃ R ∈ K V, ∀ ⦃W : 𝒟⦄ ⦃g : W ⟶ V⦄, R.arrows g →
      (Functor.fiberFunctorOfCompEq hG.comp_eq W).essImage (Functor.pullbackFiber q x' g)) :
    pullbackLocalization p u ⥤ 𝒳
```

## Tag 04WK, a lemma

[Tag 04WK](https://stacks.math.columbia.edu/tag/04WK) in the Stacks Project.

**`CategoryTheory.Functor.equivalenceFibredMorStrictPullbackStackification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackAdjunction.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackAdjunction.lean#L194).

> **The pullback of a stack along `f` is adjoint to the pushforward along `f`** (Stacks 04WK).
> Let `f : 𝒟 ⟶ 𝒞` be the morphism of sites given by a functor `u : 𝒞 ⥤ 𝒟` as in Sites 00X6, let
> `p : 𝒮 ⥤ 𝒞` be a fibred category and let `q : 𝒯 ⥤ 𝒟` be a stack. Let `G : u_p 𝒮 ⥤ 𝒮'` exhibit
> `𝒮'` as the stackification of the pullback `u_p 𝒮` of Stacks 04WG, in the sense of Stacks 02ZN, so
> that `𝒮' = f⁻¹𝒮` is the pullback of Stacks 04WJ. Then the morphism category
> `Mor_{Stacks/𝒞}(𝒮, f_*𝒯)` of 1-morphisms `𝒮 ⟶ f_*𝒯` over `𝒞` and their 2-morphisms is
> canonically equivalent to the morphism category `Mor_{Stacks/𝒟}(f⁻¹𝒮, 𝒯)`, where `f_*𝒯 = u^p 𝒯`
> is the pushforward of Stacks 04WB. The equivalence is the composite of Stacks 04WI, the same
> adjunction at the level of fibred categories, with Stacks 04W9, restriction along the
> stackification `G`.
>
> This statement is *conditional on being given a stackification* `G`: its hypotheses are the
> unfolded clauses of Stacks 02ZN, which that construction supplies once it is assembled.

```lean
noncomputable def equivalenceFibredMorStrictPullbackStackification
    (hu : ∀ (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J],
      Limits.PreservesLimitsOfShape J u)
    (hG : (Comma.pullbackProj p u).IsFibredOneMorphism p' G)
    (hmor : ∀ (V : 𝒟) (x y : (Comma.pullbackProj p u).Fiber V),
      Presheaf.IsLocallyInjective (K.over V) (hG.morPresheafMap x y) ∧
        Presheaf.IsLocallySurjective (K.over V) (hG.morPresheafMap x y))
    (hqmor : ∀ (V : 𝒟) (x y : q.Fiber V), IsMorSheaf q K V x y)
    (hobj : ∀ (V : 𝒟) (x' : p'.Fiber V), ∃ R ∈ K V, ∀ ⦃W : 𝒟⦄ ⦃f : W ⟶ V⦄, R.arrows f →
      (fiberFunctorOfCompEq hG.comp_eq W).essImage (pullbackFiber p' x' f))
    (hdesc : HasEffectiveDescent q K) :
    FibredMor p (StrictPullback.structureFunctor u q) ≌ FibredMor p' q
```

**`CategoryTheory.Functor.equivalenceFibredMorPushforwardPullbackStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackAdjunction.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackAdjunction.lean#L240).

> **Stacks 04WK**, written with the pushforward `f_*𝒯` of Stacks 04WE and the pullback `f⁻¹𝒮`
> of Stacks 04WJ. Let `f : 𝒟 ⟶ 𝒞` be the morphism of sites attached by Sites 00X6 to a continuous
> functor `u : 𝒞 ⥤ 𝒟` between a finitely complete `(𝒞, J)` and `(𝒟, K)` which is left exact, let
> `𝒮` be a stack over `(𝒞, J)` and let `𝒯` be a stack over `(𝒟, K)`. Then
>
> `Mor_{Stacks/𝒞}(𝒮, f_*𝒯) ≃ Mor_{Stacks/𝒟}(f⁻¹𝒮, 𝒯)`.
>
> The pullback `f⁻¹𝒮` is represented by the supplied stackification of `u_p 𝒮`: the stack
> `q : 𝒳 ⥤ 𝒟` and the 1-morphism `G : u_p 𝒮 ⥤ 𝒳` satisfying the clauses `hG`,
> `hmor`, `hobj` of Stacks 02ZN. So this statement too is conditional on being given a
> stackification, which Stacks 02ZN supplies once assembled.
>
> The instance `[t.IsFibered]` is implied by `ht` and is taken separately only because the notation
> `f_*𝒯` of Stacks 04WE needs it to elaborate.

```lean
noncomputable def equivalenceFibredMorPushforwardPullbackStack
    (hs : p.IsStack J) (hq : q.IsStack K)
    (hG : (Comma.pullbackProj p u).IsFibredOneMorphism q G)
    (hmor : ∀ (V : 𝒟) (x y : (Comma.pullbackProj p u).Fiber V),
      Presheaf.IsLocallyInjective (K.over V) (hG.morPresheafMap x y) ∧
        Presheaf.IsLocallySurjective (K.over V) (hG.morPresheafMap x y))
    (hobj : ∀ (V : 𝒟) (x' : q.Fiber V), ∃ R ∈ K V, ∀ ⦃W : 𝒟⦄ ⦃g : W ⟶ V⦄, R.arrows g →
      (fiberFunctorOfCompEq hG.comp_eq W).essImage (pullbackFiber q x' g))
    (ht : t.IsStack K) :
    FibredMor p (pushforwardFibredCategory J K u t) ≌ FibredMor q t
```

## Tag 04WR, a lemma

[Tag 04WR](https://stacks.math.columbia.edu/tag/04WR) in the Stacks Project.

**`CategoryTheory.pullback_stackification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackification/LocalEssSurj.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackification/LocalEssSurj.lean#L259).

> Let `f : 𝒟 ⟶ 𝒞` be the morphism of sites given by a continuous
> `u : 𝒞 ⥤ 𝒟` satisfying the hypotheses of Sites 00X6, let `p : 𝒮 ⥤ 𝒞` be a fibred category and let
> `G : 𝒮 ⥤ 𝒮'` be its stackification (clauses (1) and (2) of Stacks 02ZN, spelled out as `hmor` and
> `hobj`). Let `G' : u_p 𝒮' ⥤ 𝒯` exhibit the stack `q : 𝒯 ⥤ 𝒟` as the stackification of `u_p 𝒮'` —
> that is, let `𝒯` be `f⁻¹𝒮'` in the sense of Stacks 04WJ — and let `H : u_p 𝒮 ⥤ 𝒯` be the canonical
> functor, pinned down by its restriction `Q ⋙ H = Φ ⋙ Q' ⋙ G'` along the localization functor.
> Then `H` exhibits `𝒯` as the stackification of `u_p 𝒮`: `f⁻¹𝒮'` is the stackification of
> `u_p 𝒮`.

```lean
theorem pullback_stackification
    [p.IsFibered] [p'.IsFibered] [HasNonemptyFiniteLimits 𝒞]
    (J : GrothendieckTopology 𝒞) (K : GrothendieckTopology 𝒟) [u.IsContinuous J K]
    (hu : ∀ (J' : Type) [SmallCategory J'] [FinCategory J'] [Nonempty J'],
      Limits.PreservesLimitsOfShape J' u)
    (hGG : p.IsFibredOneMorphism p' G)
    (hmor : ∀ (U : 𝒞) (x y : p.Fiber U),
      Presheaf.IsLocallyInjective (J.over U) (hGG.morPresheafMap x y) ∧
        Presheaf.IsLocallySurjective (J.over U) (hGG.morPresheafMap x y))
    (hobj : ∀ (U : 𝒞) (x' : p'.Fiber U), ∃ R ∈ J U, ∀ ⦃U₁ : 𝒞⦄ ⦃d : U₁ ⟶ U⦄, R.arrows d →
      (Functor.fiberFunctorOfCompEq hGG.comp_eq U₁).essImage (Functor.pullbackFiber p' x' d))
    {q : 𝒯 ⥤ 𝒟} (hq : q.IsStack K)
    {G' : Comma.pullbackLocalization p' u ⥤ 𝒯}
    (hG' : haveI : (Comma.pullbackProj p' u).IsFibered := Comma.isFibered_pullbackProj p' u hu
      (Comma.pullbackProj p' u).IsFibredOneMorphism q G')
    (hmor' : haveI : (Comma.pullbackProj p' u).IsFibered := Comma.isFibered_pullbackProj p' u hu
      haveI : q.IsFibered := hq.isFibered
      ∀ (V : 𝒟) (x y : (Comma.pullbackProj p' u).Fiber V),
        Presheaf.IsLocallyInjective (K.over V) (hG'.morPresheafMap x y) ∧
          Presheaf.IsLocallySurjective (K.over V) (hG'.morPresheafMap x y))
    (hobj' : haveI : q.IsFibered := hq.isFibered
      ∀ (V : 𝒟) (z : q.Fiber V), ∃ T ∈ K V, ∀ ⦃V₁ : 𝒟⦄ ⦃β : V₁ ⟶ V⦄, T.arrows β →
        (Functor.fiberFunctorOfCompEq hG'.comp_eq V₁).essImage (Functor.pullbackFiber q z β))
    (H : Comma.pullbackLocalization p u ⥤ 𝒯)
    (hH : (Comma.idBaseStronglyCartesian p u).Q ⋙ H =
      commaMapOver u hGG.comp_eq ⋙ (Comma.idBaseStronglyCartesian p' u).Q ⋙ G') :
    haveI : (Comma.pullbackProj p u).IsFibered := Comma.isFibered_pullbackProj p u hu
    haveI : q.IsFibered := hq.isFibered
    ∃ hH' : (Comma.pullbackProj p u).IsFibredOneMorphism q H,
      (∀ (V : 𝒟) (x y : (Comma.pullbackProj p u).Fiber V),
          Presheaf.IsLocallyInjective (K.over V) (hH'.morPresheafMap x y) ∧
            Presheaf.IsLocallySurjective (K.over V) (hH'.morPresheafMap x y)) ∧
        ∀ (V : 𝒟) (z : q.Fiber V), ∃ T ∈ K V, ∀ ⦃V₁ : 𝒟⦄ ⦃β : V₁ ⟶ V⦄, T.arrows β →
          (Functor.fiberFunctorOfCompEq hH'.comp_eq V₁).essImage
            (Functor.pullbackFiber q z β)
```

## Tag 04WS, a lemma

[Tag 04WS](https://stacks.math.columbia.edu/tag/04WS) in the Stacks Project.

**`CategoryTheory.Comma.equivalenceOverPullbackStackCan`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackEquivalence.lean, line 1092](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackEquivalence.lean#L1092). The attribute's comment: “(1)”.

> **Stacks 04WS (1), as data.** Let `u : 𝒞 ⥤ 𝒟` satisfy the assumptions of Sites 00XU —
> continuous, cocontinuous, fully faithful, `𝒞` finitely complete and `u` left exact — and let
> `f : 𝒟 ⟶ 𝒞` be the associated morphism of sites. Let `𝒮` be a stack over `(𝒞, J)` and let
> `G : u_p 𝒮 ⥤ f⁻¹𝒮` exhibit `f⁻¹𝒮` as the stackification of `u_p 𝒮` over `(𝒟, K)` in the sense of
> Stacks 02ZN. Then the canonical functor `𝒮 ⟶ f_*f⁻¹𝒮` is an **equivalence of stacks over `𝒞`**:
> a quasi-inverse strictly over `𝒞`, together with vertical unit and counit isomorphisms.
>
> By Stacks 046N it suffices that the canonical functor be fully faithful and that every object of a
> fibre of `f_*f⁻¹𝒮` be locally in its essential image on fibres, which are
> `CategoryTheory.Comma.fullyFaithful_pullbackStackCan` and
> `CategoryTheory.Comma.locallyEssSurjOnFibers_pullbackStackCan`.
>
> The statement is *conditional on being given a stackification*, which Stacks 02ZN supplies once
> assembled.

```lean
noncomputable def equivalenceOverPullbackStackCan
    (hobj : ∀ (V : 𝒟) (x' : q.Fiber V), ∃ R ∈ K V, ∀ ⦃W : 𝒟⦄ ⦃g : W ⟶ V⦄, R.arrows g →
      (Functor.fiberFunctorOfCompEq hG.comp_eq W).essImage (Functor.pullbackFiber q x' g)) :
    Functor.IsEquivalenceOver p (StrictPullback.structureFunctor u q)
      (pullbackStackCan p u hG)
```

**`CategoryTheory.Comma.equivalenceFibredMorPullbackStack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackEquivalence.lean, line 1172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Functoriality/PullbackStackEquivalence.lean#L1172). The attribute's comment: “(2)”.

> **Stacks 04WS (2), for the pullbacks given by supplied stackifications.** Let `u : 𝒞 ⥤ 𝒟`
> satisfy the assumptions of Sites 00XU and let `f : 𝒟 ⟶ 𝒞` be the associated morphism of sites.
> For stacks `𝒮` and `𝒮₂` over `(𝒞, J)` with pullbacks `f⁻¹𝒮` and `f⁻¹𝒮₂` given by supplied
> stackifications of `u_p 𝒮` and `u_p 𝒮₂` (Stacks 04WJ), the morphism categories
>
> `Mor_{Stacks/𝒞}(𝒮, 𝒮₂)`  and  `Mor_{Stacks/𝒟}(f⁻¹𝒮, f⁻¹𝒮₂)`
>
> are canonically equivalent. The equivalence is the composite of post-composition with the
> canonical equivalence `𝒮₂ ⟶ f_*f⁻¹𝒮₂` of clause (1) with the adjunction of Stacks 04WK at
> `𝒯 = f⁻¹𝒮₂`; the direction `f⁻¹` is its quasi-inverse.
>
> Both clauses are conditional on being given stackifications, which Stacks 02ZN supplies once
> assembled.

```lean
noncomputable def equivalenceFibredMorPullbackStack :
    Functor.FibredMor p p₂ ≌
      Functor.FibredMor q q₂
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.12, Tag 04WA](https://stacks.math.columbia.edu/tag/04WA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
