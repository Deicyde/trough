---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chernCap_eq_of_shortExact_tensorUnit, AlgebraicGeometry.Space.PrivateChern.chernCap_succ_eq_of_shortExact, AlgebraicGeometry.Space.totalChernCap_shortExact, AlgebraicGeometry.Space.PrivateChern.totalChernCap_eq_prod_one_add_chernCap_one
statement: formalized
proof: formalized
---

# 82.30 Additivity of Chern classes

Section 82.30 of the Stacks Project, [Tag 0ES6](https://stacks.math.columbia.edu/tag/0ES6). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ES7, a lemma

[Tag 0ES7](https://stacks.math.columbia.edu/tag/0ES7) in the Stacks Project.

**`AlgebraicGeometry.Space.chernCap_eq_of_shortExact_tensorUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTrivialSubmodule.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTrivialSubmodule.lean#L80).

> **Stacks 0ES7.** In Situation 0EDT let `X/B` be good and let `ℰ`, `ℱ` be finite locally free
> `𝒪_X`-modules of ranks `r + 1` and `r` fitting into a short exact sequence
> `0 ⟶ 𝒪_X ⟶ ℰ ⟶ ℱ ⟶ 0`. Then
>
>   `c_{r+1}(ℰ) = 0`   and   `c_j(ℰ) = c_j(ℱ)` for `j = 0, …, r`.
>
> The Chern classes are those of Stacks 0ERZ, `c_n(ℰ) ∩ -` on `CH_*(X)` (`chernCap`), and `𝒪_X` is
> the unit of the tensor product of `𝒪_X`-modules (`AlgebraicGeometry.Space.modulesTensorUnit_eq`).
> A relation in `A^*(X)` is equality of the operations on `CH_*(Y)` for every good `Y ⟶ X`
> (Section 0ES3); the pullback of the sequence to `Y` is again such a sequence (with `𝒪_Y` as first
> term and the same ranks), so the statement over every good `X` is the relation in `A^*(X)`.

```lean
theorem chernCap_eq_of_shortExact_tensorUnit (hX : D.IsGood sX)
    {E F : Modules.{u, u} D.site D.base D.base_mem X hX.1}
    (i : 𝟙_ (Modules.{u, u} D.site D.base D.base_mem X hX.1) ⟶ E) (q : E ⟶ F) (hiq : i ≫ q = 0)
    (hC : (ShortComplex.mk i q hiq).ShortExact) (r : ℕ)
    (hE : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX E (r + 1))
    (hF : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX F r) :
    chernCap.{u, u + 1} E (r + 1) hE (r + 1) = 0 ∧
      ∀ j ≤ r, chernCap.{u, u + 1} E (r + 1) hE j = chernCap.{u, u + 1} F r hF j
```

## Tag 0ES8, a lemma

[Tag 0ES8](https://stacks.math.columbia.edu/tag/0ES8) in the Stacks Project.

**`AlgebraicGeometry.Space.PrivateChern.chernCap_succ_eq_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrivateChern/ChernCapInvertibleSubmodule.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrivateChern/ChernCapInvertibleSubmodule.lean#L306).

> **Stacks 0ES8.** Let `X/B` be a good algebraic space (Situation 0EDT) and
> `0 ⟶ ℒ ⟶ ℰ ⟶ ℱ ⟶ 0` a short exact sequence of `𝒪_X`-modules with `ℒ` invertible and `ℰ`, `ℱ`
> finite locally free of ranks `r + 1` and `r`. Then `c(ℰ) = c(ℒ) c(ℱ)`, degree by degree:
>
>   `c_{n+1}(ℰ) ∩ - = c_{n+1}(ℱ) ∩ - + c₁(ℒ) ∩ (c_n(ℱ) ∩ -)` on `CH_*(X)`.
>
> A relation between bivariant classes in `A^*(X)` is equality of the operations on `CH_*(Y)` for
> every good `Y ⟶ X` (Section 0ES3); since the pullback of the sequence to `Y` is again such a
> sequence, the statement over every good `X` is the relation in `A^*(X)`.

```lean
theorem chernCap_succ_eq_of_shortExact {L E F : Modules.{u, u} D.site D.base D.base_mem X hX.1}
    (i : L ⟶ E) (q : E ⟶ F) (hiq : i ≫ q = 0) (hC : (ShortComplex.mk i q hiq).ShortExact)
    (hL : IsInvertibleModule (goodSpace hX) L) (r : ℕ)
    (hE : IsFiniteLocallyFreeOfRank D sX hX E (r + 1)) (hF : IsFiniteLocallyFreeOfRank D sX hX F r)
    (n : ℕ) :
    chernCap.{u, u + 1} E (r + 1) hE (n + 1) =
      chernCap.{u, u + 1} F r hF (n + 1) +
        chernCap.{u, u + 1} L 1 (isFiniteLocallyFreeOfRank_one_of_isInvertibleModule
          (goodSpace hX) hL) 1 * chernCap.{u, u + 1} F r hF n
```

## Tag 0ES9, a lemma

[Tag 0ES9](https://stacks.math.columbia.edu/tag/0ES9) in the Stacks Project.

**`AlgebraicGeometry.Space.totalChernCap_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassWhitney.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassWhitney.lean#L45).

> **Stacks 0ES9, the Whitney formula.** In Situation 0EDT let `X/B` be good and let
> `0 ⟶ ℰ₁ ⟶ ℰ ⟶ ℰ₂ ⟶ 0` be a short exact sequence `T` of finite locally free `𝒪_X`-modules, `ℰ₁` of
> rank `r₁` and `ℰ₂` of rank `r₂`; then `ℰ` is finite locally free of rank `r₁ + r₂`
> (`AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank.of_shortExact`). The total Chern classes
> satisfy `c(ℰ) = c(ℰ₁) c(ℰ₂)`.
>
> The Chern classes are those of Stacks 0ERZ, `c_n(ℰ) ∩ -` on `CH_*(X)` (`chernCap`), and
> `c(ℰ) = c_0(ℰ) + ⋯ + c_r(ℰ)` (`totalChernCap`). An identity in `A^*(X)` is an identity of the
> operations on `CH_*(Y)` for every good `Y ⟶ X`; the operation of `c_n(ℰ)` on `CH_*(Y)` is
> `c_n(f^*ℰ) ∩ -`, and the inverse image along `f` of a short exact sequence of finite locally free
> modules is again one, of modules of the same ranks, so the statement for all good `X` is the
> statement in `A^*(X)`.

```lean
theorem totalChernCap_shortExact {X : D.Ambient} {sX : X ⟶ D.space} (hX : D.IsGood sX)
    {T : ShortComplex (Modules.{u, u} D.site D.base D.base_mem X hX.1)} (hT : T.ShortExact)
    {r₁ r₂ : ℕ} (h₁ : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX T.X₁ r₁)
    (h₂ : PrivateChern.IsFiniteLocallyFreeOfRank D sX hX T.X₃ r₂) :
    totalChernCap.{u, u + 1} T.X₂ (r₁ + r₂)
        (RingedSite.IsFiniteLocallyFreeOfRank.of_shortExact _ hT h₁ h₂) =
      totalChernCap.{u, u + 1} T.X₁ r₁ h₁ * totalChernCap.{u, u + 1} T.X₃ r₂ h₂
```

## Tag 0ESA, a lemma

[Tag 0ESA](https://stacks.math.columbia.edu/tag/0ESA) in the Stacks Project.

**`AlgebraicGeometry.Space.PrivateChern.totalChernCap_eq_prod_one_add_chernCap_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrivateChern/TotalChernClassFiltration.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrivateChern/TotalChernClassFiltration.lean#L51).

> **Stacks 0ESA, the total Chern class of a module with a filtration with invertible
> quotients.** In Situation 0EDT let `X/B` be good, let `ℒ_1, …, ℒ_r` be invertible `𝒪_X`-modules
> and let `ℰ` be a finite locally free `𝒪_X`-module of rank `r` with a filtration
> `0 = ℰ_0 ⊂ ℰ_1 ⊂ ⋯ ⊂ ℰ_r = ℰ` such that `ℰ_i / ℰ_{i-1} ≅ ℒ_i` (a monotone family `F` of subobjects
> of `ℰ` with `F 0 = ⊥`, `F r = ⊤` and identifications `e i` of the successive quotients). With
> `x_i = c₁(ℒ_i)`, `c(ℰ) = ∏_{i=1}^r (1 + x_i)`.
>
> The Chern classes are those of Stacks 0ERZ, `c_n(ℰ) ∩ -` on `CH_*(X)` (`chernCap`), and
> `c(ℰ) = c_0(ℰ) + ⋯ + c_r(ℰ)` (`totalChernCap`). An identity in `A^*(X)` is an identity of the
> operations on `CH_*(Y)` for every good `Y ⟶ X`; the operation of `c_n(ℰ)` on `CH_*(Y)` is
> `c_n(f^*ℰ) ∩ -`, and the inverse image along `f` of the filtration is again a filtration of
> `f^*ℰ` with invertible quotients `f^*ℒ_i`, so the statement for all good `X` is the statement in
> `A^*(X)`.

```lean
theorem totalChernCap_eq_prod_one_add_chernCap_one
    {r : ℕ}
    (L : Fin r → Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hL : ∀ i, IsInvertibleModule (goodSpace hX) (L i))
    (E : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hE : IsFiniteLocallyFreeOfRank D sX hX E r)
    (F : Fin (r + 1) → Subobject E) (hF : Monotone F) (h0 : F 0 = ⊥) (hr : F (Fin.last r) = ⊤)
    (e : ∀ i : Fin r, cokernel (ofLE (F i.castSucc) (F i.succ) (hF i.castSucc_le_succ)) ≅ L i) :
    totalChernCap.{u, u + 1} E r hE = (List.ofFn fun i ↦ 1 +
      chernCap.{u, u + 1} (L i) 1
        (isFiniteLocallyFreeOfRank_one_of_isInvertibleModule (goodSpace hX) (hL i)) 1).prod
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.30, Tag 0ES6](https://stacks.math.columbia.edu/tag/0ES6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
