---
declaration: section
origin: cited
lean: Ring.KrullDimLE.of_isLocalization, Ring.KrullDimLE.isNilpotent_iff_mem_maximalIdeal, Ring.KrullDimLE.isField_of_isReduced, isField_localizationAtPrime_of_minimal, localizationProdMap_injective, exists_injective_ringHom_pi_field, iUnion_minimalPrimes_eq_zeroDivisors, fractionRing_equiv_fractionRing_localization
statement: formalized
proof: formalized
---

# 10.25 Zerodivisors and total rings of fractions

Section 10.25 of the Stacks Project, [Tag 02LV](https://stacks.math.columbia.edu/tag/02LV). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00EU, a lemma

[Tag 00EU](https://stacks.math.columbia.edu/tag/00EU) in the Stacks Project.

Declarations registered for the tag:

- [`Ring.KrullDimLE.of_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ring.KrullDimLE.of_isLocalization#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L132) (StacksFrontier): “localization at a minimal prime is zero-dimensional”.
- [`Ring.KrullDimLE.isNilpotent_iff_mem_maximalIdeal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ring.KrullDimLE.isNilpotent_iff_mem_maximalIdeal#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L134) (StacksFrontier): “maximal ideal consists of nilpotents”.
- [`Ring.KrullDimLE.isField_of_isReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ring.KrullDimLE.isField_of_isReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L136) (StacksFrontier): “reduced case: the localization is a field”. References: EGA IV (5.8.4), “partial”.

## Tag 00EW, a lemma

[Tag 00EW](https://stacks.math.columbia.edu/tag/00EW) in the Stacks Project.

**`isField_localizationAtPrime_of_minimal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean#L112). The attribute's comment: “2, the factors are fields”. References: EGA 0 (1.5.8), “reduced ring”; EGA IV (20.1.3.1), “field-stalk clause”.

> The localization of a reduced ring at a minimal prime is a field.

```lean
lemma isField_localizationAtPrime_of_minimal (R : Type*) [CommRing R] [IsReduced R]
    (p : Ideal R) (hp : p ∈ minimalPrimes R) :
    haveI : p.IsPrime := hp.isPrime
    IsField (Localization.AtPrime p)
```

**`localizationProdMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean#L154). The attribute's comment: “2, injectivity; the factors are fields by isField_localizationAtPrime_of_minimal”.

> The map `R → ∏_{p minimal} R_p` from a reduced commutative ring to the product of localizations
> at minimal primes is injective.

```lean
theorem localizationProdMap_injective (R : Type*) [CommRing R] [IsReduced R] :
    Function.Injective (localizationProdMap R)
```

**`exists_injective_ringHom_pi_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean#L166). The attribute's comment: “1”.

> A reduced commutative ring embeds into a product of fields, indexed by a type in the universe
> of `R`.

```lean
theorem exists_injective_ringHom_pi_field.{u} {R : Type u} [CommRing R]
    [IsReduced R] :
    ∃ (ι : Type u) (K : ι → Type u) (_ : ∀ i, Field (K i))
      (f : R →+* (∀ i, K i)), Function.Injective f
```

**`iUnion_minimalPrimes_eq_zeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MinimalPrimes/Reduced.lean#L205). The attribute's comment: “3”. References: EGA IV (20.1.3.1), “special case”.

> The union of the minimal primes of a reduced commutative ring equals its set of zero
> divisors.

```lean
theorem iUnion_minimalPrimes_eq_zeroDivisors (R : Type*) [CommRing R] [IsReduced R] :
    (⋃ p ∈ minimalPrimes R, (p : Set R)) = zeroDivisorSet R
```

## Tag 02LW, a lemma

[Tag 02LW](https://stacks.math.columbia.edu/tag/02LW) in the Stacks Project.

**`fractionRing_equiv_fractionRing_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/FractionRing.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/FractionRing.lean#L54).

> The total ring of fractions of `R` is isomorphic (as a ring) to the total ring of fractions of
> `S⁻¹R`, whenever `S` is a multiplicative subset of `R` consisting of nonzerodivisors.

```lean
theorem fractionRing_equiv_fractionRing_localization
    (R : Type*) [CommRing R] (S : Submonoid R) (hS : S ≤ nonZeroDivisors R) :
    Nonempty (FractionRing R ≃+* FractionRing (Localization S))
```

**`fractionRing_equiv_fractionRing_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/FractionRing.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/FractionRing.lean#L71).

> The total ring of fractions of `R` is isomorphic to the total ring of fractions of its own
> total ring of fractions: `Q(R) ≅ Q(Q(R))`.

```lean
theorem fractionRing_equiv_fractionRing_fractionRing
    (R : Type*) [CommRing R] :
    Nonempty (FractionRing R ≃+* FractionRing (FractionRing R))
```

## Tag 02LX, a lemma

[Tag 02LX](https://stacks.math.columbia.edu/tag/02LX) in the Stacks Project.

**`total_fraction_ring_isoProd_localization_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/FractionRing.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/FractionRing.lean#L183). References: EGA II (6.4.7), “partial”.

> Let `R` be a commutative ring whose set of minimal primes is finite and enumerated without
> repetition as `q_1, ..., q_t` (encoded by an injective family `q : Fin t → Ideal R` of minimal
> primes; the zerodivisor hypothesis forces it to enumerate every minimal prime). Assume moreover
> that the union of the minimal primes equals the set of zerodivisors of `R`. Then the total ring of
> fractions `Q(R) = FractionRing R` is isomorphic, as an `R`-algebra, to the finite product of the
> localizations `R_{q_i}`.
>
> (An `R`-algebra isomorphism between these localizations is automatically the canonical map
> induced by the universal property, since it must commute with the structure maps from `R`.)

```lean
theorem total_fraction_ring_isoProd_localization_atPrime
    {R : Type*} [CommRing R] (t : ℕ) (q : Fin t → Ideal R)
    (hmin : ∀ i, q i ∈ minimalPrimes R)
    (hinj : Function.Injective q)
    (hzd : zeroDivisorsSet R = ⋃ i, (q i : Set R)) :
    haveI : ∀ i, (q i).IsPrime := fun i => (hmin i).isPrime
    Nonempty (FractionRing R ≃ₐ[R] (∀ i, Localization.AtPrime (q i)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.25, Tag 02LV](https://stacks.math.columbia.edu/tag/02LV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
