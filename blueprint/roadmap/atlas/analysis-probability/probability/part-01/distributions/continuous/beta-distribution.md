---
declaration: section
origin: cited
lean: ProbabilityTheory.betaPDFReal_nonneg, ProbabilityTheory.integral_betaPDFReal, ProbabilityTheory.integral_betaMeasure, ProbabilityTheory.beta_add_one_left, ProbabilityTheory.beta_comm, ProbabilityTheory.betaPDFReal_mul_pow, ProbabilityTheory.integral_pow_mul_one_sub_pow_betaMeasure, ProbabilityTheory.integral_id_betaMeasure
statement: formalized
proof: formalized
---

# Beta distribution

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html).

## Nonnegativity of the beta density

The beta density is nonnegative for positive shape parameters.

Formalized by `ProbabilityTheory.betaPDFReal_nonneg`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#beta-pdfreal-nonneg).

## Beta density integrates to one

The beta density integrates to `1` (the Bochner-integral form of
`lintegral_betaPDF_eq_one`).

Formalized by `ProbabilityTheory.integral_betaPDFReal`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#integral-beta-pdfreal).

## Integrals against the beta law

An integral against `betaMeasure α β` is the integral of the function times the beta
density. No integrability hypothesis is needed: both sides are the junk value `0` together.

Formalized by `ProbabilityTheory.integral_betaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#integral-beta-measure).

## Recurrence of the beta function in the first argument

`B(α + 1, β) = B(α, β) · α / (α + β)`.

Formalized by `ProbabilityTheory.beta_add_one_left`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#beta-add-one-left).

## Symmetry of the beta function

The beta function is symmetric.

Formalized by `ProbabilityTheory.beta_comm`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#beta-comm).

## Beta-function identity for densities

Multiplying the `Beta(α, β)` density by
`x ^ k (1 - x) ^ m` gives `B(α + k, β + m) / B(α, β)` times the `Beta(α + k, β + m)` density.

Formalized by `ProbabilityTheory.betaPDFReal_mul_pow`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#beta-pdfreal-mul-pow).

## Mixed moments of the beta law

For `α, β > 0` and natural `k, m`,
`E[X ^ k (1 - X) ^ m] = B(α + k, β + m) / B(α, β)`.

Formalized by `ProbabilityTheory.integral_pow_mul_one_sub_pow_betaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#integral-pow-mul-one-sub-pow-beta-measur).

## Mean of the beta law

For `α, β > 0`, `E[X] = α / (α + β)`.

Formalized by `ProbabilityTheory.integral_id_betaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#integral-id-beta-measure).

## Second moment of the beta law

For `α, β > 0`,
`E[X ^ 2] = α (α + 1) / ((α + β) (α + β + 1))`.

Formalized by `ProbabilityTheory.integral_sq_betaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#integral-sq-beta-measure).

## Mean of $X(1 - X)$ under a beta law

For `α, β > 0`, `E[X (1 - X)] = α β / ((α + β) (α + β + 1))` (half the expected
heterozygosity of a `Beta(α, β)` allele frequency).

Formalized by `ProbabilityTheory.integral_mul_one_sub_betaMeasure`, a theorem declared in [MathlibExt/Probability/Distributions/BetaMoments.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BetaMoments.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html#integral-mul-one-sub-beta-measure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Beta distribution](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/beta-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/continuous/beta-distribution)
