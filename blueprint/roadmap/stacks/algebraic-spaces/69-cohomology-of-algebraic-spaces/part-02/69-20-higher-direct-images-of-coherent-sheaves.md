---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ProjectiveSpaceImmersion.twist, AlgebraicGeometry.Space.exists_isZero_rightDerived_modulePushforward_tensor_twist, AlgebraicGeometry.Space.exists_twistBound_isZero_rightDerived_modulePushforward, AlgebraicGeometry.Space.isCoherent_rightDerived_modulePushforward_of_isProper, AlgebraicGeometry.Space.isCoherent_rightDerived_of_isProper, AlgebraicGeometry.Space.isCoherent_higherDirectImage_of_isProper, AlgebraicGeometry.Space.moduleFinite_cohomologyOverBase_of_isProper, AlgebraicGeometry.Space.moduleFinite_cohomologyOverBase_of_isProper_of_isCoherent
statement: formalized
proof: formalized
---

# 69.20 Higher direct images of coherent sheaves

Section 69.20 of the Stacks Project, [Tag 08AP](https://stacks.math.columbia.edu/tag/08AP). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08AQ, a lemma

[Tag 08AQ](https://stacks.math.columbia.edu/tag/08AQ) in the Stacks Project.

**`AlgebraicGeometry.Space.ProjectiveSpaceImmersion.twist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishing.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishing.lean#L221). The attribute's comment: “the twist L = i^* O\_\{P^n\_Y}(1) of the statement”.

> **The twist `L = i^* O_{P^n_Y}(1)` of Stacks 08AQ**: the inverse image of the hyperplane
> sheaf of `P^n_S` along `X ⟶ P^n_Y ⟶ P^n_S`.

```lean
noncomputable def twist (D : ProjectiveSpaceImmersion B S hS n hP X Y) :
    Modules.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.exists_isZero_rightDerived_modulePushforward_tensor_twist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishing.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishing.lean#L276). The attribute's comment: “the étale-local reduction of the source's proof, by Stacks 071Z, with representability of the composite proved; the scheme case, where the source cites Stacks 02O1, is carried as the hypothesis h02O1 and is not proved — note that h02O1 is this same eventual vanishing after base change to an étale scheme chart of Y, so it is the source's reduction target rather than side-work, and discharging it needs both the conditional repository form of Stacks 02O1 and the étale-versus-Zariski comparison Stacks 03DW”.

> **Stacks 08AQ, with the scheme case carried as `h02O1`.**
>
> Let `i : X ⟶ P^n_Y` be a closed immersion of algebraic spaces over `S` with `Y` Noetherian, let
> `f : X ⟶ Y` be the composite with the projection and let `L = i^* O_{P^n_Y}(1)`.  For a coherent
> `𝒪_X`-module `F` there is a `d₀` such that
>
> `R^p f_*(F ⊗ L^{⊗ d}) = 0` for all `d ≥ d₀` and all `p > 0`.
>
> The source's proof is the étale-local reduction on `Y`, and that is what is proved: Equation
> 69.3.0.1 (Stacks 071Z) identifies the restriction of `R^p f_*` to an étale scheme chart of `Y`
> with the corresponding higher direct image of the base change, and a module on the small étale
> site of `Y` vanishes as soon as all those restrictions do.  Representability of `f`, which
> Stacks 071Z needs, is supplied by
> `AlgebraicGeometry.Space.ProjectiveSpaceImmersion.relativelyRepresentable_hom`.  What remains is
> the conclusion over a scheme chart, which is where the source cites Stacks 02O1; it is carried
> as `h02O1` and is not proved.  Noetherianity of `Y` and coherence of `F` are the source's
> hypotheses and are what would discharge `h02O1`; the reduction itself uses neither.

```lean
theorem exists_isZero_rightDerived_modulePushforward_tensor_twist
    (hZ : B.Contains (⊤_ Scheme.{u})) (n : ℕ)
    (hP : B.Contains (projectiveSpaceOver n S)) {X Y : AlgebraicSpaces B S hS}
    (D : ProjectiveSpaceImmersion B S hS n hP X Y)
    (hY : IsNoetherian B S hS hZ Y.1) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : IsCoherent B S hS X.1 X.2 F)
    (h02O1 : ChartwiseEventualTwistVanishing B S hS D.hom D.relativelyRepresentable_hom F
      D.twist) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    ∃ d₀ : ℕ, ∀ d : ℕ, d₀ ≤ d → ∀ p : ℕ, 0 < p →
      IsZero (((modulePushforward B S hS D.hom).rightDerived p).obj
        (F ⊗ tensorPow B S hS D.twist d))
```

**`AlgebraicGeometry.Space.exists_twistBound_isZero_rightDerived_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishingNoetherian.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProjectiveTwistHigherDirectImageVanishingNoetherian.lean#L446).

> **Stacks 08AQ.** Let `i : X ⟶ P^n_Y` be a closed immersion of algebraic spaces over `S` with
> `Y` Noetherian, let `f : X ⟶ Y` be the composite with the projection and let
> `L = i^* O_{P^n_Y}(1)`. For a coherent `𝒪_X`-module `F` there is a `d₀` such that
>
> `R^p f_*(F ⊗ L^{⊗ d}) = 0` for all `d ≥ d₀` and all `p > 0`.

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

**`AlgebraicGeometry.Space.isCoherent_rightDerived_modulePushforward_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherence.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherence.lean#L305). The attribute's comment: “conditional on three cited results carried as explicit hypotheses: Stacks 0720 as h0720 (quasi-coherence of the higher direct images), Stacks 08AN as h08AN (the devissage of coherent modules, with its Noetherian hypothesis on X relaxed to the local Noetherianity that properness supplies) and the third condition of the source's devissage as hwitness (a coherent module with full support on each reduced closed subspace with irreducible point set, whose direct image has coherent higher direct images -- the source gets it from Stacks 089J, 08AQ and 02O4, and Stacks 09YC serves as well). The other two conditions of Stacks 08AN are PROVED here for this property, and so is the local Noetherianity of X”.

> **Stacks 08AR**, with the three cited inputs of the source's proof carried as hypotheses.
> Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S` with `Y` locally Noetherian
> and let `𝓕` be a coherent `𝒪_X`-module.  Then `R^i f_*𝓕` is a coherent `𝒪_Y`-module for every
> `i`.
>
> The dévissage `h08AN` of Stacks 08AN is applied to the property that all higher direct images
> are coherent.  Its local Noetherianity premise is discharged from properness by Stacks 04ZK;
> its two-out-of-three and finite-sum conditions are
> `AlgebraicGeometry.Space.hasCoherentHigherDirectImages_twoOutOfThree` and
> `AlgebraicGeometry.Space.hasCoherentHigherDirectImages_finiteSum`, proved above from the long
> exact sequence of the higher direct images together with Stacks 07UC and Stacks 07UD and
> consuming the quasi-coherence hypothesis `h0720` of Stacks 0720; its integral-subspace
> condition is `hwitness` and is not proved.

```lean
theorem isCoherent_rightDerived_modulePushforward_of_isProper (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun V : Scheme.{u} ↦ IsLocallyNoetherian V))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (h0720 : QuasicoherentHigherDirectImages B S hS f)
    (h08AN : CoherentDevissage B S hS X (HasCoherentHigherDirectImages B S hS f))
    (hwitness :
      CoherentDevissageIntegralWitness B S hS X (HasCoherentHigherDirectImages B S hS f))
    (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived i).obj F)
```

**`AlgebraicGeometry.Space.isCoherent_rightDerived_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherenceWitness.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherenceWitness.lean#L110).

> **Stacks 08AR.**  Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S` with `Y`
> locally Noetherian, and let `𝓕` be a coherent `𝒪_X`-module.  Then `R^i f_* 𝓕` is a coherent
> `𝒪_Y`-module for every `i ≥ 0`.
>
> This is `AlgebraicGeometry.Space.isCoherent_rightDerived_of_isProper_of_witness` (the reduction to
> a Noetherian affine base and the dévissage of Stacks 08AN on the source), with the integral
> witness supplied by
> `AlgebraicGeometry.Space.hasCoherentWitnessOnIntegralSubspaces_of_isProper_of_isAffine`.

```lean
theorem isCoherent_rightDerived_of_isProper {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun V : Scheme.{u} ↦ IsLocallyNoetherian V))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F) (n : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived n).obj F)
```

**`AlgebraicGeometry.Space.isCoherent_higherDirectImage_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherent.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperHigherDirectImageCoherent.lean#L86). References: EGA III (3.2.1), “more general”.

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

**`AlgebraicGeometry.Space.moduleFinite_cohomologyOverBase_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyFinite.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyFinite.lean#L141). The attribute's comment: “with the finiteness in the degrees below the vanishing bound carried as the hypothesis hlt, that being the one step needing Stacks 08AR, whose higher direct images cannot be written at the module universe of cohomologyOverBase”.

> **Stacks 08AS.**  For a Noetherian ring `A`, a proper algebraic space `X` over `Spec A` and
> a coherent `𝒪_X`-module `F`, every cohomology module `Hⁱ(X, F)` is a finite `A`-module: above
> the vanishing bound `N` the module is zero, hence finite, and below it finiteness is assumed.
> Properness and coherence are the hypotheses under which the bound and that finiteness hold and
> are used nowhere in the proof.

```lean
theorem moduleFinite_cohomologyOverBase_of_isProper [IsNoetherianRing A]
    (f : X ⟶ CategoryTheory.yoneda.obj (baseObject A B hA))
    (_hf : IsProper B (Spec (.of A)) hA f)
    (F : Modules.{u, max (u + 1) w} B (Spec (.of A)) hA X hX)
    [IsCoherent B (Spec (.of A)) hA X hX F] (N : ℕ)
    (hvan : ∀ i, N ≤ i → Limits.IsZero (cohomologyOverBase.{u, w} A B hA X hX F i))
    (hlt : ∀ i < N, Module.Finite A (cohomologyOverBase.{u, w} A B hA X hX F i)) (i : ℕ) :
    Module.Finite A (cohomologyOverBase.{u, w} A B hA X hX F i)
```

**`AlgebraicGeometry.Space.moduleFinite_cohomologyOverBase_of_isProper_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyOverBaseFinite.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyOverBaseFinite.lean#L68).

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

**`AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModuleCohomologyFinite.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperModuleCohomologyFinite.lean#L297).

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

**`AlgebraicGeometry.Space.moduleFinite_cohomology_of_isProper_of_algebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyFiniteAlgebra.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperCohomologyFiniteAlgebra.lean#L373). The attribute's comment: “ungraded, which is more general: the grading is never used by the proof”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
