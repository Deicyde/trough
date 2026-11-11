---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.ContinuousBVDiffContinuousMonotoneWanted.exists_continuous_monotone_sub_of_boundedVariationOn, MathlibExt.MeasureTheory.IndicatorIccNotAEContinuousWanted.not_exists_continuous_ae_eq_indicator_Icc
statement: formalized
---

# Differentiation of real functions: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/index.html).

Absolutely continuous, Lipschitz and bounded-variation functions of a real variable, maximal functions and almost-everywhere properties of real functions.

## Jordan decomposition of a continuous function of bounded variation

Let
$F : \mathbb{R} \to \mathbb{R}$ be continuous and of bounded variation on all of $\mathbb{R}$.
Then there are continuous non-decreasing functions $F_1, F_2 : \mathbb{R} \to \mathbb{R}$ such
that $F = F_1 - F_2$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_33`.

Stated but not proved: `MathlibExt.MeasureTheory.ContinuousBVDiffContinuousMonotoneWanted.exists_continuous_monotone_sub_of_boundedVariationOn` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ContinuousBVDiffContinuousMonotoneWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/ContinuousBVDiffContinuousMonotoneWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/index.html#exists-continuous-monotone-sub-of-bounde).

## No continuous function agrees a.e. with the indicator of $(0,1)$

Let $\chi_{[0,1]}$ be
the characteristic function of $[0,1]$. There is no continuous function
$f : \mathbb{R} \to \mathbb{R}$ such that $f(x) = \chi_{[0,1]}(x)$ for almost every
$x \in \mathbb{R}$ with respect to Lebesgue measure.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Measure and integration; Classical measure theory), problem `ma_proofbench_l1_28`.

Stated but not proved: `MathlibExt.MeasureTheory.IndicatorIccNotAEContinuousWanted.not_exists_continuous_ae_eq_indicator_Icc` is written with `theorem_wanted` in [WantedExt/MeasureTheory/IndicatorIccNotAEContinuousWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/IndicatorIccNotAEContinuousWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/index.html#not-exists-continuous-ae-eq-indicator-ic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Differentiation of real functions](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/real-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/real-functions)
