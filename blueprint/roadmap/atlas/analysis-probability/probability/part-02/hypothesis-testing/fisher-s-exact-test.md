---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.ExactTests.measureReal_add_eq_binomial, MathlibExt.Probability.Statistics.ExactTests.cond_measureReal_eq_hypergeometricReal
statement: formalized
proof: formalized
---

# Fisher's exact test

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/fisher-s-exact-test/index.html).

## Sum of independent binomials

If `X ~ Bin(n₁, p)` and `Y ~ Bin(n₂, p)` are independent,
then `X + Y ~ Bin(n₁ + n₂, p)`: `P(X + Y = t) = C(n₁ + n₂, t) p^t (1 - p)^(n₁ + n₂ - t)`.

Formalized by `MathlibExt.Probability.Statistics.ExactTests.measureReal_add_eq_binomial`, a theorem declared in [MathlibExt/Probability/Statistics/ExactTests/FisherExact.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/ExactTests/FisherExact.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/fisher-s-exact-test/index.html#measure-real-add-eq-binomial).

## Fisher's exact conditional law

Let `X ~ Bin(n₁, p)` and `Y ~ Bin(n₂, p)` be independent
with a common `p ∈ (0, 1)`. Given the margin `X + Y = t` with `t ≤ n₁ + n₂`, the cell `X` is
hypergeometric: `P(X = k | X + Y = t) = C(n₁, k) C(n₂, t - k) / C(n₁ + n₂, t)`, whatever `p`.

## Sources

- Fisher (1934, §21.02; 1935); Lehmann–Romano (2005), §4.5.

Formalized by `MathlibExt.Probability.Statistics.ExactTests.cond_measureReal_eq_hypergeometricReal`, a theorem declared in [MathlibExt/Probability/Statistics/ExactTests/FisherExact.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/ExactTests/FisherExact.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/fisher-s-exact-test/index.html#cond-measure-real-eq-hypergeometric-real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fisher's exact test](https://deicyde.github.io/atlas-lean/roadmap/Probability/hypothesis-testing/fisher-s-exact-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/hypothesis-testing/fisher-s-exact-test)
