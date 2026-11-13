---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward_of_qcqs, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_isAffineHom, AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom_of_isQuasicoherent, AlgebraicGeometry.Space.cohomologyCollapseIsoOfIsAffineHom, AlgebraicGeometry.Space.cohomologyUliftIsoOfIsAffineHom, AlgebraicGeometry.Space.cohomologyIsoOfIsAffineHom
statement: formalized
proof: formalized
---

# 69.8 Vanishing for higher direct images

Section 69.8 of the Stacks Project, [Tag 073F](https://stacks.math.columbia.edu/tag/073F). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 073G, a lemma

[Tag 073G](https://stacks.math.columbia.edu/tag/073G) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_forall_isZero_rightDerived_modulePushforward_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageUniformBound.lean, line 505](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageUniformBound.lean#L505). The attribute's comment: “n(X -> Y) is a natural number, chosen before the base change, the module and the degree; X' is any algebraic space completing a cartesian square over f”.

> **[Stacks, Tag 073G].**  Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over `S`, with `Y` quasi-compact.  There is a single degree `n(X → Y)` such that
> for every algebraic space `Y'`, every morphism `Y' ⟶ Y`, every algebraic space `X'` making
> `X' ⟶ X`, `X' ⟶ Y'` a cartesian square over `f`, and every quasi-coherent `𝒪_{X'}`-module `𝓕'`,
> the higher direct images `R^q f'_*𝓕'` vanish for `q ≥ n(X → Y)`.

```lean
theorem exists_forall_isZero_rightDerived_modulePushforward_of_qcqs {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) :
    ∃ N : ℕ, ∀ (Y' X' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y) (i' : X' ⟶ X) (f' : X' ⟶ Y'),
      IsPullback i' f' f g →
      ∀ F' : Modules.{u, u} B S hS X'.1 X'.2, F'.IsQuasicoherentOnSite → ∀ q : ℕ, N ≤ q →
        IsZero (((modulePushforward B S hS f').rightDerived q).obj F')
```

## Tag 073H, a lemma

[Tag 073H](https://stacks.math.columbia.edu/tag/073H) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardUnconditional.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardUnconditional.lean#L44).

> For an affine morphism `f : X ⟶ Y` of algebraic spaces over `S`, a quasi-coherent
> `𝒪_X`-module `𝓕` and `n > 0`, the higher direct image vanishes: `R^n f_* 𝓕 = 0`.

```lean
theorem isZero_rightDerived_modulePushforward_of_isQuasicoherentOnSite
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (haff : IsAffineHom B S hS f.hom)
    (G : Modules.{u, u} B S hS X.1 X.2) (hG : G.IsQuasicoherentOnSite) (n : ℕ) (hn : 0 < n) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsZero (((modulePushforward B S hS f).rightDerived n).obj G)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardVanishingUnconditional.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineHigherPushforwardVanishingUnconditional.lean#L140). The attribute's comment: “the full statement, for the direct image `Space.modulePushforward`”.

> Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over a scheme `S` contained in a
> big fppf site `B`, and let `𝓕` be a quasi-coherent `𝒪_X`-module. Then the higher direct images
> `R^p f_* 𝓕` vanish for `p > 0`, the direct image being
> `AlgebraicGeometry.Space.modulePushforward`.

```lean
theorem isZero_rightDerived_modulePushforward_isAffineHom (f : X ⟶ Y)
    (haff : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (p : ℕ) (hp : 0 < p) :
    IsZero (((modulePushforward B S hS f).rightDerived p).obj F)
```

**`AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_of_isAffineHom_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismHigherDirectImageVanishing.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismHigherDirectImageVanishing.lean#L99).

> **Stacks 073H.** Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and let
> `𝓕` be a quasi-coherent `𝒪_X`-module.  Then `R^n f_*𝓕 = 0` for every `n > 0`.
>
> The direct image along the representable `f` is the direct image along base change of étale
> charts (`AlgebraicGeometry.Space.modulePushforwardChartIso`); by Stacks 072W its higher direct
> images vanish once the cohomology of `𝓕` vanishes over the base changes of a covering family of
> each chart of `Y`; the affine charts form such a family, their base changes are affine charts of
> `X` because `f` is affine, and over an affine chart a quasi-coherent module has no higher
> cohomology.

```lean
theorem isZero_rightDerived_modulePushforward_of_isAffineHom_of_isQuasicoherent (f : X ⟶ Y)
    (hf : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (n : ℕ) (hn : 0 < n) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsZero (((modulePushforward B S hS f).rightDerived n).obj F)
```

## Tag 0D2U, a lemma

[Tag 0D2U](https://stacks.math.columbia.edu/tag/0D2U) in the Stacks Project.

**`AlgebraicGeometry.Space.cohomologyCollapseIsoOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapse.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapse.lean#L74). The attribute's comment: “the Leray collapse R^i Γ(Y, f\_* -)(F) ≅ H^i(Y, f\_*F), as modules over the global sections of Y, every degree”.

> **Stacks 0D2U.**  Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and `𝓕`
> a quasi-coherent `𝒪_X`-module.  Then for every `i ≥ 0` the cohomology of `𝓕` on `X`, as the
> `i`-th derived functor of `Γ(Y, f_* −) = Γ(X, −)` at `𝓕`, is the cohomology `H^i(Y, f_*𝓕)`.

```lean
def cohomologyCollapseIsoOfIsAffineHom (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := enoughInjectives_modules B S hS Y.1 Y.2
    (((modulePushforward B S hS f ⋙ globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS Y.1 Y.2).O))).rightDerived i).obj F ≅
      ((globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS Y.1 Y.2).O))).rightDerived i).obj
        ((modulePushforward B S hS f).obj F))
```

**`AlgebraicGeometry.Space.cohomologyUliftIsoOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyOverRing.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyOverRing.lean#L359).

> **Stacks 0D2U.** Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and `𝓕`
> a quasi-coherent `𝒪_X`-module. Then `Hⁱ(X, 𝓕) = Hⁱ(Y, f_*𝓕)` for every `i ≥ 0`.
>
> The cohomology is that of the universe lifts of the two modules to the universe of the small
> étale sites, the universe in which `AlgebraicGeometry.Space.eulerCharacteristic` (Stacks 0DN1)
> is taken; the isomorphism is one of abelian groups, and of `A`-modules for any ring maps to the
> global functions compatible with `f`
> (`AlgebraicGeometry.Space.cohomologyUliftOverRingIsoOfIsAffineHom`).

```lean
def cohomologyUliftIsoOfIsAffineHom.{w} (haff : IsAffineHom B S hS f.hom)
    (G : Modules.{u, u} B S hS X.1 X.2) (hG : G.IsQuasicoherentOnSite) (q : ℕ) :
    (forget₂ _ AddCommGrpCat.{max (u + 1) w}).obj
        ((globalModuleCohomology.{u + 1, u, u, w}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)) q).obj
          (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w} G)) ≅
      (forget₂ _ AddCommGrpCat.{max (u + 1) w}).obj
        ((globalModuleCohomology.{u + 1, u, u, w}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)) q).obj
          (SheafOfModules.uliftForPresentation.{u + 1, u, u, u, max (u + 1) w}
            ((modulePushforward B S hS f).obj G)))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.cohomologyIsoOfIsAffineHom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyIso.lean#L230), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapseUnconditional.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineMorphismCohomologyCollapseUnconditional.lean#L124) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.8, Tag 073F](https://stacks.math.columbia.edu/tag/073F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
