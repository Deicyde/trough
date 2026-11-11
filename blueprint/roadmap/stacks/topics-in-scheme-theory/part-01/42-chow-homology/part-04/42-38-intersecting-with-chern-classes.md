---
declaration: section
origin: cited
lean: Stacks.Chow.GenuineChern.chernCapOnCycles, Stacks.Chow.GenuineChern.chernCapOnCycles_integral_cycle, Stacks.Chow.GenuineChern.chernCapOnCycles_finsum, Stacks.Chow.GenuineChern.chernCapOnCycles_locallyFiniteSum, Stacks.Chow.exists_isChernCapFamily, Stacks.Chow.existsUnique_isChernCapFamily, Stacks.Chow.eq_of_isChernCapFamily, Stacks.Chow.GenuineChern.isChernCapFamilyOfRank_chernCapOnCycles
statement: formalized
proof: formalized
---

# 42.38 Intersecting with Chern classes

Section 42.38 of the Stacks Project, [Tag 02U4](https://stacks.math.columbia.edu/tag/02U4). 11 tags here are carried by 68 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02U5, a definition

[Tag 02U5](https://stacks.math.columbia.edu/tag/02U5) in the Stacks Project.

**`Stacks.Chow.GenuineChern.chernCapOnCycles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCycles.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCycles.lean#L100). The attribute's comment: “the operation”.

> **Stacks 02U5.** Intersection with the `j`-th Chern class of a finite locally free module of
> rank `r`, `c_j(ℰ) ∩ - : Z_k(X) ⟶ A_{k-j}(X)`, for the Chern classes of Stacks 02U0: the
> coefficientwise extension of `[W] ↦ i_*(c_j(i^*ℰ) ∩ [W])`.

```lean
def chernCapOnCycles (k : ℤ) (j : Fin (r + 1)) :
    CycleGroup C sX k →+ chowGroup C sX (k - (j : ℤ))
```

**`Stacks.Chow.GenuineChern.chernCapOnCycles_integral_cycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCycles.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCycles.lean#L109). The attribute's comment: “clause (1)”.

> **Stacks 02U5, clause (1)**, on Chow groups: for an integral closed subscheme
> `i : W ⟶ X` of delta-dimension `k`, `c_j(ℰ) ∩ [W] = i_*(c_j(i^*ℰ) ∩ [W])`, with the class
> `c_j(i^*ℰ) ∩ [W]` of Stacks 02U0.

```lean
theorem chernCapOnCycles_integral_cycle (k : ℤ) (j : Fin (r + 1)) (W : X.IdealSheafData)
    (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ sX) = (k : EInt)) :
    chernCapOnCycles C sX E r k j (cycleAssociatedToClosedSubscheme C sX W.subschemeι k) =
      haveI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback W.subschemeι E r
      properChowPushforward C (W.subschemeι ≫ sX) sX W.subschemeι rfl (k - (j : ℤ))
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ sX _ rfl _)
        (chernClassFundamentalOfRank ((Scheme.Modules.pullback W.subschemeι).obj E) r C
          (W.subschemeι ≫ sX) k j)
```

**`Stacks.Chow.GenuineChern.chernCapOnCycles_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCycles.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCycles.lean#L128). The attribute's comment: “clause (2)”.

> **Stacks 02U5, clause (2)**, at the level of cycles: on a locally finite presentation
> `α = ∑ n_t [W_t]` by integral closed subschemes of delta-dimension `k`, `c_j(ℰ) ∩ α` is the class
> of `∑ n_t i_{t,*}(c_j(i_t^*ℰ) ∩ [W_t])`, for representatives of the classes of Stacks 02U0.

```lean
theorem chernCapOnCycles_finsum (k : ℤ) (j : Fin (r + 1)) {J : Type u}
    (W : J → X.IdealSheafData) (hW : ∀ t, IsIntegral (W t).subscheme)
    (hDim : ∀ t, schemeDeltaDimension C ((W t).subschemeι ≫ sX) = (k : EInt))
    (hLocal : LocallyFinite fun t ↦ ((W t).support : Set X)) (n : J → ℤ)
    (α : CycleGroup C sX k)
    (hα : ∀ x : X, α.1 x = ∑ᶠ t : J, n t *
      (cycleAssociatedToClosedSubscheme C sX (W t).subschemeι k).1 x) :
    ∃ β : CycleGroup C sX (k - (j : ℤ)),
      chernCapOnCycles C sX E r k j α = QuotientAddGroup.mk β ∧
      ∀ x : X, β.1 x = ∑ᶠ t : J, n t *
        (chernClassComponentCycle C sX E r
          (fun g ↦ AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback g E r) k j
          (chernCycleRule C r) (W t) (hW t) (hDim t)).1 x
```

**`Stacks.Chow.GenuineChern.chernCapOnCycles_locallyFiniteSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesLocallyFiniteSum.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesLocallyFiniteSum.lean#L137). The attribute's comment: “clause (2)”.

> **Stacks 02U5, clause (2).** Let `α = ∑ n_t [W_t]` be a `k`-cycle, presented by a locally
> finite family of integral closed subschemes `i_t : W_t ⟶ X` of delta-dimension `k`, and let
> `γ_t` be any cycle on `W_t` representing `c_j(i_t^*ℰ) ∩ [W_t]`, the class of Stacks 02U0. Then
>
> 1. `i_{t,*} γ_t` represents `c_j(ℰ) ∩ [W_t]` for every `t`;
> 2. the locally finite sum `∑ n_t i_{t,*} γ_t` is a cycle on `X`;
> 3. every cycle `β` with these coefficients represents `c_j(ℰ) ∩ α`;
>
> that is, `c_j(ℰ) ∩ α = ∑ n_t c_j(ℰ) ∩ [W_t]`, independently of the representatives.

```lean
theorem chernCapOnCycles_locallyFiniteSum (k : ℤ) (j : Fin (r + 1)) {J : Type u}
    (W : J → X.IdealSheafData) (hW : ∀ t, IsIntegral (W t).subscheme)
    (hDim : ∀ t, schemeDeltaDimension C ((W t).subschemeι ≫ sX) = (k : EInt))
    (hLocal : LocallyFinite fun t ↦ ((W t).support : Set X)) (n : J → ℤ)
    (α : CycleGroup C sX k)
    (hα : ∀ x : X, α.1 x = ∑ᶠ t : J, n t *
      (cycleAssociatedToClosedSubscheme C sX (W t).subschemeι k).1 x)
    (γ : ∀ t, CycleGroup C ((W t).subschemeι ≫ sX) (k - (j : ℤ)))
    (hγ : ∀ t, haveI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback (W t).subschemeι E r
      QuotientAddGroup.mk' (rationalEquivalences C ((W t).subschemeι ≫ sX) (k - (j : ℤ))) (γ t) =
        chernClassFundamentalOfRank ((Scheme.Modules.pullback (W t).subschemeι).obj E) r C
          ((W t).subschemeι ≫ sX) k j) :
    (∀ t, QuotientAddGroup.mk' (rationalEquivalences C sX (k - (j : ℤ)))
        (properPushforward C ((W t).subschemeι ≫ sX) sX (W t).subschemeι rfl (k - (j : ℤ))
          (γ t)) =
      chernCapOnCycles C sX E r k j (cycleAssociatedToClosedSubscheme C sX (W t).subschemeι k)) ∧
    (∃ β : CycleGroup C sX (k - (j : ℤ)), ∀ x : X, β.1 x = ∑ᶠ t : J, n t *
      (properPushforward C ((W t).subschemeι ≫ sX) sX (W t).subschemeι rfl (k - (j : ℤ))
        (γ t)).1 x) ∧
    ∀ β : CycleGroup C sX (k - (j : ℤ)), (∀ x : X, β.1 x = ∑ᶠ t : J, n t *
      (properPushforward C ((W t).subschemeι ≫ sX) sX (W t).subschemeι rfl (k - (j : ℤ))
        (γ t)).1 x) →
      chernCapOnCycles C sX E r k j α = QuotientAddGroup.mk β
```

## Tag 02U6, a lemma

[Tag 02U6](https://stacks.math.columbia.edu/tag/02U6) in the Stacks Project.

**`Stacks.Chow.exists_isChernCapFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleExistence.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleExistence.lean#L157). The attribute's comment: “existence; carries the projective bundle as a flat morphism of relative dimension r - 1 with a first Chern class cap operator for its twist (Stacks 01O4, 02SO, 02TI), Stacks 02S1 for its projection, and the surjectivity half of Stacks 02TX”.

> Granted the surjectivity of the projective space bundle map of Stacks 02TX, every class
> `α ∈ A_k(X)` has a family of Chern class cap products: classes `α_j ∈ A_{k-j}(X)` with `α_0 = α`
> satisfying the projective-bundle relation.

```lean
theorem exists_isChernCapFamily
    (hsurj : ProjectiveBundleRelationSurjective C sX sP π hsP r hπ hfac twist) (k : ℤ)
    (α : chowGroup C sX k) :
    ∃ c : ∀ j : Fin (r + 1), chowGroup C sX (k - (j : ℤ)),
      IsChernCapFamily C sX sP π hsP r hπ hfac twist k α c
```

**`Stacks.Chow.existsUnique_isChernCapFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleExistence.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleExistence.lean#L183). The attribute's comment: “existence and uniqueness together; carries the projective bundle as a flat morphism of relative dimension r - 1 with a first Chern class cap operator for its twist (Stacks 01O4, 02SO, 02TI), Stacks 02S1 for its projection, and both halves of Stacks 02TX”.

> Granted both halves of Stacks 02TX, a class `α ∈ A_k(X)` has exactly one family of Chern class
> cap products.

```lean
theorem existsUnique_isChernCapFamily
    (hinj : ProjectiveBundleRelationInjective C sX sP π hsP r hπ hfac twist)
    (hsurj : ProjectiveBundleRelationSurjective C sX sP π hsP r hπ hfac twist) (k : ℤ)
    (α : chowGroup C sX k) :
    ∃! c : ∀ j : Fin (r + 1), chowGroup C sX (k - (j : ℤ)),
      IsChernCapFamily C sX sP π hsP r hπ hfac twist k α c
```

**`Stacks.Chow.eq_of_isChernCapFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleRelation.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleRelation.lean#L356). The attribute's comment: “uniqueness; carries the projective bundle as a flat morphism of relative dimension r - 1 with a first Chern class cap operator for its twist (Stacks 01O4, 02SO, 02TI), Stacks 02S1 for its projection, and the injectivity half of Stacks 02TX”.

> **Stacks 02U6, uniqueness.** Granted the injectivity of the projective space bundle map of
> Stacks 02TX, there is at most one family of Chern class cap products of a given class: the
> relation together with the value in degree `k` determines every member.
>
> This is the engine of the section: Stacks 02U7, 02U8, 02U9 and 0B7G are each proved by
> transporting the relation along an operation and appealing to this uniqueness.

```lean
theorem eq_of_isChernCapFamily (hinj : ProjectiveBundleRelationInjective C sX sP π hsP r hπ hfac
      twist) (k : ℤ) (α : chowGroup C sX k)
    {c d : ∀ j : Fin (r + 1), chowGroup C sX (k - (j : ℤ))}
    (hc : IsChernCapFamily C sX sP π hsP r hπ hfac twist k α c)
    (hd : IsChernCapFamily C sX sP π hsP r hπ hfac twist k α d) : c = d
```

**`Stacks.Chow.GenuineChern.isChernCapFamilyOfRank_chernCapOnCycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesCharacterization.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesCharacterization.lean#L74).

> **Stacks 02U6.** Let `ℰ` be finite locally free of rank `r` on `X`, with projective bundle
> `(π : 𝐏(ℰ) ⟶ X, 𝒪_{𝐏(ℰ)}(1))`, and let `α` be a `k`-cycle on `X`. The classes
> `c_j(ℰ) ∩ α ∈ A_{k-j}(X)` of Stacks 02U5 satisfy `α_0 = [α]` and
> `∑_{i=0}^{r} (-1)^i c₁(𝒪_{𝐏(ℰ)}(1))^i ∩ π^*(α_{r-i}) = 0` in the Chow group of `𝐏(ℰ)`, and they
> are the only family `(α_j)_{0 ≤ j ≤ r}`, `α_j ∈ A_{k-j}(X)`, doing so.

```lean
theorem isChernCapFamilyOfRank_chernCapOnCycles (k : ℤ) (α : CycleGroup C sX k) :
    IsChernCapFamilyOfRank E r C sX k (QuotientAddGroup.mk' (rationalEquivalences C sX k) α)
        (fun j ↦ chernCapOnCycles C sX E r k j α) ∧
      ∀ c : ∀ j : Fin (r + 1), chowGroup C sX (k - (j : ℤ)),
        IsChernCapFamilyOfRank E r C sX k (QuotientAddGroup.mk' (rationalEquivalences C sX k) α)
          c → c = fun j ↦ chernCapOnCycles C sX E r k j α
```

## Tag 02U7, a lemma

[Tag 02U7](https://stacks.math.columbia.edu/tag/02U7) in the Stacks Project.

**`Stacks.Chow.isChernCapFamily_rationallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleRelation.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleRelation.lean#L391). The attribute's comment: “carries the projective bundle as a flat morphism of relative dimension r - 1 with a first Chern class cap operator for its twist (Stacks 01O4, 02SO, 02TI), Stacks 02S1 for its projection, the injectivity half of Stacks 02TX, and the cap products of Stacks 02U5 as families satisfying the characterization of Stacks 02U6”.

> **Stacks 02U7.** If `α` and `β` are rationally equivalent `k`-cycles on `X`, then the Chern
> class cap products of `α` and of `β` agree: `c_j(ℰ) ∩ α = c_j(ℰ) ∩ β` in `A_{k-j}(X)`.
>
> The Stacks proof is exactly this: the two families are determined by the *same* equation in the
> Chow group of the projective bundle, which relies on flat pullback being compatible with rational
> equivalence, Stacks 02S1 — here the hypothesis `hfac` that produces the flat pullback of Stacks
> 0FVK in the first place.

```lean
theorem isChernCapFamily_rationallyEquivalent
    (hinj : ProjectiveBundleRelationInjective C sX sP π hsP r hπ hfac twist) (k : ℤ)
    (α β : CycleGroup C sX k) (hαβ : RationallyEquivalent C sX k α β)
    {c d : ∀ j : Fin (r + 1), chowGroup C sX (k - (j : ℤ))}
    (hc : IsChernCapFamily C sX sP π hsP r hπ hfac twist k
      (QuotientAddGroup.mk' (rationalEquivalences C sX k) α) c)
    (hd : IsChernCapFamily C sX sP π hsP r hπ hfac twist k
      (QuotientAddGroup.mk' (rationalEquivalences C sX k) β) d) : c = d
```

**`Stacks.Chow.GenuineChern.chernCapOnCycles_eq_of_rationallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesDescent.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesDescent.lean#L390).

> **Stacks 02U7.** Rationally equivalent `k`-cycles have the same cap products with the Chern
> classes: the operation of Stacks 02U5 factors through `A_k(X)`.

```lean
theorem chernCapOnCycles_eq_of_rationallyEquivalent (k : ℤ) (j : Fin (r + 1))
    (α β : CycleGroup C sX k) (h : RationallyEquivalent C sX k α β) :
    chernCapOnCycles C sX E r k j α = chernCapOnCycles C sX E r k j β
```

## Tag 02U9, a lemma

[Tag 02U9](https://stacks.math.columbia.edu/tag/02U9) in the Stacks Project.

**`Stacks.Chow.isChernCapFamily_properPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleProperPushforward.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleProperPushforward.lean#L214). The attribute's comment: “carries both projective bundles as flat morphisms of relative dimension r - 1 with first Chern class cap operators for their twists (Stacks 01O4, 02SO, 02TI), Stacks 02S1 for their projections, a proper morphism between the two bundles lying over p, the injectivity half of Stacks 02TX over the target, the compatibility of the summands of the relation with proper pushforward (Stacks 02SU and Stacks 02RG), and the cap products of Stacks 02U5 as families satisfying the characterization of Stacks 02U6”.

> **Stacks 02U9.** Proper pushforward commutes with the Chern class cap products: if `c` is the
> family of Chern class cap products of `α ∈ A_k(X)` for `p^*ℰ` and `e` is the family of Chern
> class cap products of `p_*α ∈ A_k(Y)` for `ℰ`, then `e_j = p_*(c_j)`, that is
>
>   `c_j(ℰ) ∩ p_*α = p_*(c_j(p^*ℰ) ∩ α)`.
>
> The proof is the one in the source: the proper pushforward of `c` satisfies the relation over `Y`
> and has `p_*α` in degree `k`, so the uniqueness of Stacks 02U6 identifies it with `e`.

```lean
theorem isChernCapFamily_properPushforward
    (hinjY : ProjectiveBundleRelationInjective C sY sPY πY hsPY r hπY hfacY twistY)
    (hcompat : ChernTermsCompatibleWithPushforward C sX sY sPX sPY πX hsPX πY hsPY r hπX hπY
      hfacX hfacY twistX twistY p hp p' hp') (k : ℤ)
    (α : chowGroup C sX k) (c : ∀ j : Fin (r + 1), chowGroup C sX (k - (j : ℤ)))
    (e : ∀ j : Fin (r + 1), chowGroup C sY (k - (j : ℤ)))
    (hc : IsChernCapFamily C sX sPX πX hsPX r hπX hfacX twistX k α c)
    (he : IsChernCapFamily C sY sPY πY hsPY r hπY hfacY twistY k
      (properChowPushforward C sX sY p hp k
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C sX sY p hp k) α) e) :
    e = properPushforwardChernFamily C sX sY r p hp k c
```

**`Stacks.Chow.GenuineChern.properChowPushforward_chernCapOnCycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesCharacterization.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesCharacterization.lean#L90).

> **Stacks 02U9.** Let `p : X ⟶ Y` be a proper morphism of schemes locally of finite type over
> `S`, `ℰ` finite locally free of rank `r` on `Y` and `α` a `k`-cycle on `X`. Then
> `p_*(c_j(p^*ℰ) ∩ α) = c_j(ℰ) ∩ p_*α` in `A_{k-j}(Y)`.

```lean
theorem properChowPushforward_chernCapOnCycles {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (p : X ⟶ Y) [IsProper p]
    (hp : p ≫ sY = sX) (E : Y.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ)
    (j : Fin (r + 1)) (α : CycleGroup C sX k) :
    haveI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback p E r
    properChowPushforward C sX sY p hp (k - (j : ℤ))
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C sX sY p hp _)
        (chernCapOnCycles C sX ((Scheme.Modules.pullback p).obj E) r k j α) =
      chernCapOnCycles C sY E r k j (properPushforward C sX sY p hp k α)
```

## Tag 02U8, a lemma

[Tag 02U8](https://stacks.math.columbia.edu/tag/02U8) in the Stacks Project.

**`Stacks.Chow.isChernCapFamily_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleFlatPullback.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleFlatPullback.lean#L202). The attribute's comment: “carries both projective bundles as flat morphisms of relative dimension r - 1 with first Chern class cap operators for their twists (Stacks 01O4, 02SO, 02TI), Stacks 02S1 for the three flat morphisms, the injectivity half of Stacks 02TX over X, the compatibility of the summands with flat pullback (Stacks 02SS and 02RD), and the cap products of Stacks 02U5 as families satisfying the characterization of Stacks 02U6”.

> Flat pullback commutes with the Chern class cap products. Assume the injectivity `hinjX` of
> the projective-bundle relation over `X` and the compatibility `hcompat` of its summands with flat
> pullback. If `c` is the family of Chern class cap products of `α ∈ A_k(Y)` for `ℰ` and `e` is the
> family of Chern class cap products of `f^*α ∈ A_{k+d}(X)` for `f^*ℰ`, then `e_j = f^*(c_j)`, that
> is
>
>   `c_j(f^*ℰ) ∩ f^*α = f^*(c_j(ℰ) ∩ α)`.

```lean
theorem isChernCapFamily_flatPullback
    (hinjX : ProjectiveBundleRelationInjective C sX sPX πX hsPX r hπX hfacX twistX)
    (hcompat : ChernTermsCompatibleWithFlatPullback C sX sY sPX sPY πX hsPX πY hsPY r hπX hπY
      hfacX hfacY twistX twistY f hf d hd hfacf f' hf' hd' hfacf') (k : ℤ)
    (α : chowGroup C sY k) (c : ∀ j : Fin (r + 1), chowGroup C sY (k - (j : ℤ)))
    (e : ∀ j : Fin (r + 1), chowGroup C sX (k + (d : ℤ) - (j : ℤ)))
    (hc : IsChernCapFamily C sY sPY πY hsPY r hπY hfacY twistY k α c)
    (he : IsChernCapFamily C sX sPX πX hsPX r hπX hfacX twistX (k + (d : ℤ))
      (flatPullbackChow C sX sY f hf d hd k (hfacf k) α) e) :
    e = flatPullbackChernFamily C sX sY r f hf d hd hfacf k c
```

**`Stacks.Chow.GenuineChern.flatPullbackChow_chernCapOnCycles`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesCharacterization.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesCharacterization.lean#L112).

> **Stacks 02U8.** Let `f : X ⟶ Y` be a flat morphism of relative dimension `d` between schemes
> locally of finite type over `S`, `ℰ` finite locally free of rank `r` on `Y` and `α` a `k`-cycle
> on `Y`. Then `f^*(c_j(ℰ) ∩ α) = c_j(f^*ℰ) ∩ f^*α` in `A_{k+d-j}(X)`. The source takes `d = r`;
> the relative dimension is arbitrary here.

```lean
theorem flatPullbackChow_chernCapOnCycles {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (hf : f ≫ sY = sX) (d : ℕ)
    (hd : AlgebraicGeometry.RelativeDimension f d) (E : Y.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ)
    (j : Fin (r + 1)) (α : CycleGroup C sY k) :
    haveI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback f E r
    flatPullbackChow C sX sY f hf d hd (k - (j : ℤ))
        (flatPullbackFactorsThroughRationalEquivalence_general C sX sY f hf d hd _)
        (chernCapOnCycles C sY E r k j α) =
      chowGroupCast C sX (by ring)
        (chernCapOnCycles C sX ((Scheme.Modules.pullback f).obj E) r (k + d) j
          (flatPullback C sX sY f hf d hd k α))
```

**`Stacks.Chow.GenuineChern.chernCap_flatPullback_heq_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapRuleFlatGeneral.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapRuleFlatGeneral.lean#L46). The attribute's comment: “Stated for a module on Y identified with the pullback of E, as a heterogeneous equality between the Chow groups of the two equal degrees (k + d) - j and (k - j) + d.”.

> **Stacks 02U8 for the cap products of Stacks 02U6, in every rank.** For `f : Y ⟶ X` flat of
> relative dimension `d` over the base, `ℰ` of rank `r` on `X` and `ℰ' ≅ f^*ℰ`,
>
>   `c_j(ℰ') ∩ f^*α = f^*(c_j(ℰ) ∩ α)`,
>
> as a heterogeneous equality: the two sides lie in `A_{(k+d)-j}(Y)` and `A_{(k-j)+d}(Y)`. The flat
> pullbacks are those of `Stacks.Chow.flatPullbackChow`, through the factorization through rational
> equivalence that holds in every degree.

```lean
theorem chernCap_flatPullback_heq_general {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : Y ⟶ X)
    [LocallyOfFiniteType f] [Flat f] (hf : f ≫ sX = sY) (d : ℕ)
    (hd : AlgebraicGeometry.RelativeDimension f d) (E : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r]
    (E' : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E' r]
    (eE : E' ≅ (Scheme.Modules.pullback f).obj E) (k : ℤ) (j : Fin (r + 1))
    (α : chowGroup C sX k) :
    chernCap C r sY E' (k + d) j (flatPullbackChow C sY sX f hf d hd k
        (flatPullbackFactorsThroughRationalEquivalence_general C sY sX f hf d hd k) α) ≍
      flatPullbackChow C sY sX f hf d hd (k - (j : ℤ))
        (flatPullbackFactorsThroughRationalEquivalence_general C sY sX f hf d hd _)
        (chernCap C r sX E k j α)
```

## Tag 0B7G, a lemma

[Tag 0B7G](https://stacks.math.columbia.edu/tag/0B7G) in the Stacks Project.

**`Stacks.Chow.GenuineChern.chernCapOnCycles_gysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesGysin.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapOnCyclesGysin.lean#L63).

> **Stacks 0B7G.** Let `ℰ` be finite locally free of rank `r` on `X` and let
> `(ℒ, s, i : D ⟶ X)` be as in Definition 02T8. Let `α ∈ A_{k+1}(X)`, let `a` be a cycle
> representing `α` and `b` a cycle representing `i^*α ∈ A_k(D)`. Then for every `0 ≤ j ≤ r`
>
>   `c_j(ℰ|_D) ∩ b = i^*(c_j(ℰ) ∩ a)`  in  `A_{k-j}(D)`,
>
> for the Gysin map of Stacks 02TO and intersection with Chern classes of Stacks 02U5; that is,
> `c_j(ℰ|_D) ∩ i^*α = i^*(c_j(ℰ) ∩ α)`.

```lean
theorem chernCapOnCycles_gysin (E : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ)
    (j : Fin (r + 1)) (α : chowGroup C sX (k + 1)) (a : CycleGroup C sX (k + 1))
    (ha : QuotientAddGroup.mk' (rationalEquivalences C sX (k + 1)) a = α)
    (b : CycleGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ sX) k)
    (hb : QuotientAddGroup.mk'
        (rationalEquivalences C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ sX) k) b =
      gysinChowOfInvertible C sX k L s α) :
    letI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback
      (Stacks.Divisors.zeroScheme X L s).subschemeι E r
    chernCapOnCycles C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ sX)
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj E) r k j b =
      gysinChowOfInvertible C sX (k - (j : ℤ)) L s
        (chowGroupCast C sX (show k + 1 - (j : ℤ) = k - (j : ℤ) + 1 by omega)
          (chernCapOnCycles C sX E r (k + 1) j a))
```

**`Stacks.Chow.GenuineChern.chernCap_gysin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapRuleGysin.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapRuleGysin.lean#L240).

> **Stacks 0B7G.** Let `ℰ` be finite locally free of rank `r` on `Y` and let `(ℒ, s, i : D ⟶ Y)`
> be a triple as in Definition 02T8. Then for every `0 ≤ j ≤ r` and every `α ∈ A_{k+1}(Y)`
>
>   `c_j(ℰ|_D) ∩ i^*α = i^*(c_j(ℰ) ∩ α)`  in  `A_{k-j}(D)`,
>
> for the Chern class cap products of Stacks 02U6 and the Gysin map of Stacks 02TO.

```lean
theorem chernCap_gysin (E : Y.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} E r] (k : ℤ)
    (j : Fin (r + 1)) (α : chowGroup C sY (k + 1)) :
    letI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback
      (Stacks.Divisors.zeroScheme Y L s).subschemeι E r
    chernCap C r ((Stacks.Divisors.zeroScheme Y L s).subschemeι ≫ sY)
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme Y L s).subschemeι).obj E) k j
        (gysinChowOfInvertible C sY k L s α) =
      gysinChowOfInvertible C sY (k - (j : ℤ)) L s
        (chowGroupCast C sY (show k + 1 - (j : ℤ) = k - (j : ℤ) + 1 by omega)
          (chernCap C r sY E (k + 1) j α))
```

## Tag 0B7H, a lemma

[Tag 0B7H](https://stacks.math.columbia.edu/tag/0B7H) in the Stacks Project.

**`Stacks.Chow.GenuineChern.chernClassBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernClass.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernClass.lean#L77).

> For a finite locally free module `ℰ` of rank `r` on `X` and `0 ≤ j ≤ r`, the rule assigning
> to `f : X' ⟶ X` the operation `c_j(f^*ℰ) ∩ - : A_k(X') ⟶ A_{k-j}(X')` is a bivariant class of
> degree `j`: the class `c_j(ℰ) ∈ A^j(X)` together with its characterization.

```lean
def chernClassBivariantClass :
    {c : BivariantClass C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) (j : ℤ) //
      IsChernClassBivariant C sX F r (gysinSystemOfInvertible C) (chernCap C r)
        (pullbackPreservesRank_of_isFiniteLocallyFreeOfRank F r) j c}
```

**`Stacks.Chow.GenuineChern.chernClassBivariantClassOnCycles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernClassOnCycles.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernClassOnCycles.lean#L62).

> **Stacks 0B7H.** For a locally free module `ℰ` of rank `r` on `X` and `0 ≤ j ≤ r`, the rule
> assigning to `f : X' ⟶ X` the operation `c_j(f^*ℰ) ∩ - : A_k(X') ⟶ A_{k-j}(X')` of Stacks 02U5 is
> a bivariant class of degree `j`: a class `c ∈ A^j(X)` with `c ∩ [α] = c_j(f^*ℰ) ∩ α` for every
> `f : X' ⟶ X` and every `k`-cycle `α` on `X'`, the cap operation being read on `X'` through the
> identification `X ×_X X' ≅ X'`.

```lean
def chernClassBivariantClassOnCycles :
    {c : BivariantClass C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) (j : ℤ) //
      ∀ {T : Scheme.{u}} (g : T ⟶ X) [LocallyOfFiniteType g] (k : ℤ)
        (α : CycleGroup C (g ≫ sX) k),
        letI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback g F r
        chowPushforwardOfIso C (pullback.fst (𝟙 X) g ≫ sX) (g ≫ sX)
            (identityBaseChangeIso g).hom (identityBaseChangeIso_hom_comp_base C sX g)
            (k - (j : ℤ)) (c.cap g k (QuotientAddGroup.mk' (rationalEquivalences C (g ≫ sX) k) α)) =
          chernCapOnCycles C (g ≫ sX) ((Scheme.Modules.pullback g).obj F) r k j α}
```

## Tag 0FE1, a definition

[Tag 0FE1](https://stacks.math.columbia.edu/tag/0FE1) in the Stacks Project.

**`Stacks.Chow.chernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/TotalChernClassOfModule.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/TotalChernClassOfModule.lean#L127). The attribute's comment: “c\_i(E) is the degree-i bivariant class of Stacks 0B7H”.

> **Stacks 0FE1, the `i`-th Chern class.** For `0 ≤ i ≤ r`, the `i`-th Chern class
> `c_i(ℰ) ∈ A^i(X)` of a module `ℰ` that is finite locally free of rank `r`: it *is* the bivariant
> class of degree `i` for `𝟙 X` constructed in Stacks 0B7H, namely the rule assigning to
> `f : X' ⟶ X` the operation `c_i(f^*ℰ) ∩ - : CH_k(X') ⟶ CH_{k-i}(X')`.

```lean
def chernClass (i : Fin (r + 1)) :
    BivariantClass C G sX sX (𝟙 X) (Category.id_comp sX) (i : ℤ)
```

**`Stacks.Chow.totalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/TotalChernClassOfModule.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/TotalChernClassOfModule.lean#L165). The attribute's comment: “c(E) = c\_0(E) + ... + c\_r(E) is the formal sum of the c\_i(E)”.

> **Stacks 0FE1, the total Chern class.** The total Chern class
> `c(ℰ) = c_0(ℰ) + c_1(ℰ) + ⋯ + c_r(ℰ)` of a module `ℰ` that is finite locally free of rank `r`:
> the formal sum of the `r + 1` Chern classes of Stacks 0B7H, viewed as a nonhomogeneous bivariant
> class on `X`, that is, as an element of `A^*(X ⟶ X) = ⊕_p A^p(X ⟶ X)`.

```lean
def totalChernClass : nonhomogeneousBivariantGroup C G sX sX (𝟙 X) (Category.id_comp sX)
```

**`Stacks.Chow.canonicalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/TotalChernClassOfModule.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/TotalChernClassOfModule.lean#L101). The attribute's comment: “c\_i(E) ∈ A^i(X), the degree-i bivariant class of Stacks 0B7H, with the genuine cap products of Stacks 02U6 and the canonical Gysin system; nothing assumed”.

> **Stacks 0FE1, the `i`-th Chern class.** For a module `ℰ` that is finite locally free of rank
> `r` on `X` and `0 ≤ i ≤ r`, the `i`-th Chern class `c_i(ℰ) ∈ A^i(X)`: the bivariant class of
> degree `i` for `𝟙 X` constructed in Stacks 0B7H, which assigns to `f : X' ⟶ X` the operation
> `c_i(f^*ℰ) ∩ - : A_k(X') ⟶ A_{k-i}(X')` of Stacks 02U6. It lives in the group of Stacks 0B76 at
> the canonical Gysin system, and every naturality fact the construction needs is proved.

```lean
def canonicalChernClass (i : Fin (r + 1)) :
    CanonicalBivariantClass C sX sX (𝟙 X) (Category.id_comp sX) (i : ℤ)
```

**`Stacks.Chow.canonicalTotalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/TotalChernClassOfModule.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/TotalChernClassOfModule.lean#L144). The attribute's comment: “c(E) = c\_0(E) + ... + c\_r(E), the formal sum of the c\_i(E) as a nonhomogeneous bivariant class on X, with the genuine cap products and the canonical Gysin system; nothing assumed”.

> **Stacks 0FE1, the total Chern class.** For a module `ℰ` that is finite locally free of rank
> `r` on `X`, the total Chern class `c(ℰ) = c_0(ℰ) + c_1(ℰ) + ⋯ + c_r(ℰ)`: the formal sum of the
> `r + 1` Chern classes of Stacks 0B7H, viewed as a nonhomogeneous bivariant class on `X`, that is,
> as an element of `A^*(X ⟶ X) = ⊕_p A^p(X ⟶ X)` at the canonical Gysin system. Nothing is
> assumed.

```lean
def canonicalTotalChernClass :
    nonhomogeneousBivariantGroup C (canonicalGysinSystem C) sX sX (𝟙 X) (Category.id_comp sX)
```

## Tag 02UA, a lemma

[Tag 02UA](https://stacks.math.columbia.edu/tag/02UA) in the Stacks Project.

**`Stacks.Chow.isChernCapFamily_bivariantClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClass.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClass.lean#L342). The attribute's comment: “clause (2), read on a test scheme; carries both projective bundles as flat morphisms of relative dimension r - 1 with first Chern class cap operators for their twists (01O4, 02SO, 02TI, 02S1), the injectivity half of 02TX downstairs, the compatibility of the summands with the cap product of the bivariant class (0B7B), and 02U5 as 02U6-families”.

> **Stacks 02UA (2).** A bivariant class carries the Chern class cap products of `ℰ` to those
> of `f^*ℰ`: if `d` is the family of Chern class cap products of `α ∈ A_k(T)` for `ℰ|_T` and `e` is
> the family of Chern class cap products of `c ∩ α ∈ A_{k-p}(T ×_X X')` for the pullback of `ℰ`,
> then `e_j = c ∩ d_j`, that is
>
>   `c_j(f^*ℰ) ∩ (c ∩ α) = c ∩ (c_j(ℰ) ∩ α)`,
>
> which is the identity `c ∘ c_j(ℰ) = c_j(f^*ℰ) ∘ c` of the tag, read on the test scheme `g`.
>
> The proof is the one in the source: the cap product of `c` with `d` satisfies the relation
> downstairs and has `c ∩ α` in degree `k - p`, so the uniqueness of Stacks 02U6 identifies it
> with `e`.

```lean
theorem isChernCapFamily_bivariantClass
    (hinj' : ProjectiveBundleRelationInjective C (pullback.fst f g ≫ sX')
      (pullback.fst f (πT ≫ g) ≫ sX') πT' hsPT' r hπT' hfacT' twistT')
    (hcompat : ChernTermsCompatibleWithBivariantClass C G sX' sX f hf p c g πT hsPT πT' hsPT' r
      hπT hπT' hfacT hfacT' twistT twistT') (k : ℤ) (α : chowGroup C (g ≫ sX) k)
    (d : ∀ j : Fin (r + 1), chowGroup C (g ≫ sX) (k - (j : ℤ)))
    (e : ∀ j : Fin (r + 1), chowGroup C (pullback.fst f g ≫ sX') (k - p - (j : ℤ)))
    (hd : IsChernCapFamily C (g ≫ sX) ((πT ≫ g) ≫ sX) πT hsPT r hπT hfacT twistT k α d)
    (he : IsChernCapFamily C (pullback.fst f g ≫ sX') (pullback.fst f (πT ≫ g) ≫ sX') πT' hsPT'
      r hπT' hfacT' twistT' (k - p) (c.cap g k α) e) :
    e = bivariantChernFamily C G sX' sX f hf p c g r k d
```

**`Stacks.Chow.chernCapOnChow_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClass.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClass.lean#L435). The attribute's comment: “the 'in particular' clause, for the cap products of Stacks 02U6; carries both projective bundles of F and that of E as flat morphisms of relative dimension one less than the rank, with first Chern class cap operators for their twists (01O4, 02SO, 02TI, 02S1), both halves of 02TX, and the commutation of c\_j(F) with the summands of E's relation (02SS and 02U8)”.

> **The "in particular" of Stacks 02UA.** The Chern class cap products of two finite locally
> free modules commute:
>
>   `c_i(ℰ) ∩ (c_j(ℱ) ∩ α) = c_j(ℱ) ∩ (c_i(ℰ) ∩ α)`   in   `A_{k-j-i}(X)`
>
> for every `α ∈ A_k(X)`, which is the displayed identity of the tag.
>
> The proof is the one in the source, with `c = c_j(ℱ) ∩ -` playing the role of the bivariant class
> of clause (2): the family `(c_j(ℱ) ∩ (c_i(ℰ) ∩ α))_i` satisfies the relation of Stacks 02U6 over
> `X` for the class `c_j(ℱ) ∩ α`, because capping with `c_j(ℱ)` carries each summand of the
> relation to itself, and its zeroth member is `c_j(ℱ) ∩ α`; so the uniqueness of Stacks 02U6
> identifies it with the family `(c_i(ℰ) ∩ (c_j(ℱ) ∩ α))_i`.

```lean
theorem chernCapOnChow_comm
    (hinj : ProjectiveBundleRelationInjective C sX sP π hsP r hπ hfac twist)
    (hsurj : ProjectiveBundleRelationSurjective C sX sP π hsP r hπ hfac twist)
    (hcompat : ChernTermsCompatibleWithChernCap C sX sP sQ sQP π hsP r hπ hfac twist ρ hsQ s hρ
      hfacQ twistQ ρP hsQP hρP hfacQP twistQP hinjQ hsurjQ hinjQP hsurjQP j)
    (k : ℤ) (α : chowGroup C sX k) (i : Fin (r + 1)) :
    chernCapOnChow C sX sP π hsP r hπ hfac twist hinj hsurj (k - (j : ℤ)) i
        (chernCapOnChow C sX sQ ρ hsQ s hρ hfacQ twistQ hinjQ hsurjQ k j α) =
      chowGroupCast C sX (show k - (i : ℤ) - (j : ℤ) = k - (j : ℤ) - (i : ℤ) from by omega)
        (chernCapOnChow C sX sQ ρ hsQ s hρ hfacQ twistQ hinjQ hsurjQ (k - (i : ℤ)) j
          (chernCapOnChow C sX sP π hsP r hπ hfac twist hinj hsurj k i α))
```

**`Stacks.Chow.BivariantClass.heq_bivariantCompositeOfInvertible_chernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClassGenuine.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClassGenuine.lean#L386). The attribute's comment: “(2), for a homogeneous c in A^p(X' -> X), the bivariant Chern classes of Stacks 0B7H and the composition of Stacks 0B75 at the Gysin system of the first Chern class of an invertible module; the two composites are classes for f ≫ 𝟙 X and 𝟙 X' ≫ f of degrees p + j and j + p, whence the heterogeneous equality”.

> **Stacks 02UA (2).** Let `f : X' ⟶ X` be locally of finite type, let `c ∈ A^p(X' ⟶ X)` and let
> `ℰ` be finite locally free of rank `r` on `X`. Then for `0 ≤ j ≤ r`
>
>   `c ∘ c_j(ℰ) = c_j(f^*ℰ) ∘ c`   in   `A^{p+j}(X' ⟶ X)`,
>
> the composites being those of Stacks 0B75, classes for the equal morphisms `f ≫ 𝟙 X` and
> `𝟙 X' ≫ f` of the equal degrees `p + j` and `j + p`.

```lean
theorem BivariantClass.heq_bivariantCompositeOfInvertible_chernClass
    (c : BivariantClass C (gysinSystemOfInvertible C) sX' sX f hf p) (F : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F r]
    (j : Fin (r + 1)) :
    letI := pullbackPreservesRank_of_isFiniteLocallyFreeOfRank F r f
    bivariantCompositeOfInvertible C sX' sX sX f (𝟙 X) hf (Category.id_comp sX) p j c
        (GenuineChern.chernClass C sX F r j) ≍
      bivariantCompositeOfInvertible C sX' sX' sX (𝟙 X') f (Category.id_comp sX') hf j p
        (GenuineChern.chernClass C sX' ((Scheme.Modules.pullback f).obj F) r j) c
```

**`Stacks.Chow.BivariantClass.heq_mulId_chernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClassGenuine.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassHigher/ProjectiveBundleBivariantClassGenuine.lean#L408). The attribute's comment: “(1), for the product of A^*(X) given by the composition of Stacks 0B75 at the Gysin system of the first Chern class of an invertible module, against every homogeneous c in A^q(X); the two products have degrees q + j and j + q, whence the heterogeneous equality”.

> **Stacks 02UA (1).** The Chern class `c_j(ℰ) ∈ A^j(X)` of a finite locally free module of rank
> `r` is in the center of `A^*(X)`: for every `c ∈ A^q(X)`,
>
>   `c · c_j(ℰ) = c_j(ℰ) · c`,
>
> the two products lying in `A^{q+j}(X)` and `A^{j+q}(X)`.

```lean
theorem BivariantClass.heq_mulId_chernClass {q : ℤ}
    (c : BivariantClass C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) q)
    (F : X.Modules) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F r]
    (j : Fin (r + 1)) :
    c.mulId C sX (GenuineChern.chernClass C sX F r j) ≍
      (GenuineChern.chernClass C sX F r j).mulId C sX c
```

**`Stacks.Chow.GenuineChern.comp_chernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernCentral.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernCentral.lean#L124). The attribute's comment: “(2): c ∘ c\_j(E) = c\_j(f^*E) ∘ c in A^\{p+j}(X' → X) for every f : X' → X locally of finite type and every bivariant class c in A^p(X' → X) of Stacks 0B76”.

> **Stacks 02UA (2).** Let `ℰ` be a locally free `𝒪_X`-module of rank `r`, let `f : X' ⟶ X` be
> locally of finite type and let `c ∈ A^p(X' ⟶ X)` be a bivariant class. Then
>
>   `c ∘ c_j(ℰ) = c_j(f^*ℰ) ∘ c`   in   `A^{p+j}(X' ⟶ X)`,
>
> with `c_j(ℰ) ∈ A^j(X)` and `c_j(f^*ℰ) ∈ A^j(X')` the bivariant Chern classes of Stacks 0B7H. The
> left side is a class for `f ≫ 𝟙 X` of degree `p + j`; the right side, a class for `𝟙 X' ≫ f` of
> degree `j + p`, is read as one for `f ≫ 𝟙 X` of degree `p + j` along the identity of `X'`.

```lean
theorem comp_chernClass {X' : Scheme.{u}} {sX' : X' ⟶ C.S} [LocallyOfFiniteType sX']
    (F : X.Modules) (r : ℕ) [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F r]
    (j : Fin (r + 1)) (f : X' ⟶ X) (hf : f ≫ sX = sX') {p : ℤ}
    (c : BivariantChowClass C sX' sX f hf p) :
    letI := AlgebraicGeometry.isFiniteLocallyFreeOfRank_pullback f F r
    c.comp (BivariantChowClass.equivBivariantClass.symm (chernClass C sX F r j)) =
      (((BivariantChowClass.equivBivariantClass.symm
          (chernClass C sX' ((Scheme.Modules.pullback f).obj F) r j)).comp c).degreeCongr
        (add_comm (j : ℤ) p)).transport (comp_comp_structureMorphism_eq hf (Category.id_comp sX))
        (Iso.refl X') (by simp)
```

**`Stacks.Chow.GenuineChern.chernClass_mem_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernCentral.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernCentral.lean#L229). The attribute's comment: “(1): c\_j(E) in A^j(X) is in the center of the Chow cohomology ring A^*(X) of Stacks 0B7E, for the bivariant Chern class of Stacks 0B7H”.

> **Stacks 02UA (1).** The `j`-th Chern class `c_j(ℰ) ∈ A^j(X)` of a locally free `𝒪_X`-module of
> rank `r` lies in the center of the Chow cohomology ring `A^*(X)` of Stacks 0B7E.

```lean
theorem chernClass_mem_center (F : X.Modules) (r : ℕ)
    [SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} F r] (j : Fin (r + 1)) :
    letI : Ring (chowCohomology C (gysinSystemOfInvertible C) sX) :=
      chowCohomologyRingOfInvertible C sX
    DirectSum.of (fun q : ℤ ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sX q) (j : ℤ)
        (chernClass C sX F r j) ∈
      Subring.center (chowCohomology C (gysinSystemOfInvertible C) sX)
```

Declarations registered for the tag:

- [`Stacks.Chow.GenuineChern.chernCap_chernCap_comm`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/CapRuleComm.lean#L148), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernCentral.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/BivariantChernCentral.lean#L252) (StacksFrontier): “the 'in particular': c\_i(E) ∩ c\_j(F) ∩ α = c\_j(F) ∩ c\_i(E) ∩ α in CH\_\{k-i-j}(X) for locally free E, F of ranks r, s and every α in CH\_k(X)”.

## Tag 0ESW, a remark

[Tag 0ESW](https://stacks.math.columbia.edu/tag/0ESW) in the Stacks Project.

**`Stacks.Chow.chernClassArbitraryRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean#L294). The attribute's comment: “chern\_classes\_arbitrary\_rank; the constant-rank Chern classes the remark cites enter as a quantified family; the classes of Tag 0B7H themselves are Stacks.Chow.GenuineChern.chernClassBivariantClass”.

> **Stacks 0ESW.** The `n`-th Chern class `c_n(E) ∈ A^n(X)` of a finite locally free module of
> not necessarily constant rank: the class which preserves the product decomposition of Chow
> cohomology along the rank loci and whose component on `X_r` is `c_n(E|_{X_r})`.

```lean
def chernClassArbitraryRank (n : ℕ) : chowCohomologyComponent C G sX (n : ℤ)
```

**`Stacks.Chow.rankLocusRestriction_chernClassArbitraryRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean#L301). The attribute's comment: “chern\_classes\_arbitrary\_rank; the constant-rank Chern classes the remark cites enter as a quantified family; the classes of Tag 0B7H themselves are Stacks.Chow.GenuineChern.chernClassBivariantClass”.

> **Stacks 0ESW.** The component of `c_n(E)` on the rank-`r` locus is `c_n(E|_{X_r})`, and is
> zero when `r < n`.

```lean
theorem rankLocusRestriction_chernClassArbitraryRank (n r : ℕ) :
    rankLocusRestriction C G sX E hgysO (n : ℤ)
        (chernClassArbitraryRank C G sX E hgysO hgysR hgysC cc n) r =
      rankLocusChernFamily C G sX E cc n r
```

**`Stacks.Chow.isChernClassBivariant_rankLocusRestriction_chernClassArbitraryRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean#L311). The attribute's comment: “chern\_classes\_arbitrary\_rank; the constant-rank Chern classes the remark cites enter as a quantified family; the classes of Tag 0B7H themselves are Stacks.Chow.GenuineChern.chernClassBivariantClass”.

> **Stacks 0ESW.** On the rank-`r` locus, `c_n(E)` acts by the already defined operation
> `c_n(E|_{X_r}) ∩ -`: its component there satisfies the characterization of Stacks 0B7H for the
> restricted module.

```lean
theorem isChernClassBivariant_rankLocusRestriction_chernClassArbitraryRank
    (hcc : ∀ (r : ℕ) (j : Fin (r + 1)),
      IsChernClassBivariant C ((rankLocus E r).ι ≫ sX)
        ((Scheme.Modules.pullback (rankLocus E r).ι).obj E) r G (caps r) (hrank r) j (cc r j))
    (n r : ℕ) (h : n ≤ r) :
    IsChernClassBivariant C ((rankLocus E r).ι ≫ sX)
      ((Scheme.Modules.pullback (rankLocus E r).ι).obj E) r G (caps r) (hrank r)
      ⟨n, Nat.lt_succ_of_le h⟩
      (rankLocusRestriction C G sX E hgysO (n : ℤ)
        (chernClassArbitraryRank C G sX E hgysO hgysR hgysC cc n) r)
```

**`Stacks.Chow.eq_chernClassArbitraryRank_of_rankLocusRestriction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/Basic.lean#L329). The attribute's comment: “chern\_classes\_arbitrary\_rank; the constant-rank Chern classes the remark cites enter as a quantified family; the classes of Tag 0B7H themselves are Stacks.Chow.GenuineChern.chernClassBivariantClass”.

> **Stacks 0ESW.** `c_n(E)` is the only class with these components, so the definition does
> not depend on the way the family is assembled.

```lean
theorem eq_chernClassArbitraryRank_of_rankLocusRestriction_eq (n : ℕ)
    {c : chowCohomologyComponent C G sX (n : ℤ)}
    (h : ∀ r : ℕ, rankLocusRestriction C G sX E hgysO (n : ℤ) c r =
      rankLocusChernFamily C G sX E cc n r) :
    c = chernClassArbitraryRank C G sX E hgysO hgysR hgysC cc n
```

**`Stacks.Chow.exists_infinite_chernClassOfLocallyFree_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/InfinitelyManyChernClasses.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/InfinitelyManyChernClasses.lean#L398). The attribute's comment: “it may happen that c\_p(E) is nonzero for infinitely many p”.

> **The Chern classes of a module of non-constant rank can be nonzero in infinitely many
> degrees.** There are a base situation `(S, δ)` of chapter 42, a scheme `X`
> locally of finite type over `S` and a finite locally free `𝒪_X`-module `ℰ` such that
> `c_p(ℰ) ≠ 0` for infinitely many `p`.

```lean
theorem exists_infinite_chernClassOfLocallyFree_ne_zero :
    ∃ (C : ChowSituation.{u}) (X : Scheme.{u}) (sX : X ⟶ C.S) (_ : LocallyOfFiniteType sX)
      (E : X.Modules) (_ : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E),
      {p : ℕ | SectionZeroScheme.chernClassOfLocallyFree E C sX p ≠ 0}.Infinite
```

**`Stacks.Chow.SectionZeroScheme.rankLocusChowCohomologyEquivOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L82). The attribute's comment: “A^p(X) = ∏\_r A^p(X\_r) for the rank decomposition X = ∐ X\_r of a finite locally free module (via 0FDZ), at the Gysin system of the first Chern class rule, nothing assumed”.

> **Stacks 0ESW, the decomposition of Chow cohomology.** `A^p(X) = ∏_{r ≥ 0} A^p(X_r)` for the
> decomposition of `X` by the rank of `ℰ`: restriction to the rank loci is an isomorphism onto the
> product (Stacks 0FDZ).

```lean
def rankLocusChowCohomologyEquivOfInvertible (p : ℤ) :
    chowCohomologyComponent C (gysinSystemOfInvertible C) sX p ≃+
      ∀ r : ℕ, chowCohomologyComponent C (gysinSystemOfInvertible C) ((rankLocus E r).ι ≫ sX) p
```

**`Stacks.Chow.SectionZeroScheme.idRule_chernClassOfLocallyFree_of_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L178). The attribute's comment: “c\_p(E) acts on the factors X'\_r by the already defined operations c\_p(E|\_\{X'\_r}) ∩ -: on every test scheme along which E has constant rank r the operation of c\_p(E) is the cap product c\_p(f^*E) ∩ - of 0B7H (zero for p > r)”.

> **Stacks 0ESW, the operation of `c_p(ℰ)`.** On a test scheme `f : X' ⟶ X` along which `f^*ℰ`
> has constant rank `r` — for instance the part `X'_r` of any test scheme lying over `X_r` — the
> class `c_p(ℰ)` acts by the already defined operation `c_p(f^*ℰ) ∩ -` of Stacks 0B7H, which is zero
> when `p > r`.

```lean
theorem idRule_chernClassOfLocallyFree_of_rank (r p : ℕ) {X' : Scheme.{u}} (f : X' ⟶ X)
    [LocallyOfFiniteType f]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback f).obj E) r] (k : ℤ) (α : chowGroup C (f ≫ sX) k) :
    (chernClassOfLocallyFree E C sX p).idRule C sX (gysinSystemOfInvertible C) f k α =
      if h : p ≤ r then
        GenuineChern.chernCap C r (f ≫ sX) ((Scheme.Modules.pullback f).obj E) k
          ⟨p, Nat.lt_succ_of_le h⟩ α
      else 0
```

**`Stacks.Chow.SectionZeroScheme.chowGroupRestrict_idRule_chernClassOfLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L255). The attribute's comment: “explicit form: for every X' → X locally of finite type, c\_p(E) preserves the decomposition CH\_*(X') = ∏\_r CH\_*(X'\_r) and acts on the factor X'\_r by c\_p(E|\_\{X'\_r}) ∩ -”.

> **Stacks 0ESW, explicitly.** For a test scheme `g : X' ⟶ X` locally of finite type, with the
> induced decomposition `X' = ∐ X'_r`, `X'_r = g⁻¹(X_r)`, the class `c_p(ℰ)` preserves the
> decomposition `CH_*(X') = ∏_r CH_*(X'_r)` and acts on the factor `CH_*(X'_r)` by the already
> defined operation `c_p(ℰ|_{X'_r}) ∩ -` of Stacks 0B7H (zero for `p > r`): restricting
> `c_p(ℰ) ∩ α` to `X'_r` gives `c_p(ℰ|_{X'_r}) ∩ (α|_{X'_r})`.

```lean
theorem chowGroupRestrict_idRule_chernClassOfLocallyFree (r p : ℕ) {X' : Scheme.{u}}
    (g : X' ⟶ X) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sX) k) :
    haveI := isFiniteLocallyFreeOfRank_pullback_preimage_rankLocus E g r
    chowGroupRestrict C (g ≫ sX) (((g ⁻¹ᵁ rankLocus E r).ι ≫ g) ≫ sX) (g ⁻¹ᵁ rankLocus E r).ι
        (Category.assoc _ _ _).symm ((k : ℤ) - (p : ℤ))
        ((chernClassOfLocallyFree E C sX p).idRule C sX (gysinSystemOfInvertible C) g k α) =
      if h : p ≤ r then
        GenuineChern.chernCap C r (((g ⁻¹ᵁ rankLocus E r).ι ≫ g) ≫ sX)
          ((Scheme.Modules.pullback ((g ⁻¹ᵁ rankLocus E r).ι ≫ g)).obj E) k
          ⟨p, Nat.lt_succ_of_le h⟩
          (chowGroupRestrict C (g ≫ sX) (((g ⁻¹ᵁ rankLocus E r).ι ≫ g) ≫ sX)
            (g ⁻¹ᵁ rankLocus E r).ι (Category.assoc _ _ _).symm k α)
      else 0
```

**`Stacks.Chow.SectionZeroScheme.chernClassOfLocallyFree_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L288). The attribute's comment: “c\_p(E) ∈ A^p(X) as the product of the classes c\_p(E|\_\{X\_r}) ∈ A^p(X\_r) of 0B7H under A^p(X) = ∏\_r A^p(X\_r): existence and uniqueness of the class with these restrictions”.

> **Stacks 0ESW, the Chern classes of a module of non-constant rank.** `c_p(ℰ) ∈ A^p(X)` is the
> class whose restriction to every rank locus `X_r` is the Chern class `c_p(ℰ|_{X_r})` of
> Stacks 0B7H (zero when `p > r`), and it is the only such class: under
> `A^p(X) = ∏_r A^p(X_r)` it is the product of the classes `c_p(ℰ|_{X_r})`.

```lean
theorem chernClassOfLocallyFree_spec (p : ℕ) :
    (∀ r : ℕ, haveI := isFiniteLocallyFreeOfRank_pullback_rankLocus E r
      chowCohomologyRestriction C (gysinSystemOfInvertible C) sX (rankLocus E r).ι (p : ℤ)
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C)
          (chernClassOfLocallyFree E C sX p) =
        if h : p ≤ r then
          GenuineChern.chernClass C ((rankLocus E r).ι ≫ sX)
            ((Scheme.Modules.pullback (rankLocus E r).ι).obj E) r ⟨p, Nat.lt_succ_of_le h⟩
        else 0) ∧
    ∀ c : chowCohomologyComponent C (gysinSystemOfInvertible C) sX (p : ℤ),
      (∀ r : ℕ, haveI := isFiniteLocallyFreeOfRank_pullback_rankLocus E r
        chowCohomologyRestriction C (gysinSystemOfInvertible C) sX (rankLocus E r).ι (p : ℤ)
            (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c =
          if h : p ≤ r then
            GenuineChern.chernClass C ((rankLocus E r).ι ≫ sX)
              ((Scheme.Modules.pullback (rankLocus E r).ι).obj E) r ⟨p, Nat.lt_succ_of_le h⟩
          else 0) →
      c = chernClassOfLocallyFree E C sX p
```

**`Stacks.Chow.SectionZeroScheme.totalChernClassCompleted`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L398). The attribute's comment: “the total Chern class c(E) = c\_0(E) + c\_1(E) + ... as an element of the completed bivariant cohomology ring A^*(X)^∧ of 0FE0”.

> **Stacks 0ESW, the total Chern class.** The total Chern class
> `c(ℰ) = c_0(ℰ) + c_1(ℰ) + c_2(ℰ) + … ∈ A^*(X)^∧` of a finite locally free module of arbitrary
> rank: the element of the completed bivariant group of Stacks 0FE0 whose degree `p` part is the
> Chern class `c_p(ℰ)` for `p ≥ 0` (and zero for `p < 0`).

```lean
def totalChernClassCompleted :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    {c : completedBivariantGroup C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) //
      completedBivariantSequenceOfInvertible C sX sX (𝟙 X) (Category.id_comp sX) c =
        totalChernComponent C sX E}
```

**`Stacks.Chow.SectionZeroScheme.rankClassOfLocallyFree_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L443). The attribute's comment: “the rank r(E) ∈ A^0(X): the class whose restriction to each X\_r is r times the unit of A^0(X\_r), existence and uniqueness”.

> **Stacks 0ESW, the rank as the unique class with the given restrictions.** `r(ℰ)` restricts
> to `r · 1` on each rank locus `X_r`, and it is the only class of `A^0(X)` doing so.

```lean
theorem rankClassOfLocallyFree_spec :
    (∀ r : ℕ, chowCohomologyRestriction C (gysinSystemOfInvertible C) sX (rankLocus E r).ι 0
        (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) (rankClassOfLocallyFree C sX E) =
      (r : ℤ) • bivariantIdentityClassOfInvertible C ((rankLocus E r).ι ≫ sX)) ∧
    ∀ c : chowCohomologyComponent C (gysinSystemOfInvertible C) sX 0,
      (∀ r : ℕ, chowCohomologyRestriction C (gysinSystemOfInvertible C) sX (rankLocus E r).ι 0
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c =
        (r : ℤ) • bivariantIdentityClassOfInvertible C ((rankLocus E r).ι ≫ sX)) →
      c = rankClassOfLocallyFree C sX E
```

**`Stacks.Chow.SectionZeroScheme.idRule_rankClassOfLocallyFree_of_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L469). The attribute's comment: “the rank r(E) ∈ A^0(X) is the bivariant operation sending (α\_r) to (r α\_r): on every test scheme along which E has constant rank r it acts as multiplication by r”.

> **Stacks 0ESW, the operation of the rank.** On a test scheme `f : X' ⟶ X` along which
> `f^*ℰ` has constant rank `r` — for instance the part `X'_r` of any test scheme lying over `X_r` —
> the class `r(ℰ)` acts as multiplication by `r`.

```lean
theorem idRule_rankClassOfLocallyFree_of_rank (r : ℕ) {X' : Scheme.{u}} (f : X' ⟶ X)
    [LocallyOfFiniteType f]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback f).obj E) r] (k : ℤ) (α : chowGroup C (f ≫ sX) k) :
    (rankClassOfLocallyFree C sX E).idRule C sX (gysinSystemOfInvertible C) f k α =
      (r : ℤ) • identityCapRule C sX f k α
```

**`Stacks.Chow.SectionZeroScheme.chowGroupRestrict_idRule_rankClassOfLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L493). The attribute's comment: “explicit form of the rank: r(E) is the bivariant operation sending (α\_r) ∈ ∏\_r CH\_*(X'\_r) to (r α\_r), for every X' → X locally of finite type”.

> **Stacks 0ESW, the rank explicitly.** For a test scheme `g : X' ⟶ X` locally of finite type,
> with the induced decomposition `X' = ∐ X'_r`, the class `r(ℰ)` sends `(α_r) ∈ ∏_r CH_*(X'_r)` to
> `(r α_r)`: restricting `r(ℰ) ∩ α` to `X'_r` gives `r · (α|_{X'_r})`.

```lean
theorem chowGroupRestrict_idRule_rankClassOfLocallyFree (r : ℕ) {X' : Scheme.{u}}
    (g : X' ⟶ X) [LocallyOfFiniteType g] (k : ℤ) (α : chowGroup C (g ≫ sX) k) :
    chowGroupRestrict C (g ≫ sX) (((g ⁻¹ᵁ rankLocus E r).ι ≫ g) ≫ sX) (g ⁻¹ᵁ rankLocus E r).ι
        (Category.assoc _ _ _).symm (k - 0)
        ((rankClassOfLocallyFree C sX E).idRule C sX (gysinSystemOfInvertible C) g k α) ≍
      (r : ℤ) • chowGroupRestrict C (g ≫ sX) (((g ⁻¹ᵁ rankLocus E r).ι ≫ g) ≫ sX)
        (g ⁻¹ᵁ rankLocus E r).ι (Category.assoc _ _ _).symm k α
```

**`Stacks.Chow.SectionZeroScheme.chernClassOfLocallyFree_mem_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L568). The attribute's comment: “c\_p(E) is in the center of A^*(X), for E of non-constant rank”.

> **Stacks 0ESW, centrality of the Chern classes.** For a finite locally free module `ℰ` of
> arbitrary rank, `c_p(ℰ) ∈ A^p(X)` lies in the center of the Chow cohomology ring `A^*(X)` of
> Stacks 0B7E: on each rank locus it restricts to a Chern class of Stacks 0B7H, which is central by
> Stacks 02UA, or to zero.

```lean
theorem chernClassOfLocallyFree_mem_center (p : ℕ) :
    DirectSum.of (fun q : ℤ ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sX q) (p : ℤ)
        (chernClassOfLocallyFree E C sX p) ∈
      Subring.center (chowCohomology C (gysinSystemOfInvertible C) sX)
```

**`Stacks.Chow.SectionZeroScheme.rankClassOfLocallyFree_mem_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/LocallyFreeRemark.lean#L592). The attribute's comment: “r(E) is in the center of A^*(X)”.

> **Stacks 0ESW, centrality of the rank.** `r(ℰ) ∈ A^0(X)` lies in the center of `A^*(X)`: on
> each rank locus `X_r` it restricts to `r · 1`.

```lean
theorem rankClassOfLocallyFree_mem_center :
    DirectSum.of (fun q : ℤ ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sX q) 0
        (rankClassOfLocallyFree C sX E) ∈
      Subring.center (chowCohomology C (gysinSystemOfInvertible C) sX)
```

**`Stacks.Chow.rankBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean#L215). The attribute's comment: “rank\_bivariant\_class; the flat transport axiom of Stacks 0B76 is proved here, and only the Gysin transport axiom is carried, as for the library's own first Chern class at Tag 0FDW”.

> **Stacks 0ESW.** The rank `r(E) ∈ A^0(X)` of a finite locally free module whose rank need not
> be constant: the bivariant class which preserves the product decomposition of the Chow groups
> along the rank loci and acts on the rank-`r` factor by multiplication by `r`.

```lean
def rankBivariantClass : chowCohomologyComponent C G sX 0
```

**`Stacks.Chow.rankLocusRestriction_rankBivariantClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean#L224). The attribute's comment: “rank\_bivariant\_class; the flat transport axiom of Stacks 0B76 is proved here, and only the Gysin transport axiom is carried, as for the library's own first Chern class at Tag 0FDW”.

> **Stacks 0ESW.** The component of `r(E)` on the rank-`r` locus is `r` times the unit.

```lean
theorem rankLocusRestriction_rankBivariantClass (r : ℕ) :
    rankLocusRestriction C G sX E hgysO 0
        (rankBivariantClass C G sX E hgysO hgysR hgysC hgysin) r =
      (r : ℤ) • chowCohomologyOne C ((rankLocus E r).ι ≫ sX) G
        (transportFlatNaturality_rankLocus C sX E r) (hgysin r)
```

**`Stacks.Chow.rankBivariantClass_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean#L236). The attribute's comment: “rank\_bivariant\_class; the flat transport axiom of Stacks 0B76 is proved here, and only the Gysin transport axiom is carried, as for the library's own first Chern class at Tag 0FDW”.

> **Stacks 0ESW.** `r(E)` sends `(α_r)` to `(r α_r)`: on a test scheme over the rank-`r` locus,
> capping with `r(E)` is multiplication by `r`.

```lean
theorem rankBivariantClass_cap (r : ℕ) {T : Scheme.{u}}
    (g : T ⟶ (rankLocus E r : Scheme.{u})) [LocallyOfFiniteType g] (k : ℤ)
    (α : chowGroup C (g ≫ ((rankLocus E r).ι ≫ sX)) k) :
    chowPushforwardOfIso C
        (pullback.fst (𝟙 (rankLocus E r : Scheme.{u})) g ≫ ((rankLocus E r).ι ≫ sX))
        (g ≫ ((rankLocus E r).ι ≫ sX)) (identityBaseChangeIso g).hom
        (identityBaseChangeIso_hom_comp_base C ((rankLocus E r).ι ≫ sX) g) (k - 0)
        ((rankLocusRestriction C G sX E hgysO 0
          (rankBivariantClass C G sX E hgysO hgysR hgysC hgysin) r).cap g k α) =
      (r : ℤ) • chowGroupDegreeEquiv C (g ≫ ((rankLocus E r).ι ≫ sX))
        (by omega : k = k - 0) α
```

**`Stacks.Chow.eq_rankBivariantClass_of_rankLocusRestriction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/RankClass.lean#L256). The attribute's comment: “rank\_bivariant\_class; the flat transport axiom of Stacks 0B76 is proved here, and only the Gysin transport axiom is carried, as for the library's own first Chern class at Tag 0FDW”.

> **Stacks 0ESW.** `r(E)` is the only degree-zero class with those components.

```lean
theorem eq_rankBivariantClass_of_rankLocusRestriction_eq
    {c : chowCohomologyComponent C G sX 0}
    (h : ∀ r : ℕ, rankLocusRestriction C G sX E hgysO 0 c r =
      (r : ℤ) • chowCohomologyOne C ((rankLocus E r).ι ≫ sX) G
        (transportFlatNaturality_rankLocus C sX E r) (hgysin r)) :
    c = rankBivariantClass C G sX E hgysO hgysR hgysC hgysin
```

**`AlgebraicGeometry.Scheme.Modules.rankDecomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/RankDecomposition.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/RankDecomposition.lean#L114). The attribute's comment: “the decomposition X = ∐ X\_r of a scheme by the rank of a finite locally free module: the rank is locally constant, the loci are open and closed, pairwise disjoint and covering, and the module is free of rank r near each point of X\_r. The Chern classes c\_p(E) ∈ A^p(X) of a module of non-constant rank, the total Chern class in the completed bivariant group, the rank class r(E) ∈ A^0(X) and the centrality of c\_p(E) and r(E) in A^*(X) are not covered”.

> The rank of a finite locally free module `E` on a scheme `X` is locally constant, the loci
> `X_r` where the rank is `r` are open and closed, pairwise disjoint and cover `X`, and `E` is free
> of rank `r` on a neighbourhood of every point of `X_r`.

```lean
theorem rankDecomposition :
    IsLocallyConstant ⇑(finiteLocallyFreeRank E) ∧
      (∀ r : ℕ, IsClopen (rankStratum E r : Set X)) ∧
      (∀ r s : ℕ, r ≠ s → Disjoint (rankStratum E r) (rankStratum E s)) ∧
      (⨆ r : ℕ, rankStratum E r) = ⊤ ∧
      ∀ (r : ℕ) (x : X), x ∈ rankStratum E r →
        ∃ (V : X.Opens) (_ : x ∈ V) (_ : V ≤ rankStratum E r) (I : Type u),
          Nonempty (I ≃ Fin r) ∧
            Nonempty (SheafOfModules.free.{u} I ≅ (toRingSheafModule E).over V)
```

## Tag 0FA4, a remark

[Tag 0FA4](https://stacks.math.columbia.edu/tag/0FA4) in the Stacks Project.

**`Stacks.Chow.topChernClassCompleted`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/TopChernClass.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/TopChernClass.lean#L351). The attribute's comment: “general case: c\_top(E) = ∏ c\_r(E|\_\{X\_r}) ∈ ∏ A^r(X\_r) ⊂ A^*(X)^∧”.

> **Stacks 0FA4**, general case. The top Chern class
> `c_top(ℰ) = ∏_r c_r(ℰ|_{X_r}) ∈ ∏_r A^r(X_r) ⊂ A^*(X)^∧` of a finite locally free module `ℰ` on
> `X`, for the decomposition `X = ∐ X_r` by the rank of `ℰ`: the element of the completed bivariant
> group of Stacks 0FE0 whose image `(c_p)_p ∈ ∏_p A^p(X)` has, under `A^p(X) = ∏_r A^p(X_r)` of
> Stacks 0FDZ, the component `c_r(ℰ|_{X_r})` in `A^r(X_r)` and zero in `A^p(X_r)` for `p ≠ r`.

```lean
def topChernClassCompleted :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    {c : completedBivariantGroup C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX) //
      (∀ r : ℕ, rankLocusRestriction C (gysinSystemOfInvertible C) sX E
          (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C) (r : ℤ)
          (completedBivariantSequenceOfInvertible C sX sX (𝟙 X) (Category.id_comp sX) c r) r =
        rankLocusTopChernClass C sX E r) ∧
      ∀ (p : ℤ) (r : ℕ), (r : ℤ) ≠ p →
        rankLocusRestriction C (gysinSystemOfInvertible C) sX E
          (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C) p
          (completedBivariantSequenceOfInvertible C sX sX (𝟙 X) (Category.id_comp sX) c p) r =
        0}
```

**`Stacks.Chow.topChernClassOfFinite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/TopChernClass.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassArbitraryRank/TopChernClass.lean#L407). The attribute's comment: “finite case: c\_top(E) = Σ\_r c\_r(E|\_\{X\_r}) ∈ A^*(X) = ⊕ A^*(X\_r)”.

> **Stacks 0FA4**, finite case. If only finitely many of the rank loci `X_r` are nonempty, the
> top Chern class `c_top(ℰ) = Σ_r c_r(ℰ|_{X_r}) ∈ A^*(X) = ⊕ A^*(X_r)`: the element of the graded
> group `A^*(X) = ⊕_p A^p(X)` that is the sum, over the ranks `r` that occur, of a class of degree
> `r`, and whose degree `p` part has, under `A^p(X) = ∏_r A^p(X_r)` of Stacks 0FDZ, the component
> `c_r(ℰ|_{X_r})` in `A^r(X_r)` and zero in `A^p(X_r)` for `p ≠ r`.

```lean
def topChernClassOfFinite (hfin : {r : ℕ | (rankLocus E r : Set X).Nonempty}.Finite) :
    {c : nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) sX sX (𝟙 X)
        (Category.id_comp sX) //
      c = ∑ r ∈ hfin.toFinset, DirectSum.of _ (r : ℤ) (c r) ∧
      (∀ r : ℕ, rankLocusRestriction C (gysinSystemOfInvertible C) sX E
          (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C) (r : ℤ) (c r) r =
        rankLocusTopChernClass C sX E r) ∧
      ∀ (p : ℤ) (r : ℕ), (r : ℤ) ≠ p →
        rankLocusRestriction C (gysinSystemOfInvertible C) sX E
          (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C) p (c p) r = 0}
```

**`Stacks.Chow.topChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L209). The attribute's comment: “completed top Chern class”.

> **Stacks 0FA4.** The top Chern class `c_top(E) = Σ_r c_r(E|_{X_r})` of a finite locally free
> module `E` on `X`, as an element of the completed bivariant group `A^*(X)^∧`: on a connected
> component `X_i` of `X` the rank of `E` is a constant `r`, and there the class is the `r`-th Chern
> class `c i` of `E|_{X_i}`, placed in degree `r`.

```lean
def topChernClass : completedBivariantGroup C G sX sX (𝟙 X) (Category.id_comp sX)
```

**`Stacks.Chow.topChernClass_rankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L216). The attribute's comment: “rank-locus Chern component”.

> **Stacks 0FA4.** On the locus where `E` has rank `r` the top Chern class is the `r`-th Chern
> class, in degree `r`: a connected component `X_i` lies in the locus of the rank `r` of `E` on it,
> and the degree-`r` part of `c_top(E)` there is `c_r(E|_{X_i})`.

```lean
theorem topChernClass_rankStratum (i : ConnectedComponents X) :
    X.connectedComponentOpens i ≤
        Scheme.Modules.rankStratum E (Scheme.Modules.rankOnConnectedComponent E i) ∧
      topChernClass C G sX E c i (Scheme.Modules.rankOnConnectedComponent E i : ℤ) = c i
```

**`Stacks.Chow.topChernClass_of_ne_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L227). The attribute's comment: “off-rank vanishing”.

> **Stacks 0FA4.** The top Chern class has no component in a degree other than the rank: on a
> connected component on which `E` has rank `r`, the degree-`p` part of `c_top(E)` vanishes for
> every `p ≠ r`.

```lean
theorem topChernClass_of_ne_rank (i : ConnectedComponents X) (p : ℤ)
    (h : p ≠ (Scheme.Modules.rankOnConnectedComponent E i : ℤ)) :
    topChernClass C G sX E c i p = 0
```

**`Stacks.Chow.finite_degrees_topChernClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L236). The attribute's comment: “finite-rank-locus case”.

> **Stacks 0FA4.** If only finitely many of the loci `X_r` are nonempty, then only finitely many
> degrees occur in the top Chern class, so it lies in the ordinary graded group `A^*(X)` inside its
> completion.

```lean
theorem finite_degrees_topChernClass
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite) :
    {p : ℤ | ∃ i : ConnectedComponents X, topChernClass C G sX E c i p ≠ 0}.Finite
```

**`Stacks.Chow.topChernClassFinite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L271). The attribute's comment: “ordinary finite top Chern class”.

> **Stacks 0FA4.** The top Chern class `c_top(E) = Σ_r c_r(E|_{X_r})` as an ordinary
> nonhomogeneous bivariant class on `X`, when only finitely many of the loci `X_r` are nonempty: the
> sum, over the ranks `r` that occur, of the degree-`r` part of the top Chern class.

```lean
def topChernClassFinite
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite) :
    nonhomogeneousBivariantGroup C G sX sX (𝟙 X) (Category.id_comp sX)
```

**`Stacks.Chow.topChernClassFinite_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L314). The attribute's comment: “finite-class canonical image”.

> **Stacks 0FA4.** The finite sum `Σ_r c_r(E|_{X_r})` has the completed top Chern class as its
> image under the identification of Stacks 0FDZ: in every degree and on every connected component,
> its restriction is the corresponding part of `c_top(E)`.

```lean
theorem topChernClassFinite_component
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite) (p : ℤ)
    (i : ConnectedComponents X) :
    connectedComponentBivariantEquiv C G sX p hgysO hgysR hgysC
        (topChernClassFinite C G sX E c hgysO hgysR hgysC hfin p) i =
      topChernClass C G sX E c i p
```

**`Stacks.Chow.topChernClassFinite_rankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L337). The attribute's comment: “finite-sum rank component”.

> **Stacks 0FA4.** On the locus where `E` has rank `r`, the component of the finite sum
> `Σ_r c_r(E|_{X_r})` in degree `r` is the `r`-th Chern class: a connected component `X_i` lies in
> the locus of the rank `r` of `E` on it, and the degree-`r` component of the sum there is
> `c_r(E|_{X_i})`.

```lean
theorem topChernClassFinite_rankStratum
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite)
    (i : ConnectedComponents X) :
    X.connectedComponentOpens i ≤
        Scheme.Modules.rankStratum E (Scheme.Modules.rankOnConnectedComponent E i) ∧
      connectedComponentBivariantEquiv C G sX
          (Scheme.Modules.rankOnConnectedComponent E i : ℤ) hgysO hgysR hgysC
          (topChernClassFinite C G sX E c hgysO hgysR hgysC hfin
            (Scheme.Modules.rankOnConnectedComponent E i : ℤ)) i = c i
```

**`Stacks.Chow.topChernClassFinite_of_ne_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClass.lean#L355). The attribute's comment: “finite-sum off-rank component”.

> **Stacks 0FA4.** The finite sum `Σ_r c_r(E|_{X_r})` has no component in a degree other than
> the rank: on a connected component on which `E` has rank `r`, its degree-`p` component vanishes
> for every `p ≠ r`.

```lean
theorem topChernClassFinite_of_ne_rank
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite)
    (i : ConnectedComponents X) (p : ℤ)
    (h : p ≠ (Scheme.Modules.rankOnConnectedComponent E i : ℤ)) :
    connectedComponentBivariantEquiv C G sX p hgysO hgysR hgysC
        (topChernClassFinite C G sX E c hgysO hgysR hgysC hfin p) i = 0
```

**`Stacks.Chow.topChernTotalClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L136). The attribute's comment: “top Chern class in the product of the Chow cohomology groups”.

> The top Chern class `c_top(E) = Σ_r c_r(E|_{X_r})` of a finite locally free module `E` on `X`,
> as an element of `∏_{p ≥ 0} A^p(X)`: its degree-`p` component is the class equal, on the locus
> `X_p` where `E` has rank `p`, to the `p`-th Chern class of Stacks 0ESW, and to zero on every other
> rank locus. It is assembled along the rank decomposition by Stacks 0FDZ.

```lean
def topChernTotalClass : TotalChowClass C sX
```

**`Stacks.Chow.topChernClassOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L289). The attribute's comment: “completed top Chern class”.

> The top Chern class `c_top(E) = Σ_r c_r(E|_{X_r})` of a finite locally free module `E` on `X`,
> as an element of the completed bivariant group `A^*(X)^∧`: on a connected component `X_i` of `X`
> the rank of `E` is a constant `r`, and there the class is the restriction to `X_i` of the
> degree-`r` component of `c_top(E)` — that is, of the `r`-th Chern class of Stacks 0ESW, by
> `Stacks.Chow.topChernClassOfInvertible_rankStratum` — placed in degree `r`.

```lean
def topChernClassOfInvertible :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sX (𝟙 X) (Category.id_comp sX)
```

**`Stacks.Chow.topChernClassOfInvertible_rankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L301). The attribute's comment: “rank-locus Chern component”.

> On the locus where `E` has rank `r` the top Chern class is the `r`-th Chern class, in degree
> `r`: a connected component `X_i` lies in the locus of the rank `r` of `E` on it, and the degree-`r`
> part of `c_top(E)` there is the restriction to `X_i` of the Chern class `c_r(E)` of Stacks 0ESW,
> that is `c_r(E|_{X_i})`.

```lean
theorem topChernClassOfInvertible_rankStratum (i : _root_.ConnectedComponents X) :
    X.connectedComponentOpens i ≤
        Scheme.Modules.rankStratum E (Scheme.Modules.rankOnConnectedComponent E i) ∧
      topChernClassOfInvertible C sX E i (Scheme.Modules.rankOnConnectedComponent E i : ℤ) =
        bivariantConnectedComponentRestriction C (gysinSystemOfInvertible C) sX sX (𝟙 X)
          (Category.id_comp sX) _ (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C)
          (totalChernOfFiniteLocallyFree C sX E (Scheme.Modules.rankOnConnectedComponent E i))
          i
```

**`Stacks.Chow.topChernClassOfInvertible_of_ne_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L316). The attribute's comment: “off-rank vanishing”.

> The top Chern class has no component in a degree other than the rank: on a connected component
> on which `E` has rank `r`, the degree-`p` part of `c_top(E)` vanishes for every `p ≠ r`.

```lean
theorem topChernClassOfInvertible_of_ne_rank (i : _root_.ConnectedComponents X) (p : ℤ)
    (h : p ≠ (Scheme.Modules.rankOnConnectedComponent E i : ℤ)) :
    topChernClassOfInvertible C sX E i p = 0
```

**`Stacks.Chow.finite_degrees_topChernClassOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L324). The attribute's comment: “finite-rank-locus case”.

> If only finitely many of the loci `X_r` are nonempty, then only finitely many degrees occur in
> the top Chern class, so it lies in the ordinary graded group `A^*(X)` inside its completion.

```lean
theorem finite_degrees_topChernClassOfInvertible
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite) :
    {p : ℤ | ∃ i : _root_.ConnectedComponents X,
      topChernClassOfInvertible C sX E i p ≠ 0}.Finite
```

**`Stacks.Chow.topChernClassFiniteOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L389). The attribute's comment: “ordinary finite top Chern class”.

> The top Chern class `c_top(E) = Σ_r c_r(E|_{X_r})` as an ordinary nonhomogeneous bivariant
> class on `X`, when only finitely many of the loci `X_r` are nonempty: the sum, over the ranks `r`
> that occur, of the degree-`r` part of the top Chern class.

```lean
def topChernClassFiniteOfInvertible
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite) :
    nonhomogeneousBivariantGroup C (gysinSystemOfInvertible C) sX sX (𝟙 X)
      (Category.id_comp sX)
```

**`Stacks.Chow.topChernClassFiniteOfInvertible_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L422). The attribute's comment: “finite-class canonical image”.

> The finite sum `Σ_r c_r(E|_{X_r})` has the completed top Chern class as its image under the
> identification of Stacks 0FDZ: in every degree and on every connected component, its restriction is
> the corresponding part of `c_top(E)`.

```lean
theorem topChernClassFiniteOfInvertible_component
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite) (p : ℤ)
    (i : _root_.ConnectedComponents X) :
    bivariantConnectedComponentRestriction C (gysinSystemOfInvertible C) sX sX (𝟙 X)
        (Category.id_comp sX) p (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C)
        (topChernClassFiniteOfInvertible C sX E hfin p) i =
      topChernClassOfInvertible C sX E i p
```

**`Stacks.Chow.topChernClassFiniteOfInvertible_rankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L444). The attribute's comment: “finite-sum rank component”.

> On the locus where `E` has rank `r`, the component of the finite sum `Σ_r c_r(E|_{X_r})` in
> degree `r` is the `r`-th Chern class: a connected component `X_i` lies in the locus of the rank `r`
> of `E` on it, and the degree-`r` component of the sum there is the restriction of `c_r(E)`, that is
> `c_r(E|_{X_i})`.

```lean
theorem topChernClassFiniteOfInvertible_rankStratum
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite)
    (i : _root_.ConnectedComponents X) :
    X.connectedComponentOpens i ≤
        Scheme.Modules.rankStratum E (Scheme.Modules.rankOnConnectedComponent E i) ∧
      bivariantConnectedComponentRestriction C (gysinSystemOfInvertible C) sX sX (𝟙 X)
          (Category.id_comp sX) _ (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C)
          (topChernClassFiniteOfInvertible C sX E hfin
            (Scheme.Modules.rankOnConnectedComponent E i : ℤ)) i =
        bivariantConnectedComponentRestriction C (gysinSystemOfInvertible C) sX sX (𝟙 X)
          (Category.id_comp sX) _ (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C)
          (totalChernOfFiniteLocallyFree C sX E (Scheme.Modules.rankOnConnectedComponent E i))
          i
```

**`Stacks.Chow.topChernClassFiniteOfInvertible_of_ne_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/TopChernClassOfInvertible.lean#L465). The attribute's comment: “finite-sum off-rank component”.

> The finite sum `Σ_r c_r(E|_{X_r})` has no component in a degree other than the rank: on a
> connected component on which `E` has rank `r`, its degree-`p` component vanishes for every
> `p ≠ r`.

```lean
theorem topChernClassFiniteOfInvertible_of_ne_rank
    (hfin : {r : ℕ | (Scheme.Modules.rankStratum E r : Set X).Nonempty}.Finite)
    (i : _root_.ConnectedComponents X) (p : ℤ)
    (h : p ≠ (Scheme.Modules.rankOnConnectedComponent E i : ℤ)) :
    bivariantConnectedComponentRestriction C (gysinSystemOfInvertible C) sX sX (𝟙 X)
        (Category.id_comp sX) p (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C)
        (topChernClassFiniteOfInvertible C sX E hfin p) i = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.38, Tag 02U4](https://stacks.math.columbia.edu/tag/02U4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
