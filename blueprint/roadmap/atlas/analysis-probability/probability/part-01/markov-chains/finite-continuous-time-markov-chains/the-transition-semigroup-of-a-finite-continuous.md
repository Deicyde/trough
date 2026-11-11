---
declaration: section
origin: cited
lean: ProbabilityTheory.ctmcTransition, ProbabilityTheory.ctmcTransition_zero, ProbabilityTheory.ctmcTransition_add, ProbabilityTheory.ctmcTransition_smul, ProbabilityTheory.commute_ctmcTransition, ProbabilityTheory.hasDerivAt_ctmcTransition_backward, ProbabilityTheory.hasDerivAt_ctmcTransition_forward, ProbabilityTheory.ctmcTransition_eq_exp_smul_uniformized
statement: formalized
proof: formalized
---

# The transition semigroup of a finite continuous-time Markov chain

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html).

## Probability Theory

## Transition semigroup of a continuous-time Markov chain

The transition function `P t = exp (t • Q)` of the finite continuous-time Markov chain
with generator `Q` (Norris 1997, Theorem 2.1.1).

Formalized by `ProbabilityTheory.ctmcTransition`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition).

## Transition function at time zero is the identity

At time `0` the transition function is the identity.

Formalized by `ProbabilityTheory.ctmcTransition_zero`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-zero).

## Chapman–Kolmogorov equation for the transition semigroup

The **semigroup property** (Chapman–Kolmogorov equation): `P (s + t) = P s * P t`.

Formalized by `ProbabilityTheory.ctmcTransition_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-add).

## Rescaling the generator rescales time

Rescaling the generator rescales time: `exp (t • (a • Q)) = exp ((a * t) • Q)`.

Formalized by `ProbabilityTheory.ctmcTransition_smul`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-smul).

## Generator commutes with the transition function

The generator commutes with the transition function.

Formalized by `ProbabilityTheory.commute_ctmcTransition`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#commute-ctmc-transition).

## Kolmogorov backward equation

The **Kolmogorov backward equation** `P' t = Q * P t` (Norris 1997, Theorem 2.1.1).

Formalized by `ProbabilityTheory.hasDerivAt_ctmcTransition_backward`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#has-deriv-at-ctmc-transition-backward).

## Kolmogorov forward equation

The **Kolmogorov forward equation** `P' t = P t * Q` (Norris 1997, Theorem 2.1.1).

Formalized by `ProbabilityTheory.hasDerivAt_ctmcTransition_forward`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#has-deriv-at-ctmc-transition-forward).

## Uniformization

For every real `c`,
`exp (t • Q) = e^{-c t} • exp (t • (Q + c • 1))` (Jensen 1953).

Formalized by `ProbabilityTheory.ctmcTransition_eq_exp_smul_uniformized`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-eq-exp-smul-uniformized).

## Exponential of a nonnegative matrix is nonnegative

If `A` has nonnegative entries, so does `exp (t • A)` for `t ≥ 0`.

Formalized by `ProbabilityTheory.ctmcTransition_nonneg_of_nonneg`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-nonneg-of-nonneg).

## Transition function fixes the constant vector

If `Q` annihilates the constant vector `1`, then `P t` fixes it: `P t *ᵥ 1 = 1`.

Formalized by `ProbabilityTheory.ctmcTransition_mulVec_one`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-mul-vec-one).

## Rows of the transition function sum to one

The rows of the transition function of a rate matrix sum to `1`, for every real `t`.

Formalized by `ProbabilityTheory.IsRateMatrix.sum_ctmcTransition`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#sum-ctmc-transition).

## Nonnegativity of the transition function of a rate matrix

The transition function of a rate matrix has nonnegative entries for `t ≥ 0`, by
uniformization.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcTransition_nonneg`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-nonneg).

## Transition function of a rate matrix is row-stochastic

The transition function of a rate matrix is row-stochastic for `t ≥ 0` (Norris 1997,
Theorem 2.1.2).

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcTransition_mem_rowStochastic`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/Semigroup.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html#ctmc-transition-mem-row-stochastic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The transition semigroup of a finite continuous-time Markov chain](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/the-transition-semigroup-of-a-finite-continuous)
