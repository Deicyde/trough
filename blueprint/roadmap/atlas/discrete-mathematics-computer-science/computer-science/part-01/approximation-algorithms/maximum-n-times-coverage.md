---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.MaxNTimesCoverage.coverCount, Cslib.Algorithms.Lean.MaxNTimesCoverage.nCoverage, Cslib.Algorithms.Lean.MaxNTimesCoverage.IsSubmodular, Cslib.Algorithms.Lean.MaxNTimesCoverage.coverCount_mono, Cslib.Algorithms.Lean.MaxNTimesCoverage.nCoverage_mono, Cslib.Algorithms.Lean.MaxNTimesCoverage.not_isSubmodular_nCoverage, Cslib.Algorithms.Lean.MaxNTimesCoverage.isSubmodular_nCoverage_one
statement: formalized
proof: formalized
---

# Maximum n-times coverage

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html).

## Cover count of an element under a family of overlays

The number of times the overlays `O` cover the element `i` (equation (1)).

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.coverCount`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#cover-count).

## The n-times coverage function

The `n`-times coverage function: the total weight of the elements covered at least `n`
times by `O` (equation (2)).

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.nCoverage`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#n-coverage).

## Submodular set function

A set function is submodular if adding an element to a larger set gains at most as much
as adding it to a smaller set (the diminishing-returns form, Definition 2 of the paper).

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.IsSubmodular`, a definition declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#is-submodular).

## Monotonicity of the cover count in the overlays

More overlays cover every element at least as often.

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.coverCount_mono`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#cover-count-mono).

## Monotonicity of n-times coverage for nonnegative weights

For nonnegative weights the `n`-times coverage function is monotone.

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.nCoverage_mono`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#n-coverage-mono).

## The `n`-times coverage function is not submodular

**The `n`-times coverage function is not submodular** (Liu et al., Theorem 1): for every
`n ≥ 2`, take `n` overlays that each cover a single element of weight `1` once. Adding the last
overlay to the other `n - 1` gains `1`; adding it to `∅` gains `0`.

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.not_isSubmodular_nCoverage`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#not-is-submodular-n-coverage).

## Weighted maximum coverage is submodular

For `n = 1` (weighted maximum coverage) and nonnegative weights, the objective is
submodular.

Formalized by `Cslib.Algorithms.Lean.MaxNTimesCoverage.isSubmodular_nCoverage_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Approximation/MaxNTimesCoverage.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html#is-submodular-n-coverage-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum n-times coverage](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/approximation-algorithms/maximum-n-times-coverage)
