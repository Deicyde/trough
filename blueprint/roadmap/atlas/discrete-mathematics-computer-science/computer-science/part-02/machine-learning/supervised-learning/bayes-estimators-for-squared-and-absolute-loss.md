---
declaration: section
origin: cited
lean: Cslib.MachineLearning.OptimalPredictors.sqLoss, Cslib.MachineLearning.OptimalPredictors.lintegral_sqLoss_integral_le, Cslib.MachineLearning.OptimalPredictors.posteriorMean, Cslib.MachineLearning.OptimalPredictors.IsPosteriorMean, Cslib.MachineLearning.OptimalPredictors.IsPosteriorMean.isBayesEstimator, Cslib.MachineLearning.OptimalPredictors.absLoss, Cslib.MachineLearning.OptimalPredictors.lintegral_absLoss_le_of_isMedian, Cslib.MachineLearning.OptimalPredictors.IsPosteriorMedian
statement: formalized
proof: formalized
---

# Bayes estimators for squared and absolute loss

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html).

## Posterior means for squared loss

## Squared loss

The squared loss of predicting $y \in \mathbb{R}$ when the true value is
$\theta \in \mathbb{R}$ is $(\theta - y)^2$, regarded as an element of $[0, \infty]$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.sqLoss`, a definition declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#sq-loss).

## The mean minimizes the expected squared loss

Let $\nu$ be a probability measure on
$\mathbb{R}$ with mean $m = \int t \, d\nu(t)$ (taken to be $0$ when $\nu$ has no finite first
moment). Then for every $y \in \mathbb{R}$,

$$\int (\theta - m)^2 \, d\nu(\theta) \le \int (\theta - y)^2 \, d\nu(\theta),$$

where both integrals are taken in $[0, \infty]$.

When the right side is infinite the inequality is trivial; otherwise $\nu$ has a second moment and
the variance decomposition applies.

Formalized by `Cslib.MachineLearning.OptimalPredictors.lintegral_sqLoss_integral_le`, a theorem declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#lintegral-sq-loss-integral-le).

## Posterior mean

Let $P$ be a finite kernel from $\mathbb{R}$ to a measurable space
$\mathcal{X}$, let $\pi$ be a finite measure on $\mathbb{R}$, and write $P^\dagger\pi$ for the
posterior kernel from $\mathcal{X}$ to $\mathbb{R}$. The posterior mean is the function on
$\mathcal{X}$ sending $x$ to $\int \theta \, d(P^\dagger\pi)(x)(\theta)$, the mean of the posterior
distribution given the observation $x$ (taken to be $0$ when that distribution has no finite
first moment).

Formalized by `Cslib.MachineLearning.OptimalPredictors.posteriorMean`, a definition declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#posterior-mean).

## Measurable versions of the posterior mean

Let $P$ be a finite kernel from $\mathbb{R}$ to
a measurable space $\mathcal{X}$, sending $\theta$ to the measure $P_\theta$, let $\pi$ be a
finite measure on $\mathbb{R}$, and write $P^\dagger\pi$ for the posterior kernel from
$\mathcal{X}$ to $\mathbb{R}$. A function $f : \mathcal{X} \to \mathbb{R}$ is a measurable version
of the posterior mean if $f$ is measurable and $f(x) = \int \theta \, d(P^\dagger\pi)(x)(\theta)$
(the posterior mean, taken to be $0$ when the posterior has no finite first moment) for almost
every $x$ with respect to the marginal distribution of the data, the measure
$A \mapsto \int P_\theta(A) \, d\pi(\theta)$ on $\mathcal{X}$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.IsPosteriorMean`, a structure declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#is-posterior-mean).

## The posterior mean is a Bayes estimator for squared loss

Let $P$ be a finite kernel from
$\mathbb{R}$ to a measurable space $\mathcal{X}$, sending a parameter $\theta$ to the measure
$P_\theta$ on $\mathcal{X}$, let $\pi$ be a finite prior measure on $\mathbb{R}$, and let
$f : \mathcal{X} \to \mathbb{R}$ be a measurable version of the posterior mean. Then the
deterministic estimator $x \mapsto f(x)$ is a Bayes estimator for the squared loss
$\ell(\theta, y) = (\theta - y)^2$: its average risk
$\int \int (\theta - f(x))^2 \, dP_\theta(x) \, d\pi(\theta)$ equals the Bayes risk, the infimum
of the average risks of all Markov kernels from $\mathcal{X}$ to $\mathbb{R}$, where risks take
values in $[0, \infty]$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.IsPosteriorMean.isBayesEstimator`, a theorem declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#is-bayes-estimator).

## Absolute loss

The absolute loss of predicting $y \in \mathbb{R}$ when the true value is
$\theta \in \mathbb{R}$ is $|\theta - y|$, regarded as an element of $[0, \infty]$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.absLoss`, a definition declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#abs-loss).

## The expected absolute loss is minimized at every median

Let $\nu$ be a probability measure
on $\mathbb{R}$ and let $m$ be a median of $\nu$. Then for every $y \in \mathbb{R}$,

$$\int |\theta - m| \, d\nu(\theta) \le \int |\theta - y| \, d\nu(\theta),$$

where both integrals are taken in $[0, \infty]$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.lintegral_absLoss_le_of_isMedian`, a theorem declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#lintegral-abs-loss-le-of-is-median).

## Measurable choices of posterior medians

Let $P$ be a finite kernel from $\mathbb{R}$ to a
measurable space $\mathcal{X}$, sending $\theta$ to the measure $P_\theta$, let $\pi$ be a finite
measure on $\mathbb{R}$, and write $P^\dagger\pi$ for the posterior kernel from $\mathcal{X}$ to
$\mathbb{R}$. A function $f : \mathcal{X} \to \mathbb{R}$ is a measurable choice of posterior
medians if $f$ is measurable and, for almost every $x$ with respect to the marginal distribution
$A \mapsto \int P_\theta(A) \, d\pi(\theta)$ of the data, $f(x)$ is a median of the posterior
distribution $(P^\dagger\pi)(x)$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.IsPosteriorMedian`, a structure declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#is-posterior-median).

## A posterior median is a Bayes estimator for absolute loss

Let $P$ be a finite kernel from
$\mathbb{R}$ to a measurable space $\mathcal{X}$, sending a parameter $\theta$ to the measure
$P_\theta$ on $\mathcal{X}$, let $\pi$ be a finite prior measure on $\mathbb{R}$, and let
$f : \mathcal{X} \to \mathbb{R}$ be a measurable choice of posterior medians. Then the
deterministic estimator $x \mapsto f(x)$ is a Bayes estimator for the absolute loss
$\ell(\theta, y) = |\theta - y|$: its average risk
$\int \int |\theta - f(x)| \, dP_\theta(x) \, d\pi(\theta)$ equals the Bayes risk, the infimum
of the average risks of all Markov kernels from $\mathcal{X}$ to $\mathbb{R}$, where risks take
values in $[0, \infty]$.

Formalized by `Cslib.MachineLearning.OptimalPredictors.IsPosteriorMedian.isBayesEstimator`, a theorem declared in [CSLibExt/MachineLearning/Regression/OptimalPredictors.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Regression/OptimalPredictors.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html#is-bayes-estimator-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bayes estimators for squared and absolute loss](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/bayes-estimators-for-squared-and-absolute-loss)
