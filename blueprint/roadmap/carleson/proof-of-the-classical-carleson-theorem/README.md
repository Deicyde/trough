# Proof of The Classical Carleson Theorem

The convergence of partial Fourier sums is proved in The classical Carleson theorem in two steps. In the first step, we establish convergence on a suitable dense subclass of functions. We choose smooth functions as subclass, the convergence is stated in [convergence for smooth](part-01/convergence-for-smooth.md) and proved in Smooth functions.. In the second step, one controls the relevant error of approximating a general function by a function in the subclass. This is stated in [control approximation effect](part-01/control-approximation-effect.md) and proved in The error bound. The proof relies on a bound on the real Carleson maximal operator stated in [real Carleson](part-01/real-carleson.md) and proved in Carleson on the real line, which involves showing that the real line fits into the setting of [Proof of Metric Space Carleson, overview](../proof-of-metric-space-carleson-overview/README.md). This latter proof refers to the two-sided variant of the Carleson [two-sided metric space Carleson](../two-sided-metric-space-carleson/two-sided-metric-space-carleson.md). Two assumptions in [metric space Carleson](../introduction/metric-space-carleson.md) require more work. The boundedness of the operator $T_r$ defined in [(2)](../two-sided-metric-space-carleson/README.md) is established in [Hilbert strong 2 2](part-01/hilbert-strong-2-2.md). This lemma is proved in The truncated Hilbert transform. The cancellative property is verified by [van der Corput](part-01/van-der-corput.md), which is proved in The proof of the van der Corput Lemma. Several further auxiliary lemmas are stated and proved in The classical Carleson theorem, the proof of one of these auxiliary lemmas, [spectral projection bound](part-01/spectral-projection-bound.md), is done in Partial sums as orthogonal projections.

All subsections past The classical Carleson theorem are mutually independent.

## The classical Carleson theorem

Let a uniformly continuous $2\pi$-periodic function $f:{\mathbb{R}}\to \mathbb{C}$ and $\epsilon>0$ be given. Let

$$
C_{a,q} := \frac{2^{474a^3}}{(q-1)^6}
$$

denote the constant from [two-sided metric space Carleson](../two-sided-metric-space-carleson/two-sided-metric-space-carleson.md). Define

$$
\epsilon' := \frac {\epsilon} {4 C_\epsilon} \,,
$$

where

$$
C_\epsilon = \left(\frac{8}{\pi\epsilon}\right)^\frac{1}{2} C_{4,2} + \pi \,.
$$

Since $f$ is continuous and periodic, $f$ is uniformly continuous. Thus, there is a $0\lt \delta\lt \pi$ such that for all $x,x' \in {\mathbb{R}}$ with $|x-x'|\le \delta$ we have

$$
|f(x)-f(x')|\le \epsilon' \, .\qquad\text{(1)}
$$

Define

$$
f_0:=f \ast \phi_\delta,\qquad\text{(2)}
$$

where $\phi_\delta$ is a nonnegative smooth bump function with $\operatorname{\operatorname{supp}} (\phi_\delta) \subset (-\delta, \delta)$ and $\int _{\mathbb{R}} \phi_\delta (x) \, dx = 1$.

## [smooth approximation to Dirichlet approximation](part-01/README.md)

- [smooth approximation](part-01/smooth-approximation.md)
- [convergence for smooth](part-01/convergence-for-smooth.md)
- [control approximation effect](part-01/control-approximation-effect.md)
- [classical Carleson with exceptional sets](part-01/exceptional-set-carleson.md)
- [real Carleson](part-01/real-carleson.md)
- [Hilbert strong 2 2](part-01/hilbert-strong-2-2.md)
- [van der Corput](part-01/van-der-corput.md)
- [Dirichlet kernel](part-01/dirichlet-kernel.md)
- [lower secant bound](part-01/lower-secant-bound.md)
- [spectral projection bound](part-01/spectral-projection-bound.md)
- [Hilbert kernel bound](part-01/hilbert-kernel-bound.md)
- [Hilbert kernel regularity](part-01/hilbert-kernel-regularity.md)
- [fourier-coeff-derivative](part-01/fourier-coeff-derivative.md)
- [convergence-of-coeffs-summable](part-01/convergence-of-coeffs-summable.md)
- [convergence-for-twice-contdiff](part-01/convergence-for-twice-contdiff.md)
- [modulated averaged projection](part-01/modulated-averaged-projection.md)
- [periodic domain shift](part-01/periodic-domain-shift.md)
- [Young convolution](part-01/young-convolution.md)
- [integrable bump convolution](part-01/integrable-bump-convolution.md)
- [Dirichlet approximation](part-01/dirichlet-approximation.md)

## [Dirichlet kernel - Hilbert… to real van der Corput](part-02/README.md)

- [Dirichlet kernel - Hilbert kernel relation](part-02/dirichlet-hilbert.md)
- [partial Fourier sum bound](part-02/partial-fourier-sum-bound.md)
- [real Carleson operator measurable](part-02/real-carleson-operator-measurable.md)
- [partial Fourier sums of small](part-02/partial-fourier-sums-of-small.md)
- [real line metric](part-02/real-line-metric.md)
- [real line ball](part-02/real-line-ball.md)
- [real line measure](part-02/real-line-measure.md)
- [real line ball measure](part-02/real-line-ball-measure.md)
- [real line doubling](part-02/real-line-doubling.md)
- [frequency metric](part-02/frequency-metric.md)
- [oscillation control](part-02/oscillation-control.md)
- [frequency monotone](part-02/frequency-monotone.md)
- [frequency ball doubling](part-02/frequency-ball-doubling.md)
- [frequency ball growth](part-02/frequency-ball-growth.md)
- [integer ball cover](part-02/integer-ball-cover.md)
- [real van der Corput](part-02/real-van-der-corput.md)
