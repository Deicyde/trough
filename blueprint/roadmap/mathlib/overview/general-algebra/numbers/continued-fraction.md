# Continued fraction

A **continued fraction** is an expression of the form

$$a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}$$

which may stop after finitely many steps or go on forever. In the classical case,
usually called a regular continued fraction, $a_0$ is an [integer](integer.md) and the later terms
$a_1, a_2, \dots$ are positive integers. Every [real number](real-number.md) has such an expansion,
obtained by repeatedly splitting off the integer part and inverting the rest. The expansion
stops exactly for [rational numbers](rational-number.md), and its truncations give unusually good
rational approximations, which makes continued fractions a basic tool of Diophantine approximation and
of the arithmetic of quadratic irrationals.

## Definition

A [generalized continued fraction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Basic.html#GenContFract) consists of a head term $h$ and a finite
or infinite [sequence](../../data-structures/list-like-structures/sequence.md) of pairs $(c_i, d_i)$ of partial numerators and
partial denominators, and stands for

$$h + \cfrac{c_0}{d_0 + \cfrac{c_1}{d_1 + \cfrac{c_2}{d_2 + \cdots}}}$$

It is [simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Basic.html#SimpContFract) when every partial numerator equals $1$, and a
[regular continued fraction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Basic.html#ContFract) is a simple one whose partial denominators are all
positive. In this general sense a regular continued fraction need not have integer terms; the
classical regular continued fraction above is the case where the head term and the partial
denominators are integers, with $h = a_0$ and $d_i = a_{i+1}$, and one writes it
$[a_0; a_1, a_2, \dots]$.

The $n$-th convergent of $[a_0; a_1, a_2, \dots]$ is the value $p_n/q_n$ of the truncation
$[a_0; a_1, \dots, a_n]$. Its numerator and denominator are computed by the recurrence

$$p_n = a_n p_{n-1} + p_{n-2}, \qquad q_n = a_n q_{n-1} + q_{n-2},$$

starting from $p_{-1} = 1$, $q_{-1} = 0$, $p_0 = a_0$, $q_0 = 1$. For a regular continued
fraction with terms in a linearly ordered [field](../field-theory/field.md),
[the convergents given by the recurrence equal the values of the truncated fractions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/ConvergentsEquiv.html#ContFract.convs_eq_convs').

## The expansion of a number

To expand a real number $v$, set $a_0 = \lfloor v \rfloor$. If $v$ is an integer, stop;
otherwise $v - a_0$ lies strictly between $0$ and $1$, and one expands
$1/(v - a_0) > 1$ in the same way to obtain $a_1, a_2, \dots$. This is the
[Euclidean algorithm](../divisibility-in-integral-domains/euclids-algorithm.md) in disguise: for $v = 415/93$ the successive divisions
give $415 = 4 \cdot 93 + 43$, $93 = 2 \cdot 43 + 7$, $43 = 6 \cdot 7 + 1$, $7 = 7 \cdot 1$, so

$$\frac{415}{93} = [4; 2, 6, 7],$$

with convergents $4$, $9/2$, $58/13$ and $415/93$.

The algorithm works in any linearly ordered field with a floor function. Its head term is
[the floor of $v$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Translations.html#GenContFract.of_h_eq_floor), its partial numerators are
[all equal to $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#GenContFract.of_partNum_eq_one), and its partial denominators are
[integers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#GenContFract.exists_int_eq_of_partDen) that are
[at least $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#GenContFract.of_one_le_get?_partDen), so the result is
[a regular continued fraction](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#ContFract.of).

## Examples

- **The golden ratio.** $\varphi = (1 + \sqrt 5)/2$ satisfies $\varphi = 1 + 1/\varphi$, so
  $\varphi = [1; 1, 1, 1, \dots]$. Its convergents are $1, 2, 3/2, 5/3, 8/5, \dots$, quotients
  of consecutive Fibonacci numbers.
- **The square root of two.** Since $1/(\sqrt 2 - 1) = \sqrt 2 + 1 = 2 + (\sqrt 2 - 1)$, one
  gets $\sqrt 2 = [1; 2, 2, 2, \dots]$, with convergents $1, 3/2, 7/5, 17/12, 41/29, \dots$.
  Their numerators and denominators satisfy $p_n^2 - 2 q_n^2 = \pm 1$, which links the
  expansion to [Pell's equation](../number-theory/solutions-to-pells-equation.md).

## Properties

Let $v$ lie in a linearly ordered field with a floor function, such as the real numbers, and
let $p_n/q_n$ be the convergents of its expansion.

- **Termination.** [The expansion of $v$ terminates if and only if $v$ is rational](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/TerminatesIffRat.html#GenContFract.terminates_iff_rat).
  If the expansion has no term $a_{n+1}$, then
  [the $n$-th convergent equals $v$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/CorrectnessTerminating.html#GenContFract.of_correctness_of_terminatedAt).
- **Determinant formula.** For a simple continued fraction with terms in any field, whenever
  the term $a_{n+1}$ exists,
  [$p_n q_{n+1} - q_n p_{n+1} = (-1)^{n+1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Determinant.html#SimpContFract.determinant). With integer terms
  this shows that $p_n$ and $q_n$ are coprime, so each convergent is in lowest terms.
- **Growth of denominators.** Whenever the expansion has a term $a_n$, the denominator
  [$q_n$ is at least the Fibonacci number $F_{n+1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#GenContFract.succ_nth_fib_le_of_nth_den), with $F_0 = 0$ and
  $F_1 = 1$;
  the golden ratio shows that this bound is attained.
- **Error bound.** Whenever the expansion has a term $a_{n+1}$,
  [$|v - p_n/q_n| \le 1/(q_n q_{n+1})$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#GenContFract.abs_sub_convs_le). Since the
  denominators [never decrease](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.html#GenContFract.of_den_mono), this is at most $1/q_n^2$.
- **Convergence.** When the field carries its order topology,
  [the convergents tend to $v$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Computation/ApproximationCorollaries.html#GenContFract.of_convergence).
- **Legendre's theorem.** If $v$ is real and a rational number $x/y$ in lowest terms with
  $y \ge 1$ satisfies $|v - x/y| < 1/(2y^2)$, then
  [$x/y$ is one of the convergents of $v$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/ContinuedFractions.html#Real.exists_convs_eq_rat).

Among classical regular continued fractions, every irrational real number has exactly one
infinite expansion, and every infinite one converges to an irrational number. A rational number
has exactly two finite expansions, related by
$[a_0; a_1, \dots, a_n] = [a_0; a_1, \dots, a_n - 1, 1]$ where $a_n \ge 2$ or $n = 0$, such as
$[4; 2, 6, 7] = [4; 2, 6, 6, 1]$ or $[1] = [0; 1]$. A real number has an
eventually periodic expansion if and only if it is an irrational root of a quadratic polynomial
with integer coefficients.

## Related concepts

For $n \ge 1$ the denominators strictly increase, so for an irrational real number $v$ the error
bound gives infinitely many rationals $x/y$ with $|v - x/y| < 1/y^2$, an explicit form of [Dirichlet's approximation theorem](../../../thousand-plus/number-theory/part-01/dirichlets-approximation-theorem.md). Generalized continued fractions with
arbitrary partial numerators appear in analysis as expansions of functions, and for a positive integer $d$
that is not a square, the periodic expansion of $\sqrt d$ yields the fundamental solution of
Pell's equation $x^2 - d y^2 = 1$.

## In Mathlib

Mathlib builds the three notions as successive restrictions: a generalized continued fraction
over any type, the simple ones among them, and the regular ones among those. A regular
continued fraction only asks for positive partial denominators, not for integers; integrality is a property of the expansion of a number, proved separately. The head
term is stored apart, so Mathlib's partial denominators $d_0, d_1, \dots$ are the classical
$a_1, a_2, \dots$, and a finite continued fraction is a sequence that terminates. Convergents
are defined for every index $n$ and take values in the field (more generally, division ring) of
the terms; once a continued
fraction has no term $a_{n+1}$,
[every later convergent equals the $n$-th](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/TerminatedStable.html#GenContFract.convs_stable_of_terminated). For
real numbers there is also a direct recursive definition of the convergents as rational
numbers, which [agrees with the general one](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/DiophantineApproximation/ContinuedFractions.html#Real.convs_eq_convergent).

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Integer](integer.md)
- [Rational number](rational-number.md)
- [Real number](real-number.md)
- [Sequence](../../data-structures/list-like-structures/sequence.md)
- [Field](../field-theory/field.md)

## Sources

- [Mathlib documentation: `ContFract`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/ContinuedFractions/Basic.html#ContFract)
- [Source of `ContFract` in Mathlib/Algebra/ContinuedFractions/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/ContinuedFractions/Basic.lean#L227)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L24)
