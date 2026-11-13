---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ProjectiveSpaceImmersion.twist, AlgebraicGeometry.Space.exists_twistBound_isZero_rightDerived_modulePushforward, AlgebraicGeometry.Space.isCoherent_rightDerived_modulePushforward_of_isProper, AlgebraicGeometry.Space.isCoherent_higherDirectImage_of_isProper, AlgebraicGeometry.Space.moduleFinite_cohomologyOverBase_of_isProper_of_isCoherent, AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper, AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper_of_algebra
statement: formalized
proof: formalized
---

# 69.20 Higher direct images of coherent sheaves

Section 69.20 of the Stacks Project, [Tag 08AP](https://stacks.math.columbia.edu/tag/08AP). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08AQ, a lemma

[Tag 08AQ](https://stacks.math.columbia.edu/tag/08AQ) in the Stacks Project.

**`AlgebraicGeometry.Space.ProjectiveSpaceImmersion.twist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishing.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishing.lean#L207). The attribute's comment: “the twist L = i^* O\_\{P^n\_Y}(1) of the statement”.

> **The twist `L = i^* O_{P^n_Y}(1)` of Stacks 08AQ**: the inverse image of the hyperplane
> sheaf of `P^n_S` along `X ⟶ P^n_Y ⟶ P^n_S`.

```lean
noncomputable def twist (D : ProjectiveSpaceImmersion B S hS n hP X Y) :
    Modules.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.exists_twistBound_isZero_rightDerived_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishingNoetherian.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishingNoetherian.lean#L450). The attribute's comment: “the complete statement, for Y Noetherian and F coherent”.

> **Stacks 08AQ.** Let `i : X ⟶ P^n_Y` be a closed immersion of algebraic spaces over `S` with
> `Y` Noetherian, let `f : X ⟶ Y` be the composite with the projection and let
> `L = i^* O_{P^n_Y}(1)`. For a coherent `𝒪_X`-module `F` there is a `d₀` such that
>
> `R^p f_*(F ⊗ L^{⊗ d}) = 0` for all `d ≥ d₀` and all `p > 0`.
>
> The proof is the source's: over one surjective étale chart of `Y` with Noetherian affine scheme,
> the restriction of `F ⊗ L^{⊗ d}` is a coherent module twisted by an ample invertible module on a
> scheme proper over that affine scheme, and Serre's vanishing theorem (Stacks 02O1) applies.

```lean
theorem exists_twistBound_isZero_rightDerived_modulePushforward
    (hZ : B.Contains (⊤_ Scheme.{u})) (n : ℕ)
    (hP : B.Contains (projectiveSpaceOver n S)) {X Y : AlgebraicSpaces B S hS}
    (D : ProjectiveSpaceImmersion B S hS n hP X Y)
    (hY : IsNoetherian B S hS hZ Y.1) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : IsCoherent B S hS X.1 X.2 F) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    ∃ d₀ : ℕ, ∀ d : ℕ, d₀ ≤ d → ∀ p : ℕ, 0 < p →
      IsZero (((modulePushforward B S hS D.hom).rightDerived p).obj
        (F ⊗ tensorPow B S hS D.twist d))
```

## Tag 08AR, a lemma

[Tag 08AR](https://stacks.math.columbia.edu/tag/08AR) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_rightDerived_modulePushforward_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherence.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherence.lean#L330).

> **Stacks 08AR.**  Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S` with `Y`
> locally Noetherian, and let `𝓕` be a coherent `𝒪_X`-module.  Then `R^i f_*𝓕` is a coherent
> `𝒪_Y`-module for every `i ≥ 0`.
>
> This is `AlgebraicGeometry.Space.isCoherent_higherDirectImage_of_isProper`: `R^i f_*𝓕` is
> quasi-coherent by Stacks 0720, so by Stacks 07UB it suffices that its sections over every affine
> étale chart `V` of `Y` are finite; by Stacks 03LX and the degeneration of the Leray spectral
> sequence over the affine `V` they are the cohomology of `𝓕` restricted to the proper base change
> `X_V ⟶ V`, which is finite by the dévissage of Stacks 08AN with the witness from Chow's
> lemma, `AlgebraicGeometry.Space.hasFiniteCohomologyOver_of_isProper`.

```lean
theorem isCoherent_rightDerived_modulePushforward_of_isProper (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun V : Scheme.{u} ↦ IsLocallyNoetherian V))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F) (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived i).obj F)
```

**`AlgebraicGeometry.Space.isCoherent_higherDirectImage_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherent.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherent.lean#L87). References: EGA III (3.2.1), “more general”.

> **Stacks 08AR.**  Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S` with `Y`
> locally Noetherian, and let `𝓕` be a coherent `𝒪_X`-module.  Then `R^i f_*𝓕` is a coherent
> `𝒪_Y`-module for every `i`.
>
> `R^i f_*𝓕` is quasi-coherent by Stacks 0720, so by Stacks 07UB it suffices that its sections over
> every affine étale chart `V` of `Y` are finite over `𝒪_Y(V)`.  Those sections are the sections
> over the identity chart of the restriction of `R^i f_*𝓕` to `V`, which is
> `R^i f'_*(𝓕|_U)` for the base change `f' : U = V ×_Y X ⟶ V` by Stacks 03LX; over the affine
> scheme `V` this is `R^i Γ(V, f'_* −)(𝓕|_U)`, the higher direct images of `f'` being
> quasi-coherent and hence acyclic over the affine `V` (Stacks 0720 and 03DW, degenerating the
> Leray spectral sequence).  The base change `f'` is proper (Stacks 0EPD) and `𝓕|_U` is coherent,
> so `AlgebraicGeometry.Space.hasFiniteCohomologyOver_of_isProper` applies.

```lean
theorem isCoherent_higherDirectImage_of_isProper {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsProper B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun V : Scheme.{u} ↦ IsLocallyNoetherian V))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F) (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived i).obj F)
```

## Tag 08AS, a lemma

[Tag 08AS](https://stacks.math.columbia.edu/tag/08AS) in the Stacks Project.

**`AlgebraicGeometry.Space.moduleFinite_cohomologyOverBase_of_isProper_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyOverBaseFinite.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyOverBaseFinite.lean#L66). The attribute's comment: “H^i(X, F) as cohomologyOverBase, at every module universe max (u + 1) w”.

> **Stacks 08AS.**  Let `A` be a Noetherian ring, `f : X ⟶ Spec A` a proper morphism of
> algebraic spaces and `F` a coherent `𝒪_X`-module.  Then `Hⁱ(X, F)` is a finite `A`-module for
> every `i ≥ 0`.
>
> Here `Hⁱ(X, F)` is `AlgebraicGeometry.Space.cohomologyOverBase`, at any module universe
> `max (u + 1) w`.  `F` is the universe lift of a coherent module at the universe `u` of the
> structure rings, where the finiteness is
> `AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper` (the affine case of Stacks 08AR),
> and the cohomology over the base of a lift is the lift of the cohomology.

```lean
theorem moduleFinite_cohomologyOverBase_of_isProper_of_isCoherent
    (A : Type u) [CommRing A] (B : BigFppfSite.{u}) (hA : B.Contains (Spec (.of A)))
    [IsNoetherianRing A]
    (X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseObject A B hA)) (hf : IsProper B (Spec (.of A)) hA f)
    (F : Modules.{u, max (u + 1) w} B (Spec (.of A)) hA X hX)
    [IsCoherent B (Spec (.of A)) hA X hX F] (i : ℕ) :
    Module.Finite A (cohomologyOverBase.{u, w} A B hA X hX F i)
```

**`AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModuleCohomologyFinite.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperModuleCohomologyFinite.lean#L298).

> **Stacks 08AS.**  Let `A` be a Noetherian ring, `f : X ⟶ Spec A` a proper morphism of
> algebraic spaces and `F` a coherent `𝒪_X`-module.  Then `Hⁱ(X, F)` is a finite `A`-module for
> every `i ≥ 0`.
>
> The right derived functors of `Γ(Spec A, f_* −)` are finite over the functions on `Spec A` at
> a coherent module (`AlgebraicGeometry.Space.hasFiniteCohomologyOver_of_isProper`, the core of
> Stacks 08AR), and `Γ(Spec A, f_* −)` is `Γ(X, −)` as a functor to `A`-modules
> (`AlgebraicGeometry.Space.globalSectionsOverBaseIso`); restriction of scalars and the universe
> lift are exact, so they pass through the right derived functors.

```lean
theorem moduleFinite_cohomology_of_isProper [IsNoetherianRing A]
    (X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseObject A B hA)) (hf : IsProper B (Spec (.of A)) hA f)
    (F : Modules.{u, u} B (Spec (.of A)) hA X hX) [IsCoherent B (Spec (.of A)) hA X hX F]
    (i : ℕ) :
    Module.Finite A ((ModuleCat.restrictScalars (baseRingHom A B hA X hX)).obj
      (((globalSectionsFunctor.{u + 1, u, u, u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B (Spec (.of A)) hA X hX).O)).rightDerived
          i).obj F))
```

## Tag 08AT, a lemma

[Tag 08AT](https://stacks.math.columbia.edu/tag/08AT) in the Stacks Project.

**`AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper_of_algebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyFiniteAlgebra.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyFiniteAlgebra.lean#L374). The attribute's comment: “ungraded, which is more general: the grading is never used by the proof”.

> **Stacks 08AT.**  Let `A` be a Noetherian ring, `R` a finitely generated `A`-algebra and
> `f : X ⟶ Spec A` a proper morphism of algebraic spaces.  Let `F` be a quasi-coherent
> `𝒪_X`-module which is a module over `f^* R̃` of finite type: an action `ρ : R →+* End F`
> restricting on `A` to multiplication by the scalars, such that over every affine étale chart `U`
> of `X` the sections `F(U)` are generated over `𝒪(U)` by the `ρ(R)`-translates of finitely many
> sections.
> Then `Hⁱ(X, F)` is a finite `R`-module for every `i`.
>
> The source states this for a graded `R` and a graded module; the grading is not used, and the
> graded module `Hⁱ(X, F)` of the source is the cohomology of the total module `F` here.

```lean
theorem moduleFinite_cohomology_of_isProper_of_algebra [IsNoetherianRing A]
    {X : AlgebraicSpaces B (Spec (.of A)) hA} (f : X ⟶ schemeSpace (baseObject A B hA))
    (hf : IsProper B (Spec (.of A)) hA f.hom) (F : Modules.{u, u} B (Spec (.of A)) hA X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (ρ : R →+* End F)
    (hρ : ∀ a, (ρ (algebraMap A R a)).asHom = globalSmul _ (baseRingHom A B hA X.1 X.2 a) F)
    (hfin : ∀ U : SmallEtale B (Spec (.of A)) hA X.1,
      IsAffine ((SmallEtale.toOver B (Spec (.of A)) hA X.1 ⋙
        BigFppfOver.toScheme B (Spec (.of A)) hA).obj U) →
      ∃ g : Finset (F.val.obj (op U)), Submodule.span (chartRing B (Spec (.of A)) hA X.1 X.2 U)
        {x | ∃ r, ∃ y ∈ g, x = (ρ r).asHom.val.app (op U) y} = ⊤)
    (i : ℕ) :
    letI := (spaceCohomology B (Spec (.of A)) hA X i).endActionModule ρ
    Module.Finite R ((spaceCohomology B (Spec (.of A)) hA X i).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.20, Tag 08AP](https://stacks.math.columbia.edu/tag/08AP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
