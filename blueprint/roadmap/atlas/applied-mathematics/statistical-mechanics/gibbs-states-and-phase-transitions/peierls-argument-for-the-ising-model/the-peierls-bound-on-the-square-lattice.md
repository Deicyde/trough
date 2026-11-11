---
declaration: section
origin: cited
lean: StatMech.Ising.OuterContourFill, StatMech.Ising.outerExteriorComponent, StatMech.Ising.spinCompatibleFill, StatMech.Ising.spinCompatibleFillFinset, StatMech.Ising.peierls_long_range_order_spinCompatibleFill, StatMech.Ising.peierls_probOriginMinus_le_uniform, StatMech.Ising.isoOriginCompletion, StatMech.Ising.outerContourFill_nonvacuous
statement: formalized
proof: formalized
---

# The Peierls bound on the square lattice

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html).

## Filled-cluster winding hypothesis

The filled-cluster form of the winding hypothesis, with a face-connected boundary.

Formalized by `StatMech.Ising.OuterContourFill`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#outer-contour-fill).

## Exterior component of the complement of a set

The component of the complement of `S` that contains the outside of `Λ_n`.

Formalized by `StatMech.Ising.outerExteriorComponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#outer-exterior-component).

## Set with its holes filled

The set `S` with its holes filled: the complement of its exterior component.

Formalized by `StatMech.Ising.spinCompatibleFill`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#spin-compatible-fill).

## Filled minus cluster of the origin as a finite set

The filled minus cluster of the origin, as a finset.

Formalized by `StatMech.Ising.spinCompatibleFillFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#spin-compatible-fill-finset).

## Plus and minus box measures on $\mathbb{Z}^2$ differ for large $\beta$

Plus and minus box measures on `ℤ²` differ for all `β` beyond some `β₀`. See
`peierls_probOriginMinus_le_uniform` for the informative uniform bound; the inequality of
measures itself holds for every `β > 0`.

Formalized by `StatMech.Ising.peierls_long_range_order_spinCompatibleFill`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#peierls-long-range-order-spin-compatible).

## Peierls bound

**Peierls bound** on `ℤ²`, uniform in the box: there is `β₀` such that for `β ≥ β₀` the
probability that the origin is minus under the plus-boundary box measure on `Λ_n` is at most
`twoPeierlsBound 2 β`, which is less than `1 / 2` and independent of `n`.

Formalized by `StatMech.Ising.peierls_probOriginMinus_le_uniform`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#peierls-prob-origin-minus-le-uniform).

## Configuration with only the origin minus

The configuration on `Λ_n` with only the origin minus.

Formalized by `StatMech.Ising.isoOriginCompletion`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#iso-origin-completion).

## Origin-only minus configuration satisfies the filled-cluster data

A nonvacuity check: the configuration with only the origin minus satisfies the data of
`OuterContourFill`.

Formalized by `StatMech.Ising.outerContourFill_nonvacuous`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/PeierlsSquareLattice.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html#outer-contour-fill-nonvacuous).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The Peierls bound on the square lattice](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-peierls-bound-on-the-square-lattice)
