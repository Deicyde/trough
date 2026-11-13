---
declaration: section
origin: cited
lean: MathlibExt.Probability.BerryEsseenWanted.berry_esseen_finsetSum_gaussian, MathlibExt.Probability.BerryEsseenWanted.berry_esseen_explicit, MathlibExt.Probability.BerryEsseenWanted.berry_esseen, BerryEsseenModel.IsStandardizedLaw, BerryEsseenModel.iidLaw, BerryEsseenModel.normalizedSum, BerryEsseenModel.normalizedLaw, BerryEsseenModel.normalCDF
statement: formalized
proof: formalized
---

# Berry–Esseen theorem

35 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html).

## Berry–Esseen bound for finite sums

Let $(\xi_j)_{j \in \mathbb{N}}$ be measurable, mutually
independent real random variables on a probability space, and let $s$ be a finite set of indices
such that for each $j \in s$ the variable $\xi_j$ has a finite third moment and mean
$\mathbb{E}[\xi_j] = 0$, and such that $\sum_{j \in s} \mathbb{E}[\xi_j^2] = 1$. Write $\Phi$
for the distribution function of the standard normal distribution. If $\gamma \ge 0$ is a real
number with $\sum_{j \in s} \mathbb{E}|\xi_j|^3 \le \gamma$, then for every real $z$,

$$\left|\mathbb{P}\left(\sum_{j \in s} \xi_j \le z\right) - \Phi(z)\right| \le 42\gamma.$$

Formalized by `MathlibExt.Probability.BerryEsseenWanted.berry_esseen_finsetSum_gaussian`, a theorem declared in [MathlibExt/Probability/BerryEsseen.lean, line 3441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseen.lean#L3441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#berry-esseen-finset-sum-gaussian).

## Berry–Esseen theorem with constant 42

Let $X_0, X_1, X_2, \dots$ be measurable, mutually
independent real random variables on a probability space, each with the same distribution as
$X_0$, where $X_0$ has a finite third moment, mean $\mathbb{E}[X_0] = 0$ and variance
$\sigma^2 = \operatorname{Var}(X_0) > 0$ with $\sigma > 0$. Write $\rho = \mathbb{E}|X_0|^3$,
$S_n = X_0 + \dots + X_{n-1}$, and $\Phi$ for the distribution function of the standard normal
distribution. Then for every $n \ge 1$ and every real $x$,

$$\left|\mathbb{P}\left(\frac{S_n}{\sqrt{n\sigma^2}} \le x\right) - \Phi(x)\right| \le
\frac{42\rho}{\sigma^3\sqrt{n}}.$$

Integrability of $X_0$ is not assumed separately, since on a probability space it follows from
the finite third moment.

Formalized by `MathlibExt.Probability.BerryEsseenWanted.berry_esseen_explicit`, a theorem declared in [MathlibExt/Probability/BerryEsseen.lean, line 3461](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseen.lean#L3461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#berry-esseen-explicit).

## Berry–Esseen theorem

There is a constant $C > 0$ with the following property. Let
$X_0, X_1, X_2, \dots$ be measurable, mutually independent real random variables on a probability
space, each with the same distribution as $X_0$, where $X_0$ is integrable and has a finite third
moment, mean $\mathbb{E}[X_0] = 0$ and variance $\sigma^2 = \operatorname{Var}(X_0) > 0$ with
$\sigma > 0$. Write $\rho = \mathbb{E}|X_0|^3$, $S_n = X_0 + \dots + X_{n-1}$, and $\Phi$ for the
distribution function of the standard normal distribution. Then for every $n \ge 1$ and every
real $x$,

$$\left|\mathbb{P}\left(\frac{S_n}{\sqrt{n\sigma^2}} \le x\right) - \Phi(x)\right| \le
\frac{C\rho}{\sigma^3\sqrt{n}}.$$

## Sources

- A. C. Berry, Trans. AMS 49 (1941), 122-136, DOI 10.2307/1990053; and C.-G. Esseen, Arkiv för Matematik, Astronomi och Fysik 28A no. 9 (1942), 1-19.

Formalized by `MathlibExt.Probability.BerryEsseenWanted.berry_esseen`, a theorem declared in [MathlibExt/Probability/BerryEsseen.lean, line 3633](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseen.lean#L3633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#berry-esseen).

## Standardized laws with finite third moment

A measure $\mu$ on $\mathbb{R}$ is a
standardized law when it is a probability measure with mean $\int x \, d\mu(x) = 0$ and variance
$1$, and has finite third absolute moment $\int |x|^3 \, d\mu(x) < \infty$.

Formalized by `BerryEsseenModel.IsStandardizedLaw`, a structure declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#is-standardized-law).

## I.i.d. product law

For a measure $\mu$ on $\mathbb{R}$, the i.i.d. product law of $\mu$ is
the measure on the sequence space $\mathbb{R}^{\mathbb{N}}$ that is the infinite product
$\mu^{\otimes \mathbb{N}}$ of countably many copies of $\mu$ when $\mu$ is a probability measure,
and the zero measure otherwise.

Formalized by `BerryEsseenModel.iidLaw`, a definition declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#iid-law).

## Normalized sum

For a positive integer $n$ and a real sequence
$\omega = (\omega_0, \omega_1, \dots)$, the normalized sum $S_n(\omega)$ is the sum of the first $n$
coordinates divided by $\sqrt{n}$: $S_n(\omega) = (\omega_0 + \dots + \omega_{n-1})/\sqrt{n}$.

Formalized by `BerryEsseenModel.normalizedSum`, a definition declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-sum).

## Law of the normalized sum

For a measure $\mu$ on $\mathbb{R}$ and a positive integer
$n$, the normalized law of $\mu$ at $n$ is the pushforward of the i.i.d. law of $\mu$ on
$\mathbb{R}^{\mathbb{N}}$ (the product measure $\mu^{\otimes \mathbb{N}}$ when $\mu$ is a
probability measure, and the zero measure otherwise) under the normalized sum
$\omega \mapsto (\omega_0 + \dots + \omega_{n-1})/\sqrt{n}$.

Formalized by `BerryEsseenModel.normalizedLaw`, a definition declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-law).

## Standard normal CDF

For $x \in \mathbb{R}$, $\Phi(x)$ is the value at $x$ of the
cumulative distribution function of the standard normal distribution $\mathcal{N}(0, 1)$, that
is, the probability that a standard normal random variable is at most $x$.

Formalized by `BerryEsseenModel.normalCDF`, a definition declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normal-cdf).

## Third absolute moment

The third absolute moment of a measure $\mu$ on $\mathbb{R}$ is the
real number $\int |x|^3 \, d\mu(x)$, taken to be $0$ when $x \mapsto |x|^3$ is not integrable
with respect to $\mu$.

This integrand is integrable whenever $\mu$ is a standardized law.

Formalized by `BerryEsseenModel.thirdMoment`, a definition declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#third-moment).

## Finite third absolute moment as an $L^3$ condition

For every measure $\mu$ on
$\mathbb{R}$, the identity function $x \mapsto x$ belongs to $L^3(\mu)$ if and only if
the function $x \mapsto |x|^3$ is $\mu$-integrable.

Formalized by `BerryEsseenModel.memLp_three_iff_integrable_absCube`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#mem-lp-three-iff-integrable-abs-cube).

## Kolmogorov error

For a measure $\mu$ on $\mathbb{R}$ and a positive integer $n$, the
Kolmogorov error of $\mu$ at $n$ is the real supremum
$\sup_{x \in \mathbb{R}} |F_{\mu,n}(x) - \Phi(x)|$, where $\Phi$ is the standard normal
cumulative distribution function and $F_{\mu,n}$ is Mathlib's cumulative distribution function
of the normalized law of $\mu$ at $n$. When $\mu$ is a probability measure, $F_{\mu,n}(x)$ is
the mass the normalized law gives to $(-\infty, x]$; otherwise the normalized law is the zero
measure and $F_{\mu,n}$ is a fixed but unspecified cumulative distribution function of some
probability measure, not the zero function.

The values $|F_{\mu,n}(x) - \Phi(x)|$ lie in $[0, 1]$, so the supremum is finite.

Formalized by `BerryEsseenModel.kolmogorovError`, a definition declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#kolmogorov-error).

## The i.i.d. product of a standardized law is a probability measure

If $\mu$ is a
standardized law on $\mathbb{R}$, then the i.i.d. product law of $\mu$ on $\mathbb{R}^{\mathbb{N}}$
is a probability measure.

Formalized by `BerryEsseenModel.iidLaw_probability`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#iid-law-probability).

## Measurability of the normalized sum

For every positive integer $n$, the map sending a real
sequence $\omega = (\omega_0, \omega_1, \dots)$ to $(\omega_0 + \dots + \omega_{n-1})/\sqrt{n}$ is
measurable with respect to the product $\sigma$-algebra on $\mathbb{R}^{\mathbb{N}}$.

Formalized by `BerryEsseenModel.normalizedSum_measurable`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-sum-measurable).

## The normalized law is a probability measure

For every standardized law $\mu$ on
$\mathbb{R}$ (a probability measure with mean $0$, variance $1$ and finite third absolute
moment) and every positive integer $n$, the normalized law of $\mu$ at $n$ is a probability
measure.

Formalized by `BerryEsseenModel.normalizedLaw_probability`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-law-probability).

## Coordinates of the i.i.d. product are independent

If $\mu$ is a standardized law on
$\mathbb{R}$, then the coordinate maps $\omega \mapsto \omega_i$ on $\mathbb{R}^{\mathbb{N}}$, for
$i \in \mathbb{N}$, are mutually independent under the i.i.d. product law of $\mu$.

Formalized by `BerryEsseenModel.iidLaw_independent`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#iid-law-independent).

## Coordinate laws of the i.i.d. product

If $\mu$ is a standardized law on $\mathbb{R}$ and
$i$ is a natural number, then the pushforward of the i.i.d. product law of $\mu$ under the
coordinate map $\omega \mapsto \omega_i$ from $\mathbb{R}^{\mathbb{N}}$ to $\mathbb{R}$ is $\mu$.

Formalized by `BerryEsseenModel.iidLaw_map_eval`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#iid-law-map-eval).

## Coordinates of the i.i.d. product are distributed like the original law

Let $\mu$ be a
standardized law on $\mathbb{R}$ and let $i$ be a natural number. The coordinate map
$\omega \mapsto \omega_i$ on $\mathbb{R}^{\mathbb{N}}$ under the i.i.d. product law of $\mu$ and
the identity map of $\mathbb{R}$ under $\mu$ are identically distributed.

Formalized by `BerryEsseenModel.iidLaw_identDistrib`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#iid-law-ident-distrib).

## CDF of the normalized sum

Let $\mu$ be a standardized law on $\mathbb{R}$
(a probability measure with mean $0$, variance $1$ and finite third absolute moment), let $n$ be
a positive integer and let $x \in \mathbb{R}$. Then the cumulative distribution function of the
normalized law of $\mu$ at $n$, evaluated at $x$, equals the probability under the i.i.d. law
$\mu^{\otimes \mathbb{N}}$ on $\mathbb{R}^{\mathbb{N}}$ of the event
$\{\omega \in \mathbb{R}^{\mathbb{N}} : (\omega_0 + \dots + \omega_{n-1})/\sqrt{n} \le x\}$.

Formalized by `BerryEsseenModel.normalized_cdf_eq`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-cdf-eq).

## Standardized laws have an integrable third absolute moment

If $\mu$ is a standardized law
on $\mathbb{R}$, then the function $x \mapsto |x|^3$ is integrable with respect to $\mu$.

Formalized by `BerryEsseenModel.thirdMoment_integrable`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#third-moment-integrable).

## Nonnegativity of the third absolute moment

For every measure $\mu$ on $\mathbb{R}$, the
third absolute moment $\int_{\mathbb{R}} |x|^3 \, d\mu(x)$ is nonnegative.

As a real number, this integral is taken to be $0$ when $|x|^3$ is not $\mu$-integrable.

Formalized by `BerryEsseenModel.thirdMoment_nonnegative`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#third-moment-nonnegative).

## The third absolute moment of a standardized law is positive

If $\mu$ is a standardized
law on $\mathbb{R}$, that is, a probability measure with mean $0$, variance $1$ and finite third
absolute moment, then its third absolute moment $\int |x|^3 \, d\mu(x)$ is strictly positive.

The variance condition is what excludes a zero third absolute moment.

Formalized by `BerryEsseenModel.thirdMoment_positive`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#third-moment-positive).

## The CDF error is at most one

Let $\mu$ be a measure on $\mathbb{R}$, $n$ a positive integer
and $x$ a real number. Let $F_{\mu,n}$ be the distribution function of the normalized law of $\mu$
at $n$ and $\Phi$ the standard normal distribution function. Then $|F_{\mu,n}(x) - \Phi(x)| \le 1$.

No assumption is made on $\mu$: both distribution functions take values in $[0, 1]$.

Formalized by `BerryEsseenModel.pointwise_error_le_one`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#pointwise-error-le-one).

## The CDF errors are bounded above

Let $\mu$ be a measure on $\mathbb{R}$, let $n$ be a
positive integer, let $F$ be the cumulative distribution function of the normalized law of $\mu$
at $n$, and let $\Phi$ be the standard normal cumulative distribution function. Then the set
$\{|F(x) - \Phi(x)| : x \in \mathbb{R}\}$ is bounded above.

Formalized by `BerryEsseenModel.errorRange_bddAbove`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#error-range-bdd-above).

## Each CDF error is at most the Kolmogorov error

Let $\mu$ be a measure on $\mathbb{R}$,
$n$ a positive integer, $F_{\mu,n}$ the distribution function of the normalized law of $\mu$ at
$n$ and $\Phi$ the standard normal distribution function. Then for every real $x$,
$|F_{\mu,n}(x) - \Phi(x)| \le \sup_{y \in \mathbb{R}} |F_{\mu,n}(y) - \Phi(y)|$, the right side
being the Kolmogorov error of $\mu$ at $n$.

Formalized by `BerryEsseenModel.pointwise_le_kolmogorovError`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#pointwise-le-kolmogorov-error).

## The Kolmogorov error is nonnegative

For every measure $\mu$ on $\mathbb{R}$ and every
positive integer $n$, the Kolmogorov error of $\mu$ at $n$, that is
$\sup_{x \in \mathbb{R}} |F_{\mu,n}(x) - \Phi(x)|$ where $F_{\mu,n}$ is Mathlib's cumulative
distribution function of the normalized law of $\mu$ at $n$ and $\Phi$ is the standard normal
cumulative distribution function, is nonnegative.

Here $F_{\mu,n}(x)$ is the mass the normalized law gives to $(-\infty, x]$ when $\mu$ is a
probability measure; otherwise the normalized law is the zero measure and $F_{\mu,n}$ is a
fixed but unspecified cumulative distribution function of some probability measure.

Formalized by `BerryEsseenModel.kolmogorovError_nonnegative`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#kolmogorov-error-nonnegative).

## The Kolmogorov error is at most one

For every measure $\mu$ on $\mathbb{R}$ and every
positive integer $n$, the Kolmogorov error of $\mu$ at $n$, that is
$\sup_{x \in \mathbb{R}} |F_{\mu,n}(x) - \Phi(x)|$ where $F_{\mu,n}$ is Mathlib's cumulative
distribution function of the normalized law of $\mu$ at $n$ and $\Phi$ is the standard normal
cumulative distribution function, is at most $1$.

Here $F_{\mu,n}(x)$ is the mass the normalized law gives to $(-\infty, x]$ when $\mu$ is a
probability measure; otherwise the normalized law is the zero measure and $F_{\mu,n}$ is a
fixed but unspecified cumulative distribution function of some probability measure.

Formalized by `BerryEsseenModel.kolmogorovError_le_one`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#kolmogorov-error-le-one).

## Kolmogorov error bounds are uniform CDF bounds

Let $\mu$ be a measure on $\mathbb{R}$, let
$n$ be a positive integer, let $F$ be the cumulative distribution function of the normalized law
of $\mu$ at $n$, and let $\Phi$ be the standard normal cumulative distribution function. Then for
every real $a$, the Kolmogorov error of $\mu$ at $n$ is at most $a$ if and only if
$|F(x) - \Phi(x)| \le a$ for every real $x$.

Formalized by `BerryEsseenModel.error_le_iff`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#error-le-iff).

## The standard Gaussian is a standardized law

The standard normal law $N(0,1)$ on
$\mathbb{R}$ is a standardized law: it is a probability measure with mean $0$, variance $1$ and
finite third absolute moment.

Formalized by `BerryEsseenModel.standardGaussian_isStandardized`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#standard-gaussian-is-standardized).

## The normalized law with one summand

For every standardized law $\mu$ on $\mathbb{R}$
(a probability measure with mean $0$, variance $1$ and finite third absolute moment), the
normalized law of $\mu$ at $n = 1$ is $\mu$ itself.

Formalized by `BerryEsseenModel.normalizedLaw_one`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-law-one).

## The Kolmogorov error vanishes for one standard Gaussian summand

Let $F$ be the distribution
function of the normalized law of the standard normal law $N(0,1)$ at $n = 1$, and $\Phi$ the
standard normal distribution function. Then the Kolmogorov error of $N(0,1)$ at $n = 1$,
$\sup_{x \in \mathbb{R}} |F(x) - \Phi(x)|$, equals $0$.

Formalized by `BerryEsseenModel.standardGaussian_error_one`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#standard-gaussian-error-one).

## Standardized i.i.d. models

Let $\Omega$ be a measurable space with a measure $P$, and let
$(X_i)_{i \in \mathbb{N}}$ be real-valued functions on $\Omega$. They form a standardized i.i.d.
model when $P$ is a probability measure, every $X_i$ is measurable, the $X_i$ are mutually
independent under $P$, every $X_i$ has the same law under $P$ as $X_0$, and $X_0$ has mean
$\int_\Omega X_0 \, dP = 0$, variance $1$ and finite third absolute moment
$\int_\Omega |X_0|^3 \, dP < \infty$.

Formalized by `BerryEsseenModel.IsIIDModel`, a structure declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#is-iidmodel).

## The common law of an i.i.d. model is standardized

Let $P$ be a measure on a measurable
space $\Omega$ and $X_0, X_1, \dots$ real-valued functions on $\Omega$ forming an i.i.d. model:
$P$ is a probability measure, the $X_i$ are measurable, independent and identically distributed,
and $X_0$ has mean $0$, variance $1$ and finite third absolute moment. Then the law of $X_0$, the
pushforward of $P$ under $X_0$, is a standardized law.

Formalized by `BerryEsseenModel.IsIIDModel.standardizedLaw`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#standardized-law).

## The joint law of a standardized i.i.d. model

If $(X_i)_{i \in \mathbb{N}}$ is a
standardized i.i.d. model on a measurable space $\Omega$ with measure $P$, then the law under $P$
of the sequence map $\omega \mapsto (X_i(\omega))_{i \in \mathbb{N}}$ from $\Omega$ to
$\mathbb{R}^{\mathbb{N}}$ equals the i.i.d. product law of the law of $X_0$ under $P$.

Formalized by `BerryEsseenModel.IsIIDModel.jointLaw`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#joint-law).

## Normalized sums of an i.i.d. model have the canonical law

Let $P$ be a probability
measure on a measurable space $\Omega$ and let $X_0, X_1, \dots$ be real random variables on
$\Omega$ that are measurable, independent and identically distributed under $P$, with $X_0$ of
mean $0$, variance $1$ and finite third absolute moment. Then for every positive integer $n$,
the law under $P$ of $(X_0 + \dots + X_{n-1})/\sqrt{n}$ equals the normalized law at $n$ of the
law of $X_0$.

Formalized by `BerryEsseenModel.IsIIDModel.normalizedLaw_eq`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#normalized-law-eq).

## Third absolute moment of the common law

Let $P$ be a measure on a measurable space $\Omega$
and $X_0, X_1, \dots$ real-valued functions on $\Omega$ forming an i.i.d. model: $P$ is a
probability measure, the $X_i$ are measurable, independent and identically distributed, and $X_0$
has mean $0$, variance $1$ and finite third absolute moment. Then the third absolute moment of the
law of $X_0$ equals $\int_\Omega |X_0(\omega)|^3 \, dP(\omega)$.

Formalized by `BerryEsseenModel.IsIIDModel.thirdMoment_eq`, a theorem declared in [MathlibExt/Probability/BerryEsseenModel.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/BerryEsseenModel.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html#third-moment-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Berry–Esseen theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/berry-esseen-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/central-limit-theorems/berry-esseen-theorem)
