# Extended real number

The **extended real numbers** are the [real numbers](real-number.md) together with
two further elements, $+\infty$ and $-\infty$, placed above and below every real
number. The resulting set, written $\overline{\mathbb{R}}$ or $[-\infty, +\infty]$, is the
[set of extended real numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal). Adjoining the two infinities makes
the order complete: every subset acquires a supremum and an infimum. This makes the extended reals a natural home for
suprema, infima, [limits superior and inferior](../../topology/topological-algebra/limit-infimum-and-supremum.md)
and limits of unbounded sequences, and, in their nonnegative part, for measures and
integrals of nonnegative functions.

## Definition

As a set, $\overline{\mathbb{R}} = \mathbb{R} \cup \{-\infty, +\infty\}$. The order extends that of
$\mathbb{R}$ by declaring $-\infty < x < +\infty$ for every real $x$: indeed
[$-\infty$ lies below every real number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.bot_lt_coe) and
[$+\infty$ lies above every real number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.coe_lt_top). The real line sits
inside unchanged: for real $x$ and $y$,
[$x < y$ holds in $\overline{\mathbb{R}}$ exactly when it holds in $\mathbb{R}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.coe_lt_coe_iff),
and [the real numbers are precisely the elements strictly between $-\infty$ and $+\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.range_coe_eq_Ioo).

With this order $\overline{\mathbb{R}}$ is a complete linear order, with least element
$-\infty$ and greatest element $+\infty$. A subset that is unbounded above in
$\mathbb{R}$ has supremum $+\infty$, and the empty set has supremum $-\infty$ and
infimum $+\infty$.

## Arithmetic

Negation extends to an order-reversing involution, with
[$-(+\infty) = -\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.neg_top), [$-(-\infty) = +\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.neg_bot),
and [$-a \le -b$ if and only if $b \le a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.neg_le_neg_iff), so that
[negation is an order isomorphism from $\overline{\mathbb{R}}$ to its order dual](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.negOrderIso).

Addition extends the real sum by
[$+\infty + x = +\infty$ for every $x \neq -\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.top_add_of_ne_bot).
The sum $(+\infty) + (-\infty)$ has no natural value, and conventions differ. One
common choice, used in Mathlib, sets
[$-\infty + x = -\infty$ for every $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.bot_add), including $x = +\infty$.
Consequently subtraction, defined by $a - b = a + (-b)$, gives
[$x - (+\infty) = -\infty$ for every $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.sub_top), and
while [$x - x = 0$ for real $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.sub_self), the differences $(+\infty) - (+\infty)$
and $(-\infty) - (-\infty)$ both equal $-\infty$. The extended reals
therefore form a commutative monoid under addition but not a group. Strict
inequalities still add: [if $a < b$ and $c < d$, then $a + c < b + d$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.add_lt_add).

Multiplication follows the rule of signs:
[$x \cdot (+\infty) = +\infty$ for $x > 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.mul_top_of_pos),
[$x \cdot (+\infty) = -\infty$ for $x < 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.mul_top_of_neg), and
[$(-\infty)(-\infty) = +\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.bot_mul_bot). The convention
[$0 \cdot x = 0$ for every extended real $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.zero_mul) settles the
remaining case. Multiplication is [commutative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.mul_comm) and associative,
but it does not distribute over addition in general:

$$(1 + (-1)) \cdot (+\infty) = 0, \qquad 1 \cdot (+\infty) + (-1) \cdot (+\infty) = -\infty.$$

Distributivity holds in two useful cases:
[$x(y + z) = xy + xz$ whenever $x$ is real and nonnegative](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.left_distrib_of_nonneg_of_ne_top),
and [$c(a + b) = ca + cb$ whenever $a, b \ge 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Operations.html#EReal.left_distrib_of_nonneg).

## Topology

The extended reals carry the [order topology](../../topology/topological-algebra/order-topology.md), in which the
neighbourhoods of $+\infty$ are the sets containing a ray $(r, +\infty]$ with $r$
real. The inclusion of $\mathbb{R}$ is [a homeomorphism onto an open subset](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Instances/EReal/Lemmas.html#EReal.isOpenEmbedding_coe), and
[the finite elements form a space homeomorphic to $\mathbb{R}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Instances/EReal/Lemmas.html#EReal.neBotTopHomeomorphReal).
Since $\overline{\mathbb{R}}$ is a complete linear order,
[it is compact](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/Compact.html#compactSpace_of_completeLinearOrder); it is homeomorphic to the
closed interval $[-1, 1]$, so it is a two-point compactification of the real line.
The rationals are [dense](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/Real.html#EReal.denseRange_ratCast): between any two extended
reals $a < b$ [there is a rational number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.lt_iff_exists_rat_btwn).

Convergence to the infinities matches the familiar notion: a sequence
[tends to $+\infty$ in $\overline{\mathbb{R}}$ exactly when, for every real $r$, its terms eventually exceed $r$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Instances/EReal/Lemmas.html#EReal.tendsto_nhds_top_iff_real),
and for real-valued sequences this is
[the usual divergence to $+\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Instances/EReal/Lemmas.html#EReal.tendsto_coe_nhds_top_iff). Addition is
[continuous at every pair other than $(+\infty, -\infty)$ and $(-\infty, +\infty)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Instances/EReal/Lemmas.html#EReal.continuousAt_add),
where no convention could make it continuous: near $(+\infty, -\infty)$ the sums
$n + (c - n)$, with $n$ large, take every real value $c$.

## Related concepts

- The nonnegative extended reals, in which measures and
  [integrals of nonnegative functions](../../analysis/measures-and-integral-calculus/part-01/integral-of-positive-measurable-functions.md) take their
  values, can be identified with [the closed interval $[0, +\infty]$ of $\overline{\mathbb{R}}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.range_coe_ennreal).
- The [exponential](../../analysis/special-functions/exponential.md) extends with $e^{-\infty} = 0$ and $e^{+\infty} = +\infty$
  to [a homeomorphism from $\overline{\mathbb{R}}$ onto $[0, +\infty]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Log/ENNRealLogExp.html#EReal.expHomeomorph).
  With the convention $0 \cdot \infty = 0$ on $[0, +\infty]$, it satisfies
  [$e^{x + y} = e^x e^y$ for all extended reals $x$ and $y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Log/ERealExp.html#EReal.exp_add); the
  choice $-\infty + (+\infty) = -\infty$ is what makes this hold without exception.
- The projectively extended real line adds a single point $\infty$ instead of two;
  topologically it is a circle rather than a closed interval.
- The [hyperreal numbers](hyper-real-number.md) also contain infinite elements, but they
  form an ordered field with infinitesimals; the extended reals contain no
  infinitesimals and are not a field.

## In Mathlib

Mathlib builds the extended reals by adjoining a top element to $\mathbb{R}$ and then a
bottom element to the result. Its order, lattice structure and addition come from
this construction, which is why the sum of $+\infty$ and $-\infty$ is $-\infty$: the
bottom element absorbs everything under addition. Completeness of the order is
inherited from a general fact about conditionally complete linear orders, and the
topology is defined as the order topology. Multiplication is defined by cases,
with $0$ times anything equal to $0$. Mathlib also defines a reciprocal
$x \mapsto x^{-1}$, which agrees with the real reciprocal on nonzero reals and sends
$\pm\infty$ and $0$ to $0$ ([of $+\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Inv.html#EReal.inv_top), [of $-\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Inv.html#EReal.inv_bot),
[of $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Inv.html#EReal.inv_zero)). Passing back to the reals,
[the map to $\mathbb{R}$ sends $+\infty$ to $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.toReal_top),
[sends $-\infty$ to $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.toReal_bot), and
[is the identity on real numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal.toReal_coe). The nonnegative extended
reals, used throughout measure theory, are a separate type that Mathlib maps into the
extended reals.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Real number](real-number.md)

## Sources

- [Mathlib documentation: `EReal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/EReal/Basic.html#EReal)
- [Source of `EReal` in Mathlib/Data/EReal/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/EReal/Basic.lean#L33)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L26)
