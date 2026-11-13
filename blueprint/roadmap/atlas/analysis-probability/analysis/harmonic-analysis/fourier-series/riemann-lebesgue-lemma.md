---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.norm_fourierCoeff_le_integral_norm, MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.tendsto_fourierCoeff_cofinite_of_continuous, MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.tendsto_fourierCoeff_cofinite, MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.tendsto_fourierCoeffOn_cofinite
statement: formalized
proof: formalized
---

# Riemann–Lebesgue lemma

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma/index.html).

## A Fourier coefficient is bounded by the L¹ norm

Let $T > 0$, let $\mu$ be the Haar
probability measure on the circle $\mathbb{R}/T\mathbb{Z}$, and let $E$ be a normed space over
$\mathbb{C}$. For every function $f : \mathbb{R}/T\mathbb{Z} \to E$ and every $n \in \mathbb{Z}$,
the $n$-th Fourier coefficient $\hat f(n) = \int e^{-2\pi i n t / T} f(t)\,d\mu(t)$ satisfies
$\|\hat f(n)\| \le \int \|f(t)\|\,d\mu(t)$.

The bound holds because $|e^{-2\pi i n t / T}| = 1$. No integrability is assumed: as usual for
the Bochner integral, an integral whose integrand is not integrable is $0$, and so is any
$E$-valued integral when $E$ is not complete.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.norm_fourierCoeff_le_integral_norm`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma/index.html#norm-fourier-coeff-le-integral-norm).

## Riemann–Lebesgue for continuous functions

Let $T > 0$ and let $\mu$ be the Haar
probability measure on the circle $\mathbb{R}/T\mathbb{Z}$. For every continuous function
$g : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$, the Fourier coefficients
$\hat g(n) = \int e^{-2\pi i n t / T} g(t)\,d\mu(t)$ tend to $0$ as $|n| \to \infty$, that is,
along the cofinite filter on $\mathbb{Z}$.

The proof uses Parseval's identity in $L^2(\mu)$: the sequence $|\hat g(n)|^2$ is summable, so
it tends to $0$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.tendsto_fourierCoeff_cofinite_of_continuous`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma/index.html#tendsto-fourier-coeff-cofinite-of-contin).

## Riemann–Lebesgue lemma on the circle

Let $T > 0$ and let $\mu$ be the Haar probability
measure on the circle $\mathbb{R}/T\mathbb{Z}$. For every $\mu$-integrable function
$f : \mathbb{R}/T\mathbb{Z} \to \mathbb{C}$, the Fourier coefficients
$\hat f(n) = \int e^{-2\pi i n t / T} f(t)\,d\mu(t)$ tend to $0$ as $|n| \to \infty$, that is,
along the cofinite filter on $\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.tendsto_fourierCoeff_cofinite`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma/index.html#tendsto-fourier-coeff-cofinite).

## Riemann–Lebesgue lemma on an interval

Let $a < b$ be real numbers and let
$f : \mathbb{R} \to \mathbb{C}$ be integrable on $[a, b]$. Then the Fourier coefficients of $f$
on $[a, b]$,

$$\hat f(n) = \frac{1}{b - a} \int_a^b e^{-2\pi i n x / (b - a)} f(x)\,dx,$$

tend to $0$ as $|n| \to \infty$, that is, along the cofinite filter on $\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.Fourier.AddCircle.RiemannLebesgue.tendsto_fourierCoeffOn_cofinite`, a theorem declared in [MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/AddCircle/RiemannLebesgue.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma/index.html#tendsto-fourier-coeff-on-cofinite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann–Lebesgue lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/riemann-lebesgue-lemma)
