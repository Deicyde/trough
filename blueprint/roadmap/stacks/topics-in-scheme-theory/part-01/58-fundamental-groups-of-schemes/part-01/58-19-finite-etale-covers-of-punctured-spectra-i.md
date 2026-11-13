---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.LocalLefschetzSituation, AlgebraicGeometry.LocalLefschetzSituation, Stacks.puncturedSpectrum, AlgebraicGeometry.LocalLefschetzSituation.faithful_finiteEtaleRestriction, AlgebraicGeometry.exists_finite_extension_of_completion, AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_completion, AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_dualizingComplex, AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian
statement: formalized
proof: formalized
---

# 58.19 Finite étale covers of punctured spectra, I

Section 58.19 of the Stacks Project, [Tag 0BLE](https://stacks.math.columbia.edu/tag/0BLE). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BLF, a situation

[Tag 0BLF](https://stacks.math.columbia.edu/tag/0BLF) in the Stacks Project.

**`Stacks.FundamentalGroup.LocalLefschetzSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalLefschetzSituation.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/LocalLefschetzSituation.lean#L64).

> The standing data and hypotheses of the local Lefschetz situation.

```lean
public structure LocalLefschetzSituation
```

**`AlgebraicGeometry.LocalLefschetzSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LocalLefschetz.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/LocalLefschetz.lean#L60).

> The standing data of the local Lefschetz situation: a Noetherian local ring `A` together
> with an element `f` of its maximal ideal.

```lean
structure LocalLefschetzSituation
```

Declarations registered for the tag:

- [`Stacks.puncturedSpectrum`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PuncturedSpectrum/Defs.lean#L32), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/LocalCohomology/Deps/PuncturedSpectrumAffine.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalCohomology/Deps/PuncturedSpectrumAffine.lean#L59) (StacksFrontier): “the punctured spectra”.

## Tag 0BLG, a lemma

[Tag 0BLG](https://stacks.math.columbia.edu/tag/0BLG) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.faithful_finiteEtaleRestriction`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L229).

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

**`AlgebraicGeometry.exists_finite_extension_of_completion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FiniteExtensionFromCompletion.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FiniteExtensionFromCompletion.lean#L580).

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

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulFromCompletion.lean, line 873](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulFromCompletion.lean#L873).

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

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_dualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean#L219). The attribute's comment: “for an arbitrary Noetherian local ring `A` with a dualizing complex and `(A, (f))` a henselian pair, hypothesis (c) being the disjunction of branches (i) and (ii)”.

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

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean#L141). The attribute's comment: “for an arbitrary Noetherian local ring `A`, with `H¹_𝔪(A)` and `H²_𝔪(A)` killed by a power of `f` and with `A` henselian or `(A, (f))` a henselian pair”.

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

**`AlgebraicGeometry.LocalLefschetzSituation.fullyFaithful_finiteEtaleRestriction_of_three_le_depth_of_henselianLocalRing_or`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FullyFaithfulPunctured.lean#L250). The attribute's comment: “for an arbitrary Noetherian local ring `A` of depth at least `3`, with `A` henselian or `(A, (f))` a henselian pair”.

> **[Stacks, Tag 0BLJ].** In the local Lefschetz situation assume that `A` has depth at least
> `3` and that `A` is henselian or, more generally, that the pair `(A, (f))` is henselian. Then
> `FÉt_U ⟶ FÉt_{U₀}` is fully faithful.
>
> The henselian hypothesis `hS` is the source's disjunction. This is the source's proof: depth at
> least `3` forces `H¹_𝔪(A) = H²_𝔪(A) = 0` by [Stacks, Tag 0AVZ], through
> `Stacks.LocalCohomology.isZero_localCohomology_of_lt_depth`, so the annihilation hypothesis of
> Stacks 0BM6 holds with any exponent and
> `fullyFaithful_finiteEtaleRestriction_of_annihilated_of_henselian` applies.

```lean
public theorem fullyFaithful_finiteEtaleRestriction_of_three_le_depth_of_henselianLocalRing_or
    (S : LocalLefschetzSituation.{u})
    (hS : HenselianLocalRing S.A ∨ HenselianPair S.A S.principalIdeal)
    (hdepth : 3 ≤ Module.depth S.A (maximalIdeal S.A) S.A) :
    Nonempty (finiteEtaleBaseChange S.U₀ToU).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.19, Tag 0BLE](https://stacks.math.columbia.edu/tag/0BLE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
