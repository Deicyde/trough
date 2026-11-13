---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsUnique_chernCap_and_bivariant, AlgebraicGeometry.Space.chernClass, AlgebraicGeometry.Space.totalChernClass, AlgebraicGeometry.Space.chernClass_one_eq_firstChernBivariantClass, AlgebraicGeometry.Space.ChowCohomologyClass.comp_chernCohomologyClass, AlgebraicGeometry.Space.commute_of_chernCohomologyClass, AlgebraicGeometry.Space.chernCap_apply_chernCap_comm, AlgebraicGeometry.Space.chernClassOfFiniteLocallyFree
statement: formalized
proof: formalized
---

# 82.28 The Chern classes of a vector bundle

Section 82.28 of the Stacks Project, [Tag 0ERX](https://stacks.math.columbia.edu/tag/0ERX). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ERY, a lemma

[Tag 0ERY](https://stacks.math.columbia.edu/tag/0ERY) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_chernCap_and_bivariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean, line 1198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean#L1198). The attribute's comment: “existence and uniqueness of c\_i(E) ∩ - : CH\_k(X') → CH\_\{k-i}(X'), i = 0..r, with c\_0 = id and sum\_i (-1)^i c\_1(O\_\{P'}(1))^i ∩ π'^*(c\_\{r-i}(E) ∩ α) = 0 on P' = P ×\_X X', for every morphism X' → X of good spaces over B, E finite locally free of rank r on a good X/B; and the maps c\_i(E) ∩ - form a bivariant class of degree i (BivariantClassCanonical, over chowGroupCanonical)”.

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

**`AlgebraicGeometry.Space.chernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean, line 1149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean#L1149). The attribute's comment: “the i-th Chern class c\_i(E) ∈ A^i(X), i = 0, ..., r, the bivariant class of degree i of Lemma 0ERY, for E finite locally free of rank r on a good X/B; A^i(X) = A^i(X → X) over the Chow groups chowGroupCanonical”.

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

**`AlgebraicGeometry.Space.totalChernClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean, line 1172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassBivariant.lean#L1172). The attribute's comment: “the total Chern class c(E) = c\_0(E) + c\_1(E) + ... + c\_r(E), the formal sum of the Chern classes as a nonhomogeneous class in A^*(X) = ⊕\_p A^p(X)”.

> **Stacks 0ERZ: the total Chern class** `c(ℰ) = c₀(ℰ) + c₁(ℰ) + … + c_r(ℰ)`, the formal sum of
> the Chern classes of `ℰ` (`AlgebraicGeometry.Space.chernClass`), a nonhomogeneous class in the
> Chow cohomology `A^*(X) = ⊕_p A^p(X)` (`AlgebraicGeometry.Space.chowCohomologyCanonical`).

```lean
def totalChernClass : chowCohomologyCanonical.{u + 1} D sX hX
```

## Tag 0ES0, a lemma

[Tag 0ES0](https://stacks.math.columbia.edu/tag/0ES0) in the Stacks Project.

**`AlgebraicGeometry.Space.chernClass_one_eq_firstChernBivariantClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassRankOneBivariant.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassRankOneBivariant.lean#L320). The attribute's comment: “c\_1(L) ∈ A^1(X) of Definition 0ERZ (chernClass, characterized by the projective bundle relation of Lemma 0ERY) equals the bivariant class c\_1(f^*L) ∩ - of Lemma 0ERM, as elements of A^1(X), for X/B good and L invertible”.

> **Stacks 0ES0.** In Situation 0EDT let `X/B` be good and let `ℒ` be an invertible
> `𝒪_X`-module. Then the first Chern class `c₁(ℒ) ∈ A^1(X)` of Definition 0ERZ
> (`AlgebraicGeometry.Space.chernClass` at rank `1` and index `1`, the bivariant class whose cap
> operations are the maps characterized by the projective bundle relation of Stacks 0ERY) is equal
> to the bivariant class `c₁(f^*ℒ) ∩ -` of Lemma 0ERM
> (`AlgebraicGeometry.Space.firstChernBivariantClass`), as elements of
> `A^1(X) = A^1(X → X)` (`AlgebraicGeometry.Space.chowCohomologyComponentCanonical`).

```lean
theorem chernClass_one_eq_firstChernBivariantClass :
    Space.chernClass D sX hX L 1
        ((isInvertibleModule_iff_isFiniteLocallyFreeOfRank_one (Z := goodSpace hX) L).1 hL)
        (Fin.last 1) =
      firstChernBivariantClass D sX hX L hL
```

## Tag 0ES1, a lemma

[Tag 0ES1](https://stacks.math.columbia.edu/tag/0ES1) in the Stacks Project.

**`AlgebraicGeometry.Space.ChowCohomologyClass.comp_chernCohomologyClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCentral.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCentral.lean#L418). The attribute's comment: “the main assertion: c\_j(E) ∈ A^j(X), the Chern class of Lemma 0ERY / Definition 0ERZ (chernCohomologyClass, the class chernClass read in A^j(X)), commutes with every c ∈ A^p(X): c ∘ c\_j(E) = c\_j(E) ∘ c, composition being the product of A^*(X) (0ERK). The source's c\_j(L) is a typo for c\_j(E)”.

> **Stacks 0ES1.** In Situation 0EDT let `X/B` be good and let `ℰ` be a finite locally free
> `𝒪_X`-module of rank `r`. Then `c_j(ℰ) ∈ A^j(X)` commutes with every `c ∈ A^p(X)`:
> `c ∘ c_j(ℰ) = c_j(ℰ) ∘ c` in `A^{p+j}(X) = A^{j+p}(X)`, the product of Stacks 0ERK being
> composition of bivariant classes (`AlgebraicGeometry.Space.ChowCohomologyClass.comp`). Here
> `c_j(ℰ)` is the Chern class of Stacks 0ERY and 0ERZ (`AlgebraicGeometry.Space.chernCohomologyClass`,
> the class `AlgebraicGeometry.Space.chernClass` read in `A^j(X)`). (The source's `c_j(ℒ)` is a
> typo for `c_j(ℰ)`.)

```lean
theorem ChowCohomologyClass.comp_chernCohomologyClass {p : ℤ} (c : ChowCohomologyClass D sX hX p)
    (j : Fin (r + 1)) :
    (⟨p + ((j : ℕ) : ℤ), c.comp (chernCohomologyClass E r hE j)⟩ :
        GradedMonoid (ChowCohomologyClass D sX hX)) =
      ⟨((j : ℕ) : ℤ) + p, (chernCohomologyClass E r hE j).comp c⟩
```

**`AlgebraicGeometry.Space.commute_of_chernCohomologyClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCentral.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCentral.lean#L439). The attribute's comment: “the main assertion in the algebra A^*(X) of 0ERK: c\_j(E) (chernCohomologyClass, the class chernClass of 0ERZ read in A^j(X)) commutes with every element of A^*(X) = ⊕\_p A^p(X), in particular with every c ∈ A^p(X)”.

> **Stacks 0ES1**, in the Chow cohomology algebra: `c_j(ℰ)` commutes with every element of
> `A^*(X) = ⊕_p A^p(X)` (`AlgebraicGeometry.Space.ChowCohomologyAlgebra`), so lies in its centre.

```lean
theorem commute_of_chernCohomologyClass (j : Fin (r + 1)) (x : ChowCohomologyAlgebra D sX hX) :
    Commute (DirectSum.of (ChowCohomologyClass D sX hX) ((j : ℕ) : ℤ)
      (chernCohomologyClass E r hE j)) x
```

**`AlgebraicGeometry.Space.chernCap_apply_chernCap_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCentral.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassCentral.lean#L461). The attribute's comment: “in particular: c\_i(E) ∩ c\_j(F) ∩ α = c\_j(F) ∩ c\_i(E) ∩ α in CH\_\{k-i-j} for every α ∈ CH\_k, E, F finite locally free of ranks r, s on X, the Chern classes being chernCap of Lemma 0ERY; stated on every good X' → X, X' = X included”.

> **Stacks 0ES1, in particular.** In Situation 0EDT let `X/B` be good and let `ℰ`, `ℱ` be finite
> locally free `𝒪_X`-modules of ranks `r` and `s`. Then for every good `g : X' ⟶ X` (for instance
> `X' = X`) and every `α ∈ CH_k(X')`,
>
>   `c_i(ℰ) ∩ c_j(ℱ) ∩ α = c_j(ℱ) ∩ c_i(ℰ) ∩ α`  in `CH_{k-i-j}(X')`,
>
> the Chern classes being those of Stacks 0ERY and 0ERZ (`AlgebraicGeometry.Space.chernCap`), and
> `CH_{k-j-i} = CH_{k-i-j}` the identification of equal degrees.

```lean
theorem chernCap_apply_chernCap_comm (F : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (s : ℕ) (hF : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) F s)
    (i : Fin (r + 1)) (j : Fin (s + 1)) {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX))
    (k : ℤ) (α : chowGroupCanonical.{u + 1} D (g ≫ sX) hY k) :
    chernCap D sX hX E r hE g hY i (k - ((j : ℕ) : ℤ)) (chernCap D sX hX F s hF g hY j k α) =
      ProjectiveBundleRelation.degreeCast (fun m => chowGroupCanonical.{u + 1} D (g ≫ sX) hY m)
        (by ring)
        (chernCap D sX hX F s hF g hY j (k - ((i : ℕ) : ℤ)) (chernCap D sX hX E r hE g hY i k α))
```

## Tag 0ES2, a remark

[Tag 0ES2](https://stacks.math.columbia.edu/tag/0ES2) in the Stacks Project.

**`AlgebraicGeometry.Space.chernClassOfFiniteLocallyFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean#L280). The attribute's comment: “the definition: c\_i(E) ∈ A^i(X) for E finite locally free of non-constant rank, the bivariant class preserving CH\_*(X') = ∏\_r CH\_*(X'\_r) and acting by c\_i(E|\_\{X\_r}) ∩ - on the factors”.

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

**`AlgebraicGeometry.Space.rankDecomposition_chowGroup_chernClassOfFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassNonConstantRank.lean#L322). The attribute's comment: “the whole remark: X = ∐\_r X\_r by the rank of E (open and closed), its pullback to every morphism X' → X of good spaces over B, CH\_k(X') = ∏\_r CH\_k(X'\_r) on Chow groups, and c\_i(E) ∈ A^i(X) as the unique bivariant class preserving these decompositions and acting by c\_i(E|\_\{X\_r}) ∩ - on the factors”.

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
      (∀ {Y : D.Ambient} (g : Y ⟶ X), D.IsGood (g ≫ sX) →
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

**`AlgebraicGeometry.Space.isClopenSubspaceDecomposition_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean#L279). The attribute's comment: “the decomposition of X' obtained by pullback”.

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

**`AlgebraicGeometry.Space.cycleGroupDecompositionEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ClopenDecomposition.lean#L398). The attribute's comment: “the clause CH\_*(X') = ∏ CH\_*(X'\_r), at the level of cycles”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
