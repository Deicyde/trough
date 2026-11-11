---
declaration: section
origin: cited
lean: ideal_eq_mul_colon_of_isPrincipal, isOkaFamilyUniversal_meetsSubmonoidFamily, Ideal.isOka_fg, Ideal.isOka_isPrincipal, Ideal.isPrime_of_maximally_disjoint, Ideal.IsOka.isPrime_of_maximal_not, IsNoetherianRing.of_prime, isNoetherianRing_iff_ideal_fg
statement: formalized
proof: formalized
---

# 10.28 A meta-observation about prime ideals

Section 10.28 of the Stacks Project, [Tag 05K7](https://stacks.math.columbia.edu/tag/05K7). 8 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05K8, a lemma

[Tag 05K8](https://stacks.math.columbia.edu/tag/05K8) in the Stacks Project.

**`ideal_eq_mul_colon_of_isPrincipal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/Colon.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/Colon.lean#L29).

> For a commutative ring `R`, a principal ideal `J` and an ideal `I` with
> `I ≤ J`, the ideal `I` factors as the product of `J` with the colon ideal
> `(I : J)`.

```lean
theorem ideal_eq_mul_colon_of_isPrincipal {R : Type*} [CommRing R]
    (I J : Ideal R) (hJ : J.IsPrincipal) (hIJ : I ≤ J) :
    I = J * (I.colon J)
```

## Tag 05KA, an example

[Tag 05KA](https://stacks.math.columbia.edu/tag/05KA) in the Stacks Project.

**`isOkaFamilyUniversal_meetsSubmonoidFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/OkaFamily.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/OkaFamily.lean#L93).

> **Stacks Tag 05KA.** For a commutative semiring `R` and a multiplicative subset
> `S` of `R`, the family of ideals meeting `S` is an Oka family.

```lean
theorem isOkaFamilyUniversal_meetsSubmonoidFamily {R : Type*} [CommSemiring R]
    (S : Submonoid R) : IsOkaFamilyUniversal (meetsSubmonoidFamily S)
```

## Tag 05KB, an example

[Tag 05KB](https://stacks.math.columbia.edu/tag/05KB) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.isOka_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.isOka_fg#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/OkaFamily.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/OkaFamily.lean#L32) (StacksFrontier): “the Oka-family conclusion”.

## Tag 05KC, an example

[Tag 05KC](https://stacks.math.columbia.edu/tag/05KC) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.isOka_isPrincipal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.isOka_isPrincipal#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/OkaFamily.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/OkaFamily.lean#L33) (StacksFrontier).

## Tag 05KF, a lemma

[Tag 05KF](https://stacks.math.columbia.edu/tag/05KF) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.isPrime_of_maximally_disjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.isPrime_of_maximally_disjoint#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L23) (StacksFrontier).

## Tag 05KG, a lemma

[Tag 05KG](https://stacks.math.columbia.edu/tag/05KG) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.isOka_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.isOka_fg#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L27) (StacksFrontier): “(1): `Ideal.FG` is an Oka predicate”.
- [`Ideal.IsOka.isPrime_of_maximal_not`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsOka.isPrime_of_maximal_not#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L28) (StacksFrontier): “(1)”.
- [`IsNoetherianRing.of_prime`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsNoetherianRing.of_prime#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L32) (StacksFrontier): “(2)”.
- [`isNoetherianRing_iff_ideal_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isNoetherianRing_iff_ideal_fg#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L33) (StacksFrontier): “(2)”.

## Tag 05KH, a lemma

[Tag 05KH](https://stacks.math.columbia.edu/tag/05KH) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.IsOka.isPrime_of_maximal_not`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.IsOka.isPrime_of_maximal_not#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L278) (StacksFrontier): “(1), for the Oka family `Submodule.IsPrincipal` (`Ideal.isOka_isPrincipal`)”.
- [`IsPrincipalIdealRing.of_prime`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPrincipalIdealRing.of_prime#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L281) (StacksFrontier): “(2)”.

## Tag 05KI, a lemma

[Tag 05KI](https://stacks.math.columbia.edu/tag/05KI) in the Stacks Project.

**`Ideal.isPrime_of_maximal_disjoint_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L64). The attribute's comment: “(1)”.

> An ideal maximal among the ideals which do not contain a nonzerodivisor is prime.

```lean
theorem Ideal.isPrime_of_maximal_disjoint_nonZeroDivisors {R : Type*} [CommSemiring R]
    (I : Ideal R) (hI : Maximal (fun J : Ideal R ↦ Disjoint (J : Set R) (R⁰ : Set R)) I) :
    I.IsPrime
```

**`isDomain_of_forall_nonzero_prime_containsNonZeroDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/MaximalCriteriaForPrime.lean#L74). The attribute's comment: “(2)”.

> (Characterization of a domain.) If `R` is nonzero and every nonzero prime
> ideal of `R` contains a nonzerodivisor, then `R` is a domain.

```lean
theorem isDomain_of_forall_nonzero_prime_containsNonZeroDivisor [Nontrivial R]
    (h : ∀ P : Ideal R, P.IsPrime → P ≠ ⊥ →
      ¬ Disjoint (P : Set R) (nonZeroDivisors R : Set R)) :
    IsDomain R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.28, Tag 05K7](https://stacks.math.columbia.edu/tag/05K7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
