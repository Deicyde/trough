# Rational number

A **rational number** is a number that can be written as a quotient $a/b$ of two
[integers](integer.md) with $b \neq 0$. The rational numbers form the set
$\mathbb{Q}$, the smallest number system that contains the integers and in
which division by any nonzero number is always possible. They are the most
familiar example of a [field](../field-theory/field.md), they sit between the integers and the [real numbers](real-number.md), and
both the real and the [$p$-adic numbers](p-adic-number.md) are built from them by
completion.

## Definition

A rational number is determined by a numerator $a \in \mathbb{Z}$ and a nonzero
denominator $b \in \mathbb{Z}$, but not uniquely: $1/2$ and $2/4$ name the same
number. Two quotients are identified by cross-multiplication: for integers
$a, b, c, d$ with $b \neq 0$ and $d \neq 0$,
[$a/b = c/d$ holds exactly when $ad = cb$](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Rat/Lemmas.html#Rat.divInt_eq_divInt_iff).
One construction of $\mathbb{Q}$ takes this as its starting point: a rational
number is an equivalence class of pairs $(a, b)$ with $b \neq 0$ under the
relation $(a, b) \sim (c, d)$ if and only if $ad = cb$.

Each class has a preferred representative. Dividing $a$ and $b$ by their
greatest common divisor, and changing both signs if $b < 0$, gives the
**reduced form** $p/q$, with $q > 0$ and $p$ and $q$ coprime. Lean's library
defines [a rational number to be exactly such a pair](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Rat/Basic.html#Rat): an integer
numerator and a positive natural-number denominator with no common factor
other than $1$. Every rational number $r$ [is the quotient of its numerator by its denominator](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Rat.html#Rat.num_div_den), and the reduced form is unique: if
$a/b = c/d$ with $b, d > 0$, $a$ coprime to $b$ and $c$ coprime to $d$, then
[$a = c$ and $b = d$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Lemmas.html#Rat.div_int_inj). A rational number $r$
[has denominator $1$ exactly when $r$ equals its numerator](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Defs.html#Rat.den_eq_one_iff),
that is, when $r$ is an integer.

The operations are those of school arithmetic:

$$\frac{a}{b} + \frac{c}{d} = \frac{ad + cb}{bd}, \qquad
\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd},$$

and, for positive denominators $b$ and $d$, $a/b \le c/d$ exactly when $ad \le cb$.

## Examples

- $-6/4$ has reduced form $-3/2$; $0$ has reduced form $0/1$.
- Every integer $n$ is rational, as $n/1$.
- The terminating decimal $0.75$ is $3/4$, and the repeating decimal
  $0.333\ldots$ is $1/3$. A real number is rational exactly when its decimal
  expansion is eventually periodic.
- The square root of $2$ is not rational: [$\sqrt 2$ is irrational](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Real/Irrational.html#irrational_sqrt_two) (see [irrationality of the square root of 2](../../../hundred-theorems/part-01/the-irrationality-of-the-square-root-of-2.md)). If $\sqrt 2 = p/q$ in reduced form, then
  $p^2 = 2q^2$ forces $p$ and then $q$ to be even, contradicting coprimality.

## Properties

- **Field.** With these operations [$\mathbb{Q}$ is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Field/Rat.html#Rat.instField)
  (see [field of rational numbers](../../../undergraduate/ring-theory/field-theory/field-q-of-rational-numbers.md)): every nonzero
  $a/b$ has the inverse $b/a$.
- **Field of fractions of $\mathbb{Z}$.** Every rational number is a quotient of
  integers, the map from $\mathbb{Z}$ to $\mathbb{Q}$ is injective, and every nonzero integer is invertible in $\mathbb{Q}$, so
  [$\mathbb{Q}$ is the field of fractions of $\mathbb{Z}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/FractionRing.html#Rat.isFractionRing)
  (see [field of fractions](../field-theory/field-of-fractions-of-an-integral-domain.md)).
- **Prime field of characteristic zero.** $\mathbb{Q}$
  [has characteristic zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Rat.html#Rat.instCharZero) (see [characteristic zero](../field-theory/characteristic-zero.md)). Conversely, in any field $K$ of characteristic zero
  the integers $n \cdot 1$ with $n \neq 0$ are invertible, and sending $a/b$ to
  $(a \cdot 1)(b \cdot 1)^{-1}$ defines [a ring homomorphism from $\mathbb{Q}$ to $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Cast/CharZero.html#Rat.castHom), which [is injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Cast/CharZero.html#Rat.cast_injective). Moreover
  [any two ring homomorphisms from $\mathbb{Q}$ to the same ring are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Cast/Defs.html#RingHom.ext_rat). So every field of characteristic zero contains
  exactly one copy of $\mathbb{Q}$, and that copy is its smallest subfield, the
  prime subfield.
- **Ordered field.** The order is compatible with the operations:
  [$\mathbb{Q}$ is a strictly ordered ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Rat.html#Rat.instIsStrictOrderedRing)
  (see [ordered ring](../rings/ordered-ring.md)), so sums and products of positive
  rationals are positive. It is Archimedean: every rational number is less than
  some natural number.
- **Density.** Between any two rationals $r < s$ lies a third, for instance
  $(r + s)/2$. The rationals are also dense in the reals:
  [$\mathbb{Q}$ is dense in $\mathbb{R}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Order/Archimedean.html#Rat.denseRange_cast), and more
  generally in every Archimedean ordered field with its order topology.
- **Countability.** [$\mathbb{Q}$ is countably infinite](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Rat/Denumerable.html#Rat.instDenumerable)
  (see [denumerability of the rationals](../../../hundred-theorems/part-01/the-denumerability-of-the-rational-numbers.md)): listing
  the reduced fractions by increasing $|p| + q$ puts them in bijection with
  $\mathbb{N}$. Its cardinality is [$\aleph_0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Rat.html#Cardinal.mkRat).
- **Order type.** [Any two countable dense linear orders without endpoints that are nonempty are order-isomorphic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/CountableDenseLinearOrder.html#Order.iso_of_countable_dense)
  ([Cantor's isomorphism theorem](../../../thousand-plus/combinatorics-and-ordered-structures/06-order-lattices-ordered-algebraic-structures/cantors-isomorphism-theorem.md)).
  Since $\mathbb{Q}$ is such an order, it is, up to order isomorphism, the only one.
- **Incompleteness.** The set of positive rationals $x$ with $x^2 < 2$ is bounded
  above in $\mathbb{Q}$ but has no least upper bound there. Filling these gaps
  produces the real numbers, which can be built as equivalence classes of
  Cauchy sequences of rationals.
- **Continued fractions.** [A real number has a terminating continued fraction expansion exactly when it is rational](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/TerminatesIffRat.html#GenContFract.terminates_iff_rat)
  (see [continued fraction](continued-fraction.md)); the statement holds more
  generally in any linearly ordered field with a floor function.

## Absolute values and completions

Besides the usual absolute value $|x|$, the rationals carry the $p$-adic absolute
value for each prime $p$, which is small on numbers divisible by a high power of
$p$. [Ostrowski's theorem](../../../thousand-plus/number-theory/part-02/ostrowskis-theorem.md) says these are all: [every nontrivial real-valued absolute value on $\mathbb{Q}$ is equivalent either to the usual one or to the $p$-adic one for a unique prime $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Ostrowski.html#Rat.AbsoluteValue.equiv_real_or_padic).
Completing $\mathbb{Q}$ with respect to the usual absolute value gives
$\mathbb{R}$; completing with respect to the $p$-adic one gives the field of
$p$-adic numbers.

## In Mathlib

The type of rational numbers is defined in Lean's core library, not in Mathlib
itself, as a structure holding the reduced form: an integer numerator, a
natural-number denominator, a proof that the denominator is nonzero, and a proof
that numerator and denominator are coprime. Arithmetic operations normalize
their results, so equal rational numbers have identical representations and
equality can be decided by comparing numerators and denominators. Core Lean also
defines the arithmetic operations and the order relation; Mathlib adds the field
and ordered-field structure, the topology and the cardinality results. As everywhere in
Mathlib, division is a total operation, and [dividing by zero gives zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Basic.html#div_zero), so $1/0 = 0$ in $\mathbb{Q}$. Mathlib maps rational numbers
into any division ring by the same formula as above, a map that is injective in
characteristic zero, and it defines an irrational number as a real number not in
the image of $\mathbb{Q}$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Integer](integer.md)
- [Natural number](natural-number.md)

## Sources

- [Mathlib documentation: `Rat`](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Rat/Basic.html#Rat)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L23)
