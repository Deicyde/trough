---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Sampling.mcEstimate, Cslib.MachineLearning.Sampling.integral_mcEstimate, Cslib.MachineLearning.Sampling.tendsto_mcEstimate, Cslib.MachineLearning.Sampling.isEstimate, Cslib.MachineLearning.Sampling.integral_weight_mul, Cslib.MachineLearning.Sampling.integral_isEstimate, Cslib.MachineLearning.Sampling.tendsto_isEstimate
statement: formalized
proof: formalized
---

# Monte Carlo and importance sampling

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html).

## Monte Carlo estimate

Given a function $f : \alpha \to \mathbb{R}$ and samples
$X_0, X_1, \ldots : \Omega \to \alpha$, the Monte Carlo estimate from the first $n$ samples at
$\omega \in \Omega$ is $\frac{1}{n} \sum_{i < n} f(X_i(\omega))$, which is $0$ when $n = 0$.

Formalized by `Cslib.MachineLearning.Sampling.mcEstimate`, a definition declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#mc-estimate).

## The Monte Carlo estimator is unbiased

Let $\mu$ be a measure on $\Omega$, let $\nu$ be a
measure on $\alpha$, and let $f : \alpha \to \mathbb{R}$ be measurable and integrable with respect
to $\nu$. If $X_0, X_1, \ldots : \Omega \to \alpha$ are measurable and the pushforward of $\mu$
along each $X_i$ is $\nu$, then for every $n \ne 0$ the integral with respect to $\mu$ of the
Monte Carlo estimate $\frac{1}{n} \sum_{i < n} f(X_i)$ equals $\int f \, d\nu$.

Formalized by `Cslib.MachineLearning.Sampling.integral_mcEstimate`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#integral-mc-estimate).

## The Monte Carlo estimator is consistent

**The Monte Carlo estimator is consistent** (strong law of large numbers). Let $\mu$ be a
measure on $\Omega$, let $\nu$ be a measure on $\alpha$, and let $f : \alpha \to \mathbb{R}$ be
measurable and integrable with respect to $\nu$. If $X_0, X_1, \ldots : \Omega \to \alpha$ are
measurable, pairwise independent under $\mu$, and the pushforward of $\mu$ along each $X_i$ is
$\nu$, then for $\mu$-almost every $\omega$ the Monte Carlo estimate
$\frac{1}{n} \sum_{i < n} f(X_i(\omega))$ converges to $\int f \, d\nu$ as $n \to \infty$.

Formalized by `Cslib.MachineLearning.Sampling.tendsto_mcEstimate`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#tendsto-mc-estimate).

## Importance-sampling estimate

Given a weight $w : \alpha \to [0, \infty]$, a function
$f : \alpha \to \mathbb{R}$ and samples $X_0, X_1, \ldots : \Omega \to \alpha$, the
importance-sampling estimate from the first $n$ samples at $\omega \in \Omega$ is
$\frac{1}{n} \sum_{i < n} w(X_i(\omega)) \, f(X_i(\omega))$, where an infinite weight counts as
$0$ and the estimate is $0$ when $n = 0$. If the samples are drawn from a proposal measure
$\rho$, it estimates $\int f \, d\nu$ for the target measure $\nu$ with density $w$ with respect to
$\rho$.

Formalized by `Cslib.MachineLearning.Sampling.isEstimate`, a definition declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#is-estimate).

## Change of measure for importance weights

Let $\rho$ be a measure on $\alpha$, let
$w : \alpha \to [0, \infty]$ be measurable with $w < \infty$ $\rho$-almost everywhere, and let
$\nu$ be the measure with density $w$ with respect to $\rho$. Then for every function
$f : \alpha \to \mathbb{R}$, $\int w f \, d\rho = \int f \, d\nu$.

Formalized by `Cslib.MachineLearning.Sampling.integral_weight_mul`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#integral-weight-mul).

## Importance sampling is unbiased

Let $\mu$ be a measure on $\Omega$, let $\rho$ be a
measure on $\alpha$, let $w : \alpha \to [0, \infty]$ be measurable with $w < \infty$
$\rho$-almost everywhere, and let $\nu$ be the measure with density $w$ with respect to $\rho$.
Let $f : \alpha \to \mathbb{R}$ be measurable and integrable with respect to $\nu$. If
$X_0, X_1, \ldots : \Omega \to \alpha$ are measurable and the pushforward of $\mu$ along each
$X_i$ is $\rho$, then for every $n \ne 0$ the integral with respect to $\mu$ of the
importance-sampling estimate of $f$ with weight $w$ from the first $n$ samples equals
$\int f \, d\nu$.

Formalized by `Cslib.MachineLearning.Sampling.integral_isEstimate`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#integral-is-estimate).

## Importance sampling is consistent

Let $\mu$ be a measure on $\Omega$, let $\rho$ be a
measure on $\alpha$, let $w : \alpha \to [0, \infty]$ be measurable with $w < \infty$
$\rho$-almost everywhere, and let $\nu$ be the measure with density $w$ with respect to $\rho$.
Let $f : \alpha \to \mathbb{R}$ be measurable and integrable with respect to $\nu$. If
$X_0, X_1, \ldots : \Omega \to \alpha$ are measurable, pairwise independent under $\mu$, and the
pushforward of $\mu$ along each $X_i$ is $\rho$, then for $\mu$-almost every $\omega$ the
importance-sampling estimate of $f$ with weight $w$ from the first $n$ samples at $\omega$
converges to $\int f \, d\nu$ as $n \to \infty$.

Formalized by `Cslib.MachineLearning.Sampling.tendsto_isEstimate`, a theorem declared in [CSLibExt/MachineLearning/Sampling/MonteCarlo.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Sampling/MonteCarlo.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html#tendsto-is-estimate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monte Carlo and importance sampling](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/monte-carlo-and-importance-sampling)
