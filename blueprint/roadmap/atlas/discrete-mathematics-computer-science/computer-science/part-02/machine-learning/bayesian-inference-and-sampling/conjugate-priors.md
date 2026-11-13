---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Bayesian.binomialKernel, Cslib.MachineLearning.Bayesian.beta_add_one_left, Cslib.MachineLearning.Bayesian.betaPDFReal_mul_pow, Cslib.MachineLearning.Bayesian.betaPDF_mul_binomialKernel, Cslib.MachineLearning.Bayesian.binomialKernel_comp_betaMeasure, Cslib.MachineLearning.Bayesian.posterior_binomialKernel_betaMeasure, Cslib.MachineLearning.Bayesian.binomialKernel_one_comp_betaMeasure, Cslib.MachineLearning.Bayesian.posterior_predictive_betaMeasure
statement: formalized
proof: formalized
---

# Conjugate priors

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html).

## Binomial likelihood kernel

For a natural number $n$, the binomial kernel sends a real
$\theta$ to the binomial distribution $\mathrm{Bin}(n, p)$ on $\mathbb{N}$, the law of the number of
successes in $n$ independent coin flips with success probability $p$, where $p$ is $\theta$
clipped to $[0, 1]$.

Formalized by `Cslib.MachineLearning.Bayesian.binomialKernel`, a definition declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#binomial-kernel).

## Recurrence for the beta function in the first argument

For real $a > 0$ and $b > 0$, the
beta function $B(a, b) = \Gamma(a)\Gamma(b)/\Gamma(a + b)$ satisfies
$B(a + 1, b) = B(a, b) \cdot \frac{a}{a + b}$.

Formalized by `Cslib.MachineLearning.Bayesian.beta_add_one_left`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#beta-add-one-left).

## Conjugacy of the beta density

Let $a, b > 0$ be real, $k, m$ natural numbers and
$\theta$ real. Write $f_{a,b}$ for the $\mathrm{Beta}(a, b)$ density (zero outside $(0, 1)$) and
$B(a, b) = \Gamma(a)\Gamma(b)/\Gamma(a + b)$ for the beta function. Then
$f_{a,b}(\theta) \, \theta^k (1 - \theta)^m =
\frac{B(a + k, b + m)}{B(a, b)} f_{a + k, b + m}(\theta)$.

Formalized by `Cslib.MachineLearning.Bayesian.betaPDFReal_mul_pow`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#beta-pdfreal-mul-pow).

## Beta prior times binomial likelihood

Let $a, b > 0$ be real, $n, k$ natural numbers,
$m = n - k$ if $k \le n$ and $m = 0$ otherwise, and $\theta$ real. Write $f_{a,b}$ for the
$\mathrm{Beta}(a, b)$ density (zero outside $(0, 1)$) and $B$ for the beta function. Then the
density $f_{a,b}(\theta)$ times the probability that the binomial kernel at $\theta$ gives exactly
$k$ successes in $n$ trials equals
$\binom{n}{k} \frac{B(a + k, b + m)}{B(a, b)} f_{a + k, b + m}(\theta)$, as an identity in
$[0, \infty]$.

Formalized by `Cslib.MachineLearning.Bayesian.betaPDF_mul_binomialKernel`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#beta-pdf-mul-binomial-kernel).

## The beta-binomial distribution

Let $a, b > 0$ be real, $n, k$ natural numbers and
$B(x, y) = \Gamma(x)\Gamma(y)/\Gamma(x + y)$ the beta function. Under a $\mathrm{Beta}(a, b)$
prior on the success probability, the marginal probability (the evidence) that the binomial kernel
gives exactly $k$ successes in $n$ trials is $\binom{n}{k} \frac{B(a + k, b + n - k)}{B(a, b)}$,
where $n - k$ is truncated at $0$.

Formalized by `Cslib.MachineLearning.Bayesian.binomialKernel_comp_betaMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#binomial-kernel-comp-beta-measure).

## Beta–binomial conjugacy

Let $a, b > 0$ be real and $k \le n$ natural numbers. For the
binomial kernel and a $\mathrm{Beta}(a, b)$ prior, the posterior distribution (Mathlib's posterior
kernel) after observing $k$ successes in $n$ trials is $\mathrm{Beta}(a + k, b + n - k)$.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_binomialKernel_betaMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#posterior-binomial-kernel-beta-measure).

## Prior predictive probability of a success

Let $a, b > 0$ be real. Under a
$\mathrm{Beta}(a, b)$ prior on the success probability, the probability that a single trial of the
binomial kernel succeeds is the prior mean $a / (a + b)$.

Formalized by `Cslib.MachineLearning.Bayesian.binomialKernel_one_comp_betaMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#binomial-kernel-one-comp-beta-measure).

## Posterior predictive of the beta-binomial model

Let $a, b > 0$ be real and $k \le n$
natural numbers. Under a $\mathrm{Beta}(a, b)$ prior on the success probability, after observing
$k$ successes in $n$ trials of the binomial kernel, the posterior predictive probability that one
further trial succeeds is $(a + k) / (a + b + n)$.

For $a = b = 1$ this is Laplace's rule of succession, $(k + 1) / (n + 2)$.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_predictive_betaMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/BetaBinomial.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#posterior-predictive-beta-measure).

## Probability vectors

For $n \in \mathbb{N}$, the probability vectors are the
$\theta \in \mathbb{R}^{n+1}$ with $\theta_i \ge 0$ for every $i$ and $\sum_i \theta_i = 1$; they
form the parameter space of the categorical model.

Formalized by `Cslib.MachineLearning.Bayesian.probVectors`, a definition declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#prob-vectors).

## The categorical likelihood

For $n \in \mathbb{N}$, the categorical likelihood is the
kernel from parameters $\theta \in \mathbb{R}^{n+1}$ to labels $\{0, \dots, n\}$ that sends a
probability vector $\theta$ (all $\theta_i \ge 0$ and $\sum_i \theta_i = 1$) to the law of one
label drawn with probability $\theta_i$ for label $i$, and sends every other $\theta$ to the
point mass at label $0$.

Parameters outside the probability vectors form a null set under a Dirichlet prior.

Formalized by `Cslib.MachineLearning.Bayesian.categoricalKernel`, a definition declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#categorical-kernel).

## Likelihood of a label sequence

For $\theta \in \mathbb{R}^{n+1}$ and a sequence
$s = (s_0, \dots, s_{N-1})$ of labels in $\{0, \dots, n\}$, the likelihood of $s$ is the
extended nonnegative real $\prod_{m < N} \theta_{s_m}^+$, where $x^+ = \max(x, 0)$.

Formalized by `Cslib.MachineLearning.Bayesian.seqLikelihood`, a definition declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#seq-likelihood).

## The multinomial sampling model

For $n, N \in \mathbb{N}$, the multinomial sampling
model is the kernel from parameters $\theta \in \mathbb{R}^{n+1}$ to sequences
$s = (s_0, \dots, s_{N-1})$ of $N$ labels in $\{0, \dots, n\}$ that sends a probability vector
$\theta$ (all $\theta_i \ge 0$ and $\sum_i \theta_i = 1$) to the law of $N$ independent draws
from $\theta$, which gives $s$ probability $\prod_{m < N} \theta_{s_m}$, and sends every other
$\theta$ to the point mass at the all-zero sequence.

Formalized by `Cslib.MachineLearning.Bayesian.categoricalSeqKernel`, a definition declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#categorical-seq-kernel).

## Label counts

For a sequence $s = (s_0, \dots, s_{N-1})$ of labels in $\{0, \dots, n\}$
and a label $i$, the count $n_i(s)$ is the number of positions $m < N$ with $s_m = i$.

Formalized by `Cslib.MachineLearning.Bayesian.counts`, a definition declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#counts).

## The sequence likelihood depends only on the label counts

For every
$\theta \in \mathbb{R}^{n+1}$ and every sequence $s$ of $N$ labels in $\{0, \dots, n\}$ with
label counts $n_i(s)$, the likelihood $\prod_{m < N} \theta_{s_m}^+$ of $s$ equals
$\prod_{i = 0}^{n} (\theta_i^+)^{n_i(s)}$ as extended nonnegative reals, where
$x^+ = \max(x, 0)$.

Formalized by `Cslib.MachineLearning.Bayesian.seqLikelihood_eq_prod_pow`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#seq-likelihood-eq-prod-pow).

## Evidence-weighted Dirichlet prior

Let $\alpha \in \mathbb{R}^{n+1}$ with $\alpha_i > 0$
for every $i$, and let $s$ be a sequence of $N$ labels in $\{0, \dots, n\}$ with label counts
$n_i(s)$. The Dirichlet distribution $\mathrm{Dir}(\alpha)$ weighted by the density
$\theta \mapsto P_\theta(s)$, the probability of $s$ under the multinomial sampling model with
parameter $\theta$, equals $B(\alpha + n(s)) / B(\alpha)$ times $\mathrm{Dir}(\alpha + n(s))$,
where $B$ is the multivariate Beta function and $\alpha + n(s)$ has entries $\alpha_i + n_i(s)$.

Formalized by `Cslib.MachineLearning.Bayesian.withDensity_categoricalSeqKernel`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#with-density-categorical-seq-kernel).

## Dirichlet–multinomial conjugacy

Let $\alpha \in \mathbb{R}^{n+1}$ with $\alpha_i > 0$
for every $i$, and let $s$ be a sequence of $N$ labels in $\{0, \dots, n\}$ with label counts
$n_i(s)$. Under the multinomial sampling model with the Dirichlet prior $\mathrm{Dir}(\alpha)$,
the posterior distribution of the parameter after observing $s$ is the Dirichlet distribution
with parameters $\alpha_i + n_i(s)$.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_categoricalSeqKernel_dirichletMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#posterior-categorical-seq-kernel-dirichl).

## Prior predictive of the Dirichlet–categorical model

Let $\alpha \in \mathbb{R}^{n+1}$
with $\alpha_i > 0$ for every $i$. Drawing a parameter $\theta$ from the Dirichlet
distribution $\mathrm{Dir}(\alpha)$ and then one label from the categorical likelihood with
parameter $\theta$ gives the label $i \in \{0, \dots, n\}$ with probability
$\alpha_i / \sum_j \alpha_j$, which is the mean of $\theta_i$ under $\mathrm{Dir}(\alpha)$.

Formalized by `Cslib.MachineLearning.Bayesian.categoricalKernel_comp_dirichletMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#categorical-kernel-comp-dirichlet-measur).

## Posterior predictive of the Dirichlet–multinomial model

Let $\alpha \in \mathbb{R}^{n+1}$
with $\alpha_i > 0$ for every $i$, and let $s$ be a sequence of $N$ labels in $\{0, \dots, n\}$
with label counts $n_i(s)$. Under the multinomial sampling model with the Dirichlet prior
$\mathrm{Dir}(\alpha)$, drawing a parameter from the posterior after observing $s$ and then one
label from the categorical likelihood gives the label $i$ with probability
$(\alpha_i + n_i(s)) / (\sum_j \alpha_j + N)$.

This is the Dirichlet–multinomial analogue of Laplace's rule of succession.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_predictive_dirichletMeasure`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/DirichletMultinomial.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#posterior-predictive-dirichlet-measure).

## Posterior variance of the normal–normal model

For variances $v_0, v \ge 0$, the posterior
variance is $\frac{v_0 v}{v_0 + v}$, taken to be $0$ when $v_0 = v = 0$. In the normal–normal model
with prior variance $v_0$ and known noise variance $v$, this is the variance of the posterior of the
mean after one observation.

Formalized by `Cslib.MachineLearning.Bayesian.normalPostVar`, a definition declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#normal-post-var).

## Posterior mean of the Normal–Normal model

For a prior mean $m_0 \in \mathbb{R}$, a prior
variance $v_0 \ge 0$, a noise variance $v \ge 0$ and an observation $x \in \mathbb{R}$, the
posterior mean is $(v m_0 + v_0 x)/(v_0 + v)$, taken to be $0$ when $v_0 = v = 0$. When
$v_0 + v > 0$ it is the precision-weighted average of $m_0$ and $x$.

Formalized by `Cslib.MachineLearning.Bayesian.normalPostMean`, a definition declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#normal-post-mean).

## Posterior mean as a gain update

Let $m_0, x \in \mathbb{R}$, $v_0 > 0$ and $v \ge 0$. The
posterior mean $(v m_0 + v_0 x)/(v_0 + v)$ equals $m_0 + \frac{v_0}{v_0 + v}(x - m_0)$: it moves
from the prior mean $m_0$ toward the observation $x$ by the gain $v_0/(v_0 + v)$.

Formalized by `Cslib.MachineLearning.Bayesian.normalPostMean_eq`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#normal-post-mean-eq).

## Precisions add

For variances $v_0, v > 0$, the posterior variance $s = v_0 v/(v_0 + v)$
satisfies $s^{-1} = v_0^{-1} + v^{-1}$.

Formalized by `Cslib.MachineLearning.Bayesian.inv_normalPostVar`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#inv-normal-post-var).

## Completing the square

Let $m_0, \theta, x \in \mathbb{R}$ and $v_0, v > 0$, and write
$\varphi_{\mu, s}(y) = (2 \pi s)^{-1/2} \exp(-(y - \mu)^2 / (2 s))$ for the density of the Gaussian
with mean $\mu$ and variance $s$. With $\mu(x) = (v m_0 + v_0 x)/(v_0 + v)$ and
$s = v_0 v/(v_0 + v)$,

$$
\varphi_{m_0, v_0}(\theta)\,\varphi_{\theta, v}(x) =
\varphi_{m_0, v_0 + v}(x)\,\varphi_{\mu(x), s}(\theta):
$$

the prior density at $\theta$ times the likelihood of $x$ is the marginal density of $x$ times the
posterior density at $\theta$.

Formalized by `Cslib.MachineLearning.Bayesian.gaussianPDFReal_mul_gaussianPDFReal`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#gaussian-pdfreal-mul-gaussian-pdfreal).

## Measurability of the Gaussian density in its mean and argument

For a variance $v \ge 0$,
write $\varphi_{\theta, v}(x) = (2 \pi v)^{-1/2} \exp(-(x - \theta)^2 / (2 v))$ for the density
at $x$ of the Gaussian with mean $\theta$ and variance $v$, read as $0$ when $v = 0$, with values
in $[0, \infty]$. Then $(\theta, x) \mapsto \varphi_{\theta, v}(x)$ is a measurable map on
$\mathbb{R} \times \mathbb{R}$.

Formalized by `Cslib.MachineLearning.Bayesian.measurable_gaussianPDF_mean`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#measurable-gaussian-pdf-mean).

## Gaussian likelihood with known variance

For a noise variance $v \ge 0$, the Gaussian
likelihood is the kernel from $\mathbb{R}$ to $\mathbb{R}$ that sends a parameter $\theta$ to the
law of the observation $x \sim N(\theta, v)$, the Gaussian with mean $\theta$ and variance $v$: for
$v > 0$ it is the measure with the $N(\theta, v)$ density with respect to Lebesgue measure, and for
$v = 0$ it is the point mass at $\theta$.

Formalized by `Cslib.MachineLearning.Bayesian.gaussianLikelihood`, a definition declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#gaussian-likelihood).

## Noiseless Gaussian likelihood

With noise variance $0$, the Gaussian likelihood sends each
$\theta \in \mathbb{R}$ to the Gaussian law with mean $\theta$ and variance $0$, which is the point
mass at $\theta$: the observation is the parameter.

Formalized by `Cslib.MachineLearning.Bayesian.gaussianLikelihood_zero_apply`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#gaussian-likelihood-zero-apply).

## The marginal of the data

Let $m_0 \in \mathbb{R}$ and $v_0, v > 0$, and write
$N(\mu, s)$ for the Gaussian law with mean $\mu$ and variance $s$. If the parameter $\theta$ has
prior $N(m_0, v_0)$ and the observation given $\theta$ has law $N(\theta, v)$ (the Gaussian
likelihood with noise variance $v$), then the marginal law of the observation is $N(m_0, v_0 + v)$.

Applied with the posterior in place of the prior, this also gives the posterior predictive law.

Formalized by `Cslib.MachineLearning.Bayesian.gaussianLikelihood_comp_gaussianReal`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#gaussian-likelihood-comp-gaussian-real).

## Candidate posterior kernel of the normal–normal model

Let $m_0 \in \mathbb{R}$ and
$v_0, v \ge 0$, let $s = \frac{v_0 v}{v_0 + v}$ be the posterior variance and, for
$x \in \mathbb{R}$, let $\mu(x) = \frac{v m_0 + v_0 x}{v_0 + v}$ be the posterior mean (with
$0 / 0 = 0$). The kernel from $\mathbb{R}$ to $\mathbb{R}$ sends $x$ to the measure with density
$\theta \mapsto \frac{1}{\sqrt{2 \pi s}} e^{-(\theta - \mu(x))^2 / (2 s)}$ with respect to Lebesgue
measure. For $v_0, v > 0$ this is the normal law $N(\mu(x), s)$. If $v_0 = 0$ or $v = 0$, then
$s = 0$, the density is taken to be $0$, and the kernel is the zero measure at every $x$.

Formalized by `Cslib.MachineLearning.Bayesian.normalPosteriorKernel`, a definition declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#normal-posterior-kernel).

## Disintegration of the Normal–Normal joint law

Let $m_0 \in \mathbb{R}$ and $v_0, v > 0$,
and write $N(\mu, s)$ for the Gaussian law with mean $\mu$ and variance $s$. Let $\pi = N(m_0, v_0)$
be the prior on the parameter $\theta$, let $K$ be the Gaussian likelihood with noise variance $v$,
so that $K(\theta) = N(\theta, v)$, and let $Q$ be the normal posterior kernel,
$Q(x) = N(\mu(x), s)$ with $\mu(x) = (v m_0 + v_0 x)/(v_0 + v)$ and $s = v_0 v/(v_0 + v)$. For a
measure $\rho$ and a kernel $L$, write $L \circ \rho = \int L(y)\,d\rho(y)$ and $\rho \otimes L$ for
the law of $(y, z)$ when $y \sim \rho$ and $z \sim L(y)$. Then $(K \circ \pi) \otimes Q$ is the
image of $\pi \otimes K$ under $(\theta, x) \mapsto (x, \theta)$: the joint law of $(x, \theta)$ is
the marginal law $K \circ \pi$ of $x$ followed by the posterior kernel.

Formalized by `Cslib.MachineLearning.Bayesian.compProd_normalPosteriorKernel`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#comp-prod-normal-posterior-kernel).

## Normal–Normal conjugacy with known variance

Let $m_0 \in \mathbb{R}$ and $v_0, v > 0$. Take
the prior $N(m_0, v_0)$ on the mean $\theta$ and the likelihood under which an observation $x$ has
law $N(\theta, v)$. Then for Lebesgue-almost every $x \in \mathbb{R}$, the posterior distribution of
$\theta$ given $x$ is the normal law with mean $\frac{v m_0 + v_0 x}{v_0 + v}$ and variance
$\frac{v_0 v}{v_0 + v}$.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_gaussianLikelihood_gaussianReal`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#posterior-gaussian-likelihood-gaussian-r).

## Normal–Normal posterior predictive

Let $m_0 \in \mathbb{R}$ and $v_0, v > 0$, and write
$N(\mu, s)$ for the Gaussian law with mean $\mu$ and variance $s$. Take the prior $N(m_0, v_0)$ on
the parameter $\theta$ and the Gaussian likelihood $\theta \mapsto N(\theta, v)$, and let
$\mu(x) = (v m_0 + v_0 x)/(v_0 + v)$ and $s = v_0 v/(v_0 + v)$. For Lebesgue-almost every
observation $x$, a new observation drawn from the likelihood, with $\theta$ distributed according
to the posterior given $x$, has law $N(\mu(x), s + v)$.

Formalized by `Cslib.MachineLearning.Bayesian.gaussianLikelihood_comp_posterior`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/NormalNormal.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/Bayesian/NormalNormal.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html#gaussian-likelihood-comp-posterior).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugate priors](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/conjugate-priors)
