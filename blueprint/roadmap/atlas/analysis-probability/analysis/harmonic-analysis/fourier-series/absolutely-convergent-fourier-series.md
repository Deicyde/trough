---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.memLp_of_continuousOn_Ioc, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.liftPeriodicContinuousMap, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.liftPeriodicContinuousMap_apply, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.fourierCoeffOn_zero_add, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.fourierCoeff_liftPeriodicContinuousMap, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.norm_fourierCoeffOn_le_of_bound, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.fourierCoeffOn_eq_of_hasDerivAt, MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.norm_fourierCoeffOn_eq_of_hasDerivAt
statement: formalized
---

# Absolutely convergent Fourier series

16 results, 14 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html).

## Continuous functions are square-integrable on one period

A continuous function on `ℝ` is square-integrable on one period.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.memLp_of_continuousOn_Ioc`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#mem-lp-of-continuous-on-ioc).

## Lift of a periodic continuous function to the circle

A `T`-periodic continuous function descends to a continuous function on the
circle `AddCircle T`, via `AddCircle.liftIoc`.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.liftPeriodicContinuousMap`, a definition declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#lift-periodic-continuous-map).

## Lifted periodic function agrees with the original on a period

The descended function agrees with `f` on the period `(0, T]`.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.liftPeriodicContinuousMap_apply`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#lift-periodic-continuous-map-apply).

## Fourier coefficients on $(0, 0+T)$ equal those on $(0, T)$

The interval coefficients on `(0, 0 + T]` agree with those on `(0, T]`; this
bridges Mathlib's `fourierCoeff_liftIoc_eq`, which is stated on `(a, a + T]`.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.fourierCoeffOn_zero_add`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#fourier-coeff-on-zero-add).

## Fourier coefficients of the lifted periodic function

The Fourier coefficients of the descended function are the interval
coefficients `fourierCoeffOn`.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.fourierCoeff_liftPeriodicContinuousMap`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#fourier-coeff-lift-periodic-continuous-m).

## Fourier coefficient bounded by the sup norm on a period

A Fourier coefficient bounded by the sup norm on one period.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.norm_fourierCoeffOn_le_of_bound`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#norm-fourier-coeff-on-le-of-bound).

## Coefficient identity for a `C¹` periodic function

For `n ≠ 0`,
`ĉₙ(f) = (T / (2π i n)) · ĉₙ(f')`. The boundary term in integration by parts
vanishes by periodicity.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.fourierCoeffOn_eq_of_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#fourier-coeff-on-eq-of-has-deriv-at).

## Norm form of the coefficient identity

**Norm form of the coefficient identity.**

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.norm_fourierCoeffOn_eq_of_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#norm-fourier-coeff-on-eq-of-has-deriv-at).

## Fourier coefficients of a `C¹` periodic function are absolutely summable

**Fourier coefficients of a `C¹` periodic function are absolutely summable.**

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.summable_fourierCoeffOn_of_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#summable-fourier-coeff-on-of-has-deriv-a).

## Decay rate:

`n · ‖ĉₙ(f)‖ → 0` along the cofinite filter.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.tendsto_mul_norm_fourierCoeffOn_of_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#tendsto-mul-norm-fourier-coeff-on-of-has).

## Uniform convergence:

The Fourier series of a `C¹` periodic function
converges uniformly (in `C(AddCircle T, ℂ)`) to `f` on the circle.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.hasSum_fourier_series_of_hasDerivAt`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#has-sum-fourier-series-of-has-deriv-at).

## Pointwise convergence on one period

**Pointwise convergence on one period.**

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.C1FourierSummable.hasSum_fourier_series_of_hasDerivAt_apply`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/AddCircle/C1FourierSummable.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#has-sum-fourier-series-of-has-deriv-at-a).

## Wiener algebra on the circle

Let $T > 0$. A continuous function
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ lies in the Wiener algebra when the family of its
Fourier coefficients $\hat f(n) = \frac{1}{T} \int_0^T f(x) e^{-2\pi i n x / T} \, dx$,
$n \in \mathbb{Z}$, is summable in $\mathbb{C}$.

For complex families, summability is equivalent to $\sum_{n \in \mathbb{Z}} |\hat f(n)| < \infty$,
so these are the functions with absolutely convergent Fourier series.

Formalized by `MathlibExt.Analysis.WienerLevyWanted.Analysis.WienerLevy.InWienerAlgebra`, a definition declared in [WantedExt/Analysis/WienerLevyWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WienerLevyWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#in-wiener-algebra).

## Wiener–Lévy theorem

Let $T > 0$, and let $f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ be a
continuous function in the Wiener algebra. Let $U \subseteq \mathbb{C}$ be an open set containing
the range of $f$, and let $\varphi : \mathbb{C} \to \mathbb{C}$ be analytic at every point of $U$.
Then there is a continuous function $g : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ with
$g(x) = \varphi(f(x))$ for every $x$, and $g$ lies in the Wiener algebra.

## Sources

- P. Lévy, Sur la convergence absolue des séries de Fourier, Compositio Math. 1 (1935), 1-14; N. Wiener, Tauberian theorems, Ann. of Math. 33 (1932), 1-100. Listed as §226 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Knill, §226. Problem `wiener_levy_analytic_calculus` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.WienerLevyWanted.Analysis.WienerLevy.wiener_levy_analytic_calculus` is written with `theorem_wanted` in [WantedExt/Analysis/WienerLevyWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WienerLevyWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#wiener-levy-analytic-calculus).

## Functions with absolutely convergent Fourier series

Let $T > 0$. A continuous function
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ lies in the Wiener algebra when the family of its
Fourier coefficients $\hat f(n) = \frac{1}{T} \int_0^T f(x) e^{-2\pi i n x / T} \, dx$,
$n \in \mathbb{Z}$, is summable in $\mathbb{C}$.

For complex families, summability is equivalent to
$\sum_{n \in \mathbb{Z}} |\hat f(n)| < \infty$.

Formalized by `MathlibExt.Analysis.WienerOneOverFWanted.Analysis.WienerOneOverF.InWienerAlgebra`, a definition declared in [WantedExt/Analysis/WienerOneOverFWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WienerOneOverFWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#in-wiener-algebra-2).

## Wiener's 1/f theorem

Let $T > 0$, and let $f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ be
a continuous function in the Wiener algebra with $f(x) \ne 0$ for every $x$. Then there is a
continuous function $g : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$ with $g(x) = f(x)^{-1}$ for every
$x$, and $g$ lies in the Wiener algebra.

## Sources

- N. Wiener, Tauberian theorems, Ann. of Math. 33 (1932), 1-100. Listed as §226 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Knill, §226. Problem `wiener_inverse_closed` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.WienerOneOverFWanted.Analysis.WienerOneOverF.wiener_inverse_closed` is written with `theorem_wanted` in [WantedExt/Analysis/WienerOneOverFWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/WienerOneOverFWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html#wiener-inverse-closed).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Absolutely convergent Fourier series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/absolutely-convergent-fourier-series)
