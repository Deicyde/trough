---
declaration: section
origin: cited
lean: TorusSobolev.Torus, TorusSobolev.Frequency, TorusSobolev.unitRescaling, TorusSobolev.unitRepresentative, TorusSobolev.fourierCoefficient, TorusSobolev.frequencyWeight, TorusSobolev.gradientEnergy, TorusSobolev.laplaceEnergy
statement: formalized
proof: formalized
---

# Fourier Sobolev optimization on the two-dimensional torus

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html).

## The torus of period $2\pi$

The two-dimensional torus
$\mathbb{T}^2 = (\mathbb{R}/2\pi\mathbb{Z})^2$, the product of two copies of the circle
$\mathbb{R}/2\pi\mathbb{Z}$.

Formalized by `TorusSobolev.Torus`, an abbreviation declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#torus).

## Integer frequencies

The frequencies are the elements of the lattice $\mathbb{Z}^2$,
that is, the pairs $k = (k_1, k_2)$ of integers; they index the Fourier modes of the torus
$(\mathbb{R}/2\pi\mathbb{Z})^2$.

Formalized by `TorusSobolev.Frequency`, an abbreviation declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#frequency).

## Rescaling the torus to unit period

The homeomorphism from the torus
$\mathbb{T}^2 = (\mathbb{R}/2\pi\mathbb{Z})^2$ onto the unit torus $(\mathbb{R}/\mathbb{Z})^2$
that sends $(x_1, x_2)$ to $(x_1/(2\pi), x_2/(2\pi))$.

Formalized by `TorusSobolev.unitRescaling`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#unit-rescaling).

## A function on the torus as a function on the unit torus

For a continuous function
$u : \mathbb{T}^2 \to \mathbb{R}$ on the torus $\mathbb{T}^2 = (\mathbb{R}/2\pi\mathbb{Z})^2$, its
unit representative is the continuous function $\tilde u : (\mathbb{R}/\mathbb{Z})^2 \to \mathbb{C}$
given by $\tilde u(y) = u(2\pi y)$, the composition of $u$ with the inverse of the rescaling to
unit period, with its real values regarded as complex numbers.

Formalized by `TorusSobolev.unitRepresentative`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#unit-representative).

## Fourier coefficients on the torus

Let $u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$
be continuous and let $k \in \mathbb{Z}^2$ be a frequency. The Fourier coefficient of $u$ at
$k$ is $a_k = 2\pi c_k$, where $c_k = \int_{[0,1]^2} u(2\pi y)\, e^{-2\pi i\, k \cdot y}\, dy$
is the Fourier coefficient of the rescaled function $y \mapsto u(2\pi y)$ on the unit torus
with respect to normalized Haar measure. Equivalently,
$a_k = \frac{1}{2\pi} \int_{[0,2\pi]^2} u(x)\, e^{-i\, k \cdot x}\, dx$.

Formalized by `TorusSobolev.fourierCoefficient`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#fourier-coefficient).

## Squared frequency

For a frequency $k = (k_1, k_2) \in \mathbb{Z}^2$, the frequency
weight is $|k|^2 = k_1^2 + k_2^2$, the squared frequency of the mode $e^{i k \cdot x}$ on the
torus $(\mathbb{R}/2\pi\mathbb{Z})^2$.

Formalized by `TorusSobolev.frequencyWeight`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#frequency-weight).

## Gradient energy

For a continuous function
$u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$ with Fourier coefficients $a_k$, the gradient
energy is $\sum_{k \in \mathbb{Z}^2} |k|^2 \, |a_k|^2$, where $|k|^2 = k_1^2 + k_2^2$; the sum is
taken to be $0$ when the series diverges.

By Parseval's identity, for smooth $u$ this equals $\int_{[0,2\pi]^2} |\nabla u(x)|^2 \, dx$.

Formalized by `TorusSobolev.gradientEnergy`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#gradient-energy).

## Laplacian energy

For a continuous function
$u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$ with Fourier coefficients $a_k$, the Laplacian
energy is $\sum_{k \in \mathbb{Z}^2} |k|^4 \, |a_k|^2$, where $|k|^2 = k_1^2 + k_2^2$; the sum is
taken to be $0$ when the series diverges.

By Parseval's identity, for smooth $u$ this equals $\int_{[0,2\pi]^2} |\Delta u(x)|^2 \, dx$.

Formalized by `TorusSobolev.laplaceEnergy`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#laplace-energy).

## Functions in $H^2$

A continuous function $u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$
with Fourier coefficients $a_k$ is in $H^2$ when the series
$\sum_{k \in \mathbb{Z}^2} (1 + |k|^2)^2 \, |a_k|^2$ converges, where $|k|^2 = k_1^2 + k_2^2$.

This is the full spectral $H^2$ condition, not a restriction to trigonometric polynomials.

Formalized by `TorusSobolev.IsH2`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#is-h2).

## Normalized Haar measure on the unit torus

The measure on the unit torus
$(\mathbb{R}/\mathbb{Z})^2$ that is the product of two copies of the Haar probability measure on the
circle $\mathbb{R}/\mathbb{Z}$.

Formalized by `TorusSobolev.unitHaar`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#unit-haar).

## Mean of a function on the torus

For a continuous function $u : \mathbb{T}^2 \to \mathbb{R}$
on the torus $\mathbb{T}^2 = (\mathbb{R}/2\pi\mathbb{Z})^2$, its mean is
$\int_{(\mathbb{R}/\mathbb{Z})^2} u(2\pi y)\, d\mu(y)$, where $\mu$ is the normalized Haar measure
on the unit torus $(\mathbb{R}/\mathbb{Z})^2$ and $y \mapsto 2\pi y$ is the inverse of the rescaling
to unit period.

Since $\mu$ is a probability measure, this is the average
$(2\pi)^{-2} \int_{[0, 2\pi]^2} u(x)\, dx$; the Lebesgue integral of $u$ over a period cell is
$(2\pi)^2$ times the mean.

Formalized by `TorusSobolev.mean`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#mean).

## Zero-mean $H^2$ functions

A continuous function
$u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$ is a zero-mean $H^2$ function when it is in
$H^2$ and its mean is $0$.

Formalized by `TorusSobolev.IsZeroMeanH2`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#is-zero-mean-h2).

## Conditionally admissible functions

Let $\delta$ be a real number. A continuous
function $u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$ is admissible at level $\delta$
when it is a zero-mean $H^2$ function, its gradient energy equals $1$, and its Laplacian
energy equals $\delta$.

Formalized by `TorusSobolev.ConditionalAdmissible`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#conditional-admissible).

## Squared values at the origin of admissible functions

For a real number $\delta$,
this is the set of extended real numbers $u(0)^2$, where $u$ ranges over the continuous
functions $u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$ that are conditionally admissible
at level $\delta$.

Formalized by `TorusSobolev.conditionalPointValues`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#conditional-point-values).

## Conditional supremum of the squared value at the origin

For real $\delta$,
$\theta(\delta)$ is the supremum, taken in the extended reals $[-\infty, \infty]$, of the
conditional point values at $\delta$: the numbers $u(0)^2$ over all continuous
$u : \mathbb{T}^2 \to \mathbb{R}$ on the torus $\mathbb{T}^2 = (\mathbb{R}/2\pi\mathbb{Z})^2$
that are conditionally admissible at $\delta$, that is, of mean zero and in $H^2$ with gradient
energy $1$ and Laplace energy $\delta$.

The supremum may be $+\infty$, and it is $-\infty$ when no function is admissible.

Formalized by `TorusSobolev.theta`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#theta).

## Frequency ratio

For a continuous function
$u : (\mathbb{R}/2\pi\mathbb{Z})^2 \to \mathbb{R}$, the frequency ratio is the Laplacian energy
of $u$ divided by the gradient energy of $u$.

Applications assume positive gradient energy; when the gradient energy is $0$, the quotient is
taken to be $0$.

Formalized by `TorusSobolev.frequencyRatio`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#frequency-ratio).

## Logarithmic remainder

For real $\delta$, the remainder is the extended real number
$R(\delta) = 4\pi\,\theta(\delta) - \log \delta - \log(1 + \log \delta)$, where $\theta(\delta)$
is the conditional supremum of $u(0)^2$ over the functions conditionally admissible at $\delta$.

Here $\log$ is the real logarithm with the conventions $\log 0 = 0$ and $\log x = \log |x|$ for
$x < 0$, so $R(\delta)$ is defined for every real $\delta$.

Formalized by `TorusSobolev.remainder`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#remainder).

## Set of remainder values

The set of extended real numbers $R(\delta)$ for all real
$\delta \ge 1$, where $R(\delta) = 4\pi\,\theta(\delta) - \log \delta - \log(1 + \log \delta)$
is the logarithmic remainder and $\theta(\delta)$ is the conditional supremum of $u(0)^2$ over
the functions conditionally admissible at $\delta$.

Every $\delta \ge 1$ is included, not only sufficiently large ratios.

Formalized by `TorusSobolev.sharpRemainderValues`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#sharp-remainder-values).

## Sharp logarithmic remainder

The sharp remainder is the supremum, in the extended reals
$[-\infty, \infty]$, of the remainders
$R(\delta) = 4\pi\,\theta(\delta) - \log \delta - \log(1 + \log \delta)$ over all real
$\delta \ge 1$, where $\theta(\delta)$ is the conditional supremum of $u(0)^2$ over the functions
conditionally admissible at $\delta$.

The definition does not assume that the supremum is finite or attained.

Formalized by `TorusSobolev.sharpRemainderValue`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#sharp-remainder-value).

## Uniform logarithmic remainder bound

For a real constant $L$, the bound with constant $L$
holds when, for every continuous $u : \mathbb{T}^2 \to \mathbb{R}$ on the torus
$\mathbb{T}^2 = (\mathbb{R}/2\pi\mathbb{Z})^2$ that has mean zero and lies in $H^2$, has positive
gradient energy $E(u)$, and, writing $\Delta(u)$ for its Laplace energy, has frequency ratio
$\Lambda(u) = \Delta(u)/E(u) \ge 1$, every point $x$ of the torus satisfies
$u(x)^2 \le \frac{E(u)}{4\pi}\bigl(\log \Lambda(u) + \log(1 + \log \Lambda(u)) + L\bigr)$.

Formalized by `TorusSobolev.UniformRemainderBound`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Basic.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html#uniform-remainder-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier Sobolev optimization on the two-dimensional torus](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-sobolev-optimization-on-the-two-dimensio)
