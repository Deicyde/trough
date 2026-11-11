---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.EstimationRisk.bias, MathlibExt.Probability.Statistics.EstimationRisk.bias_eq_integral, MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError, MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError_eq_integral, MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredErrorENN, MathlibExt.Probability.Statistics.EstimationRisk.ofReal_meanSquaredError, MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredErrorENN_eq_top_of_not_finite, MathlibExt.Probability.Statistics.EstimationRisk.familyBias
statement: formalized
proof: formalized
---

# Bias and mean squared error of estimators

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html).

## Bias of an estimator

Let $S$ be a measurable space, $W : S \to \mathbb{R}$ an estimator,
$\mu$ a probability measure on $S$ for which $W$ is integrable, and $\theta \in \mathbb{R}$ a
target. The bias of $W$ under $\mu$ at $\theta$ is $\int_S W \, d\mu - \theta$, the expected value
of $W$ under $\mu$ minus $\theta$.

Integrability of $W$ is part of the input: it is the domain on which the expectation exists in
the source (Chapter 2, Definition 2.2.1), so a nonintegrable estimator has no finite bias.

## Sources

- blueprint `af_723199a7ca6fb3e936a73618`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.bias`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#bias).

## Bias as an integral

Let $S$ be a measurable space, $W : S \to \mathbb{R}$ an estimator,
$\mu$ a probability measure on $S$ for which $W$ is integrable, and $\theta \in \mathbb{R}$ a
target. Then the bias of $W$ under $\mu$ at $\theta$ equals $\int_S W \, d\mu - \theta$.

## Sources

- blueprint `af_723199a7ca6fb3e936a73618`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.bias_eq_integral`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#bias-eq-integral).

## Mean squared error

Let $\mu$ be a probability measure on a measurable space $S$, let
$W : S \to \mathbb{R}$ be an estimator and $\theta \in \mathbb{R}$ a target value, and suppose the
squared error $x \mapsto (W(x) - \theta)^2$ is $\mu$-integrable. The mean squared error of $W$ at
$\theta$ under $\mu$ is the real number $\int_S (W(x) - \theta)^2 \, d\mu(x)$.

The integrability hypothesis is part of the definition: without it no finite mean squared error is
defined.

## Sources

- Casella–Berger, Definition 7.3.1; blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error).

## Mean squared error as an integral

Let $\mu$ be a probability measure on a measurable
space $S$, let $W : S \to \mathbb{R}$ and $\theta \in \mathbb{R}$, and suppose the squared error
$x \mapsto (W(x) - \theta)^2$ is $\mu$-integrable. Then the mean squared error of $W$ at $\theta$
under $\mu$ equals $\int_S (W(x) - \theta)^2 \, d\mu(x)$.

## Sources

- blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError_eq_integral`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error-eq-integral).

## Extended mean squared error

Let $\mu$ be a probability measure on a measurable space $S$,
let $W : S \to \mathbb{R}$ be an estimator and let $\theta \in \mathbb{R}$ be a target value. The
extended mean squared error of $W$ at $\theta$ under $\mu$ is the (lower) Lebesgue integral
$\int_S (W(x) - \theta)^2 \, d\mu(x)$ of the nonnegative squared error, computed in $[0, \infty]$.
It is defined for every $W$, with no integrability hypothesis.

When the squared error is $\mu$-integrable, this value is finite and equals the mean squared error;
when the squared error is almost everywhere strongly measurable but not $\mu$-integrable, it equals
$\infty$.

## Sources

- blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredErrorENN`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error-enn).

## Finite and extended mean squared error agree

Let $\mu$ be a probability measure on a
measurable space $S$, let $W : S \to \mathbb{R}$ and $\theta \in \mathbb{R}$, and suppose the
squared error $x \mapsto (W(x) - \theta)^2$ is $\mu$-integrable. Then the extended mean squared
error $\int_S (W(x) - \theta)^2 \, d\mu(x)$, computed in $[0, \infty]$, is finite and equals the
mean squared error of $W$ at $\theta$ under $\mu$.

## Sources

- blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.ofReal_meanSquaredError`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#of-real-mean-squared-error).

## Extended mean squared error of a measurable non-integrable squared error is infinite

Let
$\mu$ be a probability measure on a measurable space $S$, $W : S \to \mathbb{R}$ an estimator and
$\theta \in \mathbb{R}$. If the squared error $x \mapsto (W(x) - \theta)^2$ is almost everywhere
strongly measurable with respect to $\mu$ but not $\mu$-integrable, then the extended mean squared
error $\int_S (W(x) - \theta)^2 \, d\mu(x) \in [0, \infty]$ of $W$ at $\theta$ equals $\infty$.

## Sources

- blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredErrorENN_eq_top_of_not_finite`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error-enn-eq-top-of-not-fin).

## Family bias of an estimator

Let $S$ be a measurable space, $W : S \to \mathbb{R}$ an
estimator, $(P_\theta)_{\theta \in \Theta}$ a family of probability measures on $S$ such that $W$
is integrable for every $P_\theta$, and $\tau : \Theta \to \mathbb{R}$ a target function. The
family bias of $W$ is the function on $\Theta$ whose value at $\theta$ is the bias of $W$ under
$P_\theta$ at the target $\tau(\theta)$, that is, $\int_S W \, dP_\theta - \tau(\theta)$.

The estimator $W$ is fixed before the family and does not depend on $\theta$.

## Sources

- blueprint `af_723199a7ca6fb3e936a73618`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.familyBias`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#family-bias).

## Family bias as an integral

Let $S$ be a measurable space, $W : S \to \mathbb{R}$ an
estimator, $(P_\theta)_{\theta \in \Theta}$ a family of probability measures on $S$ such that $W$
is integrable for every $P_\theta$, and $\tau : \Theta \to \mathbb{R}$ a target function. Then for
every $\theta \in \Theta$ the family bias of $W$ at $\theta$ equals
$\int_S W \, dP_\theta - \tau(\theta)$.

## Sources

- blueprint `af_723199a7ca6fb3e936a73618`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.familyBias_apply`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#family-bias-apply).

## Family mean squared error of an estimator

Let $S$ be a measurable space,
$W : S \to \mathbb{R}$ an estimator, $(P_\theta)_{\theta \in \Theta}$ a family of probability
measures on $S$ and $\tau : \Theta \to \mathbb{R}$ a target function such that
$(W - \tau(\theta))^2$ is integrable for $P_\theta$ for every $\theta \in \Theta$. The family mean
squared error of $W$ is the function on $\Theta$ whose value at $\theta$ is the mean squared error
of $W$ under $P_\theta$ at the target $\tau(\theta)$, that is,
$\int_S (W(x) - \tau(\theta))^2 \, dP_\theta(x)$.

The estimator $W$ is fixed before the family and does not depend on $\theta$.

## Sources

- blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.familyMeanSquaredError`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#family-mean-squared-error).

## Family mean squared error as an integral

Let $S$ be a measurable space,
$W : S \to \mathbb{R}$ an estimator, $(P_\theta)_{\theta \in \Theta}$ a family of probability
measures on $S$ and $\tau : \Theta \to \mathbb{R}$ a target function such that
$(W - \tau(\theta))^2$ is integrable for $P_\theta$ for every $\theta \in \Theta$. Then for every
$\theta \in \Theta$ the family mean squared error of $W$ at $\theta$ equals
$\int_S (W(x) - \tau(\theta))^2 \, dP_\theta(x)$.

## Sources

- blueprint `af_fd40353442120bd19166139d`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.familyMeanSquaredError_apply`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#family-mean-squared-error-apply).

## Unbiased estimator

Let $(P_\theta)_{\theta \in \Theta}$ be a family of probability measures
on a measurable space $S$ and $\tau : \Theta \to \mathbb{R}$ a target function. An estimator
$W : S \to \mathbb{R}$ is unbiased for $\tau$ if for every $\theta \in \Theta$ the function $W$ is
$P_\theta$-integrable and $\int_S W \, dP_\theta = \tau(\theta)$.

Integrability is part of the definition, so a non-integrable estimator is never unbiased. The
estimator $W$ is fixed and does not depend on $\theta$.

## Sources

- Casella–Berger Definition 7.3.2 is the case $\tau(\theta) = \theta$ on real parameters; the general target follows section 7.3.2. Blueprint `af_95118d196fd6478105a6eb43`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.IsUnbiased`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#is-unbiased).

## Unbiased estimators are integrable

Let $(P_\theta)_{\theta \in \Theta}$ be a family of
probability measures on $S$ and $\tau : \Theta \to \mathbb{R}$ a target function. If an estimator
$W : S \to \mathbb{R}$ is unbiased for $\tau$, then $W$ is $P_\theta$-integrable for every
$\theta \in \Theta$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.IsUnbiased.integrable`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#integrable).

## An unbiased estimator has the target as its expectation

Let $S$ be a measurable space,
$W : S \to \mathbb{R}$ an estimator, $(P_\theta)_{\theta \in \Theta}$ a family of probability
measures on $S$ and $\tau : \Theta \to \mathbb{R}$ a target function. If $W$ is unbiased for
$\tau$ under the family $(P_\theta)$, then $\int_S W \, dP_\theta = \tau(\theta)$ for every
$\theta \in \Theta$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.IsUnbiased.expect_eq`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#expect-eq).

## An estimator is unbiased exactly when its bias vanishes

Let
$(P_\theta)_{\theta \in \Theta}$ be a family of probability measures on $S$,
$\tau : \Theta \to \mathbb{R}$ a target function, and $W : S \to \mathbb{R}$ an estimator that is
$P_\theta$-integrable for every $\theta \in \Theta$. Then $W$ is unbiased for $\tau$ if and only if
its family bias $\int_S W \, dP_\theta - \tau(\theta)$ is zero for every $\theta \in \Theta$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.isUnbiased_iff_forall_familyBias_eq_zero`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#is-unbiased-iff-forall-family-bias-eq-ze).

## A finite second moment makes the squared error integrable

Let $\mu$ be a probability
measure on $S$ and $W : S \to \mathbb{R}$ an estimator in $L^2(\mu)$. Then for every
$\theta \in \mathbb{R}$ the squared error $x \mapsto (W(x) - \theta)^2$ is $\mu$-integrable.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.integrable_sq_sub_of_memLp_two`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#integrable-sq-sub-of-mem-lp-two).

## Bias–variance decomposition of the mean squared error

Let $\mu$ be a probability measure
on a measurable space $S$, let $\theta \in \mathbb{R}$, and let $W : S \to \mathbb{R}$ be
square-integrable with respect to $\mu$, that is, $W \in L^2(\mu)$. Then the mean squared error of
$W$ at $\theta$ under $\mu$ equals $\operatorname{Var}_\mu(W) + b^2$, where
$b = \int_S W \, d\mu - \theta$ is the bias of $W$ at $\theta$ under $\mu$.

The integrability that the mean squared error and the bias require follows from $W \in L^2(\mu)$.

## Sources

- Casella–Berger, equation (7.3.1); blueprint `af_3a1bafba0b7dff99554b01f0`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError_eq_variance_add_sq_bias`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error-eq-variance-add-sq-bi).

## Mean squared error as variance plus squared mean deviation

Let $\mu$ be a probability
measure on a measurable space $S$, let $\theta \in \mathbb{R}$, and let $W : S \to \mathbb{R}$ be
square-integrable with respect to $\mu$, that is, $W \in L^2(\mu)$. Then the mean squared error of
$W$ at $\theta$ under $\mu$ equals
$\operatorname{Var}_\mu(W) + \left(\int_S W \, d\mu - \theta\right)^2$.

## Sources

- Casella–Berger, equation (7.3.1) in expectation form; blueprint `af_3a1bafba0b7dff99554b01f0`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError_eq_variance_add_sq_expectation_sub`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error-eq-variance-add-sq-ex).

## Bias–variance decomposition of the extended mean squared error

Let $\mu$ be a probability
measure on a measurable space $S$, let $\theta \in \mathbb{R}$, and let $W : S \to \mathbb{R}$ be
square-integrable with respect to $\mu$, that is, $W \in L^2(\mu)$. Then the extended mean squared
error $\int_S (W(x) - \theta)^2 \, d\mu(x)$, computed in $[0, \infty]$, is finite and equals
$\operatorname{Var}_\mu(W) + b^2$, where $b = \int_S W \, d\mu - \theta$ is the bias of $W$ at
$\theta$ under $\mu$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.ofReal_variance_add_sq_bias`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#of-real-variance-add-sq-bias).

## Bias–variance decomposition for a parametric family

Let $S$ be a measurable space,
$W : S \to \mathbb{R}$ an estimator, $(P_\theta)_{\theta \in \Theta}$ a family of probability
measures on $S$ and $\tau : \Theta \to \mathbb{R}$ a target function. Suppose that for every
$\theta \in \Theta$, $W$ has a finite second moment under $P_\theta$, and $W$ and
$(W - \tau(\theta))^2$ are integrable for $P_\theta$. Then for every $\theta \in \Theta$ the family
mean squared error of $W$ at $\theta$ equals the variance $\operatorname{Var}_{P_\theta}(W)$ of
$W$ under $P_\theta$ plus the square of the family bias of $W$ at $\theta$.

## Sources

- equation 7.3.1, in family form for a single fixed estimator.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.familyMeanSquaredError_eq_variance_add_sq_familyBias`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#family-mean-squared-error-eq-variance-ad).

## Mean squared error of an unbiased estimator

Let $\mu$ be a probability measure on a
measurable space $S$, let $\theta \in \mathbb{R}$, and let $W : S \to \mathbb{R}$ be
square-integrable with respect to $\mu$ (that is, $W \in L^2(\mu)$) and satisfy
$\int_S W \, d\mu = \theta$. Then the mean squared error of $W$ at $\theta$ under $\mu$ equals
$\operatorname{Var}_\mu(W)$.

## Sources

- the display following Definition 7.3.2.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.meanSquaredError_eq_variance_of_expect_eq`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#mean-squared-error-eq-variance-of-expect).

## An unbiased estimator has mean squared error equal to its variance

Let $S$ be a
measurable space, $W : S \to \mathbb{R}$ an estimator, $(P_\theta)_{\theta \in \Theta}$ a family of
probability measures on $S$ and $\tau : \Theta \to \mathbb{R}$ a target function. Suppose that $W$
is unbiased for $\tau$ under the family, and that for every $\theta \in \Theta$, $W$ has a finite
second moment under $P_\theta$ and $(W - \tau(\theta))^2$ is integrable for $P_\theta$. Then for
every $\theta \in \Theta$ the family mean squared error of $W$ at $\theta$ equals the variance
$\operatorname{Var}_{P_\theta}(W)$ of $W$ under $P_\theta$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.IsUnbiased.familyMeanSquaredError_eq_variance`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#family-mean-squared-error-eq-variance).

## Frequentist risk

Let $S$ be a measurable space, $\delta : S \to A$ a decision rule,
$(P_\theta)_{\theta \in \Theta}$ a family of probability measures on $S$, and
$\ell : \Theta \times A \to [0, \infty)$ a loss such that $x \mapsto \ell(\theta, \delta(x))$ is
$P_\theta$-integrable for every $\theta \in \Theta$. The frequentist risk of $\delta$ is the
function $\Theta \to \mathbb{R}$ given by
$R(\theta, \delta) = \int_S \ell(\theta, \delta(x)) \, dP_\theta(x)$.

The rule $\delta$ does not depend on $\theta$, and the action space $A$ may differ from $\Theta$.
No prior, kernel or optimality criterion enters.

## Sources

- Casella–Berger equation 7.3.16; the integrability hypothesis is the expectation domain of Chapter 2 Definition 2.2.1. Blueprint `af_36871388da7326a07a5e4f71`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.frequentistRisk`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#frequentist-risk).

## Frequentist risk as an integral

Let $S$ be a measurable space, $\delta : S \to A$ a
decision rule, $(P_\theta)_{\theta \in \Theta}$ a family of probability measures on $S$ and
$\ell : \Theta \times A \to [0, \infty)$ a loss function such that
$x \mapsto \ell(\theta, \delta(x))$ is integrable for $P_\theta$ for every $\theta \in \Theta$.
Then for every $\theta \in \Theta$ the frequentist risk of $\delta$ at $\theta$ equals
$\int_S \ell(\theta, \delta(x)) \, dP_\theta(x)$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.frequentistRisk_apply`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#frequentist-risk-apply).

## Frequentist risk is nonnegative

Let $\delta : S \to A$ be a decision rule,
$(P_\theta)_{\theta \in \Theta}$ a family of probability measures on $S$, and
$\ell : \Theta \times A \to [0, \infty)$ a loss such that $x \mapsto \ell(\theta, \delta(x))$ is
$P_\theta$-integrable for every $\theta \in \Theta$. Then the frequentist risk $R(\theta, \delta)$
of $\delta$ at $\theta$ is nonnegative for every $\theta \in \Theta$.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.frequentistRisk_nonneg`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#frequentist-risk-nonneg).

## Extended frequentist risk

Let $S$ be a measurable space, $\delta : S \to A$ a decision
rule, $(P_\theta)_{\theta \in \Theta}$ a family of probability measures on $S$, and
$\ell : \Theta \times A \to [0, \infty)$ a loss. The extended frequentist risk of $\delta$ at
$\theta \in \Theta$ is the Lebesgue integral $\int_S \ell(\theta, \delta(x)) \, dP_\theta(x)$, taken
in $[0, \infty]$.

When the loss is $P_\theta$-integrable for every $\theta$, this is the frequentist risk; when it is
measurable but not integrable at $\theta$, it equals $\infty$.

## Sources

- blueprint `af_36871388da7326a07a5e4f71`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.frequentistRiskENN`, a definition declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#frequentist-risk-enn).

## Finite and extended frequentist risk agree

Let $\Theta$ and $A$ be sets, let
$(P_\vartheta)_{\vartheta \in \Theta}$ be a family of probability measures on a measurable space
$S$, let $\delta : S \to A$ be a decision rule and $\ell : \Theta \times A \to [0, \infty)$ a
loss, and suppose $x \mapsto \ell(\vartheta, \delta(x))$ is $P_\vartheta$-integrable for every
$\vartheta \in \Theta$. Then for every $\theta \in \Theta$ the extended frequentist risk
$\int_S \ell(\theta, \delta(x)) \, dP_\theta(x)$, computed in $[0, \infty]$, is finite and equals
the frequentist risk of $\delta$ at $\theta$.

## Sources

- blueprint `af_36871388da7326a07a5e4f71`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.ofReal_frequentistRisk`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#of-real-frequentist-risk).

## Extended frequentist risk of a measurable non-integrable loss is infinite

Let $S$ be a
measurable space, $\delta : S \to A$ a decision rule, $(P_\theta)_{\theta \in \Theta}$ a family of
probability measures on $S$, $\ell : \Theta \times A \to [0, \infty)$ a loss, and
$\theta \in \Theta$. If the function $x \mapsto \ell(\theta, \delta(x))$ is almost everywhere
strongly measurable with respect to $P_\theta$ but not $P_\theta$-integrable, then the extended
frequentist risk $\int_S \ell(\theta, \delta(x)) \, dP_\theta(x) \in [0, \infty]$ of $\delta$ at
$\theta$ equals $\infty$.

So a measurable non-integrable loss is never assigned a finite extended risk.

## Sources

- blueprint `af_36871388da7326a07a5e4f71`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.frequentistRiskENN_eq_top_of_not_integrable`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#frequentist-risk-enn-eq-top-of-not-integ).

## Mean squared error is frequentist risk under squared-error loss

Let
$(P_\theta)_{\theta \in \Theta}$ be a family of probability measures on $S$,
$W : S \to \mathbb{R}$ an estimator and $\tau : \Theta \to \mathbb{R}$ a target function such that
$x \mapsto (W(x) - \tau(\theta))^2$ is $P_\theta$-integrable for every $\theta \in \Theta$. Then for
every $\theta$, the frequentist risk at $\theta$ of $W$, as a decision rule with actions in
$\mathbb{R}$, under the squared-error loss $\ell(\theta, a) = (a - \tau(\theta))^2$ equals the
family mean squared error of $W$ for $\tau$ at $\theta$.

## Sources

- blueprint `af_36871388da7326a07a5e4f71`.

Formalized by `MathlibExt.Probability.Statistics.EstimationRisk.frequentistRisk_squared_eq_familyMeanSquaredError`, a theorem declared in [MathlibExt/Probability/Statistics/EstimationRisk.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/EstimationRisk.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html#frequentist-risk-squared-eq-family-mean).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bias and mean squared error of estimators](https://deicyde.github.io/atlas-lean/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/statistical-estimation/bias-and-mean-squared-error-of-estimators)
