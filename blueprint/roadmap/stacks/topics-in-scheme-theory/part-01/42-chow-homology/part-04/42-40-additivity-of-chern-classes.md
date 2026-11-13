---
declaration: section
origin: cited
lean: Stacks.Chow.chernClass_eq_of_shortExact_of_iso_unit, Stacks.Chow.chernClassCapExt_succ_eq_add_firstChernCap, Stacks.Chow.totalChernClassCohomology_eq_mul_of_shortExact_of_isInvertible, Stacks.Chow.chernCapOnChow_eq_sum_of_shortExact, Stacks.Chow.totalChernClassCohomology_eq_mul_of_shortExact, Stacks.Chow.chernClassCapExt_eq_elemSymmChernCap, Stacks.Chow.totalChernClassCohomology_eq_prod_of_filtration
statement: formalized
proof: formalized
---

# 42.40 Additivity of Chern classes

Section 42.40 of the Stacks Project, [Tag 02UF](https://stacks.math.columbia.edu/tag/02UF). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02UG, a lemma

[Tag 02UG](https://stacks.math.columbia.edu/tag/02UG) in the Stacks Project.

**`Stacks.Chow.chernClass_eq_of_shortExact_of_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/InvertibleSubsheaf.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/InvertibleSubsheaf.lean#L164). The attribute's comment: “c\_r(E) = 0 and c\_j(E) = c\_j(F) for j = 0, ..., r - 1 in the Chow cohomology ring A^*(X) of Stacks 0B7E, for a short exact sequence 0 -> O\_X -> E -> F -> 0 on X locally of finite type over the base with E, F finite locally free of ranks r, r - 1; c\_j is the bivariant Chern class of Stacks 0B7H in A^j(X); unconditional, under exactly the source's hypotheses”.

> **Stacks 02UG.** Let `X` be locally of finite type over the base and let
> `0 ⟶ 𝒪_X ⟶ ℰ ⟶ ℱ ⟶ 0` be a short exact sequence of `𝒪_X`-modules with `ℰ`, `ℱ` finite locally
> free of ranks `r`, `r - 1`. Then
>
>   `c_r(ℰ) = 0`,  `c_j(ℰ) = c_j(ℱ)`, `j = 0, …, r - 1`,
>
> in the Chow cohomology ring `A^*(X) = ⨁_p A^p(X)` of Stacks 0B7E, the `c_j` being the bivariant
> Chern classes of Stacks 0B7H placed in their degree. No hypothesis beyond the source's is taken.
> The equivalent form on cap products is
> `Stacks.Chow.GenuineChern.chernCap_eq_of_shortExact_of_iso_unit`.

```lean
theorem chernClass_eq_of_shortExact_of_iso_unit (S : ShortComplex Y.Modules) (hS : S.ShortExact)
    (e : S.X₁ ≅ SheafOfModules.unit Y.ringCatSheaf) (r : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₂ r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₃ (r - 1)] :
    DirectSum.of (fun p ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sY p) (r : ℤ)
        (GenuineChern.chernClass C sY S.X₂ r (Fin.last r)) = 0 ∧
      ∀ j : Fin r,
        DirectSum.of (fun p ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sY p)
            (j : ℤ) (GenuineChern.chernClass C sY S.X₂ r j.castSucc) =
          DirectSum.of (fun p ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sY p)
            (j : ℤ) (GenuineChern.chernClass C sY S.X₃ (r - 1) ⟨j, by omega⟩)
```

## Tag 02UH, a lemma

[Tag 02UH](https://stacks.math.columbia.edu/tag/02UH) in the Stacks Project.

**`Stacks.Chow.chernClassCapExt_succ_eq_add_firstChernCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/CapProductRelation.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/CapProductRelation.lean#L212). The attribute's comment: “CORRECTION OF FORM: the source states c(E) = c(L)c(F) in the bivariant ring A^*(X). That product is not stated here, and cannot be: this development has no ring structure on bivariant classes and no total Chern class, because Chern classes are built as operations CycleGroup C p k -> chowGroup C p (k - j) on X's own cycles (Stacks 02U5) rather than as bivariant classes over all Y -> X -- the source's formulation needs proper pushforward on Chow groups, Stacks 0GU8, which this repository does not have. What is proved instead is the componentwise identity c\_\{i+1}(E) = c\_\{i+1}(F) + c₁(L)c\_i(F) that the source's own proof reduces the product to, for every n and every cycle alpha in CycleGroup C p n. Carried: hbinom (the equality of binomial transforms that Stacks 02UD at the twists by the inverse of the invertible subsheaf gives once Stacks 02UG is applied to them), the Stacks 02U0 data chernE and chernF, and Stacks 02TI for c₁ of the subsheaf as hfac”.

> **Stacks 02UH, componentwise on cap products.** For a short exact sequence
> `0 ⟶ S.X₁ ⟶ S.X₂ ⟶ S.X₃ ⟶ 0` of finite locally free modules with `S.X₁` invertible, `S.X₂` of
> rank `r + 1` and `S.X₃` of rank `r`, and for every `n`-cycle `α`,
>
>   `c_{i+1}(S.X₂) ∩ α = c_{i+1}(S.X₃) ∩ α + c₁(S.X₁) ∩ (c_i(S.X₃) ∩ α)`
>
> in `A_{n-i-1}(X)`, for every `i ≤ r`. Summing over `i` and expanding `c(S.X₁) = 1 + c₁(S.X₁)`
> this is the relation `c(S.X₂) = c(S.X₁) · c(S.X₃)` of the source; see the module documentation
> for why the product form cannot be written here.
>
> The hypothesis `hbinom` is the input: the equality of the binomial transform of the Chern cap
> products of `S.X₂` at `r + 1` with that of `S.X₃` at `r`, along `c₁` of the inverse of the
> invertible subsheaf. That equality is what Stacks 02UD gives for the twists of `S.X₂` and `S.X₃`
> by `S.X₁^{⊗ -1}` once Stacks 02UG has identified the two twisted sheaves' Chern classes, and
> neither of those tags is proved in this repository.

```lean
theorem chernClassCapExt_succ_eq_add_firstChernCap (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (n : ℤ) (S : ShortComplex X.Modules)
    (_hS : S.ShortExact)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property S.X₁]
    (r : ℕ) (hrankE : PullbackPreservesRank S.X₂ (r + 1))
    (hrankF : PullbackPreservesRank S.X₃ r) (chernE : ChernClassCycleRule C (r + 1))
    (chernF : ChernClassCycleRule C r) (hfac : InvertibleChernCapDescends C p S.X₁)
    (α : CycleGroup C p n) (i : ℕ) (hi : i + 1 ≤ r + 1)
    (hbinom : ∀ m ≤ r + 1,
      binomialTransform (inverseFirstChernCapStep C p n S.X₁ hfac) (r + 1)
          (chernCapFamily C p n S.X₂ (r + 1) hrankE chernE α) m =
        binomialTransform (inverseFirstChernCapStep C p n S.X₁ hfac) r
          (chernCapFamily C p n S.X₃ r hrankF chernF α) m) :
    chernClassCapExt C p n S.X₂ (r + 1) hrankE chernE (i + 1) α =
      chernClassCapExt C p n S.X₃ r hrankF chernF (i + 1) α +
        firstChernCapStep C p n S.X₁ hfac i
          (chernClassCapExt C p n S.X₃ r hrankF chernF i α)
```

**`Stacks.Chow.totalChernClassCohomology_eq_mul_of_shortExact_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/InvertibleSubsheaf.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/InvertibleSubsheaf.lean#L191). The attribute's comment: “c(E) = c(L) c(F) in the Chow cohomology ring A^*(X) of Stacks 0B7E, for a short exact sequence 0 -> L -> E -> F -> 0 on X locally of finite type over the base with L invertible and E, F finite locally free of ranks r, r - 1; c(G) is the sum in A^*(X) of the bivariant Chern classes c\_j(G) of Stacks 0B7H”.

> **Stacks 02UH.** Let `X` be locally of finite type over the base and let
> `0 ⟶ ℒ ⟶ ℰ ⟶ ℱ ⟶ 0` be a short exact sequence of `𝒪_X`-modules with `ℒ` invertible and `ℰ`, `ℱ`
> finite locally free of ranks `r`, `r - 1`. Then
>
>   `c(ℰ) = c(ℒ) c(ℱ)`
>
> in the Chow cohomology ring `A^*(X)` of Stacks 0B7E, `ℒ` being finite locally free of rank one
> (Stacks 0B8M). This is the Whitney sum formula, Stacks 02UI, for a subsheaf of rank one.

```lean
theorem totalChernClassCohomology_eq_mul_of_shortExact_of_isInvertible
    (S : ShortComplex Y.Modules) (hS : S.ShortExact)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.sheaf.obj Y.ringCatSheaf.property S.X₁]
    (r : ℕ) [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₂ r]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₃ (r - 1)] :
    letI := chowCohomologyRingOfInvertible C sY
    haveI := GenuineChern.isFiniteLocallyFreeOfRank_one_of_isInvertible S.X₁
    totalChernClassCohomology C sY S.X₂ r =
      totalChernClassCohomology C sY S.X₁ 1 * totalChernClassCohomology C sY S.X₃ (r - 1)
```

## Tag 02UI, a lemma

[Tag 02UI](https://stacks.math.columbia.edu/tag/02UI) in the Stacks Project.

**`Stacks.Chow.chernCapOnChow_eq_sum_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/ShortExactSequence.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/ShortExactSequence.lean#L419). The attribute's comment: “CORRECTION OF FORM: the source states c(E) = c(E₁)c(E₂) in the bivariant ring A^*(X). That product is not stated here, and cannot be: this development has no ring structure on bivariant classes and no total Chern class, for the reasons recorded on Stacks 02UH in StacksFrontier.AlgebraicGeometry.Chow.ChernWhitney.CapProductRelation -- Chern classes are built as operations on X's own cycles rather than as bivariant classes over all Y -> X, and the source's formulation needs proper pushforward on Chow groups, Stacks 0GU8, which this repository does not have. What is proved instead is the componentwise identity c\_m(E) cap alpha = sum over i + j = m of c\_i(E₁) cap (c\_j(E₂) cap alpha), at arbitrary ranks r₁ of E₁ and r₂ of E₂, for every k and every class alpha in A\_k(X) -- which is what the product says once it is expanded, and is the reduction the source's own proof performs. Carried: cap, the Chern cap products on Chow groups of Stacks 0B7G (built there from Stacks 02U5 and Stacks 02U7, neither of which is in this repository); hbase, the relation when E₁ has rank at most one, whose rank-one case is Stacks 02UH -- proved in this repository, but in the vocabulary of the cap product on cycles and under its own carried hypotheses, so it does not supply this statement -- and whose rank-zero case needs the normalisation c\_0 = 1 of Stacks 02U0 together with invariance of the cap products under an isomorphism of modules, neither of which holds of a cap rule that is itself a parameter; and hsplit, the splitting datum of the source's induction, namely the projective space bundle of E₁ with its flat pullback injective (Stacks 02TX) and compatible with the cap products (Stacks 02U8), its twist (Stacks 01O4), and the three short exact sequences the source forms on it. The rank of the middle term is an instance hypothesis rather than derived, as it is for Stacks 02UH; AlgebraicGeometry.SheafOfModules.rank\_add\_of\_shortExact shows r₁ + r₂ is its only possible value. NOT carried, and proved here: the associativity of the convolution, the descent along the injective pullback, and the induction on r₁ itself”.

> **Stacks 02UI, componentwise on cap products.** For a short exact sequence
> `0 ⟶ S.X₁ ⟶ S.X₂ ⟶ S.X₃ ⟶ 0` of finite locally free modules of ranks `r₁`, `r₁ + r₂` and `r₂`,
> for every class `α ∈ A_k(X)` and every `m`,
>
>   `c_m(S.X₂) ∩ α = ∑_{i + j = m} c_i(S.X₁) ∩ (c_j(S.X₃) ∩ α)`   in `A_{k-m}(X)`,
>
> the sum being taken over `j ≤ m` with `i = m - j`, and the `i`-th Chern class read as zero above
> the rank. Assembling these over `m` and expanding the product, this is the relation
> `c(S.X₂) = c(S.X₁) · c(S.X₃)` of the source; see the module documentation for why the product
> form cannot be written here.
>
> The hypotheses `hbase` and `hsplit` are the inputs: the relation for a sub-module of rank at
> most one, whose rank-one case is Stacks 02UH, and the splitting datum of the source's induction,
> which carries the projective space bundle of `S.X₁` together with Stacks 02TX and Stacks 02U8.

```lean
theorem chernCapOnChow_eq_sum_of_shortExact (C : ChowSituation.{u})
    (cap : ∀ r : ℕ, HigherChernCapRule C r)
    (hbase : ∀ r₁ ≤ 1, WhitneyChernRelation C cap r₁) (hsplit : HasChernSplitting C cap)
    {T : Scheme.{u}} (q : T ⟶ C.S) [LocallyOfFiniteType q] (S : ShortComplex T.Modules)
    (hS : S.ShortExact) (r₁ r₂ : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₁ r₁]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₂ (r₁ + r₂)]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₃ r₂]
    (k : ℤ) (m : ℕ) (α : chowGroup C q k) :
    chernCapFamilyOnChow C cap q S.X₂ (r₁ + r₂) k m α =
      ∑ j : Fin (m + 1),
        gradedDegreeCast (chowGroup C q)
          (show k - (j.val : ℤ) - ((m - j.val : ℕ) : ℤ) = k - (m : ℤ) from by
            have := j.isLt; omega)
          (chernCapFamilyOnChow C cap q S.X₁ r₁ (k - (j.val : ℤ)) (m - j.val)
            (chernCapFamilyOnChow C cap q S.X₃ r₂ k (j.val) α))
```

**`Stacks.Chow.totalChernClassCohomology_eq_mul_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/WhitneyChowCohomology.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/WhitneyChowCohomology.lean#L223). The attribute's comment: “c(E) = c(E₁) c(E₂) in the Chow cohomology ring A^*(X) of Stacks 0B7E, for a short exact sequence 0 -> E₁ -> E -> E₂ -> 0 on X locally of finite type over the base with E₁, E₂ finite locally free of ranks r₁, r₂ (E is then finite locally free of rank r₁ + r₂); c(F) is the sum in A^*(X) of the bivariant Chern classes c\_j(F) of Stacks 0B7H”.

> **Stacks 02UI, the Whitney sum formula.** Let `X` be locally of finite type over the base and
> let `0 ⟶ ℰ₁ ⟶ ℰ ⟶ ℰ₂ ⟶ 0` be a short exact sequence of `𝒪_X`-modules with `ℰ₁`, `ℰ₂` finite
> locally free of ranks `r₁`, `r₂`; then `ℰ` is finite locally free of rank `r₁ + r₂`
> (`Stacks.Chow.GenuineChern.isFiniteLocallyFreeOfRank_of_shortExact`), and the total Chern classes
> satisfy
>
>   `c(ℰ) = c(ℰ₁) c(ℰ₂)`   in `A^*(X)`.

```lean
theorem totalChernClassCohomology_eq_mul_of_shortExact (S : ShortComplex Y.Modules)
    (hS : S.ShortExact) (r₁ r₂ : ℕ)
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₁ r₁]
    [AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} S.X₃ r₂] :
    letI := chowCohomologyRingOfInvertible C sY
    haveI := GenuineChern.isFiniteLocallyFreeOfRank_of_shortExact S hS r₁ r₂ ‹_› ‹_›
    totalChernClassCohomology C sY S.X₂ (r₁ + r₂) =
      totalChernClassCohomology C sY S.X₁ r₁ * totalChernClassCohomology C sY S.X₃ r₂
```

## Tag 02UJ, a lemma

[Tag 02UJ](https://stacks.math.columbia.edu/tag/02UJ) in the Stacks Project.

**`Stacks.Chow.chernClassCapExt_eq_elemSymmChernCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/FilteredAdditivity.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/FilteredAdditivity.lean#L275). The attribute's comment: “the degree-k coefficients of c(E) = prod (1 + c\_1(L\_i)), stated on the cap products of 02U5 for k >= 1 rather than as a product in A^*(X), which has no multiplication here; the filtration enters as the tower of its quotients; 02U0, 02TI, 02UD+02UG are inputs”.

> **Stacks 02UJ, componentwise on cap products.** Let `ℰ = Q_r` be finite locally free of rank
> `r` with a filtration whose successive quotients are the invertible modules `L 0, …, L (r-1)`,
> presented as the tower of short exact sequences `0 ⟶ L j ⟶ Q_{j+1} ⟶ Q_j ⟶ 0`. Then for every
> `n`-cycle `α` and every `k ≥ 1`
>
>   `c_k(ℰ) ∩ α = e_k(c₁(L 0), …, c₁(L (r-1))) ∩ ⟦α⟧`
>
> in `A_{n-k}(X)`, the `k`-th elementary symmetric function of the first Chern class cap operations
> of the quotients applied to the class of `α`. This is the coefficient of degree `k` in the
> product formula `c(ℰ) = ∏_i (1 + c₁(ℒ_i))` of the source.
>
> The normalisation `hnorm` is asked for only at the rank-zero bottom `Q_0` of the tower: in degree
> zero a binomial transform is its own zeroth entry, so `hbinom` already identifies the degree-zero
> cap products of consecutive members, and the normalisation at every stage — in particular at
> `ℰ = Q_r` — follows by induction. See the module documentation for why the product itself cannot
> be written here, for why the assertion is made in degrees `k ≥ 1`, and for the inputs `hbinom`,
> `chern` and `hfac`.

```lean
theorem chernClassCapExt_eq_elemSymmChernCap (Q : ℕ → X.Modules)
    (sub : ∀ j : Fin r, L j ⟶ Q ((j : ℕ) + 1)) (proj : ∀ j : Fin r, Q ((j : ℕ) + 1) ⟶ Q (j : ℕ))
    (hzero : ∀ j : Fin r, sub j ≫ proj j = 0)
    (hexact : ∀ j : Fin r, (ShortComplex.mk (sub j) (proj j) (hzero j)).ShortExact)
    (hrank : ∀ m : ℕ, m ≤ r → PullbackPreservesRank (Q m) m)
    (chern : ∀ m : ℕ, ChernClassCycleRule C m) (α : CycleGroup C p n)
    (hnorm : chernClassCapExt C p n (Q 0) 0 (hrank 0 (Nat.zero_le r)) (chern 0) 0 α =
      cycleClassDegreeZero C p n α)
    (hbinom : ∀ j : Fin r, ∀ i ≤ (j : ℕ) + 1,
      binomialTransform (inverseFirstChernCapStep C p n (L j) (hfac j)) ((j : ℕ) + 1)
          (chernCapFamily C p n (Q ((j : ℕ) + 1)) ((j : ℕ) + 1) (hrank ((j : ℕ) + 1) j.isLt)
            (chern ((j : ℕ) + 1)) α) i =
        binomialTransform (inverseFirstChernCapStep C p n (L j) (hfac j)) (j : ℕ)
          (chernCapFamily C p n (Q (j : ℕ)) (j : ℕ) (hrank (j : ℕ) j.isLt.le)
            (chern (j : ℕ)) α) i)
    (k : ℕ) (_hk : 1 ≤ k) :
    chernClassCapExt C p n (Q r) r (hrank r le_rfl) (chern r) k α =
      elemSymmChernCap C p n L hfac r le_rfl k
        (QuotientAddGroup.mk' (rationalEquivalences C p n) α)
```

**`Stacks.Chow.totalChernClassCohomology_eq_prod_of_filtration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/FiltrationChowCohomology.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernWhitney/FiltrationChowCohomology.lean#L249). The attribute's comment: “c(E) = prod\_\{i=1}^r (1 + c\_1(L\_i)) in the Chow cohomology ring A^*(X) of Stacks 0B7E, for E with a filtration 0 = E\_0 ⊂ E\_1 ⊂ ... ⊂ E\_r = E by subobjects with E\_i/E\_\{i-1} ≅ L\_i invertible, on X locally of finite type over the base; c\_1(L\_i) is the class of Stacks 0B77 and E is shown to be finite locally free of rank r”.

> **Stacks 02UJ.** Let `X` be locally of finite type over the base, let `ℒ_1, …, ℒ_r` be
> invertible `𝒪_X`-modules and let `ℰ` be an `𝒪_X`-module with a filtration by submodules
>
>   `0 = ℰ_0 ⊂ ℰ_1 ⊂ ℰ_2 ⊂ … ⊂ ℰ_r = ℰ`   such that   `ℰ_i/ℰ_{i-1} ≅ ℒ_i`.
>
> Then `ℰ` is finite locally free of rank `r`
> (`Stacks.Chow.isFiniteLocallyFreeOfRank_of_filtration`), and, setting `x_i = c_1(ℒ_i)`,
>
>   `c(ℰ) = ∏_{i=1}^r (1 + x_i)`   in `A^*(X)`.
>
> The filtration is indexed by `Fin (r + 1)` and the invertible modules by `Fin r`, so that `ℒ i` is
> the quotient `ℰ_{i+1}/ℰ_i`; the product is `(1 + x_1)(1 + x_2) ⋯ (1 + x_r)` in this order.

```lean
theorem totalChernClassCohomology_eq_prod_of_filtration (r : ℕ) (E : Y.Modules)
    (L : Fin r → Y.Modules)
    [∀ i, AlgebraicGeometry.SheafOfModules.IsInvertible Y.sheaf.obj Y.ringCatSheaf.property (L i)]
    (F : Fin (r + 1) → Subobject E) (hF : Monotone F) (h0 : F 0 = ⊥) (hr : F (Fin.last r) = ⊤)
    (e : ∀ i : Fin r,
      cokernel (Subobject.ofLE (F i.castSucc) (F i.succ) (hF i.castSucc_le_succ)) ≅ L i) :
    letI := chowCohomologyRingOfInvertible C sY
    haveI := isFiniteLocallyFreeOfRank_of_filtration E L F hF h0 hr e
    totalChernClassCohomology C sY E r =
      (List.ofFn fun i ↦ 1 + DirectSum.of
        (fun p ↦ chowCohomologyComponent C (gysinSystemOfInvertible C) sY p) 1
          (GenuineChern.firstChernClass C sY (L i))).prod
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.40, Tag 02UF](https://stacks.math.columbia.edu/tag/02UF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
