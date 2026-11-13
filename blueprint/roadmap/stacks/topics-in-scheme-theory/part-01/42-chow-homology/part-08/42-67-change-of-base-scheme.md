---
declaration: section
origin: cited
lean: Stacks.Chow.FlatBaseChangeSituation, Stacks.Chow.deltaDimension_component_baseChange, Stacks.Chow.schemeDeltaDimension_baseChange_closedSubscheme_le, Stacks.Chow.schemeDeltaDimension_baseChange_support_le, Stacks.Chow.baseChangeCyclePullback_cycleAssociatedToCoherentSheaf, Stacks.Chow.baseChangeCyclePullback_cycleAssociatedToClosedSubscheme, AlgebraicGeometry.isCoherent_pullback, Stacks.Chow.baseChangeCyclePullback_maps_rationalEquivalences
statement: formalized
proof: formalized
---

# 42.67 Change of base scheme

Section 42.67 of the Stacks Project, [Tag 0FVF](https://stacks.math.columbia.edu/tag/0FVF). 10 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FVG, a situation

[Tag 0FVG](https://stacks.math.columbia.edu/tag/0FVG) in the Stacks Project.

**`Stacks.Chow.FlatBaseChangeSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Basic.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Basic.lean#L34).

> A flat morphism between two bases for Chow homology whose dimension functions differ by a
> fixed integer on the generic points of the irreducible components of every fibre.

```lean
structure FlatBaseChangeSituation
```

## Tag 0FVH, a lemma

[Tag 0FVH](https://stacks.math.columbia.edu/tag/0FVH) in the Stacks Project.

**`Stacks.Chow.deltaDimension_component_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/BaseChangeComponentDimension.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/BaseChangeComponentDimension.lean#L148).

> In the flat base-change situation of Stacks 0FVG, if `X` is integral and locally of finite
> type over `S` with `dim_δ(X) = k`, then every irreducible component of the base change
> `X ×_S S'` has delta-dimension `k + c`.

```lean
theorem deltaDimension_component_baseChange (B : FlatBaseChangeSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ B.base.S) [LocallyOfFiniteType f] [IsIntegral X]
    (k : ℤ) (hk : schemeDeltaDimension B.base f = (k : EInt))
    (Z : irreducibleComponents (pullback f B.g : Scheme.{u})) :
    deltaDimension B.baseChange (pullback.snd f B.g)
        ⟨Z, Z.2.1,
          isClosed_of_mem_irreducibleComponents
            (Z : Set (pullback f B.g : Scheme.{u})) Z.2⟩ =
      k + B.c
```

## Tag 0FVI, a lemma

[Tag 0FVI](https://stacks.math.columbia.edu/tag/0FVI) in the Stacks Project.

**`Stacks.Chow.schemeDeltaDimension_baseChange_closedSubscheme_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean#L245). The attribute's comment: “part (1): dimension bound”.

> **Stacks 0FVI, part (1), dimension bound.** In the flat base-change situation of Stacks
> 0FVG, the base change `Z' = Z ×_X X'` of a closed subscheme `Z ⊆ X` of delta-dimension at most
> `k` is a closed subscheme of `X' = X ×_S S'` of delta-dimension at most `k + c`.

```lean
theorem schemeDeltaDimension_baseChange_closedSubscheme_le (B : FlatBaseChangeSituation.{u})
    {X Z : Scheme.{u}} (f : X ⟶ B.base.S) [LocallyOfFiniteType f] (i : Z ⟶ X)
    [IsClosedImmersion i] {k : ℤ}
    (hZ : schemeDeltaDimension B.base (i ≫ f) ≤ (k : EInt)) :
    schemeDeltaDimension B.baseChange
        (pullback.snd i (pullback.fst f B.g) ≫ pullback.snd f B.g) ≤ ((k + B.c : ℤ) : EInt)
```

**`Stacks.Chow.schemeDeltaDimension_baseChange_support_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean#L264). The attribute's comment: “part (2): support dimension bound”.

> **Stacks 0FVI, part (2), dimension bound.** In the flat base-change situation of Stacks
> 0FVG, if a coherent sheaf on `X` has support of delta-dimension at most `k`, then the support of
> its base change to `X' = X ×_S S'` has delta-dimension at most `k + c`.
>
> Every point of the support of the base change lies over the support of the sheaf, so part (1)
> for the reduced support bounds the relative dimension there.

```lean
theorem schemeDeltaDimension_baseChange_support_le (B : FlatBaseChangeSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ B.base.S) [LocallyOfFiniteType f] (F : X.Modules)
    [F.IsCoherent] {k : ℤ}
    (hFk : schemeDeltaDimension B.base ((reducedSupport F).subschemeι ≫ f) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian (pullback f B.g : Scheme.{u}) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.snd f B.g)
    letI : ((Scheme.Modules.pullback (pullback.fst f B.g)).obj F).IsCoherent :=
      AlgebraicGeometry.isCoherent_pullback (pullback.fst f B.g) F
    schemeDeltaDimension B.baseChange
        ((reducedSupport ((Scheme.Modules.pullback (pullback.fst f B.g)).obj F)).subschemeι ≫
          pullback.snd f B.g) ≤ ((k + B.c : ℤ) : EInt)
```

**`Stacks.Chow.baseChangeCyclePullback_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean#L379). The attribute's comment: “part (2): cycle identity”.

> **Stacks 0FVI, part (2), cycle identity.** In the flat base-change situation of Stacks 0FVG,
> the base change of the cycle of a coherent sheaf `F` on `X` whose support has delta-dimension at
> most `k` is the cycle of the base change of `F`:
>
> `g^*[F]_k = [F']_{k + c}`.
>
> The two sides are compared at one point `x'` of `X'` at a time. If `x'` has relative dimension
> other than `k + c` both vanish, the left one because the base-change multiplicity is formed only
> in that degree. If `x'` lies off the support of `F'` then its image lies off the support of `F`,
> since the support of a pullback is the inverse image of the support, so the coefficient of
> `[F]_k` already vanishes there. In the remaining case the relative dimension of the image is
> forced to be exactly `k`, because it is at most `k` on the support of `F` while the relative
> dimension of `x'` exceeds it by at most `c`; the two multiplicities are then
> `length_A M * length_B (B / 𝔪_A B)` and `length_B (B ⊗_A M)` for `A = 𝒪_{X, x}`, `B = 𝒪_{X', x'}`
> and `M = F_x`, equal by Stacks 02M1.

```lean
theorem baseChangeCyclePullback_cycleAssociatedToCoherentSheaf (B : FlatBaseChangeSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ B.base.S) [LocallyOfFiniteType f] (F : X.Modules) [F.IsCoherent]
    (k : ℤ) (hFk : schemeDeltaDimension B.base ((reducedSupport F).subschemeι ≫ f) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian (pullback f B.g : Scheme.{u}) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.snd f B.g)
    letI : ((Scheme.Modules.pullback (pullback.fst f B.g)).obj F).IsCoherent :=
      AlgebraicGeometry.isCoherent_pullback (pullback.fst f B.g) F
    baseChangeCyclePullback B f k (cycleAssociatedToCoherentSheaf B.base f F k hFk) =
      cycleAssociatedToCoherentSheaf B.baseChange (pullback.snd f B.g)
        ((Scheme.Modules.pullback (pullback.fst f B.g)).obj F) (k + B.c)
        (schemeDeltaDimension_baseChange_support_le B f F hFk)
```

**`Stacks.Chow.baseChangeCyclePullback_cycleAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean, line 496](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean#L496). The attribute's comment: “part (1): cycle identity”.

> **Stacks 0FVI, part (1), cycle identity.** In the flat base-change situation of Stacks 0FVG,
> the base change of the cycle of a closed subscheme `Z ⊆ X` of delta-dimension at most `k` is the
> cycle of the base change `Z' = Z ×_X X'`:
>
> `g^*[Z]_k = [Z']_{k + c}`.
>
> By Stacks 02QY both cycles are cycles of coherent sheaves, namely of `i_* 𝒪_Z` and of
> `i'_* 𝒪_{Z'}`, so part (2) reduces the claim to the flat base change of `i_* 𝒪_Z` being
> `i'_* 𝒪_{Z'}`.

```lean
theorem baseChangeCyclePullback_cycleAssociatedToClosedSubscheme (B : FlatBaseChangeSituation.{u})
    {X Z : Scheme.{u}} (f : X ⟶ B.base.S) [LocallyOfFiniteType f] (i : Z ⟶ X)
    [IsClosedImmersion i] (k : ℤ)
    (hZ : schemeDeltaDimension B.base (i ≫ f) ≤ (k : EInt)) :
    baseChangeCyclePullback B f k (cycleAssociatedToClosedSubscheme B.base f i k) =
      cycleAssociatedToClosedSubscheme B.baseChange (pullback.snd f B.g)
        (pullback.snd i (pullback.fst f B.g)) (k + B.c)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isCoherent_pullback`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CoherentPullback/Basic.lean#L48), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Dimension.lean#L239) (StacksFrontier): “part (2): coherence of the base change”.

## Tag 0FVJ, a lemma

[Tag 0FVJ](https://stacks.math.columbia.edu/tag/0FVJ) in the Stacks Project.

**`Stacks.Chow.baseChangeCyclePullback_maps_rationalEquivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ChowPullback.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ChowPullback.lean#L291). The attribute's comment: “preservation of rational equivalence”.

> **Stacks Project, Tag 0FVJ, preservation of rational equivalence.** In a flat base-change
> situation with dimension shift `c`, the base-change homomorphism on cycle groups carries
> `k`-cycles rationally equivalent to zero on `X` to `(k + c)`-cycles rationally equivalent to
> zero on `X' = X ×_S S'`.
>
> By Stacks 02S4 part (4) such a cycle is the total fibre difference of a locally finite family of
> integral closed subschemes of `X ×_S 𝐏¹_S`, each of relative dimension `k + 1` at its generic
> points and contained in neither distinguished section. Its base change is the total fibre
> difference of the base-changed family, which is again locally finite, and each member of the
> base-changed family satisfies the hypotheses of Stacks 02S5 over the new base: the dimension
> bounds are those of
> `StacksFrontier.AlgebraicGeometry.Chow.ChangeBaseScheme.FamilyDimension`, and the condition on
> associated points holds because the projection to the original member is flat. The individual
> equivalences are summed by `Stacks.Chow.rationallyEquivalentToZero_finsum`, the carriers of the
> members forming a locally finite family.

```lean
theorem baseChangeCyclePullback_maps_rationalEquivalences (k : ℤ) :
    rationalEquivalences B.base f k ≤
      (rationalEquivalences B.baseChange (pullback.snd f B.g) (k + B.c)).comap
        (baseChangeCyclePullback B f k)
```

**`Stacks.Chow.baseChangeChowPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ChowPullback.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ChowPullback.lean#L348). The attribute's comment: “induced map on Chow groups”.

> **Stacks Project, Tag 0FVJ, the map on Chow groups.** The homomorphism
> `g^* : CH_k(X) ⟶ CH_{k+c}(X ×_S S')` induced on Chow groups by the base-change homomorphism
> on cycle groups, which preserves rational equivalence by
> `Stacks.Chow.baseChangeCyclePullback_maps_rationalEquivalences`.

```lean
def baseChangeChowPullback (k : ℤ) :
    chowGroup B.base f k →+ chowGroup B.baseChange (pullback.snd f B.g) (k + B.c)
```

## Tag 0FVK, a lemma

[Tag 0FVK](https://stacks.math.columbia.edu/tag/0FVK) in the Stacks Project.

**`Stacks.Chow.flat_relativeDimension_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatPullback.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatPullback.lean#L135). The attribute's comment: “flatness and relative dimension of the base-changed morphism”.

> **Stacks 0FVK.** In a flat base-change situation, the base change of a morphism locally of
> finite type and flat of relative dimension `r` is again locally of finite type and flat of
> relative dimension `r`.
>
> Flatness and local finite type are stable under base change, and the relative dimension is
> Stacks 02NK.

```lean
theorem flat_relativeDimension_baseChange (B : FlatBaseChangeSituation.{u}) {Y X : Scheme.{u}}
    (sY : Y ⟶ B.base.S) (sX : X ⟶ B.base.S) (f : Y ⟶ X) [LocallyOfFiniteType f] [Flat f]
    (f' : (pullback sY B.g : Scheme.{u}) ⟶ (pullback sX B.g : Scheme.{u}))
    (hsq : IsPullback (pullback.fst sY B.g) f' f (pullback.fst sX B.g))
    (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r) :
    letI : LocallyOfFiniteType f' :=
      MorphismProperty.of_isPullback hsq (P := @LocallyOfFiniteType) inferInstance
    Flat f' ∧ AlgebraicGeometry.RelativeDimension f' r
```

**`Stacks.Chow.baseChange_flatPullback_cycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatPullback.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatPullback.lean#L419). The attribute's comment: “commuting diagram of cycle groups”.

> **Stacks 0FVK.** The square of cycle groups commutes: base change after flat pullback is
> flat pullback after base change, as homomorphisms `Z_k(X) ⟶ Z_{k+c+r}(Y')`.
>
> The two composites land in cycle groups of degree `(k + r) + c` and `(k + c) + r`, so the
> statement is heterogeneous; its content is the coefficient identity
> `Stacks.Chow.baseChangeCyclePullback_flatPullback_apply`.

```lean
theorem baseChange_flatPullback_cycles
    (B : FlatBaseChangeSituation.{u}) {Y X : Scheme.{u}}
    (sY : Y ⟶ B.base.S) [LocallyOfFiniteType sY] (sX : X ⟶ B.base.S) [LocallyOfFiniteType sX]
    (f : Y ⟶ X) [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sX = sY)
    (f' : (pullback sY B.g : Scheme.{u}) ⟶ (pullback sX B.g : Scheme.{u}))
    [LocallyOfFiniteType f'] [Flat f']
    (hbase' : f' ≫ pullback.snd sX B.g = pullback.snd sY B.g)
    (hcomm : pullback.fst sY B.g ≫ f = f' ≫ pullback.fst sX B.g)
    (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (hf' : AlgebraicGeometry.RelativeDimension f' r) (k : ℤ) :
    HEq ((baseChangeCyclePullback B sY (k + (r : ℤ))).comp
          (flatPullback B.base sY sX f hbase r hf k))
      ((flatPullback B.baseChange (pullback.snd sY B.g) (pullback.snd sX B.g) f' hbase' r hf'
          (k + B.c)).comp (baseChangeCyclePullback B sX k))
```

**`Stacks.Chow.baseChange_flatPullback_chow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatPullback.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatPullback.lean#L446). The attribute's comment: “commuting diagram of Chow groups”.

> **Stacks 0FVK.** The square of Chow groups commutes: base change after flat pullback is flat
> pullback after base change, as homomorphisms `A_k(X) ⟶ A_{k+c+r}(Y')`.
>
> This is the image of `Stacks.Chow.baseChange_flatPullback_cycles` under the quotient maps, which
> is why the source says it suffices to prove the square of cycle groups.

```lean
theorem baseChange_flatPullback_chow
    (B : FlatBaseChangeSituation.{u}) {Y X : Scheme.{u}}
    (sY : Y ⟶ B.base.S) [LocallyOfFiniteType sY] (sX : X ⟶ B.base.S) [LocallyOfFiniteType sX]
    (f : Y ⟶ X) [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sX = sY)
    (f' : (pullback sY B.g : Scheme.{u}) ⟶ (pullback sX B.g : Scheme.{u}))
    [LocallyOfFiniteType f'] [Flat f']
    (hbase' : f' ≫ pullback.snd sX B.g = pullback.snd sY B.g)
    (hcomm : pullback.fst sY B.g ≫ f = f' ≫ pullback.fst sX B.g)
    (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (hf' : AlgebraicGeometry.RelativeDimension f' r) (k : ℤ) :
    HEq ((flatBaseChangeChowPullback B sY (k + (r : ℤ))
            (baseChangeFactorsThroughRationalEquivalence B sY (k + (r : ℤ)))).comp
          (flatPullbackChow B.base sY sX f hbase r hf k
            (flatPullbackFactorsThroughRationalEquivalence_general B.base sY sX f hbase r hf k)))
      ((flatPullbackChow B.baseChange (pullback.snd sY B.g) (pullback.snd sX B.g) f' hbase' r hf'
          (k + B.c)
          (flatPullbackFactorsThroughRationalEquivalence_general B.baseChange
            (pullback.snd sY B.g) (pullback.snd sX B.g) f' hbase' r hf' (k + B.c))).comp
        (flatBaseChangeChowPullback B sX k
          (baseChangeFactorsThroughRationalEquivalence B sX k)))
```

## Tag 0FVL, a lemma

[Tag 0FVL](https://stacks.math.columbia.edu/tag/0FVL) in the Stacks Project.

**`Stacks.Chow.isProper_baseChangeMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean#L131). The attribute's comment: “properness of the base change”.

> **Stacks Project, Tag 0FVL, properness of the base change.** In a flat base change of Chow
> situations, the morphism `f' : Y ×_S S' ⟶ X ×_S S'` induced by a proper morphism `f : Y ⟶ X` is
> proper, because it is a base change of `f` and properness is stable under base change.

```lean
theorem isProper_baseChangeMorphism [IsProper f] : IsProper (baseChangeMorphism B sX f)
```

**`Stacks.Chow.properPushforward_baseChangeCyclePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean#L309). The attribute's comment: “the cycle square”.

> **Stacks Project, Tag 0FVL, the cycle square.** In a flat base change of Chow situations,
> proper pushforward commutes with the base-change map on cycle groups: for `f : Y ⟶ X` proper
> over the base `S`, the square whose horizontal maps are `g^* : Z_k(Y) ⟶ Z_{k+c}(Y')` and
> `g^* : Z_k(X) ⟶ Z_{k+c}(X')` and whose vertical maps are `f_*` and `f'_*` commutes.
>
> Both routes are additive, and a cycle agrees, on the part of its support lying over a single
> point `x` of `X'`, with a finite sum of prime cycles: that part is the intersection of the
> support with the fibre of the proper morphism `f` over the image of `x`, hence finite, and both
> routes read the coefficient at `x` only off that part. So it suffices to treat a prime cycle,
> which is the fundamental cycle of the reduced closure of a point and so is covered by the case
> of a closed subscheme.
>
> Coherence of the direct image of a coherent module under a proper morphism to a locally
> Noetherian scheme is `Stacks.Chow.forall_properDirectImageIsCoherent`, the first assertion of
> Stacks 02O5.

```lean
theorem properPushforward_baseChangeCyclePullback
    [LocallyOfFiniteType sX] [IsProper f] (k : ℤ)
    (z : CycleGroup B.base (f ≫ sX) k) :
    letI : IsProper (baseChangeMorphism B sX f) := isProper_baseChangeMorphism B sX f
    properPushforward B.baseChange (pullback.snd (f ≫ sX) B.g) (pullback.snd sX B.g)
        (baseChangeMorphism B sX f) (baseChangeMorphism_comp_snd B sX f) (k + B.c)
        (baseChangeCyclePullback B (f ≫ sX) k z) =
      baseChangeCyclePullback B sX k (properPushforward B.base (f ≫ sX) sX f rfl k z)
```

**`Stacks.Chow.properChowPushforward_baseChangeChowPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean#L418). The attribute's comment: “the Chow square, in the generality of every Chow base-change map induced by the cycle-level one of Tag 0FVJ; instantiated at that map, with nothing left to supply, by properChowPushforward\_baseChangeChowPullback\_of\_baseChangeChowPullback below”.

> **Stacks Project, Tag 0FVL, the Chow square.** In a flat base change of Chow situations,
> proper pushforward commutes with the base-change map on Chow groups: for `f : Y ⟶ X` proper over
> the base `S`, the square whose horizontal maps are `g^* : CH_k(Y) ⟶ CH_{k+c}(Y')` and
> `g^* : CH_k(X) ⟶ CH_{k+c}(X')` and whose vertical maps are `f_*` and `f'_*` commutes.
>
> Every class is the class of a cycle, and on classes of cycles both routes are the class of the
> corresponding route on cycles, so this follows from the cycle square.
>
> The base-change map on Chow groups is a parameter `gChow` of this statement rather than a fixed
> map, constrained by `hgChow` to be induced by the base-change map on cycle groups. This is a
> generality, not an assumption: quantifying over every such map is stronger than the source's
> statement, and the map itself exists, so
> `Stacks.Chow.properChowPushforward_baseChangeChowPullback_of_baseChangeChowPullback` below
> instantiates this at the base-change map of Stacks 0FVJ and is unconditional. Coherence of the
> direct image of a
> coherent module under a proper morphism to a locally Noetherian scheme is
> `Stacks.Chow.forall_properDirectImageIsCoherent`, the first assertion of Stacks 02O5.

```lean
theorem properChowPushforward_baseChangeChowPullback
    [LocallyOfFiniteType sX] [IsProper f] (k : ℤ)
    (gChow : ∀ {W : Scheme.{u}} (sW : W ⟶ B.base.S) [LocallyOfFiniteType sW] (j : ℤ),
      chowGroup B.base sW j →+ chowGroup B.baseChange (pullback.snd sW B.g) (j + B.c))
    (hgChow : ∀ {W : Scheme.{u}} (sW : W ⟶ B.base.S) [LocallyOfFiniteType sW] (j : ℤ)
      (a : CycleGroup B.base sW j),
      gChow sW j (QuotientAddGroup.mk' (rationalEquivalences B.base sW j) a) =
        QuotientAddGroup.mk' (rationalEquivalences B.baseChange (pullback.snd sW B.g) (j + B.c))
          (baseChangeCyclePullback B sW j a))
    (w : chowGroup B.base (f ≫ sX) k) :
    letI : IsProper (baseChangeMorphism B sX f) := isProper_baseChangeMorphism B sX f
    properChowPushforward B.baseChange (pullback.snd (f ≫ sX) B.g) (pullback.snd sX B.g)
        (baseChangeMorphism B sX f) (baseChangeMorphism_comp_snd B sX f) (k + B.c)
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper B.baseChange
          (pullback.snd (f ≫ sX) B.g) (pullback.snd sX B.g) (baseChangeMorphism B sX f)
          (baseChangeMorphism_comp_snd B sX f) (k + B.c))
        (gChow (f ≫ sX) k w) =
      gChow sX k (properChowPushforward B.base (f ≫ sX) sX f rfl k
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper B.base (f ≫ sX) sX f rfl
          k) w)
```

**`Stacks.Chow.properChowPushforward_baseChangeChowPullback_of_baseChangeChowPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/ProperPushforward.lean#L460). The attribute's comment: “the Chow square for the base-change map of Tag 0FVJ”.

> **Stacks Project, Tag 0FVL, the Chow square for the base-change map of Stacks 0FVJ.** In a
> flat base change of Chow situations, proper pushforward commutes with the base-change map
> `g^* : CH_k(X) ⟶ CH_{k+c}(X ×_S S')` of Stacks 0FVJ: for `f : Y ⟶ X` proper over the base `S`,
> the square whose horizontal maps are those base-change maps for `Y` and for `X` and whose
> vertical maps are `f_*` and `f'_*` commutes.
>
> This is the Chow square with its Chow base-change map supplied rather than assumed: the map is
> `Stacks.Chow.baseChangeChowPullback`, and it meets the characterization of the general statement
> because `Stacks.Chow.baseChangeChowPullback_mk` says it sends the class of a cycle to the class
> of the base change of that cycle. Coherence of the direct image of a coherent module under a
> proper morphism to a locally Noetherian scheme is
> `Stacks.Chow.forall_properDirectImageIsCoherent`, the first assertion of Stacks 02O5.

```lean
theorem properChowPushforward_baseChangeChowPullback_of_baseChangeChowPullback
    [LocallyOfFiniteType sX] [IsProper f] (k : ℤ)
    (w : chowGroup B.base (f ≫ sX) k) :
    letI : IsProper (baseChangeMorphism B sX f) := isProper_baseChangeMorphism B sX f
    properChowPushforward B.baseChange (pullback.snd (f ≫ sX) B.g) (pullback.snd sX B.g)
        (baseChangeMorphism B sX f) (baseChangeMorphism_comp_snd B sX f) (k + B.c)
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper B.baseChange
          (pullback.snd (f ≫ sX) B.g) (pullback.snd sX B.g) (baseChangeMorphism B sX f)
          (baseChangeMorphism_comp_snd B sX f) (k + B.c))
        (baseChangeChowPullback B (f ≫ sX) k w) =
      baseChangeChowPullback B sX k (properChowPushforward B.base (f ≫ sX) sX f rfl k
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper B.base (f ≫ sX) sX f rfl
          k) w)
```

## Tag 0FVM, a lemma

[Tag 0FVM](https://stacks.math.columbia.edu/tag/0FVM) in the Stacks Project.

**`Stacks.Chow.baseChange_firstChernClassCapChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FirstChernClass.lean, line 562](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FirstChernClass.lean#L562).

> **[Stacks, Tag 0FVM].** In the flat base-change situation of [Stacks, Tag 0FVG] let `X` be
> locally of finite type over `S`, let `X' = X ×_S S'` be the base change by `S' ⟶ S`, and let `ℒ`
> be an invertible `𝒪_X`-module with base change `ℒ'` on `X'`. Then the square
>
>   `CH_{k+1}(X) --g^*--> CH_{k+1+c}(X')`
>   `      |c₁(ℒ) ∩ -             |c₁(ℒ') ∩ -`
>   `CH_k(X)     --g^*--> CH_{k+c}(X')`
>
> of Chow groups commutes, `g^*` being the base-change map of [Stacks, Tag 0FVJ].
>
> The cap product of [Stacks, Tag 02TI] is indexed by the degree of its value, so the top row is
> written at `k + 1`; the source states the square for every `k ∈ ℤ`, so nothing is lost. The
> transport between the two spellings `(k + 1) + c` and `(k + c) + 1` of the degree of the base
> change of the top-left corner is `Stacks.Chow.chowGroupCast`. The module `ℒ'` is
> `(D.baseChange g).L`, which is the pullback `g^*ℒ` by
> `Stacks.LineBundle.Situation.baseChange_L`.
>
> **Proof.** Let `p : Tot(ℒ) ⟶ X` be the line bundle attached to `ℒ` with zero section `o`. By
> clause (5) of [Stacks, Tag 0F96], `o_*α = -p^*(c₁(ℒ) ∩ α)`. Applying `g^*` and using
> [Stacks, Tag 0FVL] on `o` and [Stacks, Tag 0FVK] on `p` turns this into
>
>   `õ_*(g^*α) = -p̃^*(g^*(c₁(ℒ) ∩ α))`
>
> on the fibre product `Tot(ℒ) ×_S S'`, where `õ` and `p̃` are the base changes of `o` and `p`. On
> the other hand `Stacks.Chow.zeroSectionBaseChange_chowPushforward_eq_neg` — clause (5) for `ℒ'`,
> transported along `Tot(ℒ') ≅ Tot(ℒ) ×_S S'` — gives
>
>   `õ_*(g^*α) = -p̃^*(c₁(ℒ') ∩ g^*α)`.
>
> So `p̃^*` takes the same value on the two classes to be identified, and `p̃^*` is injective by
> `Stacks.Chow.injective_flatPullbackChow_totalSpaceBaseChangeMorphism`.

```lean
theorem baseChange_firstChernClassCapChow (k : ℤ) (α : chowGroup B.base sX (k + 1)) :
    firstChernClassCapChow B.baseChange (k + B.c) (pullback.snd sX B.g)
        (baseChangeSituation B D sX).L
        (chowGroupCast B.baseChange (pullback.snd sX B.g)
          (show k + 1 + B.c = k + B.c + 1 from by omega)
          (baseChangeChowPullback B sX (k + 1) α)) =
      baseChangeChowPullback B sX k (firstChernClassCapChow B.base k sX D.L α)
```

## Tag 0FVN, a lemma

[Tag 0FVN](https://stacks.math.columbia.edu/tag/0FVN) in the Stacks Project.

**`Stacks.Chow.baseChange_chowCohomologyCap_chernClassOfLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/GenuineChernClasses.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/GenuineChernClasses.lean#L307).

> **[Stacks, Tag 0FVN].** Let `g : S' ⟶ S` be a flat base change of Chow situations with
> dimension shift `c` ([Stacks, Tag 0FVG]), let `X` be locally of finite type over `S` with base
> change `X' = X ×_S S'`, and let `ℰ` be a finite locally free `𝒪_X`-module of rank `r` with base
> change `ℰ'` on `X'`. Then for every `i` the square
>
>   `CH_k(X)     --g^*--> CH_{k+c}(X')`
>   `    |c_i(ℰ) ∩ -              |c_i(ℰ') ∩ -`
>   `CH_{k-i}(X) --g^*--> CH_{k+c-i}(X')`
>
> commutes, where `c_i ∈ A^i` is the Chern class of [Stacks, Tag 0ESW], built from the classes of
> [Stacks, Tag 0B7H] (zero for `i > r`), and `g^*` is the map of [Stacks, Tag 0FVJ]. For `i ≤ r`
> the cap products are those of [Stacks, Tag 02U6] (`Stacks.Chow.baseChange_chernCap`).

```lean
theorem baseChange_chowCohomologyCap_chernClassOfLocallyFree (i : ℕ) (k : ℤ)
    (α : chowGroup B.base sX k) :
    letI := AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree E r
    haveI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (pullback.fst sX B.g) E r
    letI := AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree
      ((Scheme.Modules.pullback (pullback.fst sX B.g)).obj E) r
    chowCohomologyCap B.baseChange (gysinSystemOfInvertible B.baseChange) (pullback.snd sX B.g)
        (i : ℤ)
        (SectionZeroScheme.chernClassOfLocallyFree
          ((Scheme.Modules.pullback (pullback.fst sX B.g)).obj E) B.baseChange
          (pullback.snd sX B.g) i) (k + B.c) (baseChangeChowPullback B sX k α) =
      chowGroupCast B.baseChange (pullback.snd sX B.g)
        (show k - (i : ℤ) + B.c = k + B.c - (i : ℤ) from by omega)
        (baseChangeChowPullback B sX (k - (i : ℤ))
          (chowCohomologyCap B.base (gysinSystemOfInvertible B.base) sX (i : ℤ)
            (SectionZeroScheme.chernClassOfLocallyFree E B.base sX i) k α))
```

## Tag 0FVP, a lemma

[Tag 0FVP](https://stacks.math.columbia.edu/tag/0FVP) in the Stacks Project.

**`Stacks.Chow.composed_dimensionFunction_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean#L209). The attribute's comment: “part (1): the composite dimension shift is the sum of the two shifts”.

> **Stacks Project, Tag 0FVP, part (1).** For composable flat base changes of Chow situations
> with dimension shifts `B.c` and `c'`, every generic point `s''` of the fibre of `g' ≫ B.g` over
> `s` satisfies `δ''(s'') = δ(s) + (B.c + c')`.

```lean
theorem composed_dimensionFunction_eq_add (s : B.base.S)
    (s'' : genericPoints ((g' ≫ B.g) ⁻¹' {s} : Set C.S)) :
    C.dimensionFunction s''.1.1 = B.base.dimensionFunction s + (B.c + c')
```

**`Stacks.Chow.baseChangeCyclePullbackSquare_comp_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean#L396). The attribute's comment: “part (2): pullback on cycle groups respects composition, coefficientwise”.

> **Stacks Project, Tag 0FVP, part (2).** The pullbacks on cycle groups of two composable flat
> base changes compose to the pullback of the composite, read coefficientwise.
>
> Both composites send a cycle `z` to a multiple of the coefficient of `z` at the image point `x`
> of the given point, the factor depending only on the point. If `x` does not have relative
> dimension `k` then every `k`-cycle vanishes there and both sides are zero. Otherwise the
> fundamental cycle of the reduced closure of `x` is a `k`-cycle with coefficient one at `x`, so
> the two factors agree by
> `Stacks.Chow.comp_cycleAssociatedToClosedSubscheme_coeff`.

```lean
theorem baseChangeCyclePullbackSquare_comp_apply (k : ℤ) (z : CycleGroup B.base f k) (y : Y'') :
    (baseChangeCyclePullbackSquare (FlatBaseChangeSituation.second B C g' c' hg') q sq' (k + B.c)
        (baseChangeCyclePullbackSquare B f sq k z)).1 y =
      (baseChangeCyclePullbackSquare (FlatBaseChangeSituation.comp B C g' c' hg') f
        (sq'.paste_horiz sq) k z).1 y
```

**`Stacks.Chow.baseChangeCyclePullbackSquare_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean#L437). The attribute's comment: “part (2): pullback on cycle groups respects composition”.

> **Stacks Project, Tag 0FVP, part (2).** The pullbacks on cycle groups of two composable flat
> base changes compose to the pullback of the composite.

```lean
theorem baseChangeCyclePullbackSquare_comp (k : ℤ) :
    (baseChangeCyclePullbackSquare (FlatBaseChangeSituation.second B C g' c' hg') q sq'
          (k + B.c)).comp (baseChangeCyclePullbackSquare B f sq k) =
      ((cycleGroupCongrDegree C q'
          (show k + (B.c + c') = k + B.c + c' from (add_assoc k B.c c').symm)).toAddMonoidHom).comp
        (baseChangeCyclePullbackSquare (FlatBaseChangeSituation.comp B C g' c' hg') f
          (sq'.paste_horiz sq) k)
```

**`Stacks.Chow.baseChangeChowPullbackSquare_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FlatBaseChangeComposition.lean#L453). The attribute's comment: “part (3): pullback on Chow groups respects composition”.

> **Stacks Project, Tag 0FVP, part (3).** The pullbacks on Chow groups of two composable flat
> base changes compose to the pullback of the composite: both are induced by the corresponding
> pullbacks on cycle groups, which compose by
> `Stacks.Chow.baseChangeCyclePullbackSquare_comp`.

```lean
theorem baseChangeChowPullbackSquare_comp (k : ℤ) :
    (baseChangeChowPullbackSquare (FlatBaseChangeSituation.second B C g' c' hg') q sq'
          (k + B.c)).comp (baseChangeChowPullbackSquare B f sq k) =
      ((chowGroupCongrDegree C q'
          (show k + (B.c + c') = k + B.c + c' from (add_assoc k B.c c').symm)).toAddMonoidHom).comp
        (baseChangeChowPullbackSquare (FlatBaseChangeSituation.comp B C g' c' hg') f
          (sq'.paste_horiz sq) k)
```

## Tag 0FVQ, a lemma

[Tag 0FVQ](https://stacks.math.columbia.edu/tag/0FVQ) in the Stacks Project.

**`Stacks.Chow.FilteredBaseChangeSystem.exists_stageChowPullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitChow.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitChow.lean#L346). The attribute's comment: “Chow groups, surjectivity: every k-cycle class on X' comes from some X\_i”.

> **Stacks Project, Tag 0FVQ, surjectivity for Chow groups.** Every `k`-cycle class on `X'` is
> the image of a `k`-cycle class on `X_i` for some finite stage `i`.

```lean
theorem exists_stageChowPullback_eq (k : ℤ)
    (α : chowGroup s.limitBaseChange.baseChange
      (pullback.snd s.X.hom s.limitBaseChange.g) k) :
    ∃ (i : I) (β : chowGroup (s.stageSituation i)
      (pullback.snd s.X.hom (s.stageToBase i)) k),
      s.stageChowPullback i k β = α
```

**`Stacks.Chow.FilteredBaseChangeSystem.exists_transitionChowPullback_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitChow.lean, line 626](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitChow.lean#L626). The attribute's comment: “Chow groups, eventual injectivity: a k-cycle class on X\_j killed by base change to X' is killed by some transition X\_i -> X\_j”.

> **Stacks Project, Tag 0FVQ, eventual injectivity for Chow groups.** A `k`-cycle class on
> `X_j` whose image in `CH_k(X')` vanishes is annihilated by the comparison homomorphism along
> some transition `X_i ⟶ X_j`.

```lean
theorem exists_transitionChowPullback_eq_zero (j : I) (k : ℤ)
    (β : chowGroup (s.stageSituation j) (pullback.snd s.X.hom (s.stageToBase j)) k)
    (hβ : s.stageChowPullback j k β = 0) :
    ∃ (i : I) (f : i ⟶ j), s.transitionChowPullback f k β = 0
```

**`Stacks.Chow.FilteredBaseChangeSystem.exists_stageCyclePullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitCycles.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitCycles.lean#L374). The attribute's comment: “cycle groups, surjectivity: every k-cycle on X' is the image of a k-cycle on X\_i”.

> **Stacks Project, Tag 0FVQ, surjectivity for cycle groups.** Every `k`-cycle on `X'` is the
> image of a `k`-cycle on `X_i` for some finite stage `i`.
>
> Since `X'` is quasi-compact the cycle has finite support, so it is a finite integral combination
> of fundamental cycles of integral closed subschemes of `X'`. Each of those descends to a finite
> stage by `Stacks.Chow.FilteredBaseChangeSystem.exists_stage_cycleAssociatedToClosedSubscheme`,
> and the index category being cofiltered, one stage serves for all of them at once.

```lean
theorem exists_stageCyclePullback_eq (k : ℤ)
    (z : CycleGroup s.limitBaseChange.baseChange (pullback.snd s.X.hom s.limitBaseChange.g) k) :
    ∃ (i : I) (w : CycleGroup (s.stageSituation i) (pullback.snd s.X.hom (s.stageToBase i)) k),
      s.stageCyclePullback i k w = z
```

**`Stacks.Chow.FilteredBaseChangeSystem.exists_transitionCyclePullback_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitCycles.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitCycles.lean#L448). The attribute's comment: “cycle groups, eventual injectivity: a k-cycle on X\_j killed by base change to X' is killed by some transition X\_i -> X\_j”.

> **Stacks Project, Tag 0FVQ, eventual injectivity for cycle groups.** A `k`-cycle on `X_j`
> whose image in `Z_k(X')` vanishes is annihilated by the transition to some finite stage
> `X_i ⟶ X_j`.
>
> A point of `X_j` carrying a nonzero coefficient cannot lie in the image of `X'`: otherwise the
> base-changed cycle would have a nonzero coefficient at a generic point of the inverse image of
> the reduced closure of that point, by
> `Stacks.Chow.eq_zero_of_baseChangeCyclePullback_eq_zero_of_mem_range`. The cycle has finite
> support because `X_j` is quasi-compact, and `X'` is the limit of the `X_i` along affine
> transition morphisms, so finitely many points outside the image of `X'` are already outside the
> image of a single `X_i`; every coefficient of the transition of the cycle to that stage is a
> coefficient of the cycle at a point of that image, hence vanishes.

```lean
theorem exists_transitionCyclePullback_eq_zero (j : I) (k : ℤ)
    (z : CycleGroup (s.stageSituation j) (pullback.snd s.X.hom (s.stageToBase j)) k)
    (hz : s.stageCyclePullback j k z = 0) :
    ∃ (i : I) (f : i ⟶ j), s.transitionCyclePullback f k z = 0
```

**`Stacks.Chow.FilteredBaseChangeSystem.exists_projectiveLineStageCyclePullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitProjectiveLine.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/FilteredLimitProjectiveLine.lean#L294). The attribute's comment: “cycle groups, surjectivity for the projective line family”.

> **Stacks Project, Tag 0FVQ, surjectivity for the projective-line family.** Every `k`-cycle on
> `X' ×_{S'} 𝐏¹_{S'}` is the image of a `k`-cycle on `X_i ×_{S_i} 𝐏¹_{S_i}` for some finite stage
> `i`.

```lean
theorem exists_projectiveLineStageCyclePullback_eq (k : ℤ)
    (z : CycleGroup s.limitBaseChange.baseChange
      (pullback.fst (pullback.snd s.X.hom s.limitBaseChange.g)
        (relativeProjectiveLine s.limitBaseChange.baseChange.S ↘
          s.limitBaseChange.baseChange.S) ≫ pullback.snd s.X.hom s.limitBaseChange.g) k) :
    ∃ (i : I) (c : CycleGroup (s.stageSituation i)
      (pullback.fst (pullback.snd s.X.hom (s.stageToBase i))
        (relativeProjectiveLine (s.diagram.obj i) ↘ s.diagram.obj i) ≫
          pullback.snd s.X.hom (s.stageToBase i)) k),
      s.projectiveLineStageCyclePullback i k c = z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.67, Tag 0FVF](https://stacks.math.columbia.edu/tag/0FVF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
