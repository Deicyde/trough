---
declaration: section
origin: cited
lean: StatMech.Lattice.IsOpenEdge, StatMech.Lattice.openSubgraph, StatMech.Lattice.Connected, StatMech.Lattice.cluster, StatMech.Lattice.openSubgraphInduce, StatMech.Lattice.ConnectedWithin, StatMech.Lattice.connectedWithin_mono_set, StatMech.Lattice.IsOpenCircuit
statement: formalized
proof: formalized
---

# Percolation probability and critical point

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html).

## Open lattice edge of a bond configuration

The lattice edge `{x, y}` is open in the configuration `ω`: `x` and `y` are nearest neighbours
and `ω s(x, y) = true`.

Formalized by `StatMech.Lattice.IsOpenEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#is-open-edge).

## Open subgraph of a bond configuration

The open subgraph of `ω`: the spanning subgraph of `ℤ^d` consisting of the open edges.

Formalized by `StatMech.Lattice.openSubgraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#open-subgraph).

## Connection by an open path

`x` and `y` are connected by an open path, that is, reachable in `openSubgraph d ω`.

Formalized by `StatMech.Lattice.Connected`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#connected).

## Open cluster of a site

The open cluster of `x`: the set of sites connected to `x` by an open path.

Formalized by `StatMech.Lattice.cluster`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#cluster).

## Open subgraph induced on a set of sites

The open subgraph of `ω` induced on a set `S` of sites.

Formalized by `StatMech.Lattice.openSubgraphInduce`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#open-subgraph-induce).

## Connection by an open path within a set

`x` and `y` in `S` are connected by an open path that stays inside `S`.

Formalized by `StatMech.Lattice.ConnectedWithin`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#connected-within).

## Open connection within a set is monotone in the set

Connection inside `S` implies connection inside any `T ⊇ S`.

Formalized by `StatMech.Lattice.connectedWithin_mono_set`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#connected-within-mono-set).

## Open circuit in a bond configuration

A closed walk in the open subgraph that repeats no edge (an open circuit).

Formalized by `StatMech.Lattice.IsOpenCircuit`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/Clusters.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#is-open-circuit).

## Origin of the hypercubic lattice

The origin `0 ∈ ℤ^d`.

Formalized by `StatMech.Percolation.origin`, a definition declared in [MathlibExt/Probability/Percolation/Theta.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#origin).

## Percolation event for the origin

The percolation event `{0 ↔ ∞}`: the open cluster of the origin is infinite.

Formalized by `StatMech.Percolation.percolationEvent`, a definition declared in [MathlibExt/Probability/Percolation/Theta.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#percolation-event).

## Percolation probability of bond percolation

The percolation probability `θ_d(p) = ℙ_p(0 ↔ ∞)` of Bernoulli bond percolation on `ℤ^d`
with edge density `p`.

Formalized by `StatMech.Percolation.theta`, a definition declared in [MathlibExt/Probability/Percolation/Theta.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#theta).

## Set of densities with no percolation

The set of densities `p ∈ [0, 1]` at which `θ_d(p) = 0`.

Formalized by `StatMech.Percolation.subcriticalSet`, a definition declared in [MathlibExt/Probability/Percolation/Theta.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#subcritical-set).

## Critical probability of bond percolation on the hypercubic lattice

The critical probability `p_c(d) = sup {p ∈ [0, 1] : θ_d(p) = 0}` of bond percolation on `ℤ^d`.

See also `MathlibExt.Probability.ProductBondPercolation.criticalProb`, which defines the critical
point of a general countable graph through the event that *some* infinite cluster exists; the two
agree for `ℤ^d` by translation invariance.

Formalized by `StatMech.Percolation.pc`, a definition declared in [MathlibExt/Probability/Percolation/Theta.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#pc).

## Lattice clusters agree with general graph clusters

The open cluster of `x` in the lattice model is the cluster
`MathlibExt.Probability.ProductBondPercolation.gcluster` of bond percolation on the graph
`hypercubicLattice d` with the same edge configuration.

Formalized by `StatMech.Percolation.cluster_eq_gcluster`, a theorem declared in [MathlibExt/Probability/Percolation/Theta.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#cluster-eq-gcluster).

## Lattice box as a finite set

The box `Λ_n = [-n, n]^d` as a finset.

Formalized by `StatMech.Percolation.boxFinset`, a definition declared in [MathlibExt/Probability/Percolation/Theta.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Theta.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html#box-finset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Percolation probability and critical point](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/phase-transition/percolation-probability-and-critical-point)
