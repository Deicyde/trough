---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.fittingIdealInt, AlgebraicGeometry.Space.fittingIdealInt_obj_eq, AlgebraicGeometry.Space.fittingIdeal_obj_eq_fittingIdealOnChart, AlgebraicGeometry.Space.fittingIdealInt_eq_bot_of_lt_zero, AlgebraicGeometry.Space.monotone_fittingIdealInt, AlgebraicGeometry.Space.fittingIdealInt_chain, AlgebraicGeometry.Space.fittingIdealPullback_eq_fittingIdeal, AlgebraicGeometry.Space.isFiniteTypeQuasicoherentIdeal_fittingIdeal_of_isFinitePresentationOnSite
statement: formalized
proof: formalized
---

# 71.5 Fitting ideals

Section 71.5 of the Stacks Project, [Tag 0CZ3](https://stacks.math.columbia.edu/tag/0CZ3). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CZ3, the section

[Tag 0CZ3](https://stacks.math.columbia.edu/tag/0CZ3) in the Stacks Project.

**`AlgebraicGeometry.Space.fittingIdealInt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean#L275). The attribute's comment: “the chain Fit\_k, k : ℤ”.

> **The `k`-th Fitting ideal sheaf of an `𝒪_F`-module, for `k : ℤ`**: the smallest sheaf of
> ideals of `𝒪_F` whose sections over every affine étale chart contain the module-theoretic `k`-th
> Fitting ideal of the sections of the module there.
>
> For `k < 0` the chartwise ideal is zero, so `Fit₋₁(G) = 0`.

```lean
noncomputable def fittingIdealInt (G : Modules.{u, m} B S hS F hF) (k : ℤ) :
    (SheafOfModules.unit
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B S hS F hF).O))).Submodule
```

**`AlgebraicGeometry.Space.fittingIdealInt_obj_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean#L350). The attribute's comment: “the chartwise characterisation of the sections”.

> **Stacks 0CZ3: over an affine étale chart the sections of `Fit_k(G)` are exactly the
> module-theoretic `k`-th Fitting ideal of the sections of `G` over the chart ring.**
>
> One inclusion is the defining property of `AlgebraicGeometry.Space.fittingIdealInt`; the other
> holds because the sections restricting into the chartwise Fitting ideals already form a sheaf of
> ideals containing them, so the infimum is below it.

```lean
theorem fittingIdealInt_obj_eq (G : Modules.{u, m} B S hS F hF)
    (hG : IsCartesianOnAffineCharts G)
    (hfin : ∀ W : SmallEtale B S hS F,
      IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS F hF W) (G.val.obj (op W)))
    (k : ℤ) {U : SmallEtale B S hS F}
    (hU : IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj U)) :
    (fittingIdealInt B S hS F hF G k).toSubmodule.obj (op U) =
      @_root_.fittingIdeal (chartRing B S hS F hF U) _ (G.val.obj (op U)) _ _ (hfin U hU) k
```

**`AlgebraicGeometry.Space.fittingIdeal_obj_eq_fittingIdealOnChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean#L371). The attribute's comment: “the chartwise characterisation, in nonnegative degree”.

> **Stacks 0CZ3 for the `ℕ`-indexed Fitting ideal sheaf**: over an affine étale chart the
> sections of `AlgebraicGeometry.Space.fittingIdeal` are exactly the chartwise Fitting ideal of
> `AlgebraicGeometry.Space.fittingIdealOnChart`.

```lean
theorem fittingIdeal_obj_eq_fittingIdealOnChart (G : Modules.{u, m} B S hS F hF)
    (hG : IsCartesianOnAffineCharts G)
    (hfin : ∀ W : SmallEtale B S hS F,
      IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS F hF W) (G.val.obj (op W)))
    (r : ℕ) {U : SmallEtale B S hS F}
    (hU : IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj U)) :
    (fittingIdeal B S hS F hF G r).toSubmodule.obj (op U) =
      @fittingIdealOnChart B S hS F hF G r U (hfin U hU)
```

**`AlgebraicGeometry.Space.fittingIdealInt_eq_bot_of_lt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean#L404). The attribute's comment: “Fit\_\{-1} = 0”.

> **`Fit₋₁(G) = 0`, and more generally the Fitting ideal sheaves vanish in negative degree**: in
> negative degree the chartwise Fitting ideal is zero, so every sheaf of ideals belongs to the
> family whose infimum defines `Fit_k(G)`.

```lean
theorem fittingIdealInt_eq_bot_of_lt_zero (G : Modules.{u, m} B S hS F hF) {k : ℤ} (hk : k < 0) :
    fittingIdealInt B S hS F hF G k = ⊥
```

**`AlgebraicGeometry.Space.monotone_fittingIdealInt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean#L440). The attribute's comment: “the chain increases”.

> **The chain of Fitting ideal sheaves increases.**  A sheaf of ideals whose sections over every
> affine étale chart contain the chartwise `Fit_l` contains the chartwise `Fit_k` there too, for
> `k ≤ l`, so the family whose infimum is `Fit_l(G)` is contained in the family for `Fit_k(G)`.

```lean
theorem monotone_fittingIdealInt (G : Modules.{u, m} B S hS F hF) :
    Monotone fun k : ℤ => fittingIdealInt B S hS F hF G k
```

**`AlgebraicGeometry.Space.fittingIdealInt_chain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealChain.lean#L459).

> **Stacks 0CZ3.**  For a finite type quasi-coherent `𝒪_X`-module `G` on an algebraic space `X`
> the Fitting ideals form an increasing chain `0 = Fit₋₁(G) ⊆ Fit₀(G) ⊆ … ⊆ 𝒪_X` of sheaves of
> ideals, characterised by: over every affine étale chart `U` the sections of `Fit_k(G)` are the
> module-theoretic `k`-th Fitting ideal of the sections `G(U)` over the chart ring `𝒪_X(U)`.
>
> The finiteness of the sections over every affine chart is the étale-local reading of finite type
> used by the conventions of Stacks 0CZ3, under which the Fitting ideals are defined chartwise.

```lean
theorem fittingIdealInt_chain (X : AlgebraicSpaces B S hS) (G : Modules.{u, u} B S hS X.1 X.2)
    (hG : G.IsQuasicoherentOnSite)
    (hfin : ∀ W : SmallEtale B S hS X.1,
      IsAffine ((SmallEtale.toOver B S hS X.1 ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS X.1 X.2 W) (G.val.obj (op W))) :
    fittingIdealInt B S hS X.1 X.2 G (-1) = ⊥ ∧
      Monotone (fun k : ℤ => fittingIdealInt B S hS X.1 X.2 G k) ∧
      (∀ k : ℤ, fittingIdealInt B S hS X.1 X.2 G k ≤ ⊤) ∧
      ∀ (k : ℤ) (U : SmallEtale B S hS X.1)
        (hU : IsAffine ((SmallEtale.toOver B S hS X.1 ⋙ BigFppfOver.toScheme B S hS).obj U)),
        (fittingIdealInt B S hS X.1 X.2 G k).toSubmodule.obj (op U) =
          @_root_.fittingIdeal (chartRing B S hS X.1 X.2 U) _ (G.val.obj (op U)) _ _
            (hfin U hU) k
```

## Tag 0CZ4, a lemma

[Tag 0CZ4](https://stacks.math.columbia.edu/tag/0CZ4) in the Stacks Project.

**`AlgebraicGeometry.Space.fittingIdealPullback_eq_fittingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealPullbackFiniteType.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealPullbackFiniteType.lean#L65).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces and let `G` be a finite type
> quasi-coherent `𝒪_Y`-module.  Then the ideal sheaf on `X` generated by the inverse image of the
> `r`-th Fitting ideal sheaf of `G` is the `r`-th Fitting ideal sheaf of `f^*G`:
> `f^{-1}Fit_r(G) · 𝒪_X = Fit_r(f^*G)`.

```lean
theorem fittingIdealPullback_eq_fittingIdeal {f : X ⟶ Y} {G : Modules.{u, u} B S hS Y.1 Y.2}
    (hqc : G.IsQuasicoherentOnSite)
    (hft : PresheafOfModules.IsFiniteType (smallEtaleRingedSite B S hS Y.1 Y.2).J G.val)
    (r : ℕ) :
    fittingIdealPullback B S hS f G r =
      fittingIdeal B S hS X.1 X.2 ((modulePullback B S hS f).obj G) r
```

## Tag 0CZ5, a lemma

[Tag 0CZ5](https://stacks.math.columbia.edu/tag/0CZ5) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteTypeQuasicoherentIdeal_fittingIdeal_of_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealFiniteType.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealFiniteType.lean#L286).

> For a finitely presented quasi-coherent `𝒪_X`-module `ℱ` on an algebraic space `X`, the `r`-th
> Fitting ideal `Fit_r(ℱ)` is a quasi-coherent ideal of finite type.

```lean
theorem isFiniteTypeQuasicoherentIdeal_fittingIdeal_of_isFinitePresentationOnSite
    (X : AlgebraicSpaces B S hS) (G : Modules.{u, u} B S hS X.1 X.2)
    (hG : G.IsQuasicoherentOnSite) (hfp : SheafOfModules.IsFinitePresentationOnSite G) (r : ℕ) :
    IsFiniteTypeQuasicoherentIdeal B S hS X (fittingIdeal B S hS X.1 X.2 G r)
```

## Tag 0CZ6, a lemma

[Tag 0CZ6](https://stacks.math.columbia.edu/tag/0CZ6) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticSupport_le_fittingClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealZerothSchemeTheoreticSupport.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealZerothSchemeTheoreticSupport.lean#L108). The attribute's comment: “part (1)”.

> **Stacks 0CZ6, part (1).**  Let `G` be a finite type, quasi-coherent `𝒪_X`-module, let `Z₀`
> be the closed subspace of `X` cut out by `Fit_0(G)` and let `Z` be the scheme-theoretic support
> of `G`.  Then `Z ⊆ Z₀ ⊆ X` as closed subspaces.
>
> The scheme-theoretic support of Stacks 07U1 is a closed subspace by
> `AlgebraicGeometry.Space.exists_isClosedSubspace_schemeTheoreticSupport`.  It is the infimum of
> the closed subspaces whose defining ideal sheaf annihilates `G`, and `Z₀` is one of them because
> `Fit_0(G)` annihilates `G`.

```lean
theorem schemeTheoreticSupport_le_fittingClosedSubspace
    (G : Modules.{u, u} B S hS X.1 X.2) [G.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteTypeOnSite G] (Z₀ : ClosedSubspaces B S hS X.1)
    (cutOut : definingIdealSheaf B S hS X Z₀ = fittingIdeal B S hS X.1 X.2 G 0) :
    IsClosedSubspace B S hS (schemeTheoreticSupport B S hS X G) ∧
      schemeTheoreticSupport B S hS X G ≤ Z₀.1
```

**`AlgebraicGeometry.Space.range_pointsMap_schemeTheoreticSupport_eq_supportOfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealZerothSchemeTheoreticSupport.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealZerothSchemeTheoreticSupport.lean#L133). The attribute's comment: “part (2)”. References: SGA 7 VI (5.1), “more general”.

> **Stacks 0CZ6, part (2).**  Let `G` be a finite type, quasi-coherent `𝒪_X`-module, let `Z₀`
> be the closed subspace of `X` cut out by `Fit_0(G)` and let `Z` be the scheme-theoretic support
> of `G`.  Then `|Z| = |Z₀| = Supp(G)` as closed subsets of `|X|`.
>
> The point set of a closed subspace is the zero locus of its defining ideal sheaf
> (`AlgebraicGeometry.Space.range_pointsMap_ι_eq_idealZeroLocus`); the defining ideal sheaves of
> `Z` and `Z₀` are the annihilator and `Fit_0(G)`.  The support lies in the zero locus of the
> annihilator, which lies in the zero locus of `Fit_0(G)` because `Fit_0(G) ⊆ Ann(G)`, and the
> latter is the support by
> `AlgebraicGeometry.Space.idealZeroLocus_fittingIdeal_zero_eq_supportOfSheaf`.  The support is
> closed by Stacks 07TZ.

```lean
theorem range_pointsMap_schemeTheoreticSupport_eq_supportOfSheaf
    (G : Modules.{u, u} B S hS X.1 X.2) [G.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteTypeOnSite G] (Z₀ : ClosedSubspaces B S hS X.1)
    (cutOut : definingIdealSheaf B S hS X Z₀ = fittingIdeal B S hS X.1 X.2 G 0) :
    Set.range (pointsMap B S hS (schemeTheoreticSupport B S hS X G).toFunctor
        (schemeTheoreticSupport B S hS X G).ι) =
        Set.range (pointsMap B S hS Z₀.1.toFunctor Z₀.1.ι) ∧
      Set.range (pointsMap B S hS Z₀.1.toFunctor Z₀.1.ι) =
        supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj G) ∧
      IsClosed (supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj G))
```

**`AlgebraicGeometry.Space.exists_module_on_fittingClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealZerothSchemeTheoreticSupport.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealZerothSchemeTheoreticSupport.lean#L174). The attribute's comment: “part (3)”.

> **Stacks 0CZ6, part (3).**  Let `G` be a finite type, quasi-coherent `𝒪_X`-module and let
> `Z₀` be the closed subspace of `X` cut out by `Fit_0(G)`.  Then there is a finite type,
> quasi-coherent `𝒪_{Z₀}`-module `G₀` with `(Z₀ → X)_* G₀ ≅ G`.
>
> The ideal cutting out `Z₀` is `Fit_0(G)`, which annihilates `G`, so the essential-image assertion
> of Stacks 04CJ part (3) for the closed immersion `Z₀ → X`,
> `AlgebraicGeometry.Space.isQuasicoherentEssImagePushforward_of_isClosedImmersion`, produces the
> quasi-coherent module; it is of finite type by Stacks 07U0 part (3).

```lean
theorem exists_module_on_fittingClosedSubspace
    (G : Modules.{u, u} B S hS X.1 X.2) [G.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteTypeOnSite G] (Z₀ : ClosedSubspaces B S hS X.1)
    (cutOut : definingIdealSheaf B S hS X Z₀ = fittingIdeal B S hS X.1 X.2 G 0) :
    ∃ G₀ : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z₀).1
        (closedSubspaceToSpace B S hS X Z₀).2,
      G₀.IsQuasicoherentOnSite ∧ SheafOfModules.IsFiniteTypeOnSite G₀ ∧
        Nonempty ((modulePushforward B S hS (closedSubspaceInclusion B S hS X Z₀)).obj G₀ ≅
          G)
```

## Tag 0CZ7, a lemma

[Tag 0CZ7](https://stacks.math.columbia.edu/tag/0CZ7) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_fin_span_iff_fittingIdealGeometricStalk_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealGeometricStalk.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingIdealGeometricStalk.lean#L384).

> **Stacks 0CZ7.**  Let `G` be a finite type quasi-coherent `𝒪_X`-module on an algebraic space
> `X` and let `x̄` be a geometric point of `X`.  Then `G` can be generated by `r` elements on an
> affine étale neighbourhood of `x̄` if and only if the stalk `Fit_r(G)_{x̄}` of its `r`-th Fitting
> ideal is the whole étale local ring `𝒪_{X, x̄}`.
>
> The finiteness of the sections over every affine étale chart is the étale-local reading of
> finite type used by the conventions of Stacks 0CZ3, under which the Fitting ideals are defined
> chartwise; `hG` is the cartesian property of Stacks 03DX, which a quasi-coherent module has by
> `AlgebraicGeometry.Space.isCartesianOnAffineCharts_of_isQuasicoherentOnSite`.

```lean
theorem exists_fin_span_iff_fittingIdealGeometricStalk_eq_top
    (G : Modules.{u, u} B S hS F hF) (hG : IsCartesianOnAffineCharts G)
    (hfin : ∀ W : SmallEtale B S hS F,
      IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS F hF W) (G.val.obj (op W)))
    (r : ℕ) (x : GeometricPoint B S hS F) :
    (∃ U : SmallEtaleNeighborhood x,
        IsAffine ((SmallEtale.toOver B S hS F ⋙ BigFppfOver.toScheme B S hS).obj U.chart) ∧
          ∃ s : Fin r → G.val.obj (op U.chart),
            Submodule.span (chartRing B S hS F hF U.chart) (Set.range s) = ⊤) ↔
      fittingIdealGeometricStalk G r x = ⊤
```

## Tag 0CZ8, a lemma

[Tag 0CZ8](https://stacks.math.columbia.edu/tag/0CZ8) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOfRank_tfae_fittingIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingLocallyFreeRank.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingLocallyFreeRank.lean#L446).

> **Stacks Project, Tag 0CZ8.**  Let `F` be an algebraic space and let `G` be a quasi-coherent
> `𝒪_F`-module on its small étale site.  For every `r`, the following are equivalent: `G` is
> finite locally free of rank `r`; its `(r-1)`-st Fitting ideal sheaf vanishes and its `r`-th is
> the unit ideal sheaf; its Fitting ideal sheaves vanish below `r` and are the unit ideal sheaf
> from `r` onward.
>
> The condition at index `r - 1` is read with truncated subtraction and is therefore guarded by the
> disjunct `r = 0`, under which it is vacuous.  No finite type hypothesis is needed; see the
> implementation notes.

```lean
theorem isFiniteLocallyFreeOfRank_tfae_fittingIdeal
    (G : Modules.{u, u} B S hS F hF) (hG : G.IsQuasicoherentOnSite) (r : ℕ) :
    List.TFAE [
      RingedSite.IsFiniteLocallyFreeOfRank (smallEtaleRingedSite B S hS F hF) G r,
      (r = 0 ∨ fittingIdeal B S hS F hF G (r - 1) = ⊥) ∧
        fittingIdeal B S hS F hF G r = ⊤,
      (∀ k < r, fittingIdeal B S hS F hF G k = ⊥) ∧
        (∀ k, r ≤ k → fittingIdeal B S hS F hF G k = ⊤)]
```

## Tag 0CZ9, a lemma

[Tag 0CZ9](https://stacks.math.columbia.edu/tag/0CZ9) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_fittingClosedSubspaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingClosedSubspaces.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingClosedSubspaces.lean#L226). The attribute's comment: “the decreasing chain of closed subspaces cut out by the Fitting ideals”.

> **The closed subspaces cut out by the Fitting ideals of an `𝒪_X`-module.**  If every Fitting
> ideal sheaf of `G` is quasi-coherent, there is a decreasing chain of closed subspaces of `X` whose
> defining ideal sheaves are the Fitting ideals of `G`.  This is the chain
> `X ⊇ Z_0 ⊇ Z_1 ⊇ …` of Stacks 0CZ9.
>
> Each subspace comes from the surjectivity half of Stacks 03MB,
> `AlgebraicGeometry.Space.exists_definingIdealSheaf_eq_of_isQuasicoherentOnSite`, and the chain
> decreases because the Fitting ideals increase and the correspondence of Stacks 03MB reverses
> inclusions.

```lean
theorem exists_fittingClosedSubspaces (G : Modules.{u, u} B S hS X.1 X.2)
    (hqc : ∀ r : ℕ,
      (fittingIdeal B S hS X.1 X.2 G r).toSheafOfModules.IsQuasicoherentOnSite) :
    ∃ Z : ℕ → ClosedSubspaces B S hS X.1,
      (∀ r, definingIdealSheaf B S hS X (Z r) = fittingIdeal B S hS X.1 X.2 G r) ∧
        Antitone fun r ↦ (Z r).1
```

**`AlgebraicGeometry.Space.iInf_fittingClosedSubspace_eq_sheafify_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingClosedSubspaces.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingClosedSubspaces.lean#L286). The attribute's comment: “(1) the intersection is empty; (2), (3) and finite presentation not covered”.

> **Clause (1) of Stacks 0CZ9: the intersection of the Fitting closed subspaces is the empty
> algebraic space.**  For a chain of closed subspaces of `X` whose defining ideal sheaves are the
> Fitting ideals of `G`, the intersection of the chain is the sheafification of the bottom
> subfunctor, as soon as the sections of `G` over every affine étale chart form a finite module.
>
> The intersection has no points, by
> `AlgebraicGeometry.Space.iInter_range_pointsMap_ι_fittingClosedSubspace_eq_empty`, and an
> inclusion into the empty open subspace is detected on points by Stacks 03BZ; the reverse inclusion
> holds for any family of subsheaves.

```lean
theorem iInf_fittingClosedSubspace_eq_sheafify_bot
    (G : Modules.{u, u} B S hS X.1 X.2) (Z : ℕ → ClosedSubspaces B S hS X.1)
    (hZ : ∀ r, definingIdealSheaf B S hS X (Z r) = fittingIdeal B S hS X.1 X.2 G r)
    (hfin : ∀ W : SmallEtale B S hS X.1,
      IsAffine ((SmallEtale.toOver B S hS X.1 ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS X.1 X.2 W) (G.val.obj (op W))) :
    (⨅ r : ℕ, (Z r).1) = (⊥ : Subfunctor X.1).sheafify (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Space.exists_fittingClosedSubspaces_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingStratumFinitePresentation.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingStratumFinitePresentation.lean#L194). References: EGA IV (1.4.5), “the closed subspaces”.

> **Stacks 0CZ9.**  Let `X` be an algebraic space over a scheme `S` contained in a big fppf
> site `B` and let `G` be a quasi-coherent `𝒪_X`-module of finite type.  The Fitting ideal sheaves
> of `G` cut out a decreasing chain of closed subspaces `X = Z_{-1} ⊇ Z_0 ⊇ Z_1 ⊇ …` such that
>
> 1. the intersection of the `Z_r` is empty;
> 2. for every algebraic space `T ⟶ X` the module `G_T` is locally generated by at most `r`
>    sections exactly when `T ⟶ X` factors, necessarily uniquely, through `X ∖ Z_r`;
> 3. for every algebraic space `T ⟶ X` the module `G_T` is finite locally free of rank `r`
>    exactly when `T ⟶ X` factors, necessarily uniquely, through `Z_{r-1} ∖ Z_r`;
>
> and, if `G` is moreover of finite presentation, the three morphisms `Z_r ⟶ X`, `X ∖ Z_r ⟶ X` and
> `Z_{r-1} ∖ Z_r ⟶ X` are of finite presentation.
>
> The chain is the one cut out by `AlgebraicGeometry.Space.fittingIdeal`, the test objects of
> clauses (2) and (3) are arbitrary algebraic spaces rather than only schemes over `X`, and
> `Z_{r-1} ∖ Z_r` is `AlgebraicGeometry.Space.fittingRankStratum`, which for `r = 0` is
> `X ∖ Z_0`.

```lean
theorem exists_fittingClosedSubspaces_spec (hGqc : G.IsQuasicoherentOnSite)
    (hGft : SheafOfModules.IsFiniteTypeOnSite G) :
    ∃ Z : ℕ → ClosedSubspaces B S hS X.1,
      (∀ r, definingIdealSheaf B S hS X (Z r) = fittingIdeal B S hS X.1 X.2 G r) ∧
      (Antitone fun r ↦ (Z r).1) ∧
      (⨅ r : ℕ, (Z r).1) = (⊥ : Subfunctor X.1).sheafify (BigFppfOver.topology B S hS) ∧
      (∀ (T : AlgebraicSpaces B S hS) (r : ℕ) (f : T ⟶ X),
        (∀ x : points B S hS T.1, ∃ (U : SmallEtale B S hS T.1)
            (s : Fin r → ((modulePullback B S hS f).obj G).val.obj (op U)),
            IsAffine ((SmallEtale.toOver B S hS T.1 ⋙ BigFppfOver.toScheme B S hS).obj U) ∧
              Submodule.span (chartRing B S hS T.1 T.2 U) (Set.range s) = ⊤ ∧
                x ∈ Set.range (pointsMap B S hS
                  (yoneda.obj ((SmallEtale.toOver B S hS T.1).obj U)) U.1.hom)) ↔
          ∃! g : T.1 ⟶ (openComplement B S hS (Z r).1).toFunctor,
            g ≫ (openComplement B S hS (Z r).1).ι = f.hom) ∧
      (∀ (T : AlgebraicSpaces B S hS) (r : ℕ) (f : T ⟶ X),
        RingedSite.IsFiniteLocallyFreeOfRank (smallEtaleRingedSite B S hS T.1 T.2)
            ((modulePullback B S hS f).obj G) r ↔
          ∃! g : T.1 ⟶ (fittingRankStratum B S hS X Z r).toFunctor,
            g ≫ (fittingRankStratum B S hS X Z r).ι = f.hom) ∧
      (SheafOfModules.IsFinitePresentationOnSite G → ∀ r : ℕ,
        IsFinitePresentation B S hS (subspaceInclusion B S hS X (Z r)).hom ∧
          IsFinitePresentation B S hS (openComplement B S hS (Z r).1).ι ∧
            IsFinitePresentation B S hS (fittingRankStratum B S hS X Z r).ι)
```

## Tag 0CZA, a lemma

[Tag 0CZA](https://stacks.math.columbia.edu/tag/0CZA) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyClosedSubspace_and_disjoint_fittingRankStratum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingRankStrata.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingRankStrata.lean#L339). The attribute's comment: “the strata X\_r = Z\_\{r-1} \ Z\_r are disjoint locally closed subspaces”.

> **Stacks 0CZA, the Fitting rank strata.**  Let `G` be an `𝒪_X`-module and let
> `X ⊇ Z_0 ⊇ Z_1 ⊇ …` be closed subspaces of `X` whose defining ideal sheaves are the Fitting
> ideals of `G`, as in Stacks 0CZ9.  Then the strata `X_r = Z_{r-1} \ Z_r`, with the convention
> `Z_{-1} = X`, are locally closed subspaces of `X`, and distinct strata are disjoint.

```lean
theorem isLocallyClosedSubspace_and_disjoint_fittingRankStratum
    (G : Modules.{u, u} B S hS X.1 X.2) (Z : ℕ → ClosedSubspaces B S hS X.1)
    (hZ : ∀ r, definingIdealSheaf B S hS X (Z r) = fittingIdeal B S hS X.1 X.2 G r) :
    (∀ r : ℕ, IsLocallyClosedSubspace B S hS (fittingRankStratum B S hS X Z r)) ∧
      ∀ r s : ℕ, r ≠ s →
        fittingRankStratum B S hS X Z r ⊓ fittingRankStratum B S hS X Z s ≤
          (⊥ : Subfunctor X.1).sheafify (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Space.existsUnique_fittingRankStratum_index`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingRankStrata.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingRankStrata.lean#L359). The attribute's comment: “every point of X lies in exactly one stratum X\_r = Z\_\{r-1} \ Z\_r”.

> **Stacks 0CZA, the Fitting rank strata cover `X`.**  Every point of `X` lies in exactly one
> Fitting rank stratum `X_r = Z_{r-1} \ Z_r`: there is a unique `r` with the point outside `Z_r`
> and inside every earlier member of the chain.
>
> The input is clause (1) of Stacks 0CZ9,
> `AlgebraicGeometry.Space.iInter_range_pointsMap_ι_fittingClosedSubspace_eq_empty`: the point
> sets of the Fitting closed subspaces have empty intersection, so every point leaves the chain,
> and it does so at a unique index because the chain decreases.

```lean
theorem existsUnique_fittingRankStratum_index (G : Modules.{u, u} B S hS X.1 X.2)
    (Z : ℕ → ClosedSubspaces B S hS X.1)
    (hZ : ∀ r, definingIdealSheaf B S hS X (Z r) = fittingIdeal B S hS X.1 X.2 G r)
    (hfin : ∀ W : SmallEtale B S hS X.1,
      IsAffine ((SmallEtale.toOver B S hS X.1 ⋙ BigFppfOver.toScheme B S hS).obj W) →
        Module.Finite (chartRing B S hS X.1 X.2 W) (G.val.obj (op W)))
    (x : points B S hS X.1) :
    ∃! r : ℕ, x ∉ Set.range (pointsMap B S hS (Z r).1.toFunctor (Z r).1.ι) ∧
      ∀ k < r, x ∈ Set.range (pointsMap B S hS (Z k).1.toFunctor (Z k).1.ι)
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_fittingRankStratification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingRankStrata.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingRankStrata.lean#L400). The attribute's comment: “X' = ∐\_\{r ≥ 0} X\_r is an algebraic space, with its morphism to X”.

> **Stacks 0CZA, the disjoint union of the Fitting rank strata.**  The disjoint union
> `X' = ∐_{r ≥ 0} X_r` of the strata `X_r = Z_{r-1} \ Z_r` of a chain `X ⊇ Z_0 ⊇ Z_1 ⊇ …` of closed
> subspaces of `X` is an algebraic space over `S`, and its structural morphism restricts on the
> `r`-th summand to the inclusion of `X_r` in `X`.

```lean
theorem isAlgebraicSpace_fittingRankStratification (Z : ℕ → ClosedSubspaces B S hS X.1) :
    IsAlgebraicSpace B S hS (fittingRankStratification B S hS X Z).obj ∧
      ∀ r : ℕ, Sigma.ι (fun k : ℕ ↦ fittingRankStratumSpace B S hS X Z k) r ≫
          fittingRankStratificationHom B S hS X Z = fittingRankStratumHom B S hS X Z r
```

**`AlgebraicGeometry.Space.exists_fittingRankStratification_flat_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FittingStratumAssembly.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FittingStratumAssembly.lean#L443).

> **Stacks 0CZA.**  Let `X` be an algebraic space over a scheme `S` contained in a big fppf
> site `B` and let `G` be a quasi-coherent `𝒪_X`-module of finite presentation.  Then the Fitting
> ideal sheaves of `G` cut out a decreasing chain of closed subspaces
> `X = Z_{-1} ⊇ Z_0 ⊇ Z_1 ⊇ …` with empty intersection, the strata `X_r = Z_{r-1} ∖ Z_r` are
> pairwise disjoint locally closed subspaces of `X` and every point of `X` lies in exactly one of
> them, the disjoint union `X' = ∐_{r ≥ 0} X_r` is an algebraic space over `S` whose structural
> morphism restricts on the `r`-th summand to the inclusion of `X_r`, and
>
> 1. `X'` **represents the functor** sending a test object `f : h_T ⟶ X` of the site to a
>    one-point set when `G_T` is flat over `T` in the sense of Stacks 05VV and to the empty set
>    otherwise;
> 2. the pullback of `G` to `X_r` is finite locally free of rank `r`;
> 3. both `X_r ⟶ X` and `X' ⟶ X` are of finite presentation.
>
> The hypotheses are exactly the ones Stacks 0CZA makes.

```lean
theorem exists_fittingRankStratification_flat_spec (hGqc : G.IsQuasicoherentOnSite)
    (hGfp : SheafOfModules.IsFinitePresentationOnSite G) :
    ∃ Z : ℕ → ClosedSubspaces B S hS X.1,
      (∀ r, definingIdealSheaf B S hS X (Z r) = fittingIdeal B S hS X.1 X.2 G r) ∧
      (Antitone fun r ↦ (Z r).1) ∧
      (⨅ r : ℕ, (Z r).1) = (⊥ : Subfunctor X.1).sheafify (BigFppfOver.topology B S hS) ∧
      (∀ r : ℕ, IsLocallyClosedSubspace B S hS (fittingRankStratum B S hS X Z r)) ∧
      (∀ r s : ℕ, r ≠ s →
        fittingRankStratum B S hS X Z r ⊓ fittingRankStratum B S hS X Z s ≤
          (⊥ : Subfunctor X.1).sheafify (BigFppfOver.topology B S hS)) ∧
      (∀ x : points B S hS X.1, ∃! r : ℕ,
        x ∉ Set.range (pointsMap B S hS (Z r).1.toFunctor (Z r).1.ι) ∧
          ∀ k < r, x ∈ Set.range (pointsMap B S hS (Z k).1.toFunctor (Z k).1.ι)) ∧
      IsAlgebraicSpace B S hS (fittingRankStratification B S hS X Z).obj ∧
      (∀ r : ℕ, Sigma.ι (fun k : ℕ ↦ fittingRankStratumSpace B S hS X Z k) r ≫
          fittingRankStratificationHom B S hS X Z = fittingRankStratumHom B S hS X Z r) ∧
      (∀ (T : BigFppfOver B S hS) (f : schemeSpace T ⟶ X),
        IsFlatOver B S hS (schemeSpace T).2
            (𝟙 (schemeSpace T) : schemeSpace T ⟶ schemeSpace T).hom
            ((modulePullback B S hS f).obj G) ↔
          ∃! h : yoneda.obj T ⟶ (fittingRankStratification B S hS X Z).1,
            h ≫ (fittingRankStratificationHom B S hS X Z).hom = f.hom) ∧
      (∀ r : ℕ, RingedSite.IsFiniteLocallyFreeOfRank
        (smallEtaleRingedSite B S hS (fittingRankStratumSpace B S hS X Z r).1
          (fittingRankStratumSpace B S hS X Z r).2)
        ((modulePullback B S hS (fittingRankStratumHom B S hS X Z r)).obj G) r) ∧
      (∀ r : ℕ, IsFinitePresentation B S hS (fittingRankStratum B S hS X Z r).ι) ∧
      IsFinitePresentation B S hS (fittingRankStratificationHom B S hS X Z).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.5, Tag 0CZ3](https://stacks.math.columbia.edu/tag/0CZ3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
