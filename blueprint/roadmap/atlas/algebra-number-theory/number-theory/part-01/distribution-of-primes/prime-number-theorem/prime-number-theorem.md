---
declaration: section
origin: cited
lean: Nat.Primes.logDirichletSeries, Nat.Primes.logDirichletCorrectionTerm, Nat.Primes.logDirichletCorrection, Nat.Primes.logDirichletContinuation, Nat.Primes.logDirichletCorrection_analyticOn, Nat.Primes.logDirichlet_vonMangoldt_split, Nat.Primes.logDirichletSeries_eq, Nat.Primes.riemannZeta₁_ne_zero_of_one_le_re
statement: formalized
proof: formalized
---

# Prime number theorem

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html).

## Prime logarithmic Dirichlet series

For a complex number $s$, the prime logarithmic
Dirichlet series is $\Phi(s) = \sum_{p} \frac{\log p}{p^s}$, summed over all primes $p$ (the sum
is taken to be $0$ where the family is not summable).

Formalized by `Nat.Primes.logDirichletSeries`, a definition declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-series).

## Summand of the prime-power correction series

For a prime $p$, a natural number $k$ and a
complex number $s$, the correction summand is $\frac{\log p}{(p^{k+2})^s}$, the term of the
prime-power correction series that belongs to the prime power $p^{k+2}$.

Formalized by `Nat.Primes.logDirichletCorrectionTerm`, a definition declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-correction-term).

## Prime-power correction series

For a complex number $s$, the prime-power correction series
is $C(s) = \sum_{(p, k)} \frac{\log p}{(p^{k+2})^s}$, summed over all pairs of a prime $p$ and a
natural number $k \ge 0$ (the sum is taken to be $0$ where the family is not summable).

Formalized by `Nat.Primes.logDirichletCorrection`, a definition declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-correction).

## The canonical prime logarithmic continuation

For a complex number $s$, the prime
logarithmic continuation is $G(s) = -\frac{\zeta_1'(s)}{\zeta_1(s)} - C(s)$, where $\zeta_1$ is
the entire function with $\zeta_1(s) = (s - 1)\zeta(s)$ for $s \ne 1$ and $\zeta_1(1) = 1$, the
quotient is taken to be $0$ where $\zeta_1(s) = 0$, and $C$ is the prime-power correction series.

This function continues $\Phi(s) - \frac{1}{s-1}$ from $\operatorname{Re} s > 1$ to a meromorphic
function on $\operatorname{Re} s > 1/2$, where $\Phi$ is the prime logarithmic Dirichlet series.

Formalized by `Nat.Primes.logDirichletContinuation`, a definition declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-continuation).

## Analyticity of the prime-power correction series

The prime-power correction series
$C(s) = \sum_{(p, k)} \frac{\log p}{(p^{k+2})^s}$, summed over all primes $p$ and natural
numbers $k \ge 0$, is analytic at every point of the open half-plane
$\{s \in \mathbb{C} : \operatorname{Re} s > 1/2\}$.

Formalized by `Nat.Primes.logDirichletCorrection_analyticOn`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-correction-analytic-on).

## Splitting the von Mangoldt L-series over prime powers

For every complex number $s$
with $\operatorname{Re} s > 1$, the L-series $\sum_{n \ge 1} \Lambda(n) n^{-s}$ of the von
Mangoldt function $\Lambda$ equals $\Phi(s) + C(s)$, where $\Phi(s) = \sum_p \log p / p^s$ is
the prime logarithmic Dirichlet series, summed over all primes $p$, and
$C(s) = \sum_{(p, k)} \log p / (p^{k+2})^s$ is the higher-prime-power correction series, summed
over all pairs of a prime $p$ and a natural number $k \ge 0$.

Formalized by `Nat.Primes.logDirichlet_vonMangoldt_split`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-von-mangoldt-split).

## Prime logarithmic series via the logarithmic derivative of zeta

For every complex number
$s$ with $\operatorname{Re} s > 1$, $\Phi(s) = -\frac{\zeta'(s)}{\zeta(s)} - C(s)$, where $\Phi$
is the prime logarithmic Dirichlet series, $\zeta$ is the Riemann zeta function and $C$ is the
prime-power correction series.

Formalized by `Nat.Primes.logDirichletSeries_eq`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-series-eq).

## Nonvanishing of the Riemann zeta function times $s - 1$ on $\operatorname{Re} s \ge 1$

Let $\zeta$ be the Riemann zeta function and let $\zeta_1 \colon \mathbb{C} \to \mathbb{C}$ be
given by $\zeta_1(s) = (s - 1)\zeta(s)$ for $s \ne 1$ and $\zeta_1(1) = 1$. Then
$\zeta_1(s) \ne 0$ for every complex number $s$ with $\operatorname{Re} s \ge 1$.

Formalized by `Nat.Primes.riemannZeta₁_ne_zero_of_one_le_re`, a lemma declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#riemann-zeta-ne-zero-of-one-le-re).

## Meromorphy of the prime logarithmic continuation

The prime logarithmic continuation $G$
is meromorphic on the open half-plane $\{s \in \mathbb{C} : \operatorname{Re} s > 1/2\}$.

Formalized by `Nat.Primes.logDirichletContinuation_meromorphic`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-continuation-meromorphic).

## Analyticity of the prime logarithmic continuation

The prime logarithmic continuation
$G$ is analytic at every point of the closed half-plane
$\{s \in \mathbb{C} : \operatorname{Re} s \ge 1\}$.

Formalized by `Nat.Primes.logDirichletContinuation_analyticOn`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-continuation-analytic-on).

## The prime logarithmic continuation on the half-plane $\operatorname{Re} s > 1$

Let
$\Phi(s) = \sum_p \frac{\log p}{p^s}$ be the prime logarithmic Dirichlet series, summed over all
primes $p$, and let $G$ be the prime logarithmic continuation. Then
$G(s) = \Phi(s) - \frac{1}{s - 1}$ for every complex number $s$ with $\operatorname{Re} s > 1$.

Formalized by `Nat.Primes.logDirichletContinuation_agree`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-continuation-agree).

## Meromorphic continuation of the prime logarithmic Dirichlet series

Let
$\Phi(s) = \sum_p \frac{\log p}{p^s}$ be the prime logarithmic Dirichlet series. There is a
function $g : \mathbb{C} \to \mathbb{C}$ that is meromorphic on the open half-plane
$\operatorname{Re} s > 1/2$, analytic at every point of the closed half-plane
$\operatorname{Re} s \ge 1$, and satisfies $g(s) = \Phi(s) - \frac{1}{s-1}$ whenever
$\operatorname{Re} s > 1$.

## Sources

- NumberTheoryI Lemma 16.11.

Formalized by `Nat.Primes.logDirichlet_meromorphicContinuation`, a theorem declared in [MathlibExt/NumberTheory/LSeries/PrimeLog.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/LSeries/PrimeLog.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#log-dirichlet-meromorphic-continuation).

## Prime counting versus theta over log

Let $\pi(x)$ be the number of primes $p \le x$ and
let $\theta(x) = \sum_{p \le x} \log p$, the sum running over primes. As the real number $x$ tends
to $+\infty$,

$$\pi(x) - \frac{\theta(x)}{\log x} = o\left(\frac{x}{\log x}\right).$$

The proof upgrades the bound $\pi(x) - \theta(x)/\log x = O(x/(\log x)^2)$, using that
$x/(\log x)^2 = o(x/\log x)$.

Formalized by `Chebyshev.primeCounting_sub_theta_div_log_isLittleO`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#prime-counting-sub-theta-div-log-is-litt).

## Theta asymptotic implies the prime number theorem

Let $\pi(x)$ be the number of primes
$p \le x$ and let $\theta(x) = \sum_{p \le x} \log p$, the sum running over primes. If
$\theta(x) \sim x$ as the real number $x$ tends to $+\infty$, then $\pi(x) \sim x / \log x$ as
$x \to +\infty$.

Formalized by `Chebyshev.primeCounting_isEquivalent_of_theta_isEquivalent`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#prime-counting-is-equivalent-of-theta-is).

## Prime number theorem implies the theta asymptotic

Let $\pi(x)$ be the number of primes
$p \le x$ and let $\theta(x) = \sum_{p \le x} \log p$, the sum running over primes. If
$\pi(x) \sim x / \log x$ as the real number $x$ tends to $+\infty$, then $\theta(x) \sim x$ as
$x \to +\infty$.

Formalized by `Chebyshev.theta_isEquivalent_of_primeCounting_isEquivalent`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#theta-is-equivalent-of-prime-counting-is).

## Prime number theorem is equivalent to the theta asymptotic

Let $\pi(x)$ be the number of
primes $p \le x$ and let $\theta(x) = \sum_{p \le x} \log p$ be Chebyshev's theta function, the
sum running over primes. Then, as the real number $x$ tends to $+\infty$, $\pi(x) \sim x / \log x$
holds if and only if $\theta(x) \sim x$.

Formalized by `Chebyshev.primeCounting_isEquivalent_iff_theta_isEquivalent`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/Chebyshev.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#prime-counting-is-equivalent-iff-theta-i).

## The prime logarithm series

For $s \in \mathbb{C}$, the prime logarithm series at $s$
is the complex number $\sum_p \log p \cdot p^{-s}$, where the sum runs over all primes $p$ and
$p^{-s}$ is the complex power. The sum is unconditional and is taken to be $0$ by convention
when the family $(\log p \cdot p^{-s})_p$ is not summable.

## Sources

- ATLAS NumberTheoryI Lemma 16.10.

Formalized by `Chebyshev.primeLogSeries`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#prime-log-series).

## Laplace transform of $\theta(e^t)$

Let $\theta(x) = \sum_{p \le x} \log p$ be
Chebyshev's function, the sum running over the primes $p \le x$. For every $s \in \mathbb{C}$
with $\operatorname{Re} s > 1$, the Laplace transform
$\int_{(0, \infty)} e^{-st}\,\theta(e^t)\,dt$ of $t \mapsto \theta(e^t)$ at $s$ equals
$\frac{1}{s} \sum_p \log p \cdot p^{-s}$, the prime logarithm series at $s$ divided by $s$,
where the sum runs over all primes $p$.

## Sources

- ATLAS NumberTheoryI Lemma 16.10.

Formalized by `Chebyshev.laplace_theta_exp_eq_primeLogSeries_div`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#laplace-theta-exp-eq-prime-log-series-di).

## Convergence of the Laplace transform of $\theta(e^t)$

Let
$\theta(x) = \sum_{p \le x} \log p$ be Chebyshev's function, the sum running over the primes
$p \le x$. For every $s \in \mathbb{C}$ with $\operatorname{Re} s > 1$, the function
$t \mapsto \theta(e^t)$ has Laplace transform $\frac{1}{s} \sum_p \log p \cdot p^{-s}$ at $s$,
where the sum runs over all primes $p$ (this is the prime logarithm series at $s$ divided by
$s$): the function $t \mapsto e^{-st}\,\theta(e^t)$ is integrable on $(0, \infty)$ and its
integral over $(0, \infty)$ equals $\frac{1}{s} \sum_p \log p \cdot p^{-s}$.

## Sources

- ATLAS NumberTheoryI Lemma 16.10.

Formalized by `Chebyshev.hasLaplace_theta_exp`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#has-laplace-theta-exp).

## Holomorphy of the Laplace transform of $\theta(e^t)$

Let
$\theta(x) = \sum_{p \le x} \log p$ be Chebyshev's function, the sum running over the primes
$p \le x$. Then the Laplace transform $F(s) = \int_{(0, \infty)} e^{-st}\,\theta(e^t)\,dt$ of
$t \mapsto \theta(e^t)$ is complex differentiable at every point of the open half-plane
$\{s \in \mathbb{C} : \operatorname{Re} s > 1\}$, so it is holomorphic there.

## Sources

- ATLAS NumberTheoryI Lemma 16.10.

Formalized by `Chebyshev.differentiableOn_laplace_theta_exp`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceTheta.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#differentiable-on-laplace-theta-exp).

## The shifted log-Dirichlet continuation

Let $\Phi(s) = \sum_p \log p / p^s$, the sum over
primes, and let $g$ be the canonical continuation of $\Phi(s) - 1/(s - 1)$ to
$\operatorname{Re} s > 1/2$. For $s \in \mathbb{C}$, the shifted continuation is
$g_1(s) = g(s + 1)$.

Formalized by `Nat.Primes.shiftedLogDirichletContinuation`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#shifted-log-dirichlet-continuation).

## Meromorphy of the shifted continuation

The shifted continuation $g_1$ is meromorphic at
every point $s \in \mathbb{C}$ with $\operatorname{Re} s > -1/2$.

Formalized by `Nat.Primes.shiftedLogDirichletContinuation_meromorphic`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#shifted-log-dirichlet-continuation-merom).

## Holomorphy of the shifted continuation on the closed half-plane

The shifted
continuation $g_1$ is complex analytic at every point $s \in \mathbb{C}$ with
$\operatorname{Re} s \ge 0$.

Formalized by `Nat.Primes.shiftedLogDirichletContinuation_analyticOn`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#shifted-log-dirichlet-continuation-analy).

## The shifted continuation agrees with the shifted series

Let
$\Phi(s) = \sum_p \log p / p^s$ be the prime logarithmic Dirichlet series and $g_1$ the shifted
continuation. For every $s \in \mathbb{C}$ with $\operatorname{Re} s > 0$,
$g_1(s) = \Phi(s + 1) - 1/s$.

Formalized by `Nat.Primes.shiftedLogDirichletContinuation_agree`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#shifted-log-dirichlet-continuation-agree).

## The normalized Chebyshev error

For real $t$, let $H(t) = \theta(e^t) e^{-t} - 1$, where
$\theta(x) = \sum_{p \le x} \log p$ is the Chebyshev function, the sum running over primes
$p \le x$.

Formalized by `Chebyshev.normalizedThetaError`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#normalized-theta-error).

## The normalized-error continuation

Let $\Phi(s) = \sum_p \log p / p^s$, the sum over
primes, let $g$ be the canonical continuation of $\Phi(s) - 1/(s - 1)$, and let
$g_1(s) = g(s + 1)$ be the shifted continuation. For $s \in \mathbb{C}$, the normalized-error
continuation is $F(s) = (g_1(s) - 1)/(s + 1)$, with $F(-1) = 0$ since division by zero gives $0$.

Formalized by `Chebyshev.normalizedThetaErrorContinuation`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#normalized-theta-error-continuation).

## Meromorphy of the normalized-error continuation

The normalized-error continuation $F$
is meromorphic at every point $s \in \mathbb{C}$ with $\operatorname{Re} s > -1/2$.

Formalized by `Chebyshev.normalizedThetaErrorContinuation_meromorphic`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#normalized-theta-error-continuation-mero).

## Holomorphy of the normalized-error continuation on the closed half-plane

The
normalized-error continuation $F$ is complex analytic at every point $s \in \mathbb{C}$ with
$\operatorname{Re} s \ge 0$.

Formalized by `Chebyshev.normalizedThetaErrorContinuation_analyticOn`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#normalized-theta-error-continuation-anal).

## Laplace transform of the normalized Chebyshev error

Let
$\theta(x) = \sum_{p \le x} \log p$ be the Chebyshev function (the sum over primes $p \le x$),
let $H(t) = \theta(e^t) e^{-t} - 1$ for real $t$ be the normalized Chebyshev error, viewed as a
complex-valued function, and let $F$ be the normalized-error continuation. For every
$s \in \mathbb{C}$ with $\operatorname{Re} s > 0$, the function $t \mapsto e^{-st} H(t)$ is
integrable on $(0, \infty)$ and $\int_{(0, \infty)} e^{-st} H(t)\,dt = F(s)$.

Formalized by `Chebyshev.hasLaplace_normalizedThetaError`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LaplaceThetaContinuation.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#has-laplace-normalized-theta-error).

## Measurability of the normalized theta error

Let $\theta(x) = \sum_{p \le x} \log p$ be
Chebyshev's function, the sum running over primes $p$. The normalized theta error
$H(t) = \theta(e^t)e^{-t} - 1$ is a Borel measurable function of $t \in \mathbb{R}$.

Formalized by `Chebyshev.measurable_normalizedThetaError`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/NormalizedThetaError.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/NormalizedThetaError.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#measurable-normalized-theta-error).

## Explicit bound for the normalized theta error

Let $\theta(x) = \sum_{p \le x} \log p$ be
Chebyshev's function, the sum running over primes $p$, and let $H(t) = \theta(e^t)e^{-t} - 1$ be
the normalized theta error. Then $|H(t)| \le \log 4 + 1$ for every real $t$.

The bound holds for all real $t$, not only for $t \ge 0$.

Formalized by `Chebyshev.abs_normalizedThetaError_le`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/NormalizedThetaError.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/NormalizedThetaError.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#abs-normalized-theta-error-le).

## Boundedness of the normalized theta error on $(0, \infty)$

Let
$\theta(x) = \sum_{p \le x} \log p$ be Chebyshev's function, the sum running over primes $p$, and
let $H(t) = \theta(e^t)e^{-t} - 1$ be the normalized theta error. There is a real number $M$ such
that $|H(t)| \le M$ for every real $t \ge 0$.

Formalized by `Chebyshev.normalizedThetaError_bounded`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/NormalizedThetaError.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/NormalizedThetaError.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#normalized-theta-error-bounded).

## Prime number theorem

Let $\pi(n)$ be the number of primes $p \le n$. Then
$\pi(n) \sim n / \log n$ as $n \to \infty$ through the natural numbers, that is,
$\pi(n) - n / \log n = o(n / \log n)$, where $\log$ is the natural logarithm.

## Sources

- J. Hadamard and C. de la Vallée Poussin, 1896 independent proofs of PNT; original: Hadamard, Sur la distribution des zéros de ζ, Bull. Soc. Math. France 24 (1896) 199–220, de la Vallée Poussin, Recherches analytiques, Ann. Soc. Sci. Bruxelles 20 (1896); textbook in Apostol, Introduction to Analytic Number Theory

Formalized by `MathlibExt.NumberTheory.PrimeNumberTheoremWanted.prime_number_theorem`, a theorem declared in [MathlibExt/NumberTheory/PrimeNumberTheorem.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeNumberTheorem.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html#prime-number-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime number theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/prime-number-theorem)
