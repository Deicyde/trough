---
declaration: section
origin: cited
lean: MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.radon, MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.fourier1, MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.fourier2, MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.radon_can_be_diagonalized_and_pseudo_inverted
statement: formalized
---

# Radon transform

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform/index.html).

## Radon transform on the plane

For $f : \mathbb{R}^2 \to \mathbb{C}$ and
$p, \theta \in \mathbb{R}$, the Radon transform of $f$ at $(p, \theta)$ is the integral of $f$
along the line $x \cos\theta + y \sin\theta = p$ with respect to arc length,

$$Rf(p, \theta) = \int_{\mathbb{R}} f(p\cos\theta - t\sin\theta, p\sin\theta + t\cos\theta)\,dt,$$

where the integral is taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.radon`, a definition declared in [WantedExt/Analysis/RadonTransformWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RadonTransformWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform/index.html#radon).

## One-dimensional Fourier transform

For $g : \mathbb{R} \to \mathbb{C}$ and
$k \in \mathbb{R}$, the Fourier transform of $g$ at $k$ is

$$\hat g(k) = \int_{\mathbb{R}} e^{-2\pi i p k} \, g(p) \, dp,$$

where the integral is taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.fourier1`, a definition declared in [WantedExt/Analysis/RadonTransformWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RadonTransformWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform/index.html#fourier1).

## Two-dimensional Fourier transform

For $f : \mathbb{R}^2 \to \mathbb{C}$ and
$k = (k_1, k_2) \in \mathbb{R}^2$, the Fourier transform of $f$ at $k$ is

$$\hat f(k) = \int_{\mathbb{R}^2} e^{-2\pi i (x_1 k_1 + x_2 k_2)} \, f(x) \, dx,$$

where $dx$ is Lebesgue measure on $\mathbb{R}^2$ and the integral is taken to be $0$ when the
integrand is not integrable.

Formalized by `MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.fourier2`, a definition declared in [WantedExt/Analysis/RadonTransformWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RadonTransformWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform/index.html#fourier2).

## Fourier slice theorem and injectivity of the Radon transform on Schwartz functions

Write $R$ for the Radon transform, $\hat g$ for the one-dimensional Fourier transform of
$g : \mathbb{R} \to \mathbb{C}$ and $\hat f$ for the two-dimensional Fourier transform of
$f : \mathbb{R}^2 \to \mathbb{C}$. For every Schwartz function
$\varphi : \mathbb{R}^2 \to \mathbb{C}$ and all $\theta, k \in \mathbb{R}$, the Fourier transform
of $p \mapsto R\varphi(p, \theta)$ at $k$ equals $\hat\varphi(k\cos\theta, k\sin\theta)$.
Moreover, there is a map $S$ sending functions $\mathbb{R}^2 \to \mathbb{C}$ to functions
$\mathbb{R}^2 \to \mathbb{C}$ such that $S(R\varphi) = \varphi$ for every Schwartz function
$\varphi$.

The second part says only that $R$ is injective on Schwartz functions; no formula, linearity or
continuity is asserted for the left inverse $S$.

## Sources

- J. Radon (1917); R. N. Bracewell (Fourier slice theorem, 1956). Knill, *Some fundamental theorems in mathematics*, §100. Problem `radon_transform_inversion` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RadonTransformWanted.Analysis.RadonTransform.radon_can_be_diagonalized_and_pseudo_inverted` is written with `theorem_wanted` in [WantedExt/Analysis/RadonTransformWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RadonTransformWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform/index.html#radon-can-be-diagonalized-and-pseudo-inv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radon transform](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/integral-transforms/radon-transform)
