---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsUnique_chernCap_and_bivariant, AlgebraicGeometry.Space.chernClass, AlgebraicGeometry.Space.totalChernClass, AlgebraicGeometry.Space.chernCap_one_eq_firstChernBivariantClass_cap, AlgebraicGeometry.Space.ChowCohomologyClass.chernCap_commute_capChowHomology, AlgebraicGeometry.Space.chernCap_chernCap_comm, AlgebraicGeometry.Space.chernClassOfFiniteLocallyFree, AlgebraicGeometry.Space.rankDecomposition_chowGroup_chernClassOfFiniteLocallyFree
statement: formalized
proof: formalized
---

# 82.28 The Chern classes of a vector bundle

Section 82.28 of the Stacks Project, [Tag 0ERX](https://stacks.math.columbia.edu/tag/0ERX). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ERY, a lemma

[Tag 0ERY](https://stacks.math.columbia.edu/tag/0ERY) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_chernCap_and_bivariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean, line 1200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean#L1200). The attribute's comment: “existence and uniqueness of c_i(E) ∩ - : CH_k(X') → CH_{k-i}(X'), i = 0..r, with c_0 = id and sum_i (-1)^i c_1(O_{P'}(1))^i ∩ π'^*(c_{r-i}(E) ∩ α) = 0 on P' = P ×_X X', for every morphism X' → X of good spaces over B, E finite locally free of rank r on a good X/B; and the maps c_i(E) ∩ - form a bivariant class of degree i (BivariantClassCanonical, over chowGroupCanonical)”.

> **Stacks 0ERY.** In Situation 0EDT let `X/B` be good, `ℰ` a finite locally free `𝒪_X`-module
> of rank `r` and `(π : P → X, 𝒪_P(1))` its projective space bundle. For every morphism
> `g : X' → X` of good algebraic spaces over `B` there are unique maps
> `c_j(ℰ) ∩ - : CH_k(X') → CH_{k-j}(X')`, `j = 0, …, r`, such that `c₀(ℰ) ∩ α = α` and
>
> `∑_{i=0}^{r} (-1)^i c₁(𝒪_{P'}(1))^i ∩ π'^*(c_{r-i}(ℰ) ∩ α) = 0`
>
> for every `α ∈ CH_k(X')`, where `π' : P' = P ×_X X' → X'` is the base change of `π` and
> `𝒪_{P'}(1)` the pullback of `𝒪_P(1)` (`AlgebraicGeometry.Space.chernRelationSum`). Moreover these
> maps define a bivariant class `c_j(ℰ)` of degree `j` on `X`: there is `C ∈ A^j(X → X)` whose cap
> operation on every test space `X'` is `c_j(ℰ) ∩ -`, read on `X ×_X X' ≅ X'` along the flat
> pullback of relative dimension `0` (`AlgebraicGeometry.Space.testSpacePullbackChowMap`).
>
> The Chow groups are those of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK
> (`AlgebraicGeometry.Space.chowGroupCanonical`), the bivariant classes those of Stacks 0ERJ over
> them (`AlgebraicGeometry.Space.BivariantClassCanonical`), `c₀ ∩ α = α` is read through the
> identification `CH_k = CH_{k-0}`, and the class is
> `AlgebraicGeometry.Space.chernClass` (Stacks 0ERZ).

```lean
theorem existsUnique_chernCap_and_bivariant :
    (∀ {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX)),
      ∃! c : ∀ (j : Fin (r + 1)) (k : ℤ), chowGroupCanonical.{u + 1} D (g ≫ sX) hY k →+
          chowGroupCanonical.{u + 1} D (g ≫ sX) hY (k - ((j : ℕ) : ℤ)),
        (∀ k α, c 0 k α = ProjectiveBundleRelation.degreeCast
          (fun m => chowGroupCanonical.{u + 1} D (g ≫ sX) hY m) (by simp) α) ∧
          ∀ k α, chernRelationSum D sX hX E r hE g hY c k α = 0) ∧
      ∀ j : Fin (r + 1), ∃ C : chowCohomologyComponentCanonical.{u + 1} D sX hX ((j : ℕ) : ℤ),
        ∀ {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX))
          (hXg : D.IsGood (pullback.fst (𝟙 X) g ≫ sX))
          (c : ∀ (j : Fin (r + 1)) (k : ℤ), chowGroupCanonical.{u + 1} D (g ≫ sX) hY k →+
            chowGroupCanonical.{u + 1} D (g ≫ sX) hY (k - ((j : ℕ) : ℤ))),
          (∀ k α, c 0 k α = ProjectiveBundleRelation.degreeCast
            (fun m => chowGroupCanonical.{u + 1} D (g ≫ sX) hY m) (by simp) α) →
          (∀ k α, chernRelationSum D sX hX E r hE g hY c k α = 0) →
          ∀ k α, C.cap g hY hXg k α = testSpacePullbackChowMap D sX hX g hY hXg _ (c j k α)
```

## Tag 0ERZ, a definition

[Tag 0ERZ](https://stacks.math.columbia.edu/tag/0ERZ) in the Stacks Project.

**`AlgebraicGeometry.Space.chernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean#L1151). The attribute's comment: “the i-th Chern class c_i(E) ∈ A^i(X), i = 0, ..., r, the bivariant class of degree i of Lemma 0ERY, for E finite locally free of rank r on a good X/B; A^i(X) = A^i(X → X) over the Chow groups chowGroupCanonical”.

> **Stacks 0ERZ: the `j`-th Chern class `c_j(ℰ) ∈ A^j(X)`** of a finite locally free module `ℰ`
> of rank `r` on a good algebraic space `X/B`, `j = 0, …, r`: the bivariant class of degree `j` of
> Stacks 0ERY (`AlgebraicGeometry.Space.existsUnique_chernCap_and_bivariant`), in
> `A^j(X) = A^j(X → X)` (`AlgebraicGeometry.Space.chowCohomologyComponentCanonical`). Its cap
> operation on a test space `g : X' → X` is `c_j(ℰ) ∩ -` on `X'`
> (`AlgebraicGeometry.Space.chernCap`), read on `X ×_X X' ≅ X'`
> (`AlgebraicGeometry.Space.chernClass_cap`).

```lean
def chernClass (j : Fin (r + 1)) :
    chowCohomologyComponentCanonical.{u + 1} D sX hX ((j : ℕ) : ℤ)
```

**`AlgebraicGeometry.Space.totalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean, line 1174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean#L1174). The attribute's comment: “the total Chern class c(E) = c_0(E) + c_1(E) + ... + c_r(E), the formal sum of the Chern classes as a nonhomogeneous class in A^*(X) = ⊕_p A^p(X)”.

> **Stacks 0ERZ: the total Chern class** `c(ℰ) = c₀(ℰ) + c₁(ℰ) + … + c_r(ℰ)`, the formal sum of
> the Chern classes of `ℰ` (`AlgebraicGeometry.Space.chernClass`), a nonhomogeneous class in the
> Chow cohomology `A^*(X) = ⊕_p A^p(X)` (`AlgebraicGeometry.Space.chowCohomologyCanonical`).

```lean
def totalChernClass : chowCohomologyCanonical.{u + 1} D sX hX
```

## Tag 0ES0, a lemma

[Tag 0ES0](https://stacks.math.columbia.edu/tag/0ES0) in the Stacks Project.

**`AlgebraicGeometry.Space.chernCap_one_eq_firstChernBivariantClass_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassBivariantComparison.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FirstChernClassBivariantComparison.lean#L83). The attribute's comment: “c_1(L) ∈ A^1(X) of Definition 0ERZ (chernCap 1 on every good Y' → X) equals the bivariant class c_1(f^*L) ∩ - of Lemma 0ERM, for X/B good and L invertible”.

> **Stacks 0ES0.** In Situation 0EDT let `X/B` be good and let `ℒ` be an invertible
> `𝒪_X`-module. Then the first Chern class `c₁(ℒ)` of Definition 0ERZ equals the bivariant class of
> Stacks 0ERM (`AlgebraicGeometry.Space.firstChernBivariantClass`).
>
> Both are classes in `A^1(X)`, and the equality is that of their operations on the Chow groups of
> every good test space `g : Y' ⟶ X`: for every `k` and `α ∈ CH_k(Y')`, the cap operation
> `CH_k(Y') ⟶ CH_{k-1}(X ×_X Y')` of the class of Stacks 0ERM, followed by the identification of
> `X ×_X Y'` with `Y'` (pushforward along the isomorphism `X ×_X Y' ⟶ Y'`), is
> `c₁(g^*ℒ) ∩ α` for the first Chern class of Definition 0ERZ of the rank-one module `g^*ℒ` on `Y'`
> (`AlgebraicGeometry.Space.PrivateChern.chernCap`, the operation on
> `CH_*(Y') = ⨁_k CH_k(Y')`; `chowGroupCanonicalEquivChowGroup` identifies the Chow groups of
> Stacks 0EQ6 on which the bivariant classes act with the summands of `CH_*(Y')`).

```lean
theorem chernCap_one_eq_firstChernBivariantClass_cap
    (L : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hL : IsInvertibleModule (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) L)
    {Y' : D.Ambient} (g : Y' ⟶ X) (hY' : D.IsGood (g ≫ sX))
    (hX' : D.IsGood (pullback.fst (𝟙 X) g ≫ sX)) (k : ℤ)
    (α : chowGroupCanonical.{u + 1} D (g ≫ sX) hY' k) :
    properPushforwardChow.{u, u + 1} D (pullback.fst (𝟙 X) g ≫ sX) hX' (g ≫ sX) hY'
        (pullback.snd (𝟙 X) g) (by rw [← Category.assoc, ← pullback.condition, Category.comp_id])
        (isProper_of_isIso D.site D.base D.base_mem (pullback.snd (𝟙 X) g))
        (DirectSum.of _ (k - 1) (chowGroupCanonicalEquivChowGroup.{u + 1} D _ hX' (k - 1)
          ((firstChernBivariantClass D sX hX L hL).cap g hY' hX' k α))) =
      chernCap.{u, u + 1} (hX := hY') (pullbackLine D (g ≫ sX) hY' sX hX g L) 1
        (isFiniteLocallyFreeOfRank_one_pullbackLine D sX hX g hY' L hL) 1
        (DirectSum.of _ k (chowGroupCanonicalEquivChowGroup.{u + 1} D _ hY' k α))
```

## Tag 0ES1, a lemma

[Tag 0ES1](https://stacks.math.columbia.edu/tag/0ES1) in the Stacks Project.

**`AlgebraicGeometry.Space.ChowCohomologyClass.chernCap_commute_capChowHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCommutation.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCommutation.lean#L462). The attribute's comment: “the main assertion: for every good test space g : X' → X, every finite locally free E' of rank r on X' (in particular E' = g^*E) and every j, the cap operation of c ∈ A^p(X) on CH_*(X') commutes with c_j(E') ∩ -; this is c ∘ c_j(E) = c_j(E) ∘ c in A^*(X). The source's c_j(L) is a typo for c_j(E)”.

> **Stacks 0ES1.** In Situation 0EDT let `X/B` be good and let `c ∈ A^p(X)` (Stacks 0ERK,
> `AlgebraicGeometry.Space.ChowCohomologyClass`). Then `c` commutes with the Chern classes of
> Stacks 0ERZ (`AlgebraicGeometry.Space.PrivateChern.chernCap`): for every good test space
> `g : X' ⟶ X`, every finite locally free `𝒪_{X'}`-module `ℰ'` of rank `r` and every `j`,
>
>   `c ∩ (c_j(ℰ') ∩ α) = c_j(ℰ') ∩ (c ∩ α)`  for all `α ∈ CH_*(X')`,
>
> where `c ∩ -` is the cap operation of `c` on `X'` (`capChowHomology`). For a finite locally free
> `ℰ` of rank `r` on `X` the bivariant class `c_j(ℰ) ∈ A^j(X)` caps on `X'` as `c_j(ℰ|_{X'}) ∩ -`,
> so taking `ℰ' = ℰ|_{X'}` this is the identity `c ∘ c_j(ℰ) = c_j(ℰ) ∘ c` in `A^*(X)` (two
> bivariant classes being equal when their cap operations on all test spaces are); the statement
> here allows any `ℰ'` on `X'`.

```lean
theorem chernCap_commute_capChowHomology {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX))
    (E : Modules.{u, u} D.site D.base D.base_mem Y hY.1) (r : ℕ)
    (hE : PrivateChern.IsFiniteLocallyFreeOfRank D (g ≫ sX) hY E r) (j : ℕ) :
    Commute (chernCap.{u, u + 1} E r hE j) (c.capChowHomology g hY)
```

**`AlgebraicGeometry.Space.chernCap_chernCap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCommutation.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCommutation.lean#L523). The attribute's comment: “in particular: c_i(E) ∩ c_j(F) ∩ α = c_j(F) ∩ c_i(E) ∩ α for every α ∈ CH_k(X), as an identity in CH_*(X) = ⊕_k CH_k(X) (hence of the components in CH_{k-i-j}(X))”.

> **Stacks 0ES1, in particular.** In Situation 0EDT let `X/B` be good and let `ℰ`, `ℱ` be
> finite locally free `𝒪_X`-modules of ranks `r` and `s`. Then
>
>   `c_i(ℰ) ∩ c_j(ℱ) ∩ α = c_j(ℱ) ∩ c_i(ℰ) ∩ α`
>
> for all `α ∈ CH_k(X)`, the Chern classes being those of Stacks 0ERZ
> (`AlgebraicGeometry.Space.PrivateChern.chernCap`), operations on `CH_*(X) = ⨁_k CH_k(X)` carrying
> `CH_k(X)` to `CH_{k-n}(X)`. The identity is stated in `CH_*(X)`, where `α` is placed in degree
> `k`; both sides lie in the summand `CH_{k-i-j}(X)`, and an identity in `CH_*(X)` is in particular
> one of its components in `CH_{k-i-j}(X)`.

```lean
theorem chernCap_chernCap_comm (hX : D.IsGood sX)
    (E F : Modules.{u, u} D.site D.base D.base_mem X hX.1) (r s : ℕ)
    (hE : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX E r)
    (hF : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX F s)
    (i j : ℕ) (k : ℤ) (α : chowGroup.{u + 1} D sX hX k) :
    chernCap.{u, u + 1} E r hE i
        (chernCap.{u, u + 1} F s hF j (DirectSum.of (fun k => chowGroup.{u + 1} D sX hX k) k α)) =
      chernCap.{u, u + 1} F s hF j
        (chernCap.{u, u + 1} E r hE i (DirectSum.of (fun k => chowGroup.{u + 1} D sX hX k) k α))
```

## Tag 0ES2, a remark

[Tag 0ES2](https://stacks.math.columbia.edu/tag/0ES2) in the Stacks Project.

**`AlgebraicGeometry.Space.chernClassOfFiniteLocallyFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean#L280). The attribute's comment: “the definition: c_i(E) ∈ A^i(X) for E finite locally free of non-constant rank, the bivariant class preserving CH_*(X') = ∏_r CH_*(X'_r) and acting by c_i(E|_{X_r}) ∩ - on the factors”.

> **Stacks 0ES2: the `i`-th Chern class `c_i(ℰ) ∈ A^i(X)` of a finite locally free module `ℰ`
> of possibly non-constant rank** on a good algebraic space `X/B`: the bivariant class of degree `i`
> whose cap operation on a good test space `g : X' ⟶ X` preserves the product decomposition
> `CH_*(X') = ∏_r CH_*(X'_r)` along the pullback `X'_r = g^{-1}(X_r)` of the rank decomposition
> `X = ∐_r X_r` of `ℰ` and acts on the factor of `X'_r` by `c_i(ℰ|_{X_r}) ∩ -`, the Chern class of
> Stacks 0ERZ of the module `ℰ|_{X_r}` of constant rank `r` (zero for `i > r`)
> (`AlgebraicGeometry.Space.chernCapOfFiniteLocallyFree`); the cap operation is read on
> `X ×_X X' ≅ X'` (`AlgebraicGeometry.Space.chernClassOfFiniteLocallyFree_cap`).

```lean
def chernClassOfFiniteLocallyFree (i : ℕ) :
    chowCohomologyComponentCanonical.{u + 1} D sX hX (i : ℤ)
```

**`AlgebraicGeometry.Space.rankDecomposition_chowGroup_chernClassOfFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean#L322). The attribute's comment: “the whole remark: X = ∐_r X_r by the rank of E (open and closed), its pullback to every morphism X' → X of good spaces over B, CH_k(X') = ∏_r CH_k(X'_r) on Chow groups, and c_i(E) ∈ A^i(X) as the unique bivariant class preserving these decompositions and acting by c_i(E|_{X_r}) ∩ - on the factors”.

> **Stacks 0ES2.** In Situation 0EDT let `X/B` be good and let `ℰ` be a finite locally free
> `𝒪_X`-module, of possibly non-constant rank.
>
> 1. `X = X_0 ⨿ X_1 ⨿ X_2 ⨿ …`, where `X_r ⊆ X` is the open and closed subspace where `ℰ` has
>    rank `r`.
> 2. For every morphism `g : X' ⟶ X` of good algebraic spaces over `B`, the inverse images
>    `X'_r = g^{-1}(X_r)` form the corresponding decomposition of `X'`, and
> 3. the restrictions to the pieces identify `CH_k(X')` with `∏_r CH_k(X'_r)` for every `k`.
> 4. For every `i`, `c_i(ℰ) ∈ A^i(X)` (`AlgebraicGeometry.Space.chernClassOfFiniteLocallyFree`)
>    is a bivariant class which preserves these direct product decompositions and acts by
>    `c_i(ℰ|_{X_r}) ∩ -` on the factors (`AlgebraicGeometry.Space.rankPieceChernCap`: the Chern class
>    of Stacks 0ERZ of `ℰ|_{X_r}`, of constant rank `r`, and `0` for `i > r`), and it is the only
>    bivariant class of degree `i` with this property.
>
> The cap operation of a class `C ∈ A^i(X)` on `X'` lands in `CH_{k-i}(X ×_X X')`, which is read on
> `X'` along the flat pullback by the isomorphism `X ×_X X' ≅ X'`
> (`AlgebraicGeometry.Space.testSpacePullbackChowMap`).

```lean
theorem rankDecomposition_chowGroup_chernClassOfFiniteLocallyFree :
    IsClopenSubspaceDecomposition D sX
        (fun r : ULift.{u} ℕ => (rankSubspace (Y := ⟨X, hX.1⟩) E r.down).ι) ∧
      (∀ {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX)),
        ∃ hdec : IsClopenSubspaceDecomposition D (g ≫ sX)
            (fun r : ULift.{u} ℕ => ((rankSubspace (Y := ⟨X, hX.1⟩) E r.down).preimage g).ι),
          ∀ k : ℤ, Function.Bijective (chowGroupCanonicalDecompositionRestrict hdec k)) ∧
      ∀ i : ℕ,
        let P : chowCohomologyComponentCanonical.{u + 1} D sX hX (i : ℤ) → Prop := fun C =>
          ∀ {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX))
            (hXg : D.IsGood (pullback.fst (𝟙 X) g ≫ sX)) (k : ℤ)
            (α : chowGroupCanonical.{u + 1} D (g ≫ sX) hY k),
            ∃ β : chowGroupCanonical.{u + 1} D (g ≫ sX) hY (k - (i : ℤ)),
              C.cap g hY hXg k α = testSpacePullbackChowMap D sX hX g hY hXg _ β ∧
                ∀ r : ULift.{u} ℕ,
                  chowGroupCanonicalPieceRestrict
                      ((isClopenSubspaceDecomposition_rankSubspace D sX hX E hE).preimage g hY) r
                      (k - (i : ℤ)) β =
                    rankPieceChernCap D sX hX E hE i r
                      ((rankSubspace (Y := ⟨X, hX.1⟩) E r.down).fromPreimage g)
                      (((isClopenSubspaceDecomposition_rankSubspace D sX hX E hE).preimage g
                        hY).isGoodPiece r) k
                      (chowGroupCanonicalPieceRestrict
                        ((isClopenSubspaceDecomposition_rankSubspace D sX hX E hE).preimage g hY)
                        r k α)
        P (chernClassOfFiniteLocallyFree D sX hX E hE i) ∧
          ∀ C, P C → C = chernClassOfFiniteLocallyFree D sX hX E hE i
```

**`AlgebraicGeometry.Space.isClopenSubspaceDecomposition_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean#L279). The attribute's comment: “the decomposition of X' obtained by pullback”.

> A decomposition of a good algebraic space over the base into good open and closed subspaces
> pulls back along a morphism: if `X = V_0 ⊔ V_1 ⊔ V_2 ⊔ …` is such a decomposition and
> `f : X' ⟶ X` is a morphism whose source is good and whose preimages of the pieces are good, then
> the preimages form such a decomposition of `X'`.

```lean
theorem isClopenSubspaceDecomposition_preimage {sX : X ⟶ D.space} (f : X' ⟶ X)
    (h : IsClopenSubspaceDecomposition D sX fun i => (V i).ι) (hX' : D.IsGood sX')
    (hpiece : ∀ i, D.IsGood (((V i).preimage f).ι ≫ sX')) :
    IsClopenSubspaceDecomposition D sX' fun i => ((V i).preimage f).ι
```

**`AlgebraicGeometry.Space.cycleGroupDecompositionEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean#L398). The attribute's comment: “the clause CH_*(X') = ∏ CH_*(X'_r), at the level of cycles”.

> Along a decomposition `X = X_0 ⊔ X_1 ⊔ X_2 ⊔ …` of a good algebraic space over the base into
> good open and closed subspaces, the groups of `k`-cycles form a direct product
> `Z_k(X) = ∏_i Z_k(X_i)`, the projections being restriction along the inclusions of the pieces.

```lean
noncomputable def cycleGroupDecompositionEquiv (h : IsClopenSubspaceDecomposition D sX j)
    (k : ℤ) : CycleGroup D sX k ≃+ ∀ i, CycleGroup D (j i ≫ sX) k
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.28, Tag 0ERX](https://stacks.math.columbia.edu/tag/0ERX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
