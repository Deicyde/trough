---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.flatPullbackIntegralCycle, AlgebraicGeometry.Space.flatPullbackMap, AlgebraicGeometry.Space.flatCyclePullback, AlgebraicGeometry.Space.cycleGroupRestrict_eq_zero_iff, AlgebraicGeometry.Space.cycleGroupRestrict_surjective, AlgebraicGeometry.Space.IntegralClosedSubspace.preimageComponentsCycle_mem_cyclesOfDimension, AlgebraicGeometry.Space.IntegralClosedSubspace.flatPullbackMap_integralCycle_eq_preimageComponentsCycle, AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_comp
statement: formalized
proof: formalized
---

# 82.10 Flat pullback

Section 82.10 of the Stacks Project, [Tag 0EP7](https://stacks.math.columbia.edu/tag/0EP7). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EP8, a definition

[Tag 0EP8](https://stacks.math.columbia.edu/tag/0EP8) in the Stacks Project.

**`AlgebraicGeometry.Space.flatPullbackIntegralCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOfCycles.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOfCycles.lean#L169). The attribute's comment: “part (1): f^*[W] = [f^{-1}(W)]_{k+r} for an integral closed subspace W”.

> The flat pullback of the cycle of an integral closed subspace `W ⊆ Y` of δ-dimension `k`: the
> `(k+r)`-cycle `[f^{-1}(W)]_{k+r}` of the scheme-theoretic inverse image.

```lean
def flatPullbackIntegralCycle (W : IntegralClosedSubspace D.site D.base D.base_mem Y) :
    CycleGroup D sX (deltaDimension D sY W + (r : ℤ))
```

**`AlgebraicGeometry.Space.flatPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOfCycles.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOfCycles.lean#L326). The attribute's comment: “parts (2) and (3): the flat pullback of a cycle and the homomorphism Z_k(Y) → Z_{k+r}(X)”.

> The flat pullback of cycles along a morphism `f : X ⟶ Y` of good algebraic spaces over the base
> which is flat of relative dimension `r`, as a homomorphism `f^* : Z_m(Y) →+ Z_n(X)` for
> `m + r = n`.

```lean
def flatPullbackMap (m n : ℤ) (hmn : m + (r : ℤ) = n) :
    CycleGroup D sY m →+ CycleGroup D sX n
```

**`AlgebraicGeometry.Space.flatCyclePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOfCycles.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackOfCycles.lean#L372). The attribute's comment: “the whole definition, bundled with its defining formula”.

> The flat pullback of cycles along a morphism `f : X ⟶ Y` of good algebraic spaces over the base
> which is flat of relative dimension `r`, as an inhabitant of the bundled
> `AlgebraicGeometry.Space.FlatCyclePullback`: the multiplicities of the inverse images, the
> homomorphisms `Z_m(Y) →+ Z_n(X)` for `m + r = n`, the defining formula relating them, and the
> containment of the support of `f^*[W]` in `f^{-1}(W)`.

```lean
def flatCyclePullback (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) (f : X ⟶ Y) (hbase : f ≫ sY = sX) (r : ℕ)
    (hflat : IsFlat D.site D.base D.base_mem f)
    (hr : HasRelativeDimension r D.site D.base D.base_mem f) :
    FlatCyclePullback D sX hX sY hY f r
```

## Tag 0EP9, a lemma

[Tag 0EP9](https://stacks.math.columbia.edu/tag/0EP9) in the Stacks Project.

**`AlgebraicGeometry.Space.cycleGroupRestrict_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/LocalizationSequence.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/LocalizationSequence.lean#L475). The attribute's comment: “exactness at the k-cycles of the ambient space”.

> **Stacks 0EP9, exactness at the `k`-cycles of the ambient space.** In Situation 0EDT let
> `X/B` be good, let `i : Y ⟶ X` be a closed immersion over the base and let `j : U ⟶ X` be an
> open immersion over the base whose image is the complement of the image of `i`. A `k`-cycle on
> `X` restricts to zero on `U` exactly when it is the pushforward of a `k`-cycle on `Y`.

```lean
theorem cycleGroupRestrict_eq_zero_iff (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) (sU : U ⟶ D.space) (hU : D.IsGood sU) {i : Y ⟶ X}
    (hi : IsClosedImmersion D.site D.base D.base_mem i) (hic : i ≫ sX = sY) {j : U ⟶ X}
    (hj : IsOpenImmersion D.site D.base D.base_mem j) (hjc : j ≫ sX = sU)
    (hcomplement : Set.range (pointsMap D.site D.base D.base_mem Y i) =
      (Set.range (pointsMap D.site D.base D.base_mem U j))ᶜ) (k : ℤ) (α : CycleGroup D sX k) :
    cycleGroupRestrict D sX hX sU hU hj hjc k α = 0 ↔
      ∃ β : CycleGroup D sY k,
        cycleGroupClosedPushforward D hX.1 hY.1 (D.isDecentSpace_of_isGood sX hX) hi sX hX.2.2
          sY hic k β = α
```

**`AlgebraicGeometry.Space.cycleGroupRestrict_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/LocalizationSequence.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/LocalizationSequence.lean#L565). The attribute's comment: “surjectivity onto the k-cycles of the open subspace”.

> **Stacks 0EP9, surjectivity onto the `k`-cycles of the open subspace.** In Situation 0EDT let
> `X/B` and `U/B` be good and let `j : U ⟶ X` be an open immersion over the base. Every `k`-cycle
> on `U` is the restriction of a `k`-cycle on `X`, namely of the coefficient family extending it by
> zero along the map which takes the closure of the image of an integral closed subspace.
>
> That extension is a `k`-cycle: it has the right δ-dimension because taking the closure of the
> image preserves it, and its support family is locally finite because `|X|` is locally Noetherian,
> the structure morphism being locally of finite type over a locally Noetherian base.

```lean
theorem cycleGroupRestrict_surjective (sX : X ⟶ D.space) (hX : D.IsGood sX) (sU : U ⟶ D.space)
    (hU : D.IsGood sU) {j : U ⟶ X} (hj : IsOpenImmersion D.site D.base D.base_mem j)
    (hjc : j ≫ sX = sU) (k : ℤ) :
    Function.Surjective (cycleGroupRestrict D sX hX sU hU hj hjc k)
```

## Tag 0EPY, a lemma

[Tag 0EPY](https://stacks.math.columbia.edu/tag/0EPY) in the Stacks Project.

**`AlgebraicGeometry.Space.IntegralClosedSubspace.preimageComponentsCycle_mem_cyclesOfDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackComponents.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackComponents.lean#L434). The attribute's comment: “the sum of the components of the inverse image is a cycle of the same δ-dimension”.

> **Stacks 0EPY, the right-hand side of its formula.** Let `f : X ⟶ Y` be an étale morphism of
> good algebraic spaces over the base of Situation 0EDT and let `Z ⊆ Y` be an integral closed
> subspace. The formal sum of the irreducible components of the inverse image of `Z`, each with
> coefficient one, is a cycle of the δ-dimension of `Z` on `X`.
>
> The components are integral closed subspaces of `X`, they form a locally finite family, and each
> of them has the δ-dimension of `Z`; these are exactly the two conditions defining
> `Z_{δ(Z)}(X)`.

```lean
theorem IntegralClosedSubspace.preimageComponentsCycle_mem_cyclesOfDimension (sX : X ⟶ D.space)
    (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY) {f : X ⟶ Y}
    (hf : IsEtale D.site D.base D.base_mem f) (hfc : f ≫ sY = sX)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem Y) :
    Z.preimageComponentsCycle D sX hX sY hY f ∈
      cyclesOfDimension D sX (deltaDimension D sY Z)
```

**`AlgebraicGeometry.Space.IntegralClosedSubspace.flatPullbackMap_integralCycle_eq_preimageComponentsCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackIdentity.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EtalePullbackIdentity.lean#L482).

> Let `f : X ⟶ Y` be an étale morphism of good algebraic spaces over the base
> `B` of Situation 0EDT and let `Z ⊆ Y` be an integral closed subspace, of δ-dimension `m`. Then
>
> `f^*[Z] = ∑ [Z']`,
>
> the sum running over the irreducible components `Z'` of the inverse image `f^{-1}(Z)` (in the
> sense of Remark 0EE8), each with coefficient one: the coefficient family of the cycle `f^*[Z]`
> is the formal sum `AlgebraicGeometry.Space.IntegralClosedSubspace.preimageComponentsCycle` of
> those components.
>
> The left-hand side is the flat pullback `AlgebraicGeometry.Space.flatPullbackMap` of Stacks 0EP8
> at relative dimension `0`, which an étale morphism has by
> `AlgebraicGeometry.Space.hasRelativeDimension_zero_of_isEtale`, applied to the cycle `[Z]`; the
> pullback lands in degree `n` for any `n` with `m + 0 = n`.

```lean
theorem IntegralClosedSubspace.flatPullbackMap_integralCycle_eq_preimageComponentsCycle
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY) {f : X ⟶ Y}
    (hf : IsEtale D.site D.base D.base_mem f) (hfc : f ≫ sY = sX)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem Y) (m n : ℤ)
    (hm : deltaDimension D sY Z = m) (hmn : m + ((0 : ℕ) : ℤ) = n) :
    (flatPullbackMap D sX hX sY hY f hfc 0
          (isFlat_of_isEtale D.site D.base D.base_mem hf)
          (hasRelativeDimension_zero_of_isEtale D.site D.base D.base_mem f hY.1 hf) m n hmn
        (integralCycle D sY m Z hm)).1 =
      Z.preimageComponentsCycle D sX hX sY hY f
```

## Tag 0EPA, a lemma

[Tag 0EPA](https://stacks.math.columbia.edu/tag/0EPA) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatCompositeRelativeDimension.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatCompositeRelativeDimension.lean#L64). The attribute's comment: “the composite is flat of relative dimension r + s”.

> Let `X/B`, `Y/B` and `Z/B` be good algebraic spaces over the base of `D` and let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms over the base which are flat of relative dimensions `r`
> and `s`. Then the composite `f ≫ g` is flat of relative dimension `r + s`: it is locally of
> finite type, flat, and of relative dimension `r + s`.

```lean
theorem isFlat_and_hasRelativeDimension_comp (D : BaseSpaceDimensionSituation.{u})
    {X Y Z : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u}
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY)
    (sZ : Z ⟶ D.space) (hZ : D.IsGood sZ) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfbase : f ≫ sY = sX) (hgbase : g ≫ sZ = sY) (r s : ℕ)
    (hff : IsFlat D.site D.base D.base_mem f)
    (hfr : HasRelativeDimension r D.site D.base D.base_mem f)
    (hgf : IsFlat D.site D.base D.base_mem g)
    (hgs : HasRelativeDimension s D.site D.base D.base_mem g) :
    IsLocallyOfFiniteType D.site D.base D.base_mem (f ≫ g) ∧
      IsFlat D.site D.base D.base_mem (f ≫ g) ∧
        HasRelativeDimension (r + s) D.site D.base D.base_mem (f ≫ g)
```

**`AlgebraicGeometry.Space.isFlat_and_hasRelativeDimension_comp_and_flatPullbackMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackComposition.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackComposition.lean#L222). The attribute's comment: “both assertions: g ∘ f is flat of relative dimension r + s, and f^* ∘ g^* = (g ∘ f)^* as maps Z_k(Z) → Z_{k+r+s}(X)”.

> In Situation 0EDT let `X/B`, `Y/B` and `Z/B` be good and let `f : X ⟶ Y`
> and `g : Y ⟶ Z` be morphisms over the base which are flat of relative dimensions `r` and `s`.
> Then
>
> 1. `g ∘ f` is flat of relative dimension `r + s` (and locally of finite type), and
> 2. `f^* ∘ g^* = (g ∘ f)^*` as maps `Z_k(Z) → Z_{k+r+s}(X)`, for every `k`.
>
> The degree of the target is any `n` with `k + (r + s) = n`, which is how
> `AlgebraicGeometry.Space.flatPullbackMap` is graded. The flat pullback along `g ∘ f` in part (2)
> is formed with the flatness and relative dimension that part (1) provides.

```lean
theorem isFlat_and_hasRelativeDimension_comp_and_flatPullbackMap_comp :
    (IsLocallyOfFiniteType D.site D.base D.base_mem (f ≫ g) ∧
      IsFlat D.site D.base D.base_mem (f ≫ g) ∧
        HasRelativeDimension (r + s) D.site D.base D.base_mem (f ≫ g)) ∧
      ∀ (k n : ℤ) (hn : k + ((r + s : ℕ) : ℤ) = n),
        (flatPullbackMap D sX hX sY hY f hfbase r hff hfr (k + (s : ℤ)) n
            (by push_cast at hn; omega)).comp
          (flatPullbackMap D sY hY sZ hZ g hgbase s hgf hgs k (k + (s : ℤ)) rfl) =
        flatPullbackMap D sX hX sZ hZ (f ≫ g)
          (comp_structureMorphism_eq D sX sY sZ f g hfbase hgbase) (r + s)
          (isFlat_and_hasRelativeDimension_comp D sX hX sY hY sZ hZ f g hfbase hgbase r s
            hff hfr hgf hgs).2.1
          (isFlat_and_hasRelativeDimension_comp D sX hX sY hY sZ hZ f g hfbase hgbase r s
            hff hfr hgf hgs).2.2 k n hn
```

## Tag 0EPB, a lemma

[Tag 0EPB](https://stacks.math.columbia.edu/tag/0EPB) in the Stacks Project.

**`AlgebraicGeometry.Space.flatPullback_closedSubspaceCycle_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackAssociatedCycle.lean, line 591](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackAssociatedCycle.lean#L591). The attribute's comment: “part (1)”.

> **Stacks 0EPB, part (1).** In Situation 0EDT let `X/B` and `Y/B` be good and let
> `f : X ⟶ Y` be a morphism over the base which is flat of relative dimension `r`. Let `Z ⊆ Y` be
> a closed subspace with `dim_δ(Z) ≤ k`. Then `dim_δ(f^{-1}(Z)) ≤ k + r` and
>
> `[f^{-1}(Z)]_{k+r} = f^*[Z]_k` in `Z_{k+r}(X)`.
>
> The cycle of a closed subspace is `AlgebraicGeometry.Space.closedSubspaceCycle` (Stacks 0EE9)
> and the flat pullback is `AlgebraicGeometry.Space.flatPullbackMap` (Stacks 0EP8).

```lean
theorem flatPullback_closedSubspaceCycle_preimage (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (sY : Y ⟶ D.space) (hY : D.IsGood sY) (f : X ⟶ Y) (hbase : f ≫ sY = sX) (r : ℕ)
    (hflat : IsFlat D.site D.base D.base_mem f)
    (hr : HasRelativeDimension r D.site D.base D.base_mem f) (k : ℤ) (Z : Subfunctor Y)
    (hZ : IsClosedSubspace D.site D.base D.base_mem Z)
    (hZk : deltaDimensionSubspace D sY hY Z hZ ≤ (k : EInt)) :
    ∃ hdim : deltaDimensionSubspace D sX hX (Z.preimage f)
        (isClosedSubspace_preimage D.site D.base D.base_mem f Z hY.1 hX.1 hZ) ≤
          ((k + (r : ℤ) : ℤ) : EInt),
      closedSubspaceCycle D sX hX (Z.preimage f)
          (isClosedSubspace_preimage D.site D.base D.base_mem f Z hY.1 hX.1 hZ) (k + (r : ℤ))
          hdim =
        flatPullbackMap D sX hX sY hY f hbase r hflat hr k (k + (r : ℤ)) rfl
          (closedSubspaceCycle D sY hY Z hZ k hZk)
```

**`AlgebraicGeometry.Space.flatPullback_associatedCycle_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackAssociatedCycle.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackAssociatedCycle.lean#L723). The attribute's comment: “part (2)”.

> **Stacks 0EPB, part (2).** In Situation 0EDT let `X/B` and `Y/B` be good and let
> `f : X ⟶ Y` be a morphism over the base which is flat of relative dimension `r`. Let `F` be a
> coherent `𝒪_Y`-module with `dim_δ(Supp(F)) ≤ k`. Then `dim_δ(Supp(f^*F)) ≤ k + r` and
>
> `f^*[F]_k = [f^*F]_{k+r}` in `Z_{k+r}(X)`.
>
> The cycle of a coherent module is `AlgebraicGeometry.Space.associatedCycle` (Stacks 0EEB), read at
> any choice `γ_X`, `γ_Y` of geometric points over the points of `X` and `Y`; the pullback `f^*F`
> is coherent by `AlgebraicGeometry.Space.isCoherent_modulePullback`, `X` being locally
> Noetherian.

```lean
theorem flatPullback_associatedCycle_modulePullback (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (sY : Y ⟶ D.space) (hY : D.IsGood sY) (f : X ⟶ Y) (hbase : f ≫ sY = sX) (r : ℕ)
    (hflat : IsFlat D.site D.base D.base_mem f)
    (hr : HasRelativeDimension r D.site D.base D.base_mem f)
    (F : Modules.{u, u} D.site D.base D.base_mem Y hY.1)
    [IsCoherent D.site D.base D.base_mem Y hY.1 F] (k : ℤ)
    (hFk : deltaDimensionClosed D sY hY (moduleSupport D.site D.base D.base_mem hY.1 F)
      (isClosed_moduleSupport D.site D.base D.base_mem hY.1 F) ≤ (k : EInt))
    (γY : points D.site D.base D.base_mem Y → GeometricPoint D.site D.base D.base_mem Y)
    (hγY : ∀ y, (γY y).LiesOver y)
    (γX : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγX : ∀ x, (γX x).LiesOver x) :
    letI : IsCoherent D.site D.base D.base_mem X hX.1
        ((modulePullback D.site D.base D.base_mem
          (ObjectProperty.homMk f :
            (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶ ⟨Y, hY.1⟩)).obj F) :=
      haveI : Fact (HasEtaleLocalProperty D.site D.base D.base_mem X
          (fun V : Scheme.{u} => IsLocallyNoetherian V)) :=
        ⟨hasEtaleLocalProperty_isLocallyNoetherian_of_isLocallyOfFiniteType D.site D.base
          D.base_mem hX.1 D.isAlgebraicSpace sX hX.2.2 D.locallyNoetherian⟩
      isCoherent_modulePullback D.site D.base D.base_mem
        (ObjectProperty.homMk f :
          (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶ ⟨Y, hY.1⟩) F inferInstance
    ∃ hdim : deltaDimensionClosed D sX hX
        (moduleSupport D.site D.base D.base_mem hX.1
          ((modulePullback D.site D.base D.base_mem
            (ObjectProperty.homMk f :
              (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶ ⟨Y, hY.1⟩)).obj F))
        (isClosed_moduleSupport D.site D.base D.base_mem hX.1 _) ≤
          ((k + (r : ℤ) : ℤ) : EInt),
      flatPullbackMap D sX hX sY hY f hbase r hflat hr k (k + (r : ℤ)) rfl
          (associatedCycle D sY hY F k γY hγY hFk) =
        associatedCycle D sX hX
          ((modulePullback D.site D.base D.base_mem
            (ObjectProperty.homMk f :
              (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶ ⟨Y, hY.1⟩)).obj F)
          (k + (r : ℤ)) γX hγX hdim
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.10, Tag 0EP7](https://stacks.math.columbia.edu/tag/0EP7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
