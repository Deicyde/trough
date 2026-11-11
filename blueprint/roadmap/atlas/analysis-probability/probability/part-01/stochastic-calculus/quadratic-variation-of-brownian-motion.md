---
declaration: section
origin: cited
lean: ProbabilityTheory.weightedQVError, ProbabilityTheory.integral_weightedQVError_sq_le, ProbabilityTheory.tendsto_eLpNorm_weightedQVError, ProbabilityTheory.IsPreBrownianReal.indep_natural, ProbabilityTheory.adapted_natural_of_measurable, ProbabilityTheory.IsPreBrownianReal.tendsto_eLpNorm_sum_sq_sub, ProbabilityTheory.IsPreBrownianReal.tendstoInMeasure_sum_sq
statement: formalized
proof: formalized
---

# Quadratic variation of Brownian motion

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html).

## Weighted quadratic-variation error of Brownian motion

The weighted quadratic-variation error along the uniform partition of `[0, t]` into `n`
cells: `∑_{k < n} φ(B (t k / n)) ((B (t (k + 1) / n) - B (t k / n))² - t / n)`.

Formalized by `ProbabilityTheory.weightedQVError`, a definition declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#weighted-qverror).

## Second moment of the weighted quadratic-variation error

For a pre-Brownian motion `B`
adapted to `F` with increments independent of the past, and a measurable weight `φ` bounded by
`C`, `E[(∑_{k < n} φ(B_{t_k}) ((ΔB_k)² - Δt))²] ≤ 2 C² t² / n` on the uniform partition
`t_k = t k / n` (`n ≥ 1`).

Formalized by `ProbabilityTheory.integral_weightedQVError_sq_le`, a theorem declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#integral-weighted-qverror-sq-le).

## Weighted quadratic variation of Brownian motion

Under the hypotheses of
`integral_weightedQVError_sq_le`, `∑_{k < n} φ(B_{t_k}) ((ΔB_k)² - Δt) → 0` in `L²(P)`.

Formalized by `ProbabilityTheory.tendsto_eLpNorm_weightedQVError`, a theorem declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#tendsto-e-lp-norm-weighted-qverror).

## Increments are independent of the past

For a pre-Brownian motion with measurable
coordinates, each increment `B t - B s` (`s ≤ t`) is independent of the natural filtration at
time `s` (a consequence of `IsPreBrownianReal.indepFun_shift`, the weak Markov property).

Formalized by `ProbabilityTheory.IsPreBrownianReal.indep_natural`, a theorem declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#indep-natural).

## Processes with measurable coordinates are adapted to their natural filtration

A process with measurable coordinates is adapted to its natural filtration.

Formalized by `ProbabilityTheory.adapted_natural_of_measurable`, a theorem declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#adapted-natural-of-measurable).

## Quadratic variation of Brownian motion

**Quadratic variation of Brownian motion**, `[B]_t = t`: along the uniform partitions of
`[0, t]`, `∑_{k < n} (B (t (k + 1) / n) - B (t k / n))² → t` in `L²(P)`, for every pre-Brownian
motion `B` (no filtration and no measurability of the coordinates is assumed; Øksendal 2003,
Exercise 2.17; Karatzas–Shreve 1991, Theorem 1.5.8 treats continuous square-integrable
martingales in probability).

Formalized by `ProbabilityTheory.IsPreBrownianReal.tendsto_eLpNorm_sum_sq_sub`, a theorem declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#tendsto-e-lp-norm-sum-sq-sub).

## Quadratic variation of Brownian motion in probability

Along the uniform partitions of
`[0, t]`, `∑_{k < n} (B (t (k + 1) / n) - B (t k / n))² → t` in probability.

Formalized by `ProbabilityTheory.IsPreBrownianReal.tendstoInMeasure_sum_sq`, a theorem declared in [MathlibExt/Probability/BrownianQuadraticVariation.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BrownianQuadraticVariation.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html#tendsto-in-measure-sum-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Quadratic variation of Brownian motion](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/stochastic-calculus/quadratic-variation-of-brownian-motion)
