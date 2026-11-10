---
declaration: section
origin: cited
lean: Stacks.PuncturedSpectrumPicard.picardColimitSurjective, Stacks.PuncturedSpectrumPicard.exists_isCompatible, Stacks.PuncturedSpectrumPicard.exists_isCompatiblePullback_puncturedSpectrum, Stacks.PuncturedSpectrumPicard.picardColimitSurjective_of_isDualizingComplex, Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre_of_isNoetherianRing, Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre, Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre_of_localCohomology, Stacks.AlgebraicGeometry.PicardBaseChange.injective_schemePullbackClass_puncturedSpectrumCompletionMap
statement: formalized
proof: formalized
---

# 52.27 Invertible modules on punctured spectra, II

Section 52.27 of the Stacks Project, [Tag 0F2C](https://stacks.math.columbia.edu/tag/0F2C). 8 tags here are carried by 38 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F2D, a lemma

[Tag 0F2D](https://stacks.math.columbia.edu/tag/0F2D) in the Stacks Project.

**`Stacks.PuncturedSpectrumPicard.picardColimitSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/FormalPicardAlgebraization.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/FormalPicardAlgebraization.lean#L373).

> **[Stacks, Tag 0F2D].** Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪`. Assume
>
> 1. `A` is `f`-adically complete,
> 2. `f` is a nonzerodivisor,
> 3. `H¹_𝔪(A/fA)` and `H²_𝔪(A/fA)` are finite `A`-modules, and
> 4. `H³_𝔪(A/fA) = 0`.
>
> Let `U`, resp. `U₀`, be the punctured spectrum of `A`, resp. of `A/fA`. Then
> `colim_{U₀ ⊆ U' ⊆ U open} Pic(U') ⟶ Pic(U₀)` is surjective: every invertible module on `U₀` is
> the restriction of an invertible module on an open `U'` of `U` containing `U₀`. The conclusion is
> `Stacks.PuncturedSpectrumPicard.PicardColimitSurjective`, the elementwise form of surjectivity
> out of the filtered colimit.
>
> The proof is the source's. A class on `U₀` extends to a compatible family along the
> infinitesimal neighbourhoods `Uₙ = V((f𝒪_U)ⁿ⁺¹)` by [Stacks, Tag 0C6R] and
> `H²(U₀, 𝒪_{U₀}) = H³_𝔪(A/fA) = 0` (`exists_compatible_idealPowerStages`); the representing
> invertible modules, pushed forward to `U`, form a finite locally free object of `Coh(U, f𝒪_U)`
> (`Stacks.Coherent.IdealPowerStageModules`); by [Stacks, Tag 0EKZ] it is the completion of a
> finite locally free `𝒢` on an open `V ⊇ U₀` (`exists_completion_iso_of_eq_situation`); `𝒢`
> restricts to the given module on `U₀`
> (`Stacks.Coherent.IdealPowerStageModules.exists_pullback_iso_of_completion_iso`) and is
> therefore invertible on an open `U' ⊇ U₀` (`exists_opens_isInvertible_of_pullback_iso`).

```lean
theorem picardColimitSurjective [IsNoetherianRing A] (hf : f ∈ maximalIdeal A)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A) (hreg : IsSMulRegular A f)
    (hH1 : Module.Finite A (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 1))
    (hH2 : Module.Finite A (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 2))
    (hvanish3 : IsZero (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 3)) :
    PicardColimitSurjective A f
```

**`Stacks.PuncturedSpectrumPicard.exists_isCompatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/FormalTower.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/FormalTower.lean#L190). The attribute's comment: “the first half of the source's proof, in the generality the argument has: for a tower of first-order thickenings whose ideal sheaves have vanishing H², every Picard class on the bottom stage extends to a compatible family along the whole tower. That is the source's step `Pic(U_{n+1}) → Pic(U_n) → H²(U₀,𝒪_{U₀}) = H³_𝔪(A/fA) = 0, therefore each invertible 𝒪_{U₀}-module is restricted from an invertible object of Coh(U,f𝒪_U)`, and the single-stage lift is Stacks 0C6R, Stacks.Thickenings.exact\_picardRestriction in StacksFrontier.AlgebraicGeometry.Thickenings.PicardSequence. The vanishing of H² is a condition on the tower, not every tower satisfying it; for the same half at the punctured spectrum, with that vanishing derived from the source's own hypotheses (2) f a nonzerodivisor and (4) H³\_𝔪(A/fA) = 0, see Stacks.PuncturedSpectrumPicard.exists\_isCompatiblePullback\_puncturedSpectrum. NOT covered by this declaration: the tag's own conclusion, surjectivity of colim\_\{U₀ ⊆ U' ⊆ U} Pic(U') → Pic(U₀), written as Stacks.PuncturedSpectrumPicard.PicardColimitSurjective, which needs Stacks 0EKZ and through it Stacks 0EIR part (2)”.

> **The first half of the proof of [Stacks, Tag 0F2D].**  Let `X₀ ⟶ X₁ ⟶ X₂ ⟶ ⋯` be a tower of
> first-order thickenings in which the ideal sheaf of every stage has vanishing second cohomology.
> Then every Picard class on the bottom stage extends to a compatible family of Picard classes
> along the whole tower.
>
> This is the step the source writes as "this gives an exact sequence
> `Pic(U_{n+1}) → Pic(U_n) → H²(U₀, 𝒪_{U₀}) = H³_𝔪(A/fA) = 0`.  Therefore each invertible
> `𝒪_{U₀}`-module is restricted from an invertible object of `Coh(U, f𝒪_U)`."  Each single lift is
> `surjective_picardRestriction_of_forall_eq_zero`, and the family is assembled by recursion on the
> stage, choosing a lift at each step.
>
> What remains of the tag after this is [Stacks, Tag 0EKZ], which descends the formal object so
> obtained to an invertible module on an open `U'` with `U₀ ⊆ U' ⊆ U`; see
> `Stacks.PuncturedSpectrumPicard.PicardColimitSurjective` for the conclusion that needs it.

```lean
theorem exists_isCompatible
    (h2 : ∀ n, ∀ x : CategoryTheory.Sheaf.H.{u}
      (Stacks.Thickenings.idealAddSheafOnSub (T.hom n)) 2, x = 0)
    (c₀ : Pic (T.obj 0)) :
    ∃ c : (n : ℕ) → Pic (T.obj n), c 0 = c₀ ∧ IsCompatible T c
```

**`Stacks.PuncturedSpectrumPicard.exists_isCompatiblePullback_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/PuncturedSpectrumFirstHalf.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/PuncturedSpectrumFirstHalf.lean#L212). The attribute's comment: “the first half of the source's proof at the punctured spectrum itself, under the source's own hypotheses (2) f a nonzerodivisor and (4) H³\_𝔪(A/fA) = 0 and nothing else: every Picard class on U₀ extends to a family along the tower of infinitesimal neighbourhoods of U₀ in U, each the pullback of the next. The per-stage vanishing H²(U\_n's ideal sheaf) = 0 is proved here, not assumed: the layers are identified with 𝒪\_\{U₀} by multiplication by f^\{n+1} (Stacks.Thickenings.idealSheafIsoStructureSheafNthOrderBottom, which is where (2) enters) and H²(U₀,𝒪\_\{U₀}) = 0 is derived from (4). NOT covered: the tag's own conclusion, surjectivity of colim\_\{U₀ ⊆ U' ⊆ U} Pic(U') → Pic(U₀), which is the second half and needs Stacks 0EKZ, hence Stacks 0EIR part (2); hypotheses (1) f-adic completeness and (3) finiteness of H¹\_𝔪(A/fA), H²\_𝔪(A/fA) are inputs of that half alone and do not appear here”.

> **The first half of the proof of [Stacks, Tag 0F2D].** Let `(A, 𝔪)` be a Noetherian local
> ring and let `f ∈ 𝔪` be a nonzerodivisor with `H³_𝔪(A/fA) = 0`. Then every Picard class on the
> bottom stage of the tower of infinitesimal neighbourhoods of `U₀` in the punctured spectrum `U`
> extends to a family of classes along the whole tower, each the pullback of the next.
>
> Only hypotheses (2) and (4) of the tag are used. The tower is
> `Stacks.PuncturedSpectrumPicard.infinitesimalTower` of
> `Stacks.PuncturedSpectrumPicard.puncturedPrincipalImmersion`, the layers are all `𝒪_{U₀}` because
> `f` is a nonzerodivisor generating the ideal sheaf on every chart, and the single-stage lift is
> the exact sequence of [Stacks, Tag 0C6R].

```lean
theorem exists_isCompatiblePullback_puncturedSpectrum [IsNoetherianRing A]
    (hf : f ∈ maximalIdeal A) (hreg : IsSMulRegular A f)
    (hvanish3 : IsZero (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 3))
    (c₀ : Stacks.Picard.ofScheme
      (nthOrderInfinitesimalNeighbourhood (puncturedPrincipalImmersion A f) 0)) :
    ∃ c : (n : ℕ) → Stacks.Picard.ofScheme
        ((infinitesimalTower (puncturedPrincipalImmersion A f)).obj n),
      c 0 = c₀ ∧
        IsCompatiblePullback (infinitesimalTower (puncturedPrincipalImmersion A f)) c
```

## Tag 0F2E, a remark

[Tag 0F2E](https://stacks.math.columbia.edu/tag/0F2E) in the Stacks Project.

**`Stacks.PuncturedSpectrumPicard.picardColimitSurjective_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/DualizingPicardAlgebraization.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/DualizingPicardAlgebraization.lean#L85). The attribute's comment: “the whole remark: under (1)-(5) the conclusion of 0F2D holds; points (a) and (b) are commentary with no mathematical claim”.

> **[Stacks, Tag 0F2E].** Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪`. Assume
>
> 1. `A` has a dualizing complex,
> 2. `A` is `f`-adically complete,
> 3. `f` is a nonzerodivisor,
> 4. one of the following is true
>    * (a) `A_f` is `(S₂)` and for `𝔭 ⊂ A`, `f ∉ 𝔭` minimal we have `dim(A/𝔭) ≥ 4`, or
>    * (b) if `𝔭 ∉ V(f)` and `V(𝔭) ∩ V(f) ≠ {𝔪}`, then `depth(A_𝔭) + dim(A/𝔭) > 3`,
> 5. `H³_𝔪(A/fA) = 0`.
>
> Then the conclusion of [Stacks, Tag 0F2D] holds: with `U`, resp. `U₀`, the punctured spectrum of
> `A`, resp. of `A/fA`, the map `colim_{U₀ ⊆ U' ⊆ U open} Pic(U') ⟶ Pic(U₀)` is surjective. As
> for [Stacks, Tag 0F2D] (`Stacks.PuncturedSpectrumPicard.picardColimitSurjective`), the conclusion
> is `Stacks.PuncturedSpectrumPicard.PicardColimitSurjective`, the elementwise form of surjectivity
> out of the filtered colimit: every invertible module on `U₀` is the restriction of an invertible
> module on an open `U'` of `U` containing `U₀`.
>
> Hypothesis (4a) reads "`A_f` is `(S₂)`" as `PropertySkRing (Localization.Away f) 2`, Serre's
> condition of [Stacks, Tag 031P] for the ring `A_f`; in (4b), `V(f)` is the set of primes
> containing `f`. Hypothesis (1) is read in any model `[HasDerivedCategory (ModuleCat A)]` of the
> derived category; whether a dualizing complex exists does not depend on the model. These are the
> spellings of [Stacks, Tag 0EKY]
> (`Stacks.Algebraization.completionEquivalence_local_principal_finiteLocallyFree`). Hypothesis (5)
> is written, as in [Stacks, Tag 0F2D], in the library's default model, before the model of (1) is
> introduced, so that the two do not interfere.
>
> The proof is the source's: that of [Stacks, Tag 0F2D] with [Stacks, Tag 0EKY] in place of
> [Stacks, Tag 0EKZ]. A class on `U₀` extends along the infinitesimal neighbourhoods of `U₀` by
> [Stacks, Tag 0C6R] and `H²(U₀, 𝒪_{U₀}) = H³_𝔪(A/fA) = 0`, giving an invertible object of
> `Coh(U, f𝒪_U)`; by the essential surjectivity of [Stacks, Tag 0EKY] it is the completion of a
> finite locally free module on an open `V ⊇ U₀`, which is invertible near `U₀`
> (`Stacks.PuncturedSpectrumPicard.picardColimitSurjective_of_forall_isCompletionNearClosed`).

```lean
theorem picardColimitSurjective_of_isDualizingComplex [IsNoetherianRing A]
    (hf : f ∈ maximalIdeal A)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A) (hreg : IsSMulRegular A f)
    (hvanish3 : IsZero (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 3))
    [HasDerivedCategory.{w} (ModuleCat.{u} A)]
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
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
    PicardColimitSurjective A f
```

## Tag 0F2F, a lemma

[Tag 0F2F](https://stacks.math.columbia.edu/tag/0F2F) in the Stacks Project.

**`Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/ExtensionAcrossPoint.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/ExtensionAcrossPoint.lean#L533). The attribute's comment: “GRANTED, and not proved here, ONE input: h0F2D, the conclusion of Stacks 0F2D for (A,f), carried as Stacks.PuncturedSpectrumPicard.PicardColimitSurjective — the predicate the restricted 0F2D of StacksFrontier.AlgebraicGeometry.PuncturedSpectrumPicard.FormalTower states unproved and explicitly disclaims, so that tag's restriction is inherited here. The source's other input, `By Limits, Lemma 0F21 applied n times`, is NO LONGER granted: the one-point step is proved as Stacks.PuncturedSpectrumPicard.picardExtendsAcrossPoint and supplied here. Clause (2) of the source is h2, transcribed with the two standard identifications performed in the statement: a maximal ideal of A\_f is a prime 𝔭 of A with f ∉ 𝔭 maximal among such, and (A\_f)\_𝔭 = A\_𝔭 = Localization.AtPrime 𝔭”.

> **Stacks 0F2F, with the one-point extension step discharged.**  Surjectivity of
> `Pic(U) ⟶ Pic(U₀)` for the punctured spectrum `U` of a Noetherian local ring `A` and the
> punctured spectrum `U₀` of `A/fA`.
>
> This is `Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre`
> with its `hstep` hypothesis supplied by `picardExtendsAcrossPoint`, so the only input still
> granted is the conclusion of [Stacks, Tag 0F2D].

```lean
theorem surjective_schemePullbackClass_puncturedClosedFibre_of_isNoetherianRing
    (hf : f ∈ maximalIdeal A) (h0F2D : PicardColimitSurjective A f)
    (h2 : ∀ p : PrimeSpectrum A, f ∉ p.asIdeal →
      (∀ q : PrimeSpectrum A, p.asIdeal < q.asIdeal → f ∈ q.asIdeal) →
      Subsingleton (Stacks.Picard.ofScheme
        (Stacks.Divisors.puncturedSpectrum (Localization.AtPrime p.asIdeal)).toScheme)) :
    Function.Surjective (Stacks.Picard.schemePullbackClass
      (morphismRestrict (Stacks.Algebraization.closedImmersion A f)
        (Stacks.Divisors.puncturedSpectrum A)))
```

**`Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/ExtensionToPuncturedSpectrum.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/ExtensionToPuncturedSpectrum.lean#L527). The attribute's comment: “GRANTED, and NOT proved anywhere in this file, two inputs, both carried as hypotheses: (i) h0F2D, the conclusion of Stacks 0F2D for (A,f), which is clause (1) `the conditions of Lemma 0F2D hold` of the source read through that lemma's conclusion — it is Stacks.PuncturedSpectrumPicard.PicardColimitSurjective, the predicate the restricted 0F2D of StacksFrontier.AlgebraicGeometry.PuncturedSpectrumPicard.FormalTower states unproved and explicitly disclaims, so the restriction of that tag is inherited here; and (ii) hstep, Stacks.PuncturedSpectrumPicard.PicardExtendsAcrossPoint, the extension of an invertible module across ONE point 𝔭 of ONE open of Spec A whose local ring has punctured spectrum with trivial Picard group — the source's `By Limits, Lemma 0F21 applied n times` for a single n, which needs the Pic-versus-FinitePresentationModules translation and the identification of 𝒪\_\{Spec A,𝔭} with A\_𝔭 before Stacks 0F21 (proved here as AlgebraicGeometry.GlueingNearPoint.moduleGlueingEquivalenceNearClosedPoint) can discharge it. PROVED here, from those two: everything else in the source's proof — that U ∖ U' lies in D(f), is FINITE, and consists of points closed in U and maximal in A\_f (the source's `points corresponding to prime ideals 𝔭₁,…,𝔭ₙ as in (2)`), and the induction applying the one-point step n times. Clause (2) of the source is hypothesis h2, transcribed with the two standard identifications performed in the statement: a maximal ideal of A\_f is a prime 𝔭 of A with f ∉ 𝔭 maximal among such, and (A\_f)\_𝔭 = A\_𝔭 = Localization.AtPrime 𝔭”.

> **[Stacks, Tag 0F2F].**  Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪`.  Write `U` for
> the punctured spectrum of `A` and `U₀` for the punctured closed fibre.  Granted the conclusion of
> [Stacks, Tag 0F2D] for `(A, f)` and the one-point extension step
> `PicardExtendsAcrossPoint`, and assuming that every maximal ideal `𝔭` of `A_f` has
> `Pic` of the punctured spectrum of `A_𝔭` trivial, restriction `Pic(U) → Pic(U₀)` is surjective.
>
> A class on `U₀` comes, by [Stacks, Tag 0F2D], from a class on some open `U₀ ⊆ U' ⊆ U`.  The
> exceptional set `U ∖ U'` is finite and consists of points closed in `U` and maximal in `A_f`
> (`finite_exceptionalPoints`, `isOpen_puncturedSpectrum_sdiff_singleton`,
> `eq_closedPoint_of_lt_of_mem_exceptionalPoints`), so the class extends across those points one at a
> time by `surjective_schemePullbackClass_homOfLE_of_finite`.

```lean
theorem surjective_schemePullbackClass_puncturedClosedFibre (hf : f ∈ maximalIdeal A)
    (hstep : PicardExtendsAcrossPoint A) (h0F2D : PicardColimitSurjective A f)
    (h2 : ∀ p : PrimeSpectrum A, f ∉ p.asIdeal →
      (∀ q : PrimeSpectrum A, p.asIdeal < q.asIdeal → f ∈ q.asIdeal) →
      Subsingleton (Stacks.Picard.ofScheme
        (Stacks.Divisors.puncturedSpectrum (Localization.AtPrime p.asIdeal)).toScheme)) :
    Function.Surjective (Stacks.Picard.schemePullbackClass
      (morphismRestrict (Stacks.Algebraization.closedImmersion A f)
        (Stacks.Divisors.puncturedSpectrum A)))
```

**`Stacks.PuncturedSpectrumPicard.surjective_schemePullbackClass_puncturedClosedFibre_of_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/PicardSurjectivePuncturedSpectrum.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/PicardSurjectivePuncturedSpectrum.lean#L123). The attribute's comment: “the full statement: under the four conditions of Stacks 0F2D (f-adic completeness, f a nonzerodivisor, finiteness of H^1\_m(A/fA) and H^2\_m(A/fA), vanishing of H^3\_m(A/fA)) and triviality of Pic of the punctured spectrum of (A\_f)\_P for every maximal ideal P of A\_f, restriction Pic(U) -> Pic(U\_0) is surjective”.

> **[Stacks, Tag 0F2F].**  Let `(A, 𝔪)` be a Noetherian local ring and `f ∈ 𝔪`.  Assume
> (1) the conditions of [Stacks, Tag 0F2D]: `A` is `f`-adically complete, `f` is a nonzerodivisor,
> `H¹_𝔪(A/fA)` and `H²_𝔪(A/fA)` are finite `A`-modules and `H³_𝔪(A/fA) = 0`; and (2) for every
> maximal ideal `𝔓` of `A_f` the punctured spectrum of `(A_f)_𝔓` has trivial Picard group.  Let `U`,
> resp. `U₀`, be the punctured spectrum of `A`, resp. `A/fA`.  Then `Pic(U) → Pic(U₀)` is
> surjective.
>
> A class on `U₀` comes from a class on an open `U₀ ⊆ U' ⊆ U` by [Stacks, Tag 0F2D]
> (`picardColimitSurjective`); the complement `U ∖ U'` is a finite set of points that are maximal
> ideals of `A_f`, and the class extends across each of them by [Stacks, Tag 0F21]
> (`surjective_schemePullbackClass_puncturedClosedFibre_of_isNoetherianRing`), hypothesis (2)
> being read at those points by `subsingleton_picard_localizationAtPrime_of_away`.
>
> `U₀` is `Stacks.Algebraization.puncturedClosedFibre A f`, the part of `Spec(A/fA)` over `U`,
> which is the punctured spectrum of `A/fA`
> (`Stacks.PuncturedSpectrumPicard.puncturedClosedFibre_eq_puncturedSpectrum_quotient`).

```lean
theorem surjective_schemePullbackClass_puncturedClosedFibre_of_localCohomology
    [IsLocalRing A] [IsNoetherianRing A] (hf : f ∈ maximalIdeal A)
    (hcomplete : IsAdicComplete (Ideal.span {f}) A) (hreg : IsSMulRegular A f)
    (hH1 : Module.Finite A (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 1))
    (hH2 : Module.Finite A (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 2))
    (hvanish3 : IsZero (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
      {closedPoint A} ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
        (ModuleCat.of A (A ⧸ Ideal.span {f}))) 3))
    (h2 : ∀ (P : Ideal (Localization.Away f)) [P.IsMaximal],
      Subsingleton (Stacks.Picard.ofScheme
        (Stacks.Divisors.puncturedSpectrum (Localization.AtPrime P)).toScheme)) :
    Function.Surjective (Stacks.Picard.schemePullbackClass
      (morphismRestrict (Stacks.Algebraization.closedImmersion A f)
        (Stacks.Divisors.puncturedSpectrum A)))
```

## Tag 0F2G, a lemma

[Tag 0F2G](https://stacks.math.columbia.edu/tag/0F2G) in the Stacks Project.

**`Stacks.AlgebraicGeometry.PicardBaseChange.injective_schemePullbackClass_puncturedSpectrumCompletionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardBaseChange/PuncturedSpectrumCompletion.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardBaseChange/PuncturedSpectrumCompletion.lean#L393).

> **Stacks Project, Tag 0F2G.** Let `(A, 𝔪)` be a Noetherian local ring of depth at least two,
> let `A^` be its completion and let `U`, resp. `U^`, be the punctured spectrum of `A`, resp. `A^`.
> Then `Pic(U) ⟶ Pic(U^)` is injective.

```lean
theorem injective_schemePullbackClass_puncturedSpectrumCompletionMap
    (hdepth : 2 ≤ Module.depth A (maximalIdeal A) A) :
    Function.Injective
      (Stacks.Picard.schemePullbackClass (puncturedSpectrumCompletionMap A))
```

## Tag 0F2H, a lemma

[Tag 0F2H](https://stacks.math.columbia.edu/tag/0F2H) in the Stacks Project.

**`Stacks.PicardUFD.subsingleton_picardGroup_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardGroup/PuncturedSpectrumRegular.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PicardGroup/PuncturedSpectrumRegular.lean#L57). References: SGA 2 XI (3.13), “XI.3.13(i)”.

> **Stacks Project, Tag 0F2H.** Let `(A, 𝔪)` be a regular local ring. Then the Picard group of
> the punctured spectrum `Spec A ∖ {𝔪}` of `A` is trivial.

```lean
theorem subsingleton_picardGroup_puncturedSpectrum (A : Type u) [CommRing A]
    [IsRegularLocalRing A] :
    Subsingleton (Stacks.Divisors.puncturedSpectrum A).toScheme.picardGroup
```

## Tag 0F2I, a proposition

[Tag 0F2I](https://stacks.math.columbia.edu/tag/0F2I) in the Stacks Project.

**`Stacks.PuncturedSpectrumPicard.subsingleton_picardGroup_puncturedSpectrum_of_isCompleteIntersectionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/CompleteIntersection.lean, line 687](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/CompleteIntersection.lean#L687). The attribute's comment: “GRANTED, not proved here: h0F2D, the conclusion of Stacks 0F2D as PicardColimitSurjective, under that tag's conditions (1), (2) and its footnote's depth bound”.

> **[Stacks, Tag 0F2I].** Let `(A, 𝔪)` be a Noetherian local ring.  If `A` is a complete
> intersection of dimension at least four, then the Picard group of the punctured spectrum
> `U = Spec A ∖ {𝔪}` of `A` is trivial.
>
> Granted, and not proved anywhere in this library, is the conclusion of [Stacks, Tag 0F2D]: it is
> carried as the hypothesis `h0F2D`, phrased with the library's own
> `Stacks.PuncturedSpectrumPicard.PicardColimitSurjective` and quantified over the Noetherian local
> rings `B` that are `𝔪`-adically complete, the elements `g ∈ 𝔪_B` that are nonzerodivisors, and
> the bound `5 ≤ depth(B)`.  Completeness and the nonzerodivisor clause are conditions (1) and (2)
> of the source's [Stacks, Tag 0F2D], and the depth bound is that tag's own footnote, "(3) and (4)
> hold if `depth(A/fA) ≥ 4`, or equivalently `depth(A) ≥ 5`", which covers its remaining conditions
> (3) and (4).  So `h0F2D` asserts no more than [Stacks, Tag 0F2D] does, and a proof of that tag
> discharges it.
>
> The induction applies it exactly to the intermediate quotients `A' = B/(f₁, …, f_{r-1})` of the
> source's presentation: all are complete because the presenting ring is, and all have
> `depth(A') = dim(A') = dim(A) + 1 ≥ 5` because a quotient of a regular local ring by a regular
> sequence is Cohen-Macaulay.

```lean
theorem subsingleton_picardGroup_puncturedSpectrum_of_isCompleteIntersectionRing
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (h0F2D : ∀ (B : Type u) [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
      [IsAdicComplete (maximalIdeal B) B] (g : B), g ∈ maximalIdeal B →
      g ∈ nonZeroDivisors B → 5 ≤ Module.depth B (maximalIdeal B) B →
      PicardColimitSurjective B g)
    (hA : LocalCompleteIntersection.IsCompleteIntersectionRing A)
    (hdim : 4 ≤ ringKrullDim A) :
    Subsingleton (Stacks.Divisors.puncturedSpectrum A).toScheme.picardGroup
```

**`Stacks.PuncturedSpectrumPicard.subsingleton_picardGroup_puncturedSpectrum_of_completeIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/CompleteIntersectionPicardTrivial.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/CompleteIntersectionPicardTrivial.lean#L115). References: SGA 2 XI (3.13), “XI.3.13(ii)”; SGA 2 XII (4.9), “4.9 b)”.

> Let `(A, 𝔪)` be a Noetherian local ring. If `A` is a complete intersection of dimension at
> least four, then the Picard group of the punctured spectrum `U = Spec A ∖ {𝔪}` of `A` is
> trivial.

```lean
theorem subsingleton_picardGroup_puncturedSpectrum_of_completeIntersection
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : LocalCompleteIntersection.IsCompleteIntersectionRing A)
    (hdim : 4 ≤ ringKrullDim A) :
    Subsingleton (Stacks.Divisors.puncturedSpectrum A).toScheme.picardGroup
```

## Tag 0F2J, an example

[Tag 0F2J](https://stacks.math.columbia.edu/tag/0F2J) in the Stacks Project.

**`Stacks.PuncturedSpectrumPicard.QuadricCone.hypersurface`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L120). The attribute's comment: “the hypersurface”.

> The complete local hypersurface cut out by the determinant equation.

```lean
public abbrev hypersurface (k : Type u) [Field k]
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.coordinateIdeal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L129). The attribute's comment: “the ideal (x,z)”.

> The ideal generated by the first and third coordinates.

```lean
public abbrev coordinateIdeal (k : Type u) [Field k] : Ideal (hypersurface k)
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.hypersurface_isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L217). The attribute's comment: “local ring”.

> The ring `k⟦x,y,z,w⟧/(xy - zw)` is a local ring.

```lean
public theorem hypersurface_isLocalRing (k : Type u) [Field k] :
    IsLocalRing (hypersurface k)
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.hypersurface_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L225). The attribute's comment: “Noetherian ring”.

> The ring `k⟦x,y,z,w⟧/(xy - zw)` is Noetherian.

```lean
public theorem hypersurface_isNoetherianRing (k : Type u) [Field k] :
    IsNoetherianRing (hypersurface k)
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.hypersurface_isCompleteIntersectionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L366). The attribute's comment: “complete intersection”.

> The ring `k⟦x,y,z,w⟧/(xy - zw)` is a complete intersection ring.

```lean
public theorem hypersurface_isCompleteIntersectionRing (k : Type u) [Field k] :
    LocalCompleteIntersection.IsCompleteIntersectionRing (hypersurface k)
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.hypersurface_krullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L421). The attribute's comment: “dimension three”.

> The ring `k⟦x,y,z,w⟧/(xy - zw)` has Krull dimension three.

```lean
public theorem hypersurface_krullDim (k : Type u) [Field k] :
    ringKrullDim (hypersurface k) = 3
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.coordinateIdeal_not_principal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L537). The attribute's comment: “nonprincipal ideal”.

> The ideal `(x,z)` of `k⟦x,y,z,w⟧/(xy - zw)` is not generated by a single element.

```lean
public theorem coordinateIdeal_not_principal (k : Type u) [Field k] :
    ¬ ∃ a : hypersurface k, coordinateIdeal k = Ideal.span ({a} : Set (hypersurface k))
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.quotient_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L581). The attribute's comment: “quotient depth”.

> The quotient of `A = k⟦x,y,z,w⟧/(xy - zw)` by the ideal `(x,z)` has depth two as an
> `A`-module, along the maximal ideal of `A`.

```lean
public theorem quotient_depth (k : Type u) [Field k] :
    Module.depth (hypersurface k) (IsLocalRing.maximalIdeal (hypersurface k))
      (hypersurface k ⧸ coordinateIdeal k) = 2
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.coordinateIdeal_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L637). The attribute's comment: “ideal depth”.

> The ideal `(x,z)` of `A = k⟦x,y,z,w⟧/(xy - zw)` has depth three as an `A`-module, along
> the maximal ideal of `A`.

```lean
public theorem coordinateIdeal_depth (k : Type u) [Field k] :
    Module.depth (hypersurface k) (IsLocalRing.maximalIdeal (hypersurface k))
      (coordinateIdeal k) = 3
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.negativeTwist_not_trivial'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L1164). The attribute's comment: “nontrivial line bundle”.

> The sheaf `𝒪_U(-D) = ℐ_D` on the punctured spectrum `U` of `A = k⟦x,y,z,w⟧/(xy - zw)`, for
> the divisor `D` cut out by `I = (x,z)`, is not a trivial invertible `𝒪_U`-module.

```lean
public theorem negativeTwist_not_trivial' (k : Type u) [Field k] :
    ¬ Stacks.SheafOfModules.IsTrivial
        (Stacks.Divisors.puncturedSpectrum (hypersurface k)).toScheme.presheaf
        (Stacks.Divisors.puncturedSpectrum (hypersurface k)).toScheme.ringCatIsSheaf
        (Stacks.Divisors.negativeTwist' (cartierDivisor k))
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.picardGroup_not_subsingleton'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 1205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L1205). The attribute's comment: “the conclusion: Pic(U) is nontrivial, at the same Scheme.picardGroup that Stacks 0F2I is stated at, so this is literally the negation of that proposition's conclusion for this A”.

> The Picard group `AlgebraicGeometry.Scheme.picardGroup` of the punctured spectrum
> `U = Spec A ∖ {𝔪}` of `A = k⟦x,y,z,w⟧/(xy - zw)` is nontrivial.

```lean
public theorem picardGroup_not_subsingleton' (k : Type u) [Field k] :
    ¬ Subsingleton
      (Stacks.Divisors.puncturedSpectrum (hypersurface k)).toScheme.picardGroup
```

**`Stacks.PuncturedSpectrumPicard.QuadricCone.dimension_bound_isSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean, line 1228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/QuadricConeExample.lean#L1228).

> *The dimension bound in [Stacks, Tag 0F2I] is sharp.*  For every
> field `k` the ring `A = k⟦x,y,z,w⟧/(xy - zw)` is a Noetherian local complete intersection of
> dimension exactly three — so it satisfies every hypothesis of [Stacks, Tag 0F2I] except
> `dim A ≥ 4` — and the Picard group of its punctured spectrum is nontrivial.

```lean
public theorem dimension_bound_isSharp (k : Type u) [Field k] :
    IsNoetherianRing (hypersurface k) ∧ IsLocalRing (hypersurface k) ∧
      LocalCompleteIntersection.IsCompleteIntersectionRing (hypersurface k) ∧
      ringKrullDim (hypersurface k) = 3 ∧
      ¬ Subsingleton
        (Stacks.Divisors.puncturedSpectrum (hypersurface k)).toScheme.picardGroup
```

## Tag 0F9L, an example

[Tag 0F9L](https://stacks.math.columbia.edu/tag/0F9L) in the Stacks Project.

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.exists_puncturedSpectrum_firstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/PicardGroup.lean, line 635](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/PicardGroup.lean#L635). The attribute's comment: “the punctured spectra: reduction modulo w is a first-order thickening U₀ ⟶ U over Spec of the reduction, invertible global functions lift along it, and its ideal sheaf pulled back to U₀ is the structure sheaf of U₀”.

> **[Stacks, Tag 0F9L], the punctured spectra.**  Reduction modulo `w` is a first-order
> thickening `i : U₀ ⟶ U` of the punctured spectrum of `A₀` inside that of `A`, lying over
> `Spec` of the reduction `q : A → A₀`; every invertible global function on `U₀` is the
> restriction of one on `U`; and the ideal sheaf of `i`, pulled back to `U₀`, is the structure
> sheaf of `U₀`.
>
> These are the source's three geometric inputs.  The thickening is `A = A₀[w]/(w²)` read on
> spectra and restricted to the punctured spectra; the lifting of units is the section `ι` of `q`
> together with `Γ(U₀, 𝒪_{U₀}) = A₀`; and the identification of the ideal sheaf is multiplication
> by `w`, which carries `A₀` isomorphically onto the kernel `wA` of `q`.

```lean
public theorem exists_puncturedSpectrum_firstOrderThickening (k : Type u) [Field k] :
    ∃ (q : exampleRing k →+* intermediateRing k)
      (i : (Stacks.Divisors.puncturedSpectrum (intermediateRing k)).toScheme ⟶
        (Stacks.Divisors.puncturedSpectrum (exampleRing k)).toScheme)
      (_ : Stacks.Thickenings.IsFirstOrderThickening i),
      (∀ p : powerSeriesRing k 8,
        q (Ideal.Quotient.mk (eightVariableIdeal k) p) =
          Ideal.Quotient.mk (sevenVariableIdeal k) (MvPowerSeries.killCompl sevenToEight p)) ∧
      i ≫ (Stacks.Divisors.puncturedSpectrum (exampleRing k)).ι =
        (Stacks.Divisors.puncturedSpectrum (intermediateRing k)).ι ≫
          Spec.map (CommRingCat.ofHom q) ∧
      Function.Surjective (Stacks.Thickenings.unitsToSubCohomology i 0) ∧
      Nonempty ((SheafOfModules.toSheaf
        (Stacks.Divisors.puncturedSpectrum (intermediateRing k)).toScheme.ringCatSheaf).obj
          (SheafOfModules.unit
            (Stacks.Divisors.puncturedSpectrum (intermediateRing k)).toScheme.ringCatSheaf) ≅
        Stacks.Thickenings.idealAddSheafOnSub i)
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.exampleRing_scheme_picardGroup_puncturedSpectrum_not_subsingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/PicardGroup.lean, line 773](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/PicardGroup.lean#L773). The attribute's comment: “the conclusion: the Picard group of the punctured spectrum is nontrivial, at the same Scheme.picardGroup that Stacks 0F2I is stated at, so this is literally the negation of that proposition's conclusion for this A”.

> **[Stacks, Tag 0F9L], the conclusion.** The Picard group of the punctured spectrum
> `U = Spec A ∖ {𝔪}` of
> `A = k⟦a,b,x,y,z,u,v,w⟧/(a³, b³, xa² + yab + zb², w²)`
> is nontrivial.  Together with `powerSeriesRing_isRegularLocalRing` and
> `powerSeriesRing_dimension` — the ambient ring `B = k⟦a,b,x,y,z,u,v,w⟧` is regular of
> dimension `8`, and `A = B/(f₁, f₂, f₃, f₄)` with `r = 4`, so `dim B - r = 4 ≥ 4` — this is
> the source's witness that [Stacks, Tag 0F2I] fails without the hypothesis that
> `f₁, …, f_r` be a regular sequence.
>
> The Picard group is `AlgebraicGeometry.Scheme.picardGroup`, the same one [Stacks, Tag 0F2I]
> and the companion example
> `Stacks.PuncturedSpectrumPicard.QuadricCone.picardGroup_not_subsingleton'` are stated at, so
> this is literally the negation of that proposition's conclusion for this `A`.
>
> The argument itself runs in the universe-shrunk model of Tag 040B, where the exact sequence of
> [Stacks, Tag 0C6R] lives: it is
> `exampleRing_picardGroup_puncturedSpectrum_not_subsingleton'`, carried here across
> `Stacks.SheafOfModules.picardGroupShrinkAddEquiv`, the isomorphism of abelian groups between
> the two models.

```lean
public theorem exampleRing_scheme_picardGroup_puncturedSpectrum_not_subsingleton
    (k : Type u) [Field k] :
    ¬ Subsingleton
      (Stacks.Divisors.puncturedSpectrum (exampleRing k)).toScheme.picardGroup
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.socleRing_nontrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L116). The attribute's comment: “nontrivial five-variable quotient”.

> **Stacks 0F9L** (nontrivial five-variable quotient).
> The ring `A₁ = k⟦a,b,x,y,z⟧/(a³, b³, xa² + yab + zb²)` is nonzero.

```lean
public theorem socleRing_nontrivial (k : Type u) [Field k] :
    Nontrivial (socleRing k)
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.intermediateRing_nontrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L144). The attribute's comment: “nontrivial seven-variable quotient”.

> **Stacks 0F9L** (nontrivial seven-variable quotient).
> The ring `A₀ = k⟦a,b,x,y,z,u,v⟧/(a³, b³, xa² + yab + zb²)` is nonzero.

```lean
public theorem intermediateRing_nontrivial (k : Type u) [Field k] :
    Nontrivial (intermediateRing k)
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.exampleRing_nontrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L172). The attribute's comment: “nontrivial eight-variable quotient”.

> **Stacks 0F9L** (nontrivial eight-variable quotient).
> The ring `A = k⟦a,b,x,y,z,u,v,w⟧/(a³, b³, xa² + yab + zb², w²)` is nonzero.

```lean
public theorem exampleRing_nontrivial (k : Type u) [Field k] :
    Nontrivial (exampleRing k)
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.socleElement_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L190). The attribute's comment: “nonzero socle element”.

> **Stacks 0F9L** (nonzero socle element).
> The class of `a²b²` in `A₁ = k⟦a,b,x,y,z⟧/(a³, b³, xa² + yab + zb²)` is nonzero.

```lean
public theorem socleElement_ne_zero (k : Type u) [Field k] :
    socleElement k ≠ 0
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.socleElement_mul_variable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L288). The attribute's comment: “socle element annihilated by all five variables”.

> **Stacks 0F9L** (socle element annihilated by all five variables).
> The class of `a²b²` in `A₁ = k⟦a,b,x,y,z⟧/(a³, b³, xa² + yab + zb²)` is killed by each of
> the five variables `a, b, x, y, z`.

```lean
public theorem socleElement_mul_variable (k : Type u) [Field k] (i : Fin 5) :
    socleElement k * Ideal.Quotient.mk (fiveVariableIdeal k) (MvPowerSeries.X i) = 0
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.socleRing_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L340). The attribute's comment: “depth of the five-variable quotient”.

> **Stacks 0F9L** (depth of the five-variable quotient).
> The ring `A₁ = k⟦a,b,x,y,z⟧/(a³, b³, xa² + yab + zb²)` has depth `0` along its maximal
> ideal.

```lean
public theorem socleRing_depth (k : Type u) [Field k] :
    Module.depth (socleRing k) (IsLocalRing.maximalIdeal (socleRing k))
      (socleRing k) = 0
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.intermediateRing_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L517). The attribute's comment: “depth of the seven-variable quotient”.

> **Stacks 0F9L** (depth of the seven-variable quotient).
> The ring `A₀ = k⟦a,b,x,y,z,u,v⟧/(a³, b³, xa² + yab + zb²)` has depth `2` along its maximal
> ideal.

```lean
public theorem intermediateRing_depth (k : Type u) [Field k] :
    Module.depth (intermediateRing k) (IsLocalRing.maximalIdeal (intermediateRing k))
      (intermediateRing k) = 2
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.powerSeriesRing_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L529). The attribute's comment: “regular ambient ring”.

> The ambient power-series ring is regular.

```lean
public theorem powerSeriesRing_isRegularLocalRing (k : Type u) [Field k] :
    IsRegularLocalRing (powerSeriesRing k 8)
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.powerSeriesRing_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/Rings.lean#L541). The attribute's comment: “dimension of the ambient ring”.

> **Stacks 0F9L** (dimension of the ambient ring).
> The power-series ring `k⟦a,b,x,y,z,u,v,w⟧` has Krull dimension `8`.

```lean
public theorem powerSeriesRing_dimension (k : Type u) [Field k] :
    ringKrullDim (powerSeriesRing k 8) = 8
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.exampleRing_equiv_truncatedPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean#L666). The attribute's comment: “square-zero extension with its chosen coordinates”.

> The square-zero description, with the inclusion of `A₀` identified with constant
> polynomials and the chosen eighth variable identified with `X`.

```lean
public theorem exampleRing_equiv_truncatedPolynomial (k : Type u) [Field k] :
    ∃ (e : exampleRing k ≃+* truncatedPolynomialRing k)
      (ι : intermediateRing k →+* exampleRing k)
      (q : exampleRing k →+* intermediateRing k),
      (∀ p : powerSeriesRing k 7,
        ι (Ideal.Quotient.mk (sevenVariableIdeal k) p) =
          Ideal.Quotient.mk (eightVariableIdeal k) (MvPowerSeries.rename sevenToEight p)) ∧
      (∀ p : powerSeriesRing k 8,
        q (Ideal.Quotient.mk (eightVariableIdeal k) p) =
          Ideal.Quotient.mk (sevenVariableIdeal k) (MvPowerSeries.killCompl sevenToEight p)) ∧
      (∀ a : intermediateRing k,
        e (ι a) = Ideal.Quotient.mk _ (Polynomial.C a)) ∧
      e (squareZeroCoordinate k) =
        Ideal.Quotient.mk _ (Polynomial.X : Polynomial (intermediateRing k)) ∧
      (∀ a : intermediateRing k, q (ι a) = a) ∧
      q (squareZeroCoordinate k) = 0 ∧
      Function.Injective (fun a : intermediateRing k => squareZeroCoordinate k * ι a) ∧
      Function.Exact
        (fun a : intermediateRing k => squareZeroCoordinate k * ι a)
        q
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.exampleRing_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean#L714). The attribute's comment: “depth of the eight-variable quotient”.

> **Stacks 0F9L** (depth of the eight-variable quotient).
> The ring `A = k⟦a,b,x,y,z,u,v,w⟧/(a³, b³, xa² + yab + zb², w²)` has depth `2` along its
> maximal ideal.

```lean
public theorem exampleRing_depth (k : Type u) [Field k] :
    Module.depth (exampleRing k) (IsLocalRing.maximalIdeal (exampleRing k))
      (exampleRing k) = 2
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.intermediateRing_globalSections_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean, line 786](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean#L786). The attribute's comment: “global functions on the punctured spectrum of A₀”.

> Depth two identifies the global functions on the seven-variable punctured
> spectrum with the original quotient, via the canonical restriction map.

```lean
public theorem intermediateRing_globalSections_puncturedSpectrum (k : Type u) [Field k] :
    let U := Stacks.Divisors.puncturedSpectrum (intermediateRing k)
    Function.Bijective
      (((Scheme.ΓSpecIso (.of (intermediateRing k))).inv ≫ U.ι.appTop).hom)
```

**`Stacks.PuncturedSpectrumPicard.NonRegularSequence.exampleRing_globalSections_puncturedSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean, line 797](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PuncturedSpectrumPicard/NonRegularSequenceExample/SquareZero.lean#L797). The attribute's comment: “global functions on the punctured spectrum of A”.

> The same global-functions identification for the square-zero quotient.

```lean
public theorem exampleRing_globalSections_puncturedSpectrum (k : Type u) [Field k] :
    let U := Stacks.Divisors.puncturedSpectrum (exampleRing k)
    Function.Bijective
      (((Scheme.ΓSpecIso (.of (exampleRing k))).inv ≫ U.ι.appTop).hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.27, Tag 0F2C](https://stacks.math.columbia.edu/tag/0F2C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
