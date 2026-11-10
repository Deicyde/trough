---
declaration: section
origin: cited
lean: Stacks.Algebraization.BootstrapSituation, Stacks.Algebraization.depth_localized_gt_of_no_intermediate_prime, Stacks.Algebraization.finite_adicCompletion, Stacks.Algebraization.subset_adicLocus_adicCompletion, Stacks.Algebraization.stableUnderSpecialization_adicCompletion, Stacks.Algebraization.dualizing_adicCompletion, Stacks.Algebraization.cohomologicalDimension_le_adicCompletion, Stacks.Algebraization.completedLocalDepth_adicCompletion
statement: formalized
proof: formalized
---

# 52.10 Algebraization of local cohomology, III

Section 52.10 of the Stacks Project, [Tag 0EFT](https://stacks.math.columbia.edu/tag/0EFT). 9 tags here are carried by 71 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EFU, a situation

[Tag 0EFU](https://stacks.math.columbia.edu/tag/0EFU) in the Stacks Project.

**`Stacks.Algebraization.BootstrapSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapSituation.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapSituation.lean#L61).

> The standing bootstrap situation for algebraization: a Noetherian ring with a dualizing
> complex, an ideal, a finite module, a specialization-stable subset of the adic locus, and the two
> integer bounds against which depth and cohomological dimension are measured.

```lean
public structure BootstrapSituation
```

## Tag 0EID, a lemma

[Tag 0EID](https://stacks.math.columbia.edu/tag/0EID) in the Stacks Project.

**`Stacks.Algebraization.depth_localized_gt_of_no_intermediate_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapDepth.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapDepth.lean#L93).

> **Stacks Project, Tag 0EID.** In the bootstrap situation the depth at `p` exceeds `s` when
> no prime of `V(I) \ T` lies between `p` and a prime `q` of `T`.

```lean
public theorem depth_localized_gt_of_no_intermediate_prime
    (S : BootstrapSituation.{u, v, w})
    (p q : PrimeSpectrum S.A)
    (hpq : p.asIdeal ≤ q.asIdeal)
    (hp : p ∉ PrimeSpectrum.zeroLocus (S.I : Set S.A))
    (hq : q ∈ S.T)
    (h : ¬ ∃ r : PrimeSpectrum S.A,
      p.asIdeal ≤ r.asIdeal ∧ r.asIdeal ≤ q.asIdeal ∧
      r ∈ PrimeSpectrum.zeroLocus (S.I : Set S.A) ∧ r ∉ S.T) :
    enatToEInt
      (Module.depth (Localization.AtPrime p.asIdeal)
        (maximalIdeal (Localization.AtPrime p.asIdeal))
        (LocalizedModule p.asIdeal.primeCompl S.M)) > (S.s : EInt)
```

## Tag 0EFV, a lemma

[Tag 0EFV](https://stacks.math.columbia.edu/tag/0EFV) in the Stacks Project.

**`Stacks.Algebraization.finite_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean#L319). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (completion).** The completed module of a bootstrap situation is
> finite over the completed ring.

```lean
public theorem finite_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    Module.Finite (AdicCompletion S.I S.A) (AdicCompletion S.I S.M)
```

**`Stacks.Algebraization.subset_adicLocus_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean#L333). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (completion).** The completed locus is contained in the adic
> locus of the extended ideal.

```lean
public theorem subset_adicLocus_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    adicCompletionLocus S ⊆ PrimeSpectrum.zeroLocus
      ((S.I.map (algebraMap S.A (AdicCompletion S.I S.A))) :
        Set (AdicCompletion S.I S.A))
```

**`Stacks.Algebraization.stableUnderSpecialization_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean#L342). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (completion).** The completed locus is stable under
> specialization.

```lean
public theorem stableUnderSpecialization_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    StableUnderSpecialization (adicCompletionLocus S)
```

**`Stacks.Algebraization.dualizing_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean#L349). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (completion).** Assumption (1) completes: the adic completion of
> a ring with a dualizing complex has one.

```lean
public theorem dualizing_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    ∃ K : DerivedCategory (ModuleCat.{max u w} (AdicCompletion S.I S.A)),
      Dualizing.IsDualizingComplex K
```

**`Stacks.Algebraization.cohomologicalDimension_le_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean#L358). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (completion).** Assumption (3) completes: cohomological dimension
> does not increase.

```lean
public theorem cohomologicalDimension_le_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    Stacks.LocalCohomology.cohomologicalDimension (AdicCompletion S.I S.A)
      (S.I.map (algebraMap S.A (AdicCompletion S.I S.A)))
      (Ideal.fg_of_isNoetherianRing _) ≤ S.d
```

**`Stacks.Algebraization.completedLocalDepth_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletion.lean#L369). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (completion).** Assumption (6) completes: the strict depth bound
> on completed localizations persists after adic completion.

```lean
public theorem completedLocalDepth_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    ∀ q : PrimeSpectrum (AdicCompletion S.I S.A), q ∈ adicCompletionLocus S →
      let Aq := Localization.AtPrime q.asIdeal
      let Iq := (S.I.map (algebraMap S.A (AdicCompletion S.I S.A))).map
        (algebraMap (AdicCompletion S.I S.A) Aq)
      let Mq := LocalizedModule q.asIdeal.primeCompl (AdicCompletion S.I S.M)
      let A' := AdicCompletion Iq Aq
      let I' := Iq.map (algebraMap Aq A')
      let m' := (maximalIdeal Aq).map (algebraMap Aq A')
      ∀ p' : PrimeSpectrum A',
        ¬ I' ≤ p'.asIdeal →
        {r' : Ideal A' | r'.IsPrime ∧ p'.asIdeal ≤ r' ∧ I' ≤ r'} = {m'} →
        enatToEInt
          (Module.depth (Localization.AtPrime p'.asIdeal)
            (maximalIdeal (Localization.AtPrime p'.asIdeal))
            (LocalizedModule p'.asIdeal.primeCompl (AdicCompletion Iq Mq))) >
          (S.s : EInt)
```

**`Stacks.Algebraization.exists_localAlgebraizationHypotheses_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletionLocal.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletionLocal.lean#L194). The attribute's comment: “parts (G) and (D) for T = \{𝔪}: the hypotheses of Stacks 0DXP hold for the I-adic completion A', I', M' of A, I, M, whose locus is the closed point of A'”.

> In a bootstrap situation with `A` local and `T = {𝔪}`, there is an object `omega` of the
> derived category of `A'`-modules for which the `I`-adic completions `A'`, `I'`, `M'` satisfy the
> hypotheses `Stacks.Algebraization.LocalAlgebraizationHypotheses` of the local algebraization
> theorem.

```lean
public theorem exists_localAlgebraizationHypotheses_adicCompletion [IsLocalRing S.A]
    (hT : S.T = {closedPoint S.A}) :
    letI := BootstrapSituation.isLocalRing_adicCompletion_self S hT
    letI : Module.Finite (AdicCompletion S.I S.A) (AdicCompletion S.I S.M) :=
      finite_adicCompletion S
    ∃ omega : DerivedCategory (ModuleCat.{u} (AdicCompletion S.I S.A)),
      LocalAlgebraizationHypotheses (M := AdicCompletion S.I S.M)
        (S.I.map (algebraMap S.A (AdicCompletion S.I S.A))) S.s S.d omega
```

**`Stacks.Algebraization.depth_or_depth_add_dimension_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletionSituation.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletionSituation.lean#L52). The attribute's comment: “completion”.

> **Stacks Project, Tag 0EFV (G), assumption (4).** The chain-of-primes depth estimate of a
> bootstrap situation persists after `I`-adic completion, for the completed locus.

```lean
public theorem depth_or_depth_add_dimension_adicCompletion (S : BootstrapSituation.{u, v, w}) :
    ∀ p r q : PrimeSpectrum (AdicCompletion S.I S.A),
      p.asIdeal ≤ r.asIdeal → r.asIdeal ≤ q.asIdeal →
      p ∉ PrimeSpectrum.zeroLocus
        ((S.I.map (algebraMap S.A (AdicCompletion S.I S.A))) : Set (AdicCompletion S.I S.A)) →
      r ∈ PrimeSpectrum.zeroLocus
        ((S.I.map (algebraMap S.A (AdicCompletion S.I S.A))) : Set (AdicCompletion S.I S.A)) →
      r ∉ adicCompletionLocus S → q ∈ adicCompletionLocus S →
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl (AdicCompletion S.I S.M))) ≥ (S.s : EInt)) ∨
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl (AdicCompletion S.I S.M))) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap (AdicCompletion S.I S.A)
              (Localization.AtPrime q.asIdeal)))) >
        ((S.d + S.s : ℤ) : EInt))
```

**`Stacks.Algebraization.BootstrapSituation.adicCompletion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletionSituation.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCompletionSituation.lean#L103). The attribute's comment: “part (G): the completed quadruple is again a situation as in Stacks 0EFU”.

> **Stacks Project, Tag 0EFV (G).** The `I`-adic completion of a bootstrap situation: the
> completed ring `A^∧`, the extended ideal `I A^∧`, the completed module `M^∧` and the preimage of
> the locus, with the same bounds.

```lean
public def adicCompletion (S : BootstrapSituation.{u, v, w}) : BootstrapSituation.{u, v, w}
```

**`Stacks.Algebraization.depthGtOnAssociatedSubset_of_le_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean#L115). The attribute's comment: “part (A), hypothesis (6) of Stacks 0EFK for A, I, 𝔞, M”.

> **Stacks Project, Tag 0EFV, hypothesis (6) of Stacks 0EFK.** In a bootstrap situation whose
> ideal `I` lies in the Jacobson radical, a prime `𝔭 ∉ V(I)` all of whose specializations on
> `V(I)` lie on `V(𝔞)` has `depth(M_𝔭) > s`.
>
> A maximal ideal containing `𝔭` contains `I`, so `V(𝔭) ∩ V(I)` has a point `𝔮`, which lies on
> `V(𝔞)` and hence in `T`. No prime of `V(I) \ T` lies between `𝔭` and `𝔮`, since any prime of
> `V(𝔭) ∩ V(I)` lies on `V(𝔞) ⊆ T`; so Stacks 0EID gives the strict bound.

```lean
public theorem depthGtOnAssociatedSubset_of_le_jacobson
    (S : BootstrapSituation.{u, u, w}) (a : Ideal S.A) (_hIa : S.I ≤ a)
    (haT : PrimeSpectrum.zeroLocus (a : Set S.A) ⊆ S.T)
    (hjac : S.I ≤ (⊥ : Ideal S.A).jacobson) :
    DepthGtOnAssociatedSubset (M := S.M) S.I a S.s
```

**`Stacks.Algebraization.exists_mem_zeroLocus_dimension_le_of_le_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean#L137). The attribute's comment: “part (A), hypothesis (3) of Stacks 0EFI for A, I, 𝔞, M”.

> **Stacks Project, Tag 0EFV, hypothesis (3) of Stacks 0EFI.** In a bootstrap situation whose
> ideal `I` lies in the Jacobson radical, a prime `𝔭 ∉ V(I)` all of whose specializations on
> `V(I)` lie on `V(𝔞)` has one along which the relative dimension is at most `d`.
>
> This is Stacks 0DXF: a minimal prime `𝔮` of `𝔭 + I` has `dim((A/𝔭)_𝔮) ≤ cd(A, I) ≤ d`, and it
> lies on `V(𝔞)` because it lies on `V(𝔭) ∩ V(I)`.

```lean
public theorem exists_mem_zeroLocus_dimension_le_of_le_jacobson
    (S : BootstrapSituation.{u, v, w}) (a : Ideal S.A)
    (hjac : S.I ≤ (⊥ : Ideal S.A).jacobson)
    (p : PrimeSpectrum S.A)
    (hpT : p ∈ associatedSubset S.I a) :
    ∃ q : PrimeSpectrum S.A,
      q ∈ (PrimeSpectrum.zeroLocus (p.asIdeal : Set S.A) ∩
          PrimeSpectrum.zeroLocus (a : Set S.A)) ∩
          PrimeSpectrum.zeroLocus (S.I : Set S.A) ∧
      krullDimToEInt
        (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
          p.asIdeal.map (algebraMap S.A (Localization.AtPrime q.asIdeal)))) ≤
        (S.d : EInt)
```

**`Stacks.Algebraization.stabilizationHypotheses_and_depthGtOnAssociatedSubset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean#L164). The attribute's comment: “part (A): all hypotheses of Stacks 0EFI and Stacks 0EFK for A, I, 𝔞, M”.

> **Stacks Project, Tag 0EFV, part (A).** Let `S` be a bootstrap situation whose ideal `I` is
> contained in the Jacobson radical of `A`, and let `I ⊆ 𝔞` be an ideal with `V(𝔞) ⊆ T`. Then all
> hypotheses of Stacks 0EFI and of Stacks 0EFK hold for `A, I, 𝔞, M`.
>
> Hypothesis (1) is assumption (1) of the situation, hypothesis (2) is empty, hypothesis (3) is
> `Stacks.Algebraization.exists_mem_zeroLocus_dimension_le_of_le_jacobson`, hypothesis (4) is
> `Stacks.Algebraization.depth_or_depth_add_dimension_of_mem_zeroLocus`, and the extra hypothesis
> (6) of Stacks 0EFK is
> `Stacks.Algebraization.depthGtOnAssociatedSubset_of_le_jacobson`.

```lean
public theorem stabilizationHypotheses_and_depthGtOnAssociatedSubset
    (S : BootstrapSituation.{u, u, w}) (a : Ideal S.A) (hIa : S.I ≤ a)
    (haT : PrimeSpectrum.zeroLocus (a : Set S.A) ⊆ S.T)
    (hjac : S.I ≤ (⊥ : Ideal S.A).jacobson) :
    (∃ omega : DerivedCategory (ModuleCat.{max u w} S.A),
        StabilizationHypotheses (M := S.M) S.I a S.s S.d omega) ∧
      DepthGtOnAssociatedSubset (M := S.M) S.I a S.s
```

**`Stacks.Algebraization.algebraizationHypotheses_of_supplementaryBound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean#L190). The attribute's comment: “part (B): all hypotheses of Stacks 0EFL except possibly (5) for A, I, 𝔞, M”.

> **Stacks Project, Tag 0EFV, part (B).** Let `S` be a bootstrap situation whose ring is
> `I`-adically complete, and let `I ⊆ 𝔞` be an ideal with `V(𝔞) ⊆ T`. Then all hypotheses of
> Stacks 0EFL except possibly (5) hold for `A, I, 𝔞, M`: given a dimension function with its
> extreme values on `V(𝔞) ∩ V(I)` and given condition (5), the hypotheses of that lemma hold in
> full.
>
> Condition (1) is the completeness together with assumption (1) of the situation, condition (2)
> is empty, condition (3) is assumption (3) of the situation, and condition (4) is the same as
> condition (4) of Stacks 0EFI, proved in part (A).

```lean
public theorem algebraizationHypotheses_of_supplementaryBound
    (S : BootstrapSituation.{u, u, w}) (a : Ideal S.A) (_hIa : S.I ≤ a)
    (haT : PrimeSpectrum.zeroLocus (a : Set S.A) ⊆ S.T)
    (hcomplete : IsAdicComplete S.I S.A)
    (δ : PrimeSpectrum S.A → ℤ) (δmax δmin : ℤ)
    (hδ : IsDimensionFunctionProp δ)
    (hmax : IsGreatest (δ '' (PrimeSpectrum.zeroLocus (a : Set S.A) ∩
      PrimeSpectrum.zeroLocus (S.I : Set S.A))) δmax)
    (hmin : IsLeast (δ '' (PrimeSpectrum.zeroLocus (a : Set S.A) ∩
      PrimeSpectrum.zeroLocus (S.I : Set S.A))) δmin)
    (h5 : ∀ p : PrimeSpectrum S.A,
      p ∉ PrimeSpectrum.zeroLocus (S.I : Set S.A) →
      p ∉ associatedSubset S.I a →
      ((PrimeSpectrum.zeroLocus (p.asIdeal : Set S.A) ∩
        PrimeSpectrum.zeroLocus (a : Set S.A)) ∩
        PrimeSpectrum.zeroLocus (S.I : Set S.A)).Nonempty →
      enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl S.M)) < (S.s : EInt) →
      (krullDimToEInt (Module.supportDim (Localization.AtPrime p.asIdeal)
            (LocalizedModule p.asIdeal.primeCompl S.M)) < ((S.s + 2 : ℤ) : EInt) ∨
        (S.d + δmax - 1 < δ p) ∨
        (∀ q : PrimeSpectrum S.A,
          q ∈ (PrimeSpectrum.zeroLocus (p.asIdeal : Set S.A) ∩
            PrimeSpectrum.zeroLocus (a : Set S.A)) ∩
            PrimeSpectrum.zeroLocus (S.I : Set S.A) →
          enatToEInt
              (Module.depth (Localization.AtPrime p.asIdeal)
                (maximalIdeal (Localization.AtPrime p.asIdeal))
                (LocalizedModule p.asIdeal.primeCompl S.M)) +
              krullDimToEInt
                (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
                  p.asIdeal.map (algebraMap S.A (Localization.AtPrime q.asIdeal)))) >
            ((S.d + S.s + δmax - δmin - 2 : ℤ) : EInt)))) :
    ∃ omega : DerivedCategory (ModuleCat.{max u w} S.A),
      AlgebraizationHypotheses (M := S.M) S.I a S.s S.d omega δ δmax δmin
```

**`Stacks.Algebraization.localStabilizationHypotheses_and_depthGtAtMaximalIdeal_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean#L260). The attribute's comment: “part (C): all hypotheses of Stacks 0DXM and Stacks 0EFQ for A, 𝔪, I, M”.

> **Stacks Project, Tag 0EFV, part (C).** Let `S` be a bootstrap situation whose ring is local
> with maximal ideal `𝔪`, and suppose `𝔪 ∈ T`, which is the standing hypothesis `V(𝔞) ⊆ T` at
> `𝔞 = 𝔪`. Then all hypotheses of Stacks 0DXM and of Stacks 0EFQ hold for `A, 𝔪, I, M`.
>
> This is part (A) at `𝔞 = 𝔪`: in a local ring the Jacobson radical is the maximal ideal, which
> contains `I` because the closed point lies in `T ⊆ V(I)`. The hypotheses of Stacks 0DXM are
> those of Stacks 0EFI at `J = 𝔪` by `localStabilizationHypotheses_iff`, and hypothesis (6) of
> Stacks 0EFQ is hypothesis (6) of Stacks 0EFK there by
> `depthGtOnAssociatedSubset_maximalIdeal_iff`.

```lean
public theorem localStabilizationHypotheses_and_depthGtAtMaximalIdeal_of_mem
    (hmT : closedPoint S.A ∈ S.T) :
    (∃ omega : DerivedCategory (ModuleCat.{max u w} S.A),
        LocalStabilizationHypotheses (M := S.M) S.I S.s S.d omega) ∧
      DepthGtAtMaximalIdeal (M := S.M) S.I S.s
```

**`Stacks.Algebraization.localAlgebraizationHypotheses_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapHypotheses.lean#L281). The attribute's comment: “part (D): all hypotheses of Stacks 0DXP for A, 𝔪, I, M”.

> **Stacks Project, Tag 0EFV, part (D).** Let `S` be a bootstrap situation whose ring is local
> with maximal ideal `𝔪` and `I`-adically complete, and suppose `𝔪 ∈ T`, which is the standing
> hypothesis `V(𝔞) ⊆ T` at `𝔞 = 𝔪`. Then all hypotheses of Stacks 0DXP hold for `A, 𝔪, I, M`.
>
> Conditions (1) and (2) are the completeness together with assumption (1) of the situation,
> condition (3) is assumption (3) of the situation, and condition (4) is the same as condition (4)
> of Stacks 0DXM, proved in part (C).

```lean
public theorem localAlgebraizationHypotheses_of_mem
    (hcomplete : IsAdicComplete S.I S.A) (hmT : closedPoint S.A ∈ S.T) :
    ∃ omega : DerivedCategory (ModuleCat.{max u w} S.A),
      LocalAlgebraizationHypotheses (M := S.M) S.I S.s S.d omega
```

**`Stacks.Algebraization.localStabilizationHypotheses_and_depthGtAtMaximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean#L167). The attribute's comment: “part (C) for T = \{𝔪}: the hypotheses of Stacks 0DXM and hypothesis (6) of Stacks 0EFQ, with the dualizing complex of Situation 0EFU supplied as the witness omega”.

> In the bootstrap situation of Stacks 0EFU with `A` local and `T = {𝔪}`, the hypotheses
> (1)–(4) of Stacks 0DXM and hypothesis (6) of Stacks 0EFQ hold for `A, I, 𝔪, M`, for every
> dualizing complex `omega`.

```lean
public theorem localStabilizationHypotheses_and_depthGtAtMaximalIdeal [IsLocalRing S.A]
    (hT : S.T = {closedPoint S.A}) (omega : DerivedCategory (ModuleCat.{u} S.A))
    (homega : Dualizing.IsDualizingComplex omega) :
    LocalStabilizationHypotheses (M := S.M) S.I S.s S.d omega ∧
      DepthGtAtMaximalIdeal (M := S.M) S.I S.s
```

**`Stacks.Algebraization.subset_adicLocus_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L454). The attribute's comment: “localization”.

> The localized locus is contained in the adic locus of the extended ideal.

```lean
public theorem subset_adicLocus_localization
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
    locus X S ⊆ PrimeSpectrum.zeroLocus
      ((X.I.map (algebraMap X.A (Localization S))) : Set (Localization S))
```

**`Stacks.Algebraization.stableUnderSpecialization_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L462). The attribute's comment: “localization”.

> The localized locus is stable under specialization.

```lean
public theorem stableUnderSpecialization_localization
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
  StableUnderSpecialization (locus X S)
```

**`Stacks.Algebraization.dualizing_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L469). The attribute's comment: “localization”.

> Assumption (1) localizes: a localization of a ring with a dualizing complex has one.

```lean
public theorem dualizing_localization
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
    ∃ K : DerivedCategory (ModuleCat.{max u w} (Localization S)),
      Dualizing.IsDualizingComplex K
```

**`Stacks.Algebraization.cohomologicalDimension_le_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L478). The attribute's comment: “localization”.

> Assumption (3) localizes: cohomological dimension does not increase.

```lean
public theorem cohomologicalDimension_le_localization
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
    Stacks.LocalCohomology.cohomologicalDimension (Localization S)
      (X.I.map (algebraMap X.A (Localization S)))
      (Ideal.fg_of_isNoetherianRing _) ≤ X.d
```

**`Stacks.Algebraization.depth_or_depth_add_dimension_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L489). The attribute's comment: “localization”.

> Assumption (4) localizes: the chain-of-primes depth estimate holds for the localized data.

```lean
public theorem depth_or_depth_add_dimension_localization
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
    ∀ p r q : PrimeSpectrum (Localization S),
      p.asIdeal ≤ r.asIdeal → r.asIdeal ≤ q.asIdeal →
      p ∉ PrimeSpectrum.zeroLocus
        ((X.I.map (algebraMap X.A (Localization S))) : Set (Localization S)) →
      r ∈ PrimeSpectrum.zeroLocus
        ((X.I.map (algebraMap X.A (Localization S))) : Set (Localization S)) →
      r ∉ locus X S → q ∈ locus X S →
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl (LocalizedModule S X.M))) ≥
          (X.s : EInt)) ∨
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl (LocalizedModule S X.M))) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap (Localization S)
              (Localization.AtPrime q.asIdeal)))) >
        ((X.d + X.s : ℤ) : EInt))
```

**`Stacks.Algebraization.completedLocalDepth_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L532). The attribute's comment: “localization”.

> Assumption (6) localizes: the strict depth bound on completed localizations persists.

```lean
public theorem completedLocalDepth_localization
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
    ∀ q : PrimeSpectrum (Localization S), q ∈ locus X S →
      let Aq := Localization.AtPrime q.asIdeal
      let Iq := (X.I.map (algebraMap X.A (Localization S))).map
        (algebraMap (Localization S) Aq)
      let Mq := LocalizedModule q.asIdeal.primeCompl (LocalizedModule S X.M)
      let A' := AdicCompletion Iq Aq
      let I' := Iq.map (algebraMap Aq A')
      let m' := (maximalIdeal Aq).map (algebraMap Aq A')
      ∀ p' : PrimeSpectrum A',
        ¬ I' ≤ p'.asIdeal →
        {r' : Ideal A' | r'.IsPrime ∧ p'.asIdeal ≤ r' ∧ I' ≤ r'} = {m'} →
      enatToEInt
          (Module.depth (Localization.AtPrime p'.asIdeal)
            (maximalIdeal (Localization.AtPrime p'.asIdeal))
            (LocalizedModule p'.asIdeal.primeCompl (AdicCompletion Iq Mq))) >
          (X.s : EInt)
```

**`Stacks.Algebraization.BootstrapSituation.localize`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean, line 727](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalization.lean#L727). The attribute's comment: “part (F): for a multiplicative subset S ⊆ A the quadruple S⁻¹A, S⁻¹I, T', S⁻¹M, with T' the inverse image of T, is again a situation as in Stacks 0EFU”.

> **Stacks Project, Tag 0EFV, part (F).** The localization of a bootstrap situation at a
> multiplicative subset `S ⊆ A`: the quadruple `S⁻¹A, S⁻¹I, T', S⁻¹M`, with `T'` the inverse image
> of `T` in `V(S⁻¹I)`, again satisfies every assumption of Situation 0EFU, with the same bounds
> `s` and `d`.

```lean
public def localize
    (X : BootstrapSituation.{u, v, w}) (S : Submonoid X.A) :
    BootstrapSituation.{u, max u v, w}
```

**`Stacks.Algebraization.depth_or_depth_add_dimension_of_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapShrink.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapShrink.lean#L42). The attribute's comment: “shrinking\_t”.

> **Stacks Project, Tag 0EFV (shrinking `T`).** The chain-of-primes depth estimate of a
> bootstrap situation persists after restricting its locus to any subset.

```lean
public theorem depth_or_depth_add_dimension_of_subset
    (S : BootstrapSituation.{u, v, w})
    (T' : Set (PrimeSpectrum S.A)) (hsub : T' ⊆ S.T) :
    ∀ p r q : PrimeSpectrum S.A,
      p.asIdeal ≤ r.asIdeal → r.asIdeal ≤ q.asIdeal →
      p ∉ PrimeSpectrum.zeroLocus (S.I : Set S.A) →
      r ∈ PrimeSpectrum.zeroLocus (S.I : Set S.A) → r ∉ T' → q ∈ T' →
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl S.M)) ≥ (S.s : EInt)) ∨
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl S.M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap S.A (Localization.AtPrime q.asIdeal)))) >
        ((S.d + S.s : ℤ) : EInt))
```

**`Stacks.Algebraization.BootstrapSituation.shrink`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapShrink.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapShrink.lean#L74). The attribute's comment: “part (E): for a smaller specialization-stable T' ⊆ T the quadruple A, I, T', M is again a situation as in Stacks 0EFU”.

> **Stacks Project, Tag 0EFV, part (E).** The bootstrap situation obtained by restricting the
> locus of `S` to a smaller specialization-stable subset: `A, I, T', M` with `T' ⊆ T` again
> satisfies every assumption of Situation 0EFU, with the same bounds `s` and `d`.

```lean
public def BootstrapSituation.shrink
    (S : BootstrapSituation.{u, v, w})
    (T' : Set (PrimeSpectrum S.A)) (hsub : T' ⊆ S.T)
    (hstable : StableUnderSpecialization T') :
    BootstrapSituation.{u, v, w}
```

## Tag 0EFR, a lemma

[Tag 0EFR](https://stacks.math.columbia.edu/tag/0EFR) in the Stacks Project.

**`Stacks.Algebraization.exists_pow_le_annihilator_localCohomologyModule_of_eq_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean#L207). The attribute's comment: “the annihilation assertion: Hⁱ\_𝔪(M) is annihilated by a power of I for i ≤ s”.

> In the bootstrap situation of Stacks 0EFU with `A` local and `T = {𝔪}`, a single power of
> `I` annihilates `Hⁱ_𝔪(M)` in every degree `i ≤ s`.

```lean
public theorem exists_pow_le_annihilator_localCohomologyModule_of_eq_closedPoint
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) :
    ∃ n : ℕ, ∀ i : ℤ, i ≤ S.s →
      S.I ^ n ≤ Module.annihilator S.A
        (Stacks.LocalCohomology.localCohomologyModule S.A (maximalIdeal S.A)
          (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) i)
```

**`Stacks.Algebraization.isIso_localCohomologyToAdicQuotientLimit_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean#L341). The attribute's comment: “both assertions, with no carried hypothesis, for I-adically complete A”.

> In the bootstrap situation of Stacks 0EFU with `A` local, `I`-adically complete and
> `T = {𝔪}`, the map `Hⁱ_𝔪(M) ⟶ lim Hⁱ_𝔪(M/IⁿM)` is an isomorphism for `i ≤ s` and a single
> power of `I` annihilates these modules.

```lean
public theorem isIso_localCohomologyToAdicQuotientLimit_of_isAdicComplete
    [IsLocalRing S.A] [IsAdicComplete S.I S.A] (hT : S.T = {closedPoint S.A}) :
    (∀ i : ℤ, i ≤ S.s →
        IsIso (localCohomologyToAdicQuotientLimit S.A S.I (maximalIdeal S.A)
          (maximalIdeal S.A) (ModuleCat.of S.A S.M) rfl i)) ∧
      ∃ n : ℕ, ∀ i : ℤ, i ≤ S.s →
        S.I ^ n ≤ Module.annihilator S.A
          (Stacks.LocalCohomology.localCohomologyModule S.A (maximalIdeal S.A)
            (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) i)
```

**`Stacks.Algebraization.isIso_localCohomologyToAdicQuotientLimit_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean#L387). The attribute's comment: “both assertions read over the I-adic completion A', I', M' of the situation, for an arbitrary A: Hⁱ\_\{𝔪'}(M') → lim Hⁱ\_\{𝔪'}(M'/(I')ⁿM') is an isomorphism for i ≤ s and a power of I' annihilates these modules. No completeness assumption on A; this is the statement the source's proof establishes over the completion”.

> In the bootstrap situation with `A` local and `T = {𝔪}`, over the `I`-adic completion
> `A', I', M'`: the map `Hⁱ_{𝔪'}(M') ⟶ lim Hⁱ_{𝔪'}(M'/(I')ⁿM')` is an isomorphism for `i ≤ s`,
> and a single power of `I'` annihilates these modules. Nothing is assumed about `A` beyond
> Situation 0EFU and the locality of the locus.

```lean
public theorem isIso_localCohomologyToAdicQuotientLimit_adicCompletion
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) :
    letI : IsLocalRing S.adicCompletion.A :=
      BootstrapSituation.isLocalRing_adicCompletion S hT
    (∀ i : ℤ, i ≤ S.adicCompletion.s →
        IsIso (localCohomologyToAdicQuotientLimit S.adicCompletion.A S.adicCompletion.I
          (maximalIdeal S.adicCompletion.A) (maximalIdeal S.adicCompletion.A)
          (ModuleCat.of S.adicCompletion.A S.adicCompletion.M) rfl i)) ∧
      ∃ n : ℕ, ∀ i : ℤ, i ≤ S.adicCompletion.s →
        S.adicCompletion.I ^ n ≤ Module.annihilator S.adicCompletion.A
          (Stacks.LocalCohomology.localCohomologyModule S.adicCompletion.A
            (maximalIdeal S.adicCompletion.A) (Ideal.fg_of_isNoetherianRing _)
            (ModuleCat.of S.adicCompletion.A S.adicCompletion.M) i)
```

**`Stacks.Algebraization.isIso_localCohomologyToAdicQuotientLimit_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/CompletionUnitDescent.lean, line 621](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/CompletionUnitDescent.lean#L621). The attribute's comment: “both assertions over A itself for every Noetherian local ring: in Situation 0EFU with A local and T = \{𝔪}, the map Hⁱ\_𝔪(M) → lim Hⁱ\_𝔪(M/IⁿM) is an isomorphism for i ≤ s and a single power of I annihilates these modules”.

> **Stacks 0EFR.** In the bootstrap situation of Stacks 0EFU with `A` local and
> `T = {𝔪}`, the map `Hⁱ_𝔪(M) ⟶ lim Hⁱ_𝔪(M/IⁿM)` is an isomorphism for `i ≤ s`, and a single power
> of `I` annihilates these modules. Nothing is assumed about `A` beyond Situation 0EFU and the
> locality of the locus; in particular `A` need not be `I`-adically complete.
>
> The isomorphism is the composite of the two displays of the source's proof. The first,
> `Hⁱ_𝔪(M) ≅ Hⁱ(RΓ_𝔪(M)^∧)`, is
> `Stacks.Algebraization.isIso_homology_localCohomologyToCompletedLocalCohomology_closedPoint`,
> which obtains it over the `I`-adic completion from Stacks 0DXP and Stacks 0EFQ and descends it;
> the second, `Hⁱ(RΓ_𝔪(M)^∧) ≅ lim Hⁱ_𝔪(M/IⁿM)`, is Stacks 0DXJ. The annihilation assertion is
> `Stacks.Algebraization.exists_pow_le_annihilator_localCohomologyModule_of_eq_closedPoint`, which
> needs only Stacks 0EFQ over `A` itself.

```lean
public theorem isIso_localCohomologyToAdicQuotientLimit_closedPoint
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) :
    (∀ i : ℤ, i ≤ S.s →
        IsIso (localCohomologyToAdicQuotientLimit S.A S.I (maximalIdeal S.A)
          (maximalIdeal S.A) (ModuleCat.of S.A S.M) rfl i)) ∧
      ∃ n : ℕ, ∀ i : ℤ, i ≤ S.s →
        S.I ^ n ≤ Module.annihilator S.A
          (Stacks.LocalCohomology.localCohomologyModule S.A (maximalIdeal S.A)
            (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) i)
```

## Tag 0EFW, a lemma

[Tag 0EFW](https://stacks.math.columbia.edu/tag/0EFW) in the Stacks Project.

**`Stacks.Algebraization.exists_bootstrapSituation_of_depth_gt_or_depth_add_dim_gt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/AlgebraizationLocalCohomologyIIIBootstrapCriterion.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/AlgebraizationLocalCohomologyIIIBootstrapCriterion.lean#L160).

> **Stacks Project, Tag 0EFW.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A` admitting a
> dualizing complex, let `M` be a finite `A`-module and let `s`, `d` be integers with
> `cd(A, I) ≤ d`. If for every prime `p ∉ V(I)` and every `q ∈ V(p) ∩ V(𝔞)` either
> `depth(M_p) > s` or `depth(M_p) + dim((A/p)_q) > d + s`, then `A`, `I`, `V(𝔞)`, `M`, `s`, `d`
> are as in the bootstrap situation of Stacks 0EFU.

```lean
public theorem exists_bootstrapSituation_of_depth_gt_or_depth_add_dim_gt
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I a : Ideal A) (hIa : I ≤ a)
    {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (s d : ℤ)
    (hdual : ∃ K : DerivedCategory (ModuleCat.{max u w} A), Dualizing.IsDualizingComplex K)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A I
      (Ideal.fg_of_isNoetherianRing I) ≤ d)
    (hdepth : ∀ p q : PrimeSpectrum A,
      p.asIdeal ≤ q.asIdeal →
      p ∉ PrimeSpectrum.zeroLocus (I : Set A) →
      q ∈ PrimeSpectrum.zeroLocus (a : Set A) →
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M)) > (s : EInt)) ∨
      (enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M)) +
        krullDimToEInt
          (ringKrullDim ((Localization.AtPrime q.asIdeal) ⧸
            p.asIdeal.map (algebraMap A (Localization.AtPrime q.asIdeal)))) >
        ((d + s : ℤ) : EInt))) :
    ∃ S : BootstrapSituation.{u, v, w},
      S.A = A ∧
      HEq S.commRing (inferInstance : CommRing A) ∧
      HEq S.isNoetherianRing (inferInstance : IsNoetherianRing A) ∧
      HEq S.I I ∧ S.M = M ∧
      HEq S.addCommGroup (inferInstance : AddCommGroup M) ∧
      HEq S.module (inferInstance : Module A M) ∧
      HEq S.finite (inferInstance : Module.Finite A M) ∧
      HEq S.T (PrimeSpectrum.zeroLocus (a : Set A)) ∧
      S.s = s ∧ S.d = d
```

## Tag 0EFX, a lemma

[Tag 0EFX](https://stacks.math.columbia.edu/tag/0EFX) in the Stacks Project.

**`Stacks.Algebraization.exists_map_idealPowerTower_eq_zero_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapClosedPointProZero.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapClosedPointProZero.lean#L525). The attribute's comment: “the pro-zero assertion for i ≤ s at T = \{𝔪} over a Noetherian local ring in Situation 0EFU”.

> **Stacks Project, Tag 0EFX, the pro-zero assertion, at `T = {𝔪}`.** In Situation
> [Stacks, Tag 0EFU] with `A` local and `T = {𝔪}`, the inverse system `{H^i_𝔪(IⁿM)}` is pro-zero
> for every `i ≤ s`: for every `m` some transition map `H^i_𝔪(IᵏM) ⟶ H^i_𝔪(IᵐM)` vanishes.
>
> This is the first paragraph of the source's proof, carried out at this locus. Its two inputs are
> `isIso_limitLift_localCohomologyAdicCone_closedPoint`, which is part (4) of [Stacks, Tag 0EFY]
> and the isomorphism assertion of [Stacks, Tag 0EFR] in the set-indexed model, and the
> Artinianness of local cohomology at the closed point of a finite module, which supplies both
> part (1) of [Stacks, Tag 0EFY] (through a descending chain of kernels) and the Mittag-Leffler
> condition in the range form that the eventual-range lemma consumes. Nothing beyond the situation
> is assumed; in particular `A` need not be `I`-adically complete.
>
> The source's `T` is an arbitrary specialization-stable subset of `V(I)`. The general case is the
> last paragraph of the source's proof: it needs the per-prime assertion **uniformly** in `𝔮 ∈ T`,
> which the source gets by transporting the vanishing to the finite Ext modules
> `Ext^j_A(IⁿM, ω_A^•)` by local duality and spreading it out. The statement proved here is exactly
> the per-prime input of that argument at a single prime, since
> `Stacks.Algebraization.BootstrapSituation.localize` and
> `Stacks.Algebraization.BootstrapSituation.shrink` turn a situation and a `𝔮 ∈ T` into a situation
> over `A_𝔮` with locus the closed point.

```lean
theorem exists_map_idealPowerTower_eq_zero_closedPoint [IsLocalRing S.A]
    (hT : S.T = {closedPoint S.A}) (i : ℤ) (hi : i ≤ S.s) (m : ℕ) :
    ∃ k : ℕ, ∃ h : m ≤ k,
      (localCohomologyWithSupportInModuleFunctor.{u, u} S.A S.T i).map
        ((idealPowerTower.{u, u} S.I (ModuleCat.of S.A S.M)).map (homOfLE h).op) = 0
```

**`Stacks.Algebraization.hasStableImageIdealPowerCohomology_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapClosedPointProZero.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapClosedPointProZero.lean#L556). The attribute's comment: “the stable-image assertion in degree s + 1 at T = \{𝔪} over a Noetherian local ring in Situation 0EFU”.

> **Stacks Project, Tag 0EFX, the stable-image assertion, at `T = {𝔪}`.** In Situation
> [Stacks, Tag 0EFU] with `A` local and `T = {𝔪}`, the stable-image assertion of the tag holds in
> degree `s + 1`, based at `m₀ = 0`: for every `m` there is a `c ≥ m` such that for `k ≥ c` the
> image of `H^{s+1}_𝔪(IᵏM) ⟶ H^{s+1}_𝔪(IᵐM)` maps injectively to `H^{s+1}_𝔪(I⁰M)`.
>
> Its single input is the invertibility of the limit comparison in degree `s` itself, which is
> inside the range `i ≤ s` of `isIso_limitLift_localCohomologyAdicCone_closedPoint`; the
> Artinianness of the terms turns it into the containment of the stable images in the image of
> `H^s_𝔪(M)`, and the naturality of the connecting map of
> `0 → IⁿM → M → M/IⁿM → 0` does the rest. Nothing beyond the situation is assumed.
>
> As with the pro-zero assertion, the general specialization-stable `T` needs the uniformity in
> `𝔮 ∈ T` of the source's last paragraph; see
> `exists_map_idealPowerTower_eq_zero_closedPoint`.

```lean
theorem hasStableImageIdealPowerCohomology_closedPoint [IsLocalRing S.A]
    (hT : S.T = {closedPoint S.A}) :
    HasStableImageIdealPowerCohomology.{u, u} S.T S.I (ModuleCat.of S.A S.M) (S.s + 1) 0
```

**`Stacks.Algebraization.exists_map_idealPowerTower_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean#L280). The attribute's comment: “the pro-zero assertion in degrees 0 ≤ i ≤ s at a general specialization-stable T in Situation 0EFU”.

> **Stacks Project, Tag 0EFX**, the pro-zero assertion, at a general specialization-stable `T`.
> In Situation [Stacks, Tag 0EFU] the inverse system `{H^i_T(IⁿM)}` is pro-zero for every `i ≤ s`:
> for every `m` some transition map `H^i_T(IᵏM) ⟶ H^i_T(IᵐM)` vanishes.
>
> This is the source's proof carried out in full. The per-prime assertion at each `𝔮 ∈ T` is
> `Stacks.Algebraization.exists_localized_localCohomology_idealPowerTower_map_eq_zero`; its bound
> is made independent of `𝔮` by
> `Stacks.Algebraization.exists_forall_localized_localCohomology_map_eq_zero`, which is the
> local-duality paragraph; and the passage from the uniform per-prime statement to the global one
> is `Stacks.Algebraization.exists_map_idealPowerTower_eq_zero_of_uniform`, i.e. Lemma
> [Stacks, Tag 0EF9]. Nothing is assumed beyond the data of Situation [Stacks, Tag 0EFU].

```lean
theorem exists_map_idealPowerTower_eq_zero (S : BootstrapSituation.{u, u, u}) (i : ℕ)
    (hi : (i : ℤ) ≤ S.s) (m : ℕ) :
    ∃ k : ℕ, ∃ h : m ≤ k,
      (localCohomologyWithSupportInModuleFunctor.{u, u} S.A S.T (i : ℤ)).map
        ((idealPowerTower.{u, u} S.I (ModuleCat.of S.A S.M)).map (homOfLE h).op) = 0
```

**`Stacks.Algebraization.isProZeroIdealPowerCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean#L301). The attribute's comment: “the pro-zero assertion in every degree i ≤ s at a general specialization-stable T in Situation 0EFU”.

> **Stacks Project, Tag 0EFX**, the pro-zero assertion, in **every** degree `i ≤ s` and at a
> general specialization-stable `T`. In Situation [Stacks, Tag 0EFU] the inverse system
> `{H^i_T(IⁿM)}` is pro-zero for every `i ≤ s`: for every `m` some transition map
> `H^i_T(IᵏM) ⟶ H^i_T(IᵐM)` vanishes.
>
> In negative degrees the system vanishes term by term
> (`Stacks.LocalCohomology.exists_map_idealPowerTower_eq_zero_of_neg`); in degrees `0 ≤ i ≤ s`
> this is `Stacks.Algebraization.exists_map_idealPowerTower_eq_zero`, whose proof is the source's
> own, the local-duality paragraph included. This is also the form in which the consequences of
> [Stacks, Tag 0EFY] consume the assertion.

```lean
theorem isProZeroIdealPowerCohomology (S : BootstrapSituation.{u, u, u}) (i : ℤ)
    (hi : i ≤ S.s) :
    IsProZeroIdealPowerCohomology.{u, u} S.T S.I (ModuleCat.of S.A S.M) i
```

**`Stacks.Algebraization.exists_hasStableImageIdealPowerCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean#L274). The attribute's comment: “the stable-image assertion in degree s + 1 at a general specialization-stable T in Situation 0EFU”.

> **Stacks Project, Tag 0EFX**, the stable-image assertion, at a general specialization-stable
> `T`. In Situation [Stacks, Tag 0EFU] there is an `m₀` such that for every `m ≥ m₀` there is an
> `m'(m) ≥ m` with: for `k ≥ m'(m)` the image of `H^{s+1}_T(IᵏM) ⟶ H^{s+1}_T(IᵐM)` maps injectively
> into `H^{s+1}_T(I^{m₀}M)`.
>
> This is the source's proof carried out in full. The per-prime assertion at each `𝔮 ∈ T` is
> `Stacks.Algebraization.exists_localized_ker_le_ker_idealPowerTower`; its bound is made independent
> of `𝔮` by `Stacks.Algebraization.exists_forall_localized_ker_le_ker_idealPowerTower`, which is the
> local-duality paragraph in the degree the tag states this assertion in; and the passage from the
> uniform per-prime statement to the global one is Lemma [Stacks, Tag 0EFA]. In negative degrees the
> system vanishes term by term. Nothing is assumed beyond the data of Situation
> [Stacks, Tag 0EFU].

```lean
theorem exists_hasStableImageIdealPowerCohomology (S : BootstrapSituation.{u, u, u}) :
    ∃ m₀ : ℕ, HasStableImageIdealPowerCohomology.{u, u} S.T S.I (ModuleCat.of S.A S.M)
      (S.s + 1) m₀
```

**`Stacks.Algebraization.isProZero_and_hasStableImage_idealPowerCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean#L307).

> **Stacks Project, Tag 0EFX** at a general specialization-stable `T`: both assertions. In
> Situation [Stacks, Tag 0EFU] the inverse systems `{H^i_T(IⁿM)}` are pro-zero for `i ≤ s`, and
> there is an `m₀` such that for every `m ≥ m₀` there is an `m'(m) ≥ m` with: for `k ≥ m'(m)` the
> image of `H^{s+1}_T(IᵏM) ⟶ H^{s+1}_T(IᵐM)` maps injectively into `H^{s+1}_T(I^{m₀}M)`.
>
> The first assertion is `Stacks.Algebraization.isProZeroIdealPowerCohomology` and the second
> `Stacks.Algebraization.exists_hasStableImageIdealPowerCohomology`. Both are the source's own
> proof, the local-duality paragraph included; nothing beyond the data of Situation
> [Stacks, Tag 0EFU] is assumed.

```lean
theorem isProZero_and_hasStableImage_idealPowerCohomology (S : BootstrapSituation.{u, u, u}) :
    (∀ i ≤ S.s, IsProZeroIdealPowerCohomology.{u, u} S.T S.I (ModuleCat.of S.A S.M) i) ∧
      ∃ m₀ : ℕ, HasStableImageIdealPowerCohomology.{u, u} S.T S.I (ModuleCat.of S.A S.M)
        (S.s + 1) m₀
```

**`Stacks.LocalCohomology.exists_map_idealPowerTower_eq_zero_of_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean#L199). The attribute's comment: “the pro-zero assertion, from the per-prime vanishing taken as an explicit hypothesis; that per-prime vanishing is the local-duality half of the source's proof and is not proved here”.

> **Stacks Project, Tag 0EFX**, the pro-zero assertion, globalized. If for every `m` the
> transition maps `H^i_{𝔭A_𝔭}((IᵏM)_𝔭) → H^i_{𝔭A_𝔭}((IᵐM)_𝔭)` vanish for every `𝔭 ∈ T` and every
> `k ≥ m'(m)`, then the inverse system `{H^i_T(IⁿM)}` is pro-zero: for every `m` some transition
> map into the `m`-th term is zero.
>
> This is the last paragraph of the source's proof, which reduces the lemma to the per-prime
> assertion: the reduction is Lemma [Stacks, Tag 0EF9], applied to the tower `{IⁿM}`. The per-prime
> assertion itself, which the source proves by local duality, is the hypothesis `hlocal`.

```lean
theorem exists_map_idealPowerTower_eq_zero_of_local [IsNoetherianRing A]
    (hdim : ringKrullDim A < ⊤) (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (I : Ideal A) (M : ModuleCat.{max u v} A) (i : ℕ) (m' : ℕ → ℕ) (hm' : ∀ m, m ≤ m' m)
    (hlocal : ∀ (m k : ℕ) (_hbound : m' m ≤ k), ∀ p : PrimeSpectrum A, p ∈ T →
      ((ModuleCat.localizedModuleFunctor.{max u v} p.asIdeal.primeCompl ⋙
        localCohomologyModuleFunctor (Localization p.asIdeal.primeCompl) (i : ℤ)).map
        ((idealPowerTower.{u, v} I M).map (homOfLE ((hm' m).trans _hbound)).op) = 0))
    (m : ℕ) :
    ∃ k : ℕ, ∃ h : m ≤ k,
      (localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
        ((idealPowerTower.{u, v} I M).map (homOfLE h).op) = 0
```

**`Stacks.LocalCohomology.exists_eventually_injective_image_idealPowerTower_of_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean#L228). The attribute's comment: “the stable-image assertion in degree s + 1, from the per-prime stable-image hypothesis taken as an explicit hypothesis; that per-prime hypothesis is the local-duality half of the source's proof and is not proved here”.

> **Stacks Project, Tag 0EFX**, the stable-image assertion, globalized. If for every `m` there
> is a `c ≥ m` such that at every `𝔭 ∈ T` and for every `k ≥ c` the transition map of
> `{H^{i-1}_{𝔭A_𝔭}((IⁿM)_𝔭)}` vanishes, the transition image of `{H^i_{𝔭A_𝔭}((IⁿM)_𝔭)}` is
> independent of `k` and that image injects into the zeroth term, then there is an `m₀` such that
> for every `m ≥ m₀` the image of `H^i_T(IᵏM) → H^i_T(IᵐM)` injects into `H^i_T(I^{m₀}M)` for all
> large `k`.
>
> This is the reduction Lemma [Stacks, Tag 0EFA], applied to the tower `{IⁿM}`; in the source it is
> applied in degree `i = s + 1`. The per-prime hypothesis `hloc` is the local-duality half of the
> source's proof and is not proved here.

```lean
theorem exists_eventually_injective_image_idealPowerTower_of_local [IsNoetherianRing A]
    (hdim : ringKrullDim A < ⊤) (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (I : Ideal A) (M : ModuleCat.{max u v} A) (i : ℕ)
    (hloc : ∀ m : ℕ, ∃ c : ℕ, ∃ hmc : m ≤ c, ∀ p ∈ T, ∀ (k : ℕ) (hck : c ≤ k),
      ((idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
        p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
          (Localization p.asIdeal.primeCompl) ((i : ℤ) - 1)).map
            (homOfLE (hmc.trans hck)).op = 0) ∧
      (LinearMap.range ((idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).map (homOfLE (hmc.trans hck)).op).hom =
        LinearMap.range ((idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).map (homOfLE hmc).op).hom) ∧
      (∀ x : (idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).obj (op k),
        ((idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).map
              (homOfLE (hmc.trans hck)).op).hom x ∈
          LinearMap.ker ((idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
            p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
              (Localization p.asIdeal.primeCompl) (i : ℤ)).map
                (homOfLE (Nat.zero_le m)).op).hom →
        ((idealPowerTower.{u, v} I M ⋙ ModuleCat.localizedModuleFunctor.{max u v}
          p.asIdeal.primeCompl ⋙ localCohomologyModuleFunctor
            (Localization p.asIdeal.primeCompl) (i : ℤ)).map
              (homOfLE (hmc.trans hck)).op).hom x = 0)) :
    ∃ m₀ : ℕ, ∀ (m : ℕ) (hm₀m : m₀ ≤ m), ∃ c : ℕ, ∃ hmc : m ≤ c, ∀ (k : ℕ) (hck : c ≤ k),
      ∀ x : (idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).obj (op k),
        ((idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
            (homOfLE (hmc.trans hck)).op).hom x ∈
          LinearMap.ker ((idealPowerTower.{u, v} I M ⋙
            localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
              (homOfLE hm₀m).op).hom →
        ((idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T (i : ℤ)).map
            (homOfLE (hmc.trans hck)).op).hom x = 0
```

**`Stacks.LocalCohomology.exists_map_idealPowerTower_eq_zero_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean#L275). The attribute's comment: “the pro-zero assertion in negative degrees, unconditionally”.

> **Stacks Project, Tag 0EFX** in negative degrees, with no hypothesis. For `i < 0` every term
> of `{H^i_T(IⁿM)}` vanishes, so every transition map is zero and the system is pro-zero.

```lean
theorem exists_map_idealPowerTower_eq_zero_of_neg (T : Set (PrimeSpectrum A)) (I : Ideal A)
    (M : ModuleCat.{max u v} A) (i : ℤ) (hi : i < 0) (m : ℕ) :
    ∃ k : ℕ, ∃ h : m ≤ k,
      (localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
        ((idealPowerTower.{u, v} I M).map (homOfLE h).op) = 0
```

**`Stacks.LocalCohomology.exists_eventually_injective_image_idealPowerTower_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZeroLowDegree.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZeroLowDegree.lean#L188). The attribute's comment: “the stable-image assertion in negative degrees, unconditionally”.

> **Stacks Project, Tag 0EFX**, the stable-image assertion, in negative degrees and with no
> hypothesis. The assertion is that there is an `m₀` such that for every `m ≥ m₀` there is a
> `c ≥ m` beyond which the image of `H^i_T(IᵏM) → H^i_T(IᵐM)` maps injectively to
> `H^i_T(I^{m₀}M)`. For `i < 0` every term `H^i_T(IⁿM)` of the system vanishes, so `m₀ = 0` serves
> and the injectivity is automatic.
>
> This is the companion of `exists_map_idealPowerTower_eq_zero_of_neg`, and it covers the degree
> `s + 1` at which the source states the stable-image assertion exactly when `s < -1`. The
> conclusion is the conclusion of
> `exists_eventually_injective_image_idealPowerTower_of_local` verbatim, so the two theorems prove
> the same assertion in complementary ranges of the degree.

```lean
theorem exists_eventually_injective_image_idealPowerTower_of_neg (T : Set (PrimeSpectrum A))
    (I : Ideal A) (M : ModuleCat.{max u v} A) (i : ℤ) (hi : i < 0) :
    ∃ m₀ : ℕ, ∀ (m : ℕ) (hm₀m : m₀ ≤ m), ∃ c : ℕ, ∃ hmc : m ≤ c, ∀ (k : ℕ) (hck : c ≤ k),
      ∀ x : (idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T i).obj (op k),
        ((idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
            (homOfLE (hmc.trans hck)).op).hom x ∈
          LinearMap.ker ((idealPowerTower.{u, v} I M ⋙
            localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
              (homOfLE hm₀m).op).hom →
        ((idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
            (homOfLE (hmc.trans hck)).op).hom x = 0
```

**`Stacks.LocalCohomology.exists_map_idealPowerTower_eq_zero_of_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZeroLowDegree.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZeroLowDegree.lean#L296). The attribute's comment: “the pro-zero assertion in degrees i ≤ 0, for A Noetherian, M finite and T ⊆ V(I)”.

> **Stacks Project, Tag 0EFX**, the pro-zero assertion in degrees `i ≤ 0`, with no hypothesis
> beyond the data of Situation [Stacks, Tag 0EFU]: `A` Noetherian, `M` finite and `T ⊆ V(I)`. For
> `i < 0` every term of `{H^i_T(IⁿM)}` vanishes; in degree `0` the terms vanish from some index on,
> by `exists_isZero_localCohomologyWithSupportIn_idealPowerTower_zero`. In either case a transition
> map out of a vanishing term is zero.
>
> Together with the stable-image companion
> `exists_eventually_injective_image_idealPowerTower_of_le_zero` this proves both assertions of the
> tag whenever `s < 0`: the pro-zero assertion is asserted for `i ≤ s` and the stable-image
> assertion in degree `s + 1`.

```lean
theorem exists_map_idealPowerTower_eq_zero_of_le_zero [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (I : Ideal A)
    (hT : T ⊆ PrimeSpectrum.zeroLocus (I : Set A)) (M : ModuleCat.{max u v} A)
    [Module.Finite A M] (i : ℤ) (hi : i ≤ 0) (m : ℕ) :
    ∃ k : ℕ, ∃ h : m ≤ k,
      (localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
        ((idealPowerTower.{u, v} I M).map (homOfLE h).op) = 0
```

**`Stacks.LocalCohomology.exists_eventually_injective_image_idealPowerTower_of_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZeroLowDegree.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZeroLowDegree.lean#L323). The attribute's comment: “the stable-image assertion in degrees i ≤ 0, for A Noetherian, M finite and T ⊆ V(I)”.

> **Stacks Project, Tag 0EFX**, the stable-image assertion in degrees `i ≤ 0`, with no
> hypothesis beyond the data of Situation [Stacks, Tag 0EFU]: `A` Noetherian, `M` finite and
> `T ⊆ V(I)`. The assertion is that there is an `m₀` such that for every `m ≥ m₀` there is a
> `c ≥ m` beyond which the image of `H^i_T(IᵏM) → H^i_T(IᵐM)` maps injectively to `H^i_T(I^{m₀}M)`.
>
> For `i < 0` every term vanishes and `m₀ = 0` serves. In degree `0` the terms vanish from the
> index `c` of `exists_isZero_localCohomologyWithSupportIn_idealPowerTower_zero` on, so `m₀ = c`
> serves: every class in a vanishing target is zero. The conclusion is the conclusion of
> `exists_eventually_injective_image_idealPowerTower_of_local` verbatim.
>
> This covers the degree `s + 1` at which the source states the stable-image assertion exactly
> when `s < 0`.

```lean
theorem exists_eventually_injective_image_idealPowerTower_of_le_zero [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (I : Ideal A)
    (hT : T ⊆ PrimeSpectrum.zeroLocus (I : Set A)) (M : ModuleCat.{max u v} A)
    [Module.Finite A M] (i : ℤ) (hi : i ≤ 0) :
    ∃ m₀ : ℕ, ∀ (m : ℕ) (hm₀m : m₀ ≤ m), ∃ c : ℕ, ∃ hmc : m ≤ c, ∀ (k : ℕ) (hck : c ≤ k),
      ∀ x : (idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T i).obj (op k),
        ((idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
            (homOfLE (hmc.trans hck)).op).hom x ∈
          LinearMap.ker ((idealPowerTower.{u, v} I M ⋙
            localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
              (homOfLE hm₀m).op).hom →
        ((idealPowerTower.{u, v} I M ⋙
          localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
            (homOfLE (hmc.trans hck)).op).hom x = 0
```

## Tag 0EFY, a lemma

[Tag 0EFY](https://stacks.math.columbia.edu/tag/0EFY) in the Stacks Project.

**`Stacks.Algebraization.isIso_localCohomologyAdicQuotientToLimit_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCanonicalAdicLimit.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCanonicalAdicLimit.lean#L140). The attribute's comment: “part (4) at T = \{𝔪} over a Noetherian local ring in Situation 0EFU, read at the canonical comparison Hⁱ\_𝔪(M) ⟶ lim Hⁱ\_𝔪(M/IⁿM), in the range i ≤ s and with no completeness assumption on A”.

> **The canonical comparison `Hⁱ_𝔪(M) ⟶ lim Hⁱ_𝔪(M/IⁿM)` is an isomorphism for `i ≤ s`.** In
> Situation [Stacks, Tag 0EFU] with `A` local and `T = {𝔪}`, with nothing assumed beyond the
> situation — in particular `A` need not be `I`-adically complete.
>
> The map is `Stacks.Algebraization.localCohomologyAdicQuotientToLimit`, the limit comparison of
> the cone whose `n`-th leg is `Hⁱ_𝔪` of the quotient map `M ⟶ M/IⁿM`. This is the isomorphism
> assertion of [Stacks, Tag 0EFR] read at that map, which is what a consumer reasoning about the
> individual projections needs; `Stacks.Algebraization.localCohomologyToAdicQuotientLimit`, the
> arrow Tag 0EFR is registered on, is instead built from an unpinned derived-limit witness.
>
> This is also **part (4) of [Stacks, Tag 0EFY]** at `T = {𝔪}`, in the wider range `i ≤ s` that
> contains that part's range `i < s`. It improves the registration of that part carried by
> `Stacks.Algebraization.isIso_localCohomologyToAdicQuotientLimit_of_isAdicComplete`
> (`StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean`) in two ways:
> the `I`-adic completeness of `A` is not assumed, and the arrow is the canonical comparison.
> The source's `T` is an arbitrary specialization-stable subset of `V(I)`; `T = {𝔪}` over a local
> ring is one such, and the general case rests on [Stacks, Tag 0EFX], whose state in the library
> is recorded in `StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean`.

```lean
public theorem isIso_localCohomologyAdicQuotientToLimit_closedPoint
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) (i : ℤ) (hi : i ≤ S.s) :
    IsIso (localCohomologyAdicQuotientToLimit S.A S.I (maximalIdeal S.A)
      (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) i)
```

**`Stacks.Algebraization.injective_and_smul_mem_range_localCohomologyAdicQuotientToLimit_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCanonicalAdicLimit.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCanonicalAdicLimit.lean#L162). The attribute's comment: “part (6) at T = \{𝔪} over a Noetherian local ring in Situation 0EFU: the canonical map Hˢ\_𝔪(M) ⟶ lim Hˢ\_𝔪(M/IⁿM) is injective and each element of I^\{m₀} carries the limit into its image, for every m₀”.

> **Part (6) of [Stacks, Tag 0EFY] at `T = {𝔪}`.** In Situation [Stacks, Tag 0EFU] with `A`
> local and `T = {𝔪}`, the canonical map `Hˢ_𝔪(M) ⟶ lim Hˢ_𝔪(M/IⁿM)` is injective, and every
> element of `I^{m₀}` carries an element of the limit into its image — that is, the cokernel is
> killed by `I^{m₀}`, for every `m₀` whatsoever.
>
> The part is immediate from `isIso_localCohomologyAdicQuotientToLimit_closedPoint` read in degree
> exactly `s`, which is inside the range `i ≤ s` of that theorem: the comparison is then an
> isomorphism, hence injective and surjective, so the cokernel is zero and `m₀` plays no role. The
> source asserts the two halves separately because at a general specialization-stable `T` the
> comparison in the top degree `s` need not be surjective; what makes the top degree accessible
> here is that `T = {𝔪}` puts it inside the range of [Stacks, Tag 0EFR].

```lean
public theorem injective_and_smul_mem_range_localCohomologyAdicQuotientToLimit_closedPoint
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) (m₀ : ℕ) :
    Function.Injective (localCohomologyAdicQuotientToLimit S.A S.I (maximalIdeal S.A)
        (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) S.s).hom ∧
      ∀ a ∈ S.I ^ m₀, ∀ y, ∃ x, (localCohomologyAdicQuotientToLimit S.A S.I (maximalIdeal S.A)
        (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) S.s).hom x = a • y
```

**`Stacks.Algebraization.exists_forall_injective_localCohomologyAdicQuotientMap_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCanonicalAdicLimit.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapCanonicalAdicLimit.lean#L195). The attribute's comment: “part (1) at T = \{𝔪} over a Noetherian local ring in Situation 0EFU: a single m₀ beyond which Hⁱ\_𝔪(M) ⟶ Hⁱ\_𝔪(M/IⁿM) is injective for every i ≤ s at once”.

> **Part (1) of [Stacks, Tag 0EFY] at `T = {𝔪}`, with nothing assumed beyond Situation
> [Stacks, Tag 0EFU].** There is an integer `m₀` such that the canonical map
> `Hⁱ_𝔪(M) ⟶ Hⁱ_𝔪(M/IⁿM)` is injective for every `i ≤ s` and every `n ≥ m₀`.
>
> The kernels of the canonical maps form a descending chain in the Artinian module `Hⁱ_𝔪(M)` whose
> intersection is the kernel of the canonical comparison to the limit, and that comparison is
> injective by `isIso_localCohomologyAdicQuotientToLimit_closedPoint`; so the chain reaches `0`.
> The pinned derived-limit presentation that argument consumes is
> `Dualizing.isDerivedLimitWithProjections_completedLocalCohomologyProjection_of_finite`.
>
> This improves
> `exists_forall_injective_homology_localCohomologyAdicQuotientMap_of_eq_closedPoint` of
> `StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapAdicProjectionInjectivity.lean` by
> dropping both its `[IsAdicComplete]` instance and its `hproj` hypothesis.
>
> The source's `T` is an arbitrary specialization-stable subset of `V(I)`; `T = {𝔪}` over a local
> ring is one such, and the general case rests on the pro-zero assertion of
> [Stacks, Tag 0EFX], whose state in the library is recorded in
> `StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean`.

```lean
public theorem exists_forall_injective_localCohomologyAdicQuotientMap_closedPoint
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) :
    ∃ m₀ : ℕ, ∀ i : ℤ, i ≤ S.s → ∀ n : ℕ, m₀ ≤ n →
      Function.Injective ((DerivedCategory.homologyFunctor (ModuleCat.{u} S.A) i).map
        (Dualizing.localCohomologyAdicQuotientMap S.A S.I (maximalIdeal S.A)
          (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) n)).hom
```

**`Stacks.Algebraization.exists_smul_id_firstDerivedLimitLocalCohomologyAdicTower_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapFirstDerivedLimitAnnihilation.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapFirstDerivedLimitAnnihilation.lean#L148). The attribute's comment: “part (7) at a general specialization-stable T in Situation 0EFU: I^\{m₀} annihilates R¹lim Hˢ\_T(M/IⁿM)”.

> In Situation [Stacks, Tag 0EFU], at a general specialization-stable `T`, there is an integer
> `m₀` such that every element of `I^{m₀}` annihilates `R¹lim H^s_T(M/IⁿM)`.

```lean
theorem exists_smul_id_firstDerivedLimitLocalCohomologyAdicTower_eq_zero
    (S : BootstrapSituation.{u, u, u}) :
    ∃ m₀ : ℕ, ∀ a ∈ S.I ^ m₀,
      a • 𝟙 (firstDerivedLimitLocalCohomologyAdicTower.{u, u} S.T S.I
        (ModuleCat.of S.A S.M) S.s) = 0
```

**`Stacks.Algebraization.exists_bound_adicLocalCohomologyComparisons`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapFirstDerivedLimitAnnihilation.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapFirstDerivedLimitAnnihilation.lean#L172).

> At a general specialization-stable `T`, in Situation [Stacks, Tag 0EFU] there is an integer
> `m₀ ≥ 0` such that
>
> 1. `H^i_T(M) ⟶ H^i_T(M/IⁿM)` is injective for all `i ≤ s` and `n ≥ m₀`;
> 2. `{H^i_T(M/IⁿM)}` satisfies the Mittag-Leffler condition for `i < s`;
> 3. `{H^i_T(I^{m₀}M/I^{n+m₀}M)}` satisfies the Mittag-Leffler condition for `i ≤ s`;
> 4. `H^i_T(M) ⟶ lim H^i_T(M/IⁿM)` is an isomorphism for `i < s`;
> 5. `H^s_T(I^{m₀}M) ⟶ lim H^s_T(I^{m₀}M/I^{n+m₀}M)` is an isomorphism;
> 6. `H^s_T(M) ⟶ lim H^s_T(M/IⁿM)` is injective with cokernel killed by `I^{m₀}`; and
> 7. `R¹lim H^s_T(M/IⁿM)` is killed by `I^{m₀}`.
>
> Parts (3) and (5) are the source's statements for the subquotients `I^{m₀}M/IⁿM`, `n ≥ m₀`, read
> along the cofinal shift `n ↦ n + m₀`, the `n`-th term of the tower of adic quotients of `I^{m₀}M`
> being `I^{m₀}M/I^{n+m₀}M` (`Stacks.Algebraization.map_subtype_pow_smul_top`); the limits and the
> transition maps are the same.

```lean
theorem exists_bound_adicLocalCohomologyComparisons (S : BootstrapSituation.{u, u, u}) :
    ∃ m₀ : ℕ,
      (∀ i ≤ S.s, ∀ n : ℕ, m₀ ≤ n →
        Function.Injective ((localCohomologyAdicCone.{u, u} S.A S.T S.I i
          (ModuleCat.of S.A S.M)).π.app (op n)).hom) ∧
      (∀ i : ℤ, i + 1 ≤ S.s → IsMittagLefflerCategorical
        (localCohomologyAdicTower.{u, u} S.A S.T S.I i (ModuleCat.of S.A S.M))) ∧
      (∀ i ≤ S.s, IsMittagLefflerCategorical (localCohomologyAdicTower.{u, u} S.A S.T S.I i
        (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M))))) ∧
      (∀ i : ℤ, i + 1 ≤ S.s → IsIso (limit.lift
        (localCohomologyAdicTower.{u, u} S.A S.T S.I i (ModuleCat.of S.A S.M))
        (localCohomologyAdicCone.{u, u} S.A S.T S.I i (ModuleCat.of S.A S.M)))) ∧
      IsIso (limit.lift
        (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s
          (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M))))
        (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s
          (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M))))) ∧
      (Function.Injective (limit.lift
          (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))
          (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))).hom ∧
        ∀ a ∈ S.I ^ m₀, ∀ z : (limit (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s
            (ModuleCat.of S.A S.M)) : ModuleCat.{u} S.A),
          a • z ∈ LinearMap.range (limit.lift
            (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))
            (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))).hom) ∧
      (∀ a ∈ S.I ^ m₀, a • 𝟙 (firstDerivedLimitLocalCohomologyAdicTower.{u, u} S.T S.I
        (ModuleCat.of S.A S.M) S.s) = 0)
```

**`Stacks.Algebraization.exists_forall_injective_and_isIso_limitLift_localCohomologyAdicCone_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapIdealPowerAdicLimit.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapIdealPowerAdicLimit.lean#L135). The attribute's comment: “part (5) at T = \{𝔪} over a Noetherian local ring in Situation 0EFU, at the very m₀ that part (1) produces: Hˢ\_𝔪(I^\{m₀}M) ⟶ lim Hˢ\_𝔪(I^\{m₀}M/IⁿM) is an isomorphism”.

> **Parts (1) and (5) of [Stacks, Tag 0EFY] at `T = {𝔪}`, at one and the same `m₀`.** In
> Situation [Stacks, Tag 0EFU] with `A` local and `T = {𝔪}`, there is an integer `m₀` such that
>
> * `Hⁱ_𝔪(M) ⟶ Hⁱ_𝔪(M/IⁿM)` is injective for every `i ≤ s` and every `n ≥ m₀` — part (1); and
> * `Hˢ_𝔪(I^{m₀}M) ⟶ lim_n Hˢ_𝔪(I^{m₀}M/IⁿM)` is an isomorphism — part (5), **at that `m₀`**.
>
> The second item is the statement of part (5) read for the module `I^{m₀}M`: the `n`-th term of
> its tower of adic quotients is `I^{m₀}M/I^{n+m₀}M`
> (`Stacks.Algebraization.map_subtype_pow_smul_top`), so the tower is the source's system
> `{I^{m₀}M/IⁿM}_{n ≥ m₀}` along the cofinal shift `n ↦ n + m₀` and the limits agree.
>
> Nothing beyond the situation is assumed; in particular `A` need not be `I`-adically complete.
> Part (1) comes from the pro-zero assertion of [Stacks, Tag 0EFX] at this locus through
> `Stacks.LocalCohomology.exists_forall_injective_localCohomologyAdicProjection_of_proZero`, and
> part (5) holds at that `m₀` because
> `isIso_limitLift_localCohomologyAdicCone_idealPowerSubmodule_closedPoint` proves it for every
> exponent, the situation being stable under `M ↦ IᵏM`.
>
> The source's `T` is an arbitrary specialization-stable subset of `V(I)`, and the general case
> rests on [Stacks, Tag 0EFX] for that `T`, which is proved in
> `StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean`; parts (1), (3)
> and (5) at a general locus, at one and the same `m₀`, are
> `Stacks.Algebraization.exists_forall_injective_and_isMittagLeffler_and_isIso_limitLift`.

```lean
public theorem exists_forall_injective_and_isIso_limitLift_localCohomologyAdicCone_closedPoint
    [IsLocalRing S.A] (hT : S.T = {closedPoint S.A}) :
    ∃ m₀ : ℕ,
      (∀ i ≤ S.s, ∀ n : ℕ, m₀ ≤ n →
        Function.Injective ((localCohomologyAdicCone.{u, u} S.A S.T S.I i
          (ModuleCat.of S.A S.M)).π.app (op n)).hom) ∧
      IsIso (limit.lift
        (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s
          (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M))))
        (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s
          (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M)))))
```

**`Stacks.Algebraization.isIso_localCohomologyToAdicQuotientLimit_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean#L341). The attribute's comment: “part (4) at T = \{𝔪} over an I-adically complete Noetherian local ring in Situation 0EFU: Hⁱ\_𝔪(M) ⟶ lim Hⁱ\_𝔪(M/IⁿM) is an isomorphism, in the range i ≤ s, which contains the range i < s of that part”.

> In the bootstrap situation of Stacks 0EFU with `A` local, `I`-adically complete and
> `T = {𝔪}`, the map `Hⁱ_𝔪(M) ⟶ lim Hⁱ_𝔪(M/IⁿM)` is an isomorphism for `i ≤ s` and a single
> power of `I` annihilates these modules.

```lean
public theorem isIso_localCohomologyToAdicQuotientLimit_of_isAdicComplete
    [IsLocalRing S.A] [IsAdicComplete S.I S.A] (hT : S.T = {closedPoint S.A}) :
    (∀ i : ℤ, i ≤ S.s →
        IsIso (localCohomologyToAdicQuotientLimit S.A S.I (maximalIdeal S.A)
          (maximalIdeal S.A) (ModuleCat.of S.A S.M) rfl i)) ∧
      ∃ n : ℕ, ∀ i : ℤ, i ≤ S.s →
        S.I ^ n ≤ Module.annihilator S.A
          (Stacks.LocalCohomology.localCohomologyModule S.A (maximalIdeal S.A)
            (Ideal.fg_of_isNoetherianRing _) (ModuleCat.of S.A S.M) i)
```

**`Stacks.Algebraization.exists_forall_injective_and_isMittagLeffler_and_isIso_limitLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapStableImageShift.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapStableImageShift.lean#L254). The attribute's comment: “parts (1), (3) and (5) at a general specialization-stable T in Situation 0EFU, at one and the same m₀: the projections are injective from m₀ on, \{Hⁱ\_T(I^\{m₀}M/IⁿM)} is Mittag-Leffler for i ≤ s, and Hˢ\_T(I^\{m₀}M) ⟶ lim Hˢ\_T(I^\{m₀}M/IⁿM) is an isomorphism”.

> **Stacks Project, Tag 0EFY, parts (1), (3) and (5)**, at a general specialization-stable `T`,
> at one and the same `m₀`. In Situation [Stacks, Tag 0EFU] there is an integer `m₀` such that
>
> * `H^i_T(M) ⟶ H^i_T(M/IⁿM)` is injective for every `i ≤ s` and every `n ≥ m₀` — part (1);
> * `{H^i_T(I^{m₀}M/I^{n+m₀}M)}` satisfies the Mittag-Leffler condition for every `i ≤ s` — part
>   (3), **at that `m₀`**; and
> * `H^s_T(I^{m₀}M) ⟶ lim_n H^s_T(I^{m₀}M/I^{n+m₀}M)` is an isomorphism — part (5), **at that
>   `m₀`**.
>
> The last two items are the source's statements for the module `I^{m₀}M`: the `n`-th term of its
> tower of adic quotients is `I^{m₀}M/I^{n+m₀}M`
> (`Stacks.Algebraization.map_subtype_pow_smul_top`), so the tower is the source's system
> `{I^{m₀}M/IⁿM}_{n ≥ m₀}` along the cofinal shift `n ↦ n + m₀` and the limits agree — the reading
> the registrants at `T = {𝔪}` use as well.
>
> Stating the three at a common `m₀` matters: `∃ m₀, part (5) at m₀` alone is satisfiable at
> `m₀ = 0`, where part (5) degenerates into part (4) read in degree `s`. The `m₀` exhibited here is
> a bound for part (1) and for the base of the stable-image assertion of [Stacks, Tag 0EFX]
> simultaneously. Nothing beyond the data of Situation [Stacks, Tag 0EFU] is assumed.

```lean
theorem exists_forall_injective_and_isMittagLeffler_and_isIso_limitLift :
    ∃ m₀ : ℕ,
      (∀ i ≤ S.s, ∀ n : ℕ, m₀ ≤ n →
        Function.Injective ((localCohomologyAdicCone.{u, u} S.A S.T S.I i
          (ModuleCat.of S.A S.M)).π.app (op n)).hom) ∧
      (∀ i ≤ S.s, IsMittagLefflerCategorical (localCohomologyAdicTower.{u, u} S.A S.T S.I i
        (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M))))) ∧
      IsIso (limit.lift
        (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s
          (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M))))
        (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s
          (ModuleCat.of S.A ↥(S.I ^ m₀ • (⊤ : Submodule S.A S.M)))))
```

**`Stacks.Algebraization.exists_forall_injective_localCohomologyAdicProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean#L323). The attribute's comment: “part (1) at a general specialization-stable T in Situation 0EFU: one m₀ beyond which Hⁱ\_T(M) ⟶ Hⁱ\_T(M/IⁿM) is injective for every i ≤ s”.

> **Stacks Project, Tag 0EFY, part (1)**, at a general specialization-stable `T`. In Situation
> [Stacks, Tag 0EFU] there is an `m₀` such that `H^i_T(M) ⟶ H^i_T(M/IⁿM)` is injective for every
> `i ≤ s` and every `n ≥ m₀`.
>
> This is `Stacks.LocalCohomology.exists_forall_injective_localCohomologyAdicProjection_of_proZero`
> with its hypothesis discharged by
> `Stacks.Algebraization.isProZeroIdealPowerCohomology`.

```lean
theorem exists_forall_injective_localCohomologyAdicProjection
    (S : BootstrapSituation.{u, u, u}) :
    ∃ m₀ : ℕ, ∀ i ≤ S.s, ∀ n : ℕ, m₀ ≤ n →
      Function.Injective ((localCohomologyAdicCone.{u, u} S.A S.T S.I i
        (ModuleCat.of S.A S.M)).π.app (op n)).hom
```

**`Stacks.Algebraization.isMittagLefflerCategorical_localCohomologyAdicTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean#L340). The attribute's comment: “part (2) at a general specialization-stable T in Situation 0EFU: the Mittag-Leffler condition for \{Hⁱ\_T(M/IⁿM)} in every degree i < s”.

> **Stacks Project, Tag 0EFY, part (2)**, at a general specialization-stable `T`. In Situation
> [Stacks, Tag 0EFU] the inverse system `{H^i_T(M/IⁿM)}` satisfies the Mittag-Leffler condition
> for `i < s`.
>
> This is `Stacks.LocalCohomology.isMittagLefflerCategorical_localCohomologyAdicTower_of_proZero`
> with its hypothesis — pro-zero-ness in degree `i + 1`, which is `≤ s` exactly when `i < s` —
> discharged by `Stacks.Algebraization.isProZeroIdealPowerCohomology`.

```lean
theorem isMittagLefflerCategorical_localCohomologyAdicTower
    (S : BootstrapSituation.{u, u, u}) (i : ℤ) (hi : i + 1 ≤ S.s) :
    IsMittagLefflerCategorical (localCohomologyAdicTower.{u, u} S.A S.T S.I i
      (ModuleCat.of S.A S.M))
```

**`Stacks.Algebraization.isIso_limitLift_localCohomologyAdicCone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformProZero.lean#L356). The attribute's comment: “part (4) at a general specialization-stable T in Situation 0EFU: Hⁱ\_T(M) ⟶ lim Hⁱ\_T(M/IⁿM) is an isomorphism in every degree i < s”.

> **Stacks Project, Tag 0EFY, part (4)**, at a general specialization-stable `T`. In Situation
> [Stacks, Tag 0EFU] the canonical map `H^i_T(M) ⟶ lim H^i_T(M/IⁿM)` is an isomorphism for
> `i < s`.
>
> This is `Stacks.LocalCohomology.isIso_limitLift_localCohomologyAdicCone_of_proZero` with both of
> its hypotheses — pro-zero-ness in degrees `i` and `i + 1`, both `≤ s` exactly when `i < s` —
> discharged by `Stacks.Algebraization.isProZeroIdealPowerCohomology`.

```lean
theorem isIso_limitLift_localCohomologyAdicCone
    (S : BootstrapSituation.{u, u, u}) (i : ℤ) (hi : i + 1 ≤ S.s) :
    IsIso (limit.lift (localCohomologyAdicTower.{u, u} S.A S.T S.I i (ModuleCat.of S.A S.M))
      (localCohomologyAdicCone.{u, u} S.A S.T S.I i (ModuleCat.of S.A S.M)))
```

**`Stacks.Algebraization.exists_injective_limitLift_and_smul_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapUniformStableImage.lean#L326). The attribute's comment: “part (6) at a general specialization-stable T in Situation 0EFU: Hˢ\_T(M) ⟶ lim Hˢ\_T(M/IⁿM) is injective with cokernel killed by I^\{m₀}”.

> **Stacks Project, Tag 0EFY, part (6)**, at a general specialization-stable `T`. In Situation
> [Stacks, Tag 0EFU] there is an `m₀` such that `H^s_T(M) ⟶ lim H^s_T(M/IⁿM)` is injective with
> cokernel killed by `I^{m₀}`.
>
> This is `Stacks.LocalCohomology.exists_injective_limitLift_and_smul_mem_range` with both of its
> hypotheses — the two assertions of [Stacks, Tag 0EFX] — discharged by
> `Stacks.Algebraization.isProZeroIdealPowerCohomology` and
> `Stacks.Algebraization.exists_hasStableImageIdealPowerCohomology`.

```lean
theorem exists_injective_limitLift_and_smul_mem_range (S : BootstrapSituation.{u, u, u}) :
    ∃ m₀ : ℕ,
      Function.Injective (limit.lift
          (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))
          (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))).hom ∧
        ∀ a ∈ S.I ^ m₀, ∀ z : (limit (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s
            (ModuleCat.of S.A S.M)) : ModuleCat.{u} S.A),
          a • z ∈ LinearMap.range (limit.lift
            (localCohomologyAdicTower.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))
            (localCohomologyAdicCone.{u, u} S.A S.T S.I S.s (ModuleCat.of S.A S.M))).hom
```

**`Stacks.LocalCohomology.isMittagLefflerCategorical_homologyAdicQuotientLocalCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean#L106). The attribute's comment: “part (2) at T = \{𝔪} over a Noetherian local ring, in every degree”.

> **The local cohomology of the adic quotients of a finite module is Mittag-Leffler.** For a
> finite module `M` over a Noetherian local ring, the inverse system `n ↦ Hⁱ_𝔪(M/IⁿM)` satisfies
> the Mittag-Leffler condition, since each `M/IⁿM` is again a finite module.
>
> This is part (2) of [Stacks, Tag 0EFY] at the support `T = {𝔪}` of a Noetherian local ring. In
> that case it holds in every degree and draws nothing from Situation [Stacks, Tag 0EFU]: local
> cohomology at `𝔪` of a finite module over a Noetherian local ring is Artinian, and a descending
> chain of submodules of an Artinian module stabilizes, which is the Mittag-Leffler condition. A
> general specialization-stable `T ⊆ V(I)` lies beyond that argument, the modules `Hⁱ_T(M/IⁿM)`
> being in general neither finite nor Artinian; the source obtains part (2) there from the
> pro-zero assertion of [Stacks, Tag 0EFX] instead.

```lean
theorem isMittagLefflerCategorical_homologyAdicQuotientLocalCohomology
    [IsLocalRing A] [IsNoetherianRing A] (I : Ideal A) (M : ModuleCat.{u} A)
    [Module.Finite A M] (i : ℤ) :
    IsMittagLefflerCategorical
      (Dualizing.adicQuotientLocalCohomologySystem A I (IsLocalRing.maximalIdeal A)
          (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing M ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} A) i)
```

**`Stacks.LocalCohomology.isMittagLefflerCategorical_homologyAdicQuotientLocalCohomology_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/CompletedLimitComparison.lean#L128). The attribute's comment: “part (3) at T = \{𝔪} over a Noetherian local ring, for the submodule IᵏM”.

> **Part (3) of [Stacks, Tag 0EFY] at the support `T = {𝔪}`.** For a finite module `M` over a
> Noetherian local ring, an ideal `I` and a `k : ℕ`, the inverse system `n ↦ Hⁱ_𝔪(IᵏM/Iⁿ⁺ᵏM)` of
> the local cohomologies of the adic quotients of the submodule `IᵏM` satisfies the
> Mittag-Leffler condition, in every degree.
>
> The source indexes that system by `n ≥ k` and writes its terms `Hⁱ_𝔪(IᵏM/IⁿM)`; the index here
> runs over all of `ℕ` instead, which replaces `IⁿM` by `Iⁿ(IᵏM) = Iⁿ⁺ᵏM` and so gives the same
> family of modules and the same transition maps, read along the cofinal shift `n ↦ n + k`.
>
> `IᵏM` is a submodule of a finite module over a Noetherian ring, hence itself finite, so this is
> `isMittagLefflerCategorical_homologyAdicQuotientLocalCohomology` applied to it.

```lean
theorem isMittagLefflerCategorical_homologyAdicQuotientLocalCohomology_smul
    [IsLocalRing A] [IsNoetherianRing A] (I : Ideal A) (M : ModuleCat.{u} A)
    [Module.Finite A M] (k : ℕ) (i : ℤ) :
    IsMittagLefflerCategorical
      (Dualizing.adicQuotientLocalCohomologySystem A I (IsLocalRing.maximalIdeal A)
          (IsLocalRing.maximalIdeal A).fg_of_isNoetherianRing
          (ModuleCat.of A ↥(I ^ k • (⊤ : Submodule A M))) ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} A) i)
```

**`Stacks.LocalCohomology.smul_id_firstDerivedLimitLocalCohomologyAdicTower_eq_zero_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerFirstDerivedLimit.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerFirstDerivedLimit.lean#L408). The attribute's comment: “part (7) at T = \{𝔪} over a Noetherian local ring: I^\{m₀} annihilates R¹lim Hˢ\_𝔪(M/IⁿM), for every m₀ and in every degree”.

> **Part (7) of [Stacks, Tag 0EFY] at `T = {𝔪}` over a Noetherian local ring.** Every element
> of `I^{m₀}` annihilates `R¹lim H^s_𝔪(M/IⁿM)`, for every `m₀` and every degree `s`.
>
> The system `{H^s_𝔪(M/IⁿM)}` is itself Mittag-Leffler here, by
> `isMittagLefflerCategorical_localCohomologyAdicTower_closedPoint`, so its Milnor difference is an
> epimorphism and the first derived inverse limit — the cokernel of that difference — vanishes
> outright; annihilation by `I^{m₀}` follows for every `m₀`, and the degree plays no role either.
>
> That is a stronger conclusion than the part asserts, and it is available only because of the
> locus: over a Noetherian local ring with `T = {𝔪}` the modules `H^s_𝔪(M/IⁿM)` are Artinian. At a
> general specialization-stable `T` they are neither finite nor Artinian, the source obtains the
> Mittag-Leffler condition only for the subsystem `Aₙ` of part (3), and the content of part (7) is
> then genuinely the annihilation and not a vanishing; that route is
> `smul_id_firstDerivedLimitLocalCohomologyAdicTower_eq_zero_of_isMittagLeffler` above, run on
> `Stacks.LocalCohomology.isMittagLefflerCategorical_adicTowerCollapseKernelTower_of_stableImage`.

```lean
theorem smul_id_firstDerivedLimitLocalCohomologyAdicTower_eq_zero_closedPoint (A : Type u)
    [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (J : Ideal A) (N : ModuleCat.{u} A)
    [Module.Finite A N] (i : ℤ) (m₀ : ℕ) {a : A} (ha : a ∈ J ^ m₀) :
    a • 𝟙 (firstDerivedLimitLocalCohomologyAdicTower.{u, u}
      {IsLocalRing.closedPoint A} J N i) = 0
```

**`Stacks.LocalCohomology.exists_forall_injective_localCohomologyAdicProjection_of_proZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/IdealPowerProZero.lean#L339). The attribute's comment: “part (1): the injectivity of H^i\_T(M) → H^i\_T(M/I^nM) for i ≤ s and n ≫ 0, derived from the pro-zero assertion of Lemma 0EFX taken as an explicit hypothesis; that assertion is not proved here”.

> **Stacks Project, Tag 0EFY, part (1).** There is an integer `m₀` such that
> `H^i_T(M) → H^i_T(M/IⁿM)` is injective for all `i ≤ s` and all `n ≥ m₀`.
>
> *Argument.* Fix `i ≤ s`. By the pro-zero assertion of Tag 0EFX there are `k` and a transition map
> `IᵏM → M` of the tower `{IⁿM}` with vanishing `H^i_T`; since `IⁿM ⊆ M` factors through `IᵏM` for
> `n ≥ k`, the map `H^i_T(IⁿM) → H^i_T(M)` is then zero for every `n ≥ k`, and the long exact
> sequence of `0 → IⁿM → M → M/IⁿM → 0` makes `H^i_T(M) → H^i_T(M/IⁿM)` injective. A single `m₀`
> serving every `i ≤ s` is the supremum of the finitely many `k` for `0 ≤ i ≤ s`, together with the
> vanishing of `H^i_T` in negative degrees.
>
> Only the pro-zero assertion of Tag 0EFX is used, and it is a hypothesis here; it is not proved in
> the library.

```lean
theorem exists_forall_injective_localCohomologyAdicProjection_of_proZero
    (T : Set (PrimeSpectrum A)) (I : Ideal A) (M : ModuleCat.{max u v} A) (s : ℤ)
    (hpro : ∀ i ≤ s, ∃ k : ℕ, ∃ h : 0 ≤ k,
      (localCohomologyWithSupportInModuleFunctor.{u, v} A T i).map
        ((idealPowerTower.{u, v} I M).map (homOfLE h).op) = 0) :
    ∃ m₀ : ℕ, ∀ i ≤ s, ∀ n : ℕ, m₀ ≤ n →
      Function.Injective ((localCohomologyAdicCone.{u, v} A T I i M).π.app (op n)).hom
```

## Tag 0EIE, a theorem

[Tag 0EIE](https://stacks.math.columbia.edu/tag/0EIE) in the Stacks Project.

**`Stacks.LocalCohomology.Bootstrap.essentiallyConstant_and_consequences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantBootstrap.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantBootstrap.lean#L66).

> **Stacks Project, Tag 0EIE.** In Situation 0EFU, for `i ≤ s` the inverse system
> `{H^i_T(M/IⁿM)}_{n ≥ 0}` is essentially constant with value `H^i_T(M)` (with respect to the cone
> of the maps `H^i_T(M) → H^i_T(M/IⁿM)` induced by the quotient maps). In particular it is
> Mittag-Leffler, `H^i_T(M)` is annihilated by a power of `I`, and the canonical maps exhibit
> `H^i_T(M)` as `lim H^i_T(M/IⁿM)`.

```lean
theorem essentiallyConstant_and_consequences (S : BootstrapSituation.{u, u, w}) (i : ℤ)
    (hi : i ≤ S.s) :
    (∃ (j : ℕᵒᵖ) (σ : (tower.{u, u} S i).obj j ⟶ (cone.{u, u} S i).pt),
        EssentiallyConstantPro.IsEssentiallyConstantWith (tower.{u, u} S i) (cone.{u, u} S i)
          j σ) ∧
      IsMittagLefflerCategorical (tower.{u, u} S i) ∧
      (∃ n : ℕ, ∀ a ∈ S.I ^ n,
        ∀ x : (localCohomologyWithSupportInModuleFunctor.{u, u} S.A S.T i).obj
          (ModuleCat.of S.A S.M), a • x = 0) ∧
      Nonempty (IsLimit (cone.{u, u} S i))
```

**`Stacks.LocalCohomology.isEssentiallyConstantWith_localCohomologyAdicCone_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L464). The attribute's comment: “the negative-degree range, unconditionally: for i < 0 the system is essentially constant with value H^i\_T(M) = 0”.

> **Stacks Project, Tag 0EIE** in negative degrees, with no hypothesis.
> For `i < 0` the system `{H^i_T(M/IⁿM)}` is essentially constant with value `H^i_T(M)`: local
> cohomology with support in `T` of a module vanishes in negative degrees
> (`Stacks.LocalCohomology.isZero_localCohomologyWithSupportIn_single_of_neg`), so every term of
> the system and the value are zero and the zero morphism is a witness. The three consequences in
> this range follow by composing with the implications above.

```lean
theorem isEssentiallyConstantWith_localCohomologyAdicCone_of_neg (I : Ideal A) (i : ℤ)
    (hi : i < 0) (M : ModuleCat.{max u v} A) :
    EssentiallyConstantPro.IsEssentiallyConstantWith
      (localCohomologyAdicTower.{u, v} A T I i M) (localCohomologyAdicCone.{u, v} A T I i M)
      (op 0) 0
```

**`Stacks.LocalCohomology.exists_isEssentiallyConstantWith_localCohomologyAdicCone_of_pow_smul_top_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L490). The attribute's comment: “the range where I acts nilpotently on M: if I^N M = 0 then in every degree the system is essentially constant with value H^i\_T(M), for an arbitrary ring, subset of the spectrum and module”.

> **Stacks Project, Tag 0EIE** when `I` acts nilpotently on `M`, with no hypothesis and in
> every degree. If `IᴺM = 0` then the quotient maps `M → M/IᵐM` are isomorphisms for every
> `m ≥ N`, hence so are their images under `H^i_T`, and a cone whose projections are invertible
> from an index on carries essential-constancy data
> (`CategoryTheory.EssentiallyConstantPro.exists_isEssentiallyConstantWith_of_isIso_π`). The three
> consequences in this range follow by composing with the implications above.
>
> No Noetherian, finiteness or support hypothesis is used: `A` is an arbitrary commutative ring,
> `T` an arbitrary subset of its spectrum and `M` an arbitrary module.

```lean
theorem exists_isEssentiallyConstantWith_localCohomologyAdicCone_of_pow_smul_top_eq_bot
    (I : Ideal A) (i : ℤ) (M : ModuleCat.{max u v} A) {N : ℕ}
    (hN : I ^ N • (⊤ : Submodule A M) = ⊥) :
    ∃ (j : ℕᵒᵖ) (σ : (localCohomologyAdicTower.{u, v} A T I i M).obj j ⟶
        (localCohomologyAdicCone.{u, v} A T I i M).pt),
      EssentiallyConstantPro.IsEssentiallyConstantWith
        (localCohomologyAdicTower.{u, v} A T I i M) (localCohomologyAdicCone.{u, v} A T I i M)
        j σ
```

**`Stacks.LocalCohomology.Bootstrap.isEssentiallyConstantWith_of_depthBound_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 673](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L673). The attribute's comment: “the essential-constancy assertion, and with it the four consequences, for a bootstrap situation whose depth bound s is negative”.

> **Stacks Project, Tag 0EIE** for a bootstrap situation whose depth bound is negative. Every
> degree `i ≤ s < 0` is negative, so each term of `{H^i_T(M/IⁿM)}` and the value `H^i_T(M)`
> vanish and the zero morphism witnesses essential constancy with value `H^i_T(M)`. The four
> consequences above apply to this witness, and so hold with no hypothesis in this range.

```lean
theorem isEssentiallyConstantWith_of_depthBound_neg (hs : S.s < 0) (hi : i ≤ S.s) :
    EssentiallyConstantPro.IsEssentiallyConstantWith
      (tower.{u, v} S i) (cone.{u, v} S i) (op 0) 0
```

**`Stacks.LocalCohomology.Bootstrap.exists_isEssentiallyConstantWith_of_pow_smul_top_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L685). The attribute's comment: “the essential-constancy assertion for a bootstrap situation in which I acts nilpotently on M, with no hypothesis and in every degree”.

> **Stacks Project, Tag 0EIE** for a bootstrap situation in which `I` acts nilpotently on `M`,
> with no hypothesis and in every degree. The quotient maps `M → M/IᵐM` are isomorphisms from the
> nilpotency exponent on, so the canonical cone's projections are, and a cone whose projections
> are invertible from an index on carries essential-constancy data.

```lean
theorem exists_isEssentiallyConstantWith_of_pow_smul_top_eq_bot {N : ℕ}
    (hN : S.I ^ N • (⊤ : Submodule S.A S.M) = ⊥) :
    ∃ (j : ℕᵒᵖ) (σ : (tower.{u, v} S i).obj j ⟶ (cone.{u, v} S i).pt),
      EssentiallyConstantPro.IsEssentiallyConstantWith
        (tower.{u, v} S i) (cone.{u, v} S i) j σ
```

**`Stacks.LocalCohomology.Bootstrap.isMittagLeffler_of_pow_smul_top_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L697). The attribute's comment: “the Mittag-Leffler consequence for a bootstrap situation in which I acts nilpotently on M, with no hypothesis and in every degree”.

> **Stacks Project, Tag 0EIE**, the Mittag-Leffler consequence for a bootstrap situation in
> which `I` acts nilpotently on `M`, with no hypothesis and in every degree.

```lean
theorem isMittagLeffler_of_pow_smul_top_eq_bot {N : ℕ}
    (hN : S.I ^ N • (⊤ : Submodule S.A S.M) = ⊥) :
    IsMittagLefflerCategorical (tower.{u, v} S i)
```

**`Stacks.LocalCohomology.Bootstrap.exists_pow_smul_eq_zero_of_pow_smul_top_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L707). The attribute's comment: “the annihilation consequence for a bootstrap situation in which I acts nilpotently on M, with no hypothesis and in every degree”.

> **Stacks Project, Tag 0EIE**, the annihilation consequence for a bootstrap situation in which
> `I` acts nilpotently on `M`, with no hypothesis and in every degree.

```lean
theorem exists_pow_smul_eq_zero_of_pow_smul_top_eq_bot {N : ℕ}
    (hN : S.I ^ N • (⊤ : Submodule S.A S.M) = ⊥) :
    ∃ n : ℕ, ∀ a ∈ S.I ^ n,
      ∀ x : (localCohomologyWithSupportInModuleFunctor.{u, v} S.A S.T i).obj
        (ModuleCat.of S.A S.M), a • x = 0
```

**`Stacks.LocalCohomology.Bootstrap.isLimit_of_pow_smul_top_eq_bot`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L720). The attribute's comment: “the limit consequence H^i\_T(M) = lim H^i\_T(M/I^nM) for a bootstrap situation in which I acts nilpotently on M, with no hypothesis and in every degree”.

> **Stacks Project, Tag 0EIE**, the limit consequence for a bootstrap situation in which `I`
> acts nilpotently on `M`, with no hypothesis and in every degree: the quotient maps exhibit
> `H^i_T(M)` as `lim H^i_T(M/IⁿM)`.

```lean
def isLimit_of_pow_smul_top_eq_bot {N : ℕ}
    (hN : S.I ^ N • (⊤ : Submodule S.A S.M) = ⊥) :
    IsLimit (cone.{u, v} S i)
```

**`Stacks.LocalCohomology.Bootstrap.isMittagLeffler_of_eq_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean, line 748](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean#L748). The attribute's comment: “the Mittag-Leffler consequence for a bootstrap situation whose ring is local and whose locus T is the closed point, with no hypothesis and in every degree”.

> **Stacks Project, Tag 0EIE**, the Mittag-Leffler consequence for a bootstrap situation whose
> ring is local and whose locus is the closed point, with no hypothesis. The terms
> `H^i_T(M/IⁿM)` are then local cohomology at the maximal ideal of finite modules over a
> Noetherian local ring, hence Artinian, and an inverse system of Artinian modules is
> Mittag-Leffler. No degree restriction is needed either.

```lean
theorem isMittagLeffler_of_eq_closedPoint [IsLocalRing S.A]
    (hT : S.T = {IsLocalRing.closedPoint S.A}) :
    IsMittagLefflerCategorical (tower.{u, u} S i)
```

## Tag 0EG0, a lemma

[Tag 0EG0](https://stacks.math.columbia.edu/tag/0EG0) in the Stacks Project.

**`Stacks.Algebraization.exists_ideal_isIso_localCohomologyToAdicQuotientLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologyLimit.lean#L443). The attribute's comment: “for the maximal ideal of a Noetherian local ring: the tag's conclusion in full at 𝔞 = 𝔪 -- the same ideal J₀ ≤ 𝔪, the same locus condition V(J₀) ∩ V(I) = V(𝔪), the same ∀ J ≤ J₀ with V(J) ∩ V(I) = V(𝔪), the same degree s+1, IsIso -- with the source's condition (2) in full as H. The statement has no support-ideal parameter: 𝔪 is substituted throughout. The source's condition (1) is used only to obtain Mittag-Leffler-ness of \{H^s\_𝔞(M/IⁿM)} from 0EIE, which at the maximal ideal follows from the finiteness of the M/IⁿM and the Artinianness of local cohomology there, via Stacks.LocalCohomology.isMittagLefflerCategorical\_homologyAdicQuotientLocalCohomology, so (1) is not needed. The general support ideal is not covered; it needs 0EIE, which the library has only as consequences of its own essential-constancy assertion (RingTheory/LocalCohomology/EssentiallyConstantConsequences.lean). The specialisation is not vacuous: V(𝔪) is the closed point, and J ranges over the ideals with V(J) ∩ V(I) = \{𝔪}, which include ideals strictly inside 𝔪”.

> Let `A` be a Noetherian local ring with maximal ideal `𝔪`, let `I ⊆ 𝔪` be an ideal, let `M`
> be a finite `A`-module and let `s` and `d` be integers. Assume that `A, I, 𝔪, M` satisfy the
> conditions of Stacks 0EFL for `s + 1` and `d` with `J = 𝔪`. Then there is an ideal `J₀ ⊆ 𝔪` with
> `V(J₀) ∩ V(I) = V(𝔪)` such that for every ideal `J ⊆ J₀` with `V(J) ∩ V(I) = V(𝔪)` the map
>
> `H^{s+1}_J(M) ⟶ lim H^{s+1}_𝔪(M/IⁿM)`
>
> is an isomorphism.

```lean
public theorem exists_ideal_isIso_localCohomologyToAdicQuotientLimit [IsLocalRing A]
    (I : Ideal A) (hIa : I ≤ maximalIdeal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A)) (δ : PrimeSpectrum A → ℤ) (δmax δmin : ℤ)
    (H : AlgebraizationHypotheses (M := M) I (maximalIdeal A) (s + 1) d omega δ δmax δmin) :
    ∃ J₀ : Ideal A, J₀ ≤ maximalIdeal A ∧
      PrimeSpectrum.zeroLocus (J₀ : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
        PrimeSpectrum.zeroLocus ((maximalIdeal A : Ideal A) : Set A) ∧
      ∀ J : Ideal A, J ≤ J₀ →
        ∀ hJ : PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
          PrimeSpectrum.zeroLocus ((maximalIdeal A : Ideal A) : Set A),
          IsIso (localCohomologyToAdicQuotientLimit A I (maximalIdeal A) J (ModuleCat.of A M)
            (hJ.trans (zeroLocus_inter_eq_self_of_le hIa).symm) (s + 1))
```

**`Stacks.Algebraization.BootstrapSituation.exists_ideal_isIso_localCohomologyToAdicQuotientLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologySupportLimit.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/BootstrapLocalCohomologySupportLimit.lean#L117).

> **Stacks Project, Tag 0EG0.** Let `I ⊆ 𝔞` be ideals of a Noetherian ring `A`, let `M` be a
> finite `A`-module and let `s` and `d` be integers. Assume
>
> 1. `A, I, V(𝔞), M` satisfy the assumptions of Situation [Stacks, Tag 0EFU] for `s` and `d` — the
>    bootstrap situation `S`, with locus `V(𝔞)`;
> 2. `A, I, 𝔞, M` satisfy the conditions of [Stacks, Tag 0EFL] for `s + 1` and `d` with `J = 𝔞` —
>    the hypothesis `H`.
>
> Then there is an ideal `J₀ ⊆ 𝔞` with `V(J₀) ∩ V(I) = V(𝔞)` such that for every `J ⊆ J₀` with
> `V(J) ∩ V(I) = V(𝔞)` the map `H^{s+1}_J(M) ⟶ lim H^{s+1}_𝔞(M/IⁿM)` is an isomorphism.
>
> Stacks 0EFL supplies `J₀` together with the identification `H^{s+1}_J(M) = H^{s+1}(RΓ_𝔞(M)^∧)`;
> Stacks 0EEW puts `H^{s+1}(RΓ_𝔞(M)^∧)` in a short exact sequence with `R¹lim H^s_𝔞(M/IⁿM)` on the
> left and `lim H^{s+1}_𝔞(M/IⁿM)` on the right; and the left-hand term vanishes because
> `{H^s_𝔞(M/IⁿM)}` is Mittag-Leffler by Theorem [Stacks, Tag 0EIE].
>
> Condition (2) is the disjunction of the two cases in which the library states Stacks 0EFL.
> `Stacks.Algebraization.AlgebraizationHypotheses` names the extreme values of a dimension function
> on `V(𝔞) ∩ V(I) = V(𝔞)`, so it can only hold when `V(𝔞)` is nonempty; when `V(𝔞)` is empty, that
> is `𝔞 = A`, the source's condition (5), the only one naming the dimension function, is guarded by
> `V(𝔭) ∩ V(𝔞) ∩ V(I) ≠ ∅` and is vacuous, and of the source's conditions only the `I`-adic
> completeness of `A` is used, through
> `Stacks.Algebraization.isAlgebraizationIdeal_of_zeroLocus_inter_eq_empty`.
> Either disjunct follows from the source's condition (2), so the hypothesis asks for nothing beyond
> it.

```lean
public theorem BootstrapSituation.exists_ideal_isIso_localCohomologyToAdicQuotientLimit
    (S : BootstrapSituation.{u, u, u}) (a : Ideal S.A) (hIa : S.I ≤ a)
    (hT : S.T = PrimeSpectrum.zeroLocus (a : Set S.A))
    (omega : DerivedCategory (ModuleCat.{u} S.A)) (δ : PrimeSpectrum S.A → ℤ) (δmax δmin : ℤ)
    (H : AlgebraizationHypotheses (M := S.M) S.I a (S.s + 1) S.d omega δ δmax δmin ∨
      (IsAdicComplete S.I S.A ∧ PrimeSpectrum.zeroLocus (a : Set S.A) = ∅)) :
    ∃ J₀ : Ideal S.A, J₀ ≤ a ∧
      PrimeSpectrum.zeroLocus (J₀ : Set S.A) ∩ PrimeSpectrum.zeroLocus (S.I : Set S.A) =
        PrimeSpectrum.zeroLocus (a : Set S.A) ∧
      ∀ J : Ideal S.A, J ≤ J₀ →
        ∀ hJ : PrimeSpectrum.zeroLocus (J : Set S.A) ∩ PrimeSpectrum.zeroLocus (S.I : Set S.A) =
          PrimeSpectrum.zeroLocus (a : Set S.A),
          IsIso (localCohomologyToAdicQuotientLimit S.A S.I a J (ModuleCat.of S.A S.M)
            (hJ.trans (zeroLocus_inter_eq_self_of_le hIa).symm) (S.s + 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.10, Tag 0EFT](https://stacks.math.columbia.edu/tag/0EFT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
