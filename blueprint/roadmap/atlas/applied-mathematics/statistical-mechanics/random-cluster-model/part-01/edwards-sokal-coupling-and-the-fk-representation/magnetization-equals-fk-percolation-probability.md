---
declaration: section
origin: cited
lean: StatMech.IsingFK.origin_mem_box_boxVerts, StatMech.IsingFK.boxOrigin, StatMech.IsingFK.boxBoundaryConnProfile
statement: formalized
proof: formalized
---

# Magnetization equals FK percolation probability, through box graphs

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/magnetization-equals-fk-percolation-probability/index.html).

## Origin lies in every box

The origin lies in every box. Same statement as `Ising.origin_mem_box`, which this module does
not import.

Formalized by `StatMech.IsingFK.origin_mem_box_boxVerts`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/MagPercoIdBox.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/MagPercoIdBox.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/magnetization-equals-fk-percolation-probability/index.html#origin-mem-box-box-verts).

## Origin as a vertex of the box graph

The origin as a vertex of the box graph.

Formalized by `StatMech.IsingFK.boxOrigin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/MagPercoIdBox.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/MagPercoIdBox.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/magnetization-equals-fk-percolation-probability/index.html#box-origin).

## Wired probability that the origin reaches the box boundary

The probability `φ^w_n(0 ↔ ∂Λ_n)` that the origin is connected to the boundary of the box graph
of `Λ_n` under the wired FK measure with `q = 2`.

Formalized by `StatMech.IsingFK.boxBoundaryConnProfile`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/MagPercoIdBox.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/MagPercoIdBox.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/magnetization-equals-fk-percolation-probability/index.html#box-boundary-conn-profile).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Magnetization equals FK percolation probability, through box graphs](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/magnetization-equals-fk-percolation-probability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/magnetization-equals-fk-percolation-probability)
