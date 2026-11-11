---
declaration: section
origin: cited
lean: MeasureTheory.contDiff_integral_smul_comp_of_contDiff_of_hasCompactSupport, MathlibExt.MeasureTheory.DerivIntegralSeriesAbsContWanted.exists_hasDerivAt_integral_tsum_ae
statement: formalized
---

# Differentiation under the integral sign

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/differentiation-under-the-integral-sign/index.html).

## Smoothness of compactly supported parameter integrals

The integral `p ↦ ∫ x, w x • Ψ (c x, p) ∂μ` of a smooth compactly
supported function is smooth in the parameter `p`.

Formalized by `MeasureTheory.contDiff_integral_smul_comp_of_contDiff_of_hasCompactSupport`, a theorem declared in [MathlibExt/MeasureTheory/Measure/ParamSmooth.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/ParamSmooth.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/differentiation-under-the-integral-sign/index.html#cont-diff-integral-smul-comp-of-cont-dif).

## Differentiating an integral of a series term by term

Let $d \in \mathbb{N}$, let $\Omega$
be an open subset of $\mathbb{R}^d$, let $a < c < b$ be real numbers, and for each
$n \in \mathbb{N}$ let $f_n : \mathbb{R}^d \times \mathbb{R} \to \mathbb{C}$ be almost everywhere
measurable on $\Omega \times (a, b)$ with respect to Lebesgue measure. Write
$\partial_y f_n(x, y)$ for the derivative of $t \mapsto f_n(x, t)$ at $y$, taken to be $0$ where
this derivative does not exist, and give every series that does not converge absolutely the
sum $0$. Assume that:
(1) for each $n$ and almost every $x \in \Omega$, the function $y \mapsto f_n(x, y)$ is
absolutely continuous on $[a, b]$;
(2) each $\partial_y f_n$ is almost everywhere measurable on $\Omega \times (a, b)$, the series
$\sum_n |\partial_y f_n(x, y)|$ converges for almost every $(x, y) \in \Omega \times (a, b)$,
and its sum is integrable on $\Omega \times (a, b)$;
(3) the series $\sum_n |f_n(x, c)|$ converges for almost every $x \in \Omega$, and its sum is
integrable on $\Omega$.
Then there is a function $F : \mathbb{R} \to \mathbb{C}$ such that for almost every
$y \in (a, b)$ the function $x \mapsto \sum_n f_n(x, y)$ is integrable on $\Omega$,
$F(y) = \int_\Omega \sum_n f_n(x, y)\, dx$, and $F$ is differentiable at $y$ with

$$
F'(y) = \sum_n \int_\Omega \partial_y f_n(x, y)\, dx.
$$

The joint measurability of each $f_n$ is a hypothesis of the source that the first formalization
dropped. It is needed: for $d \ge 1$ and nonempty bounded $\Omega$, a non-measurable $f_0$ of
modulus one that does not depend on $y$, with $f_n = 0$ for $n \ge 1$, satisfies the other
hypotheses but not the conclusion.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_50`, with the change above.

Stated but not proved: `MathlibExt.MeasureTheory.DerivIntegralSeriesAbsContWanted.exists_hasDerivAt_integral_tsum_ae` is written with `theorem_wanted` in [WantedExt/MeasureTheory/DerivIntegralSeriesAbsContWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/DerivIntegralSeriesAbsContWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/differentiation-under-the-integral-sign/index.html#exists-has-deriv-at-integral-tsum-ae).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Differentiation under the integral sign](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/differentiation-under-the-integral-sign/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/integration/differentiation-under-the-integral-sign)
