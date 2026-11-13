---
declaration: section
origin: cited
lean: MathlibExt.Probability.ConvexSubGaussianComparison.IsOneSubGaussianTail, MathlibExt.Probability.ConvexSubGaussianComparison.ConvexDominated, MathlibExt.Probability.ConvexSubGaussianComparison.IsAdmissibleConstant, MathlibExt.Probability.ConvexSubGaussianComparison.comparisonConstant, MathlibExt.Probability.ConvexSubGaussianComparison.gaussianTailEnvelope, MathlibExt.Probability.ConvexSubGaussianComparison.one_le_of_isAdmissibleConstant, MathlibExt.Probability.ConvexSubGaussianComparison.one_le_comparisonConstant, MathlibExt.Probability.ConvexSubGaussianComparison.IsAdmissibleConstant.elim
statement: formalized
---

# Convex comparison under sub-Gaussian tails

24 results, 18 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html).

## Random variables with a 1-sub-Gaussian tail

Let $\mu$ be a probability measure on a
measurable space $\Omega$. A function $X : \Omega \to \mathbb{R}$ has a 1-sub-Gaussian tail when
it is measurable and integrable, has mean $\int X \, d\mu = 0$, and satisfies
$\mu\{\omega : |X(\omega)| > t\} \le 2 e^{-t^2/2}$ for every real $t \ge 0$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.IsOneSubGaussianTail`, a structure declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#is-one-sub-gaussian-tail).

## Convex domination

Let $\mu_X$ and $\mu_Y$ be measures on measurable spaces $\Omega_X$
and $\Omega_Y$, and let $X : \Omega_X \to \mathbb{R}$ and $Y : \Omega_Y \to \mathbb{R}$. Then $X$
(under $\mu_X$) is convexly dominated by $Y$ (under $\mu_Y$) when every convex function
$f : \mathbb{R} \to \mathbb{R}$ for which $f \circ X$ is $\mu_X$-integrable and $f \circ Y$ is
$\mu_Y$-integrable satisfies $\int f(X) \, d\mu_X \le \int f(Y) \, d\mu_Y$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.ConvexDominated`, a definition declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#convex-dominated).

## Admissible convex sub-Gaussian comparison constants

An extended nonnegative real
$C \in [0, \infty]$ is an admissible comparison constant when $0 < C < \infty$ and, for every
probability measure $\mu$ on a measurable space $\Omega$ and every function
$X : \Omega \to \mathbb{R}$ with a 1-sub-Gaussian tail under $\mu$, $X$ under $\mu$ is convexly
dominated by the function $g \mapsto \sqrt{C}\, g$ under the standard Gaussian measure
$\mathcal{N}(0, 1)$ on $\mathbb{R}$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.IsAdmissibleConstant`, a definition declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#is-admissible-constant).

## The convex sub-Gaussian comparison constant

The comparison constant is the infimum, in
$[0, \infty]$, of the set of admissible comparison constants $C$; it equals $\infty$ when no
admissible constant exists.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.comparisonConstant`, a definition declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#comparison-constant).

## The capped Gaussian tail envelope

For a real number $t$, the capped Gaussian tail
envelope at $t$ is $\min\{1, 2 e^{-t^2/2}\}$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.gaussianTailEnvelope`, a definition declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#gaussian-tail-envelope).

## Admissible comparison constants are at least one

Every admissible comparison constant
$C$ satisfies $C \ge 1$.

The proof applies the comparison to a standard Gaussian variable and the convex test function
$x \mapsto x^2$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.one_le_of_isAdmissibleConstant`, a theorem declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#one-le-of-is-admissible-constant).

## The comparison constant is at least one

The convex sub-Gaussian comparison constant is
at least $1$. This holds also when no admissible comparison constant exists, in which case the
constant is $\infty$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.one_le_comparisonConstant`, a theorem declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#one-le-comparison-constant).

## Admissible constants compare variables on every sample space

Let $C$ be an admissible
comparison constant, let $\mu$ be a probability measure on a measurable space $\Omega$, and let
$X : \Omega \to \mathbb{R}$ have a 1-sub-Gaussian tail. Then $X$ is convexly dominated by
$\sqrt{C}\,G$, where $G$ is a standard Gaussian random variable (the identity on $\mathbb{R}$
under the standard normal law $N(0, 1)$).

The definition of admissibility quantifies only over sample spaces in the lowest universe; this
form allows $\Omega$ in any universe, by pushing the law of $X$ forward to a probability measure
on $\mathbb{R}$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.IsAdmissibleConstant.elim`, a theorem declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#elim).

## Saturating the Gaussian tail envelope

Let $\mu$ be a measure on a measurable space
$\Omega$. A function $X : \Omega \to \mathbb{R}$ saturates the Gaussian tail when
$\mu\{\omega : |X(\omega)| > t\} = \min\{1, 2 e^{-t^2/2}\}$ for every real $t \ge 0$, that is,
its strict tails equal the capped Gaussian tail envelope.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparison.SaturatesGaussianTail`, a definition declared in [MathlibExt/Probability/ConvexSubGaussianComparison.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ConvexSubGaussianComparison.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#saturates-gaussian-tail).

## Standard Gaussian upper tail

For a real number $x$, the standard Gaussian upper tail at
$x$ is $Q(x) = \int_x^\infty \varphi(t)\,dt$, where $\varphi(t) = e^{-t^2/2}/\sqrt{2\pi}$ is the
standard Gaussian density.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.standardNormalTail`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#standard-normal-tail).

## The Davis–Power transition threshold

The transition threshold is the real number
$t_0 = \sqrt{2\log 2}$, where $\log$ is the natural logarithm.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.davisPowerT0`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-t0).

## The envelope integral $A$

Let $A = \int_0^\infty \min(1, 2e^{-t^2/2})\,dt$, the integral
over $[0, \infty)$ of the capped Gaussian tail envelope $t \mapsto \min(1, 2e^{-t^2/2})$.

This integral appears in equation (3) of Davis–Power (2026).

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.davisPowerA`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-a).

## Half the envelope integral, $B$

Let $B = A/2$, where
$A = \int_0^\infty \min(1, 2e^{-t^2/2})\,dt$ is the integral over $[0, \infty)$ of the capped
Gaussian tail envelope.

This constant appears in equation (3) of Davis–Power (2026).

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.davisPowerB`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-b).

## The function $h$ of Davis–Power

For real $x$, let
$h(x) = 2x e^{-x^2/2} + 2\int_x^\infty e^{-t^2/2}\,dt$.

This is equation (4) of Davis–Power (2026); the Davis–Power equation system uses $h$ only at
points above the transition threshold $\sqrt{2 \log 2}$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.davisPowerH`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-h).

## Parameter quadruples of the Davis–Power system

A parameter quadruple is a quadruple
$(a, p_0, z, c_0)$ of real numbers, the unknowns of the Davis–Power equation system. Being a
solution of the system is a separate condition.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.DavisPowerSolution`, a structure declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-solution).

## Valid solutions of the Davis–Power system

Let $\varphi(t) = e^{-t^2/2}/\sqrt{2\pi}$ be
the standard Gaussian density, $Q(x) = \int_x^\infty \varphi(t)\,dt$ its upper tail,
$t_0 = \sqrt{2\log 2}$ with $\log$ the natural logarithm,
$B = \frac{1}{2}\int_0^\infty \min(1, 2e^{-t^2/2})\,dt$ and
$h(x) = 2x e^{-x^2/2} + 2\int_x^\infty e^{-t^2/2}\,dt$. A quadruple $(a, p_0, z, c_0)$ of real
numbers is a valid solution of the Davis–Power system when $a > t_0$, $h(a) = B$,
$p_0 = 2e^{-a^2/2}$, $0 < p_0 < 1$, $Q(z) = p_0$ and $c_0 = B/\varphi(z)$.

These are equations (3)–(6) of Davis–Power (2026), with the domain conditions that select the
solution.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.DavisPowerSolution.IsValid`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#is-valid).

## Values of $c_0$ solving the Davis–Power system

Let $\varphi(t) = e^{-t^2/2}/\sqrt{2\pi}$
be the standard Gaussian density, $B = \frac12 \int_0^\infty \min(1, 2e^{-t^2/2})\,dt$ and
$h(x) = 2x e^{-x^2/2} + 2\int_x^\infty e^{-t^2/2}\,dt$. This is the set of reals $c_0$ for which
there are reals $a$, $p_0$, $z$ with $a > \sqrt{2 \log 2}$, $h(a) = B$, $p_0 = 2e^{-a^2/2}$,
$0 < p_0 < 1$, $\int_z^\infty \varphi(t)\,dt = p_0$ and $c_0 = B / \varphi(z)$.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.davisPowerC0Values`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-c0-values).

## The Davis–Power constant $c_0$

Let $\varphi(t) = e^{-t^2/2}/\sqrt{2\pi}$ be the standard
Gaussian density, $B = \frac12 \int_0^\infty \min(1, 2e^{-t^2/2})\,dt$ and
$h(x) = 2x e^{-x^2/2} + 2\int_x^\infty e^{-t^2/2}\,dt$. The constant $c_0$ is the infimum of the
set of reals $c$ for which there are reals $a$, $p_0$, $z$ with $a > \sqrt{2 \log 2}$, $h(a) = B$,
$p_0 = 2e^{-a^2/2}$, $0 < p_0 < 1$, $\int_z^\infty \varphi(t)\,dt = p_0$ and $c = B / \varphi(z)$.
The infimum of a set of reals that is empty or unbounded below is taken to be $0$.

If the system has exactly one solution $(a, p_0, z, c)$, then $c_0 = c$. The constant is defined
from the equation system, not from numerical data.

Formalized by `MathlibExt.Probability.ConvexSubGaussianComparisonWantedDavis.davisPowerC0`, a definition declared in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-c0).

## Existence and uniqueness for the Davis–Power system

There is exactly one quadruple
$(a, p_0, z, c_0)$ of real numbers that is a valid solution of the Davis–Power system.

## Sources

- Davis–Power (2026), equations (3)–(6), existence and uniqueness.

Stated but not proved: `MathlibExt.Probability.ConvexSubGaussianComparisonWanted.davisPowerSystem_existsUnique` is written with `theorem_wanted` in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-system-exists-unique).

## Finiteness of the convex sub-Gaussian comparison constant

The comparison constant is
finite. Here the comparison constant is the infimum, in $[0, \infty]$, of the variance factors
$C \in (0, \infty)$ such that every real random variable $X$ on a probability space that is
integrable, has mean zero and satisfies $P(|X| > t) \le 2e^{-t^2/2}$ for all $t \ge 0$ satisfies
$E f(X) \le E f(\sqrt{C}\,G)$ for every convex $f : \mathbb{R} \to \mathbb{R}$ for which both
expectations are finite, where $G$ is a standard Gaussian. Equivalently, such a factor $C$ exists.

## Sources

- van Handel (2025), historical one-dimensional finiteness consequence.

Stated but not proved: `MathlibExt.Probability.ConvexSubGaussianComparisonWanted.historicalFinitenessUpperBound` is written with `theorem_wanted` in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#historical-finiteness-upper-bound).

## Davis–Power upper bound: $c_0^2$ is an admissible variance factor

Let $c_0$ be the
Davis–Power constant and $G$ a standard Gaussian. Then $c_0^2 > 0$, and every real random
variable $X$ on a probability space that is measurable and integrable, has mean $0$ and satisfies
$\mathbb{P}(|X| > t) \le 2e^{-t^2/2}$ for all $t \ge 0$ is dominated by $|c_0|\,G$ in the convex
order. Here a real random variable $X$ is dominated by $Y$ in the convex order when
$\mathbb{E} f(X) \le \mathbb{E} f(Y)$ for every convex $f : \mathbb{R} \to \mathbb{R}$ such that
$f(X)$ and $f(Y)$ are integrable.

## Sources

- Davis–Power (2026), Theorem 1, the exact `c0^2` comparator upper bound.

Stated but not proved: `MathlibExt.Probability.ConvexSubGaussianComparisonWanted.davisPowerSharpUpper` is written with `theorem_wanted` in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-sharp-upper).

## Davis–Power lower bound for admissible variance factors

Every admissible variance factor
$C \in [0, \infty]$ satisfies $c_0^2 \le C$, where $c_0$ is the Davis–Power constant. Here $C$ is
admissible when $0 < C < \infty$ and every real random variable $X$ on a probability space that
is measurable and integrable, has mean $0$ and satisfies $\mathbb{P}(|X| > t) \le 2e^{-t^2/2}$ for
all $t \ge 0$ is dominated by $\sqrt{C}\,G$ in the convex order, with $G$ a standard Gaussian;
a real random variable $X$ on a probability space is dominated by $Y$ in the convex order when
$\mathbb{E} f(X) \le \mathbb{E} f(Y)$ for every convex $f : \mathbb{R} \to \mathbb{R}$ such that
$f(X)$ and $f(Y)$ are integrable.

## Sources

- Davis–Power (2026), Theorem 1, sharpness for every admissible variance factor.

Stated but not proved: `MathlibExt.Probability.ConvexSubGaussianComparisonWanted.davisPowerSharpLower` is written with `theorem_wanted` in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-sharp-lower).

## Davis–Power value of the convex sub-Gaussian comparison constant

The convex
sub-Gaussian comparison constant, the infimum in $[0, \infty]$ of all admissible variance factors,
equals $c_0^2$, where $c_0$ is the Davis–Power constant.

## Sources

- Davis–Power (2026), the exact solved one-dimensional catalogue constant.

Stated but not proved: `MathlibExt.Probability.ConvexSubGaussianComparisonWanted.comparisonConstant_eq_davisPowerC0_sq` is written with `theorem_wanted` in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#comparison-constant-eq-davis-power-c0-sq).

## Davis–Power extremal variable

Let $c_0$ be the Davis–Power constant and $G$ a standard
Gaussian, and say that a real random variable $X$ is dominated by $Y$ in the convex order when
$\mathbb{E} f(X) \le \mathbb{E} f(Y)$ for every convex $f : \mathbb{R} \to \mathbb{R}$ such that
$f(X)$ and $f(Y)$ are integrable. There is a real random variable $X$ on a probability space that
is measurable and integrable, has mean $0$ and satisfies $\mathbb{P}(|X| > t) \le 2e^{-t^2/2}$ for
all $t \ge 0$, whose tail saturates the capped envelope,
$\mathbb{P}(|X| > t) = \min(1, 2e^{-t^2/2})$ for every $t \ge 0$, and such that for every real $c$
with $0 < c < c_0$, $X$ is not dominated by $cG$ in the convex order.

## Sources

- Davis–Power (2026), the tail-saturating extremizer and smaller-factor sharpness.

Stated but not proved: `MathlibExt.Probability.ConvexSubGaussianComparisonWanted.davisPowerExtremalAttainment` is written with `theorem_wanted` in [WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ConvexSubGaussianComparisonWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html#davis-power-extremal-attainment).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convex comparison under sub-Gaussian tails](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/concentration-inequalities/convex-comparison-under-sub-gaussian-tails)
