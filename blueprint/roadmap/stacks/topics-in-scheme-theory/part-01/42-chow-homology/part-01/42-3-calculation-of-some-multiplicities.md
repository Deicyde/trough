---
declaration: section
origin: cited
lean: AlgebraicGeometry.periodicLength_mul_eq_finsum_support, AlgebraicGeometry.length_quotSMulTop_eq_sum_minimal_support, AlgebraicGeometry.length_quotient_span_sup_eq_sum_minimalPrimes, AlgebraicGeometry.periodicLength_powers_eq_zero_of_nilpotent, AlgebraicGeometry.isFiniteLength_homology_and_periodicLength_powers_eq_zero_of_nilpotent, AlgebraicGeometry.periodicLength_smul_fst, AlgebraicGeometry.periodicLength_smul_snd
statement: formalized
proof: formalized
---

# 42.3 Calculation of some multiplicities

Section 42.3 of the Stacks Project, [Tag 0EAA](https://stacks.math.columbia.edu/tag/0EAA). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02QF, a lemma

[Tag 02QF](https://stacks.math.columbia.edu/tag/02QF) in the Stacks Project.

**`AlgebraicGeometry.periodicLength_mul_eq_finsum_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/Multiplication.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/Multiplication.lean#L390).

> **Stacks Project, Tag 02QF.** The multiplicity of the periodic complex `(M, 0, x)` is
> the sum, over the nonclosed points in the support of `M`, of the order of `x` modulo that
> point times the length of the localization of `M` there.

```lean
public theorem periodicLength_mul_eq_finsum_support
    {R M : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (x : R) (hM : Module.supportDim R M ≤ 1)
    (hxM : Module.supportDim R (QuotSMulTop x M) ≤ 0) :
    periodicLength
        (twoPeriodicComplex (0 : Module.End R M) (LinearMap.lsmul R M x)
          (zero_mul _) (mul_zero _)) =
      ∑ᶠ q ∈ {q : PrimeSpectrum R |
          q ∈ Module.support R M ∧ q ≠ IsLocalRing.closedPoint R},
        ((Ring.ord (R ⧸ q.asIdeal) (Ideal.Quotient.mk q.asIdeal x)).toNat : ℤ) *
          ((Module.length (Localization.AtPrime q.asIdeal)
            (LocalizedModule q.asIdeal.primeCompl M)).toNat : ℤ)
```

## Tag 02QG, a lemma

[Tag 02QG](https://stacks.math.columbia.edu/tag/02QG) in the Stacks Project.

**`AlgebraicGeometry.length_quotSMulTop_eq_sum_minimal_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/RestrictedDivisors.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/RestrictedDivisors.lean#L143). The attribute's comment: “Cohen-Macaulay module formula”.

> **Stacks Project, Tag 02QG, first assertion.** If `M` is a finite
> Cohen--Macaulay module whose support has dimension one and whose quotient by
> `x` has zero-dimensional support, then the length of `M / xM` is the sum of
> the colength of `(x, q)` times the length of `M` localized at `q`, over the
> minimal points `q` of the support of `M`.

```lean
public theorem length_quotSMulTop_eq_sum_minimal_support
    {R M : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (x : R) (hCM : Module.IsCohenMacaulayAtMaximalIdeal R M)
    (hM : Module.supportDim R M = 1)
    (hxM : Module.supportDim R (QuotSMulTop x M) = 0) :
    Module.length R (QuotSMulTop x M) =
      ∑ᶠ q ∈ {q : PrimeSpectrum R | Minimal (· ∈ Module.support R M) q},
        Module.length R (R ⧸ (Ideal.span {x} ⊔ q.asIdeal)) *
          Module.length (Localization.AtPrime q.asIdeal)
            (LocalizedModule q.asIdeal.primeCompl M)
```

**`AlgebraicGeometry.length_quotient_span_sup_eq_sum_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/RestrictedDivisors.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/RestrictedDivisors.lean#L161). The attribute's comment: “quotient-ring formula”.

> **Stacks Project, Tag 02QG, second assertion.** If `x` is a
> nonzerodivisor on the one-dimensional quotient `R / I`, then the colength of
> `(x, I)` is the sum of the colength of `(x, q)` times the length of
> `(R / I)` localized at `q`, over the minimal primes `q` above `I`.

```lean
public theorem length_quotient_span_sup_eq_sum_minimalPrimes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (x : R) (I : Ideal R) (hx : IsSMulRegular (R ⧸ I) x)
    (hI : ringKrullDim (R ⧸ I) = 1) :
    Module.length R (R ⧸ (Ideal.span {x} ⊔ I)) =
      ∑ᶠ q ∈ {q : PrimeSpectrum R | q.asIdeal ∈ I.minimalPrimes},
        Module.length R (R ⧸ (Ideal.span {x} ⊔ q.asIdeal)) *
          Module.length (Localization.AtPrime q.asIdeal)
            (LocalizedModule q.asIdeal.primeCompl (R ⧸ I))
```

## Tag 0EAB, a lemma

[Tag 0EAB](https://stacks.math.columbia.edu/tag/0EAB) in the Stacks Project.

**`AlgebraicGeometry.periodicLength_powers_eq_zero_of_nilpotent`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/NilpotentPowers.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/NilpotentPowers.lean#L397).

> If `φ` is nilpotent of order at most `n` and
> `ker φ / range (φ ^ (n - 1))` has finite length, then the periodic length associated to
> `φ ^ i` and `φ ^ (n - i)` vanishes for every `0 ≤ i ≤ n`.
>
> Since `periodicLength` reads infinite lengths as zero, this alone does not say that the
> multiplicity is defined; the full statement of Stacks 0EAB, including the finiteness of both
> cohomology modules, is
> `isFiniteLength_homology_and_periodicLength_powers_eq_zero_of_nilpotent`.

```lean
public lemma periodicLength_powers_eq_zero_of_nilpotent {R : Type u} [Ring R]
    {M : Type v} [AddCommGroup M] [Module R M]
    (φ : Module.End R M) (n : ℕ) (hnpos : 0 < n) (hnil : φ ^ n = 0)
    (hfinite : IsFiniteLength R ((LinearMap.ker φ) ⧸
      (LinearMap.range (φ ^ (n - 1))).comap (LinearMap.ker φ).subtype)) :
    ∀ (i : ℕ) (hi : i ≤ n),
      periodicLength
        (twoPeriodicComplex (φ ^ i) (φ ^ (n - i))
          (by rw [← pow_add, Nat.add_sub_of_le hi, hnil])
          (by rw [← pow_add, Nat.sub_add_cancel hi, hnil])) = 0
```

**`AlgebraicGeometry.isFiniteLength_homology_and_periodicLength_powers_eq_zero_of_nilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/NilpotentPowers.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/NilpotentPowers.lean#L428).

> **Stacks 0EAB.** Let `φ` be an endomorphism of an `R`-module `M` and `n > 0` with
> `φ ^ n = 0` such that `ker φ / range (φ ^ (n - 1))` has finite length. Then for every
> `0 ≤ i ≤ n` the multiplicity `e_R(M, φ ^ i, φ ^ (n - i))` is defined, that is, both
> cohomology modules `ker (φ ^ i) / range (φ ^ (n - i))` and `ker (φ ^ (n - i)) / range (φ ^ i)`
> of the two-periodic complex `(M, φ ^ i, φ ^ (n - i))` have finite length, and it vanishes.

```lean
public theorem isFiniteLength_homology_and_periodicLength_powers_eq_zero_of_nilpotent
    {R : Type u} [Ring R] {M : Type v} [AddCommGroup M] [Module R M]
    (φ : Module.End R M) (n : ℕ) (hnpos : 0 < n) (hnil : φ ^ n = 0)
    (hfinite : IsFiniteLength R ((LinearMap.ker φ) ⧸
      (LinearMap.range (φ ^ (n - 1))).comap (LinearMap.ker φ).subtype)) :
    ∀ (i : ℕ) (hi : i ≤ n),
      IsFiniteLength R
        ((twoPeriodicComplex (φ ^ i) (φ ^ (n - i))
          (by rw [← pow_add, Nat.add_sub_of_le hi, hnil])
          (by rw [← pow_add, Nat.sub_add_cancel hi, hnil])).homology (0 : ZMod 2)) ∧
      IsFiniteLength R
        ((twoPeriodicComplex (φ ^ i) (φ ^ (n - i))
          (by rw [← pow_add, Nat.add_sub_of_le hi, hnil])
          (by rw [← pow_add, Nat.sub_add_cancel hi, hnil])).homology (1 : ZMod 2)) ∧
      periodicLength
        (twoPeriodicComplex (φ ^ i) (φ ^ (n - i))
          (by rw [← pow_add, Nat.add_sub_of_le hi, hnil])
          (by rw [← pow_add, Nat.sub_add_cancel hi, hnil])) = 0
```

## Tag 0EAC, a lemma

[Tag 0EAC](https://stacks.math.columbia.edu/tag/0EAC) in the Stacks Project.

**`AlgebraicGeometry.periodicLength_smul_fst`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/ScalarMultiple.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/ScalarMultiple.lean#L243). The attribute's comment: “multiplying the first differential”.

> Multiplying the first differential of a two-periodic complex by `x` subtracts the periodic
> length of its image with differentials zero and multiplication by `x`.

```lean
public lemma periodicLength_smul_fst {R : Type u} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] (M : Type v) [AddCommGroup M]
    [Module R M] [Module.Finite R M]
    (φ ψ : M →ₗ[R] M) (hφψ : φ.comp ψ = 0) (hψφ : ψ.comp φ = 0) (x : R)
    (hH₀ : IsFiniteLength R
      ((twoPeriodicComplex φ ψ hφψ hψφ).homology (0 : ZMod 2)))
    (hH₁ : IsFiniteLength R
      ((twoPeriodicComplex φ ψ hφψ hψφ).homology (1 : ZMod 2)))
    (hsupp : Module.supportDim R (QuotSMulTop x M) ≤ 0) :
    periodicLength
        (twoPeriodicComplex (x • φ) ψ
          (by change (x • φ).comp ψ = 0; rw [LinearMap.smul_comp, hφψ, smul_zero])
          (by change ψ.comp (x • φ) = 0; rw [LinearMap.comp_smul, hψφ, smul_zero])) =
      periodicLength (twoPeriodicComplex φ ψ hφψ hψφ) -
        periodicLength
          (twoPeriodicComplex (0 : Module.End R (LinearMap.range φ))
            (LinearMap.lsmul R (LinearMap.range φ) x) (zero_mul _) (mul_zero _))
```

**`AlgebraicGeometry.periodicLength_smul_snd`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/ScalarMultiple.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/CalculationMultiplicities/ScalarMultiple.lean#L294). The attribute's comment: “multiplying the second differential”.

> Multiplying the second differential of a two-periodic complex by `x` adds the periodic
> length of its image with differentials zero and multiplication by `x`.

```lean
public lemma periodicLength_smul_snd {R : Type u} [CommRing R] [IsNoetherianRing R]
    [IsLocalRing R] (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (φ ψ : M →ₗ[R] M) (hφψ : φ.comp ψ = 0) (hψφ : ψ.comp φ = 0) (x : R)
    (hH₀ : IsFiniteLength R
      ((twoPeriodicComplex φ ψ hφψ hψφ).homology (0 : ZMod 2)))
    (hH₁ : IsFiniteLength R
      ((twoPeriodicComplex φ ψ hφψ hψφ).homology (1 : ZMod 2)))
    (hsupp : Module.supportDim R (QuotSMulTop x M) ≤ 0) :
    periodicLength
        (twoPeriodicComplex φ (x • ψ)
          (by
            change φ.comp (x • ψ) = 0
            rw [LinearMap.comp_smul, hφψ, smul_zero])
          (by
            change (x • ψ).comp φ = 0
            rw [LinearMap.smul_comp, hψφ, smul_zero])) =
      periodicLength (twoPeriodicComplex φ ψ hφψ hψφ) +
        periodicLength
          (twoPeriodicComplex (0 : Module.End R (LinearMap.range ψ))
            (LinearMap.lsmul R (LinearMap.range ψ) x) (zero_mul _) (mul_zero _))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.3, Tag 0EAA](https://stacks.math.columbia.edu/tag/0EAA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
