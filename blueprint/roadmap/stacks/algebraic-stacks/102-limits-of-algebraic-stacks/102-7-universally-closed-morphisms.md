---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_affine_locallyFinitePresentation_separation_isClosed, AlgebraicGeometry.Stack.exists_affine_finitePresentation_separation, AlgebraicGeometry.Stack.AlgebraicStacks.image_preimage_eq_preimage_image_of_isTwoFibreProduct, AlgebraicGeometry.Stack.AlgebraicStacks.image_closure_image_subset_of_isTwoFibreProduct, IsOpenMap.image_closure_subset_image_of_preimage_subset, AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_of_isImmersion, AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_universallyClosed, AlgebraicGeometry.Stack.AlgebraicStacks.exists_chart_forall_isClosed_baseChange_affineSpaceChart_of_universallyClosed
statement: formalized
proof: formalized
---

# 102.7 Universally closed morphisms

Section 102.7 of the Stacks Project, [Tag 0H28](https://stacks.math.columbia.edu/tag/0H28). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H29, a lemma

[Tag 0H29](https://stacks.math.columbia.edu/tag/0H29) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_locallyFinitePresentation_separation_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/ClosedSubsetFibreSeparation.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/ClosedSubsetFibreSeparation.lean#L49). The attribute's comment: “the case of schemes, for closed subsets”.

> Let `f : X ⟶ S` be a quasi-compact morphism of schemes, `g : T ⟶ S` a morphism, `t ∈ T` a
> point and `E ⊆ X ×_S T` a closed subset whose image in `T` misses `t`. Then there are an affine
> open neighbourhood `V` of `t`, a commutative square `V ⟶ T' ⟶ S`, `V ⟶ T ⟶ S` with `T'` affine and
> `T' ⟶ S` locally of finite presentation, and a closed subset `E' ⊆ X ×_S T'` whose image in `T'`
> misses the image of `t`, such that the preimage of `E` in `X ×_S V` lies in the preimage of `E'`.
>
> This is the case of schemes, for closed subsets, of the separation lemma for algebraic stacks.

```lean
theorem exists_affine_locallyFinitePresentation_separation_isClosed
    {X S T : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f] (g : T ⟶ S)
    (t : T) (E : Set ↥(pullback f g)) (hE : IsClosed E)
    (ht : t ∉ Set.image (pullback.snd f g) E) :
    ∃ (V : T.affineOpens) (htV : t ∈ V.1)
      (T' : Scheme.{u}) (_ : IsAffine T') (b : T' ⟶ S)
      (_ : LocallyOfFinitePresentation b) (a : V.1.toScheme ⟶ T')
      (_ : V.1.ι ≫ g = a ≫ b)
      (E' : Set ↥(pullback f b)) (_ : IsClosed E')
      (p : pullback f (V.1.ι ≫ g) ⟶ pullback f g)
      (q : pullback f (V.1.ι ≫ g) ⟶ pullback f b),
      (p ≫ pullback.fst f g = pullback.fst f (V.1.ι ≫ g)) ∧
      (p ≫ pullback.snd f g = pullback.snd f (V.1.ι ≫ g) ≫ V.1.ι) ∧
      (q ≫ pullback.fst f b = pullback.fst f (V.1.ι ≫ g)) ∧
      (q ≫ pullback.snd f b = pullback.snd f (V.1.ι ≫ g) ≫ a) ∧
      (a ⟨t, htV⟩ ∉ Set.image (pullback.snd f b) E') ∧
      (p ⁻¹' E ⊆ q ⁻¹' E')
```

**`AlgebraicGeometry.Stack.exists_affine_finitePresentation_separation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ClosedSubsetSeparationAlgebraicStack.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ClosedSubsetSeparationAlgebraicStack.lean#L438).

> **Stacks 0H29.** Let `g : Z ⟶ Y` be a morphism of the big fppf category of `S` between
> objects with affine underlying schemes, let `f : 𝒳 ⟶ Y` be a quasi-compact 1-morphism of
> algebraic stacks over `S` with `𝒳` quasi-compact, let `z` be a point of `Z` and let
> `T ⊆ |𝒳 ×_Y Z|` be a closed subset whose image in `|Z|` misses `z`. Then there are an open
> neighbourhood `V` of `z` in `Z`, a commutative square `V ⟶ Z' ⟶ Y`, `V ⟶ Z ⟶ Y`, and a closed
> subset `T' ⊆ |𝒳 ×_Y Z'|` such that
>
> 1. `Z'` is affine and of finite presentation over `Y`,
> 2. the image of `z` in `|Z'|` misses the image of `T'` in `|Z'|`, and
> 3. the inverse image of `T` in `|𝒳 ×_Y V|` maps into `T'`.
>
> The two comparison 1-morphisms of the last two clauses are the canonical ones
> `AlgebraicGeometry.Stack.factorMap`; their compatibilities with the projections of the three base
> changes are `AlgebraicGeometry.Stack.factorIsoFst` and `AlgebraicGeometry.Stack.factorIsoSnd`.

```lean
theorem exists_affine_finitePresentation_separation {Y Z : BigFppfOver B S hS}
    (hY : IsAffine ((BigFppfOver.toScheme B S hS).obj Y))
    (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z)) (g : Z ⟶ Y)
    {𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ schemeStack.{u, w} B S hS Y)
    (_hf : IsQuasiCompactMorphism.{u, w} B S hS f)
    (h𝒳 : IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property)
    (z : AlgebraicStacks.points B S hS (schemeStack.{u, w} B S hS Z))
    (T : Set (AlgebraicStacks.points B S hS (baseChangeSquare B S hS f g).pt))
    (hT : @IsClosed _ (pointTopology B S hS (baseChangeSquare B S hS f g).pt.val) T)
    (hz : z ∉ AlgebraicStacks.pointsMap B S hS (baseChangeSquare B S hS f g).fst '' T) :
    ∃ (V : BigFppfOver B S hS) (j : V ⟶ Z),
      AlgebraicGeometry.IsOpenImmersion ((BigFppfOver.toScheme B S hS).map j) ∧
      ∃ v : AlgebraicStacks.points B S hS (schemeStack.{u, w} B S hS V),
        AlgebraicStacks.pointsMap B S hS (schemeStackMap.{u, w} B S hS j) v = z ∧
        ∃ (Z' : BigFppfOver B S hS) (b : Z' ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj Z') ∧
          FinitePresentation ((BigFppfOver.toScheme B S hS).map b) ∧
          ∃ (a : V ⟶ Z') (hab : j ≫ g = a ≫ b)
            (T' : Set (AlgebraicStacks.points B S hS (baseChangeSquare B S hS f b).pt)),
            @IsClosed _ (pointTopology B S hS (baseChangeSquare B S hS f b).pt.val) T' ∧
            AlgebraicStacks.pointsMap B S hS (schemeStackMap.{u, w} B S hS a) v ∉
              AlgebraicStacks.pointsMap B S hS (baseChangeSquare B S hS f b).fst '' T' ∧
            AlgebraicStacks.pointsMap B S hS (factorMap B S hS f (j ≫ g) a b hab) ''
                (AlgebraicStacks.pointsMap B S hS
                  (factorMap B S hS f (j ≫ g) j g rfl) ⁻¹' T) ⊆ T'
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.image_preimage_eq_preimage_image_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsCartesianSquare.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsCartesianSquare.lean#L56). The attribute's comment: “the cartesian-square step of the proof, on points”.

> For a 2-fibre product square of algebraic stacks over `S` with legs `fst : 𝒫 ⟶ 𝒳` and
> `snd : 𝒫 ⟶ 𝒬` over a cospan `g : 𝒳 ⟶ 𝒴`, `f : 𝒬 ⟶ 𝒴`, and for any subset `T` of `|𝒳|`, the
> image in `|𝒬|` of the preimage of `T` in `|𝒫|` is the preimage in `|𝒬|` of the image of `T`
> in `|𝒴|`.

```lean
theorem image_preimage_eq_preimage_image_of_isTwoFibreProduct
    {𝒳 𝒬 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} {g : 𝒳 ⟶ 𝒴} {f : 𝒬 ⟶ 𝒴}
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (T : Set (points B S hS 𝒳)) :
    pointsMap B S hS P.snd '' (pointsMap B S hS P.fst ⁻¹' T) =
      pointsMap B S hS f ⁻¹' (pointsMap B S hS g '' T)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.image_closure_image_subset_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PointsCartesianSquare.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PointsCartesianSquare.lean#L80). The attribute's comment: “the descent step of the proof, along a cartesian square with surjective open legs”.

> Let `P` be a 2-fibre product square of algebraic stacks over `S` with legs `fst : 𝒫 ⟶ 𝒳` and
> `snd : 𝒫 ⟶ 𝒬` over a cospan `g : 𝒳 ⟶ 𝒴`, `f : 𝒬 ⟶ 𝒴`, with `f` surjective and open on points,
> and let `π : 𝒴 ⟶ 𝒵` be a 1-morphism. If a closed subset `T' ⊆ |𝒬|` contains the image of the
> preimage of `T ⊆ |𝒳|`, then the image in `|𝒵|` of the closure of the image of `T` in `|𝒴|` is
> contained in the image of `T'` in `|𝒵|`.

```lean
theorem image_closure_image_subset_of_isTwoFibreProduct
    {𝒳 𝒬 𝒴 𝒵 : Stack.AlgebraicStacks.{u, w} B S hS} {g : 𝒳 ⟶ 𝒴} {f : 𝒬 ⟶ 𝒴} (π : 𝒴 ⟶ 𝒵)
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hsurj : Function.Surjective (pointsMap B S hS f))
    (hopen : letI := Stack.pointTopology B S hS 𝒬.val
      letI := Stack.pointTopology B S hS 𝒴.val
      IsOpenMap (pointsMap B S hS f))
    (T : Set (points B S hS 𝒳)) (T' : Set (points B S hS 𝒬))
    (hT' : letI := Stack.pointTopology B S hS 𝒬.val
      IsClosed T')
    (hsub : pointsMap B S hS P.snd '' (pointsMap B S hS P.fst ⁻¹' T) ⊆ T') :
    letI := Stack.pointTopology B S hS 𝒴.val
    pointsMap B S hS π '' closure (pointsMap B S hS g '' T) ⊆
      pointsMap B S hS (f ≫ π) '' T'
```

**`IsOpenMap.image_closure_subset_image_of_preimage_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Maps/ClosureImageSurjectiveOpen.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Maps/ClosureImageSurjectiveOpen.lean#L26). The attribute's comment: “the closure step of the proof, along a surjective open map”.

> For a surjective open continuous map `q : X → Y`, a closed subset `T ⊆ X` containing
> `q ⁻¹' A` also contains `q ⁻¹' closure A`; hence the image of `closure A` along any map
> `π : Y → Z` is contained in the image of `T` along `π ∘ q`.

```lean
theorem IsOpenMap.image_closure_subset_image_of_preimage_subset
    {X Y Z : Type*} [TopologicalSpace X] [TopologicalSpace Y] {q : X → Y}
    (hopen : IsOpenMap q) (hcont : Continuous q) (hsurj : Function.Surjective q) (π : Y → Z)
    {A : Set Y} {T : Set X} (hT : IsClosed T) (h : q ⁻¹' A ⊆ T) :
    π '' closure A ⊆ (π ∘ q) '' T
```

## Tag 0H2A, a lemma

[Tag 0H2A](https://stacks.math.columbia.edu/tag/0H2A) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L533). The attribute's comment: “closedness of a base change descends along an immersion of the base”.

> **Stacks 0H2A: closedness of a base change descends along an immersion of the base.** Let
> `F : 𝒬 ⟶ ℬ` be closed on points and let `ι : 𝒞 ⟶ ℬ` be an immersion of algebraic stacks over `S`.
> Then the base change of `F` along `ι` — the map `|𝒬 ×_ℬ 𝒞| → |𝒞|` — is closed on points.
>
> This is the step of the proof of Stacks 0H2A which writes a closed subset of `|𝒳 ×_𝒴 Z|` as the
> pullback of a closed subset of `|𝐀ⁿ × 𝒳|` along the immersion `Z ⟶ 𝐀ⁿ_V` of Stacks 04II. The base
> change of `ι` is an immersion by Stacks 045C at the immersion property, hence a topological
> embedding on points by **Stacks 0H20**; the square is cartesian on points by **Stacks 04XH**; and
> `isClosedMap_of_isEmbedding_of_cartesian` concludes. Only the embedding property of Stacks 0H20
> is used, not the local closedness of the range.

```lean
theorem isClosed_baseChange_of_isImmersion
    {𝒬 𝒞 ℬ : Stack.AlgebraicStacks.{u, w} B S hS} (F : 𝒬 ⟶ ℬ) (ι : 𝒞 ⟶ ℬ)
    (hι : IsImmersion B S hS ι) (hF : IsClosed B S hS F) :
    IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS ι F).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L620). The attribute's comment: “(1) implies (2)”.

> **Stacks 0H2A, (1) implies (2).** If `f` is universally closed then, for every object `Z` of
> the site whose scheme is *affine* and every 1-morphism `Stack.schemeStack Z ⟶ 𝒴` which is
> *locally of finite presentation*, the map `|𝒳 ×_𝒴 Z| → |Z|` is closed. Neither adjective is
> used: the clause is the restriction of universal closedness to those bases.

```lean
theorem isClosed_baseChange_affine_isLocallyOfFinitePresentation_of_universallyClosed
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : UniversallyClosed B S hS f) :
    ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
      ∀ (g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴),
        IsLocallyOfFinitePresentation B S hS g →
          IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_chart_forall_isClosed_baseChange_affineSpaceChart_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L637). The attribute's comment: “(1) implies (3)”.

> **Stacks 0H2A, (1) implies (3).** If `f` is universally closed then there are a scheme `V` of
> the site and a smooth surjective 1-morphism `Stack.schemeStack V ⟶ 𝒴` such that, for *every*
> `n ≥ 0`, the base change of `f` to affine `n`-space over `V` — the map
> `|𝐀^n × (𝒳 ×_𝒴 V)| → |𝐀^n × V|` — is closed.
>
> Any smooth surjective chart of `𝒴` by a scheme of the site serves, and every one of the base
> changes is closed because `f` is universally closed.

```lean
theorem exists_chart_forall_isClosed_baseChange_affineSpaceChart_of_universallyClosed
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : UniversallyClosed B S hS f) :
    ∃ (V : BigFppfOver B S hS) (a : Stack.schemeStack.{u, w} B S hS V ⟶ 𝒴),
      Stack.IsSurjective B S hS a ∧ IsSmooth B S hS a ∧
        ∀ n : ℕ, IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS
          (Stack.schemeStackMap.{u, w} B S hS (affineSpaceChartHom B S hS V n) ≫ a) f).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_chart_forall_isClosed_baseChange_affineSpaceChart_of_isClosed_affine_lfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L659). The attribute's comment: “(2) implies (3)”.

> **Stacks 0H2A, (2) implies (3).** Suppose every base change of `f` to an affine scheme of the
> site along a 1-morphism locally of finite presentation is closed. Then the conclusion of (3)
> holds for *any* smooth surjective chart `a : Stack.schemeStack V ⟶ 𝒴` of `𝒴` by a scheme of the
> site.
>
> Fix `n`. The target of the base change is the stack of affine `n`-space over `V`; its affine
> opens cover it and their inclusions are open immersions, hence smooth, so closedness can be read
> on that cover. Over one affine open `W` the base change of `f` is the base change along the
> composite `W ⟶ 𝐀^n_V ⟶ V ⟶ 𝒴`, whose scheme `W` is affine and which is locally of finite
> presentation — the inclusion of an open is, the projection of affine `n`-space is, and `a` is
> smooth hence locally of finite presentation by Stacks 0DNP. So (2) applies to it.

```lean
theorem exists_chart_forall_isClosed_baseChange_affineSpaceChart_of_isClosed_affine_lfp
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h : ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
      ∀ (g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴),
        IsLocallyOfFinitePresentation B S hS g →
          IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst) :
    ∃ (V : BigFppfOver B S hS) (a : Stack.schemeStack.{u, w} B S hS V ⟶ 𝒴),
      Stack.IsSurjective B S hS a ∧ IsSmooth B S hS a ∧
        ∀ n : ℕ, IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS
          (Stack.schemeStackMap.{u, w} B S hS (affineSpaceChartHom B S hS V n) ≫ a) f).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_schemeStackMap_of_forall_isClosed_baseChange_affineSpaceChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 759](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L759). The attribute's comment: “(3) implies (2), the step at a target represented by a scheme, stated at the hypotheses of Tag 04II: a quasi-affine source and a morphism locally of finite type”.

> **Stacks 0H2A, the step of (3) implies (2) at a target represented by a scheme.** Let
> `f : 𝒳 ⟶ Stack.schemeStack W` be a 1-morphism of algebraic stacks over `S` whose base change to
> affine `n`-space over `W` is closed on points for every `n ≥ 0`. Then for every morphism
> `p : Z ⟶ W` of the site whose source scheme is quasi-affine and which is locally of finite type,
> the base change of `f` along the 1-morphism that `p` induces is closed on points.
>
> By **Stacks 04II** such a `Z` immerses over `W` into affine `n`-space over `W` for some `n`. That
> immersion of schemes induces an immersion of the represented algebraic stacks, and closedness of
> a base change descends along an immersion of the base.

```lean
theorem isClosed_baseChange_schemeStackMap_of_forall_isClosed_baseChange_affineSpaceChart
    {𝒳 : Stack.AlgebraicStacks.{u, w} B S hS} {W : BigFppfOver B S hS}
    (f : 𝒳 ⟶ Stack.schemeStack.{u, w} B S hS W)
    (h : ∀ n : ℕ, IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS
      (Stack.schemeStackMap.{u, w} B S hS (affineSpaceChartHom B S hS W n)) f).fst)
    {Z : BigFppfOver B S hS} (p : Z ⟶ W)
    (hZ : ((BigFppfOver.toScheme B S hS).obj Z).IsQuasiAffine)
    (hp : LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map p)) :
    IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS
      (Stack.schemeStackMap.{u, w} B S hS p) f).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isClosed_baseChange_affine_isLocallyOfFinitePresentation_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 803](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L803). The attribute's comment: “clause (2) is inherited by a base change along a 1-morphism locally of finite presentation”.

> **Clause (2) of Stacks 0H2A is inherited by a base change along a 1-morphism locally of
> finite presentation.** Suppose every base change of `f : 𝒳 ⟶ 𝒴` to an affine scheme of the site
> along a 1-morphism locally of finite presentation is closed on points, and let `b : 𝒴' ⟶ 𝒴` be
> locally of finite presentation. Then the same holds for the base change of `f` along `b`: a
> 1-morphism `Stack.schemeStack Z ⟶ 𝒴'` locally of finite presentation composes with `b` to one
> locally of finite presentation, and base changing twice is base changing once.

```lean
theorem isClosed_baseChange_affine_isLocallyOfFinitePresentation_baseChange
    {𝒳 𝒴 𝒴' : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴) (b : 𝒴' ⟶ 𝒴)
    (hb : IsLocallyOfFinitePresentation B S hS b)
    (h : ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
      ∀ (g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴), IsLocallyOfFinitePresentation B S hS g →
        IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst)
    (Z : BigFppfOver B S hS) (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z))
    (g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴') (hg : IsLocallyOfFinitePresentation B S hS g) :
    IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g
      (Stack.twoFibreProductSquareAlgebraicStacks B S hS b f).fst).fst
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_forall_schemeStack_target_of_isClosed_affine_lfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean, line 825](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocal.lean#L825). The attribute's comment: “(2) implies (1), the reduction to a target represented by a scheme; the remaining input is Tag 0H29 for algebraic stacks, carried as `hred`”.

> **Stacks 0H2A, the reduction of (2) implies (1) to a target represented by a scheme.** If
> clause (2) implies universal closedness whenever the target is the algebraic stack of a scheme of
> the site, then it implies universal closedness for an arbitrary target.
>
> Every algebraic stack over `S` has a smooth surjective chart by a scheme of the site, universal
> closedness descends along it, and it is locally of finite presentation by Stacks 0DNP, so clause
> (2) for `f` gives clause (2) for the base change of `f` to that chart.

```lean
theorem universallyClosed_of_forall_schemeStack_target_of_isClosed_affine_lfp
    (hred : ∀ (V : BigFppfOver B S hS) (𝒲 : Stack.AlgebraicStacks.{u, w} B S hS)
      (f' : 𝒲 ⟶ Stack.schemeStack.{u, w} B S hS V),
        (∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ (g : Stack.schemeStack.{u, w} B S hS Z ⟶ Stack.schemeStack.{u, w} B S hS V),
            IsLocallyOfFinitePresentation B S hS g →
              IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f').fst) →
        UniversallyClosed B S hS f')
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (h : ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
      ∀ (g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴), IsLocallyOfFinitePresentation B S hS g →
        IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_isQuasiCompactMorphism_of_isClosed_affine_lfp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocalQuasiCompact.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocalQuasiCompact.lean#L389). The attribute's comment: “(2) implies (1), with the reduction to a target represented by a scheme”.

> **Stacks 0H2A, (2) implies (1), with the reduction to a target represented by a scheme.** Let
> `f : 𝒳 ⟶ 𝒴` be a quasi-compact 1-morphism of algebraic stacks over `S` such that the base change
> of `f` to every affine scheme of the site along a 1-morphism locally of finite presentation is
> closed on points. Then `f` is universally closed.
>
> Pick a smooth surjective chart `a : Stack.schemeStack V ⟶ 𝒴` of `𝒴` by a scheme of the site.
> Universal closedness descends along `a`, so it is enough to prove it for the base change of `f`
> along `a`, whose target is represented by a scheme of the site; that base change is quasi-compact
> by **Stacks 050V**, and it inherits the hypothesis because `a` is locally of finite presentation
> by Stacks 0DNP and clause (2) is inherited by a base change along a 1-morphism locally of finite
> presentation.

```lean
theorem universallyClosed_of_isQuasiCompactMorphism_of_isClosed_affine_lfp
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : Stack.IsQuasiCompactMorphism.{u, w} B S hS f)
    (h : ∀ Z : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
      ∀ g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴, IsLocallyOfFinitePresentation B S hS g →
        IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_of_exists_chart_forall_isClosed_baseChange_affineSpaceChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocalQuasiCompact.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocalQuasiCompact.lean#L419). The attribute's comment: “(3) implies (1)”.

> **Stacks 0H2A, (3) implies (1).** Suppose there are a scheme `V` of the site and a smooth
> surjective 1-morphism `a : Stack.schemeStack V ⟶ 𝒴` such that the base change of the quasi-compact
> `f` to affine `n`-space over `V` is closed on points for every `n ≥ 0`. Then `f` is universally
> closed.
>
> Universal closedness descends along `a`, so it is enough to prove it for the base change `f'` of
> `f` along `a`, whose target is represented by a scheme of the site. By (2) implies (1) at such a
> target it is enough to show that the base change of `f'` to every affine scheme of the site along
> a morphism of the site locally of finite presentation is closed on points; an affine scheme is
> quasi-affine and a morphism locally of finite presentation is locally of finite type, so this is
> the step of (3) implies (2) at a target represented by a scheme, which goes through the immersion
> into affine `n`-space of **Stacks 04II**.

```lean
theorem universallyClosed_of_exists_chart_forall_isClosed_baseChange_affineSpaceChart
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : Stack.IsQuasiCompactMorphism.{u, w} B S hS f)
    (h : ∃ (V : BigFppfOver B S hS) (a : Stack.schemeStack.{u, w} B S hS V ⟶ 𝒴),
      Stack.IsSurjective B S hS a ∧ IsSmooth B S hS a ∧
        ∀ n : ℕ, IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS
          (Stack.schemeStackMap.{u, w} B S hS (affineSpaceChartHom B S hS V n) ≫ a) f).fst) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.universallyClosed_tfae_of_isQuasiCompactMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocalQuasiCompact.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/UniversallyClosedSmoothLocalQuasiCompact.lean#L453).

> **Stacks 0H2A.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact 1-morphism of algebraic stacks over `S`.
> The following are equivalent:
>
> 1. `f` is universally closed;
> 2. for every object `Z` of the site whose underlying scheme is affine and every 1-morphism
>    `Stack.schemeStack Z ⟶ 𝒴` locally of finite presentation, the map `|𝒳 ×_𝒴 Z| → |Z|` is closed;
> 3. there are an object `V` of the site and a smooth surjective 1-morphism
>    `a : Stack.schemeStack V ⟶ 𝒴` such that `|𝐀^n × (𝒳 ×_𝒴 V)| → |𝐀^n × V|` is closed for every
>    `n ≥ 0`.
>
> Clause (3) is read as closedness of the base change of `f` along the composite
> `𝐀^n_V ⟶ V ⟶ 𝒴`, which is what `|𝐀^n × (𝒳 ×_𝒴 V)| → |𝐀^n × V|` is over `V`.

```lean
theorem universallyClosed_tfae_of_isQuasiCompactMorphism
    {𝒳 𝒴 : Stack.AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : Stack.IsQuasiCompactMorphism.{u, w} B S hS f) :
    List.TFAE
      [UniversallyClosed B S hS f,
        ∀ Z : BigFppfOver B S hS, IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ g : Stack.schemeStack.{u, w} B S hS Z ⟶ 𝒴, IsLocallyOfFinitePresentation B S hS g →
            IsClosed B S hS (Stack.twoFibreProductSquareAlgebraicStacks B S hS g f).fst,
        ∃ (V : BigFppfOver B S hS) (a : Stack.schemeStack.{u, w} B S hS V ⟶ 𝒴),
          Stack.IsSurjective B S hS a ∧ IsSmooth B S hS a ∧
            ∀ n : ℕ, IsClosed B S hS
              (Stack.twoFibreProductSquareAlgebraicStacks B S hS
                (Stack.schemeStackMap.{u, w} B S hS (affineSpaceChartHom B S hS V n) ≫ a)
                f).fst]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 102.7, Tag 0H28](https://stacks.math.columbia.edu/tag/0H28)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
