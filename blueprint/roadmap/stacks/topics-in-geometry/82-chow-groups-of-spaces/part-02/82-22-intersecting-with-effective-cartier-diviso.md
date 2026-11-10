---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.refinedGysin, AlgebraicGeometry.Space.effectiveCartierIntersection, AlgebraicGeometry.Space.sectionRefinedGysin, AlgebraicGeometry.Space.sectionCartierIntersection, AlgebraicGeometry.Space.canonicalTrivialRestrictionGysin, AlgebraicGeometry.Space.canonicalTrivialRestrictionGysin_integralCycle_of_le, AlgebraicGeometry.Space.canonicalTrivialRestrictionGysin_integralCycle_of_not_le, AlgebraicGeometry.Space.gysinCycleMap_eq_canonicalTrivialRestrictionGysin
statement: formalized
proof: formalized
---

# 82.22 Intersecting with effective Cartier divisors

Section 82.22 of the Stacks Project, [Tag 0ER0](https://stacks.math.columbia.edu/tag/0ER0). 7 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ER1, a definition

[Tag 0ER1](https://stacks.math.columbia.edu/tag/0ER1) in the Stacks Project.

**`AlgebraicGeometry.Space.refinedGysin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierIntersection.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierIntersection.lean#L592). The attribute's comment: “the refined Gysin homomorphism i^* : Z_{k+1}(X) → CH_k(D) of the vanishing locus D = Z(s), parts (1)(a), (1)(b) and (2); the Chow group of D and the two component cycles [D ∩ W]_k and c_1(L|_W) ∩ [W] are explicit parameters, instantiated by Stacks 0EQ6 parts (2)-(4) (chowTarget), Stacks 0EE9 (closedSubspaceCycle) and Stacks 0EQJ (canonicalFirstChernRule)”.

> **Stacks 0ER1, parts (1) and (2).** The *refined Gysin homomorphism*
> `i^* : Z_{k+1}(X) ⟶ CH_k(E)` of the vanishing locus `E = Z(s)` of a global section `s` of an
> invertible sheaf `ℒ` on a good algebraic space `X/B`, with `i : E → X` the closed immersion.
>
> On the cycle of an integral closed subspace `W ⊆ X` of δ-dimension `k + 1` it is the class of
> `[E ∩ W]_k` when `W ⊄ E`, which is part (1)(a), and the class of `i'_*(c₁(ℒ|_W) ∩ [W])` when
> `W ⊆ E`, which is part (1)(b); see
> `AlgebraicGeometry.Space.refinedGysin_integralCycle_of_not_le` and
> `AlgebraicGeometry.Space.refinedGysin_integralCycle_of_le`.  Part (2), the extension of that
> rule over an arbitrary `(k+1)`-cycle, is `AlgebraicGeometry.Space.gysinCycleMap`, which is
> proved to land in `Z_k(E)` and to be additive.
>
> The Chow group `CH_k(E)` and the two component cycles `[E ∩ W]_k` and `c₁(ℒ|_W) ∩ [W]` are
> explicit parameters, standing in for Stacks 0EQ6 parts (2)–(4), Stacks 0EE9 and Stacks 0EQJ,
> none of which is available for algebraic spaces in this repository; see the implementation notes
> of `StacksFrontier.AlgebraicGeometry.Spaces.Chow.EffectiveCartierIntersection`.

```lean
def refinedGysin (_hL : IsInvertibleSheaf D p hp L)
    (rule : GysinComponentRule D p (vanishingLocus D p hp L s) k)
    {CH : Type w} [AddCommGroup CH]
    (chow : ChowTarget.{u, w, v} D ((vanishingLocus D p hp L s).1.ι ≫ p) hE k CH) :
    CycleGroup D p (k + 1) →+ CH
```

**`AlgebraicGeometry.Space.effectiveCartierIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierIntersection.lean, line 646](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierIntersection.lean#L646). The attribute's comment: “part (3): the operation D · α = i_* i^* α of an effective Cartier divisor D = Z(s), with the Chow group of X and the component cycles [D ∩ W]_k and c_1(L|_W) ∩ [W] taken as explicit parameters, instantiated by Stacks 0EQ6 parts (2)-(4) (chowTarget), Stacks 0EE9 (closedSubspaceCycle) and Stacks 0EQJ (canonicalFirstChernRule); the pushforward i_* is applied to the cycle-level Gysin map, the source applying it to the class”.

> **Stacks 0ER1, part (3).** Intersecting with an effective Cartier divisor: when `E = Z(s)`
> is an effective Cartier divisor on `X` one writes `E · α = i_* i^* α` for the pushforward along
> the closed immersion `i : E → X` of the refined Gysin class of `α`.
>
> The pushforward is the honest pushforward of cycles along a closed immersion,
> `AlgebraicGeometry.Space.cycleGroupClosedPushforward`, applied to the cycle-level Gysin map; the
> class map of a Chow group for `X` is applied afterwards.  The source applies `i_*` to a Chow
> class, which needs proper pushforward to respect rational equivalence; the form below is that
> statement at the level of cycles, and is the same once Stacks 0EQ6 parts (2)–(4) land.

```lean
def effectiveCartierIntersection (_hL : IsInvertibleSheaf D p hp L)
    (_hCartier : IsEffectiveCartierDivisor D.site D.base D.base_mem ⟨X, hp.1⟩
      (vanishingLocus D p hp L s))
    (rule : GysinComponentRule D p (vanishingLocus D p hp L s) k)
    {CH : Type w} [AddCommGroup CH]
    (chow : ChowTarget.{u, w, v} D p hp k CH) :
    CycleGroup D p (k + 1) →+ CH
```

**`AlgebraicGeometry.Space.sectionRefinedGysin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinOfSection.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinOfSection.lean#L249). The attribute's comment: “parts (1)(a), (1)(b) and (2): the refined Gysin homomorphism i^* : Z_{k+1}(X) → CH_k(D) of the vanishing locus D = Z(s) of a global section of an invertible sheaf, with values in CH_k(D) = Z_k(D)/∼_rat of Stacks 0EQ6, clause (1)(a) the cycle [D ∩ W]_k of Stacks 0EE9 of the scheme-theoretic intersection and clause (1)(b) the pushforward of div_{L|_W}(t_W) for the regular meromorphic section of Stacks 0EPQ, every ingredient constructed”.

> The *refined Gysin homomorphism* `i^* : Z_{k+1}(X) ⟶ CH_k(E)` of the vanishing locus
> `E = Z(s)` of a global section `s` of an invertible sheaf `ℒ` on a good algebraic space `X/B`,
> `i : E → X` the closed immersion, with values in the Chow group `CH_k(E) = Z_k(E)/∼_rat`.
>
> On the cycle `[W]` of an integral closed subspace `W ⊆ X` of δ-dimension `k + 1` it is the class
> of `[E ∩ W]_k` when `W ⊄ E` (`AlgebraicGeometry.Space.sectionRefinedGysin_integralCycle_of_not_le`)
> and the class of `i'_*(c₁(ℒ|_W) ∩ [W])` when `W ⊆ E`
> (`AlgebraicGeometry.Space.sectionRefinedGysin_integralCycle_of_le`); on a general cycle
> `α = ∑ n_W [W]` it is the class of `∑ n_W i^*[W]`
> (`AlgebraicGeometry.Space.sectionRefinedGysin_apply`).

```lean
def sectionRefinedGysin (hL : IsInvertibleSheaf D p hp L) :
    CycleGroup D p (k + 1) →+
      chowGroup.{v} D ((vanishingLocus D p hp L s).1.ι ≫ p)
        (isGood_vanishingLocus D p hp L s) k
```

**`AlgebraicGeometry.Space.sectionCartierIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinOfSection.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinOfSection.lean#L313). The attribute's comment: “part (3): the operation D · α = i_* i^* α of an effective Cartier divisor D = Z(s), with values in CH_k(X) = Z_k(X)/∼_rat of Stacks 0EQ6, i^* the refined Gysin homomorphism of parts (1) and (2) with every ingredient constructed, and i_* the pushforward along the closed immersion i : D → X of the cycle representing i^* α”.

> Intersecting with an effective Cartier divisor: when `E = Z(s)` is an effective Cartier
> divisor on `X`, the operation `E · α = i_* i^* α` with values in the Chow group `CH_k(X)`, `i_*`
> being the pushforward along the closed immersion
> `i : E → X` of the cycle `∑ n_W i^*[W]` representing `i^* α`.

```lean
def sectionCartierIntersection (hL : IsInvertibleSheaf D p hp L)
    (hCartier : IsEffectiveCartierDivisor D.site D.base D.base_mem ⟨X, hp.1⟩
      (vanishingLocus D p hp L s)) :
    CycleGroup D p (k + 1) →+ chowGroup.{v} D p hp k
```

## Tag 0ER2, a remark

[Tag 0ER2](https://stacks.math.columbia.edu/tag/0ER2) in the Stacks Project.

**`AlgebraicGeometry.Space.canonicalTrivialRestrictionGysin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean#L483). The attribute's comment: “the canonical map i^* : Z_{k+1}(X) → Z_k(D) on cycles of a pair (L, s) of Definition 0ER1 with D = Z(s), constructed with clause (1)(a) of Stacks 0ER1 given by the cycle [D ∩ W]_k of Stacks 0EE9 of the scheme-theoretic intersection D ∩ W = i^{-1}(W) and clause (1)(b) by the zero cycle, which is the requirement i^*[W] = 0 for W ⊆ D of this remark; both values are then proved of the map, in canonicalTrivialRestrictionGysin_integralCycle_of_not_le and canonicalTrivialRestrictionGysin_integralCycle_of_le, and determine it, in gysinCycleMap_eq_canonicalTrivialRestrictionGysin”.

> For a pair `(ℒ, s)` as in Stacks 0ER1, with `E = Z(s)` the vanishing locus
> of `s` and `i : E → X` its closed immersion, the canonical map `i^* : Z_{k+1}(X) ⟶ Z_k(E)` on
> cycles: the additive extension of the rule which sends the cycle of an integral closed subspace
> `W ⊆ X` of δ-dimension `k + 1` to the cycle `[E ∩ W]_k` of the scheme-theoretic intersection
> when `W ⊄ E`, as Stacks 0ER1(1)(a) prescribes, and to `0` when `W ⊆ E`, which is the requirement
> of Stacks 0ER2.

```lean
def canonicalTrivialRestrictionGysin :
    CycleGroup D p (k + 1) →+ CycleGroup D ((vanishingLocus D p hp L s).1.ι ≫ p) k
```

**`AlgebraicGeometry.Space.canonicalTrivialRestrictionGysin_integralCycle_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean#L493). The attribute's comment: “the defining requirement i^*[W] = 0 for W ⊆ D, proved of the canonical map on cycles of the pair of Definition 0ER1”.

> The defining requirement for the pair of Stacks 0ER1: the canonical map on
> cycles vanishes on the cycle of an integral closed subspace contained in `E`.

```lean
theorem canonicalTrivialRestrictionGysin_integralCycle_of_le
    {W : IntegralClosedSubspace D.site D.base D.base_mem X}
    (hW : deltaDimension D p W = k + 1)
    (hWE : W.subspace ≤ (vanishingLocus D p hp L s).1) :
    canonicalTrivialRestrictionGysin D p hp L s k (integralCycle D p (k + 1) W hW) = 0
```

**`AlgebraicGeometry.Space.canonicalTrivialRestrictionGysin_integralCycle_of_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean#L507). The attribute's comment: “the remaining value i^*[W] = [D ∩ W]_k of Stacks 0ER1(1)(a), proved of the canonical map on cycles, the right-hand side being the cycle of Stacks 0EE9 of the scheme-theoretic intersection”.

> On the cycle of an integral closed subspace not contained in `E` the canonical map is the
> cycle `[E ∩ W]_k` of Stacks 0EE9 of the scheme-theoretic intersection, as Stacks 0ER1(1)(a)
> prescribes.

```lean
theorem canonicalTrivialRestrictionGysin_integralCycle_of_not_le
    {W : IntegralClosedSubspace D.site D.base D.base_mem X}
    (hW : deltaDimension D p W = k + 1)
    (hWE : ¬ W.subspace ≤ (vanishingLocus D p hp L s).1) :
    canonicalTrivialRestrictionGysin D p hp L s k (integralCycle D p (k + 1) W hW) =
      gysinIntersectionCycle D p hp (vanishingLocus D p hp L s)
        (isGood_vanishingLocus D p hp L s) k W hW hWE
```

**`AlgebraicGeometry.Space.gysinCycleMap_eq_canonicalTrivialRestrictionGysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/TrivialRestrictionGysin.lean#L523). The attribute's comment: “canonicity of the canonical map on cycles of the pair of Definition 0ER1: the requirement i^*[W] = 0 for W ⊆ D, together with the value [D ∩ W]_k of Stacks 0ER1(1)(a) on the remaining integral closed subspaces, determines the map on cycles”.

> Canonicity for the pair of Stacks 0ER1: a component rule whose cycle map
> takes the two prescribed values on the cycle of every integral closed subspace has the canonical
> map of Stacks 0ER2 as its cycle map.

```lean
theorem gysinCycleMap_eq_canonicalTrivialRestrictionGysin
    (rule' : GysinComponentRule D p (vanishingLocus D p hp L s) k)
    (hle : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem X)
      (hW : deltaDimension D p W = k + 1), W.subspace ≤ (vanishingLocus D p hp L s).1 →
      gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k rule'
        (integralCycle D p (k + 1) W hW) = 0)
    (hnotle : ∀ (W : IntegralClosedSubspace D.site D.base D.base_mem X)
      (hW : deltaDimension D p W = k + 1)
      (hWE : ¬ W.subspace ≤ (vanishingLocus D p hp L s).1),
      gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k rule'
          (integralCycle D p (k + 1) W hW) =
        gysinIntersectionCycle D p hp (vanishingLocus D p hp L s)
          (isGood_vanishingLocus D p hp L s) k W hW hWE) :
    gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k rule' =
      canonicalTrivialRestrictionGysin D p hp L s k
```

## Tag 0ER3, a remark

[Tag 0ER3](https://stacks.math.columbia.edu/tag/0ER3) in the Stacks Project.

**`AlgebraicGeometry.Space.pullbackSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean#L77). The attribute's comment: “the sheaf L' = f^*L of the construction, as the inverse image of Stacks 03LU”.

> The inverse image `ℒ' = f^*ℒ` along `f` of a sheaf of modules `ℒ` on `X`.

```lean
abbrev pullbackSheaf : Modules.{u, u} D.site D.base D.base_mem X' hp'.1
```

**`AlgebraicGeometry.Space.pullbackGlobalSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean#L83). The attribute's comment: “the section s' = f^*s of the construction, as the inverse image of a global section along f”.

> The inverse image `s' = f^*s` along `f` of a global section `s` of `ℒ`.

```lean
abbrev pullbackGlobalSection : (pullbackSheaf D p hp p' hp' f L).sections
```

**`AlgebraicGeometry.Space.pullbackDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean#L105). The attribute's comment: “the closed subspace D' = X' ×_X D of X', taken as the inverse image of D along f in the sense of Stacks 083Q; its identification with Z(s') is AlgebraicGeometry.Space.pullbackDivisor_eq_vanishingLocus”.

> The closed subspace `E' = X' ×_X E` of `X'`: the inverse image along `f` of the vanishing
> locus `E = Z(s)`.

```lean
def pullbackDivisor : ClosedSubspaces D.site D.base D.base_mem X'
```

**`AlgebraicGeometry.Space.pullbackDivisor_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean#L119). The attribute's comment: “commutativity of the diagram, g ≫ i = i' ≫ f”.

> The diagram commutes: `g ≫ i = i' ≫ f`, for `i' : E' → X'` the inclusion of the closed
> subspace `E'` and `i : E → X` the inclusion of the vanishing locus.

```lean
theorem pullbackDivisor_comm :
    pullbackDivisorProjection D p hp p' hp' f L s ≫ (vanishingLocus D p hp L s).1.ι =
      (pullbackDivisor D p hp p' hp' f L s).1.ι ≫ f.hom
```

**`AlgebraicGeometry.Space.pullbackDivisor_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean#L128). The attribute's comment: “the identification D' = X' ×_X D, as the cartesian square with legs g : D' → D and i' : D' → X'”.

> The square with legs `g : E' → E` and `i' : E' → X'` is cartesian, which is the
> identification `E' = X' ×_X E`.

```lean
theorem pullbackDivisor_isPullback :
    IsPullback (pullbackDivisorProjection D p hp p' hp' f L s)
      (pullbackDivisor D p hp p' hp' f L s).1.ι (vanishingLocus D p hp L s).1.ι f.hom
```

**`AlgebraicGeometry.Space.pullbackDivisor_eq_vanishingLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EffectiveCartierPullback.lean#L136). The attribute's comment: “the identification D' = Z(s'), the vanishing locus of the pulled-back section”.

> The identification `E' = Z(s')`: for an invertible `ℒ`, the inverse image along `f` of the
> vanishing locus of `s` is the vanishing locus of the pulled-back section `s' = f^*s`.

```lean
theorem pullbackDivisor_eq_vanishingLocus (hL : IsInvertibleSheaf D p hp L) :
    pullbackDivisor D p hp p' hp' f L s =
      vanishingLocus D p' hp' (pullbackSheaf D p hp p' hp' f L)
        (pullbackGlobalSection D p hp p' hp' f L s)
```

## Tag 0ER4, a lemma

[Tag 0ER4](https://stacks.math.columbia.edu/tag/0ER4) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_closedSubspaceCyclePushforward_gysinCycleMap_sectionGysinRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinPushforwardCap.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinPushforwardCap.lean#L312). The attribute's comment: “i_* i^* α = c₁(L) ∩ α in CH_k(X) for every (k+1)-cycle α, for X/B good, L invertible, s a global section and i : D = Z(s) → X: i^* α is the cycle of the refined Gysin map of Stacks 0ER1 (gysinCycleMap at sectionGysinRule), i_* the pushforward of cycles along the closed immersion, c₁(L) ∩ α the cycle of Stacks 0EQJ at the canonical choices, both classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical); nothing carried”.

> **Stacks 0ER4.** In Situation 0EDT let `X/B` be good, let `ℒ` be an invertible
> `𝒪_X`-module with a global section `s`, and let `i : E → X` be the closed immersion of the
> vanishing locus `E = Z(s)`. For every `(k+1)`-cycle `α` on `X`
>
> `i_* i^* α = c₁(ℒ) ∩ α` in `CH_k(X)`.
>
> Here `i^* α` is represented by the cycle `∑ n_W i^*[W]` of the refined Gysin map of Stacks 0ER1,
> `AlgebraicGeometry.Space.gysinCycleMap` at the rule
> `AlgebraicGeometry.Space.sectionGysinRule`; `i_*` is the pushforward of cycles along the closed
> immersion; `c₁(ℒ) ∩ α` is represented by the cycle of Stacks 0EQJ,
> `AlgebraicGeometry.Space.firstChernCapCycleMap` at the canonical component rule; and both classes
> are taken in `CH_k(X)` of Stacks 0EQ6, `AlgebraicGeometry.Space.chowGroupCanonical`, whose
> rational equivalences are sums of principal divisors at the canonical embeddings of Stacks 0ENK.
> As every class of `CH_{k+1}(X)` is the class of a cycle, this is the identity of the source on
> representatives.
>
> The difference of the two sides is, by
> `AlgebraicGeometry.Space.closedSubspaceCyclePushforward_gysinCycleMap_sub_firstChernCapCycleMap`
> and `AlgebraicGeometry.Space.firstChernCapCycleMap_eq_cycleFamilySum`, the locally finite sum of
> the pushforwards of the cycles `n_W ([W ×_X Z(s)]_k - c₁(ℒ|_W) ∩ [W])` for `W ⊄ Z(s)` and
> `n_W (c₁(ℒ|_W) ∩ [W] - c₁(ℒ|_W) ∩' [W])` for all `W`, the two cap products being formed with the
> two regular meromorphic sections of `ℒ|_W` the two constructions choose. By Stacks 0EQF on `W`
> (`AlgebraicGeometry.Space.closedSubspaceCycle_preimage_vanishingLocus_eq_canonicalDivisorCycleAt`)
> each of these is an integer multiple of the difference of the Weil divisors of two regular
> meromorphic sections of `ℒ|_W`, hence a principal divisor at the canonical embeddings
> (`AlgebraicGeometry.Space.isPrincipalDivisorCycleOfGood_zsmul_canonicalDivisorCycleAt_sub`).

```lean
theorem chowClassCanonical_closedSubspaceCyclePushforward_gysinCycleMap_sectionGysinRule (k : ℤ)
    (α : CycleGroup D p (k + 1)) :
    chowClassCanonical.{max (u + 1) v} D p hp k (closedSubspaceCyclePushforward D p hp
        (vanishingLocus D p hp L s) k (gysinCycleMap D p (vanishingLocus D p hp L s)
          (isGood_vanishingLocus D p hp L s) k (sectionGysinRule D p hp L s k hL) α)) =
      chowClassCanonical.{max (u + 1) v} D p hp k (firstChernCapCycleMap D p hp k
        (canonicalFirstChernRule D p hp L
          (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _ hL) k) α)
```

**`AlgebraicGeometry.Space.chowClassCanonical_closedSubspaceCyclePushforward_gysinCycleMap_canonicalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinPushforwardCap.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RefinedGysinPushforwardCap.lean#L459). The attribute's comment: “in particular: D · α = c₁(O_X(D)) ∩ α in CH_k(X) for an effective Cartier divisor D ⊆ X, with D · α = i_* i^* α of Stacks 0ER1 part (3) formed on cycles for the pair (O_X(D), 1_D) of Stacks 0847, whose vanishing locus is D, c₁(O_X(D)) ∩ α the cycle of Stacks 0EQJ at the canonical choices, and the classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical)”.

> **Stacks 0ER4, in particular.** In Situation 0EDT let `X/B` be good and let `D ⊆ X` be an
> effective Cartier divisor, with invertible sheaf `𝒪_X(D)` and canonical section `1_D`
> (Stacks 0841), whose vanishing locus `Z(1_D)` is `D` (Stacks 0847). For every `(k+1)`-cycle `α`
> on `X`
>
> `D · α = c₁(𝒪_X(D)) ∩ α` in `CH_k(X)`,
>
> where `D · α = i_* i^* α` is the operation of Stacks 0ER1, part (3), for the pair
> `(𝒪_X(D), 1_D)`: `i^* α` is represented by the cycle of the refined Gysin map,
> `AlgebraicGeometry.Space.gysinCycleMap` at `AlgebraicGeometry.Space.sectionGysinRule`, and `i_*`
> is the pushforward of cycles along `i : Z(1_D) → X`. The cap product `c₁(𝒪_X(D)) ∩ α` is
> represented by the cycle of Stacks 0EQJ at the canonical choices, and both classes are taken in
> `CH_k(X)` of Stacks 0EQ6, `AlgebraicGeometry.Space.chowGroupCanonical`. This is
> `chowClassCanonical_closedSubspaceCyclePushforward_gysinCycleMap_sectionGysinRule` for that
> pair.

```lean
theorem chowClassCanonical_closedSubspaceCyclePushforward_gysinCycleMap_canonicalSection
    (Dv : ClosedSubspaces D.site D.base D.base_mem X)
    (hDv : IsEffectiveCartierDivisor D.site D.base D.base_mem ⟨X, hp.1⟩ Dv) (k : ℤ)
    (α : CycleGroup D p (k + 1)) :
    chowClassCanonical.{max (u + 1) v} D p hp k (closedSubspaceCyclePushforward D p hp
        (vanishingLocus D p hp
          (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv)
          (canonicalSection D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv)) k
        (gysinCycleMap D p (vanishingLocus D p hp
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv)
            (canonicalSection D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv))
          (isGood_vanishingLocus D p hp _ _) k
          (sectionGysinRule D p hp
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv)
            (canonicalSection D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv) k
            (associatedInvertibleSheaf_isInvertible D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv))
          α)) =
      chowClassCanonical.{max (u + 1) v} D p hp k (firstChernCapCycleMap D p hp k
        (canonicalFirstChernRule D p hp
          (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv)
          (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _
            (associatedInvertibleSheaf_isInvertible D.site D.base D.base_mem ⟨X, hp.1⟩ Dv hDv))
          k) α)
```

## Tag 0ER5, a lemma

[Tag 0ER5](https://stacks.math.columbia.edu/tag/0ER5) in the Stacks Project.

**`AlgebraicGeometry.Space.gysinCycleMap_properPushforward_eq_of_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinCompatibility.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinCompatibility.lean#L592). The attribute's comment: “i^*f_*α' = g_*(i')^*α' at the level of cycles, on the single carried input GysinProperPushforwardComparison: the source's prime-cycle case analysis read coefficientwise at the two component parameters of Definition 0ER1”.

> **Stacks 0ER5.** In Situation 0EDT let `f : X' ⟶ X` be a proper morphism of good algebraic
> spaces over `B`, let `(ℒ, s, i : E → X)` be as in Definition 0ER1, and form the diagram of
> Remark 0ER3, with `E' = E ×_X X'`, `g : E' ⟶ E` and `i' : E' ⟶ X'`.  Then for every
> `(k+1)`-cycle `α'` on `X'`
>
>   `i^* f_* α' = g_* (i')^* α'`,
>
> an identity of `k`-cycles on `E`, hence of classes in `CH_k(E)`.
>
> `hsq` is the cartesian square of Remark 0ER3, which makes `E'` the scheme-theoretic base change
> `E ×_X X'`.  Only quasi-compactness of `f` and of `g` is used, through Stacks 0ENZ; properness,
> which the source assumes and from which it gets `g` proper by base change, is not needed for the
> pushforwards themselves.
>
> The single hypothesis beyond the setup is `cmp`, the comparison datum
> `AlgebraicGeometry.Space.GysinProperPushforwardComparison`, whose docstring explains why it does
> not follow from the other data.  Everything else — in particular the passage from the
> prime cycles of the source's case analysis to an arbitrary cycle, which is not formal because a
> cycle is an infinite formal sum — is proved.

```lean
theorem gysinCycleMap_properPushforward_eq_of_comparison
    (cmp : GysinProperPushforwardComparison D p hp p' hp' f E hE E' hE' g k rule rule')
    (hsq : IsPullback g E'.1.ι E.1.ι f) (α' : CycleGroup D p' (k + 1)) :
    gysinCycleMap D p E hE k rule (properCyclePushforward D p' hp' p hp hfbase hfqc (k + 1) α') =
      properCyclePushforward D (E'.1.ι ≫ p') hE' (E.1.ι ≫ p) hE hgbase hgqc k
        (gysinCycleMap D p' E' hE' k rule' α')
```

**`AlgebraicGeometry.Space.sectionGysin_properPushforward_eq_chowGroupCanonicalProperPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinProperPushforwardCompatibility.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinProperPushforwardCompatibility.lean#L124). The attribute's comment: “i^* f_* α' = g_* (i')^* α' in CH_k(D) for f : X' → X proper between good algebraic spaces over B, (L, s, i : D → X) as in 0ER1 and the diagram of 0ER3 (L' = f^*L, s' = f^*s, D' = Z(s') = X' ×_X D): both Gysin maps are 0ER1's at the constructed rules sectionGysinRule, CH_k = chowGroupCanonical of 0EQ6, f_* the proper pushforward of cycles of 0EP1 and g_* the proper pushforward on Chow groups of 0EQC; unconditional”.

> In Situation 0EDT let `f : X' ⟶ X` be a proper morphism of good algebraic spaces over `B`.
> Let `(ℒ, s, i : D → X)` be as in Definition 0ER1: `ℒ` an invertible `𝒪_X`-module, `s ∈ Γ(X, ℒ)`,
> `D = Z(s)` its vanishing locus (here `E`, the letter `D` being the dimension situation) and `i`
> the closed immersion. Form the diagram of Remark 0ER3
>
> ```
> E' --i'--> X'
> |          |
> g          f
> |          |
> v          v
> E  --i-->  X
> ```
>
> with `ℒ' = f^*ℒ`, `s' = f^*s` and `E' = Z(s') = X' ×_X E`
> (`AlgebraicGeometry.Space.pullbackDivisor_eq_vanishingLocus`). Then for every `(k+1)`-cycle `α'`
> on `X'`
>
> `i^* f_* α' = g_* (i')^* α'` in `CH_k(E)`,
>
> where `i^*` and `(i')^*` are the refined Gysin homomorphisms `Z_{k+1}(·) → CH_k(·)` of
> Stacks 0ER1 of the two triples, at their constructed component rules
> (`AlgebraicGeometry.Space.sectionGysinRule`: clause (1)(a) the cycle `[E ∩ W]_k` of Stacks 0EE9,
> clause (1)(b) `c₁(ℒ|_W) ∩ [W]`), `f_*` is proper pushforward of cycles (Stacks 0EP1), the Chow
> groups are those of Stacks 0EQ6 (`AlgebraicGeometry.Space.chowGroupCanonical`, `div(f)` read at
> the canonical embeddings of Stacks 0ENK) and `g_*` is proper pushforward on Chow groups,
> Stacks 0EQC (`AlgebraicGeometry.Space.chowGroupCanonicalProperPushforward`).

```lean
theorem sectionGysin_properPushforward_eq_chowGroupCanonicalProperPushforward
    (α' : CycleGroup D p' (k + 1)) :
    chowClassCanonical.{u + 1} D ((vanishingLocus D p hp L s).1.ι ≫ p)
        (isGood_vanishingLocus D p hp L s) k
        (gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k
          (sectionGysinRule D p hp L s k hL)
          (properCyclePushforward D p' hp' p hp hfbase hf.2.1.2 (k + 1) α')) =
      chowGroupCanonicalProperPushforward.{u + 1} D
        ((pullbackSectionVanishingLocus D p hp p' hp' f L s).1.ι ≫ p')
        (isGood_vanishingLocus D p' hp' _ _)
        ((vanishingLocus D p hp L s).1.ι ≫ p) (isGood_vanishingLocus D p hp L s)
        (pullbackVanishingLocusProjection_comp_structure D p hp p' hp' f L s hL hfbase)
        (isProper_pullbackVanishingLocusProjection D p hp p' hp' f L s hL hf) k
        (chowClassCanonical.{u + 1} D
          ((pullbackSectionVanishingLocus D p hp p' hp' f L s).1.ι ≫ p')
          (isGood_vanishingLocus D p' hp' _ _) k
          (gysinCycleMap D p' (pullbackSectionVanishingLocus D p hp p' hp' f L s)
            (isGood_vanishingLocus D p' hp' _ _) k
            (sectionGysinRule D p' hp' (pullbackSheaf D p hp p' hp' f L)
              (pullbackGlobalSection D p hp p' hp' f L s) k
              (isInvertibleSheaf_pullbackSheaf D p hp p' hp' f L hL)) α'))
```

**`AlgebraicGeometry.Space.gysinCycleMap_properPushforward_eq_of_genericPointData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinProperPushforwardGenericPoints.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinProperPushforwardGenericPoints.lean#L532). The attribute's comment: “i^*f_*α' = g_*(i')^*α' in Z_k(E) at the canonical component rule, with the W' ⊄ E' branch PROVED from the generic-point dictionary (the degree count, from Stacks 02M0); only the W' ⊆ E' branch, the chern comparison of Stacks 0EQS(2), is carried”.

> **Stacks 0ER5, with the non-contained branch of the comparison proved rather than carried.**
> In Situation 0EDT let `f : X' ⟶ X` be a quasi-compact morphism of good algebraic spaces over
> `B`, let `E ⊆ X` be a closed subspace with closed immersion `i : E → X`, and form the diagram of
> Remark 0ER3, with `E'` a closed subspace of `X'` whose point set is `|f|^{-1}|E|`, sitting in a
> cartesian square with `g : E' ⟶ E` and `i' : E' ⟶ X'`.  Then for every `(k+1)`-cycle `α'` on
> `X'`
>
> `i^* f_* α' = g_* (i')^* α'`,
>
> an identity of `k`-cycles on `E`, hence of classes in `CH_k(E)`, for the refined Gysin maps of
> Stacks 0ER1 built on the canonical component rule of
> `AlgebraicGeometry.Space.canonicalGysinComponentRule`.
>
> Two things are carried.  `hdata`, the local dictionary at the generic points of the pairs with
> `W' ⊄ E'` — from which **the degree count of the source's first case is proved**, by
> `AlgebraicGeometry.Space.properCycleDegree_mul_gysinIntersectionMult_eq_finsum`.  And `hchern`,
> the source's second case, which compares the cap products of Stacks 0EQJ on `X` and on `X'`:
> clause (1)(b) of Stacks 0ER1 is the free parameter
> `AlgebraicGeometry.Space.GysinComponentRule.chernCycle`, so `chern` and `chern'` are unrelated
> data and no relation between them is derivable here.  See the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Spaces.Chow.GysinProperPushforwardGenericPoints`.

```lean
theorem gysinCycleMap_properPushforward_eq_of_genericPointData
    (hfbase : f ≫ p = p') (hfqc : IsQuasiCompact D.site D.base D.base_mem f)
    (hgbase : g ≫ (E.1.ι ≫ p) = E'.1.ι ≫ p')
    (hgqc : IsQuasiCompact D.site D.base D.base_mem g)
    (hsq : IsPullback g E'.1.ι E.1.ι f)
    (hpt : subspacePointSet D.site D.base D.base_mem X' E'.1 =
      pointsMap D.site D.base D.base_mem X' f ⁻¹'
        subspacePointSet D.site D.base D.base_mem X E.1)
    (chern : FirstChernComponentCycleRule D p k)
    (chern' : FirstChernComponentCycleRule D p' k)
    (hdata : ∀ (W' : IntegralClosedSubspace D.site D.base D.base_mem X')
        (T : IntegralClosedSubspace D.site D.base D.base_mem E.1.toFunctor),
      ¬ W'.subspace ≤ E'.1 →
        Nonempty (GysinProperPushforwardGenericPointDatum.{u, v} D p hp p' hp' f E hE E' hE' g k
            W' T))
    (hchern : ∀ (W' : IntegralClosedSubspace D.site D.base D.base_mem X'),
      deltaDimension D p' W' = k + 1 → W'.subspace ≤ E'.1 →
      ∀ T : IntegralClosedSubspace D.site D.base D.base_mem E.1.toFunctor,
        (∑ᶠ W : IntegralClosedSubspace D.site D.base D.base_mem X,
            properCycleMult D p' hp' p hp f W' W *
              (gysinComponentCycle D p E hE k
                (canonicalGysinComponentRule D p hp E hE k chern) W).1 T) =
          ∑ᶠ T' : IntegralClosedSubspace D.site D.base D.base_mem E'.1.toFunctor,
            (gysinComponentCycle D p' E' hE' k
                (canonicalGysinComponentRule D p' hp' E' hE' k chern') W').1 T' *
              properCycleMult D (E'.1.ι ≫ p') hE' (E.1.ι ≫ p) hE g T' T)
    (α' : CycleGroup D p' (k + 1)) :
    gysinCycleMap D p E hE k (canonicalGysinComponentRule D p hp E hE k chern)
        (properCyclePushforward D p' hp' p hp hfbase hfqc (k + 1) α') =
      properCyclePushforward D (E'.1.ι ≫ p') hE' (E.1.ι ≫ p) hE hgbase hgqc k
        (gysinCycleMap D p' E' hE' k
          (canonicalGysinComponentRule D p' hp' E' hE' k chern') α')
```

## Tag 0ER6, a lemma

[Tag 0ER6](https://stacks.math.columbia.edu/tag/0ER6) in the Stacks Project.

**`AlgebraicGeometry.Space.gysinCycleMap_flatPullbackMap_eq_of_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinCompatibility.lean, line 950](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinCompatibility.lean#L950). The attribute's comment: “(i')^*f^*α = g^*i^*α at the level of cycles, on the single carried input GysinFlatPullbackComparison: the source's prime-cycle case analysis read coefficientwise at the two component parameters of Definition 0ER1”.

> **Stacks 0ER6.** In Situation 0EDT let `f : X' ⟶ X` be a flat morphism of relative dimension
> `r` of good algebraic spaces over `B`, let `(ℒ, s, i : E → X)` be as in Definition 0ER1, and form
> the diagram of Remark 0ER3, with `E' = E ×_X X'`, `g : E' ⟶ E` and `i' : E' ⟶ X'`.  Then for every
> `(k+1)`-cycle `α` on `X`
>
>   `(i')^* f^* α = g^* i^* α`,
>
> an identity of `(k+r)`-cycles on `E'`, hence of classes in `CH_{k+r}(E')`.
>
> `hsq` is the cartesian square of Remark 0ER3, which makes `E'` the scheme-theoretic base change
> `E ×_X X'`.  Flatness of `g` and its relative dimension `r` are hypotheses: the source gets them
> from `f` by base change along `i`.
> `hkr` is the degree bookkeeping `(k+1) + r = (k+r) + 1`, which is the convention of
> `AlgebraicGeometry.Space.flatPullbackMap`.
>
> The single hypothesis beyond the setup is `cmp`, the comparison datum
> `AlgebraicGeometry.Space.GysinFlatPullbackComparison`, whose docstring explains why it does not
> follow from the other data.  Everything else — in particular the passage from the
> prime cycles of the source's case analysis to an arbitrary cycle, which is not formal because a
> cycle is an infinite formal sum — is proved.

```lean
theorem gysinCycleMap_flatPullbackMap_eq_of_comparison
    (hkr : k + 1 + (r : ℤ) = k + (r : ℤ) + 1)
    (cmp : GysinFlatPullbackComparison D p hp p' hp' f hfbase r hflat hr E hE E' hE' g hgbase
      hgflat hgr k rule rule')
    (hsq : IsPullback g E'.1.ι E.1.ι f) (α : CycleGroup D p (k + 1)) :
    gysinCycleMap D p' E' hE' (k + (r : ℤ)) rule'
        (flatPullbackMap D p' hp' p hp f hfbase r hflat hr (k + 1) (k + (r : ℤ) + 1)
          hkr α) =
      flatPullbackMap D (E'.1.ι ≫ p') hE' (E.1.ι ≫ p) hE g hgbase r hgflat hgr k
        (k + (r : ℤ)) rfl (gysinCycleMap D p E hE k rule α)
```

**`AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_flatPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinFlatPullbackCanonical.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinFlatPullbackCanonical.lean#L130). The attribute's comment: “(i')^* f^* α = g^* i^* α in CH_{k+r}(D') for f : X' → X flat of relative dimension r between good spaces over B, (L, s, i : D → X) as in 0ER1 and D' = Z(f^*s) = X' ×_X D as in 0ER3 (g : D' → D flat of relative dimension r by base change); the Gysin maps of 0ER1 at their constructed rules (sectionGysinRule), the flat pullbacks of cycles of 0EP8, CH = chowGroupCanonical of 0EQ6. Unconditional: the case W ⊄ D is 0EQQ for f^{-1}(W) → W (an identity of cycles), the case W ⊆ D is 0EQR at one integral closed subspace, reassembled by 0EQ8”.

> **Stacks 0ER6.**  In Situation 0EDT let `f : X' ⟶ X` be a morphism over `B` of good algebraic
> spaces which is flat of relative dimension `r`, let `(ℒ, s, i : E → X)` be as in Definition 0ER1
> (`ℒ` invertible, `s ∈ Γ(X, ℒ)`, `E = Z(s)`), and form the diagram of Remark 0ER3: `ℒ' = f^*ℒ`,
> `s' = f^*s`, `E' = Z(s') = X' ×_X E` with `i' : E' → X'` and the projection `g : E' ⟶ E`, which is
> flat of relative dimension `r`.  Then for every `(k + 1)`-cycle `α` on `X`
>
> `(i')^* f^* α = g^* i^* α`   in `CH_{k+r}(E')`.
>
> Here `i^*`, `(i')^*` are the Gysin maps on cycles of Stacks 0ER1 at their constructed component
> rules, `f^*`, `g^*` the flat pullbacks of cycles of Stacks 0EP8, and `CH_{k+r}(E')` the Chow
> group of Stacks 0EQ6 (`div(f_j)` at the canonical embeddings of Stacks 0ENK).

```lean
theorem chowClassCanonical_gysinCycleMap_flatPullbackMap (α : CycleGroup D p (k + 1)) :
    chowClassCanonical.{u + 1} D ((pullbackSectionVanishingLocus D p hp p' hp' f L s).1.ι ≫ p')
        (isGood_vanishingLocus D p' hp' _ _) (k + (r : ℤ))
        (gysinCycleMap D p' (pullbackSectionVanishingLocus D p hp p' hp' f L s)
          (isGood_vanishingLocus D p' hp' _ _) (k + (r : ℤ))
          (sectionGysinRule D p' hp' (pullbackSheaf D p hp p' hp' f L)
            (pullbackGlobalSection D p hp p' hp' f L s) (k + (r : ℤ))
            (isInvertibleSheaf_pullbackSheaf D p hp p' hp' f L hL))
          (flatPullbackMap D p' hp' p hp f.hom hfbase r hflat hr (k + 1) (k + (r : ℤ) + 1)
            (by ring) α)) =
      chowClassCanonical.{u + 1} D ((pullbackSectionVanishingLocus D p hp p' hp' f L s).1.ι ≫ p')
        (isGood_vanishingLocus D p' hp' _ _) (k + (r : ℤ))
        (flatPullbackMap D ((pullbackSectionVanishingLocus D p hp p' hp' f L s).1.ι ≫ p')
          (isGood_vanishingLocus D p' hp' _ _) ((vanishingLocus D p hp L s).1.ι ≫ p)
          (isGood_vanishingLocus D p hp L s)
          (pullbackVanishingLocusProjection D p hp p' hp' f L s hL)
          (pullbackVanishingLocusProjection_comp_structure D p hp p' hp' f L s hL hfbase) r
          (isFlat_and_hasRelativeDimension_pullbackVanishingLocusProjection D p hp p' hp' f L s
            hfbase r hflat hr hL).1
          (isFlat_and_hasRelativeDimension_pullbackVanishingLocusProjection D p hp p' hp' f L s
            hfbase r hflat hr hL).2 k (k + (r : ℤ)) rfl
          (gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k
            (sectionGysinRule D p hp L s k hL) α))
```

## Tag 0ER7, a lemma

[Tag 0ER7](https://stacks.math.columbia.edu/tag/0ER7) in the Stacks Project.

**`AlgebraicGeometry.Space.gysinCycleMap_closedSubspaceCycle_coe_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinClosedSubspaceIntersectionAdditivity.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinClosedSubspaceIntersectionAdditivity.lean#L661). The attribute's comment: “i^*([Z]_{k+1}) = [D ∩ Z]_k for a closed subspace Z with dim_δ(Z) ≤ k+1 whose intersection with D is an effective Cartier divisor on Z, stated coefficientwise on the integral closed subspaces of D so that no δ-dimension bound on D ∩ Z is needed; the Gysin map is the one of Stacks 0ER1 at canonicalGysinComponentRule, so clause (1)(a) is the cycle [D ∩ W]_k of Stacks 0EE9 and only clause (1)(b), the cap product of Stacks 0EQJ, is the free parameter chern that Definition 0ER1 takes it to be here; Stacks 0EQL for (Z, s|_Z) and the non-containment of the components of Z in D are proved, not assumed”.

> **Stacks 0ER7.**  In Situation 0EDT let `X/B` be good and let `(ℒ, s, i : E → X)` be a triple
> as in Definition 0ER1: `ℒ` invertible, `s` a global section of it and `E = Z(s)` its vanishing
> locus.  Let `Z ⊆ X` be a closed subspace with `dim_δ(Z) ≤ k + 1` whose intersection `E ∩ Z` is an
> effective Cartier divisor on `Z`.  Then
>
>   `i^*([Z]_{k + 1}) = [E ∩ Z]_k`.
>
> The left-hand side is the refined Gysin map of Stacks 0ER1 at the component rule
> `AlgebraicGeometry.Space.canonicalGysinComponentRule`, so clause (1)(a) is the cycle
> `[E ∩ W]_k` of Stacks 0EE9 that the source means and only clause (1)(b) — the cap product
> `c₁(ℒ|_W) ∩ [W]` of Stacks 0EQJ — is the free parameter `chern` that Definition 0ER1 takes it to
> be in this library.  The cycle `[Z]_{k+1}` is `AlgebraicGeometry.Space.closedSubspaceCycle`, which
> is Stacks 0EE9 as an element of `Z_{k+1}(X)`, and the identity is stated coefficientwise so that
> `[E ∩ Z]_k` needs no δ-dimension bound of its own: both sides are coefficient families on the
> integral closed subspaces of `E`.
>
> **Nothing of the source's proof is assumed.**  The first two sentences — that the hypothesis is
> the regularity of `s|_Z` and that therefore `E ∩ Z = Z(s|_Z)` — are
> `AlgebraicGeometry.Space.isEffectiveCartierDivisor_interOnClosedSubspace_iff_isRegularSection` and
> `AlgebraicGeometry.Space.interOnClosedSubspace_eq_zeroScheme`; Lemma 0EQL for `(Z, ℒ|_Z, s|_Z)` is
> `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_zeroScheme_eq_componentZeroCycleSumCoeff`,
> transported to the ambient `X` by
> `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_interOnVanishingLocus_eq_finsum`; the
> non-containment `Z_i ⊄ E` is
> `AlgebraicGeometry.Space.not_le_vanishingLocus_of_cycleCoeffOfClosedSubspace_ne_zero`; and the
> final matching against the definition of the Gysin map is
> `AlgebraicGeometry.Space.gysinComponentCycle_of_not_le`.

```lean
theorem gysinCycleMap_closedSubspaceCycle_coe_eq
    (hL : IsInvertibleSheaf D p hp L)
    (chern : FirstChernComponentCycleRule D p k)
    (hZdim : deltaDimensionSubspace D p hp Z.1 Z.2 ≤ ((k + 1 : ℤ) : EInt))
    (hCartier : IsEffectiveCartierDivisor D.site D.base D.base_mem ⟨Z.1.toFunctor, Z.2.1⟩
      (interOnClosedSubspace D p hp L s Z)) :
    (gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k
        (canonicalGysinComponentRule D p hp (vanishingLocus D p hp L s)
          (isGood_vanishingLocus D p hp L s) k chern)
        (closedSubspaceCycle D p hp Z.1 Z.2 (k + 1) hZdim)).1 =
      cycleCoeffOfClosedSubspace D ((vanishingLocus D p hp L s).1.ι ≫ p)
        (isGood_vanishingLocus D p hp L s)
        (interOnVanishingLocus D p hp L s Z).1 (interOnVanishingLocus D p hp L s Z).2 k
        (canonicalGeometricPoint D.site D.base D.base_mem
          (interOnVanishingLocus D p hp L s Z).1.toFunctor)
```

**`AlgebraicGeometry.Space.gysinCycleMap_canonical_eq_of_cycleCoeffOfClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinClosedSubspaceIntersectionAdditivity.lean, line 715](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/GysinClosedSubspaceIntersectionAdditivity.lean#L715). The attribute's comment: “i^*([Z]_{k+1}) = [D ∩ Z]_k as an equality in Z_k(D), for a closed subspace Z with dim_δ(Z) ≤ k+1 whose intersection with D is an effective Cartier divisor on Z; the Gysin map is the one of Stacks 0ER1 at canonicalGysinComponentRule, so clause (1)(a) is the cycle [D ∩ W]_k of Stacks 0EE9 and only clause (1)(b), the cap product of Stacks 0EQJ, is the free parameter chern that Definition 0ER1 takes it to be here; the two cycles are elements α and β of the cycle groups whose coefficient families hα and hβ pin to Stacks 0EE9, which replaces the δ-dimension bound on D ∩ Z; Stacks 0EQL for (Z, s|_Z) and the non-containment of the components of Z in D are proved, not assumed”.

> **Stacks 0ER7, as an equality of cycles.**  In Situation 0EDT let `X/B` be good and let
> `(ℒ, s, i : E → X)` be a triple as in Definition 0ER1.  Let `Z ⊆ X` be a closed subspace with
> `dim_δ(Z) ≤ k + 1` whose intersection `E ∩ Z` is an effective Cartier divisor on `Z`.  Then
>
>   `i^*([Z]_{k + 1}) = [E ∩ Z]_k`
>
> in `Z_k(E)`, for the refined Gysin map of Stacks 0ER1 at the component rule
> `AlgebraicGeometry.Space.canonicalGysinComponentRule`.
>
> This is `AlgebraicGeometry.Space.gysinCycleMap_closedSubspaceCycle_coe_eq` read as an equality of
> cycles rather than of coefficient families.  The two cycles are the elements `α` of `Z_{k+1}(X)`
> and `β` of `Z_k(E)` whose coefficient families `hα` and `hβ` pin to those of Stacks 0EE9 — on the
> left `[Z]_{k+1}`, on the right `[E ∩ Z]_k` for the intersection read inside `E`.  For the left
> one that is no restriction, `α` being forced to be
> `AlgebraicGeometry.Space.closedSubspaceCycle`; supplying the right one takes the place of the
> bound `dim_δ(E ∩ Z) ≤ k`, which the source gets from the effective Cartier hypothesis and which
> has no declaration in this library.  Nothing weakens: both are the coefficient families the
> source's two cycles have.
>
> This is the shape in which
> `AlgebraicGeometry.Space.gysinCycleMap_eq_of_cycleCoeffOfClosedSubspace` states the identity at an
> arbitrary component rule, where clause 0ER1(1)(a) is free data; here the rule is the canonical one
> of Stacks 0ER1, so that clause is the cycle `[E ∩ W]_k` of Stacks 0EE9 and the two inputs that
> lemma takes for it — Stacks 0EQL for `(Z, ℒ|_Z, s|_Z)` and the non-containment `Z_i ⊄ E` — are
> `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_interOnVanishingLocus_eq_finsum` and
> `AlgebraicGeometry.Space.not_le_vanishingLocus_of_cycleCoeffOfClosedSubspace_ne_zero`.

```lean
theorem gysinCycleMap_canonical_eq_of_cycleCoeffOfClosedSubspace
    (hL : IsInvertibleSheaf D p hp L)
    (chern : FirstChernComponentCycleRule D p k)
    (hZdim : deltaDimensionSubspace D p hp Z.1 Z.2 ≤ ((k + 1 : ℤ) : EInt))
    (hCartier : IsEffectiveCartierDivisor D.site D.base D.base_mem ⟨Z.1.toFunctor, Z.2.1⟩
      (interOnClosedSubspace D p hp L s Z))
    (α : CycleGroup D p (k + 1))
    (hα : α.1 = cycleCoeffOfClosedSubspace D p hp Z.1 Z.2 (k + 1)
      (canonicalGeometricPoint D.site D.base D.base_mem Z.1.toFunctor))
    (β : CycleGroup D ((vanishingLocus D p hp L s).1.ι ≫ p) k)
    (hβ : β.1 = cycleCoeffOfClosedSubspace D ((vanishingLocus D p hp L s).1.ι ≫ p)
      (isGood_vanishingLocus D p hp L s)
      (interOnVanishingLocus D p hp L s Z).1 (interOnVanishingLocus D p hp L s Z).2 k
      (canonicalGeometricPoint D.site D.base D.base_mem
        (interOnVanishingLocus D p hp L s Z).1.toFunctor)) :
    gysinCycleMap D p (vanishingLocus D p hp L s) (isGood_vanishingLocus D p hp L s) k
        (canonicalGysinComponentRule D p hp (vanishingLocus D p hp L s)
          (isGood_vanishingLocus D p hp L s) k chern) α = β
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.22, Tag 0ER0](https://stacks.math.columbia.edu/tag/0ER0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
