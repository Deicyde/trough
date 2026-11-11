---
declaration: section
origin: cited
lean: StatMech.FK.boxVertIncl, StatMech.FK.boxGraphEmb, StatMech.FK.innerEdge, StatMech.FK.IsInnerVert, StatMech.FK.crossExt, StatMech.FK.innerBdry, StatMech.FK.crossWiredGraph, StatMech.FK.innerWiredGraph
statement: formalized
proof: formalized
---

# The wired box measure as a conditional measure on the next box

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html).

## A. Including `Λ_n` into `Λ_{n+1}`

## Inclusion of box vertices into the next box

The inclusion of the vertices of `Λ_n` into `Λ_{n+1}`. The case `m = n + 1` of `boxVertInclLE`.

Formalized by `StatMech.FK.boxVertIncl`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#box-vert-incl).

## Box as an induced subgraph of the next box

`Λ_n` as an induced subgraph of `Λ_{n+1}`.

Formalized by `StatMech.FK.boxGraphEmb`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#box-graph-emb).

## Inclusion of box edges into the next box

The inclusion of edges (unordered pairs) of `Λ_n` into `Λ_{n+1}`.

Formalized by `StatMech.FK.innerEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-edge).

## Vertex of the next box lying in the inner box

A vertex of `Λ_{n+1}` lies in `Λ_n`.

Formalized by `StatMech.FK.IsInnerVert`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#is-inner-vert).

## Extension of a configuration closing the annulus edges

The extension of a configuration of `Λ_n` to `Λ_{n+1}` that closes every edge not coming from
`Λ_n`.

Formalized by `StatMech.FK.crossExt`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-ext).

## Vertex on the boundary of the inner box

A vertex of `Λ_{n+1}` on the vertex boundary of `Λ_n`.

Formalized by `StatMech.FK.innerBdry`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-bdry).

## Extended open graph with the inner box boundary wired

The open subgraph of `crossExt ω` in `Λ_{n+1}` with the boundary of `Λ_n` wired.

Formalized by `StatMech.FK.crossWiredGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-wired-graph).

## Open graph of a box configuration with the box boundary wired

The open subgraph of `ω` in `Λ_n` with the boundary of `Λ_n` wired.

Formalized by `StatMech.FK.innerWiredGraph`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-wired-graph).

## Inclusion of the wired inner graph into the extended wired graph

The inclusion of the wired open graph of `Λ_n` into `crossWiredGraph`.

Formalized by `StatMech.FK.innerWiredHom`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-wired-hom).

## Map from inner wired components and annulus vertices to components

Components of `crossWiredGraph` from wired components of `ω` in `Λ_n` and annulus vertices.

Formalized by `StatMech.FK.crossComponentEquivFun`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-component-equiv-fun).

## Extended-graph components as inner components plus annulus vertices

Components of `crossWiredGraph` are the wired components of `ω` in `Λ_n` plus one singleton per
annulus vertex.

Formalized by `StatMech.FK.crossComponentEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-component-equiv).

## Number of annulus vertices between consecutive boxes

The number of vertices of the annulus `Λ_{n+1} \ Λ_n`.

Formalized by `StatMech.FK.annulusCard`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#annulus-card).

## Number of next-box edges not coming from the inner box

The number of edges of `Λ_{n+1}` not coming from `Λ_n`.

Formalized by `StatMech.FK.nonInnerEdgeCard`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#non-inner-edge-card).

## Annulus constant linking the extended and wired inner weights

The constant `(1 - p)^{#annulus edges} q^{#annulus vertices}` relating the extended weight to
the
wired weight on `Λ_n`.

Formalized by `StatMech.FK.crossShift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-shift).

## Edges of the next box coming from the inner box

The edges of `Λ_{n+1}` coming from `Λ_n`.

Formalized by `StatMech.FK.innerEdgeFinset`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-edge-finset).

## Restriction of a next-box configuration to the inner edges

The restriction of a configuration of `Λ_{n+1}` to the edges of `Λ_n`.

Formalized by `StatMech.FK.innerRestrict`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-restrict).

## Configurations closed off the inner edges as inner-box configurations

Configurations of `Λ_{n+1}` closed off the inner edges correspond to configurations of `Λ_n`.

Formalized by `StatMech.FK.innerFibreEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-fibre-equiv).

## Domain Markov property for the wired box measure

Conditioned on every edge outside `Λ_n` being
closed, the random-cluster measure on `Λ_{n+1}` with the boundary of `Λ_n` wired is the wired
random-cluster measure on `Λ_n` (Grimmett, *The Random-Cluster Model*, 2006, Lemma 4.13).

Formalized by `StatMech.FK.condBcProb_crossExt_eq_wiredFkProb`, a theorem declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cond-bc-prob-cross-ext-eq-wired-fk-prob).

## Wiring with every edge inside the annulus

Every edge of `D` joins vertices of the annulus `Λ_{n+1} \ Λ_n`.

Formalized by `StatMech.FK.IsAnnulusWiring`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 538](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L538). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#is-annulus-wiring).

## Extended wired graph with an extra wiring added

`crossWiredGraph` with the extra wiring `D` added.

Formalized by `StatMech.FK.crossWiredGraphAdd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-wired-graph-add).

## Vertices of the annulus between consecutive boxes

The vertices of the annulus `Λ_{n+1} \ Λ_n`.

Formalized by `StatMech.FK.AnnulusVert`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#annulus-vert).

## Restriction of a wiring to the annulus vertices

The restriction of `D` to the annulus vertices.

Formalized by `StatMech.FK.annulusSubgraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#annulus-subgraph).

## Inclusion of the wired inner graph into the extra-wired graph

The inclusion of the wired open graph of `Λ_n` into `crossWiredGraphAdd`.

Formalized by `StatMech.FK.innerWiredHomAdd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#inner-wired-hom-add).

## Inclusion of the annulus wiring into the extra-wired graph

The inclusion of the annulus wiring into `crossWiredGraphAdd`.

Formalized by `StatMech.FK.annulusHomAdd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#annulus-hom-add).

## Map from inner and annulus-wiring components to extra-wired ones

Components of `crossWiredGraphAdd` from wired components of `ω` in `Λ_n` and components of the
annulus wiring.

Formalized by `StatMech.FK.crossComponentEquivAddFun`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-component-equiv-add-fun).

## Extra-wired components as inner plus annulus-wiring components

Components of `crossWiredGraphAdd` are the wired components of `ω` in `Λ_n` plus the components
of
the annulus wiring.

Formalized by `StatMech.FK.crossComponentEquivAdd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-component-equiv-add).

## Annulus constant counting the components of an extra wiring

The constant `(1 - p)^{#annulus edges} q^{#components of the annulus wiring}`.

Formalized by `StatMech.FK.crossShiftAdd`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean, line 808](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/BoxCrossGraph.lean#L808). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html#cross-shift-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The wired box measure as a conditional measure on the next box](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/the-wired-box-measure-as-a-conditional-measure-o)
