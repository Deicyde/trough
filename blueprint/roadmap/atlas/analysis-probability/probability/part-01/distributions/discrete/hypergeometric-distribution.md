---
declaration: section
origin: cited
lean: ProbabilityTheory.hypergeometricReal, ProbabilityTheory.hypergeometricReal_nonneg, ProbabilityTheory.hypergeometricReal_of_lt, ProbabilityTheory.hypergeometricReal_of_lt', ProbabilityTheory.sum_hypergeometricReal, ProbabilityTheory.sum_mul_hypergeometricReal, ProbabilityTheory.hypergeometric, ProbabilityTheory.hypergeometric_apply
statement: formalized
proof: formalized
---

# Hypergeometric distribution

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html).

## Hypergeometric mass function

The hypergeometric mass function: the probability `C(K, k) C(N - K, n - k) / C(N, n)` of
drawing exactly `k` marked items in `n` draws without replacement from `N` items of which `K`
are marked; it is `0` for `k > n`. The parameter domain is `K ≤ N`, `n ≤ N`; outside it the
value is not a probability (`N - K` truncates, and `C(N, n) = 0` makes it `0` for `n > N`).

Formalized by `ProbabilityTheory.hypergeometricReal`, a definition declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#hypergeometric-real).

## Nonnegativity of the hypergeometric mass function

The hypergeometric mass function is nonnegative.

Formalized by `ProbabilityTheory.hypergeometricReal_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#hypergeometric-real-nonneg).

## Hypergeometric mass vanishes above the number of draws

The hypergeometric mass function vanishes above the number of draws.

Formalized by `ProbabilityTheory.hypergeometricReal_of_lt`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#hypergeometric-real-of-lt).

## Hypergeometric mass vanishes above the number of marked items

The hypergeometric mass function vanishes above the number of marked items.

Formalized by `ProbabilityTheory.hypergeometricReal_of_lt'`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#hypergeometric-real-of-lt-2).

## Normalization

For `K ≤ N` and `n ≤ N` the hypergeometric probabilities sum to one;
this is Vandermonde's identity `∑ₖ C(K, k) C(N - K, n - k) = C(N, n)`.

Formalized by `ProbabilityTheory.sum_hypergeometricReal`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#sum-hypergeometric-real).

## Mean

For `0 < N`, `K ≤ N` and `n ≤ N` the hypergeometric law has mean `n K / N`.

Formalized by `ProbabilityTheory.sum_mul_hypergeometricReal`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#sum-mul-hypergeometric-real).

## Hypergeometric distribution

The hypergeometric law on `ℕ` with population size `N`, `K ≤ N` marked items, and
`n ≤ N` draws without replacement.

Formalized by `ProbabilityTheory.hypergeometric`, a definition declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#hypergeometric).

## Point masses of the hypergeometric distribution

The mass of `k` under `hypergeometric N K n` is `hypergeometricReal N K n k`.

Formalized by `ProbabilityTheory.hypergeometric_apply`, a theorem declared in [MathlibExt/Probability/Distributions/Hypergeometric.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Hypergeometric.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html#hypergeometric-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypergeometric distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/hypergeometric-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/discrete/hypergeometric-distribution)
