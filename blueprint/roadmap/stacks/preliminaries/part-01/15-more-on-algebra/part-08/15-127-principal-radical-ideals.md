---
declaration: section
origin: cited
lean: length_quotient_span_pow_le_and_eq_of_mem_nonZeroDivisors, natCard_minimalPrimes_le_length_quotient_span_singleton, exists_isSystemOfParameters_cons_of_avoids_minimalPrimes, exists_isSystemOfParameters_pair_add_of_avoids_minimalPrimes, exists_nonzero_mem_isReduced_quotient_of_height_one_primes, exists_isReduced_quotient_and_dvd_pow, multiplicity_le_length_quotient_of_isSystemOfParameters, natCard_fullDimensionalMinimalPrimes_le_length_quotient_of_isSystemOfParameters
statement: formalized
proof: formalized
---

# 15.127 Principal radical ideals

Section 15.127 of the Stacks Project, [Tag 0BWR](https://stacks.math.columbia.edu/tag/0BWR). 10 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BWS, a lemma

[Tag 0BWS](https://stacks.math.columbia.edu/tag/0BWS) in the Stacks Project.

**`length_quotient_span_pow_le_and_eq_of_mem_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean#L152). References: EGA IV (21.10.13), “(i) for M=A”.

> **Stacks 0BWS.** The quotients by powers of a parameter in a one-dimensional Noetherian
> local ring have finite length. Their lengths grow at most linearly, and grow exactly linearly
> when the parameter is a non-zero-divisor.

```lean
theorem length_quotient_span_pow_le_and_eq_of_mem_nonZeroDivisors
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hdim : ringKrullDim R = 1) {x : R}
    (hx : x ∈ IsLocalRing.maximalIdeal R)
    (hx_min : ∀ p ∈ minimalPrimes R, x ∉ p) :
    let P : ℕ → ℕ∞ := fun n ↦ Module.length R (R ⧸ Ideal.span {x ^ n})
    (∀ n, P n ≠ ⊤) ∧
      (∀ n, P n ≤ (n : ℕ∞) * P 1) ∧
      (x ∈ nonZeroDivisors R → ∀ n, P n = (n : ℕ∞) * P 1)
```

## Tag 0BWT, a lemma

[Tag 0BWT](https://stacks.math.columbia.edu/tag/0BWT) in the Stacks Project.

**`natCard_minimalPrimes_le_length_quotient_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean#L392).

> **Stacks 0BWT.** The number of minimal primes of a one-dimensional Noetherian local ring is
> at most the length of its quotient by a parameter avoiding all minimal primes.

```lean
theorem natCard_minimalPrimes_le_length_quotient_span_singleton
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hdim : ringKrullDim R = 1) {x : R}
    (hx : x ∈ IsLocalRing.maximalIdeal R)
    (hx_min : ∀ p ∈ minimalPrimes R, x ∉ p) :
    Module.length R (R ⧸ Ideal.span {x}) ≠ ⊤ ∧
      (Nat.card (minimalPrimes R) : ℕ∞) ≤ Module.length R (R ⧸ Ideal.span {x})
```

## Tag 0BWU, a lemma

[Tag 0BWU](https://stacks.math.columbia.edu/tag/0BWU) in the Stacks Project.

**`exists_isSystemOfParameters_cons_of_avoids_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/SystemOfParameters.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/SystemOfParameters.lean#L176).

> **Stacks 0BWU.** In a Noetherian local ring of dimension `d > 1`, an element `f` of
> the maximal ideal which belongs to no minimal prime extends to a system of parameters
> `f, g₁, ..., g_{d-1}`, with every `gᵢ` lying in the prescribed power `m ^ k`.

```lean
theorem exists_isSystemOfParameters_cons_of_avoids_minimalPrimes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (d : ℕ) (hdim : ringKrullDim R = d) (hd : 1 < d)
    (f : R) (hf : f ∈ maximalIdeal R)
    (hfmin : ∀ p ∈ minimalPrimes R, f ∉ p) (k : ℕ) :
    ∃ gs : List R,
      gs.length = d - 1 ∧
        (∀ g ∈ gs, g ∈ maximalIdeal R ^ k) ∧
          IsSystemOfParameters (f :: gs)
```

## Tag 0BWV, a lemma

[Tag 0BWV](https://stacks.math.columbia.edu/tag/0BWV) in the Stacks Project.

**`exists_isSystemOfParameters_pair_add_of_avoids_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/SystemOfParameters.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/SystemOfParameters.lean#L255).

> **Stacks 0BWV.** In a two-dimensional Noetherian local ring, an element `f` of the maximal
> ideal which belongs to no minimal prime can be completed by an element `g` to a system of
> parameters. For every sufficiently high-order perturbation `f + h`, the pair `f + h, g` remains a
> system of parameters and defines a quotient of the same length as the quotient defined by
> `f, g`.

```lean
theorem exists_isSystemOfParameters_pair_add_of_avoids_minimalPrimes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hdim : ringKrullDim R = 2) (f : R) (hf : f ∈ maximalIdeal R)
    (hfmin : ∀ p ∈ minimalPrimes R, f ∉ p) :
    ∃ g ∈ maximalIdeal R, ∃ N : ℕ,
      IsSystemOfParameters [f, g] ∧
        ∀ h ∈ maximalIdeal R ^ N,
          IsSystemOfParameters [f + h, g] ∧
            Module.length R (R ⧸ Ideal.ofList [f, g]) =
              Module.length R (R ⧸ Ideal.ofList [f + h, g])
```

## Tag 0AXH, a lemma

[Tag 0AXH](https://stacks.math.columbia.edu/tag/0AXH) in the Stacks Project.

**`exists_nonzero_mem_isReduced_quotient_of_height_one_primes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Basic.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Basic.lean#L661).

> **Stacks 0AXH.** In a two-dimensional Noetherian normal local domain, finitely many
> height-one prime ideals contain a common nonzero element whose principal quotient is reduced.

```lean
theorem exists_nonzero_mem_isReduced_quotient_of_height_one_primes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] [IsDomain R]
    [IsIntegrallyClosed R] (hdim : ringKrullDim R = 2) (primes : Finset (Ideal R))
    (hprimes : ∀ p ∈ primes, p.IsPrime ∧ p.height = 1) :
    ∃ f : R, f ≠ 0 ∧ (∀ p ∈ primes, f ∈ p) ∧ IsReduced (R ⧸ Ideal.span {f})
```

## Tag 0AXI, a lemma

[Tag 0AXI](https://stacks.math.columbia.edu/tag/0AXI) in the Stacks Project.

**`exists_isReduced_quotient_and_dvd_pow`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Basic.lean, line 742](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Basic.lean#L742).

> **Stacks 0AXI.** In a two-dimensional Noetherian normal local domain, every nonzero element of
> the maximal ideal divides a power of an element whose principal quotient is reduced.

```lean
lemma exists_isReduced_quotient_and_dvd_pow
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] [IsDomain R]
    [IsIntegrallyClosed R] (hdim : ringKrullDim R = 2) {a : R}
    (_ha : a ∈ IsLocalRing.maximalIdeal R) (ha0 : a ≠ 0) :
    ∃ c : R, IsReduced (R ⧸ Ideal.span {c}) ∧ ∃ n : ℕ, a ∣ c ^ n
```

## Tag 0BWW, a lemma

[Tag 0BWW](https://stacks.math.columbia.edu/tag/0BWW) in the Stacks Project.

**`multiplicity_le_length_quotient_of_isSystemOfParameters`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean#L672).

> **Stacks 0BWW.** If `I` is generated by a system of parameters and the leading coefficient
> of its Hilbert–Samuel polynomial is `e / d!`, then `e ≤ length_R(R / I)`.

```lean
theorem multiplicity_le_length_quotient_of_isSystemOfParameters
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {gs : List R} (hgs : IsSystemOfParameters gs) {P : ℚ[X]}
    (hP : HilbertSamuel.IsHilbertSamuelPoly (Ideal.ofList gs) R P) {e : ℕ}
    (hlead : P.leadingCoeff = (e : ℚ) / gs.length.factorial) :
    (e : ℕ∞) ≤ Module.length R (R ⧸ Ideal.ofList gs)
```

## Tag 0BWX, a lemma

[Tag 0BWX](https://stacks.math.columbia.edu/tag/0BWX) in the Stacks Project.

**`natCard_fullDimensionalMinimalPrimes_le_length_quotient_of_isSystemOfParameters`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean, line 1195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Length.lean#L1195).

> **Stacks 0BWX.** In a Noetherian local ring, the number of minimal primes whose quotient
> has the full dimension of the ring is at most the length of the quotient by a system of
> parameters.

```lean
theorem natCard_fullDimensionalMinimalPrimes_le_length_quotient_of_isSystemOfParameters
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {gs : List R} (hgs : IsSystemOfParameters gs) :
    Module.length R (R ⧸ Ideal.ofList gs) ≠ ⊤ ∧
      (Nat.card {p : Ideal R // p ∈ minimalPrimes R ∧
        ringKrullDim (R ⧸ p) = ringKrullDim R} : ℕ∞) ≤
        Module.length R (R ⧸ Ideal.ofList gs)
```

## Tag 0BWY, a lemma

[Tag 0BWY](https://stacks.math.columbia.edu/tag/0BWY) in the Stacks Project.

**`exists_isSystemOfParameters_cons_stable_under_add_of_avoids_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/SystemOfParameters.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/SystemOfParameters.lean#L280).

> **Stacks 0BWY.** A parameter in the maximal ideal of a Noetherian local ring which avoids all
> minimal primes can be completed to a system of parameters such that perturbing the parameter by
> an element of a sufficiently high power of the maximal ideal preserves both the parameter system
> and the length of its quotient.

```lean
theorem exists_isSystemOfParameters_cons_stable_under_add_of_avoids_minimalPrimes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (d : ℕ) (hdim : ringKrullDim R = d)
    (f : R) (hf : f ∈ maximalIdeal R)
    (hfmin : ∀ p ∈ minimalPrimes R, f ∉ p) :
    ∃ gs : List R, ∃ N : ℕ,
      gs.length = d - 1 ∧
        (∀ g ∈ gs, g ∈ maximalIdeal R) ∧
          IsSystemOfParameters (f :: gs) ∧
            ∀ h ∈ maximalIdeal R ^ N,
              IsSystemOfParameters ((f + h) :: gs) ∧
                Module.length R (R ⧸ Ideal.ofList (f :: gs)) =
                  Module.length R (R ⧸ Ideal.ofList ((f + h) :: gs))
```

## Tag 0BWZ, a proposition

[Tag 0BWZ](https://stacks.math.columbia.edu/tag/0BWZ) in the Stacks Project.

**`exists_nonzero_mem_isReduced_quotient_of_isRadical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/PrincipalRadical/Basic.lean, line 1304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/PrincipalRadical/Basic.lean#L1304).

> **Stacks 0BWZ.** A nonzero radical ideal in a catenary Noetherian local normal domain
> contains a nonzero element whose principal quotient is reduced.

```lean
theorem exists_nonzero_mem_isReduced_quotient_of_isRadical
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] [IsDomain R]
    [IsIntegrallyClosed R] (hcat : Ring.IsCatenary R) (J : Ideal R) (hJ : J.IsRadical)
    (hJne : J ≠ ⊥) :
    ∃ f : R, f ≠ 0 ∧ f ∈ J ∧ IsReduced (R ⧸ Ideal.span {f})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.127, Tag 0BWR](https://stacks.math.columbia.edu/tag/0BWR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
