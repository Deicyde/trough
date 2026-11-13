---
declaration: section
origin: cited
lean: StatMech.FK.psiExt, StatMech.FK.outsideOpenGraph, StatMech.FK.outsideGraph, StatMech.FK.inducedWiring, StatMech.FK.innerImageGraph, StatMech.FK.psiWiredGraph_eq_sup, StatMech.FK.fullGraph, StatMech.FK.innerGraph
statement: formalized
proof: formalized
---

# Boundary conditions induced on a box by the outer annulus

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html).

## A. Gluing inner and outer configurations

## Gluing a box configuration into an outer configuration

Glue a configuration `ω` on `Λ_n` into an outer configuration `ψ` on `Λ_(n+1)`: edges of `Λ_n`
follow `ω`, the others follow `ψ`.

Formalized by `StatMech.FK.psiExt`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#psi-ext).

## Open edges of an outer configuration outside the inner box

The open edges of `ψ` on `Λ_(n+1)` that are not edges of `Λ_n`.

Formalized by `StatMech.FK.outsideOpenGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#outside-open-graph).

## Outer open graph plus the outer boundary clique

The outer graph: open outer edges of `ψ` together with the clique on `∂Λ_(n+1)`.

Formalized by `StatMech.FK.outsideGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#outside-graph).

## Wiring induced on a box through the outer graph

The wiring induced on `Λ_n` by `ψ`: distinct vertices of `Λ_n` connected in the outer graph.

Formalized by `StatMech.FK.inducedWiring`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#induced-wiring).

## Inner open edges viewed in the larger box

The open edges of `ω`, viewed as edges of `Λ_(n+1)`.

Formalized by `StatMech.FK.innerImageGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#inner-image-graph).

## Wired glued open graph is the union of inner and outer graphs

The wired open graph of the glued configuration is the union of the inner open edges and the
outer graph.

Formalized by `StatMech.FK.psiWiredGraph_eq_sup`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#psi-wired-graph-eq-sup).

## Wired open graph of a glued configuration

The wired open graph of the glued configuration on `Λ_(n+1)`.

Formalized by `StatMech.FK.fullGraph`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#full-graph).

## Inner open graph with the induced wiring

The open graph of `ω` on `Λ_n` with the induced wiring added.

Formalized by `StatMech.FK.innerGraph`, an abbreviation declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#inner-graph).

## Glued and inner graphs have the same connections on the box

Two vertices of `Λ_n` are connected in the glued graph iff they are connected in `innerGraph`.

Formalized by `StatMech.FK.fullGraph_reachable_boxVertIncl`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#full-graph-reachable-box-vert-incl).

## Outer vertex whose outer component avoids the inner box

A vertex of `Λ_(n+1)` whose outer component contains no vertex of `Λ_n`.

Formalized by `StatMech.FK.OutsideOnly`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#outside-only).

## Outer component avoiding the inner box

`OutsideOnly` as a predicate on components of the outer graph.

Formalized by `StatMech.FK.IsOutsideOnly`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#is-outside-only).

## Outer components avoiding the inner box

The components of the outer graph that avoid `Λ_n`.

Formalized by `StatMech.FK.OutsideOnlyComp`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#outside-only-comp).

## Component map into the wired glued graph

The map from components of `innerGraph` and outer components avoiding `Λ_n` to components of the
glued graph.

Formalized by `StatMech.FK.fullComponentMap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#full-component-map).

## Component decomposition of the wired glued graph

Components of the glued graph are components of `innerGraph` plus the outer components avoiding
`Λ_n`.

Formalized by `StatMech.FK.fullComponentEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#full-component-equiv).

## Number of outer components avoiding the inner box

The number of outer components avoiding `Λ_n`.

Formalized by `StatMech.FK.outsideShift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#outside-shift).

## Wired cluster count of a glued configuration splits additively

The wired cluster count of a glued configuration is the induced cluster count of `ω` plus
`outsideShift d n ψ`.

Formalized by `StatMech.FK.numClustersBC_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#num-clusters-bc-psi-ext).

## Outer Bernoulli edge factor of an outer configuration

The Bernoulli edge product over the edges of `Λ_(n+1)` outside `Λ_n`, evaluated at `ψ`.

Formalized by `StatMech.FK.psiEdgeFactor`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#psi-edge-factor).

## Edge product of a glued configuration factorizes

The edge product of a glued configuration factorizes into the inner edge product and
`psiEdgeFactor`.

Formalized by `StatMech.FK.edgeProduct_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#edge-product-psi-ext).

## Outer weight factor of an outer configuration

The factor depending only on `ψ`: `psiEdgeFactor · q ^ outsideShift`.

Formalized by `StatMech.FK.psiShift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#psi-shift).

## Domain Markov property for the wired measure on nested boxes

Domain Markov property: the wired measure on `Λ_(n+1)`, conditioned on the outer configuration
`ψ`, is the random-cluster measure on `Λ_n` with the induced wiring.

Formalized by `StatMech.FK.condBcProb_psiExt_eq_bcProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#cond-bc-prob-psi-ext-eq-bc-prob).

## Induced wiring lies below the inner boundary clique

The induced wiring lies below the clique on `∂Λ_n`.

Formalized by `StatMech.FK.inducedWiring_le_wired`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 693](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L693). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#induced-wiring-le-wired).

## Wired box measure dominates the induced-wiring measure for $q \ge 1$

For `q ≥ 1`, the measure on `Λ_n` with the induced wiring is dominated by the wired measure on
`Λ_n`.

Formalized by `StatMech.FK.condBcProb_psiExt_dominated_wired`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/StatisticalMechanics/RandomCluster/InducedBC.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html#cond-bc-prob-psi-ext-dominated-wired).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boundary conditions induced on a box by the outer annulus](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/boundary-conditions-induced-on-a-box-by-the-oute)
