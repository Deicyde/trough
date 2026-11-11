---
declaration: section
origin: cited
lean: TorusSobolev.mFourierCoeff_monomial, TorusSobolev.mFourierCoeff_integrable, TorusSobolev.mFourierCoeff_add, TorusSobolev.mFourierCoeff_smul, TorusSobolev.axisFrequency, TorusSobolev.lowestShellUnit, TorusSobolev.lowestShellWitness, TorusSobolev.lowestShellUnit_im_zero
statement: formalized
proof: formalized
---

# Fourier coefficients and the lowest-shell witness

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html).

## Fourier coefficients of a Fourier monomial on the 2-torus

For frequencies
$m, n \in \mathbb{Z}^2$, the $n$-th Fourier coefficient, taken with respect to normalized Haar
measure on $(\mathbb{R}/\mathbb{Z})^2$, of the monomial $e_m(x) = e^{2\pi i\, m \cdot x}$ is $1$ if
$n = m$ and $0$ otherwise.

Formalized by `TorusSobolev.mFourierCoeff_monomial`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#m-fourier-coeff-monomial).

## Integrability of Fourier integrands on the 2-torus

For every continuous function
$f : (\mathbb{R}/\mathbb{Z})^2 \to \mathbb{C}$ and every frequency $n \in \mathbb{Z}^2$, the
function $x \mapsto e^{-2\pi i\, n \cdot x} f(x)$ is integrable with respect to normalized Haar
measure.

Formalized by `TorusSobolev.mFourierCoeff_integrable`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#m-fourier-coeff-integrable).

## Additivity of Fourier coefficients on the 2-torus

For continuous functions
$f, g : (\mathbb{R}/\mathbb{Z})^2 \to \mathbb{C}$ and every frequency $n \in \mathbb{Z}^2$, the
$n$-th Fourier coefficient $\hat h(n) = \int e^{-2\pi i\, n \cdot x} h(x)\,dx$ (normalized Haar
measure) satisfies $\widehat{f + g}(n) = \hat f(n) + \hat g(n)$.

Formalized by `TorusSobolev.mFourierCoeff_add`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#m-fourier-coeff-add).

## Homogeneity of Fourier coefficients on the 2-torus

For every $c \in \mathbb{C}$, every
continuous function $f : (\mathbb{R}/\mathbb{Z})^2 \to \mathbb{C}$ and every frequency
$n \in \mathbb{Z}^2$, the $n$-th Fourier coefficient (normalized Haar measure) satisfies
$\widehat{c f}(n) = c\, \hat f(n)$.

Formalized by `TorusSobolev.mFourierCoeff_smul`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#m-fourier-coeff-smul).

## Axis frequency

For $i \in \{0, 1\}$, the axis frequency $e_i$ is the frequency in
$\mathbb{Z}^2$ whose $i$-th coordinate is $1$ and whose other coordinate is $0$.

Formalized by `TorusSobolev.axisFrequency`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#axis-frequency).

## Lowest-shell unit polynomial

For $n \in \mathbb{Z}^2$ let
$e_n(y) = e^{2\pi i\, n \cdot y}$ be the Fourier monomial on the unit torus
$(\mathbb{R}/\mathbb{Z})^2$. The lowest-shell unit polynomial is the continuous function
$P : (\mathbb{R}/\mathbb{Z})^2 \to \mathbb{C}$ given by
$P = (4\pi)^{-1}\bigl(e_{(1,0)} + e_{(-1,0)} + e_{(0,1)} + e_{(0,-1)}\bigr)$, the normalized sum
of the Fourier monomials of the four nonzero frequencies of smallest length.

Formalized by `TorusSobolev.lowestShellUnit`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-unit).

## Lowest-shell witness

The lowest-shell witness is the continuous real function $u$ on the
torus $(\mathbb{R}/2\pi\mathbb{Z})^2$ given by
$u(x_1, x_2) = \frac{1}{4\pi}(e^{i x_1} + e^{-i x_1} + e^{i x_2} + e^{-i x_2})
= \frac{\cos x_1 + \cos x_2}{2\pi}$,
the normalized sum of the four lowest nonzero Fourier modes.

Formalized by `TorusSobolev.lowestShellWitness`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-witness).

## The lowest-shell unit polynomial is real-valued

For every point $y$ of the unit torus
$(\mathbb{R}/\mathbb{Z})^2$, the lowest-shell unit polynomial $P$ satisfies
$\operatorname{Im} P(y) = 0$.

Its Fourier modes come in opposite pairs $\pm k$ with equal coefficients.

Formalized by `TorusSobolev.lowestShellUnit_im_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-unit-im-zero).

## Unit representative of the lowest-shell witness

The unit representative of the
lowest-shell witness is the lowest-shell polynomial
$(4\pi)^{-1}\bigl(e_{(1,0)} + e_{(-1,0)} + e_{(0,1)} + e_{(0,-1)}\bigr)$ on the unit torus
$(\mathbb{R}/\mathbb{Z})^2$, where $e_n(y) = e^{2\pi i\, n \cdot y}$ for $n \in \mathbb{Z}^2$.

Formalized by `TorusSobolev.unitRepresentative_lowestShellWitness`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#unit-representative-lowest-shell-witness).

## Lowest frequency shell

The lowest shell is the set $\{e_1, -e_1, e_2, -e_2\}$ of
frequencies in $\mathbb{Z}^2$, where $e_1 = (1, 0)$ and $e_2 = (0, 1)$; these are the four nonzero
frequencies of smallest length.

Formalized by `TorusSobolev.lowestShell`, a definition declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell).

## Fourier coefficients of the lowest-shell witness

For every frequency $k \in \mathbb{Z}^2$,
the Fourier coefficient of the lowest-shell witness at $k$ equals $1/2$ if $k$ lies in the
lowest shell, that is, $k$ is one of $(1, 0)$, $(-1, 0)$, $(0, 1)$, $(0, -1)$, and equals $0$
otherwise.

Formalized by `TorusSobolev.fourierCoefficient_lowestShellWitness`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#fourier-coefficient-lowest-shell-witness).

## The lowest-shell witness is in $H^2$

The lowest-shell witness $u$ belongs to the spectral
Sobolev space $H^2$: if $a_k(u)$ denotes its Fourier coefficients, the series
$\sum_{k \in \mathbb{Z}^2} (1 + |k|^2)^2 |a_k(u)|^2$ converges.

Formalized by `TorusSobolev.lowestShellWitness_isH2`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-witness-is-h2).

## Gradient energy of the lowest-shell witness

The gradient energy of the lowest-shell
witness equals $1$.

Formalized by `TorusSobolev.gradientEnergy_lowestShellWitness`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#gradient-energy-lowest-shell-witness).

## Laplacian energy of the lowest-shell witness

The Laplacian energy of the lowest-shell
witness equals $1$.

Formalized by `TorusSobolev.laplaceEnergy_lowestShellWitness`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#laplace-energy-lowest-shell-witness).

## The mean is the real part of the zeroth Fourier coefficient

For every continuous
function $u : \mathbb{T} \to \mathbb{R}$ on the torus $\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$,
the mean of $u$ equals the real part of the zeroth Fourier coefficient
$\int_{(\mathbb{R}/\mathbb{Z})^2} \tilde u(y)\,dy$, taken with respect to normalized Haar measure,
of the unit representative $\tilde u$ of $u$ (the function $u$, viewed as complex-valued and
transported to the unit-period torus $(\mathbb{R}/\mathbb{Z})^2$).

Formalized by `TorusSobolev.mean_eq_mFourierCoeff_zero_re`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#mean-eq-m-fourier-coeff-zero-re).

## The lowest-shell witness has mean zero

The lowest-shell witness, the function
$w(x_1, x_2) = (\cos x_1 + \cos x_2)/(2\pi)$ on the torus $(\mathbb{R}/2\pi\mathbb{Z})^2$, has
mean $0$.

Formalized by `TorusSobolev.mean_lowestShellWitness`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#mean-lowest-shell-witness).

## The unit rescaling fixes the origin

The coordinate rescaling from the torus
$(\mathbb{R}/2\pi\mathbb{Z})^2$ to the unit torus $(\mathbb{R}/\mathbb{Z})^2$ maps $0$ to $0$.

Formalized by `TorusSobolev.unitRescaling_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#unit-rescaling-zero).

## Value of the lowest-shell witness at the origin

The lowest-shell witness $u$ takes the
value $u(0) = 1/\pi$ at the origin of the torus.

Formalized by `TorusSobolev.lowestShellWitness_at_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-witness-at-zero).

## The lowest-shell witness is a zero-mean $H^2$ function

The lowest-shell witness $u$
belongs to the spectral Sobolev space $H^2$ and has mean $0$.

Formalized by `TorusSobolev.lowestShellWitness_isZeroMeanH2`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-witness-is-zero-mean-h2).

## The lowest-shell witness is admissible at $\delta = 1$

The lowest-shell witness $u$
satisfies the conditional constraints with $\delta = 1$: it is a zero-mean $H^2$ function on the
torus, its gradient energy is $1$, and its Laplacian energy is $1$.

Formalized by `TorusSobolev.lowestShellWitness_admissible`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#lowest-shell-witness-admissible).

## Upper bounds for the conditional supremum

Let $\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$.
For every real $\delta$, let $\theta(\delta)$, the conditional supremum, be the supremum in the
extended reals of $u(0)^2$ over all continuous functions $u : \mathbb{T} \to \mathbb{R}$ that are
conditionally admissible at $\delta$, that is, zero-mean $H^2$ functions with gradient energy $1$
and Laplacian energy $\delta$. Then for every extended real number $b$, $\theta(\delta) \le b$ if
and only if $u(0)^2 \le b$ for every such $u$.

Formalized by `TorusSobolev.theta_le_iff`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#theta-le-iff).

## Upper bounds for the sharp remainder

Let $\mathbb{T} = (\mathbb{R}/2\pi\mathbb{Z})^2$. For
real $\delta$, let $\theta(\delta)$ be the supremum in the extended reals of $u(0)^2$ over all
continuous functions $u : \mathbb{T} \to \mathbb{R}$ that are zero-mean $H^2$ functions with
gradient energy $1$ and Laplacian energy $\delta$, and let
$R(\delta) = 4\pi\,\theta(\delta) - \log\delta - \log(1 + \log\delta)$, computed in the extended
reals. For every extended real number $b$, the sharp remainder value
$\sup_{\delta \ge 1} R(\delta)$, a supremum in the extended reals, is at most $b$ if and only if
$R(\delta) \le b$ for every real $\delta \ge 1$.

Formalized by `TorusSobolev.sharpRemainderValue_le_iff`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#sharp-remainder-value-le-iff).

## Frequency weights are nonnegative

For every frequency $k = (k_0, k_1) \in \mathbb{Z}^2$,
the frequency weight $k_0^2 + k_1^2$ is nonnegative.

Formalized by `TorusSobolev.frequencyWeight_nonneg`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#frequency-weight-nonneg).

## $H^2$ functions have a summable gradient energy series

If $u$ is a continuous real
function on the torus of period $2\pi$ that lies in $H^2$, with Fourier coefficients $a_k$, then
the family $\left((k_0^2 + k_1^2) \, |a_k|^2\right)_{k \in \mathbb{Z}^2}$ is summable.

Formalized by `TorusSobolev.IsH2.gradient_summable`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#gradient-summable).

## $H^2$ functions have a summable Laplacian energy series

If $u$ is a continuous real
function on the torus of period $2\pi$ that lies in $H^2$, with Fourier coefficients $a_k$, then
the family $\left((k_0^2 + k_1^2)^2 \, |a_k|^2\right)_{k \in \mathbb{Z}^2}$ is summable.

Formalized by `TorusSobolev.IsH2.laplace_summable`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#laplace-summable).

## Fourier reconstruction

Let $u$ be a continuous real function on the torus of period
$2\pi$ in each coordinate, let $a_k$ ($k \in \mathbb{Z}^2$) be its Fourier coefficients, and let
$c_k = a_k / (2\pi)$ be the Fourier coefficients, with respect to normalized Haar measure, of its
unit representative on $(\mathbb{R}/\mathbb{Z})^2$. If the family $(c_k)_{k \in \mathbb{Z}^2}$
is summable, then for every point $x$ of the torus, with unit rescaling
$y \in (\mathbb{R}/\mathbb{Z})^2$, the series
$\sum_{k \in \mathbb{Z}^2} (2\pi)^{-1} a_k \, e^{2\pi i (k_0 y_0 + k_1 y_1)}$ converges
unconditionally to $u(x)$.

Formalized by `TorusSobolev.fourierReconstruction`, a theorem declared in [MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/TorusSobolev/Fourier.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html#fourier-reconstruction).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier coefficients and the lowest-shell witness](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/brezis-gallou-t-inequality-on-the-two-dimensiona/fourier-coefficients-and-the-lowest-shell-witnes)
