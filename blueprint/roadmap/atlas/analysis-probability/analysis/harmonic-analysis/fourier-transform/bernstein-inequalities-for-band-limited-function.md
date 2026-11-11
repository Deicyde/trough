---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.BandLimitedDerivSobolevBoundWanted.dotHSeminorm, MathlibExt.Analysis.Fourier.BandLimitedDerivSobolevBoundWanted.norm_deriv_le_rpow_mul_dotHSeminorm_of_fourier_support_Icc, MathlibExt.Analysis.Fourier.BernsteinFourierSupportLpLqWanted.exists_const_norm_toLp_le_volume_rpow_mul_norm_toLp_of_tsupport_fourier_subset, MathlibExt.Analysis.Fourier.BernsteinInequalityBandLimitedWanted.exists_norm_deriv_toLp_le_of_support_fourier_subset_ball
statement: formalized
---

# Bernstein inequalities for band-limited functions

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function/index.html).

## Homogeneous Sobolev seminorm (band-limited derivative bound)

For
$s \in \mathbb{R}$ and a Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with Fourier transform
$\hat f(\xi) = \int_{\mathbb{R}} f(x) e^{-2\pi i x\xi}\,dx$, the homogeneous Sobolev seminorm of
order $s$ is

$$\|f\|_{\dot H^s} = \left(\int_{\mathbb{R}} |\xi|^{2s}\, |\hat f(\xi)|^2\,d\xi\right)^{1/2},$$

where the integral is taken to be $0$ when its integrand is not integrable.

Formalized by `MathlibExt.Analysis.Fourier.BandLimitedDerivSobolevBoundWanted.dotHSeminorm`, a definition declared in [WantedExt/Analysis/Fourier/BandLimitedDerivSobolevBoundWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/BandLimitedDerivSobolevBoundWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function/index.html#dot-hseminorm).

## Bernstein-type bound for the derivative of a band-limited Schwartz function

Let
$s \in (\tfrac12, 1]$. For a Schwartz function $f : \mathbb{R} \to \mathbb{C}$ write
$\hat f(\xi) = \int_{\mathbb{R}} f(x) e^{-2\pi i x\xi}\,dx$ for its Fourier transform and
$\|f\|_{\dot H^s} = \left(\int_{\mathbb{R}} |\xi|^{2s} |\hat f(\xi)|^2\,d\xi\right)^{1/2}$ for
its homogeneous Sobolev seminorm. There is a constant $C_1 > 0$ such that for every real
$A \ge 0$ and every Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with $\hat f(\xi) = 0$
whenever $|\xi| > A$,

$$\sup_{x \in \mathbb{R}} |f'(x)| \le C_1 A^{3/2 - s}\, \|f\|_{\dot H^s}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_00`.

Stated but not proved: `MathlibExt.Analysis.Fourier.BandLimitedDerivSobolevBoundWanted.norm_deriv_le_rpow_mul_dotHSeminorm_of_fourier_support_Icc` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/BandLimitedDerivSobolevBoundWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/BandLimitedDerivSobolevBoundWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function/index.html#norm-deriv-le-rpow-mul-dot-hseminorm-of).

## Bernstein inequality for Schwartz functions with Fourier support of finite measure

Fix $n \in \mathbb{N}$. For a Schwartz function $f : \mathbb{R}^n \to \mathbb{C}$ write
$\hat f(\xi) = \int_{\mathbb{R}^n} f(x) e^{-2\pi i \langle x, \xi \rangle}\,dx$ for its Fourier
transform, and write $|E|$ for the Lebesgue measure of a set $E \subseteq \mathbb{R}^n$. There
is a constant $C > 0$ such that for every Borel set $E \subseteq \mathbb{R}^n$ with
$|E| < \infty$, all $p, q \in [1, \infty]$ with $p \le q$ and $p \le 2$, and every Schwartz
function $f : \mathbb{R}^n \to \mathbb{C}$ whose Fourier transform has closed support
$\overline{\{\xi : \hat f(\xi) \ne 0\}}$ contained in $E$,

$$\|f\|_{L^q(\mathbb{R}^n)} \le C\, |E|^{1/p - 1/q}\, \|f\|_{L^p(\mathbb{R}^n)},$$

where $1/q = 0$ for $q = \infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Distributions, generalized functions, distribution spaces), problem `ma_proofbench_l2_47`.

Stated but not proved: `MathlibExt.Analysis.Fourier.BernsteinFourierSupportLpLqWanted.exists_const_norm_toLp_le_volume_rpow_mul_norm_toLp_of_tsupport_fourier_subset` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/BernsteinFourierSupportLpLqWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/BernsteinFourierSupportLpLqWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function/index.html#exists-const-norm-to-lp-le-volume-rpow-m).

## Bernstein inequality for band-limited Schwartz functions

For a Schwartz function
$f : \mathbb{R} \to \mathbb{C}$ write $\hat f(\xi) = \int_{\mathbb{R}} f(x) e^{-2\pi i x\xi}\,dx$
for its Fourier transform. There is a constant $C_0 > 0$ such that for every $p \in [1, \infty]$
and every Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with $\hat f(\xi) = 0$ whenever
$|\xi| \ge 1$,

$$\|f'\|_{L^p(\mathbb{R})} \le C_0 \|f\|_{L^p(\mathbb{R})}.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_70`.

Stated but not proved: `MathlibExt.Analysis.Fourier.BernsteinInequalityBandLimitedWanted.exists_norm_deriv_toLp_le_of_support_fourier_subset_ball` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/BernsteinInequalityBandLimitedWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Fourier/BernsteinInequalityBandLimitedWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function/index.html#exists-norm-deriv-to-lp-le-of-support-fo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernstein inequalities for band-limited functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/bernstein-inequalities-for-band-limited-function)
