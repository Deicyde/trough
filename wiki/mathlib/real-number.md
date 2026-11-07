The **real numbers** are the numbers used to measure continuous quantities such as
length, time and mass; together they make up the real line $\mathbb{R}$. They extend
the [rational numbers](trough:Rat) by filling the gaps between them, so that
quantities such as $\sqrt 2$ and $\pi$ have a place on the line. Algebraically they form
an ordered [field](trough:Field), and what sets them apart is completeness: every
nonempty set of real numbers that is bounded above has a least upper bound. Completeness is what makes limits,
continuity, derivatives and integrals behave well, and nearly all of analysis takes
place over $\mathbb{R}$ or over spaces built from it.

## Definition

There are several equivalent ways to build $\mathbb{R}$ from $\mathbb{Q}$. The
construction by Cauchy sequences runs as follows. A sequence $(q_n)$ of rational numbers
is a [Cauchy sequence](trough:CauchySeq) if its terms eventually stay arbitrarily close
to one another: for every rational $\varepsilon > 0$ there is an index $N$ with
$|q_m - q_n| < \varepsilon$ for all $m, n \ge N$. Two Cauchy sequences $(p_n)$ and
$(q_n)$ are called equivalent if $p_n - q_n$ tends to $0$. A real number is an
equivalence class of Cauchy sequences of rationals; this is
how Mathlib defines the real numbers, and
two Cauchy sequences give the same real number exactly when they are equivalent.
A rational number $q$ is identified with the class of the constant sequence
$q, q, q, \dots$

Sums and products of classes are computed term by term. A class is positive when
its sequences are eventually at least some fixed positive rational,
and $x < y$ means that $y - x$ is positive. A Cauchy sequence that does not tend to $0$
is eventually bounded away from $0$, so its terms can be inverted from some point on; this
gives inverses of nonzero classes, and with these operations
$\mathbb{R}$ is a field (see
[the field of real numbers](trough:Real.instField)).

Other constructions use Dedekind cuts (splittings of $\mathbb{Q}$ into a nonempty lower
part with no greatest element and a nonempty upper part lying entirely above it) or infinite decimal expansions. One can also take $\mathbb{R}$ to be any
complete ordered field; the section on uniqueness below explains why all these
approaches give the same structure.

## Examples

- Every [natural number](trough:Nat), [integer](trough:Int) and rational number is a
  real number.
- A real number is a square exactly when it is nonnegative. In
  particular $2$ has a square root, and $\sqrt 2$ is irrational,
  that is, not equal to any rational number (see
  [the irrationality of the square root of 2](trough:irrational_sqrt_two)).
- The circle constant $\pi$ is also irrational.
- The rationals form a countable set, while the set of real numbers
  has the cardinality of the continuum, $2^{\aleph_0}$, and so
  is not countable (see
  [the non-denumerability of the continuum](trough:Cardinal.not_countable_real)). In
  particular the irrational numbers far outnumber the rational ones.

## Properties

- **Ordered field.** The order on $\mathbb{R}$ is total (see
  [order](trough:Real.linearOrder)), and
  it is compatible with the field operations:
  adding the same number to both sides of an inequality preserves it, $0 < 1$, and
  multiplying both sides of a strict inequality by a positive number preserves it.
- **Least upper bounds.**
  Every nonempty set of real numbers that is bounded above has a least upper bound,
  its supremum. This fails in $\mathbb{Q}$: the rationals $q$ with $q^2 < 2$ have no
  rational least upper bound.
- **Cauchy completeness.**
  Every Cauchy sequence of real numbers converges to a real number.
  With the distance $d(x, y) = |x - y|$, $\mathbb{R}$ is therefore a
  [complete](trough:Real.instCompleteSpace) [metric space](trough:MetricSpace) (see
[the metric structure on $\mathbb{R}$](trough:Real.metricSpace)).
- **Archimedean property.** For every real $x$ and every real $y > 0$,
  some natural multiple $ny$ is at least $x$. In particular
  no real number exceeds every natural number.
- **Density of the rationals.** If $x < y$ are real numbers,
  there is a rational $q$ with $x < q < y$; Mathlib proves this
  for every Archimedean ordered field.
- **Rigidity.** Every ring homomorphism from $\mathbb{R}$ to itself is the identity.
  Such a map sends squares to squares, hence preserves the order, and it fixes every
  rational number, so density of the rationals forces it to fix everything.

Completeness is the source of the basic theorems of real analysis, among them the
[Bolzano–Weierstrass theorem](trough:tendsto_subseq_of_bounded) and the
[intermediate value theorem](trough:intermediate_value_Icc).

## Uniqueness

An ordered field is complete if every nonempty subset that is bounded above has a least
upper bound. The real numbers are, up to isomorphism, the only complete ordered field:
for any two complete ordered fields
there is an isomorphism between them that preserves addition, multiplication and order,
and such an isomorphism is unique.
Along the way one shows that
every complete ordered field is Archimedean.
So any construction of $\mathbb{R}$ that yields a complete ordered field gives the same
object, and results about $\mathbb{R}$ do not depend on the construction chosen.

## Related concepts

- The [complex numbers](trough:Complex) are obtained from $\mathbb{R}$ by adjoining a
  square root of $-1$.
- The [extended real numbers](trough:EReal) add the two points $+\infty$ and $-\infty$.
- The [$p$-adic numbers](trough:Padic) arise by completing $\mathbb{Q}$ with respect to
  the $p$-adic absolute value instead of the usual one.
- The [hyperreal numbers](trough:Hyperreal) form an ordered field extending $\mathbb{R}$
  that is not Archimedean and contains infinitesimals.
- More generally, $\mathbb{R}$ is the [completion](trough:UniformSpace.Completion) of
  $\mathbb{Q}$ with its usual distance.

## In Mathlib

Mathlib defines the real numbers as a structure wrapping the completion of $\mathbb{Q}$
with respect to the absolute value, using the same general Cauchy-sequence completion
that also produces the $p$-adic numbers. Its Cauchy condition compares each later term
with a fixed earlier one, which is equivalent to the usual one. The construction is used
only to set up the field, order and completeness; later results rely on those
properties rather than on representing sequences. Equality and order of real numbers are
not computable, so they are decided by classical logic. Operations are made total by
convention: the inverse of $0$ is $0$ (stated for every group with
zero), so division by $0$ gives $0$; the supremum of the empty set is $0$,
as is the supremum of a set that is not bounded above;
and the square root of $x$ is $0$ exactly when $x \le 0$. The
least upper bound property appears as the statement that $\mathbb{R}$ is a conditionally
complete linear order, and the uniqueness theorem is stated for arbitrary conditionally
complete linearly ordered fields.

## Depends on

- [Rational number](trough:Rat)
- [Field](trough:Field)
- [Cauchy sequence](trough:CauchySeq)
