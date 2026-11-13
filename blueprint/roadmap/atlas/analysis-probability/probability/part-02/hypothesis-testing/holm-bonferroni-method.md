---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MultipleTesting.holmIndex, MathlibExt.Probability.Statistics.MultipleTesting.holmRejections, MathlibExt.Probability.Statistics.MultipleTesting.holmIndex_le, MathlibExt.Probability.Statistics.MultipleTesting.le_numBelow_of_le_holmIndex, MathlibExt.Probability.Statistics.MultipleTesting.le_holmIndex, MathlibExt.Probability.Statistics.MultipleTesting.mem_holmRejections_of_le, MathlibExt.Probability.Statistics.MultipleTesting.card_holmRejections, MathlibExt.Probability.Statistics.MultipleTesting.exists_le_div_card_of_holmRejections
statement: formalized
proof: formalized
---

# Holm–Bonferroni method

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html).

## Holm's step-down count

Holm's step-down count at level `α`: the largest `r ∈ {0, …, m}` such that for every
`k ∈ {1, …, r}` the `k`-th smallest p-value is at most `α / (m - k + 1)`, i.e. at least `k`
p-values are at most `α / (m - k + 1)`. (`r = 0` always qualifies.)

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.holmIndex`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#holm-index).

## Hypotheses rejected by Holm's step-down procedure

The hypotheses rejected by Holm's step-down procedure at level `α`: those whose p-value is
at most `α / (m - r + 1)` with `r = holmIndex α p`; these are the hypotheses with the `r`
smallest p-values.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.holmRejections`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#holm-rejections).

## Holm's step-down count is at most the number of tests

Holm's step-down count is at most `m`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.holmIndex_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#holm-index-le).

## Every step up to Holm's count succeeds

Every step up to Holm's count succeeds: for `1 ≤ k ≤ holmIndex α p`, at least `k`
p-values are at most `α / (m - k + 1)`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.le_numBelow_of_le_holmIndex`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#le-num-below-of-le-holm-index).

## Holm's count is the largest index where every step succeeds

Holm's count is the largest index up to which every step succeeds.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.le_holmIndex`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#le-holm-index).

## Holm's rejection set is closed under smaller p-values

The rejection set is closed under smaller p-values.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.mem_holmRejections_of_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#mem-holm-rejections-of-le).

## Number of hypotheses rejected by Holm's procedure

Holm's procedure at level `α ≥ 0` rejects exactly `holmIndex α p` hypotheses.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.card_holmRejections`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#card-holm-rejections).

## Holm rejection bound for a set of hypotheses

If Holm rejects a hypothesis in `J`, then some `j ∈ J` has p-value at most `α / |J|`:
the first hypothesis of `J` in sorted order sits at a position `k ≤ m - |J| + 1`. This
is the shared Holm rejection bound, used both for Holm's FWER control below and for
identifying Holm's procedure with the closure of the Bonferroni local tests.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.exists_le_div_card_of_holmRejections`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#exists-le-div-card-of-holm-rejections).

## Holm's procedure controls the FWER

If every true-null p-value is valid, the
probability that Holm's step-down procedure at level `α ∈ [0, 1]` rejects at least one true
null is at most `α`. No independence is assumed.

## Sources

- Holm (1979).

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.measure_holm_familywiseError_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/MultipleTesting/Holm.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html#measure-holm-familywise-error-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Holm–Bonferroni method](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/holm-bonferroni-method/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/hypothesis-testing/holm-bonferroni-method)
