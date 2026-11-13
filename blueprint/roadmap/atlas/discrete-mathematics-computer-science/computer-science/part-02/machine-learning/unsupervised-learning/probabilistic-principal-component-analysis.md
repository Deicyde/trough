---
declaration: section
origin: cited
lean: Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.inner_toEuclideanLin, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.charFun_map_toEuclideanLin, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.map_eq_multivariateGaussian, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.ppca_map_eq, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.factorAnalysis_map_eq, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.ppcaCov, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.ppca_map_eq_withDensity, Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.logLik
statement: formalized
proof: formalized
---

# Probabilistic principal component analysis

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html).

## The transpose of a real matrix is its adjoint

For every real $d \times q$ matrix $W$ and
all $z \in \mathbb{R}^q$ and $t \in \mathbb{R}^d$, the Euclidean inner products satisfy
$\langle Wz, t\rangle = \langle z, W^\top t\rangle$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.inner_toEuclideanLin`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#inner-to-euclidean-lin).

## Characteristic function of a linear image

Let $\mu$ be a measure on $\mathbb{R}^q$
and $W$ a real $d \times q$ matrix, and write
$\varphi_\nu(t) = \int e^{i\langle x, t\rangle}\,d\nu(x)$ for the characteristic function of a
measure $\nu$. Then the pushforward $W_*\mu$ of $\mu$ under $z \mapsto Wz$ satisfies
$\varphi_{W_*\mu}(t) = \varphi_\mu(W^\top t)$ for every $t \in \mathbb{R}^d$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.charFun_map_toEuclideanLin`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#char-fun-map-to-euclidean-lin).

## The marginal of probabilistic PCA and factor analysis is Gaussian

Let $Z$ and $E$ be
independent random vectors on a probability space, with values in $\mathbb{R}^q$ and
$\mathbb{R}^d$, such that $Z$ has the standard Gaussian law $N(0, I_q)$ and $E$ has law
$N(0, \Psi)$ for a positive semidefinite real $d \times d$ matrix $\Psi$. Then for every real
$d \times q$ matrix $W$ and every $\mu \in \mathbb{R}^d$, the random vector $WZ + \mu + E$ has
law $N(\mu, WW^\top + \Psi)$.

This is the marginal of Tipping and Bishop's model: probabilistic PCA is the case
$\Psi = \sigma^2 I$, factor analysis the case of a diagonal $\Psi$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.map_eq_multivariateGaussian`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#map-eq-multivariate-gaussian).

## The probabilistic PCA marginal

Let $Z$ and $E$ be independent random vectors on a
probability space, with values in $\mathbb{R}^q$ and $\mathbb{R}^d$, such that $Z$ has the
standard Gaussian law $N(0, I_q)$ and $E$ has the isotropic law $N(0, \sigma^2 I_d)$ for a real
$\sigma^2 \ge 0$. Then for every real $d \times q$ matrix $W$ and every $\mu \in \mathbb{R}^d$, the
random vector $WZ + \mu + E$ has law $N(\mu, WW^\top + \sigma^2 I_d)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.ppca_map_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#ppca-map-eq).

## The factor-analysis marginal

Let $Z$ and $E$ be independent random vectors on a
probability space, with values in $\mathbb{R}^q$ and $\mathbb{R}^d$, such that $Z$ has the
standard Gaussian law $N(0, I_q)$ and $E$ has law $N(0, \operatorname{diag}\psi)$ for a vector
$\psi \in \mathbb{R}^d$ with $\psi_i \ge 0$ for all $i$. Then for every real $d \times q$ matrix
$W$ and every $\mu \in \mathbb{R}^d$, the random vector $WZ + \mu + E$ has law
$N(\mu, WW^\top + \operatorname{diag}\psi)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.factorAnalysis_map_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCA.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#factor-analysis-map-eq).

## Probabilistic PCA covariance

For a real $d \times q$ matrix $W$ and a real number
$\sigma^2$, the probabilistic PCA covariance is the $d \times d$ matrix $W W^\top + \sigma^2 I$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.ppcaCov`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#ppca-cov).

## The density of the probabilistic PCA observation

Let $z$ and $\varepsilon$ be
independent random vectors on a probability space, with $z$ standard Gaussian in $\mathbb{R}^q$
and $\varepsilon$ Gaussian in $\mathbb{R}^d$ with mean $0$ and covariance $\sigma^2 I$, where
$\sigma^2 > 0$. Then for every real $d \times q$ matrix $W$ and every $\mu \in \mathbb{R}^d$, the
law of $x = W z + \mu + \varepsilon$ has density $\mathcal{N}(x \mid \mu, W W^\top + \sigma^2 I)$
with respect to Lebesgue measure on $\mathbb{R}^d$, where $\mathcal{N}(x \mid \mu, \Sigma)$ is the
multivariate Gaussian density with mean $\mu$ and covariance $\Sigma$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.ppca_map_eq_withDensity`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#ppca-map-eq-with-density).

## Probabilistic PCA log-likelihood

For data $x_1, \dots, x_N \in \mathbb{R}^d$, a mean
$\mu \in \mathbb{R}^d$, a real $d \times q$ loading matrix $W$ and a real number $\sigma^2$, the
probabilistic PCA log-likelihood of the data is

$$
\sum_{n=1}^N \log \mathcal{N}(x_n \mid \mu, W W^\top + \sigma^2 I),
$$

where, for a real $d \times d$ matrix $\Sigma$ and $x \in \mathbb{R}^d$,

$$
\mathcal{N}(x \mid \mu, \Sigma) = (2\pi)^{-d/2} \bigl(\sqrt{\det \Sigma}\bigr)^{-1}
\exp\bigl(-\tfrac{1}{2} (x - \mu)^\top \Sigma^{-1} (x - \mu)\bigr)
$$

is the multivariate Gaussian density formula, read with the conventions $\sqrt{t} = 0$ for
$t < 0$, $0^{-1} = 0$, $\Sigma^{-1} = 0$ for singular $\Sigma$ and $\log 0 = 0$. These conventions
matter only when $W W^\top + \sigma^2 I$ is not positive definite. When $\sigma^2 > 0$ the matrix
$W W^\top + \sigma^2 I$ is positive definite, and this is the density of the Gaussian with mean
$\mu$ and covariance $W W^\top + \sigma^2 I$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.logLik`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#log-lik).

## Sample mean

For data points $x_1, \dots, x_N \in \mathbb{R}^d$, the sample mean is
$\bar x = \frac{1}{N} \sum_{n=1}^{N} x_n \in \mathbb{R}^d$.

When $N = 0$ the sample mean is $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.sampleMean`, an abbreviation declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#sample-mean).

## Sample covariance

For data $x_1, \dots, x_N \in \mathbb{R}^d$ with sample mean
$\bar{x}$, the sample covariance is the $d \times d$ matrix
$S = \frac{1}{N} \sum_{n=1}^N (x_n - \bar{x})(x_n - \bar{x})^\top$, taken to be $0$ when
$N = 0$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.sampleCov`, an abbreviation declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#sample-cov).

## The log-likelihood of no data is zero

For the empty data set ($N = 0$), the
probabilistic PCA log-likelihood at every $\mu \in \mathbb{R}^d$, every real $d \times q$ matrix
$W$ and every real number $\sigma^2$ is $0$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.logLik_of_N_eq_zero`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#log-lik-of-n-eq-zero).

## The mean MLE is the sample mean

Let $x_1, \dots, x_N \in \mathbb{R}^d$ be data with
sample mean $\bar{x}$. For every $\mu \in \mathbb{R}^d$, every real $d \times q$ loading matrix
$W$ and every real $\sigma^2 > 0$, the probabilistic PCA log-likelihood of the data at
$(\mu, W, \sigma^2)$ is at most its value at $(\bar{x}, W, \sigma^2)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.logLik_le_sampleMean`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#log-lik-le-sample-mean).

## The probabilistic PCA likelihood is at most the unconstrained Gaussian maximum

Let
$x_1, \dots, x_N \in \mathbb{R}^d$ be data whose sample covariance $S$ is positive definite, and
let $\bar{x}$ be their sample mean. Then for every $\mu \in \mathbb{R}^d$, every real
$d \times q$ matrix $W$ and every real $\sigma^2 > 0$, the probabilistic PCA log-likelihood of the
data at $(\mu, W, \sigma^2)$ is at most $\sum_{n=1}^N \log \mathcal{N}(x_n \mid \bar{x}, S)$,
where $\mathcal{N}(x \mid \bar{x}, S)$ is the multivariate Gaussian density with mean $\bar{x}$
and covariance $S$.

The sample covariance is positive definite, for example, when the data do not all lie in an
affine hyperplane.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.logLik_le_gaussianMLE`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#log-lik-le-gaussian-mle).

## Probabilistic PCA maximum-likelihood estimate

Given data
$x_1, \dots, x_N \in \mathbb{R}^d$, a triple $(\mu_0, W_0, \sigma_0^2)$ of a mean
$\mu_0 \in \mathbb{R}^d$, a real $d \times q$ loading matrix $W_0$ and a real number $\sigma_0^2$
is a probabilistic PCA maximum-likelihood estimate when $\sigma_0^2 > 0$ and, for every
$\mu \in \mathbb{R}^d$, every real $d \times q$ matrix $W$ and every real $\sigma^2 > 0$, the
probabilistic PCA log-likelihood of the data at $(\mu, W, \sigma^2)$ is at most its value at
$(\mu_0, W_0, \sigma_0^2)$.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.IsMLE`, a definition declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#is-mle).

## Probabilistic PCA MLE when the sample covariance has the model form

Let
$x_1, \dots, x_N \in \mathbb{R}^d$ be data with sample mean $\bar{x}$ and sample covariance $S$.
If $W_0$ is a real $d \times q$ matrix and $\sigma_0^2 > 0$ is a real number with
$S = W_0 W_0^\top + \sigma_0^2 I$, then $(\bar{x}, W_0, \sigma_0^2)$ is a probabilistic PCA
maximum-likelihood estimate for the data.

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.isMLE_of_sampleCov_eq`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#is-mle-of-sample-cov-eq).

## No latent factors: the noise-variance MLE is the average sample variance

Let
$x_1, \dots, x_N \in \mathbb{R}^d$ be data with sample mean $\bar{x}$ and sample covariance $S$,
and suppose $\operatorname{tr} S > 0$. Then for every $\mu \in \mathbb{R}^d$ and every real
$\sigma^2 > 0$, the probabilistic PCA log-likelihood of the data with the zero $d \times q$
loading matrix at $(\mu, 0, \sigma^2)$ is at most its value at
$(\bar{x}, 0, \operatorname{tr} S / d)$.

Here $\operatorname{tr} S / d$ is the average sample variance (Tipping and Bishop's $\sigma^2$
estimate with no retained components).

Formalized by `Cslib.MachineLearning.LatentVariable.ProbabilisticPCA.logLik_zero_le`, a theorem declared in [CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/LatentVariable/ProbabilisticPCAMLE.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html#log-lik-zero-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Probabilistic principal component analysis](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/unsupervised-learning/probabilistic-principal-component-analysis)
