---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SpecificLimits.ExpNegSqrtNormSelfConvolutionLimitWanted.f, MathlibExt.Analysis.SpecificLimits.ExpNegSqrtNormSelfConvolutionLimitWanted.tendsto_convolution_self_div_atTop_norm
statement: formalized
---

# Convolution asymptotics of subexponential functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/convolution-asymptotics-of-subexponential-functi/index.html).

## The function $e^{-\sqrt{\|x\|}}$ on the plane

Let $f : \mathbb{R}^2 \to \mathbb{R}$ be
$f(x) = e^{-\sqrt{\|x\|}}$, where $\|x\|$ is the Euclidean norm of $x$.

Formalized by `MathlibExt.Analysis.SpecificLimits.ExpNegSqrtNormSelfConvolutionLimitWanted.f`, a definition declared in [WantedExt/Analysis/SpecificLimits/ExpNegSqrtNormSelfConvolutionLimitWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/ExpNegSqrtNormSelfConvolutionLimitWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/convolution-asymptotics-of-subexponential-functi/index.html#f).

## Asymptotics of the self-convolution of $e^{-\sqrt{\|x\|}}$

Let $f : \mathbb{R}^2 \to
\mathbb{R}$ be $f(x) = e^{-\sqrt{\|x\|}}$, where $\|x\|$ is the Euclidean norm, and let $f * f$ be
the convolution of $f$ with itself with respect to Lebesgue measure. Then

$$\lim_{\|a\| \to \infty} \frac{(f * f)(a)}{f(a)} = 2 \int_{\mathbb{R}^2} f(x)\,dx.$$

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Measures, integration, derivative, holomorphy), problem `ma_proofbench_l2_90`.

Stated but not proved: `MathlibExt.Analysis.SpecificLimits.ExpNegSqrtNormSelfConvolutionLimitWanted.tendsto_convolution_self_div_atTop_norm` is written with `theorem_wanted` in [WantedExt/Analysis/SpecificLimits/ExpNegSqrtNormSelfConvolutionLimitWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/SpecificLimits/ExpNegSqrtNormSelfConvolutionLimitWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/convolution-asymptotics-of-subexponential-functi/index.html#tendsto-convolution-self-div-at-top-norm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convolution asymptotics of subexponential functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/convolution-asymptotics-of-subexponential-functi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/asymptotic-analysis/convolution-asymptotics-of-subexponential-functi)
