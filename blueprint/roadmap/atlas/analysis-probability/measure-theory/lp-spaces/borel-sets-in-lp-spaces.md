---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.LpVanishingHalfLineIntegralBorelWanted.vanishingIntegralSet, MathlibExt.MeasureTheory.LpVanishingHalfLineIntegralBorelWanted.measurableSet_vanishingIntegralSet
statement: formalized
---

# Borel sets in Lp spaces

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/borel-sets-in-lp-spaces/index.html).

## Functions with vanishing integrals over $(0, L)$

For $0 \le p \le \infty$, this is the set
of real-valued $f \in L^p(\mathbb{R})$ (with respect to Lebesgue measure) such that
$\int_{[0, L]} f(x)\,dx \to 0$ as $L \to +\infty$, where the integral of a function that is not
integrable on $[0, L]$ counts as $0$.

Formalized by `MathlibExt.MeasureTheory.LpVanishingHalfLineIntegralBorelWanted.vanishingIntegralSet`, a definition declared in [WantedExt/MeasureTheory/LpVanishingHalfLineIntegralBorelWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpVanishingHalfLineIntegralBorelWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/borel-sets-in-lp-spaces/index.html#vanishing-integral-set).

## $L^p$ functions whose integrals over $(0, L)$ tend to $0$ form a Borel set

Let
$1 \le p \le \infty$. The set of real-valued $f \in L^p(\mathbb{R})$ (with respect to Lebesgue
measure) such that $\int_0^L f(x)\,dx \to 0$ as $L \to +\infty$ is a Borel subset of
$L^p(\mathbb{R})$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Set functions, measures and integrals with values in abstract spaces), problem `ma_proofbench_l2_25`.

Stated but not proved: `MathlibExt.MeasureTheory.LpVanishingHalfLineIntegralBorelWanted.measurableSet_vanishingIntegralSet` is written with `theorem_wanted` in [WantedExt/MeasureTheory/LpVanishingHalfLineIntegralBorelWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/LpVanishingHalfLineIntegralBorelWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/borel-sets-in-lp-spaces/index.html#measurable-set-vanishing-integral-set).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Borel sets in Lp spaces](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lp-spaces/borel-sets-in-lp-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lp-spaces/borel-sets-in-lp-spaces)
