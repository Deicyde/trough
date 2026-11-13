---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.InfConvolutionLipschitzWanted.g, MathlibExt.MeasureTheory.InfConvolutionLipschitzWanted.abs_toReal_g_sub_le_mul_dist
statement: formalized
---

# Lipschitz regularization by inf-convolution

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/lipschitz-regularization-by-inf-convolution/index.html).

## Inf-convolution with a multiple of the distance

Let $X$ be a metric space with metric
$d$, let $f : X \to [0,\infty]$, and let $n$ be a natural number. For $x \in X$,

$$
g_n(x) = \inf\{f(p) + n\,d(x,p) : p \in X\},
$$

the infimum being taken in $[0,\infty]$.

Formalized by `MathlibExt.MeasureTheory.InfConvolutionLipschitzWanted.g`, a definition declared in [WantedExt/MeasureTheory/InfConvolutionLipschitzWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/InfConvolutionLipschitzWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/lipschitz-regularization-by-inf-convolution/index.html#g).

## The inf-convolution of a lower semicontinuous function is Lipschitz

Let $X$ be a metric
space with metric $d$, and let $f : X \to [0,\infty]$ be lower semicontinuous with $f(p) < \infty$
for at least one $p \in X$. For a natural number $n$ and $x \in X$ let

$$
g_n(x) = \inf\{f(p) + n\,d(x,p) : p \in X\} \in [0,\infty].
$$

Then $|g_n(x) - g_n(y)| \le n\,d(x,y)$ for every natural number $n$ (including $n = 0$) and all
$x, y \in X$.

Each $g_n(x)$ is finite, since $g_n(x) \le f(p) + n\,d(x,p)$ for the point $p$ with
$f(p) < \infty$, so the difference is one of real numbers.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Nonlinear functional analysis), problem `ma_proofbench_l1_36`.

Stated but not proved: `MathlibExt.MeasureTheory.InfConvolutionLipschitzWanted.abs_toReal_g_sub_le_mul_dist` is written with `theorem_wanted` in [WantedExt/MeasureTheory/InfConvolutionLipschitzWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/InfConvolutionLipschitzWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/lipschitz-regularization-by-inf-convolution/index.html#abs-to-real-g-sub-le-mul-dist).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lipschitz regularization by inf-convolution](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/lipschitz-regularization-by-inf-convolution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/convex-analysis-and-variations/lipschitz-regularization-by-inf-convolution)
