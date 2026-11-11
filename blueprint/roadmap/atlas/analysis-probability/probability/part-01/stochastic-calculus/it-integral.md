---
declaration: section
origin: cited
lean: ProbabilityTheory.ElementaryIntegrand, ProbabilityTheory.IsPreBrownianReal.integral_sub_sq, ProbabilityTheory.ElementaryIntegrand.toProcess, ProbabilityTheory.ElementaryIntegrand.itoIntegral, ProbabilityTheory.ElementaryIntegrand.single, ProbabilityTheory.ElementaryIntegrand.toProcess_single, ProbabilityTheory.ElementaryIntegrand.itoIntegral_single, ProbabilityTheory.ElementaryIntegrand.itoIntegral_zero
statement: formalized
proof: formalized
---

# Itô integral

68 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html).

## Elementary integrand

An **elementary integrand** for a filtration `F` indexed by `ℝ≥0`: partition times
`time 0 ≤ ⋯ ≤ time n` and coefficients `coeff i`, bounded by `bound` and measurable with respect
to `F (time i)`, representing the process `∑ i, coeff i 1_{(time i, time (i + 1)]}`. Equal
consecutive times are allowed (the corresponding interval is empty).

Formalized by `ProbabilityTheory.ElementaryIntegrand`, a structure declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#elementary-integrand).

## Second moment of a Brownian increment

The second moment of a Brownian increment: `E[(B v - B r)²] = v - r` for `r ≤ v`.

Formalized by `ProbabilityTheory.IsPreBrownianReal.integral_sub_sq`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integral-sub-sq).

## Elementary integrand as a process

The elementary integrand as a process: `u ↦ ∑ i, coeff i 1_{(time i, time (i + 1)]}(u)`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.toProcess`, a definition declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#to-process).

## Itô integral of an elementary integrand

The **Itô integral** of an elementary integrand against a process `B`:
`t ↦ ∑ i, coeff i (B (time (i + 1) ∧ t) - B (time i ∧ t))`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.itoIntegral`, a definition declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral).

## Single-step elementary integrand

The elementary integrand `ξ 1_{(a, b]}` for `a ≤ b` and an `F a`-measurable `ξ` bounded by
`C`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.single`, a definition declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#single).

## Process of a single-step elementary integrand

The process of `single a b hab ξ hξ C hξC` is `u ↦ ξ 1_{(a, b]}(u)`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.toProcess_single`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#to-process-single).

## Elementary integrands

The Itô integral of `ξ 1_{(a, b]}` is
`ξ (B (b ∧ t) - B (a ∧ t))` (Karatzas–Shreve 1991, Section 3.2.A); this holds for every
process `B` and every `ω`, by definition.

Formalized by `ProbabilityTheory.ElementaryIntegrand.itoIntegral_single`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-single).

## Elementary Itô integral vanishes at time zero

The elementary Itô integral vanishes at time `0`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.itoIntegral_zero`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-zero).

## Itô isometry, discrete form

For a pre-Brownian motion `B` adapted to `F` whose
increments `B t - B s` are independent of `F s`,
`E[(∫_0^t H dB)²] = ∑ i, E[ξ_i²] (t_{i+1} ∧ t - t_i ∧ t)`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.integral_itoIntegral_sq_eq_sum`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integral-ito-integral-sq-eq-sum).

## Partition intervals of an elementary integrand are disjoint

The partition intervals of an elementary integrand are pairwise disjoint.

Formalized by `ProbabilityTheory.ElementaryIntegrand.disjoint_Ioc_time`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#disjoint-ioc-time).

## Elementary integrand on a partition interval

On its `i`-th interval, an elementary integrand equals its `i`-th coefficient.

Formalized by `ProbabilityTheory.ElementaryIntegrand.toProcess_eq_of_mem`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#to-process-eq-of-mem).

## Time integral of a squared elementary integrand

The time integral of the squared elementary integrand, path by path:
`∫_0^t H_u² du = ∑ i, ξ_i² (t_{i+1} ∧ t - t_i ∧ t)`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.integral_toProcess_sq`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integral-to-process-sq).

## Itô isometry

**Itô isometry** for elementary integrands: for a pre-Brownian motion `B` adapted to `F`
whose increments `B t - B s` are independent of `F s`,
`E[(∫_0^t H dB)²] = E ∫_0^t H_u² du` (Karatzas–Shreve 1991, Section 3.2.A).

Formalized by `ProbabilityTheory.ElementaryIntegrand.integral_itoIntegral_sq`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integral-ito-integral-sq).

## Martingale property

For a pre-Brownian motion `B` adapted to `F` whose increments
`B t - B s` are independent of `F s`, the elementary Itô integral `t ↦ ∫_0^t H dB` is an
`F`-martingale.

Formalized by `ProbabilityTheory.ElementaryIntegrand.martingale_itoIntegral`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#martingale-ito-integral).

## Polarized Itô isometry

**Polarized Itô isometry** for elementary integrands: for a pre-Brownian motion `B` adapted
to `F` whose increments `B t - B s` are independent of `F s`, and two elementary integrands
`H`, `K` (with possibly different partitions),
`E[(∫_0^t H dB) (∫_0^t K dB)] = E ∫_0^t H_u K_u du`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.integral_itoIntegral_mul`, a theorem declared in [MathlibExt/Probability/ElementaryItoIntegral.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ElementaryItoIntegral.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integral-ito-integral-mul).

## Riemann–Stieltjes integration by parts, uniform partitions

For a `C¹` function `g`, a
continuous path `w` and `t ≥ 0`, the left-point sums
`∑_{k < n} g (t k / n) (w (t (k + 1) / n) - w (t k / n))` converge, as `n → ∞`, to
`g t w t - g 0 w 0 - ∫_0^t g' w`.

Formalized by `ProbabilityTheory.tendsto_sum_mul_sub_uniform`, a theorem declared in [MathlibExt/Probability/ItoRiemannSums.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoRiemannSums.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#tendsto-sum-mul-sub-uniform).

## Left-point step approximation of a deterministic integrand

The left-point step approximation `∑_{k < n} g (t k / n) 1_{(t k / n, t (k + 1) / n]}` of a
deterministic `g` on the uniform partition of `[0, t]` into `n` cells, as an
elementary integrand for any filtration `F` (deterministic coefficients are measurable for every
σ-algebra).

Formalized by `ProbabilityTheory.ElementaryIntegrand.riemann`, a definition declared in [MathlibExt/Probability/ItoRiemannSums.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoRiemannSums.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#riemann).

## Itô integral of a Riemann step approximation

The elementary Itô integral of `riemann F g t n` at time `t` is the Itô–Riemann sum
`∑_{k < n} g (t k / n) (B (t (k + 1) / n) - B (t k / n))`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.itoIntegral_riemann`, a theorem declared in [MathlibExt/Probability/ItoRiemannSums.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoRiemannSums.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-riemann).

## Itô–Riemann sums of a deterministic `C¹` integrand

Along every continuous path of `B`,
the elementary Itô integrals at time `t` of the left-point approximations of `g` converge to
Wiener's integration-by-parts expression `g t B t - g 0 B 0 - ∫_0^t g'(u) B u du`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.tendsto_itoIntegral_riemann`, a theorem declared in [MathlibExt/Probability/ItoRiemannSums.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoRiemannSums.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#tendsto-ito-integral-riemann).

## Ornstein–Uhlenbeck path solution by integration by parts

The pathwise Ornstein–Uhlenbeck solution in integration-by-parts form: with `g u = e^{θu}`,
`ouPathSolution θ σ x₀ w t = e^{-θt} x₀ + σ e^{-θt} (g t w t - g 0 w 0 - ∫_0^t g'(u) w u du)`,
for any path `w` and any real `θ`, `σ`, `x₀`, `t`.

Formalized by `ProbabilityTheory.ouPathSolution_eq_integration_by_parts`, a theorem declared in [MathlibExt/Probability/ItoRiemannSums.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoRiemannSums.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ou-path-solution-eq-integration-by-parts).

## The Itô form of the Ornstein–Uhlenbeck solution

For a Brownian motion `B`, almost surely,
for every `t ≥ 0` and every initial value `X₀`, the Itô–Riemann sums
`e^{-θt} X₀ + σ e^{-θt} ∑_{k < n} e^{θ t k / n} (B (t (k + 1) / n) - B (t k / n))` of
`e^{-θt} X₀ + σ ∫_0^t e^{-θ(t-s)} dB_s` converge to the pathwise solution `ouPathSolution`
(any real `θ`, `σ`).

Formalized by `ProbabilityTheory.IsBrownianReal.ae_tendsto_ou_itoIntegral_riemann`, a theorem declared in [MathlibExt/Probability/ItoRiemannSums.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoRiemannSums.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ae-tendsto-ou-ito-integral-riemann).

## Squared $L^2$ distance between integrands

The squared `L²(P ⊗ du)` distance on `(0, t] × Ω` between two processes, in `ℝ≥0∞`:
`∫⁻ ω, ∫⁻ u in (0, t], |H u ω - K u ω|² du dP`.

Formalized by `ProbabilityTheory.integrandDist`, a definition declared in [MathlibExt/Probability/ItoIntegral.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist).

## Restriction of a process to the time interval (0, t)

The process `H` with its values at times outside `(0, t]` set to `0`. Only the values at
times in `(0, t]` enter the Itô integral at time `t`.

Formalized by `ProbabilityTheory.restrictIoc`, a definition declared in [MathlibExt/Probability/ItoIntegral.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#restrict-ioc).

## Itô-approximable process

A process `H` is **Itô-approximable on `[0, t]`** for the filtration `F` if it is jointly
measurable on `(0, t] × Ω` and is the `L²(P ⊗ du)`-limit on `(0, t] × Ω` of elementary
integrands. Neither condition involves the values of `H` at time `0` or after `t`.

Formalized by `ProbabilityTheory.IsItoApproximable`, a definition declared in [MathlibExt/Probability/ItoIntegral.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#is-ito-approximable).

## Function as an element of $L^2$

A function as an element of `L²(P)`, or `0` if it is not square integrable.

Formalized by `ProbabilityTheory.toL2`, a definition declared in [MathlibExt/Probability/ItoIntegral.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#to-l2).

## Itô integral as an element of $L^2$

The **Itô integral** `∫_0^t H dB` as an element of `L²(P)`: the `L²` limit of the elementary
Itô integrals of an approximating sequence of elementary integrands when `H` is Itô-approximable
on `[0, t]`, and `0` otherwise.

Formalized by `ProbabilityTheory.itoIntegralL2`, a definition declared in [MathlibExt/Probability/ItoIntegral.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-l2).

## Itô integral process

The **Itô integral** `t ↦ ∫_0^t H dB` as a real process: an `F t`-strongly measurable
version of `itoIntegralL2 P F B H t` when one exists (which is the case under the hypotheses of
the theorems below), and a representative of `itoIntegralL2 P F B H t` otherwise.

Formalized by `ProbabilityTheory.itoIntegral`, a definition declared in [MathlibExt/Probability/ItoIntegral.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-2).

## Itô integral process is a version of the $L^2$ integral

The Itô integral process is almost surely equal to `itoIntegralL2` at each time.

Formalized by `ProbabilityTheory.itoIntegral_ae_eq`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-ae-eq).

## Restriction to (0, t) preserves joint measurability

Restricting a jointly measurable process to the times `(0, t]` keeps it jointly
measurable.

Formalized by `ProbabilityTheory.measurable_restrictIoc`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#measurable-restrict-ioc).

## Integrand distance depends only on times in (0, t)

`integrandDist P X Y t` only depends on `X` and `Y` at times in `(0, t]`.

Formalized by `ProbabilityTheory.integrandDist_restrictIoc`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist-restrict-ioc).

## Locality of approximability

Itô-approximability on `[0, t]` only depends on the
integrand at times in `(0, t]`.

Formalized by `ProbabilityTheory.IsItoApproximable.congr`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#congr).

## Elementary integrands are jointly measurable

An elementary integrand is jointly measurable in `(u, ω)` (reading `u : ℝ` through
`Real.toNNReal`).

Formalized by `ProbabilityTheory.ElementaryIntegrand.measurable_toProcess`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#measurable-to-process).

## Uniform bound on an elementary integrand

An elementary integrand with `n` intervals is bounded by `n * bound`.

Formalized by `ProbabilityTheory.ElementaryIntegrand.abs_toProcess_le`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#abs-to-process-le).

## Square integrability of the elementary Itô integral

The elementary Itô integral against a pre-Brownian motion is square integrable.

Formalized by `ProbabilityTheory.ElementaryIntegrand.memLp_itoIntegral`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#mem-lp-ito-integral-2).

## Finite distance between elementary integrands

The `L²(P ⊗ du)` distance between two elementary integrands is finite.

Formalized by `ProbabilityTheory.ElementaryIntegrand.integrandDist_ne_top`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist-ne-top).

## Itô isometry for elementary integrands

`integrandDist` of two elementary integrands is the squared `L²(P)` distance of their Itô
integrals.

Formalized by `ProbabilityTheory.ElementaryIntegrand.integrandDist_eq_dist_sq`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist-eq-dist-sq).

## Quasi-triangle inequality for the integrand distance

Pointwise `|x - y|² ≤ 2 |x - z|² + 2 |y - z|²`, integrated: a quasi-triangle inequality
for `integrandDist` between jointly measurable processes.

Formalized by `ProbabilityTheory.integrandDist_le`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist-le).

## The Itô integral is well defined

For a pre-Brownian motion `B` adapted to `F` with
increments independent of the past, an `H` jointly measurable on `(0, t] × Ω`, and *any*
sequence of elementary integrands `Kn` converging to `H` in `L²(P ⊗ du)` on `(0, t] × Ω`, the
elementary Itô integrals of `Kn` converge in `L²(P)` to `itoIntegralL2 P F B H t`.

Formalized by `ProbabilityTheory.tendsto_toL2_itoIntegral`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#tendsto-to-l2-ito-integral).

## Locality of the Itô integral

The Itô integral at time `t` only depends on the integrand
at times in `(0, t]`.

Formalized by `ProbabilityTheory.itoIntegralL2_congr`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-l2-congr).

## Elementary integrands are Itô-approximable

An elementary integrand is Itô-approximable on every `[0, t]` (by itself).

Formalized by `ProbabilityTheory.isItoApproximable_toProcess`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#is-ito-approximable-to-process).

## Itô integral agrees with the elementary integral on elementary integrands

On an elementary integrand, the Itô integral agrees almost surely with the elementary Itô
integral.

Formalized by `ProbabilityTheory.itoIntegral_toProcess_ae_eq`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-to-process-ae-eq).

## Elementary integrands

For `a ≤ b` and a bounded `F a`-measurable `ξ`, the Itô integral
of `ξ 1_{(a, b]}` against a pre-Brownian motion `B` adapted to `F` with increments independent
of the past is `ξ (B (b ∧ t) - B (a ∧ t))` almost surely (Karatzas–Shreve 1991,
Section 3.2.A).

Formalized by `ProbabilityTheory.itoIntegral_indicator_Ioc`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-indicator-ioc).

## $L^2$ convergence of left-point approximations of a continuous function

The left-point approximations of a continuous deterministic `g` converge to `g` in
`L²(P ⊗ du)` on `(0, t] × Ω`.

Formalized by `ProbabilityTheory.tendsto_integrandDist_riemann`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#tendsto-integrand-dist-riemann).

## Wiener's integration by parts

For a Brownian motion `B` adapted to `F` with
increments independent of the past and a deterministic `C¹` integrand `g`, the Itô integral is
`∫_0^t g dB = g t B t - g 0 B 0 - ∫_0^t g'(u) B u du` almost surely (Karatzas–Shreve 1991,
Section 3.3; the right side is a pathwise Riemann integral).

Formalized by `ProbabilityTheory.itoIntegral_deterministic_eq`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-deterministic-eq).

## The Ornstein–Uhlenbeck solution in Itô form

For a Brownian motion `B` adapted to `F`
with increments independent of the past, any initial value `X₀` and any real `θ`, `σ`, the Itô
form `e^{-θt} X₀ + σ e^{-θt} ∫_0^t e^{θs} dB_s = e^{-θt} X₀ + σ ∫_0^t e^{-θ(t-s)} dB_s` of the
solution of `dX = -θ X dt + σ dB` (Karatzas–Shreve 1991, Section 5.6) agrees almost surely with
the pathwise solution `ouPathSolution`, which solves `X t = X₀ - θ ∫_0^t X + σ (B t - B 0)` path
by path (`ProbabilityTheory.ouPathSolution_integral_eq`).

Formalized by `ProbabilityTheory.ito_ou_solution_eq_ouPathSolution`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-ou-solution-eq-ou-path-solution).

## Measurability of the $L^2$ Itô integral

The `L²` Itô integral is (almost surely equal to) an `F t`-measurable function.

Formalized by `ProbabilityTheory.aestronglyMeasurable_itoIntegralL2`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#aestrongly-measurable-ito-integral-l2).

## Martingale property of the Itô integral

For a pre-Brownian motion `B` adapted to `F`
with increments independent of the past and an integrand `H` that is Itô-approximable on every
`[0, t]`, the Itô integral `t ↦ ∫_0^t H dB` is an `F`-martingale (Karatzas–Shreve 1991,
Proposition 3.2.10).

Formalized by `ProbabilityTheory.martingale_itoIntegral`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 722](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L722). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#martingale-ito-integral-2).

## Integrand distance as a squared $L^2$ seminorm

The integrand distance on `(0, t]` is the square of the `L²` seminorm on
`Ω × (0, t]`.

Formalized by `ProbabilityTheory.integrandDist_eq_eLpNorm_sq`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist-eq-e-lp-norm-sq).

## Itô isometry

**Itô isometry** for the `L²` Itô integral, in `ℝ≥0∞` form: for a pre-Brownian motion `B`
adapted to `F` with increments independent of the past and an integrand `H` that is
Itô-approximable on `[0, t]`, `E[(∫_0^t H dB)²] = E ∫_0^t H_u² du` (Karatzas–Shreve 1991,
Section 3.2).

Formalized by `ProbabilityTheory.lintegral_itoIntegral_sq`, a theorem declared in [MathlibExt/Probability/ItoIntegral.lean, line 818](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegral.lean#L818). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#lintegral-ito-integral-sq).

## Lebesgue differentiation along shrinking off-center intervals

For a locally integrable
`f : ℝ → ℝ`, for almost every `u`, the averages of `f` over intervals `[a n, b n]` converge to
`f u` whenever the lengths `b n - a n > 0` tend to `0` and the distance from `u` to the midpoint
of `[a n, b n]` is at most twice the length.

Formalized by `MeasureTheory.LocallyIntegrable.ae_tendsto_average_Icc`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ae-tendsto-average-icc).

## Progressive processes are jointly measurable

A progressive process is jointly measurable in `(u, ω)` (reading `u : ℝ` through
`Real.toNNReal`).

Formalized by `ProbabilityTheory.IsProgressive.measurable_toNNReal`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#measurable-to-nnreal).

## Truncation of a progressive process is progressive

Truncating a progressive process at level `M` (Mathlib's `ProbabilityTheory.truncation`,
which keeps the values in `(-M, M]` and sets the others to `0`) gives a progressive process.

Formalized by `ProbabilityTheory.IsProgressive.truncation`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#truncation).

## Measurability of time averages of a progressive process

For a progressive `H` and `b ≤ T`, the average of `u ↦ H u ω` over `[a, b]` is
`F T`-measurable in `ω`.

Formalized by `ProbabilityTheory.IsProgressive.measurable_average_Icc`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#measurable-average-icc).

## Delayed-average approximation of a progressive process

The **delayed-average approximation** of a progressive process `H` on `[0, t]`, truncated at
level `M`, with `n + 1` intervals: on `(t_k, t_{k+1}]`, with `t_k = k t / (n + 1)`, it equals the
average of `truncation (H ·) M` over `[t_{k-1}, t_k]` for `k ≥ 1`, and `0` for `k = 0`. For
`M ≤ 0` the truncation, and hence the approximation, is `0`.

Formalized by `ProbabilityTheory.delayedAverage`, a definition declared in [MathlibExt/Probability/ItoDensity.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#delayed-average).

## Convergence of the delayed averages

For a progressive `H` and a finite measure `P`, the
delayed-average approximations of the truncation of `H` at level `M` converge to it in
`L²(P ⊗ du)` on `(0, t] × Ω` as the mesh `t / (n + 1)` tends to `0` (Karatzas–Shreve 1991, proof of
Lemma 3.2.4(b)).

Formalized by `ProbabilityTheory.tendsto_integrandDist_delayedAverage`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#tendsto-integrand-dist-delayed-average).

## Truncation

For a jointly measurable `H` with `E ∫_0^t H_u² du < ∞`, the truncations of
`H` at levels `M → ∞` converge to `H` in `L²(P ⊗ du)` on `(0, t] × Ω`
(Karatzas–Shreve 1991, proof of Lemma 3.2.4(c)).

Formalized by `ProbabilityTheory.tendsto_integrandDist_truncation`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#tendsto-integrand-dist-truncation).

## Density of elementary integrands

A progressive integrand `H` with
`E ∫_0^t H_u² du < ∞` is the `L²(P ⊗ du)`-limit on `(0, t] × Ω` of elementary integrands
(Karatzas–Shreve 1991, Lemma 3.2.4 and Proposition 3.2.6).

Formalized by `ProbabilityTheory.isItoApproximable_of_isProgressive`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#is-ito-approximable-of-is-progressive).

## Square integrability of the Itô integral

The Itô integral at each time is square integrable: it is a version of the element
`itoIntegralL2 P F B H t` of `L²(P)` (which is `0` when `H` is not Itô-approximable).

Formalized by `ProbabilityTheory.memLp_itoIntegral`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#mem-lp-ito-integral).

## Itô isometry for progressive integrands

For a pre-Brownian motion `B` adapted to `F`
with increments independent of the past and an `F`-progressive integrand `H` with
`E ∫_0^t H_u² du < ∞`, `E[(∫_0^t H dB)²] = E ∫_0^t H_u² du` (Karatzas–Shreve 1991,
Section 3.2).

Formalized by `ProbabilityTheory.lintegral_itoIntegral_sq_of_isProgressive`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#lintegral-ito-integral-sq-of-is-progress).

## Martingale property for progressive integrands

For a pre-Brownian motion `B` adapted
to `F` with increments independent of the past and an `F`-progressive integrand `H` with
`E ∫_0^t H_u² du < ∞` for every `t`, the Itô integral `t ↦ ∫_0^t H dB` is an `F`-martingale
(Karatzas–Shreve 1991, Proposition 3.2.10).

Formalized by `ProbabilityTheory.martingale_itoIntegral_of_isProgressive`, a theorem declared in [MathlibExt/Probability/ItoDensity.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoDensity.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#martingale-ito-integral-of-is-progressiv).

## Continuous modification

The Itô integral admits a modification with continuous paths:
there is a process `J` with continuous paths such that `J t = ∫_0^t H dB` almost surely for each
`t` (Karatzas–Shreve 1991, Section 3.2). `ProbabilityTheory.itoIntegral` chooses its version
separately at each time, so it is only determined up to a null set that may depend on `t`; the
statement therefore asks for a modification rather than for a process indistinguishable from
this particular choice. Any two continuous modifications are indistinguishable.

Formalized by `ProbabilityTheory.itoIntegral_continuous_modification`, a theorem declared in [MathlibExt/Probability/ItoIntegralContinuous.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralContinuous.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-continuous-modification).

## Itô isometry for Itô-approximable integrands

The squared `L²(P ⊗ du)` distance between two Itô-approximable integrands is the squared
`L²(P)` distance between their Itô integrals.

Formalized by `ProbabilityTheory.integrandDist_eq_dist_sq_itoIntegralL2`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#integrand-dist-eq-dist-sq-ito-integral-l).

## Linearity (additivity)

The Itô integral is additive in the integrand: for
`F`-progressive integrands `H₁, H₂` with `E ∫_0^t H_i² du < ∞`, the integral of the sum is almost
surely the sum of the integrals. Together with homogeneity and the difference isometry this pins
down the integral on the whole `L²` space of progressive integrands. Only the pre-Brownian
finite-dimensional laws are used; path continuity is not required.

Formalized by `ProbabilityTheory.itoIntegral_add_of_isPreBrownianReal`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-add-of-is-pre-brownian-real).

## Linearity (additivity)

The Itô integral is additive in the integrand: for
`F`-progressive integrands `H₁, H₂` with `E ∫_0^t H_i² du < ∞`, the integral of the sum is almost
surely the sum of the integrals. Together with homogeneity and the difference isometry this pins
down the integral on the whole `L²` space of progressive integrands.

Formalized by `ProbabilityTheory.itoIntegral_add`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-add).

## Linearity (homogeneity)

The Itô integral is homogeneous in the integrand for a
pre-Brownian integrator; path continuity is not required.

Formalized by `ProbabilityTheory.itoIntegral_smul_of_isPreBrownianReal`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-smul-of-is-pre-brownian-rea).

## Linearity (homogeneity)

The Itô integral is homogeneous in the integrand.

Formalized by `ProbabilityTheory.itoIntegral_smul`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-smul).

## Difference isometry

For two `F`-progressive integrands with `E ∫_0^t H_i² du < ∞`, the
difference of the integrals is square-integrable and
`E[(∫ H₁ dB - ∫ H₂ dB)²] = E ∫ (H₁ - H₂)² du`. With linearity this is the two-integrand isometry
that, together with the elementary-integrand formula, determines the construction on the whole
`L²` space. Only the pre-Brownian finite-dimensional laws are used; path continuity is not
required.

Formalized by `ProbabilityTheory.itoIntegral_isometry_sub_of_isPreBrownianReal`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-isometry-sub-of-is-pre-brow).

## Difference isometry

For two `F`-progressive integrands with `E ∫_0^t H_i² du < ∞`, the
difference of the integrals is square-integrable and
`E[(∫ H₁ dB - ∫ H₂ dB)²] = E ∫ (H₁ - H₂)² du`. With linearity this is the two-integrand isometry
that, together with the elementary-integrand formula, determines the construction on the whole
`L²` space.

Formalized by `ProbabilityTheory.itoIntegral_isometry_sub`, a theorem declared in [MathlibExt/Probability/ItoIntegralProperties.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ItoIntegralProperties.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html#ito-integral-isometry-sub).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Itô integral](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/it-integral/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/stochastic-calculus/it-integral)
