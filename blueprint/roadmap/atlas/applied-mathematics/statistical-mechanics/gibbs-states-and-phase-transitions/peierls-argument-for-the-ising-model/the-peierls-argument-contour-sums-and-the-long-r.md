---
declaration: section
origin: cited
lean: StatMech.Ising.peierlsBound, StatMech.Ising.peierlsRatio, StatMech.Ising.probOriginMinus, StatMech.Ising.PeierlsContourBound
statement: formalized
proof: formalized
---

# The Peierls argument: contour sums and the long-range-order criterion

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r/index.html).

## A. The Peierls series

## Peierls series

The Peierls series `∑_ℓ ℓ (2d)^ℓ e^{-2βℓ}`.

Formalized by `StatMech.Ising.peierlsBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r/index.html#peierls-bound).

## Ratio $2d e^{-2\beta}$ of the Peierls series

The ratio `2d e^{-2β}` of the Peierls series.

Formalized by `StatMech.Ising.peierlsRatio`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r/index.html#peierls-ratio).

## Probability that the origin spin is minus

The probability that the origin spin is minus under the box measure with boundary condition
`η`.

Formalized by `StatMech.Ising.probOriginMinus`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r/index.html#prob-origin-minus).

## Peierls bound on the probability that the origin is minus

Under the plus box measure on `Λ_n`, the origin is minus with probability at most
`peierlsBound d β`.

Formalized by `StatMech.Ising.PeierlsContourBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsCriterion.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r/index.html#peierls-contour-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Peierls argument: contour sums and the long-range-order criterion](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-argument-contour-sums-and-the-long-r)
