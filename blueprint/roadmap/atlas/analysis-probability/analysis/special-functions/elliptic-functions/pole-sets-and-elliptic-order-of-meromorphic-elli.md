---
declaration: section
origin: cited
lean: PeriodPair.poleMultiplicity, PeriodPair.poleMultiplicity_eq_zero_of_not_meromorphicAt, PeriodPair.poleMultiplicity_eq_zero_of_nonneg, PeriodPair.poleMultiplicity_ne_zero_iff, PeriodPair.poleMultiplicity_eq_neg_divisor, PeriodPair.poleSetInFundamentalParallelogram, PeriodPair.mem_poleSetInFundamentalParallelogram_iff, PeriodPair.isBounded_fundamentalParallelogram
statement: formalized
proof: formalized
---

# Pole sets and elliptic order of meromorphic elliptic functions

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html).

## Pole multiplicity

For a function $f : \mathbb{C} \to \mathbb{C}$ and a point
$z \in \mathbb{C}$, let $\operatorname{ord}_z f \in \mathbb{Z} \cup \{\infty\}$ be the meromorphic
order of $f$ at $z$, which by convention is $0$ when $f$ is not meromorphic at $z$. The pole
multiplicity of $f$ at $z$ is the natural number $\max(0, -\operatorname{ord}_z f)$ when
$\operatorname{ord}_z f$ is finite, and $0$ when $\operatorname{ord}_z f = \infty$. Thus a pole of
order $n \ge 1$ has multiplicity $n$, and every point of nonnegative or infinite order, including
every point where $f$ is not meromorphic, has multiplicity $0$.

Only the order at $z$ is used, so the value at $z$ depends only on the behavior of $f$ near $z$.

Formalized by `PeriodPair.poleMultiplicity`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-multiplicity).

## Pole multiplicity vanishes where the function is not meromorphic

Let
$f \colon \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$. If $f$ is not meromorphic at $z$, then
the pole multiplicity of $f$ at $z$ is $0$.

This holds because the order of $f$ at such a point is $0$ by convention; no global hypothesis on
$f$ is used.

Formalized by `PeriodPair.poleMultiplicity_eq_zero_of_not_meromorphicAt`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-multiplicity-eq-zero-of-not-meromor).

## Pole multiplicity vanishes at points of nonnegative order

Let
$f \colon \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$, and let the order of $f$ at $z$ be its
meromorphic order, an element of $\mathbb{Z} \cup \{\infty\}$ that is $0$ by convention when $f$
is not meromorphic at $z$. If this order is nonnegative (possibly $\infty$), then the pole
multiplicity of $f$ at $z$ is $0$.

Formalized by `PeriodPair.poleMultiplicity_eq_zero_of_nonneg`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-multiplicity-eq-zero-of-nonneg).

## Pole multiplicity is nonzero exactly at negative order

Let
$f \colon \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$, and let the order of $f$ at $z$ be its
meromorphic order, an element of $\mathbb{Z} \cup \{\infty\}$ that is $0$ by convention when $f$
is not meromorphic at $z$. The pole multiplicity of $f$ at $z$ is nonzero if and only if this
order is negative, that is, if and only if $f$ has a pole at $z$.

No hypothesis on $f$ is needed: where $f$ is not meromorphic at $z$, its order is $0$ and both
sides are false.

Formalized by `PeriodPair.poleMultiplicity_ne_zero_iff`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-multiplicity-ne-zero-iff).

## Pole multiplicity via the divisor

Let $U \subseteq \mathbb{C}$, let
$f \colon \mathbb{C} \to \mathbb{C}$ be meromorphic on $U$ and let $z \in U$. Let $D(z)$ be the
value at $z$ of the divisor of $f$ on $U$, that is, the order of $f$ at $z$, taken to be $0$ when
that order is infinite. Then the pole multiplicity of $f$ at $z$ equals $\max(0, -D(z))$.

Unlike the divisor, the pole multiplicity is defined without reference to a domain, so no global
meromorphicity is hidden in its definition.

Formalized by `PeriodPair.poleMultiplicity_eq_neg_divisor`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-multiplicity-eq-neg-divisor).

## Poles in a fundamental parallelogram

For a period pair $L$, a function
$f : \mathbb{C} \to \mathbb{C}$ and a point $\alpha \in \mathbb{C}$, the set of poles of $f$ in
the fundamental parallelogram of $L$ with vertex $\alpha$ is the set of points $z$ of that
parallelogram at which the pole multiplicity of $f$ is nonzero.

Formalized by `PeriodPair.poleSetInFundamentalParallelogram`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-set-in-fundamental-parallelogram).

## Membership in the pole set of a fundamental parallelogram

Let $L$ be a period pair, let
$f \colon \mathbb{C} \to \mathbb{C}$ be any function and let $\alpha, z \in \mathbb{C}$. Then $z$
lies in the pole set of $f$ in the fundamental parallelogram of $L$ with vertex $\alpha$ if and
only if $z$ lies in that parallelogram and the pole multiplicity of $f$ at $z$ is nonzero.

Formalized by `PeriodPair.mem_poleSetInFundamentalParallelogram_iff`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#mem-pole-set-in-fundamental-parallelogra).

## Fundamental parallelograms are bounded

Let $L$ be a period pair. For every
$\alpha \in \mathbb{C}$, the fundamental parallelogram of $L$ with vertex $\alpha$ is a bounded
subset of $\mathbb{C}$.

The proof covers it by the continuous image of a compact cube, rather than by an explicit norm
estimate.

Formalized by `PeriodPair.isBounded_fundamentalParallelogram`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#is-bounded-fundamental-parallelogram).

## Finitely many poles in a fundamental parallelogram

Let $L$ be a period pair, let $f$ be an
elliptic function for $L$, and let $\alpha \in \mathbb{C}$. Then the set of poles of $f$ in the
fundamental parallelogram of $L$ with vertex $\alpha$ is finite.

The proof covers the parallelogram by a closed disc, on which $f$ is meromorphic, and uses that
the divisor of $f$ on that disc has finite support.

Formalized by `PeriodPair.poleSetInFundamentalParallelogram_finite`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-set-in-fundamental-parallelogram-fi).

## Elliptic order in a fundamental parallelogram

Let $L$ be a period pair, let $f$ be an
elliptic function for $L$ and let $\alpha \in \mathbb{C}$. The elliptic order of $f$ in the
fundamental parallelogram of $L$ with vertex $\alpha$ is the natural number obtained by summing
the pole multiplicity of $f$ at $z$ over all points $z$ of the pole set of $f$ in that
parallelogram, that is, over the points of the parallelogram where this multiplicity is nonzero.
Because $f$ is elliptic, this pole set is finite, so the sum is finite.

Formalized by `PeriodPair.ellipticOrderInFundamentalParallelogram`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#elliptic-order-in-fundamental-parallelog).

## Elliptic order

Let $L$ be a period pair and let $f$ be an elliptic function for $L$. The
elliptic order of $f$ is its elliptic order in the fundamental parallelogram of $L$ with vertex
$0$: the sum of the pole multiplicities of $f$ over its poles in that parallelogram.

Formalized by `PeriodPair.ellipticOrder`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#elliptic-order).

## The elliptic order is the parallelogram order at vertex zero

Let $L$ be a period pair
and let $f$ be an elliptic function for $L$. Then the elliptic order of $f$ equals the elliptic
order of $f$ in the fundamental parallelogram of $L$ with vertex $0$. This holds by definition.

Formalized by `PeriodPair.ellipticOrder_eq_orderInFundamentalParallelogram_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#elliptic-order-eq-order-in-fundamental-p).

## Pole multiplicity of a constant function

For all $c, z \in \mathbb{C}$, the pole
multiplicity at $z$ of the constant function with value $c$ is $0$. This includes the zero
constant, whose meromorphic order at every point is $\infty$.

Formalized by `PeriodPair.poleMultiplicity_const`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/Order.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html#pole-multiplicity-const).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pole sets and elliptic order of meromorphic elliptic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/elliptic-functions/pole-sets-and-elliptic-order-of-meromorphic-elli)
