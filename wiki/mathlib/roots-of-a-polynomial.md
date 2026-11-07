The **roots of a polynomial** $p$ are the values $a$ at which the
[polynomial](trough:Polynomial) [vanishes](trough:Polynomial.eval), that is, $p(a) = 0$. Over an integral
domain, the roots of a nonzero polynomial, each counted as often as its
[multiplicity](trough:Polynomial.rootMultiplicity), form a finite
[multiset](trough:Multiset) whose size is at most the degree of $p$. Roots tie the
evaluation of a polynomial to its factorization: finding the roots of $p$ is the
same as finding its factors of the form $X - a$, and this link underlies the solution of
equations, the theory of field extensions, and the fact that a polynomial of small
degree is determined by few of its values.

## Definition

Let $R$ be an integral domain: a commutative ring with $1 \neq 0$ in which a
product of nonzero elements is nonzero. An element $a \in R$ is a
root of $p \in R[X]$ when $p(a) = 0$. By the
[factor theorem](trough:Polynomial.dvd_iff_isRoot),
$a$ is a root of $p$ if and only if $X - a$ divides $p$.
For $p \neq 0$, the multiplicity of $a$ is the largest $m$ such that $(X - a)^m$
divides $p$; it is positive exactly when $a$ is a root.

The **roots** of $p$ are collected into
a multiset, the multiset of roots of $p$, in which
each element $a$ occurs as many times as its multiplicity as a root of $p$.
For nonzero $p$,
an element lies in this multiset exactly when it is a root of $p$.
Counting multiplicity, a nonzero polynomial has
at most as many roots as its degree.

The bound comes from the factor theorem and the absence of zero divisors. If $a$
is a root of a nonzero $p$, then $p = (X - a)\,q$ with $\deg q = \deg p - 1$. Any
root $b \neq a$ of $p$ satisfies $(b - a)\,q(b) = 0$, so $q(b) = 0$, and the
multiplicity of $a$ in $p$ is one more than in $q$. A polynomial with no root has the empty multiset of roots, which starts an
induction on the degree that finishes the argument.

## Examples

- The polynomial $X - a$ has the single root $a$,
  and for $n \ge 1$ $X^n$ has the root $0$ with multiplicity $n$.
- The polynomial $X^2 + 1$ has no root in the real numbers. Over the
  [complex numbers](trough:Complex.instField) it factors as $(X - i)(X + i)$, with
  roots $i$ and $-i$. Over the integers modulo $2$ it equals $(X + 1)^2$, so $1$ is
  its only root, with multiplicity $2$.
- In a [finite field](trough:Mathlib.FieldTheory.Finite.Basic) $F$ with $q$
  elements, the roots of $X^q - X$ are all the elements of $F$, each with multiplicity one.
- Without the integral domain hypothesis the bound fails. In the ring of integers
  modulo $8$ the polynomial $X^2 - 1$ has the four roots $1, 3, 5, 7$, and it
  factors in two different ways as $(X - 1)(X + 1)$ and $(X - 3)(X + 3)$.

## Properties

- **Products.** If $pq \neq 0$ (in an integral domain, this says that neither
  factor is zero), then
  the roots of $pq$ are the roots of $p$ together with the roots of $q$,
  multiplicities adding.
- **Constant factors.** For $c \neq 0$,
  the polynomials $cp$ and $p$ have the same roots.
- **Every multiset occurs.** For a finite multiset $s$ of elements of $R$,
  the roots of $\prod_{a \in s} (X - a)$ are exactly $s$.
- **Linear factors.** For every $p$,
  the product of $X - a$ over the roots $a$ of $p$, with multiplicity, divides $p$.
  If the number of roots of $p$ equals its degree, then
  $p$ is its leading coefficient times this product.
  Accordingly, a nonzero polynomial splits over $R$, meaning it is a constant
  times a product of factors $X - a$ with $a \in R$,
  if and only if its number of roots equals its degree.
- **Algebraically closed fields.** Over an
  [algebraically closed field](trough:IsAlgClosed), such as $\mathbb{C}$ by the
  [fundamental theorem of algebra](trough:Complex.isAlgClosed),
  every nonzero polynomial has exactly as many roots as its degree,
  counted with multiplicity.
- **Polynomials and their values.** A polynomial over $R$ that
  vanishes at more distinct points than its degree is the zero polynomial.
  When $R$ is infinite,
  a polynomial vanishing at every element of $R$ is zero,
  so two polynomials with the same values everywhere are equal.
  Over a finite field this fails: $X^q - X$ is nonzero but vanishes everywhere.

## Related concepts

The coefficients of a polynomial that splits are, up to sign and the leading
coefficient, the elementary symmetric functions of its roots
([Vieta's formulas](trough:Polynomial.coeff_eq_esymm_roots_of_card)). A nonconstant
polynomial without roots in its coefficient field acquires them in a larger field: a
[rupture field](trough:AdjoinRoot) of one of its irreducible factors contains at least one, and in a
[splitting field](trough:Polynomial.SplittingField) it splits completely. A nonzero
polynomial over a field is [separable](trough:Polynomial.Separable) exactly when it
has no repeated roots in such a field. For real polynomials,
[Descartes' rule of signs](trough:Polynomial.roots_countP_pos_le_signVariations)
bounds the number of positive roots. For nonconstant complex polynomials, the
[Gauss–Lucas theorem](trough:Polynomial.rootSet_derivative_subset_convexHull_rootSet)
places the roots of the derivative in the convex hull of the roots.

## In Mathlib

Mathlib defines the roots for polynomials over any commutative ring that is an
integral domain, as a multiset, so that multiplicities are part of the data. The
zero polynomial, at which every element vanishes, is
assigned the empty multiset by convention; for this
reason membership in the multiset is equivalent to being a root only for nonzero
polynomials. Because Mathlib also gives the zero polynomial degree $0$ in its
natural-number version of the degree,
the number of roots is at most that degree for every polynomial,
with no nonzero hypothesis, and the statement about algebraically closed fields
likewise holds for every polynomial. The roots of a polynomial in an algebra
$S$ over its coefficient ring, where $S$ is an integral domain (for instance a
larger field), are obtained by mapping its coefficients into $S$ and taking
the roots of the image; the
set of distinct roots in $S$ forgets multiplicities.
Mathlib's notion of splitting is defined over the coefficient ring itself, as a
product of constants and monic linear factors.

## Depends on

- [Polynomial in one indeterminate](trough:Polynomial)
- [Polynomial functions](trough:Polynomial.eval)
- [Multiset](trough:Multiset)
- [Multiplicity](trough:Polynomial.rootMultiplicity)

## Proof depends on

- [The Factor and Remainder Theorems](trough:Polynomial.dvd_iff_isRoot)
