---
article_id: af_cb60ae3629bbcc5e2ee06c20
concept: Irreducible
---

An **irreducible element** of a commutative [ring](trough:Ring) or monoid is a
non-unit that cannot be split as a product of two non-units: whenever it is
written as a product, one of the factors is a unit. Irreducible elements play the
role that prime numbers play among the [natural numbers](trough:Nat), as the
smallest building blocks of multiplication. They are the elements that appear in
factorizations, and the question of when such factorizations are unique leads to
the theory of [unique factorization domains](trough:UniqueFactorizationMonoid).

## Definition

Let $M$ be a monoid, written multiplicatively, and recall that a unit of $M$ is an
element with a two-sided inverse. An element $p$ of $M$ is
[irreducible](lean:Irreducible) when

- $p$ is not a unit, and
- whenever $p = ab$ with $a, b \in M$, at least one of $a$ and $b$ is a unit.

Equivalently, [$p$ is irreducible exactly when it is not a unit and every
factorization of $p$ has a unit factor](lean:irreducible_iff). In an integral
domain $R$ the usual textbook definition asks in addition that $p \neq 0$, but this
is automatic: if $0$ were irreducible, the factorization $0 = 0 \cdot 0$ would force
$0$ to be a unit, contradicting the first condition. So [an irreducible element of a
monoid with zero is never zero](lean:Irreducible.ne_zero).

Irreducibility depends only on $p$ up to units. Two elements $p$ and $q$ of a
commutative monoid are associated if $q = pu$ for a unit $u$, and [an element
associated with an irreducible element is again irreducible](lean:Associated.irreducible).
For instance $p$ is irreducible in $\mathbb{Z}$ if and only if $-p$ is.

## Examples

- **Natural numbers.** In the multiplicative monoid of the natural numbers the
  only unit is $1$, and [the irreducible elements are exactly the prime
  numbers](lean:Nat.irreducible_iff_nat_prime).
- **Integers.** The units of $\mathbb{Z}$ are $\pm 1$, so the irreducible elements
  of the [integers](trough:Int) are the numbers $\pm p$ with $p$ a prime number.
- **Polynomials over a field.** If $K$ is a field, the units of $K[X]$ are the
  nonzero constants, and
  [every polynomial of degree $1$ is irreducible](lean:Polynomial.irreducible_of_degree_eq_one).
  Over a field, [a polynomial of degree $2$ or $3$ is irreducible exactly when it
  has no root in the field](lean:Polynomial.irreducible_iff_roots_eq_zero_of_degree_le_three),
  since any nontrivial factorization would include a factor of degree $1$. So
  $X^2 + 1$ is irreducible over $\mathbb{R}$, while over the
  [complex numbers](trough:Complex) it factors as $(X - i)(X + i)$. Over an
  [algebraically closed field](trough:IsAlgClosed),
  [every irreducible polynomial has degree $1$](lean:IsAlgClosed.degree_eq_one_of_irreducible).
- **Gaussian integers.** A prime number need not stay irreducible in a larger ring.
  In $\mathbb{Z}[i]$ one has $2 = (1 + i)(1 - i)$ and $5 = (2 + i)(2 - i)$, with no
  factor a unit, while $3$ remains irreducible. In fact
  [a prime number that is not irreducible in $\mathbb{Z}[i]$ is a sum of two
  squares](lean:GaussianInt.sq_add_sq_of_nat_prime_of_not_irreducible), which is
  one route to the [two-squares theorem](trough:Nat.Prime.sq_add_sq).
- **Non-examples.** Units, and in particular $1$, are never irreducible; neither is
  $0$ in a ring. A power is never irreducible unless the exponent is $1$:
  [for $n \neq 1$, the element $x^n$ is not irreducible](lean:not_irreducible_pow).

## Irreducible and prime elements

A [prime element](trough:Prime) $p$ of a commutative ring is a nonzero non-unit
such that $p \mid ab$ implies $p \mid a$ or $p \mid b$. In an integral domain
[every prime element is irreducible](lean:Prime.irreducible): if $p = ab$, then $p$
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
domain, [an element is irreducible if and only if it is
prime](lean:UniqueFactorizationMonoid.irreducible_iff_prime); indeed this
equivalence, together with the existence of factorizations, characterizes such
domains. More generally,
call $a$ primal if whenever $a \mid bc$ one can write $a = a_1 a_2$ with
$a_1 \mid b$ and $a_2 \mid c$;
[in a cancellative commutative monoid with zero in which every element is primal,
such as a GCD domain, irreducible and prime elements coincide](lean:irreducible_iff_prime).

## Properties

- **Existence of factorizations.** In a commutative monoid with zero with no
  infinite sequence $a_1, a_2, \dots$ of nonzero elements in which each
  $a_n = a_{n+1} x_n$ for a non-unit $x_n$, [every
  nonzero element is a product of irreducible elements, up to a unit
  factor](lean:WfDvdMonoid.exists_factors). This applies to every
  [Noetherian](trough:IsNoetherianRing) integral domain.
- **Maximal ideals.** In a [principal ideal domain](trough:Submodule.IsPrincipal),
  [a nonzero element $p$ is irreducible if and only if the ideal $(p)$ is
  maximal](lean:Ideal.irreducible_iff_isMaximal_span_singleton) (see
  [maximal ideal](trough:Ideal.IsMaximal)). For a field $K$ this means that
  $K[X]/(f)$ is a field exactly when $f$ is irreducible, the basis of the
  construction of the [rupture field](trough:AdjoinRoot).
- **Divisibility between irreducibles.** [If $p$ and $q$ are irreducible and $p$
  divides $q$, then $q$ divides $p$](lean:Irreducible.dvd_symm). Indeed, writing
  $q = pu$, irreducibility of $q$ and the fact that $p$ is not a unit force $u$ to
  be a unit, so $p$ and $q$ are associated.

## Related concepts

Tests for irreducibility of polynomials include
[Eisenstein's criterion](trough:Polynomial.irreducible_of_eisenstein_criterion) and
reduction modulo a prime. The [minimal polynomial](trough:minpoly) of an algebraic
element over a field is irreducible. In a principal ideal domain, two elements
that are not both zero are [coprime](trough:IsCoprime) exactly when they have no
irreducible common factor, that is, when their
[greatest common divisor](trough:GCDMonoid.gcd) is a unit.

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

## Depends on

- [Ring](trough:Ring)
