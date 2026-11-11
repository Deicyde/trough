---
declaration: section
origin: cited
lean: ProbabilityTheory.integral_mul_sub_one_map_cast_binomial, ProbabilityTheory.integral_sq_map_cast_binomial, ProbabilityTheory.variance_id_map_cast_binomial, ProbabilityTheory.integral_mul_sub_one_of_hasLaw_binomial, ProbabilityTheory.integral_sq_of_hasLaw_binomial, ProbabilityTheory.variance_of_hasLaw_binomial
statement: formalized
proof: formalized
---

# Binomial distribution

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html).

## Second factorial moment of the binomial law

`E[X (X - 1)] = n (n - 1) p²`.

Formalized by `ProbabilityTheory.integral_mul_sub_one_map_cast_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialMoments.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/BinomialMoments.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html#integral-mul-sub-one-map-cast-binomial).

## Second moment of the binomial law

`E[X²] = n p (1 - p) + (n p)²`.

Formalized by `ProbabilityTheory.integral_sq_map_cast_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialMoments.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/BinomialMoments.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html#integral-sq-map-cast-binomial).

## Variance of the binomial law

`Var X = n p (1 - p)`.

Formalized by `ProbabilityTheory.variance_id_map_cast_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialMoments.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/BinomialMoments.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html#variance-id-map-cast-binomial).

## Second factorial moment of a binomial random variable

If `X` has law `Bin(ℝ, n, p)`
then `E[X (X - 1)] = n (n - 1) p²`.

Formalized by `ProbabilityTheory.integral_mul_sub_one_of_hasLaw_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialMoments.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/BinomialMoments.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html#integral-mul-sub-one-of-has-law-binomial).

## Second moment of a binomial random variable

If `X` has law `Bin(ℝ, n, p)` then
`E[X²] = n p (1 - p) + (n p)²`.

Formalized by `ProbabilityTheory.integral_sq_of_hasLaw_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialMoments.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/BinomialMoments.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html#integral-sq-of-has-law-binomial).

## Variance of a binomial random variable

If `X` has law `Bin(ℝ, n, p)` then
`Var X = n p (1 - p)`.

Formalized by `ProbabilityTheory.variance_of_hasLaw_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialMoments.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Distributions/BinomialMoments.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html#variance-of-has-law-binomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/binomial-distribution/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/binomial-distribution)
