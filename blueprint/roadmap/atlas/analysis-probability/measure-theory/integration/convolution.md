---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.ConvolutionIntegrableBoundedUniformWanted.uniformContinuous_convolution_integrable_bounded, MathlibExt.MeasureTheory.ConvolutionIntegrandIntegrableEuclideanWanted.integrable_comp_sub_mul_of_integrable_fin_append, MathlibExt.MeasureTheory.ExponentialKernelApproxIdentityWanted.tendsto_mul_integral_integral_exp_neg_two_mul_abs_sub
statement: formalized
---

# Convolution

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convolution/index.html).

## Convolution of an integrable and a bounded function is uniformly continuous

Let
$d \in \mathbb{N}$, let $f : \mathbb{R}^d \to \mathbb{R}$ be Lebesgue integrable, and let
$g : \mathbb{R}^d \to \mathbb{R}$ be Borel measurable and bounded. Then the convolution

$$
(f * g)(x) = \int_{\mathbb{R}^d} f(x - y)\, g(y)\, dy
$$

is uniformly continuous on $\mathbb{R}^d$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l1_15`.

Stated but not proved: `MathlibExt.MeasureTheory.ConvolutionIntegrableBoundedUniformWanted.uniformContinuous_convolution_integrable_bounded` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ConvolutionIntegrableBoundedUniformWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ConvolutionIntegrableBoundedUniformWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convolution/index.html#uniform-continuous-convolution-integrabl).

## Integrability of the convolution integrand

Let $d \in \mathbb{N}$ and let
$f, g : \mathbb{R}^d \to \mathbb{R}$ be Lebesgue integrable. Identify $\mathbb{R}^{2d}$ with
$\mathbb{R}^d \times \mathbb{R}^d$ by writing a point as $(x, y)$, where $x$ consists of its first
$d$ coordinates and $y$ of its last $d$ coordinates. Then the function
$(x, y) \mapsto f(x - y)\, g(y)$ is Lebesgue integrable on $\mathbb{R}^{2d}$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Measure and integration; Classical measure theory), problem `ma_proofbench_l1_72`.

Stated but not proved: `MathlibExt.MeasureTheory.ConvolutionIntegrandIntegrableEuclideanWanted.integrable_comp_sub_mul_of_integrable_fin_append` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ConvolutionIntegrandIntegrableEuclideanWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ConvolutionIntegrandIntegrableEuclideanWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convolution/index.html#integrable-comp-sub-mul-of-integrable-fi).

## Exponential kernel approximate identity

For every function $f : \mathbb{R} \to \mathbb{R}$
in $L^2(\mathbb{R})$,

$$
\lim_{n\to\infty} n\int_{\mathbb{R}}\int_{\mathbb{R}} f(x)f(y)e^{-2n|x-y|}\,dy\,dx
= \int_{\mathbb{R}} f(x)^2\,dx,
$$

where $n$ runs through the natural numbers and the integrals are with respect to Lebesgue measure.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_96`.

Stated but not proved: `MathlibExt.MeasureTheory.ExponentialKernelApproxIdentityWanted.tendsto_mul_integral_integral_exp_neg_two_mul_abs_sub` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ExponentialKernelApproxIdentityWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ExponentialKernelApproxIdentityWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convolution/index.html#tendsto-mul-integral-integral-exp-neg-tw).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convolution](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convolution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/integration/convolution)
