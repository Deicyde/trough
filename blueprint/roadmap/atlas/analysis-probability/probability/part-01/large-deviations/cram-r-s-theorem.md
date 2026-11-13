---
declaration: section
origin: cited
lean: MathlibExt.Probability.CramerUpperBound.empiricalMeanMeasureVec, MathlibExt.Probability.CramerUpperBound.logMGFVec, MathlibExt.Probability.CramerUpperBound.measure_empiricalMean_le_of_threshold, MathlibExt.Probability.CramerUpperBound.cramer_upper_bound, MathlibExt.Probability.CramerUpperBound.cramer_upper_bound_rate, MathlibExt.Probability.CramerRateFunction.extendedLogMGFVec, MathlibExt.Probability.CramerRateFunction.cramerRateFunction, MathlibExt.Probability.CramerRateFunction.logMGFVec_zero
statement: formalized
proof: formalized
---

# Cramér's theorem

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html).

## Law of the empirical mean

**Law of the empirical mean** `Aₙ = (1/n) ∑_{i<n} Xᵢ` for an `ℝᵈ`-valued sample.

Pushforward of `μ` under the map `ω ↦ (1/n) ∑_{i<n} Xᵢ(ω)`. Ported verbatim
from v1.

Formalized by `MathlibExt.Probability.CramerUpperBound.empiricalMeanMeasureVec`, a definition declared in [MathlibExt/Probability/CramerUpperBound.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerUpperBound.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#empirical-mean-measure-vec).

## Real-valued log-MGF expression

**Real-valued log-MGF expression** `Λ(t) = log E[exp ⟪t, X⟫]`.

For a random vector `X : Ω → ℝᵈ`, this returns the logarithm of the moment
generating function evaluated at the dual variable `t ∈ ℝᵈ`, using the Euclidean
inner product. Under a probability measure it represents the cumulant generating
function at directions where the exponential is integrable. For a nonintegrable
exponential, the Bochner integral is `0` and `Real.log 0 = 0`, so this definition
returns `0`. The bounds below explicitly require exponential integrability.
Ported from v1.

Formalized by `MathlibExt.Probability.CramerUpperBound.logMGFVec`, a definition declared in [MathlibExt/Probability/CramerUpperBound.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerUpperBound.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#log-mgfvec).

## Chernoff bound for the empirical mean of real-valued i.i.d. variables

**Chernoff bound for the empirical mean of real-valued i.i.d. variables**,
in event form: if on the event `E` the empirical mean
`(1/n) ∑_{i<n} Xᵢ` satisfies the threshold inequality
`a ≤ t * (empirical mean) - log (mgf of X₁ at t)`, then
`μ(E) ≤ exp(-n * a)`.

Assume a probability measure, measurable independent identically distributed
coordinates, and integrability of `exp (t * X₀)`.

This is the one-dimensional core of the Cramér upper bound. The proof splits
on the sign of `t`: for `t > 0` it applies Mathlib's upper-tail Chernoff bound
to the sum `Sₙ`, and for `t < 0` the lower-tail Chernoff bound; in both cases
the exponential moment of the sum factors as `(mgf of X₁ at t)^n` by
independence and identical distribution.

Formalized by `MathlibExt.Probability.CramerUpperBound.measure_empiricalMean_le_of_threshold`, a theorem declared in [MathlibExt/Probability/CramerUpperBound.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerUpperBound.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#measure-empirical-mean-le-of-threshold).

## Fixed-direction Chernoff bound

For i.i.d. random vectors in `ℝᵈ`,
the law `μₙ` of the empirical mean satisfies `μₙ(F) ≤ exp(-n * a)` whenever
`a` lower-bounds `⟪ξ, ·⟫ - Λ(ξ)` on measurable `F`. Assume a probability measure,
measurable coordinates and integrability of `exp ⟪ξ, X₀⟫` at this direction.

Formalized by `MathlibExt.Probability.CramerUpperBound.cramer_upper_bound`, a theorem declared in [MathlibExt/Probability/CramerUpperBound.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerUpperBound.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-upper-bound).

## Fixed-direction Chernoff bound, rate form

For a fixed `ξ` and
`s = inf_{x ∈ F} (⟪ξ, x⟫ - Λ(ξ))`, the `n`-th root of `μₙ(F)` has limsup at most
`exp(-s)`. Assume measurable i.i.d. coordinates under a probability measure,
measurable `F`, exponential integrability at `ξ`, and a bounded-below rate image
on `F`, with its real-valued `sInf` used for `s`.
Optimizing over admissible `ξ` gives the supremum of these fixed-direction rates;
the Legendre-rate Cramér upper bound requires further arguments.

Formalized by `MathlibExt.Probability.CramerUpperBound.cramer_upper_bound_rate`, a theorem declared in [MathlibExt/Probability/CramerUpperBound.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerUpperBound.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-upper-bound-rate).

## Extended log moment generating function of a random vector

Extended log moment: nonintegrable measurable exponential moments give `⊤`.

Formalized by `MathlibExt.Probability.CramerRateFunction.extendedLogMGFVec`, a definition declared in [MathlibExt/Probability/CramerRateFunction.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#extended-log-mgfvec).

## Cramér rate function

The canonical extended conjugate, converted with top preserved.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction`, a definition declared in [MathlibExt/Probability/CramerRateFunction.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function).

## Log moment generating function vanishes at zero

The canonical real log moment is zero at the zero direction.

Formalized by `MathlibExt.Probability.CramerRateFunction.logMGFVec_zero`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#log-mgfvec-zero).

## Log moment generating function of a constant vector

The canonical real log moment of a constant vector.

Formalized by `MathlibExt.Probability.CramerRateFunction.logMGFVec_const`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#log-mgfvec-const).

## Extended log moment agrees with the real one at integrable directions

Finite directions compose with the existing fixed-direction Chernoff API.

Formalized by `MathlibExt.Probability.CramerRateFunction.extendedLogMGFVec_eq_coe_logMGFVec`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#extended-log-mgfvec-eq-coe-log-mgfvec).

## Extended log moment is infinite at non-integrable directions

Measurability separates infinite moments from nonmeasurable totalized integrals.

Formalized by `MathlibExt.Probability.CramerRateFunction.extendedLogMGFVec_eq_top_of_not_integrable`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#extended-log-mgfvec-eq-top-of-not-integr).

## Extended log moment vanishes at zero

The zero direction has extended log moment zero under probability.

Formalized by `MathlibExt.Probability.CramerRateFunction.extendedLogMGFVec_zero`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#extended-log-mgfvec-zero).

## Extended log moment of a constant vector

Extended log moments of constant vectors retain the exact inner product.

Formalized by `MathlibExt.Probability.CramerRateFunction.extendedLogMGFVec_const`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#extended-log-mgfvec-const).

## Cramér rate function as a supremum

Supporting terms are obtained from the canonical conjugate, not a second transform.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction_eq_iSup`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function-eq-i-sup).

## Extended Fenchel–Young inequality for the Cramér rate function

Extended Fenchel–Young, valid for every measure and every direction.

Formalized by `MathlibExt.Probability.CramerRateFunction.le_cramerRateFunction`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#le-cramer-rate-function).

## Fenchel–Young lower bound at integrable directions

The original real supporting term remains valid at integrable directions.

Formalized by `MathlibExt.Probability.CramerRateFunction.le_cramerRateFunction_of_integrable`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#le-cramer-rate-function-of-integrable).

## Nonnegativity of the Legendre transform of the log moment

Probability makes the canonical conjugate nonnegative via the zero direction.

Formalized by `MathlibExt.Probability.CramerRateFunction.legendreTransform_extendedLogMGFVec_nonneg`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#legendre-transform-extended-log-mgfvec-n).

## Cramér rate function agrees with the extended conjugate

Under probability the conversion preserves the entire nonnegative conjugate.

Formalized by `MathlibExt.Probability.CramerRateFunction.coe_cramerRateFunction`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#coe-cramer-rate-function).

## Lower semicontinuity of the Cramér rate function

Converted canonical conjugates are lower semicontinuous for arbitrary input data.

Formalized by `MathlibExt.Probability.CramerRateFunction.lowerSemicontinuous_cramerRateFunction`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#lower-semicontinuous-cramer-rate-functio).

## Convexity of the Cramér rate function

Convexity is transported from the actual canonical conjugate epigraph.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction_convex`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function-convex).

## Cramér rate function is a convex rate function

The existing LDP convex-rate structure is available without global MGF finiteness.

Formalized by `MathlibExt.Probability.CramerRateFunction.isConvexRateFunction_cramerRateFunction`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#is-convex-rate-function-cramer-rate-func).

## Cramér rate function as a supremum when all moments are integrable

With all moments integrable, the canonical real expression represents every direction.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction_eq_iSup_of_integrable`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function-eq-i-sup-of-integra).

## Cramér rate function as a real supremum under finite moments

Physical finite-domain agreement: bounded real supporting values and integrable moments.
The finiteness premise belongs to this corollary, not the corrected definitions.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction_eq_ofReal_iSup`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function-eq-of-real-i-sup).

## Cramér rate function vanishes at the mean

The original integrable-vector and moment premises imply zero rate at the mean.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction_eq_zero_at_mean`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function-eq-zero-at-mean).

## Cramér rate function of a constant law

Constant laws retain zero at their center and top elsewhere,
including dimension zero.

Formalized by `MathlibExt.Probability.CramerRateFunction.cramerRateFunction_const`, a theorem declared in [MathlibExt/Probability/CramerRateFunction.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CramerRateFunction.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html#cramer-rate-function-const).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cramér's theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/cram-r-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/large-deviations/cram-r-s-theorem)
