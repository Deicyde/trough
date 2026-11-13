---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.BaseChangeDiagram, AlgebraicGeometry.Space.BaseChangeDiagram.pulledBack, AlgebraicGeometry.Space.BaseChangeDiagram.derivedPushforward, AlgebraicGeometry.Space.BaseChangeDiagram.derivedPushforward', AlgebraicGeometry.Space.isIso_rightDerivedFunctorPlusUnit_app_modulePushforward_isAffineHom, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_isAffineHom, AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_isAffineHom, AlgebraicGeometry.Space.isIso_moduleBaseChangeMap_app_of_isAffineHom
statement: formalized
proof: formalized
---

# 69.11 Cohomology and base change, I

Section 69.11 of the Stacks Project, [Tag 073I](https://stacks.math.columbia.edu/tag/073I). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 073J, an equation

[Tag 073J](https://stacks.math.columbia.edu/tag/073J) in the Stacks Project.

**`AlgebraicGeometry.Space.BaseChangeDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean#L168). The attribute's comment: “the cartesian square and its coefficient”.

> The base-change diagram for cohomology of algebraic spaces: a cartesian square of algebraic
> spaces over `S`, together with a quasi-coherent `𝒪_X`-module `𝓕` on the source `X` of the
> morphism `f` that is being base changed.

```lean
structure BaseChangeDiagram
```

**`AlgebraicGeometry.Space.BaseChangeDiagram.pulledBack`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean#L199). The attribute's comment: “the pulled-back coefficient”.

> The coefficient `𝓕' = (g')^*𝓕` on the base-changed source.

```lean
abbrev pulledBack : Modules.{u, u} B S hS D.X'.1 D.X'.2
```

**`AlgebraicGeometry.Space.BaseChangeDiagram.derivedPushforward`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean#L204). The attribute's comment: “the lower-right derived direct image”.

> The total derived direct image `Rf_*𝓕` on the lower-right corner.

```lean
abbrev derivedPushforward : DerivedCategory.Plus (Modules.{u, u} B S hS D.Y.1 D.Y.2)
```

**`AlgebraicGeometry.Space.BaseChangeDiagram.derivedPushforward'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyBaseChange.lean#L211). The attribute's comment: “the lower-left derived direct image”.

> The total derived direct image `Rf'_*𝓕'` on the lower-left corner.

```lean
abbrev derivedPushforward' : DerivedCategory.Plus (Modules.{u, u} B S hS D.Y'.1 D.Y'.2)
```

## Tag 07U8, a lemma

[Tag 07U8](https://stacks.math.columbia.edu/tag/07U8) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_rightDerivedFunctorPlusUnit_app_modulePushforward_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDirectImageDerivedComparison.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineDirectImageDerivedComparison.lean#L122). The attribute's comment: “f\_*F ≅ Rf\_*F: the canonical map from the direct image to the derived direct image is an isomorphism”.

> **Stacks 07U8, `f_*F ≅ Rf_*F`.** Let `f : X ⟶ Y` be an affine morphism of algebraic spaces
> over `S` and let `F` be a quasi-coherent `𝒪_X`-module. Then the canonical map from the direct
> image `f_*F`, placed in degree zero, to the derived direct image `Rf_*F` is an isomorphism: the
> unit of the right derived functor `Rf_*` of `f_*` on bounded below derived categories is
> invertible at `F[0]`.
>
> Equivalently `R^p f_*F = 0` for `p > 0`, which is
> `AlgebraicGeometry.Space.isZero_rightDerived_modulePushforward_isAffineHom` (Stacks 073H, the
> reduction of the source to Stacks 02KG through Equation 69.3.0.1); the two are equivalent for the
> left exact functor `f_*` by part (2) of Stacks 015C. No model of the derived categories is
> fixed.

```lean
theorem isIso_rightDerivedFunctorPlusUnit_app_modulePushforward_isAffineHom
    [HasDerivedCategory.{w} (Modules.{u, u} B S hS X.1 X.2)]
    [HasDerivedCategory.{w'} (Modules.{u, u} B S hS Y.1 Y.2)]
    (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) :
    IsIso ((modulePushforward B S hS f).rightDerivedFunctorPlusUnith.app
      ((HomotopyCategory.Plus.singleFunctor (Modules.{u, u} B S hS X.1 X.2) 0).obj F))
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineDirectImageQuasicoherent.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineDirectImageQuasicoherent.lean#L105). The attribute's comment: “quasi-coherence of the direct image, reduced chartwise to the case of a target represented by a scheme of the site, which is the hypothesis h”.

> **Stacks 07U8, the quasi-coherence of the direct image.** Let `f : X ⟶ Y` be an affine
> morphism of algebraic spaces over `S` and let `F` be a quasi-coherent `𝒪_X`-module. Then the
> direct image `f_*F` is quasi-coherent.
>
> The hypothesis `h` is the same statement for a target represented by a scheme of the site.
> Everything else is the reduction of the source: quasi-coherence is chartwise by Stacks 03LZ,
> the restriction of `f_*F` to a chart is the direct image along the base change of `f` by
> Stacks 03LX, and a base change of an affine morphism is affine.

```lean
theorem isQuasicoherentOnSite_modulePushforward_of_isAffineHom
    (h : SchemeTargetAffinePushforwardQuasicoherent B S hS)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    ((modulePushforward B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardQuasicoherentUnconditional.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffinePushforwardQuasicoherentUnconditional.lean#L176). The attribute's comment: “quasi-coherence of the direct image”.

> **Stacks 07U8, the quasi-coherence of the direct image, with no hypothesis.**  Let
> `f : X ⟶ Y` be an affine morphism of algebraic spaces over `S` and let `F` be a quasi-coherent
> `𝒪_X`-module. Then the direct image `f_*F` is quasi-coherent.
>
> This is `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_isAffineHom` with its
> hypothesis supplied by
> `AlgebraicGeometry.Space.schemeTargetAffinePushforwardQuasicoherent`.

```lean
theorem isQuasicoherentOnSite_modulePushforward_isAffineHom {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) :
    ((modulePushforward B S hS f).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isIso_moduleBaseChangeMap_app_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleAffineBaseChange.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModuleAffineBaseChange.lean#L228). The attribute's comment: “base change: g^*f\_*F = f'\_*(g')^*F for f affine and F quasi-coherent”.

> **Affine base change for the direct image of a quasi-coherent module** (the base change
> clause of Stacks 07U8; Stacks 02KG for schemes).  For a cartesian square of algebraic spaces
> whose right morphism `f` is affine, the base change map `g^*f_*F ⟶ f'_*(g')^*F` is an
> isomorphism at every quasi-coherent `𝒪_X`-module `F`.  The bottom morphism `g` is
> arbitrary.

```lean
theorem isIso_moduleBaseChangeMap_app_of_isAffineHom (sq : IsPullback g' f' f g)
    (hf : IsAffineHom B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) :
    IsIso ((moduleBaseChangeMap f g f' g' sq.w).app F)
```

## Tag 073K, a lemma

[Tag 073K](https://stacks.math.columbia.edu/tag/073K) in the Stacks Project.

**`AlgebraicGeometry.Space.cohomologyFlatBaseChangeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyAffineFlatBaseChange.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyAffineFlatBaseChange.lean#L288). The attribute's comment: “part (2)”.

> Flat base change of cohomology over an affine base.
>
> Let `q : W ⟶ V` be a flat morphism of affine schemes of the site, `A = Γ(V, 𝒪)` and
> `R = Γ(W, 𝒪)`.  Let `p : X ⟶ V` be a quasi-compact and quasi-separated morphism of algebraic
> spaces over `S`, `X' = W ×_V X` with projections `pr' : X' ⟶ W` and `pr : X' ⟶ X`, and `ℱ` a
> quasi-coherent `𝒪_X`-module with pullback `ℱ' = pr^* ℱ`.  Then for every `i ≥ 0`
>
> `R ⊗_A H^i(X, ℱ) ≅ H^i(X', ℱ')`
>
> as `R`-modules, `A` acting on `H^i(X, ℱ)` through `p` and `R` acting on `H^i(X', ℱ')` through
> `pr'`.

```lean
def cohomologyFlatBaseChangeEquiv [Flat ((BigFppfOver.toScheme B S hS).map q)]
    (hpc : IsQuasiCompact B S hS p.hom) (hps : IsQuasiSeparated B S hS p.hom)
    (hF : F.IsQuasicoherentOnSite) (i : ℕ) :
    letI := ((BigFppfOver.toScheme B S hS).map q).appTop.hom.toAlgebra
    Γ((BigFppfOver.toScheme B S hS).obj W, ⊤) ⊗[Γ((BigFppfOver.toScheme B S hS).obj V, ⊤)]
        cohomologyRes (baseFunctionsToGlobalSections B S hS p) i F
      ≃ₗ[Γ((BigFppfOver.toScheme B S hS).obj W, ⊤)]
      cohomologyRes (baseFunctionsToGlobalSections B S hS (pullback.fst (schemeSpaceMap q) p)) i
        ((modulePullback B S hS (pullback.snd (schemeSpaceMap q) p)).obj F)
```

**`AlgebraicGeometry.Space.BaseChangeDiagram.baseChangeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyFlatBaseChange.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyFlatBaseChange.lean#L200). The attribute's comment: “the base change map of Tag 0736 for the cartesian square, whose invertibility is what part (1) asserts. The map is CONSTRUCTED and characterized; neither part (1) nor part (2) of the tag is proved here”.

> **The base change map `g^*Rf_* ⟶ Rf'_*(g')^*`** of **Stacks 0736**, for the cartesian
> square of small étale ringed topoi attached to a cartesian square of algebraic spaces whose
> lower horizontal morphism `g` is flat.
>
> **Stacks 073K**, part (1) asserts that it is invertible.  It is built from the comparison
> `directImageSquareIso` of the two composite direct images and the flatness of the morphisms of
> ringed topoi of `g` and `g'` (`isFlat_smallEtaleRingedToposHom_base`,
> `isFlat_smallEtaleRingedToposHom_source`).

```lean
def baseChangeMap (hg : IsFlat B S hS D.g.hom) :
    (pushforwardModules (X := smallEtaleRingedTopos B S hS D.X)
          (Y := smallEtaleRingedTopos B S hS D.Y)
          (smallEtaleRingedToposHom B S hS D.f).toRingedToposModulesHom).rightDerivedFunctorPlus ⋙
        D.flatPullbackBase hg ⟶
      D.flatPullbackSource hg ⋙
        (pushforwardModules (X := smallEtaleRingedTopos B S hS D.X')
          (Y := smallEtaleRingedTopos B S hS D.Y')
          (smallEtaleRingedToposHom B S hS D.f').toRingedToposModulesHom).rightDerivedFunctorPlus
```

**`AlgebraicGeometry.Space.BaseChangeDiagram.baseChangeMap_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyFlatBaseChange.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyFlatBaseChange.lean#L222). The attribute's comment: “canonical characterization of the base change map of Tag 0736 for the cartesian square: it is determined by its agreement, after the derived-functor unit of Rf\_*, with the degreewise comparison. Neither part (1) nor part (2) of the tag is proved here”.

> **The base change map of the square is the canonical one.**  Composed with the
> derived-functor unit of `Rf_*`, it is the degreewise comparison on the bounded below homotopy
> category of `𝒪_X`-modules.  Since `Rf_* ⋙ g^*` is a right derived functor of `f_* ⋙ g^*` with
> that unit, this equation determines the map.

```lean
theorem baseChangeMap_fac (hg : IsFlat B S hS D.g.hom) :
    Functor.whiskerRight
        (pushforwardModules (X := smallEtaleRingedTopos B S hS D.X)
          (Y := smallEtaleRingedTopos B S hS D.Y)
          (smallEtaleRingedToposHom B S hS
            D.f).toRingedToposModulesHom).rightDerivedFunctorPlusUnith
        (D.flatPullbackBase hg) ≫
      (Functor.associator _ _ _).hom ≫
      Functor.whiskerLeft DerivedCategory.Plus.Qh (D.baseChangeMap hg) =
        Stacks.Cohomology.ToposBaseChange.baseChangeOnHomotopyCategory
          (smallEtaleRingedToposHom B S hS D.f) (smallEtaleRingedToposHom B S hS D.f')
          (smallEtaleRingedToposHom B S hS D.g) (smallEtaleRingedToposHom B S hS D.g')
          D.directImageSquareIso (D.isFlat_smallEtaleRingedToposHom_base hg)
          (D.isFlat_smallEtaleRingedToposHom_source hg)
```

**`AlgebraicGeometry.Space.BaseChangeDiagram.affineCohomologyBaseChangeIsoBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyBaseChangeBLinear.lean, line 742](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyBaseChangeBLinear.lean#L742). The attribute's comment: “part (2), the affine case: H^i(X,F) ⊗\_A B = H^i(X',F') as B-modules”.

> **Flat base change of cohomology over affine bases: `H^i(X, 𝓕) ⊗_A B = H^i(X', 𝓕')` as
> `B`-modules.** For the cartesian square of **Stacks 073J** with `𝓕` quasi-coherent, `g` flat, `f`
> quasi-compact and quasi-separated and the two bases affine — `Y = Spec(A)` and `Y' = Spec(B)`,
> presented by the charts `V₀` and `V₀'` with `A` and `B` their coordinate rings — the extension of
> scalars of `H^i(X, 𝓕)` along `A ⟶ B` is the cohomology of the pulled back coefficient on `X'`, in
> every degree `i`, as modules over `B`: the left hand side by its tensor factor `B` and the right
> hand side because `X'` lives over `Y' = Spec(B)`. The left hand side is written `B ⊗_A H^i(X, 𝓕)`,
> the extension of scalars.

```lean
def affineCohomologyBaseChangeIsoBase (hZ : B.Contains (⊤_ Scheme.{u}))
    (hg : IsFlat B S hS D.g.hom) (hqc : IsQuasiCompact B S hS D.f.hom)
    (hqs : IsQuasiSeparated B S hS D.f.hom)
    [IsAffine (chartScheme V₀)] [IsAffine (chartScheme V₀')] (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS D.X.1 D.X.2
    have := hasInjectiveResolutions_modules B S hS D.X'.1 D.X'.2
    have := enoughInjectives_modules B S hS D.X.1 D.X.2
    letI := baseChartAlgebra B S hS D.g V₀ V₀'
    ModuleCat.of (baseChartRing B S hS D.Y' V₀')
        (baseChartRing B S hS D.Y' V₀' ⊗[baseChartRing B S hS D.Y V₀]
          ↥(D.affineCohomologyOverBaseChart V₀ i)) ≅
      (baseChartRestrictScalars B S hS D.Y' (isTerminal_of_isIso_chart B S hS D.Y' V₀')).obj
        (D.affineCohomologyTarget i)
```

**`AlgebraicGeometry.Space.isIso_higherDirectImageBaseChangeMap_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageFlatBaseChange.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageFlatBaseChange.lean#L246). The attribute's comment: “part (1): for a cartesian square of algebraic spaces with g flat and f quasi-compact and quasi-separated, the base change map g^*R^if\_*F ⟶ R^if'\_*F' of Tag 0736 is an isomorphism for every quasi-coherent F and every i ≥ 0”.

> **Stacks 073K, part (1): flat base change for higher direct images.**  Let
>
> ```
>   X' ———→ X
>    | f'    | f
>    v       v
>   Y' ———→ Y
>       g
> ```
>
> be a cartesian square of algebraic spaces over `S` with `g` flat and `f` quasi-compact and
> quasi-separated, and let `𝓕` be a quasi-coherent `𝒪_X`-module with pullback `𝓕' = (g')^*𝓕`.  For
> every `i ≥ 0` the base change map of **Stacks 0736**
>
> `g^*R^if_*𝓕 ⟶ R^if'_*𝓕'`
>
> (`AlgebraicGeometry.Space.higherDirectImageBaseChangeMap`) is an isomorphism.
>
> The exactness of the two inverse images `g^*` and `(g')^*` that the base change map is constructed
> against is **Stacks 04JC** for the flat `g` and, `g'` being flat by **Stacks 03MO**, for `g'`.

```lean
theorem isIso_higherDirectImageBaseChangeMap_of_isFlat {f : X ⟶ Y} {g : Y' ⟶ Y}
    {f' : X' ⟶ Y'} {g' : X' ⟶ X} (sq : IsPullback g' f' f g) (hg : IsFlat B S hS g.hom)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) (i : ℕ) :
    have := preservesFiniteLimits_modulePullback_of_isFlat_hom B S hS g hg
    have := preservesFiniteColimits_modulePullback_smallEtale B S hS g
    have := preservesFiniteLimits_modulePullback_of_isFlat_hom B S hS g'
      ((isFlat_isStableUnderBaseChange B S hS).of_isPullback sq.flip hg)
    have := preservesFiniteColimits_modulePullback_smallEtale B S hS g'
    IsIso ((higherDirectImageBaseChangeMap f g f' g' sq.w i).app F)
```

## Tag 0HAP, a lemma

[Tag 0HAP](https://stacks.math.columbia.edu/tag/0HAP) in the Stacks Project.

**`AlgebraicGeometry.Space.counitSplitEpiOfSeparatedEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedEtaleDiagonalSplitEpi.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedEtaleDiagonalSplitEpi.lean#L257).

> **Stacks 0HAP.**  Let `f : X ⟶ Y` be a separated étale morphism of algebraic spaces over a
> scheme `S` contained in a big fppf site `B`, and let `ℱ` be an `𝒪_X`-module.  Then the counit
> `f^*f_*ℱ ⟶ ℱ` of the adjunction of Stacks 03LU is a split epimorphism.
>
> The reduction to the diagonal is
> `AlgebraicGeometry.Space.counitSplitEpiOfSplitEpiChartUnit`, and the splitting along the
> diagonal is `AlgebraicGeometry.Space.splitEpiDiagonalChartUnit`: extension by zero across the
> clopen diagonal.
>
> Stacks 0HAP assumes `f` quasi-compact and `ℱ` quasi-coherent; neither hypothesis is used here,
> see the implementation notes.

```lean
noncomputable def counitSplitEpiOfSeparatedEtale (F : Modules.{u, u} B S hS X.1 X.2) :
    SplitEpi ((modulePullbackAdjunction B S hS f).counit.app F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.11, Tag 073I](https://stacks.math.columbia.edu/tag/073I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
