---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair, MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.map_comp, MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.map_sub_neg, MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_le_sub, MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_abs_sub, MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_le_logRatio, MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_le_ratio, MathlibExt.Biology.PopulationGenetics.SelectionScan.xpehh
statement: formalized
proof: formalized
---

# Cross-population haplotype homozygosity

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html).

## Selection Scan

## Exchangeable pair of statistics

The pair of statistics `(X, Y)` is exchangeable under `μ`: the joint law is unchanged by
swapping the two coordinates. This is an additional calibration assumption for a two-group
haplotype test, stronger than the ordinary neutral null.
Defined as `IdentDistrib` of the two orderings, so the measurability of the joint laws is
part of the hypothesis rather than restored separately in each theorem.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#is-exchangeable-pair).

## Exchangeability is preserved by a common measurable map

Applying the same measurable function to both statistics preserves exchangeability.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.map_comp`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#map-comp).

## Difference of an exchangeable pair has a symmetric law

The difference of an exchangeable pair has a symmetric law.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.map_sub_neg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#map-sub-neg).

## Equal tails of the difference of an exchangeable pair

Equal tails: the upper tail of `X - Y` at `t` has the same probability as the lower tail
at `-t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_le_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#measure-le-sub).

## Two-sided rejection region splits into equal tails

A two-sided rejection region splits into two tails of equal probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_abs_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#measure-abs-sub).

## Equal tails of the log ratio of an exchangeable pair

For positive statistics, the log ratio — the XP-EHH form — has equal tails.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_le_logRatio`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#measure-le-log-ratio).

## Equal tails of the ratio of an exchangeable pair

The same statement for the ratio itself, the form used for relative EHH: the probability
that the ratio exceeds `c` equals the probability that it falls below `1 / c`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.IsExchangeablePair.measure_le_ratio`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#measure-le-ratio).

## Cross-population extended haplotype homozygosity (XP-EHH)

The cross-population extended haplotype homozygosity score (Sabeti et al. 2007): the log
ratio of the integrated haplotype homozygosities of the same core region in two populations.
Both arguments must be positive for the score to be meaningful. Outside that domain
`Real.log` is totalized by Mathlib, not by the stated junk value: `Real.log 0 = 0` and
`Real.log (-x) = Real.log x`, so for example `xpehh (-2) 1 = log 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.xpehh`, a definition declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#xpehh).

## XP-EHH in star-genealogy sweep models

XP-EHH computed from two star-genealogy sweep models with the same recombination rate is
the log ratio of the two ages, with the opposite sign to `ihs`.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.xpehh_ihh`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#xpehh-ihh).

## Symmetry of the XP-EHH law under exchangeability

Under exchangeability, the XP-EHH score has a symmetric law: the two tails of the
two-sided test carry the same probability.

Formalized by `MathlibExt.Biology.PopulationGenetics.SelectionScan.measure_le_xpehh`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/SelectionScan/CrossPopulationEHH.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html#measure-le-xpehh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cross-population haplotype homozygosity](https://deicyde.github.io/atlas-lean/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/detecting-selection/cross-population-haplotype-homozygosity)
