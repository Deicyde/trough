---
declaration: section
origin: cited
lean: ProbabilityTheory.ouCovariance, ProbabilityTheory.ouStationaryCovariance, ProbabilityTheory.ouCovariance_comm, ProbabilityTheory.ouCovariance_self, ProbabilityTheory.ouStationaryCovariance_self, ProbabilityTheory.tendsto_ouCovariance_add, ProbabilityTheory.IsOrnsteinUhlenbeckFromZero, ProbabilityTheory.IsStationaryOrnsteinUhlenbeck
statement: formalized
proof: formalized
---

# Ornstein–Uhlenbeck process

40 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html).

## Covariance of the Ornstein–Uhlenbeck process started at zero

The covariance function of the Ornstein–Uhlenbeck process started at `0`:
`(σ² / (2θ)) (e^{-θ|t-s|} - e^{-θ(t+s)})` (Karatzas–Shreve 1991, Section 5.6). It is meant
for `θ > 0` and times `s, t ≥ 0`; at `θ = 0` the division by zero makes it `0`.

Formalized by `ProbabilityTheory.ouCovariance`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-covariance).

## Covariance of the stationary Ornstein–Uhlenbeck process

The covariance function of the stationary Ornstein–Uhlenbeck process:
`(σ² / (2θ)) e^{-θ|t-s|}` (Uhlenbeck–Ornstein 1930). It is meant for `θ > 0`.

Formalized by `ProbabilityTheory.ouStationaryCovariance`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-stationary-covariance).

## Symmetry of the Ornstein–Uhlenbeck covariance

The OU covariance is symmetric.

Formalized by `ProbabilityTheory.ouCovariance_comm`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-covariance-comm).

## Variance of the Ornstein–Uhlenbeck process started at zero

The variance of the OU process started at `0`: `(σ² / (2θ)) (1 - e^{-2θt})`.

Formalized by `ProbabilityTheory.ouCovariance_self`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-covariance-self).

## Variance of the stationary Ornstein–Uhlenbeck process

The stationary variance `σ² / (2θ)`.

Formalized by `ProbabilityTheory.ouStationaryCovariance_self`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-stationary-covariance-self).

## Ornstein–Uhlenbeck covariance converges to the stationary one

Shifting both times by `h → ∞` turns `ouCovariance` into `ouStationaryCovariance`.

Formalized by `ProbabilityTheory.tendsto_ouCovariance_add`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#tendsto-ou-covariance-add).

## Ornstein–Uhlenbeck process started at zero

`X` is an **Ornstein–Uhlenbeck process started at `0`** with rate `θ > 0` and noise
amplitude `σ` under `P`: a centered Gaussian process with covariance `ouCovariance θ σ`.
Only the finite-dimensional laws are fixed (no path regularity).

Formalized by `ProbabilityTheory.IsOrnsteinUhlenbeckFromZero`, a structure declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-ornstein-uhlenbeck-from-zero).

## Stationary Ornstein–Uhlenbeck process

`X` is a **stationary Ornstein–Uhlenbeck process** with rate `θ > 0` and noise
amplitude `σ` under `P`: a centered Gaussian process with covariance
`ouStationaryCovariance θ σ`. Only the finite-dimensional laws are fixed.

Formalized by `ProbabilityTheory.IsStationaryOrnsteinUhlenbeck`, a structure declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-stationary-ornstein-uhlenbeck).

## Doob's clock for the Ornstein–Uhlenbeck process from zero

Doob's clock `τ t = (e^{2θt} - 1)/(2θ)` for the process started at `0`. The value is
nonnegative for every real `θ`, so `Real.toNNReal` only changes its type.

Formalized by `ProbabilityTheory.ouClock`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-clock).

## Doob's clock for the stationary Ornstein–Uhlenbeck process

Doob's clock `t ↦ e^{2θt}/(2θ)` for the stationary process (positive for `θ > 0`).

Formalized by `ProbabilityTheory.ouStationaryClock`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-stationary-clock).

## Doob's time change of Brownian motion

Doob's time change `t ↦ σ e^{-θt} B(τ t)` of a process `B`, with `τ = ouClock θ`.

Formalized by `ProbabilityTheory.ouOfBrownian`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-of-brownian).

## Doob's stationary time change of Brownian motion

Doob's stationary time change `t ↦ σ e^{-θt} B(e^{2θt}/(2θ))` of a process `B`.

Formalized by `ProbabilityTheory.ouStationaryOfBrownian`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-stationary-of-brownian).

## Construction (Doob 1942)

The time change `σ e^{-θt} B((e^{2θt} - 1)/(2θ))` of a
pre-Brownian motion is an Ornstein–Uhlenbeck process started at `0`.

Formalized by `ProbabilityTheory.IsPreBrownianReal.isOrnsteinUhlenbeckFromZero_ouOfBrownian`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-ornstein-uhlenbeck-from-zero-ou-of-br).

## Construction (Doob 1942)

The time change `σ e^{-θt} B(e^{2θt}/(2θ))` of a
pre-Brownian motion is a stationary Ornstein–Uhlenbeck process.

Formalized by `ProbabilityTheory.IsPreBrownianReal.isStationaryOrnsteinUhlenbeck_ouStationaryOfBrownian`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-stationary-ornstein-uhlenbeck-ou-stat).

## Existence of a pre-Brownian motion on path space

There is a probability measure on paths `ℝ≥0 → ℝ` under which the coordinate process is a
pre-Brownian motion (Kolmogorov extension of the Brownian finite-dimensional laws).

Formalized by `ProbabilityTheory.exists_isPreBrownianReal_eval`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#exists-is-pre-brownian-real-eval).

## Existence of the Ornstein–Uhlenbeck process started at zero

An Ornstein–Uhlenbeck process started at `0` exists for every `θ > 0` and `σ`.

Formalized by `ProbabilityTheory.exists_isOrnsteinUhlenbeckFromZero`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#exists-is-ornstein-uhlenbeck-from-zero).

## Existence of the stationary Ornstein–Uhlenbeck process

A stationary Ornstein–Uhlenbeck process exists for every `θ > 0` and `σ`.

Formalized by `ProbabilityTheory.exists_isStationaryOrnsteinUhlenbeck`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#exists-is-stationary-ornstein-uhlenbeck).

## One-time law of the Ornstein–Uhlenbeck process from zero

The one-time law of the OU process started at `0`:
`X t ~ N(0, (σ² / (2θ)) (1 - e^{-2θt}))`.

Formalized by `ProbabilityTheory.IsOrnsteinUhlenbeckFromZero.hasLaw_eval`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#has-law-eval).

## The Ornstein–Uhlenbeck process from zero starts at zero

The OU process of `IsOrnsteinUhlenbeckFromZero` starts at `0` almost surely.

Formalized by `ProbabilityTheory.IsOrnsteinUhlenbeckFromZero.eval_zero_ae_eq_zero`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#eval-zero-ae-eq-zero).

## Relaxation to stationarity

For the process started at `0`,
`cov(X (s + h), X (t + h)) → (σ² / (2θ)) e^{-θ|t-s|}` as `h → ∞`.

Formalized by `ProbabilityTheory.IsOrnsteinUhlenbeckFromZero.tendsto_covariance_add`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#tendsto-covariance-add).

## Stationary law

Each `X t` of a stationary OU process is `N(0, σ² / (2θ))`.

Formalized by `ProbabilityTheory.IsStationaryOrnsteinUhlenbeck.hasLaw_eval`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#has-law-eval-2).

## Gaussian process laws are determined by mean and covariance

The finite-dimensional laws of a real Gaussian process are determined by its mean and
covariance functions: two Gaussian processes with the same means and covariances (possibly on
different probability spaces) have the same finite-dimensional laws.

Formalized by `ProbabilityTheory.IsGaussianProcess.map_restrict_eq_of_covariance_eq`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#map-restrict-eq-of-covariance-eq).

## Time shifts of a stationary Ornstein–Uhlenbeck process

A time shift of a stationary OU process is a stationary OU process.

Formalized by `ProbabilityTheory.IsStationaryOrnsteinUhlenbeck.shift`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#shift).

## Strict stationarity

Every finite-dimensional law of a stationary OU process is
invariant under time shifts.

Formalized by `ProbabilityTheory.IsStationaryOrnsteinUhlenbeck.map_restrict_shift`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#map-restrict-shift).

## Conditional expectation of a Gaussian process given its past

For a centered Gaussian process with `cov(X u, X t) = c cov(X u, X s)` for all `u ≤ s`,
the conditional expectation of `X t` given the natural filtration at `s` is `c X s`.

Formalized by `ProbabilityTheory.IsGaussianProcess.condExp_natural_eq_of_covariance`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#cond-exp-natural-eq-of-covariance).

## Conditional law of a Gaussian process at one time given another

For a centered Gaussian process with `cov(X s, X t) = c Var(X s)`, the conditional law of
`X t` given `X s = x` is `N(c x, Var(X t) - c² Var(X s))` for almost every `x`.

Formalized by `ProbabilityTheory.IsGaussianProcess.condDistrib_eval_eq_of_covariance`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#cond-distrib-eval-eq-of-covariance).

## Mean reversion

For the OU process started at `0` and `s ≤ t`,
`E[X t | F s] = e^{-θ(t-s)} X s`, where `F` is the natural filtration of `X`.

Formalized by `ProbabilityTheory.IsOrnsteinUhlenbeckFromZero.condExp_natural`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#cond-exp-natural).

## Mean reversion

For the stationary OU process and `s ≤ t`,
`E[X t | F s] = e^{-θ(t-s)} X s`, where `F` is the natural filtration of `X`.

Formalized by `ProbabilityTheory.IsStationaryOrnsteinUhlenbeck.condExp_natural`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#cond-exp-natural-2).

## Transition law

For the OU process started at `0` and `s ≤ t`, the conditional law of
`X t` given `X s = x` is `N(e^{-θ(t-s)} x, (σ² / (2θ)) (1 - e^{-2θ(t-s)}))` for almost every
`x`.

Formalized by `ProbabilityTheory.IsOrnsteinUhlenbeckFromZero.condDistrib_eval`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 540](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L540). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#cond-distrib-eval).

## Transition law

For the stationary OU process and `s ≤ t`, the conditional law of
`X t` given `X s = x` is `N(e^{-θ(t-s)} x, (σ² / (2θ)) (1 - e^{-2θ(t-s)}))` for almost every
`x`.

Formalized by `ProbabilityTheory.IsStationaryOrnsteinUhlenbeck.condDistrib_eval`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 570](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#cond-distrib-eval-2).

## Pathwise solution of the Langevin equation

The explicit solution of the pathwise Langevin equation driven by a path `w`:
`e^{-θt} x₀ + σ (w t - e^{-θt} w 0 - θ ∫_0^t e^{-θ(t-u)} w u du)`. This is
`e^{-θt} x₀ + σ ∫_0^t e^{-θ(t-u)} dw(u)` after integration by parts (the Itô-integral form for a
Brownian path is a wanted statement).

Formalized by `ProbabilityTheory.ouPathSolution`, a definition declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-path-solution).

## Continuity of the pathwise Langevin solution

The pathwise solution is continuous when the driving path is.

Formalized by `ProbabilityTheory.continuous_ouPathSolution`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#continuous-ou-path-solution).

## Pathwise Langevin equation

For a continuous path `w` and every real `t`,
`ouPathSolution θ σ x₀ w` satisfies `x t = x₀ - θ ∫_0^t x + σ (w t - w 0)` (any real `θ`,
`σ`, `x₀`).

Formalized by `ProbabilityTheory.ouPathSolution_integral_eq`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 656](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L656). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ou-path-solution-integral-eq).

## Uniqueness

A continuous solution of `x t = x₀ - θ ∫_0^t x + σ (w t - w 0)` on
`t ≥ 0` equals `ouPathSolution θ σ x₀ w` there.

Formalized by `ProbabilityTheory.eq_ouPathSolution_of_integral_eq`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeck.lean, line 668](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeck.lean#L668). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#eq-ou-path-solution-of-integral-eq).

## Elementary Itô integrals agree for modifications

Elementary Itô integrals against two modifications of the same process agree almost
surely.

Formalized by `ProbabilityTheory.ElementaryIntegrand.itoIntegral_ae_eq_of_ae_eq`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#ito-integral-ae-eq-of-ae-eq).

## Adjoining an independent Gaussian variable

If `X₀` is a real Gaussian random variable
independent of the real Gaussian process `B`, the process indexed by `Option T` that is `X₀` at
`none` and `B t` at `some t` is a Gaussian process.

Formalized by `ProbabilityTheory.IsGaussianProcess.option_elim`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#option-elim).

## Covariance of the Wiener integrals

**Covariance of the Wiener integrals** `I_t = ∫_0^t e^{θu} dB_u`: for a pre-Brownian motion
`B` adapted to `F` with increments independent of the past and `θ ≠ 0`,
`E[I_s I_t] = (e^{2θ (s ∧ t)} - 1) / (2θ)`, by the martingale property and the Itô isometry.

Formalized by `ProbabilityTheory.integral_itoIntegralL2_exp_mul`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#integral-ito-integral-l2-exp-mul).

## The pathwise Langevin solution driven by Brownian motion is Gaussian

For a Brownian
motion `B`, `θ ≠ 0`, any real `σ`, and a start `X₀ ~ N(0, v)` independent of `B`, the process
`X t = ouPathSolution θ σ X₀ B t` (`t ≥ 0`) is a Gaussian process with `E[X t] = 0` and
`cov[X s, X t] = e^{-θ(s+t)} (v + σ² (e^{2θ (s ∧ t)} - 1) / (2θ))` (Karatzas–Shreve 1991,
Section 5.6).

Formalized by `ProbabilityTheory.IsBrownianReal.isGaussianProcess_ouPathSolution`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-gaussian-process-ou-path-solution).

## The pathwise Langevin solution is an OU process

Driven by a Brownian motion and started
at `0`, `ouPathSolution` is an Ornstein–Uhlenbeck process started at `0` (Karatzas–Shreve 1991,
Section 5.6). No filtration and no measurability of the coordinates of `B` is assumed.

Formalized by `ProbabilityTheory.IsBrownianReal.isOrnsteinUhlenbeckFromZero_ouPathSolution`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-ornstein-uhlenbeck-from-zero-ou-path).

## Stationary start

Driven by a Brownian motion `B` and started from `X₀ ~ N(0, σ²/(2θ))`
independent of `B`, `ouPathSolution` is a stationary Ornstein–Uhlenbeck process
(Karatzas–Shreve 1991, Section 5.6).

Formalized by `ProbabilityTheory.IsBrownianReal.isStationaryOrnsteinUhlenbeck_ouPathSolution`, a theorem declared in [MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/OrnsteinUhlenbeckSDE.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html#is-stationary-ornstein-uhlenbeck-ou-path).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ornstein–Uhlenbeck process](https://deicyde.github.io/atlas-lean/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/stochastic-calculus/ornstein-uhlenbeck-process)
