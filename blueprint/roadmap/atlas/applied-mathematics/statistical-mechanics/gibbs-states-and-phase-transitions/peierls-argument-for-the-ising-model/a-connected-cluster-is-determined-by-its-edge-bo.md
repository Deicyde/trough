---
declaration: section
origin: cited
lean: StatMech.Lattice.edgeStraddles, StatMech.Lattice.boundaryEdgeSet, StatMech.Lattice.latticeMinusBoundary
statement: formalized
proof: formalized
---

# A connected cluster is determined by its edge boundary

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/a-connected-cluster-is-determined-by-its-edge-bo/index.html).

## Edge with exactly one endpoint in a set

An edge straddles `K` if exactly one of its endpoints lies in `K`.

Formalized by `StatMech.Lattice.edgeStraddles`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterBoundaryRecovery.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterBoundaryRecovery.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/a-connected-cluster-is-determined-by-its-edge-bo/index.html#edge-straddles).

## Edge boundary of a set of sites

The edge boundary `∂K`: the lattice edges that straddle `K`.

Formalized by `StatMech.Lattice.boundaryEdgeSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterBoundaryRecovery.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterBoundaryRecovery.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/a-connected-cluster-is-determined-by-its-edge-bo/index.html#boundary-edge-set).

## Hypercubic lattice with the edge boundary removed

The hypercubic lattice with the edges straddling `K` removed.

Formalized by `StatMech.Lattice.latticeMinusBoundary`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterBoundaryRecovery.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/ClusterBoundaryRecovery.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/a-connected-cluster-is-determined-by-its-edge-bo/index.html#lattice-minus-boundary).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A connected cluster is determined by its edge boundary](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/a-connected-cluster-is-determined-by-its-edge-bo/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/a-connected-cluster-is-determined-by-its-edge-bo)
