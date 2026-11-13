---
declaration: section
origin: cited
lean: ProbabilityTheory.poissonCDF, ProbabilityTheory.poissonMeasure_real_Iic, ProbabilityTheory.poissonCDF_zero_left, ProbabilityTheory.poissonCDF_zero_right, ProbabilityTheory.poissonCDF_pos, ProbabilityTheory.hasDerivAt_poissonCDF, ProbabilityTheory.continuous_poissonCDF, ProbabilityTheory.gammaMeasure_real_Ioi_poissonCDF
statement: formalized
proof: formalized
---

# Poisson–Gamma duality

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html).

## Poisson distribution function as a function of the mean

The Poisson distribution function `F_k(x) = ∑_{j ≤ k} e^{-x} x^j / (j!)` as a function of
the mean `x` (defined for every real `x`; it is a probability only for `0 ≤ x`).

Formalized by `ProbabilityTheory.poissonCDF`, a definition declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf).

## Poisson distribution function agrees with the Poisson law

`poissonCDF r k` is the distribution function of Mathlib's `poissonMeasure r` at `k`.

Formalized by `ProbabilityTheory.poissonMeasure_real_Iic`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-measure-real-iic).

## Poisson distribution function at mean zero

At mean `0` the Poisson law is the point mass at `0`: `F_k(0) = 1`.

Formalized by `ProbabilityTheory.poissonCDF_zero_left`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-zero-left).

## Poisson distribution function at count zero

`F_0(x) = e^{-x}`.

Formalized by `ProbabilityTheory.poissonCDF_zero_right`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-zero-right).

## Positivity of the Poisson distribution function

The distribution function is positive at every nonnegative real mean.

Formalized by `ProbabilityTheory.poissonCDF_pos`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-pos).

## Derivative of the Poisson distribution function in the mean

The derivative in the mean telescopes: `∂_x F_k(x) = -e^{-x} x^k / (k!)`.

Formalized by `ProbabilityTheory.hasDerivAt_poissonCDF`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#has-deriv-at-poisson-cdf).

## Continuity of the Poisson distribution function in the mean

The distribution function is continuous in the mean.

Formalized by `ProbabilityTheory.continuous_poissonCDF`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#continuous-poisson-cdf).

## Poisson–Gamma duality

The Gamma law of shape `k + 1` and rate `r` (Mathlib's
`gammaMeasure`) has upper tail `P(Gamma(k + 1, r) > x) = F_k(r x)`. This is the Erlang tail
`gammaMeasure_real_Ioi_natCast_add_one` in `GammaMoments`, rewritten with the definition of
`poissonCDF`.

Formalized by `ProbabilityTheory.gammaMeasure_real_Ioi_poissonCDF`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#gamma-measure-real-ioi-poisson-cdf).

## Poisson distribution function is strictly decreasing in the mean

The distribution function is strictly decreasing in the mean on `[0, ∞)`.

Formalized by `ProbabilityTheory.poissonCDF_strictAntiOn`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-strict-anti-on).

## Poisson distribution function is strictly increasing in the count

The distribution function is strictly increasing in `k` at every positive mean.

Formalized by `ProbabilityTheory.poissonCDF_lt_poissonCDF_succ`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-lt-poisson-cdf-succ).

## Poisson distribution function is monotone in the count

The distribution function is monotone in `k` at every nonnegative mean.

Formalized by `ProbabilityTheory.poissonCDF_mono`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-mono).

## Poisson distribution function vanishes as the mean grows

For fixed `k`, `F_k(x) → 0` as the mean `x → ∞`.

Formalized by `ProbabilityTheory.tendsto_poissonCDF_atTop`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#tendsto-poisson-cdf-at-top).

## Poisson distribution function tends to one as the count grows

For a fixed nonnegative mean, `F_k(x) → 1` as `k → ∞`.

Formalized by `ProbabilityTheory.tendsto_poissonCDF_nat`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#tendsto-poisson-cdf-nat).

## Garwood's exact upper confidence bound

**Garwood's exact upper confidence bound** for a Poisson mean after observing `k`, at
level `α`: `u_α(k) = sup {x ≥ 0 | α ≤ F_k(x)}`. For `0 < α < 1` it is the root of
`F_k(u) = α` (`poissonCDF_garwoodUpper`).

Formalized by `ProbabilityTheory.garwoodUpper`, a definition declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#garwood-upper).

## Positivity of the Garwood upper bound

The bound is positive for `0 < α < 1`.

Formalized by `ProbabilityTheory.garwoodUpper_pos`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#garwood-upper-pos).

## Garwood upper bound solves the distribution function equation

The bound solves `F_k(u_α(k)) = α`.

Formalized by `ProbabilityTheory.poissonCDF_garwoodUpper`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-cdf-garwood-upper).

## Means below the Garwood upper bound are exactly the non-rejected ones

A nonnegative mean lies below the bound iff it is not rejected: `x ≤ u_α(k) ↔ α ≤ F_k(x)`.

Formalized by `ProbabilityTheory.le_garwoodUpper_iff`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#le-garwood-upper-iff).

## Garwood upper bound is strictly increasing in the count

The bound is strictly increasing in the observed count.

Formalized by `ProbabilityTheory.garwoodUpper_strictMono`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#garwood-upper-strict-mono).

## Garwood upper bound after observing zero

After observing `0` the bound is `u_α(0) = log (1 / α)` (`e^{-u} = α`).

Formalized by `ProbabilityTheory.garwoodUpper_zero`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#garwood-upper-zero).

## Super-uniformity of the distribution-function transform

For `K ~ Poisson(r)` and
every `α ≥ 0`, `P(F_r(K) ≤ α) ≤ α`. (For `α < 0` the event is empty.)

Formalized by `ProbabilityTheory.poissonMeasure_real_poissonCDF_le`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#poisson-measure-real-poisson-cdf-le).

## Exact coverage of Garwood's bound

For every mean `r ≥ 0` and `0 < α < 1`,
`P_r(r ≤ u_α(K)) ≥ 1 - α` when `K ~ Poisson(r)`.

Formalized by `ProbabilityTheory.garwoodUpper_coverage`, a theorem declared in [MathlibExt/Probability/Distributions/PoissonGamma.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/PoissonGamma.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html#garwood-upper-coverage).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poisson–Gamma duality](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/continuous/poisson-gamma-duality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/distributions/continuous/poisson-gamma-duality)
