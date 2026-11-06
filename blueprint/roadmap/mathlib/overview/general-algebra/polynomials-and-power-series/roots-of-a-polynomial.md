# Roots of a polynomial

The **roots of a polynomial** $p$ are the values $a$ at which the
[polynomial](polynomial-in-one-indeterminate.md) [vanishes](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md), that is, $p(a) = 0$. Over an integral
domain, the roots of a nonzero polynomial, each counted as often as its
[multiplicity](multiplicity.md), form a finite
[multiset](../../data-structures/sets/multiset.md) whose size is at most the degree of $p$. Roots tie the
evaluation of a polynomial to its factorization: finding the roots of $p$ is the
same as finding its factors of the form $X - a$, and this link underlies the solution of
equations, the theory of field extensions, and the fact that a polynomial of small
degree is determined by few of its values.

## Definition

Let $R$ be an integral domain: a commutative ring with $1 \neq 0$ in which a
product of nonzero elements is nonzero. An element $a \in R$ is a
[root of $p \in R[X]$ when $p(a) = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.IsRoot). By the
[factor theorem](../../../hundred-theorems/part-04/the-factor-and-remainder-theorems.md),
[$a$ is a root of $p$ if and only if $X - a$ divides $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.dvd_iff_isRoot).
For $p \neq 0$, the multiplicity of $a$ is the largest $m$ such that $(X - a)^m$
divides $p$; it is positive exactly when $a$ is a root.

The **roots** of $p$ are collected into
[a multiset, the multiset of roots of $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots), in which
[each element $a$ occurs as many times as its multiplicity as a root of $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.count_roots).
For nonzero $p$,
[an element lies in this multiset exactly when it is a root of $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.mem_roots).
Counting multiplicity, a nonzero polynomial has
[at most as many roots as its degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.card_roots).

The bound comes from the factor theorem and the absence of zero divisors. If $a$
is a root of a nonzero $p$, then $p = (X - a)\,q$ with $\deg q = \deg p - 1$. Any
root $b \neq a$ of $p$ satisfies $(b - a)\,q(b) = 0$, so $q(b) = 0$, and the
multiplicity of $a$ in $p$ is one more than in $q$. A polynomial with no root has the empty multiset of roots, which starts an
induction on the degree that finishes the argument.

## Examples

- [The polynomial $X - a$ has the single root $a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots_X_sub_C),
  and for $n \ge 1$ [$X^n$ has the root $0$ with multiplicity $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots_X_pow).
- The polynomial $X^2 + 1$ has no root in the real numbers. Over the
  [complex numbers](../../../undergraduate/ring-theory/field-theory/field-c-of-complex-numbers.md) it factors as $(X - i)(X + i)$, with
  roots $i$ and $-i$. Over the integers modulo $2$ it equals $(X + 1)^2$, so $1$ is
  its only root, with multiplicity $2$.
- In a [finite field](../../../undergraduate/ring-theory/field-theory/finite-fields.md) $F$ with $q$
  elements, [the roots of $X^q - X$ are all the elements of $F$, each with multiplicity one](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#FiniteField.roots_X_pow_card_sub_X).
- Without the integral domain hypothesis the bound fails. In the ring of integers
  modulo $8$ the polynomial $X^2 - 1$ has the four roots $1, 3, 5, 7$, and it
  factors in two different ways as $(X - 1)(X + 1)$ and $(X - 3)(X + 3)$.

## Properties

- **Products.** If $pq \neq 0$ (in an integral domain, this says that neither
  factor is zero), then
  [the roots of $pq$ are the roots of $p$ together with the roots of $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots_mul),
  multiplicities adding.
- **Constant factors.** For $c \neq 0$,
  [the polynomials $cp$ and $p$ have the same roots](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots_C_mul).
- **Every multiset occurs.** For a finite multiset $s$ of elements of $R$,
  [the roots of $\prod_{a \in s} (X - a)$ are exactly $s$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots_multiset_prod_X_sub_C).
- **Linear factors.** For every $p$,
  [the product of $X - a$ over the roots $a$ of $p$, with multiplicity, divides $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.prod_multiset_X_sub_C_dvd).
  If the number of roots of $p$ equals its degree, then
  [$p$ is its leading coefficient times this product](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.C_leadingCoeff_mul_prod_multiset_X_sub_C).
  Accordingly, a nonzero polynomial splits over $R$, meaning it is a constant
  times a product of factors $X - a$ with $a \in R$,
  [if and only if its number of roots equals its degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Splits.html#Polynomial.splits_iff_card_roots).
- **Algebraically closed fields.** Over an
  [algebraically closed field](../field-theory/algebraically-closed-field.md), such as $\mathbb{C}$ by the
  [fundamental theorem of algebra](../../analysis/complex-analysis/fundamental-theorem-of-algebra.md),
  [every nonzero polynomial has exactly as many roots as its degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.card_roots_eq_natDegree),
  counted with multiplicity.
- **Polynomials and their values.** A polynomial over $R$ that
  [vanishes at more distinct points than its degree is the zero polynomial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.eq_zero_of_natDegree_lt_card_of_eval_eq_zero').
  When $R$ is infinite,
  [a polynomial vanishing at every element of $R$ is zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.zero_of_eval_zero),
  so [two polynomials with the same values everywhere are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.funext).
  Over a finite field this fails: $X^q - X$ is nonzero but vanishes everywhere.

## Related concepts

The coefficients of a polynomial that splits are, up to sign and the leading
coefficient, the elementary symmetric functions of its roots
([Vieta's formulas](../../../undergraduate/ring-theory/polynomial-rings/relationship-between-the-coefficients-and-the-ro.md)). A nonconstant
polynomial without roots in its coefficient field acquires them in a larger field: a
[rupture field](../field-theory/rupture-field.md) of one of its irreducible factors contains at least one, and in a
[splitting field](../field-theory/splitting-field.md) it splits completely. A nonzero
polynomial over a field is [separable](separable-polynomial.md) exactly when it
has no repeated roots in such a field. For real polynomials,
[Descartes' rule of signs](../../../hundred-theorems/part-04/descartes-rule-of-signs.md)
bounds the number of positive roots. For nonconstant complex polynomials, the
[Gauss–Lucas theorem](../../../thousand-plus/analysis/30-functions-of-a-complex-variable/gauss-lucas-theorem.md)
places the roots of the derivative in the convex hull of the roots.

## In Mathlib

Mathlib defines the roots for polynomials over any commutative ring that is an
integral domain, as a multiset, so that multiplicities are part of the data. The
zero polynomial, at which every element vanishes, is
[assigned the empty multiset](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots_zero) by convention; for this
reason membership in the multiset is equivalent to being a root only for nonzero
polynomials. Because Mathlib also gives the zero polynomial degree $0$ in its
natural-number version of the degree,
[the number of roots is at most that degree for every polynomial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.card_roots'),
with no nonzero hypothesis, and the statement about algebraically closed fields
likewise holds for every polynomial. The roots of a polynomial in an algebra
$S$ over its coefficient ring, where $S$ is an integral domain (for instance a
larger field), are obtained by mapping its coefficients into $S$ and taking
[the roots of the image](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.aroots); the
[set of distinct roots in $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.rootSet) forgets multiplicities.
Mathlib's notion of splitting is defined over the coefficient ring itself, as a
product of constants and monic linear factors.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Multiset](../../data-structures/sets/multiset.md)
- [Multiplicity](multiplicity.md)

## Proof depends on

- [The Factor and Remainder Theorems](../../../hundred-theorems/part-04/the-factor-and-remainder-theorems.md)

## Sources

- [Mathlib documentation: `Polynomial.roots`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.roots)
- [Source of `Polynomial.roots` in Mathlib/Algebra/Polynomial/Roots.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Roots.lean#L54)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L97)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L163)
