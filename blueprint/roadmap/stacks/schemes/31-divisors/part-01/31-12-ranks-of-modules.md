---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.rank, AlgebraicGeometry.Scheme.Modules.rank_tfae, AlgebraicGeometry.Scheme.Modules.rank_pullback_of_isDominant, AlgebraicGeometry.Scheme.Modules.rank_of_shortExact, AlgebraicGeometry.Scheme.Modules.rank_tensor_and_rank_sheafHom, AlgebraicGeometry.Scheme.Modules.exists_rank_eq_and_over_iso_free
statement: formalized
proof: formalized
---

# 31.12 Ranks of modules

Section 31.12 of the Stacks Project, [Tag 0HAE](https://stacks.math.columbia.edu/tag/0HAE). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HAF, a definition

[Tag 0HAF](https://stacks.math.columbia.edu/tag/0HAF) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.rank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean#L76).

> **Stacks 0HAF.** The *rank* of an `𝒪_X`-module `ℱ` on an integral scheme `X` with generic
> point `η` is `dim_{κ(η)} ℱ_η`, the dimension of the stalk at the generic point over the local
> ring there, which is the residue field `κ(η)` (the function field `X.functionField`). Stacks
> makes the definition for quasi-coherent `ℱ`; the formula makes sense for every `𝒪_X`-module and
> the results below assume quasi-coherence where Stacks does.

```lean
noncomputable def rank [IsIntegral X] (F : X.Modules) : Cardinal.{u}
```

## Tag 0HAG, a lemma

[Tag 0HAG](https://stacks.math.columbia.edu/tag/0HAG) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.rank_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean#L121).

> **Stacks 0HAG.** Let `X` be an integral scheme, `ℱ` a quasi-coherent `𝒪_X`-module and `r` a
> cardinal. The following are equivalent: `ℱ` has rank `r`; for every nonempty affine open
> `U ⊆ X` the `𝒪_X(U)`-module `ℱ(U)` has rank `r`; for some nonempty affine open `U ⊆ X` the
> `𝒪_X(U)`-module `ℱ(U)` has rank `r`. The rank of a module `M` over a domain `R` is
> `dim_K (M ⊗_R K)` for `K` the fraction field of `R`.

```lean
theorem rank_tfae [IsIntegral X] (F : X.Modules) [F.IsQuasicoherent] (r : Cardinal.{u}) :
    List.TFAE [F.rank = r,
      ∀ U : X.Opens, IsAffineOpen U → Nonempty U →
        Module.rank (FractionRing Γ(X, U)) (FractionRing Γ(X, U) ⊗[Γ(X, U)] Γ(F, U)) = r,
      ∃ U : X.Opens, IsAffineOpen U ∧ Nonempty U ∧
        Module.rank (FractionRing Γ(X, U)) (FractionRing Γ(X, U) ⊗[Γ(X, U)] Γ(F, U)) = r]
```

## Tag 0HAH, a lemma

[Tag 0HAH](https://stacks.math.columbia.edu/tag/0HAH) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.rank_pullback_of_isDominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean#L152).

> **Stacks 0HAH.** Let `f : X ⟶ Y` be a dominant morphism of integral schemes and `𝒢` a
> quasi-coherent `𝒪_Y`-module. Then the rank of `𝒢` on `Y` is the rank of `f^*𝒢` on `X`.

```lean
theorem rank_pullback_of_isDominant {X Y : Scheme.{u}} [IsIntegral X] [IsIntegral Y]
    (f : X ⟶ Y) [IsDominant f] (G : Y.Modules) [G.IsQuasicoherent] :
    G.rank = ((Scheme.Modules.pullback f).obj G).rank
```

## Tag 0HAI, a lemma

[Tag 0HAI](https://stacks.math.columbia.edu/tag/0HAI) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.rank_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean#L182).

> **Stacks 0HAI.** On an integral scheme, for a short exact sequence
> `0 → ℱ → ℱ' → ℱ'' → 0` of quasi-coherent `𝒪_X`-modules the rank of `ℱ'` is the sum of the ranks
> of `ℱ` and `ℱ''`.

```lean
theorem rank_of_shortExact [IsIntegral X] (S : ShortComplex X.Modules) (hS : S.ShortExact)
    [S.X₁.IsQuasicoherent] [S.X₂.IsQuasicoherent] [S.X₃.IsQuasicoherent] :
    S.X₂.rank = S.X₁.rank + S.X₃.rank
```

## Tag 0HAJ, a lemma

[Tag 0HAJ](https://stacks.math.columbia.edu/tag/0HAJ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.rank_tensor_and_rank_sheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean#L246).

> **Stacks 0HAJ.** Let `X` be an integral scheme and `ℱ`, `𝒢` quasi-coherent `𝒪_X`-modules.
> (1) The rank of `ℱ ⊗_{𝒪_X} 𝒢` is the product of the ranks of `ℱ` and `𝒢`. (2) If `ℱ` is of
> finite presentation, the rank of `ℋom_{𝒪_X}(ℱ, 𝒢)` is the product of the ranks of `ℱ` and
> `𝒢`.

```lean
theorem rank_tensor_and_rank_sheafHom [IsIntegral X] (F G : X.Modules) [F.IsQuasicoherent]
    [G.IsQuasicoherent] :
    rank (((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨X.toRingedSpace.presheaf, X.toRingedSpace.IsSheaf⟩).obj F).obj G) =
        F.rank * G.rank ∧
      (F.IsFinitePresentation →
        rank (Stacks.SheafOfModules.SheafHomStalk.internalSheafHom X.toTopCat X.sheaf F G).obj =
          F.rank * G.rank)
```

## Tag 0HAK, a lemma

[Tag 0HAK](https://stacks.math.columbia.edu/tag/0HAK) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_rank_eq_and_over_iso_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RankOfModules.lean#L260).

> **Stacks 0HAK.** Let `X` be an integral scheme and `ℱ` a quasi-coherent `𝒪_X`-module of
> finite type. Then `ℱ` has finite rank `r ≥ 0`, and there is a nonempty open `U ⊆ X` such that
> `ℱ|_U` is free of rank `r`.

```lean
theorem exists_rank_eq_and_over_iso_free [IsIntegral X] (F : X.Modules) [F.IsQuasicoherent]
    [F.IsFiniteType] :
    ∃ r : ℕ, F.rank = r ∧ ∃ U : X.Opens, Nonempty U ∧
      Nonempty (F.over U ≅
        _root_.SheafOfModules.free (R := X.ringCatSheaf.over U) (ULift.{u} (Fin r)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.12, Tag 0HAE](https://stacks.math.columbia.edu/tag/0HAE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
