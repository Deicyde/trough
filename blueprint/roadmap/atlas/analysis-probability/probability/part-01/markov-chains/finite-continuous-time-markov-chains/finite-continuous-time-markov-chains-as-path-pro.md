---
declaration: section
origin: cited
lean: ProbabilityTheory.ctmcJumpMatrix, ProbabilityTheory.IsRateMatrix.ctmcJumpMatrix_nonneg, ProbabilityTheory.IsRateMatrix.sum_ctmcJumpMatrix, ProbabilityTheory.IsRateMatrix.ctmcJumpMatrix_mem_rowStochastic, ProbabilityTheory.IsRateMatrix.ctmcJumpPMF, ProbabilityTheory.ctmcStepMeasure, ProbabilityTheory.ctmcInputMeasure, ProbabilityTheory.ctmcJumpChain
statement: formalized
proof: formalized
---

# Finite continuous-time Markov chains as path processes

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html).

## Probability Theory

## Jump matrix of a rate matrix

The **jump matrix** `Π` of a matrix `Q` (Norris 1997, §2.6): for a state with exit rate
`q i = -Q i i ≠ 0`, `Π i j = Q i j / q i` for `j ≠ i` and `Π i i = 0`; a state with `q i = 0`
is absorbing, `Π i j = δ i j`.

Formalized by `ProbabilityTheory.ctmcJumpMatrix`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-matrix).

## Nonnegativity of the jump matrix

The entries of the jump matrix of a rate matrix are nonnegative.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcJumpMatrix_nonneg`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-matrix-nonneg).

## Rows of the jump matrix sum to one

The rows of the jump matrix of a rate matrix sum to `1`.

Formalized by `ProbabilityTheory.IsRateMatrix.sum_ctmcJumpMatrix`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#sum-ctmc-jump-matrix).

## Jump matrix is row-stochastic

The jump matrix of a rate matrix is row-stochastic.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcJumpMatrix_mem_rowStochastic`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-matrix-mem-row-stochastic).

## Row of the jump matrix as a probability mass function

Row `i` of the jump matrix of a rate matrix, as a probability mass function on `ι`.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcJumpPMF`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-pmf).

## Law of one step of the chain construction

The law of one step `(ξ, E)` of the construction: `ξ : ι → ι` has independent coordinates
with `ξ i ∼ Π i`, and `E` is an independent exponential clock of rate `1`.

Formalized by `ProbabilityTheory.ctmcStepMeasure`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-step-measure).

## Law of the driving step sequence of a Markov chain

The law of the i.i.d. step sequence `ω : ℕ → (ι → ι) × ℝ` driving the chain.

Formalized by `ProbabilityTheory.ctmcInputMeasure`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-input-measure).

## Jump chain of a continuous-time Markov chain

The **jump chain** started at `i`: `Y 0 = i` and `Y (n + 1) = ξ n (Y n)`.

Formalized by `ProbabilityTheory.ctmcJumpChain`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-chain).

## Holding times of a continuous-time Markov chain

The `n`-th **holding time** `S n = E n / q (Y n)`, where `q k = -Q k k`; it is `∞` when
`Y n` is absorbing (`q (Y n) = 0`). Negative clock values, a null event, give `S n = 0`.

Formalized by `ProbabilityTheory.ctmcHoldingTime`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-holding-time).

## Jump times of a continuous-time Markov chain

The `n`-th **jump time** `T n = S 0 + ⋯ + S (n - 1)`, with `T 0 = 0`.

Formalized by `ProbabilityTheory.ctmcJumpTime`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-time).

## Path of a continuous-time Markov chain

The **path** of the chain started at `i`: `X t = Y n` for the `n` with
`T n ≤ t < T (n + 1)`. If `t` is at or after the explosion time `sup T n` (a null event, by
`IsRateMatrix.ae_tendsto_ctmcJumpTime`), the value is an arbitrary state that does not depend
on `i`, `Q` or `ω`.

Formalized by `ProbabilityTheory.ctmcPath`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-path).

## Shift of the step sequence of a Markov chain

The shift of the step sequence by `n`: `(shift n ω) m = ω (n + m)`.

Formalized by `ProbabilityTheory.ctmcShift`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-shift).

## Jump times are nondecreasing

The jump times are nondecreasing.

Formalized by `ProbabilityTheory.ctmcJumpTime_mono`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-time-mono).

## Path value between consecutive jump times

If `T n ≤ t < T (n + 1)`, then `X t = Y n`.

Formalized by `ProbabilityTheory.ctmcPath_eq_of_mem`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-path-eq-of-mem).

## Jump chain of the shifted steps

The jump chain of the shifted steps started at `Y n` is the jump chain after `n`.

Formalized by `ProbabilityTheory.ctmcJumpChain_shift`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-chain-shift).

## Holding times of the shifted steps

The holding times of the shifted steps started at `Y n` are the holding times after `n`.

Formalized by `ProbabilityTheory.ctmcHoldingTime_shift`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-holding-time-shift).

## Additivity of jump times under shifting

`T (n + m) = T n + T' m`, where `T'` are the jump times of the shifted steps started at
`Y n`.

Formalized by `ProbabilityTheory.ctmcJumpTime_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-jump-time-add).

## Path restarts at a jump time

After a finite jump time `T n`, the path is the path started at `Y n` driven by the
shifted steps: `X (T n + s) = X' s` with `X'` built from `shift n ω` started at `Y n`.

Formalized by `ProbabilityTheory.ctmcPath_jumpTime_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-path-jump-time-add).

## First-jump decomposition

**First-jump decomposition** of the path: before the first holding time the chain is at
`i`; afterwards it is the chain started at `ξ 0 i` driven by the shifted steps.

Formalized by `ProbabilityTheory.ctmcPath_eq_ite`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-path-eq-ite).

## Measurability of the jump chain

The jump chain `Y n` is a measurable function of the steps.

Formalized by `ProbabilityTheory.measurable_ctmcJumpChain`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#measurable-ctmc-jump-chain).

## Measurability of the holding times

The holding time `S n` is a measurable function of the steps.

Formalized by `ProbabilityTheory.measurable_ctmcHoldingTime`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#measurable-ctmc-holding-time).

## Measurability of the jump times

The jump time `T n` is a measurable function of the steps.

Formalized by `ProbabilityTheory.measurable_ctmcJumpTime`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#measurable-ctmc-jump-time).

## Joint measurability of the chain path in time and steps

The path `(t, ω) ↦ X t` is jointly measurable in the time and the steps.

Formalized by `ProbabilityTheory.measurable_ctmcPath_uncurry`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#measurable-ctmc-path-uncurry).

## Measurability of the chain state at a fixed time

The state `X t` is a measurable function of the steps.

Formalized by `ProbabilityTheory.measurable_ctmcPath`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#measurable-ctmc-path).

## Non-explosion

**Non-explosion** (Norris 1997, §2.7, for a finite state space): almost surely
the jump times of the chain started at `i` tend to `∞`, so `X t` is a genuine state of the
jump chain for every `t ≥ 0`.

Formalized by `ProbabilityTheory.IsRateMatrix.ae_tendsto_ctmcJumpTime`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 754](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L754). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ae-tendsto-ctmc-jump-time).

## Strong Markov property at jump times

**Strong Markov property at jump times** (Norris 1997, §2.6–2.7): let `A` be a
measurable set of histories of the first `n` steps such that `T n < ∞` whenever the history
lies in `A`; these histories determine `Y 0, …, Y n` and `S 0, …, S (n - 1)`. Then for every
state `k` and every measurable set `B` of paths, the path after `T n` is independent of the
event `{history ∈ A, Y n = k}` and distributed as the chain started at `k`.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcInputMeasure_ctmcPath_jumpTime_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 793](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L793). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-input-measure-ctmc-path-jump-time-a).

## Kolmogorov

**Kolmogorov** (Norris 1997, §2.8, Theorem 2.8.2 for a finite state space): the chain
built from the jump chain and the holding times has transition function `exp (t • Q)`:
`P_i(X t = j) = exp (t Q) i j` for every `t ≥ 0`.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcInputMeasure_real_ctmcPath_eq`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 1126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L1126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-input-measure-real-ctmc-path-eq).

## Restart law at a fixed time

**Restart law at a fixed time** (cf. the Markov property, Norris 1997, §2.8), for events of
`X s` and of the path after `s` only: for the chain started at `i`, the probability that
`X s = k` and that the path after `s` lies in a measurable set `B` is `exp (s Q) i k` times the
probability that the chain started at `k` lies in `B`. This is weaker than the Markov property
with respect to the natural filtration: arbitrary events of the path before `s` are not covered
(only through the finite-dimensional distributions, `ctmcInputMeasure_real_ctmcPath_fdd`).

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcInputMeasure_real_ctmcPath_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 1296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L1296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-input-measure-real-ctmc-path-add).

## Finite-dimensional distributions

**Finite-dimensional distributions** (Norris 1997, §2.8, Theorem 2.8.2 (c)): with
increments `s 0, …, s (n - 1) ≥ 0`, times `t k = s 0 + ⋯ + s k`, and states `j 0, …, j (n - 1)`,
`P_i(X (t k) = j k for all k) = ∏ₖ exp (s k Q) (j (k - 1)) (j k)`, where `j (-1) = i`.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcInputMeasure_real_ctmcPath_fdd`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean, line 1496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Path.lean#L1496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html#ctmc-input-measure-real-ctmc-path-fdd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite continuous-time Markov chains as path processes](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/finite-continuous-time-markov-chains-as-path-pro)
