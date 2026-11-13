---
declaration: section
origin: cited
lean: StatMech.FK.wiredFkWeight, StatMech.FK.wiredFkZ, StatMech.FK.wiredFkProb, StatMech.FK.wiredFkPMF, StatMech.FK.boxVerts, StatMech.FK.boxGraph, StatMech.FK.boxBoundary, StatMech.FK.edgeIncl
statement: formalized
proof: formalized
---

# Finite- and infinite-volume FK measures on ℤ^d

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html).

## A. The wired random-cluster measure on a finite graph

## Wired random-cluster weight

The unnormalized wired random-cluster weight `edgeProduct G p ω · q ^ k¹(ω)`, where `k¹` counts
clusters after wiring all boundary vertices together.

Formalized by `StatMech.FK.wiredFkWeight`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-fk-weight).

## Wired random-cluster partition function

The wired partition function: the sum of `wiredFkWeight` over all configurations.

Formalized by `StatMech.FK.wiredFkZ`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-fk-z).

## Wired random-cluster probability of a configuration

The wired random-cluster probability of a configuration, `wiredFkWeight / wiredFkZ`.

Formalized by `StatMech.FK.wiredFkProb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-fk-prob).

## Wired random-cluster measure as a probability mass function

The wired random-cluster measure on a finite graph, as a probability mass function.

Formalized by `StatMech.FK.wiredFkPMF`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-fk-pmf).

## Vertices of the box $(-n, n)^d$

The vertices of the box `Λ_n = [-n, n]^d ⊆ ℤ^d`, as a subtype.

Formalized by `StatMech.FK.boxVerts`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#box-verts).

## Nearest-neighbour graph on a box

The nearest-neighbour graph on the box `Λ_n`, induced from the hypercubic lattice.

Formalized by `StatMech.FK.boxGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#box-graph).

## Vertex boundary of a box

The vertex boundary of the box: sites of `Λ_n` that are not in `Λ_(n-1)`.

Formalized by `StatMech.FK.boxBoundary`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#box-boundary).

## Inclusion of box edges into $\mathbb{Z}^d$

The inclusion of edges of the box into edges of `ℤ^d`.

Formalized by `StatMech.FK.edgeIncl`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#edge-incl).

## Extension of a box configuration by closed edges

Extend a configuration on the box to `ℤ^d` by declaring every edge outside the box closed.

Formalized by `StatMech.FK.extendEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#extend-edge).

## Free random-cluster measure on a box

The free random-cluster measure `φ⁰_n` on the box `Λ_n`, pushed to the configuration space of
`ℤ^d` by `extendEdge`.

Formalized by `StatMech.FK.freeFiniteMeasure`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#free-finite-measure).

## Wired random-cluster measure on a box

The wired random-cluster measure `φ¹_n` on the box `Λ_n` (boundary vertices wired), pushed to
the configuration space of `ℤ^d` by `extendEdge`.

Formalized by `StatMech.FK.wiredFiniteMeasure`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-finite-measure).

## Free infinite-volume random-cluster measure

A free infinite-volume random-cluster measure on `ℤ^d`: a weak limit of a subsequence of
`freeFiniteMeasure d n`, chosen by Prokhorov compactness.

Formalized by `StatMech.FK.freeInfiniteVolume`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#free-infinite-volume).

## Free infinite-volume measure is a subsequential weak limit

`freeInfiniteVolume` is the weak limit of `freeFiniteMeasure` along some strictly increasing
sequence of box sizes.

Formalized by `StatMech.FK.freeInfiniteVolume_isLimit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#free-infinite-volume-is-limit).

## Wired infinite-volume random-cluster measure

A wired infinite-volume random-cluster measure on `ℤ^d`: a weak limit of a subsequence of
`wiredFiniteMeasure d n`, chosen by Prokhorov compactness.

Formalized by `StatMech.FK.wiredInfiniteVolume`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-infinite-volume).

## Wired infinite-volume measure is a subsequential weak limit

`wiredInfiniteVolume` is the weak limit of `wiredFiniteMeasure` along some strictly increasing
sequence of box sizes.

Formalized by `StatMech.FK.wiredInfiniteVolume_isLimit`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InfiniteVolume.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html#wired-infinite-volume-is-limit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite- and infinite-volume FK measures on ℤ^d](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/finite-and-infinite-volume-fk-measures-on-d)
