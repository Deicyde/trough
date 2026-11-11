---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_derivedPullbackComparison_blowUpToBase, AlgebraicGeometry.derivedPullbackBlowUpToBaseIso, AlgebraicGeometry.isPerfect_modulePullback_blowUpToBase, AlgebraicGeometry.hasTorAmplitude_modulePullback_blowUpToBase, AlgebraicGeometry.exists_isAdmissibleBlowup_shortExact_strictTransform, AlgebraicGeometry.isAdmissibleBlowup_blowUpToBase_fittingIdealProd, AlgebraicGeometry.isEffectiveCartierDivisor_fittingIdeal_pullback_fittingIdealProd, AlgebraicGeometry.isAdmissibleBlowup_blowUpToBase_fittingIdealProdAll
statement: formalized
proof: formalized
---

# 38.41 Blowing up perfect modules

Section 38.41 of the Stacks Project, [Tag 0F8K](https://stacks.math.columbia.edu/tag/0F8K). 4 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ESS, a lemma

[Tag 0ESS](https://stacks.math.columbia.edu/tag/0ESS) in the Stacks Project.

**`AlgebraicGeometry.isIso_derivedPullbackComparison_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean#L618). The attribute's comment: “derived pullback agrees with ordinary pullback”.

> **Stacks 0ESS, the derived pullback.** For an `𝒪_X`-module of Tor dimension at most one the
> canonical comparison `Lb^*ℱ ⟶ b^*ℱ` along the blowup of `X` in a quasi-coherent ideal is
> invertible.
>
> A two-term flat resolution of `ℱ` exists by Stacks 08CI; it is K-flat by Stacks 06YQ, so the
> comparison is invertible on it by Stacks 06YJ, and its degreewise pullback is again a resolution
> of `b^*ℱ` because pullback to the blowup keeps the injection of its first term injective.

```lean
theorem isIso_derivedPullbackComparison_blowUpToBase (F : OXMod.{u, u} X.toRingedSpace)
    (htor : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F) (-1) 0) :
    IsIso ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullbackComparison
      (blowUpToBase I).toLRSHom.toShHom).app
      ((HomotopyCategory.quotient (OXMod.{u, u} X.toRingedSpace) (.up ℤ)).obj
        ((CochainComplex.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F)))
```

**`AlgebraicGeometry.derivedPullbackBlowUpToBaseIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean, line 667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean#L667). The attribute's comment: “derived pullback is the ordinary pullback”.

> **Stacks 0ESS, the identification `Lb^*ℱ = b^*ℱ`.** For an `𝒪_X`-module of Tor dimension at
> most one, the derived pullback to the blowup of `X` in a quasi-coherent ideal is the ordinary
> pullback, placed in degree `0`.

```lean
noncomputable def derivedPullbackBlowUpToBaseIso (F : OXMod.{u, u} X.toRingedSpace)
    (htor : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F) (-1) 0) :
    (Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        (blowUpToBase I).toLRSHom.toShHom).obj
        ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F) ≅
      (DerivedCategory.singleFunctor (OXMod.{u, u} (blowUp I).toRingedSpace) 0).obj
        ((modulePullback (blowUpToBase I).toLRSHom.toShHom).obj F)
```

**`AlgebraicGeometry.isPerfect_modulePullback_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean#L698). The attribute's comment: “the ordinary pullback is perfect”.

> **Stacks 0ESS, perfectness.** The ordinary pullback of a perfect `𝒪_X`-module of Tor
> dimension at most one to a blowup is perfect.

```lean
theorem isPerfect_modulePullback_blowUpToBase (F : OXMod.{u, u} X.toRingedSpace)
    (hperfect : Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, u + 1}
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F))
    (htor : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F) (-1) 0) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, u + 1}
      ((DerivedCategory.singleFunctor (OXMod.{u, u} (blowUp I).toRingedSpace) 0).obj
        ((modulePullback (blowUpToBase I).toLRSHom.toShHom).obj F))
```

**`AlgebraicGeometry.hasTorAmplitude_modulePullback_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/PerfectPullback.lean#L714). The attribute's comment: “the ordinary pullback has Tor dimension at most one”.

> **Stacks 0ESS, Tor dimension.** The ordinary pullback to a blowup of an `𝒪_X`-module of Tor
> dimension at most one again has Tor dimension at most one.

```lean
theorem hasTorAmplitude_modulePullback_blowUpToBase (F : OXMod.{u, u} X.toRingedSpace)
    (htor : Stacks.Cohomology.TorAmplitude.HasTorAmplitude X.toRingedSpace
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F) (-1) 0) :
    Stacks.Cohomology.TorAmplitude.HasTorAmplitude (blowUp I).toRingedSpace
      ((DerivedCategory.singleFunctor (OXMod.{u, u} (blowUp I).toRingedSpace) 0).obj
        ((modulePullback (blowUpToBase I).toLRSHom.toShHom).obj F)) (-1) 0
```

## Tag 0EST, a lemma

[Tag 0EST](https://stacks.math.columbia.edu/tag/0EST) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_shortExact_strictTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingNormalForm.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingNormalForm.lean#L541).

> **Stacks Project, Tag 0EST.** Let `ℱ` be a perfect `𝒪_X`-module of Tor dimension at most
> one which is finite locally free of constant rank `r` on a scheme-theoretically dense open `U`.
> Then there is a `U`-admissible blowup `b : X' ⟶ X` and a short exact sequence
>
> `0 ⟶ 𝒦 ⟶ b^*ℱ ⟶ 𝒬 ⟶ 0`
>
> with `𝒬` finite locally free of rank `r` and `𝒦` finitely presented, perfect, of Tor dimension at
> most one, and zero over `U`.
>
> The witnesses are canonical: `X'` is the base change along the identity of `X` of the blowup of
> the `r`-th Fitting ideal of `ℱ`, `𝒬` is the strict transform of `ℱ` and `𝒦` is the kernel of the
> canonical surjection onto it. The finite presentation of `ℱ`, which the Fitting ideals need, is
> not assumed: it follows from perfectness
> (`AlgebraicGeometry.isFinitePresentation_of_isPerfect_single`).

```lean
theorem exists_isAdmissibleBlowup_shortExact_strictTransform
    (U : X.Opens) (hU : Scheme.Opens.IsSchemeTheoreticallyDense U)
    (hrank : SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback U.ι).obj F) r)
    (hperfect : IsPerfect.{u, u, u + 1}
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F))
    (htor : HasTorAmplitude X.toRingedSpace
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X.toRingedSpace) 0).obj F) (-1) 0) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X), Stacks.Blowup.IsAdmissibleBlowup U b ∧
      ∃ (K Q : X'.Modules) (i : K ⟶ (Scheme.Modules.pullback b).obj F)
        (p : (Scheme.Modules.pullback b).obj F ⟶ Q) (w : i ≫ p = 0),
        (ShortComplex.mk i p w).ShortExact ∧
          SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} Q r ∧
            K.IsFinitePresentation ∧
              IsPerfect.{u, u, u + 1}
                ((DerivedCategory.singleFunctor (OXMod.{u, u} X'.toRingedSpace) 0).obj K) ∧
                HasTorAmplitude X'.toRingedSpace
                  ((DerivedCategory.singleFunctor (OXMod.{u, u} X'.toRingedSpace) 0).obj K)
                  (-1) 0 ∧
                IsZero ((Scheme.Modules.pullback (b ⁻¹ᵁ U).ι).obj K)
```

## Tag 0ESU, a lemma

[Tag 0ESU](https://stacks.math.columbia.edu/tag/0ESU) in the Stacks Project.

**`AlgebraicGeometry.isAdmissibleBlowup_blowUpToBase_fittingIdealProd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProduct.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProduct.lean#L193). The attribute's comment: “the U-admissible blowup, in the product of the Fitting ideals up to N”.

> **Stacks Project, Tag 0ESU, the blowup.** For a finitely presented `𝒪_X`-module vanishing on
> an open `U`, the blowup of `X` in the product of the Fitting ideals of index at most `N` is a
> `U`-admissible blowup: that product is of finite type and supported away from `U`.

```lean
theorem isAdmissibleBlowup_blowUpToBase_fittingIdealProd [F.IsFinitePresentation] (U : X.Opens)
    (hrank : SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback U.ι).obj F) 0) (N : ℕ) :
    Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase (fittingIdealProd F N))
```

**`AlgebraicGeometry.isEffectiveCartierDivisor_fittingIdeal_pullback_fittingIdealProd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProduct.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProduct.lean#L226). The attribute's comment: “the Fitting ideals of index at most N become effective Cartier divisors”.

> **Stacks Project, Tag 0ESU, the effective Cartier divisors.** On the blowup of `X` in the
> product of the Fitting ideals of index at most `N`, the `k`-th Fitting ideal of the pulled back
> module is an effective Cartier divisor for every `k ≤ N`.
>
> The inverse image of the whole product is the exceptional divisor of the blowup, hence an
> effective Cartier divisor by tag 02OS, and each factor of it is one by tag 07ZV; the `k`-th
> Fitting ideal of the pullback is the inverse image of the `k`-th Fitting ideal by tag 0C3D.

```lean
theorem isEffectiveCartierDivisor_fittingIdeal_pullback_fittingIdealProd
    [F.IsFinitePresentation] (N : ℕ) {k : ℕ} (hk : k ≤ N) :
    Stacks.Divisors.IsEffectiveCartierDivisor
      (fittingIdeal ((Scheme.Modules.pullback (blowUpToBase (fittingIdealProd F N))).obj F)
        (k : ℤ))
```

**`AlgebraicGeometry.isAdmissibleBlowup_blowUpToBase_fittingIdealProdAll`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProductAll.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProductAll.lean#L272). The attribute's comment: “the U-admissible blowup, in the product of all the Fitting ideals”.

> For a finitely presented `𝒪_X`-module vanishing on an open `U`, the blowup of `X` in the
> product of **all** the Fitting ideals is a `U`-admissible blowup: that product is of finite type
> and supported away from `U`.

```lean
theorem isAdmissibleBlowup_blowUpToBase_fittingIdealProdAll [F.IsFinitePresentation]
    (U : X.Opens)
    (hrank : SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      ((Scheme.Modules.pullback U.ι).obj F) 0) :
    Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase (fittingIdealProdAll F))
```

**`AlgebraicGeometry.isEffectiveCartierDivisor_fittingIdeal_pullback_fittingIdealProdAll`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProductAll.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProductAll.lean#L321). The attribute's comment: “every Fitting ideal becomes an effective Cartier divisor on the blowup”.

> On the blowup of `X` in the product of all the Fitting ideals, the `k`-th Fitting ideal of
> the pulled back module is an effective Cartier divisor for **every** `k ≥ 0`.

```lean
theorem isEffectiveCartierDivisor_fittingIdeal_pullback_fittingIdealProdAll
    [F.IsFinitePresentation] (k : ℕ) :
    Stacks.Divisors.IsEffectiveCartierDivisor
      (fittingIdeal ((Scheme.Modules.pullback (blowUpToBase (fittingIdealProdAll F))).obj F)
        (k : ℤ))
```

**`AlgebraicGeometry.exists_isAdmissibleBlowup_isEffectiveCartierDivisor_fittingIdeal_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProductAll.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FittingProductAll.lean#L336). The attribute's comment: “the U-admissible blowup making every Fitting ideal effective Cartier, for ℱ|\_U = 0”.

> For a finitely presented `𝒪_X`-module `ℱ` with `ℱ|_U = 0` there is a `U`-admissible blowup
> `b : X' → X` on which every Fitting ideal of `b^*ℱ` is an effective Cartier divisor.

```lean
theorem exists_isAdmissibleBlowup_isEffectiveCartierDivisor_fittingIdeal_pullback
    [F.IsFinitePresentation] (U : X.Opens)
    (hzero : CategoryTheory.Limits.IsZero ((Scheme.Modules.pullback U.ι).obj F)) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X), Stacks.Blowup.IsAdmissibleBlowup U b ∧
      ∀ k : ℕ, Stacks.Divisors.IsEffectiveCartierDivisor
        (fittingIdeal ((Scheme.Modules.pullback b).obj F) (k : ℤ))
```

**`AlgebraicGeometry.exists_isAdmissibleBlowup_canonicalFiltrations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DivisorSum/CanonicalFiltrations.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DivisorSum/CanonicalFiltrations.lean#L94). The attribute's comment: “the blowup, the divisors, both canonical filtrations and every graded piece's rank”.

> **Stacks Project, Tag 0ESU.** Let `ℱ` be an `𝒪_X`-module of finite presentation vanishing on
> an open `U ⊆ X`. Then there is a `U`-admissible blowup `b : X' → X` and a locally finite family of
> effective Cartier divisors `D_j` on `X'` such that the pullback `b^*ℱ` has two locally finite
> filtrations
>
> ```
> 0 = F⁰ ⊆ F¹ ⊆ ⋯ ⊆ b^*ℱ        and        b^*ℱ = F₁ ⊇ F₂ ⊇ ⋯ ⊇ 0
> ```
>
> — the global subsheaves `AlgebraicGeometry.fittingIncr` and `AlgebraicGeometry.fittingDecr` of the
> family — whose graded pieces are, on the divisor `D i`, the direct images of modules finite locally
> free of rank `i + 1` there. Both filtrations are invariant under every automorphism of `b^*ℱ`, and
> around every point an affine open with local equations `e_1, …, e_N` for the divisors describes
> them as the multiples of `e_{i+1} ⋯ e_N` and the sections killed by `e_{i+1} ⋯ e_N`.
>
> Finite presentation is more general than the source's hypothesis that `ℱ` be perfect of Tor
> dimension at most one: a perfect module of Tor dimension at most one is of finite presentation,
> and the conclusion here is the source's for every module of finite presentation.
>
> In the indexing of this directory `D j` is the source's `D_{j+1}`, so the rank `i + 1` on `D i` is
> the source's rank `i` on `D_i`.

```lean
theorem exists_isAdmissibleBlowup_canonicalFiltrations [F.IsFinitePresentation] (U : X.Opens)
    (hzero : IsZero ((Scheme.Modules.pullback U.ι).obj F)) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X) (_ : Stacks.Blowup.IsAdmissibleBlowup U b)
      (_ : ((Scheme.Modules.pullback b).obj F).IsQuasicoherent)
      (D : ℕ → X'.IdealSheafData),
      (∀ j, IsEffectiveCartierDivisor (D j)) ∧
      IsLocallyFiniteFamily D ∧
      (∀ x : X', ∃ V : X'.Opens, x ∈ (V : Set X') ∧ ∃ m : ℕ, ∀ n ≥ m,
        Disjoint (V : Set X') ((D n).support : Set X')) ∧
      (∀ k : ℕ, fittingIdeal ((Scheme.Modules.pullback b).obj F) (k : ℤ) =
        locallyFiniteSum D fun j => (j + 1) - k) ∧
      Monotone (fittingIncr D ((Scheme.Modules.pullback b).obj F)) ∧
      Antitone (fittingDecr D ((Scheme.Modules.pullback b).obj F)) ∧
      fittingIncr D ((Scheme.Modules.pullback b).obj F) 0 = ⊥ ∧
      fittingDecr D ((Scheme.Modules.pullback b).obj F) 1 = ⊤ ∧
      (∀ x : X', ∃ V : X'.Opens, x ∈ (V : Set X') ∧ ∃ m : ℕ, ∀ n ≥ m,
        IsZero ((Scheme.Modules.pullback V.ι).obj (cokernel (C := X'.Modules)
          (fittingIncr D ((Scheme.Modules.pullback b).obj F) n).ι))) ∧
      (∀ x : X', ∃ V : X'.Opens, x ∈ (V : Set X') ∧ ∃ m : ℕ, ∀ n ≥ m,
        IsZero ((Scheme.Modules.pullback V.ι).obj
          (fittingDecr D ((Scheme.Modules.pullback b).obj F) n).asModules)) ∧
      (∀ (i : ℕ) (hle : fittingIncr D ((Scheme.Modules.pullback b).obj F) i ≤
          fittingIncr D ((Scheme.Modules.pullback b).obj F) (i + 1)),
        ∃ G : (D i).subscheme.Modules,
          SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} G (i + 1) ∧
          Nonempty (submoduleGraded hle ≅
            (Scheme.Modules.pushforward (D i).subschemeι).obj G)) ∧
      (∀ (i : ℕ) (hle : fittingDecr D ((Scheme.Modules.pullback b).obj F) (i + 2) ≤
          fittingDecr D ((Scheme.Modules.pullback b).obj F) (i + 1)),
        ∃ G : (D i).subscheme.Modules,
          SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} G (i + 1) ∧
          Nonempty (submoduleGraded hle ≅
            (Scheme.Modules.pushforward (D i).subschemeι).obj G)) ∧
      (∀ (e : (Scheme.Modules.pullback b).obj F ≅ (Scheme.Modules.pullback b).obj F) (i : ℕ),
        Scheme.Modules.rangeSubmodule
            ((fittingIncr D ((Scheme.Modules.pullback b).obj F) i).ιModules ≫ e.hom) =
          fittingIncr D ((Scheme.Modules.pullback b).obj F) i) ∧
      (∀ (e : (Scheme.Modules.pullback b).obj F ≅ (Scheme.Modules.pullback b).obj F) (i : ℕ),
        Scheme.Modules.rangeSubmodule
            ((fittingDecr D ((Scheme.Modules.pullback b).obj F) i).ιModules ≫ e.hom) =
          fittingDecr D ((Scheme.Modules.pullback b).obj F) i) ∧
      ∀ x : X', ∃ V : X'.affineOpens, x ∈ (V.1 : Set X') ∧
        ∃ (N : ℕ) (e : ℕ → Γ(X', V.1)),
          (∀ j, j + 1 ≤ N → (D j).ideal V = Ideal.span {e (j + 1)}) ∧
          (∀ j, N ≤ j → (D j).ideal V = ⊤) ∧
          (∀ j, e j ∈ nonZeroDivisors Γ(X', V.1)) ∧
          (∀ j, N < j → IsUnit (e j)) ∧
          (∀ k : ℕ, (fittingIdeal ((Scheme.Modules.pullback b).obj F) (k : ℤ)).ideal V =
            ∏ j ∈ Finset.Icc (k + 1) N, Ideal.span {e j} ^ (j - k)) ∧
          (∀ (i : ℕ) (s : Γ((Scheme.Modules.pullback b).obj F, V.1)),
            s ∈ (fittingIncr D ((Scheme.Modules.pullback b).obj F) i).toSubmodule.obj (op V.1) ↔
              ∃ t : Γ((Scheme.Modules.pullback b).obj F, V.1),
                (∏ j ∈ Finset.Icc (i + 1) N, e j) • t = s) ∧
          (∀ (i : ℕ) (s : Γ((Scheme.Modules.pullback b).obj F, V.1)),
            s ∈ (fittingDecr D ((Scheme.Modules.pullback b).obj F)
                (i + 1)).toSubmodule.obj (op V.1) ↔
              (∏ j ∈ Finset.Icc (i + 1) N, e j) • s = 0)
```

**`Stacks.Divisors.isEffectiveCartierDivisor_locallyFiniteSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DivisorSum/LocallyFinite.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DivisorSum/LocallyFinite.lean#L176). The attribute's comment: “the locally finite sum E\_k = D\_\{k+1} + 2D\_\{k+2} + ⋯ is effective Cartier”. References: EGA IV (21.2.7), “partial”.

> **The sum of a locally finite family of effective Cartier divisors is an effective Cartier
> divisor.**

```lean
theorem isEffectiveCartierDivisor_locallyFiniteSum {ι : Type*} {D : ι → X.IdealSheafData}
    (hD : IsLocallyFiniteFamily D) (hcart : ∀ i, IsEffectiveCartierDivisor (D i)) (n : ι → ℕ) :
    IsEffectiveCartierDivisor (locallyFiniteSum D n)
```

**`fittingIdeal_quotient_span_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean#L151). The attribute's comment: “the Fitting ideals of a presentation matrix divided by f”.

> **Stacks Project, Tag 0ESU**, the Fitting ideals of a scaled presentation.
> If `A = f • B` is an `n`-row presentation matrix of `𝓕` and `B` presents `𝓕'`, then
> `Fit_k(𝓕) = (f)^{n-k} Fit_k(𝓕')`.

```lean
theorem fittingIdeal_quotient_span_smul {n : ℕ} {J : Type*} (B : Matrix (Fin n) J R) (f : R)
    (k : ℕ) :
    fittingIdeal (M := (Fin n → R) ⧸ (f • B).columnSpan) (k : ℤ) =
      Ideal.span {f} ^ (n - k) * fittingIdeal (M := (Fin n → R) ⧸ B.columnSpan) (k : ℤ)
```

**`Stacks.ScaledPresentation.fittingIdeal_cokernel_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean#L406). The attribute's comment: “the Fitting ideals of a square presentation matrix divided by f”.

> **Stacks Project, Tag 0ESU**, the Fitting ideals of a square presentation matrix divided by
> `f`: if `𝓕` is presented by `f • B` and `𝓕'` by `B`, then `Fit_k(𝓕) = (f)^{n-k} Fit_k(𝓕')`.

```lean
theorem fittingIdeal_cokernel_smul (k : ℕ) :
    fittingIdeal (M := Cokernel (f • B)) (k : ℤ) =
      Ideal.span {f} ^ (n - k) * fittingIdeal (M := Cokernel B) (k : ℤ)
```

**`Stacks.ScaledPresentation.shortExact_ofFree_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean#L425). The attribute's comment: “the canonical sequence 0 → 𝒪\_\{D\_n}^\{⊕n} → ℱ → ℱ' → 0 of a local presentation”.

> **Stacks Project, Tag 0ESU**, the first canonical short exact sequence of a local
> presentation. For `A = f • B` with `B` injective, writing `𝓕 = Rⁿ / A Rⁿ` and `𝓕' = Rⁿ / B Rⁿ`,
> the sequence
> ```
> 0 → (R ⧸ (f))ⁿ → 𝓕 → 𝓕' → 0
> ```
> is exact, and when `f` is a nonzerodivisor its submodule is `Ker(f : 𝓕 → 𝓕)`, which is what makes
> the sequence canonical. Here `R ⧸ (f)` is the structure sheaf of the effective Cartier divisor
> cut out by `f`.

```lean
theorem shortExact_ofFree_toBase (hf : f ∈ nonZeroDivisors R)
    (hB : Function.Injective B.mulVecLin) :
    Function.Injective (ofFree B f) ∧
      LinearMap.range (ofFree B f) = LinearMap.ker (toBase B f) ∧
      Function.Surjective (toBase B f) ∧
      LinearMap.range (ofFree B f) = LinearMap.ker (LinearMap.lsmul R (Cokernel (f • B)) f)
```

**`Stacks.ScaledPresentation.shortExact_ofBase_toFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean#L443). The attribute's comment: “the canonical sequence 0 → ℱ' → ℱ → 𝒪\_\{D\_n}^\{⊕n} → 0 of a local presentation”.

> **Stacks Project, Tag 0ESU**, the second canonical short exact sequence of a local
> presentation. For `A = f • B` with `f` a nonzerodivisor, writing `𝓕 = Rⁿ / A Rⁿ` and
> `𝓕' = Rⁿ / B Rⁿ`, the sequence
> ```
> 0 → 𝓕' → 𝓕 → (R ⧸ (f))ⁿ → 0
> ```
> is exact, and its submodule is the image of multiplication by `f` on `𝓕`, so that its quotient
> is `Coker(f : 𝓕 → 𝓕)`; this is what makes the sequence canonical.

```lean
theorem shortExact_ofBase_toFree (hf : f ∈ nonZeroDivisors R) :
    Function.Injective (ofBase B f) ∧
      LinearMap.range (ofBase B f) = LinearMap.ker (toFree B f) ∧
      Function.Surjective (toFree B f) ∧
      LinearMap.range (ofBase B f) = LinearMap.range (LinearMap.lsmul R (Cokernel (f • B)) f)
```

**`Stacks.ScaledPresentation.exists_eq_smul_and_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean#L496). The attribute's comment: “the local step: a principal Fit\_\{n-1} gives A = f A' and the two sequences”.

> **Stacks Project, Tag 0ESU**, the local step of the induction. Let `𝓕 = R^{n} / A R^{n}` be
> presented by a square matrix `A` with `n = m + 1` rows, with `A` injective, and suppose
> `Fit_{n-1}(𝓕)` is generated by a nonzerodivisor `f`. Then `A = f A'` for a square matrix `A'`
> which is again injective, so that `𝓕' = R^{n} / A' R^{n}` is presented by an exact sequence of
> the same shape, and `𝓕` sits in the two canonical short exact sequences
> ```
> 0 → (R ⧸ (f))ⁿ → 𝓕 → 𝓕' → 0    and    0 → 𝓕' → 𝓕 → (R ⧸ (f))ⁿ → 0
> ```
> whose free term is the structure sheaf of the divisor cut out by `f` — the divisor `D_n` of the
> source — and whose submodule and quotient are `Ker(f : 𝓕 → 𝓕)` and `Coker(f : 𝓕 → 𝓕)`.

```lean
theorem exists_eq_smul_and_shortExact {m : ℕ}
    (A : Matrix (Fin (m + 1)) (Fin (m + 1)) R) (hf : f ∈ nonZeroDivisors R)
    (hA : Function.Injective A.mulVecLin)
    (hfit : fittingIdeal (M := Cokernel A) (m : ℤ) = Ideal.span {f}) :
    ∃ A' : Matrix (Fin (m + 1)) (Fin (m + 1)) R, A = f • A' ∧
      Function.Injective A'.mulVecLin ∧
      (Function.Injective (ofFree A' f) ∧
        LinearMap.range (ofFree A' f) = LinearMap.ker (toBase A' f) ∧
        Function.Surjective (toBase A' f) ∧
        LinearMap.range (ofFree A' f) =
          LinearMap.ker (LinearMap.lsmul R (Cokernel (f • A')) f)) ∧
      (Function.Injective (ofBase A' f) ∧
        LinearMap.range (ofBase A' f) = LinearMap.ker (toFree A' f) ∧
        Function.Surjective (toFree A' f) ∧
        LinearMap.range (ofBase A' f) =
          LinearMap.range (LinearMap.lsmul R (Cokernel (f • A')) f))
```

**`Stacks.ScaledPresentation.fittingIdeal_cokernel_eq_top_of_fittingIdeal_smul_eq_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/ScaledPresentation.lean#L541). The attribute's comment: “the entries of A' generate the unit ideal”.

> **Stacks Project, Tag 0ESU**: the entries of `A'` generate the unit ideal. If `𝓕` is presented
> by `A = f A'` with `A'` square of size `n = m + 1` and `Fit_{n-1}(𝓕)` is generated by the
> nonzerodivisor `f`, then `Fit_{n-1}(𝓕') = R` for `𝓕' = R^{n} / A' R^{n}`: the scaling identity
> gives `(f) = (f) · Fit_{n-1}(𝓕')`, and `f` cancels. Since `Fit_{n-1}(𝓕')` is the ideal of
> `1 × 1` minors of `A'`, this says the entries of `A'` generate the unit ideal, which is the
> hypothesis under which the source invokes Algebra, Lemma 10.102.2 (tag 00MT) to drop the number
> of generators by one.

```lean
theorem fittingIdeal_cokernel_eq_top_of_fittingIdeal_smul_eq_span_singleton {m : ℕ}
    (A' : Matrix (Fin (m + 1)) (Fin (m + 1)) R) (hf : f ∈ nonZeroDivisors R)
    (hfit : fittingIdeal (M := Cokernel (f • A')) (m : ℤ) = Ideal.span {f}) :
    fittingIdeal (R := R) (M := Cokernel A') (m : ℤ) = ⊤
```

**`Stacks.ScaledPresentation.exists_cokernel_equiv_of_isUnit_entry`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/UnitEntryDescent.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/UnitEntryDescent.lean#L225). The attribute's comment: “dropping a generator: a unit relation entry gives a smaller presentation”.

> If some entry of a square matrix `A` of size `n = m + 1` is a unit, then the module `Rⁿ / A Rⁿ`
> presented by `A` is the module presented by a square matrix of size `m`, which is again injective
> if `A` is.

```lean
theorem exists_cokernel_equiv_of_isUnit_entry {m : ℕ}
    (A : Matrix (Fin (m + 1)) (Fin (m + 1)) R) (a b : Fin (m + 1)) (hu : IsUnit (A a b)) :
    ∃ ψ : Matrix (Fin m) (Fin m) R,
      Nonempty (Cokernel A ≃ₗ[R] Cokernel ψ) ∧
        (Function.Injective A.mulVecLin → Function.Injective ψ.mulVecLin)
```

**`Stacks.ScaledPresentation.exists_cover_cokernel_equiv_of_fittingIdeal_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/UnitEntryDescent.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Fitting/UnitEntryDescent.lean#L281). The attribute's comment: “the Zariski cover on which ℱ' needs only n-1 generators”.

> Let `𝓕` be presented by a square matrix `A` of size `n = m + 1` with `Fit_{n-1}(𝓕) = R`. Then
> the entries of `A` generate the unit ideal — so the basic opens `D(A i j)` cover `Spec R` — and
> over each of those basic opens the module presented by `A` is the cokernel of a square matrix of
> size `m`, and hence is generated by `m = n - 1` elements.

```lean
theorem exists_cover_cokernel_equiv_of_fittingIdeal_eq_top {m : ℕ}
    (A : Matrix (Fin (m + 1)) (Fin (m + 1)) R)
    (hfit : fittingIdeal (R := R) (M := Cokernel A) (m : ℤ) = ⊤) :
    Ideal.span (Set.range fun p : Fin (m + 1) × Fin (m + 1) => A p.1 p.2) = ⊤ ∧
      ∀ p : Fin (m + 1) × Fin (m + 1),
        ∃ ψ : Matrix (Fin m) (Fin m) (Localization.Away (A p.1 p.2)),
          Nonempty (Cokernel (A.map (algebraMap R (Localization.Away (A p.1 p.2)))) ≃ₗ[
              Localization.Away (A p.1 p.2)] Cokernel ψ) ∧
            ∃ s : Fin m → Cokernel (A.map (algebraMap R (Localization.Away (A p.1 p.2)))),
              Submodule.span (Localization.Away (A p.1 p.2)) (Set.range s) = ⊤
```

## Tag 0ESV, a lemma

[Tag 0ESV](https://stacks.math.columbia.edu/tag/0ESV) in the Stacks Project.

**`AlgebraicGeometry.exists_admissibleBlowup_isPerfectTorLEOne_ker_im_coker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/PerfectHomomorphismFittingBlowup.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/PerfectHomomorphismFittingBlowup.lean#L164). The attribute's comment: “the U-admissible blowup after which the kernel, image and cokernel of the pullback of φ are perfect of Tor dimension ≤ 1”.

> **Stacks Project, Tag 0ESV.** Let `X` be a scheme and `φ : ℱ ⟶ 𝒢` a homomorphism of perfect
> `𝒪_X`-modules of Tor dimension at most one. Let `U ⊆ X` be a scheme-theoretically dense open with
> `ℱ|_U = 0` and `𝒢|_U = 0`. Then there is a `U`-admissible blowup `b : X' ⟶ X` such that the
> kernel, the image and the cokernel of `b^*φ` are perfect `𝒪_{X'}`-modules of Tor dimension at
> most one.
>
> The blowup is the blowup of `X` in the zeroth Fitting ideal of `Coker(φ)`. That cokernel is
> finitely presented: it is the `H^0` of the cone `E` of `φ[0]` — the source's object `(ℱ ⟶ 𝒢)` of
> `D(𝒪_X)`, which is perfect by tag 08CR and hence pseudo-coherent — and `E` has no cohomology in
> positive degrees, so tag 08DN (2) applies. It vanishes over `U` because `ℱ` and `𝒢` do and
> pullback is right exact, hence is finite locally free of rank `0` there. Tag 0ESN (1) therefore
> makes the blowup `U`-admissible and tag 0ESN (4) makes `b^*Coker(φ)` perfect of Tor dimension at
> most one; right exactness of pullback identifies that module with the cokernel of `b^*φ`. The
> pullbacks `b^*ℱ` and `b^*𝒢` are perfect of Tor dimension at most one by tag 0ESS, after which the
> image — the source's "kernel of the cokernel" — and then the kernel are
> `AlgebraicGeometry.isPerfectTorLEOne_abelianImage_of_cokernel` and
> `AlgebraicGeometry.isPerfectTorLEOne_kernel`.

```lean
theorem exists_admissibleBlowup_isPerfectTorLEOne_ker_im_coker {X : Scheme.{u}}
    (F G : OXMod.{u, u} X.toRingedSpace) (φ : F ⟶ G)
    (hF : IsPerfectTorLEOne X F) (hG : IsPerfectTorLEOne X G)
    (U : X.Opens) (hU : Scheme.Opens.IsSchemeTheoreticallyDense U)
    (_hFU : IsZero ((modulePullback U.ι.toLRSHom.toShHom).obj F))
    (hGU : IsZero ((modulePullback U.ι.toLRSHom.toShHom).obj G)) :
    ∃ (X' : Scheme.{u}) (b : X' ⟶ X), Stacks.Blowup.IsAdmissibleBlowup U b ∧
      IsPerfectTorLEOne X' (kernel ((modulePullback b.toLRSHom.toShHom).map φ)) ∧
      IsPerfectTorLEOne X' (Abelian.image ((modulePullback b.toLRSHom.toShHom).map φ)) ∧
      IsPerfectTorLEOne X' (cokernel ((modulePullback b.toLRSHom.toShHom).map φ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.41, Tag 0F8K](https://stacks.math.columbia.edu/tag/0F8K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
