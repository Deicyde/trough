---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.ExactTests.leveneProb, MathlibExt.Probability.Statistics.ExactTests.hetCount, MathlibExt.Probability.Statistics.ExactTests.card_hetCount_div_choose, MathlibExt.Probability.Statistics.ExactTests.sum_leveneProb
statement: formalized
proof: formalized
---

# Exact test for Hardy–Weinberg equilibrium

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium/index.html).

## Levene's exact Hardy–Weinberg probability

Levene's conditional probability of `h` heterozygotes among `N` diploid individuals given
`nA` copies of allele `A` (and `nB = 2N - nA` of `B`) under Hardy–Weinberg equilibrium:
`N! nA! nB! 2^h / (nAA! h! nBB! (2N)!)` with `nAA = (nA - h) / 2`, `nBB = (nB - h) / 2`, when
`h ≤ nA`, `h ≤ nB` and `nA - h` is even, and `0` otherwise. The parameter domain is
`nA ≤ 2N`; for `nA > 2N` the value is `0`.

Formalized by `MathlibExt.Probability.Statistics.ExactTests.leveneProb`, a definition declared in [MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium/index.html#levene-prob).

## Number of heterozygous individuals

The number of heterozygous individuals when the `A` gametes occupy the slots `s`:
individuals `j` carrying exactly one of the slots `(j, 0)`, `(j, 1)`.

Formalized by `MathlibExt.Probability.Statistics.ExactTests.hetCount`, a definition declared in [MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium/index.html#het-count).

## Levene's formula is the conditional law under random union of gametes

Among the
`C(2N, nA)` equally likely placements of the `nA` copies of `A` in the `2N` gamete slots, the
fraction with exactly `h` heterozygous individuals is `leveneProb N nA h`.

No hypothesis `nA ≤ 2N` is needed: for `nA > 2N` there is no placement and `C(2N, nA) = 0`, so
the left side is `0 / 0 = 0`, matching `leveneProb N nA h = 0`; the statement is meaningful for
`nA ≤ 2N`. The uniform law on placements is taken as the model; deriving it from independent
gametes conditioned on `nA` is not part of this file.

## Sources

- Levene (1949); Wigginton, Cutler and Abecasis (2005).

Formalized by `MathlibExt.Probability.Statistics.ExactTests.card_hetCount_div_choose`, a theorem declared in [MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium/index.html#card-het-count-div-choose).

## Normalization of Levene's distribution

For `nA ≤ 2N` the probabilities
`leveneProb N nA h` over the admissible heterozygote counts `h` sum to one.

## Sources

- Levene (1949); Wigginton, Cutler and Abecasis (2005).

Formalized by `MathlibExt.Probability.Statistics.ExactTests.sum_leveneProb`, a theorem declared in [MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/ExactTests/HardyWeinbergExact.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium/index.html#sum-levene-prob).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exact test for Hardy–Weinberg equilibrium](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/exact-test-for-hardy-weinberg-equilibrium)
