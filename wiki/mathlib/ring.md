A **ring** is a set with two binary operations, addition and multiplication,
such that the set is an abelian [group](trough:Group) under addition, the
multiplication is associative and has an identity element, and multiplication
distributes over addition. Rings capture the arithmetic shared by the
[integers](trough:Int), the integers modulo $n$, [polynomials](trough:Polynomial)
and square [matrices](trough:Matrix): one can add, subtract and multiply, but
not necessarily divide. Commutative rings are the basic objects of commutative
algebra and algebraic number theory, and rings in general are the setting in
which divisibility, factorisation and congruences make sense.

## Definition

A ring is a set $R$ with operations $(a, b) \mapsto a + b$ and
$(a, b) \mapsto ab$ and elements $0, 1 \in R$ such that:

- $R$ is an abelian group under addition, with identity $0$; the additive
  inverse of $a$ is written $-a$, and $a - b$ means $a + (-b)$;
- multiplication is associative, $(ab)c = a(bc)$, and $1a = a = a1$ for all $a$;
- multiplication distributes over addition on both sides:
  $a(b + c) = ab + ac$ and
  $(a + b)c = ac + bc$.

Multiplication need not be commutative. A ring in which $ab = ba$ for all $a$
and $b$ is a commutative ring. The list of axioms is longer
than it needs to be: associativity of addition, a left additive identity, left
additive inverses, associativity of multiplication, a two-sided multiplicative
identity and the two distributive laws
already determine a ring. Commutativity of
addition then follows by expanding $(1 + 1)(a + b)$ with each distributive law
in turn and comparing the two results.

A map between rings that preserves addition, multiplication and $1$ is a
[ring morphism](trough:RingHom), and a subset containing $0$ and $1$ and closed
under addition, negation and multiplication is a [subring](trough:Subring).

## Examples

- The integers form a commutative ring under the usual
  operations (see [the ring structure of the integers](trough:Int.instCommRing)).
  The [natural numbers](trough:Nat) do not, since they lack additive inverses.
- For every natural number $n$, the integers modulo $n$
  form a commutative ring; for $n = 0$ this is the ring of
  integers itself.
- The [rational](trough:Rat.instField), [real](trough:Real.instField) and
  [complex](trough:Complex.instField) numbers are commutative rings, and in fact
  [fields](trough:Field): every nonzero element has a multiplicative inverse.
- If $R$ is a ring, the polynomials in one indeterminate with coefficients in $R$
  form a ring, which is
  commutative when $R$ is.
- For a positive integer $n$ and a ring $R$, the $n \times n$ matrices with
  entries in $R$ form a ring under matrix addition and
  multiplication. For $n \ge 2$ and $R$ nonzero it is not commutative: with $E$
  the matrix whose only nonzero entry is a $1$ in the top left corner and $F$
  the one with a $1$ just to the right of it, $EF = F$ but $FE = 0$.
- The additive endomorphisms of an abelian group $A$, that is, the maps
  $f : A \to A$ with $f(x + y) = f(x) + f(y)$,
  form a ring with pointwise addition and
  composition as multiplication.
- For any family of rings, the [product](trough:Pi.ring) of the family is a ring
  with componentwise operations. In particular the functions from
  any set to a ring form a ring.
- The quaternions over the real numbers
  form a division ring: every nonzero
  element is invertible, yet multiplication is not commutative.
- A set with one element is a ring, the zero ring, in which $0 = 1$.

## Basic properties

Multiplying by zero gives zero: $0a = 0 = a0$, since $0a = (0 + 0)a = 0a + 0a$.
Signs behave as in the integers:
$(-a)b = -(ab)$, $(-a)(-b) = ab$ and
$(-1)a = -a$. Multiplication also distributes over
subtraction, for instance $a(b - c) = ab - ac$.

The zero ring is the only ring in which $0$ and $1$ coincide:
$0 = 1$ holds exactly when $R$ has at most one element.

The elements of a ring that have a two-sided multiplicative inverse are its
units, and they form a group under multiplication; for
matrices over a field this is the
[general linear group](trough:Matrix.GeneralLinearGroup).

For any ring $R$ there is
a ring morphism from the integers to $R$, sending a
natural number $n$ to the sum of $n$ copies of $1$ and $-n$ to the negative of
that sum, and
it is the only ring morphism from the integers to $R$.
The [characteristic](trough:ringChar) of $R$ is the nonnegative generator of the
kernel of this morphism.

In a commutative ring the binomial theorem holds:
for all $x$, $y$ and every natural number $n$,

$$(x + y)^n = \sum_{m=0}^{n} \binom{n}{m} x^m y^{n-m}.$$

The same formula holds in any ring
whenever $xy = yx$; without that hypothesis it can fail
already for $n = 2$, where $(x + y)^2 = x^2 + xy + yx + y^2$.

## Related concepts

The structure of a commutative ring is studied through its
[ideals](trough:Ideal), which are the kernels of ring morphisms and give rise to
[quotient rings](trough:Ideal.Quotient.ring). [Prime](trough:Ideal.IsPrime) and
[maximal](trough:Ideal.IsMaximal) ideals are those whose quotients are integral
domains and fields respectively. An integral domain is a nontrivial commutative
ring in which a product of nonzero elements is nonzero. Mathlib's notion of a
domain, stated more generally for semirings, is a nontrivial
ring in which nonzero elements can be cancelled from either side of an equation; for rings this is equivalent to
having no zero divisors, and it does not require commutativity. Special classes of rings include
[Euclidean domains](trough:EuclideanDomain),
[unique factorisation domains](trough:UniqueFactorizationMonoid),
[Noetherian rings](trough:IsNoetherianRing) and
[local rings](trough:IsLocalRing).

Dropping additive inverses gives a semiring, such as the natural numbers;
dropping the multiplicative identity or associativity gives non-unital or
non-associative rings. An abelian group with a scalar multiplication by a ring
that is associative, unital and distributive over both additions is a
[module](trough:Module), and a ring that is also a module
over a commutative ring, compatibly, is an
[algebra](trough:Algebra). Rings and ring morphisms form
[the category of rings](trough:RingCat).

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

## Depends on

- [Group](trough:Group)
- [Set](trough:Set)
