---
declaration: section
origin: cited
lean: StatMech.Percolation.removeSite, StatMech.Percolation.IsTrifurcation, StatMech.Percolation.boxFinsetBK, StatMech.Percolation.Tcount, MathlibExt.Probability.Percolation.BurtonKeaneWanted.burton_keane_bernoulli
statement: formalized
---

# Uniqueness of the infinite cluster

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html).

## Configuration with all edges at a site closed

The configuration obtained from `ω` by closing every edge incident to `x`.

Formalized by `StatMech.Percolation.removeSite`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html#remove-site).

## Trifurcation point, without requiring infinite branches

`x` is connected to three distinct sites with infinite `ω`-clusters that are pairwise
disconnected after removing `x`. Unlike the classical definition, the three branches at `x` are
not required to be infinite.

Formalized by `StatMech.Percolation.IsTrifurcation`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html#is-trifurcation).

## Sites of a box as a finite set

The sites of the box `Λ_n` as a finset.

Formalized by `StatMech.Percolation.boxFinsetBK`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html#box-finset-bk).

## Number of trifurcation points in a box

The number of trifurcation points of `ω` in the box `Λ_n`.

Formalized by `StatMech.Percolation.Tcount`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/BurtonKeaneUniqueness.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html#tcount).

## Burton–Keane theorem

**Burton–Keane theorem** for Bernoulli bond percolation. For every dimension `d` and every
`p ∈ [0, 1]`, almost surely under the Bernoulli(`p`) bond percolation measure on `ℤ^d` there is
at most one infinite open cluster.

## Sources

- R. M. Burton, M. Keane, *Density and uniqueness in percolation*, Comm. Math. Phys. 121 (1989), 501–505.

Stated but not proved: `MathlibExt.Probability.Percolation.BurtonKeaneWanted.burton_keane_bernoulli` is written with `theorem_wanted` in [WantedExt/Probability/Percolation/BurtonKeaneWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/Percolation/BurtonKeaneWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html#burton-keane-bernoulli).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Uniqueness of the infinite cluster](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/phase-transition/uniqueness-of-the-infinite-cluster)
