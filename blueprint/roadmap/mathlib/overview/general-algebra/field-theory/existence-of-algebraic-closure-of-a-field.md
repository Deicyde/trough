# Existence of algebraic closure of a field

The **existence of an algebraic closure** is the theorem that every [field](field.md) $k$ has an [algebraic extension](algebraic-extension.md)
$\bar k$ that is [algebraically closed](algebraically-closed-field.md). Such a field $\bar k$ is called an
algebraic closure of $k$; it is unique up to isomorphism over $k$. The theorem
supplies, for every field, one ambient field in which every polynomial over
$k$ splits into linear factors, so that roots, [splitting fields](splitting-field.md) and
algebraic extensions of $k$ can all be studied inside a single field.

## Statement

A field is algebraically closed when every nonconstant polynomial over it has a
root; equivalently, every nonzero polynomial over it is a constant times a
product of linear factors.
Over an algebraically closed field,
[every polynomial of nonzero degree has a root](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.exists_root).
An extension $K$ of a field $k$ is an algebraic closure of $k$ when
[$K$ is algebraically closed and algebraic over $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#isAlgClosure_iff),
that is, every element of $K$ is a root of a nonzero polynomial with
coefficients in $k$.

**Theorem.** Every field $k$ has an algebraic closure: there is a field
$\bar k$ containing $k$ such that
[$\bar k$ is algebraic over $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure.isAlgebraic) and
[$\bar k$ is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure.isAlgClosed).
Mathlib constructs such a field, [the algebraic closure of $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure),
for every field $k$.

## Examples

- An algebraically closed field is
  [an algebraic closure of itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.instIsAlgClosure).
- By the [fundamental theorem of algebra](../../analysis/complex-analysis/fundamental-theorem-of-algebra.md),
  [the complex numbers form an algebraically closed field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Complex.isAlgClosed).
  Every complex number $a + bi$ is a root of the real polynomial
  $x^2 - 2ax + a^2 + b^2$, so $\mathbb{C}$ is algebraic over $\mathbb{R}$ and is an
  algebraic closure of the [real numbers](../numbers/real-number.md).
- $\mathbb{C}$ is not algebraic over the [rational numbers](../numbers/rational-number.md), since it contains
  [transcendental](../../../undergraduate/ring-theory/field-theory/transcendental-elements.md) numbers. But whenever $E$ is an algebraically closed field
  containing a field $F$,
  [the elements of $E$ algebraic over $F$ form an algebraic closure of $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AlgebraicClosure.html#algebraicClosure.isAlgClosure).
  So the algebraic numbers, the complex numbers that are roots of nonzero
  rational polynomials, form an algebraic closure of $\mathbb{Q}$; it is a
  countable field.
- No finite field is algebraically closed: if $a_1, \dots, a_n$ are all the
  elements of a field, the polynomial $(x - a_1)\cdots(x - a_n) + 1$ has no root.
  The algebraic closure of the field with $p$ elements is therefore infinite;
  it is the union of the finite fields with $p^n$ elements, $n \ge 1$, inside it.

## Properties

- **Uniqueness.** [Any two algebraic closures of $k$ are isomorphic as extensions of $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosure.equiv).
  The isomorphism is not unique in general: complex conjugation is a nontrivial
  automorphism of $\mathbb{C}$ over $\mathbb{R}$.
- **Embedding.** If $L$ is an algebraic extension of $k$ and $\Omega$ is an
  algebraically closed field containing $k$, then
  [there is a homomorphism from $L$ to $\Omega$ fixing $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.lift);
  it is injective, as is every homomorphism out of a field. In particular every
  algebraic extension of $k$, such as the splitting field of a polynomial,
  is isomorphic to a subfield of $\bar k$ containing $k$.
- **Normality and separability.** [An algebraic closure is a normal extension](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosure.normal),
  since every polynomial over $k$ splits in it. When $k$ has [characteristic zero](characteristic-zero.md),
  [an algebraic closure of $k$ is a separable extension](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosure.separable).
- **Size.** Every element of $\bar k$ is one of the finitely many roots of a
  polynomial over $k$, so $\bar k$ has at most as many elements as the set of
  polynomials over $k$. Since $k$ embeds in $\bar k$, an infinite field has an
  algebraic closure of the same cardinality, and the algebraic closure of a finite field is countable.

## Proof

Mathlib follows a construction that builds $\bar k$ in one step as a quotient of a
polynomial ring, instead of applying Zorn's lemma to a collection of algebraic
extensions of $k$; Zorn's lemma still enters, through the maximal ideal.
For each monic polynomial $f$ over $k$ of degree $n$, introduce $n$ new
variables $X_{f,1}, \dots, X_{f,n}$, and let $A$ be the
[polynomial ring](../polynomials-and-power-series/polynomial-in-several-indeterminates.md) over $k$ in all these variables, for all $f$ at once. Let $I$
be the [ideal](../ideals-and-quotients/ideal-of-a-commutative-ring.md) of $A$ generated by the coefficients, as a polynomial in a further
variable $x$, of

$$f(x) - (x - X_{f,1})(x - X_{f,2})\cdots(x - X_{f,n})$$

for every monic $f$. The quotient of $A$ by an ideal containing $I$ is a ring in
which each such $f$ factors as the product of the linear factors $x - X_{f,i}$.

First, [$I$ is a proper ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure.spanCoeffs_ne_top). If $1$ lay in $I$, it would be a finite
combination of the generators, involving only finitely many polynomials
$f_1, \dots, f_m$. In a splitting field of the product $f_1 \cdots f_m$, each
$f_j$ factors into linear factors; sending the variables $X_{f_j,i}$ to the
roots of $f_j$, listed with multiplicity, and the remaining variables to any
value gives a homomorphism from $A$ that kills every generator involved, yet
sends $1$ to $1$, a contradiction.

Next, [every proper ideal lies in a maximal ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.exists_le_maximal), so $I$ lies in a
[maximal ideal](../ideals-and-quotients/maximal-ideal.md) $M$. Since
[an ideal is maximal exactly when the quotient by it is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Basic.html#Ideal.Quotient.maximal_ideal_iff_isField_quotient),
the [quotient ring](../ideals-and-quotients/quotient-ring.md) $\bar k = A/M$ is a field. It contains a copy of $k$, and in it every
monic polynomial over $k$ splits. It is generated over $k$ by the images of the
variables, each a root of some polynomial over $k$, so $\bar k$ is algebraic
over $k$.

Finally, $\bar k$ is algebraically closed. By a general criterion,
[a field in which every monic irreducible polynomial has a root is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.of_exists_root).
Let $g$ be such a polynomial over $\bar k$ and $\alpha$ a root of $g$ in some extension
field. Then $\alpha$ is algebraic over $\bar k$, which is algebraic over $k$,
so $\alpha$ is algebraic over $k$. Its minimal polynomial over $k$ splits in
$\bar k$, so $\alpha$ lies in $\bar k$, and $g$ has a root in $\bar k$.

## Related concepts

- An [algebraically closed field](algebraically-closed-field.md) is the kind of field the theorem produces.
- A [rupture field](rupture-field.md) adjoins one root of an irreducible polynomial, and a
  [splitting field](splitting-field.md) all roots of one polynomial; the algebraic closure
  does this for all polynomials at once.
- The [perfect closure](perfect-closure.md) of a field of characteristic $p$ is, up to
  isomorphism, the smallest perfect extension of it, that is, the smallest
  extension in which every element of the extension has a $p$-th root; it embeds
  in $\bar k$.

## In Mathlib

Mathlib defines the algebraic closure of a field $k$ as a specific field built
by the construction above, a quotient of a polynomial ring in many variables by
a maximal ideal chosen by the axiom of choice, and records as instances that it is a
field, an algebra over $k$, algebraic over $k$ and algebraically closed, and
that it is an algebraic closure of $k$ in the sense of the separate property
described next. For the last step of the proof, Mathlib argues by divisibility
instead of passing to an extension field: an irreducible polynomial over
$\bar k$ divides the image of a monic irreducible polynomial over $k$, which
splits, so it splits too. The
field lives in the same universe of types as $k$. Being an algebraic closure is a
separate property of an extension, stated for a commutative ring $R$ and a field
$K$ that is a torsion-free algebra over it; the uniqueness theorem and the embedding theorem
hold more generally for an integral domain in place of $k$, with
torsion-freeness conditions on the algebras that are automatic over a field.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Field](field.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Algebraic extension](algebraic-extension.md)
- [Algebraically closed field](algebraically-closed-field.md)

## Proof depends on

- [Polynomial in several indeterminates](../polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Maximal ideal](../ideals-and-quotients/maximal-ideal.md)
- [Quotient ring](../ideals-and-quotients/quotient-ring.md)
- [Splitting field](splitting-field.md)
- [Rupture field](rupture-field.md)
- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)

## Sources

- [Mathlib documentation: `AlgebraicClosure`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure)
- [Source of `AlgebraicClosure` in Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.lean#L124)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L127)
