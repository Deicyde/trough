---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_projectiveBundleTower_hasInjectiveChowPullbacks_filtration, AlgebraicGeometry.Space.PrivateChern.chernCap_moduleDual, AlgebraicGeometry.Space.PrivateChern.chernCap_tensorObj
statement: formalized
proof: formalized
---

# 82.31 The splitting principle

Section 82.31 of the Stacks Project, [Tag 0ESB](https://stacks.math.columbia.edu/tag/0ESB). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ESC, a lemma

[Tag 0ESC](https://stacks.math.columbia.edu/tag/0ESC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_projectiveBundleTower_hasInjectiveChowPullbacks_filtration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/SplittingPrinciple.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/SplittingPrinciple.lean#L68).

> **Stacks 0ESC, the splitting principle.** Let `X/B` be good and `ℰ_i`, `i ∈ ι` finite, finite
> locally free `𝒪_X`-modules of ranks `r_i`. There are a good algebraic space `P/B` and a morphism
> `π : P ⟶ X` over `B`, flat of some relative dimension `d` and a finite composite of projective
> bundle projections, such that
>
> * for every morphism `Y ⟶ X` of good algebraic spaces over `B` the flat pullback
>   `CH_k(Y) ⟶ CH_{k+d}(Y ×_X P)` is injective (`HasInjectiveChowPullbacks`), and
> * every `π^*ℰ_i` has a filtration `0 = F_0 ⊆ F_1 ⊆ ⋯ ⊆ F_{r_i} = π^*ℰ_i` by subobjects whose
>   successive quotients `F_{j+1}/F_j` are invertible `𝒪_P`-modules.
>
> The Chow groups are those whose rational equivalences are indexed by families in
> the universe `u + 1` of the integral closed subspaces of the spaces involved, which is the universe
> in which rational equivalence on algebraic spaces over the universe-`u` site is defined.

```lean
theorem exists_projectiveBundleTower_hasInjectiveChowPullbacks_filtration
    {ι : Type*} [Finite ι] (X : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u)
    (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (E : ι → Modules.{u, u} D.site D.base D.base_mem X hX.1) (r : ι → ℕ)
    (hE : ∀ i, PrivateChern.IsFiniteLocallyFreeOfRank D sX hX (E i) (r i)) :
    ∃ (P : (BigFppfOver D.site D.base D.base_mem)ᵒᵖ ⥤ Type u) (sP : P ⟶ D.space)
      (hP : D.IsGood sP) (π : P ⟶ X) (hπ : π ≫ sX = sP)
      (d : ℕ) (hflat : IsFlat D.site D.base D.base_mem π)
      (hd : HasRelativeDimension d D.site D.base D.base_mem π),
      IsProjectiveBundleTower π ∧ HasInjectiveChowPullbacks.{u + 1} D sX hX sP hP π hπ d hflat hd ∧
        ∀ i, ∃ (F : Fin (r i + 1) → Subobject ((spaceModulePullback D hX.1 hP.1 π).obj (E i)))
          (hF : Monotone F), F 0 = ⊥ ∧ F (Fin.last (r i)) = ⊤ ∧
            ∀ j : Fin (r i), IsInvertibleModule ⟨P, hP.1⟩
              (cokernel (Subobject.ofLE (F j.castSucc) (F j.succ) (hF j.castSucc_le_succ)))
```

## Tag 0ESD, a lemma

[Tag 0ESD](https://stacks.math.columbia.edu/tag/0ESD) in the Stacks Project.

**`AlgebraicGeometry.Space.PrivateChern.chernCap_moduleDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrivateChern/ChernClassDual.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/PrivateChern/ChernClassDual.lean#L49).

> **Stacks 0ESD: the Chern classes of the dual.** Let `X/B` be good and `ℰ` a finite locally
> free `𝒪_X`-module with dual `ℰ^∨ = ℋom(ℰ, 𝒪_X)`. Then `c_i(ℰ^∨) = (-1)^i c_i(ℰ)` in `A^i(X)`: for
> every morphism `f : Y ⟶ X` of good algebraic spaces over `B` along which `f^*ℰ` has rank `r`,
> `c_i(f^*ℰ^∨) ∩ - = (-1)^i c_i(f^*ℰ) ∩ -` on `CH_*(Y)`.

```lean
theorem chernCap_moduleDual (E : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    (hE : SheafOfModules.IsFiniteLocallyFreeOnSite E) {Y : D.Ambient} (f : Y ⟶ X)
    (hY : D.IsGood (f ≫ sX)) (r : ℕ)
    (hr : IsFiniteLocallyFreeOfRank D (f ≫ sX) hY ((spaceModulePullback D hX.1 hY.1 f).obj E) r)
    (i : ℕ) :
    chernCap.{u, u + 1} (hX := hY)
        ((spaceModulePullback D hX.1 hY.1 f).obj ((ihom E).obj (𝟙_ _))) r
        (isFiniteLocallyFreeOfRank_modulePullback_dual
          (ObjectProperty.homMk f : (⟨Y, hY.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
            ⟨X, hX.1⟩) E hE hr) i =
      (-1 : ℤ) ^ i •
        chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj E) r hr i
```

## Tag 0ESE, a lemma

[Tag 0ESE](https://stacks.math.columbia.edu/tag/0ESE) in the Stacks Project.

**`AlgebraicGeometry.Space.PrivateChern.chernCap_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTensorUnconditional.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChernClassTensorUnconditional.lean#L64). The attribute's comment: “c₂ corrected to the degree-two part of ∏ (1 + x\_i + y\_j); the printed c₂ is false”.

> **Stacks 0ESE.** For finite locally free `ℰ`, `ℱ` of ranks `r`, `s` on a good algebraic space
> `X/B`:
>
> * on every good `f : Y ⟶ X`, as operations on `CH_*(Y)`,
>   `c₁(f^*(ℰ ⊗ ℱ)) = r c₁(f^*ℱ) + s c₁(f^*ℰ)` and
>   `c₂(f^*(ℰ ⊗ ℱ)) = r c₂(f^*ℱ) + s c₂(f^*ℰ) + C(r,2) c₁(f^*ℱ)² + (r s - 1) c₁(f^*ℱ) c₁(f^*ℰ) +
>   C(s,2) c₁(f^*ℰ)²`;
> * "and so on (see proof)": on a splitting `π : P ⟶ X` (flat, with injective flat pullback after
>   every base change) with invertible `ℒ_i`, `𝒩_j` and `x_i = c₁(ℒ_i)`, `y_j = c₁(𝒩_j)`,
>   `c(π^*ℰ) = ∏ (1 + x_i)`, `c(π^*ℱ) = ∏ (1 + y_j)` and `c(π^*(ℰ ⊗ ℱ)) = ∏_{i,j} (1 + x_i + y_j)`.
>
> The source prints `c₂(ℰ ⊗ ℱ) = r² c₂(ℱ) + r s c₁(ℱ) c₁(ℰ) + s² c₂(ℰ)`, which is false: for
> `r = s = 1`, `ℰ = 𝒪(1, 0)` and `ℱ = 𝒪(0, 1)` on `𝐏¹ × 𝐏¹`, `ℰ ⊗ ℱ` is invertible so
> `c₂(ℰ ⊗ ℱ) = 0`, while `c₁(ℱ) c₁(ℰ) ∩ [𝐏¹ × 𝐏¹]` is the class of a point, which is not zero. The
> identity stated here is the degree two part of the source's own product formula
> `∏_{i,j} (1 + x_i + y_j)` (Stacks 0FA6; Fulton, *Intersection theory*, Example 3.2.2).

```lean
theorem chernCap_tensorObj
    (E F : Modules.{u, u} D.site D.base D.base_mem X hX.1) (r s : ℕ)
    (hr : IsFiniteLocallyFreeOfRank D sX hX E r) (hs : IsFiniteLocallyFreeOfRank D sX hX F s) :
    (∀ {Y : D.Ambient} (f : Y ⟶ X) (hY : D.IsGood (f ≫ sX)),
      let hrY := isFiniteLocallyFreeOfRank_modulePullback D.site D.base D.base_mem
        (ObjectProperty.homMk f : (⟨Y, hY.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
          ⟨X, hX.1⟩) hr
      let hsY := isFiniteLocallyFreeOfRank_modulePullback D.site D.base D.base_mem
        (ObjectProperty.homMk f : (⟨Y, hY.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
          ⟨X, hX.1⟩) hs
      let hrsY := isFiniteLocallyFreeOfRank_modulePullback D.site D.base D.base_mem
        (ObjectProperty.homMk f : (⟨Y, hY.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
          ⟨X, hX.1⟩) (isFiniteLocallyFreeOfRank_tensorObj D.site D.base D.base_mem X hX.1 hr hs)
      chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj (E ⊗ F)) (r * s)
          hrsY 1 =
          (r : ℤ) • chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj F) s
              hsY 1 +
            (s : ℤ) • chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj E) r
              hrY 1 ∧
        chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj (E ⊗ F)) (r * s)
            hrsY 2 =
          (r : ℤ) • chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj F) s
              hsY 2 +
            (s : ℤ) • chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj E) r
              hrY 2 +
            (r.choose 2 : ℤ) • chernCap.{u, u + 1} (hX := hY)
              ((spaceModulePullback D hX.1 hY.1 f).obj F) s hsY 1 ^ 2 +
            ((r : ℤ) * s - 1) •
              (chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj F) s hsY 1 *
                chernCap.{u, u + 1} (hX := hY) ((spaceModulePullback D hX.1 hY.1 f).obj E) r
                  hrY 1) +
            (s.choose 2 : ℤ) • chernCap.{u, u + 1} (hX := hY)
              ((spaceModulePullback D hX.1 hY.1 f).obj E) r hrY 1 ^ 2) ∧
    ∃ (P : D.Ambient) (π : P ⟶ X) (hP : D.IsGood (π ≫ sX))
      (d : ℕ) (_ : IsFlat D.site D.base D.base_mem π)
      (_ : HasRelativeDimension d D.site D.base D.base_mem π),
      HasInjectiveChowBaseChange.{u + 1} D sX π d ∧
      ∃ (L : Fin r → Modules.{u, u} D.site D.base D.base_mem P hP.1)
        (N : Fin s → Modules.{u, u} D.site D.base D.base_mem P hP.1)
        (hL : ∀ i, IsFiniteLocallyFreeOfRank D (π ≫ sX) hP (L i) 1)
        (hN : ∀ j, IsFiniteLocallyFreeOfRank D (π ≫ sX) hP (N j) 1),
        (∀ i, IsInvertibleModule ⟨P, hP.1⟩ (L i)) ∧ (∀ j, IsInvertibleModule ⟨P, hP.1⟩ (N j)) ∧
        totalChernCap.{u, u + 1} ((spaceModulePullback D hX.1 hP.1 π).obj E) r
            (isFiniteLocallyFreeOfRank_modulePullback D.site D.base D.base_mem
              (ObjectProperty.homMk π : (⟨P, hP.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
                ⟨X, hX.1⟩) hr) =
          ((List.finRange r).map fun i => 1 + chernCap.{u, u + 1} (L i) 1 (hL i) 1).prod ∧
        totalChernCap.{u, u + 1} ((spaceModulePullback D hX.1 hP.1 π).obj F) s
            (isFiniteLocallyFreeOfRank_modulePullback D.site D.base D.base_mem
              (ObjectProperty.homMk π : (⟨P, hP.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
                ⟨X, hX.1⟩) hs) =
          ((List.finRange s).map fun j => 1 + chernCap.{u, u + 1} (N j) 1 (hN j) 1).prod ∧
        totalChernCap.{u, u + 1} ((spaceModulePullback D hX.1 hP.1 π).obj (E ⊗ F)) (r * s)
            (isFiniteLocallyFreeOfRank_modulePullback D.site D.base D.base_mem
              (ObjectProperty.homMk π : (⟨P, hP.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
                ⟨X, hX.1⟩) (isFiniteLocallyFreeOfRank_tensorObj D.site D.base D.base_mem X hX.1
                  hr hs)) =
          ((List.finRange r).flatMap fun i => (List.finRange s).map fun j =>
            1 + (chernCap.{u, u + 1} (L i) 1 (hL i) 1 +
              chernCap.{u, u + 1} (N j) 1 (hN j) 1)).prod
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.31, Tag 0ESB](https://stacks.math.columbia.edu/tag/0ESB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
