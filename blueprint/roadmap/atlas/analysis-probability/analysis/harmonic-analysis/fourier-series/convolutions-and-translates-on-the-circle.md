---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Fourier.ConvolutionTranslateClosureCircleWanted.T, MathlibExt.Analysis.Fourier.ConvolutionTranslateClosureCircleWanted.closure_convolution_set_eq_closure_translate_span
statement: formalized
---

# Convolutions and translates on the circle

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convolutions-and-translates-on-the-circle/index.html).

## The circle $\mathbb{R}/2\pi\mathbb{Z}$

The circle $T = \mathbb{R}/2\pi\mathbb{Z}$, the
quotient of the additive group $\mathbb{R}$ by its subgroup $2\pi\mathbb{Z}$.

Formalized by `MathlibExt.Analysis.Fourier.ConvolutionTranslateClosureCircleWanted.T`, an abbreviation declared in [WantedExt/Analysis/Fourier/ConvolutionTranslateClosureCircleWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/ConvolutionTranslateClosureCircleWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convolutions-and-translates-on-the-circle/index.html#t).

## Convolutions and linear combinations of translates have the same closure

Let
$T = \mathbb{R}/2\pi\mathbb{Z}$ with the measure induced by Lebesgue measure on $[0, 2\pi)$, and
let $L^1(T)$ be the space of real-valued integrable functions on $T$ modulo equality almost
everywhere. Fix a real-valued integrable $f$ on $T$. Let $B_f \subseteq L^1(T)$ be the set of
classes of the finite linear combinations of translates
$x \mapsto \sum_{i=1}^N a_i f(x - \tau_i)$ with $N \in \mathbb{N}$, $a_i \in \mathbb{R}$ and
$\tau_i \in T$, and let $M_f \subseteq L^1(T)$ be the set of classes of the convolutions
$(f * g)(x) = \int_T f(y)\, g(x - y)\,dy$ with $g$ real-valued and integrable on $T$. Then $M_f$
and $B_f$ have the same closure in $L^1(T)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Commutative Banach algebras and commutative topological algebras), problem `ma_proofbench_l2_12`.

Stated but not proved: `MathlibExt.Analysis.Fourier.ConvolutionTranslateClosureCircleWanted.closure_convolution_set_eq_closure_translate_span` is written with `theorem_wanted` in [WantedExt/Analysis/Fourier/ConvolutionTranslateClosureCircleWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Fourier/ConvolutionTranslateClosureCircleWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convolutions-and-translates-on-the-circle/index.html#closure-convolution-set-eq-closure-trans).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convolutions and translates on the circle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-series/convolutions-and-translates-on-the-circle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-series/convolutions-and-translates-on-the-circle)
