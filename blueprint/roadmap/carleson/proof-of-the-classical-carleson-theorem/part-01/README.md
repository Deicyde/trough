---
navigation: transparent
---

# smooth approximation to Dirichlet approximation

- [smooth approximation](smooth-approximation.md)

We prove in Smooth functions.:

- [convergence for smooth](convergence-for-smooth.md)

We prove in The error bound:

- [control approximation effect](control-approximation-effect.md)

We are now ready to prove [classical Carleson](../../introduction/classical-carleson.md). We first prove a version with explicit exceptional sets.

- [classical Carleson with exceptional sets](exceptional-set-carleson.md)

Now we turn to the proof of the statement of Carleson theorem given in the introduction.

*Proof of classical Carleson: shown with [classical Carleson](../../introduction/classical-carleson.md).*

Let $\kappa:{\mathbb{R}}\to {\mathbb{C}}$ be the function defined by $\kappa(0)=0$ and for $0<|x|<1$

$$
\kappa(x)=\frac { 1-|x|}{1-e^{ix}}\,\qquad\text{(7)}
$$

and for $|x|\ge 1$,

$$
\kappa(x)=0\, .\qquad\text{(8)}
$$

Note that this function is continuous at every point $x$ with $|x|>0$.

The proof of [control approximation effect](control-approximation-effect.md) will use the following [real Carleson](real-carleson.md), which itself is proven in Carleson on the real line as an application of [metric space Carleson](../../introduction/metric-space-carleson.md).

- [real Carleson](real-carleson.md)

One of the main assumptions of [two-sided metric space Carleson](../../two-sided-metric-space-carleson/two-sided-metric-space-carleson.md), concerning the operator $T_r$ defined in [(2)](../../two-sided-metric-space-carleson/README.md), is verified by the following lemma, which is proved in The truncated Hilbert transform.

- [Hilbert strong 2 2](hilbert-strong-2-2.md)

The next lemma will be used to verify that the collection ${\Theta}$ of modulation functions in our application of [metric space Carleson](../../introduction/metric-space-carleson.md) satisfies the condition [(12)](../../introduction/README.md). It is proved in The proof of the van der Corput Lemma.

- [van der Corput](van-der-corput.md)

We close this section with five lemmas that are used across the following subsections.

- [Dirichlet kernel](dirichlet-kernel.md)
- [lower secant bound](lower-secant-bound.md)

The following lemma will be proved in Partial sums as orthogonal projections.

- [spectral projection bound](spectral-projection-bound.md)
- [Hilbert kernel bound](hilbert-kernel-bound.md)
- [Hilbert kernel regularity](hilbert-kernel-regularity.md)

## Smooth functions.

- [fourier-coeff-derivative](fourier-coeff-derivative.md)
- [convergence-of-coeffs-summable](convergence-of-coeffs-summable.md)
- [convergence-for-twice-contdiff](convergence-for-twice-contdiff.md)

*Proof of convergence for smooth: shown with [convergence for smooth](convergence-for-smooth.md).*

## The truncated Hilbert transform

Let $M_n$ be the modulation operator acting on measurable $2\pi$-periodic functions defined by

$$
M_ng(x)=g(x) e^{inx}\, .
$$

Define the approximate Hilbert transform by

$$
L_N g=\frac 1N\sum_{n=0}^{N-1}
M_{n+N} S_{N+n}M_{-N-n}g\, .
$$

- [modulated averaged projection](modulated-averaged-projection.md)
- [periodic domain shift](periodic-domain-shift.md)
- [Young convolution](young-convolution.md)

For $0\lt r<1$, Define the kernel $k_r$ to be the $2\pi$-periodic function

$$
k_r(x):=\min \left(r^{-1}, 1+\frac r{|1-e^{ix}|^2}\right)\, ,
$$

where the minimum is understood to be $r^{-1}$ in case $1=e^{ix}$.

- [integrable bump convolution](integrable-bump-convolution.md)
- [Dirichlet approximation](dirichlet-approximation.md)
