---
declaration: section
origin: cited
lean: Stacks.Algebraization.canonicallyExtends_and_isCompletion_of_depthDim, Stacks.RingTheory.AssociatedPrimes.associatedPrimes_quotient_span_singleton_pow_succ, Stacks.RingTheory.PrincipalDivisorDepth.mem_of_depth_add_ringKrullDim_le_three, Stacks.RingTheory.PrincipalDivisorDepth.exists_mulPowQuotSMulTop_eq_zero_of_depthDimOffDivisor, Stacks.RingTheory.PrincipalDivisorDepth.one_le_depth_localization, Stacks.RingTheory.PrincipalDivisorDepth.two_le_depth_localization_of_depthDimOnDivisor, Stacks.Algebraization.CompleteNormalDomain.one_lt_depth_quotient_add_ringKrullDim_quotient, Stacks.Algebraization.CompleteNormalDomain.three_lt_depth_add_ringKrullDim_quotient
statement: formalized
proof: formalized
---

# 52.20 Algebraization of coherent formal modules, IV

Section 52.20 of the Stacks Project, [Tag 0EHJ](https://stacks.math.columbia.edu/tag/0EHJ). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DXU, a lemma

[Tag 0DXU](https://stacks.math.columbia.edu/tag/0DXU) in the Stacks Project.

**`Stacks.Algebraization.canonicallyExtends_and_isCompletion_of_depthDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalDepthDimensionWhole.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionCriteria/PrincipalDepthDimensionWhole.lean#L151).

> **[Stacks, Tag 0DXU].**  In the situation of [Stacks, Tag 0EHC] let `(ℱₙ)` be an object of
> `Coh(U, I𝒪_U)`.  Assume
>
> 1. `A` is local and `𝔞 = 𝔪` is the maximal ideal,
> 2. `A` has a dualizing complex,
> 3. `I = (f)` is principal for a nonzerodivisor `f`,
> 4. each `ℱₙ` is finite locally free over `𝒪_U/fⁿ𝒪_U`,
> 5. `depth((A/f)_𝔭) + dim(A/𝔭) > 1` for every `𝔭 ∈ V(f)` other than `𝔪`, and
> 6. `depth(A_𝔭) + dim(A/𝔭) > 3` for every `𝔭 ∉ V(f)` with `V(𝔭) ∩ V(f) ≠ {𝔪}`.
>
> Then `(ℱₙ)` extends canonically to `X = Spec(A)`; in particular, if `A` is `I`-adically complete
> then `(ℱₙ)` is the completion of a coherent `𝒪_U`-module.
>
> The proof is the source's.  Conditions (b) and (c) of the Mittag-Leffler criterion
> [Stacks, Tag 0EHH] come from hypotheses (3), (4) and (5); condition (a) is the finite length of
> the image of `H¹(U, ℱₙ) ⟶ H¹(U, ℱ₁)`, which [Stacks, Tag 0BK0] (2) and [Stacks, Tag 0EIR] turn
> into the finite length of the image of `H²_𝔪(Mₙ) ⟶ H²_𝔪(M₁)` for `Mₙ = H⁰(U, ℱₙ)`, and which
> local duality — in the shape that reads a vanishing of `Ext` back as a vanishing of local
> cohomology — reduces to the finite length of the image of
> `Ext^{-2}_A(M₁, ω) ⟶ Ext^{-2}_A(Mₙ, ω)`.  That last statement is where hypotheses (2), (4), (5)
> and (6) are spent, over the localizations `A_𝔮` at the primes `𝔮 ∈ V(f) ∖ {𝔪}`.  The normalized
> dualizing complex the computation needs is produced from hypothesis (2) by
> `Dualizing.exists_isNormalizedDualizingComplex_shift`.

```lean
theorem canonicallyExtends_and_isCompletion_of_depthDim
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A] (ha : S.a = maximalIdeal S.A)
    (omega : DerivedCategory (ModuleCat.{u} S.A))
    (homega : Dualizing.IsDualizingComplex (A := S.A) (K := omega))
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) (f : S.A)
    (hI : S.I = Ideal.span {f}) (hf : f ∈ nonZeroDivisors S.A)
    (hfree : IsFiniteLocallyFreeAdic (idealOnOpen S) F)
    (h5 : DepthDimOnDivisor f) (h6 : DepthDimOffDivisor f) :
    CanonicallyExtends S F ∧
      (IsAdicComplete (Ideal.span {f}) S.A →
        (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage
          (kerComapSystem S F))
```

**`Stacks.RingTheory.AssociatedPrimes.associatedPrimes_quotient_span_singleton_pow_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AssociatedPrime/NonZeroDivisorPowers.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/AssociatedPrime/NonZeroDivisorPowers.lean#L138). The attribute's comment: “the step of the proof asserting that the associated primes of A/fⁿA agree with those of A/fA, for f a nonzerodivisor”.

> **Stacks Project, Tag 0DXU (the associated-primes step).** For a nonzerodivisor `f` of a
> commutative ring `A`, the associated primes of `A ⧸ fⁿ⁺¹A` are those of `A ⧸ fA`.

```lean
theorem associatedPrimes_quotient_span_singleton_pow_succ (hf : f ∈ nonZeroDivisors A) (n : ℕ) :
    associatedPrimes A (A ⧸ Ideal.span {f ^ (n + 1)}) =
      associatedPrimes A (A ⧸ Ideal.span {f})
```

**`Stacks.RingTheory.PrincipalDivisorDepth.mem_of_depth_add_ringKrullDim_le_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean#L264). The attribute's comment: “the step of the proof deducing from hypothesis (6) that a prime below a point of V(f) other than the closed point, whose depth plus dimension is at most 3, contains f — the source's 'condition (6) tells us these primes are contained in V(f)'”.

> **Stacks Project, Tag 0DXU (hypothesis (6) confines the support to `V(f)`).** Let `f` be an
> element of a local ring `A` satisfying hypothesis (6), and let `𝔮` be a prime containing `f` and
> different from the maximal ideal.  Then every prime `𝔭 ⊆ 𝔮` with
> `depth(A_𝔭) + dim(A/𝔭) ≤ 3` contains `f`.
>
> This is the source's "condition (6) tells us these primes are contained in `V(f)`", used twice:
> for `dim(A/𝔮) = 2` with the primes of `depth(A_𝔭) + dim((A/𝔭)_𝔮) ≤ 1` supporting
> `H^{-1}(ω^•_{A_𝔮})`, and for `dim(A/𝔮) = 1` with the primes of
> `depth(A_𝔭) + dim((A/𝔭)_𝔮) ≤ 2` supporting `H^{-2}(ω^•_{A_𝔮})`.  In both cases
> `dim(A/𝔭) = dim((A/𝔭)_𝔮) + dim(A/𝔮)`, so the two support conditions read
> `depth(A_𝔭) + dim(A/𝔭) ≤ 3`, which is the single bound used here; `𝔮` itself is the point of
> `V(𝔭) ∩ V(f)` other than `𝔪` that lets (6) apply.

```lean
theorem mem_of_depth_add_ringKrullDim_le_three [IsLocalRing A] {f : A}
    (h6 : DepthDimOffDivisor f) {q p : PrimeSpectrum A} (hfq : f ∈ q.asIdeal)
    (hqm : q ≠ closedPoint A) (hpq : p.asIdeal ≤ q.asIdeal)
    (hle : (Module.depth A[p] (maximalIdeal A[p]) A[p] : WithBot ℕ∞) +
        ringKrullDim (A ⧸ p.asIdeal) ≤ 3) :
    f ∈ p.asIdeal
```

**`Stacks.RingTheory.PrincipalDivisorDepth.exists_mulPowQuotSMulTop_eq_zero_of_depthDimOffDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean#L336). The attribute's comment: “the step of the proof concluding, for a finite module whose support hypothesis (6) places in V(f), that multiplication by fⁿ from N/fN to N/f^(n+1)N vanishes for all large n — the source's 'thus the desired vanishing for n large enough', in both the dim(A/q) = 2 and the dim(A/q) = 1 case”.

> **Stacks Project, Tag 0DXU (the vanishing for `n` large enough).** Let `f` be an element of
> a local ring `A` satisfying hypothesis (6), let `𝔮` be a prime containing `f` and different from
> the maximal ideal, and let `N` be a finite `A`-module every prime of whose support lies below
> `𝔮` and has `depth(A_𝔭) + dim(A/𝔭) ≤ 3`.  Then the maps `fⁿ : N ⧸ fN → N ⧸ f^{n+1}N` vanish for
> all large `n`.
>
> This is the conclusion of both of the source's two remaining cases.  There `N` is
> `H^{-1}(ω^•_{A_𝔮})` when `dim(A/𝔮) = 2` and `H^{-2}(ω^•_{A_𝔮})` when `dim(A/𝔮) = 1`, each a
> finite module whose support [Stacks, Tag 0DWZ] describes by a depth-plus-dimension bound; the
> hypothesis (6) step `mem_of_depth_add_ringKrullDim_le_three` puts that support inside `V(f)`,
> which makes `f` nilpotent on `N`, and the source's "thus the desired vanishing for `n` large
> enough" is the vanishing below.

```lean
theorem exists_mulPowQuotSMulTop_eq_zero_of_depthDimOffDivisor [IsLocalRing A] {f : A}
    (h6 : DepthDimOffDivisor f) {q : PrimeSpectrum A} (hfq : f ∈ q.asIdeal)
    (hqm : q ≠ closedPoint A) (N : Type u) [AddCommGroup N] [Module A N] [Module.Finite A N]
    (hsupp : ∀ p ∈ Module.support A N, p.asIdeal ≤ q.asIdeal ∧
      (Module.depth A[p] (maximalIdeal A[p]) A[p] : WithBot ℕ∞) +
        ringKrullDim (A ⧸ p.asIdeal) ≤ 3) :
    ∃ c : ℕ, ∀ n, c ≤ n → mulPowQuotSMulTop f N n = 0
```

**`Stacks.RingTheory.PrincipalDivisorDepth.one_le_depth_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean#L416). The attribute's comment: “the step of the proof asserting that A_q has depth at least 1 for a prime q containing the nonzerodivisor f, which is what makes H^0 of the dualizing complex of A_q vanish in the case dim(A/q) = 2”.

> **Stacks Project, Tag 0DXU (`depth(A_𝔮) ≥ 1` because `f` is a nonzerodivisor).** For `f` a
> nonzerodivisor of a Noetherian ring `A` and `𝔮` a prime containing `f`, the local ring `A_𝔮` has
> depth at least one.
>
> This is the source's "`H^0(ω^•_{A_𝔮}) = 0` because `depth(A_𝔮) ≥ 1` as `f` is a
> nonzerodivisor", the input to the case `dim(A/𝔮) = 2`: the image of `f` in `A_𝔮` lies in the
> maximal ideal and is still a nonzerodivisor, so it is a regular sequence of length one, and
> [Stacks, Tag 090R] gives `depth(A_𝔮) = depth(A_𝔮/fA_𝔮) + 1 ≥ 1`.

```lean
theorem one_le_depth_localization [IsNoetherianRing A] {f : A} (hf : f ∈ nonZeroDivisors A)
    {q : PrimeSpectrum A} (hfq : f ∈ q.asIdeal) :
    1 ≤ Module.depth A[q] (maximalIdeal A[q]) A[q]
```

**`Stacks.RingTheory.PrincipalDivisorDepth.two_le_depth_localization_of_depthDimOnDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/PrincipalDivisorDepthDimension.lean#L443). The attribute's comment: “the step of the proof asserting that A_q has depth at least 2 when dim(A/q) = 1, deduced from hypothesis (5) at q together with f being a nonzerodivisor”.

> **Stacks Project, Tag 0DXU (`depth(A_𝔮) ≥ 2` when `dim(A/𝔮) = 1`).** Let `f` be a
> nonzerodivisor of a Noetherian local ring `A` satisfying hypothesis (5), and let `𝔮` be a prime
> containing `f`, different from the maximal ideal, with `dim(A/𝔮) = 1`.  Then `A_𝔮` has depth at
> least two.
>
> This is the source's "if `dim(A/𝔮) = 1`, then condition (5) combined with the fact that `f` is a
> nonzerodivisor insures that `A_𝔮` has depth at least `2`", which is what makes both
> `H^0(ω^•_{A_𝔮})` and `H^{-1}(ω^•_{A_𝔮})` vanish in that case.  Hypothesis (5) at `𝔮` reads
> `depth((A/fA)_𝔮) + 1 > 1`, so `(A/fA)_𝔮 = A_𝔮/fA_𝔮` has depth at least one, and
> [Stacks, Tag 090R] adds the one coming from the nonzerodivisor `f`.

```lean
theorem two_le_depth_localization_of_depthDimOnDivisor [IsNoetherianRing A] [IsLocalRing A]
    {f : A} (hf : f ∈ nonZeroDivisors A) (h5 : DepthDimOnDivisor f) {q : PrimeSpectrum A}
    (hfq : f ∈ q.asIdeal) (hqm : q ≠ closedPoint A)
    (hdim : ringKrullDim (A ⧸ q.asIdeal) = 1) :
    2 ≤ Module.depth A[q] (maximalIdeal A[q]) A[q]
```

## Tag 0DXV, a remark

[Tag 0DXV](https://stacks.math.columbia.edu/tag/0DXV) in the Stacks Project.

**`Stacks.Algebraization.CompleteNormalDomain.one_lt_depth_quotient_add_ringKrullDim_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CompleteNormalDomainDepthConditions.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CompleteNormalDomainDepthConditions.lean#L180). The attribute's comment: “assumption (5) of Lemma 0DXU is satisfied”.

> Let `(A, 𝔪)` be a complete Noetherian normal local domain of dimension at least four and let
> `f ∈ A` be nonzero. Then `depth((A/f)_𝔭) + dim(A/𝔭) > 1` for every prime `𝔭` containing `f` other
> than `𝔪`.

```lean
theorem one_lt_depth_quotient_add_ringKrullDim_quotient (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    [IsDomain A] [IsIntegrallyClosed A] (hdim : (4 : WithBot ℕ∞) ≤ ringKrullDim A)
    (f : A) (hf : f ≠ 0) (p : PrimeSpectrum A) (hfp : f ∈ p.asIdeal)
    (hp : p.asIdeal ≠ IsLocalRing.maximalIdeal A) :
    (1 : WithBot ℕ∞) <
      (Module.depth (Localization.AtPrime p.asIdeal)
        (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
        (LocalizedModule.AtPrime p.asIdeal (A ⧸ Ideal.span {f})) : WithBot ℕ∞) +
        ringKrullDim (A ⧸ p.asIdeal)
```

**`Stacks.Algebraization.CompleteNormalDomain.three_lt_depth_add_ringKrullDim_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CompleteNormalDomainDepthConditions.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CompleteNormalDomainDepthConditions.lean#L241). The attribute's comment: “assumption (6) of Lemma 0DXU is satisfied”.

> Let `(A, 𝔪)` be a complete Noetherian normal local domain of dimension at least four and let
> `f ∈ 𝔪`. Then `depth(A_𝔭) + dim(A/𝔭) > 3` for every prime `𝔭` not containing `f` whose closure
> meets `V(f)` outside the closed point.

```lean
theorem three_lt_depth_add_ringKrullDim_quotient (A : Type u) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] [IsAdicComplete (IsLocalRing.maximalIdeal A) A] [IsDomain A]
    [IsIntegrallyClosed A] (hdim : (4 : WithBot ℕ∞) ≤ ringKrullDim A)
    (f : A) (hfm : f ∈ IsLocalRing.maximalIdeal A) (p : PrimeSpectrum A)
    (hfp : f ∉ p.asIdeal)
    (hp : ({q : PrimeSpectrum A | p.asIdeal ≤ q.asIdeal} ∩
      {q : PrimeSpectrum A | f ∈ q.asIdeal}) ≠
      {⟨IsLocalRing.maximalIdeal A, (IsLocalRing.maximalIdeal.isMaximal A).isPrime⟩}) :
    (3 : WithBot ℕ∞) <
      (Module.depth (Localization.AtPrime p.asIdeal)
        (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
        (Localization.AtPrime p.asIdeal) : WithBot ℕ∞) +
        ringKrullDim (A ⧸ p.asIdeal)
```

**`Stacks.Algebraization.CompleteNormalDomain.satisfiesAssumptions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CompleteNormalDomainDepthConditions.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CompleteNormalDomainDepthConditions.lean#L319). The attribute's comment: “assumptions (1), (2), (3), (5) and (6) of Lemma 0DXU are satisfied”.

> Let `(A, 𝔪)` be a complete Noetherian normal local domain of dimension at least four and let
> `f ∈ 𝔪` be nonzero. Then the algebraization situation with `𝔞 = 𝔪` and `I = (f)` satisfies
> assumptions (1), (2), (3), (5) and (6) of [Stacks, Tag 0DXU]: `𝔞` is the maximal ideal, `A` has a
> dualizing complex, `I` is generated by the nonzerodivisor `f`, and the two depth-dimension
> inequalities hold off the closed point.

```lean
theorem satisfiesAssumptions (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A] [IsDomain A] [IsIntegrallyClosed A]
    (hdim : (4 : WithBot ℕ∞) ≤ ringKrullDim A) (f : A)
    (hfm : f ∈ IsLocalRing.maximalIdeal A) (hf : f ≠ 0) :
    (completeNormalSituation A f hfm).a = IsLocalRing.maximalIdeal A ∧
      (∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K) ∧
      ((completeNormalSituation A f hfm).I = Ideal.span {f} ∧ IsSMulRegular A f) ∧
      (∀ p : PrimeSpectrum A, f ∈ p.asIdeal →
        p.asIdeal ≠ IsLocalRing.maximalIdeal A →
        (1 : WithBot ℕ∞) <
          (Module.depth (Localization.AtPrime p.asIdeal)
            (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule.AtPrime p.asIdeal (A ⧸ Ideal.span {f})) : WithBot ℕ∞) +
            ringKrullDim (A ⧸ p.asIdeal)) ∧
      (∀ p : PrimeSpectrum A, f ∉ p.asIdeal →
        ({q : PrimeSpectrum A | p.asIdeal ≤ q.asIdeal} ∩
          {q : PrimeSpectrum A | f ∈ q.asIdeal}) ≠
          {⟨IsLocalRing.maximalIdeal A, (IsLocalRing.maximalIdeal.isMaximal A).isPrime⟩} →
        (3 : WithBot ℕ∞) <
          (Module.depth (Localization.AtPrime p.asIdeal)
            (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
            (Localization.AtPrime p.asIdeal) : WithBot ℕ∞) +
            ringKrullDim (A ⧸ p.asIdeal))
```

## Tag 0EHK, a lemma

[Tag 0EHK](https://stacks.math.columbia.edu/tag/0EHK) in the Stacks Project.

**`Stacks.Algebraization.exists_matlisDual_approximation_localCohomologySystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LocalCohomologyMatlisApproximation.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LocalCohomologyMatlisApproximation.lean#L455). The attribute's comment: “the dualization; the essentially constant Matlis dual model of the local cohomology system, which local duality 0AAK and Matlis duality 08Z9 supply in the source, is an explicit hypothesis”.

> **Stacks Project, Tag 0EHK.** In the situation of Stacks 0EHC, let `(M_n)` be an inverse
> system of `A`-modules as in Stacks 0DXT and let `(ℱ_n)` be the corresponding object of
> `Coh(U, I𝒪_U)`. Let `d ≥ cd(A, I)` and `s ≥ 0` be integers, assume that `A` is local with
> maximal ideal `𝔪 = 𝔞`, that `A` has a dualizing complex, and that `(ℱ_n)` satisfies the
> `(s, s + d)`-inequalities. Let `E` be an injective hull of the residue field of `A`. Then for
> `i ≤ s` there is a finite `A`-module `N` annihilated by a power of `I` and, for `n ≫ 0`,
> compatible maps `H^i_𝔪(M_n) → Hom_A(N, E)` whose cokernels have finite length and whose kernels
> `K_n` form an inverse system in which the image of `K_{n''} → K_{n'}` has finite length for
> `n'' ≫ n' ≫ 0`.
>
> The existence of an essentially constant Matlis dual model of the local cohomology system is an
> explicit hypothesis: in the source it is the system of the modules `Ext^{-i}_A(M_n, ω_A^∙)` for
> a normalized dualizing complex, identified with the Matlis duals of the local cohomology modules
> by local duality (Stacks 0AAK) and Matlis duality (Stacks 08Z9). This library proves local
> duality only objectwise, with no naturality in the module
> (`Dualizing.LocalDuality.nonempty_adicCompletion_ext_linearEquiv_linearMap_localCohomology`),
> and its Matlis biduality isomorphism
> (`Dualizing.isIso_matlisEvaluation_of_isArtinian`) assumes `A` adically complete, so the model
> cannot be produced here; the essential constancy of that system is the substance of the proof in
> the source.

```lean
public theorem exists_matlisDual_approximation_localCohomologySystem
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (M : ℕᵒᵖ ⥤ ModuleCat.{u} S.A) (hM : IsFiniteModuleModel S M) (d s : ℤ)
    (E : Type u) [AddCommGroup E] [Module S.A E]
    (ιE : IsLocalRing.ResidueField S.A →ₗ[S.A] E) [Mono (ModuleCat.ofHom ιE)]
    (hιE : Module.IsInjectiveHull (ModuleCat.ofHom ιE))
    (_hmaximal : IsLocalRing.maximalIdeal S.A = S.a)
    (_hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (_hineq : SatisfiesDepthInequalities S
      (coherentAdicSystemOfFiniteModuleModel S M hM) s (s + d))
    (_hcd : _root_.Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (Ideal.fg_of_isNoetherianRing S.I) ≤ d)
    (_hs : 0 ≤ s)
    (hmodel : ∀ i : ℤ, i ≤ s → ∃ D : MatlisDualModel S M E i,
      IsEssentiallyConstantModFiniteLength S.A S.I D.G) :
    ∀ i : ℤ, i ≤ s →
      ∃ (N : ModuleCat.{u} S.A) (n₀ : ℕ)
        (φ : ∀ n : ℕ,
          (localCohomologySystem S M i).obj (op (n₀ + n)) →ₗ[S.A] (N →ₗ[S.A] E)),
        Module.Finite S.A N ∧
        (∃ k : ℕ, S.I ^ k • (⊤ : Submodule S.A N) = ⊥) ∧
        (∀ (m n : ℕ) (h : m ≤ n),
          φ m ∘ₗ ((localCohomologySystem S M i).map
            (homOfLE (Nat.add_le_add_left h n₀)).op).hom = φ n) ∧
        (∀ n : ℕ, IsFiniteLength S.A ((N →ₗ[S.A] E) ⧸ LinearMap.range (φ n))) ∧
        (∀ m : ℕ, ∃ k : ℕ, ∀ (n : ℕ) (hmn : m ≤ n), k ≤ n →
          IsFiniteLength S.A
            (Submodule.map ((localCohomologySystem S M i).map
              (homOfLE (Nat.add_le_add_left hmn n₀)).op).hom (LinearMap.ker (φ n))))
```

**`Stacks.Algebraization.exists_matlisDual_approximation_localCohomologySystem_of_inequalities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LocalCohomologyMatlisApproximationOfInequalities.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LocalCohomologyMatlisApproximationOfInequalities.lean#L52).

> **Stacks Project, Tag 0EHK.** In the situation of Stacks 0EHC, let `(M_n)` be an inverse
> system of `A`-modules as in Stacks 0DXT and let `(ℱ_n)` be the corresponding object of
> `Coh(U, I𝒪_U)`. Let `d ≥ cd(A, I)` and `s ≥ 0` be integers, and assume that `A` is local with
> maximal ideal `𝔪 = 𝔞`, that `A` has a dualizing complex, and that `(ℱ_n)` satisfies the
> `(s, s + d)`-inequalities. Let `E` be an injective hull of the residue field of `A`. Then for
> `i ≤ s` there is a finite `A`-module `N` annihilated by a power of `I` and, for `n ≫ 0`,
> compatible maps `H^i_𝔪(M_n) → Hom_A(N, E)` whose cokernels have finite length and whose kernels
> `K_n` form an inverse system in which the image of `K_{n''} → K_{n'}` has finite length for
> `n'' ≫ n' ≫ 0`.

```lean
public theorem exists_matlisDual_approximation_localCohomologySystem_of_inequalities
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (M : ℕᵒᵖ ⥤ ModuleCat.{u} S.A) (hM : IsFiniteModuleModel S M) (d s : ℤ)
    (E : Type u) [AddCommGroup E] [Module S.A E]
    (ιE : IsLocalRing.ResidueField S.A →ₗ[S.A] E) [Mono (ModuleCat.ofHom ιE)]
    (hιE : Module.IsInjectiveHull (ModuleCat.ofHom ιE))
    (hmaximal : IsLocalRing.maximalIdeal S.A = S.a)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hineq : SatisfiesDepthInequalities S
      (coherentAdicSystemOfFiniteModuleModel S M hM) s (s + d))
    (hcd : _root_.Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (Ideal.fg_of_isNoetherianRing S.I) ≤ d)
    (hs : 0 ≤ s) :
    ∀ i : ℤ, i ≤ s →
      ∃ (N : ModuleCat.{u} S.A) (n₀ : ℕ)
        (φ : ∀ n : ℕ,
          (localCohomologySystem S M i).obj (op (n₀ + n)) →ₗ[S.A] (N →ₗ[S.A] E)),
        Module.Finite S.A N ∧
        (∃ k : ℕ, S.I ^ k • (⊤ : Submodule S.A N) = ⊥) ∧
        (∀ (m n : ℕ) (h : m ≤ n),
          φ m ∘ₗ ((localCohomologySystem S M i).map
            (homOfLE (Nat.add_le_add_left h n₀)).op).hom = φ n) ∧
        (∀ n : ℕ, IsFiniteLength S.A ((N →ₗ[S.A] E) ⧸ LinearMap.range (φ n))) ∧
        (∀ m : ℕ, ∃ k : ℕ, ∀ (n : ℕ) (hmn : m ≤ n), k ≤ n →
          IsFiniteLength S.A
            (Submodule.map ((localCohomologySystem S M i).map
              (homOfLE (Nat.add_le_add_left hmn n₀)).op).hom (LinearMap.ker (φ n))))
```

## Tag 0EJ9, a lemma

[Tag 0EJ9](https://stacks.math.columbia.edu/tag/0EJ9) in the Stacks Project.

**`Stacks.Algebraization.extendsToX_of_isLocalRing_of_eq_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ExtensionPrincipalLocalTheorem.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ExtensionPrincipalLocalTheorem.lean#L89). The attribute's comment: “first assertion: (ℱₙ) extends to X”.

> **Stacks Project, Tag 0EJ9.** In Situation 0EHC let `(ℱₙ)` be an object of `Coh(U, I𝒪_U)`.
> Assume (1) `A` is local and `𝔞 = 𝔪` is the maximal ideal, (2) `A` has a dualizing complex,
> (3) `I = (f)` is a principal ideal, and (4) `(ℱₙ)` satisfies the `(2, 3)`-inequalities. Then
> `(ℱₙ)` extends to `X`.

```lean
public theorem extendsToX_of_isLocalRing_of_eq_span_singleton
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) (f : S.A)
    (ha : S.a = IsLocalRing.maximalIdeal S.A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hI : S.I = Ideal.span {f})
    (hineq : SatisfiesDepthInequalities S F 2 3) :
    ExtendsToX S (toKerSystem S F)
```

**`Stacks.Algebraization.essImage_completionFunctor_of_isLocalRing_of_eq_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ExtensionPrincipalLocalTheorem.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ExtensionPrincipalLocalTheorem.lean#L117). The attribute's comment: “in-particular clause: over an I-adically complete A, (ℱₙ) is the completion of a coherent 𝒪_U-module”.

> **Stacks Project, Tag 0EJ9, in-particular clause.** In the situation of
> `Stacks.Algebraization.extendsToX_of_isLocalRing_of_eq_span_singleton`, if moreover `A` is
> `I`-adically complete then `(ℱₙ)` is the completion of a coherent `𝒪_U`-module.
>
> The system extends to `X`, and over an `I`-adically complete base an extendable system is the
> restriction of a completion on `X`, hence the completion of a module restricted from `X`, hence a
> completion on `U` ([Stacks, Tag 0EIL]).

```lean
public theorem essImage_completionFunctor_of_isLocalRing_of_eq_span_singleton
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A] [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) (f : S.A)
    (ha : S.a = IsLocalRing.maximalIdeal S.A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hI : S.I = Ideal.span {f})
    (hineq : SatisfiesDepthInequalities S F 2 3) :
    (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage (toKerSystem S F)
```

## Tag 0EJA, a lemma

[Tag 0EJA](https://stacks.math.columbia.edu/tag/0EJA) in the Stacks Project.

**`Stacks.Algebraization.two_lt_depth_add_dim_of_satisfiesDepthInequalities`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesUnwinding.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesUnwinding.lean#L189). The attribute's comment: “necessity of the depth inequality at the points of U ∩ Y of dimension one”.

> **Stacks Project, Tag 0EJA.** In Situation 0EHC with `A` local, `𝔞 = 𝔪` and `cd(A, I) = 1`,
> if `(ℱ_n)` satisfies the `(2, 3)`-inequalities then `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) > 2`
> for every `y ∈ U ∩ Y` with `dim({y}‾) = 1` and every prime `𝔭 ⊆ 𝒪_{X,y}^∧` not containing
> `I𝒪_{X,y}^∧`.

```lean
public theorem two_lt_depth_add_dim_of_satisfiesDepthInequalities
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (ha : S.a = maximalIdeal S.A)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (h : SatisfiesDepthInequalities S F 2 3)
    (y : S.U.toScheme) (z : S.Y) (hyz : S.U.ι.base y = S.Yι.base z)
    (hdim : Order.height (S.U.ι.base y) = 1)
    (p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y))
    (hp : ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal) :
    enatToEInt (completedStalkDepth (idealOnOpen S) F y p) +
        krullDimToEInt (ringKrullDim (completedLocalRing (idealOnOpen S) y ⧸ p.asIdeal)) >
      ((2 : ℤ) : EInt)
```

**`Stacks.Algebraization.satisfiesDepthInequalities_two_three_iff_two_lt_depth_add_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesUnwindingCriterion.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesUnwindingCriterion.lean#L449). The attribute's comment: “corrected form: the published statement, at hypotheses (1) and (2) alone, is false, by Stacks.NonCatenaryExample.not_stacks0EJA, an example in which A/I is not catenary; this is the equivalence with A/I catenary and the completed local rings of U at the points of U ∩ Y of dimension one universally catenary with Cohen-Macaulay formal fibres”.

> In Situation 0EHC let `(ℱ_n)` be an object of `Coh(U, I𝒪_U)`. Assume `A` is local with `𝔞 = 𝔪`,
> that `cd(A, I) = 1`, and that `A/I` is catenary. Assume also that, at every point `y'` of `U ∩ Y`
> with `dim({y'}‾) = 1`, the completed local ring `𝒪_{X,y'}^∧` is universally catenary and has
> Cohen--Macaulay formal fibres. Then `(ℱ_n)` satisfies the `(2, 3)`-inequalities if and only if
> `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) > 2` for every `y ∈ U ∩ Y` with `dim({y}‾) = 1` and every
> prime `𝔭 ⊆ 𝒪_{X,y}^∧` with `𝔭 ∉ V(I𝒪_{X,y}^∧)`.
>
> Without the catenarity of `A/I` and the hypotheses on the completed stalks the statement is false:
> see `Stacks.NonCatenaryExample.not_stacks0EJA`.

```lean
public theorem satisfiesDepthInequalities_two_three_iff_two_lt_depth_add_dim
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (ha : S.a = maximalIdeal S.A)
    (hcat : Ring.IsCatenary (S.A ⧸ S.I))
    (hcatStalk : ∀ (y' : S.U.toScheme) (z' : S.Y), S.U.ι.base y' = S.Yι.base z' →
      Order.height (S.U.ι.base y') = 1 →
      Ring.IsUniversallyCatenary (completedLocalRing (idealOnOpen S) y'))
    (hCMStalk : ∀ (y' : S.U.toScheme) (z' : S.Y), S.U.ι.base y' = S.Yι.base z' →
      Order.height (S.U.ι.base y') = 1 →
      IsPRing Stacks.AdicCompletionFibre.cohenMacaulayRingMapProperty.{u}
        (completedLocalRing (idealOnOpen S) y'))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) :
    SatisfiesDepthInequalities S F 2 3 ↔
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        Order.height (S.U.ι.base y) = 1 →
        ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
          ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
          ((2 : ℤ) : EInt) <
            enatToEInt (completedStalkDepth (idealOnOpen S) F y p) +
              krullDimToEInt
                (ringKrullDim (completedLocalRing (idealOnOpen S) y ⧸ p.asIdeal))
```

**`Stacks.Algebraization.satisfiesDepthInequalities_two_three_iff_two_lt_depth_add_dim_of_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesUnwindingCriterion.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesUnwindingCriterion.lean#L522). The attribute's comment: “corrected form: the published statement, at hypotheses (1) and (2) alone, is false, by Stacks.NonCatenaryExample.not_stacks0EJA, an example in which A/I is not catenary; this is the equivalence for A with a dualizing complex, the standing hypothesis of the neighbouring 0EJ9 and 0EJB”.

> In Situation 0EHC let `(ℱ_n)` be an object of `Coh(U, I𝒪_U)`. Assume `A` is local with `𝔞 = 𝔪`,
> that `A` has a dualizing complex, and that `cd(A, I) = 1`. Then `(ℱ_n)` satisfies the
> `(2, 3)`-inequalities if and only if `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) > 2` for every
> `y ∈ U ∩ Y` with `dim({y}‾) = 1` and every prime `𝔭 ⊆ 𝒪_{X,y}^∧` with `𝔭 ∉ V(I𝒪_{X,y}^∧)`.

```lean
public theorem satisfiesDepthInequalities_two_three_iff_two_lt_depth_add_dim_of_isDualizingComplex
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (ha : S.a = maximalIdeal S.A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) :
    SatisfiesDepthInequalities S F 2 3 ↔
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        Order.height (S.U.ι.base y) = 1 →
        ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
          ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
          ((2 : ℤ) : EInt) <
            enatToEInt (completedStalkDepth (idealOnOpen S) F y p) +
              krullDimToEInt
                (ringKrullDim (completedLocalRing (idealOnOpen S) y ⧸ p.asIdeal))
```

**`Stacks.NonCatenaryExample.not_stacks0EJA`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/NonCatenaryCounterexample/Final.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/NonCatenaryCounterexample/Final.lean#L40). The attribute's comment: “refutation of the published 'if' direction: at hypotheses (1) and (2) alone, the depth inequality at the points of U ∩ Y of dimension one does not imply the (2, 3)-inequalities; in the example A/I is not catenary”.

> **Stacks 0EJA is false as published.** There is an algebraization situation (Situation 0EHC)
> with `A` Noetherian local, `𝔞 = 𝔪`, `cd(A, I) = 1`, and an object `(ℱₙ)` of `Coh(U, I𝒪_U)` such
> that `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) > 2` for every `y ∈ U ∩ Y` with `dim({y}‾) = 1` and every
> `𝔭 ∉ V(I𝒪_{X,y}^∧)`, but `(ℱₙ)` does not satisfy the `(2, 3)`-inequalities.

```lean
theorem not_stacks0EJA :
    ¬ ∀ (S : AlgebraizationSituation.{u}) [IsLocalRing S.A], S.a = maximalIdeal S.A →
      Stacks.LocalCohomology.cohomologicalDimension S.A S.I (IsNoetherian.noetherian S.I) = 1 →
      ∀ F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S),
        (SatisfiesDepthInequalities S F 2 3 ↔
          ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
            Order.height (S.U.ι.base y) = 1 →
            ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
              ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
              ((2 : ℤ) : EInt) <
                enatToEInt (completedStalkDepth (idealOnOpen S) F y p) +
                  krullDimToEInt
                    (ringKrullDim (completedLocalRing (idealOnOpen S) y ⧸ p.asIdeal)))
```

## Tag 0EJB, a lemma

[Tag 0EJB](https://stacks.math.columbia.edu/tag/0EJB) in the Stacks Project.

**`Stacks.Algebraization.satisfiesDepthInequalities_of_finiteLocallyFreeOutside`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesLocallyFreeOutside.lean, line 669](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesLocallyFreeOutside.lean#L669).

> In Situation 0EHC let `(ℱ_n)` be an object of `Coh(U, I𝒪_U)`. Assume (1) `A` is local with
> `𝔞 = 𝔪`, (2) `A` has a dualizing complex, (3) `cd(A, I) = 1`, (4) for `y ∈ U ∩ Y` the module
> `ℱ_y^∧` is finite locally free outside `V(I𝒪_{X,y}^∧)`, and (5) either (a) `X \ Y` is `(S₂)` and
> every irreducible component of `X` not contained in `Y` has dimension `≥ 4`, or (b) for every prime
> `𝔭 ∉ V(I)` with `V(𝔭) ∩ V(I) ≠ {𝔪}` one has `depth(A_𝔭) + dim(A/𝔭) > 3`. Then `(ℱ_n)`
> satisfies the `(2, 3)`-inequalities.

```lean
public theorem satisfiesDepthInequalities_of_finiteLocallyFreeOutside
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A]
    (hmax : S.a = maximalIdeal S.A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1)
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hfree : ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
      ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
        ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
        Module.Free (Localization.AtPrime p.asIdeal)
          (LocalizedModule p.asIdeal.primeCompl (completedStalk (idealOnOpen S) F y)))
    (hcondition :
      ((∀ p : PrimeSpectrum S.A, ¬ S.I ≤ p.asIdeal →
          PropertySkRing (Localization.AtPrime p.asIdeal) 2) ∧
        (∀ p : PrimeSpectrum S.A, IsMinimalPrime p.asIdeal →
          ¬ S.I ≤ p.asIdeal →
          (4 : WithBot ℕ∞) ≤ ringKrullDim (S.A ⧸ p.asIdeal))) ∨
      (∀ p : PrimeSpectrum S.A, ¬ S.I ≤ p.asIdeal →
        ({q : PrimeSpectrum S.A | p.asIdeal ≤ q.asIdeal} ∩
          {q : PrimeSpectrum S.A | S.I ≤ q.asIdeal}) ≠
          {⟨maximalIdeal S.A, (IsLocalRing.maximalIdeal.isMaximal S.A).isPrime⟩} →
        (3 : WithBot ℕ∞) <
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (Localization.AtPrime p.asIdeal) : WithBot ℕ∞) +
            ringKrullDim (S.A ⧸ p.asIdeal))) :
    SatisfiesDepthInequalities S F 2 3
```

## Tag 0EJC, a remark

[Tag 0EJC](https://stacks.math.columbia.edu/tag/0EJC) in the Stacks Project.

**`Stacks.Algebraization.essImage_completionFunctor_of_hasSerreCompletedStalkConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumSerreAlgebraizationTheorem.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/PuncturedSpectrumSerreAlgebraizationTheorem.lean#L78).

> **Stacks Project, Tag 0EJC.** Let `(A, 𝔪)` be a Noetherian local ring which has a dualizing
> complex and is complete with respect to `f ∈ 𝔪`, let `(ℱₙ)` be an object of `Coh(U, f𝒪_U)` where
> `U` is the punctured spectrum of `A`, and set `Y = V(f) ⊆ X = Spec(A)`. If for every
> `y ∈ U ∩ V(f)` closed in `U`, i.e. with `dim({y}‾) = 1`, the `𝒪_{X,y}^∧`-module `ℱ_y^∧` satisfies
>
> 1. `ℱ_y^∧[1/f]` is `(S₂)` as an `𝒪_{X,y}^∧[1/f]`-module, and
> 2. `dim(𝒪_{X,y}^∧/𝔭) ≥ 3` for every `𝔭 ∈ Ass(ℱ_y^∧[1/f])`,
>
> then `(ℱₙ)` is the completion of a coherent `𝒪_U`-module.

```lean
public theorem essImage_completionFunctor_of_hasSerreCompletedStalkConditions
    (S : AlgebraizationSituation.{u}) [IsLocalRing S.A] [IsAdicComplete S.I S.A]
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S)) (f : S.A)
    (ha : S.a = IsLocalRing.maximalIdeal S.A)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (hI : S.I = Ideal.span {f})
    (hserre : ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
      Order.height (S.U.ι.base y) = 1 → HasSerreCompletedStalkConditions S F f y) :
    (completionFunctor S.U.toScheme (S.Yι.ker.comap S.U.ι)).essImage (toKerSystem S F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.20, Tag 0EHJ](https://stacks.math.columbia.edu/tag/0EHJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
