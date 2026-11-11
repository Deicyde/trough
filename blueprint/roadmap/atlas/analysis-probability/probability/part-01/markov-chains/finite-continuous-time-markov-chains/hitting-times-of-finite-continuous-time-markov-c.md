---
declaration: section
origin: cited
lean: ProbabilityTheory.ctmcHittingTime, ProbabilityTheory.ctmcHittingTime_eq_add, ProbabilityTheory.ctmcHittingTime_eq_zero, ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime, ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_of_mem, ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_le, ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_mul, ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_mul_of_mem
statement: formalized
proof: formalized
---

# Hitting times of finite continuous-time Markov chains

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html).

## Probability Theory

## Hitting time of a continuous-time Markov chain

The **hitting time** `inf {t ≥ 0 | X t ∈ A}` of a set of states `A` by the chain
`X = ctmcPath Q i ω` started at `i`, valued in `ℝ≥0∞` (it is `∞` if `A` is never visited).

Formalized by `ProbabilityTheory.ctmcHittingTime`, a definition declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#ctmc-hitting-time).

## First-jump decomposition of a hitting time

From a state `i ∉ A`, the hitting time of
`A` is the first holding time plus the hitting time of the chain restarted after the first
jump.

Formalized by `ProbabilityTheory.ctmcHittingTime_eq_add`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#ctmc-hitting-time-eq-add).

## Hitting time from inside the target set is zero

From a state `i ∈ A`, the hitting time of `A` is `0` as soon as the first holding time is
positive (which fails only on a null event, see `ctmcHoldingTime`).

Formalized by `ProbabilityTheory.ctmcHittingTime_eq_zero`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#ctmc-hitting-time-eq-zero).

## Mean hitting time, first-step equation

**Mean hitting time, first-step equation** (compare Norris 1997, §3.3): from `i ∉ A`
with `q i = -Q i i ≠ 0`, `E_i H_A = 1 / q i + ∑ⱼ Π i j E_j H_A` in `ℝ≥0∞`.

Formalized by `ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#lintegral-ctmc-hitting-time).

## Mean hitting time from inside the target set is zero

From a state of `A`, the mean hitting time of `A` is `0`.

Formalized by `ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_of_mem`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 623](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L623). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#lintegral-ctmc-hitting-time-of-mem).

## Minimality of the mean hitting time

**Minimality of the mean hitting time** (compare Norris 1997, §3.3): if every state off
`A` has a positive exit rate, every `m : ι → ℝ≥0∞` with `1 / q i + ∑ⱼ Π i j m j ≤ m i` off `A`
dominates `E_i H_A`.

Formalized by `ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_le`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#lintegral-ctmc-hitting-time-le).

## Product moment of two hitting times, first-step equation

From `i ∉ A ∪ B` with
`q i ≠ 0`, `E_i (H_A H_B) = (E_i H_A + E_i H_B) / q i + ∑ⱼ Π i j E_j (H_A H_B)` in `ℝ≥0∞`.

Formalized by `ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_mul`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#lintegral-ctmc-hitting-time-mul).

## Product moment of hitting times from inside their union is zero

From a state of `A ∪ B`, the product moment of the hitting times of `A` and `B` is `0`.

Formalized by `ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_mul_of_mem`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#lintegral-ctmc-hitting-time-mul-of-mem).

## Minimality of the product moment

If `mA`, `mB` are supersolutions of the mean
equations of `A` and `B` (as in `lintegral_ctmcHittingTime_le`) and `F` satisfies
`(mA i + mB i) / q i + ∑ⱼ Π i j F j ≤ F i` off `A ∪ B`, then `F` dominates `E_i (H_A H_B)`.

Formalized by `ProbabilityTheory.IsRateMatrix.lintegral_ctmcHittingTime_mul_le`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 697](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L697). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#lintegral-ctmc-hitting-time-mul-le).

## Backward equations for the mean hitting time

**Backward equations for the mean hitting time** (compare Norris 1997, §3.3): if
`m : ι → ℝ` is nonnegative and `(Q m) i = -1` for `i ∉ A`, then `E_i H_A ≤ m i` (so it is
finite), `E_i H_A = 0` on `A`, and the real vector `E_i H_A` solves the same backward
equations. With uniqueness of the solution, this identifies `E_i H_A`.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcHittingTime_backward`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#ctmc-hitting-time-backward).

## Backward equations for the product moment of two hitting times

Let `mA`, `mB`, `f` be
nonnegative with `(Q mA) i = -1` off `A`, `(Q mB) i = -1` off `B` and
`(Q f) i = -(mA i + mB i)` off `A ∪ B`. Then `E_i (H_A H_B) ≤ f i` (so it is finite), it is `0`
on `A ∪ B`, and its real part `p` solves `(Q p) i = -(E_i H_A + E_i H_B)` off `A ∪ B`.

Formalized by `ProbabilityTheory.IsRateMatrix.ctmcHittingTime_mul_backward`, a theorem declared in [MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean, line 786](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Process/ContinuousTimeMarkovChain/HittingTime.lean#L786). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html#ctmc-hitting-time-mul-backward).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hitting times of finite continuous-time Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/markov-chains/finite-continuous-time-markov-chains/hitting-times-of-finite-continuous-time-markov-c)
