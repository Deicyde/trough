---
declaration: section
origin: cited
lean: ProbabilityTheory.equalInput, ProbabilityTheory.stickyKernel, ProbabilityTheory.equalInputRate, ProbabilityTheory.equalInput_apply, ProbabilityTheory.equalInput_mul_self, ProbabilityTheory.stickyKernel_apply, ProbabilityTheory.stickyKernel_one, ProbabilityTheory.stickyKernel_zero
statement: formalized
proof: formalized
---

# The sticky (equal-input) kernel on a finite state space

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html).

## Equal-input matrix

The **equal-input matrix** `𝟙 πᵀ`: every row equals `π`.

Formalized by `ProbabilityTheory.equalInput`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#equal-input).

## Sticky kernel

The **sticky kernel** with persistence `c`: `c • 1 + (1 - c) • 𝟙 πᵀ`. Started from `i`,
it stays at `i` with probability `c` and otherwise redraws the state from `π`.

Formalized by `ProbabilityTheory.stickyKernel`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel).

## Equal-input generator (F81 model)

The **equal-input generator** `κ • (𝟙 πᵀ - 1)` with rate `κ` (Felsenstein's F81 model on
an arbitrary finite state space): jumps at rate `κ` to a state drawn from `π`.

Formalized by `ProbabilityTheory.equalInputRate`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#equal-input-rate).

## Entries of the equal-input matrix

Entrywise form of the equal-input matrix.

Formalized by `ProbabilityTheory.equalInput_apply`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#equal-input-apply).

## Equal-input matrix is idempotent

With `∑ π = 1`, `𝟙 πᵀ` is idempotent.

Formalized by `ProbabilityTheory.equalInput_mul_self`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#equal-input-mul-self).

## Entries of the sticky kernel

Entrywise form of the sticky kernel.

Formalized by `ProbabilityTheory.stickyKernel_apply`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-apply).

## Sticky kernel at persistence one is the identity

The sticky kernel at persistence `1` is the identity.

Formalized by `ProbabilityTheory.stickyKernel_one`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-one).

## Sticky kernel at persistence zero is the equal-input matrix

The sticky kernel at persistence `0` is `𝟙 πᵀ`.

Formalized by `ProbabilityTheory.stickyKernel_zero`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-zero).

## Nonnegativity of the sticky kernel

For `0 ≤ c ≤ 1` and `π ≥ 0` the entries of the sticky kernel are nonnegative.

Formalized by `ProbabilityTheory.stickyKernel_nonneg`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-nonneg).

## Reversibility

`π i K i j = π j K j i` (detailed balance), for all real `c`, `π`.

Formalized by `ProbabilityTheory.stickyKernel_reversible`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-reversible).

## Continuity of the sticky kernel in the persistence

The sticky kernel depends continuously on the persistence.

Formalized by `ProbabilityTheory.continuous_stickyKernel`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#continuous-sticky-kernel).

## Long-distance limit

For `κ > 0`, `K (e^{-κ t}) → 𝟙 πᵀ` as `t → ∞`.

Formalized by `ProbabilityTheory.tendsto_stickyKernel_atTop`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#tendsto-sticky-kernel-at-top).

## Short-distance limit

`K (e^{-κ t}) → 1` as `t → 0`, for every real `κ`.

Formalized by `ProbabilityTheory.tendsto_stickyKernel_nhds_zero`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#tendsto-sticky-kernel-nhds-zero).

## Rows of the sticky kernel sum to one

With `∑ π = 1`, the rows of the sticky kernel sum to `1` (for every real `c`).

Formalized by `ProbabilityTheory.sum_stickyKernel`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sum-sticky-kernel).

## Sticky kernel is row-stochastic

For `0 ≤ c ≤ 1`, `π ≥ 0` and `∑ π = 1` the sticky kernel is row-stochastic.

Formalized by `ProbabilityTheory.stickyKernel_mem_rowStochastic`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-mem-row-stochastic).

## Stationary vector of the sticky kernel

With `∑ π = 1`, `π` is a stationary vector of the sticky kernel: `π K = π`.

Formalized by `ProbabilityTheory.vecMul_stickyKernel`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#vec-mul-sticky-kernel).

## Composition

With `∑ π = 1`, `K c * K c' = K (c c')` for all real `c`, `c'`.

Formalized by `ProbabilityTheory.stickyKernel_mul`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-mul).

## Powers of the sticky kernel

With `∑ π = 1`, `K c ^ n = K (c ^ n)`: `n` steps of the sticky kernel are one step with
persistence `c ^ n`.

Formalized by `ProbabilityTheory.stickyKernel_pow`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-pow).

## Equal-input generator is a rate matrix

For `κ ≥ 0`, `π ≥ 0` and `∑ π = 1`, the equal-input generator is a rate matrix.

Formalized by `ProbabilityTheory.isRateMatrix_equalInputRate`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#is-rate-matrix-equal-input-rate).

## The sticky kernel is the equal-input transition function

With `∑ π = 1`,
`exp (t • κ (𝟙 πᵀ - 1)) = K (e^{-κ t})` for all real `κ` and `t`.

Formalized by `ProbabilityTheory.ctmcTransition_equalInputRate`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#ctmc-transition-equal-input-rate).

## Semigroup law

**Semigroup law** of the sticky kernel in time:
`K (e^{-κ s}) * K (e^{-κ t}) = K (e^{-κ (s + t)})` (with `∑ π = 1`).

Formalized by `ProbabilityTheory.stickyKernel_exp_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#sticky-kernel-exp-add).

## Covariance under the sticky kernel

If `(X, Y)` has joint law `P(X = i, Y = j) =
π i K i j` (stationary start, one step of the kernel), then
`Cov(f X, g Y) = c Cov_π(f, g)`. The algebraic identity holds for all real `π`, `f`, `g`, `c`;
it is a covariance of a probability law when `π` is a probability vector and `0 ≤ c ≤ 1`.

Formalized by `ProbabilityTheory.covariance_stickyKernel`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#covariance-sticky-kernel).

## Two-state ancestry covariance

**Two-state ancestry covariance** (the local-ancestry chain of a two-way pulse
admixture). With ancestry proportions `π = (α, 1 - α)` and persistence `c = (1 - r) ^ n`
(no recombination between the two sites along the `n` meioses since admixture, recombination
fraction `r` per meiosis), the indicators `I_x = [X = 0]`, `I_y = [Y = 0]` of ancestry `0` at
the two sites have covariance `α (1 - α) (1 - r) ^ n`. The kernel form of the ancestry pair is
the modeling assumption here; this statement does not derive it from a genealogy.

Formalized by `ProbabilityTheory.covariance_indicator_stickyKernel_two`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/StickyKernel.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html#covariance-indicator-sticky-kernel-two).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The sticky (equal-input) kernel on a finite state space](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-sticky-equal-input-kernel-on-a-finite-state)
