---
declaration: section
origin: cited
lean: StatMech.Ising.twoPeierlsBound, StatMech.Ising.InteriorAssignment, StatMech.Ising.OuterContourMap, StatMech.Ising.poc_circuitFamily, StatMech.Ising.poc_circuitSummand
statement: formalized
proof: formalized
---

# Outer contours on the square lattice

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html).

## A. The doubled Peierls series

## Twice the Peierls series

Twice the Peierls series.

Formalized by `StatMech.Ising.twoPeierlsBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html#two-peierls-bound).

## Assignment of interiors to closed walks of $\mathbb{Z}^2$

An assignment of a set of sites (its interior) to every closed walk of `ℤ²`.

Formalized by `StatMech.Ising.InteriorAssignment`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html#interior-assignment).

## Outer contour map: clusters as interiors of boundary circuits

Every cluster through the origin is the interior of one of its closed boundary circuits, for
some interior assignment.

Formalized by `StatMech.Ising.OuterContourMap`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html#outer-contour-map).

## Cycles of length less than $M$ based near the origin

The closed walks of `ℤ²` of length at most `M` based near the origin.

Formalized by `StatMech.Ising.poc_circuitFamily`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html#poc-circuit-family).

## Boltzmann weight of a closed walk in the circuit sum

The Boltzmann weight attached to a closed walk in the circuit sum.

Formalized by `StatMech.Ising.poc_circuitSummand`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/PeierlsOuterContour.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html#poc-circuit-summand).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Outer contours on the square lattice](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/outer-contours-on-the-square-lattice)
