---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.HeisenbergUncertainty.schwartz_integral_sq_eq_neg_two_mul, MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_real, MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_complex, MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_fourier, MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_shifted, MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_centered, MathlibExt.Analysis.Fourier.HeisenbergUncertaintyFourierWanted.integral_sq_mul_norm_sq_mul_integral_sq_mul_norm_fourier_sq_ge, MathlibExt.Analysis.Fourier.HeisenbergShiftedMomentsWanted.exists_const_sq_integral_sq_le_mul_shifted_moments_fourier
statement: formalized
---

# Heisenberg uncertainty principle

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html).

## Integration-by-parts identity for Heisenberg's inequality

The integration-by-parts identity underlying Heisenberg's inequality:
for real-valued Schwartz `f`, `∫ (f x)² = -2 * ∫ x * f x * f' x`.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertainty.schwartz_integral_sq_eq_neg_two_mul`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#schwartz-integral-sq-eq-neg-two-mul).

## Heisenberg's uncertainty principle

**Heisenberg's uncertainty principle** for real-valued Schwartz functions:
`(∫ (f x)²)² ≤ 4 * (∫ x² * (f x)²) * (∫ (f' x)²)`.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_real`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#heisenberg-uncertainty-real).

## Heisenberg's uncertainty principle

**Heisenberg's uncertainty principle** for complex-valued Schwartz functions:
`(∫ ‖f x‖²)² ≤ 4 * (∫ x² * ‖f x‖²) * (∫ ‖f' x‖²)`.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_complex`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#heisenberg-uncertainty-complex).

## Heisenberg's uncertainty principle

**Heisenberg's uncertainty principle** in Fourier form: with Mathlib's
Fourier normalization, the Fourier second moment about zero is `∫ ξ² * ‖𝓕 f ξ‖²`, and
`(∫ ‖f x‖²)² ≤ 16 * π² * (∫ x² * ‖f x‖²) * (∫ ξ² * ‖𝓕 f ξ‖²)`.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_fourier`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#heisenberg-uncertainty-fourier).

## Heisenberg's uncertainty principle

**Heisenberg's uncertainty principle** about an arbitrary center `a`:
the position second moment is measured about `a`; the derivative factor is unchanged.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_shifted`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#heisenberg-uncertainty-shifted).

## Heisenberg's uncertainty principle

**Heisenberg's uncertainty principle** with the position factor centered: for
`μ = (∫ y * ‖f y‖²) / (∫ ‖f x‖²)`, the position second moment about `μ` satisfies
the same bound. For positive L2 mass, `μ` is the mean position. Zero L2 mass occurs
only for `f = 0`, where `μ = 0 / 0 = 0` by Lean's convention.
Only the position factor is centered.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertainty.heisenberg_uncertainty_centered`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#heisenberg-uncertainty-centered).

## Heisenberg uncertainty principle

Denote by $\mathcal{S}(\mathbb{R})$ the Schwartz space on $\mathbb{R}$ consisting of all
complex-valued $C^\infty$ functions $f(x)$ on $\mathbb{R}$ such that
\[
\sup_{x\in\mathbb{R}} |x|^k \left|\frac{d^\ell f}{dx^\ell}(x)\right| < \infty
\quad\text{for all } k,\ell\in\mathbb{N}\cup\{0\}.
\]
Suppose $\psi(x)\in\mathcal{S}(\mathbb{R})$ satisfies
\[
\int_{-\infty}^{\infty}|\psi(x)|^2\,dx=1.
\]
Denote by $\hat{\psi}(\xi)$ the Fourier transform of $\psi(x)$ defined by
\[
\hat{\psi}(\xi)=\int_{-\infty}^{\infty}\psi(x)e^{-2\pi i x\xi}\,dx.
\]
The normalized Fourier Heisenberg corollary then gives
\[
\left(\int_{-\infty}^{\infty} x^2|\psi(x)|^2\,dx\right)
\left(\int_{-\infty}^{\infty} \xi^2|\hat{\psi}(\xi)|^2\,d\xi\right)
\ge \frac{1}{16\pi^2}.
\]

Lean variant: the Fourier transform is Mathlib's `𝓕`, which has the source's normalization `∫ ψ(x)
e^{-2πixξ} dx`, instead of the source's helper definition.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Distributions, generalized functions, distribution spaces), problem `ma_proofbench_l2_57`, with the change above.

Formalized by `MathlibExt.Analysis.Fourier.HeisenbergUncertaintyFourierWanted.integral_sq_mul_norm_sq_mul_integral_sq_mul_norm_fourier_sq_ge`, a theorem declared in [MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean, line 762](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/HeisenbergUncertainty.lean#L762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#integral-sq-mul-norm-sq-mul-integral-sq).

## Heisenberg uncertainty inequality with shifted moments

For a complex-valued Schwartz
function $f$ on $\mathbb{R}$, write
$\hat{f}(\xi) = \int_{\mathbb{R}} f(x) e^{-2\pi i x \xi}\, dx$ for its Fourier transform. There is
a constant $C > 0$ such that for all real numbers $c$ and $d$ and every complex-valued Schwartz
function $f$ on $\mathbb{R}$,

$$
\left(\int_{\mathbb{R}} |f(x)|^2\, dx\right)^2 \le C
\left(\int_{\mathbb{R}} (x - c)^2 |f(x)|^2\, dx\right)
\left(\int_{\mathbb{R}} (\xi - d)^2 |\hat{f}(\xi)|^2\, d\xi\right).
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Distributions, generalized functions, distribution spaces), problem `ma_proofbench_l2_46`.

Stated but not proved: `MathlibExt.Analysis.Fourier.HeisenbergShiftedMomentsWanted.exists_const_sq_integral_sq_le_mul_shifted_moments_fourier` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/HeisenbergShiftedMomentsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HeisenbergShiftedMomentsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#exists-const-sq-integral-sq-le-mul-shift).

## Weighted $L^2$ inequality for real Schwartz functions

For every real-valued Schwartz
function $f : \mathbb{R} \to \mathbb{R}$,

$$
\int_{\mathbb{R}} f(x)^2 \, dx \le 2 \left( \int_{\mathbb{R}} x^2 f(x)^2 \, dx \right)^{1/2}
\left( \int_{\mathbb{R}} f'(x)^2 \, dx \right)^{1/2},
$$

that is, $\|f\|_{L^2}^2 \le 2 \, \|x f\|_{L^2} \, \|f'\|_{L^2}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Inequalities in real analysis), problem `ma_proofbench_l2_40`.

Stated but not proved: `MathlibExt.Analysis.Fourier.SchwartzWeightedL2DerivInequalityWanted.integral_sq_le_two_mul_sqrt_integral_mul_sq_mul_sqrt_integral_deriv_sq` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/SchwartzWeightedL2DerivInequalityWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/SchwartzWeightedL2DerivInequalityWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html#integral-sq-le-two-mul-sqrt-integral-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heisenberg uncertainty principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/heisenberg-uncertainty-principle)
