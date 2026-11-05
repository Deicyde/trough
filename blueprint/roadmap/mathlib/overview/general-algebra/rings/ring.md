---
article_id: af_7103ec351338d590278cb5bc
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Ring
mathlib_file: Mathlib/Algebra/Ring/Defs.lean
---

# Ring

A **ring** is a set with two binary operations, addition and multiplication,
such that the set is an abelian [group](../group-theory/part-01/group.md) under addition, the
multiplication is associative and has an identity element, and multiplication
distributes over addition. Rings capture the arithmetic shared by the
[integers](../numbers/integer.md), the integers modulo $n$, [polynomials](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
and square [matrices](../../linear-algebra/matrices/ring-valued-matrix.md): one can add, subtract and multiply, but
not necessarily divide. Commutative rings are the basic objects of commutative
algebra and algebraic number theory, and rings in general are the setting in
which divisibility, factorisation and congruences make sense.

## Definition

A [ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#Ring) is a set $R$ with operations $(a, b) \mapsto a + b$ and
$(a, b) \mapsto ab$ and elements $0, 1 \in R$ such that:

- $R$ is an abelian group under addition, with identity $0$; the additive
  inverse of $a$ is written $-a$, and $a - b$ means $a + (-b)$;
- multiplication is associative, $(ab)c = a(bc)$, and $1a = a = a1$ for all $a$;
- multiplication distributes over addition on both sides:
  [$a(b + c) = ab + ac$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#left_distrib) and
  [$(a + b)c = ac + bc$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#right_distrib).

Multiplication need not be commutative. A ring in which $ab = ba$ for all $a$
and $b$ is a [commutative ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#CommRing). The list of axioms is longer
than it needs to be: associativity of addition, a left additive identity, left
additive inverses, associativity of multiplication, a two-sided multiplicative
identity and the two distributive laws
[already determine a ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/MinimalAxioms.html#Ring.ofMinimalAxioms). Commutativity of
addition then follows by expanding $(1 + 1)(a + b)$ with each distributive law
in turn and comparing the two results.

A map between rings that preserves addition, multiplication and $1$ is a
[ring morphism](ring-morphism.md), and a subset containing $0$ and $1$ and closed
under addition, negation and multiplication is a [subring](subring.md).

## Examples

- The integers [form a commutative ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Int/Defs.html#Int.instCommRing) under the usual
  operations (see [the ring structure of the integers](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)).
  The [natural numbers](../numbers/natural-number.md) do not, since they lack additive inverses.
- For every natural number $n$, the integers modulo $n$
  [form a commutative ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/ZMod/Defs.html#ZMod.commRing); for $n = 0$ this is the ring of
  integers itself.
- The [rational](../../../undergraduate/ring-theory/field-theory/part-01/field-q-of-rational-numbers.md), [real](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md) and
  [complex](../../../undergraduate/ring-theory/field-theory/part-01/field-c-of-complex-numbers.md) numbers are commutative rings, and in fact
  [fields](../field-theory/field.md): every nonzero element has a multiplicative inverse.
- If $R$ is a ring, the polynomials in one indeterminate with coefficients in $R$
  [form a ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial.ring), which is
  [commutative when $R$ is](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial.commRing).
- For a positive integer $n$ and a ring $R$, the $n \times n$ matrices with
  entries in $R$ [form a ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Matrix/Mul.html#Matrix.instRing) under matrix addition and
  multiplication. For $n \ge 2$ and $R$ nonzero it is not commutative: with $E$
  the matrix whose only nonzero entry is a $1$ in the top left corner and $F$
  the one with a $1$ just to the right of it, $EF = F$ but $FE = 0$.
- The additive endomorphisms of an abelian group $A$, that is, the maps
  $f : A \to A$ with $f(x + y) = f(x) + f(y)$,
  [form a ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/End.html#AddMonoid.End.instRing) with pointwise addition and
  composition as multiplication.
- For any family of rings, the [product](../../../undergraduate/ring-theory/fundamentals/product-of-rings.md) of the family is a ring
  with [componentwise operations](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Pi.html#Pi.ring). In particular the functions from
  any set to a ring form a ring.
- The quaternions over the real numbers
  [form a division ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Quaternion.html#Quaternion.instDivisionRing): every nonzero
  element is invertible, yet multiplication is not commutative.
- A set with one element is a ring, the zero ring, in which $0 = 1$.

## Basic properties

Multiplying by zero gives zero: $0a = 0 = a0$, since $0a = (0 + 0)a = 0a + 0a$.
Signs behave as in the integers:
[$(-a)b = -(ab)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#neg_mul), [$(-a)(-b) = ab$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#neg_mul_neg) and
[$(-1)a = -a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#neg_one_mul). Multiplication also distributes over
subtraction, for instance [$a(b - c) = ab - ac$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#mul_sub_left_distrib).

The zero ring is the only ring in which $0$ and $1$ coincide:
[$0 = 1$ holds exactly when $R$ has at most one element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Basic.html#subsingleton_iff_zero_eq_one).

The elements of a ring that have a two-sided multiplicative inverse are its
units, and they [form a group under multiplication](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Units/Defs.html#Units.instGroup); for
matrices over a field this is the
[general linear group](../../../undergraduate/group-theory/classical-automorphism-groups/general-linear-group.md).

For any ring $R$ there is
[a ring morphism from the integers to $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/Cast/Lemmas.html#Int.castRingHom), sending a
natural number $n$ to the sum of $n$ copies of $1$ and $-n$ to the negative of
that sum, and
[it is the only ring morphism from the integers to $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Int/Cast/Lemmas.html#RingHom.eq_intCast').
The [characteristic](../field-theory/characteristic-of-a-ring.md) of $R$ is the nonnegative generator of the
kernel of this morphism.

In a commutative ring the binomial theorem holds:
[for all $x$, $y$ and every natural number $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Sum.html#add_pow),

$$(x + y)^n = \sum_{m=0}^{n} \binom{n}{m} x^m y^{n-m}.$$

The same formula holds in any ring
[whenever $xy = yx$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Choose/Sum.html#Commute.add_pow); without that hypothesis it can fail
already for $n = 2$, where $(x + y)^2 = x^2 + xy + yx + y^2$.

## Related concepts

The structure of a commutative ring is studied through its
[ideals](../ideals-and-quotients/ideal-of-a-commutative-ring.md), which are the kernels of ring morphisms and give rise to
[quotient rings](../ideals-and-quotients/quotient-ring.md). [Prime](../ideals-and-quotients/prime-ideal.md) and
[maximal](../ideals-and-quotients/maximal-ideal.md) ideals are those whose quotients are integral
domains and fields respectively. An integral domain is a nontrivial commutative
ring in which a product of nonzero elements is nonzero. Mathlib's notion of a
[domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#IsDomain), stated more generally for semirings, is a nontrivial
ring in which nonzero elements can be cancelled from either side of an equation; for rings this is equivalent to
having no zero divisors, and it does not require commutativity. Special classes of rings include
[Euclidean domains](../divisibility-in-integral-domains/euclidean-domain.md),
[unique factorisation domains](../divisibility-in-integral-domains/unique-factorisation-domain.md),
[Noetherian rings](noetherian-ring.md) and
[local rings](local-ring.md).

Dropping additive inverses gives a semiring, such as the natural numbers;
dropping the multiplicative identity or associativity gives non-unital or
non-associative rings. An abelian group with a scalar multiplication by a ring
that is associative, unital and distributive over both additions is a
[module](../../linear-algebra/fundamentals/module.md), and a ring that is also a module
over a commutative ring, compatibly, is an
[algebra](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md). Rings and ring morphisms form
[the category of rings](the-category-of-rings.md).

## In Mathlib

In Mathlib a ring is a structure placed on a type, and is always associative
and has a multiplicative identity; commutativity is a separate, stronger
structure, and the variants without identity or without associativity are
declared alongside. A ring is built as a semiring whose addition forms an
abelian group, so facts proved for semirings apply to rings without change.
Mathlib's semiring axioms include $0a = 0$ and $a0 = 0$, which are redundant for
rings, and the structure also carries subtraction, integer and natural-number
multiples, powers and the map from the integers, each with a default definition
that a particular ring may replace by a better-behaved one. The zero ring is a
ring: when an argument needs $0 \ne 1$, nontriviality is assumed separately.
Many basic identities, such as the sign rules and the binomial theorem for
commuting elements, are stated for weaker structures than rings and apply to
rings as a special case.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../group-theory/part-01/group.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Ring`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html#Ring)
- [Source of `Ring` in Mathlib/Algebra/Ring/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Ring/Defs.lean#L144)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L65)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L126)
