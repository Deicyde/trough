---
declaration: section
origin: cited
lean: MetaMathlibExt.stdGaussianPDFReal, MetaMathlibExt.stdGaussianDensityMeasure, MetaMathlibExt.stdGaussian_eq_withDensity, MetaMathlibExt.map_withDensity_measurableEquiv, MetaMathlibExt.affineEquiv, MetaMathlibExt.map_affineEquiv_volume, MetaMathlibExt.multivariateGaussianPDFReal, MetaMathlibExt.norm_sq_sqrt_inv_apply
statement: formalized
---

# Multivariate normal distribution

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html).

## Standard Gaussian density function

Let $\iota$ be a finite set of size $n$. The standard
Gaussian density on the Euclidean space $\mathbb{R}^\iota$ is the real-valued function
$v \mapsto (2\pi)^{-n/2} \exp(-\|v\|^2/2)$.

Formalized by `MetaMathlibExt.stdGaussianPDFReal`, a definition declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#std-gaussian-pdfreal).

## Standard Gaussian measure via its density

Let $\iota$ be a finite set of size $n$. This is
the measure on the Euclidean space $\mathbb{R}^\iota$ with density
$v \mapsto (2\pi)^{-n/2} \exp(-\|v\|^2/2)$ with respect to Lebesgue measure.

Formalized by `MetaMathlibExt.stdGaussianDensityMeasure`, a definition declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#std-gaussian-density-measure).

## The standard Gaussian has a density

Let $\iota$ be a finite set of size $n$. The standard
Gaussian measure on the Euclidean space $\mathbb{R}^\iota$ has density
$v \mapsto (2\pi)^{-n/2} \exp(-\|v\|^2/2)$ with respect to Lebesgue measure.

Formalized by `MetaMathlibExt.stdGaussian_eq_withDensity`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#std-gaussian-eq-with-density).

## Pushforward of a measure with density

Let $e : \alpha \to \beta$ be a measurable
equivalence between measurable spaces, $\nu$ a measure on $\alpha$ and $g : \alpha \to [0, \infty]$
any function. Then the pushforward under $e$ of the measure with density $g$ with respect to $\nu$
is the measure with density $g \circ e^{-1}$ with respect to the pushforward $e_*\nu$ of $\nu$.

Formalized by `MetaMathlibExt.map_withDensity_measurableEquiv`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#map-with-density-measurable-equiv).

## The affine change of variables as a measurable equivalence

Let $\iota$ be a finite type,
$\mu \in \mathbb{R}^\iota$ and $A$ a real $\iota \times \iota$ matrix with nonzero determinant. The
map $x \mapsto \mu + Ax$ is a measurable equivalence of the Euclidean space $\mathbb{R}^\iota$ with
itself, with inverse $y \mapsto A^{-1}(y - \mu)$.

Formalized by `MetaMathlibExt.affineEquiv`, a definition declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#affine-equiv).

## Lebesgue measure under an invertible affine map

Let $\iota$ be a finite type,
$\mu \in \mathbb{R}^\iota$ and $A$ a real $\iota \times \iota$ matrix with nonzero determinant. The
pushforward of Lebesgue measure on the Euclidean space $\mathbb{R}^\iota$ under the measurable
equivalence $x \mapsto \mu + Ax$ equals $|\det A|^{-1}$ times Lebesgue measure.

Formalized by `MetaMathlibExt.map_affineEquiv_volume`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#map-affine-equiv-volume).

## Multivariate Gaussian density function

Let $\iota$ be a finite set of size $n$. For
$\mu, x \in \mathbb{R}^\iota$ and a real $\iota \times \iota$ matrix $S$, this is the real number

$$\frac{1}{(2\pi)^{n/2}\sqrt{\det S}} \exp\left(-\frac{(x - \mu)^\top S^{-1}(x - \mu)}{2}\right).$$

It is defined for every $S$, with the conventions $\sqrt{t} = 0$ for $t < 0$, $1/0 = 0$ and
$S^{-1} = 0$ for singular $S$, so its value is $0$ when $\det S \le 0$.

Formalized by `MetaMathlibExt.multivariateGaussianPDFReal`, a definition declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#multivariate-gaussian-pdfreal).

## Quadratic form of the inverse square root

Let $\iota$ be a finite type, $S$ a positive
definite real $\iota \times \iota$ matrix and $S^{1/2}$ its positive semidefinite square root. Then
for every $u$ in the Euclidean space $\mathbb{R}^\iota$,
$\|(S^{1/2})^{-1} u\|^2 = u^\top S^{-1} u$.

Formalized by `MetaMathlibExt.norm_sq_sqrt_inv_apply`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#norm-sq-sqrt-inv-apply).

## The multivariate Gaussian density

Let $\iota$ be a finite set of size $n$, let
$\mu \in \mathbb{R}^\iota$ and let $S$ be a positive definite real $\iota \times \iota$ matrix. Then
the multivariate Gaussian measure on the Euclidean space $\mathbb{R}^\iota$ with mean $\mu$ and
covariance matrix $S$ (the image of the standard Gaussian under $x \mapsto \mu + S^{1/2} x$) has
density

$$\frac{1}{(2\pi)^{n/2} \sqrt{\det S}} \exp\left(-\frac{(x - \mu)^\top S^{-1} (x - \mu)}{2}\right)$$

with respect to Lebesgue measure.

Formalized by `MetaMathlibExt.multivariateGaussian_eq_withDensity`, a theorem declared in [MathlibExt/Probability/Distributions/GaussianDensity.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/GaussianDensity.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#multivariate-gaussian-eq-with-density).

## Sheppard's formula (Gaussian arcsine law)

Let $\rho$ be a real number with $-1 < \rho < 1$,
and let $\gamma$ be the multivariate Gaussian measure on $\mathbb{R}^2$ with mean $0$ and
covariance matrix whose diagonal entries are $1$ and whose off-diagonal entries are $\rho$ (the
law of a standard bivariate normal vector with correlation $\rho$). Then the open first quadrant
$\{x \in \mathbb{R}^2 : x_1 > 0,\ x_2 > 0\}$ has $\gamma$-probability
$\frac{1}{4} + \frac{\arcsin \rho}{2\pi}$.

## Sources

- Y. L. Tong, The Multivariate Normal Distribution, Springer, 1990, Ch. 3; W. F. Sheppard, "On the application of the theory of error to cases of normal distribution and normal correlation", Phil. Trans. R. Soc. Lond. A 192 (1899), 101–167; https://en.wikipedia.org/wiki/Multivariate_normal_distribution

Stated but not proved: `MathlibExt.Probability.SheppardArcsineWanted.sheppard_quadrant_probability_arcsine` is written with `theorem_wanted` in [WantedExt/Probability/SheppardArcsineWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/SheppardArcsineWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html#sheppard-quadrant-probability-arcsine).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multivariate normal distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/multivariate-normal-distribution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/multivariate-normal-distribution)
