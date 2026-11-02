---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.primeFactorsList_unique, Int.euclideanDomain, EuclideanDomain.instIsPrincipalIdealRing, UniqueFactorizationMonoid, UniqueFactorizationMonoid.factors_unique
mathlib_file: Mathlib/Data/Nat/Factors.lean
---

# The Fundamental Theorem of Arithmetic

Mathlib records this with 5 declarations.

`Nat.primeFactorsList_unique`: **Fundamental theorem of arithmetic**

```lean
Nat.primeFactorsList_unique {n : ℕ} {l : List ℕ} (h₁ : l.prod = n) (h₂ : ∀ p ∈ l, Nat.Prime p) :
  l.Perm n.primeFactorsList
```

`Int.euclideanDomain`.

```lean
Int.euclideanDomain : EuclideanDomain ℤ
```

`EuclideanDomain.instIsPrincipalIdealRing`.

```lean
EuclideanDomain.instIsPrincipalIdealRing.{u} {R : Type u} [EuclideanDomain R] :
  IsPrincipalIdealRing R
```

`UniqueFactorizationMonoid`: Unique factorization monoids are defined as cancellative `CommMonoidWithZero`s with well-founded
strict divisibility relations, but this is equivalent to more familiar definitions:

Each element (except zero) is uniquely represented as a multiset of irreducible factors.
Uniqueness is only up to associated elements.

Each element (except zero) is non-uniquely represented as a multiset
of prime factors.

To define a UFD using the definition in terms of multisets
of irreducible factors, use the definition `of_existsUnique_irreducible_factors`

To define a UFD using the definition in terms of multisets
of prime factors, use the definition `of_exists_prime_factors`

```lean
UniqueFactorizationMonoid.{u_2} (α : Type u_2) [CommMonoidWithZero α] : Prop
```

`UniqueFactorizationMonoid.factors_unique`.

```lean
UniqueFactorizationMonoid.factors_unique.{u_1} {α : Type u_1} [CommMonoidWithZero α]
  [UniqueFactorizationMonoid α] {f g : Multiset α} (hf : ∀ x ∈ f, Irreducible x)
  (hg : ∀ x ∈ g, Irreducible x) (h : Associated f.prod g.prod) : Multiset.Rel Associated f g
```

it also has a generalized version, by showing that every Euclidean domain is a unique factorization domain, and showing that the integers form a Euclidean domain.

## Depends on

- [Euclidean domain](../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Ideal of a commutative ring](../../overview/general-algebra/ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Irreducible element](../../overview/general-algebra/divisibility-in-integral-domains/irreducible-element.md)
- [Multiset](../../overview/data-structures/sets/multiset.md)
- [Prime numbers](../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Principal ideal domain](../../overview/general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Ring structure $\Z$](../../undergraduate/ring-theory/fundamentals/ring-structure.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)

## Sources

- [Mathlib documentation: `Nat.primeFactorsList_unique`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Factors.html#Nat.primeFactorsList_unique)
- [Source of `Nat.primeFactorsList_unique` in Mathlib/Data/Nat/Factors.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Nat/Factors.lean#L168)
- [Mathlib documentation: `Int.euclideanDomain`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Int.html#Int.euclideanDomain)
- [Source of `Int.euclideanDomain` in Mathlib/Algebra/EuclideanDomain/Int.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/EuclideanDomain/Int.lean#L25)
- [Mathlib documentation: `EuclideanDomain.instIsPrincipalIdealRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#EuclideanDomain.instIsPrincipalIdealRing)
- [Source of `EuclideanDomain.instIsPrincipalIdealRing` in Mathlib/RingTheory/PrincipalIdealDomain.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/PrincipalIdealDomain.lean#L287)
- [Mathlib documentation: `UniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid)
- [Source of `UniqueFactorizationMonoid` in Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean#L113)
- [Mathlib documentation: `UniqueFactorizationMonoid.factors_unique`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Basic.html#UniqueFactorizationMonoid.factors_unique)
- [Source of `UniqueFactorizationMonoid.factors_unique` in Mathlib/RingTheory/UniqueFactorizationDomain/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/UniqueFactorizationDomain/Basic.lean#L109)
- [Freek Wiedijk's 100 theorems, no. 80](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L405)
- [1000+ theorems list: Q670235](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L735)
- [1000+ theorems project: Q670235](https://1000-plus.github.io/?length=-1#Q670235)
- [Wikipedia: Fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)
- [Wikidata: Q670235](https://www.wikidata.org/wiki/Q670235)
