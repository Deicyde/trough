---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.finite_localCohomologyWithSupportIn_iff_depth_add_dim, Stacks.LocalCohomology.localCohomologyCutoff, Module.localCohomologyCutoff_map_eq, Stacks.Algebraization.completedStalkDepth_add_ringKrullDim_succ_eq_of_specializes, Module.depth_localized_adicCompletion_le, Module.depth_add_ringKrullDim_quotient_localization_adicCompletion, Stacks.LocalCohomology.localCohomologyCutoff_adicCompletion_le, Stacks.LocalCohomology.min_succ_le_localCohomologyCutoff_adicCompletion
statement: formalized
proof: formalized
---

# 51.11 Finiteness of local cohomology, II

Section 51.11 of the Stacks Project, [Tag 0BJQ](https://stacks.math.columbia.edu/tag/0BJQ). 8 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EFD, a proposition

[Tag 0EFD](https://stacks.math.columbia.edu/tag/0EFD) in the Stacks Project.

**`Stacks.LocalCohomology.finite_localCohomologyWithSupportIn_iff_depth_add_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessDepthDimension.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessDepthDimension.lean#L61).

> **Faltings' finiteness criterion.** For a finite module `M` over a Noetherian ring `A` with a
> dualizing complex and a specialization-stable `T ⊆ Spec(A)`, the local cohomology modules
> `H^i_T(M)` are finite for `i ≤ s` if and only if
> `depth_{A_p}(M_p) + dim((A/p)_q) > s` whenever `p ⊆ q` with `p ∉ T` and `q ∈ T`.

```lean
public theorem finite_localCohomologyWithSupportIn_iff_depth_add_dim
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T) (s : ℕ)
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega)) :
    (∀ i : ℤ, i ≤ (s : ℤ) → Module.Finite A
        (localCohomologyWithSupportIn.{u, u} A T
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)) ↔
      (∀ p q : PrimeSpectrum A, p ∉ T → q ∈ T → p.asIdeal ≤ q.asIdeal →
        enatToEInt (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M)) +
          krullDimToEInt (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) > ((s : ℤ) : EInt))
```

## Tag 0BJR, an equation

[Tag 0BJR](https://stacks.math.columbia.edu/tag/0BJR) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyCutoff`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FinitenessCutoff.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FinitenessCutoff.lean#L54).

> The local cohomology finiteness cutoff
> `s_{A,I}(M) = min_{p ∉ V(I), q ∈ V(I), p ⊆ q} (depth(Mₚ) + dim((A / p)ₒ))`.

```lean
public noncomputable def localCohomologyCutoff (A : Type*) [CommRing A] (I : Ideal A)
    (M : Type*) [AddCommGroup M] [Module A M] : ℕ∞
```

## Tag 0BJS, a lemma

[Tag 0BJS](https://stacks.math.columbia.edu/tag/0BJS) in the Stacks Project.

**`Module.localCohomologyCutoff_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomologyCutoff/FiniteMap.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomologyCutoff/FiniteMap.lean#L125).

> For a finite homomorphism of Noetherian rings, extension of an ideal does not change the
> local cohomology finiteness cutoff of a finite module if the source is universally catenary.

```lean
theorem localCohomologyCutoff_map_eq
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Finite A B]
    (I : Ideal A) (M : Type w) [AddCommGroup M] [Module A M] [Module B M]
    [IsScalarTower A B M] [Module.Finite B M] (hA : Ring.IsUniversallyCatenary A) :
    Stacks.LocalCohomology.localCohomologyCutoff B (Ideal.map (algebraMap A B) I) M =
      Stacks.LocalCohomology.localCohomologyCutoff A I M
```

## Tag 0EHW, a lemma

[Tag 0EHW](https://stacks.math.columbia.edu/tag/0EHW) in the Stacks Project.

**`Stacks.Algebraization.completedStalkDepth_add_ringKrullDim_succ_eq_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CompletedStalkDepthSpecialization.lean, line 944](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CompletedStalkDepthSpecialization.lean#L944). The attribute's comment: “second display, along a specialization of points”.

> **[Stacks, Tag 0EHW] along a specialization of points**, the final step in the proof of
> [Stacks, Tag 0EJA].
>
> Let `X` be a locally Noetherian scheme, `ℐ` a quasi-coherent sheaf of ideals, `(ℱ_n)` a coherent
> `ℐ`-adic system and `y ⤳ y'` a specialization of points of `X` coming from a prime `q` of
> `𝒪_{X,y'}` which contains `ℐ_{y'}` and satisfies `dim(𝒪_{X,y'}/q) = 1`. Assume `ℐ_{y'}` lies in
> the maximal ideal and that `𝒪_{X,y'}^∧` is universally catenary with Cohen--Macaulay formal
> fibres -- the two consequences of a dualizing complex that the source's proof of
> [Stacks, Tag 0EHW] uses, and which a dualizing complex on `𝒪_{X,y'}` supplies through
> [Stacks, Tag 0BFR]. Then for every prime `𝔭` of
> `𝒪_{X,y}^∧`, with `𝔭'` its contraction along the specialization map `𝒪_{X,y'}^∧ → 𝒪_{X,y}^∧`,
>
> `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) + 1 = depth((ℱ_{y'}^∧)_{𝔭'}) + dim(𝒪_{X,y'}^∧/𝔭')`.
>
> Write `𝔮` for the prime of `𝒪_{X,y'}^∧` above `q` and `C = (𝒪_{X,y'}^∧)_𝔮`. The ring `𝒪_{X,y}^∧`
> is the `ℐ`-adic completion of `C` compatibly with the specialization map
> (`Stacks.Algebraization.exists_ringEquiv_completedLocalRing_of_specializes`) and `ℱ_y^∧` is the
> `ℐ`-adic completion of `(ℱ_{y'}^∧)_𝔮`
> (`Stacks.Algebraization.nonempty_linearEquiv_completedStalk_of_specializes`); the latter is only
> `𝒪_{X,y'}`-linear, and it is upgraded to semilinearity over the former by
> `Stacks.Algebraization.semilinear_of_localization` and
> `Stacks.Algebraization.semilinear_of_adicCompletion`. The second display of [Stacks, Tag 0EHW]
> for `C`, which inherits both hypotheses from `𝒪_{X,y'}^∧`, then gives the identity after the
> depth at `𝔭 ∩ C` is identified with the depth at `𝔭'` and `dim(C/𝔭 ∩ C) + 1` with
> `dim(𝒪_{X,y'}^∧/𝔭')`, the latter because `𝒪_{X,y'}^∧` is universally catenary and
> `dim(𝒪_{X,y'}^∧/𝔮) = dim(𝒪_{X,y'}/q) = 1`.

```lean
public theorem completedStalkDepth_add_ringKrullDim_succ_eq_of_specializes
    [IsLocallyNoetherian X] (J : X.IdealSheafData)
    (G : Stacks.Coherent.CoherentAdicSystems J) {y y' : X} (h : y ⤳ y')
    (q : PrimeSpectrum (X.presheaf.stalk y')) (hqy : X.fromSpecStalk y' q = y)
    (hq : IdealSheafData.stalk J y' ≤ q.asIdeal)
    (hJmax : IdealSheafData.stalk J y' ≤ IsLocalRing.maximalIdeal (X.presheaf.stalk y'))
    (hcat : Ring.IsUniversallyCatenary (completedLocalRing J y'))
    (hCM : IsPRing Stacks.AdicCompletionFibre.cohenMacaulayRingMapProperty.{u}
      (completedLocalRing J y'))
    (hone : ringKrullDim (X.presheaf.stalk y' ⧸ q.asIdeal) = 1)
    (p : PrimeSpectrum (completedLocalRing J y)) :
    (completedStalkDepth J G y p : WithBot ℕ∞) +
        ringKrullDim (completedLocalRing J y ⧸ p.asIdeal) + 1 =
      (completedStalkDepth J G y'
          (PrimeSpectrum.comap (completedLocalRingSpecializes J h) p) : WithBot ℕ∞) +
        ringKrullDim (completedLocalRing J y' ⧸
          (PrimeSpectrum.comap (completedLocalRingSpecializes J h) p).asIdeal)
```

**`Module.depth_localized_adicCompletion_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FinitenessLocalCohomology/DepthAdicCompletion.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FinitenessLocalCohomology/DepthAdicCompletion.lean#L45). The attribute's comment: “first display, the inequality `depth(M_𝔭) ≤ depth(M'_{𝔭'})`, without the dualizing complex and without the outer pair of primes”.

> The depth of a finite module at a prime cannot decrease after adic completion and
> localization at a prime above it.

```lean
theorem depth_localized_adicCompletion_le
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (p : Ideal A) [p.IsPrime]
    (p' : Ideal (AdicCompletion I A)) [p'.IsPrime] [p'.LiesOver p] :
    Module.depth (Localization.AtPrime p) (maximalIdeal (Localization.AtPrime p))
        (LocalizedModule p.primeCompl M) ≤
      Module.depth (Localization.AtPrime p') (maximalIdeal (Localization.AtPrime p'))
        (LocalizedModule p'.primeCompl (AdicCompletion I M))
```

**`Module.depth_add_ringKrullDim_quotient_localization_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FinitenessLocalCohomology/DepthDimAdicCompletion.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FinitenessLocalCohomology/DepthDimAdicCompletion.lean#L150). The attribute's comment: “second display”.

> **Stacks Project, Tag 0EHW, second display.** Let `A` be a Noetherian ring admitting a
> dualizing complex, let `I` be an ideal, let `M` be a finite `A`-module and write `A'` and `M'` for
> the `I`-adic completions. Let `𝔭' ⊆ 𝔮'` be primes of `A'` with `𝔮' ∈ V(I A')`, lying over primes
> `𝔭 ⊆ 𝔮` of `A`. Then
>
> `depth(M'_{𝔭'}) + dim((A'/𝔭')_{𝔮'}) = depth(M_𝔭) + dim((A/𝔭)_𝔮)`.

```lean
public theorem depth_add_ringKrullDim_quotient_localization_adicCompletion
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (hdual : ∃ K : DerivedCategory (ModuleCat.{w} A), Dualizing.IsDualizingComplex K)
    (I : Ideal A)
    (M : Type v) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (p : Ideal A) [p.IsPrime] (q : Ideal A) [q.IsPrime]
    (p' : Ideal (AdicCompletion I A)) [p'.IsPrime] [p'.LiesOver p]
    (q' : Ideal (AdicCompletion I A)) [q'.IsPrime] [q'.LiesOver q]
    (hIq' : I.map (algebraMap A (AdicCompletion I A)) ≤ q') (hpq' : p' ≤ q') :
    ((Module.depth (Localization.AtPrime p') (maximalIdeal (Localization.AtPrime p'))
            (LocalizedModule p'.primeCompl (AdicCompletion I M)) : ℕ∞) : WithBot ℕ∞) +
        ringKrullDim (Localization.AtPrime q' ⧸
          p'.map (algebraMap (AdicCompletion I A) (Localization.AtPrime q'))) =
      ((Module.depth (Localization.AtPrime p) (maximalIdeal (Localization.AtPrime p))
            (LocalizedModule p.primeCompl M) : ℕ∞) : WithBot ℕ∞) +
        ringKrullDim (Localization.AtPrime q ⧸ p.map (algebraMap A (Localization.AtPrime q)))
```

## Tag 0BJT, a lemma

[Tag 0BJT](https://stacks.math.columbia.edu/tag/0BJT) in the Stacks Project.

**`Stacks.LocalCohomology.localCohomologyCutoff_adicCompletion_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Cutoff/Completion.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Cutoff/Completion.lean#L123). The attribute's comment: “cutoff_completion_le”.

> **Stacks 0BJT.** Completion at the maximal ideal cannot increase the local cohomology
> finiteness cutoff of a finite module over a universally catenary Noetherian local ring.

```lean
public theorem localCohomologyCutoff_adicCompletion_le
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : Type v) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (hA : Ring.IsUniversallyCatenary A) :
    localCohomologyCutoff (AdicCompletion (IsLocalRing.maximalIdeal A) A)
        (I.map (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A)))
        (AdicCompletion (IsLocalRing.maximalIdeal A) M) ≤
      localCohomologyCutoff A I M
```

**`Stacks.LocalCohomology.min_succ_le_localCohomologyCutoff_adicCompletion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CutoffCompletionSerre.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CutoffCompletionSerre.lean#L312). The attribute's comment: “cutoff_completion_lower_bound_of_serre”.

> If the formal fibres of a universally catenary Noetherian local ring
> satisfy `(Sₙ)`, the cutoff after completion is at least the minimum of the
> original cutoff and `n + 1`.

```lean
public lemma min_succ_le_localCohomologyCutoff_adicCompletion
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (I : Ideal A) (M : Type v) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (n : ℕ) (hcatenary : Ring.IsUniversallyCatenary A)
    (hformal : FormalFibersHavePropertySk A n) :
    min ((n + 1 : ℕ) : ℕ∞) (localCohomologyCutoff A I M) ≤
      localCohomologyCutoff
        (AdicCompletion (IsLocalRing.maximalIdeal A) A)
        (I.map (algebraMap A (AdicCompletion (IsLocalRing.maximalIdeal A) A)))
        (AdicCompletion (IsLocalRing.maximalIdeal A) M)
```

## Tag 0BJU, a lemma

[Tag 0BJU](https://stacks.math.columbia.edu/tag/0BJU) in the Stacks Project.

**`Stacks.LocalCohomology.finite_lt_and_not_finite_localCohomologyCutoff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/GorensteinFiniteness.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/GorensteinFiniteness.lean#L168).

> **Stacks Project, Tag 0BJU.** Let `A` be a Gorenstein Noetherian local ring, let `I ⊆ A` be
> an ideal, let `Z = V(I)` and let `M` be a finite `A`-module. Let `s = s_{A,I}(M)` be the cutoff
> of Tag 0BJR. Then `H^i_Z(M)` is finite for every `i < s`, and `H^s_Z(M)` is not finite.
>
> This is a special case of Satz 1 of Faltings, and it is obtained here as the special case
> `omega = A[0]` of Faltings' finiteness criterion of Tag 0EFD, Gorensteinness of a Noetherian
> local ring being precisely the statement that `A[0]` is a dualizing complex.
>
> The first conjunct expresses `i < s` through a natural number `n` with `n < s` and `i ≤ n`; this
> covers every degree when `s = ⊤`. The second conjunct is hypothesized on `s` being a natural
> number, as it must be: the cutoff is an infimum in `ℕ∞` and there is no degree `⊤`.

```lean
public theorem finite_lt_and_not_finite_localCohomologyCutoff
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : Dualizing.IsGorensteinLocalRing A) (I : Ideal A)
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M] :
    (∀ n : ℕ, (n : ℕ∞) < localCohomologyCutoff A I M → ∀ i : ℤ, i ≤ (n : ℤ) →
        Module.Finite A
          (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)) ∧
      (∀ s : ℕ, localCohomologyCutoff A I M = (s : ℕ∞) →
        ¬ Module.Finite A
          (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A M)) (s : ℤ)))
```

## Tag 0BJV, a theorem

[Tag 0BJV](https://stacks.math.columbia.edu/tag/0BJV) in the Stacks Project.

**`Stacks.LocalCohomology.finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_formalFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean#L462). The attribute's comment: “finiteness in the degrees below the cutoff”.

> **Stacks Project, Tag 0BJV, finiteness below the cutoff.** Let `A` be a universally
> catenary Noetherian ring whose local rings have Cohen–Macaulay formal fibres, let `I ⊆ A` be an
> ideal, let `Z = V(I)` and let `M` be a finite `A`-module. Then `H^i_Z(M)` is a finite
> `A`-module in every degree `i` strictly below the cutoff `s = s_{A,I}(M)` of Tag 0BJR.
>
> The degrees `i < s` are expressed through a natural number `n` with `n < s` and `i ≤ n`, which
> for `s = ⊤` gives finiteness in every degree.

```lean
public theorem finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_formalFibers
    (hA : Ring.IsUniversallyCatenary A)
    (hformal : ∀ p : PrimeSpectrum A,
      FormalFibersAreCohenMacaulay (Localization.AtPrime p.asIdeal))
    (n : ℕ) (hn : (n : ℕ∞) < localCohomologyCutoff A I M) (i : ℤ) (hi : i ≤ (n : ℤ)) :
    Module.Finite A
      (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)
```

**`Stacks.LocalCohomology.not_finite_localCohomologyWithSupportIn_localCohomologyCutoff_of_formalFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean#L484). The attribute's comment: “non-finiteness in the cutoff degree”.

> **Stacks Project, Tag 0BJV, non-finiteness at the cutoff.** In the situation of
> `finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_formalFibers`, if the cutoff
> `s = s_{A,I}(M)` is the natural number `s`, then `H^s_Z(M)` is *not* a finite `A`-module.
>
> Were it finite it would join the finite modules in the degrees below `s` to make `H^i_Z(M)`
> finite for all `i ≤ s`; testing that on the completion of the local ring at the prime at which
> the cutoff is attained, Tag 0EFD would then force `s < s`. The hypothesis that the cutoff is a
> natural number is needed as stated: the cutoff is an infimum in `ℕ∞` and there is no degree
> `⊤`.

```lean
public theorem not_finite_localCohomologyWithSupportIn_localCohomologyCutoff_of_formalFibers
    (hA : Ring.IsUniversallyCatenary A)
    (hformal : ∀ p : PrimeSpectrum A,
      FormalFibersAreCohenMacaulay (Localization.AtPrime p.asIdeal))
    (s : ℕ) (hs : localCohomologyCutoff A I M = (s : ℕ∞)) :
    ¬ Module.Finite A
      (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) (s : ℤ))
```

**`Stacks.LocalCohomology.finite_lt_and_not_finite_localCohomologyCutoff_of_formalFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean#L523).

> **Stacks Project, Tag 0BJV.** Let `A` be a Noetherian ring, let `I ⊆ A` be an ideal, let
> `Z = V(I) ⊆ Spec(A)` and let `M` be a finite `A`-module. Set `s = s_{A,I}(M)` as in Tag 0BJR.
> Assume that `A` is universally catenary and that the formal fibres of the local rings of `A`
> are Cohen–Macaulay. Then `H^i_Z(M)` is finite for `0 ≤ i < s`, and `H^s_Z(M)` is not finite.
>
> This is a special case of Satz 2 of Faltings. The first conjunct expresses `i < s` through a
> natural number `n` with `n < s` and `i ≤ n`, which covers every degree when `s = ⊤`; the second
> is hypothesized on `s` being a natural number, as it must be.

```lean
public theorem finite_lt_and_not_finite_localCohomologyCutoff_of_formalFibers
    (hA : Ring.IsUniversallyCatenary A)
    (hformal : ∀ p : PrimeSpectrum A,
      FormalFibersAreCohenMacaulay (Localization.AtPrime p.asIdeal)) :
    (∀ n : ℕ, (n : ℕ∞) < localCohomologyCutoff A I M → ∀ i : ℤ, i ≤ (n : ℤ) →
        Module.Finite A
          (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)) ∧
      (∀ s : ℕ, localCohomologyCutoff A I M = (s : ℕ∞) →
        ¬ Module.Finite A
          (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A M)) (s : ℤ)))
```

## Tag 0BJW, a remark

[Tag 0BJW](https://stacks.math.columbia.edu/tag/0BJW) in the Stacks Project.

**`Stacks.LocalCohomology.finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_serreFormalFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SerreFormalFibresFiniteness.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SerreFormalFibresFiniteness.lean#L135). The attribute's comment: “finiteness through degree n when the formal fibres are (S_n)”.

> **Stacks Project, Tag 0BJW, finiteness through a degree below the cutoff.** Let `A` be a
> universally catenary Noetherian ring, let `I ⊆ A` be an ideal, let `Z = V(I)` and let `M` be a
> finite `A`-module. Fix a natural number `n` strictly below the cutoff `s = s_{A,I}(M)` of Tag
> 0BJR and assume only that the formal fibres of the local rings of `A` satisfy Serre's condition
> `(S_n)`. Then `H^i_Z(M)` is a finite `A`-module in every degree `i ≤ n`.
>
> This is Tag 0BJV's finiteness clause with the Cohen–Macaulay hypothesis on the formal fibres
> weakened to `(S_n)`, which is all the proof uses: the hypothesis enters only through the Tag
> 0BJT bound `lt_localCohomologyCutoff_adicCompletion_localization` at `k = n`. For `s = ⊤` the
> statement gives finiteness in every degree, provided the formal fibres are `(S_n)` for the `n`
> in question.

```lean
public theorem
    finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_serreFormalFibers
    (hA : Ring.IsUniversallyCatenary A) (n : ℕ)
    (hformal : ∀ p : PrimeSpectrum A,
      FormalFibersHavePropertySk (Localization.AtPrime p.asIdeal) n)
    (hn : (n : ℕ∞) < localCohomologyCutoff A I M) (i : ℤ) (hi : i ≤ (n : ℤ)) :
    Module.Finite A
      (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)
```

**`Stacks.LocalCohomology.not_finite_localCohomologyWithSupportIn_localCohomologyCutoff_of_serreFormalFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SerreFormalFibresFiniteness.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SerreFormalFibresFiniteness.lean#L163). The attribute's comment: “non-finiteness in the cutoff degree when the formal fibres are (S_{s-1})”.

> **Stacks Project, Tag 0BJW, non-finiteness at the cutoff.** In the situation of
> `finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_serreFormalFibers`, if the
> cutoff `s = s_{A,I}(M)` is the natural number `s` and the formal fibres of the local rings of
> `A` satisfy Serre's condition `(S_{s-1})`, then `H^s_Z(M)` is *not* a finite `A`-module.
>
> Were it finite it would join the finite modules in the degrees below `s` — available from the
> finiteness clause at `n = s - 1`, whose `(S_{s-1})` hypothesis is the one assumed here — to make
> `H^i_Z(M)` finite for all `i ≤ s`; testing that on the completion of the local ring at the prime
> at which the cutoff is attained, Tag 0EFD would then force `s < s`. The prime is produced by the
> Tag 0BJT bound `exists_localCohomologyCutoff_adicCompletion_localization_eq` at `k = s - 1`,
> which is the only place the formal-fibre hypothesis is used besides the finiteness clause. The
> hypothesis that the cutoff is a natural number is needed as stated: the cutoff is an infimum in
> `ℕ∞` and there is no degree `⊤`.

```lean
public theorem
    not_finite_localCohomologyWithSupportIn_localCohomologyCutoff_of_serreFormalFibers
    (hA : Ring.IsUniversallyCatenary A) (s : ℕ)
    (hformal : ∀ p : PrimeSpectrum A,
      FormalFibersHavePropertySk (Localization.AtPrime p.asIdeal) (s - 1))
    (hs : localCohomologyCutoff A I M = (s : ℕ∞)) :
    ¬ Module.Finite A
      (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) (s : ℤ))
```

**`Stacks.LocalCohomology.finite_lt_and_not_finite_localCohomologyCutoff_of_serreFormalFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SerreFormalFibresFiniteness.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SerreFormalFibresFiniteness.lean#L220).

> **Stacks Project, Tag 0BJW.** In the situation of Tag 0BJV — `A` a Noetherian ring,
> `I ⊆ A` an ideal, `Z = V(I) ⊆ Spec(A)`, `M` a finite `A`-module and `s = s_{A,I}(M)` the cutoff
> of Tag 0BJR — assume `A` is universally catenary and make no assumption at all on the formal
> fibres. Then both conclusions of Tag 0BJV survive under a Serre condition imposed one degree at
> a time:
>
> * given `n` with `s > n`, if the formal fibres of the local rings of `A` satisfy `(S_n)` then
>   `H^i_Z(M)` is finite for `i ≤ n`;
> * if `s` is a natural number and the formal fibres satisfy `(S_{s-1})` then `H^s_Z(M)` is not
>   finite.
>
> This is the whole remark in one statement; the two conjuncts are
> `finite_localCohomologyWithSupportIn_of_lt_localCohomologyCutoff_of_serreFormalFibers` and
> `not_finite_localCohomologyWithSupportIn_localCohomologyCutoff_of_serreFormalFibers`, and the
> shape matches the combined carrier
> `finite_lt_and_not_finite_localCohomologyCutoff_of_formalFibers` of Tag 0BJV, except that the
> formal-fibre hypothesis is bound inside each conjunct because its Serre index depends on the
> degree under discussion.

```lean
public theorem finite_lt_and_not_finite_localCohomologyCutoff_of_serreFormalFibers
    (hA : Ring.IsUniversallyCatenary A) :
    (∀ n : ℕ, (∀ p : PrimeSpectrum A,
          FormalFibersHavePropertySk (Localization.AtPrime p.asIdeal) n) →
        (n : ℕ∞) < localCohomologyCutoff A I M → ∀ i : ℤ, i ≤ (n : ℤ) →
        Module.Finite A
          (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)) ∧
      (∀ s : ℕ, (∀ p : PrimeSpectrum A,
          FormalFibersHavePropertySk (Localization.AtPrime p.asIdeal) (s - 1)) →
        localCohomologyCutoff A I M = (s : ℕ∞) →
        ¬ Module.Finite A
          (localCohomologyWithSupportIn.{u, u} A (PrimeSpectrum.zeroLocus (I : Set A))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A M)) (s : ℤ)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.11, Tag 0BJQ](https://stacks.math.columbia.edu/tag/0BJQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
