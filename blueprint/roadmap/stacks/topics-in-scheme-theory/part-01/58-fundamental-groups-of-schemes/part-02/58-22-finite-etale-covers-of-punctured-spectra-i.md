---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocalLefschetzSituation.HasLargeMissingComponents.mono, AlgebraicGeometry.LocalLefschetzSituation.faithful_finiteEtaleBaseChange_of_hasLargeMissingComponents, AlgebraicGeometry.LocalLefschetzSituation.exists_hasLargeMissingComponents, AlgebraicGeometry.LocalLefschetzSituation.exists_le_faithful_finiteEtaleBaseChange, AlgebraicGeometry.LocalLefschetzSituation.exists_le_finiteEtaleBaseChange_map_eq, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_puncturedSpectrum_of_three_le_ringKrullDim, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_puncturedSpectrum_of_isAdicComplete, Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_puncturedSpectrum_principal
statement: formalized
proof: formalized
---

# 58.22 Finite étale covers of punctured spectra, II

Section 58.22 of the Stacks Project, [Tag 0BLU](https://stacks.math.columbia.edu/tag/0BLU). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BLN, a lemma

[Tag 0BLN](https://stacks.math.columbia.edu/tag/0BLN) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.HasLargeMissingComponents.mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L260). The attribute's comment: “stability of the dimension hypothesis under shrinking `U'`”.

> The dimension condition passes to smaller opens: a minimal prime in the smaller open lies in
> the larger one.

```lean
theorem HasLargeMissingComponents.mono {S : LocalLefschetzSituation.{u}} {W W' : S.X.Opens}
    (hWW' : W' ≤ W) (hW : S.HasLargeMissingComponents W) :
    S.HasLargeMissingComponents W'
```

**`AlgebraicGeometry.LocalLefschetzSituation.faithful_finiteEtaleBaseChange_of_hasLargeMissingComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L283). The attribute's comment: “faithfulness of restriction from an open `U'` with `U₀ ⊆ U' ⊆ U`”.

> **Stacks Project, Tag 0BLN.** In the local Lefschetz situation let `U'` be an open of `X`
> with `U₀ ⊆ U' ⊆ U`. If every minimal prime of `A` lying in `U'` but not in `U₀` has
> `dim (A / 𝔭) ≥ 2`, then base change of finite étale covers along `U₀ ⟶ U'` is faithful.

```lean
theorem faithful_finiteEtaleBaseChange_of_hasLargeMissingComponents
    (S : LocalLefschetzSituation.{u}) {W : S.X.Opens} (hW : W ≤ S.UOpen)
    (r : S.U₀ ⟶ W.toScheme) (hr : r ≫ W.ι = S.U₀ToU ≫ S.UOpen.ι)
    (hdim : S.HasLargeMissingComponents W) :
    (finiteEtaleBaseChange r).Faithful
```

**`AlgebraicGeometry.LocalLefschetzSituation.exists_hasLargeMissingComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L342). The attribute's comment: “existence of an open `U'` with `U₀ ⊆ U' ⊆ U` satisfying the dimension hypothesis”.

> **Stacks Project, Tag 0BLN.** In the local Lefschetz situation there is an open `U'` of `X`
> with `U₀ ⊆ U' ⊆ U` satisfying the dimension hypothesis: remove from `U` the one-dimensional
> irreducible components of `X` that do not meet `U₀`.

```lean
theorem exists_hasLargeMissingComponents (S : LocalLefschetzSituation.{u}) :
    ∃ W : S.X.Opens, W ≤ S.UOpen ∧ S.U₀Open ≤ S.X₀ToX ⁻¹ᵁ W ∧
      S.HasLargeMissingComponents W
```

**`AlgebraicGeometry.LocalLefschetzSituation.exists_le_faithful_finiteEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L419). The attribute's comment: “cofinality of the faithful neighbourhoods of `U₀` in `U`, the criterion for faithfulness of restriction from the colimit over all such neighbourhoods”.

> **Stacks Project, Tag 0BLN.** The opens `U'` with `U₀ ⊆ U' ⊆ U` for which restriction of
> finite étale covers to `U₀` is faithful are cofinal among all opens between `U₀` and `U`: this
> is what makes restriction from `colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'}` to `FÉt_{U₀}` faithful.

```lean
theorem exists_le_faithful_finiteEtaleBaseChange (S : LocalLefschetzSituation.{u})
    {V : S.X.Opens} (hV : V ≤ S.UOpen) (hVU₀ : S.U₀Open ≤ S.X₀ToX ⁻¹ᵁ V) :
    ∃ (W : S.X.Opens) (hWU₀ : S.U₀Open ≤ S.X₀ToX ⁻¹ᵁ W),
      W ≤ V ∧ (finiteEtaleBaseChange (S.homToOpen hWU₀)).Faithful
```

**`AlgebraicGeometry.LocalLefschetzSituation.exists_le_finiteEtaleBaseChange_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/FaithfulRestriction.lean#L434). The attribute's comment: “faithfulness of restriction from the colimit over the opens between `U₀` and `U`, written out on representatives of the filtered colimit”.

> **Stacks Project, Tag 0BLN.** Two morphisms of finite étale covers of an open `U'` with
> `U₀ ⊆ U' ⊆ U` which agree after base change to `U₀` already agree after base change to some
> smaller open `U''` with `U₀ ⊆ U'' ⊆ U'`. This is faithfulness of the restriction functor
> `colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} ⟶ FÉt_{U₀}` written out on representatives.

```lean
theorem exists_le_finiteEtaleBaseChange_map_eq (S : LocalLefschetzSituation.{u})
    {V : S.X.Opens} (hV : V ≤ S.UOpen) (hVU₀ : S.U₀Open ≤ S.X₀ToX ⁻¹ᵁ V)
    {A B : FiniteEtaleOver V.toScheme} (a b : A ⟶ B)
    (hab : (finiteEtaleBaseChange (S.homToOpen hVU₀)).map a =
      (finiteEtaleBaseChange (S.homToOpen hVU₀)).map b) :
    ∃ (W : S.X.Opens) (_ : S.U₀Open ≤ S.X₀ToX ⁻¹ᵁ W) (hWV : W ≤ V),
      (finiteEtaleBaseChange (S.X.homOfLE hWV)).map a =
        (finiteEtaleBaseChange (S.X.homOfLE hWV)).map b
```

## Tag 0DXX, a lemma

[Tag 0DXX](https://stacks.math.columbia.edu/tag/0DXX) in the Stacks Project.

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_puncturedSpectrum_of_three_le_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/ReducedThickening/ThreeDimensionalReduction.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/ReducedThickening/ThreeDimensionalReduction.lean#L318). The attribute's comment: “the whole statement, under the source's hypotheses only: a dualizing complex and f-adic completeness, and dimension at least three for every irreducible component of X not contained in the zero locus of f”.

> **Restriction of finite étale covers from the neighbourhoods of `U₀` in `U` is fully
> faithful.**  Let `(A, 𝔪)` be a Noetherian local ring, `f ∈ A`, `X = Spec A`, `X₀ = V(f)`,
> `U = X ∖ {𝔪}` and `U₀ = U ∩ V(f)`.  Assume `A` has a dualizing complex, is `f`-adically complete,
> and that every irreducible component of `X` not contained in `X₀` has dimension at least `3` —
> that is, `dim (A/𝔭) ≥ 3` for every minimal prime `𝔭` of `A` with `f ∉ 𝔭`.  Then the restriction
> functor `colim_{U₀ ⊆ U' ⊆ U open} FÉt_{U'} ⟶ FÉt_{U₀}` is fully faithful.
>
> The dimension hypothesis is a bound at the minimal primes, whereas the completion theorem behind
> full faithfulness needs one at the associated primes; so `A` is first replaced by its reduction,
> where the associated primes are the minimal primes.  The punctured spectrum of the reduction is a
> thickening of `U` carrying its closed subscheme cut out by the image of `f` to `U₀`, and full
> faithfulness of restriction is insensitive to such a thickening; a dualizing complex, `f`-adic
> completeness and the dimension bound all survive the passage to the reduction.
>
> The dualizing complex is asked for in an arbitrary model of the derived category of `A`-modules,
> and moved to the standard model — the one the completion results are stated in — by
> `Stacks.Dualizing.exists_isDualizingComplex_iff_of_models`.

```lean
theorem finiteEtaleColimitFullyFaithful_puncturedSpectrum_of_three_le_ringKrullDim (A : Type u)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A] [HasDerivedCategory.{w} (ModuleCat.{u} A)]
    (f : A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (hdim : ∀ p : PrimeSpectrum A, IsMinimalPrime p.asIdeal → f ∉ p.asIdeal →
      (3 : WithBot ℕ∞) ≤ ringKrullDim (A ⧸ p.asIdeal)) :
    FiniteEtaleColimitFullyFaithful (complementZeroLocus A (maximalIdeal A) : Scheme.{u})
      (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A))
```

## Tag 0BLP, a lemma

[Tag 0BLP](https://stacks.math.columbia.edu/tag/0BLP) in the Stacks Project.

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_puncturedSpectrum_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PuncturedSpectrumFiniteEtaleFullyFaithful.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PuncturedSpectrumFiniteEtaleFullyFaithful.lean#L139). The attribute's comment: “the full statement, proved from the tag's three hypotheses through 0EKV and 0ELA”.

> **[Stacks, Tag 0BLP].** In Situation [Stacks, Tag 0BLF] — a Noetherian local ring `(A, 𝔪)`
> and `f ∈ 𝔪`, with `U = Spec(A) ∖ {𝔪}` the punctured spectrum and `U₀ = U ∩ V(f)` the closed
> subscheme of `U` cut out by `f 𝒪_U` — assume
>
> 1. `A` is `f`-adically complete,
> 2. `f` is a nonzerodivisor, and
> 3. `H¹_𝔪(A/fA)` is a finite `A`-module.
>
> Then the restriction functor `colim_{U₀ ⊆ U' ⊆ U open} FÉt_{U'} ⟶ FÉt_{U₀}` is fully faithful.
>
> The proof is the source's: [Stacks, Tag 0EKV]
> (`Stacks.FundamentalGroup.completionFullyFaithfulComplete_puncturedSpectrum_principal`) gives full
> faithfulness of the completion functor `colim_{U'} Coh(𝒪_{U'}) ⟶ Coh(U, f𝒪_U)` on finite locally
> free objects, and [Stacks, Tag 0ELA]
> (`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_completionFullyFaithfulComplete`)
> turns that into the conclusion.

```lean
theorem finiteEtaleColimitFullyFaithful_puncturedSpectrum_of_isAdicComplete
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (f : A)
    (hf : f ∈ IsLocalRing.maximalIdeal A)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (hnzd : f ∈ nonZeroDivisors A)
    (hfinite : Module.Finite A (localCohomologyModule A (IsLocalRing.maximalIdeal A)
      (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing
      (ModuleCat.of A (A ⧸ Ideal.span {f})) 1)) :
    FiniteEtaleColimitFullyFaithful
      (complementZeroLocus A (IsLocalRing.maximalIdeal A) : Scheme)
      (idealSheafNearVanishing A (Ideal.span {f}) (IsLocalRing.maximalIdeal A))
```

**`Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_puncturedSpectrum_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionFromPuncturedSpectrumNeighborhoods.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionFromPuncturedSpectrumNeighborhoods.lean#L122). The attribute's comment: “granted SectionsExtendNearSubscheme in place of the 0EKV completion input”.

> **[Stacks, Tag 0BLP], granted the section-extension input.** In Situation
> [Stacks, Tag 0BLF] — a Noetherian local ring `(A, 𝔪)` and an element `f ∈ 𝔪`, with
> `U = Spec(A) ∖ {𝔪}` the punctured spectrum and `U₀ = U ∩ V(f)` the zero locus of `f` on it —
> assume that `A` is `f`-adically complete, that `f` is a nonzerodivisor and that `H¹_𝔪(A/fA)` is
> a finite `A`-module. Then the restriction functor
> `colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} ⟶ FÉt_{U₀}` is fully faithful.
>
> **What is granted.** The three hypotheses of the tag are recorded but not consumed. They are
> the hypotheses of [Stacks, Tag 0EKV], whose conclusion — full faithfulness of the completion
> functor `colim_{U'} Coh(𝒪_{U'}) ⟶ Coh(U, f𝒪_U)` on the finite locally free objects — is the
> input the source feeds to [Stacks, Tag 0ELA]; that conclusion is not available in this library,
> and neither is the passage from it to the section-extension property, which is the remainder of
> the proof of Tag 0ELA. Accordingly
> `Stacks.FundamentalGroup.SectionsExtendNearSubscheme`, the shrinking form of the conclusion of
> [Stacks, Tag 0EL8] and the actual input of
> `Stacks.FundamentalGroup.finiteEtaleColimitFullyFaithful_of_sectionsExtendNearSubscheme`, is
> assumed here in place of hypotheses (1)–(3).

```lean
theorem finiteEtaleColimitFullyFaithful_puncturedSpectrum_principal
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (f : A)
    (_hf : f ∈ IsLocalRing.maximalIdeal A)
    (_hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (_hnzd : f ∈ nonZeroDivisors A)
    (_hfinite : Module.Finite A (localCohomologyModule A (IsLocalRing.maximalIdeal A)
      (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing
      (ModuleCat.of A (A ⧸ Ideal.span {f})) 1))
    (hsections : SectionsExtendNearSubscheme
      (complementZeroLocus A (IsLocalRing.maximalIdeal A) : Scheme)
      (idealSheafNearVanishing A (Ideal.span {f}) (IsLocalRing.maximalIdeal A))) :
    FiniteEtaleColimitFullyFaithful
      (complementZeroLocus A (IsLocalRing.maximalIdeal A) : Scheme)
      (idealSheafNearVanishing A (Ideal.span {f}) (IsLocalRing.maximalIdeal A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.22, Tag 0BLU](https://stacks.math.columbia.edu/tag/0BLU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
