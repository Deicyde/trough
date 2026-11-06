# Ordered ring

An **ordered ring** is a [ring](ring.md) equipped with an order that is compatible with its
addition and multiplication: adding the same element to both sides of an inequality preserves it,
and so does multiplying both sides by a nonnegative element. The [integers](../numbers/integer.md), the
[rational numbers](../numbers/rational-number.md) and the [real numbers](../numbers/real-number.md) are the basic examples. The
notion isolates the algebraic rules used whenever one manipulates inequalities, so that facts such
as "a product of two nonpositive elements is nonnegative" can be proved once for every ring that
obeys those rules, and facts such as "squares are nonnegative" or Bernoulli's inequality once for
every linearly ordered ring.

## Definition

Let $R$ be a ring (associative, with identity, not necessarily commutative) and let $\le$ be a
partial order on $R$. Then $R$ is an [ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsOrderedRing) if, for all
$a, b, c \in R$:

1. if $a \le b$, then $a + c \le b + c$;
2. $0 \le 1$;
3. if $a \le b$ and $0 \le c$, then $ca \le cb$ and $ac \le bc$.

Condition 3 with $a = 0$ says that the nonnegative elements are closed under multiplication.
Given conditions 1 and 2, this closure is also sufficient: if $0 \le c$ and $a \le b$, then
$0 \le b - a$ by condition 1, so $cb - ca = c(b - a)$ and $bc - ac = (b - a)c$ are products of nonnegative elements, hence
nonnegative, and adding $ca$ (respectively $ac$) to both sides by condition 1 gives $ca \le cb$
and $ac \le bc$. So [it is enough to check that $0 \le x$ and $0 \le y$ imply $0 \le xy$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsOrderedRing.of_mul_nonneg).

The ring is **linearly ordered** when any two elements are comparable. In that case condition 2
follows from the others: if $1 < 0$, then $0 < -1$ by condition 1, and condition 3 with $c = -1$
gives $0 \le (-1)(-1) = 1$, a contradiction. For a merely partial order it is a genuine
requirement: the order in which $a \le b$ only when $a = b$ satisfies conditions 1 and 3 on every
ring.

A [strictly ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsStrictOrderedRing) is a nontrivial ring with a partial order
satisfying conditions 1 and 2 in which multiplication on either side by a positive element is
strictly increasing: $a < b$ and $0 < c$ imply $ca < cb$ and $ac < bc$.
[Every strictly ordered ring is an ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsStrictOrderedRing.toIsOrderedRing).
Conventions in the literature vary: many texts reserve "ordered ring" for the linearly ordered
case, and some build strictness into the definition.

## Examples

- With their usual orders, [the integers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Int.html#Int.instIsStrictOrderedRing),
  [the rational numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Rat.html#Rat.instIsStrictOrderedRing) and
  [the real numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.instIsStrictOrderedRing) are strictly ordered rings, and their
  usual orders are linear (see [order on the real numbers](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)). The
  [natural numbers](../numbers/natural-number.md) form only a semiring, but
  [they satisfy the axioms of a strictly ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Nat.html#Nat.instIsStrictOrderedRing), which Mathlib states for semirings.
- A [subring](subring.md) of an ordered ring, with the restricted order, is again an ordered ring.
- The [polynomial ring](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) $\mathbb{Z}[x]$, with a nonzero polynomial declared
  positive when its leading coefficient is positive, is linearly and strictly ordered. Here $x - n$
  is positive for every integer $n$, so $x$ is larger than every integer.
- [A product of ordered rings, ordered coordinatewise, is an ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Pi.html#Pi.isOrderedRing).
  In $\mathbb{R}^2$ the elements $(1, 0)$ and $(0, 1)$ are incomparable, so the order is not
  linear; both are positive but their product is $0$, so the ring is not strictly ordered.
- In $\mathbb{Z}[\varepsilon]$ with $\varepsilon^2 = 0$, order $a + b\varepsilon$ by the sign of $a$,
  and by the sign of $b$ when $a = 0$. This is a linearly ordered ring that is not strictly
  ordered, since $\varepsilon > 0$ but $\varepsilon^2 = 0$.
- On the [complex numbers](../numbers/complex-number.md), declare $z \le w$ when $w - z$ is a nonnegative real
  number. [With this partial order the complex numbers form a strictly ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/RCLike/Basic.html#RCLike.toIsStrictOrderedRing). No total order does this, because squares would be
  nonnegative, giving both $0 \le 1$ and $0 \le i^2 = -1$, and adding $1$ to the second inequality
  forces $1 \le 0$, so $1 = 0$.

## Properties

Let $R$ be an ordered ring.

- [The product of two nonnegative elements is nonnegative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/GroupWithZero/Basic.html#Left.mul_nonneg), and
  [the product of two nonpositive elements is nonnegative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Unbundled/Basic.html#mul_nonneg_of_nonpos_of_nonpos).
- [The nonnegative elements form a subsemiring $P$ with $P \cap (-P) = \{0\}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Cone.html#Subsemiring.IsPointed.nonneg). Conversely,
  [if $P$ is a subsemiring of a ring with $P \cap (-P) = \{0\}$, declaring $a \le b$ when $b - a \in P$ makes the ring an ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Cone.html#IsOrderedRing.ofSubsemiring). The order is
  linear exactly when $P \cup (-P)$ is the whole ring.
- If $R$ is nontrivial, then $0 < 1$, so the multiples $n \cdot 1$ strictly increase with $n$ and
  [$R$ has characteristic zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsOrderedRing.toCharZero) (see
  [characteristic zero](../field-theory/characteristic-zero.md)). In particular no nonzero ring of positive
  characteristic, such as a finite [field](../field-theory/field.md), carries an ordered ring structure.
- If $R$ is linearly ordered, then [every square is nonnegative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Unbundled/Basic.html#sq_nonneg), and
  [the absolute value is multiplicative, $|ab| = |a|\,|b|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Abs.html#abs_mul).
- If $R$ is linearly and strictly ordered, then
  [$R$ is a domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsStrictOrderedRing.isDomain), that is, nontrivial with no zero
  divisors. In the other direction, for any partial order,
  [a nontrivial ordered ring without zero divisors is strictly ordered](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsOrderedRing.toIsStrictOrderedRing).
- If $R$ is strictly ordered, [the product of two negative elements is positive](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Unbundled/Basic.html#mul_pos_of_neg_of_neg).
- **Bernoulli's inequality.** If $R$ is linearly ordered, $2 + a \ge 0$ (that is, $a \ge -2$)
  and $n$ is a natural number, then
  [$(1 + a)^n \ge 1 + na$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Pow.html#one_add_le_pow_of_two_add_nonneg).

## Related concepts

An ordered [field](../field-theory/field.md) is an ordered ring that is a field; the rationals and the reals
are the standard examples. The polynomial example above shows that an ordered ring need not be
[Archimedean](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Defs.html#Archimedean), meaning that for every element $a$ and every positive $b$ some
multiple $nb$ with $n$ a natural number satisfies $a \le nb$: taking $b = 1$, the indeterminate
$x$ of $\mathbb{Z}[x]$ exceeds every integer. The additive group of an ordered ring, with the same
order, is an ordered abelian group: an abelian group with a partial order satisfying condition 1.

## In Mathlib

Mathlib separates the three ingredients: the algebraic structure, the order, and a property that
records how they interact. The ordered ring property is stated for semirings, so it covers the
natural numbers as well as rings, and it requires monotonicity of multiplication on both sides
because commutativity is not assumed. The axiom $0 \le 1$ is part of the definition; one
consequence is that reversing the order of an ordered ring does not in general give an ordered
ring. Linearly ordered rings are obtained by combining the property with a linear order, and
strictly ordered rings form a separate, stronger property. Many lemmas about linearly ordered
rings additionally assume the strict property. Many lemmas, including the statements
about squares, domains, nonpositive products, negative products and Bernoulli's inequality above, are proved for semirings in which $a \le b$
implies $b = a + c$ for some $c$; every ring meets this condition with $c = b - a$. The order on
the complex numbers described above is not imposed by default and is available only when
explicitly requested; Mathlib states the strictly ordered ring result for both the real and the
complex numbers at once.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](ring.md)

## Sources

- [Mathlib documentation: `IsOrderedRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsOrderedRing)
- [Source of `IsOrderedRing` in Mathlib/Algebra/Order/Ring/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Order/Ring/Defs.lean#L62)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L72)
