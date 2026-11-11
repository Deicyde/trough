---
declaration: section
origin: cited
lean: ProbabilityTheory.hypergeometricReal, ProbabilityTheory.hypergeometricReal_nonneg, ProbabilityTheory.hypergeometricReal_of_lt, ProbabilityTheory.hypergeometricReal_of_lt', ProbabilityTheory.sum_hypergeometricReal, ProbabilityTheory.sum_mul_hypergeometricReal, ProbabilityTheory.hypergeometric, ProbabilityTheory.hypergeometric_apply
statement: formalized
proof: formalized
---

# Hypergeometric distribution

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html).

## Hypergeometric mass function

The hypergeometric mass function: the probability `C(K, k) C(N - K, n - k) / C(N, n)` of
drawing exactly `k` marked items in `n` draws without replacement from `N` items of which `K`
are marked; it is `0` for `k > n`. The parameter domain is `K ≤ N`, `n ≤ N`; outside it the
value is not a probability (`N - K` truncates, and `C(N, n) = 0` makes it `0` for `n > N`).

Formalized by `ProbabilityTheory.hypergeometricReal`, a definition declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#hypergeometric-real).

## Nonnegativity of the hypergeometric mass function

The hypergeometric mass function is nonnegative.

Formalized by `ProbabilityTheory.hypergeometricReal_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#hypergeometric-real-nonneg).

## Hypergeometric mass vanishes above the number of draws

The hypergeometric mass function vanishes above the number of draws.

Formalized by `ProbabilityTheory.hypergeometricReal_of_lt`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#hypergeometric-real-of-lt).

## Hypergeometric mass vanishes above the number of marked items

The hypergeometric mass function vanishes above the number of marked items.

Formalized by `ProbabilityTheory.hypergeometricReal_of_lt'`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#hypergeometric-real-of-lt-2).

## Normalization

For `K ≤ N` and `n ≤ N` the hypergeometric probabilities sum to one;
this is Vandermonde's identity `∑ₖ C(K, k) C(N - K, n - k) = C(N, n)`.

Formalized by `ProbabilityTheory.sum_hypergeometricReal`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#sum-hypergeometric-real).

## Mean

For `0 < N`, `K ≤ N` and `n ≤ N` the hypergeometric law has mean `n K / N`.

Formalized by `ProbabilityTheory.sum_mul_hypergeometricReal`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#sum-mul-hypergeometric-real).

## Hypergeometric distribution

The hypergeometric law on `ℕ` with population size `N`, `K ≤ N` marked items, and
`n ≤ N` draws without replacement.

Formalized by `ProbabilityTheory.hypergeometric`, a definition declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#hypergeometric).

## Point masses of the hypergeometric distribution

The mass of `k` under `hypergeometric N K n` is `hypergeometricReal N K n k`.

Formalized by `ProbabilityTheory.hypergeometric_apply`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/Hypergeometric.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html#hypergeometric-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypergeometric distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/hypergeometric-distribution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/hypergeometric-distribution)
