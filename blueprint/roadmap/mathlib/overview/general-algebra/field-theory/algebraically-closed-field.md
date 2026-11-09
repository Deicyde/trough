# Algebraically closed field

An **algebraically closed field** is a [field](field.md) in which every
nonconstant [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) in one variable has a root. In such a
field every polynomial breaks up completely into linear factors, so questions about
polynomial equations reduce to questions about their [roots](../polynomials-and-power-series/roots-of-a-polynomial.md).
The complex numbers are the most familiar example. Algebraically closed fields are
the natural setting for linear algebra over a field (every square matrix of positive size has an eigenvalue)
and for classical algebraic geometry, where the Nullstellensatz needs them.

## Definition

A field $k$ is algebraically closed if
[every polynomial with coefficients in $k$ is a product of a constant and linear factors](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed):

$$f = c\,(x - a_1)(x - a_2)\cdots(x - a_n), \qquad c, a_1, \dots, a_n \in k.$$

Several conditions are equivalent to this.

- **Roots.** Over an algebraically closed field,
  [every nonconstant polynomial has a root](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.exists_root). Conversely,
  [if every monic irreducible polynomial over $k$ has a root in $k$, then $k$ is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.of_exists_root).
  The two directions together say that $k$ is algebraically closed exactly when every
  nonconstant polynomial over $k$ has a root in $k$.
- **Irreducible polynomials.** Over an algebraically closed field,
  [every irreducible polynomial has degree one](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.degree_eq_one_of_irreducible)
  (see [irreducible element](../divisibility-in-integral-domains/irreducible-element.md)). Conversely, if every irreducible
  polynomial over $k$ has degree one, then every polynomial factors into linear factors,
  since every nonzero polynomial is a product of a constant and irreducible polynomials, so $k$ is
  algebraically closed.
- **Extensions.** If $k$ is algebraically closed and $K$ is any extension field of $k$,
  then [every intermediate field $k \subseteq L \subseteq K$ that is algebraic over $k$ equals $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IntermediateField.eq_bot_of_isAlgClosed_of_isAlgebraic):
  $k$ has no proper [algebraic extension](algebraic-extension.md). Conversely,
  [if every finite extension of $k$ has degree one over $k$, then $k$ is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.of_finiteDimensional_imp_finrank_eq_one).

## Examples

- **The complex numbers.** The [fundamental theorem of algebra](../../analysis/complex-analysis/fundamental-theorem-of-algebra.md)
  says that [the field $\mathbb{C}$ of complex numbers is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Complex.isAlgClosed).
- **Algebraic closures.** Every field $k$ sits inside an algebraically closed field
  that is algebraic over $k$, called an [algebraic closure](existence-of-algebraic-closure-of-a-field.md) of $k$;
  [the algebraic closure constructed in Mathlib is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure.isAlgClosed).
  The algebraic closure of $\mathbb{Q}$ can be taken to be the field of complex numbers
  that are roots of nonzero polynomials with rational coefficients. The algebraic
  closure of the field with $p$ elements is the union of its
  [finite subfields](../../../undergraduate/ring-theory/field-theory/finite-fields.md), one of order $p^n$ for each $n \ge 1$.
- **Non-examples.** The [real numbers](../numbers/real-number.md) are not algebraically closed,
  since $x^2 + 1$ has no real root; neither are the rationals. No finite field is
  algebraically closed: if its elements are $a_1, \dots, a_q$, then the polynomial
  $(x - a_1)\cdots(x - a_q) + 1$ takes the value $1$ at every element, so it has no root.
  The same argument shows that every algebraically closed field is infinite.

## Properties

- **Counting roots.** Over an algebraically closed field, a nonzero polynomial
  [has exactly as many roots as its degree, counted with multiplicity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.card_roots_eq_natDegree)
  (see [multiplicity](../polynomials-and-power-series/multiplicity.md)).
- **Roots of elements.** For every element $x$ and every integer $n \ge 1$,
  [there is an element $z$ with $z^n = x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.exists_pow_nat_eq),
  since $z^n - x$ is a nonconstant polynomial in $z$.
- **Perfectness.** An irreducible polynomial over an algebraically closed field has
  degree one, so it has a single simple root and is
  [separable](../polynomials-and-power-series/separable-polynomial.md). Hence
  [every algebraically closed field is perfect](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.perfectField): every
  irreducible polynomial over it is separable. In [characteristic $p$](characteristic-p.md)
  this matches the fact that every element has a $p$-th root.
- **Uniqueness of algebraic closures.** An algebraic closure of $k$ is
  [an extension field of $k$ that is algebraically closed and algebraic over $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#isAlgClosure_iff),
  and [any two algebraic closures of $k$ are isomorphic by an isomorphism that fixes $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosure.equiv).
  The isomorphism is not unique in general.
- **Classification.** An algebraically closed field is determined up to isomorphism by
  its characteristic and a cardinal, its transcendence degree over its prime field: the
  size of a maximal algebraically independent subset over the smallest subfield, which is
  $\mathbb{Q}$ or the field with $p$ elements. For
  uncountable fields this cardinal equals the cardinality of the field, so
  [two uncountable algebraically closed fields with the same characteristic and the same cardinality are isomorphic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Classification.html#IsAlgClosed.ringEquiv_of_equiv_of_char_eq).

## Consequences

- **Eigenvalues.** If $V$ is a nonzero finite-dimensional vector space over an
  algebraically closed field, then
  [every linear map from $V$ to itself has an eigenvalue](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Eigenspace/Triangularizable.html#Module.End.exists_eigenvalue)
  (see [eigenvalue](../../linear-algebra/structure-theory-of-endomorphisms/eigenvalue.md)), because its characteristic
  polynomial has a root. This is what makes triangular and Jordan forms available over $\mathbb{C}$.
- **The Nullstellensatz.** Let $k$ be a field contained in an algebraically closed field
  $K$, and let $I$ be an ideal of polynomials over $k$ in finitely many variables. The
  [Nullstellensatz](../../geometry/algebraic-geometry/nullstellensatz.md) says that
  [the polynomials over $k$ that vanish at every common zero of $I$ in $K$ form exactly the radical of $I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Nullstellensatz.html#MvPolynomial.vanishingIdeal_zeroLocus_eq_radical).
  In the case $k = K$, maximal ideals correspond to points:
  [an ideal of the polynomial ring over $K$ in finitely many variables is maximal exactly when it consists of the polynomials vanishing at a single point](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Nullstellensatz.html#MvPolynomial.isMaximal_iff_eq_vanishingIdeal_singleton).

## In Mathlib

Mathlib states algebraic closedness as a property of a field, defined by asking that
every polynomial split, where a polynomial splits when it is a product of constants and
monic linear polynomials. The zero polynomial and the nonzero constants split trivially,
so the definition imposes no condition on them. The formulation through roots is a
theorem, in both directions, and the converse only asks for roots of monic irreducible
polynomials. The degree condition in the root statement only excludes the nonzero
constants, so it also covers the zero polynomial, which has every element as a root.
Being an algebraic closure is a separate property of an extension, defined over
suitable commutative rings and not only over fields. Mathlib constructs one algebraic
closure of each field, as a quotient of a polynomial ring in many variables by a maximal
ideal, and records that the complex numbers are algebraically closed. The classification
by cardinality is stated with the characteristic given as a natural number, which is $0$
in characteristic zero.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Field](field.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Roots of a polynomial](../polynomials-and-power-series/roots-of-a-polynomial.md)

## Sources

- [Mathlib documentation: `IsAlgClosed`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed)
- [Source of `IsAlgClosed` in Mathlib/FieldTheory/IsAlgClosed/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/FieldTheory/IsAlgClosed/Basic.lean#L59)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L126)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L185)
