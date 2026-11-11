---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Bayesian.linRegPostVar, Cslib.MachineLearning.Bayesian.linRegPostMean, Cslib.MachineLearning.Bayesian.inv_linRegPostVar, Cslib.MachineLearning.Bayesian.linRegLikelihoodPDFReal, Cslib.MachineLearning.Bayesian.gaussianPDFReal_mul_linRegLikelihoodPDFReal, Cslib.MachineLearning.Bayesian.linRegEvidencePDFReal, Cslib.MachineLearning.Bayesian.gaussianPDFReal_mul_linRegLikelihoodPDFReal', Cslib.MachineLearning.Bayesian.linRegLikelihoodPDF
statement: formalized
proof: formalized
---

# Bayesian linear regression

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html).

## Posterior variance in Bayesian linear regression

For a prior variance $s_0 \ge 0$,
a noise variance $\sigma^2 \ge 0$ and inputs $x \in \mathbb{R}^n$, the posterior variance
of the weight is the nonnegative real number
$s_0 \sigma^2 / (\sigma^2 + s_0 \sum_i x_i^2)$, read as $0$ when the denominator is $0$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegPostVar`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-post-var).

## Posterior mean in Bayesian linear regression

For a prior mean $m_0 \in \mathbb{R}$,
a prior variance $s_0 \ge 0$, a noise variance $\sigma^2 \ge 0$, inputs $x \in \mathbb{R}^n$
and responses $y \in \mathbb{R}^n$, the posterior mean of the weight is the real number
$(\sigma^2 m_0 + s_0 \sum_i x_i y_i) / (\sigma^2 + s_0 \sum_i x_i^2)$, read as $0$ when
the denominator is $0$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegPostMean`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-post-mean).

## Precisions add in Bayesian linear regression

Let $s_0, \sigma^2 \ge 0$ be nonzero and
$x \in \mathbb{R}^n$. Then the posterior variance $v$ of the weight for prior variance $s_0$, noise
variance $\sigma^2$ and inputs $x$ satisfies $1 / v = 1 / s_0 + (\sum_i x_i^2) / \sigma^2$.

Formalized by `Cslib.MachineLearning.Bayesian.inv_linRegPostVar`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#inv-lin-reg-post-var).

## The linear regression likelihood density

For $\sigma^2 \ge 0$, $x, y \in \mathbb{R}^n$
and $w \in \mathbb{R}$, it is the real number $\prod_i \varphi(y_i; w x_i, \sigma^2)$, where
$\varphi(t; \mu, \tau) = (2\pi\tau)^{-1/2} e^{-(t - \mu)^2 / (2\tau)}$ is the Gaussian density
with mean $\mu$ and variance $\tau$ at $t$, read as $0$ when $\tau = 0$. For $\sigma^2 \ne 0$ it
is the Lebesgue density of the responses $y$ given the weight $w$, independent with
$y_i \sim \mathcal{N}(w x_i, \sigma^2)$. With no data ($n = 0$) it is the empty product $1$, the
density of the unit mass on the single empty response. For $\sigma^2 = 0$ and $n > 0$ the
responses are deterministic and have no density, and this formula is $0$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegLikelihoodPDFReal`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-likelihood-pdfreal).

## Completing the square for linear regression

Let $m_0 \in \mathbb{R}$, let
$s_0, \sigma^2 \ge 0$ be nonzero, and let $x, y \in \mathbb{R}^n$. Write $\varphi(t; \mu, \tau)$
for the Gaussian density with mean $\mu$ and variance $\tau$ at $t$, $p(w) = \varphi(w; m_0, s_0)$
for the prior density, $L(y \mid w) = \prod_i \varphi(y_i; w x_i, \sigma^2)$ for the likelihood
density, $m$ and $v$ for the posterior mean and variance of the weight, and
$r(w) = \varphi(w; m, v)$ for the posterior density. Then for every weight $w \in \mathbb{R}$,

$$p(w) \, L(y \mid w) \, r(m) = p(m) \, L(y \mid m) \, r(w).$$

Formalized by `Cslib.MachineLearning.Bayesian.gaussianPDFReal_mul_linRegLikelihoodPDFReal`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#gaussian-pdfreal-mul-lin-reg-likelihood).

## The evidence density of Bayesian linear regression

For $m_0 \in \mathbb{R}$,
$s_0, \sigma^2 \ge 0$ and $x, y \in \mathbb{R}^n$, let $m$ and $v$ be the posterior mean and
variance of the weight, write $\varphi(t; \mu, \tau) = (2\pi\tau)^{-1/2} e^{-(t - \mu)^2 / (2\tau)}$
for the Gaussian density with mean $\mu$ and variance $\tau$ at $t$ (read as $0$ when $\tau = 0$),
and let $L(y \mid w) = \prod_i \varphi(y_i; w x_i, \sigma^2)$ be the likelihood density. The
evidence density at $y$ is

$$Z(y) = \frac{\varphi(m; m_0, s_0) \, L(y \mid m)}{\varphi(m; m, v)},$$

prior density times likelihood divided by the posterior density, all at the posterior mean (a
quotient by $0$ is read as $0$).

For $s_0 \ne 0$ and $\sigma^2 \ne 0$ the ratio does not depend on the point where it is evaluated,
and $Z$ is the Lebesgue density of the marginal law of the data. It is not a density of the
evidence in the degenerate cases.

Formalized by `Cslib.MachineLearning.Bayesian.linRegEvidencePDFReal`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-evidence-pdfreal).

## Prior times likelihood factors as evidence times posterior

Let $m_0 \in \mathbb{R}$,
let $s_0, \sigma^2 \ge 0$ be nonzero, let $x, y \in \mathbb{R}^n$ and let $w \in \mathbb{R}$.
Write $\varphi(t; \mu, \tau)$ for the Gaussian density with mean $\mu$ and variance $\tau$ at $t$,
$L(y \mid w) = \prod_i \varphi(y_i; w x_i, \sigma^2)$ for the likelihood density, $m$ and $v$ for
the posterior mean and variance of the weight, and $Z(y)$ for the evidence density. Then
$\varphi(w; m_0, s_0) \, L(y \mid w) = Z(y) \, \varphi(w; m, v)$.

Formalized by `Cslib.MachineLearning.Bayesian.gaussianPDFReal_mul_linRegLikelihoodPDFReal'`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#gaussian-pdfreal-mul-lin-reg-likelihood-2).

## The extended-real linear regression likelihood density

For $\sigma^2 \ge 0$,
$x, y \in \mathbb{R}^n$ and $w \in \mathbb{R}$, it is $\prod_i \varphi(y_i; w x_i, \sigma^2)$ as an
extended nonnegative real, where $\varphi(t; \mu, \tau)$ is the Gaussian density with mean $\mu$
and variance $\tau$ at $t$, read as $0$ when $\tau = 0$. It is the likelihood density for
$\sigma^2 \ne 0$ or $n = 0$, and it is $0$ for $\sigma^2 = 0$ and $n > 0$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegLikelihoodPDF`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-likelihood-pdf).

## The likelihood of Bayesian linear regression

**The likelihood of Bayesian linear regression** with one feature and known noise variance
$\sigma^2 \ge 0$, for fixed inputs $x \in \mathbb{R}^n$: the kernel from the weight
$w \in \mathbb{R}$ to the responses in $\mathbb{R}^n$ under which, given $w$, the responses are
independent with $y_i \sim \mathcal{N}(w x_i, \sigma^2)$. For $\sigma^2 \ne 0$ it is given by the
density $\prod_i \varphi(y_i; w x_i, \sigma^2)$ with respect to Lebesgue measure, where
$\varphi(t; \mu, \tau)$ is the Gaussian density with mean $\mu$ and variance $\tau$ at $t$; for
$\sigma^2 = 0$ it sends $w$ to the Dirac measure at $(w x_i)_i$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegLikelihood`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-likelihood).

## The noiseless linear regression likelihood

For $x \in \mathbb{R}^n$ and
$w \in \mathbb{R}$, the linear regression likelihood with noise variance $0$ and inputs $x$, given
the weight $w$, is the Dirac measure at the vector $(w x_i)_i$: the responses are exactly
$y_i = w x_i$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegLikelihood_zero_apply`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-likelihood-zero-apply).

## The linear regression likelihood is a product of Gaussians

Let $\sigma^2 \ge 0$ be
nonzero, $x \in \mathbb{R}^n$ and $w \in \mathbb{R}$. Given the weight $w$, the linear regression
likelihood with noise variance $\sigma^2$ and inputs $x$ is the product measure
$\bigotimes_i \mathcal{N}(w x_i, \sigma^2)$ on $\mathbb{R}^n$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegLikelihood_apply`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-likelihood-apply).

## Measurability of the posterior mean in Bayesian linear regression

For a prior mean
$m_0 \in \mathbb{R}$, a prior variance $s_0 \ge 0$, a noise variance $\sigma^2 \ge 0$ and inputs
$x \in \mathbb{R}^n$, the posterior mean of the weight, as a function of the responses
$y \in \mathbb{R}^n$, is a measurable map from $\mathbb{R}^n$ to $\mathbb{R}$.

Formalized by `Cslib.MachineLearning.Bayesian.measurable_linRegPostMean`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#measurable-lin-reg-post-mean).

## The evidence of Bayesian linear regression

Let $m_0 \in \mathbb{R}$, let
$s_0, \sigma^2 \ge 0$ be nonzero, and let $x \in \mathbb{R}^n$. If the weight has prior
$\mathcal{N}(m_0, s_0)$ and the responses follow the linear regression likelihood with noise
variance $\sigma^2$ and inputs $x$, then the marginal law of the responses is the measure on
$\mathbb{R}^n$ whose density with respect to Lebesgue measure is the evidence density $Z$ for
$m_0$, $s_0$, $\sigma^2$ and $x$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegLikelihood_comp_gaussianReal`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-likelihood-comp-gaussian-real).

## Bayesian linear regression

Let $m_0 \in \mathbb{R}$, let $s_0 > 0$ and $\sigma^2 > 0$,
and let $x \in \mathbb{R}^n$ be fixed inputs. Put the prior $N(m_0, s_0)$ (mean $m_0$, variance
$s_0$) on a scalar weight $w$, and let the responses be independent given $w$ with
$y_i \sim N(w x_i, \sigma^2)$. Then for Lebesgue-almost every response vector
$y \in \mathbb{R}^n$, the posterior of $w$ given $y$ is Gaussian with mean
$(\sigma^2 m_0 + s_0 \sum_i x_i y_i) / (\sigma^2 + s_0 \sum_i x_i^2)$ and variance
$s_0 \sigma^2 / (\sigma^2 + s_0 \sum_i x_i^2)$.

Formalized by `Cslib.MachineLearning.Bayesian.posterior_linRegLikelihood_gaussianReal`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#posterior-lin-reg-likelihood-gaussian-re).

## Predictive law of a linear-regression response

For a noise variance $\sigma^2 \ge 0$
and a new input $x' \in \mathbb{R}$, the predictive kernel sends a weight $w \in \mathbb{R}$
to the Gaussian law $N(w x', \sigma^2)$ of the response at $x'$, which is the point mass at
$w x'$ when $\sigma^2 = 0$.

Formalized by `Cslib.MachineLearning.Bayesian.linRegPredictive`, a definition declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-predictive).

## Posterior predictive at a new input

Let $m_0 \in \mathbb{R}$, let $s_0 > 0$ and
$\sigma^2 > 0$, and let $x \in \mathbb{R}^n$ and $x' \in \mathbb{R}$. Put the prior
$N(m_0, s_0)$ (mean $m_0$, variance $s_0$) on a scalar weight $w$, and let the responses be
independent given $w$ with $y_i \sim N(w x_i, \sigma^2)$. Then for Lebesgue-almost every
response vector $y \in \mathbb{R}^n$, integrating the law $N(w x', \sigma^2)$ of the response
at $x'$ against the posterior of $w$ given $y$ gives the Gaussian
$N(x' m, x'^2 v + \sigma^2)$, where
$m = (\sigma^2 m_0 + s_0 \sum_i x_i y_i) / (\sigma^2 + s_0 \sum_i x_i^2)$ and
$v = s_0 \sigma^2 / (\sigma^2 + s_0 \sum_i x_i^2)$ are the posterior mean and variance.

Formalized by `Cslib.MachineLearning.Bayesian.linRegPredictive_comp_posterior`, a theorem declared in [CSLibExt/MachineLearning/Bayesian/LinearRegression.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Bayesian/LinearRegression.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html#lin-reg-predictive-comp-posterior).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bayesian linear regression](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/bayesian-inference-and-sampling/bayesian-linear-regression)
