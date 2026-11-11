---
declaration: section
origin: cited
lean: MetaMathlibExt.log_multivariateGaussianPDFReal, MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_eq, MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_le_weightedMean, MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_le_of_posDef, MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_le
statement: formalized
proof: formalized
---

# Gaussian maximum likelihood

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html).

## Log-density of the multivariate Gaussian

Let $J$ be a finite set with $n$ elements, let
$\mu, x \in \mathbb{R}^J$, let $S$ be a positive definite real $J \times J$ matrix, and write
$\mathcal{N}(x \mid \mu, S)$ for the multivariate Gaussian density at $x$ with mean $\mu$ and
covariance $S$. Then $\log \mathcal{N}(x \mid \mu, S) = -\frac{n}{2} \log (2\pi) -
\frac{1}{2} \log \det S - \frac{1}{2} (x - \mu)^{\mathsf T} S^{-1} (x - \mu)$.

Formalized by `MetaMathlibExt.log_multivariateGaussianPDFReal`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianMLE.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianMLE.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html#log-multivariate-gaussian-pdfreal).

## The weighted Gaussian log-likelihood via the scatter matrix

Let $I$ be a finite set and
$J$ a finite set with $n$ elements, let $x_i \in \mathbb{R}^J$ ($i \in I$) be points with real
weights $w_i$ whose sum $W = \sum_{i \in I} w_i$ is nonzero, let $\mu \in \mathbb{R}^J$, let $S$
be a positive definite real $J \times J$ matrix, and let $C(\mu)$ be the weighted scatter matrix
of the $x_i$ about $\mu$. Write $\mathcal{N}(x \mid \mu, S)$ for the multivariate Gaussian
density at $x$ with mean $\mu$ and covariance $S$. Then
$\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid \mu, S) = -\frac{W}{2} \big(n \log (2\pi) +
\log \det S + \operatorname{tr}(S^{-1} C(\mu))\big)$.

Formalized by `MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_eq`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianMLE.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianMLE.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html#sum-mul-log-multivariate-gaussian-pdfrea).

## The weighted mean is the Gaussian MLE of the mean

Let $I$ and $J$ be finite sets, let
$x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$ such that $\sum_i w_i > 0$,
let $m$ be their weighted mean, and let $S$ be a positive definite real $J \times J$ matrix.
Write $\mathcal{N}(x \mid \mu, S)$ for the multivariate Gaussian density at $x$ with mean $\mu$
and covariance $S$. Then for every $\mu \in \mathbb{R}^J$,
$\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid \mu, S) \le
\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid m, S)$.

Formalized by `MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_le_weightedMean`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianMLE.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianMLE.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html#sum-mul-log-multivariate-gaussian-pdfrea-2).

## The weighted Gaussian MLE when the sample covariance is positive definite

Let $I$ and
$J$ be finite sets, let $x_i \in \mathbb{R}^J$ ($i \in I$) be points with real weights $w_i$ such
that $\sum_i w_i > 0$, let $m$ be their weighted mean, and let $C$ be their weighted scatter
matrix about $m$ (the weighted sample covariance); assume $C$ is positive definite. Write
$\mathcal{N}(x \mid \mu, S)$ for the multivariate Gaussian density at $x$ with mean $\mu$ and
covariance $S$. Then for every $\mu \in \mathbb{R}^J$ and every positive definite real
$J \times J$ matrix $S$,
$\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid \mu, S) \le
\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid m, C)$.

Formalized by `MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_le_of_posDef`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianMLE.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianMLE.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html#sum-mul-log-multivariate-gaussian-pdfrea-3).

## The weighted Gaussian MLE for points in general position

Let $I$ be a nonempty finite
set and $J$ a finite set, and let $x_i \in \mathbb{R}^J$ ($i \in I$) be points with positive
weights $w_i > 0$ that do not all lie in an affine hyperplane: for every nonzero
$v \in \mathbb{R}^J$ there are $i, j \in I$ with
$\langle v, x_i \rangle \ne \langle v, x_j \rangle$. Let $m$ be their weighted mean and $C$ their
weighted scatter matrix about $m$ (the weighted sample covariance), and write
$\mathcal{N}(x \mid \mu, S)$ for the multivariate Gaussian density at $x$ with mean $\mu$ and
covariance $S$. Then for every $\mu \in \mathbb{R}^J$ and every positive definite real
$J \times J$ matrix $S$,
$\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid \mu, S) \le
\sum_{i \in I} w_i \log \mathcal{N}(x_i \mid m, C)$.

Formalized by `MetaMathlibExt.sum_mul_log_multivariateGaussianPDFReal_le`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianMLE.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianMLE.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html#sum-mul-log-multivariate-gaussian-pdfrea-4).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian maximum likelihood](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/linear-models-multivariate/gaussian-maximum-likelihood)
