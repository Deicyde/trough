---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.L2ConvolutionContinuousVanishingWanted.continuous_and_tendsto_cocompact_convolution_of_memLp_two, MetaMathlibExt.convolution_theorem, MathlibExt.Analysis.Fourier.HausdorffYoungSchwartzWanted.exists_norm_fourier_toLp_le_norm_toLp_of_holderConjugate
statement: formalized
---

# Fourier transform and uncertainty principles: its own results

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/index.html).

The Fourier transform on R^n and Schwartz functions: convolution, Bochner, Hausdorff–Young, Heisenberg and fractal uncertainty, band-limited functions and Bernstein inequalities, sampling and Fourier interpolation, Kakeya sets, Beurling–Ahlfors and other singular integrals.

## Convolution of two square-integrable functions is continuous and vanishes at infinity

Let $n$ be a natural number and let $f, g : \mathbb{R}^n \to \mathbb{C}$ be square-integrable.
Then the convolution $(f \ast g)(x) = \int_{\mathbb{R}^n} f(x - y) \, g(y) \, dy$ is a continuous
function of $x \in \mathbb{R}^n$, and $(f \ast g)(x) \to 0$ as $|x| \to \infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_17`.

Stated but not proved: `MathlibExt.Analysis.Fourier.L2ConvolutionContinuousVanishingWanted.continuous_and_tendsto_cocompact_convolution_of_memLp_two` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/L2ConvolutionContinuousVanishingWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/L2ConvolutionContinuousVanishingWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/index.html#continuous-and-tendsto-cocompact-convolu).

## Convolution theorem

Let $e$ be a continuous additive character from $\mathbb{R}$ to the
unit circle, and let $\mu$ be a σ-finite measure on $\mathbb{R}$ that is preserved by every
translation $x \mapsto a + x$. For $\varphi : \mathbb{R} \to \mathbb{C}$ write
$\hat\varphi(w) = \int e(-xw)\,\varphi(x)\,d\mu(x)$ for its Fourier transform with respect to
$e$ and $\mu$, and for $f, g : \mathbb{R} \to \mathbb{C}$ write
$(f * g)(x) = \int f(t)\,g(x - t)\,d\mu(t)$ for their convolution. If $f$ and $g$ are
$\mu$-integrable, then $\widehat{f * g}(w) = \hat f(w)\,\hat g(w)$ for every $w \in \mathbb{R}$.

Proof: Integrability of the convolution integrand, Fubini's theorem, translation invariance of
$\mu$ and multiplicativity of $e$, following Stein--Shakarchi, Ch. 5, Prop. 1.11.

## Sources

- https://en.wikipedia.org/wiki/Convolution_theorem.

Formalized by `MetaMathlibExt.convolution_theorem`, a theorem declared in [MathlibExt/Analysis/Fourier/ConvolutionTheorem.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Fourier/ConvolutionTheorem.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/index.html#convolution-theorem).

## Hausdorff–Young inequality for Schwartz functions

Let $n$ be a natural number and let
$\mathcal{F}$ be the Fourier transform on $\mathbb{R}^n$,
$\mathcal{F}f(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i \langle x, \xi \rangle}\, dx$. There is a
constant $C > 0$ such that for all $p, p' \in [0, \infty]$ with $1 \le p \le 2$ and
$\frac{1}{p} + \frac{1}{p'} = 1$ (so $p' = \infty$ when $p = 1$) and every complex-valued
Schwartz function $f$ on $\mathbb{R}^n$, $\|\mathcal{F}f\|_{L^{p'}} \le C \|f\|_{L^p}$, where the
$L^p$ norms are taken with respect to Lebesgue measure on $\mathbb{R}^n$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_84`.

Stated but not proved: `MathlibExt.Analysis.Fourier.HausdorffYoungSchwartzWanted.exists_norm_fourier_toLp_le_norm_toLp_of_holderConjugate` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/HausdorffYoungSchwartzWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/HausdorffYoungSchwartzWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/index.html#exists-norm-fourier-to-lp-le-norm-to-lp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier transform and uncertainty principles](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform)
