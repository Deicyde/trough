---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chernClass_eq_of_shortExact_tensorUnit, AlgebraicGeometry.Space.ChowCohomologyAlgebra.totalChernClass_eq_mul_of_shortExact, AlgebraicGeometry.Space.ChowCohomologyAlgebra.totalChernClass_shortExact, AlgebraicGeometry.Space.totalChernCapGraded_eq_prod_one_add_chernCapGraded
statement: formalized
proof: formalized
---

# 82.30 Additivity of Chern classes

Section 82.30 of the Stacks Project, [Tag 0ES6](https://stacks.math.columbia.edu/tag/0ES6). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ES7, a lemma

[Tag 0ES7](https://stacks.math.columbia.edu/tag/0ES7) in the Stacks Project.

**`AlgebraicGeometry.Space.chernClass_eq_of_shortExact_tensorUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTrivialSubmoduleBivariant.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTrivialSubmoduleBivariant.lean#L116). The attribute's comment: “c\_r(E) = 0 and c\_j(E) = c\_j(F), j = 0, ..., r - 1, in A^*(X), for the bivariant Chern classes chernClass of Lemma 0ERZ in A^j(X) = A^j(X → X) over chowGroupCanonical; the ranks r, r - 1 are written r + 1, r”.

> **Stacks 0ES7.** In Situation 0EDT let `X/B` be good and let `ℰ`, `ℱ` be finite locally free
> `𝒪_X`-modules of ranks `r + 1` and `r` which fit into a short exact sequence
> `0 ⟶ 𝒪_X ⟶ ℰ ⟶ ℱ ⟶ 0`. Then
>
>   `c_{r+1}(ℰ) = 0`   and   `c_j(ℰ) = c_j(ℱ)`, `j = 0, …, r`,
>
> in `A^*(X)`: equalities of the Chern classes of Stacks 0ERZ (`AlgebraicGeometry.Space.chernClass`),
> bivariant classes in `A^j(X) = A^j(X → X)` over the Chow groups of Stacks 0EQ6
> (`AlgebraicGeometry.Space.chowCohomologyComponentCanonical`). The ranks `r`, `r - 1` of the source
> are written `r + 1`, `r` here, and `𝒪_X` is the unit of the tensor product of `𝒪_X`-modules
> (`AlgebraicGeometry.Space.modulesTensorUnit_eq`).

```lean
theorem chernClass_eq_of_shortExact_tensorUnit (hX : D.IsGood sX)
    {E F : Modules.{u, u} D.site D.base D.base_mem X hX.1}
    (i : 𝟙_ (Modules.{u, u} D.site D.base D.base_mem X hX.1) ⟶ E) (q : E ⟶ F) (hiq : i ≫ q = 0)
    (hC : (ShortComplex.mk i q hiq).ShortExact) (r : ℕ)
    (hE : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) E (r + 1))
    (hF : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) F r) :
    chernClass D sX hX E (r + 1) hE (Fin.last (r + 1)) = 0 ∧
      ∀ (j : ℕ) (hj : j ≤ r),
        chernClass D sX hX E (r + 1) hE ⟨j, by omega⟩ = chernClass D sX hX F r hF ⟨j, by omega⟩
```

## Tag 0ES8, a lemma

[Tag 0ES8](https://stacks.math.columbia.edu/tag/0ES8) in the Stacks Project.

**`AlgebraicGeometry.Space.ChowCohomologyAlgebra.totalChernClass_eq_mul_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassInvertibleExtension.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassInvertibleExtension.lean#L118). The attribute's comment: “c(E) = c(L) c(F) in the Chow cohomology ring A^*(X) (ChowCohomologyAlgebra, product = composition of bivariant classes) for 0 → L → E → F → 0 exact, L invertible, E, F finite locally free of ranks r + 1, r on a good X/B; c is the total Chern class of 0ERZ, the sum of the bivariant classes c\_j of 0ERY, which cap as Space.chernClass on every test space”.

> **Stacks 0ES8.** In Situation 0EDT let `X/B` be good and let `ℰ`, `ℱ` be finite locally free
> `𝒪_X`-modules of ranks `r + 1` and `r` which fit into a short exact sequence
> `0 → ℒ → ℰ → ℱ → 0` with `ℒ` invertible. Then
>
>   `c(ℰ) = c(ℒ) c(ℱ)`   in `A^*(X)`.
>
> Here `A^*(X)` is the Chow cohomology ring of Stacks 0ERK
> (`AlgebraicGeometry.Space.ChowCohomologyAlgebra`, the product being composition of bivariant
> classes), and `c(-)` is the total Chern class of Definition 0ERZ
> (`AlgebraicGeometry.Space.ChowCohomologyAlgebra.totalChernClass`), the sum of the bivariant
> classes `c_j(-)` of Stacks 0ERY, whose cap operations on every good test space are those of
> `AlgebraicGeometry.Space.chernClass` (`ChowCohomologyClass.chernClass_cap_eq`); `ℒ` has rank one.
> The source's ranks `r`, `r - 1` are `r + 1`, `r` here.

```lean
theorem totalChernClass_eq_mul_of_shortExact
    {L E F : Modules.{u, u} D.site D.base D.base_mem X hX.1}
    (i : L ⟶ E) (q : E ⟶ F) (hiq : i ≫ q = 0) (hC : (ShortComplex.mk i q hiq).ShortExact)
    (hL : IsInvertibleModule (PrivateChern.goodSpace hX) L) (r : ℕ)
    (hE : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) E (r + 1))
    (hF : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) F r) :
    ChowCohomologyAlgebra.totalChernClass D sX hX E (r + 1) hE =
      ChowCohomologyAlgebra.totalChernClass D sX hX L 1
          (isFiniteLocallyFreeOfRank_one_of_isInvertibleModule (PrivateChern.goodSpace hX) hL) *
        ChowCohomologyAlgebra.totalChernClass D sX hX F r hF
```

## Tag 0ES9, a lemma

[Tag 0ES9](https://stacks.math.columbia.edu/tag/0ES9) in the Stacks Project.

**`AlgebraicGeometry.Space.ChowCohomologyAlgebra.totalChernClass_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassWhitneyAlgebra.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassWhitneyAlgebra.lean#L73). The attribute's comment: “c(E) = c(E\_1) c(E\_2) in the Chow cohomology ring A^*(X) (ChowCohomologyAlgebra, product = composition of bivariant classes) for 0 → E\_1 → E → E\_2 → 0 exact with E\_i finite locally free of rank r\_i on a good X/B; c is the total Chern class of 0ERZ, the sum of the bivariant classes c\_j of 0ERY, which cap as Space.chernClass on every test space”.

> **Stacks 0ES9, the Whitney formula.** In Situation 0EDT let `X/B` be good and let
> `0 → ℰ₁ → ℰ → ℰ₂ → 0` be a short exact sequence `T` of finite locally free `𝒪_X`-modules, `ℰ₁` of
> rank `r₁` and `ℰ₂` of rank `r₂`, so that `ℰ` is finite locally free of rank `r₁ + r₂`
> (`AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank.of_shortExact`). Then
>
>   `c(ℰ) = c(ℰ₁) c(ℰ₂)`   in `A^*(X)`.
>
> Here `A^*(X)` is the Chow cohomology ring of Stacks 0ERK
> (`AlgebraicGeometry.Space.ChowCohomologyAlgebra`, the product being composition of bivariant
> classes), and `c(-)` is the total Chern class of Definition 0ERZ
> (`AlgebraicGeometry.Space.ChowCohomologyAlgebra.totalChernClass`), the sum of the bivariant
> classes `c_j(-)` of Stacks 0ERY, whose cap operations on every good test space are those of
> `AlgebraicGeometry.Space.chernClass` (`ChowCohomologyClass.chernClass_cap_eq`).

```lean
theorem totalChernClass_shortExact
    {T : ShortComplex (Modules.{u, u} D.site D.base D.base_mem X hX.1)} (hT : T.ShortExact)
    {r₁ r₂ : ℕ}
    (h₁ : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) T.X₁ r₁)
    (h₂ : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X hX.1) T.X₃ r₂) :
    ChowCohomologyAlgebra.totalChernClass D sX hX T.X₂ (r₁ + r₂)
        (RingedSite.IsFiniteLocallyFreeOfRank.of_shortExact _ hT h₁ h₂) =
      ChowCohomologyAlgebra.totalChernClass D sX hX T.X₁ r₁ h₁ *
        ChowCohomologyAlgebra.totalChernClass D sX hX T.X₃ r₂ h₂
```

## Tag 0ESA, a lemma

[Tag 0ESA](https://stacks.math.columbia.edu/tag/0ESA) in the Stacks Project.

**`AlgebraicGeometry.Space.totalChernCapGraded_eq_prod_one_add_chernCapGraded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassFiltration.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassFiltration.lean#L231). The attribute's comment: “c(E) = ∏ (1 + c\_1(L\_i)) in A^*(X) for the Chern classes of Definition 0ERZ (chernClass, totalChernClass), as the identity of their cap operations c(E) ∩ - and ∏ (1 + c\_1(L\_i) ∩ -) of Lemma 0ERY on ⊕\_k CH\_k(X') for every good test space X' → X”.

> **Stacks 0ESA, the total Chern class of a module with a filtration with invertible
> quotients.** In Situation 0EDT let `X/B` be good, let `ℒ_1, …, ℒ_r` be invertible `𝒪_X`-modules
> and let `ℰ` be a finite locally free `𝒪_X`-module of rank `r` with a filtration
> `0 = ℰ_0 ⊂ ℰ_1 ⊂ ⋯ ⊂ ℰ_r = ℰ` such that `ℰ_i / ℰ_{i-1} ≅ ℒ_i` (a monotone family `F` of
> subobjects of `ℰ` with `F 0 = ⊥`, `F r = ⊤` and identifications `e i` of the successive
> quotients). With `x_i = c₁(ℒ_i)`, `c(ℰ) = ∏_{i=1}^r (1 + x_i)` in `A^*(X)`.
>
> The classes are those of Stacks 0ERZ, `c_j(ℰ) ∈ A^j(X)` (`AlgebraicGeometry.Space.chernClass`)
> and `c(ℰ) = ∑_j c_j(ℰ)` (`AlgebraicGeometry.Space.totalChernClass`), with `x_i = c₁(ℒ_i)` the
> class `c_1` of the module `ℒ_i` of rank one. The product of `A^*(X)` is composition (Stacks
> 0ERK) and a bivariant class is determined by its cap operations on the good test spaces
> `g : X' ⟶ X` (Stacks 0ERJ), the cap operation of `c_j(ℰ)` on `X'` being `c_j(ℰ) ∩ -` of
> Stacks 0ERY (`AlgebraicGeometry.Space.chernClass_cap`). The identity is stated as that of the
> cap operations on `⨁_k CH_k(X')` for every good `g : X' ⟶ X`: `c(ℰ) ∩ -` is
> `totalChernCapGraded` and `c₁(ℒ_i) ∩ -` is `chernCapGraded` at `j = 1`.

```lean
theorem totalChernCapGraded_eq_prod_one_add_chernCapGraded {r : ℕ}
    (L : Fin r → Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hL : ∀ i, IsInvertibleModule (goodSpace hX) (L i))
    (E : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hE : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX E r)
    (F : Fin (r + 1) → Subobject E) (hF : Monotone F) (h0 : F 0 = ⊥) (hr : F (Fin.last r) = ⊤)
    (e : ∀ i : Fin r, cokernel (ofLE (F i.castSucc) (F i.succ) (hF i.castSucc_le_succ)) ≅ L i)
    {Y : D.Ambient} (g : Y ⟶ X) (hY : D.IsGood (g ≫ sX)) :
    totalChernCapGraded D sX hX E r hE g hY = (List.ofFn fun i => 1 +
      chernCapGraded D sX hX (L i) 1
        (isFiniteLocallyFreeOfRank_one_of_isInvertibleModule (goodSpace hX) (hL i)) g hY
          1).prod
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.30, Tag 0ES6](https://stacks.math.columbia.edu/tag/0ES6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
