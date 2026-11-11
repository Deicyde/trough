---
declaration: section
origin: cited
lean: MetaMathlibExt.mathieuFibonacciFourierCoefficient, MathlibExt.Analysis.Fourier.periodic_convolution
statement: formalized
proof: formalized
---

# Fourier series: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/index.html).

Fourier series on the circle and torus: Fejér and Dirichlet kernels, pointwise and Cesàro convergence, Riemann–Lebesgue, uniqueness, absolutely convergent series and Wiener's theorems, periodic convolution, Fourier optimization on the torus.

## Fourier coefficients of the Mathieu–Fibonacci periodic function

Let
$\varphi = (1 + \sqrt{5}) / 2$ be the golden ratio. For each natural number $n \ge 1$, the $n$-th
coefficient is the real number
$c_n = (2 / \log \varphi) \, |\Gamma(1 + 2 n \pi i / \log \varphi)|^2$, where $\Gamma$ is the
complex Gamma function.

In the source, these are the coefficients of the cosine series
$H(x) = 1 + \sum_{n \ge 1} c_n \cos(4 n \pi x / \log \varphi)$ of a periodic function $H$.

Formalized by `MetaMathlibExt.mathieuFibonacciFourierCoefficient`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/MathieuFibonacciFourierCoefficient.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/MathieuFibonacciFourierCoefficient.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/index.html#mathieu-fibonacci-fourier-coefficient).

## Periodic convolution

Let $A$ be a normed ring that is a normed algebra over
$\mathbb{R}$ (for example $\mathbb{R}$ or $\mathbb{C}$), let $T$ be a real number, and let
$f, g : \mathbb{R} \to A$ with $g$ periodic of period $T$, that is, $g(x + T) = g(x)$ for all
real $x$. Then the function $x \mapsto \int_0^T f(t)\, g(x - t)\, dt$ is periodic of period
$T$. The function $f$ need not be periodic or integrable.

Formalized by `MathlibExt.Analysis.Fourier.periodic_convolution`, a theorem declared in [MathlibExt/Analysis/Fourier/PeriodicConvolution.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/PeriodicConvolution.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/index.html#periodic-convolution).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series)
