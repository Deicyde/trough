---
declaration: section
origin: cited
lean: Fourier.fourierLaplace, Fourier.fourierLaplace_ofReal, Fourier.hasDerivAt_fourierLaplace, Fourier.differentiable_fourierLaplace
statement: formalized
proof: formalized
---

# Fourier–Laplace transform

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform/index.html).

## Fourier–Laplace transform

For $f : \mathbb{R} \to \mathbb{C}$ and $z \in \mathbb{C}$,
the Fourier–Laplace transform of $f$ at $z$ is the Lebesgue integral
$\int_{\mathbb{R}} f(x) \, e^{-2\pi i x z} \, dx$, taken to be $0$ when the integrand is not
integrable.

Formalized by `Fourier.fourierLaplace`, a definition declared in [MathlibExt/Analysis/Fourier/FourierLaplace.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FourierLaplace.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform/index.html#fourier-laplace).

## Fourier–Laplace transform on the real axis

For every $f : \mathbb{R} \to \mathbb{C}$
and every real $r$, the Fourier–Laplace transform of $f$ at the complex number $r$, namely
$\int_{\mathbb{R}} f(x) \, e^{-2\pi i x r} \, dx$, equals the Fourier transform of $f$ at $r$
with the $2\pi$ normalization, $\hat f(r) = \int_{\mathbb{R}} e^{-2\pi i x r} f(x) \, dx$.

Formalized by `Fourier.fourierLaplace_ofReal`, a theorem declared in [MathlibExt/Analysis/Fourier/FourierLaplace.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FourierLaplace.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform/index.html#fourier-laplace-of-real).

## Derivative of the Fourier–Laplace transform

Let $f : \mathbb{R} \to \mathbb{C}$ be
integrable with compact support, and let $F(z) = \int_{\mathbb{R}} f(x) \, e^{-2\pi i x z} \, dx$
be its Fourier–Laplace transform. Then at every $z \in \mathbb{C}$, $F$ is complex differentiable
with derivative $F'(z) = \int_{\mathbb{R}} f(x) \, (-2\pi i x) \, e^{-2\pi i x z} \, dx$.

Formalized by `Fourier.hasDerivAt_fourierLaplace`, a theorem declared in [MathlibExt/Analysis/Fourier/FourierLaplace.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FourierLaplace.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform/index.html#has-deriv-at-fourier-laplace).

## The Fourier–Laplace transform of an integrable compactly supported function is entire

Let $f : \mathbb{R} \to \mathbb{C}$ be integrable with compact support. Then its Fourier–Laplace
transform $z \mapsto \int_{\mathbb{R}} f(x) \, e^{-2\pi i x z} \, dx$ is complex differentiable
at every $z \in \mathbb{C}$, that is, it is entire.

Formalized by `Fourier.differentiable_fourierLaplace`, a theorem declared in [MathlibExt/Analysis/Fourier/FourierLaplace.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/FourierLaplace.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform/index.html#differentiable-fourier-laplace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier–Laplace transform](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/fourier-laplace-transform)
