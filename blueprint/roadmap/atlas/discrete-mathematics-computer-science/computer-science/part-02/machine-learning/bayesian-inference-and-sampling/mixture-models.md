---
declaration: section
origin: cited
lean: Cslib.MachineLearning.LatentVariable.BernoulliMixture.sum_mul_log_le_sum_mul_log_div, Cslib.MachineLearning.LatentVariable.BernoulliMixture.bernPMF, Cslib.MachineLearning.LatentVariable.BernoulliMixture.Params, Cslib.MachineLearning.LatentVariable.BernoulliMixture.Params.Valid, Cslib.MachineLearning.LatentVariable.BernoulliMixture.ValidParams, Cslib.MachineLearning.LatentVariable.BernoulliMixture.joint, Cslib.MachineLearning.LatentVariable.BernoulliMixture.resp, Cslib.MachineLearning.LatentVariable.BernoulliMixture.mass
statement: formalized
proof: formalized
---

# Mixture models

61 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html).

## The weighted log-likelihood is bounded by its value at the normalized counts

Let $Z$ be
a finite set, let $c \colon Z \to \mathbb{R}$ be nonnegative counts with positive total
$C = \sum_{z \in Z} c_z > 0$, and let $w \colon Z \to \mathbb{R}$ be positive weights with
$\sum_{z \in Z} w_z = 1$. Then $\sum_{z \in Z} c_z \log w_z \le \sum_{z \in Z} c_z \log(c_z / C)$
(Gibbs' inequality).

When every count is positive the normalized counts $c_z / C$ are themselves admissible weights,
so they maximize.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.sum_mul_log_le_sum_mul_log_div`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#sum-mul-log-le-sum-mul-log-div).

## Product Bernoulli probability mass function

For a vector $p \in \mathbb{R}^d$ of success
probabilities and a binary vector $x \in \{0, 1\}^d$, the probability of $x$ under the product of
$d$ independent Bernoulli distributions with parameters $p_1, \dots, p_d$ is

$$\prod_{j=1}^{d} p_j^{x_j} (1 - p_j)^{1 - x_j},$$

that is, the product over $j$ of $p_j$ when $x_j = 1$ and of $1 - p_j$ when $x_j = 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.bernPMF`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#bern-pmf).

## Parameters of a Bernoulli mixture

The parameters of a mixture of $K$ products of $d$
Bernoulli distributions are real mixing weights $\pi_k$ for $k < K$ and real success
probabilities $p_{kj}$ for every component $k < K$ and coordinate $j < d$. No constraint is
imposed on these numbers here; the admissible ones are the valid parameters.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.Params`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#params).

## Valid parameters of a Bernoulli mixture

Parameters of a mixture of $K$ products of $d$
Bernoulli distributions, with mixing weights $\pi_k$ and success probabilities $p_{kj}$, are valid
when $\pi_k > 0$ for every $k < K$, $\sum_{k < K} \pi_k = 1$, and $0 < p_{kj} < 1$ for every
$k < K$ and $j < d$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.Params.Valid`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#valid).

## The parameter space of a Bernoulli mixture

The parameter space of EM for a mixture of
$K$ products of $d$ Bernoulli distributions is the set of valid parameters: mixing weights
$\pi_k$ and success probabilities $p_{kj}$ ($k < K$, $j < d$) with every $\pi_k > 0$,
$\sum_{k < K} \pi_k = 1$ and every $p_{kj}$ strictly between $0$ and $1$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.ValidParams`, an abbreviation declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#valid-params).

## Joint distribution of the Bernoulli mixture

For valid parameters $\theta$ of a mixture of
$K$ products of $d$ Bernoulli distributions, with mixing weights $\pi_k$ and success probabilities
$p_{kj}$, the joint probability of a binary vector $x \in \{0, 1\}^d$ and a component $k$ is

$$p_\theta(x, k) = \pi_k \prod_{j=1}^{d} p_{kj}^{x_j} (1 - p_{kj})^{1 - x_j},$$

that is, $\pi_k$ times the product Bernoulli probability of $x$ with parameters
$p_{k1}, \dots, p_{kd}$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.joint`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#joint).

## Responsibilities of a Bernoulli mixture

Let $\theta$ be valid parameters of a mixture of
$K$ products of $d$ Bernoulli distributions, and write $p_\theta(x, k)$ for the joint probability
of a binary vector $x \in \{0,1\}^d$ and a component $k < K$ under $\theta$. The responsibility of
$k$ for $x$ is the posterior probability $r_k(x) = p_\theta(x, k) / \sum_{k' < K} p_\theta(x, k')$.
Computing it is the E-step of EM.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.resp`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#resp).

## Effective number of points of a Bernoulli-mixture component

For data
$x_1, \dots, x_N \in \{0, 1\}^d$ and valid parameters $\theta$ of a mixture of $K$ products of $d$
Bernoulli distributions, the effective number of points of component $k$ is
$N_k = \sum_{n=1}^{N} r_{nk}$, where $r_{nk}$ is the posterior probability (responsibility) of
component $k$ given $x_n$ under $\theta$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.mass`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#mass).

## Responsibility-weighted count of ones

For data $x_1, \dots, x_N \in \{0, 1\}^d$, valid
parameters $\theta$ of a mixture of $K$ products of $d$ Bernoulli distributions, a component $k$
and a coordinate $j$, this is the sum $\sum_{n \,:\, x_{nj} = 1} r_{nk}$, over the points whose
$j$-th coordinate is $1$, of the posterior probability $r_{nk}$ of component $k$ given $x_n$
under $\theta$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.ones`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#ones).

## Responsibility-weighted count of zeros

Let $\theta$ be valid parameters of a mixture of
$K$ products of $d$ Bernoulli distributions, let $x_0, \dots, x_{N-1} \in \{0,1\}^d$ be data, and
let $k < K$ be a component and $j < d$ a coordinate. Write $x_{nj}$ for the $j$-th coordinate of
$x_n$ and $r_k(x_n)$ for the responsibility of component $k$ for $x_n$ under $\theta$. The
weighted count is $\sum_{n < N,\ x_{nj} = 0} r_k(x_n)$, the sum of the responsibilities over the
points whose $j$-th coordinate is $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.zeros`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#zeros).

## The M-step of the Bernoulli mixture

Let $x_1, \dots, x_N \in \{0, 1\}^d$ be data and
$\theta$ valid parameters of a mixture of $K$ products of $d$ Bernoulli distributions. With $r_{nk}$
the posterior probability of component $k$ given $x_n$ under $\theta$, $N_k = \sum_n r_{nk}$ and
$A_{kj} = \sum_n r_{nk} x_{nj}$, the M-step returns the parameters with mixing weights
$\pi'_k = N_k / N$ and success probabilities $p'_{kj} = A_{kj} / N_k$, where a quotient by $0$ is
read as $0$. These parameters need not be valid.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.mStep`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#m-step).

## Rich data for a Bernoulli mixture

Data $x_0, \dots, x_{N-1} \in \{0,1\}^d$ are rich when
$N > 0$ and, for every coordinate $j < d$, some $x_n$ has $j$-th coordinate $1$ and some $x_m$
has $j$-th coordinate $0$. These are the data on which the M-step yields valid parameters.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.Rich`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#rich).

## One EM step for the Bernoulli mixture

Let $x_1, \dots, x_N \in \{0, 1\}^d$ be data with
$N \ge 1$ in which every coordinate takes both values. For valid parameters $\theta$ of a mixture
of $K$ products of $d$ Bernoulli distributions, the EM step maps $\theta$ to the parameters with
mixing weights $\pi'_k = N_k / N$ and success probabilities $p'_{kj} = A_{kj} / N_k$, where
$r_{nk}$ is the posterior probability of component $k$ given $x_n$ under $\theta$,
$N_k = \sum_n r_{nk}$, and $A_{kj}$ is the sum of $r_{nk}$ over the points with $x_{nj} = 1$. On
such data these parameters are again valid.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.emStep`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-step).

## Decomposition of the EM objective for the Bernoulli mixture

Let
$x_1, \dots, x_N \in \{0, 1\}^d$ be data and let $\theta$ and $\theta'$ be valid parameters of a
mixture of $K$ products of $d$ Bernoulli distributions (positive mixing weights summing to one and
success probabilities in $(0, 1)$), where $\theta'$ has mixing weights $\pi'_k$ and success
probabilities $p'_{kj}$. Write $p_\theta(x, k)$ for the joint probability of $x$ and component $k$
under $\theta$ (the mixing weight of $k$ times the product Bernoulli probability of $x$),
$r_{nk} = p_\theta(k \mid x_n) = p_\theta(x_n, k) / \sum_l p_\theta(x_n, l)$ for the posterior
probability of component $k$ given $x_n$, $N_k = \sum_n r_{nk}$, and $A_{kj}$ and $B_{kj}$ for the
sums of $r_{nk}$ over the points $x_n$ whose $j$-th coordinate $x_{nj}$ is $1$ and is $0$
respectively. Then the EM objective
$Q(\theta' \mid \theta) = \sum_n \sum_k r_{nk} \log p_{\theta'}(x_n, k)$ equals

$$\sum_{k=1}^{K} \Big( N_k \log \pi'_k + \sum_{j=1}^{d} \big( A_{kj} \log p'_{kj} +
B_{kj} \log (1 - p'_{kj}) \big) \Big).$$

The first term depends only on the mixing weights and each remaining term on a single $p'_{kj}$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.emQ_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-q-eq).

## The M-step of the Bernoulli mixture maximizes the EM objective

Let
$x_1, \dots, x_N \in \{0, 1\}^d$ be rich data: $N > 0$, and for every coordinate $j < d$ some
$x_n$ has $j$-th coordinate $1$ and some $x_m$ has $j$-th coordinate $0$. Let $\theta$ be valid
parameters of a mixture of $K$ products of $d$ Bernoulli distributions, and let $\theta^+$ be the
result of the EM step applied to $\theta$. Then every valid parameter $\theta'$ satisfies
$Q(\theta' \mid \theta) \le Q(\theta^+ \mid \theta)$, where $Q$ is the EM objective of the
mixture's joint distribution.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.emQ_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-q-le-em-step).

## Each EM step for the Bernoulli mixture does not decrease the log-likelihood

Let
$x_1, \dots, x_N \in \{0, 1\}^d$ be rich data: $N > 0$, and for every coordinate $j < d$ some
$x_n$ has $j$-th coordinate $1$ and some $x_m$ has $j$-th coordinate $0$. Let $\theta$ be valid
parameters of a mixture of $K$ products of $d$ Bernoulli distributions. Then
$\ell(\theta) \le \ell(\theta^+)$, where $\ell$ is the log-likelihood of the data under the
mixture's joint distribution and $\theta^+$ is the result of the EM step applied to $\theta$.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.logLik_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-lik-le-em-step).

## The log-likelihood is monotone along the EM iterates of a Bernoulli mixture

Let
$x_1, \dots, x_N \in \{0, 1\}^d$ be rich data: $N > 0$, and for every coordinate $j < d$ some
$x_n$ has $j$-th coordinate $1$ and some $x_m$ has $j$-th coordinate $0$. Let $\theta_0$ be valid
parameters of a mixture of $K$ products of $d$ Bernoulli distributions, and let $\theta_t$ be the
result of $t$ EM steps from $\theta_0$. Then $\ell(\theta_t)$ is nondecreasing in
$t \in \mathbb{N}$, where $\ell$ is the log-likelihood of the data under the mixture's joint
distribution.

Formalized by `Cslib.MachineLearning.LatentVariable.BernoulliMixture.logLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/BernoulliMixture.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-lik-iterate-em-step-monotone).

## Isotropic Gaussian density

For a mean $\mu \in \mathbb{R}^d$ and a variance $v \ge 0$,
the isotropic Gaussian density at $x \in \mathbb{R}^d$ is
$\mathcal{N}(x \mid \mu, v I) = \prod_{i=1}^{d} \varphi_{\mu_i, v}(x_i)$, where
$\varphi_{m, v}$ is the one-dimensional Gaussian density with mean $m$ and variance $v$.

For $v = 0$ the one-dimensional density is identically $0$, following Mathlib's convention.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.isoGaussPDF`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#iso-gauss-pdf).

## Log-density of the isotropic Gaussian

For $\mu, x \in \mathbb{R}^d$ and a variance
$v > 0$, the isotropic Gaussian density $\mathcal{N}(x \mid \mu, v I)$ with mean $\mu$ and
covariance $v I$ satisfies
$\log \mathcal{N}(x \mid \mu, v I) = -\tfrac{d}{2} \log(2 \pi v) - \|x - \mu\|^2 / (2 v)$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.log_isoGaussPDF`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-iso-gauss-pdf).

## Parameters of an isotropic Gaussian mixture

Parameters of a $K$-component isotropic
Gaussian mixture in $d$ dimensions consist, for each component $k < K$, of a mixing weight
$\pi_k \in \mathbb{R}$, a mean $\mu_k \in \mathbb{R}^d$ and a variance $\sigma_k^2 \ge 0$; component
$k$ has covariance $\sigma_k^2 I$.

No constraint is placed on the weights here; validity is a separate condition.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.Params`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#params-2).

## Validity of isotropic Gaussian mixture parameters

Parameters of a $K$-component
isotropic Gaussian mixture in $d$ dimensions, with mixing weights $\pi_k$, means $\mu_k$ and
variances $\sigma_k^2 \ge 0$, are valid when every $\pi_k > 0$, $\sum_k \pi_k = 1$, and every
$\sigma_k^2 > 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.Params.Valid`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#valid-2).

## The parameter space of isotropic Gaussian mixture EM

For a $K$-component isotropic
Gaussian mixture in $d$ dimensions, the parameter space of EM is the set of parameters (mixing
weights $\pi_k$, means $\mu_k \in \mathbb{R}^d$ and variances $\sigma_k^2 \ge 0$) that are
valid: every $\pi_k > 0$, $\sum_k \pi_k = 1$, and every $\sigma_k^2 > 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.ValidParams`, an abbreviation declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#valid-params-2).

## Joint density of an isotropic Gaussian mixture

For valid parameters $\theta$ of a
$K$-component isotropic Gaussian mixture in $\mathbb{R}^d$, with weights $\pi_k$, means $\mu_k$
and variances $\sigma_k^2$, the joint density of a point $x \in \mathbb{R}^d$ and a component $k$
is $p_\theta(x, k) = \pi_k \, \mathcal{N}(x \mid \mu_k, \sigma_k^2 I)$, where
$\mathcal{N}(\cdot \mid \mu, v I)$ is the isotropic Gaussian density.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.joint`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#joint-2).

## Mixture density of an isotropic Gaussian mixture

For valid parameters $\theta$ with
mixing weights $\pi_k$, means $\mu_k$ and variances $\sigma_k^2$, and every $x \in \mathbb{R}^d$,
the marginal $p_\theta(x) = \sum_k p_\theta(x, k)$ of the joint density equals
$\sum_k \pi_k \, \mathcal{N}(x \mid \mu_k, \sigma_k^2 I)$, where $\mathcal{N}(x \mid \mu, v I)$
is the isotropic Gaussian density.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.marginal_joint`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#marginal-joint).

## Responsibilities in an isotropic Gaussian mixture

For valid parameters $\theta$ with mixing
weights $\pi_k$, means $\mu_k$ and variances $\sigma_k^2$, a point $x \in \mathbb{R}^d$ and a
component $k$, the responsibility of $k$ for $x$ is the posterior
$p_\theta(k \mid x) = \pi_k \mathcal{N}(x \mid \mu_k, \sigma_k^2 I) /
\sum_j \pi_j \mathcal{N}(x \mid \mu_j, \sigma_j^2 I)$, where $\mathcal{N}(x \mid \mu, v I)$ is the
isotropic Gaussian density. Computing it at each data point is the E-step.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.resp`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#resp-2).

## Valid mixture parameters have at least one component

If $\theta$ is a valid parameter of
a $K$-component isotropic Gaussian mixture in $d$ dimensions, then $K \ge 1$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.nonempty_of_valid`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#nonempty-of-valid).

## Effective number of points in an isotropic Gaussian mixture

Given data points
$x_0, \dots, x_{N-1}$ in $\mathbb{R}^d$, valid parameters $\theta$ of a $K$-component isotropic
Gaussian mixture and a component $k$, the effective number of points of $k$ is
$N_k = \sum_n r_{nk}$, where $r_{nk}$ is the responsibility of component $k$ for $x_n$ under
$\theta$, the posterior probability of $k$ given $x_n$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.mass`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#mass-2).

## M-step mean update for an isotropic Gaussian mixture

Given data points
$x_0, \dots, x_{N-1}$ in $\mathbb{R}^d$, valid parameters $\theta$ of a $K$-component isotropic
Gaussian mixture and a component $k$, the updated mean of $k$ is the responsibility-weighted
mean $\mu_k' = N_k^{-1} \sum_n r_{nk} x_n$, where $r_{nk}$ is the responsibility of component $k$
for $x_n$ under $\theta$ and $N_k = \sum_n r_{nk}$.

The inverse of $0$ is read as $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.newMean`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#new-mean).

## Responsibility-weighted scatter in an isotropic Gaussian mixture

Given data points
$x_0, \dots, x_{N-1}$ in $\mathbb{R}^d$, valid parameters $\theta$ of a $K$-component isotropic
Gaussian mixture and a component $k$, the scatter of $k$ is
$S_k = \sum_n r_{nk} \lVert x_n - \mu_k' \rVert^2$, where $r_{nk}$ is the responsibility of
component $k$ for $x_n$ under $\theta$, $N_k = \sum_n r_{nk}$ and
$\mu_k' = N_k^{-1} \sum_n r_{nk} x_n$ is the responsibility-weighted mean.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.scatter`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#scatter).

## M-step variance update for an isotropic Gaussian mixture

Given data points
$x_0, \dots, x_{N-1}$ in $\mathbb{R}^d$, valid parameters $\theta$ of a $K$-component isotropic
Gaussian mixture and a component $k$, the updated variance of $k$ is
$\sigma_k'^2 = S_k / (d N_k)$, where $r_{nk}$ is the responsibility of component $k$ for $x_n$
under $\theta$, $N_k = \sum_n r_{nk}$, $\mu_k' = N_k^{-1} \sum_n r_{nk} x_n$ and
$S_k = \sum_n r_{nk} \lVert x_n - \mu_k' \rVert^2$.

Division by zero is read as $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.newVar`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#new-var).

## M-step of EM for an isotropic Gaussian mixture

Let $x_0, \dots, x_{N-1}$ be data
points in $\mathbb{R}^d$, let $\theta$ be valid parameters of a $K$-component isotropic Gaussian
mixture, and let $r_{nk}$ be the responsibility of component $k$ for $x_n$ under $\theta$. With
$N_k = \sum_n r_{nk}$, the M-step returns the parameters with mixing weights
$\pi_k' = N_k / N$, means $\mu_k' = N_k^{-1} \sum_n r_{nk} x_n$ and variances
$\sigma_k'^2 = S_k / (d N_k)$, where $S_k = \sum_n r_{nk} \lVert x_n - \mu_k' \rVert^2$.

Division by zero is read as $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.mStep`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#m-step-2).

## The weighted centroid decomposition

Let $F$ be a real inner product space, $s$ a finite
index set, $w_i \in \mathbb{R}$ weights with $W = \sum_{i \in s} w_i \ne 0$, and $x_i \in F$
points for $i \in s$, and let $m = W^{-1} \sum_{i \in s} w_i x_i$. Then for every $c \in F$,

$$\sum_{i \in s} w_i \|x_i - c\|^2 = \sum_{i \in s} w_i \|x_i - m\|^2 + W \|m - c\|^2.$$

This is the weighted version of the centroid decomposition behind $k$-means. When $W > 0$ it
shows that $m$ minimizes $c \mapsto \sum_{i \in s} w_i \|x_i - c\|^2$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.sum_mul_norm_sub_sq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#sum-mul-norm-sub-sq).

## With positive total weight, the weighted mean minimizes the weighted sum of squared distances

**With positive total weight, the weighted mean minimizes the weighted sum of squared
distances.** Let $F$ be a real inner product space, $s$ a finite index set, $w_i \in \mathbb{R}$
weights with $W = \sum_{i \in s} w_i > 0$, and $x_i \in F$ points for $i \in s$, and let
$m = W^{-1} \sum_{i \in s} w_i x_i$ be the weighted mean. Then for every $c \in F$,

$$\sum_{i \in s} w_i \|x_i - m\|^2 \le \sum_{i \in s} w_i \|x_i - c\|^2.$$

The individual weights need not be nonnegative; only their total is assumed positive.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.sum_mul_norm_sub_sq_mean_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#sum-mul-norm-sub-sq-mean-le).

## Data that are not all equal

A finite family of points $x_0, \dots, x_{N-1}$ in
$\mathbb{R}^d$ is not all equal when there are indices $n$ and $n'$ with $x_n \ne x_{n'}$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.NotAllEqual`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#not-all-equal).

## The EM step for isotropic Gaussian mixtures

Let $x_1, \dots, x_N$ be points of
$\mathbb{R}^d$ that are not all equal and let $\theta$ be valid parameters of a $K$-component
isotropic Gaussian mixture. With $r_{nk}$ the responsibility of component $k$ for $x_n$ under
$\theta$ (the E-step), the EM step sends $\theta$ to the valid parameters with weights
$\pi_k' = N_k / N$, means $\mu_k' = N_k^{-1} \sum_n r_{nk} x_n$ and variances
$v_k' = S_k / (d N_k)$, where $N_k = \sum_n r_{nk}$ and $S_k = \sum_n r_{nk} \|x_n - \mu_k'\|^2$
(the M-step).

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.emStep`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-step-2).

## Component term of the EM objective for isotropic Gaussian mixtures

Given points
$x_1, \dots, x_N$ of $\mathbb{R}^d$, valid parameters $\theta$ of a $K$-component isotropic
Gaussian mixture, a component $k$, a mean $\mu \in \mathbb{R}^d$ and a real number $v$, the
component term is

$$
C_k(\mu, v) = \sum_n r_{nk} \bigl(-\tfrac{d}{2} \log(2\pi v) - \|x_n - \mu\|^2 / (2v)\bigr),
$$

where $r_{nk}$ is the responsibility of component $k$ for $x_n$ under $\theta$.

For $v > 0$ this is $\sum_n r_{nk} \log \mathcal{N}(x_n \mid \mu, v I)$, where
$\mathcal{N}(\cdot \mid \mu, v I)$ is the isotropic Gaussian density with mean $\mu$ and
covariance $v I$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.compTerm`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#comp-term).

## The EM objective of an isotropic Gaussian mixture splits by component

Let
$x_1, \dots, x_N$ be points of $\mathbb{R}^d$, and let $\theta'$ and $\theta$ be valid parameters
of a $K$-component isotropic Gaussian mixture, where $\theta'$ has weights $\pi_k'$, means
$\mu_k'$ and variances $v_k'$. Then the EM objective of the mixture's joint density satisfies

$$
Q(\theta' \mid \theta) = \sum_k \bigl(N_k \log \pi_k' + C_k(\mu_k', v_k')\bigr),
$$

where $r_{nk}$ is the responsibility of component $k$ for $x_n$ under $\theta$,
$N_k = \sum_n r_{nk}$ and
$C_k(\mu, v) = \sum_n r_{nk} \bigl(-\tfrac{d}{2} \log(2\pi v) - \|x_n - \mu\|^2 / (2v)\bigr)$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.emQ_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-q-eq-2).

## Isotropic Gaussian mixtures: the weight update maximizes the weights term

Let
$x_1, \dots, x_N$ be $N > 0$ points of $\mathbb{R}^d$, let $\theta$ be valid parameters of a
$K$-component isotropic Gaussian mixture in $d$ dimensions, and let $N_k = \sum_n r_{nk}$ be the
mass of component $k$, where $r_{nk}$ is the responsibility of component $k$ for $x_n$ under
$\theta$. Then for all real $w_1, \dots, w_K > 0$ with $\sum_k w_k = 1$,

$$\sum_k N_k \log w_k \le \sum_k N_k \log \frac{N_k}{N}.$$

That is, the M-step weights $N_k / N$ maximize the weights term (Gibbs' inequality).

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.sum_mass_mul_log_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#sum-mass-mul-log-le).

## The mean and variance updates maximize each component term

Let $x_1, \dots, x_N$ be
points of $\mathbb{R}^d$ that are not all equal, let $\theta$ be valid parameters of a
$K$-component isotropic Gaussian mixture, let $k$ be a component, and let $r_{nk}$ be the
responsibility of component $k$ for $x_n$ under $\theta$. For every $\mu \in \mathbb{R}^d$ and
every real $v > 0$, the component term

$$
C_k(\mu, v) = \sum_n r_{nk} \bigl(-\tfrac{d}{2} \log(2\pi v) - \|x_n - \mu\|^2 / (2v)\bigr)
$$

satisfies $C_k(\mu, v) \le C_k(\mu_k', v_k')$, where $N_k = \sum_n r_{nk}$,
$\mu_k' = N_k^{-1} \sum_n r_{nk} x_n$ is the responsibility-weighted mean,
$S_k = \sum_n r_{nk} \|x_n - \mu_k'\|^2$ and $v_k' = S_k / (d N_k)$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.compTerm_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#comp-term-le).

## The M-step for isotropic Gaussian mixtures maximizes the EM objective

Let
$x_1, \dots, x_N$ be points of $\mathbb{R}^d$ that are not all equal, let $\theta$ be valid
parameters of a $K$-component isotropic Gaussian mixture, and let $\theta^+$ be the result of
the EM step applied to $\theta$. Then every valid parameter $\theta'$ satisfies
$Q(\theta' \mid \theta) \le Q(\theta^+ \mid \theta)$, where $Q$ is the EM objective of the
mixture's joint density.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.emQ_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-q-le-em-step-2).

## Each EM step for the Gaussian mixture does not decrease the log-likelihood

Let
$x_1, \dots, x_N$ be points of $\mathbb{R}^d$ that are not all equal and let $\theta$ be valid
parameters of a $K$-component isotropic Gaussian mixture. Then $\ell(\theta) \le \ell(\theta^+)$,
where $\ell$ is the log-likelihood of the data under the mixture and $\theta^+$ is the result of
the EM step applied to $\theta$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.logLik_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-lik-le-em-step-2).

## The log-likelihood is monotone along the EM iterates of an isotropic Gaussian mixture

Let $x_1, \dots, x_N$ be points of $\mathbb{R}^d$ that are not all equal, let $\theta_0$ be valid
parameters of a $K$-component isotropic Gaussian mixture, and let $\theta_t$ be the result of $t$
EM steps from $\theta_0$. Then $\ell(\theta_t)$ is nondecreasing in $t \in \mathbb{N}$, where
$\ell$ is the log-likelihood of the data under the mixture.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixture.logLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixture.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-lik-iterate-em-step-monotone-2).

## Parameters of a full-covariance Gaussian mixture

A parameter of the $K$-component
Gaussian mixture in $d$ dimensions with full covariances consists of, for each component
$k < K$, a real mixing weight $\pi_k$, a mean $\mu_k \in \mathbb{R}^d$ and a real $d \times d$
covariance matrix $\Sigma_k$, with no constraints imposed.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.Params`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#params-3).

## Validity of full-covariance Gaussian mixture parameters

Parameters
$(\pi_k, \mu_k, \Sigma_k)_{k\lt K}$ of a $K$-component Gaussian mixture in $d$ dimensions are valid
when every weight $\pi_k$ is positive, the weights sum to one, and every covariance matrix
$\Sigma_k$ is positive definite.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.Params.Valid`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#valid-3).

## Valid parameters of a full-covariance Gaussian mixture

The parameter space of EM for the
$K$-component Gaussian mixture in $d$ dimensions with full covariances is the set of parameters
$(\pi_k, \mu_k, \Sigma_k)_{k\lt K}$ that are valid: every weight $\pi_k$ is positive, the weights
sum to one, and every covariance matrix $\Sigma_k$ is positive definite.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.ValidParams`, an abbreviation declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#valid-params-3).

## Joint density of the full-covariance Gaussian mixture

For valid parameters $\theta$ with
weights $\pi_k$, means $\mu_k$ and covariances $\Sigma_k$, the joint density of a point
$x \in \mathbb{R}^d$ and a component $k$ is
$p_\theta(x, k) = \pi_k \, \mathcal{N}(x \mid \mu_k, \Sigma_k)$, where
$\mathcal{N}(x \mid \mu, \Sigma)$ is the multivariate Gaussian density.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.joint`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#joint-3).

## Responsibilities of the full-covariance Gaussian mixture

For valid parameters
$\theta = (\pi_j, \mu_j, \Sigma_j)_{j\lt K}$, a point $x \in \mathbb{R}^d$ and a component $k$, write
$p_k(x) = \pi_k \, \mathcal{N}(x \mid \mu_k, \Sigma_k)$, where $\mathcal{N}(\cdot \mid \mu, \Sigma)$
is the multivariate Gaussian density. The responsibility of $k$ for $x$ is the posterior
probability of component $k$ given $x$ (the E-step),

$$r_k(x) = \frac{p_k(x)}{\sum_j p_j(x)}.$$

For data $(x_n)_{n\lt N}$ one writes $r_{nk} = r_k(x_n)$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.resp`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#resp-3).

## Effective number of points of a full-covariance mixture component

For data
$x_1, \dots, x_N \in \mathbb{R}^d$ and valid parameters $\theta$ with responsibilities $r_{nk}$,
the effective number of points of component $k$ is $N_k = \sum_n r_{nk}$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.mass`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#mass-3).

## Mean update of the full-covariance Gaussian mixture

Given data $(x_n)_{n\lt N}$ in
$\mathbb{R}^d$, valid parameters $\theta$ and a component $k$, let $r_{nk}$ be the
responsibility of component $k$ for $x_n$ and let $N_k = \sum_n r_{nk}$. The mean update is the
responsibility-weighted mean

$$\mu_k' = \frac{1}{N_k} \sum_n r_{nk} x_n \in \mathbb{R}^d.$$

When there are no data ($N = 0$), $N_k = 0$ and the convention $N_k^{-1} = 0$ makes
$\mu_k' = 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.newMean`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#new-mean-2).

## Covariance update of the full-covariance Gaussian mixture

Given data $(x_n)_{n\lt N}$
in $\mathbb{R}^d$, valid parameters $\theta$ and a component $k$, let $r_{nk}$ be the
responsibility of component $k$ for $x_n$, let $N_k = \sum_n r_{nk}$, and let $\mu_k'$ be the
responsibility-weighted mean $N_k^{-1} \sum_n r_{nk} x_n$. The covariance update is the real
$d \times d$ matrix

$$\Sigma_k' = \frac{1}{N_k} \sum_n r_{nk} (x_n - \mu_k')(x_n - \mu_k')^{\top}.$$

When there are no data ($N = 0$), $N_k = 0$ and the convention $N_k^{-1} = 0$ makes
$\Sigma_k' = 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.newCov`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#new-cov).

## M-step of the full-covariance Gaussian mixture

For data
$x_1, \dots, x_N \in \mathbb{R}^d$ and valid parameters $\theta$ with responsibilities $r_{nk}$,
let $N_k = \sum_n r_{nk}$. The M-step parameters have weights $\pi'_k = N_k / N$, means
$\mu'_k = N_k^{-1} \sum_n r_{nk} x_n$ and covariances
$\Sigma'_k = N_k^{-1} \sum_n r_{nk} (x_n - \mu'_k)(x_n - \mu'_k)^{\top}$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.mStep`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#m-step-3).

## Data that span the space affinely

A family $(x_n)_{n\lt N}$ of points of $\mathbb{R}^d$
is in general position when it has at least one point ($N > 0$) and is not contained in an
affine hyperplane: for every nonzero $v \in \mathbb{R}^d$ there are indices $n, n'$ with
$\langle v, x_n \rangle \neq \langle v, x_{n'} \rangle$.

On such data every responsibility-weighted sample covariance is positive definite.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.SpansAffinely`, a structure declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#spans-affinely).

## The covariance update is positive definite

Let $(x_n)_{n\lt N}$ be data in $\mathbb{R}^d$
in general position: $N > 0$, and for every nonzero $v \in \mathbb{R}^d$ the values
$\langle v, x_n \rangle$ are not all equal. Then for all valid parameters $\theta$ of the
$K$-component full-covariance Gaussian mixture and every component $k$, the covariance update
$\Sigma_k'$ (the responsibility-weighted sample covariance of the data about the
responsibility-weighted mean) is positive definite.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.newCov_posDef`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#new-cov-pos-def).

## EM step for the full-covariance Gaussian mixture

For data
$x_1, \dots, x_N \in \mathbb{R}^d$ in general position (at least one point, and not all in an
affine hyperplane) and valid parameters $\theta$, the EM step returns the M-step parameters of
$\theta$: with responsibilities $r_{nk}$ under $\theta$ and $N_k = \sum_n r_{nk}$, the new
weights are $N_k / N$, the new means are the responsibility-weighted means and the new
covariances are the responsibility-weighted sample covariances. General position makes these
parameters valid.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.emStep`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-step-3).

## Component term of the EM objective for full-covariance Gaussian mixtures

Given points
$x_1, \dots, x_N$ of $\mathbb{R}^d$, valid parameters $\theta$ of a $K$-component
full-covariance Gaussian mixture, a component $k$, a mean $\mu \in \mathbb{R}^d$ and a real
$d \times d$ matrix $S$, the component term is

$$
C_k(\mu, S) = \sum_n r_{nk} \log \mathcal{N}(x_n \mid \mu, S),
$$

where $r_{nk}$ is the responsibility of component $k$ for $x_n$ under $\theta$ and
$\mathcal{N}(\cdot \mid \mu, S)$ is the multivariate Gaussian density with mean $\mu$ and
covariance matrix $S$.

The matrix $S$ is not required to be positive definite; the density is defined for every real
matrix.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.compTerm`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#comp-term-2).

## The EM objective of a full-covariance Gaussian mixture splits by component

Let
$x_1, \dots, x_N$ be points of $\mathbb{R}^d$, and let $\theta'$ and $\theta$ be valid parameters
of a $K$-component full-covariance Gaussian mixture, where $\theta'$ has weights $\pi_k'$, means
$\mu_k'$ and covariance matrices $\Sigma_k'$. Then the EM objective of the mixture's joint density
satisfies

$$
Q(\theta' \mid \theta) = \sum_k \bigl(N_k \log \pi_k' + C_k(\mu_k', \Sigma_k')\bigr),
$$

where $r_{nk}$ is the responsibility of component $k$ for $x_n$ under $\theta$,
$N_k = \sum_n r_{nk}$ and $C_k(\mu, S) = \sum_n r_{nk} \log \mathcal{N}(x_n \mid \mu, S)$, with
$\mathcal{N}(\cdot \mid \mu, S)$ the multivariate Gaussian density with mean $\mu$ and covariance
matrix $S$.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.emQ_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-q-eq-3).

## The mean and covariance updates maximize each component term

Let
$x_1, \dots, x_N \in \mathbb{R}^d$ be data in general position (at least one point, and not all
in an affine hyperplane), let $\theta$ be valid mixture parameters with responsibilities
$r_{nk}$, and fix a component $k$. Write $\mathcal{N}(x \mid \mu, S)$ for the multivariate
Gaussian density and let $\mu'_k$ and $\Sigma'_k$ be the responsibility-weighted mean and the
responsibility-weighted sample covariance of the data for component $k$. Then for every
$\mu \in \mathbb{R}^d$ and every positive definite $d \times d$ matrix $S$,

$$\sum_n r_{nk} \log \mathcal{N}(x_n \mid \mu, S) \le
\sum_n r_{nk} \log \mathcal{N}(x_n \mid \mu'_k, \Sigma'_k).$$

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.compTerm_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#comp-term-le-2).

## The weight update maximizes the weights term of the full-covariance mixture

Let
$(x_n)_{n\lt N}$ be data in $\mathbb{R}^d$ with $N > 0$, let $\theta$ be valid parameters, and let
$N_k = \sum_n r_{nk}$, where $r_{nk}$ is the responsibility of component $k$ for $x_n$. Then for
all real weights $w_k > 0$ with $\sum_k w_k = 1$,

$$\sum_k N_k \log w_k \le \sum_k N_k \log \frac{N_k}{N}.$$

The proof is Gibbs' inequality.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.sum_mass_mul_log_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#sum-mass-mul-log-le-2).

## The M-step of the full-covariance Gaussian mixture maximizes the EM objective

Let
$x_1, \dots, x_N \in \mathbb{R}^d$ be data in general position: $N > 0$, and for every nonzero
$v \in \mathbb{R}^d$ the values $\langle v, x_n \rangle$ are not all equal. Let $\theta$ be valid
parameters of a $K$-component full-covariance Gaussian mixture, and let $\theta^+$ be the result
of the EM step applied to $\theta$. Then every valid parameter $\theta'$ satisfies
$Q(\theta' \mid \theta) \le Q(\theta^+ \mid \theta)$, where $Q$ is the EM objective of the
mixture's joint density.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.emQ_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#em-q-le-em-step-3).

## Each EM step for the full-covariance Gaussian mixture does not decrease the log-likelihood

**Each EM step for the full-covariance Gaussian mixture does not decrease the
log-likelihood.** Let $x_1, \dots, x_N \in \mathbb{R}^d$ be data in general position (at least
one point, and not all in an affine hyperplane) and let $\theta$ be valid parameters. If
$\theta^{+}$ is the result of one EM step from $\theta$, then $\ell(\theta) \le \ell(\theta^{+})$,
where $\ell$ is the log-likelihood of the data under the mixture.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.logLik_le_emStep`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-lik-le-em-step-3).

## The log-likelihood is monotone along the EM iterates of a full-covariance Gaussian mixture

**The log-likelihood is monotone along the EM iterates of a full-covariance Gaussian
mixture.** Let $x_1, \dots, x_N \in \mathbb{R}^d$ be data in general position: $N > 0$, and for
every nonzero $v \in \mathbb{R}^d$ the values $\langle v, x_n \rangle$ are not all equal. Let
$\theta_0$ be valid parameters of a $K$-component full-covariance Gaussian mixture, and let
$\theta_t$ be the result of $t$ EM steps from $\theta_0$. Then $\ell(\theta_t)$ is nondecreasing
in $t \in \mathbb{N}$, where $\ell$ is the log-likelihood of the data under the mixture's joint
density.

Formalized by `Cslib.MachineLearning.LatentVariable.GaussianMixtureFullCov.logLik_iterate_emStep_monotone`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/GaussianMixtureFullCov.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html#log-lik-iterate-em-step-monotone-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mixture models](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/mixture-models)
