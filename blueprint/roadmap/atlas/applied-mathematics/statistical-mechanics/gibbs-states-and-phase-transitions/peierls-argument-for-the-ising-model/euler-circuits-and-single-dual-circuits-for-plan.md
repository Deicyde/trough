---
declaration: section
origin: cited
lean: StatMech.Lattice.EulerianExistence.degree_eq_card_filter_edges, StatMech.Lattice.EulerianExistence.spliceWalk, StatMech.Lattice.EulerianExistence.exists_closed_eulerian, StatMech.Lattice.EulerianExistence.exists_closed_isEulerian, StatMech.Lattice.EulerianExistence.exists_closed_eulerian_of_finite_support, StatMech.Lattice.FaceBoundaryConnected, StatMech.Lattice.boundarySupport
statement: formalized
proof: formalized
---

# Euler circuits and single dual circuits for planar contours

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html).

## A. Closed trails and splicing

## Degree of a vertex equals the number of edges containing it

The degree of a vertex is the number of edges containing it. See also
`SimpleGraph.card_incidenceFinset_eq_degree`.

Formalized by `StatMech.Lattice.EulerianExistence.degree_eq_card_filter_edges`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#degree-eq-card-filter-edges).

## Splicing a closed walk into another at a shared vertex

Splice a closed walk `c` at a vertex `w` of the closed walk `p` into `p`.

Formalized by `StatMech.Lattice.EulerianExistence.spliceWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#splice-walk).

## Euler's theorem

**Euler's theorem** (existence direction): a finite connected graph with all degrees even has a
closed trail through every edge, based at any vertex. See also
`SimpleGraph.Connected.exists_isEulerian` in `MathlibExt`, which does not prescribe the base
vertex.

Formalized by `StatMech.Lattice.EulerianExistence.exists_closed_eulerian`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#exists-closed-eulerian).

## Eulerian circuit at any vertex of a finite connected even graph

The closed trail of `exists_closed_eulerian` is an Eulerian circuit in Mathlib's sense, based
at any prescribed vertex. See also `SimpleGraph.Connected.exists_isEulerian`.

Formalized by `StatMech.Lattice.EulerianExistence.exists_closed_isEulerian`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#exists-closed-is-eulerian).

## Euler's theorem for a graph supported on a finite connected set

Euler's theorem for a locally finite graph whose support lies in a finite set `T` on which the
induced graph is connected. See also `SimpleGraph.ConnectedSupport.exists_isEulerian` in
`MathlibExt`.

Formalized by `StatMech.Lattice.EulerianExistence.exists_closed_eulerian_of_finite_support`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#exists-closed-eulerian-of-finite-support).

## Connectedness of the face-boundary graph on a face set

The face-boundary graph of `K` is connected on the finite set of faces `T`.

Formalized by `StatMech.Lattice.FaceBoundaryConnected`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#face-boundary-connected).

## Finite face set containing the face-boundary support

A finite set of faces containing the support of the face-boundary graph of a finite set `K`.

Formalized by `StatMech.Lattice.boundarySupport`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsSingleCircuit.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html#boundary-support).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler circuits and single dual circuits for planar contours](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/euler-circuits-and-single-dual-circuits-for-plan)
