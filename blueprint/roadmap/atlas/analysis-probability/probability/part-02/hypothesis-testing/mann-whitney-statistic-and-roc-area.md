---
declaration: section
origin: cited
lean: ProbabilityTheory.rocRate, ProbabilityTheory.rocRateAbove, ProbabilityTheory.empiricalAUC, ProbabilityTheory.mannWhitneyU, ProbabilityTheory.rocRateAbove_eq_rocRate_of_forall_not_mem_Ioo, ProbabilityTheory.rocRateAbove_eq_zero_of_forall_le, ProbabilityTheory.empiricalAUC_eq_mannWhitneyU
statement: formalized
proof: formalized
---

# Mann–Whitney statistic and ROC area

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html).

## Empirical ROC rate at or above a threshold

Empirical rate `#{i | t ≤ z i} / k` of scores at or above the threshold `t` (the true- or
false-positive rate when `z` are the positive or negative scores).

Formalized by `ProbabilityTheory.rocRate`, a definition declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#roc-rate).

## Empirical ROC rate strictly above a threshold

Empirical rate `#{i | t < z i} / k` of scores strictly above `t`: the ROC coordinate at the
next larger distinct score.

Formalized by `ProbabilityTheory.rocRateAbove`, a definition declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#roc-rate-above).

## Empirical area under the ROC curve

Trapezoidal area under the empirical ROC curve of positive scores `x` and negative scores
`y`: the sum over the distinct observed scores `t` of the trapezoid from the point
`(rocRateAbove y t, rocRateAbove x t)` to `(rocRate y t, rocRate x t)`.

Formalized by `ProbabilityTheory.empiricalAUC`, a definition declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#empirical-auc).

## Mann–Whitney U statistic

Mann–Whitney count `U = ∑ᵢ ∑ⱼ (1[y j < x i] + ½ 1[y j = x i])` of (positive, negative)
pairs ranked correctly, with ties counted one half.

Formalized by `ProbabilityTheory.mannWhitneyU`, a definition declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#mann-whitney-u).

## Strict ROC rate equals the rate at the next score

If no score lies strictly between `t < t'`, the strict rate at `t` is the rate at `t'`: the
left end of the trapezoid at `t` is the ROC point of the next larger distinct score.

Formalized by `ProbabilityTheory.rocRateAbove_eq_rocRate_of_forall_not_mem_Ioo`, a theorem declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#roc-rate-above-eq-roc-rate-of-forall-not).

## Strict ROC rate vanishes above the largest score

Above the largest score the strict rate is zero: the first trapezoid starts at `(0, 0)`.

Formalized by `ProbabilityTheory.rocRateAbove_eq_zero_of_forall_le`, a theorem declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#roc-rate-above-eq-zero-of-forall-le).

## Empirical AUC = Mann–Whitney with ties

**Empirical AUC = Mann–Whitney with ties** (Bamber 1975): the trapezoidal area under the
empirical ROC curve equals `U / (m n)`, for nonempty samples.

Formalized by `ProbabilityTheory.empiricalAUC_eq_mannWhitneyU`, a theorem declared in [MathlibExt/Probability/Statistics/MannWhitneyAUC.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MannWhitneyAUC.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html#empirical-auc-eq-mann-whitney-u).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mann–Whitney statistic and ROC area](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/hypothesis-testing/mann-whitney-statistic-and-roc-area)
