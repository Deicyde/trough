---
declaration: section
origin: cited
lean: StatMech.FK.ocd_IsInnerVert, StatMech.FK.ocd_innerEdge, StatMech.FK.ocd_innerEdge_injective, StatMech.FK.ocd_innerEdge_mk, StatMech.FK.ocd_AdjMatch, StatMech.FK.ocd_psiExt, StatMech.FK.ocd_innerRestrict, StatMech.FK.ocd_innerEdgeFinset
statement: formalized
proof: formalized
---

# Domination of an inner wired FK measure by an outer one

77 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html).

## A.1. Inner edges

## Inner vertex of the outer graph

A vertex of `G_out` is inner if it lies in the image of `ι`.

Formalized by `StatMech.FK.ocd_IsInnerVert`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-is-inner-vert).

## Image of an inner-graph edge in the outer graph

The image in `G_out` of an edge of `G_in` under `ι`.

Formalized by `StatMech.FK.ocd_innerEdge`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-edge).

## Injectivity of the edge map

The edge map `Sym2.map ι` is injective when `ι` is.

Formalized by `StatMech.FK.ocd_innerEdge_injective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-edge-injective).

## Edge map sends $\{x, y\}$ to $\{\iota x, \iota y\}$

The image of the edge `{x, y}` is `{ι x, ι y}`.

Formalized by `StatMech.FK.ocd_innerEdge_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-edge-mk).

## Adjacency matching of the inner embedding

The map `ι` matches adjacency: `x ~ y` in `G_in` iff `ι x ~ ι y` in `G_out`.

Formalized by `StatMech.FK.ocd_AdjMatch`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-adj-match).

## Gluing of inner and outer configurations

The configuration on `G_out` that equals the inner configuration `ω` on inner edges and the
outer configuration `ψ` elsewhere.

Formalized by `StatMech.FK.ocd_psiExt`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-ext).

## Restriction of an outer configuration to inner edges

The restriction of a configuration on `G_out` to the edges of `G_in`, read through `ι`.

Formalized by `StatMech.FK.ocd_innerRestrict`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-restrict).

## Finite set of inner edges

The finite set of inner edges of `G_out`.

Formalized by `StatMech.FK.ocd_innerEdgeFinset`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-edge-finset).

## Inner edge set is the range of the edge map

Membership in the inner edge set is membership in the image of the edge map.

Formalized by `StatMech.FK.ocd_mem_innerEdgeFinset`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-mem-inner-edge-finset).

## Glued configuration takes the inner value on inner edges

The glued configuration takes the inner value on inner edges.

Formalized by `StatMech.FK.ocd_psiExt_innerEdge`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-ext-inner-edge).

## Glued configuration equals the outer one at each non-inner edge

The glued configuration takes the outer value off the inner edges.

Formalized by `StatMech.FK.ocd_psiExt_eq_psi_of_not_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-ext-eq-psi-of-not-range).

## Glued value on $\{\iota x, \iota y\}$ is the inner value on $\{x, y\}$

The glued configuration on `{ι x, ι y}` is the inner value on `{x, y}`.

Formalized by `StatMech.FK.ocd_psiExt_innerEdge_pair`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-ext-inner-edge-pair).

## Restricting a glued configuration recovers the inner one

Restricting a glued configuration recovers the inner configuration.

Formalized by `StatMech.FK.ocd_innerRestrict_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-restrict-psi-ext).

## Glued configuration agrees with the outer one off the inner edge set

A glued configuration agrees with the outer configuration off the inner edges.

Formalized by `StatMech.FK.ocd_agreesOff_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-agrees-off-psi-ext).

## Agreeing configuration is the gluing of its own restriction

A configuration that agrees with `ψ` off the inner edges is the gluing of `ψ` with its own
restriction.

Formalized by `StatMech.FK.ocd_psiExt_innerRestrict_of_agreesOff`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-ext-inner-restrict-of-agrees-off).

## Conditioning fibre is the set of gluings

The configurations agreeing with `ψ` off the inner edges are exactly the gluings of `ψ` with
inner configurations.

Formalized by `StatMech.FK.ocd_condFibre_eq_image_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-cond-fibre-eq-image-psi-ext).

## Graph of open non-inner edges

The graph of `ψ`-open edges of `G_out` that are not inner edges.

Formalized by `StatMech.FK.ocd_outsideOpenGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-open-graph).

## Outside graph with the wired boundary clique

The outside graph: `ψ`-open non-inner edges together with the clique on the wired boundary
`∂_out`.

Formalized by `StatMech.FK.ocd_outsideGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-graph).

## Outside-graph adjacency: open non-inner edge or boundary pair

Adjacency in the outside graph.

Formalized by `StatMech.FK.ocd_outsideGraph_adj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-graph-adj).

## Wiring induced on the inner graph

The wiring induced on `G_in` by `ψ`: distinct inner vertices are adjacent when their images
are joined in the outside graph.

Formalized by `StatMech.FK.ocd_inducedWiring`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-induced-wiring).

## Induced-wiring adjacency: distinct and joined in the outside graph

Adjacency in the induced wiring.

Formalized by `StatMech.FK.ocd_inducedWiring_adj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-induced-wiring-adj).

## Image of the inner open subgraph in the outer graph

The image in `G_out` of the open subgraph of an inner configuration `ω`.

Formalized by `StatMech.FK.ocd_innerImageGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-image-graph).

## Inner cluster graph with the induced wiring

The inner cluster graph: open edges of `ω` together with the induced wiring.

Formalized by `StatMech.FK.ocd_innerGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-graph).

## Cluster graph of a glued configuration

The cluster graph of the glued configuration on `G_out` with the wired boundary clique.

Formalized by `StatMech.FK.ocd_fullGraph`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-graph).

## Outside graph is a subgraph of the full cluster graph

The outside graph is a subgraph of the full cluster graph.

Formalized by `StatMech.FK.ocd_outsideGraph_le_fullGraph`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-graph-le-full-graph).

## Glued configuration on inner edges ignores the outer configuration

On inner edges the glued configuration does not depend on the outer configuration.

Formalized by `StatMech.FK.ocd_psiExt_eq_false_of_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-ext-eq-false-of-range).

## Full cluster graph as the union of inner image and outside graphs

The full cluster graph is the union of the inner image graph and the outside graph.

Formalized by `StatMech.FK.ocd_psiWiredGraph_eq_sup`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-wired-graph-eq-sup).

## Endpoints of inner image edges are inner vertices

Both endpoints of an inner image edge are inner vertices.

Formalized by `StatMech.FK.ocd_innerImageGraph_adj_inner`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-image-graph-adj-inner).

## Inner image graph on embedded vertices is the open subgraph

The inner image graph on images of `ι` is the open subgraph of `ω`.

Formalized by `StatMech.FK.ocd_innerImageGraph_adj_ιV`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-image-graph-adj-v).

## Outside reachability gives inner cluster reachability

Inner vertices whose images are joined in the outside graph are joined in the inner cluster
graph.

Formalized by `StatMech.FK.ocd_innerGraph_reachable_of_outsideReachable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-graph-reachable-of-outside-rea).

## Inner cluster reachability gives full-graph reachability of images

Reachability in the inner cluster graph gives reachability of the images in the full cluster
graph.

Formalized by `StatMech.FK.ocd_fullGraph_reachable_of_innerGraph`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-graph-reachable-of-inner-graph).

## Full-graph reachability of images gives inner cluster reachability

Reachability of images in the full cluster graph gives reachability in the inner cluster
graph.

Formalized by `StatMech.FK.ocd_innerGraph_reachable_of_fullGraph`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-graph-reachable-of-full-graph).

## Full-graph and inner cluster reachability agree on embedded vertices

Images of inner vertices are joined in the full cluster graph iff the vertices are joined in
the inner cluster graph.

Formalized by `StatMech.FK.ocd_fullGraph_reachable_ιV`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-graph-reachable-v).

## Full-graph edges at non-inner vertices are outside-graph edges

A full cluster graph edge at a non-inner vertex is an outside graph edge.

Formalized by `StatMech.FK.ocd_fullGraph_adj_of_outside`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-graph-adj-of-outside).

## Outside-only vertex

A vertex is outside-only if its outside cluster contains no inner vertex.

Formalized by `StatMech.FK.ocd_OutsideOnly`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-only).

## Outside-only vertices are not inner

An outside-only vertex is not inner.

Formalized by `StatMech.FK.ocd_outsideOnly_self_not_inner`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-only-self-not-inner).

## Outside-only property is constant on outside clusters

Being outside-only is constant on outside clusters.

Formalized by `StatMech.FK.ocd_outsideOnly_of_reachable`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-only-of-reachable).

## Full-graph reachability from an outside-only vertex stays outside

From an outside-only vertex, reachability in the full cluster graph stays in the outside
graph.

Formalized by `StatMech.FK.ocd_outsideGraph_reachable_of_fullGraph_outsideOnly`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-graph-reachable-of-full-grap).

## Outside-only property of an outside cluster

The outside-only property of a cluster of the outside graph.

Formalized by `StatMech.FK.ocd_IsOutsideOnly`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-is-outside-only).

## Cluster of a vertex is outside-only iff the vertex is

The cluster of `v` is outside-only iff `v` is.

Formalized by `StatMech.FK.ocd_isOutsideOnly_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-is-outside-only-mk).

## Outside-only clusters

The outside clusters that contain no inner vertex.

Formalized by `StatMech.FK.ocd_OutsideOnlyComp`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-only-comp).

## Cluster map into the clusters of a glued configuration

The map from inner clusters and outside-only clusters to the clusters of the glued
configuration.

Formalized by `StatMech.FK.ocd_fullComponentMap`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-component-map).

## Cluster map sends the inner cluster of $x$ to that of $\iota x$

The cluster map sends the inner cluster of `x` to the full cluster of `ι x`.

Formalized by `StatMech.FK.ocd_fullComponentMap_inl_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-component-map-inl-mk).

## Cluster map sends an outside-only cluster of $v$ to that of $v$

The cluster map sends an outside-only cluster of `v` to the full cluster of `v`.

Formalized by `StatMech.FK.ocd_fullComponentMap_inr_mk`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-component-map-inr-mk).

## Injectivity of the cluster map

The cluster map is injective.

Formalized by `StatMech.FK.ocd_fullComponentMap_injective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-component-map-injective).

## Surjectivity of the cluster map

The cluster map is surjective.

Formalized by `StatMech.FK.ocd_fullComponentMap_surjective`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 604](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L604). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-component-map-surjective).

## Cluster bijection for a glued configuration

The clusters of the glued configuration are in bijection with the inner clusters plus the
outside-only clusters.

Formalized by `StatMech.FK.ocd_fullComponentEquiv`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 625](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L625). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-full-component-equiv).

## Number of outside-only clusters

The number of outside-only clusters of `ψ`.

Formalized by `StatMech.FK.ocd_outsideShift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-outside-shift).

## Glued cluster count is induced-wiring count plus outside-only clusters

The wired cluster count of a glued configuration is the induced-wiring cluster count of the
inner configuration plus the number of outside-only clusters.

Formalized by `StatMech.FK.ocd_numClustersBC_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-num-clusters-bc-psi-ext).

## Edges of the inner graph map onto the inner edges of the outer graph

The image of the edges of `G_in` is the set of inner edges of `G_out`.

Formalized by `StatMech.FK.ocd_innerEdge_image_edgeFinset`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-edge-image-edge-finset).

## Outer Bernoulli edge weight of a configuration

The Bernoulli edge weight of `ψ` on the non-inner edges of `G_out`.

Formalized by `StatMech.FK.ocd_psiEdgeFactor`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-edge-factor).

## Positivity of the outer edge weight

The outer edge weight is positive for `p ∈ (0, 1)`.

Formalized by `StatMech.FK.ocd_psiEdgeFactor_pos`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-edge-factor-pos).

## Factorization of the edge weight of a glued configuration

The edge weight of a glued configuration factors into the inner edge weight and the outer edge
weight.

Formalized by `StatMech.FK.ocd_edgeProduct_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-edge-product-psi-ext).

## Outer factor of the FK weight of a glued configuration

The factor `ψ` contributes to the FK weight of a glued configuration: its outer edge weight
times `q` to the number of outside-only clusters.

Formalized by `StatMech.FK.ocd_psiShift`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 717](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L717). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-shift).

## Positivity of the outer factor

The outer factor is positive for `p ∈ (0, 1)` and `q > 0`.

Formalized by `StatMech.FK.ocd_psiShift_pos`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-psi-shift-pos).

## Factorization of the wired FK weight of a glued configuration

The wired FK weight of a glued configuration is the induced-wiring FK weight of the inner
configuration times the outer factor.

Formalized by `StatMech.FK.ocd_bcWeight_psiExt`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-bc-weight-psi-ext).

## Factorization of the conditioned outer partition function

The partition function of the outer measure conditioned on `ψ` is the induced-wiring partition
function times the outer factor.

Formalized by `StatMech.FK.ocd_inducedBcZ_psi`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 745](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L745). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-induced-bc-z-psi).

## Conditional outer measure is the induced-wiring FK measure

Conditioned on `ψ` off the inner edges, the outer wired measure of a glued configuration is
the induced-wiring FK measure of the inner configuration.

Formalized by `StatMech.FK.ocd_condBcProb_psiExt_eq_bcProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 760](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L760). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-cond-bc-prob-psi-ext-eq-bc-prob).

## Conditional outer probability as an induced-wiring probability

The conditional outer probability of an event is the induced-wiring probability of its
pullback under gluing.

Formalized by `StatMech.FK.ocd_condBcProb_psiExt_sum_eq_inducedBox`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-cond-bc-prob-psi-ext-sum-eq-induced).

## Domination by the inner wired measure under a coarser induced wiring

If the induced wiring is coarser than the clique on `∂_in`, the induced-wiring measure is
dominated by the wired measure on `G_in` (for `q ≥ 1`).

Formalized by `StatMech.FK.ocd_condBcProb_psiExt_dominated`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 809](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L809). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-cond-bc-prob-psi-ext-dominated).

## Free inner measure is dominated by every induced-wiring measure

The free FK measure on `G_in` is dominated by every induced-wiring measure (for `q ≥ 1`).

Formalized by `StatMech.FK.ocd_free_le_inducedBcProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-free-le-induced-bc-prob).

## Free inner measure is dominated by the conditional outer measure

The free FK measure on `G_in` is dominated by the restricted conditional outer measure (for `q
≥ 1`).

Formalized by `StatMech.FK.ocd_free_le_condBcProb_innerRestrict`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 838](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L838). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-free-le-cond-bc-prob-inner-restrict).

## Projection closing every inner edge

The projection of a configuration on `G_out` that closes every inner edge.

Formalized by `StatMech.FK.ocd_outProj`, a definition declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 864](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L864). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-out-proj).

## Projected configuration is closed on inner edges

The projection closes inner edges.

Formalized by `StatMech.FK.ocd_outProj_eq_false_of_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 869](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L869). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-out-proj-eq-false-of-range).

## Projection keeps non-inner edges

The projection keeps non-inner edges.

Formalized by `StatMech.FK.ocd_outProj_eq_of_not_range`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 877](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L877). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-out-proj-eq-of-not-range).

## Idempotence of the inner-edge projection

The projection is idempotent.

Formalized by `StatMech.FK.ocd_outProj_idem`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 884](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L884). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-out-proj-idem).

## Projection fibres are conditioning fibres

The fibre of the projection over a projected configuration is its conditioning fibre.

Formalized by `StatMech.FK.ocd_filter_outProj_eq_condFibre`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 892](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L892). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-filter-out-proj-eq-cond-fibre).

## Outer wired fibre masses sum to one

The outer wired masses of the fibres over projected configurations sum to one.

Formalized by `StatMech.FK.ocd_sum_fibreMass_eq_one`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 912](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L912). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-sum-fibre-mass-eq-one).

## Law of total probability over outside configurations

Law of total probability for the outer wired measure over the configuration off the inner
edges. See also `bcProb_fibre_decompose` in `FKDisjointBoxDomainMarkov` for a general
conditioned edge set.

Formalized by `StatMech.FK.ocd_bcProb_decompose`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 935](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L935). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-bc-prob-decompose).

## Conditional outer wired probability at most the inner wired one, $q \ge 1$

Conditioned on `ψ`, the restricted outer wired probability of an increasing event is at most
its wired probability on `G_in`, if the induced wiring is coarser than the clique on `∂_in`.

Formalized by `StatMech.FK.ocd_condBcProb_innerRestrict_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 980](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L980). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-cond-bc-prob-inner-restrict-le).

## Inner wired domination of the restricted outer wired measure

Domination of the restricted outer wired measure by the inner wired measure on increasing
events, when every induced wiring is coarser than the clique on `∂_in` (for `q ≥ 1`).

Formalized by `StatMech.FK.ocd_wired_inner_dominated_bcProb`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1000](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1000). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-wired-inner-dominated-bc-prob).

## Lattice inclusion matches induced adjacency

The inclusion of a vertex set of `ℤ^d` into a larger one matches the induced hypercubic
adjacency.

Formalized by `StatMech.FK.ocd_latticeAdjMatch`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1041](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1041). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-lattice-adj-match).

## Inner vertex with an outside-graph edge lies on the inner boundary

An inner vertex joined to a non-inner vertex in the outside graph lies on the inner boundary.

Formalized by `StatMech.FK.ocd_bdryIn_of_outsideGraph_adj`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1058](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1058). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-bdry-in-of-outside-graph-adj).

## Lattice induced wirings are coarser than the inner boundary clique

For sub-boxes of `ℤ^d` avoiding the outer boundary, every induced wiring is coarser than the
clique on the inner boundary.

Formalized by `StatMech.FK.ocd_latticeInducedWiring_le`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1089](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1089). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-lattice-induced-wiring-le).

## Inner wired domination for vertex sets of $\mathbb{Z}^d$

For a vertex set of `ℤ^d` inside a larger one and avoiding its wired boundary, the restricted
outer wired FK measure is dominated by the inner wired FK measure on increasing events (for `q
≥ 1`).

Formalized by `StatMech.FK.ocd_latticeWired_inner_dominated`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-lattice-wired-inner-dominated).

## Restriction pulls back all-open events to their images

The pullback of "all edges of `t` are open" under restriction is "all edges of `ι(t)` are
open".

Formalized by `StatMech.FK.ocd_innerRestrict_preimage_multiOpenEvent`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-inner-restrict-preimage-multi-open-e).

## Outer wired all-open probability at most the inner wired one

For a vertex set of `ℤ^d` inside a larger one and avoiding its wired boundary, the outer wired
probability that all edges of `ι(t)` are open is at most the inner wired probability that all
edges of `t` are open (for `q ≥ 1`).

Formalized by `StatMech.FK.ocd_latticeWired_multiMass_dominated`, a lemma declared in [PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean, line 1156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/StatisticalMechanics/RandomCluster/OffCentreDomination.lean#L1156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html#ocd-lattice-wired-multi-mass-dominated).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Domination of an inner wired FK measure by an outer one](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-cluster-model/infinite-volume-random-cluster-measures/domination-of-an-inner-wired-fk-measure-by-an-ou)
