---
declaration: section
origin: cited
lean: MathlibExt.Probability.LinearBirthDeath.extinctionProb, MathlibExt.Probability.LinearBirthDeath.geomRatio, MathlibExt.Probability.LinearBirthDeath.prob, MathlibExt.Probability.LinearBirthDeath.prob_zero_time, MathlibExt.Probability.LinearBirthDeath.prob_nonneg, MathlibExt.Probability.LinearBirthDeath.hasSum_prob, MathlibExt.Probability.LinearBirthDeath.hasSum_mul_prob, MathlibExt.Probability.LinearBirthDeath.hasDerivAt_prob_zero
statement: formalized
proof: formalized
---

# Linear birth–death process

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html).

## Kendall's extinction probability for the birth–death process

Kendall's extinction probability `α t = P(X t = 0 | X 0 = 1)` of the linear birth–death
process with per-capita birth rate `b` and death rate `d`: `d (E - 1) / (b E - d)` with
`E = exp ((b - d) t)` if `b ≠ d`, and `b t / (1 + b t)` if `b = d`. Meaningful for `0 ≤ b`,
`0 ≤ d`, `0 ≤ t`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.extinctionProb`, a definition declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#extinction-prob).

## Kendall's geometric tail ratio

Kendall's ratio `β t` of the geometric tail of the law of `X t`: `b (E - 1) / (b E - d)`
with `E = exp ((b - d) t)` if `b ≠ d`, and `b t / (1 + b t)` if `b = d`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.geomRatio`, a definition declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#geom-ratio).

## Kendall's law of the linear birth–death process

Kendall's law of the linear birth–death process at time `t` started from one individual:
`prob b d t 0 = α t` and `prob b d t (n + 1) = (1 - α t) (1 - β t) (β t) ^ n`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.prob`, a definition declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#prob).

## Linear birth–death law at time zero

At time `0` the population is one individual: `prob b d 0 = δ₁`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.prob_zero_time`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#prob-zero-time).

## Nonnegativity of Kendall's probabilities

Kendall's probabilities are nonnegative.

Formalized by `MathlibExt.Probability.LinearBirthDeath.prob_nonneg`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#prob-nonneg).

## Kendall's probabilities sum to one

Kendall's probabilities sum to `1`: no mass escapes to infinity.

Formalized by `MathlibExt.Probability.LinearBirthDeath.hasSum_prob`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#has-sum-prob).

## Mean population size of the linear birth–death process

The mean population size at time `t` started from one individual is
`E[X t] = exp ((b - d) t)` (Kendall 1948; Bailey 1964, ch. 8).

Formalized by `MathlibExt.Probability.LinearBirthDeath.hasSum_mul_prob`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#has-sum-mul-prob).

## Forward Kolmogorov equation for the empty state

Forward Kolmogorov equation for state `0`: `p_0' = d p_1`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.hasDerivAt_prob_zero`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#has-deriv-at-prob-zero).

## Forward Kolmogorov equation for positive states

Forward Kolmogorov equation for state `n + 1`:
`p_(n+1)' = b n p_n - (b + d) (n + 1) p_(n+1) + d (n + 2) p_(n+2)`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.hasDerivAt_prob_succ`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#has-deriv-at-prob-succ).

## Backward Kolmogorov equation for the extinction probability

Backward Kolmogorov equation for the extinction probability:
`α' = d - (b + d) α + b α²` (Karlin–Taylor 1975, ch. 4).

Formalized by `MathlibExt.Probability.LinearBirthDeath.hasDerivAt_extinctionProb`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#has-deriv-at-extinction-prob).

## Uniqueness of the extinction probability solving the backward equation

The extinction probability is the only `[0, 1]`-valued solution `q` on `[0, ∞)` of the
backward equation `q' = d - (b + d) q + b q²` with `q 0 = 0`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.eq_extinctionProb_of_hasDerivWithinAt`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#eq-extinction-prob-of-has-deriv-within-a).

## Limiting extinction probability in the supercritical case

Supercritical case: if `d < b`, the extinction probability tends to `d / b`.

Formalized by `MathlibExt.Probability.LinearBirthDeath.tendsto_extinctionProb_of_lt`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#tendsto-extinction-prob-of-lt).

## Certain extinction in the critical and subcritical cases

Critical and subcritical cases: if `b ≤ d` and `0 < d`, extinction is certain in the limit.

Formalized by `MathlibExt.Probability.LinearBirthDeath.tendsto_extinctionProb_of_le`, a theorem declared in [MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BranchingProcess/LinearBirthDeath.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html#tendsto-extinction-prob-of-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear birth–death process](https://deicyde.github.io/atlas-lean/roadmap/Probability/branching-processes/linear-birth-death-process/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/branching-processes/linear-birth-death-process)
