---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.HighFrequencySupNormSobolevBoundWanted.dotHSeminorm, MathlibExt.Analysis.Fourier.HighFrequencySupNormSobolevBoundWanted.sSup_norm_le_rpow_mul_dotHSeminorm_of_tsupport_fourier_compl_Icc
statement: formalized
---

# Sup-norm bounds for high-frequency functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-for-high-frequency-functions/index.html).

## Homogeneous Sobolev seminorm for the high-frequency sup-norm bound

For a real number $s$
and a Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with Fourier transform
$\hat f(\xi) = \int_{\mathbb{R}} e^{-2\pi i x \xi} f(x) \, dx$, the homogeneous Sobolev seminorm
of $f$ is

$$
\|f\|_{\dot H^s} = \left( \int_{\mathbb{R}} |\xi|^{2s} \, |\hat f(\xi)|^2 \, d\xi \right)^{1/2},
$$

where the integral is taken to be $0$ when the integrand is not integrable.

Formalized by `MathlibExt.Analysis.Fourier.HighFrequencySupNormSobolevBoundWanted.dotHSeminorm`, a definition declared in [WantedExt/Analysis/Fourier/HighFrequencySupNormSobolevBoundWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HighFrequencySupNormSobolevBoundWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-for-high-frequency-functions/index.html#dot-hseminorm).

## Sup bound for Schwartz functions with high-frequency Fourier support

Let
$s \in (\tfrac12, 1]$, and for a Schwartz function $f : \mathbb{R} \to \mathbb{C}$ with Fourier
transform $\hat f$ let
$\|f\|_{\dot H^s} = \left( \int_{\mathbb{R}} |\xi|^{2s} |\hat f(\xi)|^2 \, d\xi \right)^{1/2}$
be its homogeneous Sobolev seminorm. There is a constant $C_2 > 0$ such that for every real
$A > 0$ and every Schwartz function $f : \mathbb{R} \to \mathbb{C}$ whose Fourier transform has
closed support contained in $\mathbb{R} \setminus [-A, A]$,

$$
\sup_{x \in \mathbb{R}} |f(x)| \le C_2 \, A^{-s + \frac12} \, \|f\|_{\dot H^s}.
$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_05`.

Stated but not proved: `MathlibExt.Analysis.Fourier.HighFrequencySupNormSobolevBoundWanted.sSup_norm_le_rpow_mul_dotHSeminorm_of_tsupport_fourier_compl_Icc` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/HighFrequencySupNormSobolevBoundWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/HighFrequencySupNormSobolevBoundWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-for-high-frequency-functions/index.html#s-sup-norm-le-rpow-mul-dot-hseminorm-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sup-norm bounds for high-frequency functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/function-spaces/sup-norm-bounds-for-high-frequency-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/function-spaces/sup-norm-bounds-for-high-frequency-functions)
