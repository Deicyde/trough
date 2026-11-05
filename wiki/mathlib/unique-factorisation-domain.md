---
article_id: af_4b729714cc43a24e116b2d25
concept: UniqueFactorizationMonoid
---

A **unique factorisation domain** (UFD) is an integral domain in which every
nonzero non-unit is a product of [irreducible elements](trough:Irreducible), and
this product is unique up to the order of the factors and multiplication of the
factors by units. It is the setting in which the [fundamental theorem of
arithmetic](trough:Nat.primeFactorsList_unique) generalises: the integers,
polynomial rings over fields, and polynomial rings over the integers all have
unique factorisation, and in such rings greatest common divisors, coprimality and
divisibility can be read off from factorisations exactly as for whole numbers.

## Definition

Let $R$ be an integral domain, that is, a nonzero commutative [ring](trough:Ring)
without zero divisors. Two elements $a, b$ are associated if $b = au$ for a unit
$u$. Then $R$ is a [unique factorisation domain](lean:UniqueFactorizationMonoid) if

- every nonzero non-unit $a$ can be written as $a = p_1 p_2 \cdots p_m$ with each
  $p_i$ irreducible, and
- whenever $p_1 \cdots p_m = q_1 \cdots q_n$ with all $p_i$ and $q_j$ irreducible,
  then $m = n$ and, after reordering, each $p_i$ is associated with $q_i$.

Allowing an extra unit factor, the first condition says that every nonzero element
is associated with a product of irreducibles (the empty product $1$ covers the
units). An integral domain with both properties is a UFD in the sense of Mathlib's
definition: [existence and uniqueness of irreducible factorisations imply unique
factorisation](lean:UniqueFactorizationMonoid.of_existsUnique_irreducible_factors).
Conversely, in a UFD [every nonzero element is associated with a product of prime
elements](lean:UniqueFactorizationMonoid.exists_prime_factors), which are in
particular irreducible, and [two finite families of irreducible elements with
associated products can be matched up so that corresponding elements are
associated](lean:UniqueFactorizationMonoid.factors_unique).

An equivalent definition uses [prime elements](trough:Prime), the nonzero non-units
$p$ such that $p \mid ab$ implies $p \mid a$ or $p \mid b$:
[an integral domain is a UFD if and only if every nonzero element is associated with
a product of prime elements](lean:UniqueFactorizationMonoid.iff_exists_prime_factors).
Factorisations into primes are automatically unique, since a prime dividing a
product of primes must be associated with one of them and can be cancelled.

## Examples

- **Principal ideal domains.** [Every principal ideal domain is a
  UFD](lean:PrincipalIdealRing.to_uniqueFactorizationMonoid) (see [principal ideal
  domain](trough:Submodule.IsPrincipal)). Since [every Euclidean domain is a
  principal ideal domain](lean:EuclideanDomain.instIsPrincipalIdealRing) (see
  [Euclidean domain](trough:EuclideanDomain)), this covers the
  [integers](trough:Int), the Gaussian integers
  $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$, and the polynomial
  ring $K[X]$ over a field $K$. Fields are UFDs trivially, since they have no
  nonzero non-units.
- **Natural numbers.** The multiplicative monoid of the [natural
  numbers](trough:Nat) is not a ring, but it [satisfies Mathlib's unique
  factorisation axioms](lean:Nat.instUniqueFactorizationMonoid); this is the
  fundamental theorem of arithmetic.
- **Polynomial rings.** [If $D$ is a UFD, then so is the polynomial ring
  $D[X]$](lean:Polynomial.uniqueFactorizationMonoid), and, more generally,
  [the ring of polynomials over $D$ in any set of variables, finite or infinite, is a
  UFD](lean:MvPolynomial.uniqueFactorizationMonoid) (see [polynomial in several
  indeterminates](trough:MvPolynomial)). Thus $\mathbb{Z}[X]$ and $K[X, Y]$ are UFDs,
  although neither is a principal ideal domain: the ideals $(2, X)$ and $(X, Y)$ are
  not principal.
- **A non-example.** In $\mathbb{Z}[\sqrt{-5}]$ the elements $2$, $3$ and
  $1 \pm \sqrt{-5}$ are irreducible, and
  $$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$$
  are two factorisations of $6$ in which no factor on the left is associated with a
  factor on the right. So $\mathbb{Z}[\sqrt{-5}]$ is not a UFD, although it is
  [Noetherian](trough:IsNoetherianRing) and so every nonzero non-unit does have some
  factorisation into irreducibles.

## Properties

- **Irreducible equals prime.** In a UFD [an element is irreducible if and only if it
  is prime](lean:UniqueFactorizationMonoid.irreducible_iff_prime). In any integral
  domain [every prime element is irreducible](lean:Prime.irreducible), but the
  converse can fail, as the element $2$ of $\mathbb{Z}[\sqrt{-5}]$ shows.
- **Greatest common divisors.** Taking the smaller exponent of each prime factor
  shows that [every UFD has greatest common divisors and least common
  multiples](lean:UniqueFactorizationMonoid.toGCDMonoid) (see
  [greatest common divisor](trough:GCDMonoid.gcd)).
- **Integral closure.** [A UFD is integrally closed in its field of
  fractions](lean:UniqueFactorizationMonoid.instIsIntegrallyClosed) (see [field of
  fractions](trough:IsFractionRing)): a fraction in lowest terms that is a root of a
  monic polynomial with coefficients in the ring has a unit denominator. This
  generalises the irrationality of $\sqrt{2}$.
- **Kaplansky's criterion.** [An integral domain is a UFD exactly when each of its
  nonzero prime ideals contains a prime
  element](lean:UniqueFactorizationMonoid.iff_exists_prime_mem_of_isPrime) (see
  [prime ideal](trough:Ideal.IsPrime)).
- **Noetherian domains.** In a Noetherian integral domain [there is no infinite
  sequence of elements in which each element is nonzero and divides the one before
  with a non-unit cofactor](lean:IsNoetherianRing.wfDvdMonoid), so factorisations into
  irreducibles exist. A Noetherian domain is therefore a UFD exactly when its
  irreducibles are prime; equivalently, [a Noetherian domain is a UFD if and only if
  every prime ideal of height one, that is, every nonzero prime ideal containing no
  smaller nonzero prime ideal, is
  principal](lean:UniqueFactorizationMonoid.iff_forall_isPrincipal_of_height_eq_one).
- **Dedekind domains.** A Dedekind domain is a Noetherian, integrally closed
  integral domain in which every nonzero prime ideal is maximal. [A Dedekind domain
  that is a UFD is a principal ideal
  domain](lean:IsPrincipalIdealRing.of_isDedekindDomain_of_uniqueFactorizationMonoid),
  and [a Dedekind domain with finite class group is a principal ideal domain exactly
  when its class number, the order of that group, is
  $1$](lean:card_classGroup_eq_one_iff). The ring of integers of a number field is a
  Dedekind domain with [finite class
  group](trough:NumberField.RingOfIntegers.instFintypeClassGroup), so it has unique
  factorisation of elements exactly when its class number is $1$.

## Related concepts

The main classes of integral domains form a chain of inclusions: Euclidean domains,
principal ideal domains, unique factorisation domains, GCD domains, and integrally
closed domains. Each inclusion is strict; for example, the ring of all algebraic
integers has greatest common divisors but no irreducible elements at all (every
algebraic integer is the square of one), although it has nonzero non-units such as
$2$, so it is not a UFD. Unique factorisation of nonzero ideals into prime ideals,
rather than of elements, characterises Dedekind domains, and [Eisenstein's
criterion](trough:Polynomial.irreducible_of_eisenstein_criterion) is a test for
irreducibility in polynomial rings, most often applied over a UFD such as the
integers.

## In Mathlib

Mathlib defines unique factorisation for a commutative monoid with zero rather than
for a ring, and with different axioms: cancellation by nonzero elements, the absence
of infinite chains of proper divisors described above, and the equivalence of
irreducible and prime elements. These are equivalent to the textbook conditions, and
the existence of factorisations follows from them: [every nonzero element is
associated with a product of prime
elements](lean:UniqueFactorizationMonoid.exists_prime_factors). Uniqueness is stated
for unordered lists with repetition, matched up to association. A unique
factorisation domain is a commutative ring that is an integral domain and satisfies
this class; the class alone does not exclude the zero ring, since [a monoid with zero
that has only one element satisfies
it](lean:UniqueFactorizationMonoid.of_subsingleton). The same class covers the
natural numbers under multiplication, which form no ring.

## Depends on

- [Ring](trough:Ring)
- [Irreducible element](trough:Irreducible)
- [Prime numbers](trough:Prime)
