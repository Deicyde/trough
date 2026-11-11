---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.MultipleTesting.permutationPValue, MathlibExt.Probability.Statistics.MultipleTesting.card_filter_rankCount_le, MathlibExt.Probability.Statistics.MultipleTesting.isValidPValue_permutationPValue, MathlibExt.Probability.Statistics.MultipleTesting.monteCarloPermutationPValue, MathlibExt.Probability.Statistics.MultipleTesting.isValidPValue_monteCarloPermutationPValue
statement: formalized
proof: formalized
---

# Permutation tests

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html).

## Permutation p-value

The permutation (group-invariance) p-value of the statistic `T` at `ω`: the fraction of
group elements `g` with `T (g • ω) ≥ T ω`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.permutationPValue`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/PermutationPValue.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/PermutationPValue.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html#permutation-pvalue).

## Counting lemma for rank counts

Counting lemma: for any family of reals `t` indexed by `G` and any `k`, at most `k`
elements `h` have rank count `#{g | t h ≤ t g}` at most `k`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.card_filter_rankCount_le`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/PermutationPValue.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/PermutationPValue.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html#card-filter-rank-count-le).

## Validity of permutation p-values

Lehmann and Romano (2005), §15.2; Hemerik and Goeman (2018): if the law `μ` is invariant
under the action of a finite group `G`, the permutation p-value of any measurable statistic is
valid.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.isValidPValue_permutationPValue`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/PermutationPValue.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/PermutationPValue.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html#is-valid-pvalue-permutation-pvalue).

## Monte Carlo permutation p-value

The Monte Carlo permutation p-value `(1 + #{b | T(g_b • ω) ≥ T(ω)}) / (B + 1)` of the
statistic `T` at the data `ω` with the `B` drawn group elements `g`.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.monteCarloPermutationPValue`, a definition declared in [MathlibExt/Probability/Statistics/MultipleTesting/MonteCarloPermutationPValue.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/MonteCarloPermutationPValue.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html#monte-carlo-permutation-pvalue).

## Validity of Monte Carlo permutation p-values

Phipson and Smyth (2010); Hemerik and Goeman (2018): if the null law `μ` is invariant under
a finite group `G` and `g₁, …, g_B` are drawn independently and uniformly from `G`,
independently of the data, then `(1 + #{b | T(g_b • ω) ≥ T(ω)}) / (B + 1)` is a valid p-value
under the joint law.

Formalized by `MathlibExt.Probability.Statistics.MultipleTesting.isValidPValue_monteCarloPermutationPValue`, a theorem declared in [MathlibExt/Probability/Statistics/MultipleTesting/MonteCarloPermutationPValue.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/MultipleTesting/MonteCarloPermutationPValue.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html#is-valid-pvalue-monte-carlo-permutation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation tests](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/permutation-tests/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/permutation-tests)
