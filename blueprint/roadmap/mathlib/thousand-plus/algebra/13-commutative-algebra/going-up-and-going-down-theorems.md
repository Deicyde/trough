---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Ideal.exists_ideal_over_prime_of_isIntegral_of_isDomain, Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime, Algebra.HasGoingDown.iff_generalizingMap_primeSpectrumComap, Algebra.HasGoingDown.of_comap_localRingHom_surjective
mathlib_file: Mathlib/RingTheory/Ideal/GoingUp.lean
---

# Going-up and going-down theorems

Mathlib records this with 4 declarations.

`Ideal.exists_ideal_over_prime_of_isIntegral_of_isDomain`: `comap (algebraMap R S)` is a surjection from the prime spec of `R` to prime spec of `S`.
`hP : (algebraMap R S).ker ≤ P` is a slight generalization of the extension being injective

```lean
Ideal.exists_ideal_over_prime_of_isIntegral_of_isDomain.{u_1, u_2} {R : Type u_1} [CommRing R]
  {S : Type u_2} [CommRing S] [Algebra R S] [IsDomain S] [Algebra.IsIntegral R S] (P : Ideal R)
  [P.IsPrime] (hP : RingHom.ker (algebraMap R S) ≤ P) : ∃ Q, Q.IsPrime ∧ Ideal.under R Q = P
```

`Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime`: More general going-up theorem than `exists_ideal_over_prime_of_isIntegral_of_isDomain`.
Generalized to arbitrary length chains in `Ideal.exists_ltSeries_of_hasGoingUp`.

```lean
Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime.{u_1, u_2} {R : Type u_1} [CommRing R]
  {S : Type u_2} [CommRing S] [Algebra R S] [Algebra.IsIntegral R S] (P : Ideal R) [P.IsPrime]
  (I : Ideal S) [I.IsPrime] (hIP : Ideal.under R I ≤ P) : ∃ Q ≥ I, Q.IsPrime ∧ Ideal.under R Q = P
```

`Algebra.HasGoingDown.iff_generalizingMap_primeSpectrumComap`: An `R`-algebra `S` has the going down property if and only if generalizations lift
along `Spec S → Spec R`.

```lean
Algebra.HasGoingDown.iff_generalizingMap_primeSpectrumComap.{u_3, u_4} {R : Type u_3} {S : Type u_4}
  [CommRing R] [CommRing S] [Algebra R S] :
  Algebra.HasGoingDown R S ↔ GeneralizingMap (PrimeSpectrum.comap (algebraMap R S))
```

`Algebra.HasGoingDown.of_comap_localRingHom_surjective`: If for every prime of `S`, the map `Spec Sₚ → Spec Rₚ` is surjective,
the algebra satisfies going down.

```lean
Algebra.HasGoingDown.of_comap_localRingHom_surjective.{u_3, u_4} {R : Type u_3} {S : Type u_4}
  [CommRing R] [CommRing S] [Algebra R S]
  (H :
    ∀ (P : Ideal S) [inst : P.IsPrime],
      Function.Surjective
        (PrimeSpectrum.comap (Localization.localRingHom (Ideal.under R P) P (algebraMap R S) ⋯))) :
  Algebra.HasGoingDown R S
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Filter](../../../overview/topology/general-topology/part-01/filter.md)
- [Localization](../../../overview/general-algebra/rings/localization.md)
- [Polynomial in one indeterminate](../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Ring](../../../overview/general-algebra/rings/ring.md)
- [Zariski topology](../../../overview/geometry/algebraic-geometry/zariski-topology.md)

## Proof depends on

- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Local ring](../../../overview/general-algebra/rings/local-ring.md)
- [Maximal ideal](../../../overview/general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Quotient ring](../../../overview/general-algebra/ideals-and-quotients/quotient-ring.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Ideal.exists_ideal_over_prime_of_isIntegral_of_isDomain`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/GoingUp.html#Ideal.exists_ideal_over_prime_of_isIntegral_of_isDomain)
- [Source of `Ideal.exists_ideal_over_prime_of_isIntegral_of_isDomain` in Mathlib/RingTheory/Ideal/GoingUp.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/GoingUp.lean#L308)
- [Mathlib documentation: `Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/GoingUp.html#Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime)
- [Source of `Ideal.exists_ideal_over_prime_of_isIntegral_of_isPrime` in Mathlib/RingTheory/Ideal/GoingUp.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/GoingUp.lean#L329)
- [Mathlib documentation: `Algebra.HasGoingDown.iff_generalizingMap_primeSpectrumComap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/GoingDown.html#Algebra.HasGoingDown.iff_generalizingMap_primeSpectrumComap)
- [Source of `Algebra.HasGoingDown.iff_generalizingMap_primeSpectrumComap` in Mathlib/RingTheory/Ideal/GoingDown.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/GoingDown.lean#L103)
- [Mathlib documentation: `Algebra.HasGoingDown.of_comap_localRingHom_surjective`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/GoingDown.html#Algebra.HasGoingDown.of_comap_localRingHom_surjective)
- [Source of `Algebra.HasGoingDown.of_comap_localRingHom_surjective` in Mathlib/RingTheory/Ideal/GoingDown.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/GoingDown.lean#L134)
- [1000+ theorems list: Q2379132](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2196)
- [1000+ theorems project: Q2379132](https://1000-plus.github.io/?length=-1#Q2379132)
- [Wikipedia: Going up and going down](https://en.wikipedia.org/wiki/Going_up_and_going_down)
- [Wikidata: Q2379132](https://www.wikidata.org/wiki/Q2379132)
