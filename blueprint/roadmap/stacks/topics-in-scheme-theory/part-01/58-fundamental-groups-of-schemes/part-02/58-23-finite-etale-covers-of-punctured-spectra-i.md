---
declaration: section
origin: cited
lean: Stacks.FundamentalGroup.finiteEtaleColimitEquivalence_puncturedSpectrum_of_dualizing, AlgebraicGeometry.LocalLefschetzSituation.isColimitRestrictionEquivalence, Stacks.FundamentalGroup.finiteEtaleColimitEquivalence_puncturedSpectrum_of_isAdicComplete, AlgebraicGeometry.finiteEtaleColimitEquivalence_puncturedSpectrum_of_propertySk, AlgebraicGeometry.finiteEtaleColimitEquivalence_puncturedSpectrum_of_isIntegrallyClosed
statement: formalized
proof: formalized
---

# 58.23 Finite étale covers of punctured spectra, III

Section 58.23 of the Stacks Project, [Tag 0EK7](https://stacks.math.columbia.edu/tag/0EK7). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DXY, a lemma

[Tag 0DXY](https://stacks.math.columbia.edu/tag/0DXY) in the Stacks Project.

**`Stacks.FundamentalGroup.finiteEtaleColimitEquivalence_puncturedSpectrum_of_dualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitDualizingEquivalence.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/RestrictionColimitDualizingEquivalence.lean#L327). The attribute's comment: “the restriction functor colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} → FÉt_{U₀} is an equivalence: fully faithful, and every finite étale cover of U₀ extends to a neighbourhood”.

> **[Stacks, Tag 0DXY].** In Situation [Stacks, Tag 0BLF] — `(A, 𝔪)` a Noetherian local ring,
> `f ∈ 𝔪`, `U = Spec(A) ∖ {𝔪}` the punctured spectrum of `A` and `U₀ = U ∩ V(f)` the punctured
> spectrum of `A/fA`, as the closed subscheme of `U` cut out by `f 𝒪_U` — assume
>
> 1. `A` has a dualizing complex and is `f`-adically complete, and
> 2. one of
>    * (a) `A_f` is `(S₂)` and `dim(A/𝔭) ≥ 4` for every minimal prime `𝔭` of `A` with `f ∉ 𝔭`, or
>    * (b) `depth(A_𝔭) + dim(A/𝔭) > 3` for every prime `𝔭 ∉ V(f)` with `V(𝔭) ∩ V(f) ≠ {𝔪}`.
>
> Then the restriction functor `colim_{U₀ ⊆ U' ⊆ U open} FÉt_{U'} ⟶ FÉt_{U₀}` is an equivalence.
>
> The colimit is directed, so the functor is an equivalence exactly when the two conjuncts below
> hold. The first is that it is fully faithful, in the form
> `Stacks.FundamentalGroup.FiniteEtaleColimitFullyFaithful`: morphisms between restrictions to `U₀`
> come from a smaller neighbourhood, and morphisms agreeing on `U₀` agree on a smaller
> neighbourhood. The second is that it is essentially surjective: every finite étale cover of `U₀`
> is the restriction of a finite étale cover of some open `U'` with `U₀ ⊆ U' ⊆ U`.
>
> As in the source, this is [Stacks, Tag 0EK1] for the closed subscheme `U₀` of `U`, with the
> completion equivalence of [Stacks, Tag 0EKY] as input. Full faithfulness is [Stacks, Tag 0ELA]
> applied to
> `Stacks.FundamentalGroup.completionFullyFaithfulComplete_puncturedSpectrum_of_dualizing`, and the
> essential image is the algebraization step of [Stacks, Tag 0EK1] fed by that same input together
> with
> `Stacks.FundamentalGroup.exists_finiteLocallyFree_completion_puncturedSpectrum_of_dualizing`.

```lean
public theorem finiteEtaleColimitEquivalence_puncturedSpectrum_of_dualizing
    [HasDerivedCategory.{w} (ModuleCat.{u} A)] (hf : f ∈ maximalIdeal A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A)
    (hcond :
      (PropertySkRing (Localization.Away f) 2 ∧
          ∀ p : PrimeSpectrum A, IsMinimalPrime p.asIdeal → f ∉ p.asIdeal →
            (4 : WithBot ℕ∞) ≤ ringKrullDim (A ⧸ p.asIdeal)) ∨
        (∀ p : PrimeSpectrum A, f ∉ p.asIdeal →
          ({q : PrimeSpectrum A | p.asIdeal ≤ q.asIdeal} ∩
            {q : PrimeSpectrum A | f ∈ q.asIdeal}) ≠
            {⟨maximalIdeal A, (maximalIdeal.isMaximal A).isPrime⟩} →
          (3 : WithBot ℕ∞) <
            (Module.depth (Localization.AtPrime p.asIdeal)
              (maximalIdeal (Localization.AtPrime p.asIdeal))
              (Localization.AtPrime p.asIdeal) : WithBot ℕ∞) +
              ringKrullDim (A ⧸ p.asIdeal))) :
    FiniteEtaleColimitFullyFaithful (complementZeroLocus A (maximalIdeal A) : Scheme)
        (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)) ∧
      ∀ C : FiniteEtaleOver
        (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)).subscheme,
      ∃ (W : Neighborhood (complementZeroLocus A (maximalIdeal A) : Scheme)
          (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)))
        (V : FiniteEtaleOver (Neighborhood.open _ _ W).toScheme),
        Nonempty ((finiteEtaleBaseChange (Neighborhood.toSchemeHom _ _ W)).obj V ≅ C)
```

## Tag 0BLV, a lemma

[Tag 0BLV](https://stacks.math.columbia.edu/tag/0BLV) in the Stacks Project.

**`AlgebraicGeometry.LocalLefschetzSituation.isColimitRestrictionEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NeighbourhoodRestrictionEquivalence.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/NeighbourhoodRestrictionEquivalence.lean#L328). The attribute's comment: “the equivalence, carrying as explicit hypotheses the purity of restriction `FÉt_{Spec (A/fA)} ⟶ FÉt_{U₀}` and the purity of restriction `FÉt_{Spec A} ⟶ FÉt_{U'}` for the opens `U₀ ⊆ U' ⊆ U`”.

> **Stacks Project, Tag 0BLV.**  In the local Lefschetz situation of Stacks 0BLF assume that
> `A` is `f`-adically complete, that `f` is a nonzerodivisor, and that `H¹_𝔪(A / fA)` and
> `H²_𝔪(A / fA)` are finite `A`-modules.  Then the restriction functor
>
> ```
> colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} ⟶ FÉt_{U₀}
> ```
>
> is an equivalence.
>
> Two purity statements are carried as explicit hypotheses, each about a restriction functor out
> of an affine spectrum and neither about the functor above: that restriction
> `FÉt_{Spec (A / fA)} ⟶ FÉt_{U₀}` is an equivalence, and that restriction `FÉt_{Spec A} ⟶ FÉt_{U'}`
> is an equivalence for every open `U'` between `U₀` and `U`.  The `f`-adic completeness
> hypothesis is discharged: it makes `(A, fA)` a henselian pair, so that Stacks 09ZS identifies
> `FÉt_{Spec A}` with `FÉt_{Spec (A / fA)}`, which is what turns the two carried statements into
> the equivalence of restriction from each neighbourhood `U'` to `U₀`.

```lean
theorem isColimitRestrictionEquivalence (h : S.Hypotheses)
    (hfibre : S.RestrictionToClosedFibreIsEquivalence)
    (hnbhd : S.RestrictionToNeighbourhoodsIsEquivalence) :
    S.IsColimitRestrictionEquivalence
```

**`Stacks.FundamentalGroup.finiteEtaleColimitEquivalence_puncturedSpectrum_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/PuncturedNeighbourhoodEquivalence.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/PuncturedNeighbourhoodEquivalence.lean#L152). The attribute's comment: “the restriction functor colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} → FÉt_{U₀} is an equivalence: fully faithful, and every finite étale cover of U₀ extends to a neighbourhood”.

> **[Stacks, Tag 0BLV].** In Situation [Stacks, Tag 0BLF] — `(A, 𝔪)` a Noetherian local ring,
> `f ∈ 𝔪`, `U = Spec(A) ∖ {𝔪}` the punctured spectrum of `A` and `U₀ = U ∩ V(f)` the punctured
> spectrum of `A/fA` — assume
>
> 1. `A` is `f`-adically complete,
> 2. `f` is a nonzerodivisor, and
> 3. `H¹_𝔪(A/fA)` and `H²_𝔪(A/fA)` are finite `A`-modules.
>
> Then the restriction functor `colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} ⟶ FÉt_{U₀}` is an equivalence.
>
> The colimit is directed, so the functor is an equivalence exactly when the two conjuncts below
> hold. The first is that it is fully faithful, in the form
> `Stacks.FundamentalGroup.FiniteEtaleColimitFullyFaithful`: morphisms between restrictions to
> `U₀` come from a smaller neighbourhood, and morphisms agreeing on `U₀` agree on a smaller
> neighbourhood. The second is that it is essentially surjective: every finite étale cover of `U₀`
> is the restriction of a finite étale cover of some open `U'` with `U₀ ⊆ U' ⊆ U`.

```lean
theorem finiteEtaleColimitEquivalence_puncturedSpectrum_of_isAdicComplete
    (hf : f ∈ IsLocalRing.maximalIdeal A)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A) (hnzd : f ∈ nonZeroDivisors A)
    (hH1 : Module.Finite A (localCohomologyModule A (IsLocalRing.maximalIdeal A)
      (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing
      (ModuleCat.of A (A ⧸ Ideal.span {f})) 1))
    (hH2 : Module.Finite A (localCohomologyModule A (IsLocalRing.maximalIdeal A)
      (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing
      (ModuleCat.of A (A ⧸ Ideal.span {f})) 2)) :
    FiniteEtaleColimitFullyFaithful (complementZeroLocus A (IsLocalRing.maximalIdeal A) : Scheme)
        (idealSheafNearVanishing A (Ideal.span {f}) (IsLocalRing.maximalIdeal A)) ∧
      ∀ C : FiniteEtaleOver
        (idealSheafNearVanishing A (Ideal.span {f}) (IsLocalRing.maximalIdeal A)).subscheme,
      ∃ (W : Neighborhood (complementZeroLocus A (IsLocalRing.maximalIdeal A) : Scheme)
          (idealSheafNearVanishing A (Ideal.span {f}) (IsLocalRing.maximalIdeal A)))
        (V : FiniteEtaleOver (Neighborhood.open _ _ W).toScheme),
        Nonempty ((finiteEtaleBaseChange (Neighborhood.toSchemeHom _ _ W)).obj V ≅ C)
```

## Tag 0BLW, a remark

[Tag 0BLW](https://stacks.math.columbia.edu/tag/0BLW) in the Stacks Project.

**`AlgebraicGeometry.finiteEtaleColimitEquivalence_puncturedSpectrum_of_propertySk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompleteFourDimensional.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompleteFourDimensional.lean#L84). The attribute's comment: “the equivalence of the remark, from the tag's own hypotheses: `A` complete local Noetherian, `f ∈ 𝔪` nonzero, `A_f` satisfying `(S₂)`, and every irreducible component of `Spec A` of dimension at least 4; nothing beyond them is assumed”.

> **Stacks Project, Tag 0BLW.**  Let `(A, 𝔪)` be a complete local Noetherian ring and let
> `f ∈ 𝔪` be nonzero.  Assume `A_f` satisfies Serre's condition `(S₂)` and every irreducible
> component of `Spec A` has dimension at least `4`.  Then the restriction functor
>
> ```
> colim_{U₀ ⊆ U' ⊆ U open} FÉt_{U'} ⟶ FÉt_{U₀}
> ```
>
> is an equivalence, where `U = Spec A ∖ {𝔪}` and `U₀ = U ∩ V(f)`.
>
> This is Stacks 0DXY under its hypothesis (2)(a).  Its hypothesis (1) is available: a complete
> local Noetherian ring has a dualizing complex by Stacks 0BFR, and it is `f`-adically complete
> because `f A` is contained in the maximal ideal, with respect to which it is complete.  The
> dimension bound of (2)(a) is on the components of `Spec A` not contained in `V(f)`, so the bound
> on all of them is more than enough.

```lean
theorem finiteEtaleColimitEquivalence_puncturedSpectrum_of_propertySk
    [HasDerivedCategory.{w} (ModuleCat.{u} A)] [IsAdicComplete (maximalIdeal A) A]
    (hf : f ∈ maximalIdeal A) (_hfne : f ≠ 0)
    (hS2 : PropertySkRing (Localization.Away f) 2)
    (hdim : ∀ p : PrimeSpectrum A, IsMinimalPrime p.asIdeal →
      (4 : WithBot ℕ∞) ≤ ringKrullDim (A ⧸ p.asIdeal)) :
    FiniteEtaleColimitFullyFaithful (complementZeroLocus A (maximalIdeal A) : Scheme)
        (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)) ∧
      ∀ C : FiniteEtaleOver
        (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)).subscheme,
      ∃ (W : Neighborhood (complementZeroLocus A (maximalIdeal A) : Scheme)
          (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)))
        (V : FiniteEtaleOver (Neighborhood.open _ _ W).toScheme),
        Nonempty ((finiteEtaleBaseChange (Neighborhood.toSchemeHom _ _ W)).obj V ≅ C)
```

**`AlgebraicGeometry.finiteEtaleColimitEquivalence_puncturedSpectrum_of_isIntegrallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompleteFourDimensional.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/PurityLocalCase/CompleteFourDimensional.lean#L161). The attribute's comment: “the example at the end of the remark: a complete local normal domain of dimension at least 4, with `f ∈ 𝔪` nonzero, satisfies the remark's hypotheses, so the equivalence holds for it; normality is `IsDomain` together with `IsIntegrallyClosed` and nothing beyond the remark's own hypotheses is assumed”.

> **Stacks Project, Tag 0BLW, the example at the end of the remark.**  The hypotheses of
> `AlgebraicGeometry.finiteEtaleColimitEquivalence_puncturedSpectrum_of_propertySk` hold when `A`
> is a complete local normal domain of dimension at least `4` and `f ∈ 𝔪` is nonzero, so the
> restriction functor `colim_{U₀ ⊆ U' ⊆ U} FÉt_{U'} ⟶ FÉt_{U₀}` is an equivalence in that case.
>
> A localization of a normal domain at a set of nonzero elements is again a normal domain, so `A_f`
> and each of its local rings is an integrally closed domain; Serre's criterion then gives `(S₂)`
> for `A_f`.  The only minimal prime of a domain is `(0)`, and `A / (0) = A` has dimension at
> least `4`, which is the dimension bound on the irreducible components of `Spec A`.

```lean
theorem finiteEtaleColimitEquivalence_puncturedSpectrum_of_isIntegrallyClosed
    [HasDerivedCategory.{w} (ModuleCat.{u} A)] [IsAdicComplete (maximalIdeal A) A]
    [IsDomain A] [IsIntegrallyClosed A]
    (hdim : (4 : WithBot ℕ∞) ≤ ringKrullDim A) (hf : f ∈ maximalIdeal A) (hfne : f ≠ 0) :
    FiniteEtaleColimitFullyFaithful (complementZeroLocus A (maximalIdeal A) : Scheme)
        (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)) ∧
      ∀ C : FiniteEtaleOver
        (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)).subscheme,
      ∃ (W : Neighborhood (complementZeroLocus A (maximalIdeal A) : Scheme)
          (idealSheafNearVanishing A (Ideal.span {f}) (maximalIdeal A)))
        (V : FiniteEtaleOver (Neighborhood.open _ _ W).toScheme),
        Nonempty ((finiteEtaleBaseChange (Neighborhood.toSchemeHom _ _ W)).obj V ≅ C)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.23, Tag 0EK7](https://stacks.math.columbia.edu/tag/0EK7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
