---
declaration: section
origin: cited
lean: MathlibExt.Probability.IsotropicConstant.covarianceMatrix, MathlibExt.Probability.IsotropicConstant.differentialEntropy, MathlibExt.Probability.IsotropicConstant.FullDimensionalBody, MathlibExt.Probability.IsotropicConstant.LogConcaveLaw, MathlibExt.Probability.IsotropicConstant.covarianceMatrix_posSemidef, MathlibExt.Probability.IsotropicConstant.covarianceMatrix_eq_one_of_isIsotropic, MathlibExt.Probability.IsotropicConstant.bodyLaw, MathlibExt.Probability.IsotropicConstant.bodyIsotropicConstant
statement: formalized
proof: formalized
---

# Isotropic constant of log-concave laws

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html).

## Covariance matrix

For a measure $\mu$ on $\mathbb{R}^n$, the covariance matrix of $\mu$ is
the $n \times n$ real matrix whose $(i, j)$ entry is
$\int (x_i - m_i)(x_j - m_j) \, d\mu(x)$, where $m_i = \int x_i \, d\mu(x)$ is the mean of the
$i$-th coordinate.

## Sources

- `constants/20b.md`, covariance definition.

Formalized by `MathlibExt.Probability.IsotropicConstant.covarianceMatrix`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#covariance-matrix).

## Differential entropy

For a function $f \colon \mathbb{R}^n \to \mathbb{R}$, usually the
Lebesgue density of a probability law, the differential entropy of $f$ is
$-\int_{\mathbb{R}^n} f(x) \log f(x) \, dx$, with the natural logarithm and $0 \log 0 = 0$.

## Sources

- `constants/20b.md`, Ent(μ)=-∫f log f.

Formalized by `MathlibExt.Probability.IsotropicConstant.differentialEntropy`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#differential-entropy).

## Full-dimensional convex body

For a natural number $n$, a full-dimensional convex body in
dimension $n$ is a nonempty compact convex set $K$ in the Euclidean space $\mathbb{R}^n$ whose
interior is nonempty, where $n$ is required to be positive.

## Sources

- `constants/20b.md`, convex-body domain.

Formalized by `MathlibExt.Probability.IsotropicConstant.FullDimensionalBody`, a structure declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#full-dimensional-body).

## Log-concave law

For a positive integer $n$, a log-concave law on $\mathbb{R}^n$ is a
probability measure $\mu$ on $\mathbb{R}^n$ together with a Lebesgue density $f$ of $\mu$ that is
log-concave: $f$ is measurable and nonnegative, and $f((1-t)x + ty) \ge f(x)^{1-t} f(y)^t$ for all
$x, y \in \mathbb{R}^n$ and $0 < t < 1$. Moreover every coordinate $x_i$ and every product
$x_i x_j$ is $\mu$-integrable, and $f \log f$ is Lebesgue integrable.

## Sources

- `constants/20b.md`; finite moments and entropy integrability ensure the displayed real integrals do not use the non-integrable default value.

Formalized by `MathlibExt.Probability.IsotropicConstant.LogConcaveLaw`, a structure declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#log-concave-law).

## Covariance matrices of log-concave laws are positive semidefinite

For every log-concave
law $\mu$ on $\mathbb{R}^n$, the covariance matrix of $\mu$ is positive semidefinite.

The proof writes the quadratic form of the covariance matrix as the integral of the square of a
centered linear form.

Formalized by `MathlibExt.Probability.IsotropicConstant.covarianceMatrix_posSemidef`, a theorem declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#covariance-matrix-pos-semidef).

## Isotropic log-concave laws have identity covariance

If $\mu$ is an isotropic log-concave
probability measure on $\mathbb{R}^n$, then the covariance matrix of $\mu$ is the $n \times n$
identity matrix.

Formalized by `MathlibExt.Probability.IsotropicConstant.covarianceMatrix_eq_one_of_isIsotropic`, a theorem declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#covariance-matrix-eq-one-of-is-isotropic).

## Uniform distribution on a convex body

For a full-dimensional convex body $K$ in
$\mathbb{R}^n$, the uniform law on $K$ is the probability measure obtained by restricting
Lebesgue measure to $K$ and dividing by the volume of $K$; it gives a set $A$ the mass
$\operatorname{vol}(A \cap K) / \operatorname{vol}(K)$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyLaw`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-law).

## Isotropic constant of a convex body

For a full-dimensional convex body $K$ in
$\mathbb{R}^n$, let $\operatorname{Cov}(K)$ be the covariance matrix of the uniform probability
law on $K$ and let $\operatorname{vol}(K)$ be the Lebesgue volume of $K$. The isotropic constant
of $K$ is the real number
$L_K = \left(\det \operatorname{Cov}(K) / \operatorname{vol}(K)^2\right)^{1/(2n)}$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyIsotropicConstant`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-isotropic-constant).

## Isotropic constant of a log-concave law

For a log-concave law $\mu$ on $\mathbb{R}^n$ with
Lebesgue density $f$, the isotropic constant of $\mu$ is
$L_\mu = e^{-h(f)/n} (\det \mathrm{Cov}(\mu))^{1/(2n)}$, where
$h(f) = -\int_{\mathbb{R}^n} f \log f$ is the differential entropy of $f$ and $\mathrm{Cov}(\mu)$
is the covariance matrix of the coordinates under $\mu$.

Formalized by `MathlibExt.Probability.IsotropicConstant.lawIsotropicConstant`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#law-isotropic-constant).

## Supremum of isotropic constants in a fixed dimension

For $n \in \mathbb{N}$, this is
$\sup_K L_K \in [0, \infty]$, the supremum of the isotropic constants $L_K$ over all
full-dimensional convex bodies $K$ in $\mathbb{R}^n$. Full-dimensional convex bodies are taken
only in dimension $n \ge 1$, so for $n = 0$ the supremum is over the empty family and is $0$.

Formalized by `MathlibExt.Probability.IsotropicConstant.dimensionBodySupremum`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#dimension-body-supremum).

## Supremum of entropic isotropic constants in a fixed dimension

For $n \in \mathbb{N}$, this
is $\sup_\mu L_\mu \in [0, \infty]$, the supremum of the isotropic constants
$L_\mu = e^{-\operatorname{Ent}(f)/n} (\det \operatorname{Cov}(\mu))^{1/(2n)}$ over all
log-concave laws $\mu$ on $\mathbb{R}^n$, where $f$ is the log-concave Lebesgue density of $\mu$,
$\operatorname{Ent}(f)$ its differential entropy and $\operatorname{Cov}(\mu)$ its covariance
matrix. Here a log-concave law is a probability measure on $\mathbb{R}^n$ with $n \ge 1$, with
finite second moments and with $f \log f$ integrable, so for $n = 0$ the supremum is over the
empty family and is $0$.

Formalized by `MathlibExt.Probability.IsotropicConstant.dimensionLawSupremum`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#dimension-law-supremum).

## Supremum of isotropic constants of convex bodies

This is the value
$\sup_{n \ge 1} \sup_K L_K \in [0, \infty]$, where for each dimension $n \ge 1$ the inner
supremum runs over all full-dimensional convex bodies $K$ in $\mathbb{R}^n$ and $L_K$ is the
isotropic constant of $K$.

## Sources

- `constants/20b.md`, the sharp-value body constant.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodySupremum`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-supremum).

## Centrally symmetric convex body

For a natural number $n$, a full-dimensional convex
body $K \subseteq \mathbb{R}^n$ is centrally symmetric when $K = -K$, that is, for every
$x \in \mathbb{R}^n$, $x \in K$ if and only if $-x \in K$.

## Sources

- arXiv:2412.15044v1, Introduction after Theorem 1.2.

Formalized by `MathlibExt.Probability.IsotropicConstant.IsCentrallySymmetric`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#is-centrally-symmetric).

## Supremum of isotropic constants of symmetric convex bodies

This is the value
$\sup_{n \ge 1} \sup_K L_K \in [0, \infty]$, where for each dimension $n \ge 1$ the inner
supremum runs over the full-dimensional convex bodies $K$ in $\mathbb{R}^n$ that are centrally
symmetric, that is $K = -K$, and $L_K$ is the isotropic constant of $K$.

Formalized by `MathlibExt.Probability.IsotropicConstant.centrallySymmetricBodySupremum`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#centrally-symmetric-body-supremum).

## Squared-radius thin-shell width

For a natural number $n$, the squared-radius thin-shell
width in dimension $n$ is the supremum, in $[0, \infty]$, of
$\left(\int (|x|^2 - n)^2 \, d\mu(x) / n\right)^{1/2}$ (with $0/0 = 0$) over all isotropic
log-concave probability measures $\mu$ on $\mathbb{R}^n$, that is, those with a log-concave
Lebesgue density, mean zero and identity covariance.

It measures the fluctuation of the squared radius $|x|^2$, not of the radius $|x|$.

Formalized by `MathlibExt.Probability.IsotropicConstant.squaredRadiusThinShellWidth`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#squared-radius-thin-shell-width).

## Supremum of the isotropic constant over full-dimensional log-concave laws

This is the
supremum, in $[0, \infty]$, of the isotropic constant
$L_\mu = e^{-h(f)/n} (\det \mathrm{Cov}(\mu))^{1/(2n)}$ over all positive integers $n$ and all
log-concave laws $\mu$ on $\mathbb{R}^n$ with Lebesgue density $f$, where
$h(f) = -\int_{\mathbb{R}^n} f \log f$ is the differential entropy of $f$ and $\mathrm{Cov}(\mu)$
is the covariance matrix of the coordinates under $\mu$.

Each such law has a density on all of $\mathbb{R}^n$, so laws supported on a proper affine
subspace are not included here.

Formalized by `MathlibExt.Probability.IsotropicConstant.fullDimensionalLawSupremum`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicConstant.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicConstant.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#full-dimensional-law-supremum).

## Constant densities on convex sets are log-concave

Let $K \subseteq \mathbb{R}^n$ be a
measurable convex set and let $c > 0$. Then the function equal to $c$ on $K$ and to $0$ outside
$K$ is a log-concave density.

## Sources

- the uniform convex-body example in `constants/20b.md`.

Formalized by `MathlibExt.Probability.ThinShell.isLogConcaveDensity_indicator_const`, a theorem declared in [MathlibExt/Probability/Geometry/LogConcaveUniform.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/LogConcaveUniform.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#is-log-concave-density-indicator-const).

## Conditioning on a set is the normalized indicator density

Let $\mu$ be a measure on a
measurable space $\alpha$ and let $K \subseteq \alpha$ be a measurable set with $\mu(K) \neq 0$.
Then the conditional measure $\mu(\cdot \mid K)$, that is $\mu(K)^{-1}$ times the restriction of
$\mu$ to $K$, equals the measure with density $x \mapsto \mu(K)^{-1} \mathbf{1}_K(x)$ with respect
to $\mu$. Here $\mu(K)^{-1}$ is taken in $[0, \infty]$, so it is $0$ when $\mu(K) = \infty$.

## Sources

- `constants/20b.md`, normalized Lebesgue law on a convex body.

Formalized by `MathlibExt.Probability.ThinShell.cond_eq_withDensity_indicator`, a theorem declared in [MathlibExt/Probability/Geometry/LogConcaveUniform.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/LogConcaveUniform.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#cond-eq-with-density-indicator).

## Uniform density of a convex body

Let $n \ge 1$ and let $K \subseteq \mathbb{R}^n$ be a
full-dimensional convex body, so that its Lebesgue measure $\mathrm{Vol}(K)$ is finite and
positive. The uniform density of $K$ is the function $f_K \colon \mathbb{R}^n \to \mathbb{R}$ equal
to $1/\mathrm{Vol}(K)$ on $K$ and to $0$ outside $K$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyDensity`, a definition declared in [MathlibExt/Probability/Geometry/UniformBody.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformBody.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-density).

## Uniform law of a convex body

Let $n \ge 1$ and let $K \subseteq \mathbb{R}^n$ be a
full-dimensional convex body of Lebesgue measure $\mathrm{Vol}(K)$. The uniform law of $K$ is the
log-concave law on $\mathbb{R}^n$ whose probability measure is Lebesgue measure restricted to $K$
and divided by $\mathrm{Vol}(K)$, and whose density is the uniform density of $K$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyLogConcaveLaw`, a definition declared in [MathlibExt/Probability/Geometry/UniformBody.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformBody.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-log-concave-law).

## Entropy of the uniform density of a convex body

Let $n \ge 1$ and let
$K \subseteq \mathbb{R}^n$ be a full-dimensional convex body with Lebesgue measure
$\mathrm{Vol}(K)$ and uniform density $f_K$, equal to $1/\mathrm{Vol}(K)$ on $K$ and to $0$
outside $K$. Then the differential entropy $-\int_{\mathbb{R}^n} f_K(x) \log f_K(x) \, dx$ of
$f_K$ equals $\log \mathrm{Vol}(K)$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyDensity_entropy`, a theorem declared in [MathlibExt/Probability/Geometry/UniformBody.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformBody.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-density-entropy).

## The entropy and volume isotropic constants of a convex body agree

Let $n \ge 1$ and let
$K \subseteq \mathbb{R}^n$ be a full-dimensional convex body of Lebesgue measure
$\mathrm{Vol}(K)$, with uniform probability measure $\lambda_K$, uniform density $f_K$, and
covariance matrix $C_K$ of the coordinates under $\lambda_K$. Then the entropy isotropic constant
of the uniform law of $K$ equals the isotropic constant of $K$, that is,
$\exp\big(\frac{1}{n} \int_{\mathbb{R}^n} f_K(x) \log f_K(x) \, dx\big) (\det C_K)^{1/(2n)} =
\big(\det C_K / \mathrm{Vol}(K)^2\big)^{1/(2n)}$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyLogConcaveLaw_isotropicConstant`, a theorem declared in [MathlibExt/Probability/Geometry/UniformBody.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformBody.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-log-concave-law-isotropic-constant).

## Body isotropic constants are bounded by the law supremum

For every $n \in \mathbb{N}$,
the supremum of the isotropic constants of full-dimensional convex bodies in $\mathbb{R}^n$ is at
most the supremum of the entropy isotropic constants of probability laws on $\mathbb{R}^n$ with a
log-concave Lebesgue density $f$ such that every coordinate $x_i$ and every product $x_i x_j$ is
integrable under the law and $f \log f$ is Lebesgue integrable, both suprema taken in
$[0, \infty]$. Both families are defined only for $n \ge 1$, so for $n = 0$ they are empty and
both suprema are $0$.

Formalized by `MathlibExt.Probability.IsotropicConstant.dimensionBodySupremum_le_lawSupremum`, a theorem declared in [MathlibExt/Probability/Geometry/UniformBody.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformBody.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#dimension-body-supremum-le-law-supremum).

## Log-concave law in intrinsic coordinates

Fix an ambient dimension $N$. An intrinsic
log-concave law on $\mathbb{R}^N$ consists of a dimension $d$, a log-concave law $\nu$ on
$\mathbb{R}^d$ (that is, $d > 0$ and $\nu$ is a probability measure with a log-concave Lebesgue
density $f$, integrable coordinates and coordinate products, and integrable $f \log f$), an
affine isometric embedding $\varphi : \mathbb{R}^d \to \mathbb{R}^N$ of Euclidean spaces, and a
measure $\mu$ on $\mathbb{R}^N$, such that $\mu$ is the pushforward $\varphi_* \nu$ and the image
of $\varphi$ equals the affine span of the support of $\mu$.

The pushforward identity ties the ambient law $\mu$ to the density and entropy of $\nu$, which
are computed in the intrinsic coordinates.

Formalized by `MathlibExt.Probability.IsotropicConstant.IntrinsicLogConcaveLaw`, a structure declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#intrinsic-log-concave-law).

## Isotropic constant of an intrinsic log-concave law

Let $\mu$ be an intrinsic log-concave
law on $\mathbb{R}^N$, given by a log-concave law $\nu$ on $\mathbb{R}^d$ with density $f$ and an
affine isometric embedding of $\mathbb{R}^d$ onto the affine span of the support of $\mu$. The
isotropic constant of $\mu$ is the entropy isotropic constant of $\nu$,

$$L_\mu = e^{-h(f)/d} \, \det(\operatorname{Cov} \nu)^{1/(2d)},$$

where $h(f) = -\int_{\mathbb{R}^d} f \log f$ is the differential entropy of $f$ and
$\operatorname{Cov} \nu$ is the covariance matrix of the coordinates under $\nu$.

Entropy and covariance are thus computed relative to the intrinsic affine span.

Formalized by `MathlibExt.Probability.IsotropicConstant.intrinsicLawIsotropicConstant`, a definition declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#intrinsic-law-isotropic-constant).

## Supremum of intrinsic isotropic constants in a fixed ambient dimension

For a natural
number $N$, this is the supremum in $[0, \infty]$ of the isotropic constants $L_\mu$ over all
intrinsic log-concave laws $\mu$ on $\mathbb{R}^N$.

The family includes laws whose support spans a proper affine subspace of positive dimension.

Formalized by `MathlibExt.Probability.IsotropicConstant.dimensionIntrinsicLawSupremum`, a definition declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#dimension-intrinsic-law-supremum).

## Entropy-convention isotropic constant

This is the supremum, in $[0, \infty]$, over all
dimensions $N > 0$ of the supremum of the isotropic constants $L_\mu$ over all intrinsic
log-concave laws $\mu$ on $\mathbb{R}^N$. A law supported on a proper affine subspace thus
contributes the isotropic constant computed in orthonormal coordinates on its affine span.

## Sources

- C20b, with the entropy convention and actual intrinsic-span laws.

Formalized by `MathlibExt.Probability.IsotropicConstant.entropyIsotropicConstant`, a definition declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#entropy-isotropic-constant).

## The entropy isotropic constant is at most the full-dimensional supremum

The entropy
isotropic constant, the supremum of the isotropic constants of intrinsic log-concave laws over
all ambient dimensions $N > 0$, is at most the supremum in $[0, \infty]$, over all dimensions
$n > 0$ and all log-concave laws $\nu$ on $\mathbb{R}^n$, of the entropy isotropic constant
$L_\nu = e^{-h(f)/n} \det(\operatorname{Cov} \nu)^{1/(2n)}$, where $f$ is the density of $\nu$
and $h(f) = -\int f \log f$.

Each intrinsic law contributes the isotropic constant of its coordinate law, which is a
full-dimensional log-concave law.

Formalized by `MathlibExt.Probability.IsotropicConstant.entropyIsotropicConstant_le_fullDimensionalSupremum`, a theorem declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#entropy-isotropic-constant-le-full-dimen).

## The uniform law on a convex body spans the whole space

For a full-dimensional convex
body $K \subseteq \mathbb{R}^n$ (a convex body with nonempty interior, $n > 0$), the affine span
of the support of the uniform probability law on $K$ is all of $\mathbb{R}^n$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyLaw_affineSpan_support`, a theorem declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-law-affine-span-support).

## The uniform law on a convex body as an intrinsic log-concave law

For a full-dimensional
convex body $K \subseteq \mathbb{R}^n$, this is the intrinsic log-concave law on $\mathbb{R}^n$
of intrinsic dimension $n$ whose chart is the identity map of $\mathbb{R}^n$, whose law is the
uniform probability law on $K$, and whose coordinate law is that uniform law viewed as a
log-concave law with density $\mathbf{1}_K / \operatorname{vol}(K)$.

Formalized by `MathlibExt.Probability.IsotropicConstant.bodyIntrinsicLogConcaveLaw`, a definition declared in [MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IntrinsicIsotropicConstant.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#body-intrinsic-log-concave-law).

## Identification of the line with one-dimensional Euclidean space

The linear isometric
isomorphism from $\mathbb{R}$ onto one-dimensional Euclidean space $\mathbb{R}^1$ that sends a
real number $x$ to the vector whose only coordinate is $x$.

Formalized by `MathlibExt.Probability.ThinShell.lineIsometry`, a definition declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#line-isometry).

## Symmetric interval in one-dimensional Euclidean space

For a real number $a$, the set of
points of one-dimensional Euclidean space $\mathbb{R}^1$ whose only coordinate lies in the closed
interval $[-a, a]$. It is empty when $a < 0$.

Formalized by `MathlibExt.Probability.ThinShell.symmetricInterval`, a definition declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#symmetric-interval).

## Uniform distribution on a symmetric interval

For a real number $a$, the measure on
one-dimensional Euclidean space $\mathbb{R}^1$ obtained by conditioning Lebesgue measure on the
set $\{x : -a \le x_1 \le a\}$ of points whose only coordinate $x_1$ lies in $[-a, a]$, that is,
Lebesgue measure restricted to this set and divided by its measure. For $a > 0$ this is the
uniform probability distribution with density $1/(2a)$ on the interval; for $a \le 0$ the set has
measure zero and the conditioned measure is the zero measure.

It is conditioned Lebesgue measure, not a discrete uniform measure.

Formalized by `MathlibExt.Probability.ThinShell.uniformInterval`, a definition declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#uniform-interval).

## The uniform law on (−√3, √3) is isotropic log-concave

The uniform distribution on the
symmetric interval $[-\sqrt{3}, \sqrt{3}]$ of one-dimensional Euclidean space $\mathbb{R}^1$ is
an isotropic log-concave probability measure: it has a log-concave density with respect to
Lebesgue measure, mean zero and identity covariance.

## Sources

- the one-dimensional isotropic cube, uniform on [-√3, √3].

Formalized by `MathlibExt.Probability.ThinShell.uniformInterval_sqrt_three_isIsotropicLogConcave`, a theorem declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#uniform-interval-sqrt-three-is-isotropic).

## Thin-shell variance bound for the uniform law on (−√3, √3)

Let $\mu$ be the uniform
distribution on the symmetric interval $[-\sqrt{3}, \sqrt{3}]$ of one-dimensional Euclidean
space $\mathbb{R}^1$. Its normalized radius variance $\int (\|x\|^2 - 1)^2 \, d\mu(x)$ is at most
the thin-shell variance constant, the supremum of the normalized radius variance over all
isotropic log-concave probability measures in all positive dimensions.

Formalized by `MathlibExt.Probability.ThinShell.uniformInterval_variance_le_thinShellConstant`, a theorem declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#uniform-interval-variance-le-thin-shell).

## Radius fluctuation of the uniform law on (−√3, √3)

Let $\mu$ be the uniform distribution
on the symmetric interval $[-\sqrt{3}, \sqrt{3}]$ of one-dimensional Euclidean space
$\mathbb{R}^1$. Then $\int (\|x\| - \sqrt{1})^2 \, d\mu(x)$, the mean squared deviation of the
Euclidean norm from $\sqrt{1} = 1$, is at most the thin-shell variance constant.

Formalized by `MathlibExt.Probability.ThinShell.uniformInterval_radiusFluctuation_le_thinShellConstant`, a theorem declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#uniform-interval-radius-fluctuation-le-t).

## The uniform law on (−1, 1) is not isotropic log-concave

The uniform distribution on the
symmetric interval $[-1, 1]$ of one-dimensional Euclidean space $\mathbb{R}^1$ is not an isotropic
log-concave probability measure.

Its second moment is $1/3$ rather than $1$.

Formalized by `MathlibExt.Probability.ThinShell.uniformInterval_one_not_isIsotropicLogConcave`, a theorem declared in [MathlibExt/Probability/Geometry/UniformInterval.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/UniformInterval.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#uniform-interval-one-not-is-isotropic-lo).

## Symmetric interval as a convex body

For a real number $a > 0$, this is the closed
interval $[-a, a]$ in the one-dimensional Euclidean space, regarded as a full-dimensional convex
body.

Formalized by `MathlibExt.Probability.IsotropicConstant.intervalBody`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicCube.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicCube.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#interval-body).

## Unit interval body

The unit interval body is the closed interval $[-1/2, 1/2]$, of length
one and centred at the origin, in the one-dimensional Euclidean space, regarded as a
full-dimensional convex body.

Formalized by `MathlibExt.Probability.IsotropicConstant.unitIntervalBody`, a definition declared in [MathlibExt/Probability/Geometry/IsotropicCube.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicCube.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#unit-interval-body).

## Cube lower bound for the supremal isotropic constant

The supremum, over all positive
integers $n$ and all full-dimensional convex bodies $K \subseteq \mathbb{R}^n$, of the isotropic
constant $L_K = \left(\det \mathrm{Cov}(K) / \mathrm{Vol}(K)^2\right)^{1/(2n)}$, where
$\mathrm{Cov}(K)$ is the covariance matrix of the uniform distribution on $K$, is at least
$1/\sqrt{12}$.

The interval $[-1/2, 1/2]$ in dimension one already attains $L_K = 1/\sqrt{12}$.

Formalized by `MathlibExt.Probability.IsotropicConstant.inv_sqrt_twelve_le_bodySupremum`, a theorem declared in [MathlibExt/Probability/Geometry/IsotropicCube.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicCube.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#inv-sqrt-twelve-le-body-supremum).

## Membership in the unit interval body

A point $x$ of the one-dimensional Euclidean space
lies in the unit interval body if and only if its single coordinate $x_1$ satisfies
$-1/2 \le x_1 \le 1/2$.

Formalized by `MathlibExt.Probability.IsotropicConstant.unitIntervalBody_mem_iff`, a theorem declared in [MathlibExt/Probability/Geometry/IsotropicCube.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Geometry/IsotropicCube.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html#unit-interval-body-mem-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isotropic constant of log-concave laws](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/high-dimensional-probability/isotropic-constant-of-log-concave-laws)
