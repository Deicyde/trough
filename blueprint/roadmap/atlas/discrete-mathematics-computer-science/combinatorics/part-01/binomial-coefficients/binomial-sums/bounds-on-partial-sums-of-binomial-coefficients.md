---
declaration: section
origin: cited
lean: Real.pow_mul_sum_choose_le, Real.pow_mul_sum_choose_le_exp, Real.sum_choose_le_pow
statement: formalized
proof: formalized
---

# Bounds on partial sums of binomial coefficients

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/bounds-on-partial-sums-of-binomial-coefficients/index.html).

## Weighted partial binomial sum bounded by the full expansion

A weighted partial binomial sum is bounded by the full binomial expansion.

Formalized by `Real.pow_mul_sum_choose_le`, a theorem declared in [MathlibExt/Combinatorics/BinomialPartialSum.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/BinomialPartialSum.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/bounds-on-partial-sums-of-binomial-coefficients/index.html#pow-mul-sum-choose-le).

## Exponential bound on a weighted partial binomial sum

Exponential bound on the weighted partial binomial sum, including the zero-weight boundary.

Formalized by `Real.pow_mul_sum_choose_le_exp`, a theorem declared in [MathlibExt/Combinatorics/BinomialPartialSum.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/BinomialPartialSum.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/bounds-on-partial-sums-of-binomial-coefficients/index.html#pow-mul-sum-choose-le-exp).

## Number of subsets of size at most $r$ is at most $(3D/r)^r$

For `1 ≤ r ≤ D`, the number of subsets of size at most `r` is at most `(3 * D / r) ^ r`.

Formalized by `Real.sum_choose_le_pow`, a theorem declared in [MathlibExt/Combinatorics/BinomialPartialSum.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/BinomialPartialSum.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/bounds-on-partial-sums-of-binomial-coefficients/index.html#sum-choose-le-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds on partial sums of binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/bounds-on-partial-sums-of-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/bounds-on-partial-sums-of-binomial-coefficients)
