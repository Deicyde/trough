---
declaration: section
origin: cited
lean: Cslib.MachineLearning.LatentVariable.ExpectationMaximization.IsDist, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.sum_mul_log_sub_le, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.sum_div_mul_log_sub, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.marginal, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.logLik, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.posterior, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.elbo, Cslib.MachineLearning.LatentVariable.ExpectationMaximization.emQ
statement: formalized
proof: formalized
---

# Expectation–maximization algorithm

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html).

## Gibbs' inequality

## Probability distributions on a finite latent space

A function $q : Z \to \mathbb{R}$ on a
finite set $Z$ is a probability distribution when $q(z) \ge 0$ for every $z \in Z$ and
$\sum_{z \in Z} q(z) = 1$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.IsDist`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#is-dist).

## Gibbs' inequality (evidence lower bound form)

Let $Z$ be a finite set, let
$p : Z \to \mathbb{R}$ satisfy $p(z) > 0$ for all $z$, and let $q$ be a probability distribution
on $Z$. Then $\sum_{z \in Z} q(z) (\log p(z) - \log q(z)) \le \log \sum_{z \in Z} p(z)$.

This is the log-sum inequality with $\sum_{z} q(z) = 1$; terms with $q(z) = 0$ contribute $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.sum_mul_log_sub_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#sum-mul-log-sub-le).

## Equality case of Gibbs' inequality

Let $Z$ be a finite nonempty set, let
$p : Z \to \mathbb{R}$ satisfy $p(z) > 0$ for all $z$, and write $P = \sum_{z \in Z} p(z)$. Then

$$\sum_{z \in Z} \frac{p(z)}{P} \left(\log p(z) - \log \frac{p(z)}{P}\right) = \log P,$$

that is, the bound of Gibbs' inequality is attained at the distribution $q = p / P$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.sum_div_mul_log_sub`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#sum-div-mul-log-sub).

## Marginal of a latent-variable model

For a joint model $p$ assigning a real number
$p_\theta(x, z)$ to each parameter $\theta$, observation $x$ and latent value $z$ in a finite
latent space $Z$, the marginal is $p_\theta(x) = \sum_{z \in Z} p_\theta(x, z)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.marginal`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#marginal).

## Log-likelihood of a latent-variable model

For a joint model $p$ with finite latent space
$Z$ and data $x_0, \dots, x_{N-1}$, the log-likelihood at the parameter $\theta$ is
$\ell(\theta) = \sum_{n < N} \log p_\theta(x_n)$, where
$p_\theta(x) = \sum_{z \in Z} p_\theta(x, z)$ is the marginal.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.logLik`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#log-lik).

## Posterior of a latent-variable model

For a joint model $p$ with finite latent space $Z$,
the posterior of the latent value $z$ given the observation $x$ at the parameter $\theta$ is
$p_\theta(z \mid x) = p_\theta(x, z) / p_\theta(x)$, where
$p_\theta(x) = \sum_{z' \in Z} p_\theta(x, z')$ is the marginal (the quotient is read as $0$
when the marginal is $0$). Computing it is the E-step of expectation-maximization.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.posterior`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#posterior).

## Evidence lower bound of latent distributions

Let $Z$ be a finite set, let
$p_\theta(x, z)$ be real numbers indexed by parameters $\theta$, observations $x$ and latent values
$z \in Z$, and let $x_1, \dots, x_N$ be data. For a parameter $\theta$ and functions
$q_1, \dots, q_N : Z \to \mathbb{R}$ (one latent distribution per data point), the evidence lower
bound is $\sum_{n=1}^N \sum_{z \in Z} q_n(z) \bigl(\log p_\theta(x_n, z) - \log q_n(z)\bigr)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.elbo`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#elbo).

## The EM objective

Let $Z$ be a finite set, let $p_\theta(x, z)$ be real numbers indexed by
parameters $\theta$, observations $x$ and latent values $z \in Z$, let $x_1, \dots, x_N$ be data,
and write $p_\theta(z \mid x) = p_\theta(x, z) / \sum_{z' \in Z} p_\theta(x, z')$ for the posterior.
For parameters $\theta'$ and $\theta$, the EM objective is
$Q(\theta' \mid \theta) = \sum_{n=1}^N \sum_{z \in Z} p_\theta(z \mid x_n) \log p_{\theta'}(x_n, z)$
(maximized over $\theta'$ in the M-step).

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.emQ`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#em-q).

## Posterior entropy

For a joint model $p$ with finite latent space $Z$, data
$x_0, \dots, x_{N-1}$ and a parameter $\theta$, the posterior entropy is
$-\sum_{n < N} \sum_{z \in Z} p_\theta(z \mid x_n) \log p_\theta(z \mid x_n)$, where
$p_\theta(z \mid x)$ is the posterior of $z$ given $x$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.postEntropy`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#post-entropy).

## Posteriors are probability distributions

Let $Z$ be a nonempty finite set and let
$p_\theta(x, z)$ be real numbers indexed by parameters $\theta$, observations $x$ and latent values
$z \in Z$, with $p_\theta(x, z) > 0$ for all $\theta$, $x$, $z$. For every parameter $\theta$ and
observation $x$, the posterior $z \mapsto p_\theta(x, z) / \sum_{z' \in Z} p_\theta(x, z')$ is a
probability distribution on $Z$: its values are nonnegative and sum to $1$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.isDist_posterior`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#is-dist-posterior).

## The evidence lower bound

Let $Z$ be a finite set, let $p_\theta(x, z)$ be real numbers
indexed by parameters $\theta$, observations $x$ and latent values $z \in Z$, with
$p_\theta(x, z) > 0$ for all $\theta$, $x$, $z$, and let $x_1, \dots, x_N$ be data. For every
parameter $\theta$ and all probability distributions $q_1, \dots, q_N$ on $Z$,

$$
\sum_{n=1}^N \sum_{z \in Z} q_n(z) \bigl(\log p_\theta(x_n, z) - \log q_n(z)\bigr) \le
\sum_{n=1}^N \log \sum_{z \in Z} p_\theta(x_n, z),
$$

that is, the evidence lower bound of $q_1, \dots, q_N$ at $\theta$ is at most the log-likelihood
of the data at $\theta$. Terms with $q_n(z) = 0$ count as $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.elbo_le_logLik`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#elbo-le-log-lik).

## The bound is tight at the posterior

Let $Z$ be a nonempty finite set, let
$p_\theta(x, z)$ be real numbers indexed by parameters $\theta$, observations $x$ and latent values
$z \in Z$, with $p_\theta(x, z) > 0$ for all $\theta$, $x$, $z$, and let $x_1, \dots, x_N$ be data.
For every parameter $\theta$, the posteriors
$q_n(z) = p_\theta(z \mid x_n) = p_\theta(x_n, z) / \sum_{z' \in Z} p_\theta(x_n, z')$ satisfy

$$
\sum_{n=1}^N \sum_{z \in Z} q_n(z) \bigl(\log p_\theta(x_n, z) - \log q_n(z)\bigr) =
\sum_{n=1}^N \log \sum_{z \in Z} p_\theta(x_n, z),
$$

that is, the evidence lower bound at $\theta$ of the posteriors equals the log-likelihood of the
data at $\theta$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.elbo_posterior`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#elbo-posterior).

## The ELBO at the posterior is the EM objective plus the entropy

Let $Z$ be a finite set,
let $p_\theta(x, z)$ be real numbers indexed by parameters $\theta$, observations $x$ and latent
values $z \in Z$, let $x_1, \dots, x_N$ be data, and write
$p_\theta(z \mid x) = p_\theta(x, z) / \sum_{z' \in Z} p_\theta(x, z')$ for the posterior,
$Q(\theta' \mid \theta) = \sum_{n=1}^N \sum_{z \in Z} p_\theta(z \mid x_n) \log p_{\theta'}(x_n, z)$
for the EM objective and
$H(\theta) = -\sum_{n=1}^N \sum_{z \in Z} p_\theta(z \mid x_n) \log p_\theta(z \mid x_n)$ for the
entropy of the posteriors. For all parameters $\theta'$ and $\theta$, the evidence lower bound at
$\theta'$ of the posteriors $q_n = p_\theta(\cdot \mid x_n)$ satisfies

$$
\sum_{n=1}^N \sum_{z \in Z} q_n(z) \bigl(\log p_{\theta'}(x_n, z) - \log q_n(z)\bigr) =
Q(\theta' \mid \theta) + H(\theta),
$$

that is, it splits as the EM objective $Q(\theta' \mid \theta)$ plus the posterior entropy.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.elbo_posterior_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#elbo-posterior-eq).

## The EM inequality

Let $Z$ be a nonempty finite set, let $p_\theta(x, z)$ be real numbers
indexed by parameters $\theta$, observations $x$ and latent values $z \in Z$, with
$p_\theta(x, z) > 0$ for all $\theta$, $x$, $z$, and let $x_1, \dots, x_N$ be data. Write
$p_\theta(z \mid x) = p_\theta(x, z) / \sum_{z' \in Z} p_\theta(x, z')$ for the posterior,
$Q(\theta' \mid \theta) = \sum_{n=1}^N \sum_{z \in Z} p_\theta(z \mid x_n) \log p_{\theta'}(x_n, z)$
for the EM objective and $\ell(\theta) = \sum_{n=1}^N \log \sum_{z \in Z} p_\theta(x_n, z)$ for the
log-likelihood. For all parameters $\theta'$ and $\theta$,
$Q(\theta' \mid \theta) - Q(\theta \mid \theta) \le \ell(\theta') - \ell(\theta)$: the
log-likelihood gains at least as much as $Q(\cdot \mid \theta)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.emQ_sub_le_logLik_sub`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#em-q-sub-le-log-lik-sub).

## The EM theorem

Let $Z$ be a nonempty finite set, let $p_\theta(x, z)$ be real numbers
indexed by parameters $\theta$, observations $x$ and latent values $z \in Z$, with
$p_\theta(x, z) > 0$ for all $\theta$, $x$, $z$, and let $x_1, \dots, x_N$ be data. Write
$p_\theta(z \mid x) = p_\theta(x, z) / \sum_{z' \in Z} p_\theta(x, z')$ for the posterior,
$Q(\theta' \mid \theta) = \sum_{n=1}^N \sum_{z \in Z} p_\theta(z \mid x_n) \log p_{\theta'}(x_n, z)$
for the EM objective and $\ell(\theta) = \sum_{n=1}^N \log \sum_{z \in Z} p_\theta(x_n, z)$ for the
log-likelihood. For parameters $\theta$ and $\theta'$, if
$Q(\theta \mid \theta) \le Q(\theta' \mid \theta)$, then $\ell(\theta) \le \ell(\theta')$: a step
that does not decrease $Q(\cdot \mid \theta)$ does not decrease the log-likelihood.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.logLik_le_of_emQ_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#log-lik-le-of-em-q-le).

## EM iterates have monotone likelihood

Let $Z$ be a nonempty finite set, let
$p_\theta(x, z)$ be real numbers indexed by parameters $\theta$, observations $x$ and latent values
$z \in Z$, with $p_\theta(x, z) > 0$ for all $\theta$, $x$, $z$, and let $x_1, \dots, x_N$ be data.
Write $p_\theta(z \mid x) = p_\theta(x, z) / \sum_{z' \in Z} p_\theta(x, z')$ for the posterior,
$Q(\theta' \mid \theta) = \sum_{n=1}^N \sum_{z \in Z} p_\theta(z \mid x_n) \log p_{\theta'}(x_n, z)$
for the EM objective and $\ell(\theta) = \sum_{n=1}^N \log \sum_{z \in Z} p_\theta(x_n, z)$ for the
log-likelihood. Let $M$ be a map on parameters, with $k$-th iterate $M^k$ ($M^0$ the identity),
such that $Q(M\theta \mid \theta) \ge Q(\theta \mid \theta)$ for every $\theta$ (in particular if
$M\theta$ maximizes $Q(\cdot \mid \theta)$, or $M$ is a generalized-EM step). Then for every
$\theta_0$ the sequence $k \mapsto \ell(M^k \theta_0)$ is nondecreasing.

Formalized by `Cslib.MachineLearning.LatentVariable.ExpectationMaximization.logLik_iterate_monotone`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/LatentVariable/ExpectationMaximization.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html#log-lik-iterate-monotone).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Expectation–maximization algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/expectation-maximization-algorithm)
