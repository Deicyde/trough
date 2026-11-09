# Field

A **field** is a set with an addition and a multiplication in which the usual
rules of arithmetic hold and division by any nonzero element is possible. The
rational, real and complex numbers are the familiar examples. Fields are where
linear algebra takes place, since a [vector space](../../linear-algebra/fundamentals/module.md) is a module over a field,
and they are the setting for the theory of polynomial equations, from
[splitting fields](splitting-field.md) to the [Galois correspondence](galois-correspondence.md).

## Definition

A [field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html#Field) is a commutative [ring](../rings/ring.md) $K$ with identity in which
$1 \neq 0$ and every nonzero element $a$ has a multiplicative inverse, an element
$a^{-1}$ with

$$a\,a^{-1} = a^{-1}a = 1.$$

The condition $1 \neq 0$ excludes the zero ring, in which every nonzero element
trivially has an inverse because there are none. Spelled out, $K$ is an abelian group under addition with identity $0$; the
nonzero elements form an abelian group under multiplication with identity $1$;
and multiplication distributes over addition. The inverse of a nonzero element is
unique, and division is defined by $a / b = a\,b^{-1}$ for $b \neq 0$.

## Examples

- [The rational numbers $\mathbb{Q}$ form a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Rat.html#Rat.instField), and so do
  [the real numbers $\mathbb{R}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.instField) and
  [the complex numbers $\mathbb{C}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.instField) (see
  [rational number](../numbers/rational-number.md), [real number](../numbers/real-number.md) and
  [complex number](../numbers/complex-number.md)).
- The [integers](../numbers/integer.md) do not form a field: $2$ has no integer inverse.
- For a prime $p$, the integers modulo $p$ form a field with $p$ elements. For a
  composite modulus they do not: modulo $6$, the product $2 \cdot 3$ is $0$, which
  cannot happen in a field. More generally, for a commutative ring $R$ and an
  ideal $I$, the [quotient ring](../ideals-and-quotients/quotient-ring.md) $R/I$
  [is a field exactly when $I$ is a maximal ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Basic.html#Ideal.Quotient.maximal_ideal_iff_isField_quotient)
  (see [maximal ideal](../ideals-and-quotients/maximal-ideal.md)).
- Every integral domain [embeds in](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/FractionRing.html#IsFractionRing.injective) its [field of fractions](field-of-fractions-of-an-integral-domain.md),
  as $\mathbb{Z}$ embeds in $\mathbb{Q}$. Applied to the polynomial ring $K[X]$, this
  gives the field $K(X)$ of [rational functions](../../../undergraduate/ring-theory/field-theory/rational-fraction-fields-with-one-indeterminate.md) in one variable.
- [Finite fields](../../../undergraduate/ring-theory/field-theory/finite-fields.md) exist beyond the integers
  modulo a prime: for example, adjoining a root of $X^2 + X + 1$ to the field with two
  elements gives a field with four elements.

## Properties

- **No zero divisors.** If $ab = 0$ and $a \neq 0$, multiplying by $a^{-1}$ gives
  $b = 0$. So [every field is an integral domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/IsField.html#IsField.isDomain).
- **Ideals.** If an ideal contains a nonzero element $a$, it contains
  $a^{-1}a = 1$ and hence everything. So
  [the only ideals of a field are $\{0\}$ and the field itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Lattice.html#Ideal.eq_bot_or_top).
- **Homomorphisms.** The kernel of a ring homomorphism from a field to a nonzero
  ring is an ideal not containing $1$, hence zero, so
  [every ring homomorphism from a field to a nonzero ring is injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/SimpleRing/Basic.html#RingHom.injective).
  A homomorphism of fields therefore identifies its source with a
  [subfield](subfield.md) of its target.
- **Characteristic.** If $n \cdot 1 = 0$ for some positive integer $n$, the least such
  $n$ is not $1$, since $1 \neq 0$, and it cannot factor as $n = rs$ with
  $1 < r, s < n$: by minimality $r \cdot 1$ and $s \cdot 1$ are nonzero, yet their
  product is $n \cdot 1 = 0$, which cannot happen in an integral domain. So the
  [characteristic](characteristic-of-a-ring.md) of a field
  [is either $0$ or a prime number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html#CharP.char_is_prime_or_zero) (see
  [characteristic zero](characteristic-zero.md) and [characteristic $p$](characteristic-p.md)).
- **Size of finite fields.** A finite field of characteristic $p$ is a vector space
  of some finite dimension $n \geq 1$ over its subfield with $p$ elements, so
  [it has exactly $p^n$ elements, with $p$ prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.card).
- **Polynomials.** A nonzero [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) of degree $n$ over a
  field [has at most $n$ roots, counted with multiplicity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.card_roots')
  (see [roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)). A field in which every
  nonconstant polynomial has a root is [algebraically closed](algebraically-closed-field.md),
  and every field has an [algebraic closure](existence-of-algebraic-closure-of-a-field.md), an algebraic
  extension that [is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure.isAlgClosed).
- **Finite integral domains.** In a finite integral domain, multiplication by a
  nonzero element is injective, hence surjective, so some element is its inverse:
  [every finite commutative integral domain is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/IntegralDomain.html#Finite.isField_of_domain).

## Generalizations

Dropping commutativity of multiplication gives a division ring, also called a skew
field; the quaternions are the standard example of one that is not a field. No
finite example exists:
[Wedderburn's little theorem](../../../thousand-plus/algebra/13-commutative-algebra/wedderburns-little-theorem.md) says that
[every finite division ring is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/LittleWedderburn.html#littleWedderburn). Dropping additive
inverses instead gives a semifield, such as the nonnegative rational numbers.

## In Mathlib

Mathlib defines a field as a commutative ring that is also a division ring, and the
condition $1 \neq 0$ is part of the definition. Inversion is a function on all of
$K$, so it must take a value at $0$: by convention
[the inverse of $0$ is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Defs.html#inv_zero), and consequently
[$a / 0 = 0$ for every $a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Basic.html#div_zero). The usual identity
[$a\,a^{-1} = 1$ holds for every $a \neq 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Defs.html#mul_inv_cancel%E2%82%80). This convention
makes division total without changing any statement about nonzero denominators. A
field structure also carries a chosen map from the rationals into the field, which
lets Mathlib control how $\mathbb{Q}$ acts on it. Because these are data, Mathlib
also has [a property of a ring saying that it is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/IsField.html#IsField), which
makes no choice of inverse;
[every field has this property](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/IsField.html#Field.toIsField), and
[a ring with it can be given a field structure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/IsField.html#IsField.toField). Several of the
facts above are proved in greater generality: the statement about ideals for every
division semiring, the injectivity of homomorphisms for every simple ring, the embedding of a ring
in its ring of fractions for every commutative ring, the
dichotomy for the characteristic for every nonzero ring without zero divisors, and
the bound on roots for every integral domain.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../group-theory/part-01/group.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `Field`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Defs.html#Field)
- [Source of `Field` in Mathlib/Algebra/Field/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Algebra/Field/Defs.lean#L170)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L120)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L171)
