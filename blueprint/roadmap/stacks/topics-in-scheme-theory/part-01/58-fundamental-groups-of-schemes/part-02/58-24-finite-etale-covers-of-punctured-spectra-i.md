---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocalLefschetzSituation.essSurj_finiteEtaleBaseChange_U₀ToU_of_dualizing, AlgebraicGeometry.LocalLefschetzSituation.essSurj_finiteEtaleBaseChange_U₀ToU_of_isAdicComplete
statement: formalized
proof: formalized
---

# 58.24 Finite étale covers of punctured spectra, IV

Section 58.24 of the Stacks Project, [Tag 0EK8](https://stacks.math.columbia.edu/tag/0EK8). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EK9, a lemma

[Tag 0EK9](https://stacks.math.columbia.edu/tag/0EK9) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.essSurj_finiteEtaleBaseChange_U₀ToU_of_dualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NeighbourhoodVocabularyDualizing.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NeighbourhoodVocabularyDualizing.lean#L133). The attribute's comment: “the restriction functor FÉt\_U ⥤ FÉt\_\{U₀} is essentially surjective, under the tag's three hypotheses; nothing beyond them is assumed”.

> **Stacks Project, Tag 0EK9.**  Let `(A, 𝔪)` be a Noetherian local ring and let `f ∈ 𝔪`.
> Write `X = Spec A`, let `U = X ∖ {𝔪}` and `U₀ = Spec (A / fA) ∖ {𝔪}` be the two punctured
> spectra.  Assume
>
> 1. `A` has a dualizing complex and is `f`-adically complete,
> 2. one of
>    * (a) `A_f` satisfies Serre's condition `(S₂)` and every irreducible component of `X` not
>      contained in `V(f)` has dimension at least `4`, or
>    * (b) `depth(A_𝔭) + dim(A/𝔭) > 3` whenever `𝔭 ∉ V(f)` and `V(𝔭) ∩ V(f) ≠ {𝔪}`,
> 3. purity holds for `(A_f)_𝔭` for every maximal ideal `𝔭 ⊂ A_f`.
>
> Then the restriction functor `FÉt_U ⥤ FÉt_{U₀}` is essentially surjective.
>
> The source's argument is followed.  Hypotheses (1) and (2) make the restriction functor
> `colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} ⥤ FÉt_{U₀}` an equivalence, so a given finite étale cover of `U₀`
> is already the restriction of a cover of some open `U'` of `X` with `U₀ ⊆ U' ⊆ U`.  The points of
> `U` that `U'` omits correspond to maximal ideals of `A_f`, so hypothesis (3) makes purity
> available at each of them and the cover extends from `U'` across them to a cover of `U`.

```lean
theorem essSurj_finiteEtaleBaseChange_U₀ToU_of_dualizing
    [HasDerivedCategory.{w} (ModuleCat.{u} S.A)]
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcomplete : IsAdicComplete (Ideal.span {S.f}) S.A)
    (hcond :
      (PropertySkRing (Localization.Away S.f) 2 ∧
          ∀ p : PrimeSpectrum S.A, IsMinimalPrime p.asIdeal → S.f ∉ p.asIdeal →
            (4 : WithBot ℕ∞) ≤ ringKrullDim (S.A ⧸ p.asIdeal)) ∨
        (∀ p : PrimeSpectrum S.A, S.f ∉ p.asIdeal →
          ({q : PrimeSpectrum S.A | p.asIdeal ≤ q.asIdeal} ∩
            {q : PrimeSpectrum S.A | S.f ∈ q.asIdeal}) ≠
            {⟨maximalIdeal S.A, (maximalIdeal.isMaximal S.A).isPrime⟩} →
          (3 : WithBot ℕ∞) <
            (Module.depth (Localization.AtPrime p.asIdeal)
              (maximalIdeal (Localization.AtPrime p.asIdeal))
              (Localization.AtPrime p.asIdeal) : WithBot ℕ∞) +
              ringKrullDim (S.A ⧸ p.asIdeal)))
    (haway : ∀ (p : Ideal (Localization.Away S.f)) [p.IsMaximal],
      HasPurity (Localization.AtPrime p)) :
    (finiteEtaleBaseChange S.U₀ToU).EssSurj
```

## Tag 0EKA, a lemma

[Tag 0EKA](https://stacks.math.columbia.edu/tag/0EKA) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.essSurj_finiteEtaleBaseChange_U₀ToU_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/HypersurfaceExtension.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/HypersurfaceExtension.lean#L247). The attribute's comment: “the restriction functor FÉt\_U ⥤ FÉt\_\{U₀} is essentially surjective, under the tag's four hypotheses; nothing beyond them is assumed”.

> **Stacks Project, Tag 0EKA.**  Let `(A, 𝔪)` be a Noetherian local ring and let `f ∈ 𝔪`.
> Assume
>
> 1. `A` is `f`-adically complete,
> 2. `f` is a nonzerodivisor,
> 3. `H¹_𝔪(A/fA)` and `H²_𝔪(A/fA)` are finite `A`-modules, and
> 4. purity holds for `(A_f)_𝔭` for every maximal ideal `𝔭 ⊂ A_f`.
>
> Then the restriction functor `FÉt_U ⥤ FÉt_{U₀}` is essentially surjective.
>
> The source proves this by the proof of Stacks 0EK9 with Stacks 0BLV in place of Stacks 0DXY, and
> that is what happens here.  Hypotheses (1)–(3) are the hypotheses of Stacks 0BLV, and give an
> open `U'` of `X` with `U₀ ⊆ U' ⊆ U` over which a given finite étale cover of `U₀` is already
> defined.  The points of `U` outside `U'` are maximal ideals of `A_f`, so hypothesis (4) makes
> purity available at each of them and the cover extends from `U'` to `U`.

```lean
theorem essSurj_finiteEtaleBaseChange_U₀ToU_of_isAdicComplete
    (hcomplete : IsAdicComplete S.principalIdeal S.A) (hnzd : S.f ∈ nonZeroDivisors S.A)
    (hH1 : Module.Finite S.A (localCohomologyModule S.A (maximalIdeal S.A)
      (maximalIdeal S.A).fg_of_isNoetherianRing (ModuleCat.of S.A S.quotientRing) 1))
    (hH2 : Module.Finite S.A (localCohomologyModule S.A (maximalIdeal S.A)
      (maximalIdeal S.A).fg_of_isNoetherianRing (ModuleCat.of S.A S.quotientRing) 2))
    (haway : ∀ (p : Ideal (Localization.Away S.f)) [p.IsMaximal],
      HasPurity (Localization.AtPrime p)) :
    (finiteEtaleBaseChange S.U₀ToU).EssSurj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.24, Tag 0EK8](https://stacks.math.columbia.edu/tag/0EK8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
