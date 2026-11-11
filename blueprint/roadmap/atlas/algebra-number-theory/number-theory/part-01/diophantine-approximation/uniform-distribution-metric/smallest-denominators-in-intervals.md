---
declaration: section
origin: cited
lean: MetaMathlibExt.smallestDenominator, MetaMathlibExt.smallestDenominator_le, MetaMathlibExt.exists_denominator_mem_window, MetaMathlibExt.smallestDenominator_spec, MetaMathlibExt.not_mem_window_of_lt_smallestDenominator, MetaMathlibExt.smallestDenominator_le_iff, MetaMathlibExt.smallestDenominator_eq_one, MetaMathlibExt.logSmallestDenominatorDensity
statement: formalized
---

# Smallest denominators in intervals

12 results, 10 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html).

## Smallest denominator in an interval

For real numbers $x$ and $\delta$, the smallest
denominator $q_{\min}(x, \delta)$ is the least positive integer $q$ for which there is an integer
$p$ with $|x - p/q| < \delta/2$, that is, with $p/q$ in the open interval
$(x - \delta/2, x + \delta/2)$. If there is no such $q$, which happens only when $\delta \le 0$,
then $q_{\min}(x, \delta) = 0$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.smallestDenominator`, a definition declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#smallest-denominator).

## Denominators of nearby rationals bound the smallest denominator

Let $x$ and $\delta$ be
real numbers, let $q$ be a positive integer and let $p$ be an integer. If $|x - p/q| < \delta/2$,
then the smallest denominator satisfies $q_{\min}(x, \delta) \le q$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.smallestDenominator_le`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#smallest-denominator-le).

## Every real number has arbitrarily close rationals

For every real number $x$ and every
real $\delta > 0$ there are a positive integer $q$ and an integer $p$ with $|x - p/q| < \delta/2$.

Taking $q > 1/\delta$ and $p$ the integer nearest to $qx$ gives
$|x - p/q| \le 1/(2q) < \delta/2$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.exists_denominator_mem_window`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#exists-denominator-mem-window).

## The smallest denominator is positive and attained

For every real number $x$ and every
real $\delta > 0$, the smallest denominator $q = q_{\min}(x, \delta)$ is positive and there is an
integer $p$ with $|x - p/q| < \delta/2$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.smallestDenominator_spec`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#smallest-denominator-spec).

## Minimality of the smallest denominator

Let $x$ and $\delta$ be real numbers and let $q$
be a positive integer with $q < q_{\min}(x, \delta)$, where $q_{\min}(x, \delta)$ is the smallest
denominator. Then there is no integer $p$ with $|x - p/q| < \delta/2$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.not_mem_window_of_lt_smallestDenominator`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#not-mem-window-of-lt-smallest-denominato).

## Upper bounds on the smallest denominator

Let $x$ be a real number, let $\delta > 0$ be
real, let $q$ be a natural number and let $q_{\min}(x, \delta)$ be the smallest denominator. Then
$q_{\min}(x, \delta) \le q$ if and only if there are a positive integer $q' \le q$ and an integer
$p$ with $|x - p/q'| < \delta/2$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.smallestDenominator_le_iff`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#smallest-denominator-le-iff).

## Wide intervals have smallest denominator one

For every real number $x$ and every real
$\delta > 1$, the smallest denominator $q_{\min}(x, \delta)$ equals $1$.

The open interval $(x - \delta/2, x + \delta/2)$ has length greater than $1$, so it contains an
integer.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.1).

Formalized by `MetaMathlibExt.smallestDenominator_eq_one`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#smallest-denominator-eq-one).

## Density of the logarithmic smallest denominator

The function $\eta_{\log}$ on the real
line is defined by $\eta_{\log}(s) = \frac{6}{\pi^2} e^{2s}$ for $s \le 0$, by
$\eta_{\log}(s) = \frac{6}{\pi^2}\left(-e^{2s} + 2 + 4s\right)$ for $0 < s \le \log 2$, and by

$$
\eta_{\log}(s) = \frac{6}{\pi^2}\left(-e^{2s} + 2 + 2e^{2s}\sqrt{\tfrac14 - e^{-2s}} -
4\log\left(\tfrac12 + \sqrt{\tfrac14 - e^{-2s}}\right)\right)
$$

for $s > \log 2$.

In the cited paper, $\eta_{\log}$ is the density of the limit law, as $\delta \to 0^+$, of
$\log q_{\min}(x, \delta) + \frac12 \log \delta$ for uniformly random $x$, where
$q_{\min}(x, \delta)$ is the smallest denominator of a rational in $(x - \delta/2, x + \delta/2)$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.3).

Formalized by `MetaMathlibExt.logSmallestDenominatorDensity`, a definition declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#log-smallest-denominator-density).

## Value of the log smallest-denominator density at zero

The density $\eta_{\log}$ of the
logarithmic smallest denominator satisfies $\eta_{\log}(0) = 6/\pi^2$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.3).

Formalized by `MetaMathlibExt.logSmallestDenominatorDensity_zero`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#log-smallest-denominator-density-zero).

## The log smallest-denominator density for nonpositive arguments

For every real $s \le 0$,
the density $\eta_{\log}$ of the logarithmic smallest denominator satisfies
$\eta_{\log}(s) = \frac{6}{\pi^2} e^{2s}$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Equation (1.3).

Formalized by `MetaMathlibExt.logSmallestDenominatorDensity_of_nonpos`, a theorem declared in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#log-smallest-denominator-density-of-nonp).

## Limit law of the smallest denominator

For real $x$ and $\delta > 0$ let
$q_{\min}(x, \delta)$ be the smallest positive integer $q$ such that some rational $p/q$ lies in
the open interval $(x - \delta/2, x + \delta/2)$, and let $\eta_{\log}$ be the log smallest
denominator density. Then $\eta_{\log}$ is a probability density on $\mathbb{R}$:
$\eta_{\log}(s) \ge 0$ for every real $s$ and $\int_{-\infty}^{\infty} \eta_{\log}(s) \, ds = 1$.
Moreover, for all real numbers $a$, $b$, $L$ with $0 \le a \le b \le 1$, as $\delta \to 0^+$ the
Lebesgue measure of $\{x \in [a, b] : \log q_{\min}(x, \delta) > L - \tfrac12 \log \delta\}$
tends to $(b - a) \int_L^\infty \eta_{\log}(s) \, ds$.

The interval is taken closed; its endpoints do not affect the measures.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Proposition 1.

Stated but not proved: `MetaMathlibExt.tendsto_volume_log_smallestDenominator_gt` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#tendsto-volume-log-smallest-denominator).

## Convergence of the log moments of smallest denominators

Let $0 \le a \le b \le 1$ be
real numbers and let $n \ge 0$ be an integer. For real $x$ and $\delta > 0$ let
$q_{\min}(x, \delta)$ be the smallest positive integer $q$ such that some rational $p/q$ lies in
the open interval $(x - \delta/2, x + \delta/2)$, and let $\eta_{\log}$ be the log smallest
denominator density. Then, as $\delta \to 0^+$,

$$
\int_a^b \bigl(\log q_{\min}(x, \delta) + \tfrac12 \log \delta\bigr)^n \, dx \to \mu_n \, (b - a),
$$

where $\mu_n = \int_{-\infty}^{\infty} s^n \, \eta_{\log}(s) \, ds$.

The moment $\mu_n$ is an integral over the whole real line: $\eta_{\log}$ has mass $3/\pi^2$ on
$(-\infty, 0]$, so integrating only over $s \ge 0$ would give $\mu_0 = 1 - 3/\pi^2$ instead of
the correct limit $1$.

## Sources

- Jens Marklof, *The Log Moments of Smallest Denominators*, INTEGERS 24 (2024), Article A55, Proposition 2.

Stated but not proved: `MetaMathlibExt.tendsto_integral_log_smallestDenominator_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SmallestDenominatorLogMomentsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html#tendsto-integral-log-smallest-denominato).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smallest denominators in intervals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/smallest-denominators-in-intervals)
