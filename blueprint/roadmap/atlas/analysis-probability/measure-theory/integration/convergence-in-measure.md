---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.L0MetricTendstoInMeasureWanted.L0UnitInterval, MathlibExt.MeasureTheory.L0MetricTendstoInMeasureWanted.L0PseudoMetric, MathlibExt.MeasureTheory.L0MetricTendstoInMeasureWanted.tendsto_L0PseudoMetric_zero_iff_tendstoInMeasure
statement: formalized
---

# Convergence in measure

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convergence-in-measure/index.html).

## Measurable functions representing $L^0((0,1))$

The type of Borel measurable functions
$f : \mathbb{R} \to \mathbb{R}$, used as representatives of the elements of $L^0([0,1])$.

The pseudometric and the convergence in measure built on them depend only on the restriction
of $f$ to $[0,1]$ up to a null set.

Formalized by `MathlibExt.MeasureTheory.L0MetricTendstoInMeasureWanted.L0UnitInterval`, an abbreviation declared in [WantedExt/MeasureTheory/L0MetricTendstoInMeasureWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/L0MetricTendstoInMeasureWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convergence-in-measure/index.html#l0-unit-interval).

## The $L^0$ pseudometric on $(0,1)$

For Borel measurable functions
$f, g : \mathbb{R} \to \mathbb{R}$,

$$
d(f,g) = \int_{[0,1]} \frac{|f(x) - g(x)|}{1 + |f(x) - g(x)|}\,dx,
$$

the integral being with respect to Lebesgue measure on $[0,1]$.

This is a pseudometric: functions that agree almost everywhere on $[0,1]$ are at distance $0$,
and on the almost-everywhere classes it is the usual metric of $L^0([0,1])$.

Formalized by `MathlibExt.MeasureTheory.L0MetricTendstoInMeasureWanted.L0PseudoMetric`, a definition declared in [WantedExt/MeasureTheory/L0MetricTendstoInMeasureWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/L0MetricTendstoInMeasureWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convergence-in-measure/index.html#l0-pseudo-metric).

## Convergence in the $L^0$ pseudometric is convergence in measure

Let $f$ and
$f_0, f_1, f_2, \ldots$ be Borel measurable functions $\mathbb{R} \to \mathbb{R}$, and let $d$ be
the pseudometric

$$
d(g,h) = \int_{[0,1]} \frac{|g(x) - h(x)|}{1 + |g(x) - h(x)|}\,dx
$$

on such functions, the integral being with respect to Lebesgue measure. Then
$d(f_n, f) \to 0$ as $n \to \infty$ if and only if $f_n \to f$ in measure with respect to
Lebesgue measure on $[0,1]$: for every $\varepsilon > 0$, the Lebesgue measure of
$\{x \in [0,1] : |f_n(x) - f(x)| \ge \varepsilon\}$ tends to $0$ as $n \to \infty$.

The source states this for $L^0([0,1])$, on which $d$ is a metric; here it is stated for
representatives, on which $d$ is only a pseudometric. Both sides depend only on the
almost-everywhere classes of the functions on $[0,1]$, so the two statements say the same thing.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functional analysis; Linear function spaces and their duals), problem `ma_proofbench_l2_07`, with the change above.

Stated but not proved: `MathlibExt.MeasureTheory.L0MetricTendstoInMeasureWanted.tendsto_L0PseudoMetric_zero_iff_tendstoInMeasure` is written with `theorem_wanted` in [WantedExt/MeasureTheory/L0MetricTendstoInMeasureWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/L0MetricTendstoInMeasureWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convergence-in-measure/index.html#tendsto-l0-pseudo-metric-zero-iff-tendst).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convergence in measure](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/convergence-in-measure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/integration/convergence-in-measure)
