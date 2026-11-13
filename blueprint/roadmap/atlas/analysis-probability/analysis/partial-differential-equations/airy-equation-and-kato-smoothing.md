---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.AiryKatoSmoothingIdentityWanted.AirySolution, MathlibExt.Analysis.Fourier.AiryKatoSmoothingIdentityWanted.exists_pos_const_integral_norm_deriv_airySolution_sq_eq
statement: formalized
---

# Airy equation and Kato smoothing

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/airy-equation-and-kato-smoothing/index.html).

## Fourier solution of the Airy equation

For $u_0 : \mathbb{R} \to \mathbb{C}$, let
$\widehat{u_0}(\xi) = (2\pi)^{-1/2} \int_{\mathbb{R}} u_0(y) e^{-iy\xi}\,dy$ be its unitary
Fourier transform. The Airy solution with initial datum $u_0$ is the function
$u : \mathbb{R}^2 \to \mathbb{C}$ given by

$$u(t, x) = (2\pi)^{-1/2} \int_{\mathbb{R}} e^{i(t\xi^3 + x\xi)}\, \widehat{u_0}(\xi)\,d\xi,$$

where an integral whose integrand is not integrable is taken to be $0$.

For $u_0 \in C_c^\infty(\mathbb{R})$ this function solves the Airy equation
$\partial_t u + \partial_x^3 u = 0$ with $u(0, \cdot) = u_0$.

Formalized by `MathlibExt.Analysis.Fourier.AiryKatoSmoothingIdentityWanted.AirySolution`, a definition declared in [WantedExt/Analysis/Fourier/AiryKatoSmoothingIdentityWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/AiryKatoSmoothingIdentityWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/airy-equation-and-kato-smoothing/index.html#airy-solution).

## Kato smoothing identity for the Airy equation

For $u_0 : \mathbb{R} \to \mathbb{C}$ let
$\widehat{u_0}(\xi) = (2\pi)^{-1/2} \int_{\mathbb{R}} u_0(y) e^{-iy\xi}\,dy$ be its unitary
Fourier transform, and let
$u(t, x) = (2\pi)^{-1/2} \int_{\mathbb{R}} e^{i(t\xi^3 + x\xi)}\, \widehat{u_0}(\xi)\,d\xi$ be
the Airy solution with initial datum $u_0$. There is a constant $c_0 > 0$ such that for every
smooth compactly supported $u_0 : \mathbb{R} \to \mathbb{C}$ and every $x_0 \in \mathbb{R}$, the
function $t \mapsto \partial_x u(t, x_0)$ belongs to $L^2(\mathbb{R})$ and

$$\int_{\mathbb{R}} |\partial_x u(t, x_0)|^2\,dt = c_0 \int_{\mathbb{R}} |u_0(x)|^2\,dx.$$

The source's formalization used the transform $\int u_0(y) e^{-2\pi i y\xi}\,dy$ together with
the unitary phase and prefactor, so its initial datum was not $u_0$ but the $L^2$-isometric
rescaling $x \mapsto (2\pi)^{-1/2} u_0(x / 2\pi)$; the identity holds for both with the same
$c_0$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Distributions, generalized functions, distribution spaces), problem `ma_proofbench_l2_27`, with the change above.

Stated but not proved: `MathlibExt.Analysis.Fourier.AiryKatoSmoothingIdentityWanted.exists_pos_const_integral_norm_deriv_airySolution_sq_eq` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/AiryKatoSmoothingIdentityWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/AiryKatoSmoothingIdentityWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/airy-equation-and-kato-smoothing/index.html#exists-pos-const-integral-norm-deriv-air).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Airy equation and Kato smoothing](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/airy-equation-and-kato-smoothing/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/partial-differential-equations/airy-equation-and-kato-smoothing)
