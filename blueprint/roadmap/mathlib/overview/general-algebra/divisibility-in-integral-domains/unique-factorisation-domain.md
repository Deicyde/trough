# Unique factorisation domain

A **unique factorisation domain** (UFD) is an integral domain in which every
nonzero non-unit is a product of [irreducible elements](irreducible-element.md), and
this product is unique up to the order of the factors and multiplication of the
factors by units. It is the setting in which the [fundamental theorem of arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md) generalises: the integers,
polynomial rings over fields, and polynomial rings over the integers all have
unique factorisation, and in such rings greatest common divisors, coprimality and
divisibility can be read off from factorisations exactly as for whole numbers.

## Definition

Let $R$ be an integral domain, that is, a nonzero commutative [ring](../rings/ring.md)
without zero divisors. Two elements $a, b$ are associated if $b = au$ for a unit
$u$. Then $R$ is a [unique factorisation domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid) if

- every nonzero non-unit $a$ can be written as $a = p_1 p_2 \cdots p_m$ with each
  $p_i$ irreducible, and
- whenever $p_1 \cdots p_m = q_1 \cdots q_n$ with all $p_i$ and $q_j$ irreducible,
  then $m = n$ and, after reordering, each $p_i$ is associated with $q_i$.

Allowing an extra unit factor, the first condition says that every nonzero element
is associated with a product of irreducibles (the empty product $1$ covers the
units). An integral domain with both properties is a UFD in the sense of Mathlib's
definition: [existence and uniqueness of irreducible factorisations imply unique factorisation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Basic.html#UniqueFactorizationMonoid.of_existsUnique_irreducible_factors).
Conversely, in a UFD [every nonzero element is associated with a product of prime elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid.exists_prime_factors), which are in
particular irreducible, and [two finite families of irreducible elements with associated products can be matched up so that corresponding elements are associated](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Basic.html#UniqueFactorizationMonoid.factors_unique).

An equivalent definition uses [prime elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md), the nonzero non-units
$p$ such that $p \mid ab$ implies $p \mid a$ or $p \mid b$:
[an integral domain is a UFD if and only if every nonzero element is associated with a product of prime elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Basic.html#UniqueFactorizationMonoid.iff_exists_prime_factors).
Factorisations into primes are automatically unique, since a prime dividing a
product of primes must be associated with one of them and can be cancelled.

## Examples

- **Principal ideal domains.** [Every principal ideal domain is a UFD](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#PrincipalIdealRing.to_uniqueFactorizationMonoid) (see [principal ideal domain](principal-ideal-domain.md)). Since [every Euclidean domain is a principal ideal domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#EuclideanDomain.instIsPrincipalIdealRing) (see
  [Euclidean domain](euclidean-domain.md)), this covers the
  [integers](../numbers/integer.md), the Gaussian integers
  $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$, and the polynomial
  ring $K[X]$ over a field $K$. Fields are UFDs trivially, since they have no
  nonzero non-units.
- **Natural numbers.** The multiplicative monoid of the [natural numbers](../numbers/natural-number.md) is not a ring, but it [satisfies Mathlib's unique factorisation axioms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Nat.html#Nat.instUniqueFactorizationMonoid); this is the
  fundamental theorem of arithmetic.
- **Polynomial rings.** [If $D$ is a UFD, then so is the polynomial ring $D[X]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/UniqueFactorization.html#Polynomial.uniqueFactorizationMonoid), and, more generally,
  [the ring of polynomials over $D$ in any set of variables, finite or infinite, is a UFD](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/UniqueFactorization.html#MvPolynomial.uniqueFactorizationMonoid) (see [polynomial in several indeterminates](../polynomials-and-power-series/polynomial-in-several-indeterminates.md)). Thus $\mathbb{Z}[X]$ and $K[X, Y]$ are UFDs,
  although neither is a principal ideal domain: the ideals $(2, X)$ and $(X, Y)$ are
  not principal.
- **A non-example.** In $\mathbb{Z}[\sqrt{-5}]$ the elements $2$, $3$ and
  $1 \pm \sqrt{-5}$ are irreducible, and
  $$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$$
  are two factorisations of $6$ in which no factor on the left is associated with a
  factor on the right. So $\mathbb{Z}[\sqrt{-5}]$ is not a UFD, although it is
  [Noetherian](../rings/noetherian-ring.md) and so every nonzero non-unit does have some
  factorisation into irreducibles.

## Properties

- **Irreducible equals prime.** In a UFD [an element is irreducible if and only if it is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid.irreducible_iff_prime). In any integral
  domain [every prime element is irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Prime/Defs.html#Prime.irreducible), but the
  converse can fail, as the element $2$ of $\mathbb{Z}[\sqrt{-5}]$ shows.
- **Greatest common divisors.** Taking the smaller exponent of each prime factor
  shows that [every UFD has greatest common divisors and least common multiples](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/GCDMonoid.html#UniqueFactorizationMonoid.toGCDMonoid) (see
  [greatest common divisor](greatest-common-divisor.md)).
- **Integral closure.** [A UFD is integrally closed in its field of fractions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/RationalRoot.html#UniqueFactorizationMonoid.instIsIntegrallyClosed) (see [field of fractions](../field-theory/field-of-fractions-of-an-integral-domain.md)): a fraction in lowest terms that is a root of a
  monic polynomial with coefficients in the ring has a unit denominator. This
  generalises the irrationality of $\sqrt{2}$.
- **Kaplansky's criterion.** [An integral domain is a UFD exactly when each of its nonzero prime ideals contains a prime element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Kaplansky.html#UniqueFactorizationMonoid.iff_exists_prime_mem_of_isPrime) (see
  [prime ideal](../ideals-and-quotients/prime-ideal.md)).
- **Noetherian domains.** In a Noetherian integral domain [there is no infinite sequence of elements in which each element is nonzero and divides the one before with a non-unit cofactor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Noetherian/UniqueFactorizationDomain.html#IsNoetherianRing.wfDvdMonoid), so factorisations into
  irreducibles exist. A Noetherian domain is therefore a UFD exactly when its
  irreducibles are prime; equivalently, [a Noetherian domain is a UFD if and only if every prime ideal of height one, that is, every nonzero prime ideal containing no smaller nonzero prime ideal, is principal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/UFD.html#UniqueFactorizationMonoid.iff_forall_isPrincipal_of_height_eq_one).
- **Dedekind domains.** A Dedekind domain is a Noetherian, integrally closed
  integral domain in which every nonzero prime ideal is maximal. [A Dedekind domain that is a UFD is a principal ideal domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/DedekindDomain/PID.html#IsPrincipalIdealRing.of_isDedekindDomain_of_uniqueFactorizationMonoid),
  and [a Dedekind domain with finite class group is a principal ideal domain exactly when its class number, the order of that group, is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/ClassGroup/Basic.html#card_classGroup_eq_one_iff). The ring of integers of a number field is a
  Dedekind domain with [finite class group](../algebraic-number-theory/finiteness-of-the-class-number.md), so it has unique
  factorisation of elements exactly when its class number is $1$.

## Related concepts

The main classes of integral domains form a chain of inclusions: Euclidean domains,
principal ideal domains, unique factorisation domains, GCD domains, and integrally
closed domains. Each inclusion is strict; for example, the ring of all algebraic
integers has greatest common divisors but no irreducible elements at all (every
algebraic integer is the square of one), although it has nonzero non-units such as
$2$, so it is not a UFD. Unique factorisation of nonzero ideals into prime ideals,
rather than of elements, characterises Dedekind domains, and [Eisenstein's criterion](../polynomials-and-power-series/eisensteins-criterion.md) is a test for
irreducibility in polynomial rings, most often applied over a UFD such as the
integers.

## In Mathlib

Mathlib defines unique factorisation for a commutative monoid with zero rather than
for a ring, and with different axioms: cancellation by nonzero elements, the absence
of infinite chains of proper divisors described above, and the equivalence of
irreducible and prime elements. These are equivalent to the textbook conditions, and
the existence of factorisations follows from them: [every nonzero element is associated with a product of prime elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid.exists_prime_factors). Uniqueness is stated
for unordered lists with repetition, matched up to association. A unique
factorisation domain is a commutative ring that is an integral domain and satisfies
this class; the class alone does not exclude the zero ring, since [a monoid with zero that has only one element satisfies it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid.of_subsingleton). The same class covers the
natural numbers under multiplication, which form no ring.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Irreducible element](irreducible-element.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)

## Sources

- [Mathlib documentation: `UniqueFactorizationMonoid`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid)
- [Source of `UniqueFactorizationMonoid` in Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.lean#L113)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L86)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L144)
