---
article_id: af_79357b10507c88c794242a5f
declaration: class
origin: cited
mathlib: true
mathlib_declaration: EuclideanDomain
mathlib_file: Mathlib/Algebra/EuclideanDomain/Defs.lean
---

# Euclidean domain

A **Euclidean domain** is an integral domain in which one can divide with
remainder, the remainder being smaller than the divisor for some measure of
size. The [integers](../numbers/integer.md), every [field](../field-theory/field.md) and the
[polynomials over a field](../polynomials-and-power-series/k-x-is-euclidean.md) are the main
examples. Division with remainder is exactly what the Euclidean algorithm needs,
so in a Euclidean domain greatest common divisors can be computed, every ideal is
principal, and factorization into irreducible elements is unique.

## Definition

An integral domain $R$, that is, a nonzero commutative [ring](../rings/ring.md) without
zero divisors, is Euclidean if there is a function $f$ from the nonzero elements
of $R$ to the [natural numbers](../numbers/natural-number.md) with the following property: for all
$a, b \in R$ with $b \neq 0$ there are $q, r \in R$ such that

$$a = bq + r, \qquad r = 0 \ \text{or}\ f(r) < f(b).$$

The element $q$ is a quotient and $r$ a remainder of $a$ on division by $b$; they
need not be unique. Such an $f$ is called a Euclidean function. Many authors also
require $f(a) \le f(ab)$ for all nonzero $a$ and $b$. This changes nothing about
which rings are Euclidean, since a Euclidean function $f$ can always be replaced by
$a \mapsto \min_{c \neq 0} f(ac)$, which has the extra property.

Mathlib's [definition of a Euclidean domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain) is more general
in one respect. Instead of a function to the natural numbers it asks for a
well-founded relation $\prec$ on $R$, one with no infinite descending chain
$\cdots \prec x_2 \prec x_1$. A function $f$ gives such a relation by declaring
$x \prec y$ when $f(x) < f(y)$, with $0$ placed below every nonzero element. The
structure also carries chosen quotient and remainder operations, written $a / b$
and $a \bmod b$, which satisfy
[$b\,(a/b) + (a \bmod b) = a$ for all $a$ and $b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain.div_add_mod)
and [$(a \bmod b) \prec b$ whenever $b \neq 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain.mod_lt), together
with $a/0 = 0$ and the analogue of $f(a) \le f(ab)$: for $b \neq 0$, never
$ab \prec a$. Rings that are Euclidean in this wider sense are sometimes called
transfinite Euclidean domains, and there are such rings that admit no Euclidean
function with values in the natural numbers.

## Examples

- **The integers.** [The integers form a Euclidean domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Int.html#Int.euclideanDomain)
  with size the absolute value: dividing $a$ by $b \neq 0$ leaves a remainder $r$
  with $0 \le r < |b|$. For instance $-7 = 2 \cdot (-4) + 1$.
- **Fields.** [Every field is a Euclidean domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Field.html#Field.toEuclideanDomain):
  division by a nonzero element is exact, so the remainder on division by any
  nonzero element is $0$.
- **Polynomials over a field.** For a field $K$,
  [the polynomial ring $K[X]$ is a Euclidean domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.instEuclideanDomain),
  with size the degree; this is polynomial long division.
- **Gaussian integers.** The ring $\mathbb{Z}[i]$ is Euclidean for the norm
  $N(a + bi) = a^2 + b^2$: given $\alpha$ and $\beta \neq 0$, round each coordinate of
  $\alpha / \beta \in \mathbb{Q}(i)$ to a nearest integer to get a quotient, and
  the remainder [has norm less than $N(\beta)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Zsqrtd/GaussianInt.html#GaussianInt.norm_mod_lt),
  in fact at most $N(\beta)/2$.
- **Discrete valuation rings.**
  [Every discrete valuation ring can be made a Euclidean domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/DiscreteValuationRing/Basic.html#IsDiscreteValuationRing.toEuclideanDomain),
  with size measured by the valuation.
- **Isomorphic copies.** [A commutative ring isomorphic to a Euclidean domain is again one](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#RingEquiv.euclideanDomain).

## Properties

- **Principal ideals.** [Every ideal of a Euclidean domain is principal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#EuclideanDomain.instIsPrincipalIdealRing),
  so a Euclidean domain is a [principal ideal domain](principal-ideal-domain.md).
  The zero ideal is $(0)$. If $I$ is a nonzero [ideal](../ideals-and-quotients/ideal-of-a-commutative-ring.md), well-foundedness gives a nonzero
  $m \in I$ that is minimal for $\prec$ among the nonzero elements of $I$. For
  $x \in I$ the remainder $x \bmod m = x - m(x/m)$ lies in $I$ and is smaller than
  $m$, so it is $0$; hence $m$ divides $x$ and $I = (m)$.
- **Unique factorization.** Since
  [every principal ideal domain is a unique factorization domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#PrincipalIdealRing.to_uniqueFactorizationMonoid),
  every Euclidean domain is a [unique factorization domain](unique-factorisation-domain.md).
- **Divisibility by remainders.** [The remainder of $a$ on division by $b$ is $0$ exactly when $b$ divides $a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.mod_eq_zero).
- **The Euclidean algorithm.** A [greatest common divisor](greatest-common-divisor.md) is
  computed by setting $\gcd(0, b) = b$ and, for $a \neq 0$,
  [$\gcd(a, b) = \gcd(b \bmod a,\ a)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_val); the recursion
  ends because the first argument decreases for $\prec$ (see
  [the article on the algorithm](../../../hundred-theorems/part-04/greatest-common-divisor-algorithm.md)). The result
  [divides both $a$ and $b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_dvd), and
  [every common divisor of $a$ and $b$ divides it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.dvd_gcd).
- **[Bézout's identity](../../../undergraduate/ring-theory/divisibility-in-integral-domains/bezouts-identity.md).** Keeping track of the quotients along the way, the extended
  Euclidean algorithm produces $s$ and $t$ with
  [$\gcd(a, b) = as + bt$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Basic.html#EuclideanDomain.gcd_eq_gcd_ab).
- **Irreducible elements.** If $x$ is [irreducible](irreducible-element.md), then for
  every $y$ [either $x$ divides $y$ or $x$ and $y$ are coprime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/EuclideanDomain.html#EuclideanDomain.dvd_or_coprime),
  in the sense that $ux + vy = 1$ for some $u$ and $v$ (see
  [coprime element](coprime-element.md)).

## Related concepts

Euclidean domains sit in a chain of classes of integral domains:

$$\text{fields} \subset \text{Euclidean domains} \subset \text{principal ideal domains} \subset \text{unique factorization domains}.$$

Each inclusion is strict. The integers are Euclidean but not a field. The ring
$\mathbb{Z}\big[\tfrac{1 + \sqrt{-19}}{2}\big]$ is a principal ideal domain that
admits no Euclidean function. The polynomial ring $\mathbb{Z}[X]$ has unique
factorization, but its ideal $(2, X)$ is not principal, so it is not Euclidean
either. Outside the chain altogether lies $\mathbb{Z}[\sqrt{-5}]$, which lacks
unique factorization: $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ are two
factorizations into irreducible elements, no two of which are associates (no
element has norm $2$ or $3$).

## In Mathlib

Mathlib treats a Euclidean domain as a commutative ring equipped with data: chosen
quotient and remainder operations and a well-founded relation, rather than the
mere existence of a Euclidean function. A ring can therefore carry several
Euclidean structures, and the structures Mathlib provides for the integers, fields
and polynomial rings are specific choices; for the integers the remainder on
division by a nonzero integer is always nonnegative. Division by zero gives $0$ and the remainder on division by $0$
is the element itself. The absence of zero divisors is not an axiom: Mathlib
derives from the axioms that a Euclidean domain is an integral domain. The greatest
common divisor and the extended Euclidean algorithm are defined as functions on the
ring, which needs a way to decide whether two elements are equal (in particular
whether an element is $0$); Mathlib takes this decidability as an extra assumption
on the ring, which is automatic in classical mathematics.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `EuclideanDomain`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/EuclideanDomain/Defs.html#EuclideanDomain)
- [Source of `EuclideanDomain` in Mathlib/Algebra/EuclideanDomain/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/EuclideanDomain/Defs.lean#L68)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L90)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L149)
