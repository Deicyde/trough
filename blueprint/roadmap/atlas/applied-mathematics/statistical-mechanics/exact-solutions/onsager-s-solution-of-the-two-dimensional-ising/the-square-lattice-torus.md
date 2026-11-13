---
declaration: section
origin: cited
lean: StatMech.Onsager.onsTorusAdj, StatMech.Onsager.onsTorusGraph, StatMech.Onsager.onsTorusGraph_eq_circulantGraph
statement: formalized
proof: formalized
---

# The square-lattice torus

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-square-lattice-torus/index.html).

## A. The torus graph

## Nearest-neighbor adjacency on the discrete torus

Nearest-neighbor adjacency on `ℤ_L × ℤ_L`: the two sites differ by `±1` in exactly one
coordinate.

Formalized by `StatMech.Onsager.onsTorusAdj`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/Torus.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/Torus.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-square-lattice-torus/index.html#ons-torus-adj).

## The $L \times L$ square-lattice torus graph

The `L × L` square-lattice torus as a simple graph on `ℤ_L × ℤ_L`, for `L > 2`.

Formalized by `StatMech.Onsager.onsTorusGraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/Torus.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/Torus.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-square-lattice-torus/index.html#ons-torus-graph).

## The torus graph is a circulant graph with jumps $(1,0)$ and $(0,1)$

The torus graph is the circulant graph of `ℤ_L × ℤ_L` with jumps `(1, 0)` and `(0, 1)`.

Formalized by `StatMech.Onsager.onsTorusGraph_eq_circulantGraph`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/Torus.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/Torus.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-square-lattice-torus/index.html#ons-torus-graph-eq-circulant-graph).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The square-lattice torus](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-square-lattice-torus/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/the-square-lattice-torus)
