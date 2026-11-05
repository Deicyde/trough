---
article_id: af_640fc2315f148082203c1440
concept: Field
---

A **field** is a set with an addition and a multiplication in which the usual
rules of arithmetic hold and division by any nonzero element is possible. The
rational, real and complex numbers are the familiar examples. Fields are where
linear algebra takes place, since a [vector space](trough:Module) is a module over a field,
and they are the setting for the theory of polynomial equations, from
[splitting fields](trough:Polynomial.SplittingField) to the [Galois
correspondence](trough:IsGalois.intermediateFieldEquivSubgroup).

## Definition

A [field](lean:Field) is a commutative [ring](trough:Ring) $K$ with identity in which
$1 \neq 0$ and every nonzero element $a$ has a multiplicative inverse, an element
$a^{-1}$ with

$$a\,a^{-1} = a^{-1}a = 1.$$

The condition $1 \neq 0$ excludes the zero ring, in which every nonzero element
trivially has an inverse because there are none. Spelled out, $K$ is an abelian group under addition with identity $0$; the
nonzero elements form an abelian group under multiplication with identity $1$;
and multiplication distributes over addition. The inverse of a nonzero element is
unique, and division is defined by $a / b = a\,b^{-1}$ for $b \neq 0$.

## Examples

- [The rational numbers $\mathbb{Q}$ form a field](lean:Rat.instField), and so do
  [the real numbers $\mathbb{R}$](lean:Real.instField) and
  [the complex numbers $\mathbb{C}$](lean:Complex.instField) (see
  [rational number](trough:Rat), [real number](trough:Real) and
  [complex number](trough:Complex)).
- The [integers](trough:Int) do not form a field: $2$ has no integer inverse.
- For a prime $p$, the integers modulo $p$ form a field with $p$ elements. For a
  composite modulus they do not: modulo $6$, the product $2 \cdot 3$ is $0$, which
  cannot happen in a field. More generally, for a commutative ring $R$ and an
  ideal $I$, the [quotient ring](trough:Ideal.Quotient.ring) $R/I$
  [is a field exactly when $I$ is a maximal ideal](lean:Ideal.Quotient.maximal_ideal_iff_isField_quotient)
  (see [maximal ideal](trough:Ideal.IsMaximal)).
- Every integral domain [embeds in](lean:IsFractionRing.injective) its [field of fractions](trough:IsFractionRing),
  as $\mathbb{Z}$ embeds in $\mathbb{Q}$. Applied to the polynomial ring $K[X]$, this
  gives the field $K(X)$ of [rational functions](trough:RatFunc) in one variable.
- [Finite fields](trough:Mathlib.FieldTheory.Finite.Basic) exist beyond the integers
  modulo a prime: for example, adjoining a root of $X^2 + X + 1$ to the field with two
  elements gives a field with four elements.

## Properties

- **No zero divisors.** If $ab = 0$ and $a \neq 0$, multiplying by $a^{-1}$ gives
  $b = 0$. So [every field is an integral domain](lean:IsField.isDomain).
- **Ideals.** If an ideal contains a nonzero element $a$, it contains
  $a^{-1}a = 1$ and hence everything. So
  [the only ideals of a field are $\{0\}$ and the field itself](lean:Ideal.eq_bot_or_top).
- **Homomorphisms.** The kernel of a ring homomorphism from a field to a nonzero
  ring is an ideal not containing $1$, hence zero, so
  [every ring homomorphism from a field to a nonzero ring is injective](lean:RingHom.injective).
  A homomorphism of fields therefore identifies its source with a
  [subfield](trough:Subfield) of its target.
- **Characteristic.** If $n \cdot 1 = 0$ for some positive integer $n$, the least such
  $n$ is not $1$, since $1 \neq 0$, and it cannot factor as $n = rs$ with
  $1 < r, s < n$: by minimality $r \cdot 1$ and $s \cdot 1$ are nonzero, yet their
  product is $n \cdot 1 = 0$, which cannot happen in an integral domain. So the
  [characteristic](trough:ringChar) of a field
  [is either $0$ or a prime number](lean:CharP.char_is_prime_or_zero) (see
  [characteristic zero](trough:CharZero) and [characteristic $p$](trough:CharP)).
- **Size of finite fields.** A finite field of characteristic $p$ is a vector space
  of some finite dimension $n \geq 1$ over its subfield with $p$ elements, so
  [it has exactly $p^n$ elements, with $p$ prime](lean:FiniteField.card).
- **Polynomials.** A nonzero [polynomial](trough:Polynomial) of degree $n$ over a
  field [has at most $n$ roots, counted with multiplicity](lean:Polynomial.card_roots')
  (see [roots of a polynomial](trough:Polynomial.roots)). A field in which every
  nonconstant polynomial has a root is [algebraically closed](trough:IsAlgClosed),
  and every field has an [algebraic closure](trough:AlgebraicClosure), an algebraic
  extension that [is algebraically closed](lean:AlgebraicClosure.isAlgClosed).
- **Finite integral domains.** In a finite integral domain, multiplication by a
  nonzero element is injective, hence surjective, so some element is its inverse:
  [every finite commutative integral domain is a field](lean:Finite.isField_of_domain).

## Generalizations

Dropping commutativity of multiplication gives a division ring, also called a skew
field; the quaternions are the standard example of one that is not a field. No
finite example exists:
[Wedderburn's little theorem](trough:littleWedderburn) says that
[every finite division ring is a field](lean:littleWedderburn). Dropping additive
inverses instead gives a semifield, such as the nonnegative rational numbers.

## In Mathlib

Mathlib defines a field as a commutative ring that is also a division ring, and the
condition $1 \neq 0$ is part of the definition. Inversion is a function on all of
$K$, so it must take a value at $0$: by convention
[the inverse of $0$ is $0$](lean:inv_zero), and consequently
[$a / 0 = 0$ for every $a$](lean:div_zero). The usual identity
[$a\,a^{-1} = 1$ holds for every $a \neq 0$](lean:mul_inv_cancel₀). This convention
makes division total without changing any statement about nonzero denominators. A
field structure also carries a chosen map from the rationals into the field, which
lets Mathlib control how $\mathbb{Q}$ acts on it. Because these are data, Mathlib
also has [a property of a ring saying that it is a field](lean:IsField), which
makes no choice of inverse;
[every field has this property](lean:Field.toIsField), and
[a ring with it can be given a field structure](lean:IsField.toField). Several of the
facts above are proved in greater generality: the statement about ideals for every
division semiring, the injectivity of homomorphisms for every simple ring, the embedding of a ring
in its ring of fractions for every commutative ring, the
dichotomy for the characteristic for every nonzero ring without zero divisors, and
the bound on roots for every integral domain.

## Depends on

- [Group](trough:Group)
- [Ring](trough:Ring)
