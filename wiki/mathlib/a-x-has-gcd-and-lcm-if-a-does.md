The statement that **$A[X]$ has gcd and lcm if $A$ does** says that if every two
elements of an integral domain $A$ have a [greatest common divisor](trough:GCDMonoid.gcd)
and a [least common multiple](trough:GCDMonoid.lcm), then the same holds in the
[polynomial ring](trough:Polynomial) $A[X]$. In other words, the polynomial ring over a
GCD domain is again a GCD domain. The result explains why polynomials over the
integers, or over any [unique factorisation domain](trough:UniqueFactorizationMonoid),
admit gcds even though division with remainder is not available in general, and it is the main
structural output of the theory of contents and primitive polynomials around
Gauss's lemma.

## Statement

Let $A$ be an integral domain. An element $d$ is a greatest common divisor of $a$
and $b$ if $d$ divides both and every common divisor of $a$ and $b$ divides $d$;
equivalently, an element divides $\gcd(a,b)$ exactly when it divides both $a$ and $b$.
Dually, $\operatorname{lcm}(a,b)$ divides an element exactly when $a$ and $b$ both divide it.
These are determined only up to multiplication by a unit, so one fixes a
normalization: a rule choosing one representative in each class of associated
elements, such as the nonnegative integer in $\mathbb{Z}$.

**Theorem.** If $A$ is an integral domain equipped with a normalization in which
every pair of elements has a normalized gcd and lcm, then
$A[X]$ carries the same structure. The
normalization on $A[X]$ is induced from $A$:
a polynomial $p$ is normalized by multiplying it by the constant unit that normalizes its leading coefficient,
so a polynomial counts as normalized exactly when its leading coefficient is
normalized in $A$. In particular,
the leading coefficient of the normalization of $p$ is the normalization of the leading coefficient of $p$.

When $A$ is a [field](trough:Field), every nonzero element normalizes to $1$, so the
gcd of two polynomials, not both zero, is the monic gcd familiar from the
[Euclidean algorithm in $A[X]$](trough:Polynomial.instEuclideanDomain).

## Examples

- **Integer polynomials.** In $\mathbb{Z}[X]$ take $p = 6X^2 - 6 = 6(X-1)(X+1)$ and
  $q = 4X^2 + 8X + 4 = 4(X+1)^2$. The contents (gcds of the coefficients) are $6$ and $4$,
  with gcd $2$, and the primitive parts $(X-1)(X+1)$ and $(X+1)^2$ have gcd $X+1$, so $\gcd(p,q) = 2X + 2$; similarly
  $\operatorname{lcm}(p,q) = 12(X-1)(X+1)^2$. The product of the gcd and the lcm is $24(X-1)(X+1)^3 = pq$.
- **Gcds without Bézout.** In $\mathbb{Z}[X]$ the gcd of $2$ and $X$ is $1$, yet $1$ is
  not of the form $2f + Xg$, since every such polynomial has an even constant term.
  So [Bézout's identity](trough:exists_gcd_eq_mul_add_mul) fails, so gcds in
  $A[X]$ cannot be produced by a Euclidean algorithm that tracks Bézout coefficients.
- **Beyond unique factorisation.** Every unique factorisation domain
  with a chosen normalization is a GCD domain,
  but not conversely: the ring of all algebraic integers is a GCD domain with no
  irreducible elements at all. The theorem applies to such rings as well.

## Content and primitive polynomials

Over a GCD domain $A$, the content of a polynomial $p$ is
the gcd of its coefficients. A polynomial is
primitive when the only constants dividing it are
units, which over a GCD domain means that
its content is $1$. Every polynomial
factors as its content times a primitive part,
and the primitive part is primitive. The key
facts are the forms of Gauss's lemma:

- a product of primitive polynomials is primitive;
- the content of $pq$ is associated to the product of the contents,
  and it equals that product when the normalization of
  $A$ is multiplicative, as it is for $\mathbb{Z}$.

From these one obtains a divisibility test: for $q \neq 0$,
$p$ divides $q$ if and only if the content of $p$ divides that of $q$ and the primitive part of $p$ divides that of $q$.

## Proof

It suffices to construct least common multiples; in a cancellative commutative monoid with zero
in which every pair has an lcm, the gcd of two nonzero elements is their product divided by
their lcm.

First, any two primitive polynomials $p$ and $q$ have a primitive lcm.
Among the primitive common multiples of $p$ and $q$ (the product $pq$ is one), choose
$r$ of least degree. Let $s$ be any nonzero common multiple; replacing $s$ by its
primitive part, one may assume $s$ primitive, so $\deg r \le \deg s$. If $s$ is
constant, then so is $r$, and a primitive constant is a unit. Otherwise
the polynomial

$$s' = \operatorname{lc}(r)\, s - \operatorname{lc}(s)\, X^{\deg s - \deg r}\, r$$

is a common multiple of smaller degree, where $\operatorname{lc}$ denotes the
leading coefficient. By induction on degree $r$ divides $s'$, hence divides
$\operatorname{lc}(r)\,s$, and because $r$ is primitive Gauss's lemma lets one
cancel the constant: $r$ divides $s$.

For arbitrary $p$ and $q$, let $r$ be a primitive lcm of their primitive parts. Then
$\operatorname{lcm}(c(p), c(q))\, r$, with $c$ the content, is an lcm of $p$ and $q$:
by the divisibility test, a nonzero $s$ is a multiple of both exactly when $c(s)$ is
a multiple of $c(p)$ and $c(q)$ and the primitive part of $s$ is a multiple of both
primitive parts.

## Consequences

- By induction on the number of variables, $A[X_1, \dots, X_n]$ is a GCD domain
  whenever $A$ is; for instance $\mathbb{Z}[X,Y]$ and $K[X,Y]$ over a field $K$.
- For $p \neq 0$,
  the gcd of $p$ and $q$ has degree at most that of $p$.
- The parallel statement for factorisation, that a polynomial ring over a unique
  factorisation domain is again one, is the companion
  [theorem on polynomial rings over UFDs](trough:MvPolynomial.uniqueFactorizationMonoid);
  its conclusion is stronger, but the gcd version also covers GCD domains that are
  not UFDs.

## In Mathlib

Mathlib records the theorem as an instance: a commutative ring with a normalized gcd
structure yields one on its polynomial ring. A gcd structure includes cancellation of
nonzero factors, so the base ring is automatically an integral domain or the zero
ring; nontriviality is never assumed. Gcd and lcm are total operations, normalized
so that they are well defined rather than defined up to units; the gcd of $0$ and $0$
is $0$. The proof constructs the lcm as above, choosing it from an existence statement,
and derives the gcd from it; the resulting operations are noncomputable. Separate instances transfer the version with a
multiplicative normalization, and the bare property of having gcds without a chosen
normalization, to the polynomial ring. The common textbook route through the field of
fractions is not used.

## Depends on

- [Greatest common divisor](trough:GCDMonoid.gcd)
- [Least common multiple](trough:GCDMonoid.lcm)
- [Polynomial in one indeterminate](trough:Polynomial)
