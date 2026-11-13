---
declaration: section
origin: cited
lean: MathlibExt.Probability.ContinuousPathConvergence.continuousPath_measure_ext_of_finset_eval, MathlibExt.Probability.ContinuousPathConvergence.tendsto_continuousPath_of_tight_of_finset_eval
statement: formalized
proof: formalized
---

# Weak convergence in the space of continuous functions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/weak-convergence-in-the-space-of-continuous-func/index.html).

## Continuous-path laws are determined by finite-dimensional marginals

Probability measures on continuous real paths over `[0, T]` are
determined by all of their finite evaluation pushforwards. The empty `Finset`
is included, and repeated coordinates are identified by `Finset`.

Formalized by `MathlibExt.Probability.ContinuousPathConvergence.continuousPath_measure_ext_of_finset_eval`, a theorem declared in [MathlibExt/Probability/ContinuousPathConvergence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ContinuousPathConvergence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/weak-convergence-in-the-space-of-continuous-func/index.html#continuous-path-measure-ext-of-finset-ev).

## Tightness plus finite-dimensional convergence gives weak convergence

Let `T > 0`. A tight sequence of probability laws on
`C(Set.Icc 0 T, ℝ)` converges weakly to `μ` in the uniform topology if every
finite evaluation pushforward converges weakly to the corresponding
pushforward of `μ`.

This is a condition-to-convergence criterion, not a process convergence
theorem: applications must separately prove tightness and all finite-dimensional
convergences for their constructed laws.

Formalized by `MathlibExt.Probability.ContinuousPathConvergence.tendsto_continuousPath_of_tight_of_finset_eval`, a theorem declared in [MathlibExt/Probability/ContinuousPathConvergence.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/ContinuousPathConvergence.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/weak-convergence-in-the-space-of-continuous-func/index.html#tendsto-continuous-path-of-tight-of-fins).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weak convergence in the space of continuous functions](https://deicyde.github.io/atlas-lean/roadmap/Probability/convergence-of-measures/weak-convergence-in-the-space-of-continuous-func/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/convergence-of-measures/weak-convergence-in-the-space-of-continuous-func)
