---
article_id: af_976b44bde6657b6d86344fdd
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Real
mathlib_file: Mathlib/Basic/Real/Basic.lean
---

# Real number

The **real numbers** are the numbers used to measure continuous quantities such as
length, time and mass; together they make up the real line $\mathbb{R}$. They extend
the [rational numbers](rational-number.md) by filling the gaps between them, so that
quantities such as $\sqrt 2$ and $\pi$ have a place on the line. Algebraically they form
an ordered [field](../field-theory/field.md), and what sets them apart is completeness: every
nonempty set of real numbers that is bounded above has a least upper bound. Completeness is what makes limits,
continuity, derivatives and integrals behave well, and nearly all of analysis takes
place over $\mathbb{R}$ or over spaces built from it.

## Definition

There are several equivalent ways to build $\mathbb{R}$ from $\mathbb{Q}$. The
construction by Cauchy sequences runs as follows. A sequence $(q_n)$ of rational numbers
is a [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md) if its terms eventually stay arbitrarily close
to one another: for every rational $\varepsilon > 0$ there is an index $N$ with
$|q_m - q_n| < \varepsilon$ for all $m, n \ge N$. Two Cauchy sequences $(p_n)$ and
$(q_n)$ are called equivalent if $p_n - q_n$ tends to $0$. A real number is an
equivalence class of Cauchy sequences of rationals; this is
[how Mathlib defines the real numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real), and
[two Cauchy sequences give the same real number exactly when they are equivalent](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.mk_eq).
A rational number $q$ is identified with the class of the constant sequence
$q, q, q, \dots$

Sums and products of classes are computed term by term. A class is positive when
[its sequences are eventually at least some fixed positive rational](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.mk_pos),
and $x < y$ means that $y - x$ is positive. A Cauchy sequence that does not tend to $0$
is eventually bounded away from $0$, so its terms can be inverted from some point on; this
gives inverses of nonzero classes, and with these operations
[$\mathbb{R}$ is a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.instField) (see
[the field of real numbers](../../../undergraduate/ring-theory/field-theory/part-01/field-r-of-real-numbers.md)).

Other constructions use Dedekind cuts (splittings of $\mathbb{Q}$ into a nonempty lower
part with no greatest element and a nonempty upper part lying entirely above it) or infinite decimal expansions. One can also take $\mathbb{R}$ to be any
complete ordered field; the section on uniqueness below explains why all these
approaches give the same structure.

## Examples

- Every [natural number](natural-number.md), [integer](integer.md) and rational number is a
  real number.
- [A real number is a square exactly when it is nonnegative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Sqrt.html#Real.isSquare_iff). In
  particular $2$ has a square root, and $\sqrt 2$ [is irrational](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Real/Irrational.html#irrational_sqrt_two),
  that is, not equal to any rational number (see
  [the irrationality of the square root of 2](../../../hundred-theorems/part-01/the-irrationality-of-the-square-root-of-2.md)).
- The circle constant $\pi$ [is also irrational](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Pi/Irrational.html#irrational_pi).
- The rationals form a countable set, while the set of real numbers
  [has the cardinality of the continuum, $2^{\aleph_0}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Cardinality.html#Cardinal.mk_real), and so
  [is not countable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Cardinality.html#Cardinal.not_countable_real) (see
  [the non-denumerability of the continuum](../../../hundred-theorems/part-02/the-non-denumerability-of-the-continuum.md)). In
  particular the irrational numbers far outnumber the rational ones.

## Properties

- **Ordered field.** [The order on $\mathbb{R}$ is total](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.linearOrder) (see
  [order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)), and
  [it is compatible with the field operations](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real.instIsStrictOrderedRing):
  adding the same number to both sides of an inequality preserves it, $0 < 1$, and
  multiplying both sides of a strict inequality by a positive number preserves it.
- **Least upper bounds.**
  [Every nonempty set of real numbers that is bounded above has a least upper bound](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html#Real.exists_isLUB),
  its supremum. This fails in $\mathbb{Q}$: the rationals $q$ with $q^2 < 2$ have no
  rational least upper bound.
- **Cauchy completeness.**
  [Every Cauchy sequence of real numbers converges to a real number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html#Real.cauSeq_converges).
  With the distance [$d(x, y) = |x - y|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/MetricSpace/Pseudo/Defs.html#Real.dist_eq), $\mathbb{R}$ is therefore a
  [complete](../../../undergraduate/single-variable-real-analysis/topology-of-r/completeness-of-r.md) [metric space](../../topology/metric-spaces/metric-space.md) (see
[the metric structure on $\mathbb{R}$](../../../undergraduate/single-variable-real-analysis/topology-of-r/metric-structure.md)).
- **Archimedean property.** For every real $x$ and every real $y > 0$,
  [some natural multiple $ny$ is at least $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html#Real.instArchimedean). In particular
  no real number exceeds every natural number.
- **Density of the rationals.** If $x < y$ are real numbers,
  [there is a rational $q$ with $x < q < y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Basic.html#exists_rat_btwn); Mathlib proves this
  for every Archimedean ordered field.
- **Rigidity.** [Every ring homomorphism from $\mathbb{R}$ to itself is the identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Hom.html#Real.ringHom_apply).
  Such a map sends squares to squares, hence preserves the order, and it fixes every
  rational number, so density of the rationals forces it to fix everything.

Completeness is the source of the basic theorems of real analysis, among them the
[Bolzano–Weierstrass theorem](../../../undergraduate/single-variable-real-analysis/topology-of-r/bolzano-weierstrass-theorem.md) and the
[intermediate value theorem](../../topology/topological-algebra/intermediate-value-theorem.md).

## Uniqueness

An ordered field is complete if every nonempty subset that is bounded above has a least
upper bound. The real numbers are, up to isomorphism, the only complete ordered field:
for any two complete ordered fields
[there is an isomorphism between them that preserves addition, multiplication and order](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/CompleteField.html#ConditionallyCompleteLinearOrderedField.inducedOrderRingIso),
and [such an isomorphism is unique](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/CompleteField.html#ConditionallyCompleteLinearOrderedField.uniqueOrderRingIso).
Along the way one shows that
[every complete ordered field is Archimedean](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/CompleteField.html#ConditionallyCompleteLinearOrderedField.to_archimedean).
So any construction of $\mathbb{R}$ that yields a complete ordered field gives the same
object, and results about $\mathbb{R}$ do not depend on the construction chosen.

## Related concepts

- The [complex numbers](complex-number.md) are obtained from $\mathbb{R}$ by adjoining a
  square root of $-1$.
- The [extended real numbers](extended-real-number.md) add the two points $+\infty$ and $-\infty$.
- The [$p$-adic numbers](p-adic-number.md) arise by completing $\mathbb{Q}$ with respect to
  the $p$-adic absolute value instead of the usual one.
- The [hyperreal numbers](hyper-real-number.md) form an ordered field extending $\mathbb{R}$
  that is not Archimedean and contains infinitesimals.
- More generally, $\mathbb{R}$ is the [completion](../../topology/uniform-notions/completion.md) of
  $\mathbb{Q}$ with its usual distance.

## In Mathlib

Mathlib defines the real numbers as a structure wrapping the completion of $\mathbb{Q}$
with respect to the absolute value, using the same general Cauchy-sequence completion
that also produces the $p$-adic numbers. Its Cauchy condition compares each later term
with a fixed earlier one, which is equivalent to the usual one. The construction is used
only to set up the field, order and completeness; later results rely on those
properties rather than on representing sequences. Equality and order of real numbers are
not computable, so they are decided by classical logic. Operations are made total by
convention: [the inverse of $0$ is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/GroupWithZero/Defs.html#inv_zero) (stated for every group with
zero), so division by $0$ gives $0$; [the supremum of the empty set is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html#Real.sSup_empty),
as is [the supremum of a set that is not bounded above](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html#Real.sSup_of_not_bddAbove);
and [the square root of $x$ is $0$ exactly when $x \le 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Real/Sqrt.html#Real.sqrt_eq_zero'). The
least upper bound property appears as the statement that $\mathbb{R}$ is a conditionally
complete linear order, and the uniqueness theorem is stated for arbitrary conditionally
complete linearly ordered fields.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Rational number](rational-number.md)
- [Field](../field-theory/field.md)
- [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md)

## Sources

- [Mathlib documentation: `Real`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Real/Basic.html#Real)
- [Source of `Real` in Mathlib/Basic/Real/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Basic/Real/Basic.lean#L33)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L25)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L280)
