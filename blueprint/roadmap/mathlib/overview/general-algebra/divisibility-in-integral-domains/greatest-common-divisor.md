# Greatest common divisor

The **greatest common divisor** of two elements $a$ and $b$ is a common divisor
of $a$ and $b$ that every other common divisor divides. For
[integers](../numbers/integer.md) not both zero, the largest integer dividing both is a
greatest common divisor, so that $\gcd(12, 18) = 6$. It governs when fractions can be reduced, when linear
equations $ax + by = c$ have integer solutions, and when two elements share no
common factor. The same notion makes sense in any commutative
[ring](../rings/ring.md), and in an integral domain a greatest common divisor, when it
exists, is determined up to multiplication by a unit.

## Definition

Let $R$ be an integral domain, or more generally a cancellative commutative
monoid with zero (one in which $ab = ac$ with $a \ne 0$ implies $b = c$).
An element $d$ of $R$ is a greatest common divisor of $a$ and $b$ if

- $d$ divides $a$ and $d$ divides $b$, and
- every $c$ that divides both $a$ and $b$ also divides $d$.

"Greatest" refers to divisibility, not to size. If $d$ and $d'$ are both greatest
common divisors of $a$ and $b$, each divides the other, so they are associated:
$d' = ud$ for a unit $u$. Conversely every associate of a greatest common divisor
is again one. The greatest common divisor is therefore determined only up to a
unit, and a choice of normal form singles out one representative: the nonnegative
one in $\mathbb{Z}$, the monic one (or $0$) in a polynomial ring over a field. A
domain in which every pair of elements has a greatest common divisor is called a
GCD domain, and in Mathlib the
[greatest common divisor operation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#GCDMonoid.gcd) is a choice of such an
element for each pair.

In $\mathbb{Z}$ the two descriptions agree. For $a$ and $b$ not both zero, the
largest common divisor is positive and is divisible by every common divisor; and
$\gcd(0, 0) = 0$, since every integer divides $0$.

## Examples

- $\gcd(12, 18) = 6$ and $\gcd(-4, 6) = 2$; the sign of the arguments plays no role.
- $\gcd(a, 0)$ is $a$ up to a unit, and $\gcd(a, 1)$ is a unit, normalized to $1$.
- Over $\mathbb{Q}$, since $x^2 - 1 = (x - 1)(x + 1)$ and
  $x^2 - 3x + 2 = (x - 1)(x - 2)$, the monic greatest common divisor of these two
  polynomials is $x - 1$.
- In $\mathbb{Z}[\sqrt{-5}]$ the elements $6$ and $2 + 2\sqrt{-5}$ have no
  greatest common divisor. Both $2$ and $1 + \sqrt{-5}$ divide each of them, so a
  greatest common divisor $d$ would have norm divisible by $4$ and by $6$, while
  dividing $6$ and $2 + 2\sqrt{-5}$ forces its norm to divide $36$ and $24$. The
  norm would be $12$, but $x^2 + 5y^2 = 12$ has no integer solutions.

## Properties

Fix a domain in which greatest common divisors exist, with a chosen one for each
pair.

- [An element divides $\gcd(a, b)$ if and only if it divides both $a$ and $b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#dvd_gcd_iff).
- [$\gcd(a, b) = 0$ if and only if $a = b = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_eq_zero_iff).
- With normalized values, $\gcd$ is [commutative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_comm) and
  [associative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_assoc), [$\gcd(a, 0)$ is the normal form of $a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_zero_right),
  and [$\gcd(a, 1) = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_one_right). Without normalization the same
  statements hold up to associates, for instance
  [$\gcd(a, b)$ is associated with $\gcd(b, a)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_comm').
- [$\gcd(ca, cb)$ is associated with $c \gcd(a, b)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_mul_left').
- [$\gcd(a, b)$ times the least common multiple of $a$ and $b$ is associated with $ab$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#GCDMonoid.gcd_mul_lcm)
  (see [least common multiple](least-common-multiple.md)).
- [$\gcd(a, b)$ is a unit if and only if every common divisor of $a$ and $b$ is a unit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_isUnit_iff_isRelPrime).
- In a commutative ring with normalized greatest common divisors,
  [if $a$ divides $b - c$ then $\gcd(a, b) = \gcd(a, c)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#gcd_eq_of_dvd_sub_right).
  Taking $c$ to be the remainder of $b$ on division by $a$ gives the step of the
  [Euclidean algorithm](../../../hundred-theorems/part-03/greatest-common-divisor-algorithm.md): for example
  $\gcd(252, 198) = \gcd(198, 54) = \gcd(54, 36) = \gcd(36, 18) = 18$.

## Bézout's identity

In a [principal ideal domain](principal-ideal-domain.md) the greatest common
divisor is a linear combination of the two elements:
[there are $x$ and $y$ with $\gcd(a, b) = ax + by$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#exists_gcd_eq_mul_add_mul).
This is [Bézout's identity](../../../undergraduate/ring-theory/divisibility-in-integral-domains/bezouts-identity.md). In ideal-theoretic
terms, [the ideal generated by $a$ and $b$ is the principal ideal generated by $\gcd(a, b)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#span_gcd). Consequently, in such a domain,
[$\gcd(a, b)$ is a unit if and only if $ax + by = 1$ for some $x$ and $y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PrincipalIdealDomain.html#gcd_isUnit_iff),
that is, if and only if $a$ and $b$ are [coprime](coprime-element.md); for integers,
[$a$ and $b$ are coprime exactly when $\gcd(a, b) = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Coprime/Lemmas.html#Int.isCoprime_iff_gcd_eq_one).
Running the Euclidean algorithm backwards produces the coefficients: from the
example above, $18 = 4 \cdot 252 - 5 \cdot 198$. The
[extended Euclidean algorithm](euclids-algorithm.md) does this systematically: given
natural numbers $a$ and $b$,
[the integers $x$ and $y$ it returns satisfy $\gcd(a, b) = ax + by$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Nat.gcd_eq_gcd_ab),
and [the same holds for integers $a$ and $b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/GCD.html#Int.gcd_eq_gcd_ab), with the
algorithm run on their absolute values and the signs adjusted.
Both statements need more than the existence of greatest common divisors: in the
polynomial ring $\mathbb{Z}[x]$, where they exist, $\gcd(2, x) = 1$ but $1$ is not
of the form $2f + xg$.

## Existence

In a [unique factorization domain](unique-factorisation-domain.md) two nonzero
elements have as a greatest common divisor the product of the common prime
factors, each raised to the smaller of its two exponents, and
[every unique factorization domain carries a greatest common divisor operation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/UniqueFactorizationDomain/GCDMonoid.html#UniqueFactorizationMonoid.toGCDMonoid).
This covers $\mathbb{Z}$, polynomial rings over a field, and every principal ideal
domain. Moreover, [the polynomial ring over a GCD domain is again a GCD domain](../polynomials-and-power-series/a-x-has-gcd-and-lcm-if-a-does.md). The example of
$\mathbb{Z}[\sqrt{-5}]$ shows that existence can fail in an integral domain.

## In Mathlib

Mathlib packages the greatest common divisor as a structure on a cancellative
commutative monoid with zero. The structure supplies two operations, the
greatest common divisor and the least common multiple, together with the
axioms that the first divides both arguments, that every common divisor divides
it, that their product is associated with the product of the arguments, and
that the least common multiple with $0$ is $0$. Because the value is fixed only
up to units, general results are stated up to associates; a normalized variant,
which requires every value to be in normal form, gives exact equalities such as
commutativity. For the integers the value
[is nonnegative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Nat.html#Int.gcd_nonneg) and
[agrees with the greatest common divisor of their absolute values, computed in the natural numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Nat.html#Int.coe_gcd);
for polynomials over a field, [the normal form of a nonzero polynomial is monic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.monic_normalize). Euclidean domains also carry a separate,
computable greatest common divisor defined by the Euclidean algorithm, which is
not normalized.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `GCDMonoid.gcd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GCDMonoid/Basic.html#GCDMonoid.gcd)
- [Source of `GCDMonoid.gcd` in Mathlib/Algebra/GCDMonoid/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/GCDMonoid/Basic.lean#L319)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L87)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L145)
