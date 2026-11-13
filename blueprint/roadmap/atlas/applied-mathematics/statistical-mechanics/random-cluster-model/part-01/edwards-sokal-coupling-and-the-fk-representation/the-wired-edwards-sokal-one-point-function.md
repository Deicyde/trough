---
declaration: section
origin: cited
lean: StatMech.IsingFK.wiredColourEquiv, StatMech.IsingFK.ConnToBdry, StatMech.IsingFK.esWiredOnePoint, StatMech.IsingFK.wiredConnToBdryProb, StatMech.IsingFK.esWiredOnePoint_eq_wiredConnToBdryProb
statement: formalized
proof: formalized
---

# The wired Edwards–Sokal one-point function

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html).

## A. Counting pinned colorings

## Wired colorings as cluster colorings with a pinned boundary cluster

Colorings constant on wired clusters with boundary color `b` correspond to colorings of the
clusters of `wiredSub` with the boundary cluster colored `b`.

Formalized by `StatMech.IsingFK.wiredColourEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html#wired-colour-equiv).

## Open connection of a vertex to the boundary

The vertex `x` is joined by an open path of `ω` to a boundary vertex.

Formalized by `StatMech.IsingFK.ConnToBdry`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html#conn-to-bdry).

## Wired Edwards–Sokal one-point function

The one-point function `⟨σ_x⟩` of the wired Edwards–Sokal measure with boundary color `b` and `q
= 2`.

Formalized by `StatMech.IsingFK.esWiredOnePoint`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html#es-wired-one-point).

## Wired random-cluster probability of connecting to the boundary

The probability `φ^w(x ↔ ∂)` that `x` is connected to the boundary under the wired
random-cluster measure with `q = 2`.

Formalized by `StatMech.IsingFK.wiredConnToBdryProb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html#wired-conn-to-bdry-prob).

## Edwards–Sokal one-point identity

With `+` boundary condition, the Ising magnetization at
`x` equals the probability that `x` is connected to the boundary in the wired FK measure with `q
= 2` (Edwards and Sokal, Phys. Rev. D 38 (1988); Grimmett, *The Random-Cluster Model*, Theorem
1.16).

Formalized by `StatMech.IsingFK.esWiredOnePoint_eq_wiredConnToBdryProb`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/FKRepresentation/FvES.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html#es-wired-one-point-eq-wired-conn-to-bdry).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The wired Edwards–Sokal one-point function](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/edwards-sokal-coupling-and-the-fk-representation/the-wired-edwards-sokal-one-point-function)
