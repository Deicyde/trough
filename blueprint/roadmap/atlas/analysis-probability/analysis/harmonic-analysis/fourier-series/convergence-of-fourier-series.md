---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.DirichletTheoremWanted.dirichlet_pointwise_convergence, MathlibExt.Analysis.FourierConvergenceWanted.Analysis.fourierPartialSum, MathlibExt.Analysis.FourierConvergenceWanted.Analysis.fourierCesaroMean, MathlibExt.Analysis.FourierConvergenceWanted.Analysis.dirichlet_pointwise, MathlibExt.Analysis.FourierConvergenceWanted.Analysis.fejer
statement: formalized
---

# Convergence of Fourier series

5 results, 2 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html).

## Dirichlet–Jordan theorem on pointwise convergence of Fourier series

Let
$f : \mathbb{R} \to \mathbb{C}$ be $2\pi$-periodic and of bounded variation on $[-\pi, \pi]$,
and for $n \in \mathbb{Z}$ let $c_n = \frac{1}{2\pi} \int_0^{2\pi} f(t) e^{-int}\,dt$ be its
Fourier coefficients. Then at every $x \in \mathbb{R}$ the one-sided limits
$f(x^+) = \lim_{y \to x,\, y > x} f(y)$ and $f(x^-) = \lim_{y \to x,\, y < x} f(y)$ exist, and
the symmetric partial sums of the Fourier series converge to their average:

$$\lim_{N \to \infty} \sum_{n=-N}^{N} c_n e^{inx} = \frac{f(x^+) + f(x^-)}{2}.$$

By periodicity, the coefficients $c_n$ equal the corresponding integrals over $[-\pi, \pi]$.

This is the bounded-variation (Dirichlet–Jordan) form. It is distinct from the version of
Dirichlet's theorem that assumes $f$ continuously differentiable and concludes convergence to
$f(x)$; here $f$ may be discontinuous and the limit is the average of the one-sided limits.

## Sources

- Y. Katznelson, *An Introduction to Harmonic Analysis*, 3rd ed., Ch. I, §5 (functions of bounded variation; Dirichlet–Jordan test).
- https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_Fourier_series

Stated but not proved: `MathlibExt.Analysis.Fourier.DirichletTheoremWanted.dirichlet_pointwise_convergence` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/DirichletTheoremWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/DirichletTheoremWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html#dirichlet-pointwise-convergence).

## Symmetric Fourier partial sums

For $f \colon \mathbb{R} \to \mathbb{C}$, a natural number
$N$ and $x \in \mathbb{R}$, the $N$-th symmetric Fourier partial sum of $f$ at $x$ is
$S_N(f)(x) = \sum_{n=-N}^{N} \hat f_n e^{inx}$, where
$\hat f_n = \frac{1}{2\pi} \int_0^{2\pi} e^{-int} f(t)\,dt$ is the $n$-th Fourier coefficient of $f$
on the interval $[0, 2\pi]$.

Formalized by `MathlibExt.Analysis.FourierConvergenceWanted.Analysis.fourierPartialSum`, a definition declared in [WantedExt/Analysis/FourierConvergenceWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FourierConvergenceWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html#fourier-partial-sum).

## Cesàro means of Fourier series

For $f \colon \mathbb{R} \to \mathbb{C}$, a natural number
$N$ and $x \in \mathbb{R}$, the $N$-th Cesàro mean of the Fourier series of $f$ at $x$ is the
average of the first $N + 1$ symmetric Fourier partial sums,
$\sigma_N(f)(x) = \frac{1}{N+1} \sum_{k=0}^{N} S_k(f)(x)$, where
$S_k(f)(x) = \sum_{n=-k}^{k} \hat f_n e^{inx}$ and
$\hat f_n = \frac{1}{2\pi} \int_0^{2\pi} e^{-int} f(t)\,dt$ is the $n$-th Fourier coefficient of
$f$ on the interval $[0, 2\pi]$.

Formalized by `MathlibExt.Analysis.FourierConvergenceWanted.Analysis.fourierCesaroMean`, a definition declared in [WantedExt/Analysis/FourierConvergenceWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FourierConvergenceWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html#fourier-cesaro-mean).

## Dirichlet's theorem on pointwise convergence of Fourier series

Let
$f \colon \mathbb{R} \to \mathbb{C}$ be $2\pi$-periodic and continuously differentiable, and for
$n \in \mathbb{Z}$ let $\hat f_n = \frac{1}{2\pi} \int_0^{2\pi} e^{-int} f(t)\,dt$ be the $n$-th
Fourier coefficient of $f$ on $[0, 2\pi]$. Then for every $x \in \mathbb{R}$ the symmetric Fourier
partial sums $S_N(f)(x) = \sum_{n=-N}^{N} \hat f_n e^{inx}$ converge to $f(x)$ as $N \to \infty$.

## Sources

- P. G. L. Dirichlet (1829) and L. Fejér (1900). Listed as §46 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `fourier_dirichlet_fejer` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.FourierConvergenceWanted.Analysis.dirichlet_pointwise` is written with `theorem_wanted` in [WantedExt/Analysis/FourierConvergenceWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FourierConvergenceWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html#dirichlet-pointwise).

## Fejér's theorem

Let $f \colon \mathbb{R} \to \mathbb{C}$ be continuous and
$2\pi$-periodic, and write $S_k(f)$ for the $k$-th symmetric Fourier partial sum of $f$. Then the
Cesàro means $\sigma_N(f) = (S_0(f) + S_1(f) + \dots + S_N(f)) / (N + 1)$ converge to $f$
uniformly on $\mathbb{R}$ as $N \to \infty$.

## Sources

- P. G. L. Dirichlet (1829) and L. Fejér (1900). Listed as §46 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `fourier_dirichlet_fejer` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.FourierConvergenceWanted.Analysis.fejer` is written with `theorem_wanted` in [WantedExt/Analysis/FourierConvergenceWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FourierConvergenceWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html#fejer).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convergence of Fourier series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/convergence-of-fourier-series)
