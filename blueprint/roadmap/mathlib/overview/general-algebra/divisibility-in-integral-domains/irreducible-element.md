# Irreducible element

An **irreducible element** of a commutative [ring](../rings/ring.md) or monoid is a
non-unit that cannot be split as a product of two non-units: whenever it is
written as a product, one of the factors is a unit. Irreducible elements play the
role that prime numbers play among the [natural numbers](../numbers/natural-number.md), as the
smallest building blocks of multiplication. They are the elements that appear in
factorizations, and the question of when such factorizations are unique leads to
the theory of [unique factorization domains](unique-factorisation-domain.md).

## Definition

Let $M$ be a monoid, written multiplicatively, and recall that a unit of $M$ is an
element with a two-sided inverse. An element $p$ of $M$ is
[irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Irreducible/Defs.html#Irreducible) when

- $p$ is not a unit, and
- whenever $p = ab$ with $a, b \in M$, at least one of $a$ and $b$ is a unit.

Equivalently, [$p$ is irreducible exactly when it is not a unit and every factorization of $p$ has a unit factor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Irreducible/Defs.html#irreducible_iff). In an integral
domain $R$ the usual textbook definition asks in addition that $p \neq 0$, but this
is automatic: if $0$ were irreducible, the factorization $0 = 0 \cdot 0$ would force
$0$ to be a unit, contradicting the first condition. So [an irreducible element of a monoid with zero is never zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Prime/Defs.html#Irreducible.ne_zero).

Irreducibility depends only on $p$ up to units. Two elements $p$ and $q$ of a
commutative monoid are associated if $q = pu$ for a unit $u$, and [an element associated with an irreducible element is again irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Associated.html#Associated.irreducible).
For instance $p$ is irreducible in $\mathbb{Z}$ if and only if $-p$ is.

## Examples

- **Natural numbers.** In the multiplicative monoid of the natural numbers the
  only unit is $1$, and [the irreducible elements are exactly the prime numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Prime/Defs.html#Nat.irreducible_iff_nat_prime).
- **Integers.** The units of $\mathbb{Z}$ are $\pm 1$, so the irreducible elements
  of the [integers](../numbers/integer.md) are the numbers $\pm p$ with $p$ a prime number.
- **Polynomials over a field.** If $K$ is a field, the units of $K[X]$ are the
  nonzero constants, and
  [every polynomial of degree $1$ is irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.irreducible_of_degree_eq_one).
  Over a field, [a polynomial of degree $2$ or $3$ is irreducible exactly when it has no root in the field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/SpecificDegree.html#Polynomial.irreducible_iff_roots_eq_zero_of_degree_le_three),
  since any nontrivial factorization would include a factor of degree $1$. So
  $X^2 + 1$ is irreducible over $\mathbb{R}$, while over the
  [complex numbers](../numbers/complex-number.md) it factors as $(X - i)(X + i)$. Over an
  [algebraically closed field](../field-theory/algebraically-closed-field.md),
  [every irreducible polynomial has degree $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.degree_eq_one_of_irreducible).
- **Gaussian integers.** A prime number need not stay irreducible in a larger ring.
  In $\mathbb{Z}[i]$ one has $2 = (1 + i)(1 - i)$ and $5 = (2 + i)(2 - i)$, with no
  factor a unit, while $3$ remains irreducible. In fact
  [a prime number that is not irreducible in $\mathbb{Z}[i]$ is a sum of two squares](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Zsqrtd/GaussianInt.html#GaussianInt.sq_add_sq_of_nat_prime_of_not_irreducible), which is
  one route to the [two-squares theorem](../number-theory/sum-of-two-squares.md).
- **Non-examples.** Units, and in particular $1$, are never irreducible; neither is
  $0$ in a ring. A power is never irreducible unless the exponent is $1$:
  [for $n \neq 1$, the element $x^n$ is not irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Irreducible/Lemmas.html#not_irreducible_pow).

## Irreducible and prime elements

A [prime element](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) $p$ of a commutative ring is a nonzero non-unit
such that $p \mid ab$ implies $p \mid a$ or $p \mid b$. In an integral domain
[every prime element is irreducible](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Prime/Defs.html#Prime.irreducible): if $p = ab$, then $p$
divides $a$ or $b$, say $a = pc$, and cancelling $p$ from $p = pcb$ shows that $b$
is a unit.

The converse fails in general. In the ring $\mathbb{Z}[\sqrt{-5}]$, consider the
norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$, which is multiplicative. The elements of norm $1$
are exactly the units $\pm 1$, so a factorization of $2$, of norm $4$, into two
non-units would need two factors of norm $2$. No element has norm $2$ (nor $3$),
so $2$ is irreducible. Yet
$$2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}),$$
and $2$ divides neither factor on the right, so $2$ is not prime. The same equation
shows that $6$ has two essentially different factorizations into irreducibles.

The converse does hold in the rings of most interest. In a unique factorization
domain, [an element is irreducible if and only if it is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#UniqueFactorizationMonoid.irreducible_iff_prime); indeed this
equivalence, together with the existence of factorizations, characterizes such
domains. More generally,
call $a$ primal if whenever $a \mid bc$ one can write $a = a_1 a_2$ with
$a_1 \mid b$ and $a_2 \mid c$;
[in a cancellative commutative monoid with zero in which every element is primal, such as a GCD domain, irreducible and prime elements coincide](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Prime/Defs.html#irreducible_iff_prime).

## Properties

- **Existence of factorizations.** In a commutative monoid with zero with no
  infinite sequence $a_1, a_2, \dots$ of nonzero elements in which each
  $a_n = a_{n+1} x_n$ for a non-unit $x_n$, [every nonzero element is a product of irreducible elements, up to a unit factor](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/Defs.html#WfDvdMonoid.exists_factors). This applies to every
  [Noetherian](../rings/noetherian-ring.md) integral domain.
- **Maximal ideals.** In a [principal ideal domain](principal-ideal-domain.md),
  [a nonzero element $p$ is irreducible if and only if the ideal $(p)$ is maximal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#Ideal.irreducible_iff_isMaximal_span_singleton) (see
  [maximal ideal](../ideals-and-quotients/maximal-ideal.md)). For a field $K$ this means that
  $K[X]/(f)$ is a field exactly when $f$ is irreducible, the basis of the
  construction of the [rupture field](../field-theory/rupture-field.md).
- **Divisibility between irreducibles.** [If $p$ and $q$ are irreducible and $p$ divides $q$, then $q$ divides $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Prime/Defs.html#Irreducible.dvd_symm). Indeed, writing
  $q = pu$, irreducibility of $q$ and the fact that $p$ is not a unit force $u$ to
  be a unit, so $p$ and $q$ are associated.

## Related concepts

Tests for irreducibility of polynomials include
[Eisenstein's criterion](../polynomials-and-power-series/eisensteins-criterion.md) and
reduction modulo a prime. The [minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md) of an algebraic
element over a field is irreducible. In a principal ideal domain, two elements
that are not both zero are [coprime](coprime-element.md) exactly when they have no
irreducible common factor, that is, when their
[greatest common divisor](greatest-common-divisor.md) is a unit.

## In Mathlib

Mathlib defines irreducibility for an arbitrary monoid, which need not be
commutative or have a zero element, as a structure recording the two conditions: not a
unit, and a unit factor in every factorization. It deliberately leaves out the
condition $p \neq 0$, which would require a zero element; in a monoid with zero it
follows as a lemma. The same definition therefore serves rings, the natural
numbers under multiplication, and monoids of associated classes, and Mathlib also has an
additive version, written out separately and paired with it so that lemmas
transfer between the two. Mathlib's prime numbers are defined as the
irreducible elements of the natural numbers, which makes the natural-number example
hold by definition. Prime elements form a separate notion, and Mathlib's
unique factorization monoids are required to satisfy the equivalence of the two as
one of their axioms.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `Irreducible`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Irreducible/Defs.html#Irreducible)
- [Source of `Irreducible` in Mathlib/Algebra/Group/Irreducible/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Group/Irreducible/Defs.lean#L40)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L84)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L104)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L141)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L159)
