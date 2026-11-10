---
declaration: section
origin: cited
lean: Stacks.Algebraization.exists_notMem_mem_annihilator_homology_derivedCompletion_localCohomology_maximalIdeal, Stacks.Algebraization.localStabilizationHypotheses_iff, Stacks.Algebraization.zeroLocus_stabilizingIdeal_maximalIdeal_inter, Stacks.Algebraization.exists_stabilization, Stacks.Algebraization.exists_stabilization_finite_localCohomologyModule_maximalIdeal, Stacks.Algebraization.depthAddDimGtOnZeroLocus_maximalIdeal_iff, Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal_maximalIdeal, Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal_maximalIdeal_of_exists
statement: formalized
proof: formalized
---

# 52.9 Algebraization of local cohomology, II

Section 52.9 of the Stacks Project, [Tag 0EFP](https://stacks.math.columbia.edu/tag/0EFP). 5 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DXK, a lemma

[Tag 0DXK](https://stacks.math.columbia.edu/tag/0DXK) in the Stacks Project.

**`Stacks.Algebraization.exists_notMem_mem_annihilator_homology_derivedCompletion_localCohomology_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorCompletedLocalCohomology.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/AnnihilatorCompletedLocalCohomology.lean#L396). The attribute's comment: “the full statement: an element outside `p` annihilating the cohomology of the derived `I`-adic completion of `RΓ_{V(𝔪)}(M)` in every degree `≤ s`”.

> Let `(A, 𝔪)` be a Noetherian local ring with a dualizing complex, let `I` be an ideal with
> `cd(A, I) ≤ d`, let `M` be a finite `A`-module and let `p` be a prime with
> `depth_{A_p}(M_p) + dim(A/p) > d + s`. Then some `f ∈ A` outside `p` annihilates the degree-`i`
> cohomology of the derived `I`-adic completion of `RΓ_{V(𝔪)}(M)` for every `i ≤ s`.

```lean
theorem exists_notMem_mem_annihilator_homology_derivedCompletion_localCohomology_maximalIdeal
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I : Ideal A) (p : PrimeSpectrum A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (homega : Dualizing.IsDualizingComplex (A := A) (K := omega))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A I I.fg_of_isNoetherianRing ≤ d)
    (hdepth : enatToEInt
          (Module.depth (Localization.AtPrime p.asIdeal)
            (maximalIdeal (Localization.AtPrime p.asIdeal))
            (LocalizedModule p.asIdeal.primeCompl M)) +
        krullDimToEInt (ringKrullDim (A ⧸ p.asIdeal)) > ((d + s : ℤ) : EInt))
    {r : ℕ} (gen : Fin r → A) (hgen : Ideal.span (Set.range gen) = I) :
    ∃ f : A, f ∉ p.asIdeal ∧ ∀ i : ℤ, i ≤ s →
      f ∈ Module.annihilator A
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
          ((DerivedCompletion.derivedCompletionFunctor A gen).obj
            ((Dualizing.derivedPowerTorsionProperty A (maximalIdeal A)
                (maximalIdeal A).fg_of_isNoetherianRing).ι.obj
              ((Dualizing.localCohomologyFunctor.{u, u} A (maximalIdeal A)
                  (maximalIdeal A).fg_of_isNoetherianRing).obj
                ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                  (ModuleCat.of A M))))))
```

## Tag 0DXM, a lemma

[Tag 0DXM](https://stacks.math.columbia.edu/tag/0DXM) in the Stacks Project.

**`Stacks.Algebraization.localStabilizationHypotheses_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdeal.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdeal.lean#L200). The attribute's comment: “the hypotheses, identified with those of Stacks 0EFI at J = 𝔪”.

> **Stacks 0DXM.** Hypotheses (1)–(4) of the lemma are exactly the properness of `I` together
> with the hypotheses of Stacks 0EFI for `J = 𝔪`.
>
> This biconditional is the content of the source's proof, which reads "this is a special case of
> Lemma 0EFI": at `J = 𝔪` the set `V(𝔭) ∩ V(𝔪) ∩ V(I)` of Stacks 0EFI is the single point `𝔪`,
> where its relative dimension `dim((A/𝔭)_𝔮)` is `dim(A/𝔭)`.

```lean
public theorem localStabilizationHypotheses_iff (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{w} A)) :
    LocalStabilizationHypotheses (M := M) I s d omega ↔
      (I ≠ ⊤ ∧ StabilizationHypotheses (M := M) I (maximalIdeal A) s d omega)
```

**`Stacks.Algebraization.zeroLocus_stabilizingIdeal_maximalIdeal_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdeal.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdeal.lean#L250). The attribute's comment: “the ideal J₀, with V(J₀) ∩ V(I) = \{𝔪}”.

> **Stacks 0DXM.** The ideal that Stacks 0EFI selects at `J = 𝔪` meets `V(I)` in the closed
> point only, which is the first clause of the conclusion of the lemma.

```lean
public theorem zeroLocus_stabilizingIdeal_maximalIdeal_inter (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{w} A))
    (H : LocalStabilizationHypotheses (M := M) I s d omega) :
    PrimeSpectrum.zeroLocus
          ((stabilizingIdeal I (maximalIdeal A) s d omega
            H.toStabilizationHypotheses : Ideal A) : Set A) ∩
        PrimeSpectrum.zeroLocus (I : Set A) = {closedPoint A}
```

**`Stacks.Algebraization.exists_stabilization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealExistence.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealExistence.lean#L315). The attribute's comment: “the conclusion: an ideal J₀ and one exponent n such that every J ⊆ J₀ with V(J) ∩ V(I) = \{𝔪} has RΓ\_\{J₀}(M) → RΓ\_J(M) an isomorphism on cohomology in degrees ≤ s and (J₀ I) ^ n annihilating those modules”.

> **Stacks 0DXM.** Let `(A, 𝔪)` be a Noetherian local ring, let `I ⊂ A` be an ideal, let `M` be
> a finite `A`-module and let `s` and `d` be integers. Under hypotheses (1)–(4) of the lemma there
> is an ideal `J₀` with `V(J₀) ∩ V(I) = {𝔪}` such that for every ideal `J ⊆ J₀` with
> `V(J) ∩ V(I) = {𝔪}` the comparison `RΓ_{J₀}(M) → RΓ_J(M)` induces an isomorphism in cohomology
> in degrees `≤ s`, and one power of `J₀ I` annihilates all of those cohomology modules.
>
> This is `Stacks.Algebraization.exists_stabilization_of_exists` with its hypothesis discharged by
> `Stacks.Algebraization.exists_isStabilizingData_maximalIdeal`. Taking `J = J₀` gives the
> annihilation of `H^i_{J₀}(M)` by a power of `J₀ I`.

```lean
public theorem exists_stabilization (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (H : LocalStabilizationHypotheses (M := M) I s d omega) :
    ∃ J₀ : Ideal A, ∃ n : ℕ,
      PrimeSpectrum.zeroLocus (J₀ : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
          {closedPoint A} ∧
        ∀ J : Ideal A, ∀ hJ : J ≤ J₀,
          PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
            {closedPoint A} →
          ∀ i : ℤ, i ≤ s →
            IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
                (localCohomologyComparison A J₀ J J₀.fg_of_isNoetherianRing
                  J.fg_of_isNoetherianRing hJ
                  ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                    (ModuleCat.of A M)))) ∧
              (J₀ * I) ^ n ≤ Module.annihilator A
                ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
                  ((Dualizing.localCohomologyFunctor A J J.fg_of_isNoetherianRing).obj
                    ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                      (ModuleCat.of A M))).obj)
```

## Tag 0DXN, a lemma

[Tag 0DXN](https://stacks.math.columbia.edu/tag/0DXN) in the Stacks Project.

**`Stacks.Algebraization.exists_stabilization_finite_localCohomologyModule_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LocalStabilizationFiniteness.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LocalStabilizationFiniteness.lean#L171).

> **Stacks 0DXN.** Let `(A, 𝔪)` be a Noetherian local ring, `I ⊂ A` an ideal, `M` a finite
> `A`-module and `s`, `d` integers. Assume (1) `A` has a dualizing complex, (2') every prime
> `𝔭 ∈ V(I)` other than `𝔪` has `depth(M_𝔭) + dim(A/𝔭) > s`, (3) every prime `𝔭 ∉ V(I)` with
> `V(𝔭) ∩ V(I) = {𝔪}` has `dim(A/𝔭) ≤ d`, and (4) every prime `𝔭 ∉ V(I)` with
> `V(𝔭) ∩ V(I) ≠ {𝔪}` has `depth(M_𝔭) ≥ s` or `depth(M_𝔭) + dim(A/𝔭) > d + s`. Then there is an
> ideal `J₀` with `V(J₀) ∩ V(I) = {𝔪}` such that for every `J ⊆ J₀` with `V(J) ∩ V(I) = {𝔪}` the
> map `RΓ_{J₀}(M) → RΓ_J(M)` is an isomorphism on cohomology in degrees `≤ s` and one power of
> `J₀ I` annihilates those cohomology modules (the conclusion of Stacks 0DXM), and moreover
> `H^i_{J₀}(M)` is a finite `A`-module for every `i ≤ s`.
>
> Hypotheses (1), (3), (4) and the source's standing assumption `I ≠ A` (without which
> `V(J₀) ∩ V(I) = {𝔪}` is unattainable) are `LocalStabilizationHypotheses`; (2') is
> `DepthAddDimGtAtMaximalIdeal`. The integers `s` and `d` are arbitrary. For `s < 0` the
> finiteness is the vanishing of local cohomology in negative degrees; for `d < 0` the hypotheses
> force `I` to be nilpotent (`LocalStabilizationHypotheses.mem_zeroLocus_of_neg`).

```lean
public theorem exists_stabilization_finite_localCohomologyModule_maximalIdeal
    (I : Ideal A) (s d : ℤ) (omega : DerivedCategory (ModuleCat.{u} A))
    (H : LocalStabilizationHypotheses (M := M) I s d omega)
    (h2 : DepthAddDimGtAtMaximalIdeal (M := M) I s) :
    ∃ J₀ : Ideal A, ∃ n : ℕ,
      PrimeSpectrum.zeroLocus (J₀ : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
          {closedPoint A} ∧
        (∀ J : Ideal A, ∀ hJ : J ≤ J₀,
          PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
            {closedPoint A} →
          ∀ i : ℤ, i ≤ s →
            IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
                (localCohomologyComparison A J₀ J J₀.fg_of_isNoetherianRing
                  J.fg_of_isNoetherianRing hJ
                  ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                    (ModuleCat.of A M)))) ∧
              (J₀ * I) ^ n ≤ Module.annihilator A
                ↥((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj
                  ((Dualizing.localCohomologyFunctor A J J.fg_of_isNoetherianRing).obj
                    ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
                      (ModuleCat.of A M))).obj)) ∧
        ∀ i : ℤ, i ≤ s →
          Module.Finite A
            (localCohomologyModule A J₀ J₀.fg_of_isNoetherianRing (ModuleCat.of A M) i)
```

**`Stacks.Algebraization.depthAddDimGtOnZeroLocus_maximalIdeal_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealFiniteness.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealFiniteness.lean#L117). The attribute's comment: “hypothesis (2') is hypothesis (2') of Stacks 0EFJ at J = 𝔪, for every ideal I”.

> **Stacks 0DXN.** Hypothesis (2') of the lemma is hypothesis (2') of Stacks 0EFJ at
> `J = 𝔪`, for every ideal `I`.
>
> This biconditional is the content of the source's proof, which reads "this is a special case of
> Lemma 0EFJ": at `J = 𝔪` the set `V(𝔪) ∩ V(I)` is the single point `𝔪`, so a prime of `V(I)`
> lies outside it exactly when it differs from `𝔪`, and the only specialization of it available
> in `V(𝔪) ∩ V(I)` is `𝔪` itself, where `dim((A/𝔭)_𝔪)` is `dim(A/𝔭)`.
>
> That reading of `V(𝔪) ∩ V(I)` uses `𝔪 ∈ V(I)`, the source's standing assumption that `I` is
> proper. It is not needed for the equivalence itself: for `I = A` the locus `V(I)` is empty, so
> both conditions quantify over nothing.

```lean
public theorem depthAddDimGtOnZeroLocus_maximalIdeal_iff {I : Ideal A} (s : ℤ) :
    DepthAddDimGtOnZeroLocus (M := M) I (maximalIdeal A) s ↔
      DepthAddDimGtAtMaximalIdeal (M := M) I s
```

**`Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealFiniteness.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealFiniteness.lean#L153). The attribute's comment: “H^i\_\{J₀}(M) is a finite A-module for i ≤ s, given the annihilation clause of Stacks 0DXM and 0 ≤ s”.

> **Stacks 0DXN.** Under hypotheses (1), (3), (4) of Stacks 0DXM together with hypothesis
> (2') in place of its empty hypothesis (2), the local cohomology of `M` supported in the ideal
> `J₀` that Stacks 0DXM selects is a finite `A`-module in every degree `i ≤ s`.
>
> This is Stacks 0EFJ at `J = 𝔪`. The annihilation of `H^i_{J₀}(M)` by a power of `J₀ I` for
> `i ≤ s` is a clause of the conclusion of Stacks 0DXM and is carried as a hypothesis, as it is in
> Stacks 0EFJ.

```lean
public theorem finite_localCohomologyModule_stabilizingIdeal_maximalIdeal
    (h2 : DepthAddDimGtAtMaximalIdeal (M := M) I s) (hs : 0 ≤ s)
    (hann : ∃ n : ℕ, ∀ j : ℤ, j ≤ s →
      ((stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses * I) ^ n
        : Ideal A) ≤ Module.annihilator A
        (localCohomologyModule A
          (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses)
          (Ideal.fg_of_isNoetherianRing
            (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses))
          (ModuleCat.of A M) j))
    (i : ℤ) (hi : i ≤ s) :
    Module.Finite A
      (localCohomologyModule A
        (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses)
        (Ideal.fg_of_isNoetherianRing
          (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses))
        (ModuleCat.of A M) i)
```

**`Stacks.Algebraization.finite_localCohomologyModule_stabilizingIdeal_maximalIdeal_of_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealFiniteness.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealFiniteness.lean#L181). The attribute's comment: “H^i\_\{J₀}(M) is a finite A-module for i ≤ s, for 0 ≤ s and 0 ≤ d”.

> **Stacks 0DXN.** The same finiteness, with the annihilation clause of Stacks 0DXM proved
> from Stacks 0EFI.
>
> The hypotheses are then exactly those of Stacks 0DXM with its empty hypothesis (2) replaced by
> (2'), together with `0 ≤ s` and the hypothesis `0 ≤ d` that Stacks 0EFI needs and the source
> of Stacks 0DXM uses silently; see the module documentation.

```lean
public theorem finite_localCohomologyModule_stabilizingIdeal_maximalIdeal_of_exists
    (h2 : DepthAddDimGtAtMaximalIdeal (M := M) I s) (hs : 0 ≤ s) (hd : 0 ≤ d)
    (i : ℤ) (hi : i ≤ s) :
    Module.Finite A
      (localCohomologyModule A
        (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses)
        (Ideal.fg_of_isNoetherianRing
          (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses))
        (ModuleCat.of A M) i)
```

## Tag 0EFQ, a lemma

[Tag 0EFQ](https://stacks.math.columbia.edu/tag/0EFQ) in the Stacks Project.

**`Stacks.Algebraization.isIso_homologyMap_localCohomologyComparison_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean#L203). The attribute's comment: “H^i\_J(M) = H^i\_𝔪(M) for i ≤ s, for every J with V(J) ∩ V(I) = \{𝔪}”.

> Under hypothesis (6) the local cohomology of `M` supported in any ideal `J` with
> `V(J) ∩ V(I) = {𝔪}` agrees with the local cohomology supported in `𝔪` in all degrees `i ≤ s`:
> `H^i_J(M) = H^i_𝔪(M)`.

```lean
public theorem isIso_homologyMap_localCohomologyComparison_maximalIdeal
    (I J : Ideal A) (s : ℤ) (h6 : DepthGtAtMaximalIdeal (M := M) I s)
    (hJ : PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
      {closedPoint A})
    (i : ℤ) (hi : i ≤ s) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
      (localCohomologyComparison A (maximalIdeal A) J
        (Ideal.fg_of_isNoetherianRing (maximalIdeal A)) (Ideal.fg_of_isNoetherianRing J)
        (le_maximalIdeal_of_zeroLocus_inter_eq_closedPoint hJ).1
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M))))
```

**`Stacks.Algebraization.isIso_homologyMap_localCohomologyComparison_stabilizingIdeal_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean#L241). The attribute's comment: “H^i\_\{J₀}(M) = H^i\_𝔪(M) for i ≤ s”.

> Under hypothesis (6) the local cohomology of `M` supported in the ideal `J₀` produced by
> Stacks 0DXM agrees with the local cohomology supported in `𝔪` in all degrees `i ≤ s`:
> `H^i_{J₀}(M) = H^i_𝔪(M)`.

```lean
public theorem isIso_homologyMap_localCohomologyComparison_stabilizingIdeal_maximalIdeal
    (h6 : DepthGtAtMaximalIdeal (M := M) I s) (i : ℤ) (hi : i ≤ s) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
      (localCohomologyComparison A (maximalIdeal A)
        (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses)
        (Ideal.fg_of_isNoetherianRing (maximalIdeal A))
        (Ideal.fg_of_isNoetherianRing
          (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses))
        (stabilizingIdeal_le I (maximalIdeal A) s d omega H.toStabilizationHypotheses)
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M))))
```

**`Stacks.Algebraization.isIso_homologyMap_localCohomologyComparison_stabilizingIdeal_of_depthGt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean#L260). The attribute's comment: “H^i\_\{J₀}(M) = H^i\_J(M) for i ≤ s”.

> Under hypothesis (6) the local cohomology of `M` supported in the ideal `J₀` produced by
> Stacks 0DXM agrees with the local cohomology supported in any further ideal `J ⊆ J₀` with
> `V(J) ∩ V(I) = {𝔪}`, in all degrees `i ≤ s`: `H^i_{J₀}(M) = H^i_J(M)`.

```lean
public theorem isIso_homologyMap_localCohomologyComparison_stabilizingIdeal_of_depthGt
    (h6 : DepthGtAtMaximalIdeal (M := M) I s) (J : Ideal A)
    (hJle : J ≤ stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses)
    (hJ : PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
      {closedPoint A})
    (i : ℤ) (hi : i ≤ s) :
    IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).map
      (localCohomologyComparison A
        (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses) J
        (Ideal.fg_of_isNoetherianRing
          (stabilizingIdeal I (maximalIdeal A) s d omega H.toStabilizationHypotheses))
        (Ideal.fg_of_isNoetherianRing J) hJle
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M))))
```

**`Stacks.Algebraization.exists_pow_le_annihilator_localCohomologyModule_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean#L282). The attribute's comment: “the annihilation assertion through Stacks 0EFK, in the numerical range 0 ≤ s and 0 ≤ d in which that lemma is stated”.

> Under hypothesis (6), `0 ≤ s` and `0 ≤ d`, a single power of `I` annihilates `H^i_J(M)` in
> every degree `i ≤ s`, uniformly in every ideal `J` with `V(J) ∩ V(I) = {𝔪}`.

```lean
public theorem exists_pow_le_annihilator_localCohomologyModule_maximalIdeal
    (h6 : DepthGtAtMaximalIdeal (M := M) I s) (hs : 0 ≤ s) (hd : 0 ≤ d) :
    ∃ n : ℕ, ∀ J : Ideal A,
      PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
        {closedPoint A} →
      ∀ i : ℤ, i ≤ s →
        I ^ n ≤ Module.annihilator A
          (localCohomologyModule A J (Ideal.fg_of_isNoetherianRing J)
            (ModuleCat.of A M) i)
```

**`Stacks.Algebraization.exists_pow_le_annihilator_localCohomologyModule_maximalIdeal_of_depthGt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/StabilizationMaximalIdealCollapse.lean#L323). The attribute's comment: “the annihilation assertion: a power of I annihilates H^i\_J(M) for i ≤ s, for every J with V(J) ∩ V(I) = \{𝔪}, with no hypothesis beyond the tag's”.

> Under hypothesis (6) a single power of `I` annihilates `H^i_J(M)` in every degree `i ≤ s`,
> uniformly in every ideal `J` with `V(J) ∩ V(I) = {𝔪}`; this includes `J = 𝔪` and `J = J₀`, by
> `zeroLocus_maximalIdeal_inter` and `zeroLocus_stabilizingIdeal_maximalIdeal_inter`.

```lean
public theorem exists_pow_le_annihilator_localCohomologyModule_maximalIdeal_of_depthGt
    (h6 : DepthGtAtMaximalIdeal (M := M) I s) :
    ∃ n : ℕ, ∀ J : Ideal A,
      PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
        {closedPoint A} →
      ∀ i : ℤ, i ≤ s →
        I ^ n ≤ Module.annihilator A
          (localCohomologyModule A J (Ideal.fg_of_isNoetherianRing J)
            (ModuleCat.of A M) i)
```

## Tag 0DXP, a lemma

[Tag 0DXP](https://stacks.math.columbia.edu/tag/0DXP) in the Stacks Project.

**`Stacks.Algebraization.exists_isLocalAlgebraizationIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparisonLocal.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationComparisonLocal.lean#L329). The attribute's comment: “existence of J₀”.

> **Stacks 0DXP.** Let `(A, 𝔪)` be a Noetherian local ring, let `I ⊆ A` be a proper ideal, let
> `M` be a finite `A`-module and let `s` and `d` be integers. Assume `A` is `I`-adically complete
> with a dualizing complex, that `cd(A, I) ≤ d`, and that every prime `𝔭 ∉ V(I)` with
> `V(𝔭) ∩ V(I) ≠ {𝔪}` has `depth(M_𝔭) ≥ s` or `depth(M_𝔭) + dim(A/𝔭) > d + s`. Then there is an
> ideal `J₀` with `V(J₀) ∩ V(I) = {𝔪}` such that for every ideal `J ⊆ J₀` with
> `V(J) ∩ V(I) = {𝔪}` the canonical map
>
> `RΓ_J(M) ⟶ RΓ_𝔪(M)^∧`
>
> is an isomorphism on cohomology in all degrees `≤ s`.
>
> This is the source's own proof: the case `s < 0` is
> `Stacks.Algebraization.isLocalAlgebraizationIdeal_of_lt_zero`, and for `0 ≤ s` the statement is
> the case `J = 𝔪` of Stacks 0EFL, by
> `Stacks.Algebraization.LocalAlgebraizationHypotheses.toAlgebraizationHypotheses` on the
> hypotheses and `Stacks.Algebraization.isLocalAlgebraizationIdeal_of_isAlgebraizationIdeal` on
> the conclusion.
>
> Condition (5) of Stacks 0EFL is stated against a dimension function on `Spec(A)`, which the
> statement of Stacks 0DXP does not mention. No such datum is assumed here: hypothesis (1)
> provides a dualizing complex, and the dimension function attached to one by Stacks 0A7Z is
> `Dualizing.dualizingDimensionFunctionOfArbitraryUniverse`.

```lean
public theorem exists_isLocalAlgebraizationIdeal (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (H : LocalAlgebraizationHypotheses (M := M) I s d omega) :
    ∃ J₀ : Ideal A, IsLocalAlgebraizationIdeal (M := M) I H.ne_top s J₀
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.9, Tag 0EFP](https://stacks.math.columbia.edu/tag/0EFP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
