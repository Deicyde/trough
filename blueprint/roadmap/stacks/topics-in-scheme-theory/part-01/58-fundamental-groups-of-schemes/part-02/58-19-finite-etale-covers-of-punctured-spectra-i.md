---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.LocalLefschetzSituation, AlgebraicGeometry.LocalLefschetzSituation, Stacks.Divisors.puncturedSpectrum, Stacks.puncturedSpectrum, AlgebraicGeometry.LocalLefschetzSituation.faithful_finiteEtaleRestriction, AlgebraicGeometry.exists_finite_extension_of_completion, AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_completion, AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_depth
statement: formalized
proof: formalized
---

# 58.19 Finite étale covers of punctured spectra, I

Section 58.19 of the Stacks Project, [Tag 0BLE](https://stacks.math.columbia.edu/tag/0BLE). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BLF, a situation

[Tag 0BLF](https://stacks.math.columbia.edu/tag/0BLF) in the Stacks Project.

**`Stacks.FundamentalGroup.LocalLefschetzSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalLefschetzSituation.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalLefschetzSituation.lean#L64).

> The standing data and hypotheses of the local Lefschetz situation.

```lean
public structure LocalLefschetzSituation
```

**`AlgebraicGeometry.LocalLefschetzSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LocalLefschetz.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LocalLefschetz.lean#L62).

> The standing data of the local Lefschetz situation: a Noetherian local ring `A` together
> with an element `f` of its maximal ideal.

```lean
structure LocalLefschetzSituation
```

Declarations registered for the tag:

- [`Stacks.Divisors.puncturedSpectrum`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Stacks.Divisors.puncturedSpectrum#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LocalLefschetz.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LocalLefschetz.lean#L57) (StacksFrontier): “the punctured spectra”.
- [`Stacks.puncturedSpectrum`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PuncturedSpectrum/Defs.lean#L32), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/LocalCohomology/Deps/PuncturedSpectrumAffine.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Deps/PuncturedSpectrumAffine.lean#L59) (StacksFrontier): “the punctured spectra”.

## Tag 0BLG, a lemma

[Tag 0BLG](https://stacks.math.columbia.edu/tag/0BLG) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.faithful_finiteEtaleRestriction`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L229).

> **Stacks Project, Tag 0BLG.** In the local Lefschetz situation, base change of finite étale
> covers from the punctured spectrum of `A` to the punctured spectrum of `A / fA` is faithful,
> provided either that `dim (A / 𝔭) ≥ 2` for every minimal prime `𝔭` of `A` with `f ∉ 𝔭`, or
> that every connected component of `U` meets `U₀`.

```lean
lemma faithful_finiteEtaleRestriction (S : LocalLefschetzSituation.{u})
    (h :
      (∀ p : PrimeSpectrum S.A, IsMinimalPrime p.asIdeal →
        S.f ∉ p.asIdeal → 2 ≤ ringKrullDim (S.A ⧸ p.asIdeal)) ∨
      (∀ c : ConnectedComponents S.U,
        ∃ x : S.U₀, ConnectedComponents.mk (S.U₀ToU.base x) = c)) :
    (finiteEtaleBaseChange S.U₀ToU).Faithful
```

## Tag 0BLH, a lemma

[Tag 0BLH](https://stacks.math.columbia.edu/tag/0BLH) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_extension_of_completion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FiniteExtensionFromCompletion.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FiniteExtensionFromCompletion.lean#L580).

> A finite cover of the punctured spectrum which extends over the completed
> spectrum extends over the original local spectrum, compatibly with both given
> covers.

```lean
lemma exists_finite_extension_of_completion
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (V : Scheme.{u}) (pi : V ⟶ (Stacks.Divisors.puncturedSpectrum A).toScheme)
    [IsFinite pi] :
    let Ahat := AdicCompletion (maximalIdeal A) A
    let Xhat := Spec (.of Ahat)
    let completionMap : Xhat ⟶ Spec (.of A) :=
      Spec.map (CommRingCat.ofHom (algebraMap A Ahat))
    let Uhat := pullback (Stacks.Divisors.puncturedSpectrum A).ι completionMap
    let UhatToU : Uhat ⟶ (Stacks.Divisors.puncturedSpectrum A).toScheme := pullback.fst _ _
    let Vhat := pullback pi UhatToU
    let pihat : Vhat ⟶ Uhat := pullback.snd _ _
    ∀ (Yhat : Scheme.{u}) (fhat : Yhat ⟶ Xhat) [IsFinite fhat]
      (ghat : Vhat ⟶ Yhat),
      IsPullback pihat ghat
          (pullback.snd (Stacks.Divisors.puncturedSpectrum A).ι completionMap) fhat →
        (∃ (Y : Scheme.{u}) (f : Y ⟶ Spec (.of A)) (g : V ⟶ Y) (h : Yhat ⟶ Y),
          IsFinite f ∧
            IsPullback pi g (Stacks.Divisors.puncturedSpectrum A).ι f ∧
            IsPullback fhat h completionMap f ∧
            (pullback.fst pi UhatToU ≫ g = ghat ≫ h))
```

## Tag 0BLI, a lemma

[Tag 0BLI](https://stacks.math.columbia.edu/tag/0BLI) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulFromCompletion.lean, line 873](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulFromCompletion.lean#L873).

> **Stacks Project, Tag 0BLI.** In the local Lefschetz situation assume that `A` is henselian,
> or more generally that `(A, fA)` is a henselian pair. If restriction of finite étale covers from
> the punctured spectrum of the `𝔪`-adic completion to its closed fibre is fully faithful, then
> restriction from `U` to `U₀` is fully faithful.

```lean
theorem fullyFaithful_finiteEtaleRestriction_of_completion
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianLocalRing S.A ∨ HenselianPair S.A S.principalIdeal)
    (h : let X' := Spec (.of (AdicCompletion (IsLocalRing.maximalIdeal S.A) S.A))
      let completionMap : X' ⟶ S.X :=
        Spec.map (CommRingCat.ofHom
          (algebraMap S.A (AdicCompletion (IsLocalRing.maximalIdeal S.A) S.A)))
      let U'ToU := pullback.fst S.UOpen.ι completionMap
      let U'₀ToU' := pullback.snd S.U₀ToU U'ToU
      Nonempty (finiteEtaleBaseChange U'₀ToU').FullyFaithful) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

## Tag 0EK5, a lemma

[Tag 0EK5](https://stacks.math.columbia.edu/tag/0EK5) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulComplete.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulComplete.lean#L334). The attribute's comment: “under hypothesis (c)(ii), the depth-plus-dimension form, and in the case where `A` is in addition `f`-adically complete; branch (c)(i) and the reduction to the complete case are not carried out, and hEKP (the chain (1) ⇒ (4) of Stacks 0EKP), h0GN2 (Stacks 0GN2) and halgebra are granted as general hypotheses about other rings and other schemes”.

> **[Stacks, Tag 0EK5]** under hypothesis (c)(ii), in the case where `A` is in addition
> `f`-adically complete. In the local Lefschetz situation assume that `A` has a dualizing complex,
> that the pair `(A, (f))` is henselian, and that `depth(A_𝔭) + dim(A/𝔭) > 2` for every prime
> `𝔭 ⊂ A` with `f ∉ 𝔭`. If moreover `A` is `f`-adically complete, then `FÉt_U ⟶ FÉt_{U₀}` is
> fully faithful.
>
> Two restrictions of the tag are recorded in the attribute.
>
> * Hypothesis (c) of the tag is a disjunction, and only branch (ii) — the depth-plus-dimension
>   inequality — is treated. Branch (c)(i) is not: deducing (ii) from it is the
>   `(S₂)`-plus-dimension argument of the source, which goes through Stacks 0339, 0A80, 0AW6 and
>   0AWY and is not carried out here.
> * The `f`-adic completeness of `A` is the one hypothesis beyond the tag's own. The source
>   obtains it by replacing `A` by its `𝔪`-adic completion, which is Stacks 0BLI, available here
>   as `…fullyFaithful_finiteEtaleRestriction_of_completion`, together with Stacks 0EHW for the
>   inheritance of (c)(ii); that reduction is not carried out here. The henselian hypothesis `hS`
>   is the tag's hypothesis (b) and is exactly what the omitted reduction consumes, so it is
>   stated but not used below.
>
> The carried hypotheses `hEKP`, `h0GN2` and `halgebra` are the ones discussed on
> `fullyFaithful_finiteEtaleRestriction_of_annihilated`; here `hEKP` arrives through
> `Stacks.Algebraization.completionFullyFaithful_of_isAdicComplete_of_depth` (Stacks 0EKT) rather
> than through Stacks 0EKS. None of the three mentions `A`, `f`, `U` or `U₀`, and none is about
> finite étale covers.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_depth
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianPair S.A S.principalIdeal)
    (omega : DerivedCategory (ModuleCat.{u} S.A))
    (homega : Dualizing.IsDualizingComplex (A := S.A) (K := omega))
    (hcomplete : IsAdicComplete (Ideal.span {S.f}) S.A)
    (hdepth : ∀ p : PrimeSpectrum S.A, S.f ∉ p.asIdeal →
      enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl S.A)) +
        krullDimToEInt (ringKrullDim (S.A ⧸ p.asIdeal)) > ((2 : ℤ) : EInt))
    (hEKP : ∀ (B : Type u) [CommRing B] [IsNoetherianRing B] (b : Ideal B) (g : B),
      Scheme.IsQuasiAffine (complementZeroLocus B b : Scheme) →
      Function.Bijective
        (Stacks.Algebraization.ComplementTower.sectionsToLimit B b g (ModuleCat.of B B)) →
      CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus B b : Scheme)
        (complementPrincipalIdealSheaf B b g))
    (h0GN2 : ∀ {Z Z' : Scheme.{u}} (κ : Z' ⟶ Z) [IsClosedImmersion κ] (N : Z.Modules),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} N →
      Stacks.Algebraization.IsInfinitesimalSectionsComplete κ
        (Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf N) →
      (∀ φ ψ : N ⟶ SheafOfModules.unit Z.ringCatSheaf,
          (∀ n : ℕ, φ ≫ nthOrderUnitMap κ n = ψ ≫ nthOrderUnitMap κ n) → φ = ψ) ∧
        ∀ α : ∀ n : ℕ, N ⟶ AlgebraSheaf.underlyingModule (nthOrderAlgebra κ n),
          (∀ n : ℕ, α (n + 1) ≫ nthOrderTransitionMap κ n = α n) →
          ∃ φ : N ⟶ SheafOfModules.unit Z.ringCatSheaf,
            ∀ n : ℕ, φ ≫ nthOrderUnitMap κ n = α n)
    (halgebra : ∀ {Z : Scheme.{u}} (B C : AlgebraSheaf Z) (D : ℕ → AlgebraSheaf Z)
      (r : ∀ n : ℕ, C ⟶ D n)
      (φ : AlgebraSheaf.underlyingModule B ⟶ AlgebraSheaf.underlyingModule C),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (AlgebraSheaf.underlyingModule B) →
      _root_.SheafOfModules.IsCoherent (AlgebraSheaf.underlyingModule B) →
      (∀ n : ℕ, ∃ ψ : B ⟶ D n,
        AlgebraSheaf.underlyingModuleMap ψ = φ ≫ AlgebraSheaf.underlyingModuleMap (r n)) →
      (∀ P : Z.Modules, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} P →
        _root_.SheafOfModules.IsCoherent P →
        ∀ a b : P ⟶ AlgebraSheaf.underlyingModule C,
          (∀ n : ℕ, a ≫ AlgebraSheaf.underlyingModuleMap (r n) =
            b ≫ AlgebraSheaf.underlyingModuleMap (r n)) → a = b) →
      ∃ ψ : B ⟶ C, AlgebraSheaf.underlyingModuleMap ψ = φ) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_dualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean#L216).

> **[Stacks, Tag 0EK5].** In the local Lefschetz situation assume
>
> * (a) `A` has a dualizing complex,
> * (b) the pair `(A, (f))` is henselian,
> * (c) one of the following is true:
>   * (i) `A_f` is `(S₂)` and every irreducible component of `X` not contained in `X₀` has
>     dimension `≥ 3`, or
>   * (ii) for every prime `𝔭 ⊂ A` with `f ∉ 𝔭` we have `depth(A_𝔭) + dim(A/𝔭) > 2`.
>
> Then the restriction functor `FÉt_U ⟶ FÉt_{U₀}` is fully faithful.
>
> Hypothesis (a) is `hdual`, (b) is `hS` and (c) is the disjunction `hc`. In branch (c)(i), `(S₂)`
> for `A_f` is `PropertySkRing (Localization.Away S.f) 2`, and an irreducible component of `X` not
> contained in `X₀` is `V(𝔮)` for a minimal prime `𝔮` of `A` with `f ∉ 𝔮`, of dimension
> `dim(A/𝔮)`. In branch (c)(ii) the depth of `A_𝔭` is that of `A_𝔭` as a module over itself along
> its maximal ideal, and the inequality is read in the extended integers.
>
> The proof is the source's: branch (c)(i) implies branch (c)(ii), by
> `two_lt_depth_add_ringKrullDim_of_propertySkRing_away` — `A` is universally catenary by
> Stacks 0A80 because it has a dualizing complex — and under (c)(ii) the statement is
> `fullyFaithful_finiteEtaleRestriction_of_depth_add_dim`: reduction to the `𝔪`-adic completion by
> Stacks 0BLI, then Stacks 0EKT and Stacks 0EL8.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_dualizingComplex
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
          krullDimToEInt (ringKrullDim (S.A ⧸ p.asIdeal)) > ((2 : ℤ) : EInt)) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

## Tag 0BM6, a lemma

[Tag 0BM6](https://stacks.math.columbia.edu/tag/0BM6) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulComplete.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulComplete.lean#L258). The attribute's comment: “the case where `A` is in addition `f`-adically complete, the reduction to that case (Stacks 0BLI together with Stacks 0ALZ) not being carried out; granted hEKP (the chain (1) ⇒ (4) of Stacks 0EKP), h0GN2 (Stacks 0GN2) and halgebra, all three carried as general hypotheses about other rings and other schemes”.

> **[Stacks, Tag 0BM6]** in the case where `A` is in addition `f`-adically complete. In the
> local Lefschetz situation assume that `H¹_𝔪(A)` and `H²_𝔪(A)` are annihilated by a power of `f`
> and that `A` is henselian — or more generally that the pair `(A, (f))` is henselian. If moreover
> `A` is `f`-adically complete, then `FÉt_U ⟶ FÉt_{U₀}` is fully faithful.
>
> The `f`-adic completeness of `A` is the one hypothesis beyond the tag's own. The source's proof
> obtains it by replacing `A` with its `𝔪`-adic completion, which is Stacks 0BLI, available here as
> `AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_completion`,
> together with Stacks 0ALZ for the inheritance of the annihilation hypothesis; that reduction is
> *not* carried out here, so the statement is the tag restricted to an `f`-adically complete `A`.
> The henselian hypothesis `hS` is the tag's hypothesis (2); it is exactly what the omitted
> reduction consumes, so it is stated but not used below.
>
> Three hypotheses about other objects are carried, each inherited verbatim from the result that
> needs it and each stated about arbitrary rings or arbitrary schemes:
>
> * `hEKP` is the chain (1) ⇒ (4) of [Stacks, Tag 0EKP], the hypothesis of
>   `Stacks.Algebraization.completionFullyFaithful_of_isAdicComplete_of_annihilated`
>   (Stacks 0EKS). It speaks of every Noetherian ring `B`, every ideal `𝔟 ⊆ B` and every `g ∈ B`.
> * `h0GN2` is [Stacks, Tag 0GN2] in the shape in which Stacks 0EL8 uses it, and `halgebra` is the
>   multiplicativity criterion for a morphism of the underlying modules of two sheaves of
>   algebras; both are the hypotheses of
>   `Stacks.FundamentalGroup.fullyFaithful_finiteEtaleBaseChange_of_completionFullyFaithful`
>   (Stacks 0EL8) and both are stated about arbitrary schemes and arbitrary closed immersions.
>
> None of the three mentions `A`, `f`, `U` or `U₀`, and none is about finite étale covers of a
> punctured spectrum.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_annihilated
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianLocalRing S.A ∨ HenselianPair S.A S.principalIdeal)
    (hcomplete : IsAdicComplete (Ideal.span {S.f}) S.A)
    (h1 : ∃ n, ∀ x : localCohomologyModule S.A (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing (maximalIdeal S.A)) (ModuleCat.of S.A S.A) 1,
      S.f ^ n • x = 0)
    (h2 : ∃ n, ∀ x : localCohomologyModule S.A (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing (maximalIdeal S.A)) (ModuleCat.of S.A S.A) 2,
      S.f ^ n • x = 0)
    (hEKP : ∀ (B : Type u) [CommRing B] [IsNoetherianRing B] (b : Ideal B) (g : B),
      Scheme.IsQuasiAffine (complementZeroLocus B b : Scheme) →
      Function.Bijective
        (Stacks.Algebraization.ComplementTower.sectionsToLimit B b g (ModuleCat.of B B)) →
      CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus B b : Scheme)
        (complementPrincipalIdealSheaf B b g))
    (h0GN2 : ∀ {Z Z' : Scheme.{u}} (κ : Z' ⟶ Z) [IsClosedImmersion κ] (N : Z.Modules),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} N →
      Stacks.Algebraization.IsInfinitesimalSectionsComplete κ
        (Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf N) →
      (∀ φ ψ : N ⟶ SheafOfModules.unit Z.ringCatSheaf,
          (∀ n : ℕ, φ ≫ nthOrderUnitMap κ n = ψ ≫ nthOrderUnitMap κ n) → φ = ψ) ∧
        ∀ α : ∀ n : ℕ, N ⟶ AlgebraSheaf.underlyingModule (nthOrderAlgebra κ n),
          (∀ n : ℕ, α (n + 1) ≫ nthOrderTransitionMap κ n = α n) →
          ∃ φ : N ⟶ SheafOfModules.unit Z.ringCatSheaf,
            ∀ n : ℕ, φ ≫ nthOrderUnitMap κ n = α n)
    (halgebra : ∀ {Z : Scheme.{u}} (B C : AlgebraSheaf Z) (D : ℕ → AlgebraSheaf Z)
      (r : ∀ n : ℕ, C ⟶ D n)
      (φ : AlgebraSheaf.underlyingModule B ⟶ AlgebraSheaf.underlyingModule C),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (AlgebraSheaf.underlyingModule B) →
      _root_.SheafOfModules.IsCoherent (AlgebraSheaf.underlyingModule B) →
      (∀ n : ℕ, ∃ ψ : B ⟶ D n,
        AlgebraSheaf.underlyingModuleMap ψ = φ ≫ AlgebraSheaf.underlyingModuleMap (r n)) →
      (∀ P : Z.Modules, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} P →
        _root_.SheafOfModules.IsCoherent P →
        ∀ a b : P ⟶ AlgebraSheaf.underlyingModule C,
          (∀ n : ℕ, a ≫ AlgebraSheaf.underlyingModuleMap (r n) =
            b ≫ AlgebraSheaf.underlyingModuleMap (r n)) → a = b) →
      ∃ ψ : B ⟶ C, AlgebraSheaf.underlyingModuleMap ψ = φ) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean#L139).

> **[Stacks, Tag 0BM6].** In the local Lefschetz situation assume that `H¹_𝔪(A)` and `H²_𝔪(A)`
> are annihilated by a power of `f` and that `A` is henselian, or more generally that the pair
> `(A, (f))` is henselian. Then `FÉt_U ⟶ FÉt_{U₀}` is fully faithful.
>
> The proof is the source's. Replacing `A` by its `𝔪`-adic completion reduces the statement to the
> case of an `f`-adically complete `A`, which is Stacks 0BLI in the form
> `fullyFaithful_finiteEtaleRestriction_of_isAdicCompleteCase`; the henselian hypothesis `hS` is
> what that reduction consumes, and the annihilation hypothesis passes to the completion by
> Stacks 0ALZ, which is `annihilated_completion`. In the complete case completion along `(f)𝒪_U`
> is fully faithful on the finite locally free sheaves by Stacks 0EKS,
> `Stacks.Algebraization.completionFullyFaithfulOnFiniteLocallyFree_of_isAdicComplete_of_`
> `annihilated`, and
> `fullyFaithful_finiteEtaleRestriction_of_completionFullyFaithfulOnFiniteLocallyFree` concludes.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianLocalRing S.A ∨ HenselianPair S.A S.principalIdeal)
    (h1 : ∃ n, ∀ x : localCohomologyModule S.A (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing (maximalIdeal S.A)) (ModuleCat.of S.A S.A) 1,
      S.f ^ n • x = 0)
    (h2 : ∃ n, ∀ x : localCohomologyModule S.A (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing (maximalIdeal S.A)) (ModuleCat.of S.A S.A) 2,
      S.f ^ n • x = 0) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

## Tag 0BLJ, a lemma

[Tag 0BLJ](https://stacks.math.columbia.edu/tag/0BLJ) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_three_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulComplete.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulComplete.lean#L409). The attribute's comment: “the case where `A` is in addition `f`-adically complete, inherited from the form in which Stacks 0BM6 is available here: the reduction to that case (Stacks 0BLI together with Stacks 0ALZ) is not carried out; granted hEKP (the chain (1) ⇒ (4) of Stacks 0EKP), h0GN2 (Stacks 0GN2) and halgebra, all three carried as general hypotheses about other rings and other schemes. The passage from the depth hypothesis to the vanishing of `H¹_𝔪(A)` and `H²_𝔪(A)`, which is the source's own proof, is supplied unconditionally from Stacks 0AVZ”.

> **[Stacks, Tag 0BLJ]** in the case where `A` is in addition `f`-adically complete. In the
> local Lefschetz situation assume that `A` has depth at least `3` and that the pair `(A, (f))` is
> henselian. Then `FÉt_U ⟶ FÉt_{U₀}` is fully faithful.
>
> This is the source's two-line proof: depth at least `3` forces `H¹_𝔪(A) = H²_𝔪(A) = 0` by
> [Stacks, Tag 0AVZ], so the annihilation hypothesis of Stacks 0BM6 holds with any exponent and
> `fullyFaithful_finiteEtaleRestriction_of_annihilated` applies. The henselian hypothesis is
> stated in the more general of the two forms the source offers — `(A, (f))` a henselian pair,
> rather than `A` henselian — and is handed on unchanged.
>
> The restrictions are inherited from `fullyFaithful_finiteEtaleRestriction_of_annihilated` and
> are nothing beyond them: `A` is assumed `f`-adically complete, the reduction to that case
> (Stacks 0BLI with Stacks 0ALZ) not being carried out, and `hEKP`, `h0GN2` and `halgebra` are
> carried as discussed there. None of the three mentions `A`, `f`, `U` or `U₀`. The depth
> hypothesis itself is consumed here, not carried.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_three_le_depth
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianPair S.A S.principalIdeal)
    (hdepth : 3 ≤ Module.depth S.A (maximalIdeal S.A) S.A)
    (hcomplete : IsAdicComplete (Ideal.span {S.f}) S.A)
    (hEKP : ∀ (B : Type u) [CommRing B] [IsNoetherianRing B] (b : Ideal B) (g : B),
      Scheme.IsQuasiAffine (complementZeroLocus B b : Scheme) →
      Function.Bijective
        (Stacks.Algebraization.ComplementTower.sectionsToLimit B b g (ModuleCat.of B B)) →
      CompletionFullyFaithfulOnFiniteLocallyFree (complementZeroLocus B b : Scheme)
        (complementPrincipalIdealSheaf B b g))
    (h0GN2 : ∀ {Z Z' : Scheme.{u}} (κ : Z' ⟶ Z) [IsClosedImmersion κ] (N : Z.Modules),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} N →
      Stacks.Algebraization.IsInfinitesimalSectionsComplete κ
        (Stacks.AlgebraicGeometry.ReflexiveModules.dualSheaf N) →
      (∀ φ ψ : N ⟶ SheafOfModules.unit Z.ringCatSheaf,
          (∀ n : ℕ, φ ≫ nthOrderUnitMap κ n = ψ ≫ nthOrderUnitMap κ n) → φ = ψ) ∧
        ∀ α : ∀ n : ℕ, N ⟶ AlgebraSheaf.underlyingModule (nthOrderAlgebra κ n),
          (∀ n : ℕ, α (n + 1) ≫ nthOrderTransitionMap κ n = α n) →
          ∃ φ : N ⟶ SheafOfModules.unit Z.ringCatSheaf,
            ∀ n : ℕ, φ ≫ nthOrderUnitMap κ n = α n)
    (halgebra : ∀ {Z : Scheme.{u}} (B C : AlgebraSheaf Z) (D : ℕ → AlgebraSheaf Z)
      (r : ∀ n : ℕ, C ⟶ D n)
      (φ : AlgebraSheaf.underlyingModule B ⟶ AlgebraSheaf.underlyingModule C),
      AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u}
        (AlgebraSheaf.underlyingModule B) →
      _root_.SheafOfModules.IsCoherent (AlgebraSheaf.underlyingModule B) →
      (∀ n : ℕ, ∃ ψ : B ⟶ D n,
        AlgebraSheaf.underlyingModuleMap ψ = φ ≫ AlgebraSheaf.underlyingModuleMap (r n)) →
      (∀ P : Z.Modules, AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} P →
        _root_.SheafOfModules.IsCoherent P →
        ∀ a b : P ⟶ AlgebraSheaf.underlyingModule C,
          (∀ n : ℕ, a ≫ AlgebraSheaf.underlyingModuleMap (r n) =
            b ≫ AlgebraSheaf.underlyingModuleMap (r n)) → a = b) →
      ∃ ψ : B ⟶ C, AlgebraSheaf.underlyingModuleMap ψ = φ) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_three_le_depth_of_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean#L246).

> **[Stacks, Tag 0BLJ].** In the local Lefschetz situation assume that `A` has depth at least
> `3` and that the pair `(A, (f))` is henselian. Then `FÉt_U ⟶ FÉt_{U₀}` is fully faithful.
>
> This is the source's proof: depth at least `3` forces `H¹_𝔪(A) = H²_𝔪(A) = 0` by
> [Stacks, Tag 0AVZ], through `Stacks.LocalCohomology.isZero_localCohomology_of_lt_depth`, so the
> annihilation hypothesis of Stacks 0BM6 holds with any exponent and
> `fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian` applies. The henselian
> hypothesis is the more general of the two forms the source offers — `(A, (f))` a henselian pair,
> rather than `A` henselian.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_three_le_depth_of_henselian
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianPair S.A S.principalIdeal)
    (hdepth : 3 ≤ Module.depth S.A (maximalIdeal S.A) S.A) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.19, Tag 0BLE](https://stacks.math.columbia.edu/tag/0BLE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
