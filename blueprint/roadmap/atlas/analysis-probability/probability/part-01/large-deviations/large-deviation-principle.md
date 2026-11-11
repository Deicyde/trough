---
declaration: section
origin: cited
lean: MathlibExt.Probability.LargeDeviationPrinciple.IsRateFunction, MathlibExt.Probability.LargeDeviationPrinciple.IsGoodRateFunction, MathlibExt.Probability.LargeDeviationPrinciple.IsConvexRateFunction, MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP, MathlibExt.Probability.LargeDeviationPrinciple.IsGoodRateFunction.isRateFunction, MathlibExt.Probability.LargeDeviationPrinciple.IsConvexRateFunction.isRateFunction, MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP.borel_lower_bound, MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP.borel_upper_bound
statement: formalized
proof: formalized
---

# Large deviation principle

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html).

## Rate function

Let $X$ be a topological space. A rate function on $X$ is a lower
semicontinuous function $I : X \to [0, \infty]$.

This is the basic regularity hypothesis used in the formulation of a large deviation principle.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.IsRateFunction`, a structure declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#is-rate-function).

## Good rate function

Let $X$ be a topological space. A function $I : X \to [0, \infty]$ is a
good rate function if it is a rate function and, for every real number $a \ge 0$, the sub-level
set $\{x \in X : I(x) \le a\}$ is compact.

Compactness is required only at finite levels: the sub-level set at level $\infty$ is all of $X$,
so requiring it as well would force $X$ itself to be compact.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.IsGoodRateFunction`, a structure declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#is-good-rate-function).

## Convex rate function

Let $X$ be a real vector space carrying a topology (no compatibility
between the topology and the linear structure is assumed). A function $I : X \to [0, \infty]$ is a
convex rate function if it is a rate function and $I(ax + by) \le a I(x) + b I(y)$ for all
$x, y \in X$ and all real numbers $a, b \ge 0$ with $a + b = 1$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.IsConvexRateFunction`, a structure declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#is-convex-rate-function).

## Large deviation principle for a sequence of measures

Let $X$ be a topological space with
a $\sigma$-algebra containing every open set, let $(\mu_n)_{n \in \mathbb{N}}$ be a sequence of
measures on $X$, and let $I : X \to [0, \infty]$. The sequence $(\mu_n)$ satisfies the large
deviation principle with rate function $I$ and speed $n$ if $I$ is a rate function, every open
set $U \subseteq X$ satisfies

$$\liminf_{n \to \infty} \frac{1}{n} \log \mu_n(U) \ge -\inf_{x \in U} I(x),$$

and every closed set $F \subseteq X$ satisfies

$$\limsup_{n \to \infty} \frac{1}{n} \log \mu_n(F) \le -\inf_{x \in F} I(x).$$

Here $\log 0 = -\infty$, an infimum over the empty set is $\infty$, and the limits are taken in
the extended reals.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP`, a structure declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#satisfies-ldp).

## Good rate functions are rate functions

Every good rate function on a topological space
is a rate function.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.IsGoodRateFunction.isRateFunction`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#is-rate-function-2).

## Convex rate functions are rate functions

Every convex rate function on a real vector space
with a topology is a rate function.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.IsConvexRateFunction.isRateFunction`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#is-rate-function-3).

## Large deviation lower bound for arbitrary sets

Let $X$ be a topological space with a
$\sigma$-algebra in which every open set is measurable, and let $(\mu_n)_{n \in \mathbb{N}}$ be
measures on $X$ satisfying the large deviation principle with rate function
$I : X \to [0, \infty]$. Then for every set $\Gamma \subseteq X$, not necessarily measurable (for
non-measurable $\Gamma$, $\mu_n(\Gamma)$ is its outer measure), with interior $\Gamma^\circ$,

$$-\inf_{x \in \Gamma^\circ} I(x) \le \liminf_{n \to \infty} \frac{1}{n} \log \mu_n(\Gamma),$$

computed in the extended reals with $\log 0 = -\infty$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP.borel_lower_bound`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#borel-lower-bound).

## Large deviation upper bound for arbitrary sets

Let $X$ be a topological space with a
$\sigma$-algebra in which every open set is measurable, and let $(\mu_n)_{n \in \mathbb{N}}$ be
measures on $X$ satisfying the large deviation principle with rate function
$I : X \to [0, \infty]$. Then for every set $\Gamma \subseteq X$, not necessarily measurable (for
non-measurable $\Gamma$, $\mu_n(\Gamma)$ is its outer measure), with closure $\overline{\Gamma}$,

$$\limsup_{n \to \infty} \frac{1}{n} \log \mu_n(\Gamma) \le -\inf_{x \in \overline{\Gamma}} I(x),$$

computed in the extended reals with $\log 0 = -\infty$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP.borel_upper_bound`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#borel-upper-bound).

## Large deviation bounds for arbitrary sets

Let $X$ be a topological space with a
$\sigma$-algebra in which every open set is measurable, and let $(\mu_n)_{n \in \mathbb{N}}$ be
measures on $X$ satisfying the large deviation principle with rate function
$I : X \to [0, \infty]$. Then for every set $\Gamma \subseteq X$, not necessarily measurable (for
non-measurable $\Gamma$, $\mu_n(\Gamma)$ is its outer measure), with interior $\Gamma^\circ$ and
closure $\overline{\Gamma}$, both

$$-\inf_{x \in \Gamma^\circ} I(x) \le \liminf_{n \to \infty} \frac{1}{n} \log \mu_n(\Gamma)$$

and

$$\limsup_{n \to \infty} \frac{1}{n} \log \mu_n(\Gamma) \le -\inf_{x \in \overline{\Gamma}} I(x)$$

hold, computed in the extended reals with $\log 0 = -\infty$. In particular the bounds hold for
every Borel set $\Gamma$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.SatisfiesLDP.borel_bounds`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#borel-bounds).

## Large deviation principle from bounds on measurable sets

Let $X$ be a topological space
with a $\sigma$-algebra containing every open set, let $(\mu_n)_{n \in \mathbb{N}}$ be a sequence
of measures on $X$, and let $I$ be a rate function on $X$. Suppose that every measurable set
$\Gamma \subseteq X$, with interior $\Gamma^\circ$ and closure $\overline{\Gamma}$, satisfies

$$\liminf_{n \to \infty} \frac{1}{n} \log \mu_n(\Gamma) \ge -\inf_{x \in \Gamma^\circ} I(x)$$

and

$$\limsup_{n \to \infty} \frac{1}{n} \log \mu_n(\Gamma) \le -\inf_{x \in \overline{\Gamma}} I(x),$$

where $\log 0 = -\infty$, an infimum over the empty set is $\infty$, and the limits are taken in
the extended reals. Then $(\mu_n)$ satisfies the large deviation principle with rate function $I$.

Open and closed sets are measurable and equal to their interior and closure respectively, so the
hypothesis contains the open-set and closed-set bounds. On a Borel space this is the textbook
Borel-set converse.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.satisfiesLDP_of_borel_bounds`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#satisfies-ldp-of-borel-bounds).

## Rate function of a Dirac mass

For a point $x_0$ of a set $X$, the Dirac rate function
at $x_0$ is the function $X \to [0, \infty]$ that equals $0$ at $x_0$ and $\infty$ at every other
point.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.diracRate`, a definition declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#dirac-rate).

## The Dirac rate function vanishes at its center

For every point $x_0$ of a set $X$, the
Dirac rate function at $x_0$ takes the value $0$ at $x_0$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.diracRate_apply_self`, a lemma declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#dirac-rate-apply-self).

## The Dirac rate function is infinite away from its center

For points $x \ne x_0$ of a set
$X$, the Dirac rate function at $x_0$ takes the value $\infty$ at $x$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.diracRate_apply_of_ne`, a lemma declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#dirac-rate-apply-of-ne).

## Infimum of the Dirac rate function over a set containing the center

For a point $x_0$ of
a set $X$ and a subset $s \subseteq X$ with $x_0 \in s$, the infimum over $x \in s$ of the Dirac
rate function at $x_0$, evaluated at $x$, is $0$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.iInf_diracRate_of_mem`, a lemma declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#i-inf-dirac-rate-of-mem).

## Infimum of the Dirac rate function over a set avoiding the center

For a point $x_0$ of a
set $X$ and a subset $s \subseteq X$ with $x_0 \notin s$, the infimum over $x \in s$ of the Dirac
rate function at $x_0$, evaluated at $x$, is $\infty$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.iInf_diracRate_of_notMem`, a lemma declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#i-inf-dirac-rate-of-not-mem).

## Log-scaled Dirac mass of a set containing the center

Let $X$ be a measurable space, let
$\delta_{x_0}$ be the Dirac measure at a point $x_0 \in X$, and let $s \subseteq X$ be a set with
$x_0 \in s$. Then $\frac{1}{n} \log \delta_{x_0}(s) = 0$ in the extended reals for every natural
number $n$, the factor $1/n$ being read as $0$ when $n = 0$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.dirac_ldp_term_eq_zero_of_mem`, a lemma declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#dirac-ldp-term-eq-zero-of-mem).

## Log-scaled Dirac mass of a set avoiding the center

Let $X$ be a measurable space in which
every singleton is measurable, let $\delta_{x_0}$ be the Dirac measure at a point $x_0 \in X$, and
let $s \subseteq X$ be a set with $x_0 \notin s$. Then for every natural number $n \ge 1$,
$\frac{1}{n} \log \delta_{x_0}(s) = -\infty$ in the extended reals, with $\log 0 = -\infty$.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.dirac_ldp_term_eq_bot_of_notMem`, a lemma declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#dirac-ldp-term-eq-bot-of-not-mem).

## Large deviation principle for a Dirac mass

Let $X$ be a $T_1$ topological space equipped
with its Borel $\sigma$-algebra, and let $x_0 \in X$. The constant sequence of measures
$\mu_n = \delta_{x_0}$ satisfies the large deviation principle with the Dirac rate function of
$x_0$, which is $0$ at $x_0$ and $\infty$ elsewhere.

Indeed, the mass $1$ stays at $x_0$, so the exponential cost of a set is $0$ if it contains $x_0$
and $\infty$ otherwise.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.satisfiesLDP_dirac`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#satisfies-ldp-dirac).

## The absolute value is a good rate function

The function $x \mapsto |x|$, viewed as a map
$\mathbb{R} \to [0, \infty]$, is a good rate function on $\mathbb{R}$.

It is continuous, hence lower semicontinuous, and its sub-level sets at finite levels are closed
intervals (or the singleton $\{0\}$ for a negative level), hence compact.

Formalized by `MathlibExt.Probability.LargeDeviationPrinciple.isGoodRateFunction_abs`, a theorem declared in [MathlibExt/Probability/LargeDeviationPrinciple.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LargeDeviationPrinciple.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html#is-good-rate-function-abs).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large deviation principle](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/large-deviation-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/large-deviations/large-deviation-principle)
