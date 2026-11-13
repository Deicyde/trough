---
declaration: section
origin: cited
lean: ProbabilityTheory.multinomialReal, ProbabilityTheory.multinomialReal_nonneg, ProbabilityTheory.multinomialReal_of_sum_ne, ProbabilityTheory.multinomialReal_eq_factorial_div, ProbabilityTheory.multinomialReal_of_notMem, ProbabilityTheory.sum_multinomialReal_eq_pow, ProbabilityTheory.sum_multinomialReal, ProbabilityTheory.multinomial
statement: formalized
proof: formalized
---

# Multinomial distribution

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html).

## Multinomial mass function

The multinomial mass function: the probability `N! / ∏ᵢ xᵢ! · ∏ᵢ pᵢ ^ xᵢ` that `N`
independent throws, landing in cell `i` with probability `pᵢ`, produce the cell counts `x`; it is
`0` unless `∑ᵢ xᵢ = N`. The formula is a polynomial in `p` and is defined for every real vector
`p`; it is a probability mass function when `p` is a probability vector
(`0 ≤ pᵢ`, `∑ᵢ pᵢ = 1`), which the normalization theorems assume. The converse does not hold
in general: for `N = 0` it is the point mass at the zero vector for every `p`, even vectors
that are not probability vectors.

Formalized by `ProbabilityTheory.multinomialReal`, a definition declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial-real).

## Nonnegativity of the multinomial mass function

The multinomial mass function is nonnegative for a nonnegative vector `p`.

Formalized by `ProbabilityTheory.multinomialReal_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial-real-nonneg).

## Multinomial mass vanishes off the simplex

The multinomial mass function vanishes off the simplex `∑ᵢ xᵢ = N`.

Formalized by `ProbabilityTheory.multinomialReal_of_sum_ne`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial-real-of-sum-ne).

## Multinomial mass formula on the simplex

On the simplex the multinomial mass is `N! / ∏ᵢ xᵢ! · ∏ᵢ pᵢ ^ xᵢ`.

Formalized by `ProbabilityTheory.multinomialReal_eq_factorial_div`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial-real-eq-factorial-div).

## Support of the multinomial mass lies in the antidiagonal

The multinomial mass function vanishes outside the finite set `piAntidiag univ N` of
count vectors with total `N`: the support is contained in the antidiagonal. Equality of
the support with the antidiagonal needs all `p i > 0` (e.g. for `p = (1, 0)`, `N = 1` the
vector `(0, 1)` is in the antidiagonal but has mass `0`).

Formalized by `ProbabilityTheory.multinomialReal_of_notMem`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial-real-of-not-mem).

## Multinomial theorem

`∑ₓ P(x) = (∑ᵢ pᵢ) ^ N` for every real vector `p`.

Formalized by `ProbabilityTheory.sum_multinomialReal_eq_pow`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-multinomial-real-eq-pow).

## Normalization

For `∑ᵢ pᵢ = 1` the multinomial masses sum to one.

Formalized by `ProbabilityTheory.sum_multinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-multinomial-real).

## Multinomial distribution as a probability mass function

The multinomial law of `N` throws with cell probabilities `p` (a probability vector), as a
probability mass function on count vectors `ι → ℕ`.

Formalized by `ProbabilityTheory.multinomial`, a definition declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial).

## Mass of the multinomial distribution at a count vector

The mass of the multinomial PMF at `x` is `multinomialReal N p x`.

Formalized by `ProbabilityTheory.multinomial_apply`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#multinomial-apply).

## Mean, polynomial form

`∑ₓ xᵢ P(x) = N pᵢ (∑ⱼ pⱼ) ^ (N - 1)` for every real vector `p`.

Formalized by `ProbabilityTheory.sum_mul_multinomialReal_eq`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-mul-multinomial-real-eq).

## Second factorial moment, polynomial form

For `i ≠ j`,
`∑ₓ xᵢ xⱼ P(x) = N (N - 1) pᵢ pⱼ (∑ₗ pₗ) ^ (N - 2)` for every real vector `p`.

Formalized by `ProbabilityTheory.sum_mul_mul_multinomialReal_of_ne_eq`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-mul-mul-multinomial-real-of-ne-eq).

## Second factorial moment, polynomial form

`∑ₓ xᵢ (xᵢ - 1) P(x) = N (N - 1) pᵢ² (∑ₗ pₗ) ^ (N - 2)` for every real vector `p`.

Formalized by `ProbabilityTheory.sum_mul_sub_one_multinomialReal_eq`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-mul-sub-one-multinomial-real-eq).

## Mean

For a probability vector (`0 ≤ pᵢ`, `∑ⱼ pⱼ = 1`), `E Xᵢ = N pᵢ`. The
underlying `sum_mul_multinomialReal_eq` is a polynomial identity holding for every real `p`.

Formalized by `ProbabilityTheory.sum_mul_multinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-mul-multinomial-real).

## Mixed second moment

For a probability vector and `i ≠ j`, `E[Xᵢ Xⱼ] = N (N - 1) pᵢ pⱼ`.

Formalized by `ProbabilityTheory.sum_mul_mul_multinomialReal_of_ne`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-mul-mul-multinomial-real-of-ne).

## Second factorial moment

For a probability vector, `E[Xᵢ (Xᵢ - 1)] = N (N - 1) pᵢ²`.

Formalized by `ProbabilityTheory.sum_mul_sub_one_multinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-mul-sub-one-multinomial-real).

## Covariance

For a probability vector (`0 ≤ pᵢ`, `∑ₗ pₗ = 1`),
`Cov(Xᵢ, Xⱼ) = ∑ₓ (xᵢ - N pᵢ) (xⱼ - N pⱼ) P(x) = N (δᵢⱼ pᵢ - pᵢ pⱼ)`; in particular
`Var Xᵢ = N pᵢ (1 - pᵢ)` and `Cov(Xᵢ, Xⱼ) = -N pᵢ pⱼ` for `i ≠ j`.

Formalized by `ProbabilityTheory.sum_covariance_multinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#sum-covariance-multinomial-real).

## Poisson conditioning

Let `Xᵢ ~ Po(λᵢ)`, `i ∈ ι`, be independent Poisson counts with
`∑ᵢ λᵢ > 0`. Given their total `∑ᵢ Xᵢ = N`, the count vector is multinomial with
`N` throws and cell probabilities `λᵢ / ∑ⱼ λⱼ`:
`P(X = x | ∑ᵢ Xᵢ = N) = multinomialReal N (λ / ∑ λ) x`.

Formalized by `ProbabilityTheory.cond_measureReal_eq_multinomialReal`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#cond-measure-real-eq-multinomial-real).

## Poisson conditioning, two cells

For independent `X ~ Po(a)` and `Y ~ Po(b)` with
`a + b > 0`, the law of `X` given `X + Y = N` is binomial `Bin(N, a / (a + b))`.

Formalized by `ProbabilityTheory.cond_measureReal_eq_binomial`, a theorem declared in [MathlibExt/Probability/Distributions/Multinomial.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/Multinomial.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html#cond-measure-real-eq-binomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multinomial distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/discrete/multinomial-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/discrete/multinomial-distribution)
