---
declaration: section
origin: cited
lean: StatMech.Lattice.dualLattice, StatMech.Lattice.rot90Fun, StatMech.Lattice.rot90Inv, StatMech.Lattice.rot90Equiv, StatMech.Lattice.rot90Iso, StatMech.Lattice.selfDual, StatMech.Lattice.selfDualCross, StatMech.Lattice.crossingEdgeEquiv
statement: formalized
proof: formalized
---

# Self-duality of the square lattice

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html).

## Dual square lattice

The dual square lattice. Its vertices are the face centres of `ℤ²`, relabelled as integer
points, so as a graph it is `hypercubicLattice 2`.

Formalized by `StatMech.Lattice.dualLattice`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#dual-lattice).

## Quarter-turn rotation of the square lattice

The quarter-turn rotation `(a, b) ↦ (-b, a)` of `ℤ²`.

Formalized by `StatMech.Lattice.rot90Fun`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#rot90-fun).

## Inverse quarter-turn rotation

The inverse quarter-turn rotation `(a, b) ↦ (b, -a)` of `ℤ²`.

Formalized by `StatMech.Lattice.rot90Inv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#rot90-inv).

## Quarter-turn rotation as a permutation

The quarter-turn rotation as a permutation of `ℤ²`.

Formalized by `StatMech.Lattice.rot90Equiv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#rot90-equiv).

## Quarter-turn rotation as a lattice automorphism

The quarter-turn rotation as a graph automorphism of the square lattice.

Formalized by `StatMech.Lattice.rot90Iso`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#rot90-iso).

## Identity self-duality of the square lattice

The identity isomorphism between the square lattice and its dual.

Formalized by `StatMech.Lattice.selfDual`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#self-dual).

## Rotational self-duality of the square lattice

The isomorphism between the square lattice and its dual given by the quarter-turn rotation.

Formalized by `StatMech.Lattice.selfDualCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#self-dual-cross).

## Bijection between primal and dual edges

The bijection between primal and dual edges induced by `rot90Iso`.

Formalized by `StatMech.Lattice.crossingEdgeEquiv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#crossing-edge-equiv).

## Unordered pairs under an equivalence

An equivalence `α ≃ β` induces an equivalence of unordered pairs `Sym2 α ≃ Sym2 β`.

Formalized by `StatMech.Lattice.sym2Congr`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#sym2-congr).

## Quarter-turn rotation of unordered site pairs

The bijection on unordered pairs of sites induced by the quarter-turn rotation
`(a, b) ↦ (-b, a)`. It maps lattice edges to lattice edges, but not to the dual edge crossing them:
`{(0,0), (1,0)}` goes to `{(0,0), (0,1)}`. For the geometric crossing use `sharedPrimalEdge`.

Formalized by `StatMech.Lattice.crossEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#cross-edge).

## Rotated dual configuration

The configuration in which `e` is open exactly when the inverse quarter turn `crossEdge.symm e`
of `e` is closed in `ω`. This is the dual configuration only up to the rotation: applying it twice
gives the half-turn of `ω` (`dualConfig_dualConfig`), not `ω`.

Formalized by `StatMech.Lattice.dualConfig`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarDual.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html#dual-config).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Self-duality of the square lattice](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/self-duality-of-the-square-lattice)
