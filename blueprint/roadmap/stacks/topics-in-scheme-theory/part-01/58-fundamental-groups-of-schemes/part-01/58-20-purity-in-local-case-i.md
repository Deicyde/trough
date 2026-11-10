---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_iso_spec_sections_punctured_spectrum, AlgebraicGeometry.exists_finiteEtale_extension_iff_globalSections_finiteEtale, AlgebraicGeometry.NormalPurity.globalSections_isEquivalence_normalFiniteEtaleAwayAlgebra, AlgebraicGeometry.NormalPurity.exists_finiteEtale_extension_iff_globalSections_finiteEtale, AlgebraicGeometry.exists_finiteEtale_extension_iff_completion, AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_dualizingComplex, AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_localCohomology_annihilated, AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_three_le_depth_self
statement: formalized
proof: formalized
---

# 58.20 Purity in local case, I

Section 58.20 of the Stacks Project, [Tag 0BM7](https://stacks.math.columbia.edu/tag/0BM7). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BM8, a lemma

[Tag 0BM8](https://stacks.math.columbia.edu/tag/0BM8) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_spec_sections_punctured_spectrum`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/Basic.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/Basic.lean#L134).

> **Stacks Project, Tag 0BM8.** A scheme finite over the spectrum of a Noetherian local ring,
> whose local rings at closed points all have depth at least two, is canonically the spectrum of
> its sections over the inverse image of the punctured spectrum.

```lean
lemma exists_iso_spec_sections_punctured_spectrum
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {Y : Scheme.{u}} (π : Y ⟶ Spec (.of A)) [IsFinite π]
    (hdepth : ∀ y : Y, IsClosed ({y} : Set Y) →
      2 ≤ Module.depth (Y.presheaf.stalk y)
        (IsLocalRing.maximalIdeal (Y.presheaf.stalk y)) (Y.presheaf.stalk y)) :
    let U : (Spec (.of A)).Opens :=
      ⟨({IsLocalRing.closedPoint A} : Set (PrimeSpectrum A))ᶜ,
        IsLocalRing.isClosed_singleton_closedPoint A |>.isOpen_compl⟩
    let V : Y.Opens := π ⁻¹ᵁ U
    ∃ e : Y ≅ Spec Γ(Y, V),
      e.hom ≫ Spec.map (Y.presheaf.map (homOfLE le_top).op) = Y.toSpecΓ
```

## Tag 0BLK, a lemma

[Tag 0BLK](https://stacks.math.columbia.edu/tag/0BLK) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_extension_iff_globalSections_finiteEtale`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/GlobalSectionsCriterion.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/GlobalSectionsCriterion.lean#L274).

> **Stacks Project, Tag 0BLK.** For a Noetherian local ring of depth at least two, a finite
> étale scheme over the punctured spectrum extends to a finite étale scheme over the whole
> spectrum if and only if its ring of global sections is finite étale over the ring.

```lean
lemma exists_finiteEtale_extension_iff_globalSections_finiteEtale
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (V : Scheme.{u}) (π : V ⟶ (Stacks.Divisors.puncturedSpectrum A).toScheme)
    [IsFinite π] [Etale π]
    (hdepth : 2 ≤ Module.depth A (IsLocalRing.maximalIdeal A) A) :
    (∃ (Y : Scheme.{u}) (f : Y ⟶ Spec (.of A)) (g : V ⟶ Y),
      IsFinite f ∧ Etale f ∧ IsPullback π g (Stacks.Divisors.puncturedSpectrum A).ι f) ↔
      letI : Algebra A Γ(V, ⊤) :=
        ((Scheme.ΓSpecIso (.of A)).inv ≫
          (π ≫ (Stacks.Divisors.puncturedSpectrum A).ι).appTop).hom.toAlgebra
      Module.Finite A Γ(V, ⊤) ∧ Algebra.Etale A Γ(V, ⊤)
```

## Tag 0BM9, a lemma

[Tag 0BM9](https://stacks.math.columbia.edu/tag/0BM9) in the Stacks Project.

**`AlgebraicGeometry.NormalPurity.globalSections_isEquivalence_normalFiniteEtaleAwayAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NormalEquivalence.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NormalEquivalence.lean#L992). The attribute's comment: “the equivalence”.

> **Stacks Project, Tag 0BM9.** On a Noetherian normal local ring of dimension at least two,
> global sections give an equivalence from the opposite of the category of finite étale covers of
> the punctured spectrum to finite normal torsion-free algebras which are étale there.

```lean
public theorem globalSections_isEquivalence_normalFiniteEtaleAwayAlgebra
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (hnormal : IsNormalRing A) (hdim : (2 : WithBot ℕ∞) ≤ ringKrullDim A) :
    ∃ F : Functor
        (FiniteEtaleOver (Stacks.Divisors.puncturedSpectrum A).toScheme)ᵒᵖ
        (NormalFiniteEtaleAwayAlgebra A),
      F.IsEquivalence ∧ Nonempty
        (F ⋙ ObjectProperty.ι _ ≅ globalSections A)
```

**`AlgebraicGeometry.NormalPurity.exists_finiteEtale_extension_iff_globalSections_finiteEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NormalEquivalence.lean, line 1019](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NormalEquivalence.lean#L1019). The attribute's comment: “the extension criterion”.

> **Stacks Project, Tag 0BM9.** A finite étale cover of the punctured spectrum extends to a
> finite étale cover of the whole spectrum exactly when its ring of global sections is finite
> étale over the base ring.

```lean
public theorem exists_finiteEtale_extension_iff_globalSections_finiteEtale
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (hnormal : IsNormalRing A) (hdim : (2 : WithBot ℕ∞) ≤ ringKrullDim A)
    (V : Scheme.{u}) (π : V ⟶ (Stacks.Divisors.puncturedSpectrum A).toScheme)
    [IsFinite π] [Etale π] :
    (∃ (Y : Scheme.{u}) (f : Y ⟶ Spec (.of A)) (g : V ⟶ Y),
      IsFinite f ∧ Etale f ∧ IsPullback π g (Stacks.Divisors.puncturedSpectrum A).ι f) ↔
      letI : Algebra A Γ(V, ⊤) :=
        ((Scheme.ΓSpecIso (.of A)).inv ≫
          (π ≫ (Stacks.Divisors.puncturedSpectrum A).ι).appTop).hom.toAlgebra
      Module.Finite A Γ(V, ⊤) ∧ Algebra.Etale A Γ(V, ⊤)
```

## Tag 0BLL, a lemma

[Tag 0BLL](https://stacks.math.columbia.edu/tag/0BLL) in the Stacks Project.

**`AlgebraicGeometry.exists_finiteEtale_extension_iff_completion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompletionCriterion.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompletionCriterion.lean#L50).

> **Stacks Project, Tag 0BLL.** A finite étale cover of the punctured spectrum of a
> Noetherian local ring extends over the spectrum exactly when its base change to the adic
> completion extends over the completed spectrum.

```lean
lemma exists_finiteEtale_extension_iff_completion
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (V : Scheme.{u}) (pi : V ⟶ (Stacks.Divisors.puncturedSpectrum A).toScheme)
    [IsFinite pi] [Etale pi] :
    let Ahat := AdicCompletion (maximalIdeal A) A
    let Xhat := Spec (.of Ahat)
    let completionMap : Xhat ⟶ Spec (.of A) :=
      Spec.map (CommRingCat.ofHom (algebraMap A Ahat))
    let Uhat := pullback (Stacks.Divisors.puncturedSpectrum A).ι completionMap
    let UhatToU : Uhat ⟶ (Stacks.Divisors.puncturedSpectrum A).toScheme :=
      pullback.fst _ _
    let Vhat := pullback pi UhatToU
    let pihat : Vhat ⟶ Uhat := pullback.snd _ _
    (∃ (Y : Scheme.{u}) (f : Y ⟶ Spec (.of A)) (g : V ⟶ Y),
      IsFinite f ∧ Etale f ∧
        IsPullback pi g (Stacks.Divisors.puncturedSpectrum A).ι f) ↔
      ∃ (Yhat : Scheme.{u}) (fhat : Yhat ⟶ Xhat) (ghat : Vhat ⟶ Yhat),
        IsFinite fhat ∧ Etale fhat ∧
          IsPullback pihat ghat (pullback.snd (Stacks.Divisors.puncturedSpectrum A).ι completionMap)
            fhat
```

## Tag 0EK6, a lemma

[Tag 0EK6](https://stacks.math.columbia.edu/tag/0EK6) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_dualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/ExtensionFromHypersurface.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/ExtensionFromHypersurface.lean#L243).

> **[Stacks, Tag 0EK6].** In the local Lefschetz situation (Tag 0BLF) let `V` be finite étale
> over `U`. Assume
>
> * (a) `A` has a dualizing complex,
> * (b) the pair `(A, (f))` is henselian,
> * (c) one of the following is true:
>   (i) `A_f` is `(S₂)` and every irreducible component of `X` not contained in `X₀` has dimension
>   `≥ 3`, or (ii) `depth(A_𝔭) + dim(A/𝔭) > 2` for every prime `𝔭 ⊂ A` with `f ∉ 𝔭`,
> * (d) `V₀ = V ×_U U₀` is equal to `Y₀ ×_{X₀} U₀` for some `Y₀ → X₀` finite étale.
>
> Then `V = Y ×_X U` for some `Y → X` finite étale.
>
> Spelling. Hypothesis (a) is `hdual`, (b) is `hS` and (c) is the disjunction `hc`. "`A` has a
> dualizing complex" is `∃ ω, Dualizing.IsDualizingComplex ω`, the predicate of [Stacks, Tag 0A7B]
> on the derived category of `A`-modules. `(S₂)` for `A_f` is
> `PropertySkRing (Localization.Away S.f) 2`, Serre's condition of [Stacks, Tag 031P]. The
> irreducible components of `X = Spec A` are the `V(𝔮)` for `𝔮` a minimal prime of `A`; `V(𝔮)` is
> contained in `X₀ = V(f)` exactly when `f ∈ 𝔮`, and its dimension is `dim(A/𝔮)`; so the second
> half of (c)(i) is the quantification over minimal primes `𝔮` with `f ∉ 𝔮`. In (c)(ii)
> `depth(A_𝔭)` is the depth of the `A_𝔭`-module `A_𝔭` along its maximal ideal and the sum is formed
> in `ℤ ∪ {±∞}`. Hypothesis (d) and the conclusion record "`V₀ = Y₀ ×_{X₀} U₀`" and
> "`V = Y ×_X U`" as cartesian squares (`CategoryTheory.IsPullback`), `V ×_U U₀` being the chosen
> pullback.
>
> The proof is the source's. Branch (c)(i) implies branch (c)(ii) for a ring with a dualizing
> complex (`two_lt_depth_add_ringKrullDim_of_propertySkRing_away`, through the universal
> catenarity of Stacks 0A80), and under (c)(ii) the statement is
> `exists_finiteEtale_extension_of_depth_add_dim`: Stacks 0BLL reduces to the complete case,
> where Stacks 09ZL/09ZS lifts `Y₀` (the pair being henselian by Stacks 0ALJ) and Stacks 0EK5
> descends the isomorphism over `U₀` to one over `U`.

```lean
public theorem exists_finiteEtale_extension_of_dualizingComplex
    (S : LocalLefschetzSituation.{u})
    (hdual : ∃ omega : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex omega)
    (hS : HenselianPair S.A S.principalIdeal)
    (hc : (PropertySkRing (Localization.Away S.f) 2 ∧
        ∀ q : Ideal S.A, q ∈ minimalPrimes S.A → S.f ∉ q →
          (3 : WithBot ℕ∞) ≤ ringKrullDim (S.A ⧸ q)) ∨
      ∀ p : PrimeSpectrum S.A, S.f ∉ p.asIdeal →
        enatToEInt
            (Module.depth (Localization.AtPrime p.asIdeal)
              (maximalIdeal (Localization.AtPrime p.asIdeal))
              (LocalizedModule p.asIdeal.primeCompl S.A)) +
          krullDimToEInt (ringKrullDim (S.A ⧸ p.asIdeal)) > ((2 : ℤ) : EInt))
    (V : Scheme.{u}) (pi : V ⟶ S.U) [IsFinite pi] [Etale pi]
    (Y₀ : Scheme.{u}) (f₀ : Y₀ ⟶ S.X₀) [IsFinite f₀] [Etale f₀]
    (g₀ : pullback pi S.U₀ToU ⟶ Y₀)
    (h₀ : IsPullback (pullback.snd pi S.U₀ToU) g₀ S.U₀Open.ι f₀) :
    ∃ (Y : Scheme.{u}) (p : Y ⟶ S.X) (g : V ⟶ Y),
      IsFinite p ∧ Etale p ∧ IsPullback pi g S.UOpen.ι p
```

## Tag 0BLS, a lemma

[Tag 0BLS](https://stacks.math.columbia.edu/tag/0BLS) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_localCohomology_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/ExtensionFromHypersurface.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/ExtensionFromHypersurface.lean#L288).

> **[Stacks, Tag 0BLS].** In the local Lefschetz situation let `V` be finite étale over `U` and
> assume (1) `H¹_𝔪(A)` and `H²_𝔪(A)` are annihilated by a power of `f`, and (2) `V ×_U U₀` is
> `Y₀ ×_{X₀} U₀` for some `Y₀ → X₀` finite étale. Then `V = Y ×_X U` for some `Y → X` finite étale.
>
> The proof is the source's. Stacks 0BLL reduces the existence of the extension to the case of an
> `f`-adically complete base, which is
> `…LocalLefschetzSituation.exists_finiteEtale_extension_of_isAdicCompleteCase`, and the annihilation
> hypothesis is inherited by the `𝔪`-adic completion through Stacks 0ALZ, which is
> `…LocalLefschetzSituation.annihilated_completion`. In the complete case `(A, fA)` is a henselian
> pair by Stacks 0ALJ (`IsAdicComplete.henselianRing` and `henselianPair_of_henselianRing`); that
> henselian pair feeds Stacks 09ZS, lifting `Y₀` to a finite étale `Y → X`, and is also hypothesis
> (2) of Stacks 0BM6, which supplies the full faithfulness of restriction that the descent step
> needs, as `fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian`.

```lean
public theorem exists_finiteEtale_extension_of_localCohomology_annihilated
    (S : LocalLefschetzSituation.{u})
    (h1 : ∃ n, ∀ x : localCohomologyModule S.A (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing (maximalIdeal S.A)) (ModuleCat.of S.A S.A) 1,
      S.f ^ n • x = 0)
    (h2 : ∃ n, ∀ x : localCohomologyModule S.A (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing (maximalIdeal S.A)) (ModuleCat.of S.A S.A) 2,
      S.f ^ n • x = 0)
    (V : Scheme.{u}) (pi : V ⟶ S.U) [IsFinite pi] [Etale pi]
    (Y₀ : Scheme.{u}) (f₀ : Y₀ ⟶ S.X₀) [IsFinite f₀] [Etale f₀]
    (g₀ : pullback pi S.U₀ToU ⟶ Y₀)
    (h₀ : IsPullback (pullback.snd pi S.U₀ToU) g₀ S.U₀Open.ι f₀) :
    ∃ (Y : Scheme.{u}) (p : Y ⟶ S.X) (g : V ⟶ Y),
      IsFinite p ∧ Etale p ∧ IsPullback pi g S.UOpen.ι p
```

## Tag 0BLM, a lemma

[Tag 0BLM](https://stacks.math.columbia.edu/tag/0BLM) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_three_le_depth_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/ExtensionFromHypersurface.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/ExtensionFromHypersurface.lean#L317).

> **[Stacks, Tag 0BLM].** In the local Lefschetz situation let `V` be finite étale over `U` and
> assume (1) `A` has depth at least `3`, and (2) `V ×_U U₀` is `Y₀ ×_{X₀} U₀` for some `Y₀ → X₀`
> finite étale. Then `V = Y ×_X U` for some `Y → X` finite étale.
>
> This is the source's proof. Depth at least `3` forces `H¹_𝔪(A) = H²_𝔪(A) = 0` by
> [Stacks, Tag 0AVZ] (`Stacks.LocalCohomology.subsingleton_localCohomologyModule_of_lt_depth`), so
> both are annihilated by `f ^ 0`, and the conclusion is [Stacks, Tag 0BLS] at `S`, which is
> `exists_finiteEtale_extension_of_localCohomology_annihilated`.

```lean
public theorem exists_finiteEtale_extension_of_three_le_depth_self
    (S : LocalLefschetzSituation.{u})
    (hdepth : 3 ≤ Module.depth S.A (maximalIdeal S.A) S.A)
    (V : Scheme.{u}) (pi : V ⟶ S.U) [IsFinite pi] [Etale pi]
    (Y₀ : Scheme.{u}) (f₀ : Y₀ ⟶ S.X₀) [IsFinite f₀] [Etale f₀]
    (g₀ : pullback pi S.U₀ToU ⟶ Y₀)
    (h₀ : IsPullback (pullback.snd pi S.U₀ToU) g₀ S.U₀Open.ι f₀) :
    ∃ (Y : Scheme.{u}) (p : Y ⟶ S.X) (g : V ⟶ Y),
      IsFinite p ∧ Etale p ∧ IsPullback pi g S.UOpen.ι p
```

**`AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_three_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LiftFromDepthThree.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LiftFromDepthThree.lean#L178). The attribute's comment: “the unrestricted Stacks 0BLS is carried as a named general hypothesis”.

> **[Stacks, Tag 0BLM]** In the local Lefschetz situation let `V` be finite étale over `U` and
> assume (1) `A` has depth at least `3`, and (2) `V ×_U U₀` is `Y₀ ×_{X₀} U₀` for some
> `Y₀ → X₀` finite étale.  Then `V = Y ×_X U` for some `Y → X` finite étale.
>
> This is the source's proof.  Depth at least `3` forces `H¹_𝔪(A) = H²_𝔪(A) = 0` by
> [Stacks, Tag 0AVZ], which is the whole content supplied here, and the conclusion is then
> [Stacks, Tag 0BLS] at the situation `S`.
>
> That last step is the hypothesis `hLiftFromHypersurface`, stated in the unrestricted form the
> source gives [Stacks, Tag 0BLS], universally quantified over all local Lefschetz situations, with
> its own annihilation hypothesis intact — it is not specialised to `S`, says nothing about depth,
> and does not grant this statement's conclusion.  It holds by
> `exists_finiteEtale_extension_of_localCohomology_annihilated`.  The `f`-adically complete case is
> `exists_finiteEtale_extension_of_three_le_depth_of_isAdicComplete` above, where it is
> discharged.

```lean
public theorem exists_finiteEtale_extension_of_three_le_depth
    (S : LocalLefschetzSituation.{u})
    (hdepth : 3 ≤ Module.depth S.A (maximalIdeal S.A) S.A)
    (hLiftFromHypersurface : ∀ T : LocalLefschetzSituation.{u},
      (∃ n : ℕ, ∀ x : localCohomologyModule T.A (maximalIdeal T.A)
        (Ideal.fg_of_isNoetherianRing (maximalIdeal T.A)) (ModuleCat.of T.A T.A) 1,
        T.f ^ n • x = 0) →
      (∃ n : ℕ, ∀ x : localCohomologyModule T.A (maximalIdeal T.A)
        (Ideal.fg_of_isNoetherianRing (maximalIdeal T.A)) (ModuleCat.of T.A T.A) 2,
        T.f ^ n • x = 0) →
      ∀ (W : Scheme.{u}) (ρ : W ⟶ T.U), IsFinite ρ → Etale ρ →
      ∀ (Z₀ : Scheme.{u}) (q₀ : Z₀ ⟶ T.X₀), IsFinite q₀ → Etale q₀ →
      ∀ e₀ : pullback ρ T.U₀ToU ⟶ Z₀,
        IsPullback (pullback.snd ρ T.U₀ToU) e₀ T.U₀Open.ι q₀ →
        ∃ (Z : Scheme.{u}) (q : Z ⟶ T.X) (e : W ⟶ Z),
          IsFinite q ∧ Etale q ∧ IsPullback ρ e T.UOpen.ι q)
    (V : Scheme.{u}) (pi : V ⟶ S.U) [IsFinite pi] [Etale pi]
    (Y₀ : Scheme.{u}) (f₀ : Y₀ ⟶ S.X₀) [IsFinite f₀] [Etale f₀]
    (g₀ : pullback pi S.U₀ToU ⟶ Y₀)
    (h₀ : IsPullback (pullback.snd pi S.U₀ToU) g₀ S.U₀Open.ι f₀) :
    ∃ (Y : Scheme.{u}) (p : Y ⟶ S.X) (g : V ⟶ Y),
      IsFinite p ∧ Etale p ∧ IsPullback pi g S.UOpen.ι p
```

**`AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_lift_of_three_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LiftFromDepthThreeCompletion.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LiftFromDepthThreeCompletion.lean#L65).

> **[Stacks, Tag 0BLM]** In the local Lefschetz situation let `V` be finite étale over `U`
> and assume (1) `A` has depth at least `3`, and (2) `V ×_U U₀` is `Y₀ ×_{X₀} U₀` for some
> `Y₀ → X₀` finite étale. Then `V = Y ×_X U` for some `Y → X` finite étale.
>
> The reduction to the complete case is by Tag 0BLL, as in the source's proof of Tag 0BLS
> (`AlgebraicGeometry.LocalLefschetzSituation.exists_finiteEtale_extension_of_isAdicCompleteCase`):
> the completion `Â` has the same depth (Tag 07NW) and is `f`-adically complete, and the base change
> of `Y₀` to `Spec (Â / fÂ)` witnesses hypothesis (2) for the base change of `V`.

```lean
theorem exists_finiteEtale_lift_of_three_le_depth
    (hdepth : 3 ≤ Module.depth S.A (maximalIdeal S.A) S.A)
    (V : Scheme.{u}) (pi : V ⟶ S.U) [IsFinite pi] [Etale pi]
    (Y₀ : Scheme.{u}) (f₀ : Y₀ ⟶ S.X₀) [IsFinite f₀] [Etale f₀]
    (g₀ : pullback pi S.U₀ToU ⟶ Y₀)
    (h₀ : IsPullback (pullback.snd pi S.U₀ToU) g₀ S.U₀Open.ι f₀) :
    ∃ (Y : Scheme.{u}) (p : Y ⟶ S.X) (g : V ⟶ Y),
      IsFinite p ∧ Etale p ∧ IsPullback pi g S.UOpen.ι p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.20, Tag 0BM7](https://stacks.math.columbia.edu/tag/0BM7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
