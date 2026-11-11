---
declaration: section
origin: cited
lean: ogoma_ker_eq_of_localization, Stacks.Smoothing.exists_parameters_pow_mem_and_annihilator_sq_eq, Stacks.Smoothing.canBeResolved_of_isRegularLocalRing_of_isSeparableExtension
statement: formalized
proof: formalized
---

# 16.10 Separable residue fields

Section 16.10 of the Stacks Project, [Tag 07FB](https://stacks.math.columbia.edu/tag/07FB). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07FC, a lemma

[Tag 07FC](https://stacks.math.columbia.edu/tag/07FC) in the Stacks Project.

**`ogoma_ker_eq_of_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/OgomaKernelStabilization.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/OgomaKernelStabilization.lean#L66).

> Stacks Tag 07FC (Ogoma's lemma). Over a Noetherian ring `A`, for a finite
> `A`-module `M`, a multiplicative subset `S` and `π : A`, if multiplication by `π`
> and `π²` have the same kernel on the localization `S⁻¹M`, then there is a single
> `s ∈ S` such that for all `n > 0`, multiplication by `sⁿπ` and `(sⁿπ)²` have the
> same kernel on `M`.

```lean
theorem ogoma_ker_eq_of_localization {A M : Type*} [CommRing A] [AddCommGroup M] [Module A M]
    [IsNoetherianRing A] [Module.Finite A M] (S : Submonoid A) (π : A)
    (h : LinearMap.ker (LinearMap.lsmul A (LocalizedModule S M) π)
      = LinearMap.ker (LinearMap.lsmul A (LocalizedModule S M) (π ^ 2))) :
    ∃ s ∈ S, ∀ n : ℕ, 0 < n →
      LinearMap.ker (LinearMap.lsmul A M (s ^ n * π))
        = LinearMap.ker (LinearMap.lsmul A M ((s ^ n * π) ^ 2))
```

## Tag 07FD, a lemma

[Tag 07FD](https://stacks.math.columbia.edu/tag/07FD) in the Stacks Project.

**`Stacks.Smoothing.exists_parameters_pow_mem_and_annihilator_sq_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/ParametersWithPowersInIdeal.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/ParametersWithPowersInIdeal.lean#L214).

> **Stacks 07FD.** Let `Λ` be a Noetherian ring, let `I` and `q` be ideals of `Λ` with `q`
> prime, and let `n`, `e` be positive integers. Assume that the extension of `q ^ n` to `Λ_q` is
> contained in the extension of `I`, and that `Λ_q` is a regular local ring of dimension `d`.
> Then there are `π₁, …, π_d ∈ Λ` such that `(π₁, …, π_d) Λ_q = q Λ_q`, such that `π_i ^ n ∈ I`
> for every `i`, and such that for every `i` the annihilator of `π_i` in
> `Λ ⧸ (π₁ ^ e, …, π_{i-1} ^ e)` is the annihilator of `π_i ^ 2`.

```lean
theorem exists_parameters_pow_mem_and_annihilator_sq_eq
    (Λ : Type*) [CommRing Λ] [IsNoetherianRing Λ] (I q : Ideal Λ) [q.IsPrime]
    (n e d : ℕ) (hn : 0 < n) (he : 0 < e)
    (hqI : Ideal.map (algebraMap Λ (Localization.AtPrime q)) (q ^ n) ≤
      Ideal.map (algebraMap Λ (Localization.AtPrime q)) I)
    [IsRegularLocalRing (Localization.AtPrime q)]
    (hd : ringKrullDim (Localization.AtPrime q) = d) :
    ∃ π : Fin d → Λ,
      Ideal.map (algebraMap Λ (Localization.AtPrime q)) (Ideal.span (Set.range π)) =
          Ideal.map (algebraMap Λ (Localization.AtPrime q)) q ∧
      (∀ i : Fin d, π i ^ n ∈ I) ∧
      (∀ i : Fin d, ∀ x : Λ ⧸ Ideal.span
          (Set.range fun j : Fin i.1 => π (j.castLE (Nat.le_of_lt i.2)) ^ e),
        x * Ideal.Quotient.mk _ (π i) = 0 ↔ x * Ideal.Quotient.mk _ (π i ^ 2) = 0)
```

## Tag 07FE, a lemma

[Tag 07FE](https://stacks.math.columbia.edu/tag/07FE) in the Stacks Project.

**`Stacks.Smoothing.canBeResolved_of_isRegularLocalRing_of_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/SeparableResidueFieldResolution/RegularSeparableResolution.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Smoothing/SeparableResidueFieldResolution/RegularSeparableResolution.lean#L83).

> **Stacks 07FE.** Let `k → A → Λ ⊃ q` be a local smoothing situation over a field `k`
> with `Λ` Noetherian, `q` minimal over `𝔥_A = √(H_{A/k} Λ)`, `Λ_q` a regular local ring and the
> residue field extension `κ(q)/k` separable. Then the chain can be resolved at `q`.

```lean
theorem canBeResolved_of_isRegularLocalRing_of_isSeparableExtension
    (k : Type u) (A : Type v) (Lambda : Type w)
    [Field k] [CommRing A] [CommRing Lambda]
    [Algebra k A] [Algebra k Lambda] [Algebra A Lambda]
    [IsScalarTower k A Lambda] [Algebra.FinitePresentation k A]
    [IsNoetherianRing Lambda] (q : Ideal Lambda) [q.IsPrime]
    (hq : (Ideal.map (algebraMap A Lambda)
      (Stacks.Smoothing.singularIdeal k A)).radical.IsMinimalPrime q)
    [IsRegularLocalRing (Localization.AtPrime q)]
    [Algebra.IsSeparableExtension k q.ResidueField] :
    CanBeResolved k A Lambda q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.10, Tag 07FB](https://stacks.math.columbia.edu/tag/07FB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
