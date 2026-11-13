---
declaration: section
origin: cited
lean: StatMech.Lattice.BoundaryCondition, StatMech.Lattice.IsOpen, StatMech.Lattice.openGraph, StatMech.Lattice.numClustersFree, StatMech.Lattice.wireRel, StatMech.Lattice.boundaryCliqueGraph, StatMech.Lattice.wiredGraph, StatMech.Lattice.numClustersWired
statement: formalized
proof: formalized
---

# Boundary conditions for bond configurations

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html).

## Boundary conditions for a bond model

Boundary conditions for a bond model on a finite graph.

Formalized by `StatMech.Lattice.BoundaryCondition`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#boundary-condition).

## Open edge in a bond configuration

The edge `{x, y}` of `G` is open in the configuration `ω`.

Formalized by `StatMech.Lattice.IsOpen`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#is-open).

## Open subgraph of a bond configuration

The spanning subgraph of `G` consisting of the open edges of `ω`.

Formalized by `StatMech.Lattice.openGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#open-graph).

## Number of open clusters with free boundary conditions

The number of open clusters (connected components of the open graph) with free boundary
conditions.

Formalized by `StatMech.Lattice.numClustersFree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#num-clusters-free).

## Boundary wiring relation

Both vertices lie on the boundary.

Formalized by `StatMech.Lattice.wireRel`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#wire-rel).

## Complete graph on the boundary vertices

The complete graph on the boundary vertices, used to wire the boundary together.

Formalized by `StatMech.Lattice.boundaryCliqueGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#boundary-clique-graph).

## Wired open graph

The wired open graph: the open edges of `ω` together with an edge between every two distinct
boundary vertices.

Formalized by `StatMech.Lattice.wiredGraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#wired-graph).

## Number of open clusters with wired boundary conditions

The number of open clusters with wired boundary conditions: all boundary vertices lie in a
single cluster.

Formalized by `StatMech.Lattice.numClustersWired`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#num-clusters-wired).

## Number of open clusters under a boundary condition

The number of open clusters under a boundary condition. The periodic case uses the free count:
the periodic identification is built into the graph `G`.

Formalized by `StatMech.Lattice.numClusters`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConditions.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html#num-clusters).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boundary conditions for bond configurations](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/random-fields/boundary-conditions-for-bond-configurations)
